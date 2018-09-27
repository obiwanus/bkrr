
#    Булки, кефир и рок-н-ролл. День 6    #

label bkrr_day6_start:

    $ bkrr_new_chapter(6)

    jump bkrr_day6_common

label bkrr_day6_common:

    scene expression bkrr_awakening_atl("bg int_house_of_mt_day")
    show unblink
    with None

    $ bkrr_set_time()

    play music music_list["my_daily_life"] fadein 3

    play ambience ambience_int_cabin_day fadein 5

    $ renpy.pause(5.0, hard=True)

    window show

    "Для разнообразия сегодня я проснулся первым."
    "Ольга всё ещё спала, негромко бормоча что-то сквозь сон. {w}Загорелая ножка выглядывала из-под одеяла и наводила меня на совсем не пионерские мысли."
    th "Раз уж она так заботилась обо мне – кормёжка, одёжка, мыло с порошком, надо и мне сделать ей что-нибудь приятное."
    th "Чем там вообще принято радовать женщин по утрам?"
    "Я смог вспомнить только нежный поцелуй и кофе в постель."
    "Я представил себе, как цел{b}у{/b}ю вожатую."

    window hide

    show blink

    $ renpy.pause(1.0, hard=True)

    stop ambience

    stop music

    play sound bkrr_sfx_list["kiss"]

    $ renpy.pause(2.5, hard=True)

    scene bg int_house_of_mt_day
    show mt angry nightdress close at center
    show prologue_dream:
        alpha 0.25
    with bkrr_fade(0.5)

    play ambience ambience_int_cabin_day

    play music music_list["drown"] fadein 3

    window show

    mt "Cемён! Ты что творишь? Всё! На улице будешь теперь ночевать!"

    window hide

    stop ambience

    play sound bkrr_sfx_list["thunder"]

    play ambience bkrr_ambience_list["rain_outside"]

    scene bg ext_house_of_mt_night_without_light_rainy_bkrr
    show bkrr_eff_rain_r
    show mi sad wet pioneer at center
    show prologue_dream:
        alpha 0.25
    with bkrr_fade(0.5)

    $ bkrr_set_time("night")

    window show

    mi "Что, Семён, на улице ночуешь?"
    mi "Тебя правда из домика выгнали, потому что ты к вожатой приставал? {w}Так тебе и надо!"
    mi "Я думала, что ты хороший, а ты… {w}Разочаровал ты меня! Не подходи ко мне больше никогда!"

    window hide

    stop ambience

    stop music

    play sound bkrr_sfx_list["whiteout2"]

    scene bg int_house_of_mt_day with bkrr_fade(0.5)

    $ bkrr_set_time()

    play music music_list["my_daily_life"] fadein 10

    play ambience ambience_int_cabin_day fadein 5

    window show

    th "Нет, лезть целоваться – это перебор, а вот чашечка кофе будет в самый раз."
    "Я тихо встал и включил электрочайник."
    "Всё-таки жить с вожатой – это не только волнующие картинки по утрам, но и доступ к утюгу, кипятку и прочим радостям цивилизации. {w}Удобно, как ни посмотри."
    "Ожидая, пока вода закипит, я насыпал кофе в чашки, достал блюдце и выложил на него трофейные конфеты."
    "Вспоминая, как Уля вчера отрывала их от сердца, я не смог сдержать улыбку."
    th "Интересно, теперь мы вроде как друзья? {w}К тому же она часто с Мику общается, а значит…"

    window hide

    play sound sfx_angry_ulyana

    $ renpy.pause(1.0, hard=True)

    window show

    "Переливистый свист вырвал меня из раздумий."
    th "Вот ведь растяпа, снять свисток забыл. Сейчас Ольга проснётся и будет ворчать, что помешал ей спать."

    stop sound fadeout 2.5

    "Я торопливо выключил чайник и налил кипяток в чашки. {w}Комната тут же наполнилась бодрящим кофейным запахом."
    "Вожатая во сне вздохнула и заворочалась."
    "До звонка будильника оставалась ещё пара минут. Пожалуй, уже можно. Я поднёс чашку к изголовью кровати и помахал рукой, направляя ароматный пар к лицу вожатой. Вышло прямо, как в рекламе кофе."

    mt "М-м-м…"
    "Ольга открыла глаза и с интересом посмотрела на меня."
    mt "Ко-о-офе… {w}Это сон, да?"
    me "А вот и нет! Всё настоящее! {w}Ну, во всяком случае, пахнет настоящим."
    mt "Семён кофе достал… {w}Я его так люблю!"
    "Она счастливо вздохнула и перекатилась на другой бок."
    "Я решил уточнить:"
    me "Меня или кофе?"
    mt "Кофе, конечно."
    me "Ну, вот… {w}Эх, нет в жизни счастья."
    me "Ладно, давайте, делайте открытие века. А потом второго!"

    play sound bkrr_sfx_list["alarm_clock_hit"]

    "Будильник зажужжал, готовясь зазвенеть, но короткий тычок в кнопку заставил его умолкнуть."

    show mt surprise nightdress at center with dissolve

    mt "Чего? Какое ещё открытие? "

    show mt laugh nightdress at center with dspr

    extend "А, дошло."

    show mt smile nightdress at center with dspr

    mt "Ты откуда кофе-то добыл?"
    me "Места знать надо!"
    mt "Только не говори, что столовую ограбил вчера ночью."
    me "А если и так? Что, вернуть назад?"
    mt "Нет, кофе, я, конечно, не отдам, но мне придётся быть твоей соучастницей! Это не педагогично!"

    show mt sad nightdress at center with dspr

    mt "А ты что, правда стянул?"
    me "Обижаете! Я вам что, Ульяна?"

    show mt normal nightdress at center with dspr

    mt "Тогда откуда?"
    me "Охотничий трофей! {w}Обменял на пять кило жира и меха. Вношу в общий котёл, так сказать."
    mt "На что обменял?"

    hide mt with dissolve

    "Я пересказал ей вчерашнюю историю с котом и поварихами. {w}Отсмеявшись, она одобрительно покивала."

    show mt laugh nightdress at center with dissolve

    mt "Да, вы там не скучали. {w}Говоришь, Наталья просила тебя почаще на картошку посылать?"
    me "Нет! Не надо!"

    show mt smile nightdress at center with dspr

    mt "Ладно, посмотрим. Ох, как вставать-то не хочется!"

    window hide

    hide mt with dissolve

    $ renpy.pause(1.0, hard=True)

    window show

    "Ольга присела в кровати. Покрывало поползло вниз, открывая загорелые плечи с тонкими светлыми полосками от купальника, но {b}самое{/b} интересное, увы, было прикрыто тонкой ночной рубашкой, только пикантная ложбинка приковывала глаза."
    mt "Отвернись, пожалуйста, я оденусь."
    "Я послушно отвернулся, а сзади в очередной раз донеслось волнующее шуршание одежды."
    mt "Можно поворачиваться!"
    "Сейчас, в спортивной одежде Ольге смело можно было дать и восемнадцать. Очень хорошенькая у нас вожатая."
    "Да и вообще, все здесь какие-то слишком красивые. Даже Женя при некоторой неухоженности выглядела милой растрёпой, а не неряхой."
    "Ольга протянула мне банку."

    show mt normal bkrr_sport at center with dissolve

    mt "Может, себе оставишь? С друзьями попьёте?"
    me "Нет-нет! Вы меня бутербродами кормили, одеждой снабжали, плавки даже нашли. Считайте, это моя маленькая благодарность. {w}За спасение от заплыва в розовых плавках в цветочек."

    show mt smile bkrr_sport at center with dspr

    mt "Ну всё, я слабая женщина и не могу больше сопротивляться! Вот тогда моя доля. Бери, угощайся."
    "Из шкафчика появились пакет с печеньем и ещё один, поменьше, с пряниками."
    mt "Из райцентра привезли. Так сладкого захотелось, попросила водителя. Ты, угощайся в любое время."

    hide mt with dissolve

    "Вгрызаясь в большой пряник, я поймал себя на том, что снова получаю удовольствие от мелких радостей жизни. Как в том анекдоте: «а жизнь-то налаживается!»."
    "Столько новых впечатлений, что даже ломки от отсутствия компьютера не ощущается. Поглощённый едой, я не сразу понял, что она только что сказала."

    stop music fadeout 3

    me "Как это, «из райцентра»? А… единственный автобус через неделю?"

    show mt grin bkrr_sport at center with dissolve

    mt "Ну, извини, соврала."
    mt "Машина продуктовая через день ходит, да ты и сам видел, наверное. {w}Просто бывает, что вы ныть начинаете, домой проситься. Вот и говорю, что автобус нескоро. А потом втянетесь – ещё и не выгонишь!"
    me "И что, могу вот так сесть и уехать? В любое время?"

    show mt sad bkrr_sport at center with dspr

    mt "А ты что, всё ещё домой хочешь?"
    th "Не то, чтобы я на самом деле так уж хотел вырваться отсюда. {w}Не сейчас. {w}Место, конечно, очень странное, но уютное. {w}Да и куда я пойду, если действительно провалился в прошлое?"
    me "А если бы захотел, то… ну, можно будет?"

    show mt surprise bkrr_sport at center with dspr

    mt "Ты, кажется, пионерский лагерь спутал с исправительно-трудовым. {w}Можно, конечно."

    show mt normal bkrr_sport at center with dspr

    mt "Ну, если что, завтра садись в автобус и поезжай. {w}В город, пыль глотать да перед телевизором просиживать."
    th "По-моему, она приняла моё нежелание оставаться в лагере близко к сердцу. Ну, да, для неё-то я просто странный и капризный пионер. {w}Или нет?"
    "Вожатая тем временем продолжала:"
    mt "Только реши заранее, я же не могу тебя вот так в чистое поле отправить. Надо оформить по документам."
    th "И здесь бюрократия."
    "Я хмыкнул и принялся застилать постель."

    window hide

    stop ambience fadeout 3

    $ bkrr_timeskip()

    scene bg ext_dining_hall_away_day with bkrr_circleout_transition

    play ambience ambience_camp_center_day fadein 3

    $ renpy.pause(1.0, hard=True)

    window show

    "У входа в столовую о чём-то спорили наши кибернетики."
    sh "А я говорю, деталей не хватит."
    el "Ну и что? Из робота пару резисторов достанем?"
    sh "Да что ж тебе бедный робот сделал? Как чего не хватает, сразу «из робота достанем». Не трогай его, я в другом месте возьму!"
    el "Опять в старый лагерь? {w}Попадёт ведь!"
    sh "Если никто не узнает, то и не попадёт."

    window hide

    scene bg ext_dining_hall_near_day with dissolve

    show sh normal pioneer at left
    show el normal pioneer at right
    with dissolve

    window show

    sh "О! Доброе утро, Семён."
    me "Привет!  Ты… это… ну, извини за вчера."
    el "Семён, привет!"
    el "Вчера?"

    show el upset pioneer at right with dspr

    el "А что было вчера?"

    show sh smile pioneer at left with dspr

    sh "Ничего не было."
    sh "Он… э-э-э… мой шампунь разлил."

    show el smile pioneer at right with dspr

    el "И всего-то? {w}Ну, не переживай, я свой дам. На неделю хватит."
    sh "Спасибо, ты настоящий друг."

    show sh normal pioneer at left with dspr

    sh "Значит, детали я завтра…"

    window hide

    hide sh
    hide el
    with dissolve

    $ renpy.pause(1.0, hard=True)

    window show

    "Они потеряли ко мне интерес и ушли в столовую."
    "Я собрался было зайти следом, но мне преградили путь сразу три симпатичные пионерки."

    window hide

    $ renpy.pause(0.5, hard=True)

    show dv normal pioneer at left
    show us normal pioneer at right
    show mi normal pioneer at center
    with dissolve

    play music music_list["timid_girl"] fadein 3

    window show

    dv "Мику, вот он. Ну, давай!"

    show mi shy pioneer at center with dspr

    mi "Но я…"
    dv "Давай! Он тебе не откажет! {w}Да, Семён?"

    window hide

    show mi shocked pioneer at center:
        ease 0.25 zoom 1.1
        ease 0.5 zoom 1.075

    $ renpy.pause(1.0, hard=True)

    show mi sad_smile pioneer at center:
        zoom 1.075
    with dspr

    show dv smile pioneer at left with dspr

    window show

    "Алиса подтолкнула Мику ко мне и улыбнулась."
    me "Привет! Ничего не обещаю."

    show us dontlike pioneer at right with dspr

    us "Опять он ломается. А может, мы тебя на чай с тортиком позвать хотели!"
    me "А вы хотели?"

    show us normal pioneer at right
    show dv normal pioneer at left
    with dspr

    dv "Нет! Мику, объясни ему."

    show mi smile pioneer at center:
        zoom 1.075
    with dspr

    mi "Ну, нет, у нас тортика нет. А чай есть! Вкусный, с сахаром и с лимончиком! {w}Ну, если ты захочешь конечно."

    show mi happy pioneer at center:
        zoom 1.075
    with dspr

    mi "Ты как любишь, сладкий или не очень? Я вот – сладкий. Только слишком сладкий вредно, мама говорит…"

    window hide

    show mi shocked pioneer at center:
        ease 0.25 zoom 1.15
        ease 0.5 zoom 1.125
    with dspr

    $ renpy.pause(1.0, hard=True)

    show mi shy pioneer at center:
        zoom 1.125
    with dspr

    window show

    "Алиса ещё раз легонько подтолкнула Мику."
    dv "Ближе к теме!"

    show mi sad_smile pioneer at center:
        zoom 1.125
    with dspr

    mi "Понимаешь, вожатая Толика забрала на работы, а мы вчера гитары и усилители в домик Алисы и Ульяны отнесли, чтобы порепетировать. {w}Теперь нужно назад вернуть, а они такие тяжёлые. Ты не мог бы, ну если ничем не занят, помочь нам их назад перенести?"
    mi "А то хочется начать репетицию пораньше, а мы их будем нести в три захода, лишние сорок минут точно потратим. {w}Ну, если тебе не очень тяжело."

    show mi sad pioneer at center:
        zoom 1.125
    with dspr

    mi "Поможешь?"

    show dv grin pioneer at left
    show mi shy pioneer at center:
        zoom 1.125
    with dspr

    dv "Семён, выручай! Один ты у нас мужик остался, остальных разобрали."

    show us smile pioneer at right with dspr

    us "Ты же не допустишь, чтобы хрупкие девочки сами всё тащили?"

    show dv smile pioneer at left with dspr

    me "Хрупкие, говоришь?"

    show us dontlike pioneer at right with dspr

    us "Да ладно тебе к словам-то придираться? {w}Поможешь?"

    show us upset pioneer at right with dspr

    us "Микуська, не молчи!"

    show mi sad_smile pioneer at center:
        zoom 1.125
    with dspr

    mi "Помоги нам, пожалуйста."
    me "Да не вопрос. После завтрака и пойдём."

    window hide

    stop ambience fadeout 2

    stop music fadeout 3

    $ bkrr_timeskip_short()

    scene bg int_dining_hall_people_day with bkrr_timeskip_transition()

    play ambience ambience_dining_hall_full fadein 3

    window show

    "Я неторопливо умял завтрак, отнёс посуду и отправился было к выходу, поджидать трёх интриганок. Перенесу им барахло, а там, глядишь, и до обеда отсижусь, подальше от работы."
    "Но Ольга Дмитриевна заметила меня раньше, и вместе со Славяной они быстро перекрыли мне путь."

    window hide

    play music music_list["always_ready"] fadein 3

    show mt smile pioneer at cleft
    show sl normal pioneer at cright
    with dissolve

    window show

    mt "Семён? Тебя-то я и ищу."

    show sl smile pioneer at cright with dspr

    sl "Доброе утро! Еле тебя поймали."
    me "Привет, Славя! Ну, я особо и не скрывался…"
    "Соврал я."

    show mt grin pioneer at cleft with dspr

    mt "Ну, что ты. Конечно же, нет."

    show mt smile pioneer at cleft with dspr

    mt "У нас тут мужская работа, без тебя никак. {w}Поможешь Славе, хорошо?"
    me "Э… ну, я вообще обещал девчонкам помочь инструмент перенести…"

    show mt normal pioneer at cleft with dspr

    mt "Ну, значит попозже поможешь. А вообще их трое, справятся без тебя. А Славя одна."
    me "Ну, раз так…"
    "«Мужская работа»… мне сразу представились бесконечные ряды каких-нибудь мешков с углём, рытьё траншеи или что-нибудь в том же духе."

    show sl normal pioneer at cright with dspr

    sl "Вот и отлично! Тогда переоденься во что-нибудь, а то испачкаешься, и пойдём."
    th "«Испачкаешься»."
    "Подтверждались мои худшие опасения."
    th "Точно, копать. {w}Или грузить. {w}Или ещё что-нибудь."
    me "А куда?"

    show sl smile pioneer at cright with dspr

    sl "На Кудыкину гору!"

    show sl normal pioneer at cright with dspr

    sl "Вначале – сцену чуть-чуть починим, а потом… {w}Ну, там видно будет. Посмотрим, как управимся."

    window hide

    stop ambience fadeout 1

    stop music fadeout 1

    scene bg ext_house_of_mt_day with fade

    play ambience ambience_camp_center_day fadein 3

    window show

    "Мы подошли к нашему с вожатой домику."

    window hide

    stop ambience fadeout 0.5

    stop music fadeout 0.5

    play sound sfx_open_door_1

    scene bg int_house_of_mt_day with dissolve

    play ambience ambience_int_cabin_day fadein 3

    window show

    "Я быстро посмотрел, что у меня есть немаркого."
    "Вместе с формой Ольга подбросила мне кое-каких вещей, но пары рабочих джинсов среди них, конечно, не нашлось. {w}Придётся ограничиться спортивной формой. В брюках будет жарковато, но работать лучше с закрытыми ногами, мало ли что."
    "Мелькнула мысль покинуть домик через окно и скрыться. {w}Будь на месте Слави кто-то другой, я бы, конечно, так и поступил."

    window hide

    stop ambience fadeout 0.5

    stop music fadeout 0.5

    scene bg ext_house_of_mt_day with dissolve

    play sound sfx_close_door_1

    play ambience ambience_camp_center_day fadein 3

    window show

    me "Я готов!"

    show sl normal pioneer at center with dissolve

    sl "Ну и отлично. Пошли, займёмся делом."
    me "А ты что, переодеваться не будешь?"

    show sl surprise pioneer at center with dspr

    sl "Ой, точно! Совсем забыла."

    show sl shy pioneer at center with dspr

    sl "Я тебя не очень задержу?"
    me "А куда нам спешить…"
    "Вздохнул я."
    me "Сцена никуда не денется."

    show sl laugh pioneer at center with dspr

    sl "Это у тебя учёт в рублях, а у меня – в сутках!"
    me "Ну-ну. Я не в том смысле."

    show sl normal pioneer at center with dspr

    sl "Да я понимаю. Ну, прости, что придётся крюк сделать. {w}Я быстро!"

    window hide

    scene bg ext_house_of_sl_day with fade

    show sl normal pioneer at center with dissolve

    window show

    sl "Одну минутку! Я сейчас! {w}Ты присядь пока."

    window hide

    hide sl with dissolve

    window show

    "Я огляделся."
    "Скамейка под сиренью была как раз на самом солнцепёке, так что садиться на неё не хотелось. {w}Ладно, постою в тени."

    window hide

    $ renpy.pause(1.0, hard=True)

    window show

    "Я задумался о том, что совсем рядом, за тонкой стенкой переодевается прекрасная пионерка, прислонился к стене, не заметив стоящие грабли."

    play sound bkrr_sfx_list["rake_hit"]

    with vpunch

    "Они напомнили о себе, больно треснув меня по спине."
    mz_v "Если бы они были детские, было бы больнее, правда?"
    "Раздалось откуда-то сбоку."

    play music music_list["your_bright_side"] fadein 3

    show mz normal glasses pioneer at center with dissolve

    me "А, привет, Женя. {w}Да, намного."

    show mz smile glasses pioneer at center with dspr

    mz "Чего ты тут делаешь? В гости пришёл? {w}Или, может, тебя вожатая прислала мне на помощь?"
    me "Жень, я бы с радостью, но меня уже к Славяне направили. Извини."

    show mz bukal glasses pioneer at center with dspr

    mz "Да ладно!"
    "Она взмахнула рукой."

    show mz normal glasses pioneer at center with dspr

    mz "Славе помощник нужнее. Парней в отряде нет, так она за всех крутится."
    me "Как нет? {w}А Шурик с Сыроежкой?"
    mz "Так то ж кибернетики!"
    "Отмахнулась Женя."
    mz "Толку от них. Сыроежку вон попросила выключатель починить, так он, гад, поставил какой-то не наш, который по хлопку включается и выключается."
    mz "Будет, говорит, тебе удобнее. Изобретатель, понимаешь."
    me "Ну так круто же!"

    show mz angry glasses pioneer at center with dspr

    mz "Ага! Круто. Книжку на стол положишь, свет гаснет. {w}Комара убьёшь, свет гаснет."
    mz "Еле заставила нормальный выключатель поставить."
    me "Понимаю."

    show mz bukal glasses pioneer at center with dspr

    mz "Ну, значит, одна буду порядок наводить. {w}Просила у вожатой помощника – ни в какую."
    mz "Бери, говорит, из младших отрядов, кого хочешь. {w}А что, они мне полки подвигают?"
    me "А помочь совсем некому?"
    mz "Ну, раз ты занят, пойду этих юных техников просить. {w}Не хочется, а придётся."

    hide mz with dissolve

    stop music fadeout 3

    "Она вздохнула и зашла в домик."

    window hide

    $ renpy.pause(1.0, hard=True)

    window show

    "Ещё минута-две, и наружу вышла Славя. {w}На этот раз она была в уже знакомом мне чёрном спортивном костюме."

    show sl normal sport far at center with dissolve

    sl "Я готова! Идём!"
    "Я с трудом отвёл взгляд от её ножек и кивнул."
    me "Идём! А куда?"

    show sl surprise sport at center with dspr

    sl "Я же говорила: на сцене нужно кое-что сделать."

    show sl smile sport at center with dspr

    sl "Ну, пошли, пошли."

    window hide

    stop ambience fadeout 1

    scene bg ext_stage_normal_day with fade

    play music music_list["everyday_theme"] fadein 3

    play ambience ambience_camp_center_day fadein 3

    window show

    "Через несколько минут мы подошли к сцене."
    "Там переминался с ноги на ногу незнакомый круглолицый пионер, которого я раньше не встречал. {w}При виде Слави он оживился и поспешил к нам."

    show sl normal sport at center with dissolve

    sl "Толя? Доброе утро! Ты инструмент принёс?"

    window hide

    show sl normal sport at right with ease

    show tol smile pioneer at left with dissolve

    window show

    tol "Да, конечно! Вот всё, что ты просила."

    show tol normal pioneer at left with dspr

    tol "Молотки, гвозди, пила, рулетка. Гвоздодёр не дали, дали клещи."

    show sl shy sport at right with dspr

    sl "Спасибо, ты просто чудо. Вы с Семёном знакомы?"

    show tol smile pioneer at left with dspr

    tol "Нет!"

    show tol smile pioneer close at left with dspr

    "Он протянул руку."
    tol "Меня Толик звать. {w}Спасибо, что Мику помог вчера, я никак не мог, занят был."

    show tol normal pioneer at left with dspr

    th "Тот самый Толик, который в музклубе состоит? Интересно."
    "При виде его я почему-то испытал облегчение. {w}Будь он роковым красавцем и вертись возле Мику, я бы расстроился, а так…"
    me "Не за что. А меня – Семён. {w}Ты же не из нашего отряда?"

    show tol sad pioneer at left with dspr

    tol "Нет."
    "Развёл руками он."
    tol "Я в третьем. Так вышло."

    show sl normal sport at right with dspr

    sl "Ну, мальчики, смотрите, что нам надо: вот тут, тут, тут и тут – прогнили доски."
    sl "Нужно их отодрать, набить новые, а завтра девочки покрасят. {w}Сможете?"
    tol "Ну…"
    "Протянул Толик."
    tol "Я с молотком вообще не очень дружу."

    show sl smile sport at right with dspr

    sl "Понятно. {w}А ты, Семён?"
    me "Ну, гвоздь забить смогу. Наверное."

    show sl laugh sport at right with dspr

    sl "Ну, уж постарайтесь. Ладно?"
    me_tol_d "Ладно!"
    "Хором протянули мы."

    show tol smile pioneer at left with dspr

    tol "Постараемся."

    show sl smile sport at right with dspr

    sl "А я пока траву вдоль сцены подёргаю. {w}Вы давайте, давайте, приступайте."

    window hide

    hide sl
    hide tol
    with dissolve

    $ renpy.pause(2.5, hard=True)

    stop music fadeout 3

    window show

    "Ломать – не строить. Гнилые доски обшивки отдирать было очень легко."

    play sound_loop bkrr_sfx_list["saw_loop"]

    "Плотницкие работы были мне в новинку, но нам с Толиком удалось напилить новые доски на куски примерно одинаковой длины."
    "Славя тем временем забралась на сцену и постукивала ногой по доскам настила, проверяя, не нужно ли их укрепить."

    stop sound_loop fadeout 3

    sl "Эх! Рассохлось всё."
    sl "Я карандашом помечу, где нужно будет по паре гвоздиков забить, чтоб не болталось. А потом…"

    show tol normal pioneer at center with dissolve

    tol "Славя, не всё сразу! Давай это закончим."
    "Он тяжело пыхтел и обливался потом."
    sl "Я так, на будущее. Заканчивайте, конечно. Потом отдохнём."

    window hide

    show tol normal pioneer at right with ease

    show sl normal sport at left with dissolve

    window show

    "Славя спрыгнула к нам и присела рядом."

    show sl normal sport at left with dspr

    sl "Давайте я буду держать, а ты прибивай. Толик, смотри, чтобы ровно выходило."

    hide sl
    hide tol
    with dissolve

    play sound_loop bkrr_sfx_list["hammer_loop"]

    "Сейчас, с дырками в облицовке, сцена походила на малыша, который потерял молочные зубы."
    "Я примерился по гвоздю и промахнулся, согнув его."
    me "Сейчас. Руки дрожат после пилы."
    sl "Конечно, не спеши."

    stop sound_loop fadeout 3

    "Второй гвоздь согнулся так же. Третий вошёл как надо, но на последнем ударе я здорово приложил себя по пальцу."

    me "Б… больно."
    "Вовремя перехватил нецензурное слово я."

    show tol normal pioneer at right
    show sl normal sport at left
    with dissolve

    tol "Ты чего?"
    "Удивился Толик, больше уделявший внимания вырезу спортивной майки Слави, чем плотницким работам."
    me "По пальцу попал."

    show tol sad pioneer at right with dspr

    tol "Ты осторожней!"
    me "Вот сам попробуй!"

    show sl shy sport at left with dspr

    sl "Ему нельзя. Он гитарист! {w}Если повредит пальцы, беда будет."
    tol "Славь, ну не подкалывай. Если бы не концерт, ничего, но репетировать же надо. Если пораню руки, Алиса меня съест."
    th "Алиса? А она тут причём?"
    "Впрочем, мне было не до вопросов."
    "Скажу больше: на какую-то минуту желание узнать, где я, отступило на второй план, уступив первенство желанию забить этот чёртов гвоздь."

    show sl smile sport at left with dspr

    sl "Да ладно, всё я понимаю. Всё равно, спасибо за помощь!"

    window hide

    hide sl
    hide tol
    with dissolve

    play sound_loop bkrr_sfx_list["hammer_loop"]

    $ renpy.pause(2.5, hard=True)

    stop sound_loop fadeout 3

    window show

    "Наконец, ценой пары ушибленных пальцев и парочки заноз очередная доска встала на место. Оставалось набить ещё две."

    show tol normal pioneer at right
    show sl normal sport at left
    with dissolve

    sl "Красота! Я наверх пошла. Семён, возьми пяток гвоздей и давай сюда!"

    window hide

    hide sl
    hide tol
    with dissolve

    scene bg ext_stage_big_day_bkrr with dissolve

    window show

    "Мы поднялись на сцену."
    "Я вспомнил, как Ульяна поймала меня за игрой на воображаемой гитаре, и улыбнулся."
    me "Всегда мечтал попасть на сцену! Правда, не с молотком."

    show tol normal pioneer at center with dspr

    tol "Ай, ничего интересного."
    me "А ты выступал?"

    show tol smile pioneer at center with dspr

    tol "Пару раз, когда на контрабасе играл, на экзаменах."
    me "На контрабасе? А как же гитара?"
    tol "Так бас-гитара. Просто, для девчонок всё равно, что басуха, что гитара."

    window hide

    show tol smile pioneer at right with ease

    show sl serious sport at left with dissolve

    window show

    sl "Ну, прости, пожалуйста, что я не музыкант!"

    show tol sad pioneer at right with dspr

    tol "Нет-нет, я ничего не имел в виду."

    play sound bkrr_sfx_list["keys_fall"]

    show sl surprise sport at left with dspr

    "Тут раздался металлический лязг."
    "Тяжёлая связка ключей, которую Славя держала в руках, упала на настил сцены и, как назло, провалилась в широкую щель между досок."
    sl "Вот ведь не везёт! Нужно было что-то с карманами надеть. Ещё думала в коробку положить."
    me "И что теперь?"

    show sl shy sport at left with dspr

    sl "Ну, две доски вы ещё не прибили, так что я пролезу, наверное, и достану."
    tol "А пролезешь? Может, дверцу вон ту отпереть, и через неё?"

    show sl laugh sport at left with dspr

    sl "Отличная идея! Только ключ от замка – внутри."

    show sl normal sport at left with dspr

    sl "Надо бежать к Ольге Дмитриевне, рассказывать «ай-яй, Ольга Дмитриевна, я ключи от всего лагеря потеряла, дайте мне свою связку!». {w}Не хочу, подумает, что я безответственная."
    me "Понимаю… Ну, давай, может, ещё пару досок снимем?"
    sl "Не надо! Я пролезу."

    window hide

    hide sl with dissolve

    $ renpy.pause(0.5, hard=True)

    scene bg ext_stage_normal_day with dissolve

    window show

    "Соскочив со сцены, Славя встала на четвереньки и протиснулась в щель между досками."

    show tol normal pioneer at right with dissolve

    tol "Ты как? Может, давай доску отдерём? Не застрянешь?"
    sl "Не! Я связку вижу, только дотянуться не могу. {w}Сейчас. {w}Тут проволоки кусок лежит, я его согну и…"

    window hide

    play sound bkrr_sfx_list["whiteout1"]

    play music music_list["glimmering_coals"]

    scene cg d6_sl_ass at d6_sl_ass_atl with bkrr_fade(0.5)

    $ renpy.pause(1.5)

    window show

    "Мы не могли ничем помочь, так что просто присели на траве и рассматривали окружающий пейзаж. {w}Особенно – пару замечательной формы ножек, выглядывающих из-под сцены."
    "Да и то место, откуда они начинались, было выше всяких похвал. Я почувствовал, что краснею."
    th "Хороша!"
    dv_v "Ах вы, коты мартовские!"
    "Раздалось из-за спины."
    dv_v "На что это вы с такими рожами глазеете, а?"

    window hide

    scene bg ext_stage_normal_day
    show tol smile pioneer at left
    show dv grin pioneer at right
    with dissolve

    window show

    tol "Здорово, Алиса!"

    show dv smile pioneer at right with dspr

    dv "Здоровее видали. Что это вы так рассматривали?"
    me_tol_d "Ничего!"
    "Хором ответили мы."

    show dv normal pioneer at right with dspr

    dv "Так я и поверила."
    dv "А ну, повернулись к лесу передом, к Славке задом."

    window hide

    hide tol
    hide dv
    with dissolve

    stop music fadeout 3

    window show

    "Она вела себя так нагло, что даже мысли поспорить не возникало. {w}Задом-не задом, но всё-таки мы отвернулись."
    "Алиса подошла к сцене и небрежно похлопала Славяну пониже спины."
    dv "Эй, Славя! Чего позируешь?"
    sl "Ай! Кто там балуется?"
    dv "Это я, Алиса. Эти обормоты тебя разглядывали, я тут постою. {w}Ты там надолго?"
    sl "Да уже вылезаю!"

    window hide

    $ renpy.pause(1.0, hard=True)

    show sl shy sport at center with dissolve

    window show

    "Славя подалась назад и выбралась из-под сцены, продемонстрировав нам связку ключей."
    sl "Вот они! Еле нашла."
    "Алиса задумчиво кивнула, потом подошла к замку на дверце, потянула его одним пальцем, отчего петля, висевшая на одном ржавом гвозде, оторвалась совсем."

    window hide

    play sound sfx_door_squeak_light

    $ renpy.pause(1.0, hard=True)

    show sl shy sport at right with ease

    show dv laugh pioneer at left with dissolve

    window show

    dv "Стоило так мучиться. Дверь же не заперта."

    show sl surprise sport at right with dspr

    sl "А ты откуда знаешь?"
    dv "У Ульяны там секретное место, чтобы прятаться. Ну, теперь-то уже не секретное."

    show sl serious sport at right with dspr

    sl "И где же ты раньше была! А я тут измазалась вся, пока доставала. {w}Ты нам помочь пришла?"

    show dv normal pioneer at left with dspr

    dv "Вообще-то Толика забрать."

    show sl angry sport at right with dspr

    sl "Погоди, мне его вожатая на весь день дала!"

    show dv guilty pioneer at left with dspr

    dv "Славя, ну не лезь в бутылку! {w}У нас инструмент в домике лежит со вчера – вдвоём не натаскаемся."
    dv "Семёна забрали, а Улька на стадион убежала. {w}Ну, отпусти его хоть до обеда!"

    show sl serious sport at right with dspr

    sl "Ладно! До обеда."

    show sl normal sport at right with dspr

    sl "Семён, ты как, один справишься? Нужно будет ещё прибить кое-что, и отдыхаем."
    me "Да чего тут. Справлюсь."

    hide sl
    hide dv
    with dissolve

    show tol sad pioneer at center with dissolve

    tol "Спасибо, друг. Ну, извини. Пойду я."

    hide tol with dissolve

    show sl smile sport at center with dissolve

    sl "Чай пить будут вместо работы."
    sl "Ну, раз мы с тобой вдвоём… {w}давай продолжим?"

    window hide

    stop ambience fadeout 2

    $ bkrr_timeskip_short()

    scene bg ext_stage_normal_day with bkrr_timeskip_transition()

    play ambience ambience_camp_center_day fadein 3

    play music music_list["two_glasses_of_melancholy"] fadein 3

    window show

    "Я успел набить оставшиеся доски на облицовку, укрепить настил сцены и даже побренчать на расстроенном пианино, пылившемся под стенкой. {w}Вышло отвратительно."

    show sl shy sport at center with dissolve

    sl "Да уж. Музыка – это явно не твоё!"
    me "Наверное. Но слушатель я хороший."
    dv "Эй, вы двое! Хорош пианино терзать."

    window hide

    show sl serious sport at left with ease

    show dv normal pioneer at right with dissolve

    window show

    sl "Ты ещё что-то хотела? Семёна не отдам!"

    show dv smile pioneer at right with dspr

    dv "Ой, нужен он мне сто лет. Берите вот! Это вам за Толика!"
    "Она поставила на край сцены бутылку минералки со стаканом на горлышке."

    show sl shy sport at left with dspr

    sl "Спасибо, Алиса!"
    me "Спасибо!"

    show dv grin pioneer at right with dspr

    dv "Да чего там! Стакан потом в столовую верните!"

    window hide

    hide dv with dissolve

    show sl smile sport at center with ease

    window show

    sl "Вот такая она у нас. Алиса-то."
    sl "Стакан только один. Давай, пей ты первый."
    me "Мы люди не гордые, мы и из горлышка попьём."

    window hide

    hide sl with dissolve

    $ renpy.pause(2.5, hard=True)

    window show

    "Передохнув, мы сложили инструмент в коробку и отправились дальше."

    window hide

    stop music fadeout 3

    stop ambience fadeout 3

    scene bg ext_clubs_day with fade3

    play ambience ambience_camp_center_day fadein 3

    window show

    "Близилось время обеда. {w}Мы стояли на центральной аллее, у самых ворот, где предстояло сделать завершающий штрих."

    show sl normal sport at center with dissolve

    sl "Семён, ты высоты не боишься?"
    me "Ну, не то, чтобы боялся…"

    show sl shy sport at center with dspr

    sl "Вот и хорошо. А то я боюсь!"

    show sl smile sport at center with dspr

    sl "Смотри, вот здесь, над входом в кружки, надо транспарант будет приделать. {w}Он как раз на вход смотреть будет."
    sl "Приделаем два крючка и на них подвесим, потом легко снять можно будет. {w}Сможешь?"
    th "Почему-то в присутствии Слави мне стало стыдно признаваться в том, что высоты я побаиваюсь. Но, раз уж обещал, надо выполнять."
    me "Постараюсь."

    show sl normal sport at center with dspr

    sl "Ну, беги переодевайся. Пообедаем и закончим."

    play sound sfx_dinner_horn_processed

    th "Как время-то летит. Уже и обедать пора."

    window hide

    stop sound fadeout 1

    stop ambience fadeout 1

    scene bg int_dining_hall_people_day with fade

    play ambience ambience_dining_hall_full fadein 3

    window show

    "Я поспешил переодеться и пришёл в столовую с небольшим опозданием."

    show mt normal pioneer at center with dissolve

    mt "Семён? Опаздываешь! Давай, вот там место есть."

    hide mt with dissolve

    "Сесть с Мику не получилось. Они с Алисой и Ульяной устроились в своём уголке."
    "Неожиданно появилась запыхавшаяся Славя. Ольга что-то спросила у неё и показала в мою сторону."

    show sl normal pioneer at center with dissolve

    sl "Не возражаешь, если я с тобой сяду? {w}Припоздала я с этими переодеваниями."
    me "Садись, конечно. Приятного!"

    show chair_c behind sl
    show sl normal pioneer at bkrr_sit_center
    with dissolve

    sl "Спасибо-спасибо."
    sl "Ой, смотри, ещё один опоздавший. {w}Толик, иди к нам!"

    show tol smile pioneer far at right with dissolve

    tol "Бегу!"

    show tol smile pioneer at right with dspr

    tol "А то уже думал, места не найду, ждать придётся."

    window hide

    stop ambience fadeout 3

    $ bkrr_timeskip()

    scene bg int_dining_hall_people_day with bkrr_circleout_transition

    play ambience ambience_dining_hall_full fadein 3

    show chair_l behind sl
    show chair_r behind tol
    show sl normal pioneer at bkrr_sit_left
    show tol normal pioneer at bkrr_sit_right
    with dissolve

    window show

    "Когда мы закончили с едой, к нам подошла Алиса и, не обращая внимания на нас со Славей, потянула Толика за рукав."

    show dv normal pioneer behind sl with dissolve

    dv "Вставай, пошли! Репетировать будем!"
    tol "Ну, я вроде как Славе и Семёну помогал. Вожатая ругаться будет."
    dv "А откуда она узнает? Если, конечно, никто жаловаться не побежит…"

    show sl surprise pioneer at bkrr_sit_left with dspr

    sl "Алиса, давай без намёков. {w}Мы же договаривались: до обеда Толик у вас, после обеда – с нами. {w}Да, Толя?"

    show tol sad pioneer at bkrr_sit_right with dspr

    tol "Так-то оно так, но…"

    show dv guilty pioneer at center with dspr

    dv "Да мало ли что договаривались. {w}Ну, не вредничай! Нам к концерту готовиться надо."
    sl "Алиса, я не вредничаю."

    show sl serious pioneer at bkrr_sit_left with dspr

    sl "Ну, давай так: ещё час поработает с нами, и забирайте. Мы вдвоём никак не управимся."

    show dv normal pioneer at center with dspr

    dv "Полчаса! Не больше."
    sl "Хорошо, полчаса."
    dv "Я за ним приду."

    show dv normal pioneer far at center with dspr

    dv "Толян, держись!"

    hide dv with dissolve

    tol "Да ладно тебе."
    "Алиса развернулась, подошла к беседующим в сторонке Мику и Ульяне, и все они втроём вышли из столовой."

    show sl normal pioneer at bkrr_sit_left with dspr

    sl "Ну, пойдём? {w}Семён, а ты где инструменты оставил?"
    me "У кибернетиков, сразу за дверью лежат."
    tol "А не сопрут? Мне ведь их вернуть надо!"
    sl "Не волнуйся, не украдут."

    show tol pain pioneer at bkrr_sit_right with dspr

    tol "Ага… Тебе легко говорить. {w}Мне электрик сказал: «и не вздумай что-нибудь потерять!»."

    stop ambience fadeout 3

    window hide

    scene bg ext_clubs_day with fade3

    play ambience ambience_camp_center_day fadein 3

    window show

    "Инструмент оказался на месте."
    "Под стенкой кружка юных техников стоял большой транспарант с надписью «Добро пожаловать!», натянутый на деревянную раму. {w}Рядом лежала старая деревянная лестница."
    "Я сглотнул. {w}Лезть наверх по этой развалюхе очень не хотелось. {w}Совсем невысоко, конечно, но как-то страшновато."

    show sl normal pioneer at left
    show tol normal pioneer at right
    with dissolve

    sl "Ну, Семён… давай на лестницу. {w}Мы тебе его подадим, прибьёшь крючок, мы его зацепим за один угол, потом выровняем по нему второй, и на сегодня всё."

    show sl shy pioneer at left with dspr

    sl "Я потом, наверное, в волейбол сыграю. {w}Не хочешь со мной?"
    me "Жарковато. Да и не умею я."

    show sl laugh pioneer at left with dspr

    sl "А чего там уметь. Я тебя научу, не переживай."
    th "Интересно, почему столько внимания?"
    me "Ты что, совсем не устала?"

    show sl tender pioneer at left with dspr

    sl "От чего? Вы всю работу сделали. {w}Я так, траву подёргала."

    show sl normal pioneer at left with dspr

    sl "Ну, кто наверх? {w}Семён, ты?"

    window hide

    hide sl with easeoutleft

    show tol normal pioneer at center with ease

    window show

    "Я отвёл Толика в сторону."
    me "Толя… тут такое дело. Можешь сам залезть?"
    tol "Чего?"
    me "Я высоты боюсь. Только Славе не говори."

    show tol smile pioneer at center with dspr

    tol "Да ладно? "

    show tol normal pioneer at center with dspr

    extend "Ну, хорошо. Подержи лестницу."

    hide tol with dissolve

    "Толя забрался вверх по лестнице и принялся размечать места под крючки для транспаранта. Славя помогала ему снизу, а я ждал, пока понадобится моя помощь."
    "На дорожке появилась тяжело навьюченная Алиса. На каждом плече у неё висело по гитаре, а в руках она тащила большую коробку."
    "Подойдя к нам, Алиса недовольно посмотрела на меня, потом на Толика, увлечённо возившегося с рулеткой."

    show dv normal pioneer at center with dissolve

    dv "Уфф… тяжело-то как."
    "Она поставила коробку на землю, поправила ремни гитар на плечах и с нажимом поинтересовалась:"

    show dv angry pioneer at center with dspr

    dv "Семён, вот я не поняла. {w}Почему Толя наверху, а ты тут?"
    dv "Я тут надрываюсь, ишачу, а ты стоишь и за лестницу держишься."
    me "Ну, так вышло."

    show dv guilty pioneer at center with dspr

    dv "Вы скоро там?"

    window hide

    show dv guilty pioneer at right with ease

    show sl normal pioneer at left with easeinleft

    window show

    sl "Скоро! А полчаса ещё не прошло. Ты чего пришла?"

    show dv normal pioneer at right with dspr

    dv "Да гитары в клуб несу. {w}Чуть руки не оторвала. Решила вот Толика назад забрать."

    show sl normal pioneer at left with dspr

    sl "Ну, что ты сразу всё ухватила. Хочешь, я нести помогу?"

    show dv normal pioneer at right with dspr

    dv "Не, это не всё, я лучше Толика подожду, и с ним перетаскаем."
    dv "Толя, давай живее там!"
    tol "Сейчас!"
    sl "Мальчики-девочки, мне отойти надо, я скоро вернусь."

    show sl shy pioneer at left with dspr

    sl "Алис, ты им помоги, если что, ладно?"

    show dv angry pioneer at right with dspr

    dv "Чего? {w}Славка, я вообще-то сама за помощником пришла, а не помогать!"

    show sl serious pioneer at left with dspr

    sl "Алиса, ну будь другом, постой тут пять минут, присмотри, чтоб не перекосили. {w}Я туда и обратно."

    show dv normal pioneer at right with dspr

    dv "Ладно, ладно. Посмотрю. {w}Нет, я удивляюсь, как это у тебя выходит вообще?"

    show sl smile pioneer at left with dspr

    sl "Просто, я волшебное слово знаю! «Пожалуйста»."
    dv "Иди уже, волшебница. Только смотри, недолго!"

    window hide

    hide sl with easeoutleft

    show dv normal pioneer at center with ease

    window show

    me "Да поставь ты гитары, чего ты их держишь? Тяжело ведь."
    dv "Да, точно."

    hide dv with dissolve

    "Алиса бережно устроила гитары на крыльце клуба, коробку и стойку оставила посреди дорожки, затем запрокинула голову и недовольно поинтересовалась:"
    dv "Ну, что там у вас смотреть-то надо?"

    show dv normal pioneer at center with dissolve

    tol "Смотри, я здесь крючок приделаю, а вон там, слева, второй уже прибит. {w}Глянь со стороны, ровно?"
    dv "Да, вроде бы… {w}Не вижу отсюда."

    show dv grin pioneer at center with dspr

    dv "Да нормально, прибивай уже, да пошли."
    tol "Семён, давай транспарант! {w}Сейчас мы его!"
    tol "Алиса, а ну, посмотри ещё разок!"

    hide dv with dissolve

    "Я с натугой поднял тяжёлую деревянную раму, обтянутую холстом, и поднёс её к Толику."
    "Тот ухватился за неё и принялся двигать вверх-вниз, пытаясь сделать ровно. {w}Я удерживал вторую сторону, стоя на земле, а Алиса следила, чтобы мы ничего не перекосили."
    th "Кажется, она вошла во вкус и с удовольствием командовала процессом."

    show dv normal pioneer at center with dissolve

    dv "Левее!"
    tol "Так?"
    dv "А теперь повыше!"
    tol "Так хватит?"

    show dv sad pioneer at center with dspr

    dv "Да, всё там ровно, хорош уже!"

    window hide

    play sound bkrr_sfx_list["box_fall"]

    show dv shocked pioneer:
        truecenter
        ease 0.85 ypos 1.5 zoom 0.9 rotate 25

    $ renpy.pause(0.85, hard=True)

    hide dv

    window show

    "Алиса сделала несколько шагов назад, споткнулась о стоящую на земле коробку."
    "Та опрокинулась, на землю высыпались какие-то железки, чайные чашки, банка с сахаром, гитарный ключ, свёрнутые в кольцо струны и ещё много всякой всячины."
    dv "Ах ты, зараза такая!"
    "Она нагнулась и принялась собирать всё обратно в коробку. {w}Короткая форменная юбка высоко задралась, открыв увлекательный вид на две розовые половинки, едва прикрытые узкими ярко-оранжевыми плавками."
    "Я почувствовал, что краснею."
    tol "Семён! Вывеску подай!"
    "Я, не отводя глаз от Алисы, машинально сунул транспарант в его сторону. {w}Рама упёрлась во что-то мягкое."

    play music music_list["doomed_to_be_defeated"]

    tol "Ай! Ты что дела…а-а-а-а!"
    "Затем сопротивление внезапно пропало, а лестница заскрежетала по стене клуба, заваливаясь набок. {w}Нужно было придержать её, но я впал в ступор и мог только смотреть, как он летит вниз."

    window hide

    show blink

    $ renpy.pause(1.0, hard=True)

    play sound sfx_fall_grass

    $ renpy.pause(1.0, hard=True)

    play sound2 sfx_fall_wood_floor

    window show

    "Конечно, высота небольшая, но… Я зажмурился."

    window hide

    hide blink
    show unblink

    $ renpy.pause(1.5, hard=True)

    window show

    "Алиса выпрямилась, какую-то секунду соображала, что происходит, а затем бросилась к лежащему пионеру."

    show dv shocked pioneer at right behind unblink with dissolve

    dv "ТОЛИК! ЧТО С ТОБОЙ??? ЗОВИТЕ МЕДСЕСТРУ!!!"

    show tol pain pioneer at left behind unblink with dissolve

    "Толик сидел на земле, среди обломков лестницы и транспаранта. {w}Он держался за руку, которая на глазах опухала."
    tol "Ох… Рука. Больно!"
    "Рыжая пионерка вперила в меня негодующий взгляд."

    show dv angry pioneer at right with dspr

    dv "Сенька? Это ты специально, да? Дурак криворукий! Ты посмотри, что ты наделал!"
    me "Прости меня, пожалуйста. {w}Толя, ты живой? Я не хотел, честно."
    "На шум подошли несколько незнакомых пионеров, они молча смотрели на нас, видимо, не зная что делать."
    tol "Рука болит! {w}Алиса, я к медсестре пойду, ты гитары отнеси сама, ладно?"

    show dv sad pioneer at right with dspr

    dv "А ты сам-то дойдёшь? {w}Может тебя проводить? Давай Ульянку позову."

    show dv angry pioneer at right with dspr

    dv "Ну чего вы стоите, глаза пучите, ну помогите ему кто-нибудь!"

    show dv guilty pioneer at center with ease

    "Толик взмахнул здоровой рукой."

    show tol sad pioneer at left with dspr

    tol "Дойду, дойду. Не суетись. {w}Вроде только руку ушиб."

    "С помощью Алисы Толик тяжело поднялся и захромал в сторону медпункта."

    window hide

    hide tol with dissolve

    stop music fadeout 3

    $ renpy.pause(1.0, hard=True)

    window show

    "Мне стало очень стыдно. {w}Алиса посмотрела вслед уходящему товарищу и снова переключилась на меня."

    show dv sad pioneer at center with dspr

    dv "А ты чего вылупился? Ты понимаешь, что натворил?"
    "Я попытался успокоить её."
    me "Да я же не специально! Ну не кипятись так."

    show dv rage pioneer at center with dspr

    "Игра воображения, конечно, но мне почудилось, что из её ноздрей повалил дымок."
    dv "НЕ КИПЯТИСЬ?"
    dv "Да ты единственному басисту в лагере руку искалечил. {w}Неделя подготовки насмарку! Кто на басу играть будет?"
    me "Алиса, ну хватит. Я, правда, не нарочно."
    me "И вообще, если бы ты юбку подлиннее носила, ничего бы не случилось. {w}А то сверкаешь тут… Конечно, я отвлёкся."

    show dv shy pioneer at center with dspr

    "Алиса порозовела, потом покраснела, а потом приобрела дивный свекольный цвет."

    window hide

    stop ambience

    play music music_list["awakening_power"]

    $ renpy.pause(1.0, hard=True)

    show dv rage pioneer at center with dspr

    window show

    "Она перехватила инструмент за гриф и замахнулась гитарой, как Джимми Хендрикс на колонку. {w}Голос её взлетел куда-то в область ультразвука."

    window hide

    scene cg d6_guitar_hit with bkrr_fade(1.0)

    $ renpy.pause(3.50, hard=True)

    play sound bkrr_sfx_list["guitar_hit"]

    scene black
    show bkrr_bang:
        truecenter
        alpha 1.1
        zoom 1.1
        linear 2.5 alpha 0.0 zoom 0.9
    with None

    stop music fadeout 1.0

    window show

    "Последнее, что я разобрал – это надпись «электрогитара полуакустическая, 4-х струнная, цена 129 рублей, Ленинград, ул. Ча…», несущуюся к моей голове."
    "Дальше был негромкий хруст и тишина. {w}Почему-то очень захотелось узнать, как же называлась улица."
    "Но кто-то слишком быстро погасил свет."

    window hide

    scene anim prolog_1 with fade3

    $ bkrr_set_time("prologue")

    play music music_list["sparkles"] fadein 5

    $ renpy.pause(1.0, hard=True)

    $ bkrr_set_mode(nvl)

    nvl show dissolve

    bus "Сдавай!"
    "Большой красный автобус в зелёных очках сидел напротив меня и неторопливо попыхивал сигареткой, зажатой в переднем колесе. {w}На коленях у него восседала хрупкая девочка в рваном платьице и шевелила кошачьими ушками."
    "Я перевёл взгляд на свои руки. Колода карт, зелёное сукно. {w}Где я?"
    bus "Ну, сдавай уже."
    "Ладно. {w}Я перетасовал колоду, дал ему снять, что он и проделал свободным колесом."
    "Очень изящно, надо сказать. {w}Одна… Две… Пять!"
    me "Слушай. Ты извини… но ты ведь автобус?"
    bus "Да. А что? Когда я угощал тебя пивом, тебя это не смущало."
    me "И правда."
    bus "То-то же."
    "На руках у меня было две пары. {w}Неплохо. Можно играть."
    me "На что играем, кстати?"
    bus "Как обычно."
    me "Это как?"
    bus "Сенька, хватит вертеть хвостом. Прости, Юля."
    bus "Давай, менять будешь, нет?"
    me "Одну. А ты?"
    bus "Мне хватит."

    nvl clear

    "Я поменял одну карту. {w}Джокер. {w}Неплохо, получается фулхаус."
    me "Вскрываемся?"
    "Девочка наморщила нос, а потом заревела. {w}Автобус укоризненно покачал кабиной."
    bus "Ты охренел так шутить? {w}Лену только закопали."
    bus "Свинья ты, вот что!"
    me "Прости, я не…"
    bus "А, ну да. Ты же не в курсе. {w}Но больше так не шути."
    me "Открываем карты?"
    bus "А то!"
    "Я выложил свои на стол. Автобус ехидно ухмыльнулся."
    bus "Не твой сегодня день. {w}У меня каре. Ну… Давай."
    me "Что?"
    bus "Будешь меня купать сегодня. {w}Вот тебе орудие труда…"
    "Он протянул мне носовой платок и ведро воды. {w}Девочка отплясывала на столе и напевала «а немытым трубочистам – стыд и срам!». {w}Я дисциплинированно постарался смыть корку грязи с его огромного корпуса, но он был покрыт ею в несколько слоёв. {w}В отчаянии я стукнул по ведру, и ледяной поток потёк по моему лицу."

    nvl hide dissolve

    stop music fadeout 3

    $ renpy.pause(1.0, hard=True)

    scene black with fade3

    $ bkrr_set_time()

    $ renpy.pause(1.0, hard=True)

    $ bkrr_set_mode()

    window show

    th "Бр-р-р! Холодная!"
    mi "Ой, Алис, смотри, он пришёл в себя! {w}Сеня, ты нас так не пугай!"

    window hide

    scene bg int_music_club_mattresses_day
    show expression bkrr_offset_defocusing("bg int_music_club_mattresses_day", intensity=2):
        zoom 1.025
        linear 7.5 alpha 0.0
    show unblink
    with None

    $ renpy.pause(7.5, hard=True)

    play ambience ambience_music_club_day fadein 3

    window show

    "Когда я смог открыть один глаз, то первое, что увидел – знакомые белые и зелёные полоски."
    "Почему то мелькнула неуместная мысль:"
    th "Три дня прошло. У неё все такие же, в полосочку, или она снова ту самую пару надела?"
    "Я лежал на матрасе, расстеленном прямо на полу музыкального кружка."

    play music music_list["miku_song_flute"] fadein 3

    show mi normal pioneer close at center with dissolve

    "Рядом сидела Мику и выкручивала мокрое полотенце, готовясь снова положить его мне на голову."
    "Кажется, кроме шишки ничего страшного не случилось. {w}Мику успокаивающе погладила меня по голове, отчего боль сразу утихла."
    th "Такая симпатичная девушка за мной ухаживает… {w}Удар по голове показался не слишком высокой ценой."
    "Холодная ткань снова легла на лоб. {w}Мику улыбнулась."

    show mi smile pioneer close at center with dspr

    me "Я… не хотел. Оно как-то само собой вышло."
    mi "Ты как?"

    show mi sad_smile pioneer close at center with dspr

    mi "Прости Алису, пожалуйста, она не со зла, просто импульсивная такая. {w}Она так хотела выступить, так хотела сыграть, а тут Толика увезли, а без бас-гитары ничего не выйдет…"
    mi "Ну правда, так всё неудачно сложилось. {w}Ничего, что мы тебя здесь положили?"

    show mi normal pioneer close at center with dspr

    mi "Виола пришла, тебя посмотрела, сказала, что всё нормально, только голова поболит, а в медпункте, пока Толика осматривали, нашатырь разбили. Мы предложили тебя здесь и оставить, а то ведь нашатырь, он пахнет плохо, им потому при обмороках и…"

    hide mi with dissolve

    "Нить её рассуждений, как обычно, ушла куда-то в сторону."

    window hide

    stop music fadeout 3

    $ renpy.pause(1.0, hard=True)

    window show

    "Я осторожно приподнялся, подождал, пока комната перестала качаться, и осмотрелся."
    th "Притащили сюда? Почему сюда?"
    th "Ну, вообще да, до домика было бы дальше. Может, из-за матрасов? {w}Да какая разница вообще?"
    "Сейчас музыкальный кружок не был таким чистеньким и нежилым, как пару дней назад."
    "По углам лежали ноты, на тумбочке стояли уже знакомые мне чашки и чайник, на дальнем стуле почему-то висели кеды. Ударная установка была собрана и стояла у рояля, а под стенкой стоял разобранный усилитель."
    "На винтовом табурете от пианино сидела Алиса и колдовала над электрогитарой."
    "Кажется, она слегка успокоилась, хотя всё равно злобно сопела и шипела сквозь зубы что-то неразборчивое, но явно нелестное."
    "На полу валялся уже знакомый мне чёрный кот, босой ногой Алиса поглаживала его мягкое брюхо. {w}Тот в экстазе обнимал её ступню лапами и облизывал пальцы."
    th "Кот-футфетишист?"
    "Так прошло несколько минут. {w}Я озирался, Алиса ворчала, Мику просто смотрела на нас, накручивая волосы на палец."

    show dv angry pioneer far at left
    show cat musclub_1
    with dissolve

    "Наконец, Алиса шмыгнула носом и, виновато потупившись, спросила:"
    dv "Ты как, Семён? Голова сильно болит? Живой? Как себя чувствуешь?"
    "Я решил не заострять конфликт и попробовал отшутиться."
    me "Как будто гитарой по лбу шарахнули."

    show dv smile pioneer far at left with dspr

    "Дурацкая шутка, но всё же сработала. Алиса слегка улыбнулась и снова потупилась."
    dv "Ты извини меня, пожалуйста. Не сдержалась я."

    show dv rage pioneer far at left with dspr

    dv "Но ты и сам виноват!"

    show dv shy pioneer far at left with dspr

    dv "Ой, прости. Я нервничала, а ты такое сказал, я от стыда и… Вот. {w}Ну не сердись, ладно?"
    me "Ладно, я и сам хорош. Как Толик?"

    show dv sad pioneer far at left with dspr

    dv "Плохо Толик. {w}Сам в порядке, но рука распухла. Наверное, сломал."

    show dv guilty pioneer far at left with dspr

    dv "Я понимаю, что ты не хотел, но мы в полной жо… беде теперь. {w}Его на рентген в город увезли, а играть точно не сможет."
    me "Извините вы меня. Честное слово, случайно получилось. {w}Отвлёкся, и… Ну, ты понимаешь."

    window hide

    show dv guilty pioneer far at left with ease

    show mi smile pioneer close at right with easeinright

    window show

    mi "Ну всё, всё, помирились, и ладушки."

    show mi normal pioneer close at right with dspr

    mi "Толик жив-здоров, ну, то есть скоро будет здоров."
    mi "Только что же мы делать-то будем? А жалко, только-только сыгрались – и остались без басиста. {w}А без него плохо звучать будем, бледно и неинтересно. Без баса никак."
    "Алиса удручённо махнула рукой."

    show dv angry pioneer far at left with dspr

    dv "Да здесь одно сплошное «никак». {w}Раз в жизни выпал шанс на сцене выступить. Когда ещё такой будет? {w}И на тебе, из-за одного пионера всё коту под хвост."

    $ bkrr_play_random(bkrr_meow_list)

    cat "Мяу!"
    dv "Прости, Пират, я не про тебя!"

    show dv sad pioneer far at left with dspr

    dv "Тем более, эти иностранцы слов не поймут."
    dv "Надо музыку дать! Ритм! А без баса какой ритм… {w}Мику, а ты не сможешь? Ну, если я одна на гитаре буду?"

    show mi sad pioneer close at right with dspr

    mi "Ой, Алиска, ну ты же знаешь, на басу мне тяжело. У меня пальцы слабые, я на грифе струны не прижму нормально. Ты ведь знаешь, струны есть разного натяжения, так вот тут они стоят очень толстые, у меня сил не хватит. Я, конечно, могу эспандером позаниматься до концерта, может и успею, но всё равно, кто тогда на второй гитаре будет играть?"
    mi "Нет-нет, не вариант! Хотя, я могу переписать наши партии так, чтобы…"

    hide mi
    hide dv
    hide cat
    with dissolve

    "Алиса страдальчески подняла глаза к потолку, слушая её щебетание."
    "Мику гениальна в части музыки. {w}Ходили слухи, что она может играть на любом из инструментов, что были в кружке, от тромбона до рояля. Кроме того, у неё потрясающий чистый голос."
    "Но вот если она начинала говорить о чём-то, то…"
    "Кажется, Алиса уже привыкла к такой манере, просто подошла к ней со спины и мягко, но настойчиво прикрыла ей рот ладонью."
    "Мику по инерции попыталась сказать ещё несколько слов, потом вздохнула и замолчала."

    show dv sad pioneer close at left
    show mi sad pioneer close at right
    with dissolve

    dv "Извини, что перебила. Всё, всё, я поняла. Ты не можешь."
    dv "Тогда… Раз нет басиста, надо гитариста. {w}Хоть плохонького. {w}Переучим!"

    show dv guilty pioneer close at left with dspr

    dv "Может, эту, как её? {w}Лилю? Алёну? {w}Ну, что из третьего отряда?"
    dv "Она у костра под гитару пела, помню. Но она меня не любит, я ей там на пляже… {w}неважно."
    dv "Может, попросишь её с нами сыграть?"

    show mi serious pioneer close at right with dspr

    mi "Да я её не знаю совсем, приду и начну просить сыграть? {w}Давай лучше Электроника попросим к ней сходить? Кажется, он ей нравится."
    dv "Но он и так занят по уши. Да и не умеет он с девушками договариваться."

    show dv sad pioneer close at left with dspr

    dv "Г-р-р-р! {w}Ну где мне найти человека, знающего, где у гитары гриф?"
    dv "Музыкальная школа, называется. Одни скрипачи да кларнетисты, чтоб их."

    show mi angry pioneer close at right with dspr

    "Мику наморщила лоб, а затем довольно щёлкнула пальцами."

    window hide

    $ renpy.pause(1.0, hard=True)

    play music music_list["you_lost_me"]

    show mi happy pioneer close at right with dspr

    window show

    mi "А вот Семён, кажется, что-то умеет. {w}Помнишь, Сеня?"

    show mi smile pioneer close at right with dspr

    mi "Ты когда с бегунком приходил, что-то наиграл. Хорошо получалось!"
    me "Я?"
    "Голова болела, так что я не сразу понял, о чём это она."
    me "Играл? {w}Точно. Было такое. {w}Играл."
    mi "Ну, конечно, было! Помнишь, там ещё приятная мелодия такая."

    show dv grin pioneer close at left with dspr

    "На лице Алисы появилось выражение кошки, увидевшей воробья."
    dv "Семён, у тебя совесть есть? {w}Ты нас оставил без басиста, сам умеешь играть на гитаре, смотришь на мои страдания и молчишь? {w}Ну, кто ты после этого?"
    me "Не умею я!"

    show dv rage pioneer close at left with dspr

    dv "Ну-ну. Не ври мне!"
    me "Честно, не умею!"
    dv "А Мику говорит – умеешь."
    dv "Вот. Всё само собой решилось! {w}Микуля, ты молодец!"

    show dv laugh pioneer close at left with dspr

    dv "А ты, членовредитель, не бойся! Ничего сложного, это же бас. {w}За неделю мы тебя поднатаскаем, и всё будет хорошо."
    th "Кажется, она слишком размечталась. И забыла меня спросить, хочу ли я вообще играть."
    me "Подожди, Алиска! Я говорю тебе, что я не у-ме-ю! И за неделю не научусь!"

    show dv smile pioneer close at left with dspr

    dv "Ну, во-первых, не за неделю, а за двенадцать дней."
    dv "А во-вторых, ты даже не представляешь, сколько можно выучить под нашим чутким руководством, да занимаясь по двенадцать часов в день."
    me "Сколько-сколько часов?"

    show dv laugh pioneer close at left with dspr

    dv "Ну да, я понимаю, маловато. Но тебе же ещё спать и кушать надо. Больше двенадцати не получится."
    dv "Зато смотри: мы тебя освободим от работ. {w}Никакой краски, гвоздей, пыли, грязи. Никаких тяжестей и подметаний. {w}И в компании трёх очаровательных девушек."

    show dv normal pioneer close at left with dspr

    dv "И вину перед нами и, особенно, перед Толиком загладишь. {w}Давай, Семён, не ломайся!"

    show dv normal pioneer at left
    show mi normal pioneer at right
    with dspr

    me "Ну, я даже не знаю, ребятам нужна помощь с трибунами. {w}И режим соблюдать надо. {w}И Лена с Виолой просили помочь в медпункте. {w}И вообще…"
    "Продолжая отнекиваться, я медленно отступал к двери."
    "Шаг. {w}Ещё. {w}Ещё. {w}Пауза. {w}Ещё шаг."

    show dv normal pioneer far at left
    show mi normal pioneer far at right
    with dspr

    th "Вроде бы дистанция подходящая. Есть!"

    hide dv
    hide mi
    with dissolve

    "Я бросился к двери и толкнул её."
    th "Заперто? Что за чертовщина…"
    "Я лихорадочно искал замок. Бросив взгляд через плечо, я увидел Мику и Алису, медленно идущих ко мне. {w}Всё выглядело как в ужастике."

    show dv angry pioneer at left
    show mi grin pioneer at right
    with dspr

    dv "Сёма, вернись!"
    me "Нет!"
    dv "Я очень прошу. Ну не подводи нас?"
    me "НЕТ! НЕ БУДУ!"

    show dv rage pioneer at left with dspr

    dv "Не умеешь – заставим, не хочешь – научим!"
    me "Без меня!"
    "Шпингалет обнаружился у самого пола. {w}Заперт…"
    th "Они ожидали, что я попытаюсь бежать?"

    window hide

    stop ambience fadeout 0.5

    play sound sfx_open_door_2

    scene bg ext_music_club_verandah_day_v1:
        pos(0.5, 0.6)
        anchor(0.5, 0.5)
        zoom 1.75
    with dissolve

    window show

    "Я открыл дверь и успел сделать шаг за порог, когда сзади донеслось:"
    dv "Мику, хватай, не дай уйти! Я тебе пирожное дам!"
    mi "Попался!"

    window hide

    scene bg int_music_club_mattresses_day with dissolve

    window show

    "Тут же меня ухватили за воротник и втянули назад."

    window hide

    stop music fadeout 3

    scene bg int_music_club_mattresses_day:
        truecenter
        parallel:
            ease 0.5 zoom 2.0 rotate -9
        parallel:
            ease 0.3 ypos 0.6
            ease 0.2 ypos 0.25
    show red:
        alpha 0.0
        pause 0.35
        ease 0.15 alpha 0.5
    with None

    $ renpy.pause(0.5, hard=True)

    play sound bkrr_sfx_list["sem_falls_on_floor"]

    scene black

    $ renpy.pause(2.5, hard=True)

    window show

    "Не знаю, как это у неё вышло, но непонятная сила увлекла меня вниз, мягко уронила на пол и тут же прижала к нему. {w}Рубашка жалобно затрещала, но пуговицы выдержали."

    window hide

    play music music_list["waltz_of_doubts"]

    play sound bkrr_sfx_list["whiteout2"]

    scene cg d6_on_floor at d6_on_floor_atl with bkrr_fade(2.0)

    $ renpy.pause(1.0)

    window show

    "Внезапно я обнаружил, что на груди и шее у меня лежат стройные ножки в чёрных чулках."
    "Мику ловко взяла мою руку на болевой приём, прижимая её к своей груди. {w}На лице у меня поневоле расплылась довольная ухмылка."
    "Я подёргался для порядка, а потом устроился поудобнее. Грудь Мику под моей рукой была тёплой, упругой и очень приятной на ощупь. {w}Жаль, касался я её только тыльной стороной ладони. Больно не было, Мику держала цепко, но руку не ломала, просто не давала освободиться."
    th "Какие крепкие у неё пальцы, а кажутся такими тонкими и изящными. От гитары, наверное."
    me "Попался! Сдаюсь. Как ты это сделала?"
    mi "А это джиу-джитсу. {w}Мама меня научила нескольким приёмам, рассказывала, что это может меня защитить, если я встречу преступника."
    mi "Конечно, я и подумать не могла, что буду ловить басиста для нашей группы. {w}А ведь и правда, преступников, наверное, больше чем музыкантов, а может, и наоборот. {w}Интересно, кто-нибудь считал?"
    mi "А как их сосчитать-то? Это ведь у всех спрашивать надо. А если врать будут? Вот я бы преступником была, не созналась бы…"
    mi "Я больно тебе не сделала? Я постаралась мягонько. Ты не ушибся? Вот в Японии, говорят, такие мастера, если тебя бросят, то сразу ломается пара костей, и… {w}Если я и тебе сломала бы руку, глупо бы вышло, правда? Тебе не больно?"
    "Я слегка пошевелил рукой, по-прежнему прижатой к её груди."
    th "Мне показалось, или она вздрогнула?"
    me "Нет-нет, нормально. Держи покрепче, а то убегу."
    "Она послушно сжала моё запястье, ещё плотнее прижав её к себе."
    th "Снова держусь за руку с девушкой… На этот раз с той, которая мне нравится. {w}Ну, не я держусь, а она меня держит, но всё равно здорово! Может, и не очень романтичный первый раз, но уж как вышло."
    mi "А куда же ты убежишь?"
    me "Куда-куда. {w}В дверь, конечно."
    me "А потом вы с Алисой будете меня искать, а я буду прятаться под кроватью вожатой."
    mi "Ну, не убегай, пожалуйста. {w}Алиса расстроится. {w}И я тоже… {w}И Ульяна."
    mi "Правда, она ещё не знает, что случилось, но когда узнает, будет рада. А может, и расстроится, ей, по-моему, нравится над Толиком подшучивать. Вообще-то мы с ним только-только познакомились, особо и не дружили, но всё равно…"
    "В этот раз я надеялся, что она будет говорить подольше. Уху и щеке было тепло и приятно, а ощущение груди Мику под рукой было просто непередаваемым. Пришлось согнуть ноги, чтобы реакция моего организма не так бросалась в глаза."
    "Алиса разглядела, что лицо у меня не сильно-то несчастное. Скорее, наоборот."
    dv "Ладно, отпусти его, Микуля. А то смотри, как он лыбится, сейчас помрёт от счастья."
    dv "Сень! Ну войди в наше положение, нам правда очень нужна твоя помощь."
    th "Наверное, она очень не любит просить. Тем более, у человека, которого перед этим стукнула гитарой по голове."

    window hide

    stop music fadeout 5

    scene bg int_music_club_mattresses_day
    show cat musclub_2
    with dissolve

    play ambience ambience_music_club_day fadein 3

    window show

    "Мику помогла мне подняться и повисла на моей руке. {w}Приятное тепло разливалось от того места, где мы соприкасались."
    "Если она прижмётся ещё хоть немножко сильнее, то у меня и вправду лицо от счастья треснуть может."

    show mi sad pioneer close at center with dissolve

    mi "Сеня, помоги нам, пожалуйста!"
    mi "А я за это с тобой в кино пойду. И на танцы. И рубашку тебе постираю. Хочешь? Ну скажи, что согласен!"
    th "Она ещё спрашивает."

    window hide

    hide mi with dissolve

    show dv normal pioneer at center with dissolve

    window show

    dv "С другой стороны, если ты откажешься…"
    "Подключилась Алиса."

    play music music_list["that_s_our_madhouse"]

    show dv rage pioneer at center with dspr

    dv "… то я тебе устрою весёлую жизнь."
    dv "Сколопендра и ведро воды покажутся отдыхом! {w}Ты будешь бояться есть, спать, ходить в душ."

    show dv smile pioneer at center with dspr

    dv "Ты ведь не сомневаешься в нашей с Ульянкой изобретательности?"
    "Оригинальная у неё манера просить о чём-то."
    "Я наставил на неё палец."
    me "Ты нас не пужай! Мы ужо пужатые!"

    show dv surprise pioneer at center with dspr

    th "Кажется, эту хохму здесь не слышали."
    "Алиска удивлённо вскинула брови."
    dv "Чего-о-о? Куда-куда жатые?"
    me "Того самого. Не пугай, говорю. {w}А ты о чём подумала, творческая натура?"

    window hide

    show dv laugh pioneer at left with ease

    show mi laugh pioneer close at right with dissolve

    window show

    "Мы с ней хором рассмеялись. {w}Мику присоединилась к нам, деликатно прикрыв ладошкой рот."

    stop music fadeout 3

    show dv smile pioneer close at left
    show mi smile pioneer close at right
    with dspr

    "Кажется, напряжение спадало. Алиса не собиралась отступать и снова подёргала меня за рукав."
    dv "Ну? Какой будет твой положительный ответ?"
    mi "Да, Сеня, что ты решил?"

    hide dv
    hide mi
    with dissolve

    "Алиса смотрела с нажимом, Мику – просительно и ласково."
    th "Кнут и пряник. Хороший коп и плохой коп."
    "Самое смешное, что на самом деле мне очень захотелось согласиться."
    "Ну, вламывать по двенадцать часов в день, конечно, не хотелось. {w}А вот сама идея того, что я кому-то нужен, была непривычна и очень нравилась. {w}Несмотря на то, что перед этим нуждающиеся приласкали меня гитарой по голове."
    th "А может, именно поэтому? Последствия удара и всё такое."
    "Додумать я не успел. Девчонки подхватили меня под руки и вопросительно смотрели в глаза."
    "Стены моего бастиона дали трещину."

    play music music_list["so_good_to_be_careless"] fadein 3

    me "Чёрт с вами, давайте попробуем!"

    window hide

    $ bkrr_get_achievement("bass")

    window show

    "Пионерки пришли в восторг."
    "Алиска изобразила нечто, напоминающее боевой танец индейцев, а Мику просто зааплодировала, предусмотрительно стоя между мной и дверью. {w}Тут она о чём-то вспомнила."

    show dv normal pioneer close at left
    show mi grin pioneer close at right
    with dissolve

    mi "Эй, Алиска?"
    dv "Что?"
    mi "Пирожное давай!"

    show dv grin pioneer close at left with dspr

    dv "Какое пирожное? {w}Микуля, ну откуда я его возьму среди леса-то? Я так сказала, в общем."

    show mi angry pioneer close at right with dspr

    mi "Ничего не знаю, обещала – давай вкусняшку!"

    show dv smile pioneer close at left with dspr

    dv "Ну, скушай мою булочку! И завтра! И послезавтра."

    show mi sad pioneer close at right with dspr

    mi "Я булку не хочу, я от них толстею."

    show mi serious pioneer close at right with dspr

    mi "Гитарист сказал – гитарист сделал! Давай пирожное! А то напишу тебе такую табулатуру на концерт, что пальцы сломаешь играть! Ноты ведь выучить так и не собралась, вот и помучишься."

    show dv guilty pioneer close at left with dspr

    dv "Шантажистка!"

    show mi dontlike pioneer close at right with dspr

    mi "А ты обманщица!"

    show dv normal pioneer close at left with dspr

    dv "Ну ладно, ладно… Я Ольгу Дмитриевну попрошу в городе купить, потерпи."

    show mi smile pioneer close at right with dspr

    mi "Смётано. Но не надейся, что я забуду."

    show dv laugh pioneer close at left with dspr

    dv "«Замётано» надо говорить."

    show mi serious pioneer close at right with dspr

    mi "За-мё-та-но! {w}Но всё равно, не надейся!"

    hide dv
    hide mi
    with dissolve

    th "Девчонки… что с них взять?"
    "Я кое-как почистился от пыли и направился к выходу."

    stop music fadeout 3

    show mi shy pioneer close at center with dissolve

    mi "Сеня! Постой!"
    "Мику ухватила меня за руку, но тут же смущённо отпустила."
    me "Что-то случилось?"
    mi "Случилось…"
    "Мику посмотрела мне на плечо."

    show mi sad_smile pioneer close at center with dspr

    mi "Сень, ты только не ругайся, а?"
    me "А почему я должен ругаться?"
    mi "У тебя это…"
    "Она вздохнула."

    show mi sad pioneer close at center with dspr

    mi "Рубашка. {w}Прости, пожалуйста. {w}Я слишком сильно дёрнула, когда ты убежать хотел, и вот. {w}Порвалась."

    hide mi with dissolve

    "Я пощупал рукав. {w}Шов на плече разошёлся, так что теперь моя форменная белая рубашка с золотыми пуговицами обзавелась дополнительной вентиляцией."
    "Мику так трогательно расстроилась, что я не мог сердиться. Вместо этого улыбнулся и дружески дотронулся до её плеча."
    me "Вечером зашью, минутное дело. {w}Мику, не переживай ты так. Всё равно рубашка не моя, мне её вожатая дала."
    "Алиса покачала головой."

    show dv normal pioneer at center with dspr

    dv "Нет, так ходить нельзя. Дмитриевна увидит – ругаться будет! Надо что-то сделать."
    me "А у вас иголка с ниткой найдутся?"
    dv "Сенька!"
    "Алиса покрутила пальцем у виска."
    dv "Мы же музыкальный клуб!"
    "Она помолчала, улыбнулась и прибавила:"

    show dv smile pioneer at center with dspr

    dv "Конечно, у нас есть иголки и нитки!"
    me "Дай на пять минут, я заштопаю."

    show dv laugh pioneer at center with dspr

    dv "Могу себе представить. {w}Мику, а где твоя коробочка с шитьём? Тащи сюда!"

    hide dv with dissolve

    "Мику полезла в тумбочку и принялась шуршать и рыться там."
    "При этом она наклонилась так сильно, что можно было увидеть плавную линию её тронутых загаром бёдер в промежутке между юбкой и краем чулок."
    "Хотелось верить, что нитки найдутся не сразу, а затеряются где-нибудь в дальнем углу, и поиски затянутся."
    "Увы, меньше чем через минуту раздалось довольное восклицание, и Мику повернулась к нам, показав коробочку с швейными принадлежностями."
    "Я потянулся было к ниткам, но Алиса меня остановила."

    show dv normal pioneer at center with dissolve

    dv "Семён, быть членом нашего кружка – это не только изнурительные репетиции и тяжёлый труд! {w}Это ещё и три прекрасные пионерки… {w}Нет, две с половиной прекрасные пионерки, готовые помочь товарищу в трудную минуту."
    me "Ничего не понял. Переведи."

    show dv grin pioneer at center with dspr

    dv "Ой, Микуля, смотри, какой он сообразительный. Ну просто настоящий басист!"
    me "Алиса, меня гитарой по голове шарахнули, мне простительно. {w}Ты о чём?"

    show dv smile pioneer at center with dspr

    dv "Ой, ну хватит! Я же извинилась! Я это всё к чему… ты рубашку-то снимай!"
    me "Зачем?"

    show dv normal pioneer at center with dspr

    dv "Затем, что Мику у нас не только красавица, она ещё и шить умеет. {w}Да, Микуля?"

    window hide

    show dv normal pioneer at right with ease

    show mi smile pioneer at left with dissolve

    window show

    "Мику оживлённо закивала."
    mi "Умею! У меня в школе только пятёрки по домоводству были, а ещё меня мама учила, я очень хорошо умею! Ну, не так хорошо, как играть, конечно, это ведь совсем другое, хотя и там и там точность движений очень важна. Мама говорит, что нужно разбираться во всех домашних делах, чтобы стать хорошей женой. Так что раздевайся!"
    me "А?"
    th "Какой неожиданный поворот!"

    show dv laugh pioneer at right
    show mi shy pioneer at left
    with dspr

    mi "Ой. Я не то хотела сказать. Ну, вернее, я сказала то, что хотела, просто не имела в виду «полностью», а то подумаешь, что надо всё снимать."
    "Алиса едва сдерживала смех."

    show dv smile pioneer at right with dspr

    dv "Мику имела в виду «снимай рубашку». {w}Погуляешь, она рукав тебе пришьёт."

    show dv grin pioneer at right with dspr

    dv "А вообще, может она хотела тебя целиком осмотреть? {w}Рёбра пощупать, в зубы заглянуть. Я не знаю, как там вообще басистов на базаре выбирают. {w}Мику, ему всё снимать?"
    "Мику помотала головой."

    show mi sad pioneer at left with dspr

    mi "Алиска! Не язви, я просто оговорилась."

    show dv laugh pioneer at right with dspr

    dv "Да? А глазки такие хитрые-хитрые. {w}Ну ладно. Оговорилась, так оговорилась."

    show mi smile pioneer at left with dspr

    mi "Через часик сделаю, хорошо? Или тебе срочно надо? Просто нам нужно ещё кое-что по местам разложить, уже начали, не хочу прерываться, а то настроение пропадёт."
    me "Час? А мне голому всё это время бегать?"

    show dv smile pioneer at right with dspr

    dv "Ну, чего сразу «голому»? Я ж тебе штаны снимать не предлагаю. {w}Вот тебе футболка Толика, наденешь пока. Не кривись, она чистая. Он как раз постирался, хотел в домик забрать. До того, как… всё случилось."
    "Алиса вздохнула. Я почувствовал неловкость. Нужно было хоть что-то сказать."
    me "Вы уж извините, что так вышло."

    show dv smile pioneer at right with dspr

    dv "Да ничего! Ты иди, Ольге Дмитриевне расскажи, что жив-здоров."

    show dv laugh pioneer at right with dspr

    dv "А то, пока ты тут сидишь, Мику не на шитьё смотрит, а на тебя. {w}Пришьёт ещё рукав на спину, тебе ходить неудобно будет."

    show mi angry pioneer at left with dspr

    mi "Алиса!"
    "Мику сделала вид, что сейчас бросит в неё коробкой с нитками."
    dv "Да шучу я, шучу."

    hide dv
    hide mi
    with dissolve

    "Я отошёл в сторону, снял рубашку, натянул безразмерную белую футболку и отправился в наш с Ольгой домик."
    "Нужно было объяснить, что меня взяли в плен и приговорили к двум неделям музыкального образования, а значит, оформлять сцену придётся уже без меня."

    window hide

    stop ambience fadeout 3

    scene bg ext_houses_sunset with fade3

    $ bkrr_set_time("sunset")

    play ambience ambience_camp_center_evening fadein 3

    window show

    "По пути к домику мне встретились Славя и Лена. Славя тут же обеспокоенно подбежала ко мне."

    show sl surprise pioneer close at left
    show un normal pioneer at right
    with dissolve

    sl "Семён, ну как ты? {w}А то я пришла, никого из вас нет, лестница сломанная лежит. Саша с Серёжей говорят, что вас в медпункт унесли обоих. Называется: доверили руководить работами."
    me "Насчёт Толика не знаю, вроде в город на рентген увезут, а я в порядке, не волнуйся."

    show sl tender pioneer close at left with dspr

    sl "Скажешь тоже: «Не волнуйся!». Знаешь, как я испугалась?"
    sl "Нашла тебя у музыканток, но они меня не пустили, сказали, что тебя беспокоить нельзя."

    show sl surprise pioneer close at left with dspr

    sl "А чего тебя туда вообще понесли?"
    me "Не знаю… {w}Они сказали, там нашатырь разбили в медпункте."

    show un serious pioneer at right with dspr

    un "Нашатырь? {w}Странно, я не слышала."

    show un normal pioneer at right with dspr

    un "Ну, неважно. {w}Как твоя голова? Болит? {w}Алиса сказала, ты сильно ей ушибся."
    me "Ерунда. Шишка будет, вот и всё."

    show un serious pioneer at right with dspr

    "Лена очень серьёзно посмотрела на меня и покачала головой."
    un "Виолы до вечера не будет, так что ты смотри, если разболится, приходи, я тебе анальгин дам. {w}А если кружиться начнёт, сразу вожатой говори!"
    me "Да не переживайте вы так."

    show sl shy pioneer close at left with dspr

    sl "Ну, на хозработы мы тебя больше не берём… {w}Как голова пройдёт – приходи, поплаваем, или в волейбол поиграем. Я ведь обещала научить!"
    me "Ой, с этим теперь будет сложно. {w}Меня это… В музклуб записали. Сказали, что будем много репетировать."

    show sl surprise pioneer close at left
    show un surprise pioneer at right
    with dspr

    sl "Вот как?!"
    un "А ты музыкант?"
    me "Нет. Совсем не умею."
    sl "Но тебя в клуб записали."
    me "Ага. Кажется, басистом."

    show sl normal pioneer close at left with dspr

    sl "Понятно… Ну, раз ты так говоришь…"

    show un normal pioneer at right with dspr

    un "Ну… мы пойдём наверное."

    window hide

    hide sl
    hide un
    with dissolve

    $ renpy.pause(1.0, hard=True)

    window show

    "Они отошли на несколько шагов, но я всё же услышал:"
    sl "Странные он вещи говорит. Может, сильно ударился?"
    un "Не знаю. {w}И правда, странно это всё. Может, ему померещилось?"
    "Девушки ушли по своим пионерским делам, а я отправился в наш с Ольгой домик. Хотелось прилечь."

    window hide

    stop ambience fadeout 1

    play sound sfx_open_door_1

    scene bg int_house_of_mt_sunset with fade

    play ambience ambience_int_cabin_evening fadein 3

    window show

    "Голова всё ещё побаливала, да и все эти утренние работы на свежем воздухе забрали кучу сил. Думаю, если я засну на полчасика, никто не будет против."

    window hide

    show blink

    stop ambience fadeout 3

    $ renpy.pause(1.0, hard=True)

    $ bkrr_timeskip()

    scene black

    play ambience ambience_int_cabin_evening fadein 3

    window show

    mt "Лежишь, Семён?"
    me "Угу…"
    mt "Как себя чувствуешь?"

    window hide

    scene bg int_house_of_mt_sunset
    show unblink
    with None

    $ renpy.pause(1.5, hard=True)

    window show

    "Я с удивлением понял, что чувствую себя нормально. Мелькнула мысль, что это мог быть только сон, но стоило дотронуться до места, куда меня стукнули, как…"
    th "Ай! Нет, всё было наяву. Ну, голова не болит, и ладно."
    me "Да вроде нормально, спасибо."

    show mt angry panama pioneer at center behind unblink with dissolve

    mt "Раз нормально, чего режим нарушаем, валяемся на кровати днём?"

    play music music_list["she_is_kind"] fadein 5

    show mt grin panama pioneer at center with dissolve

    mt "Вставай, чай пить будем. С пряниками. Хочешь?"
    me "Очень!"

    window hide

    hide mt with dissolve

    $ renpy.pause(1.0, hard=True)

    window show

    "Ольга налила нам чай, достала из шкафчика пакет со сладостями."

    show mt smile pioneer at center with dissolve

    mt "Давай к столу, говорить будем! Угощайся."
    me "М-м-м… как здорово пахнет. {w}Говорить? А о чём?"
    th "Может, о том, как я сюда попал, и что будет дальше? Пора бы уже!"

    show mt sad pioneer at center with dspr

    mt "Что расскажешь про несчастный случай? А то Славя отлучилась, Алиса путается в версиях, а Толик вообще утверждает, что не понял, как всё получилось. А налицо два пионера: один с ушибами, второй вообще без сознания."
    me "Да глупо как-то всё вышло. Отвлёкся, когда транспарант подавал наверх, толкнул Толика, ну а дальше вы знаете. И сам стукнулся."
    mt "Знаю, знаю. А на что отвлёкся?"
    th "Как же ей объяснить, в самом-то деле? И не придумывается ничего. Не говорить же правду?"
    me "Глупо как-то всё вышло, одно к одному. {w}Тут Алиса, там Толик… как-то окликнули с двух сторон. {w}Я от неожиданности и толкнул лестницу."
    th "Да, вроде правдоподобно."
    me "Можем реконструкцию провести!"

    show mt angry pioneer at center with dspr

    mt "Не надо умничать. Мне ещё отчёт писать."
    mt "Причину надо указать, по которой случился несчастный случай, и принятые меры."

    show mt normal pioneer at center with dspr

    mt "Двачевская говорит, что нечаянно толкнула Толика. И ты говоришь, что нечаянно толкнул Толика. {w}Кто-то из вас врёт, конечно."

    show mt sad pioneer at center with dspr

    mt "Ну, я сама виновата, не уследила. Думаю, всё обойдётся. Чёрт-те как смена началась. То дерётесь, то калечитесь. {w}Ладно, пионеров больше к таким работам не подпускаю, Алиске внушение сделаю. Только не решила, за что: за враньё или за то, что друга с лестницы уронила."

    hide mt with dissolve

    "Она разговаривала больше сама с собой, чем со мной. Явно была расстроена."
    "Вот уж не думал, что в местах вроде этого лагеря тоже есть бумажная возня."
    "Очень захотелось подбодрить и успокоить Ольгу, но нужные слова не нашлись."
    th "Алиса меня выгораживает? Очень мило, но оставить это просто так нельзя. Сам не знаю, почему."
    me "Ольга Дмитриевна…"

    stop music fadeout 3

    show mt normal pioneer at center with dissolve

    mt "Да?"
    me "Тут такое дело… {w}Алиса соврала. Она не толкала лестницу, это я."

    show mt grin pioneer at center with dspr

    mt "Вот как?"
    me "Угу. Не наказывайте её, пожалуйста."

    show mt normal pioneer at center with dspr

    mt "Вот уж не думала, что Двачевская будет за кого-то вступаться. {w}Интересно, почему?"

    show mt smile pioneer at center with dspr

    mt "Ну ладно, так и напишем: внезапный приступ головокружения. Убедительно звучит?"
    me "Ещё как. Могу добавить объяснительную. {w}Хотите? {w}Я здорово умею."

    show mt laugh pioneer at center with dspr

    mt "Такой молодой, а уже бюрократ."

    show mt normal pioneer at center with dspr

    mt "Нет, пока не нужно."

    show mt smile pioneer at center with dspr

    "Ольга помассировала виски, потом устало улыбнулась."
    mt "И ещё. Боишься высоты, воды, темноты, клоунов – не надо стесняться, надо было сказать."

    show mt sad pioneer at center with dspr

    mt "Ладно, у Толика просто сильный ушиб, а если бы ты сам упал?"
    mt "Что мне потом с тобой делать? И ещё вопрос. Ты говоришь, голову ушиб транспарантом. {w}Тут говорят, что она тебя гитарой ударила, да так, что ты сознание потерял. Это правда?"
    me "Да ну… Она скорее своим телом гитару прикроет."
    me "Ломать инструмент об мою голову? {w}Даже представить не могу. Это я Толика поймать пытался, стукнулся."

    show mt normal pioneer at center with dspr

    mt "Ладно, так и запишем."
    me "А насчёт «что делали бы», я не думаю, что меня кто-то искать будет. {w}Да вы и сами знаете."
    me "Подозреваю, что даже документов на меня нет, верно?"
    "Как обычно, когда я задавал подобные вопросы, Ольга Дмитриевна мастерски притворилась обычной вожатой."

    show mt surprise pioneer at center with dspr

    mt "Не понимаю я тебя, Семён! Шуточки у тебя."

    show mt grin pioneer at center with dspr

    mt "Все документы есть. Не из леса же ты появился?"
    me "Как скажете…"

    show mt smile pioneer at center with dspr

    mt "Как скажу? {w}Вот как я скажу."
    mt "Иди-ка ты ужинать! Аппетит не испортил сладким?"
    me "Нет, спасибо! Мой аппетит он такой! Его не перебить!"
    mt "Тогда беги. {w}Вернёшься – не шуми, я лягу пораньше. Если что – все ключи у Слави, меня не будить. Устала я сегодня – сил нет."
    me "Хорошо! Может, вам принести что-то из столовой?"

    show mt grin pioneer at center with dspr

    mt "Не нужно. Но спасибо, что предложил. Очень мило с твоей стороны."

    show mt smile pioneer close at center with dspr

    "Ольга взъерошила мне волосы."
    th "Давненько мне так не делали, наверное, с самого детства."
    "Я почувствовал, что краснею. С чего бы вдруг?"

    window hide

    stop ambience fadeout 2

    $ bkrr_timeskip_short()

    scene bg ext_dining_hall_near_sunset with bkrr_timeskip_transition()

    play music music_list["gentle_predator"] fadein 3

    play ambience ambience_camp_center_evening fadein 3

    window show

    "После ужина меня крепко взяли в оборот."
    "Первой успела Славя."

    show sl tender pioneer at cleft with easeinleft

    sl "Семён, раз у меня тут кое-что недоделанное осталось. Может, закончим сегодня?"
    me "Славя, не могу, меня…"

    show mz angry glasses pioneer at cright with easeinright

    mz "Его я пригласила!"
    "Вмешалась Женя."
    mz "У меня полки двигать нужно! Так что извини, попользовалась сама – уступи другому!"
    me "Жень, я тоже не смогу, у меня…"

    show sl tender pioneer at left
    show mz angry glasses pioneer at right
    with ease

    show dv smile pioneer2 close at center with dissolve

    dv "Девчата, Семён поступает в собственность музыкального клуба, так что кто не успел, тот опоздал."
    "Отстранила их Алиса."

    show sl serious pioneer at left with dspr

    sl "А вожатая в курсе?"
    "Поинтересовалась Славяна."

    show dv laugh pioneer2 close at center with dspr

    dv "Вожатая? {w}Она не возражала."

    show sl surprise pioneer at left
    show mz bukal glasses pioneer at right
    with dspr

    sl_mz_s "Ладно…"
    "Разочарованно вздохнули пионерки."
    dv "Где эта Мику делась? {w}Тебя же чуть не увели из-под носа!"

    show sl surprise pioneer at offscreenleft
    show mz bukal glasses pioneer at offscreenright
    with ease

    "Алиса отстранила Женю и Славю, подхватила меня под руку и потащила в музкружок."

    stop music fadeout 3

    stop ambience fadeout 3

    window hide

    scene bg int_music_club_mattresses_sunset with fade3

    play ambience ambience_music_club_night fadein 3

    window show

    "Мику уже сидела там, с аппетитом грызя большое румяное яблоко. {w}Увидев нас, помахала и попыталась поздороваться. Вышло мило, но не очень разборчиво."

    show mi normal pioneer at center with dissolve

    mi "Ммммф-ммммм-Смммн!"
    me "Приятного аппетита!"

    show mi happy pioneer at center with dspr

    mi "Ффппфба!"

    hide mi with dissolve

    "Мику отложила яблоко, сбегала к вешалке на стене и принесла мне рубашку."
    "Я потрогал пальцем шов и с восхищением посмотрел на стоящую рядом девушку."

    show mi normal pioneer at center with dissolve

    me "Потрясающе! Будто так и было. Спасибо тебе большое!"

    show mi sad_smile pioneer at center with dspr

    mi "Пожалуйста! Извини, только белых ниток не было, я светло-серыми зашила, если изнутри смотреть, то видно будет. Ничего? Или я завтра в кройке и шитье возьму белые. Просто хотела побыстрее, а получилось…"
    "Я покачал головой."
    me "Если бы ты не сказала, я бы и не заметил. Просто замечательно."

    show mi smile pioneer at center with dspr

    me "Ну, что теперь?"

    window hide

    show mi smile pioneer at cright with ease

    show dv normal pioneer2 at cleft with dissolve

    window show

    dv "Теперь ждём недостающих… {w}и начинаем!"
    me "А кого именно мы ждём?"

    show mi normal pioneer at cright with dspr

    mi "Ульяну, конечно. Вообще ещё Толик должен был, но он…"

    window hide

    hide mi
    hide dv
    with dissolve

    stop ambience fadeout 3

    play music music_list["two_glasses_of_melancholy"] fadein 3

    $ bkrr_set_mode(nvl)

    window show

    "Как оказалось, кроме Мику, в музыкальном кружке «Совёнка» состояли Толик, Алиса и Ульяна. {w}Толик временно выбыл, остальные же каждый день сыгрывались, готовясь поразить всех слушателей на закрытии смены. {w}Ульяна, конечно, говорила, что репетирует, но, пока сам не убедился – не верил. {w}Ульяна и усидчивость? {w}С другой стороны, кого и представить барабанщицей, как не эту егозу?"
    "Ещё путём шантажа был почти завербован Электроник. {w}Накануне в душе он чистым красивым голосом распевал «О соле, о соле мио!». {w}Какая неосмотрительность… {w}Особенно если учесть, что в кустах возле душевой совершенно случайно оказались Алиса и Ульяна."
    "Разумеется, кибернетика тут же добровольно-принудительно записали в ансамбль на подпевку. {w}Кажется, даже не дав одеться. {w}Правда, от пения Серёжке удалось увильнуть под предлогом ремонта радиовещания лагеря, но взамен его обязали починить некстати сгоревший усилитель, пообещав в противном случае рассказать всем, как он голый приставал к Ульяне."

    window hide

    $ renpy.pause(1.0, hard=True)

    stop music fadeout 3

    play ambience ambience_music_club_day fadein 3

    show dv normal pioneer2 at cleft
    show mi normal pioneer at cright
    with dissolve

    $ bkrr_set_mode()

    window show

    dv "Ну, начинайте уже планёрку, да давайте поиграем! Микуля, что там у тебя?"
    mi "Но Ульяны ещё нет…"

    show dv laugh pioneer2 at cleft with dspr

    dv "Она тебя хоть раз слушала?"

    show mi sad pioneer at cright with dspr

    mi "Вообще-то нет."
    dv "Вот без неё и поговорим."

    show dv smile pioneer2 at cleft with dspr

    dv "Ну, рассказывай, что выходила?"

    show mi smile pioneer at cright with dspr

    mi "Я говорила с Ольгой Дмитриевной! Нам дадут сыграть пять песен."
    mi "Она сначала хотела три, но я начала объяснять, что три это мало, и надо пять, что у нас много планов, что у нас большой творческий по-тен-ци-ал… {w}Тут Ольга Дмитриевна почему-то заторопилась, сказала: «Да пойте, что хотите, пойте пять!» и убежала. Спешила, наверное. Может, по делам…"

    show mi normal pioneer at cright with dspr

    mi "Но вот мне дали сетку концерта. Там, где пустые строчки, там надо вписать, что мы будем играть."

    show dv guilty pioneer2 at cleft with dspr

    "Алиса покачала головой."
    th "Да уж, Мику в больших дозах переносить непросто. Скорее всего, вожатая согласилась бы и на десять песен, лишь бы сбежать."

    window hide

    $ renpy.pause(1.0, hard=True)

    play sound sfx_slam_door_campus

    play music music_list["i_want_to_play"]

    window show

    "Раздался топот, и в клуб галопом влетела Ульянка с охапкой… журналов? {w}Хм-м… Неожиданное сочетание."

    hide dv
    hide mi
    with dissolve

    show us smile pioneer at center with dissolve

    us "Алиска! Толик! Мику! Совещаетесь уже? {w}А почему без меня?"

    show us normal pioneer at center with dspr

    us "А где Толик?"

    show us laugh pioneer at center with dspr

    us "Микуська, я библиотеку ограбила! {w}Смотри, сколько музыкальных журналов, тут точно есть хорошие песни! Женя упиралась, говорила, что больше трёх изданий в одни руки не даёт! Но я её убедила!"

    show us grin pioneer at center with dspr

    us "Ульянка – молодец!"

    show us surp1 pioneer at center with dspr

    us "Ой, Семёныч, привет! А ты здесь что делаешь?"

    show us laugh pioneer at center with dspr

    us "Решил-таки меня снасильничать? Алиска, Микуля, спасите-помогите! Он маньяк! И отшлёпать хотел!"
    "Мику открыла было рот, чтобы начать объяснять, но Алиса быстро перехватила инициативу."

    window hide

    show us laugh pioneer at right with easeinright

    show dv normal pioneer2 at left with dissolve

    window show

    dv "Это наш новый басист. Толик руку поранил, его в город увезли на рентген. Играть, наверное, не сможет. Ольга Дмитриевна сказала, ушиб."

    stop music fadeout 3

    show us sad pioneer at right with dspr

    "Ульяна сразу поутихла, окинув меня недоверчивым взглядом."
    us "Бедный Толя. А я думала, куда он делся. {w}Ужин пропустить – это на него не похоже."

    show us dontlike pioneer at right with dspr

    us "Погоди-погоди… {w}Басист? {w}Этот? {w}А он умеет вообще? {w}Сенька, ты что, играешь?"
    me "Нет."
    "Честно признался я."

    show us sad pioneer at right with dspr

    us "Ничего не пойму. Тогда как?"

    show us smile pioneer at right with dspr

    us "А-а-а, знаю! {w}Ты пустишь магнитофон, а его с гитарой на сцену выпустишь? Для декорации? Да? {w}Угадала?"

    show dv smile pioneer2 at left with dspr

    dv "Улька, гений, белка ты моя! Надо было так и сделать. {w}Но поздно. Мы с Мику уже поспорили."

    show dv normal pioneer2 at left with dspr

    dv "В общем, я его буду учить. И Мику. И ты, рыжая."

    show us upset pioneer at right with dspr

    us "Сама рыжая! А у меня красивый цвет закатного солнца, мне так мама говорила!"

    show dv grin pioneer2 at left with dspr

    dv "Я не рыжая, я золотая! А от тебя костёр разводить можно! Где лопата, которой ты убила дедушку?"

    show us dontlike pioneer at right with dspr

    us "Щас укушу!"

    show dv normal pioneer2 at left
    show us sad pioneer at right
    with dspr

    "Ульянка вполне натурально оскалилась. Потом, кажется, до неё дошёл смысл Алисиных слов."

    show us surp2 pioneer at right with dspr

    us "УЧИТЬ?"

    show us dontlike pioneer at right with dspr

    us "Алис, а ты на солнышке не перегрелась? Концерт же через две недели. {w}Даже меньше."

    show us smile pioneer at right with dspr

    us "Нет, на сцене он корячится красиво, я видела… Но там же надо ещё и струны дёргать?"
    th "Кажется, моя клоунада на сцене и игра на воображаемой гитаре больше не секрет."

    show dv smile pioneer2 at left with dspr

    dv "Не боись, подруга! Нам ведь не рок-звезду надо вырастить. А две-три простые песенки можно и макаку научить играть. {w}Особенно на басу."
    dv "А Сенька-то наш поумнее макаки будет. Ну, может, и не умнее, но не сильно глупее – точно."

    show dv laugh pioneer2 at left
    show us laugh pioneer at right
    with dspr

    "Я возмутился:"
    me "Эй, кто тут глупее макаки? Может, хамить не будем? И кстати, что это за спор такой?"

    show dv smile pioneer2 at left
    show us smile pioneer at right
    with dspr

    dv "Сеня, ты ещё право голоса не заработал! Твоё дело сейчас не вопросы задавать, а учиться играть! Времени мало!"

    window hide

    hide us
    hide dv
    with dissolve

    $ renpy.pause (1.0, hard=True)

    play music music_list["silhouette_in_sunset"] fadein 3

    window show

    "Такие дела."
    th "Кажется, в иерархии группы мне отвели место где-то между котом Пиратом и гиацинтом на подоконнике. Невесело. Может, сбежать?"
    th "Да как можно выучиться чему-то за две недели? И о чём я вообще думаю, – какая учёба, какой концерт?"
    th "Надо путь отсюда искать! Ну, или хотя бы понять, куда меня забросило. Но, по-моему, за меня всё уже решили."
    "Словно уловив это пораженческое настроение, Мику присела рядом и погладила меня по руке."

    show mi sad_smile pioneer close:
        center
        zoom 1.1
    with dissolve

    mi "Ты не слушай, на самом деле они хорошие, просто шутят так. Не бойся, у тебя всё получится! Мы тебе все поможем!"
    me "Да я не то, чтобы боюсь. Подвести вас не хочу. Я ведь бас даже в руках не держал."

    show mi smile pioneer close:
        center
        zoom 1.1
    with dissolve

    mi "Не подведёшь! Я в тебя верю, и Алиса тоже. И Ульяна. Наверное. Ну, во всяком случае, немножко. А гитару завтра подержишь, нам не жалко."

    hide mi with dissolve

    show dv normal pioneer2 at center with dissolve

    "Алиса с очень серьёзным лицом добавила:"
    dv "Будешь хорошо себя вести – даже ручки покрутить дадим!"
    me "Ну, хорошо. А что играть-то будем?"
    dv "Вот, решаем как раз. Сегодня утвердим, и начинаем усиленно разучивать."
    dv "Значит… {w}что тут у нас? Мику, что Ольга Дмитриевна сказала?"

    window hide

    show dv normal pioneer2 at left with ease

    show mi normal pioneer at right with dissolve

    window show

    mi "Никакой иностранщины – это раз."

    show dv guilty pioneer2 at left with dspr

    dv "Кисс отпадает, я поняла. Вычёркиваем."
    mi "Песен про насилие, взрослые темы – тоже нельзя."

    show dv sad pioneer2 at left with dspr

    dv "Да что такое? Вычёркиваем. Раз, два… Ещё что?"
    mi "Ещё…"

    hide dv
    hide mi
    with dissolve

    "По мере того, как Мику объясняла условия, Алиса мрачнела."

    stop music fadeout 3

    "Наконец, она отшвырнула карандаш, чуть не выколов глаз Бетховену на стене."

    show us sad pioneer at center with dissolve

    us "Алиска, а ты чего?"

    hide us with dissolve

    show dv angry pioneer2 at center with dissolve

    dv "Все эти условия меня бесят! Всё понятно. Играем «Антошка, пошли копать картошку!». Пять раз."
    me "Э-э-э… а что ты вообще хотела бы?"

    show dv guilty pioneer2 at center with dspr

    dv "Не знаю я. Но уж точно не «вместе весело шагать по просторам». {w}Рок хочу. Чтоб энергетика была, знаешь, быстро, ритмично, чтоб в зале все подскочили и начали подпевать. Ну или хотя бы руками замахали."

    show dv normal pioneer2 at center with dspr

    dv "Киссов там или Кино. Или пинкфлойдов. И чтоб соло гитарное на пять минут. И я такая… Вся в чёрном… А в динамиках басы ревут, публика руками машет."

    hide dv with dissolve

    "Как и тогда, на сцене, Алиса мечтательно прикрыла глаза, в руках она сжимала воображаемый инструмент и энергично перебирала воображаемые же струны. Пришлось внести немножко реализма."
    me "Ого? А сыграть справитесь? Ну хотя бы «Кино»?"

    show dv normal pioneer2 at center with dissolve

    dv "Да запросто! Мы тебе не ансамбль песни и пляски «Капитошка»! Мику на слух партии расписывает, я сама обалдела, когда увидела."
    dv "И я гитару не первый день в руках держу. {w}Ульяна – ударник от природы, ну это ты ещё услышишь. {w}Толик там у себя в какой-то группе играл, показывал, что и как. Главное песни по-быстрому подобрать, а там справимся."

    window hide

    hide dv with dissolve

    play sound bkrr_sfx_list["ba_dum_tsss_piano"]

    $ renpy.pause(1.0, hard=True)

    window show

    "Мику и Ульяна молча кивнули и синхронно сделали «тыдымс» на тарелках и рояле."
    th "Ясно. {w}Кажется, их девиз «ввяжемся в бой, а там поглядим!»."
    "Не знаю, что они там готовили, но репертуара ещё нет. А вообще, что можно сыграть на пионерском празднике? {w}В голове завертелись старые советские фильмы, потом вспомнились старые же песни."
    "Это наводило меня на интересную мысль."
    th "Если Мику сможет расписать музыку…"
    "Обмозговав задумку так и эдак, я подал голос."
    me "Девчата, у меня тут идея есть. Насчёт песен."
    "Алиса бросила на меня взгляд из-под рыжей чёлки."

    show dv laugh pioneer2 at center with dissolve

    dv "Только пришёл, а уже идея у него. {w}Боюсь даже представлять, какая именно. Ну, давай, излагай."

    show dv grin pioneer2 at center with dspr

    dv "Не «лунную сонату», надеюсь? И не битлов, битлы устарели."
    me "Не язви! Только мне надо в домик смотаться, в вещах лежит кое-что, что нам поможет. Если только дома не оставил."

    show dv smile pioneer2 at center with dspr

    dv "Ага-ага. Лежит. Что-то. Семён, а не сбежать ли ты планируешь? {w}Ты же не обманешь трёх доверчивых девочек?"
    me "Слово царя – твёрже сухаря! Не сбегу, не бойся. Я ведь обещал."

    show dv normal pioneer2 at center with dspr

    dv "Вот не верю! Мику, Ульянка, может, всё-таки проводите его, а то, боюсь, сбежит. Сильно честное лицо у него. {w}Как по-вашему?"

    hide dv with dissolve

    show mi dontlike pioneer at center with dissolve

    mi "Хорошее лицо у него, не надо!"
    "Заступилась за меня Мику."

    hide mi with dissolve

    show us smile pioneer at center with dissolve

    us "И правда, рожа хитрющая."
    "Не согласилась Ульяна."
    us "Только мне туда-обратно бегать лениво. На часы глянь, спать скоро. Может, привяжем его на верёвочку? А потом назад втянем."
    "Я не выдержал, рассмеялся."
    me "Да вернусь я, хватит уже!"

    hide us with dissolve

    show dv normal pioneer2 at center with dissolve

    dv "Точно? Ну ладно…"
    "Алиса отбросила командный тон и почти ласково попросила:"
    dv "Сень, ты возвращайся только поскорее, ладно? Время позднее, спать уже хочется."

    hide dv with dissolve

    "Может ведь быть милой, когда хочет. Жалко, хочет редко."

    window hide

    stop ambience fadeout 3

    scene bg ext_house_of_mt_sunset with fade3

    play ambience ambience_camp_center_evening fadein 1

    window show

    "Как бы то ни было, я вернулся к нашему с Ольгой домику."

    window hide

    stop ambience fadeout 0.5

    play sound sfx_open_door_1

    scene bg int_house_of_mt_sunset with dissolve

    play ambience ambience_int_cabin_evening fadein 3

    window show

    "Там, в кармане пальто, лежал мой mp3-плеер. {w}Тяжеловато будет объяснить, что это такое, но совру что-нибудь про микрокассету внутри."
    "К счастью, модель была старенькая, массивная. {w}Как и телефон, который я не менял уже лет восемь."
    "Тихонько, чтобы не разбудить соседку по комнате, я полез в карман пальто. Прикосновение к предмету из будущего напомнило, что я вообще-то не отсюда."
    th "Что я делаю вообще?"
    th "Я правда собираюсь учиться играть на гитаре для участия в пионерском концерте? Да ещё и с этой рыжей доставалой?"
    th "Получается, да. Ведь там будет…"
    me "Мику…"

    window hide

    $ renpy.pause(1.0, hard=True)

    window show

    "Предвкушая смесь удивления и восторга на лицах пионерок, особенно у Мику, я нашаривал плеер. {w}Странно, но его там не оказалось."
    "Ладно, этому я сильно не удивился. {w}Но карман и не пустовал. Вместо плеера там лежали две магнитофонные кассеты. {w}МК-60."

    window hide

    $ bkrr_get_item("tape")

    window show

    "Когда-то у меня были такие. Папа на них записывал «Любэ», Газманова и прочие песни времён перестройки."
    "Почему-то стало очень обидно. Раз уж чудеса происходят, то они могли бы стать хромовыми TDK, BASF, ну «Сони» на худой конец. {w}Нет, самые хреновые советские кассеты."
    "Хотя, если учесть, в какую технику их тут предстоит совать, то, может, и к лучшему. Кажется, нежные немецкие плёнки на раз жевались советскими магнитофонами."
    th "Что за бред?"
    "Мобильник остался мобильником, дешёвый китайский фонарик на ключах тоже. А плеер стал кассетами. Всё просто и логично."
    th "Может, всё-таки я сплю?"
    "На всякий случай я крепко ущипнул себя за бедро."
    th "Больно! Ладно, не сон."
    "На вкладышах в подкассетниках прыгающим почерком было расписано содержимое."
    "Саундтреков к аниме в списке не было, групп из моего времени тоже. {w}Зато целая куча ретро-песен, которые я обычно пролистывал."
    "Особенно порадовали песни из детских фильмов в рок-обработке. {w}Думаю, это как раз то, что мы ищем, и рок, и детская тематика, не придерёшься. Надеюсь, девочкам понравится."

    window hide

    $ renpy.pause(1.0, hard=True)

    window show

    "Ольга Дмитриевна заворочалась во сне."
    mt "Виола, не надо! Не трогай меня!"
    "Человек или нет, но во сне она выглядела так мило."
    "Я с трудом подавил желание поглазеть подольше. Всё-таки надо думать головой, а не чем-нибудь ещё."
    "Ещё немного полюбовавшись на спящую вожатую, я выбрался наружу."

    window hide

    stop ambience fadeout 0.5

    scene bg ext_house_of_mt_sunset with dissolve

    play ambience ambience_camp_center_evening fadein 1

    window show

    "Вслед донеслось:"
    mt "Ну что ты такое делаешь?! Прекрати!"

    window hide

    play sound sfx_close_door_1

    $ renpy.pause(1.0, hard=True)

    stop ambience fadeout 3

    scene bg int_music_club_mattresses_sunset with fade3

    play ambience ambience_music_club_night fadein 3

    window show

    "Несмотря на позднее время, Алиса всё ещё сидела в кружк{b}е{/b}."
    "Рояль всё так же был завален хламом, на этот раз – музыкальными сборниками, что притащила Ульянка. Объедки куда-то делись."
    "В руках у Алисы снова была гитара, на этот раз обычная, акустика. Рыжая пионерка тихонько перебирала струны, напевая вполголоса."
    "Она, не прерываясь, кивком показала, чтобы я присаживался, и продолжила играть."

    window hide

    scene cg d6_dv_guitar at d6_dv_guitar_atl with dissolve

    window show

    "Песня оказалась знакомой, «Браво» мне нравилось, и эта песня была одной из любимых."
    "В женском исполнении она почему-то звучала печальнее, чем в мужском. Словно грустный монолог брошенной девушки."
    "Я заслушался."

    window hide

    stop ambience fadeout 3

    play sound bkrr_music_list["how_sad"] fadein 3

    $ renpy.pause(12.0)

    show bkrr_lyrics_screen with bkrr_blindstotop_transition

    show bkrr_song "На тёмный ряд домов\n\nЛишь одинокий свет в окне,\n\nИ стук моих шагов\n\nЗвучит в полночной тишине.\n\n\nПо этой мостовой,\n\nВдоль этих скверов до утра\n\nБродили мы с тобой,\n\nИ это было как вчера.\n\n\n\nКак жаль, но ты сегодня не со мной,\n\nИ только каждый раз,\n\nКогда иду по этой мостовой,\n\nЯ думаю о нас.\n\n\nВсё так же, как тогда,\n\nТакой же мягкий лунный свет.\n\nБлестит в реке вода,\n\nИ лишь тебя со мною нет.":
        xalign 0.5
        ypos 1.0
        linear 35.0 ypos -2.0

    $ renpy.pause(35.0)

    hide bkrr_lyrics_screen
    hide bkrr_song
    with bkrr_blindstobottom_transition

    stop sound fadeout 5

    play ambience ambience_music_club_night fadein 3

    window show

    "На последнем куплете она сильно сфальшивила, выругалась вполголоса, переиграла его ещё раз. {w}И ещё."
    "Закончив, Алиса опёрлась подбородком на гитару и молча посмотрела на меня."

    window hide

    scene bg int_music_club_mattresses_sunset with dissolve

    window show

    me "Красиво поёшь! Только грустная песня, не ожидал от тебя такой… {w}лирики."
    me "Думал, для себя играешь что-то более тяжёлое."

    show dv smile pioneer2 at center with dissolve

    "Она улыбнулась без своего обычного нахальства, шутливо отмахнулась."
    dv "Ай, что ты там понимаешь. {w}«Лирика»."
    dv "Это же блюз!"
    me "Как скажешь. Всё равно здорово."

    show dv normal pioneer2 at center with dspr

    dv "Спасибо за похвалу."
    dv "Ты всё-таки вернулся? {w}Я думала, спать ляжешь."
    me "Я же обещал."

    show dv guilty pioneer2 at center with dspr

    dv "Это не обязательно значит, что обещание выполнят, знаешь ли."
    me "Знаю. Но я, если обещаю, стараюсь выполнять."
    dv "Все вы так говорите. А потом в кусты."

    show dv normal pioneer2 at center with dspr

    dv "Ты вот обещал научиться. {w}Сможешь, как думаешь?"
    "Я подумал и честно ответил:"
    me "Ну, пока не услышал, что даже ты можешь сфальшивить, думал, не смогу. Теперь почти уверен, что получится."

    show dv guilty pioneer2 at center with dspr

    "Алиса напустила на себя оскорблённый вид."
    dv "Эй, кто тут фальшивит? Это атональная импровизация! {w}Эх, село ты неасфальтированное!"

    hide dv with dissolve

    "Забавно было слышать это от малолетки из какого-то провинциального городка в далёком прошлом."
    th "Показал бы я тебе интернет, да посмотрел бы на твои глаза по пять копеек."
    "Я даже обидеться не сумел как следует. Вообще, то ли возраст тому виной, то ли вся эта уютная обстановка, но я стремительно утрачивал умение злиться."
    "Даже когда Ульяна обрушила на меня тарелки, я ворчал на неё скорее для порядка, чем по-настоящему. {w}Вот и сейчас… Вместо того, чтобы разозлиться, мне стало весело."
    me "А, извини. Я таких умных слов не знаю. Выглядело как косяк в аккорде."

    show dv smile pioneer2 at center with dissolve

    dv "Сильно ты ушастый, Сёма. А с чего ты взял, что раз я сфальшивила, то ты сможешь сыграть?"
    me "Не знаю, как объяснить."

    show dv normal pioneer2 at center with dspr

    dv "Давай, как сможешь."
    "Казалось, её забавляла роль наставницы."
    me "Ну, чтобы сыграть, мне надо до вашего уровня подтянуться. Мику ошибок делать не умеет. Играть, как она, я никогда не смогу."

    show dv smile pioneer2 at center with dspr

    dv "Я бы очень удивилась, если бы смог. И что с того?"
    me "А вот ты играешь здорово, но можешь ошибаться. И думаю, что играть, как ты, я смогу научиться."
    me "Не знаю, за две недели или нет, но с тобой можно соревноваться и к твоему уровню можно стремиться. Как-то так."

    show dv grin pioneer2 at center with dspr

    dv "Ты как Мику прямо. Она тоже говорит-говорит, слова понятные, а спроси, о чём она, – и не поймёшь."
    dv "Давай без виляний. Сможешь или нет?"
    me "Сделаю всё, что смогу. За две недели не обещаю, но постараюсь."
    "Я почти поверил в свои слова, но мысленно добавил:"
    th "Только отвяжись."

    show dv smile pioneer2 at center with dspr

    dv "Не пойдёт! Надо чтоб не просто смог, а смог на концерте, иначе и начинать не стоит."
    dv "Кстати, о практике… {w}Мику там говорила, ты ей играл что-то. Да ещё и не сильно коряво."
    me "Было такое."

    show dv grin pioneer2 at center with dspr

    dv "А ну, сбацай-ка мне! Или слаб{b}о{/b}?"

    hide dv with dissolve

    th "Играть перед этой язвой? Как-то неуютно."
    th "Но какого чёрта, ей от силы шестнадцать и даже если я не справлюсь, то никто меня тут не держит в случае чего."
    th "Зато если выйдет нормально… {w}Может, доставать перестанет?"
    me "Не слаб{b}о{/b}."
    me "Только не ржать в случае чего. Я не волшебник, я только учусь."
    dv "Играй, играй, там посмотрим."

    window hide

    scene cg d6_sem_guitar with dissolve

    window show

    "Я принял гитару, ещё тёплую от её тела."
    "Мотив очень простой, напортачить в нём почти невозможно."
    "Я прогнал его дважды, закончил довольно чистым аккордом и вопросительно глянул на Алису."

    window hide

    scene bg int_music_club_mattresses_sunset
    show dv grin pioneer2 close at center
    with dissolve

    window show

    dv "Хм… А ну, дай сюда!"

    window hide

    scene cg d6_dv_guitar with dissolve

    window show

    "Она сделала неопределённый жест рукой и отобрала гитару назад."
    "Взяла пару аккордов и изобразила что-то очень похожее на то, что я играл. {w}Только гораздо лучше, чище и красивее."
    dv "Вот так."
    me "Красиво!"

    window hide

    scene bg int_music_club_mattresses_sunset
    show dv normal pioneer2 close at center
    with dissolve

    window show

    dv "Да ничего особенного."
    dv "Ну, я ожидала худшего. Так себе, если честно."
    dv "Играешь одним пальцем, но слух есть, ритм держишь, да и руки поставлены более-менее."

    show dv smile pioneer2 close at center with dspr

    dv "Работы непочатый край. Если тебя гонять как следует, то сможешь. {w}Медиатором не умеешь?"
    me "Медиатором? {w}Ну, немного. {w}Совсем немного."
    dv "Плохо. Переучивать уже некогда."
    dv "Ладно, на этом полене и пальцами сойдёт. Сколько учился-то?"
    me "Года полтора, но давно. Пару лет гитару не держал."
    dv "Ну, мог и не говорить, это и так видно. {w}Ладно, на крайний случай, возьмём обезьяну."
    "Она улыбнулась почти по-дружески."
    me "Слушай, хватит уже! Не всем быть музыкантами."

    show dv laugh pioneer2 close at center with dspr

    dv "Вот отговорок не надо. А ну-ка, попробуй аккорды позажимать, я послушаю."

    window hide

    stop ambience fadeout 3

    $ bkrr_timeskip()

    scene bg int_music_club_mattresses_night with bkrr_circleout_transition

    $ bkrr_set_time("night")

    play ambience ambience_music_club_night fadein 3

    window show

    dv "Хватит, хватит! Пощади мои уши."
    "Я, конечно, понимал, что умею чуть больше, чем ничего, но всё-таки подсознательно надеялся, что сейчас она посмотрит на меня со смесью удивления и восхищения, возьмёт за руки и будет сбивчиво говорить, что такого гитариста видит впервые, и что это самая чудесная мелодия, которую она слышала. {w}И повиснет на шее, радостно повизгивая."
    "Увы, чуда не произошло. {w}Предсказуемо."
    "Янтарно-коричневые глаза насмешливо буравили меня."

    show dv grin pioneer2 at center with dissolve

    dv "Обиделся?"
    dv "Ну, сходи в уголок, пореви, если что. Я не говорю, что руки совсем кривые. {w}Для Васи с улицы – неплохо. Чтобы играть в группе – слабо."
    me "Да ладно, я всё понял. Значит, учёба отменяется?"

    show dv laugh pioneer2 close at center with dspr

    "Алиса присела рядом и внезапно звонко рассмеялась, хлопнула меня по спине."
    dv "Размечтался! Ну, не хмурься ты."
    dv "Выучим мы тебя, Сенька! Будешь ты у нас двести пятьдесят шестые ноты играть только так. Главное, не сдувайся сразу."
    me "Тебя не поймёшь. То смогу, то не смогу."
    me "Вы, девушки, вообще говорите что-нибудь напрямую?"

    show dv normal pioneer2 close at center with dspr

    dv "Не-а! Никогда! Так интереснее. {w}Ты, кстати, принёс, что обещал?"
    me "Да, вот."
    "Я помахал кассетами."
    me "А где девчонки?"
    dv "Спать пошли, где же ещё? {w}На часы глянь. Девятый час."
    me "А ты?"

    show dv smile pioneer2 close at center with dspr

    dv "А я – «сова». {w}Вечером не уложишь, утром не добудишься."
    dv "Давай, оставляй свои кассеты, завтра все вместе послушаем."

    show dv grin pioneer2 close at center with dspr

    "Алиса сладко потянулась."
    dv "Пойду-ка я, проветрюсь перед сном."

    show dv normal pioneer2 close at center with dspr

    dv "Эта жара просто убивает, только ночью и можно погулять. Ну и утром ещё, пока духота не началась."
    me "Мимо душевых?"
    "Я подмигнул."

    show dv angry pioneer2 close at center with dspr

    dv "Эй, ты на что намекаешь, наглая морда?"
    dv "Я тогда просто мимо шла!"
    "Алиса изобразила оскорблённую невинность."
    dv "Очень мне надо подсматривать. Да и не за кем… {w}уже."
    me "Конечно-конечно. {w}А когда Электроник голышом пел, вы с Ульяной, наверное, в кустах у душевых собирали гербарий. {w}Или ловили бабочек? {w}Или Чёрную Вожатую?"

    show dv laugh pioneer2 close at center with dspr

    "Она рассмеялась. {w}Странно."

    hide dv with dissolve

    "Ещё утром я настороженно относился к этой рыжей, в обед она злилась на меня и чуть не проломила голову."
    "А теперь вот дружески болтаем, словно знакомы уже не один год. Не припомню, чтобы я так легко сходился с людьми. Раньше я вообще многого не делал из того, что здесь получается легко и свободно."

    window hide

    $ renpy.pause(1.0, hard=True)

    window show

    "Видимо, я задумался. Алиска уже уложила гитару в стойку и стояла в дверях."

    show dv normal pioneer2 close at center with dspr

    dv "Эй, басила! Ты идёшь? Сейчас фонари погасят."

    play sound bkrr_sfx_list["box_fall"]

    show dv scared pioneer2 close:
        center
        ease 0.75 zoom 1.2
        ease 0.25 zoom 1.15
    with dspr

    "Я заторопился следом, но в темноте споткнулся обо что-то, полетел вперёд и, чтобы не упасть, опёрся на стену рядом с ней."
    "Наши лица оказались так близко друг к другу, что почти соприкасались."
    "Глаза Алисы испуганно расширились, рот приоткрылся, но она не издала ни звука, только смотрела на меня. {w}До чего же близко…"
    "Я ощутил её тёплое дыхание на своём лице. Мы простояли так несколько секунд."

    window hide

    show dv shy pioneer2 close:
        center
        zoom 1.15
    with dspr

    $ renpy.pause(1.5, hard=True)

    window show

    dv "Ты… ч-чего?"
    "Она нарушила молчание первой."
    "Алиса несмело положила мне руку на грудь, то ли отталкивая, то ли поощряя, отвела взгляд в сторону, словно смущённая школьница после первого поцелуя."
    "Кто бы мог подумать, что рыжая гроза лагеря умеет так мило смущаться? {w}Я улыбнулся и отодвинулся."
    me "Извини, я споткнулся."

    show dv smile pioneer2 close:
        center
        zoom 1.15
    with dspr

    "К Алисе вернулся обычный настрой."
    dv "Все вы так говорите!"
    "Она притворно вздохнула."

    window hide

    stop ambience fadeout 3

    scene bg ext_music_club_night_bkrr with fade3

    play ambience ambience_camp_center_night fadein 3

    show dv normal pioneer2 at center with dissolve

    window show

    dv "Ладно. Ну, до завтра? Я к себе, а тебе туда."
    me "Пойдём, провожу. А то вдруг медведь из леса выйдет? Или привидение?"

    show dv smile pioneer2 at center with dspr

    dv "Сами нападут, сами пусть и защищаются."
    "Беззаботно отмахнулась Алиса, но предложение всё-таки приняла."

    window hide

    scene bg ext_houses_night_bkrr with fade

    window show

    "По ночному лагерю мы шли молча, но молчание это не было неловким, а таким, когда в словах просто нет необходимости. {w}Нарушать его не хотелось, но была ещё одна вещь."
    me "Да… Алиса. Я хотел сказать кое-что."

    show dv guilty pioneer2 at center with dissolve

    dv "Не признание делать собрался?"
    "Она остановилась и вопросительно взглянула на меня."
    dv "Я не готова!"
    me "Нет, не сегодня."

    show dv normal pioneer2 at center with dspr

    dv "Тогда что?"
    me "Я хотел сказать: спасибо тебе!"

    show dv sad pioneer2 at center with dspr

    "Пожатие плечами, опущенные глаза."
    "Помолчав, Алиса негромко спросила:"
    dv "Пожалуйста. А ты о чём сейчас?"
    me "Ольга Дмитриевна говорила, что ты призналась, что толкнула лестницу. И что будет тебя за это наказывать."

    show dv grin pioneer2 at center with dspr

    dv "Ах, это. Ты не волнуйся. Не возьмут пару раз на пляж, делов-то."
    dv "Гордиться тут нечем, сама знаю, но нас с Улькой, кажется, уже записали в хулиганки. {w}С чего бы это?"

    show dv guilty pioneer2 at center with dspr

    "Она убедительно изобразила непонимание, пожала плечами, грудь под завязанной на узел рубашкой волнующе колыхнулась."
    dv "Так что разом больше, разом меньше…"
    me "Я рассказал всё, как было на самом деле. {w}Ну, без деталей, конечно. Что толкнул Толика и ушиб голову, когда лестницу пытался поймать."
    dv "Ну, и зачем?"
    "Тут уже я не удержался от смеха."
    me "Не мог же я допустить, чтобы ты брала на себя мою вину. Меня потом совесть замучила бы. {w}Да и не по-мужски это: прятаться за девочку. Должно быть наоборот."
    "Серьёзное лицо она сохранила буквально несколько секунд, потом снова негромко засмеялась."

    show dv laugh pioneer2 at center with dspr

    dv "МужЫк! Уважаю. Но у меня была причина. {w}Важная."
    me "Да? Какая же?"

    show dv normal pioneer2 at center with dspr

    dv "Тут до твоего приезда два пацана из-за девчонки подрались. Их по домам разослали. {w}А через пару дней опять – один парень другого поранил."
    dv "Тебя могли наказать, а то и домой отправить, не разбирая, что случилось. Просто чтобы не рисковать и отписок не писать."
    me "Пока не вижу связи. Ну, отослали бы. Переживу. {w}Так сильно музыкант нужен?"

    show dv smile pioneer2 at center with dspr

    dv "Музыкант? {w}Ты? {w}Да не смеши меня."

    show dv guilty pioneer2 at center with dspr

    dv "Не в том дело. Просто…"
    "Она чуть-чуть помялась."

    show dv normal pioneer2 at center with dspr

    dv "Просто ты очень нравишься моей подруге, и она сильно расстроилась бы. Хотя не пойму, что она в тебе нашла."
    me "Ум и красоту, что же ещё."

    show dv smile pioneer2 at center with dspr

    dv "Ой-ой. Не лопни от гордости."
    me "Интере-е-е-есно."

    hide dv with dissolve

    me "Нравлюсь подруге? {w}Кому же?"

    window hide

    $ bkrr_thoughts_show("~ Ульяне? ~", "~ Мику? ~", "~ Лене? ~", "~ Ещё кому-нибудь? ~")

    window show

    th "Точно, Ульяне."
    "Только по-настоящему любимому парню можно подложить червяка в тарелку. Да и шуточки про «насиловать будешь?» тоже наводят на мысли. То-то она так выспрашивала, кто мне нравится."

    show dv smile pioneer2 at center with dissolve

    dv "Не скажу! Секрет!"
    "Она показала язык."
    me "Интриганка! Ну скажи, кому? Я же не усну теперь!"

    show dv grin pioneer2 at center with dspr

    dv "Одной моей подруге, я же сказала. Мучайся!"
    dv "А расскажу… {w}А расскажу, когда две песни сыграешь как надо. Только поторопись, до конца смены всего ничего."

    window hide

    scene bg ext_house_of_dv_night with dissolve

    window show

    th "А может, всё проще? «Одной моей подруге?»."
    "Прямо как в анекдоте:"
    "– Доктор, один мой знакомый думает, что подхватил гонорею.\n– Да? Ну, спускайте штаны, и давайте посмотрим на вашего знакомого."
    th "Неужели это я {b}ей{/b} нравлюсь?"
    "До встречи с Мику я бы был счастлив, но сейчас, пожалуй, лишнее внимание Алисы будет проблемой."
    "Говорить это в лоб я как-то постеснялся, а потому просто подыграл."
    me "Придётся поднапрячься. Ну, спасибо вам обеим. Можешь передать, что теперь я заинтригован и буду репетировать в два раза больше!"

    show dv normal pioneer2 at center with dissolve

    dv "Я передам."

    show dv smile pioneer2 at center with dspr

    dv "Ну, вот мы и пришли. {w}Доброй ночи, Сёма!"

    window hide

    play sound sfx_open_door_1

    show dv smile pioneer2 at left with ease

    show us yawn night_shirt at right with dissolve

    window show

    "Дверь приоткрылась, из-за неё выглянула заспанная Ульяна в одной красной футболке. {w}Взлохмаченная и с сонно надутыми губами, она выглядела совсем ребёнком."
    us "Тили-тили тесто… Алиска и Семён."
    "Пробурчала она."

    show us sad night_shirt at right with dspr

    us "Чего так поздно-то? Я уже думала, ты там в клубе и заснула. А ты ходишь тут. {w}Со всякими."

    show us grin night_shirt at right with dspr

    us "Не целовались хоть? А то знаю я вас… Он меня грязно домогался, имей в виду!"

    show dv laugh pioneer2 at left with dspr

    dv "Улька, ну ты что. Вот с этим вот? Как я могла?"

    show dv grin pioneer2 at left with dspr

    dv "Всё, Семён, погубил ты мою честь. Теперь, как честный человек, ты должен застрелиться."
    me "Чего? Обычно говорят «жениться»."

    show dv smile pioneer2 at left
    show us smile night_shirt at right
    with dspr

    dv "Ну раз ты предложил, я подумаю. Ульянка, ты свидетель!"

    show us yawn night_shirt at right with dspr

    us "Ну хватит уже, пошли спа-а-а-а-ать."
    "Ульяна заразительно зевнула."

    show dv normal pioneer2 at left with dspr

    dv "Прости-прости. Уже иду."

    hide us with dissolve

    dv "Сеня, доброй ночи!"
    me "И тебе. Вам обеим."

    hide dv with dissolve

    "Помахав мне на прощание, Алиса скрылась за дверью."
    th "Странно. Такая переменчивая натура."
    "Днём казалась злюкой, в обед – обычным провинившимся подростком, а сейчас прямо как взрослая себя ведёт."
    "Ладно. Подумаю об этом завтра."

    window hide

    scene bg ext_houses_night_bkrr with dissolve

    window show

    "Обратно я шёл не спеша."
    "Ночь была такая безоблачная, тёплая. {w}Сирень и ещё какие-то неизвестные цветы наполняли её такими запахами, что заходить в помещение никак не хотелось. {w}Кажется, не мне одному."

    show sh smile pioneer far at center with dissolve

    "Шурик брёл куда-то с мечтательным выражением на лице."

    hide sh with dissolve

    th "Может, к девочке?"
    th "А что, дело молодое."
    "Я хотел его окликнуть, но передумал. Хотелось побыть одному."

    window hide

    $ renpy.pause(1.0, hard=True)

    $ bkrr_set_mode(nvl)

    stop ambience fadeout 3

    play music music_list["farewell_to_the_past_edit"] fadein 3

    nvl show dissolve

    "Прошедшие события медленно прокручивались в голове. {w}Если и были какие-то сомнения, что это не просто провал во времени, то сегодня они отпали окончательно. {w}Происшествие с плеером, странное поведение «пионеров», их возраст, опять же, да и просто целая куча ничего не значащих мелочей, которые объединялись в одно странное целое. {w}Что же тут происходит?! {w}Куда я попал и где мои вещи?!"
    "Плен не был неприятным. {w}В конце концов, что ждало меня дома? {w}Конура без ремонта, нелюбимые подработки, скука, незаметно сменяющие друг друга дни, одинаковые, как китайцы, а мирок сужен до пятна света, отбрасываемого монитором. {w}Здесь же…"
    "Здесь я чувствовал себя живым. Желание вернуться домой и желание вырваться из той рутины сплелись в запутанный клубок."
    "Не знаю, что будет потом, но пока что играю свою пионерскую роль, а там, глядишь, и за пределы лагеря удастся выбраться. {w}Расслабляемся и получаем удовольствие."

    nvl hide dissolve

    $ renpy.pause(1.0, hard=True)

    scene bg ext_square_night with dissolve

    play ambience ambience_camp_center_night fadein 3

    $ bkrr_set_mode()

    window show

    "Несмотря на позднее время, на площади сидела Лена с неизменной книжкой."
    "Рядом с ней исходила паром чашка чая. {w}Фонари на ночь гасили, но несколько «дежурных» давали достаточно света, чтобы читать."
    th "Интересно, она спит вообще?"
    me "Привет!"
    "Я помахал ей."

    stop music fadeout 3

    show un shy pioneer at center with dissolve

    "Она слегка смутилась, но улыбнулась и кивнула в ответ."

    show un smile pioneer at center with dspr

    un "Уже виделись!"
    me "Поздновато для чтения. Тоже не спится?"

    show un normal pioneer at center with dspr

    un "Нет, соседка во сне шумит."
    me "Соседка…"
    un "Ну да. Мы же с Мику живём. {w}Она иногда начинает во сне болтать, громко."
    me "А-а-а. Ну да. Во сне и наяву. И что, так и будешь сидеть всю ночь?"
    un "Нет, конечно. Как заснёт покрепче, я и пойду. Да и главу дочитать хочется."
    me "Понимаю… Тебе не страшно одной?"
    un "Мне? {w}Нет."
    me "Тогда доброй тебе ночи!"

    show un smile pioneer at center with dspr

    un "И тебе."

    hide un with dissolve

    "Разговор зашёл в тупик. Я уже отходил, когда она окликнула меня."

    un "Семён?"

    show un normal pioneer far at center with dissolve

    me "Да?"
    un "А ты не знаешь, куда Шурик пошёл?"
    un "Шёл к лесу и бормотал что-то под нос. Я его позвала, а он даже не повернулся. {w}Лунатик, что ли?"
    me "Был бы лунатик – в трусах гулял бы. {w}Я его тоже видел."
    me "Не бери в голову. Наверное, девочка у него, будут держаться за руки, смотреть на звёзды и по-пионерски целоваться в щёчку. {w}Даже завидно."

    show un smile pioneer far at center with dspr

    un "А-а-а… тогда пускай."

    hide un with dissolve

    "Лена снова уткнулась в книжку."

    window hide

    stop ambience fadeout 3

    scene bg int_house_of_mt_night2 with fade3

    play ambience ambience_int_cabin_night fadein 3

    play sound sfx_close_door_1

    window show

    "Когда я вернулся в домик, часы показывали одиннадцать."
    "Ольга сбросила во сне покрывало и в коротенькой ночной рубашке выглядела чертовски соблазнительно."

    window hide

    $ renpy.pause(1.0, hard=True)

    window show

    "С трудом поборов искушение поглазеть подольше, я подобрал покрывало, стряхнул и аккуратно укрыл вожатую до подбородка, стараясь не разбудить. {w}Она что-то пробормотала сквозь сон и укуталась поплотнее."
    "Мне нечасто приходилось рассматривать спящих девушек, так что я присел на край стола и какое-то время любовался её профилем, пока не почувствовал, что глаза слипаются."
    me "Спокойной ночи, Ольга Дмитриевна."
    "Тихо шепнул я для очистки совести."

    window hide

    show blink

    $ renpy.pause(1.5, hard=True)

    window show

    "Стоило коснуться подушки, как меня моментально сморило. Ещё один день в этом странном месте подошёл к концу."

    window hide

    $ persistent.bkrr_check[7] = True

    jump bkrr_day7_start
