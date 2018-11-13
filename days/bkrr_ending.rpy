
#    Булки, кефир и рок-н-ролл. Концовка    #

init 3 python:

    bkrr_characters["dr"] = [u"Водитель", "#B3B3B3"]
    bkrr_characters["sta"] = [u"Стася", "#AAF"]

    emotion_to_pose["mii"] = {
        'laugh': 1, 'normal': 1, 'smile': 1, 'surp': 1, 'cry_smile': 1,
    }

    make_sprites_for('mii', 'inside', ['mod:inside', 'mod:<emotion>'])
    make_sprites_for('mii', 'outside', ['mod:outside', 'mod:<emotion>'])
    make_sprites_for('mii', 'outside snow', ['mod:outside', 'mod:snow', 'mod:<emotion>'])

    emotion_to_pose["sta"] = {
        'dontlike': 1, 'normal': 1, 'sad': 1, 'scared': 1, 'smile': 1, 'surp': 1,
    }

    make_sprites_for('sta', 'inside', ['mod:inside', 'mod:<emotion>'])
    make_sprites_for('sta', 'outside', ['mod:outside', 'mod:<emotion>'])

init:

    image bg int_bus_people_day_bkrr = BKRR_IMAGES + "bg/int_bus_people_day.jpg"
    image bg ext_bus_stop_night = BKRR_IMAGES + "bg/ext_bus_stop_night.jpg"
    image bg ext_street_night = BKRR_IMAGES + "bg/ext_street_night.jpg"
    image bg int_entrance_day = bkrr_fast_livecomposite(BKRR_IMAGES + "misc/int_entrance_day_outside.png", "snow", BKRR_IMAGES + "bg/int_entrance_day.png")
    image bg int_entrance_day_with_cat = bkrr_fast_livecomposite(BKRR_IMAGES + "misc/int_entrance_day_outside.png", "snow", BKRR_IMAGES + "bg/int_entrance_day.png", BKRR_IMAGES + "misc/int_entrance_day_cat.png")
    image bg int_school_night:
        contains:
            BKRR_IMAGES + "bg/int_school_ext.jpg"
        contains:
            "snow"
            zoom 0.7
            alpha 0.4
        contains:
            BKRR_IMAGES + "bg/int_school_night.png"

    image bg int_classroom_night:
        contains:
            BKRR_IMAGES + "bg/int_classroom_ext.jpg"
        contains:
            "snow"
            zoom 0.7
            alpha 0.4
        contains:
            BKRR_IMAGES + "bg/int_classroom_night.png"

    # SnowBlossom(img, count=int, border=int, xspeed=tuple, yspeed=tuple, start=int, fast=bool, horizontal=bool)

    python:
        def bkrr_skylight(size, color):
            return BKRR_IMAGES + "effects/particles/svet/skylight%s%s.png" % (color, size)

    image bkrr_epilogue_skylight:
        contains:
            SnowBlossom(bkrr_skylight(1, 1), 5, 50, (15, 30), (-50, -300), fast=True)
        contains:
            SnowBlossom(bkrr_skylight(1, 2), 5, 50, (15, 30), (-50, -300), fast=True)
        contains:
            SnowBlossom(bkrr_skylight(1, 3), 5, 50, (15, 30), (-50, -300), fast=True)
        contains:
            SnowBlossom(bkrr_skylight(1, 4), 5, 50, (15, 30), (-50, -300), fast=True)
        contains:
            SnowBlossom(bkrr_skylight(2, 1), 6, 50, (15, 30), (-50, -300), fast=True)
        contains:
            SnowBlossom(bkrr_skylight(2, 2), 6, 50, (15, 30), (-50, -300), fast=True)
        contains:
            SnowBlossom(bkrr_skylight(2, 3), 6, 50, (15, 30), (-50, -300), fast=True)
        contains:
            SnowBlossom(bkrr_skylight(2, 4), 6, 50, (15, 30), (-50, -300), fast=True)
        contains:
            SnowBlossom(bkrr_skylight(3, 1), 8, 50, (15, 30), (-50, -300), fast=True)
        contains:
            SnowBlossom(bkrr_skylight(3, 2), 8, 50, (15, 30), (-50, -300), fast=True)
        contains:
            SnowBlossom(bkrr_skylight(3, 3), 8, 50, (15, 30), (-50, -300), fast=True)
        contains:
            SnowBlossom(bkrr_skylight(3, 4), 8, 50, (15, 30), (-50, -300), fast=True)

    image bkrr_epilogue_skylight_behind:
        contains:
            SnowBlossom(bkrr_skylight(3, 1), 3, 50, (15, 30), (-50, -300), fast=True)
        contains:
            SnowBlossom(bkrr_skylight(3, 2), 3, 50, (15, 30), (-50, -300), fast=True)
        contains:
            SnowBlossom(bkrr_skylight(3, 3), 3, 50, (15, 30), (-50, -300), fast=True)
        contains:
            SnowBlossom(bkrr_skylight(3, 4), 3, 50, (15, 30), (-50, -300), fast=True)

    transform bkrr_snow_movement(time, start_pos, x_deviation=0.05, pause_time=0.0, fade_time=1.0):
        truecenter
        ypos -0.25 + 1.5 * start_pos  # стартовая позиция в процентах
        xpos 0.5 - x_deviation + 2 * x_deviation * start_pos  # стартовая девиация
        pause pause_time
        block:
            block:
                alpha 1.0
                parallel:
                    linear (time * (1 - start_pos)) ypos 1.1 xpos (0.5 + x_deviation)
                parallel:
                    pause ((time * (1 - start_pos)) - fade_time)
                    linear fade_time alpha 0.0
            block:
                ypos -0.25
                xpos 0.5 - x_deviation
                alpha 1.0
                linear (time * start_pos) ypos (-0.25 + 1.5 * start_pos) xpos (0.5 - x_deviation + 2 * x_deviation * start_pos)
            repeat

    image mii_snow_close = im.Composite((1050, 1080), (0, 0), BKRR_IMAGES + "sprites/close/mii/mii_1_snow.png")
    image epilogue_falling_star = BKRR_IMAGES + "misc/epilogue_falling_star.png"
    image epilogue_falling_star_star:
        BKRR_IMAGES + "misc/epilogue_falling_star_star.png"
        subpixel True
        truecenter
        ease 10.0 rotate 120.0
    image epilogue_falling_star_tail1 = BKRR_IMAGES + "misc/epilogue_falling_star_tail1.png"
    image epilogue_falling_star_tail2 = BKRR_IMAGES + "misc/epilogue_falling_star_tail2.png"

    image bkrr_snow_layer0_img = BKRR_IMAGES + "effects/snow/0.png"
    image bkrr_snow_layer1_img = BKRR_IMAGES + "effects/snow/1.png"
    image bkrr_snow_layer2_img = BKRR_IMAGES + "effects/snow/2.png"
    image bkrr_snow_layer3_img = BKRR_IMAGES + "effects/snow/3.png"

    image bkrr_snow_layer0_anim:
        contains:
            "bkrr_snow_layer0_img"
            bkrr_snow_movement(8, 0.0, -0.05)
        contains:
            "bkrr_snow_layer0_img"
            bkrr_snow_movement(8, 0.25, -0.05)
        contains:
            "bkrr_snow_layer0_img"
            bkrr_snow_movement(8, 0.5, -0.05)
        contains:
            "bkrr_snow_layer0_img"
            bkrr_snow_movement(8, 0.75, -0.05)

    image bkrr_snow_layer1_anim:
        contains:
            "bkrr_snow_layer1_img"
            bkrr_snow_movement(10, 0.0, 0.05, pause_time=0.5)
        contains:
            "bkrr_snow_layer1_img"
            bkrr_snow_movement(10, 0.25, 0.05, pause_time=0.5)
        contains:
            "bkrr_snow_layer1_img"
            bkrr_snow_movement(10, 0.5, 0.05, pause_time=0.5)
        contains:
            "bkrr_snow_layer1_img"
            bkrr_snow_movement(10, 0.75, 0.05, pause_time=0.5)

    image bkrr_snow_layer2_anim:
        contains:
            "bkrr_snow_layer2_img"
            bkrr_snow_movement(15, 0.0, -0.05, pause_time=1.0)
        contains:
            "bkrr_snow_layer2_img"
            bkrr_snow_movement(15, 0.25, -0.05, pause_time=1.0)
        contains:
            "bkrr_snow_layer2_img"
            bkrr_snow_movement(15, 0.5, -0.05, pause_time=1.0)
        contains:
            "bkrr_snow_layer2_img"
            bkrr_snow_movement(15, 0.75, -0.05, pause_time=1.0)

    image bkrr_snow_layer3_anim:
        contains:
            "bkrr_snow_layer3_img"
            bkrr_snow_movement(20, 0.0, 0.07)
        contains:
            "bkrr_snow_layer3_img"
            bkrr_snow_movement(20, 0.25, 0.07)
        contains:
            "bkrr_snow_layer3_img"
            bkrr_snow_movement(20, 0.5, 0.07)
        contains:
            "bkrr_snow_layer3_img"
            bkrr_snow_movement(20, 0.75, 0.07)

    image bkrr_snow_layer0_anim_quick:
        contains:
            "bkrr_snow_layer0_img"
            bkrr_snow_movement(3, 0.0, -0.03)
        contains:
            "bkrr_snow_layer0_img"
            bkrr_snow_movement(3, 0.25, -0.03)
        contains:
            "bkrr_snow_layer0_img"
            bkrr_snow_movement(3, 0.5, -0.03)
        contains:
            "bkrr_snow_layer0_img"
            bkrr_snow_movement(3, 0.75, -0.03)

    image bkrr_snow_layer1_anim_quick:
        contains:
            "bkrr_snow_layer1_img"
            bkrr_snow_movement(4, 0.0, 0.05)
        contains:
            "bkrr_snow_layer1_img"
            bkrr_snow_movement(4, 0.25, 0.05)
        contains:
            "bkrr_snow_layer1_img"
            bkrr_snow_movement(4, 0.5, 0.05)
        contains:
            "bkrr_snow_layer1_img"
            bkrr_snow_movement(4, 0.75, 0.05)

    image bkrr_snow_layer2_anim_quick:
        contains:
            "bkrr_snow_layer2_img"
            bkrr_snow_movement(5, 0.0, -0.05)
        contains:
            "bkrr_snow_layer2_img"
            bkrr_snow_movement(5, 0.25, -0.05)
        contains:
            "bkrr_snow_layer2_img"
            bkrr_snow_movement(5, 0.5, -0.05)
        contains:
            "bkrr_snow_layer2_img"
            bkrr_snow_movement(5, 0.75, -0.05)

    image bkrr_snow_layer3_anim_quick:
        contains:
            "bkrr_snow_layer3_img"
            bkrr_snow_movement(5, 0.0, 0.03)
        contains:
            "bkrr_snow_layer3_img"
            bkrr_snow_movement(5, 0.25, 0.03)
        contains:
            "bkrr_snow_layer3_img"
            bkrr_snow_movement(5, 0.5, 0.03)
        contains:
            "bkrr_snow_layer3_img"
            bkrr_snow_movement(5, 0.75, 0.03)

    image bkrr_traffic_light:
        contains:
            BKRR_IMAGES + "misc/traffic_light/back_green.png"
            alpha 1.0
            pause 14.5
            ease 0.5 alpha 0.0
            pause 10.0
            pause 22.0
            ease 0.5 alpha 1.0
            pause 3.0
            repeat
        contains:
            BKRR_IMAGES + "misc/traffic_light/back_red.png"
            alpha 0.0
            pause 14.5
            ease 0.5 alpha 1.0
            pause 10.0
            pause 22.0
            ease 0.5 alpha 0.0
            pause 3.0
            repeat
        contains:
            BKRR_IMAGES + "misc/traffic_light/sml_green.png"
            alpha 0.0
            pause 25.5
            ease 0.5 alpha 1.0
            pause 19.0
            ease 0.5 alpha 0.0
            pause 5.0
            repeat
        contains:
            BKRR_IMAGES + "misc/traffic_light/sml_red.png"
            alpha 1.0
            pause 25.5
            ease 0.5 alpha 0.0
            pause 19.0
            ease 0.5 alpha 1.0
            pause 5.0
            repeat
        contains:
            BKRR_IMAGES + "misc/traffic_light/big_red.png"
            alpha 0.0
            pause 24.0
            ease 0.5 alpha 1.0
            pause 25.0
            ease 0.5 alpha 0.0
            repeat
        contains:
            BKRR_IMAGES + "misc/traffic_light/big_yellow.png"
            alpha 0.0
            pause 25.0
            pause 22.0
            ease 0.5 alpha 1.0
            pause 2.0
            ease 0.5 alpha 0.0
            repeat
        contains:
            BKRR_IMAGES + "misc/traffic_light/big_green.png"
            alpha 1.0
            pause 20.0
            ease 0.2 alpha 0.0
            pause 0.3
            ease 0.2 alpha 1.0
            pause 0.3
            ease 0.2 alpha 0.0
            pause 0.3
            ease 0.2 alpha 1.0
            pause 0.3
            ease 0.2 alpha 0.0
            pause 0.3
            ease 0.2 alpha 1.0
            pause 0.3
            ease 0.2 alpha 0.0
            pause 0.3
            ease 0.2 alpha 1.0
            pause 0.3
            ease 0.5 alpha 0.0
            pause 25.0
            ease 0.5 alpha 1.0
            repeat


    image cg ep_mi:
        contains:
            BKRR_IMAGES + "cg/ep_mi_background.jpg"
        contains:
            "bkrr_epilogue_skylight_behind"
            truecenter
            alpha 0.7
        contains:
            BKRR_IMAGES + "cg/ep_mi.png"
            subpixel True
            truecenter
            zoom 1.3
            ease 15.0 zoom 1.0
        contains:
            "bkrr_epilogue_skylight"
            truecenter
            alpha 0.7

    image bkrr_ep_ending_bg = BKRR_IMAGES + "cg/epilogue_ending_bg.jpg"
    image bkrr_ep_ending = BKRR_IMAGES + "cg/epilogue_ending.png"

    python:
        for i in range(9):
            renpy.image("cg bkrr_epilogue_{0}".format(i + 1), BKRR_IMAGES + "cg/epilogue_inbus_{0}.jpg".format(i))

        def bkrr_calendar_sheets(day, month, year, tag):
            from datetime import datetime
            weekday = datetime.strptime("{0}/{1}/{2}".format(day, month, year), "%d/%m/%Y")
            months = [u"Январь", u"Февраль", u"Март", u"Апрель", u"Май", u"Июнь", u"Июль", u"Август", u"Сентябрь", u"Октябрь", u"Ноябрь", u"Декабрь"]
            days = [u"Понедельник", u"Вторник", u"Среда", u"Четверг", u"Пятница", u"Суббота", u"Воскресенье"]
            renpy.show("bkrr_calendar_sheet", what=LiveComposite((362, 445), (0, 0), bkrr_ui["img"]["day_no"], (0.2, 0.28), Text(day, style="bkrr_service2", kerning=2.5, size=72, color="#000" if weekday.weekday() < 5 else "#A00"), (0.47, 0.32), Text(year, style="bkrr_service2", kerning=3.0, size=28, color="#000"), (0.47, 0.42), Text(months[int(month[1])-1 if month.startswith("0") else int(month)-1], style="bkrr_service2", bold=False, kerning=1.2, size=24, color="#000"), (0.22, 0.62), Text(days[weekday.weekday()], style="bkrr_service2", bold=False, kerning=1.25, size=28, color="#000" if weekday.weekday() < 5 else "#A00")), tag=tag, at_list=[truecenter])
            renpy.with_statement(dspr)

    # Календарь
    image bkrr_calendar = BKRR_IMAGES + "misc/calendar/calendar.png"
    image bkrr_calendar_dec1 = BKRR_IMAGES + "misc/calendar/december_1.png"
    image bkrr_calendar_dec5 = BKRR_IMAGES + "misc/calendar/december_5.png"
    image bkrr_calendar_dec8 = BKRR_IMAGES + "misc/calendar/december_8.png"
    image bkrr_calendar_dec15 = BKRR_IMAGES + "misc/calendar/december_15.png"
    image bkrr_calendar_jan = BKRR_IMAGES + "misc/calendar/january_12.png"
    image bkrr_calendar_feb = BKRR_IMAGES + "misc/calendar/february_24.png"
    image bkrr_calendar_mar = BKRR_IMAGES + "misc/calendar/march_3.png"
    image bkrr_calendar_apr = BKRR_IMAGES + "misc/calendar/april_13.png"
    image bkrr_calendar_may = BKRR_IMAGES + "misc/calendar/may_30.png"
    image bkrr_calendar_jun = BKRR_IMAGES + "misc/calendar/june_28.png"
    image bkrr_calendar_jul = BKRR_IMAGES + "misc/calendar/july_18.png"
    image bkrr_calendar_aug = BKRR_IMAGES + "misc/calendar/august_7.png"
    image bkrr_calendar_sep = BKRR_IMAGES + "misc/calendar/september_4.png"
    image bkrr_calendar_oct = BKRR_IMAGES + "misc/calendar/october_31.png"
    image bkrr_calendar_nov = BKRR_IMAGES + "misc/calendar/november_21.png"

    transform cal_sheet_right:
        truecenter
        parallel:
            ease 2.5 xpos 1.3 rotate -90
        parallel:
            linear 1.5 ypos 1.2
        parallel:
            ease 1.0 alpha 0.0
    transform cal_sheet_left:
        truecenter
        parallel:
            ease 2.5 xpos -0.3 rotate 90
        parallel:
            linear 1.5 ypos 1.2
        parallel:
            ease 1.0 alpha 0.0
    transform cal_sheet_cright:
        truecenter
        parallel:
            ease 2.5 xpos 0.9 rotate -90
        parallel:
            linear 1.5 ypos 1.2
        parallel:
            ease 1.0 alpha 0.0
    transform cal_sheet_cleft:
        truecenter
        parallel:
            ease 2.5 xpos 0.1 rotate 90
        parallel:
            linear 1.5 ypos 1.2
        parallel:
            ease 1.0 alpha 0.0


