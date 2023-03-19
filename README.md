# Zeenode Селфбот


# T.O.S
#### Этот репозиторий / проект находится под лицензией MIT, если вы его используете, пожалуйста, оставьте водяной знак организации (github.com/zeenode). Я оставил, этот проект будет как русский Zeenode, под русскую аудиторию

## Портфолио селфбота 
###### https://zeenode.github.io/selfbot-site/

### Об этом проекте

- Этот проект в основном создан для людей, которые хотят понять discord.py, чтобы они могли развивать свои навыки программирования в ее использовании. Discord запрещает селфботы, поэтому, если вы хотите использовать это, вы будете использовать это на свой страх и риск.

# Предупреждение

- Вы соглашаетесь не (и не пытаться) использовать Сервис для любых целей, кроме тех, которые прямо разрешены настоящими Условиями; копировать, адаптировать, модифицировать, готовить производные работы на основе, распространять, лицензировать, продавать, передавать, публично демонстрировать, публично исполнять, передавать, транслировать в потоковом режиме, пытаться обнаружить любой исходный код, реконструировать, декомпилировать, дизассемблировать или иным образом использовать Сервис или любую часть Сервиса, за исключением случаев, прямо разрешенных настоящими Условиями; или использовать интеллектуальный анализ данных, роботов, пауков или аналогичные инструменты сбора и извлечения данных на службе.

- - Вкратце это означает, что Discord запрещает любую форму ботов и автоматизации, что означает, что selfbot запрещен ToS. Это только в образовательных целях, если вы хотите его использовать, используйте на свой страх и риск. Мы не несем за вас никакой ответственности.


## Как установить и использовать селфбота?
- Windows:
    1. Скачайте python, предпочтительно версию 3.7.0. Вот ссылка на скачивание питона - https://www.python.org/downloads/release/python-370/. 
    2. Git клонирует репозитории. Вы можете склонировать репозиторий, введя в командной строке "git clone https://github.com/zeenode-ru/selfbot-on-ru" (Вам понадобится git, который вы можете скачать с https://git-scm.com/download/win)
    3. Запустите install.bat, затем запустите.bat и введите свой токен. Вам нужно будет делать это каждый раз, когда вы запускаете селфбота. Что бы каждый раз не вставлять токен в CMD вы можете вставить свой токен в "config.py".
- GNU/Linux:
    1. Скачайте python, предпочтительно версию 3.7.0. Вот ссылка на скачивание питона - https://www.python.org/downloads/release/python-370 / и установите исходный файл tarball. (Обратите внимание, что вам нужно будет создать python из исходного кода. В качестве альтернативы вы можете загрузить его с терминала, используя менеджер пакетов вашего дистрибутива, хотя это будет самая новая версия, а не 3.7.0)
    2. Git клонирует репозитории. Вы можете склонировать наш репозиторий, введя в своем терминале "git clone https://github.com/zeenode-ru/selfbot-on-ru" (Для этого вам понадобится git, который вы можете загрузить с терминала, используя менеджер пакетов вашего дистрибутива.)
    3. Запустите файл launch.py и введите свой токен. Вам нужно будет делать это каждый раз, когда вы запускаете selfbot. Что бы каждый раз не вставлять токен в CMD вы можете вставить свой токен в "config.py".
    



## Commands / How to use?
###### Type (prefix)help (ex. $help) to see list of categories !
###### Type (prefix)help (category) (ex. $help textencoding) to see list of commands in category !





<!---

## Commands

## You can see this by typing (prefix)help in any discord channel.



### Activity:

$**listening** *(text)* - Shows listening status.       

$**playing** *(text)* - Shows playing status. 

$**stopactivity** - Stops activity.

$**streaming** *(text)* - Shows streaming status.

$**watching** *(text)* - Shows watching status. 





### Fun:



$**cat** - Sends a cute cat image.

$**dog** - Sends a cute dog image.

$**dick** *@user* - Shows user dick size.                                                                                

$**hug** *@user* - Sends a hug to user.

$**kiss** *@user* - Sends a kiss to user.                                                                            

$**meme** - Sends a meme.         

$**nitro** - Sends a nitro.                                                                                           

$**slap** *@user* - Sends a slap to user.                                                                                 
                                                       

### Main:

$**ascii** *(message)* - Sends message as ascii art.    

$**av** - Sends your avatar in the chat.            

$**embed** *(message)* - Sends embed message.   

$**guildicon** - Shows server(guild) icon.     

$**hypesquad** *(badge)* - Changes your hypesquad badge.                                                                  

$**purge** *(number of messages)* - Deletes messages.      

$**serverinfo** - Shows server info.

$**suggest** *Question* - Sends question with embed leaving thumbsup & thumbsdown sign.

$**whois** *Tag(User)* - Sends info about user.

$**geoip** *ip* - Looks up geoip data of an IP address provided.
                                                                        




### Currency:

$**btc** - Shows Bitcoin Price.

$**doge** - Shows Doge price.

$**eth** - Shows Ethereum price.

$**XMR** - Shows Monero price.

$**xrp** - Shows Ripple Price.


###### Notice: More values will be added soon!








### Emoticons:

#### $**listemoticons** - Lists all the cool emoticons you can send because there are too many to list on this README file.


### Text Encoding:

$**encode_base64** *(word/message)* - Encodes text with Base64.                                                                  

$**encode_leet** *(word/message)* - Encodes text with leet speak (if you don't know what is leet it is basicly hacker language).

$**encode_md5** *(word/message)* - Encodes text with MD5 hash.   


$**encode_sha1** *(word/message)* - Encodes text with Sha1.

$**encode_sha224** *(word/message)* - Encodes text wish SHA224.

$**encode_sha384** *(word/message)* - Encodes text with Sha384.

$**Encode_sha212** *(word/message)* - Encodes text with Sha512.



### Mass:

$**massreact** *:(emoji):* - Reacts to last 20 messages with emojis.

$**spam** *number* *message* - Spams message number of times.


### Nsfw:


$**anal** *(User tag)* - Sends nsfw anime content.

$**blowjob** *(User Tag)* - Sends nsfw anime content.

$**boobs** *(User Tag)* - Sends nsfw anime content.

$**hentai** *(User Tag)* - Sends hentai. ( Anime porn )

## End of commands.


-->

## Notice:

### Activity Status like:
- $watching, $listening or $playing won't work if you actually have already an activity! 
- Only $streaming will work!

- To Get help with commands type (prefix)"$help main" and from there you can use $help and the name of category.
- Command zoki makes no sense. It is added because today is my good friend's "eqxm" aka. zoki birthday.

# Disclaimer:

#### For educational purposes only, (Github Organisation) Zeenode is not resposible for whatever you do with this.
