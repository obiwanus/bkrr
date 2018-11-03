
#    Булки, кефир и рок-н-ролл. День 8    #

label bkrr_day8_start:

    $ bkrr_new_chapter(8)

    jump bkrr_day8_common

label bkrr_day8_common:

    scene bg int_house_of_mt_day
    show unblink
    with None

    $ bkrr_set_time()

    play ambience ambience_int_cabin_day fadein 3

    play music music_list["everyday_theme"] fadein 5

    # $ bkrr_get_achievement("hatiko")
    # ачивка для второго эпизода

    $ renpy.pause(1.5, hard=True)

    window show

    "Погода с утра не баловала."
    "Снова началась жара, и хотя умывание холодной водой чуть-чуть разогнало сонливость, всё равно не хотелось никуда идти, только лечь и ещё поспать."
    "Слегка поборовшись с нежеланием выходить на солнце, я поспешил на завтрак, подгоняемый желанием увидеть Мику."

    window hide

    stop ambience fadeout 3

    scene bg int_dining_hall_people_day_bkrr with fade3

    play ambience ambience_dining_hall_full fadein 3

    window show

    "Поболтать с Мику не вышло."
    "Ольга Дмитриевна сегодня с утра пропадала в администрации, так что в столовой царил полный кавардак. {w}Мику сидела в самом уголке, а вокруг неё столпилась куча пионеров, в основном девочек, наперебой расспрашивая что-то про предстоящий концерт. Мику пыталась отвечать всем сразу, но только добавляла этим суматохи."
    "Сложив грязную посуду в мойку, я прислонился к стене и принялся наблюдать за Мику."

    window hide

    $ renpy.pause(1.0, hard=True)

    window show

    "Меня дружески хлопнули по плечу."

    show dv grin pioneer at center with dissolve

    dv "Доброе утро! Что, соскучился?"
    me "Привет. Ну… А так заметно?"

    show dv smile pioneer at center with dspr

    dv "Смотришь, как кот на сметану."
    me "Ага! Думал, позавтракаем за одним столом, все вместе… {w}А тут такое."

    show dv normal pioneer at center with dspr

    dv "Ой, насидимся ещё на репетиции. Я тут к ней пробовала прорваться – безнадёжно."
    me "А что за суета?"
    dv "Сценарий праздника сочиняют. А эта ду…"

    show dv smile pioneer at center with dspr

    "Алиса улыбнулась."
    dv "Это наивное создание сказало, что все могут вносить предложения."

    show dv laugh pioneer at center with dspr

    dv "Ну и вот. Вносят. {w}Где поймают. {w}По-моему, ей даже поесть не дали."
    me "Ну, пошла бы, шугнула? Помогла бы подруге?"

    show dv angry pioneer at center with dspr

    dv "Нет, я не поняла, что за намёки. Так ты что, говоришь, что я такая страшная, что мной детей пугать можно?"
    "Она выдержала паузу и продолжила:"
    dv "Нет, я, конечно, им сказала, что если хоть кто-то появится в музклубе без приглашения и помешает репетировать, то я им уши оборву. Но если ты думаешь, что мне нравится, что меня считают пугалом, то подумай ещё раз. {w}Это бесит, между прочим!"
    me "Нет-нет. Я имел в виду, что ты… э-э-э… авторитет имеешь! {w}В смысле – пользуешься. И, может, заставишь их разойтись."

    show dv smile pioneer at center with dspr

    dv "Не льсти, не поможет. Делать мне больше нечего."
    me "Но Мику ведь…"

    show dv laugh pioneer at center with dspr

    dv "Да пускай. Посмотри, ей же самой нравится, когда вокруг народу много. Не будет ничего с твоей Мику."
    me "Моей?"

    show dv normal pioneer at center with dspr

    dv "Ну не моей же."

    stop music fadeout 5

    "Алиса посмотрела куда-то в сторону, потом улыбнулась."
    dv "Давай лучше кино посмотрим."
    me "Какое ещё кино?"

    show dv normal pioneer at center with dspr

    dv "Приключенческое! С ограблением и погоней."
    me "Ты о чём вообще?"
    dv "Тс-с! Сам смотри."

    hide dv with dissolve

    "Она показала в сторону столика, где сидели кибернетики."
    "Шурик уже доел кашу и теперь потянулся за компотом, когда возле него, словно из ниоткуда, возникла Ульяна."
    "Из-за шума я не смог разобрать, что она говорила."
    "Потом Ульяна показала куда-то вверх, а стоило Шурику поднять глаза…"

    play music music_list["eat_some_trouble"]

    scene cg d8_theft

    "… ловко цапнула большую ватрушку, лежавшую на его стакане."
    "Еще секунда – и она, ловко огибая пионеров, пронеслась к выходу. Шурик ринулся вдогонку, но сразу понял, что это безнадёжно. Он махнул рукой и вернулся за столик."
    dv "Вот такое кино."

    scene bg int_dining_hall_people_day_bkrr
    show dv normal pioneer at center
    with dissolve

    me "Чего это она? Не наелась? Добавки бы взяла."
    dv "Ай, Сенька, ничего ты не понимаешь!"
    me "Чужое вкуснее?"

    show dv guilty pioneer at center with dspr

    "Алиса посмотрела на меня со странным выражением."
    dv "Нет, ты не притворяешься. Эх! Безнадёга."

    hide dv with dissolve

    "Она отошла в сторону и с трудом раздвинула пару пионерок, подсовывающих Мику листки с какими-то каракулями."

    show dv normal pioneer at center with dspr

    dv "Мы пошли! Ты как, с нами?"

    window hide

    stop music fadeout 3

    show dv normal pioneer at left with ease

    show mi sad_smile pioneer at right with dspr

    window show

    mi "Ой, Алисочка, сейчас, мы тут чуть-чуть ещё, а то в музклуб они идти почему-то не хотят. Тут столько предложений, сейчас, ещё пять минуток! Вы идите, я догоню!"
    "Алиса с сомнением посмотрела на толпу пионеров, что-то прикинула и вздохнула."

    show dv smile pioneer at left with dspr

    dv "Мы догоним. Сень, ты иди пока, я через пять минут разгоню этот базар и приведу нашу массовичку-затейницу."

    show mi smile pioneer at right with dspr

    mi "Да-да, мы догоним! Иди, отпирай, поиграй то, что мы вчера учили. И, пожалуйста, окошки открой, пусть проветрится, пока жары нет. А то днём жара, вечером комары, только с утра и можно прове… {w}А?"

    window hide

    hide dv with easeoutleft

    show mi serious pioneer at center with ease

    window show

    "Тут ей подсунули очередной листок."
    mi "Что? Импровизация на саксофоне? А саксофона у нас в клубе нет. У тебя есть свой? Нет, ну правда, нету! Точно-точно! Тромбон, кажется, есть, и ещё…"

    hide mi with dissolve

    me "Ну, как скажете."

    window hide

    stop ambience fadeout 3

    scene bg ext_music_club_day_bkrr with fade3

    play ambience ambience_camp_center_day fadein 3

    window show

    "По пути в клуб я поймал себя на том, что с нетерпением жду начала репетиции. {w}В первую очередь, конечно, из-за Мику. Но не только."
    "То, что у меня появилась цель, тоже воодушевляло. {w}Цель. Стать басистом в пионерской группе. Смешная, конечно, цель, но уж какая есть."
    "Почему-то подсознательно я надеялся, что если буду хорошо играть свою роль, то и закончится всё тоже хорошо. Так или иначе, но хорошо."

    window hide

    scene bg ext_music_club_verandah_day_v3 with dissolve

    window show

    "И всё-таки первым в клуб пришёл не я. На веранде сидела Ульянка и присматривалась к трофейной ватрушке, пытаясь решить, откуда её начать есть."

    show us grin pioneer at center with dissolve

    us "Сенька! Я ждала тебя, как маму!"
    me "Как маму? А что такое? Привет, кстати."

    show us normal pioneer at center with dspr

    us "Привет! Да я ключ в домике оставила. {w}Сижу, жду. Алиски нет, Микуськи нет, тебя тоже нет."
    us "Думала, придётся в окно уже лезть. Давай, отпирай скорее!"
    me "Что, не терпится побарабанить? Погодка-то какая, посидим на улице."

    show us calml pioneer at center with dspr

    us "Да компот сильно сладкий, не напилась, да ещё ватрушка эта, тоже сладкая… водички хочу!"
    me "И кто ж тебя этой ватрушкой кормил насильно? Что, объела бедного Шурика?"

    show us dontlike pioneer at center with dspr

    us "Вот не надо тут! От него не убудет. И вообще, он заслужил."
    me "Чем же?"

    show us normal pioneer at center with dspr

    us "Он… Да не твоё дело!"
    me "Как скажешь. Значит, без повода, просто лишаешь Сашку калорий… {w}А ватрушки-то вкусные, кстати."

    show us smile pioneer at center with dspr

    us "Намёк поняла. Держи!"
    "Она отломила хороший кусок от ватрушки и протянула мне."
    me "Да я не в том смысле."

    show us dontlike pioneer at center with dspr

    us "Смыслы-шмыслы… {w}Любишь ты всё усложнять! Ну, отломила уже, жуй давай. Только сначала дверь открой, пожалуйста."

    window hide

    hide us with dissolve

    $ renpy.pause(0.5, hard=True)

    play sound sfx_unlock_medpunkt_door

    $ renpy.pause(3.0, hard=True)

    play sound sfx_open_door_2

    scene bg int_music_club_mattresses_day with dissolve

    play ambience ambience_music_club_day fadein 3

    play music music_list["smooth_machine"] fadein 7.5

    window show

    "Музклуб встретил нас приятной прохладой. Я открыл форточки, и тёплый, пахнущий лесом воздух наполнил комнату."
    me "Может, заодно и чайник поставим? А то там Мику поесть не дали толком…"

    show us smile pioneer at center with dissolve

    us "А сама виновата! Мы ей говорили, чтоб за сценарий не бралась. {w}Теперь мало того, что Ольга Дмитриевна её постоянно подгоняет, так ещё и эти прохода не дают."

    window hide

    hide us with dissolve

    $ renpy.pause(1.0, hard=True)

    window show

    "Она залпом выпила стакан воды, довольно погладила себя по животу и счастливо вздохнула."

    show us grin pioneer at center with dspr

    us "Но попить чайку всем вместе – это святое! Ещё бы печенек каких-нибудь."

    show cat musclub_1 with dissolve

    "Она покосилась на неизвестно откуда взявшегося в клубной комнате Пирата."

    show us smile pioneer at center with dspr

    us "Слушай… А давай его в трубу на кухне засунем? Глядишь, ещё сладкого дадут. Кис-кис-кис…"

    hide cat with dissolve

    "Кот настороженно посмотрел на Ульяну и, на всякий случай, ушёл подальше."
    me "Пират, не волнуйся, она шутит! {w}Наверное."
    me "Интересно, а в первый раз не она тебе помогла туда попасть?"

    show us calml pioneer at center with dspr

    us "Везёт мне на товарищей по группе. Одна на людей кидается с гитарой, другая болтает, как радио, а третий меня с котами обсуждает. Дурдом!"
    me "Да ладно, я же не слышу, как он мне отвечает. Вот как услышу – так меня к медсестре и поведёте."

    show us smile pioneer at center with dspr

    us "Обязательно! И поставит она тебе большой-пребольшой укол! О, чайник закипел."
    me "Не хочу. Терпеть не могу уколы."

    show us grin pioneer at center with dspr

    us "Тем более надо! Чтоб, значит, характер закалить! Тебе один, два?"
    me "Укола?"

    show us dontlike pioneer at center with dspr

    us "Дурак, что ли? Сахара тебе один, два куска?"
    "На тумбочке стояла пара наполненных чашек, а в руках Ульяна держала картонную коробочку с рафинадом."

    show us normal pioneer at center with dspr

    "Пионерка вопросительно смотрела на меня."
    me "Два. Спасибо!"

    window hide

    stop ambience fadeout 2

    stop music fadeout 2

    $ bkrr_timeskip_short()

    scene bg int_music_club_mattresses_day
    show cat musclub_2
    with bkrr_timeskip_transition()

    play ambience ambience_music_club_day fadein 3

    window show

    "Мы успели выпить по чашке чая, а девчонки всё не шли."
    me "Ну где же они?"

    show us normal pioneer at center with dissolve

    us "Наверное, окольными тропинками крадутся сюда, чтобы никто не приставал по пути. До обеда придут!"
    me "Долго ждать. Я надеялся, что Мику меня дальше учить будет…"

    show us smile pioneer at center with dspr

    us "Ага. Знаю я, на что ты надеялся! Что будете бок о бок сидеть с счастливыми мордашками. {w}Да?"
    us "Но ты, Семёныч, губку закати, сегодня я тебя буду учить!"
    me "Ты? Учить? Интересно, чему."

    show us dontlike pioneer at center with dspr

    us "Я не поняла, что за удивление? Мы не просто так, мы ритм-секция, нам положено вот так быть!"

    show us smile pioneer at center with dspr

    "Она сжала ладонь ладонью и показала, как именно мы с ней должны быть."
    us "Алиса с Мику будут на гитарах сыгрываться, а мы с тобой займёмся ритмом. Я вчера даже у Микуси умных слов набралась, так что будешь слушать и запоминать."
    me "Посмотрим…"

    show us grin pioneer at center with dspr

    us "Никаких «посмотрим». Я тоже учителем побыть хочу!"

    play music music_list["so_good_to_be_careless"] fadein 3

    play sound sfx_open_door_2

    show us surp1 pioneer at center with dspr

    us "О! Вот они, наконец-то!"

    show us smile pioneer at center with dspr

    us "Девчонки, чай пить будем?"

    window hide

    show us smile pioneer at right with ease

    show dv normal pioneer at left with easeinleft

    window show

    dv "Улька, мы только с завтрака! Не лопнешь?"

    show us dontlike pioneer at right with dspr

    us "Вот давай не будем выяснять, кто из нас лопнет, а? {w}Кто там вчера в медпункте три раза перевзвешивался и стонал, что двести грамм прибавил?"
    dv "А ну, тихо! Ладно, давай уже. Сень, ты будешь?"

    show us normal pioneer at right with dspr

    me "Не… Мы уже попили."

    window hide

    hide dv with easeoutleft

    show mi normal pioneer at left with easeinleft

    window show

    mi "А у нас печенье есть! Меня Лена угостила утром. {w}Всё равно не соблазним? Вкусненькое!"
    me "Микусь, ну правда, уже не могу. Спасибо!"

    window hide

    hide mi with easeoutleft

    show us grin pioneer at center with ease

    window show

    us "Он не будет. Да и ладно, нам больше останется! Давай я его печенье заберу!"
    me "Куда! От печенья никто не отказывался!"
    "Я ловко выхватил свою долю прямо из-под загребущих ульянкиных пальцев. Она не обиделась, только засмеялась."

    show us laugh pioneer at center with dspr

    us "Ну вот. А говорят, басисты медлительные! {w}Врут! Я же говорила!"

    window hide

    stop ambience fadeout 2

    stop music fadeout 2

    $ bkrr_timeskip_short()

    scene bg int_music_club_mattresses_day with bkrr_timeskip_transition()

    show us smile pioneer at center with dissolve

    play ambience ambience_music_club_day fadein 3

    window show

    us "Семёныч, ты готов?"
    me "Ну…"
    us "Готов-готов! Тогда начинаем лекцию!"

    show us normal pioneer at center with dspr

    us "Бери свою гитару и пошли в уголок. Слушай меня внимательно и не вздумай что-то забыть!"
    "Она напустила на себя профессорский вид и принялась рассказывать:"

    play music music_list["i_want_to_play"] fadein 3

    us "Начинаем с основного. Ты знаешь, для чего ты здесь?"
    th "Конечно, Мику кое-что объясняла про роль басиста, но я старательно изобразил непонимание."
    me "Не знаю! Помню, оглушили, заломали, принудили к вступлению в группу и угрожали в случае отказа."

    show us dontlike pioneer at center with dspr

    us "Ну не вредничай! Я имела в виду, зачем ты здесь сидишь с басухой."
    me "Сам удивляюсь. И зачем же?"

    show us calml pioneer at center with dspr

    us "Как же тебе попроще-то…"

    show us grin pioneer at center with dspr

    us "Ты сказку про репку знаешь?"
    me "Конечно. А при чём тут это?"

    show us smile pioneer at center with dspr

    us "При том, Сенька! При том. Вот представь, что я – это репка."
    "Алиса отпила чая и громким шёпотом прокомментировала:"

    show dv laugh pioneer far at fleft with easeinleft

    dv "Ни капли не похожа… {w}Скорее на редиску. Или помидорку."

    show us calml pioneer at center with dspr

    us "Алиска, не мешай! Я же вам не мешала!"

    show mi dontlike pioneer far at fright with easeinright

    mi "Да, Алис, мы же ей обещали."
    dv "Прости-прости. Продолжайте, пожалуйста."

    window hide

    show dv laugh pioneer far at offscreenleft
    show mi dontlike pioneer far at offscreenright
    with ease

    hide dv
    hide mi
    with None

    show us normal pioneer at center with dspr

    window show

    us "Так вот. Я на ударных задаю ритм. Ты подхватываешь его, и мы вместе создаём э… м-м-м… как её там."

    show us smile pioneer at center with dspr

    us "А! Ритмическую основу. Понял?"

    show dv laugh pioneer close:
        fleft
        rotate 17
    with easeinleft

    dv "Аритмическую?"

    show us angry pioneer at center with dspr

    us "Алиса!"

    show dv smile pioneer close:
        fleft
        rotate 17
    with dspr

    dv "Молчу!"

    hide dv with easeoutleft

    show us calml pioneer at center with dspr

    us "Вредина."

    show us normal pioneer at center with dspr

    us "В общем, Сень, я задаю ритм тебе, ты – остальным. Басист – он сердце группы. Переходное звено!"

    show dv grin pioneer close:
        fright
        rotate -17
    with easeinright

    dv "От обезьяны к гитаристу!"

    show us grin pioneer at center with dspr

    hide dv with easeoutright

    us "От ударника к рыжему орангутангу!"

    show us normal pioneer at center with dspr

    us "И если это звено будет слабым, то ритм распадётся и все собьются. {w}Понял?"
    "Мику, слушавшая нас краем уха, обиженно заметила, что она не собьётся ни при каких обстоятельствах."

    show us smile pioneer at center with dspr

    us "Правильное замечание. Все, кроме Мику. Понял?"
    me "Конечно! Сразу всё понятно стало. У тебя здорово объяснять получается. {w}А репка тут при чём была?"

    show us dontlike pioneer at center with dspr

    us "Забудь про репку!"
    me "Нет, погоди, ты сказала – ты репка. И сказала: «Не вздумай что-то забыть». Как же я могу?"

    show us calml pioneer at center with dspr

    us "Сенька, ты издеваешься?"
    "Я сделал честное и в меру глупое выражение лица и кивнул."
    me "Извини. Немножко. Ты так серьёзно рассказывала, я не удержался. Прости, я больше не буду."

    show us smile pioneer at center with dspr

    "Против ожидания, Ульяна не разозлилась. Напротив, ехидно улыбнулась и погрозила мне пальцем."
    us "Ладно, Семёныч, клоун ты наш, сейчас посмотрим, какой ты умный."
    us "Дёргать струны ты более-менее наловчился, сегодня попробуем сыграть под барабан. Падай вот сюда, бери гитару и пробаси-ка вот этот кусочек. Сможешь?"
    me "Сейчас узнаем."

    window hide

    hide us with dissolve

    stop music fadeout 3

    $ renpy.pause(1.0, hard=True)

    window show

    "Я довольно чисто отыграл три такта несколько раз подряд."
    "Ульяна показала большой палец, затем преувеличенно громко восхитилась."

    show us smile pioneer at center with dissolve

    us "Моя ж ты умничка. Девчата, он двенадцать нот запомнил! А теперь давай под барабан?"

    hide us with dissolve

    "Очень скоро оказалось, что играть одному – это одно, а попадать в такт с ударными – совсем другое."
    "Через несколько неудачных попыток Ульяна закапризничала."

    show us calml pioneer at center with dissolve

    us "Не могу я с ним! Алиска, ну он вообще тугоухий. Верните мне Толика!"
    "Алиса изобразила на гитаре длинный риф, отдалённо похожий на «Smoke On The Water», и отмахнулась от Ульянкиных претензий."

    window hide

    show us sad pioneer at left with ease

    show dv normal pioneer at right with easeinright

    window show

    dv "Не будет Толика, играй с кем есть!"

    show us fear pioneer at left with dspr

    us "Но он же… {w}Он же никакой!"

    show dv grin pioneer at right with dspr

    dv "Рыжик, ну потерпи, а? Сейчас он соберёт отсутствующие таланты и сделает вид, что он басист, а не пионер с поленом. {w}Да, Сёмка?"
    dv "Где были мои уши, когда я взяла тебя в нашу банду?"

    hide us
    hide dv
    with dissolve

    "Я злобно засопел. {w}Можно подумать, это я рвался к ним в группу, пока меня не согласились взять."
    "Умом я понимал, что она специально дразнится, чтобы я старался, но зубами всё-таки поскрипывал."
    "Мику отложила альбом с табулатурами и присела рядом со мной."

    show mi dontlike pioneer close at center with dissolve

    mi "Алиска, Ульяна, не давите на него. Сами такими были. Давайте лучше я попробую!"
    "Хоть кто-то меня защищает в этом скорпионнике. Алиса насмешливо кивнула."

    window hide

    show mi dontlike pioneer close at right with ease

    show dv grin pioneer far at left with easeinleft

    window show

    dv "Ну-ну. А мы пока с Ульяной сыграемся."

    show dv laugh pioneer far at left with dspr

    dv "Только ты построже, построже! Не балуй его! Басиста хвалить нельзя, он обнаглеет и обленится!"

    show mi angry pioneer close at right with dspr

    mi "Алиска, ты помнишь, как три аккорда взять не могла? Если бы я на тебя рычала тогда?"

    show dv guilty pioneer far at left with dspr

    dv "Помню…"

    show mi smile pioneer close at right with dspr

    mi "Вот то-то же. Мы с ним по-хорошему, и всё у нас получится."

    show dv normal pioneer far at left with dspr

    dv "Ого! Ну, раз так, я молчу. Репетируйте, голубки."

    window hide

    hide dv with easeoutleft

    show mi smile pioneer close at center with ease

    window show

    "Алиса подмигнула нам, потом принялась преувеличенно серьёзно крутить колки на гитаре."

    play music music_list["miku_song_flute"] fadein 3

    show mi normal pioneer close at center with dspr

    mi "Здесь мешать друг другу будем. Кабеля на улицу не хватит, так что эту отложи пока. Бери Машу, пойдём на веранду."
    me "Машу? Какую ещё Машу?"

    show mi smile pioneer close at center with dspr

    mi "А, ну да… Это у нас шутка такая. Бас-гитара «Мария» называется. Мы её Машей зовём."

    window hide

    hide mi with dissolve

    $ renpy.pause(1.0, hard=True)

    window show

    "Я сменил бас на акустический, тот самый, которым меня оглушили."
    th "Маша, значит?"
    "Мику сняла с полки обычный пионерский барабан и направилась к выходу."

    window hide

    stop ambience fadeout 0.5

    play sound sfx_open_door_2

    scene bg ext_music_club_verandah_day_v3 with dissolve

    play ambience ambience_camp_center_day fadein 3

    window show

    "Мы с Мику вышли на улицу и присели на узкой скамейке. Солнце уже жарило вовсю, но на веранде было достаточно тени."

    show mi normal pioneer at center with dissolve

    mi "Хорошо-то как на улице!"
    me "Да, здорово. И не мешают."

    hide mi with dissolve

    stop music fadeout 3

    "Я думал, как половчее заговорить о вчерашних событиях. {w}Мику вела себя совсем как обычно, словно и не было ничего."
    "Я не слишком хорошо разбирался во всех тонкостях ухаживаний, так что ломал голову, как же мне себя теперь вести."
    th "Вроде бы со вчера мы стали как-то ближе?"
    th "Ещё и Алиса сказала, что я нравлюсь Мику. Могла и подшутить, конечно, но, кажется, не врёт."
    "Мику вытянула обтянутые чёрным нейлоном ножки, сбросила туфли, пошевелила пальцами ног. Потом легко и непринуждённо взяла меня за руку."

    show mi smile pioneer close at center with dissolve

    mi "Сеня, я понимаю, что ты только начал учиться, но надо немножко собраннее. Чувство ритма у тебя хорошее, но вот концентрации не хватает. Ну, и практики, конечно. Так что мы тут с тобой отдельно позанимаемся. {w}Ты ведь не против?"
    th "Она ещё спрашивает!"
    me "Давай, конечно. А ничего, что ты тратишь на меня столько времени? Тебе ведь тоже нужно репетировать."

    show mi happy pioneer close at center with dspr

    mi "А мне не надо, я не умею играть неправильно."

    show mi upset pioneer close at center with dspr

    mi "Это, между прочим, не достоинство. Например, импровизировать я тоже не умею, там нужно… ну, я не знаю. Что-то, чего у меня нет. Джаз, например, не для меня."
    "Мику вздохнула, и я поспешил поднять ей настроение."
    me "Здорово! Частные уроки от тебя, да ещё и бесплатно."

    show mi grin pioneer close at center with dspr

    mi "А вот и не бесплатно!"
    me "Я чувствовал подвох."

    show mi normal pioneer close at center with dspr

    mi "Ну что ты. Никаких подвохов."
    mi "Просто я пол в клубе завтра помыть хочу, а воду принести некому."

    show mi shy pioneer close at center with dspr

    mi "Ты не мог бы, ну то есть, если тебе не очень тяжело, и если ты ничем не занят… ?"
    "Она замолчала, смущённо вертя в руках барабанные палочки."
    me "С удовольствием помогу. Ну а что мы сейчас будем делать?"
    "Я очень надеялся, что она обнимет меня за шею и шепнёт в ухо: «Целоваться, глупенький!», – но, увы…"

    show mi normal pioneer close at center with dspr

    mi "Отрабатывать взаимодействие! Я буду за Ульянку, а ты старайся попадать в ритм. Вы слишком быструю мелодию для начала выбрали, вот у тебя и не получалось. Давай, не спеша!"

    hide mi with dissolve

    "Она показала, что именно играть."

    window hide

    $ renpy.pause(1.0, hard=True)

    window show

    "После того, как я вполне удовлетворительно отыграл кусок несколько раз, Мику устроила барабан на коленях и взялась за палочки."
    mi "А теперь вместе!"
    "Попасть в такт оказалось совсем не просто."
    "Первый раз я «потерялся» сразу, второй – на середине, третий – вообще опоздал с началом."
    "Из окна выглянула Алиса, прислушалась, покачала головой."

    play music music_list["that_s_our_madhouse"] fadein 5

    show dv grin pioneer far at center with dissolve

    dv "Когда женишься, напишу твоей жене письмо с соболезнованиями. Такое никудышное чувство ритма. {w}А ну, давай ещё раз! Иначе сладкого лишим!"
    "Ульянка в глубине помещения задумчиво выстучала небольшую серию, а затем громко предложила:"
    us "Может, всё-таки поищем кого другого? Испортит ведь всё! Помидорами забросают! {w}Или цветами. {w}В горшках."
    "Алиса подмигнула нам с Мику, покачала головой, а затем выдала:"

    show dv smile pioneer far at center with dspr

    dv "Ещё чего! Это же вызов нашим талантам! Мы из него сделаем человека. {w}Ну, или басиста хотя бы."

    show dv laugh pioneer far at center with dspr

    dv "И чем он хуже, тем интереснее наша задача!"

    hide dv with dissolve

    th "Кажется, мои усилия их не очень впечатляли. Я обиделся и со злости ухитрился попасть в такт."
    "Мику одобрительно улыбнулась и разрешила передохнуть положенные пять минут. Алиска перевесилась через подоконник и показала большой палец."

    show dv normal pioneer far at center with dissolve

    dv "Вот, видишь? Можешь ведь!"
    dv "Думаешь, мне самой нравится на тебя рычать, бассота? Ну ведь не понимаешь иначе. Давай в том же духе."

    hide dv with dissolve

    stop music fadeout 5

    "Вскоре я начал понимать, что же такое «поймать ритм»."
    "Довольно сносно отыграв положенные сорок минут, мы вернулись в помещение."

    window hide

    stop ambience fadeout 3

    $ bkrr_timeskip()

    scene bg int_music_club_mattresses_day with bkrr_circleout_transition

    play ambience ambience_music_club_day fadein 3

    play sound bkrr_sfx_list["broken_amp"]

    window show

    "Долго поиграть не вышло."
    "Есть мнение, что понедельник – день тяжёлый. {w}Может, и правда так."
    "Когда Алиска сыграла какой-то особо сложный пассаж, усилитель издал негромкий стон, обогатил атмосферу вонючим дымом и наотрез отказался работать."
    "Алиса так увлеклась, что продолжала играть ещё секунд десять и лишь затем обратила внимание на отсутствие звука."

    show dv surprise pioneer at center with dissolve

    dv "Что за…? Где звук? И что это за вонища?"

    window hide

    show dv surprise pioneer at cleft with ease

    show us sad pioneer at cright with easeinright

    window show

    us "Сдаётся мне, что наш усилок помер."
    "Алиса с отвращением потрогала усилитель ногой."

    show dv sad pioneer at cleft with dspr

    dv "Техника на грани фантастики. И что теперь? Будем играть на акустике?"
    dv "Ну что за невезение! То басист не басит, то усилитель не усиливает."

    hide dv
    hide us
    with dissolve

    "Мику приблизила лицо к коробке аппарата, сморщилась и отпрянула."

    show mi dontlike pioneer at center with dissolve

    mi "Фе-е-е! И что будем делать? Может, электрика попросим?"
    "Алиса сокрушённо покачала головой."

    window hide

    show mi dontlike pioneer at cright with ease

    show dv guilty pioneer at cleft with easeinleft

    window show

    dv "Не пойдёт. Он в таком не разбирается. Да и занят."
    dv "В город, что ли, везти? Концерт-то под угрозой."

    show mi upset pioneer at cright with dspr

    mi "А если…"

    window hide

    hide dv
    hide mi
    with dissolve

    $ renpy.pause(1.0, hard=True)

    window show

    "Девчонки препирались ещё несколько минут. Я решил вмешаться."
    me "А может, попросим Шурика с Электроником?"

    show dv angry pioneer at cleft
    show us surp2 pioneer at cright
    with dissolve

    dv_us_d "НЕТ!"

    window hide

    show dv angry pioneer at left
    show us surp2 pioneer at right
    with ease

    show mi upset pioneer at center with dissolve

    window show

    mi "Нет, не согласятся."

    hide mi with dissolve

    show us dontlike pioneer at right with dspr

    us "А всё потому, что какая-то рыжая хулиганка Сыроежкину фингал набила ни за что!"

    show dv rage pioneer at left with dspr

    dv "Нет, всё потому, что какая-то мелкая зараза постоянно Шурика изводит!"

    show us upset pioneer at right with dspr

    us "Да что я сделала? Это всё из-за тебя!"

    show dv guilty pioneer at left with dspr

    dv "Нет, из-за тебя!"

    show us angry pioneer at right with dspr

    us "Нет, ты виновата!"
    dv "Нет, ты!"

    window hide

    hide dv
    hide us
    with dissolve

    window show

    "Правы были обе, но я благоразумно промолчал."
    "Мику в принципе не умела с кем-то конфликтовать, но соблюдала девичью солидарность и с кибернетиками почти не общалась. {w}Так что нельзя было просто так пойти и снова попросить починить аппаратуру."
    me "Как у вас всё сложно-то. Ладно, я сам попробую с ними договориться."
    "Алиса отложила гитару, подошла ко мне вплотную и попыталась обнять. {w}Я вежливо отодвинул её."
    "Не обидевшись, рыжая громко прошептала мне на ухо:"

    show dv grin pioneer close at center with dissolve

    dv "Сенька, если чего-нибудь добьёшься, сделаю всё, что хочешь!"
    me "И даже мусорить перестанешь? А то Мику убирать за вами замучалась."

    show dv guilty pioneer close at center with dspr

    dv "Ну, не настолько «всё». Ты ж не наглей. Может, сойдёмся на паре поцелуев?"
    me "Ещё чего. Моё сердце навеки принадлежит тёте Наташе, она заботливая и добрая."

    show dv smile pioneer close at center with dspr

    dv "Дурак! Она же старая для тебя!"
    me "Ну и что? Зато какие булочки печёт!"

    hide dv with dissolve

    me "Ладно, давайте сюда свой гробик, попробую что-нибудь сделать. Со мной они пока не ссорились."

    window hide

    stop ambience fadeout 3

    play music music_list["two_glasses_of_melancholy"] fadein 3

    scene bg ext_clubs_day at bkrr_moving_forward_far(5.0, 1.5) with fade3

    $ renpy.pause(1.5)

    play sound sfx_open_door_clubs

    scene bg int_clubs_male_day with dissolve

    window show

    "Кружок кибернетиков встретил меня запахом канифоли и жужжанием моторчиков."

    scene cg d5_clubs_robot with dissolve

    "На рабочем столе стоял робот с кошачьими ушками, а в его внутренностях увлечённо копошились двое белобрысых пионеров. Из недр робота подымался дымок, голова вертелась, глаза-лампочки быстро перемигивались, а ноги мелко подёргивались."
    me "Здорово, пионеры! Пошто животинку мучите?"
    el "О! Семён, привет!"
    sh "Доброе утро!"
    "Сергей приветственно помахал, а Шурик, вздохнув, пригласил меня войти."
    "Я оставил усилитель у дверей."
    th "Вряд ли кто-то захочет его стянуть. А кто захочет – сам пусть и надрывается."

    window hide

    scene bg int_clubs_male_day
    show sh normal pioneer at center
    with dissolve

    window show

    me "За что вы робота так?"

    show sh smile pioneer at center with dspr

    sh "Да вот, что-то движок заедает. Робот должен аккуратно перешагивать с ноги на ногу, а он прыгает. Регулируем червячную передачу. {w}Знал бы ты, как тут тяжело с деталями… Простую шестерёнку не достанешь!"
    "Я развёл руками."
    me "Шестерёнки нет. Есть только искреннее сочувствие. {w}Сойдёт?"

    show sh serious pioneer at center with dspr

    sh "Спасибо и на этом. Ты как, хотел чего, или просто в гости забежал? А может, решил вступить к нам в кружок наконец?"
    me "Нет, прости, теперь уже не могу. Я вообще-то с просьбой."

    show sh normal_smile pioneer at center with dspr

    sh "Рассказывай."
    "Шурик поправил очки."
    me "У нас тут усилитель немножко сгорел…"

    show sh surprise pioneer at center with dspr

    sh "Как? Опять? Сергей же только чинил. {w}Что вы с ним делаете?"
    me "Нет, это второй. Честь Родины в опасности, сам понимаешь. {w}Нельзя нам перед иностранными товарищами опозориться."

    show sh serious pioneer at center with dspr

    sh "Да, никак нельзя. А чего эти рыжие бандитки тебя прислали?"
    me "Алиса раскаивается за случай с Сергеем, а Улю мучит совесть за утренний эпизод с ватрушкой. {w}Стесняются они, меня попросили. Да и тяжёлый он."

    show sh smile pioneer at center with dspr

    "Шурик улыбнулся."
    sh "Эх! Нас на девчонок променял! {w}На трёх. Хотя и симпатичных, что есть, то есть."

    show sh normal_smile pioneer at center with dspr

    sh "Чего ты, кстати, в группу вступил? Ты же не музыкант, кажется?"
    me "Я сам поражаюсь. Ты разве не слышал?"

    show sh serious pioneer at center with dspr

    sh "Слухи только. Расскажешь, что произошло?"

    window hide

    hide sh with dissolve

    $ renpy.pause(1.0, hard=True)

    window show

    "Я пересказал историю с доской, раненым Толиком и музыкальным рабством, закончив событиями сегодняшнего утра. {w}Особо подчеркнул, что взамен на усилитель Ульяна обязуется больше не подходить к кружку вообще и к Шурику в частности ближе, чем на пять метров. {w}Шурик просиял."

    show sh smile pioneer at center with dissolve

    sh "Да? Раз так, давай сюда больного."

    window hide

    hide sh with dissolve

    $ renpy.pause(1.0, hard=True)

    window show

    "Я втащил куб усилителя и взвалил его на стол."
    me "Вот."
    "Быстрыми точными движениями Шурик раскрутил корпус, заглянул вовнутрь и скривился."

    show sh serious pioneer at center with dissolve

    sh "Ох, вот это гадюшник. Пыль, тараканы, вот и перегрелся."

    show sh upset pioneer at center with dspr

    sh "Нельзя так с техникой! Оставляй, я до завтра всё исправлю. {w}Тут, видишь, конденсаторы повздувались, надо порыться по старым платам, выпаять, я так сразу замену не найду."
    me "Ну, спасибо. Ты очень нас выручаешь. Что я могу сделать взамен?"

    show sh normal_smile pioneer at center with dspr

    sh "Не за что. Главное – Ульяну к нам не подпускай."
    me "Постараюсь. Только ты присмотрись, может, она на тебя виды заимела. {w}Ну знаешь… девочки, они такие. А ты вот так, бессердечно её отвергаешь."

    show sh smile pioneer at center with dspr

    sh "Ульяна? Да ну, глупости. Она же маленькая совсем."

    window hide

    show sh normal pioneer at right with ease

    show el smile pioneer at left with easeinleft

    window show

    el "Шурик у нас мелких не любит. Вот нравилась ему девочка в том году, она в баскетбол играла…"

    window hide

    hide el with easeoutleft

    show sh serious pioneer at center with ease

    window show

    sh "Цыц! Не напоминай!"

    show sh normal_smile pioneer at center with dspr

    "Кибернетик грустно улыбнулся и пояснил:"
    sh "Вечно он меня этой историей подкалывает. Мы, понимаешь, в больнице с одной старшеклассницей познакомились. {w}Она с переломом ноги лежала, а я как раз лодыжку повредил."

    show sh normal pioneer at center with dspr

    sh "Я по ошибке в её палату зашёл, разговорились. Хорошая девочка, физику углублённо изучала. Ей в палате скучно было одной, я в гости ходил. Сидели, беседовали, телевизор смотрели."

    show sh upset pioneer at center with dspr

    sh "Сколько я её видел, она или лежала, или сидела. А потом, уже перед самой выпиской, она встала, чтобы меня проводить. И оказалось, что ростом она метра два, не меньше. {w}В общем, не сложилось."

    hide sh with dissolve

    stop music fadeout 5

    play ambience ambience_clubs_inside_day fadein 3

    "Шурик вздохнул. Его приятель тем временем беззаботно раскачивался на стуле. Лицо у Сыроежки было заспанное, но довольное."
    "С заговорщическим видом он подмигнул мне и улыбнулся ещё шире. Я поискал глазами, куда бы присесть, но ничего не нашлось. Пришлось сесть на стол."
    me "Сыроежка, ты бы лимон скушал."

    show el surprise pioneer at center with dissolve

    el "А?"
    me "Лимон, говорю, скушай. А то лицо сильно счастливое. Лопнешь ведь от счастья."
    "Он развёл руками."

    show el smile pioneer at center with dspr

    el "Сам виноват! Нечего было нас с Женей запирать."
    "Я понизил голос, поинтересовался:"
    me "Ну… это… как всё прошло? Всё в порядке?"

    show el grin pioneer at center with dspr

    el "Как-как. Зашёл я, про танцы с ней поговорили… а потом пригласил погулять, а дверь не открывается. А она меня за галстук и к стенке."

    show el smile pioneer at center with dspr

    el "«Соблазнять меня пришёл, коза новая белобрысая? Чего так долго тянул?»."
    el "И поцеловала."

    show el upset pioneer at center with dspr

    el "Я что, так на козу похож? Даже обидно как-то."
    me "Казанова, наверное. Был такой литературный герой, очень женщин любил."

    show el laugh pioneer at center with dspr

    el "Тогда ладно."

    show el normal pioneer at center with dspr

    el "Ну, в общем, она через чёрный ход вышла, в домик сбегала, принесла сладкого, мы попили чай и целовались до самого отбоя."
    el "Только ты это, не рассказывай, смотри, никому. Хорошо?"
    th "Не сочиняет про бурную ночь, честь дамы бережёт. {w}Джентльмен, понимаешь."
    "Я завистливо вздохнул, улыбнулся."
    me "Красавчик. На свадьбу пригласить не забудь."

    show el grin pioneer at center with dspr

    el "Посмотрим, посмотрим. И да… это… ну, спасибо, что помог."
    me "Не за что."

    hide el with dissolve

    "Шурик посмотрел на нас, хмыкнул. И правда – не по годам серьёзен."
    "Он потянулся и столкнул со стола книгу. {w}Я машинально поймал её, ссадив костяшку об угол стола, глянул на обложку."
    "Г. Уэллс, «Машина времени»."
    me "О, хорошая книга! Люблю про путешествия во времени."
    "Шурик поправил очки."

    show sh smile pioneer at center with dissolve

    sh "Да, мне тоже нравится."

    show sh normal_smile pioneer at center with dspr

    sh "Как знать, может, когда-нибудь советская наука сможет создать устройство для перемещения во времени. {w}Ты представляешь себе все перспективы такого открытия?"
    me "Ты считаешь, что это возможно?"

    show sh serious pioneer at center with dspr

    sh "Наука допускает такую возможность, значит, и техническая реализация – всего лишь вопрос времени. Хотелось бы, знаешь, побывать в другой эпохе."
    me "А где? В прошлом или в будущем?"

    show sh smile pioneer at center with dspr

    sh "Да везде! И на Ивана Грозного посмотреть, и на отлёт Первой Советской Межзвёздной Экспедиции. Как рак победили… как на Марс слетали…"
    th "Эх, Сашка! Знал бы ты, что в моём времени уже нет никакого СССР, «Буран» сгнил, а вместо рака теперь СПИД."
    th "Хотя, не факт, что моё будущее такое же, как ваше. Кстати, почему бы не спросить?"
    me "Раз уж мы заговорили на эту тему. Ты знаешь что-нибудь о параллельных мирах?"

    show sh serious pioneer at center with dspr

    sh "Только название и общие принципы. Неофициально… Ну, есть кое-какие статьи, в той же «Науке и жизни», но никто ничего толком не знает. {w}Общее мнение, что таких миров может быть бесконечное множество."
    sh "Я читал, что мелкие субатомные частицы, кварки называются, теоретически, могут проникать из одного пространства в другое. Значит, тоже теоретически, и б{b}о{/b}льшие объекты могут тоже. Официально эту теорию не слишком признают, доказательств существования никаких…"
    "Доказательство существования параллельных миров спрыгнуло со стола и подошло поближе."
    me "Жаль. Интересно было бы узнать побольше."

    show sh normal pioneer at center with dspr

    sh "А почему тебя это заинтересовало? {w}И вообще, мало кто из наших сверстников вообще знает такое слово. Может, ну её, эту музыку, да пойдёшь всё-таки по научной части?"

    show sh smile pioneer at center with dspr

    sh "Образование – дело наживное, главное – определённый склад ума."
    me "Не могу. Обещание есть обещание. К тому же я не придумал ещё, чем хочу заниматься в будущем. Может, и в науку пойду."

    show sh serious pioneer at center with dspr

    sh "Понимаю. Ну, как знаешь. Хотя, по-моему, наука интереснее."

    hide sh with dissolve

    "Он потерял ко мне интерес и стал рыться в коробочках с радиодеталями."
    "Я обошёл стол, посмотрел на робота."
    "Грубоватый, но любовно сделанный макет человека в натуральную величину. {w}Судя по всё ещё двигающимся ножкам – подвижный. {w}Судя по выпуклостям на корпусе – женский."
    th "Вот ведь маньяки, а?"
    me "И что он будет уметь делать, когда вы его закончите?"

    show el normal pioneer at center with dissolve

    el "Ходить и руками вращать."

    hide el with dissolve

    me "Интересный функционал. А успеете до конца смены?"

    show sh normal pioneer at center with dissolve

    sh "Конечный результат – дело десятое. Главное – процесс."
    me "А что у вас ещё интересного есть?"
    sh "Вот, гляди."

    hide sh with dissolve

    "Он достал из ящика стола мыльницу в форме головы бегемота."
    th "Симпатичная вещичка, детям, наверное, нравилась. {w}До того, как в ней проковыряли дырки, наполнили какой-то электроникой и выпустили наружу кнопку, лампочку и короткую телескопическую антенну."
    "Теперь бегемот был похож на киборга-убийцу."
    "Шурик перекинул выключатель, лампочка загорелась, а из решётки, врезанной в нос бегемота, раздалось шипение."

    play sound sfx_radio_squelch_1

    show sh normal pioneer at center with dissolve

    sh "Знаешь, что это?"
    me "Приёмник в мыльнице?"

    show sh normal_smile pioneer at center with dspr

    sh "Обижаешь! Приёмники для младшеклассников. Стой тут."

    window hide

    hide sh with dissolve

    $ renpy.pause(1.0, hard=True)

    play sound sfx_open_door_clubs_nextroom

    window show

    "Сыроежкин не участвовал в нашем разговоре, а легкомысленно вертел в руках пистолет-паяльник, видимо, воображая его бластером. Шурик ушёл в маленькую кладовку, а затем мыльница вдруг заговорила его голосом."

    play sound sfx_radio_squelch_2

    sh_radio "Раз-раз, проверка связи! Нажми на кнопку и скажи что-нибудь!"
    "Я нажал на кнопку, поднёс мыльницу поближе и сказал первое, что пришло в голову:"
    me "Если б я имел коня – это был бы номер! Если б конь имел меня, я б, наверно, помер!"
    "Серёжка заржал, Шурик через секунду присоединился, затем вышел к нам."

    window hide

    play sound sfx_open_door_clubs_nextroom

    $ renpy.pause(1.0, hard=True)

    show sh smile pioneer at center with dissolve

    window show

    sh "Такие дела. Это мы сами сделали. В кладовке большой передатчик стоит, его кто-то до нас собрал, а это так, баловство, для отдыха спаяли."

    show sh normal pioneer at center with dspr

    sh "Я сам удивился, как проверил дальность: принимает на пять километров, передаёт, кажется, на четыре, всё не соберёмся испытать. {w}Ты, кстати, точно не хочешь к нам?"
    "Внезапно сменил тему он."
    me "Хочу всё больше и больше. Но слово есть слово, сам понимаешь."

    show sh serious pioneer at center with dspr

    sh "Да уж, понимаю. Раз такое дело, ты хоть в гости заходи. {w}А то в этом бабском царстве и поговорить стало не с кем."
    "Электроник обиженно нацелился в Шурика из паяльника."

    window hide

    show sh serious pioneer at right with ease

    show el serious pioneer at left with easeinleft

    window show

    el "Что значит «не с кем»? А я?"

    show sh upset pioneer at right with dspr

    sh "Я имел в виду вообще. {w}К тому же, Серёжа, ты уже потерян для науки до конца смены."
    el "Чего это?"
    sh "А того это! Раз появилась девушка – это всё."

    show sh normal pioneer at right with dspr

    sh "Сначала будешь сбегать в библиотеку по поводу и без, потом гулять с ней за ручку, потом проводить с ней свободное время… и всё, нет кружка. {w}Останусь я тут один, вольтметру на одиночество жаловаться буду."
    sh "Хотя я рад за тебя, Женя умная. И симпатичная."
    "Серёжка поучительно поднял палец."

    show el normal pioneer at left with dspr

    el "Ну, во-первых, даже Эдисон был женат."
    "Шурик отмахнулся и перебил:"

    show sh serious pioneer at right with dspr

    sh "А во-вторых, я тебя не упрекаю. {w}Просто тебе интересны глазки-губки, а мне наука. Только и всего."

    show sh normal pioneer at right with dspr

    sh "Вот, Семён, ты как считаешь?"
    me "Думаю, что вы оба правы. Девушки нужны, науки тоже. Зачем же так их противопоставлять?"
    sh "Интересная мысль. Ну, вот и увидим, как у Серёжи получится совмещать. {w}Кстати… Сыроежкин!"
    el "А?"
    sh "Ты к Жене обещал заскочить до обеда. Обед уже приближается, а ты тут сидишь, паяльники крутишь."

    show el surprise pioneer at left with dspr

    el "Ой… уже бегу!"

    hide el with easeoutleft

    "Сыроежкин посмотрел на часы, торопливо вскочил и побежал к двери, не выпуская паяльника."
    "У самых дверей провод натянулся и не пустил влюблённого кибернетика дальше. Шурик поправил очки."

    show sh smile pioneer at right with dspr

    sh "Паяльник-то оставь… или хоть из розетки выдерни. До библиотеки шнура не хватит."
    el "Ай, не будь занудой!"

    play sound sfx_slam_door_campus

    "Сергей бросил паяльник на подставку и выбежал из кружка."
    "Мы проводили его взглядами. {w}Я – понимающим, Шурик – укоризненным."

    stop ambience fadeout 3

    play music music_list["everyday_theme"] fadein 5

    show sh normal pioneer at center with ease

    sh "Что я и говорил. Влюблённое создание, врубив форсаж, умчалось на свидание."
    me "А я за них рад. Молодость бывает только раз."
    sh "Я тоже, ты не подумай."

    show sh smile pioneer at center with dspr

    "Тут он мечтательно улыбнулся, что-то вспоминая, видимо."
    th "Я-то догадываюсь, о чём он думает, но зачем его зря расстраивать? Интересно, к кому он тогда бегал? Полный лагерь симпатичных пионерок…"
    me "Я и не думал."

    show sh normal_smile pioneer at center with dspr

    sh "Просто у меня другие интересы."
    me "Робота делать?"

    show sh serious pioneer at center with dspr

    sh "Робот это так, баловство. А вот поставить задачу, как одним маломощным движком запитать обе его ноги, поиск решения и его воплощение в металле – вот это удовольствие. {w}Странно звучит?"
    me "Нет. Просто говоришь как немолодой учёный. Ты пионер вообще-то. Не забыл?"
    "Намёк был достаточно прямым, чтобы его понял такой же случайный пришелец, как я. {w}Очень уж по-взрослому он говорил. Вывод напрашивался сам собой. Но Шурик развёл руками."

    show sh normal pioneer at center with dspr

    sh "Знаю, ты не первый, кто меня упрекает."
    sh "Такой уж я есть. Что выросло – то выросло, как моя мама говорит."
    sh "Ладно, я вашу коробку гляну, только после обеда. Не волнуйся, отыграете в лучшем виде. И на будущее: если что-то нужно – просто попросите."
    "Я согласно кивнул."
    me "Договорились."
    "Попрощавшись с Главным Кибернетиком всея «Совёнка», я выскочил на улицу."

    window hide

    stop music fadeout 3

    $ bkrr_timeskip()

    scene bg int_dining_hall_people_day_bkrr with bkrr_circleout_transition

    play ambience ambience_dining_hall_full fadein 3

    $ renpy.pause(1.0, hard=True)

    $ bkrr_set_mode(nvl)

    nvl show dissolve

    "Сегодня на обеде мне досталось уединённое место у окна, так что, жуя, я рассматривал пустынные дорожки и размышлял, правильно ли я сделал, что вообще вступил в музыкальный клуб."
    "С одной стороны, там Мику. {w}С другой – лучшего способа удерживать меня от побега и не придумать. {w}Симпатичная подруга и много работы. {w}Только изредка я мог хоть немного подумать о том, что происходит вокруг."
    "Я так много времени проводил в музыкальном кружке и с девочками, что как-то даже упустил из виду, что в пионерском лагере полагается ещё и отдыхать. {w}Нет, конечно, подготовке лагеря к приезду иностранцев уделялось много времени, но остальные пионеры не вкалывали круглосуточно."

    nvl hide dissolve

    $ renpy.pause(1.0, hard=True)

    show us normal pioneer close at center with dissolve

    $ bkrr_set_mode()

    window show

    us "Сень, а Сень? Можешь доброе дело сделать?"
    me "Доброе, говоришь? А что надо-то? И где девчонки?"

    show us sad pioneer close at center with dspr

    us "Тут такое дело… они заигрались чуть-чуть и решили, что я им обед отнесу. Тётя Наташа бутерброды сделала. Ну и перекус на вечер сразу прихватим."
    me "А я тут при чём?"
    us "Понимаешь, мы с Алиской на пляж идём. Не хочу бегать туда-обратно. {w}Не отнесёшь в клуб? Пожалуйста-пожалуйста! А я за купальником побегу. Ты ведь на пляж не идёшь?"
    me "С чего ты взяла? Иду!"

    show us smile pioneer close at center with dspr

    us "Сень… ты не понял. Это {b}мы{/b} с Алисой на пляж идём. {w}А Мику не идёт. Она в клубе. Одна-одинёшенька. {w}Продолжать?"
    me "Вот оно как… Ты знаешь, я тут вдруг подумал, что жару плохо переношу и загорать не люблю… И плавать не умею!"

    show us grin pioneer close at center with dspr

    us "Я знала, что ты это скажешь. И уже Ольгу Дмитриевну предупредила."
    me "Ты просто прелесть."
    us "Я знаю!"
    "Я ласково взъерошил её волосы."

    show us dontlike pioneer close at center with dspr

    us "Ай! Ну что ты делаешь? Не порти причёску!"
    me "Буду должен!"

    show us smile pioneer close at center with dspr

    us "Ещё как будешь! И не надейся, что я забуду. Ну, иди, бери сумку у тёти Наташи."

    window hide

    stop ambience fadeout 2

    $ bkrr_timeskip_short()

    scene bg int_dining_hall_day with bkrr_timeskip_transition()

    play ambience ambience_dining_hall_empty fadein 3

    window show

    "Сегодня девчонки решили репетировать подольше и отпросились у Ольги Дмитриевны с ужина. {w}Вожатая разрешила, но при условии, что мы полноценно поедим в клубе."

    window hide

    $ bkrr_get_item("food")

    window show

    "Тётя Наташа щедрой рукой отсыпала нам свежайших булочек (обычного хлеба я тут так и не видел, видно, пекли их прямо здесь), несколько пакетов кефира, а для витаминизации набросала сверху спелых яблок и банку сгущённого молока."

    window hide

    stop ambience fadeout 0.5

    scene bg ext_dining_hall_near_day with dissolve

    play ambience ambience_camp_center_day fadein 3

    window show

    "Осторожно придерживая набитую провиантом коробку, я вышел из столовой и двинулся к кружку."
    "Груз получился не то чтобы неподъёмный, но тяжёлый."

    window hide

    stop ambience fadeout 1

    scene bg ext_path_day with fade

    play ambience ambience_forest_day fadein 3

    window show

    "Идти через раскалённую площадь не хотелось, так что я решил сделать небольшой крюк вокруг столовой и пройти по тенистой тропинке за медпунктом."
    "Тут за кустами мелькнуло что-то коричневое. Не собака, слишком здоровая туша."
    th "Бурёнка, что ли, какая заблудилась?"
    "Я осторожно подошёл поближе и удивлённо-восхищённо охнул. {w}Прямо передо мной стоял олень."
    "Не знаю, как вообще выглядит обычный олень, в зоопарке был давным-давно, но этот наверняка был обычным. {w}Невысокий, короткие рожки, бока в белых пятнах."
    "Чем-то он напоминал большую бродячую собаку. Взъерошенный какой-то, в репьях, грязноватый. Совсем не диснеевский Бэмби."
    me "Эй… иди сюда! Держи!"
    "Я поставил коробку с провизией, отломил половинку булки, раскрошил и протянул ему."
    "Олень с интересом оглядел меня, пофыркал, потом подошёл поближе и принялся жевать хлебный мякиш. Осторожно, чтобы не спугнуть, я вытянул вторую руку и почесал его между рогами."
    me "Непорядок вообще-то. Ты же гордое дикое животное! Ты должен сам добывать себе еду. Разве нет?"
    "Гордое дикое животное вздрогнуло, но жевать не перестало, зато замахало ушами. Почему-то стало смешно."
    "Из-за спины негромко донеслось:"
    un_v "Ты неплохо ладишь с животными…"

    show un smile pioneer at center with dissolve

    "Почему-то я ожидал увидеть Славяну, но это оказалась Лена."

    show un smile pioneer close at center with dspr

    "Она медленно приблизилась и присела рядом. Олень засопел, но не ушёл, только косил на Лену карим глазом."
    un "Как ты его приманил?"
    me "Да… не знаю, как вышло. Наверное, он просто есть хотел."
    "Олень дожевал половинку булки и вопросительно посмотрел на меня. Я понял намёк и дал ему ещё."

    show un normal pioneer close at center with dspr

    un "Он приходит сюда. {w}Иногда."
    un "Но обычно, если рядом кто-то чужой, то он не показывается. Я его подкармливаю время от времени. А вот к тебе почему-то подошёл."

    show un smile pioneer close at center with dspr

    un "Наверное, ты хороший человек. Животные это чуют. Ну, я-то сразу это поняла."

    hide un with dissolve

    "Я невольно задумался."
    th "А ведь мы с Леной познакомились сразу же… но после нескольких попыток разговорить её я сдался."
    th "А потом эта история с музыкальным кружком закрутила меня, и всё. Почему так вышло?"
    "Ведь Лена мне симпатична. Не знаю, чем, может, эта её трогательная застенчивость так действует."
    me "А ты любишь животных?"

    show un smile pioneer close at center with dissolve

    un "Очень! Я в охотничьем хозяйстве часто бывала. Охоту не очень люблю, мне зверушек жалко, а вот подкармливать, с детёнышами возиться любила."
    me "Здорово. У тебя кто-то охотник в семье? Или просто так ездила?"

    show un normal pioneer close at center with dspr

    "В детстве я любил наблюдать за улитками после дождя."
    "Стоило приблизиться, как она пряталась в раковину, но если посидеть достаточно долго, то из раковины выглядывали рожки, а затем и сама улитка. Что-то подобное происходило сейчас."
    "Лена грустно покачала головой."
    un "Прости, я не хочу об этом. Ты не обидишься?"
    me "Нет, конечно. На вот, лучше покорми Бяшку."
    "Я дал ей яблоко. Лена протянула его оленю и удивлённо глянула на меня."

    show un surprise pioneer close at center with dspr

    un "Кого-кого?"
    me "Ну, Бяшку. Не знаю, как ласково называют оленей, так что будет Бяшка."

    window hide

    show un laugh pioneer close at center with dspr

    $ renpy.pause(1.0, hard=True)

    show un smile pioneer close at center with dspr

    window show

    "На секунду её лицо осветилось улыбкой, и я даже услышал негромкий смешок. {w}Лёгкий, едва слышный."
    "Лена взяла яблоко и протянула оленю. Тот с аппетитом принялся его есть прямо с рук."
    un "Бяшка… Скажешь тоже. Он же не барашек. {w}Но мне нравится. А тебе, Бяшка?"
    "Олень снова издал нечто среднее между рёвом и блеяньем."
    un "Кажется, ему тоже."
    me "А ты ему не придумала имени?"

    show un shy pioneer close at center with dspr

    un "Нет. А зачем оно ему?"
    me "Пригодится. Вдруг ещё один заведётся, вот и будем их различать."

    show un smile pioneer close at center with dspr

    un "Логично. Давай вместе?"
    me "Знаешь, оленьим крёстным мне ещё не приходилось выступать. Давай!"

    window hide

    $ renpy.pause(0.5, hard=True)

    show un laugh pioneer close at center with dspr

    $ renpy.pause(1.0, hard=True)

    stop ambience fadeout 3

    play music music_list["what_do_you_think_of_me"] fadein 3

    scene cg d8_deer:
        subpixel True
        ypos -360
        ease 5.0 ypos -120
    with fade3

    play ambience ambience_forest_day fadein 3

    $ renpy.pause(2.0, hard=True)

    window show

    "Минут пять мы обсуждали, как можно назвать эту неопрятную живность. {w}Лена выдвигала литературно-аристократические версии вроде Эшли, Рудольфа и прочих. {w}Я склонялся к традиционно русским вроде Васьки и Емели. {w}Наконец сошлись на том, что звать его будем по имени-отчеству. Рудольф Васильевич."
    "Занимались мы, конечно, откровенной ерундой, но это было так весело…"
    "Лена повернулась ко мне, довольно улыбаясь."
    un "Ты так изменился со дня приезда."
    me "Сильно?"
    un "Да нет. Просто повеселел. Я когда увидела тебя в первый день, ты был какой-то, м-м-м…"
    me "Перепуганный?"
    th "Ну, с учётом того, что случилось, ничего странного. Не каждый день в прошлое проваливаешься, к такому привыкнуть нужно."
    th "Она… обратила на меня внимание ещё тогда? Интересно. И почему-то приятно."
    un "Ну, нет. Скорее грустный. А сейчас – другое дело."
    me "Да и ты тоже… не такая, как обычно. И, по секрету, у тебя очень симпатичная улыбка, я был бы рад видеть её почаще."
    "Она, кажется, очень серьёзно обдумала мою просьбу, затем улыбнулась чуть пошире и подытожила:"
    un "Хорошо, я постараюсь."
    me "Рад это слышать. Странно как-то выходит, вроде бы и познакомились сразу, как я сюда приехал, а почти не общаемся."
    un "Ну, ты почти всё время проводишь с этими… тремя мушкетёрами."
    me "Интересное прозвище. Славя тоже их так называла."
    "Рудольф озадаченно переводил взгляд с меня на Лену и обратно, пытаясь понять, зачем мы трясёмся и издаём странные звуки."
    th "Интересно, олени знают, что такое смех?"
    un "Ну да, девчонки их так зовут. Мы ведь из одной школы, ну ты знаешь, наверное?"
    me "Нет, не слышал. Я же на неделю позже приехал, многого ещё не знаю."
    un "Да, точно, я подзабыла. Они с первого дня сдружились, хотя Мику и Ульяну представить вместе в одной компании тяжело."
    me "Как там у Пушкина… «Они сошлись, вода и камень, чего-то там, и лёд и пламень…»."
    "Лена улыбнулась и кивнула."
    un "«Чего-то там»… Ну да. Это точно Пушкин."
    un "Ты поэзию любишь?"
    me "Читать – да. А вот наизусть как-то не получается."
    un "Ничего…"
    me "Знаешь, Славяна ожидала, что четвёртым мушкетёром будешь ты."

    window hide

    scene bg ext_path_day
    show un shy pioneer close at center
    with dissolve

    window show

    un "Вы обо мне со Славей разговаривали? А почему?"
    "Лена с интересом посмотрела на меня."
    me "Э… к слову пришлось. Она говорила, что хотела бы, чтобы вы побольше общались, ну и как-то слово за слово и вышли на эту тему."

    show un sad pioneer close at center with dspr

    "Ответом был разочарованный вздох. Лена покачала головой."
    un "Вот оно что… Славя, она хорошая, добрая. Но не всё понимает."

    show un normal pioneer close at center with dspr

    un "Знаешь, есть такие люди, которым не составляет трудности подружиться с кем-то? А есть такие, для которых это, наоборот, очень тяжело."
    me "Знаю, у меня то же самое. Для меня это всегда было непросто."
    un "Может, поэтому мы с тобой особо и не разговаривали. Я тоже такая."
    me "Кажется, я понимаю, о чём ты. Ну, мы-то с тобой друзья? Мы вот даже одного оленя кормим!"

    show un smile pioneer close at center with dspr

    "Лена согласно кивнула."
    un "Да, повод не хуже другого. Друзья!"
    me "Жаль только, что так редко разговариваем."

    show un normal pioneer close at center with dspr

    un "Да, мне тоже жаль. Ну, это не из-за тебя. Просто ты почти всё время проводишь с Алисой, а мы с ней…"

    window hide

    $ renpy.pause(1.0, hard=True)

    hide un with dissolve

    stop music fadeout 10

    $ renpy.pause(1.0, hard=True)

    window show

    "Она задумалась. Мы помолчали, одновременно почёсывая пятнистые оленьи бока."
    "В романтических фильмах в такой момент, как правило, руки героев соприкасаются, парочка смотрит друг другу в глаза, а потом сливается в поцелуе."
    th "Но… не знаю. Что-то меня останавливало."
    th "Чего вроде бы ещё? Симпатичная зеленоглазая пионерка, романтическая обстановка, даже, вот, олень лежит."
    "Мелькнула мысль, что всё могло сложиться иначе. {w}Но сейчас я уже не мог воспринимать её иначе, чем подругу, пусть и близкую. {w}Даже сейчас я думал, что скоро увижу Мику."
    "Лена вздохнула и продолжила, обращаясь даже не столько ко мне, сколько в пространство:"

    show un normal pioneer close at center with dissolve

    un "А мы с Двачевской сейчас не ладим. {w}Потому и с тобой особо не болтали."
    un "Ну не в столовой же к тебе с разговорами цепляться, верно?"
    me "Случается и такое. Можно и в столовой. Кое-кого это никогда не останавливало."

    show un smile pioneer close at center with dspr

    th "Банальное замечание, но чем ещё я мог заполнить неловкую паузу."
    "Лена продолжала перебирать оленью шерсть. Сейчас она явно думала о чём-то своём и улыбалась."
    "И у неё действительно потрясающе красивая улыбка. Я думал, что Лена просто не услышала моих слов, но после паузы она кивнула."
    un "Да."

    hide un with dissolve

    th "Кажется, ответа никто и не ожидал."
    "Разговор зашёл в тупик."
    th "Сейчас она встанет и уйдёт, а между нами останется неловкость. А неловкости я не люблю. Попробуем разрядить обстановку."

    window hide

    scene cg d8_deer with dissolve

    window show

    "Я протянул руку и почесал оленя между ушей."
    me "Ну, во всяком случае, сейчас мы с тобой выкроили время. Бяшка помог, раз уж два человека разумных не справляются. {w}Надеюсь, это не последний раз."
    "Она улыбнулась, хотя в глазах оставалось какое-то странное выражение."
    un "Верно. Я тоже надеюсь, что не последний."
    "Лена вдруг поинтересовалась:"
    un "Я слышала от Мику, что ты теперь будешь играть с ними и сейчас ускоренно учишься."
    me "Вроде того…"
    un "Удивительно, как ты вообще согласился, если играть не умеешь. Я бы не решилась."
    me "Меня особо не спрашивали, ухватили за шкирку, дали в зубы гитару и стали учить. Добровольно-принудительно."
    "Лена звонко рассмеялась."
    un "Да… Мику мне всё пересказала. В лицах."
    me "Могу себе представить. Глупо, наверное, выглядело?"
    un "Да нет, по-моему, весело. Особенно, когда ты бежать пытался. Ты правда рвал на груди рубашку и кричал «русские не сдаются»?"
    me "Не припомню такого."
    un "Вот выдумщица. Значит, сочинила. А так смешно показывала…"
    me "Мне вообще смешно, как я во всё это ввязался. Вот только боюсь не справиться."
    un "Знаешь, мне папа одну вещь рассказывал. Что есть два вида страха: первый – помогает стать лучше, второй – сковывает и не даёт делать даже то, что умеешь. И вот в первом ничего плохого нет, он заставляет тебя напрягать все силы и достичь цели."
    me "Интересная теория. Мне нравится. Он философию не преподаёт случайно?"
    un "Нет, он охотник. {w}Был."

    window hide

    scene bg ext_path_day with dissolve

    $ renpy.pause(1.0, hard=True)

    window show

    "Мы ещё немного помолчали, на этот раз напряжения не было. Олень потыкался мордой в коробку, норовя урвать ещё что-нибудь вкусное."
    th "Ну уж нет, родной, свою порцию я тебе скормил, а чужую не дам, девчонки меня за такое расточительство заругают."
    "Лена улыбнулась."

    show un smile2 pioneer close at center with dissolve

    un "Всё, теперь вы друзья навсегда. Ну, или пока кормить будешь. Не разбалуй его, смотри. А то лопнет."
    me "Постараюсь."

    show un smile pioneer close at center with dspr

    un "Ладно. Я пойду, ты не против?"
    "Она вопросительно посмотрела на меня."
    th "По-моему, в её глазах было ожидание, что я буду возражать и попрошу посидеть ещё. Даже надежда."
    "Увы, я уже сделал свой выбор."
    "С непонятным сожалением я кивнул."
    me "Жаль, конечно, хорошо посидели. Ну, ничего, ещё увидимся. Беги, конечно."
    "Она не выглядела разочарованной, но я всё равно чувствовал себя не очень уютно, словно чем-то обидел её."

    show un smile pioneer at center with dspr

    "Ещё одна улыбка."
    un "Увидимся на ужине."

    hide un with dissolve

    "Я проводил Лену взглядом."
    th "Такая милая девушка…"
    th "Не знаю, может, причиной был мой нерешительный характер, а может – просто какие-то детские комплексы или просто понятное желание защищать и оберегать, но именно такие, застенчивые, мне всегда нравились."
    th "Интересно, на что было бы похоже – встречаться с ней? Наверное, романтично. Кино, сладкая вата, мороженое в парке."
    "Я усмехнулся. Всё-таки это молодое тело даёт о себе знать."
    th "Ну, меня ждёт другая красавица."

    window hide

    stop ambience fadeout 3

    scene bg ext_music_club_day_bkrr with fade3

    play ambience ambience_camp_center_day fadein 3

    window show

    "Странно, но я уже привык считать музыкальный клуб своим домом. {w}Такая себе сумасшедшая квартирка."
    "Нам было весело и, пожалуй, не совру, если скажу, что мы всё больше и больше сближались. {w}Постепенно я научился ладить с Алисой, иногда даже получалось предугадывать, что может выкинуть Ульяна… {w}И я всё сильнее привязывался к Мику."
    "Она могла быть незаметной, но без неё сразу становилось неуютно. {w}Как воздух, как земля под ногами. {w}Мы не замечаем их, но сразу ощущаем их отсутствие. {w}Весь остаток дня мы проведём вместе. Разве не здорово?"

    window hide

    scene bg ext_music_club_verandah_day_v3 with dissolve

    window show

    "Сквозь открытое окно я увидел Мику."
    "Она сидела на горе матрасов, болтала ногами и наигрывала на гитаре незнакомую мне мелодию. Больше в клубе никого не было видно."
    "Девчонки имели привычку переодеваться прямо здесь, так что я на всякий случай повысил голос."
    me "К вам можно?"
    "Мику увидела меня, улыбнулась, отложила гитару и соскочила на пол. "

    play sound sfx_open_door_2

    extend "Ещё секунда, и меня взяли за руку и увлекли внутрь."

    window hide

    stop ambience fadeout 0.5

    scene bg int_music_club_mattresses_day with dissolve

    play ambience ambience_music_club_day fadein 3

    play music music_list["sweet_darkness"] fadein 5

    window show

    "Мику тянула меня к инструментам, попутно рассказывая, как ей было скучно."

    show mi normal pioneer at center with dissolve

    mi "К нам нужно! Никого нет, я тут одна сижу. Полчаса с обеда прошло, все разбежались, жду, когда ты придёшь, а тебя нет. Я уже и играла, и пела, уходить собиралась!"

    show mi smile pioneer at center with dspr

    mi "А что там у тебя в коробке?"
    me "Тётя Наташа снабдила нас провиантом. Кефир, булки, яблоки, ещё что-то там."

    show mi surprise pioneer at center with dspr

    mi "Ого! Сколько всего. Как мы это всё есть будем? Нас же всего четверо."
    me "Втроём. Я свою порцию оленю скормил."
    mi "Оленю?"

    show mi shocked pioneer at center with dspr

    "Мику удивлённо посмотрела на меня."
    me "Ага. Оленю. Шёл с обеда, встретил оленя, не удержался и покормил."

    show mi smile pioneer at center with dspr

    mi "Ой, как интересно! Лена рассказывала, что к столовой олень приходит, но я его не видела ни разу. А жалко…"

    show mi happy pioneer at center with dspr

    me "Как-нибудь вместе попробуем его покормить. Отправим Алису и Ульянку играть и пойдём. Кстати, а где это они?"
    "Конечно, я знал ответ, но всё-таки…"

    show mi normal pioneer at center with dspr

    mi "На пляж ушли. До ужина не появятся."
    me "А ты чего не пошла?"
    "Мику смутилась."

    show mi upset pioneer at center with dspr

    mi "Просто…"

    show mi normal pioneer at center with dspr

    mi "… не хочется."
    me "Не любишь загорать?"

    show mi normal pioneer at center with dspr

    mi "Загорать – не очень. Я сгораю легко, у меня кожа светлая, я так хожу, по полчасика утром и вечером, если есть время."

    show mi dontlike pioneer at center with dspr

    mi "А почему ты выспрашиваешь про наших рыженьких? Тебе со мной не интересно, да?"
    "Мику притворно нахмурилась."
    mi "Я, может, с ним побыть хотела, а он по этим двум скучает!"

    show mi normal pioneer close at center with dspr

    "Как и тогда, после танцев, я потянулся к Мику, осторожно завёл руки под водопад её волос и обнял её."
    "Мику вздрогнула, но не отстранилась."
    me "Я по ним не скучаю, наоборот: я очень рад, что наконец-то мы побудем вдвоём. Впервые за целый день."

    window hide

    show mi shy pioneer close at center with dspr

    $ renpy.pause(1.0, hard=True)

    show mi smile pioneer close at center with dspr

    window show

    "Мику смущённо посмотрела в сторону и несмело обняла меня в ответ."

    stop music fadeout 5

    mi "Ты… тоже рад?"
    "От этого «тоже» сердце радостно ёкнуло. Я кивнул, протянул руку и погладил её по голове."
    me "Ну, конечно. Мне нравится, когда ты рядом."

    show mi happy pioneer close at center with dspr

    "Она ничего не ответила, только положила голову мне на плечо и улыбнулась."
    me "Мику, я вот тут подумал…"

    show mi smile pioneer close at center with dspr

    mi "Да?"
    me "Может, раз половины группы нет, пойдём прогуляемся?"

    show mi dontlike pioneer close at center with dspr

    "Мику с напускной строгостью заглянула мне в глаза."
    mi "Ай-яй. Сеня, ты что, решил расслабиться? Гитара сама играть не научится. Репетировать можно и вообще одному. А ты не один, я…"
    "Она запнулась."

    window hide

    show mi upset pioneer close at center with dspr

    $ renpy.pause(1.0, hard=True)

    show mi smile pioneer close at center with dspr

    window show

    mi "Я с тобой!"
    me "Ничего я не решил. Я так, для порядка поинтересовался. Вдруг ты хочешь отдохнуть, а тут со мной возиться нужно?"

    show mi normal pioneer close at center with dspr

    mi "Какой ты внимательный! Иногда слишком. Не мешаешь, не волнуйся. {w}Будем репетировать? Ты как? Готов?"
    me "Будем! Пионер, он всегда готов!"

    play music music_list["afterword"] fadein 5

    "Мику подождала немного, потом деликатно потыкала пальчиком мне в руку."

    show mi smile pioneer close at center with dspr

    mi "Тогда придётся тебе меня отпустить. А то я до гитары не дотянусь…"
    me "А без этого никак? Мне так больше нравится."
    "Негромкий смешок. {w}Длинные хвостики качнулись, пощекотав мне руки, и Мику со вздохом ответила, что никак."
    me "Жалко…"

    show mi normal pioneer close at center with dspr

    mi "Мне тоже. Когда ты так делаешь, мне так… приятно."
    "Последние слова прозвучали еле слышно."
    me "Тогда посидим ещё немного? И репетировать."

    show mi happy pioneer close at center with dspr

    mi "Хорошо…"

    hide mi with dissolve

    "Мику улыбнулась и прижалась ко мне."
    "Пользуясь удобным моментом, я снова попытался поцеловать её, и снова она, тихо смеясь, увернулась."
    th "Как ей это удаётся? Кошки-мышки какие-то."
    "Наконец, со вздохом я отпустил её и кивнул."
    me "Ну что, поиграем?"
    "Мику подхватила электрогитару из стойки и присела на «диван» из матрасов."

    show mi normal pioneer at center with dissolve

    mi "Садись, бери инструмент, разрабатывай пальцы. Пальцы – это наше всё! Ты как, не устал после вчерашних танцев?"
    me "О, у меня тяжелейшее растяжение мышц!"
    "Она всполошилась."

    show mi upset pioneer at center with dspr

    mi "Да? Ой, ну что же ты не сказал? Не руки, надеюсь? Тебе сейчас калечиться нельзя! Тебе руки беречь надо."
    "Я присел рядом на стуле, устроил бас поудобнее и пробежался по струнам, демонстрируя, что с руками всё в порядке."
    me "Да нет, только лицевых! Улыбался всю ночь, как ненормальный, вспоминая наши с тобой танцы."

    show mi laugh pioneer close at center with dspr

    "Мику хлопнула меня по руке, а затем по клубу разнёсся её смех."

    show mi smile pioneer close at center with dspr

    mi "Ну тебя! Напугал! У меня то же самое. Лена говорит, я всю ночь хихикала и говорила «ещё один танец, ну ещё один». Жаль только, я сон не запомнила."
    me "Надеюсь, он был с моим участием?"

    show mi normal pioneer close at center with dspr

    mi "Может быть, может быть."

    hide mi with dissolve

    "Она загадочно улыбнулась, потом буднично попросила включить драм-бокс."
    "Коробка загудела, а потом начала издавать знакомый барабанный ритм. Будь аппарат чуть побольше, я бы заподозрил, что внутри сидит Ульяна."
    "То ли потому, что мне хотелось порадовать Мику, то ли просто от хорошего настроения, но сегодня выходило лучше обычного. Я с удивлением слушал, как под один и тот же ритм Мику ухитрялась играть совершенно разные мелодии."
    "Моё дело было маленькое – дёргать струны под барабан."

    stop music fadeout 5

    "Во время перерыва я поинтересовался:"

    show mi normal pioneer at center with dissolve

    me "Мику, всё забываю спросить. Вы ведь говорили, что играем пять песен, да?"
    mi "Верно."
    me "А партий восемь. Мне, конечно, не тяжело, но почему больше?"
    mi "Так надо. Всякое может быть. Могут на бис позвать, могут одну песню отменить."

    show mi smile pioneer at center with dspr

    mi "К тому же тебе это на пользу, одно и то же подряд повторять тяжело. Если поочерёдно играть разные мелодии, то голова лучше работает и запоминать легче."
    me "Кажется, да. Кстати, а что за мелодию ты играла, когда я пришёл?"

    show mi shy pioneer at center with dspr

    "Она слегка покраснела."
    mi "А тебе… нравится?"
    me "Очень. Не слышал её раньше."

    show mi smile pioneer at center with dspr

    mi "Это я перед сном сочинила… ну как сочинила. Придумала, записала сразу, а потом начала додумывать кусочки, и получилась вот такая мелодия, только я её ещё не закончила, подбирала музыку дальше. Знаешь, это потому что у меня настроение хорошее было."
    me "Значит, тебе вчера тоже было весело?"
    mi "Ну, конечно! Особенно, когда Алиска нас ругала."
    me "Ох уж эта Алиса. Знаешь, я немножко удивлён, что вы подруги. Вы такие непохожие! {w}Это из-за музыки, да?"

    show mi upset pioneer at center with dspr

    mi "Не только… знаешь, когда я только пришла в школу, то меня не очень хорошо приняли. Ну, сам понимаешь, я немножко отличаюсь. Да ещё и говорила с акцентом, понимала не всё."
    me "А сколько тебе тогда было?"

    show mi normal pioneer at center with dspr

    mi "Пять лет назад."
    me "Всего пять лет, и ты так здорово говоришь по-русски?"
    mi "Ну да, мама с папой не сразу поженились, я сначала в Японии жила, а потом мы сюда переехали. Много читала на русском, в школу при посольстве ходила. Мы сразу определились, что будем переезжать, так что готовились заранее."
    me "Вот оно как."

    play music music_list["reminiscences"] fadein 5

    show mi sad_smile pioneer at center with dspr

    mi "Так вот… здесь, в школе, у меня друзей не было. Обижать не обижали, но никто сидеть вместе не хотел, учебником никто не поделится, только если учитель скажет."

    window hide

    $ renpy.pause(1.0, hard=True)

    hide mi with dissolve

    window show

    "Она вздохнула, видимо, вспоминая то время."
    "Я отложил бас, пересел к ней поближе, приобнял за плечи."
    me "Дети бывают жестокими."

    show mi sad pioneer close at center with dissolve

    mi "Не жестокими – равнодушными."
    mi "Мне было одиноко. Я от этого даже плакала иногда, думала, что так ни с кем и не подружусь."

    show mi sad_smile pioneer close at center with dspr

    mi "А потом на физкультуре я одного мальчика обогнала, он от зависти меня косоглазой назвал. {w}Я плакать начала, тут рыжая девочка подбежала и в глаз ему дала, хотела драку устроить, я её еле оттащила. {w}Это Алиса была."

    window hide

    scene cg d8_chibi with bkrr_circleout_transition

    window show

    "Я живо представил себе малолетнюю Алису, дрыгающую ногами и размахивающую кулачками, в то время как Мику пытается её удержать. Картинка получалась такая, что я еле сдерживал смех. Сидящая рядом Мику недоумённо посмотрела на меня."

    window hide

    scene bg int_music_club_mattresses_day
    show mi surprise pioneer close at center
    with bkrr_circlein_transition

    window show

    mi "Ты чего?"
    me "Да так… представил вас с Алисой маленькими."

    show mi smile pioneer close at center with dspr

    "Мику тоже улыбнулась, затем продолжила."
    mi "Ну а потом знаешь, как бывает. Алиса познакомила меня с Леной и Ульяной."

    show mi normal pioneer close at center with dspr

    stop music fadeout 5

    mi "Мы все музыкой увлекаемся, книжки-фильмы одинаковые любим, как-то так вот вышло. Ульяна мне с математикой помогала, Алиса – с химией, Лена – с русским языком… {w}А я им с музыкой помогала и готовить учила. Меня мама с детства учит."
    me "И как?"

    show mi laugh pioneer close at center with dspr

    "Мику негромко рассмеялась."
    mi "Ульяна ещё туда-сюда, а Алискин предел – бутерброд ровно намазать. Только ей этого не говори."
    me "Группу создавать не думали?"

    show mi normal pioneer close at center with dspr

    "Мику неопределённо покачала головой."
    mi "Вряд ли. Алиса, по-моему, хочет стать гитаристкой. Может, у них с Толиком что-то и выйдет. Я музыку люблю, но всю жизнь ей заниматься не хочу. Она даётся так легко, что это бывает скучно."
    mi "Хочется стать учителем музыки, а не музыкантом, вот, на тебе тренируюсь. Больше-то не на ком…"
    me "Ты замечательный учитель. А ещё можно на кошках тренироваться!"

    show mi serious pioneer close at center with dspr

    mi "На кошках? Ну, Пират вон сидит, а при чём тут кошки?"
    me "Фильм есть такой, «Операция Ы», там…"

    window hide

    hide mi with dissolve

    $ renpy.pause(1.0, hard=True)

    window show

    "Я пересказал ей сюжет сценки с кошками-копилками и хлороформом."
    "Пират проснулся от нашего смеха, подошёл, проверил содержимое коробки, не нашёл там колбасы и разочарованно вернулся в свой угол."

    show mi normal pioneer close at center with dissolve

    mi "Знаешь, я его не видела. Интересный, наверное! Приеду домой – обязательно посмотрю!"
    me "Хотел бы я составить тебе компанию. Ты так красиво смеёшься, а там смешных сценок очень много."
    th "Да и сцена с поцелуем тоже есть…"
    "Мысленно добавил я."

    show mi smile pioneer close at center with dspr

    mi "Ну, это ещё когда будет. А завтра хочешь, вместе в кино сходим? Я ведь обещала, что пойду с тобой."
    me "Припоминаю такое. Только, если это просто из-за обещания, то не нужно себя заставлять."

    window hide

    show mi upset pioneer close at center with dspr

    $ renpy.pause(1.0, hard=True)

    show mi dontlike pioneer close at center with dspr

    window show

    "Мику вздохнула и несильно шлёпнула меня по руке."

    play music music_list["so_good_to_be_careless"] fadein 5

    mi "Сень, ты вроде умный, а бываешь такой… непонятливый."

    show mi smile pioneer close at center with dspr

    mi "Я тебя приглашаю, а ты ещё отговариваешься. Мог бы и сам пригласить, кстати."
    me "Не мог. Я не знал, что тут кино крутят."

    show mi laugh pioneer close at center with dspr

    mi "А, точно. Я опять забыла, что ты тут не с начала смены."

    show mi normal pioneer close at center with dspr

    mi "Ну а теперь-то знаешь?"

    "В памяти почему-то всплыли строки «Нам нужен король мудрый, благородный и способный понимать намёки тоньше, чем летящий ему в лицо кирпич»."
    me "Мику, мне тут одна замечательная девушка подсказала, что завтра кино будет. Я бы очень-очень хотел, чтобы ты со мной пошла."

    show mi smile pioneer close at center with dspr

    mi "Ой, я даже не знаю. Так внезапно… {w}Мне надо подумать!"

    hide mi with dissolve

    "Она притворилась, что погрузилась в раздумья. Я тем временем играл концами её длинных хвостиков."
    th "Интересно, как она ухитряется не садиться на них? А плавать с ними? А расчёсывать? Какие шелковистые волосы, касаться их так приятно."
    "Наконец, я не выдержал:"
    me "Итак, каков будет твой положительный ответ?"

    show mi normal pioneer close at center with dissolve

    mi "Я согласна! Но раз мы идём в кино, то репетиция будет короче. А значит – сегодня надо будет поработать побольше! Бери гитару!"
    "Я с сожалением оторвался от игры с её волосами и снова взялся за бас."
    me "Командуй."
    mi "Вот тебе кусочек для изучения на сегодня. Сначала послушай, я сыграю…"

    window hide

    stop music fadeout 3

    stop ambience fadeout 3

    $ bkrr_timeskip()

    scene bg int_music_club_mattresses_sunset with bkrr_circleout_transition

    $ bkrr_set_time("sunset")

    play ambience ambience_music_club_day fadein 3

    play music music_list["silhouette_in_sunset"] fadein 7.5

    window show

    "Через какое-то время моя наставница довольно похлопала меня по спине. Я прислонил бас к стене, повалился на матрас и раскинул руки."
    me "Ну как? Я заслужил сегодня свой ужин?"
    "Мику повернулась ко мне и радостно кивнула."

    show mi normal pioneer at center with dissolve

    mi "Ты молодец! Главное – не останавливайся, и всё получится."
    me "Ну, отыграть то, что надо, смогу. Не уверен, но постараюсь."
    mi "Ты не веришь в свои силы? А я вот верю, что ты сможешь. {w}И Ульянка верит. {w}Алиса тоже, но она на тебя рычит, чтобы ты старался."
    me "Я стараюсь!"

    show mi smile pioneer at center with dspr

    mi "Если стараешься, то всё обязательно получится! Я думаю, хватит на сегодня. После ужина я буду занята, зато завтра…"
    me "А завтра снова, на том же месте…"

    show mi normal pioneer at center with dspr

    mi "И в тот же час!"

    window hide

    stop ambience fadeout 3

    scene bg ext_music_club_sunset_bkrr with fade3

    play ambience ambience_camp_center_evening fadein 3

    window show

    "Алиса с Ульяной так и не появились. {w}Поздняя репетиция, судя по всему, отменилась, и мы решили пойти поужинать со всеми, оставив принесённую еду на следующий раз."

    show mi normal pioneer at center with dissolve

    me "Пойдём, провожу тебя до столовой."

    window hide

    scene bg ext_houses_sunset with dissolve

    window show

    "Пока мы шли по длинной аллее, ведущей от кружка к душевым, я взял её за руку. Мику смутилась."

    show mi shy pioneer close at center with dissolve

    mi "А если увидят?"
    me "А что такого?"
    mi "Шушукаться станут…"
    me "Пускай завидуют. Я веду за руку самую красивую девушку в лагере."
    mi "Ой, ну скажешь тоже…"
    me "Скажу-скажу. И не раз."

    window hide

    show mi smile pioneer close at center with dspr

    $ renpy.pause(1.0, hard=True)

    show mi happy pioneer close at center with dspr

    stop ambience fadeout 2

    $ bkrr_timeskip_short()

    scene bg ext_square_sunset with bkrr_timeskip_transition()

    play ambience ambience_camp_center_evening fadein 3

    window show

    "После ужина Ольга Дмитриевна забрала Мику в вожатскую, где они вместе работали над сценарием."
    "Ульяна убежала по своим делам, а Алиса ушла в клуб, сказав, что устала после пляжа и хочет поиграть в одиночестве, а не заниматься моим обучением."
    "Раз уж у меня внезапно образовалось свободное время, я решил прогуляться по лагерю и посмотреть, что к чему."

    window hide

    stop ambience fadeout 3

    scene bg ext_playground_sunset_bkrr with fade3

    play ambience ambience_camp_center_evening fadein 3

    window show

    "Возле спортплощадки я увидел кибернетиков, перетаскивающих деревянные кресла из склада в спортзал."
    me "Привет! Что это вы?"

    show sh normal pioneer at center with dissolve

    sh "Да вот, завтра кино будет, кинозал обустраиваем."
    "Он размял плечи, глянул на часы."

    show sh normal_smile pioneer at center with dspr

    sh "Точнее сказать, закончили. {w}Семён, тут один блок остался, ты не поможешь Серёжке вовнутрь занести, а то у меня дело срочное?"
    me "Да, конечно. Беги давай."

    window hide

    hide sh with dissolve

    $ renpy.pause(1.0, hard=True)

    window show

    "Мы с Электроником втянули последний блок кресел в спортзал и присели на скамейке у входа."

    stop music fadeout 5

    show el smile shirt at center with dissolve

    el "Ну… если хоть одно из них завтра не будет занятым, я кого-нибудь побью!"
    me "Я со своей стороны обещаю занять два. Меня бить не нужно."
    el "Я тоже два. А ты с кем?"
    me "С Мику, конечно. С кем же ещё?"

    show el laugh shirt at center with dspr

    el "Вот оно что! А рассказывал: «заставили», «басистом стать хочу»."
    me "Меня правда заставили!"

    show el smile shirt at center with dspr

    el "А ты и не против."
    me "Конечно, не против. А ты, значит, с Женей?"

    show el grin shirt at center with dspr

    el "Да уж не с Двачевской. Завтра в кино, а сегодня вечером гулять с Женей пойдём. На звёзды посмотрим…"

    hide el with dissolve

    th "Интересно, когда я думаю о Мику, у меня такое же мечтательное лицо?"
    "Со всей этой музыкально-погрузочной чехардой я совсем забыл, что у меня было дело к кибернетикам."
    "Плоская коробочка аккумулятора от телефона уже который день болталась у меня в кармане. Мой верный мобильник держался сколько мог, но всё же отключился, а до появления зарядных устройств к нему было ещё лет двадцать, никак не меньше."
    me "Сергей, слушай… а можешь мне помочь?"

    show el normal shirt at center with dissolve

    el "Могу, конечно. А чем?"
    me "Мне тут батарею надо хитрую зарядить. Есть у вас блок питания на…"
    "Я посмотрел на бумажку."
    me "… четыре вольта?"

    show el serious shirt at center with dspr

    el "Подберём. Саму батарею дашь?"
    me "Держи."
    "Я протянул ему аккумулятор."

    show el surprise shirt at center with dspr

    el "Ого… никогда такого не видел. Откуда он?"
    me "Да так, примочка одна к гитаре."

    show el sad shirt at center with dspr

    el "Семён, ну за дурака-то меня не держи. Я все их примочки знаю. Не хочешь говорить, не надо."
    me "Извини. Не могу."

    show el normal shirt at center with dspr

    el "Ладно, сегодня поставлю на зарядку, у меня там был блок питания почти подходящий. Завтра заберёшь."
    "Он покрутил батарею в руках и равнодушно сунул её в карман. Похоже, предстоящая прогулка с Женей волновала его куда больше."
    el "Пойду душ приму. Надеюсь, Алиса и Улька меня сегодня ловить не будут?"
    me "Вроде не собирались."

    show el smile shirt at center with dspr

    el "До завтра тогда."

    hide el with dissolve

    "Он, кряхтя, встал и пошёл в сторону их с Шуриком дома."

    window hide

    stop music fadeout 3

    stop ambience fadeout 3

    $ bkrr_timeskip()

    scene bg ext_square_night with bkrr_circleout_transition

    $ bkrr_set_time("night")

    play ambience ambience_camp_center_night fadein 3

    play music music_list["trapped_in_dreams"] fadein 5

    $ renpy.pause(1.0, hard=True)

    $ bkrr_set_mode(nvl)

    nvl show dissolve

    "Спать ещё не хотелось, так что я решил просто прогуляться по лагерю. {w}Давненько я не бродил вот так вот, без дела. {w}Чтобы не мелькать среди домиков на глазах у вожатых, я вернулся обратно в спортгородок. {w}Здесь приятно тянуло запахами леса и озера, не было ярких фонарей и можно было полюбоваться звёздами. {w}Вдруг захотелось сбегать к Мику и вытащить её на ночную прогулку. {w}Интересно, Электроник с Женей тоже где-то тут будут гулять? Не хотелось бы им помешать."

    nvl hide dissolve

    $ renpy.pause(1.0, hard=True)

    scene bg ext_playground_night with fade

    play sound_loop bkrr_sfx_list["basketball_loop"] fadein 3

    $ renpy.pause(1.0, hard=True)

    $ bkrr_set_mode()

    window show

    "Моё внимание привлёк стук мяча. Шёл он с баскетбольной площадки. Между щитами взад-вперёд бегала Ульяна."

    window hide

    $ renpy.pause(1.0, hard=True)

    window show

    "Увидев меня, она приняла эффектную позу с мячом, а затем точным движением послала его в противоположное кольцо. "

    stop sound_loop fadeout 3

    extend "Через всё поле."
    th "Впечатляет, чего уж там."
    us "Йес!"

    stop music fadeout 5

    show us smile sport far at center with dissolve

    us "Сеня, что, не спится? {w}Как тебе?"
    me "Вот это бросок! {w}Да так, решил прогуляться. А ты чего в такое время тут?"
    us "Да вот. Мяч вышла побросать, комаров покормить. Только одной не интересно. {w}Не хочешь со мной размяться?"
    me "Давай, конечно."

    hide us with dissolve

    "В баскетбол я не играл со школы. С командными видами спорта у меня вообще плохо ладится."
    th "Но что я, не справлюсь со школьницей, которая мне и до плеча не достаёт? Пусть даже она попадает в кольцо через всю площадку."

    window hide

    $ renpy.pause(1.0, hard=True)

    $ bkrr_timeskip_short()

    scene bg ext_playground_night with bkrr_timeskip_transition()

    window show

    "Не тут-то оно было."
    "Разделали меня под орех, играючи. Десять-один, да и то – один вышел случайно, мяч отскочил от моей головы и попал в корзину."
    "Ульяна присела, вытирая разгорячённое лицо полотенцем."
    th "Какая-то она тихая сегодня. Даже не язвит по поводу моей неумелой игры."
    me "Уля, с тобой всё хорошо?"

    show us normal sport at center with dissolve

    "Она посмотрела на меня, наклонив голову, а потом ответила вопросом на вопрос:"
    us "А почему ты спрашиваешь?"
    me "Ну, обычно от тебя шума побольше… а тут как будто подменили."

    show us sad sport at center with dspr

    us "Может, мне надоело шуметь?"
    me "Может быть, может быть. А тебе надоело?"

    show us normal sport at center with dspr

    us "Нет!"

    window hide

    hide us with dissolve

    $ renpy.pause(1.0, hard=True)

    window show

    "Она залезла с ногами на лавку, обняла колени руками."
    "Я опустился рядом, позаимствовал полотенце и тоже утёрся. {w}Ульяна словно бы и не обратила внимания."
    th "Обычно верещит, если беру её вещи, значит – точно расстроена."

    play music music_list["raindrops"] fadein 5

    show us normal sport at center with dissolve

    us "Сень… можешь мне ответить на вопрос?"
    me "Только не по математике, я в ней слабоват."

    show us smile sport at center with dspr

    us "Ха-ха. Мне мужской совет нужен. {w}Про мальчиков."

    show us sad sport at center with dspr

    us "А кроме тебя спросить некого."
    me "Вот оно что… ну, постараюсь. Может, лучше у Алисы спросишь?"

    show us normal sport at center with dspr

    us "Не! Она не поможет, мне мужское мнение надо. {w}Вот скажи, я странная?"
    me "Да нет, вроде нормальная. Хулиганистая немножко, с шилом пониже спины, но вполне нормальная девочка. {w}А почему ты спрашиваешь?"

    show us dontlike sport at center with dspr

    us "Да что ж вы все про шило говорите. Нету у меня там шила."
    us "Почему? Да так… сказали."
    me "Девчонки часто говорят гадости. Наплюй."

    show us sad sport at center with dspr

    us "Не девчонка. Мальчик."
    me "Понимаю. И как это случилось?"
    us "Я его в кино пригласила, а он отказался."
    me "А ты ему перед этим ничего… такого не делала? Знаешь, кнопку на стул, червячка в тарелку, воды в кровать? Зубной пастой не мазала?"

    show us upset sport at center with dspr

    us "Ничего такого!"
    me "Совсем-совсем ничего?"
    us "Почти ничего. Так, по мелочам… Но я же по дружбе!"
    me "Вот тебе и ответ. {w}Обиделся он. Подростки – они существа ранимые, даже если кажется наоборот."

    show us dontlike sport at center with dspr

    us "Ой-ой, скажешь тоже. {w}Как взрослый говоришь."

    show us upset sport at center with dspr

    us "Ты вон даже Алиску спокойно переносишь, а она тяжело с людьми сходится. Я на вас смотрю, думаю: всё, сейчас он ей в глаз даст. А ты сидишь да хихикаешь. «Ранимый» нашёлся."
    me "Я не про себя. А про Алиску я знаю, что она не со зла, это характер у неё такой. Хотя…"
    "Я улыбнулся."
    me "… немножко витамина «Эр» ей бы не помешало."

    show us surp1 sport at center with dspr

    us "Какого-какого витамина? Нету такого!"
    me "А вот и есть!"

    show us dontlike sport at center with dspr

    us "А вот и нет! У меня по биологии пятёрка!"
    me "Есть! Хочешь, покажу?"

    show us smile sport at center with dspr

    us "А хочу!"
    "Я задрал рубашку, демонстрируя ремень на шортах. {w}Ульяна пошевелила губами, затем заливисто рассмеялась."

    show us laugh sport at center with dspr

    us "Вспомнила! Бабуля моя так говорит."
    me "Вот, видишь! Признавайся, дома часто грозятся и тебе дозу-другую прописать?"

    show us shy sport at center with dspr

    us "Нет, ты что. Дома я воспитанная тихоня."
    us "У меня все военные, кроме мамы. Не забалуешь. {w}Это здесь расслабляюсь. Отличницей-зубрилой быть так скучно, если бы ты знал."
    me "Отличница, тихоня? Ты-то?"

    show us upset sport at center with dspr

    us "Я-то!"

    show us normal sport at center with dspr

    "Ульяна приняла позу примерной ученицы и чопорно посмотрела на меня."
    me "Ни в жизни не поверю. Разыгрываешь?"

    show us smile sport at center with dspr

    us "Ни капельки. Хочешь, завтра фото покажу? У меня с собой есть."
    me "Знаешь, хочу! Даже не представляю тебя в таком имидже."

    show us surp3 sport at center with dspr

    us "В чём-в чём?"
    "Ульяна посмотрела на меня непонимающе."
    me "Прости, оговорился. В таком образе."

    show us normal sport at center with dspr

    us "Я бы сейчас показала, но там Алиска, наверное, спит уже. А спит она голышом."

    show us grin sport at center with dspr

    us "Или, если интересно, пойдём, посмотрим? Мальчики такое любят, кажется?"
    me "Не-а. Не стоит. У меня Мику есть."

    show us smile sport at center with dspr

    us "Какой-то ты весь правильный, аж страшно. А ну, дай-ка я спину твою потрогаю."

    hide us with dissolve

    "Она бесцеремонно ощупала мои лопатки."

    show us grin sport at center with dissolve

    us "Нет, нету. А то я думала, крылышки режутся."
    me "Ну тебя!"
    "Я улыбнулся ей."

    show us smile sport at center with dspr

    us "Да ладно, смешно ведь?"
    me "Да, смешно. Рад, что ты повеселела."
    us "Спасибо!"

    show us shy2 sport at center with dspr

    us "И… Сеня?"
    me "Да?"
    "Ульяна посмотрела в сторону, потом на меня."

    show us shy sport at center with dspr

    us "Вот чисто теоретически. Ты бы в меня мог влюбиться?"
    me "Не знаю. В твоём возрасте, наверное, смог бы."

    show us dontlike sport at center with dspr

    us "Что значит – «в моём возрасте»? Два года – разница небольшая. {w}Я ж просто в школу в пять лет пошла."
    me "Вот оно что… я и думаю, чего ты такая…"
    us "Мелкая? {w}Глупая? {w}Или…"

    show us upset sport at center with dspr

    "Она вздохнула."
    us "Или плоская?"
    me "Тьфу на тебя. Непоседливая, я хотел сказать. Не сочиняй глупостей. И не парься насчёт размеров."
    th "Конечно, детская непосредственность и всё такое… но это вообще нормально такое с малознакомым парнем обсуждать?"

    show us smile sport at center with dspr

    "Ульяна невесело улыбнулась и заглянула себе за пазуху."
    us "Парни любят большие, да?"
    "Я привлёк её к себе, погладил по голове. Она смущённо опустила глаза, но не отодвинулась."
    me "Парни разные любят, не переживай, всё ещё будет. Да и вообще – дело не в размере."

    show us shy sport at center with dspr

    us "Ага! Лена то же самое говорит. Ей легко, у неё вот такие!"
    "Ульяна показала руками, какие именно."
    th "Разговор, конечно, интересный, но нужно сменить тему."
    me "Слушай, а вы, получается, с Леной дружите?"

    show us normal sport at center with dspr

    us "Ну, как тебе сказать… больше через Алису."
    us "Они в одном доме живут и всё такое, а со мной только в школе общались. {w}А потом… Там кое-что случилось, и они сильно поссорились. Ну а мне пришлось выбирать."
    me "Да, я с Леной разговаривал, она тоже сказала, что раздружились. Ты их помирить не пробовала?"

    show us sad sport at center with dspr

    us "Там всё серьёзно. Ты вроде как почти свой, так что намекну – семейные проблемы. {w}Больше ничего не расскажу. {w}Извини. {w}Хочешь, их спроси, но без меня."
    me "Да ладно. Мне своих секретов хватает. Я сам одна большая загадка!"

    stop music fadeout 10

    show us smile sport at center with dspr

    us "Тоже мне, человек-загадка. Енот-кроссворд. Медведь-ребус. Ещё партию?"
    me "Ну, разве что одну. Загоняла ты меня."

    window hide

    $ renpy.pause(1.0, hard=True)

    hide us with dissolve

    $ renpy.pause(1.0, hard=True)

    stop ambience fadeout 3

    scene bg ext_house_of_mt_night with fade3

    play ambience ambience_camp_center_night fadein 3

    window show

    "Предсказуемо продув ещё одну игру, я отвёл нашу неугомонную барабанщицу к её домику, а сам вернулся в свой."
    th "Спать не хотелось, так почему бы не поваляться на свежем воздухе?"

    window hide

    $ renpy.pause(1.0, hard=True)

    window show

    "Уставший, но в отличном настроении, я растянулся в шезлонге. {w}Ещё один день подошёл к концу."
    "Обнаглевшее комарьё попыталось полакомиться моей кровью."
    "Я вспомнил про подарок от вожатой. {w}Парфюм так себе, но она и сказала, что это не для девчонок, а для комаров. Точнее, {b}от{/b} комаров."
    "Пришлось вставать и идти в домик."

    window hide

    $ renpy.pause(1.0, hard=True)

    stop ambience fadeout 3

    play sound sfx_open_door_1

    scene bg int_house_of_mt_night with dissolve

    play ambience ambience_int_cabin_night fadein 3

    window show

    "Ольга гипнотизировала чайник, словно проверяя правдивость мифа, что он не закипает, пока на него смотрят. {w}Увидев меня, понимающе подмигнула."

    show mt grin bkrr_sport at center with dissolve

    mt "Ну что, Семён? Опять гуляешь сам по себе?"

    show mt smile bkrr_sport at center with dspr

    mt "Признавайся, с девочкой гулял?"
    "Я решил не вдаваться в подробности про ночной баскетбол. Всё-таки мелкое, но нарушение режима."
    me "Нет, просто по лагерю прошёлся."
    mt "Ну, и как впечатления?"
    me "Да вот… даже не знаю, как сказать."
    mt "Уж скажи как-нибудь."
    me "Хорошо здесь! Только комары злые!"

    show mt angry bkrr_sport at center with dspr

    mt "Я тебя одеколоном зачем снабдила?"

    window hide

    show mt laugh bkrr_sport at center with dspr

    $ renpy.pause(1.0, hard=True)

    hide mt with dissolve

    play sound sfx_angry_ulyana

    window show

    "Ольга рассмеялась и повернулась спиной к чайнику. Тот немедленно воспользовался моментом и засвистел."

    stop sound fadeout 1.5

    "Я открыл флакон и щедро полил ладонь резко пахнущей жидкостью."
    me "… Убивает комаров наповал. Одним своим запахом!"
    "Мстительно ворчал я, натирая руки и шею."

    window hide

    stop ambience fadeout 0.5

    play sound sfx_open_door_1

    scene bg ext_house_of_mt_night with dissolve

    play ambience ambience_camp_center_night fadein 3

    window show

    "У комаров тоже была своя гордость, и к пахнущему {b}так{/b} человеку они больше не подлетали, так что я спокойно вернулся в шезлонг и залюбовался ночным небом."

    play music music_list["goodbye_home_shores"] fadein 5

    th "Кстати, ведь ровно неделя, как я здесь. Юбилей, в некотором роде."
    "Ольга Дмитриевна в спортивном костюме выбралась на свежий воздух, присела рядом, на ступеньках, поставила на деревянный настил две чашки чая. {w}Только тут я понял, что хотел сделать себе чашку, но поленился."
    th "Как она узнала? Или совпадение?"
    "Ольга ласково улыбнулась, достала из кармана «дорожный» сахар в бумажке с поездом, дала мне пакетик, а второй бросила себе в чашку."
    me "Красота…"
    "Ольга с наслаждением втянула воздух, согласно кивнула."

    show mt smile bkrr_sport at center with dissolve

    mt "Да, мне тоже нравится. В городе скучно, пыль да жара, а здесь… {w}Смотрю на вас, таких молодых, и школьницей себя чувствую."
    me "Знаете, у меня такое же чувство."

    show mt grin bkrr_sport at center with dspr

    mt "Ой, дедуля нашёлся! Сказки-то давно читать перестал?"
    me "Давненько, как на фантастику подсел. Вы фантастику любите?"

    show mt surprise bkrr_sport at center with dspr

    mt "Неожиданный вопрос."

    show mt smile bkrr_sport at center with dspr

    mt "Знаешь, люблю. А ты?"
    me "Я тоже. А про путешествия во времени?"

    show mt normal bkrr_sport at center with dspr

    mt "Ну, не знаю. «Машина времени» как-то не пошла, уныло слишком. {w}Я больше про космос, только не про войну, а такое, знаешь… Исследования, романтика далёких планет."
    mt "Стругацких запоем читала, Кларка, Ефремова люблю. А почему ты спросил?"
    me "Да так."

    show mt smile bkrr_sport at center with dspr

    mt "Для поддержания разговора?"
    me "Вроде того. Странно как-то, вроде бы неделю живём под одной крышей, а толком и не разговаривали."

    show mt grin bkrr_sport at center with dspr

    mt "Ну, разница в возрасте. {w}Тебе со мной не интересно, наверное?"
    me "О, мне всегда говорили, что я умён не по годам."

    show mt smile bkrr_sport at center with dspr

    mt "Правда?"
    me "Да. Что ума, как у пятилетнего."

    window hide

    show mt surprise bkrr_sport at center with dspr

    $ renpy.pause(1.0, hard=True)

    hide mt with dissolve

    window show

    "Шутка немудрёная, но вожатая всё-таки поперхнулась чаем, пришлось похлопать её по спине, отчего её грудь под тонкой тканью костюма упруго качнулась."
    "Кровь бросилась к щекам, я сглотнул и отвёл взгляд."
    "Ольга шутливо шлёпнула меня по руке."

    show mt laugh bkrr_sport at center with dissolve

    mt "Ну тебя! Чуть не облилась."
    me "Чуть не считается."

    show mt smile bkrr_sport at center with dspr

    mt "Уверяю тебя, тебе точно больше пяти лет. Я как раз твою карточку вчера записывала. {w}Чего это ты молодишься?"
    me "Карточку? Интересно-интересно. А из какого я города?"

    show mt surprise bkrr_sport at center with dspr

    mt "Семён, ты меня пугаешь."
    me "Нет, мне правда интересно."

    show mt normal bkrr_sport at center with dspr

    mt "Из нашего, конечно. Может, головой стукнулся сильнее, чем думал?"
    "Чуть не попался. Но для таких вопросов ответ у меня уже готов. Его я сочинил ещё во второй день, когда понял, что вопросов о происхождении не избежать."
    "С вожатой, у которой есть бумажки, не сработает, но всё же."
    me "Да нет, всё проще. У меня предки переезжают часто, работа такая. {w}Так что я не знаю, где сейчас записан: уже здесь или ещё там."

    show mt surprise bkrr_sport at center with dspr

    mt "А кто они у тебя?"
    me "Энергетики. Раньше много ездили, теперь вроде решили тут осесть надолго."

    show mt normal bkrr_sport at center with dspr

    mt "Вот оно что… {w}Так ты, наверное, много повидал?"
    me "Ничего интересного… {w}Мелкие городки, поезда да разные школы."

    show mt smile bkrr_sport at center with dspr

    mt "Интересный ты, пионер Семён."
    me "Да ладно вам."
    th "Чёрт, кажется своим враньём я пробудил её интерес. Наверняка на каждого пионера есть какая-то личная карточка, документы… Надо выкрутиться."
    me "Да, Ольга Дмитриевна… {w}Тут такое дело. Не хочу, чтобы вы думали, что я вас обманываю."

    show mt normal bkrr_sport at center with dspr

    me "У родителей что-то связанное с оборонкой, так что место работы может быть записано любое: учителя, колхозники… {w}да хоть оператор поливальной машины. Сам не знаю."

    show mt smile bkrr_sport at center with dspr

    mt "А, вот оно что… буду иметь в виду."
    "Её большие зелёные глаза смотрели понимающе, но в то же время насмешливо."
    th "Такое ощущение, что она знает гораздо больше, чем показывает мне."
    me "Глупо себя чувствую. Не знать своего адреса. Смешно, да?"

    show mt grin bkrr_sport at center with dspr

    mt "Ничего страшного. Ну, спать пойдём?"

    hide mt with dissolve

    "Двусмысленная фразочка. Но почему-то пошлых мыслей не возникло."
    th "Привык, наверное? Всё-таки который день под одной крышей живём."
    me "Да, пора бы уже. Вы разд… кхм. Переодевайтесь, я схожу, чашки помою."

    window hide

    scene cg d8_fstar with dissolve

    $ renpy.pause(4.5, hard=True)

    window show

    "Я вставал из шезлонга, когда Ольга дёрнула меня за рукав и указала на небо."

    scene cg d8_fstar_main with dissolve

    mt "Смотри! Звезда падает! Загадывай желание, быстро!"

    scene cg d8_fstar_mt with dissolve

    "Светло-жёлтая полоска прочертила ночное небо. В голове теснилась куча желаний, но какое из них важнее, я так и не понял."

    window hide

    scene bg ext_house_of_mt_night
    show mt normal bkrr_sport close at center
    with dissolve

    window show

    mt "Успел?"
    me "Нет. Сильно много желаний, не сообразил, какое загадать."

    show mt smile bkrr_sport close at center with dissolve

    "Вожатая понимающе кивнула."
    mt "Ты никогда не думал, что проблема может быть именно в этом?"
    me "Проблема? Нет у меня проблем. Вроде бы."

    show mt grin bkrr_sport close at center with dspr

    mt "Ну-ну. Может быть и так. Стучись, как придёшь, я переодеваться буду."

    hide mt with dissolve

    "Она подняла глаза к звёздному небу, глубоко вдохнула свежий ночной воздух и зашла в домик."

    window hide

    $ renpy.pause(1.0, hard=True)

    window show

    "Время от времени наша вожатая переставала сыпать комсомольско-пионерскими лозунгами и выдавала туманные фразы, словно знала о чём-то, чего не знаю я."
    "Прямые вопросы вязли в её уклончивых ответах, словно в вате, зато полунамёки сыпались, словно из рога изобилия."

    window hide

    $ renpy.pause(1.0, hard=True)

    scene cg d8_fstar_lone with dissolve

    window show

    "Возвращаясь обратно, я задумался об услышанном."
    th "Карточка какая-то. На меня есть документы?"
    th "Бумажки не рождаются из воздуха. Чтобы возникла запись в личной карточке, должно быть свидетельство о рождении и куча всего остального."
    "Я готов поверить в чертей, демонов, инопланетян, да вообще кого угодно, в любых существ, что перенесли мою бренную тушку в этот странный лагерь с призраками и пионерами. {w}Но представить себе инопланетянина, прилежно царапающего авторучкой бланки свидетельства о рождении… {w}Как-то не верится."
    "Поиск ответов интересовал меня всё меньше и меньше. Всё вокруг напоминало декорацию, тонкую шёлковую занавесь с нарисованным на ней пейзажем."
    th "Да, если задамся целью, то, пожалуй, смогу сорвать её и нарушить этот странный маскарад. Но хочу ли я этого?"

    stop music fadeout 5

    "В первые дни я без колебаний ответил бы «да!». Сейчас… {w}Скорее нет, чем да."
    "Я успел привязаться к этому месту и его странноватым обитателям."

    window hide

    $ persistent.bkrr_check[9] = True

    jump bkrr_day9_start
