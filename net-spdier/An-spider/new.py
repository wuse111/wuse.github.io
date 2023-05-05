# coding: utf-8
# Author：戏不能停啊
# Date ：2021/5/12 12:49
# Tool ：PyCharm
import requests
import re
from time import sleep
from lxml import etree
import pandas as pd
import random


def get_x(x):
    x1 = abs(float(x))
    the_x = x1 / 14 + 1
    return int(the_x)


def get_y(y):
    y2 = abs(float(y))
    the_y = y2 - 1 + 24
    return int(the_y)


def get_id():
    res = requests.get(
        'http://s3plus.meituan.net/v1/mss_0a06a471f9514fc79c981b5466f56b91/svgtextcss/e23815950ca036ee18984f5870ce397c.css')
    list1 = re.findall(r'\}\.(.*?)\{background:(.*?)px (.*?)px;', res.text)
    id_dict = {}
    for i in list1:
        id_dict[i[0]] = [i[1], i[2]]
    return id_dict

def get_ally():
    '''破解哪个带id的'''
    news ='<defs><path id="1" d="M0 44 H600"/><path id="2" d="M0 83 H600"/><path id="3" d="M0 123 H600"/><path id="4" d="M0 156 H600"/><path id="5" d="M0 198 H600"/><path id="6" d="M0 234 H600"/><path id="7" d="M0 269 H600"/><path id="8" d="M0 300 H600"/><path id="9" d="M0 333 H600"/><path id="10" d="M0 371 H600"/><path id="11" d="M0 402 H600"/><path id="12" d="M0 447 H600"/><path id="13" d="M0 495 H600"/><path id="14" d="M0 544 H600"/><path id="15" d="M0 590 H600"/><path id="16" d="M0 633 H600"/><path id="17" d="M0 682 H600"/><path id="18" d="M0 720 H600"/><path id="19" d="M0 769 H600"/><path id="20" d="M0 806 H600"/><path id="21" d="M0 856 H600"/><path id="22" d="M0 906 H600"/><path id="23" d="M0 940 H600"/><path id="24" d="M0 987 H600"/><path id="25" d="M0 1030 H600"/><path id="26" d="M0 1072 H600"/><path id="27" d="M0 1107 H600"/><path id="28" d="M0 1157 H600"/><path id="29" d="M0 1200 H600"/><path id="30" d="M0 1249 H600"/><path id="31" d="M0 1286 H600"/><path id="32" d="M0 1334 H600"/><path id="33" d="M0 1367 H600"/><path id="34" d="M0 1403 H600"/><path id="35" d="M0 1439 H600"/><path id="36" d="M0 1479 H600"/><path id="37" d="M0 1515 H600"/><path id="38" d="M0 1564 H600"/><path id="39" d="M0 1596 H600"/><path id="40" d="M0 1628 H600"/><path id="41" d="M0 1674 H600"/><path id="42" d="M0 1720 H600"/><path id="43" d="M0 1752 H600"/><path id="44" d="M0 1793 H600"/><path id="45" d="M0 1825 H600"/><path id="46" d="M0 1870 H600"/><path id="47" d="M0 1919 H600"/><path id="48" d="M0 1950 H600"/><path id="49" d="M0 1996 H600"/><path id="50" d="M0 2038 H600"/><path id="51" d="M0 2081 H600"/><path id="52" d="M0 2113 H600"/><path id="53" d="M0 2151 H600"/><path id="54" d="M0 2195 H600"/><path id="55" d="M0 2229 H600"/><path id="56" d="M0 2275 H600"/><path id="57" d="M0 2310 H600"/><path id="58" d="M0 2348 H600"/><path id="59" d="M0 2384 H600"/><path id="60" d="M0 2434 H600"/><path id="61" d="M0 2470 H600"/><path id="62" d="M0 2505 H600"/><path id="63" d="M0 2550 H600"/><path id="64" d="M0 2586 H600"/><path id="65" d="M0 2628 H600"/><path id="66" d="M0 2672 H600"/><path id="67" d="M0 2712 H600"/><path id="68" d="M0 2747 H600"/><path id="69" d="M0 2779 H600"/><path id="70" d="M0 2817 H600"/><path id="71" d="M0 2852 H600"/><path id="72" d="M0 2902 H600"/><path id="73" d="M0 2948 H600"/><path id="74" d="M0 2995 H600"/><path id="75" d="M0 3037 H600"/><path id="76" d="M0 3084 H600"/><path id="77" d="M0 3134 H600"/><path id="78" d="M0 3181 H600"/><path id="79" d="M0 3221 H600"/><path id="80" d="M0 3269 H600"/><path id="81" d="M0 3307 H600"/><path id="82" d="M0 3347 H600"/><path id="83" d="M0 3387 H600"/><path id="84" d="M0 3427 H600"/></defs>'
    list1 = re.findall('<path id="(.*?)" d="M0 (.*?) H600"/>',news)
    come_dict = {}
    for s in list1:
        come_dict[s[1]] = s[0]
    return come_dict
