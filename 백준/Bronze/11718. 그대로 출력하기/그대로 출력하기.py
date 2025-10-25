while True:
    try:
        line = input()
        if len(line) > 100:
            #print("100글자를 초과함")
            break
        print(line)
    except:  # EOFError가 없으면 '모든 예외를 무시하고 그냥 지나가게 됨. (권장X)
        break
    # except EOFError: -> 입력이 끝났을 때만 예외 처리. (권장O)