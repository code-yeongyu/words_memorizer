import random


def save(num_of_solved, num_of_answers, solved_text):
    f = open("시험지.txt", 'w')
    f.write("총 "+str(num_of_solved)+"개의 문제를 푸셨고 그 중 " +
            str(num_of_answers)+"개를 맞았습니다.\n\n")
    f.write(solved_text)
    f.close()


def stop(solved_text, remain_dict):
    for key in remain_dict.keys():
        solved_text = solved_text + key + " no\n"
    return solved_text
    pass  # 남아있는 딕셔너리를 더하고 리턴


letters = {"가렴주구": "세금을 가혹하게 거두어들이고, 무리하게 재물을 빼앗음.",
           "각골난망": "남에게 입은 은혜가 뼈에 새길 만큼 커서 잊히지 아니함.",
           "감언이설": "귀가 솔깃하도록 남의 비위를 맞추거나 이로운 조건을 내세워 꾀는 말.",
           "감탄고토": "달면 삼키고 쓰면 뱉는다는 뜻으로, 자신의 비위에 따라서 사리의 옳고 그름을 판단함을 이르는 말.",
           "갑론을박": "여러 사람이 서로 자신의 주장을 내세우며 상대편의 주장을 반박함."}


def main():
    solved = ""
    num_of_answers = 0
    num_of_solved = 0

    print("누가 만들었을까요? 선린인고 19학번 1-3반 김연규가 만들었습니다 ㅎㅎ")
    print("문제를 푸시다가 잘 모르겠다면 0, 그만 풀고 내가 맞춘 문제 목록을 저장하려면 1을 눌러주세요.\n\n")
    for i in range(0, len(letters.keys())):
        keys = letters.keys()
        rand_num = random.randrange(0, len(keys))

        print(str(i+1)+"번째 문제: "+letters[list(letters.keys())[rand_num]])
        isFailed = False
        while(True):
            value = input()
            if(value == list(letters.keys())[rand_num]):
                print("정답입니다.\n\n\n")
                print(len(keys))
                if isFailed:
                    solved = solved + list(letters.keys())[rand_num] + " △\n"
                else:
                    solved = solved + list(letters.keys())[rand_num] + " ○\n"
                num_of_answers = num_of_answers + 1
                break
            elif value == str(0):
                solved = solved + list(letters.keys())[rand_num] + " X\n"
                print("문제를 넘기셨습니다. 정답은 "+list(letters.keys())
                      [rand_num]+"였습니다.\n\n\n")
                break
            elif value == str(1):
                solved = stop(solved, letters)
                save(i, num_of_answers, solved)
                print("시험지.txt 파일을 확인해주세요.\n결과가 저장되었습니다.\n\n\n")
                return
            else:
                isFailed = True
                print("틀렸습니다. 다시 시도하세요.")
        del letters[list(letters.keys())[rand_num]]
        num_of_solved = num_of_solved + 1
    save(num_of_solved, num_of_answers, solved)


main()
