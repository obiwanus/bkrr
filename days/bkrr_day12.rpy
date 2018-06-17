
#    Булки, кефир и рок-н-ролл. День 12    #

label bkrr_day12_start:

    $ bkrr_new_chapter(12)

    jump bkrr_day12_common

label bkrr_day12_common:

    scene expression bkrr_awakening_atl("bg int_house_of_mt_day")
    show prologue_dream:
       alpha 0.1
    show unblink
    with None

    $ bkrr_set_time()

    play ambience ambience_int_cabin_day fadein 3

    $ renpy.pause(2.5, hard=True)

    window show

    th "… уже утро? Как же не хочется вставать! Да ещё и ноги замёрзли. Куда делось моё одеяло? И подушка…"
    th "И почему это я одетый сплю? А будильник? Он-то почему молчит?"

    window hide

    $ renpy.pause(1.0, hard=True)

    window show

    th "Неважно, всё равно сейчас вожатая встанет и, как обычно, начнёт меня тормошить…"

    window hide

    $ renpy.pause(1.0, hard=True)

    window show

    th "Что происходит?"
    "Вместо того, чтобы потрясти меня за плечо, Ольга Дмитриевна нежно провела рукой по моей щеке, а затем наклонилась и поцеловала в губы."

    play sound bkrr_sfx_list["whiteout1"]

    scene bg int_old_building_room_day_bkrr_v2 with bkrr_fade(0.25)

    $ bkrr_set_volume("ambience", 0.3)

    play ambience ambience_day_countryside_ambience fadein 3

    "От неожиданности я дёрнулся и проснулся окончательно. Несколько секунд ушло на то, чтобы сообразить, где я и как сюда попал."
    th "Точно! Лес, дождь, странный пионер."
    th "И Мику."

    with vpunch

    me "Мику!"
    "Кажется, я позвал её вслух. Во всяком случае, мне ответили."

    play music music_list["tried_to_bring_it_back"] fadein 5

    mi "Я здесь!"
    "Я резко сел в кровати и потряс головой, разгоняя остатки сна."

    window hide

    $ renpy.pause(1.0, hard=True)

    window show

    "Мику сидела рядом и с улыбкой наблюдала за мной. Сама она уже переоделась в подсохшую форму, а курткой укрыла меня."
    me "Доброе утро!"

    show mi normal pioneer close at center with dissolve

    mi "Доброе!"

    window hide

    # $ bkrr_get_achievement("far")
    # ачивка для третьего эпизода

    $ renpy.pause(1.0, hard=True)

    window show

    "Я огляделся по сторонам. Печка успела погаснуть, но ещё давала немного тепла. В комнате царил бодрящий утренний холодок."
    "Мику поинтересовалась:"
    mi "Как спалось?"
    me "Спал как младенец. Ещё и такая приятная побудка…"

    show mi smile pioneer close at center with dspr

    "Я счастливо вздохнул, а Мику притворно пожала плечами."
    mi "Не понимаю, о чём ты. Завтракать будешь?"
    me "Завтракать? Буду!"
    "Затем я сообразил, где мы находимся."
    me "А чем? У нас что-нибудь осталось?"

    show mi normal pioneer close at center with dspr

    "Мику довольно кивнула."
    mi "Ещё как осталось! Я тут в твоём рюкзаке порылась, ничего?"
    mi "Чай нашла хороший, индийский. Маловато, но нам на двоих хватит, чтобы согреться. Уже заваривается. {w}Плохо, чайника нет, так что я просто в чашках залила, чаинки будут плавать. Ещё у нас есть полпачки печенья, сахар, соль, только солить нечего. И ещё…"

    window hide

    hide mi with dissolve

    $ renpy.pause(1.0, hard=True)

    window show

    "Мику перебирала содержимое вещмешка. В нём обнаружились маленькая печка-спиртовка, алюминиевая тарелка, железная кружка…"
    th "Это что, я вчера весь этот металлолом на себе тащил?"
    th "Ну, кибернетики, ну туристы чёртовы!"
    th "А я-то думал, это рюкзак от воды так потяжелел. Спасибо, хоть сковородку не запихнули."
    "Мику тем временем закончила ревизию и довольно кивнула."
    mi "… так что сейчас мы будем кушать!"
    "Через пару минут Мику приглашающе махнула рукой в сторону печки. Там исходили паром две кружки."

    window hide

    $ renpy.pause(1.0, hard=True)

    scene bg int_old_building_room_day_bkrr_v1 with dissolve

    window show

    me "Наверное, я ещё сплю. Завтрак с любимой девушкой – это слишком хорошо, чтобы быть правдой. Ущипни-ка меня."

    show mi upset pioneer close at center with dissolve

    "Мику с сомнением посмотрела на меня, обдумала просьбу, затем покачала головой."
    mi "Не буду я тебя щипать, ты хороший! Ну давай уже, вставай, бока лижи!"
    me "Лизать бока?"

    show mi serious pioneer close at center with dspr

    mi "Ну, у вас говорят: бока лижи! Если кто-то долго спал."
    me "А, это «лежебока». В смысле – на боку лежит. Соня, в общем."

    show mi smile pioneer close at center with dspr

    mi "Ле-же-бо-ка. Да, точно."
    "Мику сладко потянулась."
    mi "Это тот, кто много спит."
    mi "Знаешь, а я здесь так хорошо выспалась! Странно, да? {w}Я обычно в незнакомых местах плохо засыпаю, долго уснуть не могу, а здесь – р-р-раз! – и уснула. Интересно, почему так?"
    me "Устала, замёрзла, перенервничала. Вот и задремала."
    "Она хихикнула."

    show mi happy pioneer close at center with dspr

    mi "Нет. Это из-за тебя. Мне рядом с тобой было уютно и спокойно, вот. Правда, я из-за тебя просыпалась пару раз. Знаешь, почему?"

    show mi normal pioneer close at center with dspr

    "Мику улыбнулась и замолчала."
    "Я вспомнил, как держал её в своих руках, тёплую и сонную, мечтательно вздохнул. Очень захотелось снова пережить эти ощущения. Мику ждала ответа, так что я попытался отгадать."
    me "Я ворочался во сне?"
    mi "Нет."
    me "Храпел?"

    show mi smile pioneer close at center with dspr

    mi "Тоже нет."
    me "Мику, я готов к самой страшной правде. Неужели я тащил на себя одеяло?"

    show mi laugh pioneer close at center with dspr

    "Мику рассмеялась и покачала головой."

    show mi normal pioneer close at center with dspr

    mi "Не было никакого одеяла. Нет, ты меня звал во сне. Я тебе приснилась, да?"
    me "Не помню…"
    "Я вздохнул. Нужно было сказать «да», Мику было бы приятно."
    th "Может, Алиска была права, сравнивая меня с пнём?"
    me "Я плохо запоминаю сны, прости."

    show mi smile pioneer close at center with dspr

    mi "Всё равно, я рада, что ты обо мне думал."

    show mi normal pioneer close at center with dspr

    "Мику смущённо улыбнулась и замолчала, затем тихо чихнула, мило сморщив нос."
    me "Будь здорова!"
    mi "Спасибо! Наверное, кто-то меня вспоминает."
    me "В смысле?"

    show mi serious pioneer close at center with dspr

    mi "Знаешь, это в Японии примета такая шуточная. Если кого-то обсуждают за спиной, то он в этот момент чихает. Один чих – говорят хорошее…"
    "Мику снова чихнула и принялась загибать пальцы."
    mi "… два – плохое, три – говорящий влюблён, а четыре…"
    me "Что значат четыре?"

    show mi smile pioneer close at center with dspr

    mi "Что ты простудился. Что же ещё?"
    me "Лучше пусть обсуждают. Четыре раза нам не надо. Ну-ка, иди сюда…"

    window hide

    show mi happy pioneer close at center with dspr

    $ renpy.pause(1.0, hard=True)

    hide mi with dissolve

    window show

    "Я обнял Мику и коснулся губами её лба. {w}Температуры, кажется, не было."
    me "Не простыла после такого купания?"

    show mi normal pioneer close at center with dissolve

    mi "Нет, всё хорошо, не волнуйся. {w}А как твоя голова?"
    "Я отшутился:"
    me "Сотрясения вроде нет…"

    show mi upset pioneer close at center with dspr

    "Но Мику восприняла всё всерьёз."
    mi "Точно нет? Ты уверен?"
    "Я отвёл волосы с лица Мику, заглянул ей в глаза и улыбнулся."

    show mi normal pioneer close at center with dspr

    me "Уверен, уверен."

    show mi happy pioneer close:
        center
        ease 1.5 zoom 1.2
    with dspr

    "Мику вздохнула и прижалась ко мне. Мы посидели так ещё немного, потом она шепнула мне на ухо:"

    show mi sad_smile pioneer close:
        center
        zoom 1.2
    with dspr

    mi "В лагере, наверное, уже волнуются. Пойдём назад?"
    mi "Ольга Дмитриевна ругаться будет. Ой, чувствую, попадёт мне сегодня!"
    me "Нет, она обещала тебя не ругать. Мы очень за тебя волновались. {w}И Ольга Дмитриевна, и рыжие, и Лена, и Шурик с Сыроежкой."
    th "Кстати, надо успокоить товарищей."

    window hide

    hide mi with dissolve

    $ renpy.pause(1.0, hard=True)

    stop music fadeout 5

    window show

    "Я с сожалением отпустил плечи Мику, порылся в вещах и достал рацию-мыльницу. Батарейка за ночь «отдохнула», и чудо пионерской техники снова заработало."
    "То ли они дежурили у приёмника, то ли так совпало, но ответ пришёл почти сразу. На этот раз говорил не Шурик, а Электроник."

    play sound_loop bkrr_sfx_list["radio_noise_loop"] fadein 1

    play sound sfx_radio_squelch_1

    el_radio "Наконец-то! Чего не отвечал? Мы тут волновались, ночью такой град шёл!"
    el_radio "Ольга Дмитриевна уже рвётся идти вас забирать. Вы как, в порядке?"
    me "Да, мы ночевали в старом лагере. Решили до утра пересидеть. А что у вас?"

    play sound sfx_radio_squelch_2

    el_radio "Пару стёкол выбило, провода порвало кое-где, а так всё хорошо. Возвращаетесь скоро?"
    me "Сейчас выходим. Минут через сорок будем в лагере. Может, чуть позже, тут такое болото после дождя!"

    play sound sfx_radio_squelch_1

    el_radio "Отлично! Ждём вас!"
    "Он помолчал, затем неприлично официальным тоном закончил:"
    el_radio "Понял вас, Старый Лагерь! Конец связи!"
    "Из динамика раздался смех и чуть смущённое:"

    play sound sfx_radio_squelch_2

    el_radio "Всегда хотел так сказать. Возвращайтесь скорее."

    stop sound

    stop sound_loop

    "Мику с интересом наблюдала за этим. Вчера ей было не до достижений технического прогресса, а сейчас она удивлённо следила, как я разговариваю с пластмассовой головой бегемота."

    show mi surprise pioneer at center with dissolve

    mi "Ого! Настоящая рация? Откуда?"
    me "Кибернетики дали. Электроник волновался, как мы тут."

    show mi normal pioneer at center with dspr

    mi "А как мы тут?"
    "Я улыбнулся ей."
    me "По-моему, лучше не бывает!"

    window hide

    show mi smile pioneer at center with dspr

    $ renpy.pause(1.0, hard=True)

    hide mi with dissolve

    window show

    "Мику принялась укладывать посуду в рюкзак, потом повернулась ко мне:"

    show mi normal pioneer at center with dissolve

    mi "Кстати, глянь, чего я нашла!"

    window hide

    hide mi with dissolve

    $ renpy.pause(1.0, hard=True)

    window show

    "Она протянула мне большую картонную коробку. {w}Картон был старый, выгоревший. Раньше на коробке было что-то нарисовано, но сейчас остались только смутные контуры и рыжие пятна."
    "Я осторожно заглянул внутрь. {w}Из коробки на меня уставился смешной плюшевый медведь, запаянный в толстый полиэтилен."
    me "Какой симпатяга. Где ты его достала?"

    show mi normal pioneer at center with dissolve

    mi "Я ждала, пока дождь закончится, и мне стало скучно. Решила пройти по комнатам, посмотреть, что там есть интересного. {w}Там всякие коробки лежали, я в одну заглянула и нашла его."

    show mi upset pioneer at center with dspr

    mi "А потом кто-то зафыркал, засопел и укусил меня за ногу. Я бросила мишку и наружу убежала, а там дождь! Кстати, кто же всё-таки сопел?"
    "Мику опасливо осмотрелась вокруг, словно ожидая, что сейчас из стен полезут призраки пионеров. Я поспешил её успокоить."
    me "Не волнуйся, это был ёжик, их здесь много. Они ночью к нам приходили. Погреться, наверное. {w}Или посмотреть, кто тут в их доме безобразничает."

    show mi dontlike pioneer at center with dspr

    mi "Просто ежи?"
    "Мику недоверчиво посмотрела на меня."
    me "Не просто ежи! Они были большие и очень грозные. Веришь, я когда сопение услышал, чуть не кинулся на них с ножом."

    window hide

    show mi laugh pioneer at center with dspr

    $ renpy.pause(1.0, hard=True)

    hide mi with dissolve

    window show

    "Про странного гостя в химзащите я решил промолчать. Может, он мне просто приснился."
    "Мику довольно устроила медведя в рюкзаке, потом повернулась ко мне."

    show mi normal pioneer at center with dissolve

    mi "Мой герой! Гроза диких животных и спаситель пугливых пионерок. Мишку заберём, хорошо?"
    me "Конечно. Будешь с ним спать?"

    show mi shy pioneer at center with dspr

    mi "Нет, мне уже не по возрасту. Я его Ульяне отдам. Она… {w}Ты не будешь смеяться?"
    me "Буду, конечно. Но не при ней."

    show mi smile pioneer at center with dspr

    mi "Она привыкла спать с игрушкой. Знаешь, у неё дома есть игрушечный медведь, только она его сюда не взяла, чтобы не смеялись. {w}Алиса жаловалась, что Ульяна без него спит плохо. Может быть, мишка ей поможет."

    window hide

    stop ambience fadeout 2

    $ bkrr_timeskip_short()

    scene bg ext_old_building_day_bkrr with bkrr_timeskip_transition()

    $ bkrr_set_volume("ambience", 1.0)

    play ambience ambience_day_countryside_ambience fadein 3

    window show

    "Ещё несколько минут на сборы, и мы вышли во двор. Ночью старый лагерь казался мне зловещим и пугающим, а сейчас вызывал скорее сочувствие. {w}Покинутые здания печально смотрели на нас окнами без стёкол. Почему-то картина нагоняла грусть."

    window hide

    stop ambience fadeout 3

    scene bg ext_path_day with fade3

    play ambience ambience_forest_day fadein 3

    play music bkrr_music_list["eo"] fadein 3

    window show

    "Земля под ногами была густо усеяна оборванными листьями и обломками веток. Прямо поперёк дорожки лежала высокая сосна, её корни смотрели в небо."
    th "Похоже, мне крепко повезло, что на меня упала всего одна небольшая ветка."
    "Мику всё время держала меня за руку, словно боялась, что я куда-нибудь исчезну, стоит её отпустить."

    show mi sad_smile pioneer close at center with dissolve

    mi "Сеня?"
    "Она говорила тихо, неуверенно. Очень не похоже на привычную мне Мику."
    me "Да, милая?"

    show mi upset pioneer close at center with dspr

    mi "Я вчера наговорила… много всего. Чтобы ты уходил, про Виолу… И ударила. Извини меня, ладно?"
    me "Всё в порядке. Знаешь, как приятно, что ты меня ревнуешь. Значит, я тебе правда нравлюсь."

    show mi dontlike pioneer close at center with dspr

    mi "Ничего я не…"
    "Мику помолчала, потом махнула рукой."

    show mi sad_smile pioneer close at center with dspr

    mi "Хорошо, хорошо. Ревную. Ты правда не сердишься? Столько начудила, вас заставила волноваться. Ты из-за меня под дождём бегал…"

    show mi sad pioneer close at center with dspr

    mi "Я так глупо себя чувствую!"
    "Я обнял её за плечи, повернул к себе и покачал головой."
    me "Ну конечно, не сержусь. И вообще, когда ещё мне выпал бы случай спасти красавицу из беды? {w}Прямо как в кино."

    show mi smile pioneer close at center with dspr

    me "Кстати! Мику, знаешь, о чём я подумал?"

    show mi normal pioneer close at center with dspr

    mi "О чём же?"
    me "После всего, что случилось, мы можем считаться официальной парочкой."

    show mi surprise pioneer close at center with dspr

    me "Теперь мне полагается дарить тебе цветы, водить в кино и угощать мороженым. А ещё целовать не реже трёх раз в день. {w}И на сегодня норма ещё не выполнена!"

    hide mi with dissolve

    "Нам пришлось остановиться. {w}Мику с удовольствием ответила на мой поцелуй, а потом задумчиво поинтересовалась:"

    show mi serious pioneer close at center with dissolve

    mi "А мне что полагается делать?"
    me "А ты не знаешь?"

    show mi smile pioneer close at center with dspr

    "Мику покачала головой и улыбнулась."
    mi "Не знаю! У меня это впервые, знаешь ли."
    me "Да ну. Такая красивая девушка, и ни разу ни с кем не встречалась?"

    show mi upset pioneer close at center with dspr

    mi "Нет… Я же тебе говорила, что начинаю молоть всякую чушь, когда нервничаю. {w}А с мальчиками я всегда нервничаю. Да ты сам видел."
    mi "Все думают, что я дура, и как-то ни с кем никогда не складывалось."
    "Она вздохнула и развела руками."
    me "Ты меня разыгрываешь."

    show mi normal pioneer close at center with dspr

    mi "Нет, был один мальчик, которому я нравилась. Это давно было, когда я только переехала. Он дёргал меня за хвостики и бил дневником по голове. А ещё, попозже, по пути домой носил мой портфель. Его ещё дразнили «Двапортфеля». Это считается?"
    me "Даже не знаю. Вот если бы учебником по геометрии, тогда бы я приревновал, а дневником – это так, лёгкий флирт."

    show mi laugh pioneer close at center with dspr

    mi "Ну тебя! Ты вообще бываешь серьёзным?"
    me "Случается. Вот когда говорю, что ты мне очень нравишься – я серьёзен до невозможности. Имей это в виду."

    show mi smile pioneer close at center with dspr

    mi "Спасибо! И я."

    show mi shy pioneer close at center with dspr

    mi "Ты… тоже… мне…"
    "Она мило смутилась и потупилась."

    window hide

    stop ambience fadeout 3

    scene bg ext_path3_day_bkrr with fade3

    play ambience ambience_forest_day fadein 3

    window show

    "По дороге в лагерь мы строили планы, обсуждали будущий концерт и как пойдём на танцы…"
    "Иногда беспокоили мысли о том, что я могу внезапно исчезнуть и вернуться домой, но я гнал их прочь."
    "Сейчас я даже не был полностью уверен в том, кто же я такой."
    th "Может, на самом деле я советский пионер Семён, которому приснился странный сон о будущем?"
    th "Нет, я точно знаю, кто я такой, но воспоминания о моём времени постепенно теряли чёткость, словно я стремился забыть о нём."

    window hide

    scene bg ext_polyana_day with fade3

    window show

    "Вокруг было очень красиво. Если не смотреть на обломки веток и ковёр из оборванных листьев, то трудно было бы поверить, что несколько часов назад бушевала буря."
    "Солнце, пробивающееся сквозь ветки деревьев, уже подсушивало грязь, капли воды на листьях переливались сотнями маленьких искорок."
    "Может, для той же Славяны этот пейзаж был привычным и скучным, но мне утренний лес очень нравился."

    window hide

    $ renpy.pause(1.0, hard=True)

    stop music fadeout 10

    window show

    "Краем глаза я заметил какие-то ярко-красные искорки чуть в стороне от тропинки."
    me "Мику, подожди секундочку!"
    "Я подошёл поближе. {w}Покрытая росой трава тут же промочила мне ноги. {w}Искорки оказались россыпью спелой ярко-красной земляники."
    "Мику осталась стоять на тропинке и оттуда поинтересовалась:"

    show mi smile pioneer at cleft with dissolve

    mi "А что там?"
    me "Сюрприз! Закрой глаза, открой рот!"
    "Она погрозила мне пальцем."

    show mi dontlike pioneer at cleft with dspr

    mi "Ага! Хитрый! Плавали, знаем."
    mi "Мне Ульянка так же сказала сделать, а потом одуванчик в рот положила!"
    th "Вот негодница."

    window hide

    show mi dontlike pioneer close at cleft with dspr

    $ renpy.pause(1.0, hard=True)

    show mi happy pioneer close at cleft with dspr

    $ renpy.pause(1.0, hard=True)

    hide mi with dissolve

    window show

    "Тем не менее моя спутница доверчиво зажмурилась и приоткрыла рот. Я выбрал самую большую и сочную земляничину, оторвал хвостик и осторожно положил на язык Мику."
    me "Пробуй. Вкусно?"
    "Мику задумчиво пожевала ягоду, потом улыбнулась и счастливо закивала."

    show mi smile pioneer close at center with dissolve

    mi "М-м-м… Очень! Спелая-спелая! А ещё есть? Давай наберём, девчонок угостим!"
    me "Давай. Вот только во что? Что там у нас с посудой?"

    window hide

    hide mi with dissolve

    $ renpy.pause(1.0, hard=True)

    window show

    "Разумеется, корзины не нашлось. {w}Даже запасливые кибернетики, набивая рюкзак хламом, не подумали, что в лесу мне потребуется корзина. Из термоса потом не достанем, тарелка мелкая…"
    "Я подумал, а не отрезать ли капюшон у плаща, но потом представил себе, как вожатая будет ругаться за порчу имущества."
    "В итоге мы сняли полиэтиленовую упаковку с игрушечного медведя, протёрли дочиста полотенцем и насобирали в неё приличную кучку земляники."

    show mi normal pioneer close at center with dissolve

    mi "Сеня!"
    me "Да?"

    show mi smile pioneer close at center with dspr

    "Мику показала мне большую ягоду."
    mi "Я тоже так хочу. Закрой глаза, открой рот!"

    window hide

    show blink

    $ renpy.pause(2.5, hard=True)

    window show

    "Я опустил на землю пакет с ягодами, завёл руки за спину и закрыл глаза. {w}Сладкая мякоть коснулась моих губ, а затем на мои плечи легли руки Мику."
    th "Обе руки… А земляника?"
    "Земляничку она держала, зажав губами."
    me "И правда… очень… спелая. И сладкая."

    window hide

    hide blink
    show mi laugh pioneer close at center
    show unblink
    with None

    $ renpy.pause(2.5, hard=True)

    window show

    "Мику рассмеялась, довольная своей выдумкой."

    show mi smile pioneer close at center with dspr

    mi "Возвращаемся?"
    "Я поправил рюкзак и кивнул."
    me "Да, пойдём. В лагере, наверное, волнуются."

    hide mi with dissolve

    "Мику оглядывалась по сторонам и удивлялась, какая вчера была буря. {w}Вся дорога была усеяна обломками веток, так что оставалось гадать, как я вообще вчера дошёл."

    window hide

    stop ambience fadeout 3

    scene bg ext_boathouse_day with fade3

    play ambience ambience_boat_station_day fadein 3

    play music music_list["reminiscences"] fadein 5

    window show

    "Ворота лагеря были открыты. Ольга Дмитриевна уже поджидала нас у входа."
    "Вожатая взволнованно подбежала к нам, обняла обоих, а затем, отступив на шаг, принялась строго, но сбивчиво отчитывать."

    show mt angry panama pioneer close at center with dissolve

    mt "Мику, Семён, ну что же вы делаете, а? Взяли и пропали на всю ночь."

    show mt sad panama pioneer close at center with dspr

    mt "Я вся извелась, думала в милицию звонить, сама в лес бежать хотела. Мику, не ходи больше одна так далеко, ладно?"
    "Мику виновато поклонилась ей."

    window hide

    show mt sad panama pioneer close at cleft with ease

    show mi sad pioneer close at cright with easeinright

    window show

    mi "Простите меня, пожалуйста, я больше не буду. Я думала, чуть-чуть пройдусь и вернусь, а потом заблудилась, и ещё дождь пошёл… Извините, что доставила столько неприятностей."

    show mt smile panama pioneer close at cleft with dspr

    "Вожатая улыбнулась."
    mt "Забыли. Главное, что все живы-здоровы."

    show mt normal panama pioneer close at center
    show mi sad pioneer close at offscreenright
    with ease

    hide mi with None

    mt "Семён, а что с лицом? Где ты так лоб разбил?"
    me "Да так, о дерево стукнулся. Ничего страшного."

    show mt smile panama pioneer close at center with dspr

    "Ольга Дмитриевна понимающе кивнула."
    mt "Ясно. Идите к Виоле, пусть она вас осмотрит, а потом – в столовую! Мы оставили для вас завтрак."
    mt "В бане есть горячая вода, сходите и помойтесь, а то не пионеры, а партизаны какие-то. {w}Или поросята."
    "При мысли о горячей воде и мыле я блаженно заулыбался."
    me "Банька? Это я с удовольствием!"
    "Тут вожатая посмотрела на меня и укоризненно покачала головой."

    show mt laugh panama pioneer close at center with dspr

    mt "Семён, не улыбайся так, а то лицо от счастья сведёт!"

    show mt grin panama pioneer close:
        center
        ease 1.0 zoom 1.2
    with dspr

    "Она наклонилась к самому моему уху и добавила шёпотом:"
    mt "Я имела в виду – по очереди!"

    show mt smile panama pioneer close:
        center
        zoom 1.2
        ease 1.0 zoom 1.0
    with dspr

    "Потом добавила уже нормальным голосом:"
    mt "Я Славе скажу, она вам двери откроет."
    "Мику тоже довольно кивнула."
    mi "Ой, искупаться – это здорово!"
    "Затем вожатая ухватила меня за руку."

    show mt normal panama pioneer close at center with dspr

    mt "Семён?"
    me "Да?"
    mt "На два слова! Мику, подожди там, пожалуйста."

    window hide

    stop music fadeout 5

    hide mt
    hide mi
    with dissolve

    $ renpy.pause(1.0, hard=True)

    window show

    "Ольга отвела меня в сторонку. Мику проводила нас взглядом, потом отошла чуть подальше и принялась не спеша лакомиться земляникой."
    "После короткой паузы вожатая вздохнула и поинтересовалась:"

    show mt normal panama pioneer close at center with dissolve

    mt "Семён, извини, но я должна спросить. Вы, ну… не делали ничего такого?"
    "Я старательно изобразил непонимание."
    me "Мы сейчас о чём?"

    show mt smile panama pioneer close at center with dspr

    "Ольга едва заметно улыбнулась и уточнила:"
    mt "Два подростка вместе наедине. Тем более она тебе нравится. {w}Всякое бывает. И последствия потом иногда тоже бывают. {w}Понимаешь?"
    me "А, я понял, о чём вы. Нет-нет, ничего такого, о чём я постеснялся бы рассказать вам или её родителям. {w}Особенно маме, которая знает джиу-джитсу."
    me "Строго между нами – на радостях мы поцеловались. Кажется, от этого детей не бывает! Я почти уверен."

    window hide

    show mt angry panama pioneer close at center with dspr

    $ renpy.pause(1.0, hard=True)

    show mt laugh panama pioneer close at center with dspr

    window show

    "Ольга Дмитриевна напустила было строгий вид, но потом рассмеялась."

    show mt smile panama pioneer close at center with dspr

    mt "Пошути мне ещё тут! Всё, больше вопросов не имею."
    mt "Я же знаю, что вы чуть больше, чем просто друзья, потому и переживаю."
    me "По мне не скажешь, но я знаю, что такое ответственность. Нет, ничего такого не было."
    "Я помялся, потом не удержался и спросил:"
    me "А что, сильно заметно? Ну, про нас с Мику?"
    mt "Заметно?"

    show mt laugh panama pioneer close at center with dspr

    mt "Нет, ну что ты. Вы так здорово всё скрываете. Почти как Штирлиц. {w}Подумаешь, проводите всё свободное время вместе, обнимаетесь, в кино ходите, ты признание перед Фантомасом репетируешь, да ещё в грозу бросился её искать."
    mt "Нет-нет, никто ни о чём не догадывается."

    show mt smile panama pioneer close at center with dspr

    mt "Всё, будем считать профилактическую беседу о пестиках и тычинках законченной, бегите завтракать."
    mt "На сегодня освобождаетесь от всех мероприятий. {w}Для вас у меня особо важное задание: поесть и отдохнуть. {w}И не заболеть."
    me "Спасибо! Простите, что заставили волноваться."
    mt "Идите уже, пионеры. Работа у меня такая – волноваться за всех вас."

    show mt grin panama pioneer close at center with dspr

    mt "Во всём есть хорошая сторона. Я, наконец, нормально выспалась! Первый раз за неделю. {w}Никто не бегал среди ночи туда-сюда, спать не мешал. А то я уже подумывала, куда бы тебя отселить."
    me "Простите, не знал, что от меня столько неудобств."

    show mt smile panama pioneer close at center with dspr

    mt "Не делай такое виноватое лицо, я шучу. Всё, иди, а то Мику тебя заждалась."

    hide mt with dissolve

    "Я сбегал к Мику, набрал горсть земляники и протянул Ольге Дмитриевне."

    show mt smile panama pioneer close at center with dissolve

    me "Вот, угощайтесь."
    mt "Спасибо!"
    "Ольга растроганно улыбнулась и взяла земляничину."
    mt "Вкусная! Кстати, до завтрака сходите и успокойте Алису. Она очень переживала за вас. Только я этого не говорила!"

    window hide

    stop ambience fadeout 3

    scene bg ext_music_club_verandah_day_v6 with fade3

    play ambience ambience_camp_center_day fadein 3

    window show

    "Заплаканная Алиса сидела на ступеньках музыкального кружка. Рядом с ней хлопотала Ульяна, тоже непривычно тихая и серьёзная. Мелкая гладила Алису по голове и, кажется, успокаивала."
    th "Алиса плачет? Да ну, быть не может."

    window hide

    show dv surprise pioneer far at center with easeinbottom

    $ renpy.pause(1,0, hard=True)

    show dv sad pioneer far at center with dspr

    window show

    "Увидев нас, Алиса подскочила и, прихрамывая, бросилась навстречу."

    show dv sad pioneer at center with dspr

    "Не дойдя пары шагов, она остановилась и потупилась."
    th "Всё-таки чувствует себя виноватой из-за той истории с рубашками?"
    dv "Мику, Семён… {w}Вы как?"

    hide dv with dissolve

    "Не сговариваясь, мы обняли Алису с двух сторон."
    mi "Всё замечательно, не волнуйся! И не вздумай больше плакать, а то!.."

    play music music_list["i_want_to_play"] fadein 3

    "Что именно будет, если Алиса заплачет, я не узнал."
    "Ульянка подбежала следом и повисла на нас, не дав Мику договорить. Прямо в ухо раздалось звонкое:"

    show us laugh sport close at center with dissolve

    with vpunch

    us "Ура-ура-ура! Вернулись! Что ты мне принёс?"
    me "Тише, Ульянка, с ног свалишь! Мику привёл, тебе что, мало?"

    show us angry sport close at center with dspr

    us "Мику ты себе привёл! А мне ты что обещал? Ты мне обещал ёжика! Забыл уже?"
    me "Извини, из головы вылетело."

    show us laugh sport close at center with dspr

    us "Не знаю, что там у тебя вылетело, но прилетело точно! Вот это шишак!"

    window hide

    $ renpy.pause(1.0, hard=True)

    show us dontlike sport close at center with dspr

    window show

    "Ульяна сморщила нос, глядя на нас с Мику."
    us "Сёма, Мику, может, хватит уже обниматься! Идём в столовую, я хоть твою булочку съем!"
    me "Это с какого перепугу?"
    us "Ты мне обещал ёжика поймать, а пришёл с пустыми руками и какой-то девицей!"

    window hide

    show us dontlike sport close at cleft with ease

    show mi smile pioneer close at cright with easeinright

    window show

    "Мику довольно улыбнулась и потянула меня за лямку рюкзака."
    mi "Не с пустыми. Сеня, дай, пожалуйста, я трофей достану!"

    window hide

    hide us
    hide mi
    with dissolve

    $ renpy.pause(1.0, hard=True)

    window show

    "С трудом размотав разбухшую от воды шнуровку, Мику извлекла на свет медведя и басом произнесла:"

    show dv smile pioneer close at left
    show mi grin pioneer close at center
    show us surp2 sport close at right
    with dissolve

    mi "Привет! Где тут девочка, которая любит плюшевых медведей?"

    show us normal sport close at right with dspr

    "Ульяна широко распахнула глаза и машинально потянулась к игрушке, но тут же одёрнула себя и изобразила равнодушие."
    us "А это чего?"

    show dv laugh pioneer close at left
    show mi normal pioneer close at center
    with dspr

    mi "А это охотничий трофей! Ежа не нашли, медведь сойдёт?"

    show mi dontlike pioneer close at center with dspr

    mi "Ну, бери! А то Алисе отдам!"

    show dv grin pioneer close at left
    show mi normal pioneer close at center
    with dspr

    dv "Классный! Давай, я заберу."

    show us upset sport close at right with dspr

    us "Перетопчется! Дай сюда!"

    show dv laugh pioneer close at left
    show mi surprise pioneer close at center
    show us laugh sport close at right
    with dspr

    "Ульяна радостно схватила подарок."
    th "Какой она всё-таки ещё ребёнок."

    show dv normal pioneer close at left
    show mi normal pioneer close at center
    with dspr

    "Словно услышав мои мысли, Ульяна ненатурально возмутилась:"

    show us normal sport close at right with dspr

    us "Эй! Микуля, я ведь не маленькая!"
    mi "Ну что ты. Игрушки дарят и взрослым девушкам."

    show us smile sport close at right with dspr

    hide mi with dissolve

    us "Тогда ладно… Спасибо тебе большущее! Алиса, учти, спать с ним буду я!"

    show dv grin pioneer close at left with dspr

    dv "Хорошо, хорошо! Я и не претендую. А подержать-то дашь?"
    us "Раз в день! По пять минут."

    show dv smile pioneer close at left with dspr

    dv "Жадина…"

    show us laugh2 sport close at right with dspr

    us "Я не жадная! Я домовитая!"

    window hide

    stop music fadeout 5

    hide dv
    hide us
    with dissolve

    $ renpy.pause(1.0, hard=True)

    window show

    "Мику наблюдала за их спором с улыбкой. {w}Тут она что-то вспомнила, подмигнула мне и потянула Алису за рукав."

    show dv normal pioneer close at cleft
    show mi normal pioneer close at cright
    with dissolve

    mi "Алиса, а как твоя нога, кстати?"
    "Алиса отмахнулась."
    dv "Танцевать не буду, а так ничего."
    me "Так ты же и не танцуешь никогда?"

    show dv smile pioneer close at cleft with dspr

    dv "Не танцую. Но теперь уважительная причина будет!"

    show mi happy pioneer close at cright with dspr

    mi "Значит, ножка у тебя уже не болит?"
    dv "Нет…"
    "Рыжая довольно улыбалась, глядя на нас."

    show mi smile pioneer close at cright with dspr

    mi "Раз выздоровела, то пирожное давай! Ты мне всё ещё должна!"

    show dv guilty pioneer close at cleft with dspr

    dv "Мику, опять двадцать пять. Где же я тебе его возьму?"

    show mi normal pioneer close at cright with dspr

    mi "Ничего не знаю. Пионер сказал – пионер сделал!"

    show dv normal pioneer close at cleft with dspr

    dv "А вот возьму и не отдам! И что ты сделаешь?"

    show mi grin pioneer close at cright with dspr

    "Мику зловеще произнесла:"
    mi "О-о-о… Месть моя будет страшна!"
    mi "Я тебе струну на гитаре расстрою! {w}И не скажу, какую!"

    show dv shocked pioneer close at cleft with dspr

    "Алиса наигранно ужаснулась."
    dv "Семён, растяпа, ты кого из леса привёл? Наша Мику до таких угроз никогда не доходила!"

    show mi smile pioneer close at cright
    show dv sad pioneer close at cleft
    with dspr

    dv "Она была белая и пушистая! Веди назад и ищи другую, правильную!"
    "Я покачал головой."
    me "И не подумаю! Мне другая не нужна, только эта!"

    window hide

    show mi happy pioneer close at cright with dspr

    $ renpy.pause(1.0, hard=True)

    hide mi with dissolve

    window show

    "Мику не покраснела и даже не отвела глаз. Вместо этого она взяла меня под руку и положила голову мне на плечо."
    mi "Вот!"

    show dv surprise pioneer close at cleft with dspr

    "Алиса и Ульяна удивлённо уставились на нас. Разумеется, это не стало для них новостью, но вот так, вслух прозвучало, кажется, впервые."

    play music music_list["timid_girl"] fadein 5

    show us laugh2 sport close at cright behind dv with easeinbottom

    "Ульяна очнулась первой. Радостно подпрыгнула, подбежала поближе."
    us "Опаньки! А когда свадьба? Меня подружкой невесты возьмёте?"

    show dv angry pioneer close at center with ease

    dv "Ульянка, ты куда лезешь? По старшинству!"
    "Алиса попыталась оттеснить её в сторону."

    show dv angry pioneer close at cleft with ease

    us "Ничего не знаю! Я первая забила! А ты можешь в сторонке постоять."

    show us grin sport close at cright with dspr

    us "Может, доверим голубя подержать! Или коробочку с кольцами…"

    show dv rage pioneer close at cleft with dspr

    dv "Ах ты, мелкая…"

    show us laugh sport close at center with ease

    us "Зато ты у нас сильно большая!"

    show us laugh sport close at offscreenright with ease

    hide dv
    hide us
    with dissolve

    "Ульяна похлопала Алису по животу и спряталась за меня."
    "Я вопросительно заглянул в глаза Мику, она подмигнула, а затем охладила разбушевавшихся подруг."

    show mi dontlike pioneer close at cright with dissolve

    mi "Эй, эй, какая свадьба, я ещё школу не закончила! {w}А будете ругаться – никого не позову!"

    hide mi with dissolve

    "Глядя на их шутливую перепалку, я впервые за многие годы чувствовал, что это такое – иметь близких людей."
    "Приятное ощущение, когда можно с кем-то побыть самим собой, говорить не то, что положено, а то, что хочется."
    th "Мы сильно сблизились за прошедшее время. Смешно теперь вспоминать, как Ульяна облила меня борщом, а Алиса стукнула гитарой."
    "При мысли о борще желудок предупредительно зарычал и постучал в стенки своей темницы."
    "Я вздохнул."
    me "Девочки, не знаю, кто как, а я проголодался. Может, продолжим планировать бракосочетание в столовой? Есть хочу со страшной силой."
    "Ульяна шутливо потыкала меня пальцем в живот."

    show us smile sport at center with dissolve

    us "Смотрите, пожалуйста. Мы тут о чувствах, а ему лишь бы жрать!"
    me "Ничего подобного! Просто пока тут кто-то сидел в тепле и уюте, мы мокли, прятались от бури в доме с привидениями и с трудом поддерживали огонь, чтобы не замёрзнуть!"
    "В ответ Ульяна пренебрежительно взмахнула рукой."

    show us dontlike sport at center with dspr

    us "Ой, да ладно. «Буря», тоже мне. Дождик пошёл, а он уже героя-полярника из себя строит."

    show dv grin pioneer at cleft behind us with dissolve

    "Алиса ласково взъерошила волосы Ульяне."
    dv "А скажи-ка мне, рыжая, кто там от каждого удара грома подскакивал, дрожал, а потом ко мне под одеяло просился, потому что одной спать страшно?"

    show us calml sport at center with dspr

    us "Не было такого!"

    show dv laugh pioneer at cleft with dspr

    dv "А вот и было!"

    stop music fadeout 5

    show us normal sport at center with dspr

    "Ульяна решила сменить тему."
    us "Хватит болтать, идём! А то эти голубки с голоду помрут."

    window hide

    stop ambience fadeout 3

    scene bg ext_dining_hall_away_day with fade3

    play ambience ambience_camp_center_day fadein 3

    play music music_list["everyday_theme"] fadein 5

    window show

    "Проводив нас до столовой, Алиса с Ульяной отправились по каким-то своим пионерским делам, обещав скоро вернуться. Пакет с земляникой они забрали для лучшей сохранности."
    th "Ну, ничего. Мы успели поесть, хотя жаль, что остальное слопают без нас."

    window hide

    stop ambience fadeout 2

    $ renpy.pause(0.5, hard=True)

    scene bg ext_dining_hall_near_day with dissolve

    $ renpy.pause(0.5, hard=True)

    scene bg int_dining_hall_day with dissolve

    play ambience ambience_dining_hall_empty fadein 3

    show nt normal cook at cright with dissolve

    window show

    nt "Доброе утро!"

    show mi normal pioneer at cleft with dissolve

    mi "Здравствуйте, тётя Наташа. Если можно, нам бы покушать. Очень хочется! Погреете что-нибудь?"

    window hide

    show nt smile cook at cright with dspr

    $ renpy.pause(1.0, hard=True)

    hide mi
    hide nt
    with dissolve

    window show

    "Наталья понимающе улыбнулась и поставила нам две полные тарелки горячего супа с фрикадельками."

    show nt smile cook at cright with dissolve

    nt "Ольга мне рассказала про ваши приключения."
    nt "Завтрак уже остыл, разогретое будет невкусно. Ешьте суп, он свеженький, на обед сварила. Заодно снимете пробу."

    show nt normal cook at cright with dspr

    nt "Вкусно?"

    show chair_l behind mi
    show mi smile pioneer at bkrr_sit_left
    with dissolve

    me "Не то слово!"
    mi "Очень вкусно!"
    nt "Добавку будете?"

    show mi happy pioneer at bkrr_sit_left with dspr

    mi "Обязательно!"

    window hide

    $ bkrr_timeskip_short()

    scene bg int_dining_hall_day with bkrr_timeskip_transition()

    window show

    "Мы бодро умяли завтрак, а потом и добавку. {w}Суп был действительно очень вкусным, ещё и эти приключения пробудили зверский аппетит."
    "Я еле удержался, чтобы не взять третью тарелку. И без того чувствовал себя удавом, проглотившим целого поросёнка."
    "Оставалось посетить медсестру, принять душ, и можно отдыхать."

    window hide

    stop ambience fadeout 5

    stop music fadeout 5

    scene bg ext_aidpost_day at bkrr_moving_forward_far(5.0, 1.5) with fade3

    $ renpy.pause(1.5)

    scene bg int_aidpost_day
    show cs smile glasses far at center
    with dissolve

    play ambience ambience_medstation_inside_day fadein 3

    window show

    cs "Здравствуйте, пионеры. Чем вы меня порадуете сегодня? Переломы, растяжения?"
    "Голос был наигранно сердитый, но Виола приветливо улыбалась."

    window hide

    hide cs with dissolve

    $ renpy.pause(1.0, hard=True)

    window show

    "Мы с Мику предъявили Виоле свои страшные раны: несколько царапин и шишку. {w}Конечно, мы здорово намёрзлись ночью, но, кажется, всё прошло без последствий."

    show cs normal stethoscope close at cright with dissolve

    cs "Теперь давай посмотрим твою спину. Снимай рубашку!"

    window hide

    play sound sfx_blanket_off_stand

    $ renpy.pause(1.0, hard=True)

    show mi shocked pioneer far at cleft with easeinleft

    window show

    cs "Ох, вот это да!"
    mi "Ничего себе!"

    show mi sad pioneer far at cleft with dspr

    "Я горделиво выпрямился и ещё больше расправил плечи, но их впечатлил не мой голый торс."
    "Виола и Мику смотрели на мою спину. Быстрый взгляд в зеркало прояснил причину: через всю спину шёл внушительный синяк, а там, где сук ткнулся под лопатку, виднелась глубокая ссадина."
    "Медсестра покачала головой."
    cs "Что это у нас, пионер?"
    me "Да так, веточка упала."
    "Виола покачала головой, обрабатывая рану."
    cs "Веточка, как же. {w}Брёвнышко, не меньше."

    play sound bkrr_sfx_list["coldwater_shock1"]

    show red:
        alpha 0.3
        linear 0.25 alpha 0.0
    with hpunch

    "Она коснулась ссадины салфеткой, спину защипало."

    show mi sad_smile pioneer far at cleft with dspr

    cs "Не дёргайся, пионер."
    "Медсестра тем временем продолжала возиться с моей спиной."
    cs "Я сейчас мазь положу. Голова не кружится?"
    me "Н-нет вроде."
    cs "Если заболит или температура поднимется, сразу ко мне! Понял?"
    me "Понятно."
    "Затем Виола быстро смазала мою спину какой-то мазью. Кожу приятно захолодило, и боль тут же ушла."

    show cs smile stethoscope close at cright with dspr

    cs "Вот и всё, пионеры. Идите отдыхать."

    window hide

    show mi normal pioneer far at cleft with dspr

    stop ambience fadeout 2

    $ renpy.pause(1.0, hard=True)

    scene bg ext_aidpost_day with fade

    play ambience ambience_camp_center_day fadein 3

    window show

    "Медсестра быстро осмотрела Мику и отпустила нас. Мы вышли из медпункта."

    show mi normal pioneer at center with dissolve

    mi "Столько всего случилось! Что-то я устала."
    me "Знаешь, я тоже. Пойдём отдыхать?"

    show mi smile pioneer at center with dspr

    mi "Да-а-а! Сейчас я как лягу и как засну! Только искупаемся сначала."
    "Я с затаённой надеждой поинтересовался:"
    me "Вожатая сказала, что в бане есть горячая вода. Потереть тебе спинку?"

    show mi shy pioneer at center with dspr

    mi "Ну…"
    "Мику зарделась и покачала головой."

    show mi upset pioneer at center with dspr

    mi "Я не против, но, наверное, нам ещё рано так далеко заходить? Нет, если очень сильно хочешь, то… {w}наверное… {w}Но это как-то не очень правильно?"
    "Взгляд у неё был растерянный и немного напуганный."
    "Я поспешил развеять её подозрения."
    me "Я шучу. Хочется, конечно, но не будем спешить."

    show mi serious pioneer at center with dspr

    th "Мне показалось, или она едва слышно выдохнула: «А жаль…»?"

    window hide

    scene bg ext_houses_day with dissolve

    show mi normal pioneer close at center with dissolve

    window show

    mi "Не хочу в домик идти. Мыло в бане точно есть, а у тебя в рюкзаке ведь полотенце лежало? Вроде чистое."
    me "Полотенце есть. А шампунь? Только не говори, что будешь мыть свои волосы мылом, это преступление!"

    show mi smile pioneer close at center with dspr

    "Я провёл рукой по её волосам. Мику улыбнулась, согласно кивнула."

    mi "И не поспоришь. Тогда сделаем маленький крюк, я возьму всё, что нужно."

    window hide

    hide mi with dissolve

    scene bg ext_house_of_un_day with dissolve

    show mi normal pioneer close at center with dissolve

    window show

    mi "Подожди меня пять минут. Я сейчас!"

    play sound sfx_open_door_1

    hide mi with dissolve

    mi "Лена, можно? {w}Ой, а её тут нет… {w}Наверное, где-то гуляет."

    window hide

    $ renpy.pause(1.0, hard=True)

    window show

    "Хорошо, что Лены не оказалось дома. Начни Мику пересказывать ей наши приключения, и в баню мы попали бы только на ночь глядя."

    window hide

    $ renpy.pause(1.0, hard=True)

    play sound sfx_open_door_1

    show mi normal pioneer close at center with dissolve

    window show

    "Я опасался зря. Мику собралась на удивление быстро. {w}Несколько минут ожидания, и моя спутница вернулась с небольшой яркой сумкой."
    "И конечно же, на сумке тоже были изображены котики."
    mi "Всё! Я готова."

    window hide

    stop ambience fadeout 3

    scene bg ext_bathhouse_day_bkrr with fade3

    play ambience ambience_day_countryside_ambience fadein 3

    window show

    "Славяна уже ждала у бани, поигрывая связкой ключей. Увидев нас, она тепло улыбнулась."

    show sl normal pioneer at center with dissolve

    sl "Вот вы где! Ольга Дмитриевна сказала вам баньку открыть. Там в баке горячая вода, разберётесь."

    show sl smile pioneer at center with dspr

    sl "Семён, так удачно, что ты много дров наколол, очень пригодились. Нужно будет Ульяне спасибо сказать. Если бы она над тобой не подшутила…"

    window hide

    hide sl with dissolve

    play sound sfx_open_dooor_campus_2

    $ renpy.pause(1.0, hard=True)

    window show

    "Славя улыбнулась и открыла двери бани."
    me "Ага. Рубил я, а спасибо Ульяне. Пригодились, говоришь?"

    show sl normal pioneer at center with dissolve

    sl "В котельной провода порвало, мы на тех дровах воду грели. Ещё бы не порвало, такая буря была!"
    sl "Вы сами-то как?"
    "Мику крутила в руках веник из дубовых листьев и ничего не ответила."
    me "Да немножко намёрзлись, немножко перепачкались, а так всё хорошо."

    show sl smile pioneer at center with dspr

    sl "Не беда, сейчас все проблемы разом решим. И согреетесь, и искупаетесь. Папа говорит: «Дух в парной – дух живой!»."
    "Славяна покачала головой."

    show sl sad pioneer at center with dspr

    sl "Правда, пара-то не будет. Просто горячая вода. Не баня, а так, одно название."
    "Я кивнул."
    me "Может, оно и к лучшему. Если попарюсь, то до утра уже не проснусь. А столько всего хочется успеть!"

    show sl tender pioneer at center with dspr

    sl "Не знаешь ты, чего лишаешься! Баня – это… {w}Это ух!"

    hide sl with dissolve

    "Она набрала в грудь воздуха, чтобы рассказать про банные традиции, но Мику деликатно прервала её, поинтересовавшись:"

    show mi normal pioneer close at center with dissolve

    mi "Кто первый, ты или я?"

    show mi happy pioneer close:
        center
        ease 0.5 zoom 1.2
    with dspr

    "Она наклонилась к самому моему уху и едва слышно шепнула:"
    mi "Или всё-таки вместе?"
    "Я так же тихо ответил ей:"
    me "Давай!"

    show mi shy pioneer close:
        center
        zoom 1.2
        ease 0.5 zoom 1.0
    with dspr

    "Мику густо покраснела и отошла на шаг."
    mi "Я же пошутила!"
    "Я развёл руками и притворно вздохнул:"
    me "Тогда дамы вперёд!"

    window hide

    show mi smile pioneer close at center with dspr

    $ renpy.pause(1.0, hard=True)

    hide mi with dissolve

    $ renpy.pause(1.0, hard=True)

    window show

    "Мику зашла в парную. Я присел на ступенях, бросив рюкзак прямо на пол. При этом раздался металлический лязг."
    "Славя осторожно потрогала мокрый брезент рюкзака. Тот снова отозвался звяканьем."

    show sl tender pioneer at center with dissolve

    sl "Ого. Что там у тебя? Только не говори, что банные принадлежности. Чугунный ковшик, проволочная щётка… {w}Нет?"
    me "Нет-нет. Это кибернетики меня в поход собирали и наложили полный мешок металлолома. Уверен, если поискать, где-то там на дне валяется аккумулятор и две кастрюли."

    show sl laugh pioneer at center with dspr

    sl "А зачем ты его в баню потащил?"
    me "Чужое ведь. Нельзя бросать где попало. Возьмут и ноги приделают."

    show sl normal pioneer at center with dspr

    sl "Думаешь? Здесь не воруют. Кроме…"

    show sl smile pioneer at center with dspr

    "Она улыбнулась."
    sl "Кроме рыжих барабанщиц, которые конфеты из кухни таскают."

    window hide

    hide sl with dissolve

    $ renpy.pause(1.0, hard=True)

    stop ambience fadeout 3

    play music music_list["eternal_longing"] fadein 3

    play sound bkrr_sfx_list["whiteout2"]

    scene cg d12_mi_bath_1 with bkrr_fade(3.0)

    window show

    "Я услышал плеск воды и представил себе, как прямо сейчас Мику медленно намыливается, она вся в белой пене, мочалка скользит по изгибам её тела, светлая кожа раскраснелась от горячей воды…"
    "Кровь бросилась в лицо. {w}Не будь рядом Слави, я бы точно не выдержал и зашёл бы к Мику, и будь что будет! {w}Хоть совместное купание, хоть тазиком по морде. Мечты, мечты…"

    window hide

    play sound bkrr_sfx_list["whiteout2"]

    scene bg ext_bathhouse_day_bkrr
    show sl surprise pioneer at center
    with bkrr_fade(0.5)

    play ambience ambience_day_countryside_ambience fadein 3

    window show

    "Славя удивлённо посмотрела на меня."
    sl "Ты чего такой красный? Не простыл?"
    "Не говорить же правду. Я изобразил кашель и виновато улыбнулся."
    me "Наверное, немного перемёрз."

    window hide

    show sl normal pioneer at center with dspr

    stop music fadeout 5

    $ renpy.pause(1.0, hard=True)

    hide sl with dissolve

    window show

    "Поверила она или сделала вид, но больше вопросов не было. {w}Славя подставила лицо тёплому июльскому солнцу и думала о чём-то своём."

    window hide

    $ bkrr_timeskip_short()

    scene bg ext_bathhouse_day_bkrr with bkrr_timeskip_transition()

    window show

    "Минут через пятнадцать Мику вышла наружу."

    show mi normal pioneer_loo at center with dissolve

    mi "Ой, хорошо-то как… словно заново родилась! {w}Сень, давай теперь ты!"

    window hide

    hide mi with dissolve

    stop ambience fadeout 3

    $ renpy.pause(1.0, hard=True)

    play sound sfx_open_dooor_campus_2

    scene bg int_bathhouse_bkrr with fade2

    play ambience bkrr_ambience_list["indoors_day"] fadein 3

    window show

    "«Парилка» оказалась простой комнатой, обшитой досками с деревянными скамьями под стенками."
    th "Интересно, на какой из них… {w}ну, всё происходило?"
    "Я бы предпочёл полежать в ванне, но пришлось ограничиться тазиком горячей воды и ковшиком."
    "Вместе с грязью вода смыла усталость и переживания прошедших суток. Запоздало я подумал, что мазь на спине тоже смылась."
    th "Надеюсь, она успела подействовать."
    "На сухом участке пола виднелись отпечатки небольших босых ножек. {w}В голову снова полезли шаловливые мысли о том, что Мику только что была здесь и…"

    window hide

    stop ambience fadeout 3

    play sound bkrr_sfx_list["whiteout2"]

    play music music_list["take_me_beautifully"] fadein 5

    scene cg d12_mi_bath_1 with bkrr_fade(3.0)

    play sound_loop sfx_head_heartbeat fadein 3

    window show

    mi "Ой! Кто здесь?"
    me "Не бойся, это я."
    mi "Сеня… {w}ты… {w}ты что здесь делаешь?"
    mi "Почему ты голый?"
    me "Я же обещал потереть тебе спинку!"

    window hide

    scene cg d12_mi_bath_2 with dissolve

    $ renpy.pause(1.0, hard=True)

    window show

    mi "Но я же шутила!"
    me "А я нет."
    mi "Мы ведь… поступаем неправильно?"
    "Её взгляд медленно опускается всё ниже и ниже."
    "Кажется, Мику раскраснелась не от жара и даже не от смущения."

    window hide

    scene bg int_bathhouse_bkrr
    show mi surprise shorts close at center
    with dissolve

    window show

    "Она попыталась прикрыться полотенцем."
    me "Совсем неправильно! Но я очень этого хочу."
    mi "Чего «этого»?"
    me "Тебя!"

    show mi shy shorts close at center with dspr

    mi "Ой, ну что ты такое говоришь. И не смотри так! Я стесняюсь."
    me "Не надо стесняться. Ведь это же я."

    window hide

    stop music fadeout 10

    $ renpy.pause(1.0, hard=True)

    show mi smile shorts close at center with dspr

    $ renpy.pause(0.5, hard=True)

    show mi normal shorts close at center with dspr

    window show

    "Я медленно приближаюсь к ней. {w}Мику подалась было назад, но затем улыбнулась и сделала шаг мне навстречу."
    mi "А я боялась, ты так и не решишься!"
    me "Я здесь, и я весь твой!"
    mi "Ну, иди же ко мне! Только будь понежнее, хорошо?"

    scene cg d12_mi_bath_scene

    "Мику протягивает руки, и полотенце плавно скользит вниз, дразняще-медленно обнажая её грудь. Я делаю шаг навстречу, наши тела вот-вот соприкоснутся. Я уже ощущаю мягкое тепло, идущее от её кожи, ещё мгновение, и…"

    window hide

    stop sound_loop

    play music music_list["revenga"]

    play sound bkrr_sfx_list["whiteout2"]

    scene bg int_bathhouse_bkrr:
        truecenter
        parallel:
            ease 0.5 zoom 2.0 rotate -9
        parallel:
            ease 0.3 ypos 0.6
            ease 0.2 ypos 0.25
    show red:
        alpha 0.0
        pause 0.35
        linear 0.15 alpha 0.5
    with None

    play ambience bkrr_ambience_list["indoors_day"] fadein 3

    $ renpy.pause(0.5, hard=True)

    play sound sfx_chair_fall

    play sound2 sfx_bodyfall_1

    play sound3 sfx_fall_wood_floor

    scene black

    $ renpy.pause(1.0, hard=True)

    window show

    "Замечтавшись, я шагнул вперёд, опрокинул жестяное ведро, стоявшее на полу, оно оглушительно загремело и укатилось под лавку, обдав мои ноги холодной водой."

    window hide

    scene bg int_bathhouse_bkrr with dissolve

    window show

    "От неожиданности я подскочил, опёрся рукой на полку, смахивая какие-то банные мелочи, наступил на кусок мыла и с размаху сел в холодную лужу на полу. {w}Потёртый дубовый веник, висевший на стене, сорвался с гвоздика и мягко шлёпнул меня по голове."
    th "Хорошо, что не ковшиком. Сходил в баньку, называется…"
    "Из-за тонкой двери раздались встревоженные девичьи голоса:"
    sl "Семён? Ты там в порядке? Эй!"
    mi "Славя, а вдруг он сознание потерял, он ведь в лесу головой ушибся! Нужно что-то делать, зови кого-нибудь, пусть дверь ломают!"

    stop music fadeout 5

    me "НЕТ!!! {w}Не надо никого звать! Я просто ведро опрокинул!"
    sl "Тихо, Мику, всё хорошо. {w}Слышишь? {w}Живой твой Семён."
    mi "Сеня, осторожнее, пожалуйста!"
    me "Хорошо!"
    "От мысли, что Мику совсем рядом, за стенкой, организм бодро отрапортовал о готовности. {w}Я вздохнул и полил себя холодной водой, чтобы успокоиться."

    window hide

    $ bkrr_get_achievement("bath")

    $ renpy.pause(1.0, hard=True)

    $ bkrr_timeskip_short()

    scene bg int_bathhouse_bkrr with bkrr_timeskip_transition()

    window show

    "Выйдя в предбанник, я понял, что придётся снова надевать грязные джинсы и футболку."
    th "Но не идти же через весь лагерь в полотенце?"

    window hide

    $ renpy.pause(0.5, hard=True)

    play sound sfx_open_dooor_campus_2

    $ renpy.pause(1.0, hard=True)

    scene cg d12_mi_hair_sl with fade

    play ambience ambience_day_countryside_ambience fadein 3

    window show

    "Холодное обливание взбодрило меня. Спать не то чтобы расхотелось, просто усталость слегка отступила, пообещав вернуться попозже."
    "Мику сидела на ступеньках и довольно щурилась, а Славя большим деревянным гребнем расчёсывала её роскошные волосы. Я улыбнулся, вытирая голову полотенцем."
    me "Как мило! Что это вы делаете?"
    "Увидев меня, Славя развела руки, чтобы я мог оценить длину волос Мику."
    sl "Красоту наводим, что же ещё. Знаешь, как непросто за такими длинными волосами ухаживать! Всё ради вас, парней, чтоб быть красивыми."
    me "Нет, не знаю."
    "Я ухватил прядь своей шевелюры и показал."
    me "У меня таких не было. Что, сильно тяжело?"

    scene bg ext_bathhouse_day_bkrr
    show sl smile pioneer close at center
    with dissolve

    sl "А ты возьми, сам попробуй!"
    "Славяна подмигнула мне и протянула гребень."

    window hide

    hide sl with dissolve

    $ bkrr_get_item("comb")

    show mi normal pioneer_loo close at center with dissolve

    window show

    me "Ты не против?"
    mi "Нет. Только осторожно, хорошо?"
    me "Конечно."

    scene cg d12_mi_hair_sem with dissolve

    "В гребне оказалось четыре отверстия для пальцев. Я взял его, как показала Славя, и осторожно провёл им по волосам Мику. Получалось, словно расчёсываешь и гребнем и пальцами одновременно. Мику глубоко вздохнула и села, чтобы мне было удобнее."
    "Занятие оказалось очень приятным, так что я с энтузиазмом принялся за дело."
    sl "Ну как, справится? "
    "Мику довольно кивнула."

    window hide

    play sound sfx_open_dooor_campus_1

    $ renpy.pause(1.0, hard=True)

    window show

    "Славя улыбнулась, заперла двери и отправилась в сторону лагеря, деликатно оставив нас наедине."
    "Я неторопливо водил гребнем по волосам Мику и тихо млел от этого необычного, но очень приятного ощущения."
    th "Какие же они длинные и красивые… Наверное, ей действительно непросто ухаживать за ними."
    "Каждая прядка уже была расчёсана, и не один раз, но останавливаться не хотелось. {w}Хотелось без конца продолжать эти плавные движения, ощущать под кончиками пальцев эту шелковистую мягкость, вдыхать аромат волос Мику и любоваться её по-детски безмятежным лицом."
    "Мику тоже явно получала удовольствие. {w}Она слегка откинула голову назад и прикрыла глаза."
    "Наконец, я сделал перерыв и взглянул на гребень. Был он явно не новым: дерево потемнело от времени, на широкой части выжжены затейливые узоры."
    me "Какой интересный, никогда такого не видел. Ты его из Японии привезла?"
    "Мику приоткрыла один глаз и покачала головой."
    mi "Нет! Это Славин. Она в первый же день, как увидела мои волосы, тут же стала уговаривать косы заплести. Я попробовала, но мне что-то не понравилось."
    mi "Я вообще косу только на ночь заплетаю, иначе спать неудобно. Славя сказала, что это какой-то очень старый гребень и что он счастье приносит. Только не смейся!"
    me "И в мыслях не было. Ну, кажется, всё."
    "Я мягко провёл гребнем сверху донизу."
    mi "Ой, здорово как! Спасибо!"
    "Я наклонился, чтобы вернуть ей гребень."

    scene cg d12_mi_hair_sem_bite with dissolve

    "Розовое ушко оказалось так близко к моим губам и выглядело так заманчиво, что я не удержался и коснулся его губами."
    "Мику вздрогнула, но ничего не сказала, только подалась назад, почти прижавшись ко мне спиной. Я обнял её за плечи и повторил поцелуй. Срывающимся шёпотом Мику поинтересовалась:"
    mi "Ой… что ты делаешь. {w}А вдруг кто-то увидит?"
    me "Так ведь нет никого."
    mi "Всё равно..."
    "Тёплые ладошки Мику легли поверх моих рук и мягко прижали их, то ли поощряя, то ли пытаясь остановить. Осмелев окончательно, я принялся посасывать мочку её уха и попытался опустить руки ниже, к груди."
    "Мику ласково, но твёрдо остановила мои поползновения и покачала головой, выдохнув:"
    mi "Ну не шали, пожалуйста!"
    me "Ничего не обещаю."

    scene bg ext_bathhouse_day_bkrr
    show mi smile pioneer_loo close at center
    with dissolve

    "Мику осторожно освободилась, встала и с улыбкой посмотрела на меня. Её щёки раскраснелись, и причиной наверняка была не только баня."
    mi "Это было… здорово."
    me "Мне и самому понравилось… Повторим?"
    th "Что именно она имеет в виду? Расчёсывание или то, что было после?"
    mi "Обязательно! Но попозже."

    show mi normal pioneer_loo close at center with dspr

    mi "Смотри, не спутай, а то опять расчёсывать придётся!"
    me "Напугала кота сметаной."
    "Я встал со ступенек, подал руку Мику."
    me "Пошли?"
    mi "Да, идём. А то сейчас засну прямо здесь."

    window hide

    hide mi with dissolve

    $ renpy.pause(1.0, hard=True)

    window show

    "Мику улыбнулась, сложила в сумку банную мелочёвку, и мы двинулись по тропинке в лагерь."

    window hide

    stop ambience fadeout 3

    scene bg ext_house_of_un_day with fade3

    play ambience ambience_camp_center_day fadein 3

    window show

    "Возле домика Мику сиреневое деревце скрыло нас от нескромных взглядов. {w}Я обнял её."

    show mi normal pioneer_loo close at center with dissolve

    me "Знаешь, после всего, что было, я боюсь терять тебя из виду. Вдруг отвернусь, а ты исчезнешь куда-нибудь."
    me "Может, к вам с Леной переехать? Постелите мне на коврике…"

    show mi smile pioneer_loo close at center with dspr

    "Мику коснулась пальцем кончика моего носа и с улыбкой покачала головой."
    mi "Я, конечно, не против, но Лена стесняться будет. И потом, ты увидишь меня утром, когда я сонная, лохматая и ворчу. {w}Увидишь и сбежишь!"
    me "Ты ворчишь? Не верю."

    show mi laugh pioneer_loo close:
        center
        ease 1.0 zoom 1.2
    with dspr

    mi "Ой, сколько иллюзий ещё предстоит разбить!"
    "Мику звонко рассмеялась и прижалась ко мне."
    me "И Мику…"

    show mi normal pioneer_loo close:
        center
        zoom 1.2
    with dspr

    mi "М-м-м?"
    me "Я никуда не сбегу!"

    window hide

    show mi smile pioneer_loo close:
        center
        zoom 1.2
    with dspr

    $ renpy.pause(1.0, hard=True)

    hide mi with dissolve

    window show

    "С этими словами я поцеловал её. {w}В этот момент я сам верил в то, что говорю."
    th "Вот только я могу исчезнуть отсюда так же, как и появился…"
    "Я загнал эту мысль подальше и строго-настрого запретил ей показываться на глаза."

    show mi normal pioneer_loo close at center with dissolve

    me "Чуть не забыл. Там Лена очень за тебя волновалась. Успокоишь её, хорошо?"
    mi "Обязательно!"

    window hide

    hide mi with dissolve

    $ renpy.pause(1.0, hard=True)

    play sound sfx_open_door_1

    $ renpy.pause(2.5, hard=True)

    play sound sfx_close_door_1

    window show

    "Мику послала мне воздушный поцелуй и скрылась в домике."

    window hide

    stop ambience fadeout 3

    scene bg ext_music_club_day with fade3

    play ambience ambience_camp_center_day fadein 3

    window show

    "Перед тем, как идти отдыхать, я решил зайти в музклуб. {w}Там лежала моя последняя чистая футболка, да и форменную рубашку, причину моих приключений, тоже нужно было забрать."
    "Боюсь, если я попрошу у Ольги ещё один комплект формы, она обязательно прочтёт мне длинную и очень нудную нотацию про бережное отношение к имуществу лагеря."
    th "Интересно, они мне хоть немного земляники оставили? А то я, кроме той единственной ягоды, так её и не попробовал."

    window hide

    scene bg ext_music_club_day at bkrr_moving_forward_far(3.0, 1.5)

    $ renpy.pause(2.5, hard=True)

    scene bg ext_music_club_verandah_day_v6 with dissolve

    window show

    "Разумеется, вместо репетиции рыжие сидели на веранде и вовсю били баклуши."
    "Алиса притворилась, что не узнаёт меня."

    show dv normal pioneer2 at cleft
    show us smile sport at cright
    with dissolve

    dv "Ульяна, кто это? Романтические лохмотья, рюкзак… {w}Наверное, геолог какой-то заблудился?"
    us "Не! Геологи – они с бородой! {w}Это Сенька наш. Только одет не по форме и грязный."

    show dv smile pioneer2 at cleft
    show us grin sport at cright
    with dspr

    us "Сень, ты что, решил панк играть? Тогда джинсы надо порвать на коленях и ещё какую-нибудь гадость на футболке написать. На ненашем языке!"
    me "Шёл мимо, решил по пути к вам заглянуть, а вы бездельничаете. Что бы Мику сказала?"

    show us upset sport at cright with dspr

    us "Не нуди, у нас перерыв! А ты чего не отдыхаешь?"
    me "Я вообще к кибернетикам шёл, хотел рюкзак им вернуть."

    show us normal sport at cright with dspr

    us "Не твой сегодня день, Семёныч. Я только от них. {w}Никого там нет, они помогают электрику провода тянуть где-то в лагере. Так что кидай багаж у нас, а вечером вернёшь."
    "Ульяна посмотрела на небо."
    us "Жарковато… {w}Может, внутрь зайдём?"

    window hide

    hide dv
    hide us
    with dissolve

    $ renpy.pause(1.0, hard=True)

    window show

    "Она помогла Алисе подняться. Та слегка прихрамывала, но вроде бы шла на поправку. {w}Я подал Алисе руку, она опёрлась на неё, буркнув что-то вроде: «Спасибо, но я и сама могу…»."
    th "Что тут скажешь. Лучше умрёт, чем признает свою слабость."

    window hide

    play sound sfx_open_door_2

    scene bg int_music_club_mattresses_day with dissolve

    play ambience bkrr_ambience_list["indoors_day"] fadein 3

    play music music_list["smooth_machine"] fadein 7.5

    window show

    me "Можешь, можешь. Просто захотел тебя за ручку подержать. Как нога?"

    show dv guilty pioneer2 close at cleft with dissolve

    dv "Да так…"
    "Алиса вздохнула."
    dv "То ничего, то ныть начинает. На дождь – ужас, как крутило. {w}Поиграла в баскетбол, называется."

    show dv normal pioneer2 close at cleft with dspr

    dv "Ладно, хоть не рука, а то пришлось бы концерт отменять."
    me "Ничего! Будем по твоей ноге погоду определять! Крутит – к дождю. Сильно крутит – к туману."

    show dv angry pioneer2 close at cleft with dspr

    dv "Ща кого-то стукну!"
    "Алиса изобразила замах."
    me "Тогда придётся меня к медсестре тащить, а у тебя нога болит. {w}Оно тебе надо?"

    show dv normal pioneer2 close at cleft with dspr

    "Алиса подумала, потом согласилась."
    dv "Убедил."

    window hide

    hide dv with dissolve

    $ renpy.pause(1.0, hard=True)

    scene cg d12_noon_rest_1 with dissolve

    window show

    "Рыжая уселась на матрасах, устроила больную ногу на стул, пощипала струны, потом заявила, что репетировать сегодня не может, слишком переволновалась, да и руководитель кружка бессовестно спит."
    dv "Вы идите, я одна посижу. Семён, не дашь мне тетрадку? Вон, возле тебя. Я так удобно устроилась, вставать не хочу."
    me "Сейчас."

    window hide

    scene bg int_music_club_mattresses_day with dissolve

    window show

    "Я взял в руки две одинаковые тетради."
    me "А какую тебе? Одна…"
    "Я пролистал страницы."
    me "… с нотами, а другая…"
    dv "СТОЙ!"

    play sound sfx_punch_medium

    "Я не успел остановиться и начал открывать вторую. Раздался шорох рассекаемого воздуха, и в стену возле меня врезалась Алискина босоножка." with vpunch
    dv "НЕ СМОТРИ!!!"

    scene cg d12_noon_rest_2 with dspr

    "У меня было искушение заглянуть, но Алиса уже нашла новый снаряд в виде увесистой книги. Женя просила меня поберечь библиотечное имущество. Я ведь ей обещал."
    us "Лучше делай, как она говорит."
    me "Всё-всё. Кладу. Уже положил. Ты чего так взбесилась-то?"

    scene cg d12_noon_rest_3 with dspr

    us "Как подскочила! А ну глянь, может, у неё там пять рублей спрятано?"
    dv "Нет! Там… личное!"
    "Я поднял босоножку, прикинул, бросить в неё обратно или свести в шутку. {w}В конце концов, это же Алиса. Если она начнёт вести себя нормально, то станет скучно."
    me "Ну, хорошо, хорошо. Вот, Золушка, твои тетрадки, вот твоя туфелька. Вот тебе ещё перекус, чтоб не вставать."
    "Я поставил рядом с ней пакет кефира и пару булок из столовой. Затем опустился на одно колено и принялся надевать метательный снаряд обратно. {w}Ступня Алисы была очень мягкой и тёплой. {w}Я не удержался и пощекотал её."

    scene cg d12_noon_rest_4 with dspr

    dv "Ай!!!"
    "Алиса взбрыкнула ногой, чуть не угодив мне в нос."
    me "Больная-больная, а ногами машешь, как здоровая. Симулируешь небось?"
    dv "Поговори мне тут ещё!"
    "Рыжая честно попыталась говорить угрожающе, но не выдержала и рассмеялась. "

    scene cg d12_noon_rest_5 with dspr

    extend "Она поправила босоножку и взяла у меня тетради."
    dv "Спасибо. Ты извини, что я тапкой. Привыкла Ульяну от своих вещей отгонять, вот и бросила по привычке. Я тебя не ушибла?"
    me "Нет, не попала."

    window hide

    scene bg int_music_club_mattresses_day
    show dv normal pioneer2 at cleft
    show us smile sport at cright
    with dissolve

    window show

    "Ульяна невинно заметила:"
    us "Значит, плохо целилась! А надо было стукнуть! Он там тебе под юбку смотрел!"

    show dv rage pioneer2 at cleft with dspr

    dv "Чего-о-о???"
    "Алиса потянулась за гитарой."
    dv "Ах ты, кобель!"
    me "Неправда!"

    show us laugh2 sport at cright with dspr

    us "Ну ладно, ладно. Неправда. Алиса так смешно бесится, я не удержалась."

    show dv angry pioneer2 at cleft with dspr

    dv "Ничего я не бешусь! Идите уже, ритм-секция. Надоели! Дайте от вас отдохнуть!"

    window hide

    hide dv
    hide us
    with dissolve

    stop music fadeout 5

    stop ambience fadeout 0.5

    scene bg ext_music_club_verandah_day_v6 with dissolve

    play ambience ambience_camp_center_day fadein 3

    window show

    "Я не возражал. Снова накатила усталость, потянуло в сон."
    "Мы с Ульяной вышли из клуба, а в спину нам донеслась какая-то незнакомая, но красивая мелодия на гитаре."
    "Ульяна подёргала меня за руку."

    show us normal sport close at center with dissolve

    us "Расскажи, что там было-то? Ну, в лесу?"
    me "Да ничего такого. Бегал, как ужаленный, и кричал: «Мику! Мику!», – а она в старом лагере нашлась."
    us "И всё?"
    me "Ещё встретил своего двойника, чёрную вожатую и злого ежа-оборотня!"

    show us grin sport close at center with dspr

    us "Ой-ой. Ври больше."
    "Ульяна показала мне язык и рассмеялась."
    th "Кстати, о вранье."
    me "Ульянка, мне нужно тебе кое-что сказать."

    show us surp2 sport close at center with dspr

    us "Что?"

    show us surp2 sport close:
        center
        ease 0.5 zoom 1.1
    with dspr

    "Я остановился, приобнял её и поцеловал в макушку."
    me "Спасибо тебе большое."

    show us smile sport close:
        center
        zoom 1.1
        ease 0.5 zoom 1.0
    with dspr

    us "Пожалуйста. Какие мы добрые сегодня. Ещё и целоваться полез… {w}А ты о чём сейчас?"
    me "Когда мы с Алисой ругались, а ты за меня вступилась. На самом деле ты ведь не видела Шурика с Виолой. В смысле – в тот день."

    show us normal sport close at center with dspr

    us "Не-а. Девчонки шушукались, но я их вместе не видела. {w}А как ты понял?"
    me "Да так. Они вместе не ходят. Конспираторы, понимаешь. {w}А соврала зачем?"

    show us laugh sport close:
        center
        ease 0.5 zoom 1.1
    with dspr

    "Она встала на цыпочки и легонько хлопнула меня кончиками пальцев по лбу и засмеялась."

    show us laugh sport close:
        center
        zoom 1.1
        ease 0.5 zoom 1.0
    with dspr

    us "Потому, что ты дурак."
    me "Грубо, Уля, грубо!"
    "Странно, но обижаться на неё я не мог."

    show us smile sport close at center with dspr

    us "Зато правда. У тебя на лбу вот такенными буквами написано, что Мику тебе нравится. И лицо у тебя глупое, когда ты о ней говоришь. {w}Не мог ты так поступить."
    "Ульяна показала, какое именно лицо у меня было."
    me "Опять дразнишься?"

    show us normal sport close at center with dspr

    us "Ну, может, не совсем такое, но похожее. У неё, кстати, такое же, если мы тебя обсуждаем! Только никому не говори!"
    me "Хорошо, рыжик, не буду."

    show us smile sport close at center with dspr

    us "В общем, я подумала и решила, что ты правду говоришь. Любишь ведь её, да?"
    me "Секрет!"

    show us upset sport close at center with dspr

    us "Ой-ой, можно подумать, можно подумать. {w}Я и так знаю, потому и помогала."

    show us normal sport close at center with dspr

    us "Алиса, понимаешь, парням не очень доверяет. Конечно, ты бы её убедил, но я немного ускорила события."
    me "Спасибо!"

    show us grin sport close at center with dspr

    us "Спасибо с чаем не попьёшь, если ты понимаешь, о чём я."
    me "Я ей о чувствах, а ей лишь бы сладкого урвать."
    us "А то! Так что с тебя конфеты и рассказ."
    me "Конфеты попозже, а рассказ могу сейчас. {w}Выскочил я, значит, за ворота и побежал сразу в лес. А там…"

    window hide

    stop ambience fadeout 3

    $ bkrr_timeskip()

    scene bg ext_houses_day with bkrr_circleout_transition

    play ambience ambience_camp_center_day fadein 3

    window show

    "Живописание моих приключений заняло какое-то время. Ульяна слушала, время от времени вставляя язвительные комментарии. {w}Конечно, я не рассказал ни про двойника, ни про девочку с хвостом, ни про наше с Мику признание."

    show us normal sport close at center with dissolve

    us "Эх, Семёныч! Самое удивительное, что ты вообще вернулся. Ты в походы ходил вообще?"
    me "Два раза. Полтора, точнее. Один раз вернулся с половины."

    show us smile sport close at center with dspr

    us "Тогда понятно. {w}Я тоже с тобой просилась, но Ольга запретила, сказала, что ты чуть ли не лесной следопыт. Виннету пополам с Чингачгуком. {w}А ты такого начудил."
    me "А что не так?"
    us "Да всё не так. Ладно, вернулся и вернулся. Домой приеду, дедушке расскажу, пусть посмеётся."
    me "Ну, главное, что вернулись. В такую бурю…"

    show us normal sport close at center with dspr

    us "Я и говорю – удивительно."

    show us shy sport close at center with dspr

    us "Слушай… {w}А вы с Мику… {w}Ну, это? Это самое?"
    me "Ты о чём?"

    show us shy2 sport close at center with dspr

    us "Ну…"
    "Она густо покраснела, махнула рукой."

    show us upset sport close at center with dspr

    us "Ничего."
    me "Настоящий мужчина не будет болтать, даже если что-то и было."

    show us laugh2 sport close at center with dspr

    us "Так то ж настоящий! А ты же лопнешь, если не поделишься. Ну, было что-то?"
    me "Мы поцеловались и спали в обнимку. Больше ничего. Устали и замёрзли."

    show us normal sport close at center with dspr

    us "И всё? А я-то думала: парень, девушка, наедине, всю ночь. А у вас ничего не было. Как неинтересно! Что же мне Алиске сказать…"
    me "Уля, только от себя не сочиняй ничего, ладно?"

    show us calml sport close at center with dspr

    "Она обиженно посмотрела на меня."
    us "Семён-Семён. Обижаешь! Думаешь, я буду распускать такие слухи про лучшую подругу? Да ни за что!"
    me "Извини, не подумал."

    show us smile sport close at center with dspr

    us "Вот про тебя – другое дело. Расскажу-ка я всем, что ты там Мику от медведя спасал."
    me "Ульяна!!!"

    show us normal sport close at center with dspr

    us "Хотя нет. {w}Медведь тебя сожрал бы. Никто не поверит. Не буду рассказывать."
    me "И на том спасибо."
    us "А вот я после вчерашнего поверила бы. Знаешь, я когда увидела тебя в первый раз, там, у кружков, решила, что ты чудик какой-то. {w}А ты ничего, нормальный. Я бы с тобой в разведку пошла."
    me "Слушай, вы с Алиской меня пугаете. То она говорит, что я не совсем бездарь, то ты говоришь, что я «ничего» и «нормальный». Сильно вы ласковые, я чую подвох."
    us "Это ты типа пошутил, да?"
    me "Да нет, правда. Последний раз, когда вы были такими милыми, я басистом стал."

    show us smile sport close at center with dspr

    us "Басист? {w}Ты? {w}Не смеши меня. Дёргать одну струну – это не значит быть басистом."
    me "Я не понял! А где солидарность ритм-секции? Ты же меня должна поддерживать и ободрять. А ты только язвишь."

    show us laugh2 sport close at center with dspr

    us "Поддержка? Это я могу!"

    show us normal sport close at center with dspr

    "Ульяна положила руку мне на плечо, сделала очень серьёзное лицо, заглянула мне в глаза и доверительно сообщила:"
    us "Семён! Давно хотела тебе сказать. {w}Ты… {w}ты… {w}Ты очень многообещающая личинка басиста!"

    show us smile sport close at center with dspr

    us "Так лучше?"
    me "Знаешь… Лучше язви."

    show us dontlike sport close at center with dspr

    us "Парни. {w}Вы вообще знаете, чего хотите?"
    me "Знаю! Лично я хочу переодеться, наконец, в чистое и лечь спать!"

    show us smile sport close at center with dspr

    us "Это ты правильно! А то подумают, что в лагере хиппи завелись."

    window hide

    scene bg ext_square_day with dissolve

    $ renpy.pause(1.0, hard=True)

    window show

    "Мы вышли на площадь."

    show us normal sport close at center with dissolve

    us "Ну, вам налево, нам направо!"

    window hide

    $ renpy.pause(1.0, hard=True)

    window show

    "Она помялась, потом добавила:"
    us "Я после обеда приду. Дело есть! Важное!"
    "Я ответил цитатой из старого мультфильма:"
    me "Не хочу есть дело, хочу крем-брюле!"

    show us smile sport close at center with dspr

    us "Обжора!"

    hide us with dissolve

    "Ульяна хлопнула меня по плечу и умчалась в сторону своего домика."

    window hide

    stop ambience fadeout 3

    scene bg int_house_of_mt_day with fade3

    play ambience ambience_int_cabin_day fadein 3

    window show

    "Я вошёл к себе. Ольги Дмитриевны не было видно."

    window hide

    $ renpy.pause(1.0, hard=True)

    window show

    "Неторопливо раздевшись, я убрал джинсы и зимние ботинки подальше в шкаф, а сам растянулся на кровати."
    th "Сколько всего случилось…"
    "Стоило мне решить, что это самый обычный лагерь из прошлого, как чудеса посыпались одно за другим. {w}Все эти странные сны на пляже, двойник в лесу, незнакомец в старом лагере…"
    "Но это не пугало. {w}Скорее забавляло. {w}Не верилось, что здесь могло случиться что-то плохое."
    th "Ведь мы с Мику снова вместе. А что ещё нужно?"
    th "Нужно…"

    window hide

    show blink

    $ renpy.pause(1.5, hard=True)

    window show

    "Додумать, что именно нужно, я не успел, вместо этого погрузившись в здоровый послеобеденный сон."

    window hide

    stop ambience fadeout 5

    play music music_list["faceless"] fadein 5

    play sound sfx_intro_bus_transition

    $ renpy.pause(2.0, hard=True)

    scene bg semen_room_clean_bkrr:
        truecenter
        zoom 1.3
        ease 8.0 zoom 1.0
    show prologue_dream:
        alpha 0.25
    with fade3

    $ bkrr_set_time("prologue")

    $ renpy.pause(3.0, hard=True)

    window show

    th "В комнате кто-то есть."
    th "Какое странное ощущение. Знакомое место, но всё неуловимо изменилось. Это моя комната, но в то же время не моя."

    $ bkrr_set_name("me", "Я")

    me "Кто здесь?"

    show bkrr_pi normal at cright behind prologue_dream with dissolve

    pi "Не бойся."
    th "Это {b}его{/b} голос. {w}{b}Его{/b}, но звучит он совсем иначе. Голос такой, каким был когда-то."
    me "Ты? {w}Но ты ведь в командировке. {w}Почему ты здесь?"
    pi "Сложно объяснить так, чтобы ты поняла. Извини, что вот так, среди ночи, но у нас очень мало времени."
    me "Мало времени? {w}На что?"
    pi "Нам нужна твоя помощь."
    me "Помощь? Какая ещё помощь? {w}И кому это «нам»?"
    pi "Ты помнишь место, где мы познакомились?"
    me "Конечно."
    th "Как будто это можно забыть. Такое не забывается."
    pi "Ты никогда не хотела туда вернуться?"
    th "Хотел{b}а{/b}? Что он имеет в виду?"
    me "Ни разу."
    "До меня внезапно стало доходить, что голос, которым я говорю, совсем даже не мой. Приятный грудной голос взрослой женщины. Его я точно не слышал, но есть в нём что-то очень знакомое…"

    show uv normal at fleft behind prologue_dream with dissolve

    "В темноте вспыхивают два жёлтых огонька и со стороны двери на кухню доносится мягкий вкрадчивый голос."
    uv "Это хорошо. Именно то, что нам нужно. Скажи, если бы я предложила тебе снова там побывать, ты бы согласилась?"
    me "Нет! Я не хочу ничего менять!"

    show uv sad at fleft behind prologue_dream with dspr

    "Я не испытываю страха сам, но ощущаю страх говорящей. Она дико, до дрожи в коленках и холодного пота боится. {w}Но не этих двоих, что стоят перед ней ночью в пустой квартире, а чего-то другого."
    uv "Не волнуйся, ты останешься здесь и никуда не денешься. Просто… {w}иногда ты будешь видеть сны про тот лагерь. {w}Это ведь не страшно, правда? Нам действительно очень нужна твоя помощь."
    me "Что вам нужно, вы скажете или нет?"

    show uv smile at fleft behind prologue_dream with dspr

    uv "Я всё тебе расскажу. {w}Но там."
    uv "Там у нас будет больше времени. Не бойся, это будет всего лишь сон."

    window hide

    show uv smile close at fleft behind prologue_dream with dspr

    $ renpy.pause(1.0, hard=True)

    show blink

    $ renpy.pause(1.5, hard=True)

    window show

    "Её жёлтые глаза всё ближе, ближе и ближе… Совсем как тогда, на пляже."

    window hide

    stop music

    $ bkrr_set_name("me", "Семён")

    scene bg int_house_of_mt_day at bkrr_shake_atl with vpunch

    $ bkrr_set_time()

    play ambience ambience_int_cabin_day

    window show

    "Я дёргаюсь и просыпаюсь."
    th "А что, если я действительно превратился в женщину? Нет. Только не это. Нет!"
    "Рука машинально потянулась к низу живота."

    window hide

    $ renpy.pause(1.0, hard=True)

    window show

    th "Всё на месте, ничего не пропало. {w}Всё нормально. {w}По лесу набегался, вот и приснилась ерунда. Это просто сон."
    "Довольный этим открытием, я перевернулся на другой бок и снова уснул."

    window hide

    stop ambience fadeout 2.5

    show blink

    $ renpy.pause(2.5, hard=True)

    scene bg int_house_of_mt_sunset
    show unblink

    $ bkrr_set_time("sunset")

    play ambience ambience_int_cabin_evening fadein 3

    $ renpy.pause(1.5, hard=True)

    window show

    th "Ладно, будем вставать."
    "Будильник на окне показывал начало шестого. Ольги в домике не было, но брошенная как попало форма была аккуратно развешана на спинке стула."
    th "Скоро ужин… Интересно, Мику уже проснулась?"

    window hide

    stop ambience fadeout 0.5

    play sound sfx_open_door_1

    scene bg ext_house_of_mt_sunset with dissolve

    play ambience ambience_camp_center_evening fadein 3

    $ renpy.pause(1.5, hard=True)

    play sound sfx_close_door_1

    window show

    "Я оделся и выглянул на улицу. Там меня уже поджидали."
    "Ульяна сидела в шезлонге у входа в домик и тормошила Пирата. Тот урчал и пытался облизать ей уши."

    show us normal pioneer at center with dissolve

    us "Ну наконец-то! Сколько можно дрыхнуть?"
    "Увидев меня, рыжая опустила кота на землю и принялась отчитывать, копируя интонации вожатой."

    show us calml pioneer at center with dspr

    us "Сколько можно спать, я спрашиваю? Ты что сюда, ради этого приехал?"
    me "Не исключено."

    show us smile pioneer at center with dspr

    us "Соня! Ладно, ты что сейчас делать будешь?"
    me "Ничего вроде. К Мику хотел пойти."
    us "Я у неё была, она ещё спит. Пошли!"
    me "Куда? Зачем?"

    show us laugh2 pioneer at center with dspr

    us "Надо!"

    window hide

    scene bg ext_houses_sunset with dissolve

    window show

    "Подсознательно я ожидал, что по возвращении мне вручат медаль «За спасение заблудившихся в лесу» с закруткой на спине, устроят в мою честь торжественную линейку или хоть тортиком угостят в честь такого знаменательного события."
    "Ничего подобного."
    "Словно ничего не случилось. Никому не было дела, что пионерка Мику заблудилась в лесу, а пионер Семён бросился в бурю искать подругу."

    show us normal pioneer at center with dissolve

    us "Ты чего кислый такой?"
    me "А? Нет, просто я задумался."

    show us smile pioneer at center with dspr

    us "Сделай лицо попроще, а то Мику испугаешь, если встретим."
    me "Погоди, ты говорила, она спит."
    us "Всё может быть! Ага. Мы почти пришли."

    window hide

    stop ambience fadeout 1

    scene bg int_shed_bkrr_v1 with fade

    $ bkrr_set_time("sunset", "day")

    play ambience bkrr_ambience_list["indoors_evening"] fadein 3

    window show

    "Ульяна притащила меня к уже знакомому сараю. Открыв скрипучую дверь, она завела меня вовнутрь. {w}Тот самый склад."
    "Грубо сколоченный щит стоял на прежнем месте, скрывая дыру в стене, ведущую в лес."
    me "И зачем мы здесь?"

    show us sad pioneer close at center with dissolve

    us "Сень… это…"
    me "Да?"
    "Я ободряюще положил ей руку на плечо."

    show us shy pioneer close at center with dspr

    us "Знаешь, есть одно дело… очень важное. {w}Можешь помочь? Вся надежда на тебя."
    me "Рассказывай. Опять привидение ловить?"
    us "Нет!"

    window hide

    show us shy2 pioneer close at center with dspr

    $ renpy.pause(0.5)

    show us shy pioneer close at center with dspr

    $ renpy.pause(1.0)

    show us shy2 pioneer close at center with dspr

    window show

    "Она помялась, глядя куда-то вбок, потом глубоко вздохнула и выпалила:"

    play music music_list["always_ready"]

    show us surp3 pioneer close at center with dspr

    with vpunch

    us "Покажимнекакнадоцеловаться!"
    "Вначале я подумал, что ослышался."
    me "Что-что?"

    show us shy2 pioneer close at center with dspr

    us "Да всё ты слышал!"

    play sound sfx_tennis_serve_1

    show us dontlike pioneer close at center with vpunch

    "Ульяна топнула ножкой, а затем медленно, как слабоумному, повторила:"
    us "Покажи. {w}Мне. {w}Как. {w}Надо. {w}Целоваться."
    th "Нет. Я не ослышался."
    th "Может, девчонки проверку затеяли? С них станется."
    me "Ульяна, мне Мику нравится, понимаешь? Если я сейчас буду целоваться с другой, то это будет полным свинством."

    show us sad pioneer close at center with dspr

    "Ульяна грустно вздохнула."
    us "Да… {w}Я всё понимаю. Но мне больше некого попросить."
    me "Вон, Алиску попроси. Она научит."

    show us calml pioneer close at center with dspr

    us "Фу! Она же девушка."

    show us smile pioneer close at center with dspr

    "Ульяна улыбнулась. Смущение уступало место обычному задору."
    us "И она не умеет. Я спрашивала."
    me "А почему тебе так приспичило?"

    show us sad pioneer close at center with dspr

    us "Танцы скоро. И я хочу там кое с кем поговорить. Он меня за ребёнка считает."
    me "Вот оно как."
    th "Кое с кем поговорить. Ага. С блондинистым любителем женщин в белых халатах, видимо."

    show us normal pioneer close at center with dspr

    us "В общем, покажи! Мало ли что."
    me "Точно хочешь, чтобы я показал?"

    show us dontlike pioneer close at center with dspr

    us "Да точно, точно! Семёныч, долго я тебя уламывать буду, как солдат гимназистку? Я что, такая противная?"
    me "Да нет, ты симпатичная, всё в порядке. Но я не хочу обманывать Мику."

    show us upset pioneer close at center with dspr

    us "Вот непробиваемый, а…"

    window hide

    $ renpy.pause(1.0, hard=True)

    show us grin pioneer close at center with dspr

    window show

    "Она на минутку задумалась, потом просияла."
    us "Сень. А вот если бы я тонула, ты бы сделал мне искусственное дыхание?"
    me "Ну… да."

    show us smile pioneer close at center with dspr

    us "Вот, считай, что спасаешь мне жизнь. Если мы с… {w}с ним поцелуемся, и у меня получится плохо, я ведь от стыда умру."
    me "Ладно, ладно. Хватит драмы. К тому же, если ты помрёшь, то кто барабанить будет."
    us "Наконец-то. Ну, давай уже закончим побыстрее."
    me "Мы с Мику только помирились. Если сейчас она застанет нас целующимися, то не поверит, что это просто дружеская помощь."

    show us laugh2 pioneer close at center with dspr

    "Ульяна немного подумала, затем согласно кивнула."
    us "Значит, запри дверь!"

    window hide

    hide us with dissolve

    $ renpy.pause(1.0, hard=True)

    play sound sfx_lock_close

    stop music fadeout 3

    window show

    "Я убедился, что в сарае никого нет, потом запер дверь на щеколду, и мы присели рядом на коробках."

    scene cg d12_us_kiss_2 with dissolve

    "Ульяна смотрела на меня с интересом и явно волновалась."
    "До поцелуя с Мику мои знания были чисто теоретическими, но Ульяна умела и того меньше. Я вдруг ощутил себя очень старым и очень опытным."
    th "Как там, в том видео делали…"
    me "В общем…"
    "Я поднял было палец, начиная лекцию."
    me "… для начала чуть приоткрой губы и…"

    window hide

    play music music_list["eat_some_trouble"]

    scene cg d12_us_kiss_1 at bkrr_shake_atl with vpunch

    $ renpy.pause(0.5, hard=True)

    window show

    "Ульяна решила, что грамм практики стоит тонны теории и с размаху залепила мне рот своими губами."
    "Меня отбросило на стену, наши зубы клацнули друг о дружку, а нос сильно упёрся ей в щёку, чуть не сложившись пополам."

    scene cg d12_us_kiss_3 with dspr

    "Ульяна отстранилась и довольно посмотрела на меня."
    us "Ну как?"
    me "Очень… энергично."
    us "А то!"
    me "Хорошо, как {b}не{/b} надо, ты уже знаешь. После такого нахрапа он от тебя убежит и запрётся в кладовке."

    scene cg d12_us_kiss_4 with dspr

    me "Теперь давай не спеша и аккуратнее."
    us "Какой ты нудный. Мог бы и похвалить!"
    "Ульяна показала мне язык."
    me "То же самое, но помедленнее. Как я понимаю, сам он тебя, скорее всего, не поцелует…"
    us "Это чего это вдруг?"
    th "Из-за Виолы, конечно."
    me "Постесняется. Мы не можем ждать милостей от природы. Взять их – вот наша задача! Значит, вначале тебе надо будет до него дотянуться. Лучше, конечно, если сидеть будете… Меня Мику слегка за галстук потянула, попробуй тоже так. Только не задуши!"
    us "Слушай, разберусь, ты к делу давай! Или ты сам ничего не знаешь? Соврал, что с Мику целовались, да?"
    me "Да знаю я! В общем, главное – знать, куда деть нос, и не биться зубами о зубы. Сейчас медленно, без замаха, коснись губами губ…"

    window hide

    scene cg d12_us_kiss_5
    show blink
    with dspr

    $ renpy.pause(1.7, hard=True)

    hide blink
    show unblink


    $ renpy.pause(1.5, hard=True)

    window show

    "Ульяна выполнила задание и замерла, смешно глядя на меня снизу вверх с губами «уточкой». {w}Я чуть подался назад, чтобы получить возможность говорить."
    th "Только бы не заржать. Укусит ведь."
    me "Молодец. Это так, просто коснулись губами, для первого раза. Теперь дальше."
    us "Знаю! Я в кино видела! Надо языком достать до его языка…"
    me "Тьфу, это что ж за кино такое?"
    us "Не знаю. Немецкое какое-то, про водопроводчика. Знакомый привёз кассету, я до поцелуя досмотрела, а потом мама с папой меня почему-то выгнали из комнаты. А что не так?"
    me "С языком сразу не нужно."

    window hide

    show blink

    $ renpy.pause(1.5, hard=True)

    window show

    me "Начни с поочерёдного лёгкого посасывания нижней и верхней…"
    me "Ай! Да не откусывания, а посасывания!"

    scene cg d12_us_kiss_6
    show unblink


    "Рыжая пионерка смущённо развела руками."
    us "Прости, Семёныч. Я только на помидорах тренировалась… Они не жаловались."
    me "На помидорах?"
    us "Ну да. Очень похоже, кстати, на губы, только нужно…"
    me "И знать не хочу, оставь мне мои иллюзии про юных пионерок. Я тебе не помидор, не отгрызай мне губу."
    me "Легонько посасываешь то верхнюю, то нижнюю губы, глаза лучше закрой… {w}И руки на шею. {w}Да не за горло хватай, а обними. Вот, как-то так."

    window hide

    scene cg d12_us_kiss_3
    show blink
    with dspr

    $ renpy.pause(1.7, hard=True)

    window show

    us "Давай ещё раз."
    "Со второго раза вышло почти как надо."

    hide blink
    show unblink


    me "Ладно, вроде ничего."
    "Ульяна не унималась."
    us "А язык?"
    "Я смутился."
    me "С языком тебе рановато. Хватит и того, что мы уже освоили."

    scene cg d12_us_kiss_5 with dspr

    us "Можно ещё разок?"
    me "Ну ладно. Один раз, и пойдём. Дядя Семён устал, он всю ночь по лесу бегал, он хочет ужинать!"

    scene cg d12_us_kiss_4:
        truecenter
        ease 1.5 zoom 1.2
    with dspr

    us "Хватит ныть. Иди сюда!"
    "Она с силой потянула меня за галстук, словно овчарку за поводок."
    th "Я создал чудовище…"
    th "То пусто, то густо. То прожил четверть века не целовавшись, то за одни сутки попробовал на вкус губы двух симпатичных девушек… или девочек? Не важно."

    window hide

    show blink

    $ renpy.pause(1.7, hard=True)

    scene cg d12_us_kiss_3
    show unblink
    with None

    window show

    "Отработав на мне технику ещё пару раз, Ульяна довольно улыбнулась."
    us "Ну всё… {w}Теперь-то он от меня не уйдёт. Семёныч, спасибо!"
    me "Вроде хорошо получилось. Ему понравится. Нужны будут уроки – обращайся."
    us "Не-не! Дальше мы сами! Кстати, теперь у меня есть чем тебя шантажировать! Имей это в виду!"

    stop music fadeout 5

    scene bg int_shed_bkrr_v1 with dissolve

    "Она быстро поцеловала меня в щёку и выскочила из сарайчика."

    stop ambience fadeout 0.5

    scene bg ext_path_sunset with dissolve

    $ bkrr_set_time("sunset")

    play ambience ambience_forest_evening fadein 3

    "Я вышел следом."
    "… И, конечно же, мимо шла Славя. Она проводила взглядом Ульяну и с лёгким удивлением посмотрела на меня."

    show sl surprise pioneer at center with dissolve

    sl "Семён? А что это Ульяна так выскочила? И что вы там делали?"
    me "Что делали, что делали. {w}В доктора играли!"

    show sl normal pioneer at center with dspr

    sl "Придумаешь тоже. Признавайся, сгущёнки хотели?"
    me "Ну…"
    "Я замялся."
    "До появления этой шутки оставалось ещё добрых тридцать лет, так что Славя имела в виду именно то, что имела."
    "Под стенкой стояло несколько ящиков с консервами. Я-то ещё думал, что это под нами железно постукивало. {w}Сгущённое молоко я люблю, так что, если бы знал, то непременно «одолжил» бы пару банок."
    me "Угадала. Улька, вон, за мешком побежала."

    show sl smile pioneer at center with dspr

    "Славя улыбнулась и погрозила мне пальцем."
    sl "Дай-ка я его запру от греха подальше! Чего он вообще открытый стоял? Хм…"

    window hide

    hide sl with dissolve

    $ renpy.pause(0.5, hard=True)

    play sound sfx_unlock_medpunkt_door

    $ renpy.pause(3.0, hard=True)

    show sl normal pioneer at center with dissolve

    window show

    "Славя заперла склад и повернулась ко мне."
    sl "Вот. Так-то лучше. Ты в столовую?"
    me "Да, что-то проголодался."

    show sl tender pioneer at center with dspr

    sl "Пойдём, ужин уже скоро начнётся."

    window hide

    stop ambience fadeout 3

    scene bg int_dining_hall_people_sunset_bkrr with fade3

    play ambience ambience_dining_hall_full fadein 3

    window show

    "Девчонки по традиции оккупировали один стол у стены, я же, чтобы не толкаться четвёртым лишним, присел с кибернетиками."

    show chair_r behind el
    show chair_l behind sh
    show el normal pioneer at bkrr_sit_right
    show sh normal pioneer at bkrr_sit_left
    with dissolve

    el "Привет!"
    sh "Привет! Семён, а ты рацию не потерял?"
    me "Нет, в клубе лежит. Вас-то не было…"

    show sh normal_smile pioneer at bkrr_sit_left

    sh "Вечером занесёшь, ладно? {w}Ну, как тебе? С радиосвязью-то?"
    "Шурик поправил очки."
    me "Очень удобно!"

    show sh upset pioneer at bkrr_sit_left

    sh "Слушай, тут с рубашкой твоей ерунда вышла. Представляешь, украли! Я на складе завтра новую попрошу, мне за помощь с электричеством сказали: «Проси, что хочешь!»."
    "Я старательно изобразил удивление."
    me "Украли? Бывает же. Я пока эту постираю, а там – как получится."
    sh "Прости, сам не знаю, как вышло."
    th "Я-то знал, как вышло, но зачем его зря волновать? Девчонки обещали помалкивать, а ему знать не обязательно."

    window hide

    scene bg int_dining_hall_people_sunset_bkrr with dissolve

    window show

    "В промежутках между поглощением ужина мы обсудили, как компактные средства связи преобразят мир. Сергей отнёсся скептически, упирая на то, что перенасыщенность эфира радиосигналами будет создавать хаос, и вообще, это никому не нужно."
    "Шурик же был уверен, что всё это технически преодолимо, и персональные радиостанции качественно изменят жизнь и быт."
    "Я подумывал, а не показать ли ему мобильник, но подавил это желание. {w}Ещё отберёт для изучения, увидит иностранные детали, вопросов не оберёшься."
    "Знали бы они, что в корпусе размером с записную книжку будут помещаться часы, фотоаппарат, диктофон, радиоприёмник, навигатор и ещё куча второстепенного, но необходимого барахла… {w}вплоть до компьютера, который в десятки раз мощнее того, что у них."
    "И что вместо научных подвигов всё это служит для бессмысленного трёпа о походах в клуб, о новой косметике или обсуждений, кто, кого и в какой позе."

    window hide

    stop ambience fadeout 3

    scene bg ext_dining_hall_near_sunset with fade3

    play ambience ambience_camp_center_evening fadein 3

    window show

    "Поужинав, я стал прикидывать, чем заняться дальше."
    th "Сейчас найду Мику и…"

    play music music_list["gentle_predator"] fadein 3

    show dv laugh pioneer2 close at left
    show mi grin pioneer close at center
    show us grin pioneer close at right
    with easeinbottom

    dv "ВОТ ОН!!! Хватайте, не дайте уйти!"
    "Алиса, Мику и Ульяна окружили меня кольцом, взявшись за руки, словно в игре… {w}Как там её? «Метеор», «Зарница»… {w}Не помню."

    show mi laugh pioneer close at center with dspr

    "Мику довольно рассмеялась."
    mi "Попался!"
    me "Да я и не убегал. А зачем вы меня поймать-то хотели?"

    show dv grin pioneer2 close at left with dspr

    dv "У нас вечером собрание клуба! Явка добровольная, но принудительная. А у тебя талант исчезать в самый неподходящий момент."

    window hide

    stop music fadeout 3

    stop ambience fadeout 3

    scene bg int_music_club_mattresses_sunset with fade3

    play ambience bkrr_ambience_list["indoors_evening"] fadein 3

    play music music_list["so_good_to_be_careless"] fadein 5

    window show

    "Собрание заключалось в том, что мы пили чай, заедали всё не кончающимся печеньем и обсуждали организационные вопросы вроде того, как уговорить Шурика наладить капризный микшерный пульт."
    "Алиса встала и решительно рассекла воздух ладонью."

    show dv normal pioneer2 far at cleft with dissolve

    dv "Мы все забыли об одной важной вещи!"

    show mi serious pioneer close at cright with easeinright

    "Мику с интересом посмотрела на неё."
    mi "О какой?"
    dv "Как называется наша группа?"

    show mi upset pioneer close at cright with dspr

    mi "Я даже не знаю… {w}А что, обязательно надо называть?"

    show dv normal pioneer2 far at cleft with dspr

    dv "Обязательно надо!"
    me "Даже на один концерт?"

    show dv grin pioneer2 far at cleft with dspr

    dv "Семён, ты не понимаешь. Даже на один! Давайте любые идеи!"

    window hide

    $ bkrr_timeskip_short()

    scene bg int_music_club_mattresses_sunset with bkrr_timeskip_transition()

    window show

    "За следующие полчаса мы успели перебрать и забраковать с десяток вариантов: «Рыжая кошка», «Костёр», «Молния», «Алые паруса», и даже «ВИА \"Красные Гитары\"»."
    "Всегда находился кто-то недовольный. {w}Я всё больше помалкивал, зато девчонки готовы были до хрипоты спорить, даже Мику с азартом отстаивала свои варианты и критиковала чужие."
    "Наконец, уморившись, мы решили снова решить дело жребием. {w}Снова бумажки, ваза и Ульяна, готовящаяся тянуть билетик."
    "Я быстро черканул «K-ON» и усмехнулся."
    th "Даже если шутку никто, кроме тебя, не понимает, всё равно весело."

    stop music fadeout 5

    "Мику положила свою бумажку в вазу и тихо шепнула мне на ухо:"

    show mi smile pioneer close at cright with dissolve

    mi "А что ты написал?"
    me "Не скажу. Сюрприз!"
    th "… Интересно, сейчас это сокращение уже в ходу? Всё-таки двадцать лет разницы, может, его ещё не используют?"

    show mi upset pioneer close at cright with dspr

    mi "Ты поосторожнее с сюрпризами. А вдруг вытащат? {w}И будем мы называться «Букет зябликов»."

    show mi normal pioneer close at cright with dspr

    mi "Ты представляешь себе лицо Ольги Дмитриевны, когда она будет объявлять наше выступление? После такого нас точно посадят под замок до конца смены."
    me "Если меня посадят вместе с тобой, то я готов."

    show mi smile pioneer close at cright with dspr

    "Мику улыбнулась и прижалась к моему плечу."
    mi "Я тоже! Даже если посадят в разные комнаты, мы выкопаем подземный ход, как в «Графе Монте-Кристо», и будем ходить друг к другу в гости."

    hide mi with dissolve

    "Алиса и Ульяна сложили свои бумажки в вазу."

    show us laugh2 pioneer at cleft with dissolve

    us "Отлично! А теперь я вытягиваю…"

    show dv angry pioneer2 at cright with dissolve

    "Алиса перехватила её руку и подозрительно нахмурилась"
    dv "А почему это ты тянешь? Смухлевать хочешь?"
    us "А больше никто не сможет. Ты ведь сама эту вазу выбрала?"
    dv "Ну?"
    us "Сунь руку."

    window hide

    show dv normal pioneer2 at cright with dspr

    $ renpy.pause(1.0, hard=True)

    show dv guilty pioneer2 at cright with dspr

    show us grin pioneer at cleft with dspr

    window show

    "Алиса попробовала, но её ладонь не проходила в горлышко. Ульяна показала ей язык."
    us "То-то же. А называться мы будем…"
    "На её ладони виднелись две слипшиеся бумажки."

    show us normal pioneer at cleft with dspr

    us "Ой! Видно, от сладкого склеились. Смотри, Алиска, твоя и моя."

    play music music_list["you_won_t_let_me_down"] fadein 5

    us "По-хорошему не вышло."

    show dv angry pioneer2 at cright with dspr

    dv "Тогда придётся по-плохому."

    show us evsmile pioneer at cleft with dspr

    "Алиса помрачнела, встала и с хрустом размяла костяшки. Ульяна пружинисто поднялась и встала напротив."
    us "Значит, решим между собой? Как обычно."

    show dv rage pioneer2 at cright with dspr

    dv "Да, рыжая. Только ты и я."
    us "Ну, раз так… Делать нечего."

    window hide

    hide dv
    hide us
    with dissolve

    $ renpy.pause(1.0, hard=True)

    window show

    "Ульяна сделала несколько быстрых выпадов, словно боксёр перед боем. Двигалась она нервно, порывисто."
    "Алиса, наоборот, стояла неподвижно, спокойно сжимала и разжимала кулаки, держа их на уровне лица. {w}Галстук туго обматывал правое запястье, наверное, чтоб не выбить."
    "Я обалдело переводил взгляд с одной пионерки на другую."
    th "Они что, взаправду?"
    "Ульяна негромко бросила:"

    show us smile pioneer at cleft
    show dv angry pioneer2 at cright
    with dissolve

    us "Алиса, у тебя нога… Может, сдашься сама?"
    dv "Она мне не помешает. Не сейчас."

    show us calml pioneer at cleft with dspr

    us "Как знаешь. Не ной потом, что нога болела, и только поэтому ты проиграла."

    show dv rage pioneer2 at cright with dspr

    dv "Посмотрим, кто будет ныть."
    us "Не дави на меня!"

    show us dontlike pioneer at cleft with vpunch

    "Ульяна возмущённо топнула."
    us "Я только начинаю."

    show dv grin pioneer2 at cright with dspr

    "Алиса повела плечами, разогреваясь."
    dv "Что, нервишки шалят?"
    "Я решил, что пора вмешаться."
    me "Эй, девчата, вы чего?"
    th "Ещё драки не хватало."

    window hide

    hide dv
    hide us
    with dissolve

    show mi smile pioneer close at cright with dissolve

    window show

    "Мику покачала головой, потянула меня за рукав, чтобы я сел назад."
    mi "Ой, что сейчас начнётся! Сама же их и научила. Теперь любой спор так решают. Лишь бы не сломали ничего. Скакать ведь начнут, по сторонам не смотрят."
    me "Нужно их остановить!"

    hide mi with dissolve

    "Я попытался встать между ними, но рыжие просто отошли, не сводя друг с друга напряжённые взгляды."
    "Алиса, не оглядываясь, коротко бросила:"

    show us calml pioneer far at cleft
    show dv angry pioneer2 far at cright
    with dissolve

    dv "Семён, полезешь под руку – зашибу."
    us "А я добавлю!"
    dv "Мику, командуй!"

    "Я почти услышал потрескивание разрядов в воздухе."
    th "Интересно, кто кого?"
    "Ульяна мелкая, но быстрая, а Алиса не может быстро двигаться из-за ноги…"
    th "Может, если брошусь между ними, то остановятся? Вряд ли. Но нужно попытаться."
    th "Драться из-за такой ерунды… {w}Это же глупо."

    stop music fadeout 3

    stop ambience fadeout 3

    "Мику вздохнула, резко выдохнула: «Начали!», – взмахнула рукой и отскочила на пару шагов назад. {w}Она взяла меня за руку, не давая подойти к рыжим."

    window hide

    show blink

    $ renpy.pause(1.5, hard=True)

    $ bkrr_set_volume("sound", 0.3, 0.0)

    play music music_list["doomed_to_be_defeated"] fadein 1.5

    play sound sfx_nightmare_explosion

    play sound2 sfx_nightmare_underground_rumble

    scene cg d12_fight with bkrr_fade(1.0)

    $ renpy.pause(5.0, hard=True)

    window show

    "Быстрым, неуловимым движением девчонки выбросили вперёд руки. Сейчас раздастся отвратительный звук ударов по живому… {w}Но вместо этого зазвучали синхронные возгласы."

    window hide

    play sound3 bkrr_sfx_list["metalclang"]
    show bkrr_service "Камень!" at truecenter with vpunch
    $ renpy.pause(0.5, hard=True)
    play sound3 bkrr_sfx_list["metalclang"]
    show bkrr_service "Ножницы!":
        truecenter
        zoom 1.25
    with vpunch
    $ renpy.pause(0.5, hard=True)
    play sound3 bkrr_sfx_list["metalclang"]
    show bkrr_service "Бумага!":
        truecenter
        zoom 1.5
    with vpunch
    $ renpy.pause(0.5, hard=True)

    window hide

    stop music fadeout 5

    $ bkrr_set_volume("sound", 1.0, 0.0)

    scene bg int_music_club_mattresses_sunset  with bkrr_fade(1.0)

    play ambience bkrr_ambience_list["indoors_evening"] fadein 3

    window show

    "Алиса засмеялась, помахала рукой с «ножницами». Ульяна, выбросившая открытую ладонь, насупилась."

    show us dontlike pioneer at cleft
    show dv laugh pioneer2 at cright
    with dissolve

    us "Нечестно! Давай два из трёх! Ты мухлевала!"

    show dv grin pioneer2 at cright with dspr

    dv "Вилять начинаешь? Ну, давай переиграем! Иногда и черепахи летают, только низко и недалеко!"

    hide us
    hide dv
    with dissolve

    play music music_list["silhouette_in_sunset"] fadein 5

    "То ли Ульяне сегодня не везло, то ли ещё почему, но Алиса разгромила её и в «два из трёх», и в «три из пяти», и даже «кто первый десять наберёт»."
    "Наконец, они вернулись к столу. Мику с умилением наблюдала за ними."
    "Я нервно рассмеялся и махнул рукой."
    me "Ну вас! Я думал, вы драться будете."

    show us normal pioneer at cleft
    show dv angry pioneer2 at cright
    with dissolve

    dv "Ты что, дурак? Мы же девочки, а девочки не дерутся! Не хватало ещё носы разбить перед концертом."
    "Алиса покрутила пальцем у виска."
    me "Просто вы так себя вели…"

    show us smile pioneer at cleft with dspr

    us "Обычно мы проще всё делаем, но решили устроить для тебя представление. Ты так трогательно пытался нас разнять… {w}Даже приятно!"
    me "Смешно вам. Волнуюсь за вас, а вы тут."

    show us smile pioneer close at cleft
    show dv smile pioneer2 close at cright
    with dissolve

    "Алиса и Ульяна подошли и одновременно обняли меня с двух сторон."
    dv "Мы ценим!"

    show us laugh2 pioneer close at cleft with dspr

    us "Но ты такой доверчивый… до сих пор."
    "Мику тихо засмеялась и погладила меня по голове."
    me "Ладно, ладно. Я доверчивый. Так как мы будем называться-то?"
    "Алиса развернула бумажку и довольно зачитала:"

    show dv normal pioneer2 close at cright with dspr

    dv "Теперь мы все – участники коллектива музыкальной самодеятельности «СОВЁНОК»."

    show us upset pioneer close at cleft with dspr

    "Ульяна пренебрежительно фыркнула."
    us "Очень оригинально. Потрясающе! Долго сочиняла? Ночей не спала?"
    dv "Зато вожатые не забракуют. И вообще, мне – нравится!"

    show us sad pioneer close at cleft with dspr

    us "А мне вот – не очень!"
    dv "Горе проигравшим!"

    hide us
    hide dv
    with dissolve

    "Мику подлила нам ещё чая и поинтересовалась:"

    show mi dontlike pioneer at center with dissolve

    mi "Музыкальный клуб, мы сегодня репетировать будем или чаи распивать до самого заката? Если репетировать, то самое время начинать, потому что Семён в такт не всегда попадает, а Ульяна…"

    window hide

    stop music fadeout 10

    stop ambience fadeout 3

    $ bkrr_timeskip()

    scene bg ext_music_club_verandah_night_v2 with bkrr_circleout_transition

    $ bkrr_set_time("night")

    play ambience ambience_camp_center_night fadein 3

    window show

    "Когда мы с Мику вышли из клуба, солнце уже скрылось за верхушками сосен."

    show mi normal pioneer close at center with dissolve

    window show

    mi "Ну и денёк. Зато будет, что дома рассказать."

    show mi smile pioneer close at center with dspr

    mi "Папа не поверит, скажет, что у меня бурная фантазия. А мама, конечно, поверит и будет говорить, что воспитанные девочки не убегают в лес, не теряются там и не заставляют старших волноваться."
    th "И не ночуют на одном диване с пришельцами из будущего."
    "Мику улыбнулась, наверное, вспоминая наши приключения, потом вздохнула."

    show mi normal pioneer close at center with dspr

    mi "Целый день проспала, и всё равно хочется. Пойдём отдыхать?"
    me "Я тебя провожу."

    show mi happy pioneer close:
        center
        ease 0.5 zoom 1.2
    with dspr

    mi "Конечно! А то там темно и страшно!"
    "Мику изобразила испуг и взяла меня под руку. Алиса понимающе улыбнулась нам."

    show dv normal pioneer2 at fleft behind mi
    show us smile pioneer at left behind mi
    with dissolve

    dv "Доброй ночи, что ли. Семён, присмотри за Мику. И веди себя хорошо, а то я тебе!"

    show mi smile pioneer close:
        center
        zoom 1.2
    with dspr

    me "Я постараюсь."

    show us laugh pioneer at left with dspr

    us "Сенька, только не {b}слишком{/b} хорошо!"

    window hide

    hide dv
    hide us
    with dissolve

    stop ambience fadeout 3

    scene bg ext_path2_night with fade3

    play ambience ambience_forest_night fadein 3

    window show

    "Алиса с Ульяной двинулись по аллее, ведущей в сторону площади, мы же пошли короткой дорогой, через лесок. {w}Земля подсохла, и сейчас там можно было спокойно пройти, не налепив себе на обувь по три кило грязи."
    "Мы столько времени проводим вместе, но мне всё мало. Хочется постоянно быть рядом с Мику и не отходить от неё ни на шаг. {w}Странное ощущение. Но… такое приятное. Я очень к ней привязался."
    me "Помнишь это место?"
    "Я показал на ничем не примечательный участок тропинки под высокой сосной."

    show mi upset pioneer close at center with dissolve

    mi "Ой, что-то с памятью моей стало!"

    show mi happy pioneer close at center with dspr

    mi "Совсем забыла. Нужно освежить!"

    window hide

    scene cg d9_kiss with dissolve

    play music bkrr_music_list["promise"] fadein 7.5

    "Я мягко привлёк её к себе и поцеловал."

    scene bg ext_path2_night
    show mi smile pioneer close at center
    with dissolve

    me "А теперь?"
    "Мику смотрела на меня и улыбалась. На щеках у неё играл лёгкий румянец, а в глазах сверкали озорные искорки. {w}А может, отражались звёзды? {w}Почему я теряю голову каждый раз, когда она так на меня смотрит?"
    mi "Теперь вспомнила!"

    window hide

    hide mi with dissolve

    $ renpy.pause(1.0, hard=True)

    scene cg d12_fireflies
    show bkrr_eff_fireflies:
        alpha 0.0
        ease 5.0 alpha 1.0
    with dissolve

    $ renpy.pause(1.0, hard=True)

    window show

    "Мы вышли из-под деревьев на открытое место."
    "Мику показала на небо, держа меня за руку."
    mi "Ой, смотри… Какая красота!"
    "Прямо из травы вверх медленно поднимались крошечные зеленоватые звёздочки. {w}Сотни? Тысячи? {w}Не знаю."
    "Они летали вокруг, расчерчивая вечернее небо светящимися узорами, не обращая внимания на парочку пионеров, которые стояли внизу и, затаив дыхание от восхищения, любовались их полётом."
    "Я наклонился и осторожно снял один огонёк с травинки."
    me "Никогда раньше не видел светлячков. Вот они какие. Красиво-то как!"
    "Мику согласно кивнула."
    mi "Знаешь, когда мы жили в Японии, наш дом стоял у самой реки. И там было очень много светлячков. Летом мы с друзьями часто ходили на старый мост и смотрели на их полёт."
    mi "Когда я была совсем маленькая, мама мне рассказывала, что светлячки питаются нашей любовью, и чем больше их возле дома, тем счастливее те, кто в нём живут. А если люди ссорятся и обижают друг друга, то светлячки умирают."
    mi "Наверное, это смешно звучит, да? Я понимаю, что это сказка, но она мне очень нравится."
    me "А по-моему, красивая сказка! Значит, это хорошо, что их в лагере так много!"
    "Светлячок взлетел с моей руки и присоединился к огонькам, кружащим в небе."
    "Мику проводила его взглядом и вздохнула."
    mi "Знаешь, я всегда хотела посмотреть на полёт светлячков с тем, кого… кто мне нравится. У нас это считается хорошей приметой."
    "Вместо ответа я обнял её, и мы стояли, любуясь крошечными огоньками, утратив счёт времени."

    window hide

    $ renpy.pause(2.5, hard=True)

    stop ambience fadeout 3

    $ bkrr_timeskip(False, False)

    scene bg ext_path2_night with bkrr_circleout_transition

    play ambience ambience_forest_night fadein 3

    stop music fadeout 15

    window show

    "Сигнал на отбой прервал нашу идиллию. Мику вздохнула и взъерошила мне волосы."

    show mi normal pioneer close at center with dissolve

    mi "Пойдём? А то Ольга Дмитриевна тебя заругает."
    me "Она уже привыкла. Я неисправимый нарушитель режима. Но ты права, лучше пойдём. {w}Кроме милых светлячков, тут ещё есть злобные комары, они кушают не любовь, а неосторожных пионеров. Не хочу, чтобы они тебя искусали."

    show mi smile pioneer close at center with dspr

    "Мику улыбнулась и снова взяла меня под руку."
    mi "Идём!"

    window hide

    stop ambience fadeout 3

    scene bg ext_square_night with fade3

    play ambience ambience_camp_center_night fadein 3

    window show

    me "Увидимся завтра!"

    show mi normal pioneer close at center with dissolve

    mi "Обязательно увидимся. Если только я опять где-нибудь не заблужусь."

    show mi smile pioneer close at center with dspr

    "Она тихо засмеялась."
    me "Если заблудишься, то я всё равно тебя найду."

    show mi dontlike pioneer close at center with dspr

    mi "Обещаешь?"
    me "Обещаю!"

    window hide

    show mi smile pioneer close at center with dspr

    $ renpy.pause(1.0, hard=True)

    hide mi with dissolve

    $ renpy.pause(1.0, hard=True)

    scene bg ext_houses_night_bkrr with fade

    window show

    "Я поцеловал Мику на прощание, сошёл с аллеи на неосвещённую дорожку за домиками и отправился к себе. На душе было необыкновенно легко и хорошо."

    window hide

    stop ambience fadeout 3

    scene bg int_house_of_mt_night with fade3

    play ambience ambience_int_cabin_night fadein 3

    window show

    "Ольга в спортивном костюме лежала на кровати и читала какой-то журнал. Увидев меня, она демонстративно взглянула на часы."

    show mt grin bkrr_sport at center with dissolve

    mt "Вот и пропажа пришла! Ну, как погуляли?"
    me "С чего вы взяли? Может, я репетировал в поте лица!"

    show mt smile bkrr_sport at center with dspr

    mt "После репетиции так не улыбаются. Кто-то не теряет времени зря, да?"
    "Я смутился и поспешил сменить тему."
    me "Ольга Дмитриевна, можно вопрос?"

    show mt normal bkrr_sport at center with dspr

    mt "Умный?"
    me "Не знаю."
    mt "Попробуй. Только один! Я прошлую ночь не спала, глаза закрываются."
    me "Если я захочу выйти за ворота, что будет? Я смогу уйти? Как вчера, в лес?"

    show mt surprise bkrr_sport at center with dspr

    "Вожатая странно посмотрела на меня, потом просто ответила:"
    mt "Да, сможешь. Дверь ведь не заперта, так, на проволочку закручена."

    show mt laugh bkrr_sport at center with dspr

    mt "А что, уже надоело? Сбежать собираешься?"
    me "Нет, конечно."

    show mt smile bkrr_sport at center with dspr

    mt "Вот то-то же. Я ведь говорила, что ты не захочешь отсюда уезжать."

    hide mt with dissolve

    "С этими словами она отложила журнал."

    window hide

    $ renpy.pause(1.0, hard=True)

    window show

    me "Что же это за место такое?"

    show mt laugh bkrr_sport at center with dissolve

    mt "Пионерский лагерь «Совёнок»."
    "Ольга рассмеялась и покачала головой."

    show mt grin bkrr_sport at center with dspr

    mt "Забыл уже?"
    me "Но…"

    show mt smile bkrr_sport at center with dspr

    mt "Мы договорились: один вопрос. {w}Завтра, всё завтра. Выйди, пожалуйста, я переоденусь!"

    window hide

    stop ambience fadeout 0.5

    scene bg ext_house_of_mt_night with dissolve

    play ambience ambience_camp_center_night fadein 3

    window show

    "Я вздохнул, вышел на крыльцо и сел на тёплые доски."
    "Через пару минут я поймал себя на том, что пытаюсь разглядеть в темноте окна домика Мику."
    th "«… не захочешь». Я уже не хочу!"

    window hide

    $ persistent.bkrr_check[13] = True

    jump bkrr_day13_start
