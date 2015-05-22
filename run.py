#!/usr/bin/env python
from performance.routine import Tool, Config
from performance.web import Request
import config


def main():
    tool = Tool(config=config.CONFIG)
    tool.run()

if __name__ == '__main__':
    main()