def get_allword():
    word_pass = '''
    <textPath xlink:href="#1" textLength="322">音坊陪坚蓄帝烈朱佩忠那床胳挡率凶迹县槐神处罐您</textPath>
    <textPath xlink:href="#2" textLength="476">鞠仓嫂剑奉次胀柔挺克屋齐驾乙枯炮岭联坡衣巧帅炊孙给丰息模小脆四异类酬</textPath>
    <textPath xlink:href="#3" textLength="308">朗长滔单楚抗断餐遮晨屠诞佣摘圈牛冠弹葱悲卡绿</textPath>
    <textPath xlink:href="#4" textLength="392">橡够黎箩寇绸良梨浮扛赶烛底柿谜弯集昼服欠捞他稿聪丑娃茫币</textPath>
    <textPath xlink:href="#5" textLength="462">信务翻桂胆掏倚华车然整痒届艺荡填骨粉道甚握蒸吵来肤笋躬寸树栏线歉杨</textPath>
    <textPath xlink:href="#6" textLength="322">细邮原暖委趣析哀壮负疯鞋愉奔造配违蚁啦帽庙饱唐</textPath>
    <textPath xlink:href="#7" textLength="294">箭谢敏统楼抽守章锄娱关倾蛋散棒哨岛喜殊汉狸</textPath>
    <textPath xlink:href="#8" textLength="504">梁都航愚壤境拉酱邀误展陆岩远拜打包让调臭济掌才果站牺江磨震筝袍估旁不嘱其</textPath>
    <textPath xlink:href="#9" textLength="392">逆捧接掉骑垂敢犯哈袭眯抱失霉厕俭拖钥煌强筋穿谁份伐坦凉骄</textPath>
    <textPath xlink:href="#10" textLength="406">彻挎丛蔬子铸爆御泄洪绪溜组茂呢中竭告阔殃程支字哗糟差缝梅笔</textPath>
    <textPath xlink:href="#11" textLength="378">推定霸疗圆烘杰五杆银邪技遭洽普竿隔蝶深厉耗茅心阳物欣觉</textPath>
    <textPath xlink:href="#12" textLength="364">涂肌涌煤烤认舒铜人朴真值念棍栋寄阶城斯随肢咳桥饼授览</textPath>
    <textPath xlink:href="#13" textLength="336">般嫩苏郑射利身脂辉陕执状论债层叮省沈万病瞒探钉炕</textPath>
    <textPath xlink:href="#14" textLength="476">溉捎纲休视附非丽倘讨垮俗颜凯瓶善熄踪名肯武筒稳软终流败桶蓝农额曾脉秃</textPath>
    <textPath xlink:href="#15" textLength="546">呀抵愿牵扭千遇化盯麦孤厘一械领徒宇迈恰黑垒芦腥厦俱雷孝剃会芒患宜巨谨紧贤护涛饿</textPath>
    <textPath xlink:href="#16" textLength="322">菌雾画筛拳烫鲜瘦尼昏询洒勒齿船座兔宣烂舟坐筑滴</textPath>
    <textPath xlink:href="#17" textLength="434">观证等祝嗓考怎尸压呆窃嫌左尖威斥挨下须嘉译河好勺塑醋宫内奴仆照</textPath>
    <textPath xlink:href="#18" textLength="378">督乌请微叠茧舱把工旷群毯馅属庭碗残现福计菠森酷叛蜜扮载</textPath>
    <textPath xlink:href="#19" textLength="532">漫敌夸惰端宙蜻替貌召骆义说你登扰板亭锁志思改恭绑禁挑语试袄串纱踏薄学直对摊糖</textPath>
    <textPath xlink:href="#20" textLength="322">苹晴和劳循狂自最雨馋篮闲勤樱螺东颂埋做假肺运露</textPath>
    <textPath xlink:href="#21" textLength="588">窗分求轿片贞贩抹供早卷瓦否找要获蚊育瑞雄搁百察兼陡抓多太弃宴恐鄙锯去摆滥此以灌慧赴污</textPath>
    <textPath xlink:href="#22" textLength="546">啄何留于仍谈肃枕宝援冤吧兆欧令吊停居冶操秧凳慨削坏赖年迟边缺夺步表摄罗七蒜始悟</textPath>
    <textPath xlink:href="#23" textLength="406">裤瞎膛允蹲顾匀手含贷兄撒乏益气竹狱评极秆承天未偷堡疑诱战椒</textPath>
    <textPath xlink:href="#24" textLength="308">甲盖廊叨阿架锦阀蹈俩间筐很光彼酸验喷距固萝浓</textPath>
    <textPath xlink:href="#25" textLength="336">默纺欢殿策赌诸迁歪竟革候个医辆框青鸡痰众妄梦升没</textPath>
    <textPath xlink:href="#26" textLength="448">企睛斧坟相畅悦嗽退满玩生置点部谋浙险贺束葛切慕偏夫消跌皱葬先庄冈</textPath>
    <textPath xlink:href="#27" textLength="308">袋涝腰或抬歇公浅跪体待蛙乒十村效穴本惑滋炎云</textPath>
    <textPath xlink:href="#28" textLength="448">喇遍栽劫葡靠悬耻风轧窜亦镰问荷到少石导红割限减典花捉出腐房赤染需</textPath>
    <textPath xlink:href="#29" textLength="532">撤鞭宏愈陶致艰瓜质蚂辈鼓聋仔栗誓摇裁超概某铲贫痕讽剖龟墓掘腔案炭墙牙帐嚷悄议</textPath>
    <textPath xlink:href="#30" textLength="546">转略听秤雁冰交乃今敬围扎叔撕泥剥棚漆智膜扩特情尺命话垄门忽块巡着湾哄颤纸阅戏塞</textPath>
    <textPath xlink:href="#31" textLength="420">危峡储欺严临恢空饭宽吐姿二野壁北况鸦贡劲斩沫咸坛鬼大卵咐昨疮</textPath>
    <textPath xlink:href="#32" textLength="294">零富屯挥烧有倍既杀高魂攀泉咱党数伍复样吗羡</textPath>
    <textPath xlink:href="#33" textLength="574">粒习液匆旨惭牧桌释挤全反毕使损诊殖该衡常砖跃驴赔灵划挂姥鹅象控障独镜跨若笛疼销幸狼</textPath>
    <textPath xlink:href="#34" textLength="392">寻封列睁沙夕翅沸吓枣局隐另核喘别淘立桐妨凝过波鸟被帆径春</textPath>
    <textPath xlink:href="#35" textLength="294">具犬久洋看皮装衬初盲祖丢鱼净脾蚕伙知些防妹</textPath>
    <textPath xlink:href="#36" textLength="420">姜许永态适鹊飘姑行幼贿海巴砌骤横羞朋捷荒钟堵界积薯鸣狠资木罢</textPath>
    <textPath xlink:href="#37" textLength="308">掀补已誉辞仪兰成两垃冬研赢奥朽攻劈稼午陵铃优</textPath>
    <textPath xlink:href="#38" textLength="308">佛匪盛引隙德拴喉宁扑振院签备镇忧送性图盾上阁</textPath>
    <textPath xlink:href="#39" textLength="350">世甘芽针曲缘招筹肝恩宪申保奸识宗碍疤购漏旱错比汁浪</textPath>
    <textPath xlink:href="#40" textLength="364">充暮岂用启英爽暂希培尽弦室滤铁册谎丧突烟括女响页灰沿</textPath>
    <textPath xlink:href="#41" textLength="336">售袖走政泽母止怖辨易钓据迎起又回在粪忙棋咬毙逼摧</textPath>
    <textPath xlink:href="#42" textLength="490">俯柜者惩鸽触地糠桨泰套灯族姻匙己献抖腾锻弄懂爹抄喝扁羽色艳乞投肿客灾驻</textPath>
    <textPath xlink:href="#43" textLength="350">柴私食课洁眼绵队姓伤葵宾近织祥进脱慰湖实诉军场外融</textPath>
    <textPath xlink:href="#44" textLength="294">戚夜睡油赵滑柱颠锣膨乐取盼侵注励孕伸吹且男</textPath>
    <textPath xlink:href="#45" textLength="546">胸裹锤辛泪奖遥受日猴扔衰胖矮惊乓讯票伯辩吞脊赚便慢闷审六静惹饮治只答环订址阴功</textPath>
    <textPath xlink:href="#46" textLength="560">氏刚婶鼻闯熊勇犹预披苦借熟盐助闭愁粮托甜即枪丘节遣怪版陷明速术救废诗事截囊蒙录歌</textPath>
    <textPath xlink:href="#47" textLength="504">汗互皇甩纪戴科颈碰渐珠莲因携晋席鼠促灭演丈乡辰越拍胶毛虎唯帮绍盗钩歼索漂</textPath>
    <textPath xlink:href="#48" textLength="392">搬商侄虽的慎测纤绒叉绕窝港维较童魔朝堪项位户株声刺责途炼</textPath>
    <textPath xlink:href="#49" textLength="308">纵厅飞型击虫耍店崭头延钞泛健驶期梳搜彩旋每读</textPath>
    <textPath xlink:href="#50" textLength="462">饰入续惕康傅焦醒旧形吉井吴所洗余裂得硬裳冲香炉及谱匠燃谣舰倦按示番</textPath>
    <textPath xlink:href="#51" textLength="392">锈敲燥毁牲也担八专亏雀趁理往从代袜民末更症透跳箱排拾崇乳</textPath>
    <textPath xlink:href="#52" textLength="434">砍惧邻带广臣畏卸蛾脸塘圣舍饺乔趟称沉础跟马滚迅坝当之市享胞浩碑</textPath>
    <textPath xlink:href="#53" textLength="560">刻辣例肥藏偶时它几浑汤域屈犁傻扶应链爷膏络雅咽寨侍望尾尊疾激晕拼血翠谊规爪舌判徐</textPath>
    <textPath xlink:href="#54" textLength="406">倡沃哥阵清贝继归姐国逢萌杠第约懒降礼饲里星猫连浊惯密煎混抢</textPath>
    <textPath xlink:href="#55" textLength="336">坑难磁介朵凤岸旺扯述持绳缠孟缩丙僵扒焰骡茶批序虏</textPath>
    <textPath xlink:href="#56" textLength="476">辽毅动建郎谦叶就嘴贪结由爱警氧汇仁龄禾贵椅沟肾首恼向冻通季拘款弱根吨</textPath>
    <textPath xlink:href="#57" textLength="462">驼猾火府捡聚胃禽婚耕锅川味占缴裙社区尝松蛛完轨与戒脖墨书句渡龙秘萄</textPath>
    <textPath xlink:href="#58" textLength="392">度正协盟棵牢共裕匹输腿赛沾却嚼斤闹如素粥淋尘前暴阻暑秒伴</textPath>
    <textPath xlink:href="#59" textLength="448">央容蹄浴择新叫缸趋恶狐副并怕屿园淹仙笑驳究傲财亚饶塔痛盒兴宋感闻</textPath>
    <textPath xlink:href="#60" textLength="588">怒轻籍蜂钳胜权堆帘馒僻刘酿州为材俘亩宰祸笨揉冒灿丹贯开月涨故躺帖脑伞吼催丁尤师鲁离牌</textPath>
    <textPath xlink:href="#61" textLength="532">景垦稠盏影泻山堂免死拿确婆肉耐勉捐乱梯肩傍疏娇侧洲言哭讲元恨篇泊卖摸员博肚题</textPath>
    <textPath xlink:href="#62" textLength="308">必刮球弊缓耳将煮皂毒晶南叼逃京怠猪面张再厨词</textPath>
    <textPath xlink:href="#63" textLength="532">哑衔厌剂狮热杜壳哪勿巩芹赏基蓬毫制蕉搅妻矩眠渠编忍辟岁历颗芳挽蠢参予换溪顿梢</textPath>
    <textPath xlink:href="#64" textLength="322">宵轰精姨铺无绘盆叹炒魄豪鹰槽机锐崖妙雕法任业绞</textPath>
    <textPath xlink:href="#65" textLength="378">卧寒押抚廉符董王悠烦仰吃怜田晃写晌校监拌杏林窄霜急传丝</textPath>
    <textPath xlink:href="#66" textLength="532">准搂是害钱产变派竖寿夏量旬呜遗九家劝详愧忌加卫了拐映宿悉迷孔劣可蝴角纽教摩纳</textPath>
    <textPath xlink:href="#67" textLength="406">移锡翼著秩我访爸晒营君翁势么豆紫挖刊睬唉扫淡麻娘榴潮右斗均</textPath>
    <textPath xlink:href="#68" textLength="476">快递种惜低解斜搏欲友平仿刷儿斑呈疆像温举笼播皆侨侮浸悼啊标描燕电隶屑</textPath>
    <textPath xlink:href="#69" textLength="434">诵官什艇胁棕膊式孩蜘档查塌舅芬号粱衫菜口困设跑鹿旅僚券恒士趴潜</textPath>
    <textPath xlink:href="#70" textLength="574">枝虾班合唇修舞泳律纠码挪算慈荐猛买放植捏办返愤咏破粘足辜膝胡巷杂赠矿柳躲悔泡谷练亮</textPath>
    <textPath xlink:href="#71" textLength="392">穗乖逗似滩草报付刃亲渗莫屡拥狡妇晚拨刀泼水格但揪顷住幅累</textPath>
    <textPath xlink:href="#72" textLength="532">妈鸭玻碎肆湿台疲训们显选逮眉盘拆忆顺迫蝇灶辫卜铅惠喂父遵想罪增昂踢顽碧背范贱</textPath>
    <textPath xlink:href="#73" textLength="588">方罩征谅郊仅霞费津蚀绣践汽桃职收帜慌撇货黄施腊西浆养贸创奏锋弓经耽各古蹦决凑萍依碌拢</textPath>
    <textPath xlink:href="#74" textLength="448">作幕源荣吸菊品辱奋疫俊醉纹乎庸秋辅奶钻尚掠脏厂贴折检岗橘司稀团轮</textPath>
    <textPath xlink:href="#75" textLength="448">馆榨落锹琴安插伪岔酒畜布棉短亡后掩见兵虹庆奇际澡逝剪暗稍驰池料稻</textPath>
    <textPath xlink:href="#76" textLength="392">揭倒巾李争纷寺隆陈提件追窑骗妥臂仗堤偿拦摔妖雹总宅渣絮怀</textPath>
    <textPath xlink:href="#77" textLength="308">扣佳力榜盈唤干脚缎炸存文浇勾库闸桑呼钢拔至添</textPath>
    <textPath xlink:href="#78" textLength="490">驱幻虚蔽目粗记榆则游怨渔管肠腹剩瓣糊丸敞汪圾侦耀珍璃三昌同剧哲删租滨膀</textPath>
    <textPath xlink:href="#79" textLength="336">兽昆绢苗骂繁漠糕爬蔑虑挣税蛮狗覆旗能而药重意半尿</textPath>
    <textPath xlink:href="#80" textLength="308">柏秀金纯喊简苍涉史避嫁贼柄亿凭叙韵薪凡网润壶</textPath>
    <textPath xlink:href="#81" textLength="322">仇路活眨羊拒键股捆达猜杯除街恳洞系玉擦逐诚狭刑</textPath>
    <textPath xlink:href="#82" textLength="322">惨赞蛇峰熔夹米忘茄伏发恋绝搭役鉴吩伟乘旦艘渴伶</textPath>
    <textPath xlink:href="#83" textLength="546">条绩土双她唱搞指撑美蜓芝老捕周努顶茎采挠弟还闪厚扬抛价这垫矛级主雪蜡瞧冷撞竞器</textPath>
    <textPath xlink:href="#84" textLength="154">罚穷构拣段猎躁饥白踩晓</textPath>
    '''

    # lsit1 = re.findall('<text x="0" y="(.*?)">(.*?)</text>', word_pass)
    lsit1 = re.findall('<textPath xlink:href="#(.*?)" textLength=".*?">(.*?)</textPath>', word_pass)
    word_dict = {}
    for i in lsit1:
        word_dict[i[0]] = i[1]
    return word_dict

