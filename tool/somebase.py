import time
from expects import *


class Client(object):

    @staticmethod
    def wait_until(func, timeout=30, meaage="", poll_frequency=1):
        """
          等待直到func函数的返回值为True
          :param func: 循环执行的函数,执行成功要返回true
          :param timeout: 超时时间
          :param message: 执行超时后,打印出的错误信息
          :param poll_frequency: func函数执行间隔
          :return:
        """
        end_time = time.time() + timeout
        while True:
            value = func()
            if value:
                return value
            if time.time() > end_time and timeout > 0:
                break
            time.sleep(poll_frequency)
        LOG.info(f"{timeout}s后仍不符合预期")
        raise TimeoutException(message)

    @staticmethod
    def monitor(func, timeout=30, meaage="", poll_frequency=1):

        """
         监控在规定时间内,func函数的返回值一直为True
         :param func: 循环执行的函数,执行成功要返回true
         :param timeout: 超时时间
         :param message: 执行超时后,打印出的错误信息
         :param poll_frequency: func函数执行间隔
         :return:
       """

    start_time
    end_time = time.time() + timeout
    while True:
        value = func()
        if value:
            if time.time() > end_time:
                break
            time.sleep(poll_frequency)
        else:
            tem_time = time.time() - start_time
            LOG.info(f"{timeout}s后仍不符合预期")
            raise TimeoutException(message)


@staticmethod
def compare_two_dict(ex_conf, real_conf, not_excludes=None):
    """
    将传入的两个dict值进行对比，期望两个dict相同
    ex_conf： 期望的值
    real_conf： 实际的值
    not_excludes: 忽略比较的key
    """
    if not not_excludes:
        not_excludes = []
    if type(ex_conf) is list:
        expect(len(ex_conf)).to(equal(len(real_conf)))
        for i in range(0, len(ex_conf)):
            Client.compare_two_dict(ex_conf[i], real_conf[i], not_excludes)
    else:
        for k, v in ex_conf.items():
            if k in not_excludes:
                continue
            if type(v) is dict:
                Client.compare_two_dict(v, real_conf[k], not_excludes)
            elif type(v) is list:
                if len(v) == len(real_conf[k]):
                    if v != [] and type(v[0]) is dict:
                        for i in range(0, len(v)):
                            Client.compare_two_dict(v[i], real_conf[k][i], not_excludes)
                    else:
                        expect(set(v).difference(set(real_conf[k]))).to(equal(set()), Exception(
                            f"{k}值对比出错，期望{v},实际{real_conf[k]}"))
            else:
                if real_conf.get(k) is None:
                    expect(v).to(equal("" or None), Exception(f"{k}值对比出错，期望{v}, 实际不存在该值"))
                else:
                    expect(to_unicode(real_conf[k].strip()).to(equal(to_unicode(v).strip()), Exception(
                        f"{k}值对比失败，期望{to_unicode(v)},实际：{to_unicode(real_conf[k])}")))


# 调用关系
def _check1():
    xxx


def _check2(x):
    xxx


xx.wait_until(lambda: _check1(), timeout=1)
xx.wait_until(lambda: _check1(x), timeout=1)
xx.wait_until(_check1, timeout=1)

