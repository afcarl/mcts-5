#!/usr/bin/env python
# encoding: utf-8

VERSION = '0.0.1'
APPNAME = 'mcts'

srcdir = '.'
blddir = 'build'

from waflib.Build import BuildContext


def options(opt):
    opt.load('compiler_cxx')
    opt.load('compiler_c')


def configure(conf):
    conf.load('compiler_cxx')
    conf.load('compiler_c')

    if conf.env.CXX_NAME in ["icc", "icpc"]:
        common_flags = "-Wall -std=c++11"
        opt_flags = " -O3 -xHost  -march=native -mtune=native -unroll -fma -g"
    elif conf.env.CXX_NAME in ["clang"]:
        common_flags = "-Wall -std=c++11"
        opt_flags = " -O3 -march=native -g"
    else:
        if int(conf.env['CC_VERSION'][0]+conf.env['CC_VERSION'][1]) < 47:
            common_flags = "-Wall -std=c++0x"
        else:
            common_flags = "-Wall -std=c++11"
        opt_flags = " -O3 -march=native -g"

    all_flags = common_flags + opt_flags
    conf.env['CXXFLAGS'] = conf.env['CXXFLAGS'] + all_flags.split(' ')
    print conf.env['CXXFLAGS']


def build(bld):
    bld.program(features = 'cxx',
              source='src/my_mcts.cpp',
              includes = './include',
              target='my_mcts')