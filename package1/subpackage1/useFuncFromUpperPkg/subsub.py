from package1 import p1
from useFuncFromSamePkg import p3_1
from .. import sub


def subsubTest():
    print("subsubTest() @ useFuncFromUpperPkg")
    p1.p_test1()
    p3_1.p_test3()
    sub.sub()
