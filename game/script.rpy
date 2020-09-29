define m = Character(_("我"), color="#2467b7")
define b = Character(_(""), color="#ec9324")
define x = Character(_("欣欣"), color="#ff6e6d")
define c = Character(_("水晶土豆"), color="#d33682")
define p = Character(_("Padme"), color="#da70d7")


define fadehold = Fade(2.0, 0.2, 1.5)
define dissolvehold = Dissolve(1.5, alpha=True, time_warp=None)

define hack = False
define berliner = False
define rebellion = False
define tattletale = False


label start:
    scene bg intro
    with dissolvehold

    "{cps=15}要在此互动式小说中操作，请使用空格或鼠标左键来前进，点击下方菜单的回退按钮来回退。{/cps}"
    "{cps=15}提示：\n按 F11 可以进入全屏。\n点击下方的“自动”按钮来自动前进。{/cps}"
    "{cps=15}接下来的画面将会有声音，请检查你的音量。{/cps}"
        

label wakeup:
    play music "Dreamland - Aakash Gandhi.mp3"
    scene bg sunshine table
    with fadehold


    "{cps=10}这是一个秋日温暖的午后{/cps}"
    "{cps=10}你刚刚从一个长长的午睡中醒来{/cps}"


    scene bg sunshine room blured
    with fadehold

    "{cps=10}在一个大大的哈欠后，你睁开了眼睛，发现周围熟悉的一切似乎有哪里不太一样……{/cps}"


    scene bg sunshine room
    with dissolvehold

    "{cps=10}房间里的一切……变回了很多年前的样子……{/cps}"


    scene bg window
    with dissolvehold

    "{cps=15}你看向了窗外，小声自言自语到：{/cps}{cps=10}“这不会是一个{b}梦{/b}吧”{/cps}"

    menu wakeupchoice:
        "{cps=10}现在做些什么？{/cps}"
        "在家里转一转":
            jump wander
        "再睡一会，看看会不会醒来":
            "{cps=10}你再一次趴到了桌子上，闭上了眼睛……{/cps}"
            jump wakeup
        

label wander:
    menu wheretogo:
        "{cps=10}现在去哪个房间呢？{/cps}"
        "厨房":
            scene bg kitchen
            with fadehold
            "{cps=10}吃了一些{b}蜂蜜{/b}{/cps}"
            show honey at top
            with dissolve
            "{cps=10}太甜了！\n又喝了很多水{/cps}"
            # 添加 图片
            jump wander
        "卧室":
            scene bg bedroom off
            with fadehold
            "{cps=10}“这台家里新买的电脑我还没有用过……”{/cps}"
            menu opencomputer:
                "{cps=10}是否打开电脑？{\b}"
                "开机！":
                    jump startcomputer
                "一会吧……":
                    jump wander
        "客厅":
            scene bg livingroom
            with fadehold
            "{cps=10}收拾了一下房间，感觉不错{/cps}"
            jump wander
                    
    
label startcomputer:
    scene bg bedroom on
    with dissolvehold

    play sound "xp startup.mp3"
    scene bg xp
    with fadehold

    "{cps=10}咦？{/cps}"
    play sound "knock.mp3"
    "{cps=15}会是谁在敲门呢？{/cps}"
    "{cps=15}原来是好朋友{b}{color=#ff6e6d}欣欣{/color}{/b}！{/cps}"
    scene bg door
    with fadehold

    x "{cps=15}你也{b}上网冲浪{/b}啊！{/cps}"
    m "{cps=15}对啊，咱们一起上网吧！\n我可是上网冲浪的{b}高手{/b}！{/cps}"
    scene bg xp
    with fadehold
    x "{cps=15}咱们快打开{b}浏览器{/b}吧！{/cps}"
    "打开了{b}浏览器{/b}"
    show bg chrome
    jump browserchoice



