#!/usr/bin/env python3
"""Simple website traffic checker using CountAPI.

This script uses only Python's standard library to retrieve or increment
visit counts for a given key. Embed the same key in your webpage to track
visits and query it from the command line.
"""

import argparse
import json
import urllib.parse
import urllib.request


def fetch_json(url: str) -> dict:
    with urllib.request.urlopen(url, timeout=10) as response:
        return json.loads(response.read().decode())


def get_count(key: str) -> int:
    url = f"https://api.countapi.xyz/get/{urllib.parse.quote(key)}"
    data = fetch_json(url)
    return data.get("value", 0)


def hit(key: str) -> int:
    url = f"https://api.countapi.xyz/hit/{urllib.parse.quote(key)}"
    data = fetch_json(url)
    return data.get("value", 0)


def main() -> None:
    parser = argparse.ArgumentParser(description="Check website traffic using CountAPI")
    parser.add_argument("key", help="Unique key identifying the site, e.g. 'unknownai/visits'")
    parser.add_argument(
        "--increment",
        action="store_true",
        help="Increment the counter before retrieving the count",
    )
    args = parser.parse_args()

    count = hit(args.key) if args.increment else get_count(args.key)
    print(f"Total visits for {args.key}: {count}")


if __name__ == "__main__":
    main()
