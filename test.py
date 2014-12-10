#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest2canopsis.connector import CanopsisTestResult
import unittest


class TestUnitTest2Canopsis(unittest.TestCase):
    def setUp(self):
        self.testresult = CanopsisTestResult('unittest2canopsis', None)
        self.testtuple = ({'foo': 'bar'}, 'msg')

    def tearDown(self):
        del self.testresult

    def test_issuccess(self):
        state, msg = self.testresult.testResult(self.testtuple[0])

        self.assertEqual(state, 0)
        self.assertEqual(msg, 'OK')

    def test_isfailure(self):
        self.testresult.failures.append(self.testtuple)
        state, msg = self.testresult.testResult(self.testtuple[0])

        self.assertEqual(state, 2)
        self.assertEqual(msg, 'msg')

    def test_iserror(self):
        self.testresult.errors.append(self.testtuple)
        state, msg = self.testresult.testResult(self.testtuple[0])

        self.assertEqual(state, 3)
        self.assertEqual(msg, 'msg')


if __name__ == '__main__':
    unittest.main()