label browserchoice:
    menu browserwhattodo:
        "{cps=10}现在做些什么？{/cps}"
        "打开你们最喜欢的明星的微博主页":
            "{cps=10}发现和上次一样，她更新了许多有趣的图片{/cps}"
            x "{cps=10}我好想看看她在自己的生活中而不是网络上是什么样子的啊！{/cps}"
            m "{cps=10}这还不简单，我们进到{b}她的邮箱{/b}里看看不就知道了？{/cps}"
            x "可是……\n{cps=10}这样不会……{/cps}{cps=15}犯法吗？{/cps}"

            menu hack:
                "{cps=10}你要怎么做？{/cps}"
                "没事，我可厉害了，没有人能发现我！":
                    $ hack = True
                    m "{cps=10}你看，只要发送一个{b}钓鱼邮件{/b}就行{/cps}"
                    x "{cps=10}好吧……{/cps}"
                    m "{cps=10}哈哈，她竟然打开了，小菜一碟！\n现在咱们要不要把这些照片发到网上？{/cps}"
                    x "{cps=10}还是别了，给别的同学看看就好了{/cps}"
                    m "{cps=10}你说的对，那样就太过分了{/cps}"
                    jump browserchoice
                "好像是这样啊……\n那还是算了吧，这样不好……":
                    $ hack = False
                    jump browserchoice
        "随便在前几天发现的论坛里找网友聊天":
            "有一个网友的帖子引起了你们的注意。\n{cps=15}{p=1.0}{i}大家快来{a=https://www.notion.so/47a4437b157549ed9075aed0be7bc8b0}{b}这个链接{/b}{/a}里看看 {image=hands.png} 在 ** 年的黑历史！{/i}{/cps}"
            "{cps=10}好奇心驱使这你们点击了这个链接……\n但是……{/cps}"
            scene bg blocked
            with fadehold
            m "{cps=10}**，{/cps}{cps=15}这个网站被屏蔽了！{/cps}{p=1.0}\n{cps=15}不过我们打开{b}代理{/b}就可以访问了!{/cps}"
            x "{cps=10}那咱们快看看吧！{/cps}"


            menu wronghistory:
                "{cps=10}你要怎么做？{/cps}"
                "嘿嘿马上就好！":
                    $ berliner = True
                    "{cps=10}你们看完了这个境外网站上的这篇文章，{s}久久不能自已{/s}{/cps}"
                    jump browserchoice
                "还是算了吧，咱们可是光荣的{color=#f00}共青团员{/color}，不应该看这些的！":
                    $ berliner = False
                    x "{cps=10}我也觉得是这样，我们还是看看别的吧！{/cps}"
                    jump browserchoice
        "关掉浏览器":
            x "{cps=10}咱们不上网了吗？{/cps}"
            menu emmm:
                "{cps=10}嗯……{/cps}"
                "咱们在 QQ 上找人聊天吧！":
                    jump qq
                "那咱们再看会吧":
                    jump browserchoice
                "关掉电脑":
                    jump no_more_screen_time


label qq:
    scene bg xp
    with fadehold

    show qq at top
    with dissolve

    "{b}蓝舟市群聊{/b} | 收到 17 条新消息{p=1.0}{b}点击立即查看{/b}"

    m "{cps=10}我又来聊天啦！最近有什么{b}大新闻{/b}吗？{/cps}"
    p "{cps=15}据说蓝舟市的一个工厂发生了病毒泄漏，感染了3000多人呢{/cps}！"
    m "{cps=15}啊？真的吗？{/cps}"
    c "{cps=15}对啊对啊，我也听说了！{/cps}"
    x "{cps=2}稍等一下……{/cps}{cps=10}我总感觉这些网友是在瞎说……{/cps}\n{cps=15}我记得爸爸说政府已经辟谣了！{/cps}"

    menu rumour:
        "{cps=10}你准备做些什么？{/cps}"
        "这么多人说肯定是真的，咱们{b}转发{/b}到微博和别的群里吧":
            $ rebellion = True
            "你将这个消息发到了微博和学校群里。{p=1.0}{cps=15}出大事了！蓝舟发生病毒泄露啦！{/cps}"
            jump no_more_screen_time
        "我觉得也是，既然{color=#f00}政府{/color}说了就肯定没发生过这种事！":
            menu v:
                "{cps=10}要如何处置这些造谣的人？{/cps}"
                "举报 Ta 们！":
                    $ tattletale = True
                    "你把这些网友举报给了网警！"
                    jump no_more_screen_time
                "{b}批判一番{/b}就算了":
                    m "{cps=15}你们这些人天天造谣有什么意思？我要参与到{color=#f00}科学发展观{/color}的建设中去了！{/cps}"
                    jump no_more_screen_time
                

