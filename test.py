#!/usr/bin/env python
# Copyright 2014 Bastian Bowe
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys
import unittest2 as unittest

def is_jython():
    return sys.platform.lower().startswith('java')

class TestBuildWorks(unittest.TestCase):

    @unittest.skipUnless(is_jython(), "requires jython")
    def test_java_stuff_external_java_library(self):
        from org.joda.time import DateTime
        dt = DateTime(2014, 2, 1, 0, 0)
        self.assertEqual(u"February", dt.monthOfYear().getAsText())

    @unittest.skipUnless(is_jython(), "requires jython")
    def test_java_stuff(self):
        from java.lang import Math
        maxval = Math.max(4, 7)
        self.assertEqual(7, maxval)

    def test_python_stuff(self):
        self.assertEqual(7, max(4, 7))

if __name__ == '__main__':
    unittest.main()
