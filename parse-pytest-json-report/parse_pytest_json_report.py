from itertools import chain
import json
import sys

TYPES_WE_WANT = {"Function", "TestCaseFunction"}


def main(path):
    with open(path) as f:
        data = json.load(f)
    collectors = data["collectors"]
    results = [c["result"] for c in collectors]
    flattened_results = chain(*results)
    tests_we_want = (r for r in flattened_results if r.get("type") in TYPES_WE_WANT)
    for result in tests_we_want:
        print(result["nodeid"])


if __name__ == "__main__":
    main(sys.argv[1])
