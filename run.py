#!/usr/bin/env python
from performance.routine import Tool, Config


def main():
    config = Config(host='http://www.google.de', requests_per_client=10, clients_count=3)
    tool = Tool(config=config)
    tool.run()

if __name__ == '__main__':
    main()
