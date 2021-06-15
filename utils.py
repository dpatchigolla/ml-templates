## Common python utility functions
from threading import Thread
import requests
import json
import logging
import urllib3
from typing import List


# Save a dict as a json
def save_dict(dictionary: dict, file_name: str) -> None:
    with open(file_name, "w") as f:
        json.dump(dictionary, f)


# Load a json as dict
def load_dict(file_name: str) -> dict:
    with open(file_name, "r") as f:
        return json.load(f)


# API utils
class API(object):
    # Disables insecure request warnings
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    @staticmethod
    def get_api_response(api_url: str, query: str) -> dict:
        """
        :param api_url: api url with placeholder for query
        :param query:
        :return: Returns the complete response from the api_url
        """
        return json.loads(requests.get(api_url.format(query), verify=False).content.decode("utf-8"))

    @staticmethod
    def single_api_response(queries: List[str], api: str, results: dict={}) -> dict:
        try:
            assert type(queries) is list
        except AssertionError:
            raise("api_response expects List as input. Please check the input type and re-run")
        for query in queries:
            try:
                results[query] = API.get_api_response(api, query)
            except Exception as e:
                logging.warning(str(e) + " for query {}".format(query))
                results[query] = None
        return results

    @staticmethod
    def threaded_api_response(nthreads: int, query_range: List[str], api: str) -> dict:
        store = {}
        threads = []
        queries_unique = list(set(list(query_range)))
        for i in range(nthreads):
            queries = queries_unique[i::nthreads]
            t = Thread(target=API.single_api_response, args=(queries, api, store))
            threads.append(t)
        [t.start() for t in threads]
        [t.join() for t in threads]
        return store

