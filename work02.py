def main():
    # 昇順にソートされた配列
    sorted_array = [1, 2, 3, 5, 12, 7890, 12345]
    # 探索対象の番号
    target_number = 7890
    # 探索実行
    target_index = serch_index(sorted_array, target_number)
    # 結果出力
    print(target_index)

def serch_index(sorted_array, target_number):

    # ここから記述
    
    low = 0                        #探索リストの一番小さい値のindexをlowとする。
    high = len(sorted_array) - 1   #探索リストの一番大きい値のindexをhighとする。
    
    while low <= high:             # 1つの要素に絞り込まれるまでの間繰り返す
        mid = (low + high) // 2    #　　配列の中間の値をmidとする。配列の長さが偶数の時は切り捨て除算をして中間の一個前のindexを取得させる。
        guess = sorted_array[mid]          # 真ん中の要素をguessとする。
        if guess == target_number:          # 探索対象の数値を検出
            return mid
        if guess > target_number:           # 真ん中の要素 > 探索対象の数値の場合
            high = mid - 1
        else:                      # 真ん中の要素 < 探索対象の数値の場合
            low = mid + 1     

    # ここまで記述

    # 探索対象が存在しない場合、-1を返却
    return -1

if __name__ == '__main__':
    main()