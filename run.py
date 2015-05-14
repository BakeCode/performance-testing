#!/usr/bin/env python
from performance_testing.command_line import Tool


def main():
    tool = Tool(config='config.yml', output_directory='result')
    tool.run()

if __name__ == '__main__':
    main()