def get_pass():
    # 难度2
    word_pass = '''
    	<text x="0" y="35">专梦赠挺试痛故踪冷洋歌网售但刘链偏给沾军谈幅灯涨泻练虚狗胖堂猛粱孔然倍斧柱穴匪暑生域</text>
	<text x="0" y="71">汁惜中得顶冤茧控绿命赔稿耻缝演验许话寸看浪织松岸裳甘卜鬼治贱叮服候们锻善暴咏老他切断</text>
	<text x="0" y="118">组敬仓弟俩杂浓期倦萄喊遥亮狠步奶来轿桃稼补轧泽本惨文坟毒应启就丁府情橘趟侄扇兵屿此践</text>
	<text x="0" y="149">紧况拜垦昏锅邻赶渗精国耗佩讯泊衬望巩鼠奥剃慕种侨梨膛己伶廊趣卧沉娃宽孩欢僚掉董畅惊优</text>
	<text x="0" y="193">扒傲呼依岔柏泰萍仍女盒皮点炮彻有量杰吼漫交假核旨帮挽停醋离男隔竿置增摄抱瑞裁截汤汉瓦</text>
	<text x="0" y="237">旅蛾唇门犁领岭芒俊毕苏教投色委管料堆卖役赛宾村抗破好长扫起傍颤昂渣热寿够灌迈雁债返七</text>
	<text x="0" y="275">黎周络颈柳划茶母侦你归砖宪留段旱绝念斥待叉却碍冬税贼属木瓜又拨节概抢幸艘抬误协禽仗牲</text>
	<text x="0" y="324">贴家含鹊顽莲湖戒住招楼超叼巾絮用蜓芝横该力察词券哨翠宗解劈汗福陆寻废被仔忠伴蚂伍促纳</text>
	<text x="0" y="358">浅身爆荣乓葱股狮九泪闭亦捕航粒栏森凝世蜘课饲坛操鸽竹嘉沈颜救闷腰细备索蜂号卷贡渴雾伯</text>
	<text x="0" y="405">采蜡隙沃饭赴亭商弹臭妨定滚尤粉利宝萝胶秩访渔硬宰堵孙吨齐仆始气筐单立唯决自途缘赌驶鹅</text>
	<text x="0" y="449">悔颂笛膊窃探土劣白棋船校祝陵膝哈输歼贵衫丸方朵偿篇暖射霞娱诱打祖填丢塌碌祥徐鹰焦武栗</text>
	<text x="0" y="488">展爷肩灰各系牛韵犬赚液储考伤物稻五春今壤鞭减阀惯掏末裹窝匆殿体蝴厉告灾肾谣羊毫绕务社</text>
	<text x="0" y="529">啄及亚晶垒抓养洁乌锐君柿炎供疯脾比农挣喜哭底则愚肥睡箱桌娘杠磁特饱货键脖欺纱艰乞冠剑</text>
	<text x="0" y="564">发越汪丑恼确珠膜兰导仙封因郑除卸耀态扔艇稠宅的刃逝岂劳信岗睁刚洲缺佳溪钢院孝洗晓抹予</text>
	<text x="0" y="609">是友铁碎箩档移霜鞋宴帝牢真血玉妥成榨叙南素度迫励喂尾禁满甜蹦儿征谷众裙醒馒忘攀咽欲队</text>
	<text x="0" y="642">未剂说消泛贺绣钩窜并分筛尼添妈赤漆亲咳件资督猪菜港哥租揪肆剥前炭例惭礼富怪称秀房干颠</text>
	<text x="0" y="686">疲碰回劲钟疆城橡绪批饮净芳拘晚戴荒崖铸铃达述蓄风伙皇润昆尚纤同份近绘座罗俯架需民霉央</text>
	<text x="0" y="729">疤滩沿搜患必隆照酸率表避于览费忍陡携杏耐矛逃锯混恒宁引泳阶猫献背问谦抽鸟里俭志势吹喘</text>
	<text x="0" y="767">省芬坐巨仪肝页番游垄火烟井败寒鞠挠跑吐昨时答健讨浩枪听东四仰灵援赖处呜惧掩奔吊伐惑跃</text>
	<text x="0" y="799">撤千庆厅肃介恭味泼劫搁饥狱十赏勾朋肌振州雄烤与对炼英慢披独漂围退田驰狂居堪排林姿堡站</text>
	<text x="0" y="840">辉蛋滋忧凳脉舌境追趁父割骄李集罪星轰犹揭蔬菌厌恢蚁赞难谋棚担像贷榴悦梅沸筒砌汽材庸销</text>
	<text x="0" y="878">狭蚀动崇眼着袜辛薯允幻蝇和选辆觉去剖笔牙抛灭姻走腊先傅迟触激行调损伏啊月歇若肢扑绒俗</text>
	<text x="0" y="914">碑忌炊吗盐凉怨士菠鸭墓河参哄扛某八恩显晕恳把皂煎些擦括著虾板龟染桥舞捆繁勤送殊矿堤额</text>
	<text x="0" y="952">叔磨咱马肉丝俘名坦斯障按犯上塞灿榆夫险撞狼僵路搭暗审状可豆呈筝盗恶至魔哀后司普口雪贿</text>
	<text x="0" y="996">拦株罐溉无兽题拿令爱疏刺肯帖经雨蹲仇市顾悠闻乳再姓碗海手史密子在辜学驾贝滴计示郊舱习</text>
	<text x="0" y="1045">叠贞建眠少洞谎浸疑露登享滤骂抚蜜掀童竖几技估鲁肚齿描绵一致滥囊疮穿鸦术列涉唤模弓袭熔</text>
	<text x="0" y="1076">责锁脑限偷赢挎知垃型式辣摊沫跌喝撑娇攻下狐皆厘傻勒姥姜踢笼谢靠蛛腐么侍道巧浊山湿葵策</text>
	<text x="0" y="1118">绩找希胜似形肤绑枯捞竟渡轨躺哲饰痒改圆第弊饺迎丘悄棵凭荐持扯抵稳誉藏缠科燕还舅支偶铅</text>
	<text x="0" y="1157">旧沙所散轮求凶薪遗丛企旦效甚随变兼腿耍秒付弯勇嚼云往泥笨粗孟剩即源桑驴阅蛮岁怖煌砍荷</text>
	<text x="0" y="1202">乏活贤远范将私阴闲最逗折博御撒腥托妹油溜巷杜蓬症锄拳值愤胀检购禾辞关黄搅耕让饿茫钓骡</text>
	<text x="0" y="1242">小珍肺总蛙乒畜尖迹斤绸非郎厚过线腾坡舰育侵劝讽零蚕寄摘樱心巴漠编浴邮爸转它嗓尸战包敲</text>
	<text x="0" y="1288">图屑根贫伸器湾到盖脸出猾阳止胆译终虽屋伞摩栋护萌秘嫂笋章搞粪奖躁现医外竞扭粥础滨池辰</text>
	<text x="0" y="1329">人双评数矩制事族孕串闯乎脊统乙煤王怠惹连慎余锦录旬壶吉龄查奴片脱躬吵茂观燃京涂奸瘦驼</text>
	<text x="0" y="1378">甩敏嫁叫价糕绳僻峰直或花悬斗瞒敢哪蒜苍复闹画朝益灶良圣怒疼寺欠日速休规坊糖书诞冰丰化</text>
	<text x="0" y="1416">借佛牧妙抄裕也互做拉雷夕锣角胞既拔胃盾江旷羽声驻询累幕宙充茄元性修地植整掠摆畏莫配肠</text>
	<text x="0" y="1462">膨辨争烛坏略拒造拥丽缸泄递法果醉冒帜席了厦麦电华嫩吸忆耽品脏算实胳腹判苗愧百纸个谨聪</text>
	<text x="0" y="1502">视洽棍会津跳捐店趋烫筹叶古疗谁谊脂腔蹄苦订县之睬勺柴梢痕拐庙睛誓氧牺施全息员买测虎宫</text>
	<text x="0" y="1550">理裤短万承刊场肿继监彩瓣尿皱宇温升埋慨乘记饶谜诚跟爬纹疫乖基低掌帽浇澡缩翅夹骤者只屠</text>
	<text x="0" y="1586">茅缴具亿欧脚扰爽保三执勿摇拌且梁挂请鸡镇详辅宜蔑免尊翁开死邪尝壮鹿膏很倡以卵臣右震笑</text>
	<text x="0" y="1623">躲官摸册句盘预违衡挡祸餐翻大雀晌读催易德纺窄卡垮扣异舟掘朽两陷墨烧版辈毁眨尺替铜清枝</text>
	<text x="0" y="1671">叨墙秧捷臂杨悲别强空青响举阻炕梯天丹残玻胸透敌见西守雹愉便轻届柔助逆宋项次熟摔葛亡龙</text>
	<text x="0" y="1708">俱晒毛淹唱挪群吃魂贪据套拢典影镰燥脆软慰运挥槐戏卫钱扎歪园绢机锋框另亩永思飞初稀占续</text>
	<text x="0" y="1744">删新蝶拴姨斜公挖师什悟刷案唐沟倘愈间隶顺枣窑秋边桨宵悉副迅暂每户块朱刀格螺派压痰炒矮</text>
	<text x="0" y="1788">当岩稍剪贯锹迷岛爪没黑忙窗洪提耳陕样培相盆临办厕涝眉击完已桐荡任平错鉴遮竭冶目焰识坑</text>
	<text x="0" y="1821">坝盟污遇蜻罩糊伪产胡乔戚美坚晨淋帆毯骨旺芹彼冻铲梳匹陈召斩兴蔽塔米奇妄碧疾那宏猴眯急</text>
	<text x="0" y="1865">柄纠言刻慧逐固申树拣弱羡姑其逢袖烈政尘艳这镜蓝殖拾季恐附踏街棉徒忽红字纯覆仁昼诗厂我</text>
	<text x="0" y="1902">奉盼取均虫渐议纽车葡鼓食孤紫跨袄陶扁弄裂款烘吧严乐寨符棒太般拖距愁阵暮结签蒸冈貌捉烦</text>
	<text x="0" y="1940">插尽辟泡爹晃宿遍阔叹程嫌静您饼刮融馆放蠢舍传槽搂伟址亏北何乱夸蛇扶义斑较要约夜穗病载</text>
	<text x="0" y="1972">晋秤阿刑琴鸣联袍须能熊凯简妖盲辫嘴押意猎苹授朗氏想聋仿曾酬接盈诊舒吞挑景呆宣扬淘邀啦</text>
	<text x="0" y="2021">骑证罢遣麻语纷握蚊差诉使丧汇虹光库映位壁衣久惕际存钻陪早削雅头纵径年室璃极栽从纲纪适</text>
	<text x="0" y="2059">喉歉抖翼营首峡代香猜遭炸盯悼穷由象业济作剧匙换揉屈鱼恨加雕瓶二杆泉毙牵摧羞主认踩酒条</text>
	<text x="0" y="2096">历凑屡威释牌环漏巡惠析厨盏装辱石构哑研欣共懒顿妻狸叛收屯药嚷夺骆涛捧唉滑鄙馅飘粮芦多</text>
	<text x="0" y="2140">注塘负圈滔贸跪熄涌筑籍霸原鼻权绞惩锡写潮侮容烂内匀榜枕音钞票豪推突针财如衔正夏顷吴等</text>
	<text x="0" y="2173">创怀职流择高草奏挨呢拆功倚否危壳客绍究困兆丈驱冲而帅聚革局薄受佣她不乃球昌通杯敞崭半</text>
	<text x="0" y="2205">粘帐虏秆设嘱洒失缓银垫筋旁质秃向反贩兔凡吓兄柜胁阁浆降殃玩慈妇辽警束六婆庄椅魄蕉区喷</text>
	<text x="0" y="2249">慌安训逮迁入克感狡寇怕害塑才常咐恰咬廉袋桂层虑辩水惰恋深喇愿广野播带蹈隐骗咸篮倾撇论</text>
	<text x="0" y="2291">撕赵趴律扩闸努懂奋团微级馋凤界钳防足仅智捎旋张驳罚瞧台酱瞎乡晴搏挤呀鲜楚菊婶合延芽朴</text>
	<text x="0" y="2340">倒班面重弃桶都币遵准部姐金午怜糟淡艺毅报锤波维捏庭默拍垂床箭进川钥渠获械婚讲衰谅浮蒙</text>
	<text x="0" y="2378">逼拼搬诸酷杀党吩扮幼标膀葬浙盛左怎明序哗棕颗缎茎匠酿积工更码嗽捡曲丙落甲循糠谱浑侧旗</text>
	<text x="0" y="2423">指钉快煮帘闪为勉弦康神锈诵圾炉端布椒铺类潜</text>
	<text x="0" y="32">七古保兴乌汕滨康前上威中河沿工道肇太茂拥莞凤朝旗谊山肃川迁淄惠绍县杭南孝徽重结洛遵港</text>
	<text x="0" y="72">木廊四农宁长六镇胜才信连黄东家贵设冈谐迎金曙盐蒙湾解路宾进藏鞍昆门感京沙新富江凰汾津</text>
	<text x="0" y="96">州黑坊德疆海春爱祥府成沈厦衢合公石园文创教乡庆五西机桂台治庄宿三村襄永武十通潍昌甘心</text>
	<text x="0" y="128">宜夏关博红一珠辽安风明烟民体开市育封层波泉深站汉岛学齐锡济佛赣化银主澳生花肥岳韶青大</text>
	<text x="0" y="156">人定向都二皇尔圳天建无湛交幸林鲁弄乐浙省和放年临振平环福广龙友内梅楼隆远健陕泰扬晋秦</text>
	<text x="0" y="183">光清云利名嘉湖郑阳徐场绵充哈锦九义头邢号北苏香街温源八华淮团常城区衡业军吉</text>
    '''
    lsit1 = re.findall('<text x="0" y="(.*?)">(.*?)</text>', word_pass)
    word_dict = {}
    for i in lsit1:
        word_dict[i[0]] = i[1]
    return word_dict


