#!/usr/bin/env python
# coding:utf-8

__all__ = ["set_runtime", "set_cpu_runtime",
           "set_max_memory", "set_max_cpu", "set_max_cpu0"]

import os
import signal
import resource


def set_runtime(seconds=0):
    '''
    RuntimeError, max runtime of the function in decorators
    '''
    def wrap(func):
        def runtime_exceeded(signum, frame):
            # os.killpg(os.getpid(), signal.SIGKILL)
            raise RuntimeError

        def to_do(*args, **kwargs):
            signal.signal(signal.SIGALRM, runtime_exceeded)
            signal.alarm(seconds)
            res = func(*args, **kwargs)
            signal.alarm(0)
            return res
        return to_do
    return wrap


def set_cpu_runtime(seconds=0):
    '''
    RuntimeError, max soft cpu runtime of the function in decorators
    '''
    def wrap(func):
        def cpu_runtime_exceeded(signum, frame):
            # os.killpg(os.getpid(), signal.SIGKILL)
            raise RuntimeError

        def to_do(*args, **kwargs):
            soft, hard = resource.getrlimit(resource.RLIMIT_CPU)
            resource.setrlimit(resource.RLIMIT_CPU, (int(
                seconds) if int(seconds) > 0 else soft, hard))
            signal.signal(signal.SIGXCPU, cpu_runtime_exceeded)
            return func(*args, **kwargs)
        return to_do
    return wrap


def set_max_memory(size=0):
    '''
    max memory of the function in decorators
    '''
    def wrap(func):
        def to_do(*args, **kwargs):
            soft, hard = resource.getrlimit(resource.RLIMIT_AS)
            resource.setrlimit(resource.RLIMIT_AS, (int(
                size) if int(size) > 0 else soft, hard))
            return func(*args, **kwargs)
        return to_do
    return wrap


def set_max_cpu(nproc=65535):
    '''
    max ncpu of the function in decorators
    '''
    def wrap(func):
        def to_do(*args, **kwargs):
            soft, hard = resource.getrlimit(resource.RLIMIT_NPROC)
            resource.setrlimit(resource.RLIMIT_NPROC, (int(
                nproc) if int(nproc) > 0 else soft, hard))
            return func(*args, **kwargs)
        return to_do
    return wrap


def set_max_cpu0(nproc=65535):
    '''
    max ncpu of the function in main process
    '''
    soft, hard = resource.getrlimit(resource.RLIMIT_NPROC)
    resource.setrlimit(resource.RLIMIT_NPROC, (int(
        nproc) if int(nproc) > 0 else soft, hard))
