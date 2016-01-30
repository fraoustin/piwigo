#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Basic Test Case
"""

import unittest
from piwigo import Piwigo, WsNotExistException, WsErrorException, WsPiwigoException, PiwigoException


class BasicTestCase(unittest.TestCase):
    """
        Class for Basic Test for piwigo
    """
    def setUp(self):
        self.url = "http://aspery.piwigo.com/"
        self.usertest = 'Aoustin'
        self.passwordtest = 'alice'
        self.piwigo = Piwigo(self.url)
        pass

    def test_basic(self):
        self.assertTrue(self.piwigo.pwg.getVersion())
 
    def test_checkUrl(self):
        self.assertRaises(PiwigoException, Piwigo(''))

   
    def test_checkMethod(self):
        self.assertRaises(WsNotExistException, self.piwigo.pwg.methodNotExist)

    def test_postOnly(self):
         self.assertEqual(self.piwigo.pwg.getVersion._getPostOnly(), False)
         self.assertEqual(self.piwigo.pwg.images.addSimple._getPostOnly(), True)

    def test_errorUrl(self):
        pwglocal = Piwigo("http://errorurl.com/")
        self.assertRaises(WsErrorException, pwglocal.pwg.getVersion)

    def test_errorPiwigo(self):
        self.assertRaises(WsPiwigoException, self.piwigo.reflection.getMethodDetails, methodName = "methodNotExist")

    def test_login(self):
        self.piwigo.pwg.session.login(username=self.usertest, password=self.passwordtest)
        self.assertTrue(self.piwigo.pwg.extensions.checkUpdates())
        self.piwigo.pwg.session.logout()
        self.assertRaises(WsPiwigoException, self.piwigo.pwg.extensions.checkUpdates)

    def test_str(self):
        self.assertEqual(str(self.piwigo.pwg.getVersion), 'pwg.getVersion : Returns the Piwigo version.')
 
    def test_getParams(self):
        self.assertFalse(len(self.piwigo.pwg.getVersion.getParams()))
        self.assertTrue(len(self.piwigo.pwg.session.login.getParams()))

    def test_manageBoolean(self):
        self.assertTrue(len(self.piwigo.pwg.categories.getList(fullname=True)))
        self.assertTrue(len(self.piwigo.pwg.categories.getList(fullname=False)))
        self.assertRaises(WsPiwigoException, self.piwigo.pwg.categories.getList, fullname='titi')

if __name__ == '__main__':
    unittest.main()
