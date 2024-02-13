#!/bin/usr/python3
""" poultry management console"""
import cmd
import re
import shlex

class PIMSCommand(cmd.Cmd):
    """PIMS console comand"""
    prompt = "PIMS"
