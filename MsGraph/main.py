#!/usr/bin/python3
import asyncio
import configparser
from graph import graph
#
async def main():
    print('python graph tutorial')
    #
    #load settings
    config = configparser.ConfigParser()
    config.read(['config.cfg', 'config.dev.cfg'])
    azure_settings = config['azure']
    #
    await greet_user(graph)
    #
    choice = -1
    #
    while choice != 0:
        print('1 Make a graph call')
        print('2 Exit')
        try:
            choice = int(input())
        except:
            Choice = -1
        if choice == 2:
            print('Goodbye......')
            quit()
        if choice == 1:
            await make_graph_call(graph)
        else:
            print('invalid choice\n')
        


