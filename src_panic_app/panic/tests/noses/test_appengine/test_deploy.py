import os
import urllib2
import re
import unittest


import subprocess
from pexpect import spawn, ExceptionPexpect

def cmd_output_as_line(command):
    """
    pexpects command and returns output lines joined in a string
    """
    return "".join(spawn(command, timeout=None))

def cmd_output_as_lines(command):
    """
    pexpects command and returns output as a lines list
    """
    output = []
    try:
        child = spawn(command, timeout=None)                              
        for line in child:                                                  
            output.append(line)
    except ExceptionPexpect:
        output.append("Command '%s' could not be executed properly!" %command)
    return output




class TC(unittest.TestCase):
    def shortDescription(self):
        return self.__name__ + "|"

def write_to_logg(que):
    print que

apps_path = "/root/panic_app/panic/tests/noses/test_appengine/apps/"
appcfg_py = "appcfg.py "

# TODO icomrporar el path apropiado a nose tests

#@unittest.skip("OK")
class GoAppTestCase(TC):
    #@unittest.skip("xq si!")
    def test_01_go_app_does_not_exist(self):
    
        r= urllib2.urlopen("http://go.panic-tests.appspot.com/")
        assert r.read() == 'Hello, Default version!'
    
    
    def test_02_serving_default_app(self):
    
        r= urllib2.urlopen("http://panic-tests.appspot.com/")
        assert r.read() == 'Hello, Default version!'
    
    
    def test_03_upload_go_app(self):
    
        """upoading app: panic-tests, version: go
        We will check only last line of command output:
            ['10:13 PM Application: panic-tests; version: go\r\n',
             '10:13 PM Host: appengine.google.com\r\n',
             '10:13 PM \r\n',
             'Starting update of app: panic-tests, version: go\r\n',
              ...
             '10:13 PM Checking if updated app version is serving.\r\n',
             '10:13 PM Completed update of app: panic-tests, version: go\r\n']"""
        os.chdir(apps_path)
        stdout = cmd_output_as_line(appcfg_py + "update go/")
        must_contain = "PM Completed update of app: panic-tests, version: go"
        write_to_logg("\n\ntest_upload_go_app\n" + stdout)
        assert re.search(must_contain, stdout)
    
    
    def test_04_serving_go_app(self):
    
        r= urllib2.urlopen("http://go.panic-tests.appspot.com/")
        assert r.read() == 'Hello, Panic!'
    
    
    def test_05_delete_go_app(self):
    
        """test_deploy.test_delete_go_app
        mroman@marcial-tools-better:~$ appcfg.py delete_version -A panic-tests -V go
        10:58 PM Host: appengine.google.com
        Deleting version go...
        Success.
        """
        os.chdir(apps_path)
        stdout = cmd_output_as_line(appcfg_py + "delete_version -A panic-tests -V go")
        must_contain_1 = 'Deleting version go...\r\n'
        must_contain_2 = 'Success.\r\n'
        assert re.search(must_contain_1, stdout)
        assert re.search(must_contain_2, stdout)
    
    
    def test_06_not_serving_go_app(self):
    
        r= urllib2.urlopen("http://go.panic-tests.appspot.com/")
        assert r.read() == 'Hello, Default version!'
    
