import os
import nose
from panic import ALL_RESOURCES as resources
from helpers.site import TESTS_DIR, NOSE_TESTS_DIR
from helpers.html import to_br


class Walker(object):
    @staticmethod
    def walk(self):
        info = ""
        info += "This is using getsize to see how much every file consumes\n"
        info += "---------------\n"
        from os.path import join, getsize
        zero = len(TESTS_DIR)
        for root, dirs, files in os.walk(TESTS_DIR):
            info += "\n" + root[zero:]
            info += " consumes " + str(sum([getsize(join(root, name)) for name in files]))
            info += " bytes in " + str(len(files)) + " files"

        return to_br(info)


class JsonWalker(Walker):
    def __init__(self):
        pass


class ShellWalker(Walker):
    def __init__(self):
        pass


class NoseWalker(Walker):
    def test_to_json(self, test):
        id = test.id()
        filepath, filename, testinfile = test.address()
        dot = id.rfind('.')
        # old
        # return {'id': id[dot+1:], 'url': '/noses/' + id, 'name': id[dot:]}
        new_id = filepath[len(NOSE_TESTS_DIR) + 1:-3].replace('/', '.') + ":" + testinfile
        return {'id': id[dot + 1:], 'url': '/noses/' + new_id, 'name': id[dot:]}

    def __init__(self):
        print "NOSE_TESTS_DIR: %s" % NOSE_TESTS_DIR
        self.tests = self._collect_tests_from_dir(NOSE_TESTS_DIR)
        self.dict_tests = {t.id(): t for t in self.tests}

    def get_jsons(self):
        return [self.test_to_json(t) for t in self.tests]

    def traverse_recursive(self, suite, found):
        if isinstance(suite, nose.case.Test):
            found.append(suite)
        else:
            for t in suite._tests:
                self.traverse_recursive(t, found)

    def _collect_tests_from_dir(self, dir_to_collect):
        """ Uses nose's collect plugin"""
        # from pprint import pprint
        # APP_ENGINE_TESTS_DIR = "/home/marcial/repos/flask_docker/src_panic_app/panic/tests/noses/test_appengine"
        from nose.config import Config
        conf = Config()
        from nose.loader import TestLoader
        loader = TestLoader()
        from nose.plugins.collect import CollectOnly, TestSuiteFactory, TestSuite
        collect = CollectOnly()
        collect.conf = conf
        collect.prepareTestLoader(loader)

        tests = loader.loadTestsFromDir(dir_to_collect)

        suite = TestSuite()
        suite.addTests(tests)
        # from nose.core import TextTestRunner
        # TextTestRunner().run(suite)

        # ....:for test in suite._tests[0]._tests[0]:
        # ....:     print test.id()
        found = []
        self.traverse_recursive(suite, found)
        return found

    def _get_test(self, name):
        return self.dict_tests[name]


class Collection(object):
    def __init__(self):
        self.jsons = JsonWalker()
        self.noses = NoseWalker()
        self.shells = ShellWalker()

    def get_tests_for_page(self, what):
        tests = []
        for res in resources:
            if res.menu == what or what == 'tests':
                tests.append({'id': res.name, 'url': res.url, 'name': res.name})
        if what == 'nose_tests':
            tests.extend(self.noses.get_jsons())

        return tests

    def get_all_tests(self):
        tests = []
        for res in resources:
            tests.append({'id': res.name, 'url': res.url, 'name': res.name})
        tests.extend(self.noses.get_jsons())

        return tests

    def get_nose_test(self, name):
        return self.noses._get_test(name)

    def html_info(self):
        return "lala"


collection = Collection()
