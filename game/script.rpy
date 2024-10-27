# 이 파일에 게임 스크립트를 입력합니다.

# image 문을 사용해 이미지를 정의합니다.
# image eileen happy = "eileen_happy.png"

# 게임에서 사용할 캐릭터를 정의합니다.
define e = Character('아이린', color="#c8ffc8")



# 문제 이미지

image q1 = "images/question/1.png"


# 배경

image class = "images/background/classroom.jpeg"

# 여기에서부터 게임이 시작합니다.
label start:

    scene  class

    show q1 at Transform(xalign=0.5, yalign=0.5)

    'ㅋㅋ' "다음 빈칸에 들어가야할껀?"
    menu:
        "stdio.h":
            e "dd"
        
        "iostream":
            e "dd"

        "math.h":
            e "dd"

        "string":
            e "dd"

        "algorithm":
            e "dd"



    
    return
