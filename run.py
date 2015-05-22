#!/usr/bin/env python
from performance.routine import Tool, Config
from performance.web import Request


def main():
    config = Config(host='http://www.example.com', requests_per_client=10, clients_count=3)
    config.add_request(Request(url='/'))
    tool = Tool(config=config)
    tool.run()

if __name__ == '__main__':
    main()
