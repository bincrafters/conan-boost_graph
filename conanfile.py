#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.67.0@bincrafters/testing")

class BoostGraphConan(base.BoostBaseConan):
    name = "boost_graph"
    url = "https://github.com/bincrafters/conan-boost_graph"
    lib_short_names = ["graph"]
    cycle_group = "boost_level14group"
    b2_requires = [
        "boost_level14group",
    ]


