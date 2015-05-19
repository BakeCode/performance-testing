#!/usr/bin/env python
from performance_testing.command_line import Tool
import config


def main():
    tool = Tool(config=config.CONFIG, result_directory='result')
    tool.run()

if __name__ == '__main__':
    main()