label no_more_screen_time:
    x "{cps=15}今天上网冲浪真有意思啊！{/cps}"
    m "{cps=15}是啊，咱们去小公园的假山上玩吧！{/cps}"
    scene bg park
    with fadehold
    "{cps=10}时间过得很快{p=1.5}转眼就到了晚上{/cps}"
    scene bg bed
    with fadehold
    "{cps=10}你回到了家，很快就睡了过去……{/cps}"
    scene bg lzu
    with fadehold
    "{cps=10}{b}第二天{/b}醒来的时候……\n一切又回到了原来的样子……{/cps}"
    
    
label expose_and_criticize:
    scene bg brother
    with fadehold
    "{cps=15}现在到了回顾时间{/cps}"
    if hack:
        "{cps=15}你入侵了 ta 人的计算机系统……{/cps}"
        "{cps=15}你违反了《中华人民共和国网络安全法》第三十八条！{p=1.0}{size=30}任何{b}个人{/b}和组织不得窃取或者以其他非法方式获取公民个人信息，不得出售或者非法向他人提供公民个人信息。{/size}{/cps}"
        "{cps=15}还有第二十二条：{size=30}任何{b}个人{/b}和组织不得从事入侵他人网络、干扰他人网络正常功能、窃取网络数据等危害网络安全的活动；不得提供从事入侵网络、干扰网络正常功能、窃取网络数据等危害网络安全活动的工具和制作方法；不得为他人实施危害网络安全的活动提供技术支持、广告推广、支付结算等帮助。{/size}{/cps}"
    if not hack:
        "{cps=15}你没有入侵 ta 人的计算机系统"
        "{cps=15}你遵守了《中华人民共和国网络安全法》第三十八条：{p=1.0}{size=30}任何{b}个人{/b}和组织不得窃取或者以其他非法方式获取公民个人信息，不得出售或者非法向他人提供公民个人信息。{/size}{/cps}"
        "{cps=15}以及第二十二条：{size=30}任何{b}个人{/b}和组织不得从事入侵他人网络、干扰他人网络正常功能、窃取网络数据等危害网络安全的活动；不得提供从事入侵网络、干扰网络正常功能、窃取网络数据等危害网络安全活动的工具和制作方法；不得为他人实施危害网络安全的活动提供技术支持、广告推广、支付结算等帮助。{/size}{/cps}"


    if berliner:
        "{cps=15}你使用了非法信道进行国际联网……{/cps}"
        "{cps=15}你违反了《中华人民共和国计算机信息网络国际联网管理暂行规定实施办法》第七条!{p=1.0}{size=30}我国境内的计算机信息网络直接进行国际联网，必须使用邮电部国家公用电信网提供的国际出入口信道。任何单位和{b}个人{/b}不得自行建立或者使用其他信道进行国际联网。{/size}{/cps}"
        "{cps=15}考虑到“信道”的定义在立法和执行层面目前比较模糊，可以理解为是一个灰色地带。{/cps}"
    if not berliner:
        "{cps=15}你没有尝试使用非法信道进行国际联网{/cps}"
        "{cps=15}你遵守了《中华人民共和国计算机信息网络国际联网管理暂行规定实施办法》第七条：{p=1.0}{size=30}我国境内的计算机信息网络直接进行国际联网，必须使用邮电部国家公用电信网提供的国际出入口信道。任何单位和{b}个人{/b}不得自行建立或者使用其他信道进行国际联网。{/size}{/cps}"


    if rebellion:
        "{cps=15}你转发了没有得到政府证实的信息！{/cps}"
        "{cps=15}你违反了《中华人民共和国网络安全法》第九条！{p=1.0}{size=25}任何{b}个人{/b}和组织使用网络应当遵守宪法和法律，遵守公共秩序，尊重社会公德，不得危害网络安全，不得利用网络从事危害国家安全、宣扬恐怖主义和极端主义、宣扬民族仇恨和民族歧视、传播淫秽色情信息、侮辱诽谤他人、扰乱社会秩序、损害公共利益、侵害他人知识产权和其他合法权益等活动。{/size}{/cps}"
    if not rebellion:
        "{cps=15}你没有转发未得到政府证实的信息。"
        "{cps=15}你遵守了《中华人民共和国网络安全法》第九条：{p=1.0}{size=25}任何{b}个人{/b}和组织使用网络应当遵守宪法和法律，遵守公共秩序，尊重社会公德，不得危害网络安全，不得利用网络从事危害国家安全、宣扬恐怖主义和极端主义、宣扬民族仇恨和民族歧视、传播淫秽色情信息、侮辱诽谤他人、扰乱社会秩序、损害公共利益、侵害他人知识产权和其他合法权益等活动。{/size}{/cps}"
        if tattletale:
            "{cps=15}你将传播谣言的网友举报了。{/cps}"
            "{cps=15}你行使了《中华人民共和国网络安全法》第十条赋予你的权力：{p=1.0}{size=30}任何{b}个人{/b}和组织都有权对危害网络安全的行为向网信、工业和信息化、公安等部门举报。收到举报的部门应当及时依法作出处理；不属于本部门职责的，应当及时移送有权处理的部门。{/size}{/cps}"
        if not tattletale:
            "{cps=15}你没有举报传播谣言的网友。{/cps}"
            "{cps=15}下次你可以行使《中华人民共和国网络安全法》第十条赋予你的权力：{p=1.0}{size=30}任何{b}个人{/b}和组织都有权对危害网络安全的行为向网信、工业和信息化、公安等部门举报。收到举报的部门应当及时依法作出处理；不属于本部门职责的，应当及时移送有权处理的部门。{/size}{/cps}"
    
    "{cps=15}这基本上就是作为{b}个人{/b}能够遵守的《中华人民共和国网络安全法》的全部内容了！{/cps}"
    scene bg end
    with fadehold
    jump ever_after