if __name__ == '__main__':
    # http://s3plus.meituan.net/v1/mss_0a06a471f9514fc79c981b5466f56b91/svgtextcss/21787638fa1db174160889e5421045f1.svg

    id_dict = get_id()
    #难度2
    word_dict = get_pass()
    #难度1
    # word_dict = get_allword()
    # com_dict = get_ally()
    print(id_dict)
     # class="review-words Hide"
    user_agent = [
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
        "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0",
        "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)",
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
        "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
        "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
        "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
    ]
    all_list = []
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Referer": "http://www.dianping.com/shop/k7a1VkZePZmh0ZxC/review_all",
        "cookie": "lxsdk_cuid=17960817c27c8-0796fcec533919-5771031-144000-17960817c28c8; _lxsdk=17960817c27c8-0796fcec533919-5771031-144000-17960817c28c8; _hc.v=e70fe4b8-a481-d12e-d7ea-5fbab9991ea2.1620984014; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1620984014; dplet=32b09d477fb7f934b5e51ff5555f79be; dper=de19aaabd19029da9c5a933fbb2f0d971b4ae8232e247b78c128537a7185c46fe1d9ce926bd99167025f57a7cbd5f4eccd2bfa45661d64c620fec795f182971d39c51000d580e3aa98c2f6889ac11a6fa077a7208133e52a24de0c5b3578e10a; ll=7fd06e815b796be3df069dec7836c3df; ua=%E6%97%A0%E8%89%B2%E7%9A%84%E4%B8%B6; ctu=3e1d71edaa3f105d92878b58dc0f4bfdcf6f9bff63b7058c754193b27d769ea9; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1620984089; _lxsdk_s=1796a2cff27-75c-64d-720%7C%7C335"
    }
    error = 0
    for page in range(50):
        if page == 0:
            url = f"http://www.dianping.com/shop/k7a1VkZePZmh0ZxC/review_all"
        else:
            url = f"http://www.dianping.com/shop/k7a1VkZePZmh0ZxC/review_all/p{page + 1}"
        sleep(6)
        print(url)
        res = requests.get(url, headers=headers)
        print(res.text)
        print(res.status_code)
        tree = etree.HTML(res.text)
        back = tree.xpath('//div[@class="main-review"]/div[@class="review-words Hide"]')
        print(len(back))
        if len(back) == 0:
            error += 1
            if error >= 6:
                break
        else:
            for i in back:
                new = etree.tostring(i, encoding="utf-8").decode('utf-8')
                new = re.sub('\s+', "", new)  # 替换空白符
                de_ok = re.findall('<divclass="review-wordsHide">(.*?)<divclass="less-words">', new)[0]
                new_list = re.findall('<svgmtsiclass="(.*?)"/>', de_ok)
                for n in new_list:
                    the = id_dict.get(str(n))
                    locate = get_x(the[0])
                    y = get_y(the[1])
                    #难度1
                    # the_id = com_dict.get(str(y))
                    # the_word = word_dict.get(the_id)
                    # 难度2
                    the_word = word_dict.get(str(y))
                    de_ok = re.sub(f'<svgmtsiclass="{n}"/>', the_word[locate - 1], de_ok)
                print(de_ok)
                all_list.append(de_ok)
            # headers["User-Agent"] = user_agent[random.randint(0, 19)]

    df = pd.DataFrame(all_list)
    df.to_excel("国金一店.xlsx", header=['评论内容'], index=False)
