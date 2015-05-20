#!/usr/bin/env python
from performance.routine import Tool
import config


def main():
    tool = Tool(config=config.CONFIG)
    tool.run()

if __name__ == '__main__':
    main()