label ever_after:
    menu wtf:
        "{cps=15}现在你想做些什么？{/cps}"
        "我还是不太明白这个{b}互动式小说{/b}的意义。":
            "{cps=15}这个小说会记录你对于一些个人在互联网上经常遇见的场景的反应，并根据你做出的不同决定来告诉你哪些行为可能会触犯《中华人民共和国网络安全法》。\n简单来说，这是一个普法作品。{/cps}"
            jump ever_after
        "等一下，我想要做一些更 exciting 的测试！":
            jump pill
        "我想结束这个故事。":
            jump bye
    
label pill:
    scene bg quiz
    with fadehold
    "{cps=15}欢迎来到这个测试！{p=1.0}{size=30}这个测试只有一道题，如果你无法通过就说明对大清的国情了解不够，不配上网 ;){p=1.0}注意，这个测试和现实没有任何关系，仅供娱乐。{/size}{/cps}"
    "题目：\n{cps=15}{size=30}有一天你发了一条关于如何制作煎蛋的微博：“第一步，洗净平底锅，第二步，打碎鸡蛋，第三步，加热油锅，第四步，把鸡蛋放进去”\n但是微博的审查系统告诉你因为违禁词无法发送，那么违禁词出现在第几步呢？{/size}{/cps}"
    menu winnie:
        "{cps=15}你的选择是？{/cps}"
        "我不会！":
            "{cps=15}真遗憾。\n正确答案是第一步。{/cps}"
        "第一步":
            show winnie at top
            with dissolve
            "{cps=10}恭喜你,答对了！{/cps}"
        "第二步":
            "{cps=15}真遗憾。\n正确答案是第一步！{/cps}"
        "第三步":
            "{cps=15}真遗憾。\n正确答案是第一步！{/cps}"
        "第四步":
            "{cps=15}真遗憾。\n正确答案是第一步！{/cps}"

label bye:
    "{cps=10}我们的故事到此结束了，谢谢:){/cps}"
    return
