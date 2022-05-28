def main():
    #ランダムに並べられた重複のない整数の配列
    array = [5, 4, 6, 2, 1, 9, 8, 3, 7, 10]
    # ソート実行
    sortedArray = sort(array)
    # 結果出力
    [print(i) for i in sortedArray]

def sort(array):
    # 要素が一つの場合はソートの必要がないので、そのまま返却
    if len(array) == 1:
        return array

    
    # 配列の先頭を基準値とする
    pivot = array[0]

    # ここから記述
    
    def partition(array,start,end):
        flag = False
        pivot_position = 0

        for epoch in range(len(array)):

            for i in range(start,end):
                if array[i] >= pivot:
                    start = i #startの更新
                    break    
                #探索終了indexまでやって基準値以上が見つからない時は探索終了→endがpivot_position(end以下のindexで全てpivot未満の値をとっている)
                if i == end:
                    pivot_position = end
                    flag = True
                    break


            #配列の逆から参照し基準値未満のindexを見つける範囲はendからstartまで
            for i in reversed(range(start+1,end)):
                if array[i] < pivot:
                    end = i
                    #入れ替え
                    array[start],array[end] = array[end],array[start]
                    break
                #探索終了indexまでやって基準値未満が見つからない時は探索終了→startがpivot_position(start以降のindexで全てpivot以上の値をとっている)
                if i == start+1: #最初のループ時、配列の先頭が最小値ならばpivot_positionをstart+1に変更する工夫が必要
                    if start !=0:
                        pivot_position = start
                    else:
                        pivot_position = 1
                        
                    flag = True
                    break

            if flag:
                break        

            if start+1 == end: #indexが交差するようなら終了
                pivot_position = start+1
                break
            else:
                start += 1
        return pivot_position
    
    
    beginning = 0
    ending = len(array)
    
    def quick_sort(array, beginning, ending):
        #pivot_pozisitionの前半部分
        beginning = 0
        ending = len(array)
        pivot_position = partition(array, beginning, ending)
        pivot_position1 = partition(array, beginning, pivot_position)
        pivot_position1_1 = partition(array, beginning, pivot_position1)
        pivot_position1_2 = partition(array,pivot_position1,pivot_position)
        #pivot_pozisitionの後半部分
        pivot_position2 = partition(array,pivot_position,ending)
        pivot_position2_2 = partition(array,pivot_position2,ending)
        pivot_position3_1 = partition(array, pivot_position2,pivot_position2_2)
        return array

    return quick_sort(array, beginning, ending)
    
    
    # ここまで記述

if __name__ == '__main__':
    main()