label bkrr_ep_sheets:
    python:
        for y in range(2012, 2016):
            y = str(y)
            for m in range(1, 13):
                m = str(m)
                if len(m) < 2:
                    m = "0" + m
                for d in range(1, 31):
                    d = str(d)
                    if len(d) < 2:
                        d = "0" + d
                    tag = "bkrr_calendar_sheet{0}{1}{2}".format(d, m, y)
                    try:
                        bkrr_calendar_sheets(d, m, y, tag)
                        renpy.pause(0.05)
                        renpy.hide(tag)
                    except ValueError:
                        pass

label bkrr_epilogue:

    $ bkrr_new_chapter("Эпилог")

    jump bkrr_epilogue_common

label bkrr_epilogue_common:

    $ bkrr_set_time("night")

    scene bg ext_music_club_verandah_night_v2 with fade3

    play ambience ambience_camp_center_night fadein 3

    window show

    "Я ожидал, что мы снова останемся вместе до утра, но Мику сонно попросила меня проводить её домой. А лучше – отнести на ручках."
    "После всего, что было, идея показалось мне отличной…"

    window hide
    scene bg ext_house_of_un_night_bkrr with fade2
    window show

    "Но ненадолго.{w} Дорога была слишком ухабистая, а я был готов уснуть на ходу. Когда мы в очередной раз чуть не упали, Мику согласилась идти пешком.{w} Если не считать пары столкновений с сиреневыми зарослями, мы добрались без приключений."

    window hide

    scene bg ext_house_of_mt_night_without_light with fade2

    window show

    "Усталый и счастливый, я вернулся к нашему с Ольгой домику."
    "Снова и снова я вспоминал тёплое дыхание на своём лице и то чувство, когда сперва пальцы, а потом и ногти Мику, впивались мне в спину…"
    "Перед глазами стояло её лицо с закушенной губой и закрытыми глазами, а в ушах раздавались её сбивчивые стоны, глубокое дыхание и вскрики, где русские слова мешались с японскими…"
    "Если бывает ещё лучше, то я не знаю, как люди могут жить дальше после такого."

    window hide

    stop ambience fadeout 0.5

    play sound sfx_door_squeak_light

    scene bg int_house_of_mt_night2 with dissolve

    window show

    play ambience ambience_int_cabin_night fadein 2.5

    "Вожатая явно не ожидала, что я приду ночевать. Она свалила всю одежду из шкафа на свою кровать, а сама устроилась спать на моём месте."
    th "Великолепно. А мне куда? Обратно в клуб? Или спать на травке под окном?"

    "Можно растолкать соседку по дому, и объяснять, где я был.{w} Но она рассердится, что не дал поспать."
    "А можно тихо скользнуть к ней под одеяло и…{w} спать, просто спать. Но тогда рассердится Мику."
    "Оставалось одно."

    window hide

    play sound sfx_blanket_off_stand fadein 1

    $ renpy.pause(1.5, hard=True)

    window show

    "Я расстелил на полу одеяло, переложил на него одежду с кровати, а сам устроился в кровати вожатой, стараясь не обращать внимание на запахи духов и шампуня, идущие от постели."

    window hide

    stop ambience fadeout 2
    show blink

    $ renpy.pause(2.0, hard=True)

    window show

    "Едва коснувшись подушки, я моментально выключился."

    window hide

    $ bkrr_timeskip()
    $ bkrr_set_time("sunset")
    scene black
    window show

    "Кажется, мне снилось что-то приятное. {w}Во всяком случае, очень не хотелось открывать глаза, когда меня принялись трясти за плечо."

    play ambience ambience_int_cabin_day fadein 2.5

    with vpunch
    mt "Эй, вставай!"

    window hide
    scene bg int_house_of_mt_sunset
    show mt surprise nightdress at center
    show unblink
    with None
    play music music_list["she_is_kind"] fadein 10
    $ renpy.pause(1.0, hard=True)
    window show

    me "Оля… В смысле, Ольга Дмитриевна. Доброе утро…"
    "Я потряс головой и огляделся."
    me "А почему я в вашей постели? Мы… Не… Мы ведь не?"

    show mt sad nightdress at center with dspr

    "Ольга внимательно осмотрела меня с ног до головы и сокрушённо вздохнула."
    mt "Семён… Ты исчезаешь неизвестно куда, появляешься за полночь с наглой, довольной рожей, перепачканной в помаде…"
    "Я машинально потянулся за полотенцем и провел по лицу. На нём остались светло-розовые пятна."
    th "Мику… Милая, она так хотела выглядеть ещё красивее. Как будто это вообще возможно."
    "Вожатая даже поперхнулась от такой наглости, отняла полотенце и, размахивая им, словно флагом, продолжила:"

    show mt angry nightdress at center with dspr

    mt "…лезешь в мою кровать, пачкаешь помадой моё любимое домашнее полотенце. И потом задаёшь мне такие вопросы."
    mt "Ну должен же быть какой-то предел, а?"
    me "Я больше не буду."

    window hide

    show mt angry nightdress at center with dspr

    play sound sfx_blanket_off_stand fadein 0.8 fadeout 0.2

    scene black with Dissolve(0.15)

    window show

    "Маска строгой вожатой слетела, когда Ольга бросила полотенце мне на голову и похлопала по макушке."

    mt "Конечно не будешь. Не успеешь! Ещё несколько часов, и я расцелую автобус на котором вы уедете."
    mt "Такой хлопотной смены у меня не было с…{w} хм. Вообще не было. Ни разу!"
    mt "Ну, чего молчишь? Скажи что-нибудь!"
    me "Изви…"

    scene bg int_house_of_mt_sunset
    show mt normal nightdress at center
    with Dissolve(0.12)

    "Я стянул полотенце, зевнул так, что чуть не вывихнул челюсть."
    me "…ните. Спать хочу, сил нет."

    show mt smile nightdress at center with dspr

    mt "Намёк поняла. Кофе налить, Ромео?"
    me "А есть?"

    show mt grin nightdress at center with dspr

    mt "Конечно, нет. Я так предложила, шутки ради. {w}Так будешь или нет?"
    me "Буду!"

    window hide

    hide mt with dissolve

    $ renpy.pause(1.0, hard=True)

    window show

    "Пока кофе остывал, Ольга перебирала какие-то бумаги лежащие на столе."

    show mt normal nightdress at center with dissolve

    mt "Хорошо, что всё позади. Жалко, что вас не было, когда мы прощались с иностранцами.{w} Да и комиссия хотела напоследок поблагодарить вас за отличное выступление."
    me "Правда?"

    show mt grin nightdress at center with dspr

    mt "Правда-правда. Но я сказала, что вы репетировали всю ночь, очень устали и легли спать пораньше."
    "Она подмигнула мне."
    mt "В целом где-то так и было, да?"

    hide mt with dissolve

    "Я смутился и отошел к двери. Там вовсю светило солнце, а по дорожкам сновали пионеры.{w} Они были отвратительно бодрые и полны энергии. Стало завидно."
    "Но я вспомнил, куда ушли мои силы… И не мог не улыбнуться."
    "Доза кофеина тёплой волной разошлась по моему телу и помогла разлепить веки."

    window hide

    $ renpy.pause(1.0, hard=True)

    stop music fadeout 5

    stop ambience fadeout 3

    $ bkrr_timeskip()
    $ bkrr_set_time()

    scene bg ext_square_day with bkrr_circleout_transition

    play ambience ambience_camp_center_day fadein 3

    $ renpy.pause(1.0, hard=True)

    window show

    "Этим утром всеми овладело чемоданное настроение. Праздник пролетел быстро, как будто и не было ничего.{w} Только флажки с гирляндами напоминали о том, что ещё вчера здесь были иностранные гости, играла музыка и четверо пионеров захватывали сцену… Чтобы вскоре её покинуть."
    "Стоил ли весь этот цирк таких усилий?{w} Я вспомнил улыбки девчонок на концерте. Наверное, стоил."
    "После завтрака Ольга Дмитриевна в последний раз собрала нас на линейку и принялась раздавать ценные руководящие указания."

    window hide

    scene cg d2_lineup with dissolve

    play music music_list["my_daily_life"] fadein 10

    window show

    mt "Отряд! Слушай мою команду. Сегодня до одиннадцати ноль-ноль необходимо привести в порядок жилые помещения."
    mt "И когда я говорю «навести порядок», я имею в виду именно «навести порядок».{w} Это не значит замести грязь под коврик и с честным лицом прийти ко мне с ключами. Вопросы есть?"
    dv "А нам нечем убирать! Веники пали смертью храбрых на растопке вчерашнего костра!"
    us "Да. Так что убирать будет следующая смена."
    mt "Я ждала чего-то подобного. Но всё учтено, у нас есть запасы! Славяна, раздай орудия труда. На всех хватит?"
    sl "Да, Ольга Дмитриевна. Всем по одному, плюс две штуки – оперативный резерв."
    mt "Вольно, солдат! В смысле… Отличная работа, пионеры!{w} Итак… Времени мало, а грязи много, так что работаем быстро. Иначе я раздам следующей смене ваши домашние адреса, и мы вышлем на них весь оставшийся мусор. Поняли?"
    all "Понятно…"
    mt "Кроме того… Семён, Мику, на вас музклуб. Алиса с Ульяной, как закончат, присоединятся к вам."
    mt "Саша, Сергей, наведёте порядок в мастерской. Непонятную постройку с падающим бочонком – ликвидировать, мне трупы пионеров не нужны."
    mt "Женя – в библиотеку…"
    mz "Ещё вчера навела порядок."
    mt "Очень хорошо. Что ещё…"
    mt "Автобус отбывает в полдень. Свои вещи сложить в сумки, всё проверить, лагерное имущество на память не увозить. Постельное бельё свернуть и оставить на кроватях."
    mt "Если в домиках остаются казённые чашки-ложки, выложите их на видное место, мы с Натальей потом соберём."
    mt "Дополнительная мотивация для вас: те, кто закончат первыми и без замечаний, смогут выбрать места в автобусе, остальные сядут, где придётся. Опоздавшие отправятся пешком! {w}Вопросы есть? {w}Вопросов нет."

    window hide

    scene bg ext_square_day with dissolve

    play sound bkrr_sfx_list["whistle"]

    window show

    "Она энергично дунула в свисток и захлопала в ладоши."

    show mt grin panama pioneer at center with dissolve

    mt "Побежали-побежали-побежали!!! Время пошло!"
    "Неровная шеренга пионеров быстро рассосалась по домикам."

    show mt smile panama pioneer at center with dspr

    "Ольга повернулась ко мне и уже нормальным тоном добавила:"
    mt "Как в старые добрые времена… Нет, ну какой командир пропадает."
    me "Да, ничего так. Я побежал?"

    show mt normal panama pioneer at center with dspr

    mt "А вас, товарищ нездешний, попрошу остаться. Серьёзные вещи обсуждать будем."
    me "А музклуб?"
    mt "Семён, Мику никуда не денется. А вот с тобой надо что-то делать. Сначала вещи."
    me "Какие вещи?"
    mt "Твои. Пошли в дом."

    window hide

    scene bg black with dissolve

    stop ambience fadeout 2

    $ renpy.pause(1.0, hard=True)

    play sound sfx_open_door_1

    scene bg int_house_of_mt_day with dissolve

    window show

    play ambience ambience_int_cabin_day fadein 2.5

    "Мы зашли в домик."

    show mt smile panama pioneer at center with dissolve

    mt "Ты ведь приехал без вещей, да?"
    me "Как будто вы не знаете."

    show mt grin panama pioneer at center with dspr

    mt "Всякое бывает. Может, спрятал где-нибудь. Был здесь один неместный. Называл себя «выживальщик»."
    mt "Не знаю, что это такое, но он вместо того, чтобы зайти в лагерь через ворота, как все нормальные люди, украл одежду из склада, зарыл свои вещи под забором, переоделся и постарался смешаться с отрядом."
    me "Удачно?"

    show mt smile panama pioneer at center with dspr

    mt "Почти. Два дня я не могла понять, куда девается лишняя порция в столовой. И ведь смешался бы, но его сгубило любопытство.{w} Этот самый проныра влез в админкорпус и гвоздём открыл директорский сейф. Документы, наверное искал…"
    mt "А там у электрика лежали бутылка «посольской» водки и блок сигарет, так что всё было под сигнализацией. Она сработала, взломщик убежал в лес, вывихнув плечо чтобы пролезть в узкую форточку, и неделю прятался в старом лагере, поедая ящериц и птичьи яйца."
    mt "Очень сложный случай. К счастью, мы вовремя его нашли."

    me "Бывает же. Нет, у меня из багажа только моя одежда."

    show mt normal panama pioneer at center with dspr

    mt "Это ты так думаешь."

    stop music fadeout 10

    "Ольга бросила на кровать тёмную спортивную сумку, расстегнула молнию. Внутри лежала какая-то одежда."
    mt "Вот. Это тебе на первое время. Не ходить же тебе в зимнем пальто, правда?"
    me "Прощальный подарок от лагеря?"

    show mt sad panama pioneer at center with dspr

    "Вожатая серьёзно посмотрела на меня, огляделась по сторонам, потом рассмеялась и покачала головой."

    show mt grin panama pioneer at center with dspr

    mt "Ещё чего. Это прощальный подарок от меня. Когда машина ездила в город, я попросила подругу купить кое-что. Одни убытки от тебя!"
    "Она улыбнулась."
    me "Простите… Много потратили?"
    mt "Рублей семьдесят. Не волнуйся, не обеднею. В лагере деньги тратить некуда, а там следующую зарплату получу."
    me "Спасибо…"

    show mt normal panama pioneer at center with dspr

    mt "На здоровье. Вещи бы всё равно появились. Здесь всё устраивается. Так или иначе…{w} Хотя «иначе» бывает по-всякому, лучше решим всё сами."

    window hide

    play music music_list["reminiscences"] fadein 10

    $ renpy.pause(0.5, hard=True)

    window show

    "Я задал вопрос, который не давал мне покоя всю последнюю неделю."

    me "Ольга Дмитриевна… А что дальше?"
    mt "В смысле? Дальше паковать вещи и убирать музклуб."
    me "Дальше.{w} Куда я приеду? И что мне там делать?"

    show mt sad panama pioneer at center with dspr

    mt "Понятия не имею."
    me "Я думал, вы знаете всё и про всех."
    mt "Упаси боже. Но во сне ты не исчез, и остальные могут тебя видеть. Значит, ещё ничего не кончилось. Так что вот тебе подъёмные."
    "Она протянула мне фиолетовую бумажку с профилем Ленина."

    show mt normal panama pioneer at center with dspr

    mt "Двадцать пять рублей хватит, чтобы жить пару недель.{w} А вот это – мой адрес…"
    "Вожатая быстро написала что-то на листке."

    show mt smile panama pioneer at center with dspr

    mt "Если на стоянке к тебе не бросятся незнакомые люди, крича «Сынуля, ты приехал!!!» и родители Мику не пригласят тебя пожить у них, то поедешь в этот адрес. {w}Поживёшь в моей квартире, а потом, когда я приеду, мы что-нибудь придумаем."
    mt "Ночевать на вокзале не рекомендую, а в гостиницу тебя, сам понимаешь, не поселят. Мал ещё."
    mt "Можешь, конечно, разбить стекло в магазине и уютно переночевать в милиции, но я советую мой вариант.{w} Ключи возьмёшь у моей соседки, её зовут Вера Семёновна."
    me "И что я ей скажу?"

    show mt laugh panama pioneer at center with dspr

    mt "Что ты мой любовник, очевидно же."
    me "Что???"

    show mt grin panama pioneer at center with dspr

    mt "Надо же, как покраснел. Скажешь, что мой племянник из… {w}Не знаю. Из глуши какой-нибудь.{w} Например, из Саратова."
    me "Приходит незнакомый парень без документов и просит ключи от соседской квартиры. Я бы милицию вызвал."

    show mt normal panama pioneer at center with dspr

    mt "Правильно рассуждаешь. Поэтому вот тебе и свидетельство о рождении."

    window hide
    $ bkrr_get_item("birth_certificate")
    window show

    "Она протянула мне зелёную книжечку с гербом СССР. Я тут же уставился в неё и скривился, увидев фамилию.{w} Если этот лагерь и разумный, то чувство юмора у него отвратительное."
    me "Но… Откуда оно?"
    mt "Из ящика стола. Нашла примерно в день твоего приезда. Откуда-то взялось."
    me "… Вот так? Из воздуха?"

    show mt smile panama pioneer at center with dspr

    mt "Я конечно не уверена, но думаю, что его подбросила Юля."
    me "Почему именно Юля?"
    mt "Элементарно, Ватсон. Отпечатки босых ног на подоконнике – это раз. Пропажа валерьянки из аптечки – это два. Кто же ещё?"

    hide mt with dissolve

    "Я снова перечитал фамилию, втайне надеясь что она изменилась…{w} Шутка вполне в духе моего двойника. Если бы я захотел подшутить на прощение, то сочинил бы что-то в этом духе."
    "Потёртые «корочки» свидетельства обещали новую жизнь… {w}И внушали странное ощущение спокойствия."
    "Как будто кто-то подошёл и пообещал: «Ты останешься с Мику. Не волнуйся!»."
    th "Наверное, я бюрократ в душе."
    me "Ещё бы фамилию другую… Вам смешно, а мне всю жизнь с ней мучиться."

    show mt smile panama pioneer at center with dissolve

    mt "Слушай, ты долго носом будешь вертеть? Лопай, что дают! Женишься на Мику, возьмёшь её фамилию. Вот тебе лишний стимул за неё держаться."
    th "Как будто мне нужны какие-то стимулы."
    th "Кстати, я так и не узнал, какая же у неё фамилия. Если папина, то еще ладно, но если мамина… Наверняка что-нибудь заковыристое и японское."
    me "Ладно, давайте убираться?"
    mt "Ещё чего. У меня здесь, знаешь ли, кое-какие вещицы, которые тебе видеть не положено! Так что принеси ведро воды и можешь идти в музклуб."
    th "Где-то я это уже слышал… Ведро воды здесь стандартная валюта?"

    window hide

    hide mt with dissolve

    stop music fadeout 10

    $ bkrr_timeskip_short()

    scene bg int_house_of_mt_day with bkrr_timeskip_transition()

    window show

    "Сбегав за водой, я быстро просмотрел купленные Ольгой вещи. Джинсы, рубашка, кеды…"
    me "Если я в поездку надену джинсы, мне не пришьют аморальное поведение и урон облику советского пионера?"

    show mt normal pioneer close at center with dissolve

    mt "Нет. Что за глупые идеи. Вот свариться – можешь. А так носи на здоровье."
    me "И с рубашкой… Будет нормально."

    show mt smile pioneer close at center with dspr

    mt "Нет, вы посмотрите на этого жмота. Четыре недели я кормлю его, пою и воспитываю, купила полный чемодан одежды, а он испортил две рубашки и пытается украсть третью."
    me "Ладно, ладно…"
    mt "Я шучу. Не выделяйся, пока не сойдёшь с автобуса. Дальше справляйся, как знаешь, а до отъезда из лагеря я за тобой присмотрю."
    me "Спасибо."
    mt "На здоровье. Ну, беги быстрее, времени мало."
    "Сейчас её глаза смотрели по-матерински тепло."
    "На секунду мне показалось, что она куда старше, чем хочет казаться. Но через секунду иллюзия исчезла."
    mt "Знаешь, за что я обожаю эту часть смены?"
    me "За что?"

    show mt grin pioneer close at center with dspr

    mt "За то, что завтра вас всех здесь не будет!"
    me "Цинично-то как звучит… Я вот как чувствовал, что вы только притворяетесь хорошей."
    "Ольга протянула руку и взъерошила мне волосы."

    show mt smile pioneer close at center with dspr

    mt "Ага! Наконец-то раскусил. Всё, пошёл-пошёл-пошёл!"

    window hide

    hide mt with dissolve

    stop ambience fadeout 0.5

    scene bg ext_house_of_mt_day with dissolve

    play ambience ambience_camp_center_day fadein 3

    $ renpy.pause(1.0, hard=True)

    play sound sfx_close_door_1

    window show

    "Она энергично хлопнула в ладоши и вытолкала меня из домика."

    window hide

    stop ambience fadeout 0.5

    scene bg ext_music_club_verandah_day_v9 with dissolve

    play ambience ambience_camp_center_day fadein 3

    window show

    "Девчонки уже поджидали меня у клуба, но внутрь не спешили."

    show us smile sport at left
    show dv smile bkrr_sport at center
    show mi smile bkrr_sport at right
    with dissolve

    dv "Ага! Вот он."
    mi "Сеня, ты уже собрался?"
    us "Я же говорила, что вчера был не последний раз!"
    me "Да."

    window hide

    play sound sfx_open_door_2

    scene bg int_music_club_day with dissolve

    play ambience bkrr_ambience_list["indoors_day"] fadein 3
    play music music_list["farewell_to_the_past_edit"] fadein 5

    window show

    "Я шагнул через порог и остановился."
    "Сколько всего случилось…"

    window hide
    python:

        for cg in ["cg d6_sem_guitar", "cg d6_on_floor", "cg d12_noon_rest_1", "cg d7_mi_embrace"]:
            renpy.scene()
            renpy.show("cg", [d4_mttalk_cgs_atl(renpy.random.choice([-7.5, 7.5]))], what=bkrr_make_sepia_img(cg))
            renpy.with_statement(dissolve)
            renpy.pause(0.25, hard=True)

    scene bg int_music_club_day with dissolve
    window show

    "Вчера, разбирая музыку, мы бросали вещи куда придётся, так что теперь предстояло распутать змеиный клубок кабелей, навести здесь подобие порядка, и…"
    me "А где матрасы?"

    show mi normal bkrr_sport at center with dissolve

    mi "Вернулись на вещевой склад, где же ещё. Я хотела найти тех двоих, которые их побросали, но они как сквозь землю провалились. Ни разу их больше не видела."
    me "Мику… А как они выглядели?"

    show mi upset bkrr_sport at center with dspr

    mi "Ну что ты такое спрашиваешь… три недели ведь прошло. М-м-м…"
    "Она нахмурилась, вспоминая."

    show mi serious bkrr_sport at center with dspr

    mi "Один… лохматый такой. На тебя очень похож! Я ещё когда тебя увидела, подумала, что это ты вернулся… В смысле – он вернулся."
    mi "Только у него волосы короче были. И одет по-другому. И рожи постоянно корчил странные."

    show us laugh2 sport at left with easeinleft

    us "Ага-а-а!!! Так это Сенька подстроил! Только не понятно, зачем."

    show mi grin bkrr_sport at center with dspr

    mi "А второй – мелкий, вот как Ульяна…"

    show us dontlike sport at left with dspr

    us "Чего? Ты сейчас на что намекаешь?"

    show mi smile bkrr_sport at center with dspr

    mi "Ни на что. Я ещё подумала сразу, что это девочка, он сам был маленький и голос такой… тонкий. {w}Он ещё лицо всё время прятал, панаму чуть ли не до плеч натянул."
    dv "Точно Улька!"

    show us upset sport at left with dspr

    us "Нет!"

    show mi normal bkrr_sport at center with dspr

    mi "Нет-нет. У того волосы тёмные были… Ульяна, конечно, могла успеть покрасить, а потом обратно, или парик, но нет, не может такого быть, и вообще, она же в другом месте была."

    window hide

    hide mi
    hide us
    with dissolve

    $ renpy.pause(1.0, hard=True)

    window show

    "Я улыбнулся."
    "Вполне в духе Мику – не узнать меня через пять минут после общения с моим двойником. Хотя…{w} Тогда я был для неё одним из толпы. Кто бы мог представить, что всё так сильно изменится…"

    show us normal sport at cright with dissolve

    us "Товарищи музыканты, если кто-то надеется что пол сам себя помоет, то зря! Может, будем начинать? Я не хочу в спортивке домой ехать, мне еще переодеться надо."

    show dv laugh bkrr_sport at cleft with dissolve

    dv "Ой, кого ты обманываешь? Так ведь и поедешь."

    show us calml sport at cright

    us "Не умничай! Я не хочу, чтобы следующая смена спрашивала, что за хрюшки тут занимались!"

    window hide

    show us angry sport:
        cright
        ease 0.17 yoffset 75
        ease 0.25 yoffset 0
    with None

    $ renpy.pause(0.17, hard=True)

    stop music fadeout 1
    play sound sfx_bus_window_hit

    with vpunch

    play sound2 sfx_water_emerge fadein 1.6 fadeout 0.9

    play music music_list["you_lost_me"]

    show dv shocked bkrr_sport at cleft
    show us surp2 sport at cright
    with dspr

    $ renpy.pause(1.0, hard=True)

    hide dv
    hide us
    with dissolve

    window show

    "Ульяна топнула ногой и нечаянно опрокинула ведро с водой. Мыльная пена тут же растеклась по полу."
    dv "{b}…! {w}…!!! {w}…!!!{/b}"
    "Алиса выдала непереводимую игру слов, щедро сдобренную междометиями, и бросилась поднимать с пола нотные тетради, кабели и тапочки."
    "Ульяна тут же бросилась на помощь, а мы с Мику ухватили тряпки и принялись устранять наводнение."

    window hide

    stop music fadeout 10

    $ renpy.pause(1.0, hard=True)

    window show

    "Вскоре на досках пола стало можно лежать, как на палубе парусника после большой флотской уборки."

    show dv smile bkrr_sport far at fleft with easeinleft

    dv "Это был ульянкин секретный приём: неподражаемые руки-крюки!"

    show mi smile bkrr_sport at fright with easeinright

    mi "Тогда уже ноги…"

    show us sad sport close at center with easeinbottom

    us "Я нечаянно! Хватит нудить. Сень, ну скажи ты им."
    me "Смотри с хорошей стороны. Так бы мы до вечера бы собирались."

    show us laugh2 sport close at center with dspr

    us "Вот! Точно!"

    show mi normal bkrr_sport at fright with dspr

    "Мику провела пальцами по роялю, тронула струны стоявшей рядом гитары."
    mi "Может, по чайку? На дорожку?"


    "Чашка в руках Ульяны материализовалась словно из ниоткуда."

    play sound [ bkrr_sfx_list["cup_clank1"], bkrr_sfx_list["cup_clank2"] ]
    show us surp1 sport close at center with dspr

    us "Да-а-а!!!"

    show dv guilty bkrr_sport far at fleft with dspr

    dv "НЕТ! Скоро ехать. Сейчас напьешься чаю, потом автобус будем каждые десять минут останавливать.{w} Приедем, тогда вечером соберемся и сходим куда-нибудь."

    window hide

    stop ambience fadeout 3

    scene bg ext_music_club_verandah_day_v1_ajar:
        subpixel True
        truecenter
        zoom 1.25
        ease 5.0 zoom 1.0
    with fade3

    play ambience ambience_camp_center_day fadein 3

    play music bkrr_music_list["forever_smile"] fadein 5

    $ renpy.pause(3.0, hard=True)

    window show

    "Наконец последняя нотная тетрадь легла на полку, последняя пылинка смахнута тряпкой, шторы задернуты, чтобы яркий солнечный свет не портил лак на инструментах, чашки вымыты, струны на гитарах отпущены, барабаны и рояль зачехлены.{w} Сделана еще куча необязательных мелочей…"
    "Никому не хотелось уходить отсюда… {w}Но время пришло."

    window hide
    $ renpy.pause(1.0, hard=True)
    play sound sfx_close_door_1
    scene bg ext_music_club_verandah_day_v1 with dissolve
    window show

    "Мы вышли из клуба, я аккуратно закрыл дверь и отошёл в сторону."

    show mi normal bkrr_sport far at cleft with dissolve

    "Мику посмотрела на ключ и вздохнула."
    mi "Вот и всё. Как руководитель музыкального клуба, объявляю текущий состав участников распущенным."
    us "Алиса, ты слышала? Она меня распущенной назвала!"
    dv "Тс-с-с!"

    show mi sad_smile bkrr_sport far at cleft with dspr

    mi "Здесь родилась наша группа. Её история была недолгой, но яркой. Мы репетировали, готовились, здесь мы праздновали удачное завершение концерта, и… {w}и…"

    show mi shy bkrr_sport far at cleft with dspr

    "Она смутилась и посмотрела на меня."

    hide mi with dissolve

    "Я знал, о чём она подумала."
    "Здесь мы с Мику нашли друг друга."
    "В этих стенах наша дружба стала симпатией, симпатия – любовью, а потом…"
    "Как называется то чувство, когда понимаешь, что не сможешь жить без своей второй половинки?"
    "Наверняка этому есть название, и мне ещё предстоит его найти."
    "Мику молчала, так что я обнял её и закончил фразу:"
    me "И теперь, когда всё позади, нам всем немножко грустно. Но это не беда."
    me "Что-то закончится, что-то начнётся, и мы обязательно ещё сыграем вместе. Но мне будет не хватать этого клуба… Я очень к нему привязался. И ко всем вам тоже."

    show dv normal bkrr_sport at cleft with dissolve

    dv "Ой, ты как будто прощаешься. Сбежать надумал?"
    me "Не дождётесь!"

    hide dv with dissolve

    th "Во всяком случае, я очень-очень на это надеюсь."

    show mi cry_smile close bkrr_sport at cright with dissolve

    "Мику шмыгнула носом, коснулась уголка глаза и тихо попросила:"
    mi "Девочки, дайте ключи от клуба, пожалуйста."
    "Я достал ключ из кармана, Алиса с Ульяной тоже протянули свои."

    hide mi with dissolve

    "Мику постаралась собрать их на кольцо, но оно было тугим и не поддавалось."
    me "Давай я."

    window hide

    $ renpy.pause(1.0, hard=True)

    window show

    play sound sfx_keys_rattle

    "Немного повозившись, я позвенел получившейся связкой. {w}Мой, Мику, ключ Алисы, ключ Ульяны. Впервые за три недели они собрались вместе."
    th "Как знать, может, им тоже есть, о чём поговорить?"
    me "Совсем как мы вчетвером, да? {w}Есть в этом что-то символичное."
    me "В моём городе есть такая примета: когда парочка встречается, они пишут свои имена на замке, вешают его куда-нибудь, на мост или на забор, а ключ выбрасывают в воду."

    show dv laugh bkrr_sport at cleft
    show mi upset bkrr_sport at cright
    show us smile sport at center
    with dissolve

    dv "Я не поняла, это к чему вообще?"

    show us laugh2 sport at center with dspr

    us "К тому, что мы – его гарем, очевидно же."

    show mi sad_smile bkrr_sport at cright with dspr

    mi "Сеня… я пока не готова к такому. Тебе что, мало меня?"
    "Она старательно изображала обиду, но её глаза светились теплом и… {w}любовью?"

    window hide

    hide dv
    hide mi
    hide us
    with dissolve

    $ renpy.pause(1.0, hard=True)

    window show

    "Ради того, чтобы на тебя смотрели таким взглядом, стоило провалиться в прошлое, сменить внешность, изображать пионера… {w}Стать другим человеком."
    "Я улыбнулся и развеял подозрения подруг."

    show dv normal bkrr_sport at cleft
    show mi normal bkrr_sport at cright
    show us smile sport at center
    with dissolve

    me "Ну вас! Я имел в виду, что наши ключи все вместе, на одном кольце, не разделить, совсем как нашу с вами дружбу, и… {w}Блин, в голове это звучало не так глупо."
    me "Ладно, давайте запирать."
    dv "Да уж. Торжественные речи – это явно не твоё. Но я понимаю, что ты имел в виду."

    show dv smile bkrr_sport at cleft with dspr

    dv "Я чувствую то же самое. {w}И не вздумай потеряться, у меня большие планы на тебя как на басиста! Сыграем на выпускном, и в этот раз – с вокалом! Я тут…"

    show dv shy bkrr_sport at cleft with dspr

    "Она смутилась."
    dv "Написала… Кое-что. {w}Но на концерте оно было не к месту."

    show mi surprise bkrr_sport at cright
    show us surp1 sport at center
    with dspr

    us "Ух ты… {w}Ты всё-таки набралась смелости и покажешь свои стихи?"

    show us smile sport at center
    show mi smile bkrr_sport at cright
    with dspr

    mi "Поверить не могу… Но когда приедем, я посмотрю, как их на музыку положить. {w}Обещаю."

    show dv sad bkrr_sport at cleft with dspr

    dv "Только если кто засмеётся – я ему нос сломаю. {w}Понятно?"
    "Алиса смотрела на меня."
    th "Неужели ей так важно моё мнение?"
    "Я улыбнулся ей."
    me "Сейчас не успеем. Дашь почитать, пока будем ехать?"

    show dv normal bkrr_sport at cleft with dspr

    dv "Я подумаю. Посмотрю на твоё поведение."

    window hide

    hide dv
    hide mi
    hide us
    with dissolve

    $ renpy.pause(1.0, hard=True)

    play sound sfx_lock_open_close_1

    window show

    "Мику мягко накрыла мою руку своей, и мы вместе повернули ключ на второй оборот."

    show mi cry_smile bkrr_sport at cleft with dissolve

    mi "В последний раз."

    show us normal sport at cright with dissolve

    us "В предпоследний."

    show mi upset bkrr_sport at cleft with dspr

    mi "В смысле?"

    show us grin sport at cright with dspr

    us "Алиса там свою гитару оставила, домашнюю."

    show mi upset bkrr_sport at cleft
    show dv angry bkrr_sport close at center
    with dspr

    dv "Японский…{w} магнитофон… Сенька, это всё ты."

    show dv normal bkrr_sport close at center with dspr

    dv "Развёл тут прощальную речь… Я ещё думаю: что-то должно быть в руках. {w}А эта зараза мелкая всё видела и молчала!"

    hide dv
    hide mi
    hide us
    with dissolve

    "Она шутя отвесила Ульяне подзатыльник."
    us "Ай! Меня-то за что?"
    dv "Почему не сказала?"
    us "Семён с Мику такую речь толкнули, разве я могла их прервать?"

    window hide

    $ renpy.pause(1.0, hard=True)

    play sound sfx_lock_open_close_1

    $ renpy.pause(0.8, hard=True)

    play sound sfx_lock_open_close_1 fadeout 0.18

    $ renpy.pause(1.0, hard=True)

    play sound sfx_open_door_2

    scene bg int_music_club_day with dissolve

    play ambience bkrr_ambience_list["indoors_day"] fadein 3

    window show

    "Мне показалось, что отмытый до блеска клуб радостно вздохнул, когда мы снова вошли под его крышу. {w}Иллюзия, конечно."
    "Просто лёгкий сквозняк колыхнул шторы."
    "Алиса торопливо упаковала гитару в чехол, другую – белую с синим – устроила в подставке поудобнее, заправила между струн один из своих медиаторов."
    "Повернувшись к нам, она пояснила:"

    show dv normal bkrr_sport at cleft with dissolve

    dv "Их никогда не хватает. Пусть кому-то будет подарок."

    window hide

    hide dv with dissolve

    $ renpy.pause(1.0, hard=True)

    stop ambience fadeout 0.5

    play sound sfx_open_door_2

    scene bg ext_music_club_verandah_day_v1_ajar with dissolve

    play ambience ambience_camp_center_day fadein 3

    $ renpy.pause(0.5, hard=True)

    play sound sfx_close_door_1
    scene bg ext_music_club_verandah_day_v1 with dissolve

    $ renpy.pause(1.0, hard=True)

    play sound sfx_lock_open_close_1

    $ renpy.pause(0.8, hard=True)

    play sound sfx_lock_open_close_1 fadeout 0.18

    $ renpy.pause(1.0, hard=True)

    window show

    "Второй раз мы уже не прощались с клубом и не говорили трогательных речей."

    window hide

    scene bg ext_music_club_day_empty_bkrr:
        subpixel True
        truecenter
        zoom 1.25
        ease 5.0 zoom 1.0
    with dissolve

    window show

    "Просто заперли замок, подёргали дверь и поспешили по своим домикам."
    "До отъезда оставалось всего ничего."

    window hide

    stop music fadeout 15

    stop ambience fadeout 2

    $ bkrr_timeskip(sounded=False)

    scene bg ext_house_of_un_day with fade

    play ambience ambience_camp_center_day fadein 3

    window show

    "Вожатой в домике не было, так что я быстро собрал все свои вещи и поспешил к домику Мику."

    window hide

    stop ambience fadeout 0.5

    play sound sfx_open_door_1

    scene bg int_house_of_un_day with dissolve

    play ambience ambience_int_cabin_day fadein 3

    window show

    "Конечно же, она была ещё там."
    "И, конечно же, всё ещё собирала по углам домика разбросанные где и как попало расчёски, тапочки, мыльницу, будильник в форме котика и прочую девичью мелочёвку."
    "Лены в домике уже не было, как и её вещей. Наверное, она догадалась, что я приду, и тактично оставила нас с Мику вдвоём."

    show mi normal civil far at cleft with dissolve

    mi "Ой… Ты уже? А я вот… Столько вещей, надо было, конечно, со вчера начать сборы, но этот концерт… {w}а потом вечером…"

    show mi shy civil far at cleft with dspr

    mi "Было… {w}Ну… Некогда."
    "Она густо покраснела и посмотрела на меня."
    me "Виноват, кругом виноват. Ну, раз уж я не дал тебе выспаться, давай помогу со сборами."

    window hide

    show mi smile civil far at cleft with dspr

    $ renpy.pause(1.0, hard=True)

    hide mi with dissolve

    $ renpy.pause(1.0, hard=True)

    stop ambience fadeout 0.5

    play sound sfx_open_door_1

    scene bg ext_house_of_un_day with dissolve

    play ambience ambience_camp_center_day fadein 3

    window show

    "Вдвоём мы быстро уложили вещи в сумку."

    show mi serious civil close at center with dissolve

    mi "Вот и всё… Как будто нас здесь и не было."

    show mi sad_smile civil close at center with dspr

    mi "Больше не будет нашей группы, не будет лагеря… Нет, ну он-то будет, только мы в него уже не вернёмся."
    mi "Я последний раз так себя чувствовала, когда мы уезжали из Японии. Только тогда я была маленькая, и мне было интересно, что там, за океаном. А сейчас…"

    show mi upset civil close at center with dspr

    "Она вздохнула и продолжила:"
    mi "Ни за что бы не поверила, что можно так быстро привязаться к новому месту. Мне очень не хочется отсюда уезжать. И потом…"

    show mi happy civil close:
        subpixel True
        center
        ease 2.5 zoom 1.2
    with dspr

    "Мику прижалась ко мне и продолжила:"
    mi "Здесь у меня есть ты. Я знаю, что и потом ты никуда не денешься, но когда мы уедем, всё уже будет по-другому… {w}Наверное."
    mi "Если бы могла, я бы осталась здесь подольше."

    th "Кому что. Кто-то хочет уйти, кто-то – остаться."
    "Когда мы покинем лагерь, возврата не будет, говорила вожатая."

    me "Милая, ну что за грустные мысли. Всё только начинается."

    hide mi with dissolve

    "Я обнял её, поцеловал и отобрал сумки."
    me "Пошли. Иначе автобус уедет без нас, и твоё желание исполнится. Только не уверен, что нас здесь будут кормить."

    window hide

    scene bg ext_houses_day with dissolve

    window show

    "На полпути к остановке Мику вдруг остановилась."

    show mi upset civil close at center with dissolve

    mi "Я совсем забыла…"
    me "Вернёмся? Время есть."

    show mi upset civil close at center with dspr

    play music music_list["memories_piano_outdoors"] fadein 10

    mi "Нет, я не в том смысле. Я ничего не взяла на память."

    show mi sad_smile civil close at center with dspr

    mi "Трук увёз планер, Ульяна насобирала ракушек, Алиса – пластинку от Клауса, а я всё откладывала, думала, что времени ещё полно… {w}И вот никаких сувениров."

    "Я шутливо обнял её и обиженным тоном поинтересовался:"
    me "А я, значит, на роль сувенира не подхожу?"

    show mi normal civil close at center with dspr

    mi "Ну, прекрати…"
    "Она улыбнулась и попыталась освободиться."
    mi "Ты не сувенир, ты – мой любимый. А надо что-нибудь такое, чтобы на полочку поставить и вспоминать об этом лете… {w}Вот только что? Даже фотографий не получилось, Ульянка плёнку засветила."
    me "Ничего! Сейчас что-нибудь придумаем."

    hide mi with dissolve

    "Я поискал глазами что-нибудь подходящее… Но до появления сувенирных киосков, где можно купить чашку с фотографией лагеря, ручку или там значок, оставалось ещё добрых двадцать лет. Даже завалящего карманного календарика с фотографией причала не было."
    "Идею отодрать дверную ручку или табличку с номером домика я отверг сразу."
    me "Вот!"
    "Я осторожно сорвал яркий вьющийся цветок и протянул Мику."

    show mi sad_smile civil close at center with dissolve

    mi "Но он же завянет…"
    me "Положишь его в книжку, он там высохнет, потом…"
    "Я напряг память, вспоминая, что там делают дальше."
    me "Потом зажмём его между двух стёкол, найдём красивую подставку и аккуратно подпишем: «Пионерлагерь «Совёнок», тысяча девятьсот м-м-м… Какой?"

    show mi serious civil close at center with dspr

    mi "Ой, как всё запущено…"
    me "И ты туда же."

    show mi laugh civil close at center with dspr

    mi "Не скажу. Пусть это будет для тебя сюрпризом."
    me "Ладно…"

    show mi normal civil close at center with dspr

    mi "Только книжки у меня нет."
    me "Не страшно. У меня тетрадь есть."

    hide mi with dissolve

    "Я открыл общую тетрадь с табулатурами. Она уже слегка поистрепалась, последние три недели у неё была нелёгкая жизнь."
    "Надёжно устроив цветок между страниц, я положил тетрадь в сумку и прижал одеждой."

    show mi smile civil close at center with dissolve

    mi "Я не поняла, это кому сувенир? Мне или тебе?"
    me "Тебе."
    mi "Тогда отдавай."
    me "Потом, когда приедем."

    show mi grin civil close at center with dspr

    mi "Вот ты какой жадный. Не ожидала."

    hide mi with dissolve

    "Она улыбнулась и сорвала ещё один цветок."
    "Отряд не заметил потери бойца, вся изгородь была густо усеяна такими же цветами, и их хватило бы на десяток влюблённых пар."
    "Она устроила его в волосах."

    show mi normal civil close at center with dissolve

    mi "Нравится?"
    me "Красота! Только в автобус лучше в руках занеси. А то вдруг Ольга ругаться будет."
    mi "Договорились!"

    window hide

    stop music fadeout 7

    stop ambience fadeout 1

    scene bg ext_bus with fade3

    play ambience ambience_camp_entrance_day_people fadein 3
    play sound_loop ambience_medium_crowd_outdoors fadein 3

    window show

    "На стоянке сегодня было шумно и многолюдно. Наш отряд собрался у знакомого автобуса.{w} Девчонки утащили Мику в сторону и спорили, кто куда сядет."
    "Я остался один на один с вожатой."
    "Предстоящая посадка в автобус заставляла меня нервничать. Я бы предпочёл этого не делать."
    "Мутный он какой-то. Сначала загадочным образом превратился из «ЛиАЗа» в «Икарус», потом изменил моё тело и выплюнул в мистическом лагере, то через пару дней явился снова, подразнил, оттолкнул непонятной силой и растворился в вечерних сумерках."
    "А ещё во сне он явно жульничал в карты.{w} Одним словом – никакого доверия к этому автобусу у меня не было."

    play music music_list["afterword"] fadein 5
    show mt normal panama pioneer at center with dissolve

    mt "Ну что за кислое лицо? Как будто в армию едешь."
    me "Мне страшно. А вдруг я сяду и… {w}исчезну отсюда. Иначе – никак?"

    show mt smile panama pioneer at center with dspr

    mt "Никак."
    "Она похлопала по борту автобуса."
    mt "Но опыт показывает, что обычно вы исчезаете во сне, так что… Думаю, никуда ты не денешься."
    me "Неубедительно."
    mt "Уж как есть. К тому же тебя перестали бы замечать и помнить. А девчонки вон бросают на тебя злые взгляды. Так что, как сказал бы Андрей, ты всё ещё принадлежишь к этой объективной реальности, данной нам в ощущениях."
    "Она произнесла это таким деловым тоном, что я не выдержал и засмеялся."
    "Алиса стояла возле своей огромной сумки и злобно зыркала на меня."
    me "Да… Этот тоже говорил, что во сне. А потом растворился в воздухе."
    mt "Ты {b}меня{/b} слушай, а не сумасшедших призраков. Так что убери эту несчастную мордочку и садись в автобус. А то уедут без тебя, и придётся их догонять."
    me "Бегом, что ли?"

    show mt grin panama pioneer at center with dspr

    mt "Зачем бегом? Я тебе велосипед дам."
    me "Это вот тот, который возле домика?"
    mt "Да-да. Он самый. Детский, конечно, но другого нет."

    hide mt with dissolve

    "Я представил себе, как мчусь за автобусом на трогательном складном «Салюте», задевая коленками подбородок, а из-за стекла автобуса Мику смотрит на меня и отчаянно пытается не упасть со смеху…"
    "А остальные пионеры просто ржут, не стесняясь, указывают пальцами, а если боковые окна открыты, то ещё и кричат в них: «Жми! Быстрее!»."
    me "Нет, давайте без велосипедов. Я пошёл?"

    show mt smile panama pioneer at center with dissolve

    mt "Погоди. Ничего не забыл? Телефон этот свой непонятный, одежду, в которой приехал? Вещи из карманов?"
    me "Вроде бы нет…"
    mt "Проверь ещё раз. Сюда не возвращаются… {w}Если ты не вожатый, конечно."
    me "Что? Вы не говорили…"
    mt "Я много чего не говорила. И много чего не скажу. Уйдёшь – пути назад не будет. Просто не найдёшь поворота с шоссе, как будто и не было его никогда."
    me "Но…"

    show mt normal panama pioneer at center with dspr

    mt "Хватит разговоров. Мне вас нужно еще по головам пересчитать… И вообще."

    window hide
    hide mt with dissolve
    $ renpy.pause(1.0, hard=True)
    play sound bkrr_sfx_list["whistle"] fadein 1
    window show

    "Ольга Дмитриевна достала из кармана свисток и от души в него подула."
    "Завладев вниманием пионеров, вожатая сказала…{w} Нет. Не сказала. Скомандовала."

    mt "Отря-а-а-ад, вдоль бордюра в шеренгу становись!!!"
    "Я снова задумался, кем же она была там, до лагеря.{w} Идеи в голову приходили самые разные."
    "Построив отряд в какое-то подобие линии, Ольга окинула взглядом своих подопечных."

    show mt normal panama pioneer far at center with dissolve

    mt "Ну что, товарищи пионеры? Кажется, ваш отдых здесь подходит к концу. Жертв и разрушений нет… "

    "Она выразительно посмотрела на Шурика и улыбнулась."

    show mt grin panama pioneer far at center with dspr

    mt "Практически нет.{w} Учитывая всё, что случилось за последние недели, включая шторм, приезд комиссии и визит иностранных гостей, я считаю её завершённой успешно."

    show mt smile panama pioneer far with dspr

    mt "Лично я горжусь тем, как вы справлялись со всеми трудностями… "
    dv "Которые сами себе героически создавали!"

    show mt normal panama pioneer far with dspr

    mt "Я рада была провести с вами эти дни, надеюсь, что и вы тоже отдохнули, набрались сил, завели новых друзей…{w} И я хотела бы увидеть всех вас следующим летом."
    mt "Но пока – сделайте одолжение, доберитесь до города без приключений и не доставляйте хлопот сопровождающим. Ладно?"
    sl "А разве вы с нами не поедете?"

    show mt smile panama pioneer far with dspr

    "Ольга улыбнулась и покачала головой."
    mt "Нет. Я останусь здесь. Скоро следующая смена, и всё должно быть готово к их приезду. "

    sl "Но ведь все остальные вожатые едут?"

    mt "Вот они-то за вами и присмотрят.{w} Если отдельные пионерки не станут захватывать автобус, прыгать из окон и закрывать глаза водителю…"

    show mt grin panama pioneer far with dspr

    mt "Да, Ульяна?"

    us "Нет, ну а почему сразу Ульяна?"

    show mt smile panama pioneer far with dspr

    mt "То поездка завершится без приключений. А пока – всё."

    "Она неожиданно взмахнула рукой, отсалютовав нам.{w} Пионеры ответили ей тем же, и даже я, хотя никогда и не был на пионерских линейках, попытался, как мог, воспроизвести этот прощальный жест.{w} Наверное, он должен был выглядеть комично, но не выглядел."

    mt "Всем спасибо, все свободны. А теперь – организованно…{w} Подчеркиваю: {i}ор-га-ни-зо-ван-но{/i} садимся в автобус, ваши ряды – в задней части автобуса, по обе стороны."
    mt "Тяжелые сумки ставим под ноги или отдаём в багажное отделение, наверх – только легкие. Обивку сидений не пачкаем, неприличных слов на ней не пишем, в салоне не мусорим."
    mt "Если кто-то чувствует, что надо посетить уединенное белокаменное строение, сделайте это сейчас."
    mt "Отряд, разойдись!"

    hide mt with dissolve

    "Кто-то принялся перекладывать сумки вниз, девчонки окружили Ольгу, чтобы попрощаться, кто-то отошел к друзьям из других отрядов…"
    "Мику помогала Алисе устроить гитару на багажной полке и теперь они привязывали инструмент милыми синими ленточками."

    show mt smile panama pioneer close with dissolve

    "Вожатая тепло улыбнулась, и показала мне на дверь автобуса."

    mt "Мику ждёт. Иди давай."

    hide mt with dissolve
    stop music fadeout 7

    "Я хотел что-то спросить, но Ольга уже смотрела поверх моего плеча."

    mt "Шурик! Куда ты тащишь радио? Оно же клубное!"
    mt "Что значит «ты привёз»? Я вижу инвентарный номер!"
    mt "Как это поставили по ошибке? {w}Кто? {w}Завхоз? {w}Точно? {w}Всё-всё, не надо инструкцию искать, я верю."
    "Под ногами вертелся Пират и тёрся об мою штанину.{w} Я наклонился и почесал его за ухом."
    me "Ты уж присмотри за лагерем."

    $ bkrr_play_random(bkrr_meow_list)

    "Кот важно мяукнул, то ли соглашаясь, то ли требуя жрать."

    window hide

    scene bg ext_camp_entrance_day with dissolve

    $ renpy.pause(1.0, hard=True)

    window show

    "Я в последний раз оглянулся на ворота лагеря…"

    window hide
    scene bg ext_bus with dissolve
    window show

    "И больше уже не смотрел назад."

    play music music_list["so_good_to_be_careless"] fadein 5

    "Новый незнакомый мир. Новое будущее и, видимо, новое прошлое, к которому ещё предстоит привыкать и в которое придётся вживаться."
    "Необходимость сделать шаг вперёд пугала, но там, в конце пути, меня ожидала новая, с иголочки, жизнь."
    "И почему-то я был уверен, что не растрачу её так же глупо, как ту, прежнюю."
    "Помотав головой, я покрепче ухватил сумку и поспешил к автобусу. Чего гадать, скоро всё узнаю."

    window hide

    stop ambience fadeout 0.5
    stop sound_loop fadeout 0.5

    scene bg int_bus_people_day_bkrr with dissolve

    play ambience bkrr_ambience_list["indoors_day"] fadein 3

    $ renpy.pause(1.0, hard=True)

    window show

    "К счастью, наш отряд был небольшим, и мы с Мику устроились там, где нам не будут мешать нескромные взгляды попутчиков. {w}Алиса и Ульяна заняли места напротив." #TODO "не смогли бы помешать"
    "В салоне стоял шум, все делились впечатлениями, обменивались адресами и телефонами… А я смотрел на сидящую рядом Мику и не мог отвести глаз. Наконец, она не выдержала и с улыбкой поинтересовалась:"

    scene cg bkrr_epilogue_2 with dissolve

    mi "У меня что-то на лице?"
    me "Нет. Просто…"
    "Я вздохнул и накрыл её руку своей. Ну как ей объяснить, что последние несколько дней я всё время боялся, что исчезну и больше никогда её не увижу?"
    me "Всё слишком хорошо."
    mi "Так и должно быть."

    window hide

    stop ambience fadeout 3

    $ bkrr_set_volume("sound_loop", 0.5)
    play sound_loop sfx_bus_interior_moving fadein 2
    play ambience ambience_medium_crowd_outdoors fadein 2

    $ renpy.pause(1.0, hard=True)

    scene bg int_bus_people_day_bkrr at bkrr_bus_shaking with dissolve

    $ bkrr_set_mode(nvl)

    nvl show dissolve

    "Автобус мягко заурчал, бетонная ограда лагеря поплыла мимо окон и вскоре сменилась сочной зеленью лесополосы, за которой проглядывали жёлто-зелёные поля подсолнухов, золотистые моря пшеницы и ещё чего-то, что городской житель вроде меня не мог распознать."
    "Я коснулся твёрдой обложки свидетельства о рождении. {w}Глупо, конечно, но потёртая зелёная книжка внушала куда больше уверенности, чем все обещания, данные мне вожатой, двойником, девочкой кошкой. {w}Какая уверенность может быть в чуде, пусть уже и случавшемся? {w}А документ есть документ. {w}Если бы ещё не фамилия…"
    "Я хмыкнул и мысленно пожелал двойнику забыть надеть куртку, чтобы в самый пикантный момент Юля его исцарапала. {w}Если, конечно, это его рук дело, а не лагеря, который, может быть, и не лагерь вовсе."
    "Что же это было за место? {w}За последние дни я узнал о нём много… {w}И в то же время ничего. {w}А теперь, наверное, уже никогда и не узнаю."
    "Тайна осталась тайной, но кусочек чуда я всё-таки увёз с собой. {w}Помолодевшее тело, шанс начать всё с начала… {w}И любимую девушку, которая сидела рядом и улыбалась мне…"
    "Мику действительно смотрела на меня, но отчаянно боролась со сном."

    nvl clear

    nvl hide dissolve

    $ renpy.pause(1.0, hard=True)

    $ bkrr_set_mode()

    window show

    me "Не выспалась?"

    scene cg bkrr_epilogue_2 at bkrr_bus_shaking with dissolve

    "Она сладко зевнула."
    mi "Да… В смысле, нет. Не выспалась. И кто в этом виноват, ты не знаешь?"
    me "Оба, милая. Оба!"
    "Она смущённо улыбнулась и кивнула."
    mi "Сейчас засну."
    me "Так поспи. Ольга Дмитриевна говорила, что нам ехать часа три, успеешь отдохнуть."
    mi "Ну! Мы же парочка, нам положено держаться за руки и смотреть друг на дружку влюблёнными глазами. А ты предлагаешь мне спать?"
    me "Я думаю, у нас ещё всё впереди."
    mi "Ты прав. Не обидишься, если я немножко посплю?"
    "Она подмигнула мне."
    me "Страшно обижусь. И не прощу, пока не проведёшь мне экскурсию по нашему городу."
    mi "Я подумаю! Потом… Когда проснусь."

    stop music fadeout 5

    scene cg bkrr_epilogue_3 at bkrr_bus_shaking with dissolve

    "Мику показала мне язык, положила голову мне на плечо и закрыла глаза."
    "Обсуждать с рыжими прошедший концерт мне совсем не хотелось, так что я устроился поудобнее и рассматривал то проносившиеся за окном поля, то посапывающую на моём плече любимую."

    scene cg bkrr_epilogue_4 at bkrr_bus_shaking with dissolve

    "Какая же она милая, когда спит.{w} Многие девчонки жаловались на сухость кожи и нежеланный загар, но лицо Мику словно светилось изнутри."
    th "Как красиво падает свет…"
    "Я поправил прядку волос, упавшую на её лицо."
    "Ещё какое-то время можно ехать и ни о чём не волноваться. Но дорога закончится, и что тогда?"
    "Искать квартиру Ольги… Если она вообще есть в природе. {w}А если нет?"
    "Если наша вожатая – ещё один фантом, созданный этим загадочным лагерем? Если этого адреса нет, если соседка сделает удивлённое лицо и скажет, что не знает никакую Ольгу Дмитриевну."
    "Нужно будет как-то устраиваться. Как? Кем? Куда?"
    "Конечно, Ольга обещала, что всё как-то устроится. Но обещания – это одно, а перспектива ночевать на вокзале или объяснять родителям Мику, что идти мне некуда и что из дома я не сбегал – совсем другое. {w}Куда более реальное."
    "В лагере всё было словно понарошку, и мне казалось, что впереди ещё полно времени. Что реальная жизнь осталась где-то позади, и такие мелочи больше не будут меня волновать."
    "А сегодня сказка заканчивается. Нужно будет что-то есть, где-то жить… {w}Интересно, есть ли КГБ в этом прошлом?"
    "Когда Мику проснётся, мне нужно будет с ней очень серьёзно поговорить."

    scene bg int_bus_people_day_bkrr at bkrr_bus_shaking with dissolve

    "В любом случае придётся рассказать, кто я, откуда взялся… {w}И что без её помощи мне ни за что не справиться."
    th "Вот только как начать? Что-то вроде «Мику, милая, любишь ли ты фантастику?»"
    th "Или слышала ли она о путешествиях во времени."
    "Мелочь в кармане, кое-какая мелочёвка вроде зажигалки с фонариком, телефон в конце концов…"
    "Наверное, я смогу её убедить."
    "Она любит меня и поверит в такую фантастическую историю."
    "А её родители? {w}С ними будет сложнее."
    "Появляется ухажёр без дома, без родителей и несёт мистическую чушь. {w}Наверное, придётся поговорить с отцом. Я ведь не прошу брать меня на содержание… {w}Только поверить и поддержать на первых порах."
    "Ещё эта подростковая внешность…"
    "Если Ольга не шутила и мне официально шестнадцать или семнадцать, то ещё два года я даже не смогу работать, зато нужно будет ходить в школу. {w}Документы… Деньги на одежду… Еда и жильё."
    "Но это лучше, чем снова стать прежним. {w}Если Мику проснётся и увидит, что её любимый Семён стал старше на десяток лет, обзавёлся щетиной, мешками под глазами и прочими атрибутами не слишком следящего за собой двадцатипятилетнего мужчины, то…"
    "Не хочу даже думать, как она отреагирует. Любовь-то она, конечно, слепая, но ведь не настолько же."
    "Ничего. Главное, что мы вместе. Пока она рядом, я смогу всё. Ну, или почти всё."
    "Ободрённый этой мыслью, я посмотрел на Мику."

    window hide

    scene cg bkrr_epilogue_4 at bkrr_bus_shaking with Dissolve(3.0)

    window show

    "Чтобы увидеть…"

    window hide

    scene cg bkrr_epilogue_5 at bkrr_bus_shaking with Dissolve(1.0)

    play music music_list["orchid"] fadein 5

    window show

    "Как она медленно исчезает."
    "Тает в воздухе. Медленно, но неотвратимо…"
    "Как привидение."
    "Я отчётливо видел узор на обивке кресла, просвечивающий сквозь лицо Мику."
    me "Нет… Пусть это будет сон, галлюцинация, да что угодно."
    me "Только не надо так."
    me "Пожалуйста…"
    "Я не знал, к кому обращаюсь."
    "И, конечно, это не помогло."
    me "Мику!"

    window hide

    scene bg int_bus_people_day_bkrr at bkrr_bus_shaking with dissolve

    window show

    "Мику услышала меня, улыбаясь, открыла глаза, посмотрела на меня, шевельнула губами, но я не услышал ни звука."

    scene cg bkrr_epilogue_6 at bkrr_bus_shaking with dissolve

    "Ещё несколько секунд – и она исчезла совсем."
    "Без следа. Только сорванный по пути к автобусу цветок мягко упал на сиденье."
    "Я вцепился в него, как в последнюю ниточку, которая связывала меня с реальностью."

    scene cg bkrr_epilogue_8 at bkrr_bus_shaking with dissolve

    me "{b}Мику!!!{/b}"
    "Кажется, я кричал."
    "И никто не отреагировал на мой вопль. Даже не обернулся. Словно так и должно быть: пионер с диким взглядом орёт на весь автобус."
    "Только Алиса на соседнем сиденье повернулась ко мне и лениво поинтересовалась:"

    scene cg bkrr_epilogue_7 at bkrr_bus_shaking with dissolve

    dv "Сенька, ну чего шумишь?"

    window hide

    scene bg int_bus_people_day_bkrr at bkrr_bus_shaking
    show dv normal civil close at cright
    with dissolve

    window show

    me "Алиса, Мику пропала!"
    dv "Мелки? Под сиденьем глянь, может, выпали? {w}Тоже мне горе."

    hide dv with dissolve

    "Она зевнула и подвинула шторку, закрывая лицо спящей Ульяны от солнца."
    me "Да не мелки! Мику!"

    show dv surprise civil close at cright with dissolve

    dv "Что за Мику?"
    th "Сон. Точно сон. Осталось только проснуться…"
    th "Если это наяву, я сойду с ума. Тут же. Не сходя с места."
    me "Алиса, хватит шуток. Мы с Мику садились вдвоём в автобус. Она здесь была. А теперь… Вот."

    show dv guilty civil close at cright with dspr

    dv "Сенька, тебе что, голову напекло? Мы втроём сели. {w}Ты, я, Ульяна."

    show dv sad civil close at cright with dspr

    dv "Что за кличка такая вообще? Ты себе кошку нашёл?"

    hide dv with dissolve

    stop music fadeout 5

    "В моей голове замелькали мысли."
    th "Уходят во сне."
    th "Её отсутствия не замечают."
    th "Зато я остался здесь."
    th "Значит…{w} Она была не отсюда?"

    window hide

    $ renpy.pause(1.0, hard=True)

    scene bg int_bus_people_day_bkrr at bkrr_bus_shaking with dissolve

    play music music_list["no_tresspassing"]

    $ bkrr_set_mode(nvl)

    nvl show dissolve

    "Выходит, она была не из этого места и времени с самого начала? {w}Теперь… {w}Если сложить в голове все её рассказы и оговорки, то её история была слишком фантастичной. И в чём-то похожа на мою."
    "Переехала из Японии, нет друзей… Нет дома, точнее – есть, но постоянно переезжают… {w}И её рассказы напоминали истории анимешницы, а не настоящей японки."
    "Если бы я оказался девочкой из будущего, то сочинил бы что-то в этом духе. Даже наверняка."
    "Кусочки головоломки со щелчками становились на места. {w}В пазле оставалось немало дыр, но я всё острее понимал, что планы на счастливую семейную жизнь здесь и знакомство с дедушкой-японцем можно больше не строить."

    nvl clear

    nvl hide dissolve

    $ renpy.pause(1.0, hard=True)

    scene cg bkrr_epilogue_7 at bkrr_bus_shaking with dissolve

    $ bkrr_set_mode()

    window show

    th "Но я-то почему всё ещё здесь?"
    th "Я – её фантазия? Да ну, быть не может. Я настоящий. Я всё помню, кто я и откуда."
    th "Если… Разве что двойник не врал и перенос происходит только во сне."
    "Но сейчас, с зажатым в кулаке измятым цветком и бушующим адреналином, я точно не усну."
    th "И Алиса с Ульяной. Почему они не замечают, что Мику нет? Это то самое «выборочное восприятие», как с двойником?"
    th "Или на самом деле это и не люди совсем, а кто-то с виду похожий на моих подруг. Фантомы? Декорация? Может, и не было никакой Алисы и Ульяны?"

    scene cg bkrr_epilogue_8 at bkrr_bus_shaking with dissolve

    th "Нет, хватит. Так можно и с катушек съехать."
    "Мы ведь вместе зашли в автобус."
    "Алиса ещё подавала сумку Мику, чтобы положить на верхнюю полку…"
    "Я поднял глаза. Сумки тоже не было."
    "Смешная спортивная сумка с котиками пропала вместе с хозяйкой."
    th "То, что… {w}Не принадлежит этому месту."
    th "Или снова начались шутки со временем? Вдруг тот, второй Я, где-то в прошлом помешал нам с Мику встретиться, и возник временной парадокс?"
    th "Но зачем? Он приложил столько усилий…"
    th "И как он мог это сделать?"
    "Сволочная фантазия тут же услужливо нарисовала мне способы: перелом, похищение… или ещё что похуже."
    th "Да что же это творится?"
    "Идей было много. Из области мистики, фантастики и прикладной психиатрии."
    "Совсем как в первый день."
    "Мне снова страшно захотелось опуститься на пол, принять позу эмбриона и кричать: «За что? Почему я?»"
    "Я с опаской глянул на соседние кресла. Алиса продолжала смотреть на меня."
    th "Наблюдает? Изучает? Замышляет что-то?"

    "Но рыжая пионерка напротив смотрела на меня с искренней заботой."
    dv "Сень, ты как в целом? Не укачало? Ты зелёный весь… И глаза дикие."
    us "Они у него всегда дикие. Больной он. Да, Семёныч? Приедем, сдадим тебя в поликлинику. Для опытов."
    me "Что-то мне нехорошо. Водички нет?"
    dv "Так и есть. Укачало. Ты воду не пей, а то стошнит. {w}На, мятные леденцы хорошо помогают."
    "Она протянула мне конфету и добродушно улыбнулась."

    scene bg int_bus_people_day_bkrr at bkrr_bus_shaking with dissolve

    "Если это была не «моя» Алиса, то она чертовски хорошо ей притворялась."
    "Я послушно развернул леденец, взял его в рот и прикрыл глаза, пытаясь взять себя в руки."
    me "Алиса…"

    show dv normal civil close at cright with dissolve

    dv "Больше не дам. У меня два – тебе и Ульяне."
    me "Нет. Я не об этом."
    dv "А о чём?"
    me "Сколько человек в музклубе?"
    dv "Трое… С Толиком – четверо."
    me "А… имя Мику тебе ничего не говорит?"

    show dv guilty civil close at cright with dspr

    dv "Да что за Мику такое?"
    me "Японка. Музыкантка. Ты её не помнишь?"

    show dv smile civil close at cright with dspr

    dv "Не было никаких японцев. Вьетнамец был, немец… Ну и эти, мелкие, черненькие."
    me "Нет. Она не из Японии, она здесь живёт. В нашем отряде такой нет?"
    "Я вдруг снова ощутил себя разведчиком на чужой территории… Как тогда, в день приезда. Когда следил за каждым своим словом и видел в каждом врага. Или потенциальную угрозу. Даже в Славе."

    show us normal sport close at cleft with dissolve

    us "Сенька, ты головой не бился? Ну сам подумай, откуда здесь взяться японке? Алиска, ты ему все-таки мозги отшибла!"
    me "Извините, мне что-то нехорошо."

    show dv normal civil close at cright with dspr

    dv "Ты отдыхай, мы тебя разбудим."
    me "Алиса, кто на второй гитаре играл?"

    show dv laugh civil close at cright with dspr

    dv "Как это «кто». Слушай, тебе к врачу надо. Может, нам тебя связать?"
    "Я знал этот тон. Она шутила, как умела, но в голосе сквозило явное беспокойство."
    me "Нет. Наверное, что-то приснилось."

    show dv normal civil close at cright with dspr

    dv "Клаус играл. Ты на басу. Я на гитаре. Улька барабанила."
    dv "Что, комплимента захотел? {w}Ладно. Хорошо вышло, молодец!"
    me "А репетировали мы втроём?"
    dv "Нет, блин! С симфоническим оркестром! Сначала с Толей, потом с тобой. Еще вопросы?"
    me "И рядом со мной никого не было?"

    show dv smile civil close at cright with dspr

    dv "Нет, конечно! Кое-кто был."
    me "Кто?"
    dv "Как кто? Ульяна хотела к окошку, но потом ко мне перебралась."

    show us laugh2 sport close at cleft with dspr

    us "Алиска, давай верёвку. У нас басист чокнулся!"
    dv "Это он с недосыпу. Ты поспи, я тебя растолкаю."

    show us grin sport close at cleft with dspr

    us "Сенька, не ведись. Она тебе усы нарисует. Или слово плохое на лбу напишет!"
    dv "Дура!"
    us "Сама такая!"

    window hide

    scene cg bkrr_epilogue_7 at bkrr_bus_shaking with dissolve

    window show

    "Они принялись в шутку бороться, а я откинулся на спинку кресла и зажмурился."
    "Наверное, мне нужно было вскочить со своего места и… {w}Не знаю. Наверное, кричать? {w}Тормошить всех вокруг и доказывать, что Мику – не сон. Что она была здесь! Минуту назад была!"
    "Но я понимал, что из этого ничего не выйдет. Меня охватило тяжёлое, гнетущее отчаяние. Мерзкое ощущение. Я пытался придумать, что делать, но в голову ничего не шло. Да и что здесь можно поделать?"
    "Моя любимая девушка только что медленно истаяла в воздухе."
    th "Кричать и звать на помощь?"
    "Бессмысленно. И почему-то стыдно."
    th "«Выдернуть шнур, выдавить стекло» и бежать назад в лагерь, прося Юлю, Ольгу, да хоть чёрта с рогами о помощи?"
    "Поздно. Лагерь остался далеко позади, и, если верить вожатой, то я его уже просто не найду."

    stop music fadeout 10

    "Я отчаянно пытался придумать хоть какое-то решение…"
    "Но его не было."
    "Алиса с Ульяной всё ещё веселились, но не пытались заговорить…"
    "И, кажется, смотрели сквозь меня, не задерживая взгляд."
    "Без Мику мне здесь было нечего делать."
    "Кто-то из нас явно сошёл с ума. Я или мир вокруг."
    "А значит…"

    stop sound_loop fadeout 0.5

    window hide
    play sound sfx_intro_bus_transition

    scene anim intro_14 with bkrr_fade(1.0)

    $ renpy.pause(1.0, hard=True)

    scene anim intro_15:
        align(0.5, 0.4)
        zoom 1.4
    with dspr

    $ renpy.pause(1.5, hard=True)

    stop sound_loop fadeout 0.5
    stop ambience fadeout 0.5
    play sound2 bkrr_sfx_list["whiteout1"]

    scene bg int_bus_night at bkrr_bus_shaking
    show black
    with bkrr_fade(0.2)

    $ bkrr_set_time("night")

    play sound_loop2 sfx_head_heartbeat fadein 5

    window show

    "Я так и не решил, что нужно делать, когда всё случилось само."
    "Странное онемение разлилось по всему телу, я не мог ни вздохнуть, ни пошевелиться. Открыть глаза было труднее, чем встать после того первого удара по голове."
    th "Может, я всё ещё в медпункте, и это только бред от лекарств и температуры?"
    "Я отчаянно цеплялся за эту мысль, пытаясь поднять непослушные веки. О том, чтобы пошевелить рукой, нечего было и думать."
    "Тело не слушалось, оно обмякло и было тяжёлым, словно налилось свинцом."
    "Наконец, я смог совладать хотя бы с веками. Открывая глаза, я был готов увидеть что угодно. {w}Свою квартиру, потолок домика в лагере, а может, и серый бетон бомбоубежища под лагерем."

    window hide

    hide black
    show unblink
    with None

    play sound_loop sfx_bus_interior_moving fadein 2.5
    stop sound_loop2 fadeout 5

    $ renpy.pause(2.5, hard=True)

    window show

    play music music_list["sunny_day"] fadein 10

    "Шумная компания пионеров исчезла, исчезли и их сумки."
    "Салон был пуст. Ни людей, ни вещей…"
    "Ни водителя, раз уж на то пошло. В зеркале над водительским местом отражалась пустая кабина."
    "Но мотор гудел, автобус куда-то ехал, изредка подпрыгивая на неровностях дороги, а за окном проносился безликий пейзаж, леса и поля, скрытые туманом. {w}На горизонте мелькали какие-то домики, а необычайно низкая луна заливала всё призрачным голубоватым светом."
    th "Если уже ночь… То куда делся день?"
    "А я-то надеялся, что чудеса закончились…"
    "Как наивно."
    "И я был не один. Рядом стоял… {w}А может, и сидел кто-то ещё."
    ml "Я боялась, что не успею. Но, кажется, ещё не поздно."
    me "Кто ты? И где Мику? И… Все остальные."
    ml "Едут по домам, в город. И понятия не имеют, что вы с Мику были в одном автобусе с ними."
    me "А Мику? Она исчезла… Куда… Где она? Она просто исчезла…"
    "Я замолчал, пытаясь привести мысли в порядок."

    stop music fadeout 10

    $ bkrr_set_char_color("ml", "#DDDB80")

    ml "Во-первых, не волнуйся. С ней всё в порядке, и она там, где должна быть. Дома. У себя дома."
    me "Она была… Не отсюда?"
    ml "Наверное. Этот лагерь вытворяет странные штуки с памятью. Там я была уверена, что мы давно знаем друг друга… А теперь я помню, что она появилась немного раньше тебя."
    "Голос был взрослый, приятный… И странным образом успокаивал. {w}Я слышал его раньше. Дважды…"
    "Раз – когда ехал сюда. {w}Это она уговаривала меня не волноваться."
    "И второй – во сне. Это была она. {w}Она говорила с той парочкой в квартире, так похожей на мою, но не моей…"
    me "Можно её вернуть?"

    stop sound_loop fadeout 15
    play music music_list["into_the_unknown"] fadein 10

    "Моя собеседница молча посмотрела в окно, затем покачала головой."
    ml "Ничего не выйдет. Это дорога в один конец. Тот, второй, смог вернуться… но у него была эта его кошка, нам такой вариант не пойдёт."
    me "Ты знаешь про них?"
    ml "Ты не единственный, кого они использовали… И по чьим головам прошлись."
    me "О чём ты?"

    $ bkrr_set_char_color("ml", "#CED28D")

    ml "Он рассказал тебе жалостливую историю про то, как не может жить без Юли, но ей нет места в вашем мире, да?"
    me "Всё так и было."
    ml "Они хорошо умеют дёргать за ниточки. Знают, что сказать, чтобы ты сам захотел сделать то, что им нужно. Особенно, если ты маленькая и глупая девчонка."
    "Она негромко фыркнула, словно от сдерживаемого смеха."
    ml "Или наивный дурачок в теле пионера."
    me "Откуда ты всё это знаешь? Кто ты?"
    ml "Если я расскажу, это всё испортит… Ты ведь хочешь вернуть Мику? Мой ответ ничем не поможет."
    me "А… Что поможет?"
    ml "Для начала можешь минутку помолчать. Мне нужно…"
    "Она вздохнула."

    $ bkrr_set_char_color("ml", "#BFC99B")

    ml "Вспомнить. И подумать. Тогда я сделала всё на эмоциях, у меня получилось почти случайно, и прошло столько лет…"
    me "Что вспомнить? О чём ты вообще?"
    ml "Вспомнить, как это было."
    ml "Мику сюда уже не вернётся. Тем более, что этого «сюда» на самом деле нет."
    me "Как нет? Где мы тогда?"

    $ bkrr_set_char_color("ml", "#ADBFAA")

    ml "Нигде. И в то же время – везде. Если хочешь, можешь назвать это «суперпозиция»."
    ml "Но скоро мы окажемся… Где-то. Пока не уверена, где."
    me "Восхитительно…"
    ml "Хватит жаловаться. Всё могло быть хуже."
    me "Куда уж хуже-то?"
    "Она подвинулась ближе."
    ml "Хуже может быть всегда. И это как раз наш случай."
    me "Что вообще происходит?"

    $ bkrr_set_char_color("ml", "#9EB6B6")

    ml "Эти двое решили не рисковать."
    ml "Тебя здесь быть не должно. Любое твоё действие, даже взятое со стола яблоко может вызвать непредсказуемые изменения… Как круги на воде."
    ml "Поэтому источник возмущений быстро убрали подальше. А источник – ты."
    me "Откуда ты всё это знаешь?"
    ml "Они и рассказали. Юля действительно не могла жить там, у вас. Потому что её, строго говоря, нет.{w} Она существует только в лагере и не может выйти за его пределы."
    ml "Но есть одна молоденькая глупышка, которая смогла сделать лагерь и всё вокруг него… более материальным.{w} Для себя и… еще для одного человека."
    me "Ничего себе… И что будет дальше?"
    ml "Став реальной здесь, эта кошка сможет выбраться в другой мир и остаться в нём. Так себе план, но другого у нас… У них не было."
    me "Мику… Сделала лагерь реальным?"

    $ bkrr_set_char_color("ml", "#81A6CF")

    "Моя собеседница негромко хмыкнула."
    ml "Нет. Она потрясающий музыкант и хорошо поёт, но такие вещи ей не под силу."
    me "Тогда зачем всё это?"
    ml "Чтобы эта глупая девчонка захотела сделать то, что сделала.{w} Она уже создала тихий мирок, где её желания исполнились, и повторять это ещё раз просто не стала бы."
    me "А для меня, значит, стала бы?"
    ml "Для вас двоих она пошла бы на всё. Чувство вины – страшная сила. Не спрашивай, почему."
    me "Не буду. {w}И как? У них получилось?"
    ml "Наверное. Не знаю.{w} Я уже давно не видела снов про лагерь до сегодняшнего дня, так что… Наверное, я им больше не нужна."
    "Она помолчала."
    ml "Вот только мне не нравится, как они обошлись с вами двумя. {w}Это жестоко… и не нужно."
    ml "Но кое чего они не учли."

    $ bkrr_set_char_color("ml", "#B956FF")

    "Девушка положила руки мне на плечи. Краешком глаза я почти мог увидеть её лицо… {w}Знакомое и незнакомое одновременно."
    me "Чего?"
    ml "Меня."
    "Она подалась вперёд и быстро коснулась губами моей щеки, обдав её легким ароматом."
    ml "На удачу."
    "Земляника. {w}Снова земляника…"
    "Я почувствовал, что теряю сознание…"

    window hide
    stop music fadeout 7
    scene white with Dissolve(2.0)
    $ renpy.pause(1.0, hard=True)
    window show

    "И дальше был только яркий свет."

    window hide

    $ renpy.pause(4.0, hard=True)
    $ bkrr_set_time("prologue")
    play sound bkrr_sfx_list["brake_hit"]
    $ bkrr_set_volume("sound3", 0.5)
    $ bkrr_set_volume("sound_loop2", 0.2)
    play sound3 bkrr_sfx_list["bus_leaving"] fadein 3
    $ renpy.pause(1.0, hard=True)
    play sound2 bkrr_sfx_list["horn_tooting"]
    play sound_loop bkrr_sfx_list["taxiloop"] fadein 4
    play sound_loop2 bkrr_sfx_list["traffic_outside"] fadein 4
    play music music_list["lightness_radio_bus"] fadein 7

    scene bg ext_bus_stop_night
    show snow
    show white:
        ease 5.0 alpha 0.0
    with None

    window show

    dr "Вот же ж…"
    "Водитель добавил несколько непечатных слов."
    dr "И как таким … только доверяют автобус вести, а?{w} Нет, ты видел…"
    dr "А, ну да. Проснулся? Мы приехали."
    me "Приехали? Куда приехали?"
    dr "Как это куда. В адрес. До дома-то дойдёшь?"
    me "До дома? Какого?"
    dr "Эх, молодёжь. Пить не умеете, а туда же."
    dr "Давай, просыпайся. Вон твой дом."

    window hide

    $ renpy.pause(1.0, hard=True)

    play sound bkrr_sfx_list["cardoor"]
    $ bkrr_set_volume("music", 0.3)
    with vpunch

    play ambience ambience_cold_wind_loop fadein 3
    $ bkrr_set_volume("sound_loop", 1.0, 1.0)

    window show

    "Водитель назвал улицу и дом. Адрес был мой.{w} В смысле – тот самый, откуда я уехал месяц назад. {w}Он участливо посмотрел на меня и показал на сугроб."
    dr "Если совсем развезло, вон зачерпни снежка, лицо потри, сразу попустит. Всегда так делаю, лучше всякого кофе! Только жёлтый не бери!"
    "Он заржал над своей немудрёной шуткой, а я соображал, где нахожусь."

    stop music fadeout 3
    stop sound_loop fadeout 2
    play sound bkrr_sfx_list["car_leaving"] fadein 3

    th "Ведь только что…"
    th "Это что, был сон?"
    th "Или…"
    "Я машинально уставился на свои руки. Маленьких твердых мозолей на пальцах больше не было.{w} Полученный в «Совёнке» загар сменился привычной бледностью, а едва заметный ожог от чайника исчез."
    "Коснувшись подбородка, я понял, что моя лёгкая небритость снова со мной…"
    th "Просто сон."

    stop music fadeout 5

    "Натирать лицо снегом я, конечно, не стал, а просто побрёл к себе."

    window hide

    stop sound_loop2 fadeout 3
    stop ambience fadeout 3

    scene bg black with Dissolve(3.0)

    play sound sfx_close_door_1

    $ renpy.pause(1.0, hard=True)

    scene bg semen_room with Dissolve(3.0)

    $ bkrr_set_volume("music", 1.0, 1.0)

    play sound_loop sfx_street_traffic_outside fadein 5

    window show

    "Квартира встретила меня привычным затхлым запахом, беспорядком и полным отсутствием намёка на уют."
    "Отстающие обои, древняя мебель, хлам на всех горизонтальных поверхностях и пыль там, откуда хлам соскальзывал. {w}Умирающий от старости чай на столе и…"
    me "Вот я и дома…"

    window hide

    play sound sfx_open_cabinet_2

    $ renpy.pause(1.0, hard=True)

    window show

    "Машинально я открыл шкаф, чтобы повесить пальто. Вешалка в прихожей давно отвалилась, да так и стояла, прислонённая к стене."
    "В зеркале отразилась слегка посвежевшая и отдохнувшая физиономия. {w}Моя, двадцатипятилетняя."

    window hide

    play sound sfx_close_cabinet

    $ renpy.pause(1.5, hard=True)

    $ bkrr_set_volume("music", 1.0)

    play music music_list["farewell_to_the_past_edit"] fadein 5

    window show

    "Кажется, сказка закончилась."
    "Телефон в кармане поймал, наконец, сеть и заверещал сигналами о входящих сообщениях."
    "Несколько пропущенных звонков от друга, который так и не дождался меня на той встрече, несколько реклам, предложение нового супервыгодного тарифа…"
    "Судя по часам, я где-то провёл всю ночь."
    th "Нужно было спросить водителя, откуда мы ехали, кто его вызвал…"
    th "Хотя какая разница?"
    "Я брезгливо шаркнул ногой по слою мелкого мусора на полу."

    window hide

    show blink

    $ renpy.pause(1.5, hard=True)

    hide blink
    show unblink
    with None

    $ renpy.pause(1.5, hard=True)

    window show

    th "Так не пойдёт. С завтрашнего утра я начну поиски Мику… Точнее, уже с сегодняшнего."
    "Даже если она переживёт мою повзрослевшую внешность, то из этой берлоги выскочит в ужасе. И больше никогда не вернется."
    "По телу разливалась странная бодрость. У меня было чувство, что я хорошо и крепко выспался, так что предстояло занять чем-то остаток ночи до утра."

    "Нужно что-то делать. Много с чем… С полом… С обоями… {w}И в первую очередь – с собой."
    "Компьютер, который я не выключил перед выходом, всё ещё смотрел на меня белым прямоугольником монитора. Я уже собрался сесть за него и раствориться в том мире за стеклом, где проводил последние годы."
    "Это действие было привычным, на уровне рефлекса. Оно обещало комфорт, сесть за компьютер было как сунуть ноги в пару разношенных до удобной мягкости тапочек. И это очень помогло бы мне отвлечься от мыслей."

    "Но я вздохнул и побрёл выкапывать из-под завалов в углу комнаты веник. {w}Последний пакет для пылесоса был использован давным-давно, а купить новый всё не доходили руки."

    window hide

    stop music fadeout 10

    scene bg int_entrance_day with fade3

    window show

    "Утро застало меня в самом разгаре уборки. Пакетов с мусором накопилось много, так что путь к мусоропроводу и обратно я проделал несколько раз."

    window hide

    play sound sfx_hatch_drop

    $ renpy.pause(1.5)

    play sound sfx_brass_drop

    $ renpy.pause(1.0)

    window show

    "Когда очередной пакет с какими-то бутылками и старым хламом загрохотал вниз по трубе, под ноги мне с писком метнулось что-то большое и чёрное."

    play sound bkrr_sfx_list["kitten"] fadein 1

    th "Крыса? Ну а что, место подходящее. Надо же, какая здоровая."
    "Но «крыса» сидела под ногами и не делала попыток скрыться, только тихо пищала."
    "Я присмотрелся."
    "Это оказался маленький чёрный котёнок в белых носочках. {w}Опять подбросили."
    "Каждый месяц в подъезде появлялись подкидыши, а потом куда-то исчезали. Никогда не задумывался, куда."

    play music bkrr_music_list["i_am_a_cat"] fadein 5
    scene bg int_entrance_day_with_cat with dissolve

    "Запах мусорника ел глаза не хуже иприта, но я задержал дыхание, нагнулся и взял котёнка в руку."

    play sound bkrr_sfx_list["meow6"]

    "Почувствовав тепло, он обхватил лапками мою руку и снова тихо запищал, словно прося не оставлять его здесь, на холодной и тёмной лестнице."
    "Раньше я просто отнёс бы его вниз. {w}Самое большее – вынес бы что-то съедобное."
    "Но сейчас…"
    "Он смотрел на меня с какой-то обречённой готовностью."
    "Словно говорил: «Да, я всё понимаю. Только не бей меня ногой, просто поставь, и я уйду искать еду в другом месте»."
    th "А почему бы и нет?"
    "Я успел привыкнуть к тому, что поблизости вертится кот. {w}Там, во сне. {w}Если это был сон."

    window hide

    stop music fadeout 7
    scene bg int_entrance_day with dissolve

    window show

    "Находка котёнка, точь-в точь похожего на Пирата, показалась мне добрым знаком."
    "Я спрятал тёплый комок меха за пазуху, где он тут же затих и заурчал, а потом поинтересовался у находки:"
    me "Пойдёшь ко мне жить?"

    play sound bkrr_sfx_list["meow5"]

    "То ли он понял вопрос, то ли просто отреагировал на голос, но в ответ донеслось согласное: «Мяу»."
    me "А звать я тебя буду Пиратом. Ты очень похож на одного моего знакомого кота."
    "И на этот раз он тоже не возражал."

    window hide

    stop sound_loop fadeout 2

    scene bg semen_room_half_clean_bkrr with fade2

    play sound sfx_close_door_1
    play sound_loop sfx_street_traffic_outside fadein 5

    window show

    "Я вернулся в квартиру, отыскал в холодильнике старую котлету и полпакета молока, а потом какое-то время наблюдал за тощим, как велосипед, котёнком, жадно набивающим живот."
    "Остаток утра прошёл в уборке, попытках объяснить пищащему Пирату, что я не могу всё время таскать его на руках, и мыслях."
    "О Мику."
    "О том, где её искать."
    "Как искать…"
    "И что я скажу ей, если найду."
    th "Нет. Не «если». Когда найду."

    window hide

    stop sound_loop fadeout 3

    play music music_list["a_promise_from_distant_days"] fadein 7

    # GOVNOKOD ALERT
    scene anim prolog_1 with Dissolve(2.0)

    show bkrr_calendar:
        truecenter
    show bkrr_calendar_dec8:
        pause 8.0
        cal_sheet_right
    show bkrr_calendar_nov:
        pause 7.5
        cal_sheet_left
    show bkrr_calendar_oct:
        pause 7.0
        cal_sheet_right
    show bkrr_calendar_sep:
        pause 6.5
        cal_sheet_left
    show bkrr_calendar_aug:
        pause 6.0
        cal_sheet_right
    show bkrr_calendar_jul:
        pause 5.5
        cal_sheet_left
    show bkrr_calendar_jun:
        pause 5.0
        cal_sheet_right
    show bkrr_calendar_may:
        pause 4.5
        cal_sheet_left
    show bkrr_calendar_apr:
        pause 4.0
        cal_sheet_right
    show bkrr_calendar_mar:
        pause 3.5
        cal_sheet_left
    show bkrr_calendar_feb:
        pause 3.0
        cal_sheet_right
    show bkrr_calendar_jan:
        pause 2.0
        cal_sheet_left
    with Dissolve(2.0)

    $ renpy.pause(7.0)

    scene anim prolog_1
    show bkrr_calendar:
        truecenter
    show bkrr_calendar_nov:
        pause 2.8
        cal_sheet_left
    show bkrr_calendar_oct:
        pause 2.6
        cal_sheet_right
    show bkrr_calendar_sep:
        pause 2.4
        cal_sheet_left
    show bkrr_calendar_aug:
        pause 2.2
        cal_sheet_right
    show bkrr_calendar_jul:
        pause 2.0
        cal_sheet_left
    show bkrr_calendar_jun:
        pause 1.75
        cal_sheet_right
    show bkrr_calendar_may:
        pause 1.5
        cal_sheet_left
    show bkrr_calendar_apr:
        pause 1.25
        cal_sheet_right
    show bkrr_calendar_mar:
        pause 1.0
        cal_sheet_left
    show bkrr_calendar_feb:
        pause 0.75
        cal_sheet_right
    show bkrr_calendar_jan:
        pause 0.5
        cal_sheet_left
    with dissolve

    $ renpy.pause(2.0)

    scene anim prolog_1
    show bkrr_calendar:
        truecenter
    show bkrr_calendar_dec15
    show bkrr_calendar_nov:
        pause 1.8
        cal_sheet_left
    show bkrr_calendar_oct:
        pause 1.65
        cal_sheet_cright
    show bkrr_calendar_sep:
        pause 1.5
        cal_sheet_cleft
    show bkrr_calendar_aug:
        pause 1.35
        cal_sheet_right
    show bkrr_calendar_jul:
        pause 1.2
        cal_sheet_left
    show bkrr_calendar_jun:
        pause 1.05
        cal_sheet_right
    show bkrr_calendar_may:
        pause 0.9
        cal_sheet_left
    show bkrr_calendar_apr:
        pause 0.75
        cal_sheet_right
    show bkrr_calendar_mar:
        pause 0.6
        cal_sheet_left
    show bkrr_calendar_feb:
        pause 0.45
        cal_sheet_cright
    show bkrr_calendar_jan:
        pause 0.3
        cal_sheet_cleft
    show bkrr_calendar_dec8:
        pause 0.15
        cal_sheet_right
    with dissolve

    $ renpy.pause(1.5)

    scene anim prolog_1 with Dissolve(2.0)

    $ bkrr_set_mode(nvl)

    $ renpy.pause(1.0)

    nvl show dissolve

    "Никто не может упрекнуть меня в том, что я не пытался."
    "Остались позади долгие пешие прогулки, когда я часами бродил по улицам родного города, вглядываясь в лица прохожих."
    "Сошли на нет бесконечные поиски её имени в соцсетях."
    "Я больше не проводил ночи напролёт на музыкальных форумах, просматривая сотни фотографий и проверяя состав любых, даже самых мелких, уровня школы или универа, музыкальных групп… В поисках знакомого лица или хотя бы имени. {w}Увы, моё умение играть на бас-гитаре осталось там, во сне, но умение общаться и заводить знакомых никуда не делось."
    "Многие считали меня чудаком или безобидным сумасшедшим. {w}Но иногда, под настроение, обычно под алкогольными парами, знакомые музыканты искренне пытались помочь мне отыскать «девушку с восточной внешностью, умеющую играть на чём угодно». {w}Мне давали имена, адреса, телефоны… {w}\nДевушек, подходящих под описание, хватало."
    "Многие из них были очень симпатичными, кое-кому я нравился, но у всех у них был один недостаток. {w}Незначительный, в общем-то, но критичный для меня."
    "Ни одна из них не была Мику."
    "Девушка из сна, которую я любил… Она стала моей мечтой, недостижимым идеалом. Моей манией."

    nvl clear

    "Конечно, хороший психолог уложил бы меня на кушетку и как дважды два рассказал бы, что никакой Мику нет и не было.{w} Он бы убедил меня, что я придумал себе идеальный образ, влюбился в него, что пора бы уже перестать думать о глупостях."
    "Что мне стоит проанализировать свою историю: ну разве бывает так, что люди попадают в прошлое, меняют возраст, а потом возвращаются обратно, забыв всё, чему научились."
    "И что этим я себе что-то компенсирую, а моя фантазия ищет выхода в такой форме, и лучше бы мне…"
    "И он дал бы совет, как побыстрее забыть этот сон.{w} Наверняка, очень хороший и действенный совет, как стать нормальным."
    "Но я не хотел становиться нормальным."
    "Я хотел снова увидеть её."

    nvl hide dissolve

    scene bg semen_room_window with fade3

    play ambience ambience_cold_wind_loop fadein 3

    $ bkrr_set_mode()

    window show

    "Обычно ищущий сужает круги. Я их расширял."
    "Сперва искал в городе, потом в области. Потом в соседних, некогда братских республиках, а сейчас – независимых государствах."
    "Иногда, очень редко, мне казалось, что я её вижу."
    "То в проносящемся навстречу троллейбусе, то на противоположной стороне улицы, а иногда – где-то на самом краю кадра в городских новостях."
    "Но это всегда оказывался кто-то другой."

    window hide

    stop ambience fadeout 3
    stop music fadeout 7

    scene bg semen_room_clean_bkrr with fade3

    play sound_loop sfx_street_traffic_outside fadein 5

    window show

    "В бесконечных поисках я сам не заметил, как прошло почти три года с того дня, когда я вышел из дома, чтобы ехать на встречу институтских друзей."
    "Я потихоньку свыкся с мыслью, что не стану кинозвездой, политиком или бизнесменом, но в целом жизнь меня устраивала."
    "«Совёнок» всё-таки изменил меня. Люди вырастают и оставляют позади подростков, которыми они когда-то были, но я привёз из этого странного лагеря умение заводить друзей и стремиться к цели. Не самый худший багаж."
    "Родители были очень рады произошедшим со мной переменам. Ещё бы: сын, на котором можно было ставить крест, взялся за ум. Пошёл на работу, привёл в порядок квартиру, ещё бы невесту хорошую нашёл…"
    "Но с последним пунктом не задалось. Я так и не смог снова влюбиться."
    "Наверное, потому, что я подсознательно сравнивал всех с Ней."
    "И сравнение, увы, было не в их пользу."
    "Наверное, пришла пора прекращать мечтать о несбыточном, спускаться на землю и думать о будущем."
    "Кот – это, конечно, хорошо, но всё чаще я ловил себя на том, что хочется, чтобы кто-то ещё встречал меня дома и радовался моему приходу."
    "Именно такие мысли одолевали меня, когда я читал газету в тихий зимний день."

    play sound_loop2 bkrr_sfx_list["purr_loop"] fadein 5

    "Отпуск зимой – не весело, но всё-таки отдых."
    "Выросший до неприличных размеров Пират уютно урчал у меня на коленях, согревая их. На столе исходила паром чашка отличного чая, и впереди оставалось целых четыре дня полной свободы."
    "По радио в очередной раз звучала реклама вечера джаза в клубе неподалёку.{w} А что? Не худший способ провести вечер. Если, конечно, я заставлю себя выйти из тёплой квартиры на мороз."

    play sound sfx_door_bell
    stop sound_loop2 fadeout 1

    "Идиллию прервал звонок в дверь."

    play sound2 bkrr_sfx_list["meow1"] fadein 3

    "Я согнал кота с рук и пошёл открывать."

    window hide

    play sound sfx_lock_open

    $ renpy.pause(1.0)

    play sound sfx_open_dooor_campus_2

    $ renpy.pause(1.5)

    show sta surp outside at center with dissolve

    play music bkrr_music_list["hide_and_seek"] fadein 5

    window show

    sta "Дядя Семён, привет!"
    "На пороге стояла моя племянница. Сводная сестра и её муж частенько просили меня посидеть с ней."
    "Я не отказывался, она чем-то напоминала мне Ульяну, хотя разрушений от неё было куда меньше."

    window hide
    scene bg semen_room_clean_bkrr
    show sta smile inside at cright
    with fade2
    window show

    sta "Дядя Семён, а какие у тебя планы на вечер?"

    window show

    me "Самое лучшее в отпуске – это никаких планов.{w} А что ты хотела? Опять на каток?"
    "Племяшка села на диван и, болтая ногами, начала рассказывать."

    show sta normal inside at cright with dspr

    sta "Не-е-е! Тут такое дело. Папа с мамой заняты, они на сутках, а кому-то надо на родительское собрание сходить. {w}Можешь выручить?"
    me "Ага. Заняты, говоришь? И это никак не связано с тем, что кто-то написал баллончиком «Оксана – дура» на стене школы, да? Да и в табеле у тебя не фонтан. Куда только родители смотрят? Может, им звякнуть? Приставку отберут на недельку, интернета лишат…"

    show sta sad inside at cright with dspr

    "Племяшка пожала плечами и фыркнула."

    show sta dontlike inside at cright with dspr

    sta "Дядя Семён, ты сейчас нудишь, прямо как моя бабушка. Я думала, что на тебя можно положиться, а ты вот какой."
    me "Ладно, прикрою тебя перед родителями. Для чего ещё существуют дяди. Когда оно?"

    show sta surp inside at cright with dspr

    sta "Через час."
    "Я глянул в зеркало. Моя пятидневная небритость уже заслужила право называться щетиной, но в целом можно показаться на люди…"
    me "Ты бы ещё позже сказала. Чего тянула до последнего?"

    show sta normal inside at cright with dspr

    sta "Да я это… пешком пройтись решила. Но мы же успеем?"

    window hide

    hide sta with dissolve

    $ renpy.pause(1.0, hard=True)

    window show

    "Быстро приведя себя в порядок, я повязал галстук и остался доволен результатом."
    "Удивительно полезный кусок материи. Без него – холостяцкая щетина. С ним – стильная небритость."

    show sta normal outside at cright with dissolve

    me "Успеем."

    window hide

    show sta surp outside at cright with dspr

    $ renpy.pause(1.0, hard=True)

    stop music fadeout 3

    stop sound_loop fadeout 3

    play ambience sfx_bus_interior_moving fadein 3
    scene bg intro_xx with fade3
    stop ambience fadeout 3
    $ renpy.pause(1.0, hard=True)
    scene bg ext_street_night
    show bkrr_traffic_light
    show snow
    with fade2
    $ renpy.pause(1.0, hard=True)
    play sound_loop ambience_medium_crowd_indoors_1 fadein 3
    scene bg int_school_night with fade2

    $ renpy.pause(1.0, hard=True)

    $ bkrr_set_mode(nvl)

    $ bkrr_set_time("prologue", "day")

    nvl show dissolve

    "Я думал, что глухая тоска по затерянному во времени лагерю осталась в прошлом, но, войдя в класс и ощутив смесь запахов лакированного дерева, бумаги и меловой пыли, я понял: ничего не забыто, просто задвинуто на задворки памяти. {w}На время."
    "Мне вдруг страшно захотелось снова обнять Мику, услышать дружескую перебранку Алисы с Ульяной и ощутить в своих руках потёртую бас-гитару."
    "Классная руководительница тем временем долго и нудно рассказывала об успеваемости учеников, планах на ближайший месяц, сборах денег на ремонт и прочих деталях, а я изо всех сил старался не думать о том лете."
    "Я ухитрился дослушать её до конца, записать в блокнот то, что нужно было запомнить и передать сестре, и даже кивнуть, когда учитель спросила меня, придут ли родители Стаси на следующее собрание."

    nvl clear

    nvl hide dissolve

    $ renpy.pause(1.0, hard=True)

    $ bkrr_set_mode()

    window show

    "Племяшка ждала меня в коридоре."

    show sta normal inside at cright with dissolve

    sta "Наконец-то. Долго вы сегодня!"

    show sta sad inside at cright with dspr

    sta "Слушай, а чего у тебя лицо такое… {w}Странное. {w}Что, меня ругали?"

    me "Нет, просто задумался.{w} Не волнуйся, про тебя не вспоминали, я записал всё, что нужно передать родителям."

    show sta smile inside at cright with dspr

    sta "Спасибо большое, ты меня просто спас! Хочешь, обратно на такси подъедем? Я плачу!"
    me "Да брось ты, хорош дядя, который будет лишать племянницу карманных денег."
    sta "Тогда пополам!"

    hide sta with dissolve

    "Перспектива доехать до дома, не толкаясь в вечернем троллейбусе, мне понравилась."
    me "Годится. Сейчас вызовем…"
    "Я достал телефон и принялся вспоминать номер службы такси."
    th "Как же она называлась? Сонет – не сонет, аккорд не аккорд… Что-то музыкальное."

    window hide
    $ renpy.pause(1.0, hard=True)
    $ bkrr_set_volume("music", 0.2)
    stop sound_loop fadeout 15
    play music bkrr_music_list["sd"] fadein 10
    window show

    th "А почему я подумал именно про музыку?"
    "Где-то на краю сознания я понял, что музыка действительно звучит в школьном коридоре. {w}Та самая, из моего сна. {w}Мику играла её для меня, в день когда мы…"

    window hide

    $ renpy.pause(1.0, hard=True)

    window show

    "Когда всё началось."
    "Несколько секунд во мне боролись желание найти невидимого пианиста и страх, что мелодия просто мне почудилась."

    show sta normal inside at cleft with dissolve

    me "Стася, посиди тут. Я сейчас."
    sta "Ладно…"

    show sta surp inside at cleft with dspr

    sta "Ой, Ромка, ты тоже здесь?"

    window hide

    hide sta with easeoutleft

    window show

    "Она отбежала к однокласснику, а я, прислушиваясь, отправился на поиски источника музыки."
    "Я не слышал её три года, с тех самых пор, как вернулся из лагеря… Или проснулся, решив, что был там. {w}И вот она снова звучит. {w}Пусть не на гитаре, а на пианино, но хотя бы спрошу, как она называется…"

    $ bkrr_set_volume("music", 0.4, 3.0)

    "Я прошёлся по коридору в поисках двери, за которой сидел таинственный пианист."
    "Нужная дверь отыскалась быстро. Это был музыкальный класс."
    th "А чего я ожидал? Где ещё в школе может стоять рояль?"
    "Я осторожно постучался. Хорош буду, если вломлюсь в класс посреди урока и начну расспрашивать про название мелодии."

    play sound sfx_knocking_door_outside fadein 2

    "Я постучал, но никто не ответил. Кольнуло сомнение:"
    th "А вдруг играет какое-нибудь забытое радио…"

    play sound sfx_knocking_door_outside fadein 1

    "Но звук был слишком сочным и живым. {w}Я постучал ещё и ещё, а потом набрался наглости и вошёл без разрешения."

    play sound sfx_door_squeak_light fadein 1
    $ bkrr_set_volume("music", 0.6, 0.5)

    me "Извините, можно?"

    window hide

    play sound2 bkrr_sfx_list["whiteout2"]

    scene cg ep_mi with bkrr_fade(2.5)

    window show

    "За роялем сидела молодая женщина. Я видел только её спину, но почему-то сразу решил, что она молодая… И симпатичная."
    me "Я стучал, но никто не ответил…"
    "Пианистка не повернулась, только громко, перекрикивая свою же музыку, ответила:"

    $ bkrr_set_name("mi", "Девушка")

    mi "Да-да, заходите, я задумалась. Извините. Здравствуйте! Вы кого-то ищете? Занятия уже закончились!"
    me "Добрый день. Я услышал музыку… {w} И хотел спросить, как она называется. Очень знакомо звучит, а вспомнить не могу."
    th "Похоже на неумелый подкат. Сейчас она фыркнет и попросит закрыть дверь с той стороны."
    "Но вместо этого моя собеседница прекратила играть и повернулась ко мне."

    window hide

    play sound bkrr_sfx_list["whiteout1"] fadein 1
    scene bg int_classroom_night
    show mii surp inside far at cleft
    with bkrr_fade(2.0)

    window show

    "И посмотрела на меня до боли знакомыми глазами неуловимого сине-зелёного оттенка."
    "Конечно, со стороны это выглядело странно: вваливается незнакомец, задаёт странные вопросы, а потом и вовсе молчит, глупо хлопая глазами…"
    "Я очень хотел и очень боялся поверить в то, что вижу."
    "Но она действительно была передо мной. Живая и настоящая."
    "Конечно, она не бросилась мне на шею с криком «Как долго я тебя ждала! Где ты пропадал?»"
    "Кажется, она меня не узнала…{w} Если вообще когда-нибудь видела."
    "Но это была она. Не могла не быть."

    "Девушка нарушила молчание первой."

    show mii normal inside far at cleft with dspr

    mi "Она пока никак не называется. Я сама её сочинила и ещё только думаю над названием.{w} Знаете, ведь название – это половина смысла для мелодии. У меня очень много идей, но там точно будет слово «ожидание».{w} А может, подберу что-нибудь на японском…"
    "Она сделала паузу, затем добавила:"
    mi "И раз вы – мой первый слушатель, то скажите, пожалуйста, вам нравится?"
    me "Очень! А я думал… Что она из какого-то детского фильма. {w}Почему-то сразу подумал о пионерах."

    window hide

    show mii surp inside far at cleft with dspr

    $ renpy.pause(1.0, hard=True)

    show mii laugh inside far at cleft with dspr

    window show

    "Несколько секунд она молча смотрела на меня, потом засмеялась."
    mi "Да. Забавно, что вы тоже так решили. Когда-то мне приснился сон про пионерский лагерь, и я написала её под впечатлением.{w} Надеюсь, это не плагиат на какую-то старую песню? Бывают же совпадения, правда? Наверное, просто немного похожа на какую-то музыку из кино."
    "Она помолчала, потом почему-то добавила:"

    show mii normal inside far at cleft with dspr

    mi "Я здесь преподаю музыку. А у вас здесь…{w} кто-то учится?"

    window hide

    $ renpy.pause(1.0, hard=True)

    window show

    "По коридору раздались лёгкие шаги. Стася устала меня ждать и отправилась на поиски."
    th "Не хватало, чтобы она решила, будто она моя дочь."
    "Я машинально глянул на её руки и облегчённо выдохнул. {w}Обручального кольца не было видно."
    "Конечно, это ещё ничего не значит, но…"

    show sta normal inside  at right with easeinright

    sta "Дядь Семён, я тут Ромку встретила с родителями. Они меня подвезут, ты доберешься домой один?"

    show sta surp inside at right with dspr

    sta "Здрасьте, Мария Николаевна!"

    $ bkrr_set_name("mi", "Мария")

    show mii smile inside far at cleft
    show sta smile inside at right
    with dspr

    mi "Точно, как же я не догадалась. Вы с ней очень похожи."
    "Я поспешил уточнить:"
    me "Моя племянница. Я на родительском собрании был…"
    "Стася подёргала мой рукав."
    sta "Так я поеду с ними?"
    me "Давай! Родителям привет. Позвони, как приедешь, ладно?"

    show sta normal inside at right with dspr

    sta "Хорошо!"

    hide sta with easeoutright

    "Стася развернулась и умчалась по коридору.{w} Её появление почему-то разрядило обстановку. Во всяком случае, я слегка расслабился и даже присел на край парты."

    show mii surp inside far at cleft with dspr

    "Девушка бросила взгляд на часы и удивлённо ахнула."
    mi "Надо же, сколько времени. Хорошо, что вы пришли, иначе я бы сидела бы до ночи, с меня станется.{w} Музыка так увлекает, я перестаю следить за временем. С вами когда-нибудь так бывало?"
    me "Да, иногда случается."

    window hide

    show mii smile inside far at cleft with dspr
    $ renpy.pause(0.5, hard=True)
    hide mii with dissolve

    window show

    "А дальше всё случилось само собой.{w} Я помог ей надеть пальто, потом держал сумку, пока Мику…{w} Нет. Мария. Пока она возилась с ключами, а затем предложил провести её до остановки, на что моя новая знакомая с удовольствием согласилась."

    window hide

    stop ambience fadeout 3

    stop music fadeout 5

    scene bg ext_street_night
    show bkrr_traffic_light
    show snow
    with fade3

    $ bkrr_set_time("prologue")
    $ bkrr_set_volume("sound", 0.5)
    $ bkrr_set_volume("sound_loop", 0.1)
    $ bkrr_set_volume("sound_loop2", 0.3)

    play ambience ambience_cold_wind_loop fadein 3
    play sound_loop bkrr_sfx_list["traffic_outside"] fadein 3

    window show

    "По дороге мы беседовали о всякой ерунде.{w} Расстояние до остановки стремительно сокращалось, а я всё не мог заставить себя сделать следующий шаг и…{w} спросить."
    "Казалось бы, чего проще.{w} Но после всех этих поисков я боялся ошибиться и принять желаемое за действительное…"
    "Боялся ошибиться.{w} Снова."

    show mii normal outside close at cleft with dissolve

    mi "… пытаюсь научить ценить хорошую музыку. Конечно, смешно ждать, что они станут слушать рокабилли или блюзы, но этот их сделанный на коленке дабстеп, это грустно.{w} Я не осуждаю, ведь когда-то и джаз считали бунтарским стилем-однодневкой, но всё-таки это была музыка… с ритмом и мелодией…"

    "Я слушал её голос, поскрипывание снега под ногами и боялся поверить, что это наяву.{w} А еще – лихорадочно пытался понять, что же делать дальше."
    "Хотя, «что делать» было как раз понятно.{w} Каким то шестым чувством я понимал, что нельзя дать ей уйти, иначе я уже не наберусь смелости вот так прийти к ней в школу."

    show mii surp outside close at cleft with dspr

    mi "Ой, я вас не заболтала? Мне часто говорят, что я слишком разговорчивая. И на родине, до переезда сюда, и здесь…{w} Я потом вам расскажу, наверное, уже надоела разговорами, да?"
    me "Нет-нет, совсем наоборот."

    show mii smile outside close at cleft
    with dspr

    mi "Тогда хорошо."
    "Она улыбнулась… той самой улыбкой…"
    "Я думал, что уже разучился волноваться, как мальчишка, но сейчас воспоминания, казалось бы, надежно упрятанные в дальний уголок памяти, снова вырвались наружу."

    show bkrr_snow_layer3_anim behind mii:
        alpha 0.0
        ease 4.0 alpha 1.0
    show bkrr_snow_layer2_anim behind mii:
        alpha 0.0
        ease 7.0 alpha 1.0
    show bkrr_snow_layer1_anim behind mii:
        alpha 0.0
        ease 8.0 alpha 1.0
    show bkrr_snow_layer0_anim:
        alpha 0.0
        ease 9.0 alpha 1.0
    show snow:
        ease 6.0 alpha 0.0
    show mii_snow_close at cleft:
        alpha 0.0
        pause 2.0
        ease 20.0 alpha 0.8

    "Словно и не было этих месяцев, полных одиночества, безуспешных поисков и попыток забыть обо всём, что было {b}там{/b}."

    show mii surp outside close with dspr

    mi "Ой, снег пошел… Надо же..? "
    hide snow

    me "Здорово… Люблю снегопад."

    show mii smile outside close with dspr

    mi "Там, откуда я приехала, снег редко идёт…{w} Только в феврале и то не каждый год."

    $ bkrr_set_volume("sound", 0.2, 5.0)
    play sound bkrr_sfx_list["bus_arriving"] fadein 1
    play sound_loop2 bkrr_sfx_list["bus_idle"] fadein 15
    show mii surp outside close at cleft with dspr

    mi "Как раз мой автобус. Спасибо, что проводили. Я побежала!"

    window hide
    show mii smile outside close at cleft with dspr
    $ renpy.pause(0.5, hard=True)
    hide mii
    hide mii_snow_close
    with dissolve
    window show

    "Она улыбнулась, и поспешила к остановке."

    "А я стоял и боролся с отказавшим вдруг языком, пытаясь сказать хоть что-то…"

    "Моя спутница успела сделать несколько шагов, когда я смог выговорить…"
    "Даже, скорее, выдохнуть.{w} Одно единственное слово."

    play music music_list["everlasting_summer"] fadein 2

    me "Мику?"

    window hide
    $ renpy.pause(1.0, hard=True)
    show mii surp outside snow far at cleft behind bkrr_snow_layer1_anim with dissolve
    window show

    "Вздрогнула и остановилась.{w} Её сумка упала в снег, но хозяйка не обратила на это внимания."
    "Я не знал, что сказать, поэтому просто повторил, уже нормальным голосом:"
    me "Мику? Это…{w} Ведь это ты?"

    window hide
    $ renpy.pause(2.0, hard=True)
    show mii cry_smile outside snow far at cleft with dissolve
    $ renpy.pause(1.0, hard=True)
    window show

    "Она не ответила."
    "Не знаю, кто из нас сделал первый шаг…"

    window hide
    hide mii with dissolve
    scene bkrr_ep_ending_bg:
        yalign 1.0
    show bkrr_snow_layer3_anim
    show bkrr_ep_ending
    show bkrr_snow_layer2_anim
    show bkrr_snow_layer1_anim
    show bkrr_snow_layer0_anim
    with Dissolve(2.0)
    window show

    "Но секунду спустя Мику… Мария…{w} Кем бы она ни была, уже прижималась ко мне и, всхлипывая, шептала, как боялась ошибиться, как не могла понять – я ли это, и как ей было страшно, вдруг я её не узнаю…"

    $ bkrr_set_volume("sound", 0.2)
    stop sound_loop2 fadeout 3
    play sound bkrr_sfx_list["bus_leaving"] fadein 3

    "Водитель пустующего автобуса явно решил, что не стоит ждать эту ненормальную пару, и тронулся без нас."

    stop sound fadeout 3
    stop ambience fadeout 10
    stop sound_loop fadeout 3

    "Я покрепче прижал Мику к себе и теперь глупо улыбался, стараясь не сойти с ума от переполнявших меня чувств."
    "Трудно было поверить, что мои безнадёжные поиски были не зря, и что всё это не сон, что всё это взаправду."
    "Но Мику в моих руках была живой и настоящей."

    $ bkrr_set_name("mi", "Мику")

    mi "Ты…{w} ведь никуда больше не исчезнешь?"
    me "Никуда!"
    "Она затихла и теперь молча обнимала меня, словно боясь, что я пропаду, стоит ей разжать руки."
    "Снег пошел сильнее, как будто хотел скрыть нас от нескромных глаз и дать возможность побыть вдвоём."

    window hide
    scene bkrr_ep_ending_bg:
        subpixel True
        yalign 1.0
        ease 10.0 yalign 0.0
    show bkrr_snow_layer3_anim_quick:
        ease 7.0 alpha 0.0
    show bkrr_ep_ending:
        subpixel True
        ease 5.5 ypos 1.0
    show bkrr_snow_layer2_anim_quick:
        ease 7.0 alpha 0.0
    show bkrr_snow_layer1_anim_quick:
        ease 7.0 alpha 0.0
    show bkrr_snow_layer0_anim_quick:
        ease 7.0 alpha 0.0
    with dissolve

    $ renpy.pause(10.5, hard=True)
    scene stars:
        subpixel True
        truecenter
        pause 0.5
        ease 15.0 zoom 1.4 rotate 7.5
        ease 40.0 zoom 1.8 rotate -30
    with dissolve

    $ renpy.pause(1.0, hard=True)

    show epilogue_falling_star_tail2:
        truecenter
        pos (0.4, 0.6)
        ease 4.5 alpha 0.0
    show epilogue_falling_star_tail1:
        truecenter
        pos (0.4, 0.6)
        ease 2.5 alpha 0.0
    show epilogue_falling_star_star:
        truecenter
        pos (0.38, 0.615)
        ease 7.0 alpha 0.0
    with bkrr_star_falling_transition

    window show

    "Что-то заканчивалось…"
    "Что-то начиналось."

    window hide
    scene black with Dissolve(10)

    stop music fadeout 10
    $ renpy.pause(12, hard=True)

    $ persistent.bkrr_check["credits4"] = True

    jump bkrr_credits

label bkrr_credits:

    stop ambience fadeout 3
    stop sound_loop fadeout 3

    $ renpy.movie_cutscene(bkrr_video_list["credits"], delay=193.0)

    $ bkrr_set_name("mi", "Мику")
    $ bkrr_set_volume("sound", 1.0)
    $ bkrr_set_volume("sound_loop", 1.0)
    $ bkrr_set_volume("sound_loop2", 1.0)

    jump bkrr
