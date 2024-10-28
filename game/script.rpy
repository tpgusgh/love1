init python:
    def set_player_name():
        global pn
        pn = renpy.input("당신의 이름을 입력하세요:")

        # 이름이 비어 있을 경우 기본 이름으로 설정
        if pn == "":
            pn = "김주인"

# 게임에서 사용할 캐릭터를 정의합니다.
define u = Character('정유진', color="#ffee00")
define pn = ""


# 캐릭터 이미지


image ujin = "images/charter/ujin.png"




# 문제 이미지

image q1 = "images/question/1.png"


# 배경

image class = "images/background/classroom.jpeg"

# 여기에서부터 게임이 시작합니다.
label start:

    $ set_player_name()
    "주인공 이름이 '[pn]'으로 설정되었습니다."

    scene  class

    show q1 at Transform(xalign=0.5, yalign=0.5)

    pn "(다음 빈칸에 들어가야할껀?)"
    menu:
        "stdio.h":
            hide q1

            show ujin at Transform(xalign=0.2, yalign=0.5)
            u "얘들아 폰내라"
        
        "iostream":
            u "dd"

        "math.h":
            u "dd"

        "string":
            u "dd"

        "algorithm":
            u "dd"



    
    return
