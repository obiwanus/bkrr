
#    Булки, кефир и рок-н-ролл. Пролог    #

label bkrr_prologue:

    $ bkrr_new_chapter("Пролог")

    scene black

    $ bkrr_set_time("sunset")

    play music music_list["afterword"] fadein 2.5

    show bkrr_service bkrr_title_message:
        truecenter
        subpixel True
        linear 8.0 zoom 1.5
    with bkrr_blindstoright_transition

    $ renpy.pause(5.0)

    hide bkrr_service with bkrr_blindstoleft_transition

    $ renpy.pause(1.0, hard=True)

    scene expression bkrr_make_sepia_img("bg int_musclub_day")
    show mi normal pioneer sepia at center
    with bkrr_blindstoleft_transition

    $ bkrr_set_name("mi", "Пионерка")

    play ambience ambience_music_club_day fadein 3

    window show

    mi_r "Вижу, у тебя обходной. Новенький?"
    me "Да."

    show mi smile pioneer sepia at center with dspr

    mi_r "Меня Мику зовут."

    $ bkrr_set_name("mi", "Мику")

    mi_r "Нет, честно-честно! Никто не верит, а меня правда так зовут. Просто у меня мама из Японии."

    window hide

    $ renpy.pause(0.25, hard=True)

    $ bkrr_set_mode(nvl)

    nvl show dissolve

    "Всего-то и надо было: дать этой миловидной пионерке с экзотическим именем бумажку, получить подпись и бежать себе дальше. {w}Но стоило мне увидеть её…"

    nvl hide dissolve

    scene expression bkrr_make_sepia_img("cg d2_miku_piano2") with bkrr_blindstoleft_transition

    $ bkrr_set_mode()

    window show

    th "Да нет! Я не про это!"

    window hide

    $ renpy.pause(0.25, hard=True)

    $ bkrr_set_mode(nvl)

    nvl show dissolve

    "Дело было совсем не в зелёных и белых полосочках. {w}Просто веяло от неё чем-то таким мило-неуклюжим и жизнерадостным одновременно. {w}Почему-то расхотелось уходить."
    "Поводов задержаться вроде и не было, но тут…"

    nvl hide dissolve

    scene expression bkrr_make_sepia_img("bg int_musclub_day")
    show mi normal pioneer sepia at center
    with bkrr_blindstoright_transition

    $ bkrr_set_mode()

    window show

    mi_r "Ты на чём-нибудь играть умеешь?"

    hide mi with dissolve

    "С самодовольной рожей я подошёл к стоящей в уголке гитаре, украшенной чернильным клеймом «инв. №123895, «Совёнок» и, призвав все свои таланты, сыграл нехитрую мелодию."
    "Когда-то я пробовал научиться, выучил несколько аккордов, но, как и многое другое, забросил, не прозанимавшись и года. {w}Это была единственная мелодия, которую я знал, зато после бесконечных повторений она выходила хорошо."
    "Дослушав, Мику кивнула."

    show mi smile pioneer sepia at center with dissolve

    mi_r "Ну… неплохо! Нет, правда неплохо!"
    mi_r "А ещё что-нибудь умеешь?"
    me "Боюсь, нет. Я и это еле-еле вспомнил."
    me "Ну, я пойду? Бегунок подпишешь? А то ещё надо обежать медпункт, библиотеку, клубы эти."
    mi_r "Ну, что за вопрос, конечно же, подпишу. {w}Давай его сюда."

    show mi normal pioneer sepia at center with dspr

    mi_r "Сейчас, я только на бумажке попробую подпись… Я вообще редко расписываюсь. Знаешь, в Японии не подписи ставят, а именные печати. Кругленькие такие, красные. Я такую и себе хотела сделать, но папа сказал, что надо привыкать к традициям страны, где живёшь, а у вас принято подпись ручкой ставить. А жалко, по-моему, красиво."
    mi_r "Вот. Ну, держи свой обходной!"
    me "Спасибо!"
    th "Интересно, она всегда так много говорит? Обычно я быстро устаю от таких вот, разговорчивых, но почему-то сейчас слушал с удовольствием."
    "Мику протянула мне листок, потом добавила:"
    mi_r "Пожалуйста! И смотри, Ульяне в руки его не давай, а лучше – вообще не показывай."

    show mi sad pioneer sepia at center with dspr

    mi_r "А то я в первый день не подписала, так она мне туда добавила столовую, баню и спортзал. Представляешь, я в столовую пришла, а повариха на меня смотрит, как на дурочку. И подписывать ничего не хочет, только смеётся!"
    mi_r "Я так расстроилась, думала, бегунок не заполню. А уж когда в баню за подписью пошла…"
    "Мику замолчала и  вздохнула, видимо, вспомнив свои приключения."
    "Я был не прочь посидеть с ней ещё, но нужно было обойти остальные места."
    me "Спасибо. Ну, я пойду?"

    show mi normal pioneer sepia at center with dspr

    mi_r "Иди! Только приходи ещё, ладно? Мне здесь скучно одной."
    me "Хорошо."
    mi_r "Смотри, я  буду ждать!"

    window hide

    stop ambience fadeout 1

    scene expression bkrr_make_sepia_img("bg ext_music_club_verandah_day_v1") with bkrr_blindstoleft_transition

    play ambience ambience_camp_center_day fadein 3

    $ renpy.pause(1.0, hard=True)

    show dv normal pioneer2 sepia at left
    show us grin pioneer sepia at right
    with dissolve

    window show

    us_r "Сенька, привет!"
    me "Здорово."
    dv_r "Здоровей видали. Чего приходил?"
    me "Подписать бегунок."
    dv_r "Подписал?"
    me "Да!"
    dv_r "Свободен."

    window hide

    hide dv
    hide us
    with dissolve

    scene expression bkrr_make_sepia_img("bg ext_music_club_day_bkrr") with bkrr_blindstoleft_transition

    window show

    "Уходя, я услышал обрывки разговора:"

    stop music fadeout 10

    us_r "Чего ты на него так…"
    dv_r "Потому что!"
    us_r "Может, он тебе нра… {w}Ай! Чего дерёшься?"
    dv_r "Будешь болтать глупости – ещё стукну!"
    us_r "Ой-ой, какие мы обидчивые."
    "Девчонки прошли в клуб и скрылись в нём."

    window hide

    stop ambience fadeout 5

    scene bg ext_music_club_day_bkrr with Dissolve(5.0)

    # $ bkrr_get_achievement("start")
    # ачивка для первого эпизода (если очень хочешь собрать все ачивки – раскомментируй строку выше)

    $ persistent.bkrr_check[4] = True

    jump bkrr_opening

#    Булки, кефир и рок-н-ролл. Опенинг    #

label bkrr_opening:

    scene black with fade3

    $ renpy.movie_cutscene(bkrr_video_list["intro"], delay = 39.0)

    scene black

    jump bkrr_day4_start
