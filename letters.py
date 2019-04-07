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
           "갑론을박": "여러 사람이 서로 자신의 주장을 내세우며 상대편의 주장을 반박함.",
           "개과천선": "지난날의 잘못이나 허물을 고쳐 올바르고 착하게 됨.",
           "견강부회": "이치에 맞지 않는 말을 억지로 끌어 붙여 자기에게 유리하게 함.",
           "견원지간": "개와 원숭이의 사이라는 뜻으로, 사이가 매우 나쁜 두 관계를 비유적으로 이르는 말.",
           "경거망동": "경솔하여 생각 없이 망령되게 행동함. 또는 그런 행동.",
           "고립무원": "고립되어 구원을 받을 데가 없음.",
           "고진감래": "쓴 것이 다하면 단 것이 온다는 뜻으로, 고생 끝에 즐거움이 옴을 이르는 말",
           "공평무사": "공평하여 사사로움이 없음.",
           "과유불급": "정도를 지나침은 미치지 못함과 같다는 뜻으로, 중용이 중요함을 이르는 말.",
           "구우일모": "아홈 마리의 소 가운데 박힌 하나의 털이란 뜻으로, 매우 많은 것 가운데 극히 적은 수를 이르는 말.",
           "구중심처": "밖으로 잘 드러나지 않는 깊숙지 곳, 구중궁궐",
           "구중궁궐": "겹겹이 문으로 막은 깊은 궁궐이라는 뜻으로, 매우 많은 것 가운데 극히 적은 수를 이르는 말.",
           "근묵자흑": "먹을 가까이하는 사람은 검어진다는 뜻으로, 나쁜 사람과 가까이 지내면 나쁜 버릇에 물들기 쉬움을 비유적으로 이르는 말.",
           "금과옥조": "금이나 옥처럼 귀중히 여겨 꼭 지켜야 할 법칙이나 규정.",
           "기사회생": "거의 죽을 뻔하다가 도로 살아남.",
           "노심초사": "몹시 마음을 쓰며 애를 태움.",
           "능소능대": "모든 일에 두루 능함.",
           "다다익선": "많으면 많을수록 더욱 좋음. 중국 한나라의 장수 한신이 고조와 장수의 역량에 대하여 얘기할 때 고조는 10만 정도의 병사를 지휘할 수 있는 그릇이지만, 자신은 병사의 수가 많을수록 잘 지휘할 수 있다고 한 말에서 유래한다.",
           "단사표음": "대나무로 만든 밥그릇에 담은 밥과 표주박에 든 물이라는 뜻으로, 청빈하고 소박한 생활을 이르는 말.",
           "단표누항": "누항에서 먹는 한 그릇의 밥과 한 바가지의 물이라는 뜻으로, 선비의 청빈한 생활을 이르는 말, 누항단표와 반댓말.",
           "누항": "좁고 지저분하며 더러운 거리, 자기가 사는 거리나 동네를 겸손하게 이르는 말.",
           "당랑거철": "제 역량을 생각하지 않고, 강한 상대나 되지 않을 일에 덤벼드는 무모한 행동거지를 비유적으로 이르는 말. 중국 제나라 장공이 사냥을 나가는데 사마귀가 앞발을 들고 수레바퀴를 멈추려 했다는 데서 유래한다. <<장자>>의 <인간세편>에 나오는 말이다.",
           "답": "물음과는 전혀 상관없는 엉뚱한 대답.",
           "동병상련": "같은 병을 앓는 사람끼리 서로 가엾게 여긴다는 뜻으로, 어려운 처지에 있는 사람끼리 서로 가엾게 여김을 이르는 말. <<오월춘추>>의 합려내전에 나온다.",
           "동분서주": "동쪽으로 뛰고 서쪽으로 뛴다는 뜻으로, 사방으로 이리저리 몹시 바쁘게 돌아다님을 이르는 말.",
           "동상이몽": "같은 자리에 자면서 다른 꿈을 꾼다는 뜻으로, 겉으로는 같이 행동하면서도 속으로는 각각 딴생각을 하고 있음을 이르는 말. 동상각몽과 반댓말.",
           "두문불출": "집에만 있고, 바깥출입을 아니함. 집에서 은거하면서 관직에 나가지 아니하거나 사회의 일을 하지 아니함을 비유적으로 이르는 말.",
           "마이동풍": "동풍이 말의 귀를 스쳐 간다는 뜻으로, 남의 말을 귀담아듣지 아니하고 지나쳐 흘려버림을 이르는 말.",
           "막역지우": "서로 거스름이 없는 친구라는 뜻으로, 허물이 없이 아주 친한 친구를 이르는 말.",
           "만시지탄": "시기에 늦어 기회를 놓쳤음을 안타까워하는 탄식.",
           "망양지탄": "갈림길이 매우 많아 잃어버린 양을 찾을 길이 없음을 탄식한다는 뜻으로, 학문의 길이 여러 갈래여서 한 갈래의 진리도 얻기 어려움을 이르는 말. 큰 바다를 바라보며 하는 한탄이란 뜻으로, 어떤 일에 자기 자신의 힘이 미치지 못할 때에 하는 탄식을 이르는 말.",
           "맥수지탄": "고국의 멸망을 한탄함을 이르는 말. 기자가 은나라가 망한 뒤에도 보리만은 잘 자라는 것을 보고 한탄하였다는 데서 유래한다.",
           "면종복배": "겉으로는 복종하는 체하면서 내심으로 배반함.",
           "명재경각": "거의 죽게 되어 곧 숨이 끊어질 지경에 이름.",
           "목불인견": "눈앞에 벌어진 상황 따위를 눈 뜨고는 차마 볼 수 없음.",
           "반신반의": "얼마쯤 믿으면서도 한편으로는 의심함.",
           "방약무인": "곁에 사람이 없는 것처럼 아무 거리낌 없이 함부로 말하고 행동하는 태도가 있음.",
           "백년하청": "중국의 황허 강이 늘 흐려 맑을 떄가 없다는 뜻으로, 아무리 오랜시일이 지나도 어떤 일이 이루어지기 어려움을 이르는 말.",
           "백중지세": "서로 우열을 가리기 힘든 형세.",
           "난형난제": "누구를 형이라 하고 누구를 아우라 하기 어렵다는 뜻으로, 두 사물이 비슷하여 낫고 못함을 정하기 어려움을 이르는 말.",
           "막상막하": "더 낫고 더 못함의 차이가 거의 없음.",
           "부화뇌동": "줏대 없이 남의 의견에 따라 움직임.",
           "비분강개": "슬프고 분하여 의분이 북받침.",
           "사필귀정": "모든 일은 반드시 바른길로 돌아감.",
           "살신성인": "자기의 몸을 희생하여 인을 이룸.",
           "상전벽해": "뽕나무밭이 변하여 푸른 바다가 된다는 뜻으로, 세상일의 변천이 심함을 비유적으로 이르는 말.",
           "새옹지마": "인생의 길흉화복은 변화가 많아서 예측하기가 어렵다는 말. 옛날에 새옹이 기르던 말이 오랑캐 땅으로 달아나서 노인이 낙심하였는데, 그 후에 달아놨던 말이 준마를 한 필 끌고 와서 그 덕분에 훌륭한 말을 얻게 되었으나 아들이 그 준마를 타다가 떨어져서 다리가 부러졌으므로 노인이 다시 낙심하였는데, 그로 인하여 아들이 전쟁에 끌려 나가지 아니하고 죽음을 면하라 수 있었다는 이야기에서 유래한다.",
           "설상가상": "눈 위에 서리가 덮인다는 뜻으로, 난처한 일이나 불행한 일이 잇따라 일어남을 이르는 말",
           "설왕설래": "서로 변론을 주고받으며 옥신각신함. 또는 말이 오고 감.",
           "소탐대실": "작은 것을 탐하다가 큰 것을 잃음.",
           "속수무책": "손을 묶은 것처럼 어찌할 도리가 없어 꼼짝 못 함.",
           "수원수구": "누구를 원망하고 누구를 탓하겠냐는 뜻으로, 남을 원망하거나 탓할 것이 없음을 이르는 말.",
           "수구초심": "여우가 죽을 때에 머리를 자기가 살던 굴 쪽으로 둔다는 뜻으로, 고향을 그리워하는 마음을 이르는 말.",
           "수수방관": "팔짱을 끼고 보고만 있다는 뜻으로, 간섭하거나 거들지 아니하고 그대로 버려둠을 이르는 말. '내버려 둠', '보고만 있음'으로 순화.",
           "수주대토": "한 가지 일에만 얽매여 발전을 모르는 어리석인 사람을 비유적으로 이르는 말. 중국 송나라의 한 농부가 우연히 나무 그루터기에 토끼가 부딪쳐 죽은 것을 잡은 후, 또 그와 같이 토끼를 잡을까 하여 일도 하지 않고 그루터기만 지키고 있었다는 데서 유래한다.",
           "순망치한": "입술이 없으면 이가 시리다는 뜻으로, 서로 이해관계가 밀접한 사이에 어느 한쪽이 망하면 다른 한쪽도 그 영향을 받아 온전하기 어려움을 이르는 말.",
           "식자우환": "학식이 있는 것이 오히려 근심을 사게 됨.",
           "아전인수": "자기 논에 물 대기라는 뜻으로, 자기에게만 이롭게 되도록 생각하거나 행동함을 이르는 말.",
           "안분지족": "편안한 마음으로 제 분수를 지키며 반족할 줄을 앎.",
           "안빈낙도": "가난한 생활을 하면서도 편안한 마음으로 도를 즐겨 지킴."}


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
    print("시험지.txt를 확인해주세요. 푼 결과가 저장되었습니다.")


main()
