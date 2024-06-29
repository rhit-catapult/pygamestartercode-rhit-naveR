import play

import play


background1 = play.new_image("corndog.jpg")
airplane = play.new_image("airplane.png", size=20, x=-150, y=150)
sigma = play.new_text('Sigma', font_size=70)





background = []
for k in range(10):
    backgrounds = play.new_image("corndog.jpg")
    backgrounds.go_to(play.random_position())
    background.append(background)


scissors_list = []
def forever_loop():
    airplane.point_towards(play.mouse)
    airplane.move(5)
    for background in backgrounds:
        if airplane.is_touching(background):
            backgrounds.remove(background)
            backgrounds.remove()
    for scissors in scissors_list:
        scissors.point_towards(airplane)
        scissors.move(1)
        if scissors.is_touching(airplane):
            airplane.go_to(-350,-250)

@play.repeat_forever
def forever_loop():
    airplane.point_towards(play.mouse)
    airplane.move(5)






play.start_program()