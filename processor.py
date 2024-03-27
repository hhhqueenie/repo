import numpy as np

writer_list = ["4680", "4201", "1678","威廉·莎士比亚","但丁","荷马","列夫·托尔斯泰","乔叟", "狄更斯", "詹姆斯·乔伊斯", "弥尔顿", "维吉尔", "歌德"]

fun_list = ["1678","4201","4680"]

def do(str):
    np.random.seed(hash(str) % 2**32)
    return np.random.choice(fun_list)
