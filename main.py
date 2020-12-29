import time
from collections import defaultdict
from typing import List
from typing import Tuple
from random import randint

SET_NUM = 10295472


def get_numbers(min: int = 1, max: int = 37) -> List[int]:
    """
    ランダムに番号を7つ取得する
    """
    return [randint(min, max) for _ in range(7)]


def is_correct_numbers(numbers: List[int]) -> bool:
    """
    番号に重複がない正しい数列かチェックする
    """
    s = set(numbers)
    return len(s) == 7


def to_strnum(numbers: List[int]) -> str:
    """
    数値の配列を文字列に変換する
    """
    num = map(str, sorted(numbers))
    num = ' '.join(num)
    return num


def calc_number_counts(set_num: int = SET_NUM) -> defaultdict:
    """
    数列の出現回数を集計する
    """
    print('回数集計中...')
    count_dict = defaultdict(int)
    correct_num_cnt = 0
    while set_num >= correct_num_cnt:
        nums = get_numbers()
        if is_correct_numbers(nums):
            correct_num_cnt += 1
            str_nums = to_strnum(nums)
            #print(str_nums)
            count_dict[str_nums] += 1
        #time.sleep(0.01)

    print('回数集計完了')
    return count_dict


def get_top_numbers(count_dict: defaultdict, top: int = 1) -> List[Tuple[str, int]]:
    """
    出現回数が上位の数列を取得する
    """
    sorted_dict = sorted(count_dict.items(), key=lambda x: x[1], reverse=True)
    return sorted_dict[:top]


def main():
    d = calc_number_counts()
    tops = get_top_numbers(d, top=1)
    print('numbers, count')
    for top in tops:
        print(f'[{top[0]}], [{top[1]}]')

if __name__ == '__main__':
    main()
    