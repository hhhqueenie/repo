import numpy as np

writer_list = ["威廉·莎士比亚","但丁","荷马","列夫·托尔斯泰","乔叟", "狄更斯", "詹姆斯·乔伊斯", "弥尔顿", "维吉尔", "歌德"]

def do(str):
    np.random.seed(hash(str) % 2**32)
    return np.random.choice(writer_list)