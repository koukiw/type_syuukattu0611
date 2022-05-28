for num in range(1, 101):
    string = ''
    
    # ここから記述
    #3か5で割り切れるものの中で両方で割り切れる場合の「FizzBuzz」を先に処理
    if num % 15 == 0: 
        string = 'FizzBuzz' 
        
    elif num % 3 == 0: 
        string = 'Fizz'
        
    elif num % 5 == 0:
        string = 'Buzz'
        
    else:
        string = str(num) #numはint型だから他と合わせるためにstr型に変更する
    # ここまで記述

    print(string)