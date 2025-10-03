import ybc_game
import random
from math import *
from time import *
import ybc_ui
import os


from datetime import datetime,timedelta

def calculate_time_since_target(target_month=2, target_day=16):
    # 获取当前日期
    today = datetime.now()
    current_year = today.year
    
    # 构造目标日期（今年的2月16日）
    target_date_this_year = datetime(current_year, target_month, target_day)
    
    # 如果今年目标日期还没到，则计算去年的目标日期
    if today < target_date_this_year:
        target_date = datetime(current_year - 1, target_month, target_day)
    else:
        target_date = target_date_this_year
    
    # 计算差值
    years = today.year - target_date.year
    months = today.month - target_date.month
    days = today.day - target_date.day
    
    # 处理借位情况（如 3月1日 - 2月28日）
    if days < 0:
        # 获取上个月的最后一天
        
        last_day_of_prev_month = (today.replace(day=1) - timedelta(days=1)).day
        days += last_day_of_prev_month
        months -= 1
    
    if months < 0:
        months += 12
        years -= 1
    
    # 返回字符串格式的年、月、日
    return str(years), str(months), str(days)

# 示例用法（自动计算今天距离2月16日多久）
year, months, day = calculate_time_since_target()
print(f"今天是 {datetime.now().strftime('%Y-%m-%d')}，距离今年2月16日已过去：")
print(f"- 年: {year}")
print(f"- 月: {months}")
print(f"- 天: {day}")
mobile_key_type6()
ybc_game.size(2000,1000)
ybc_game.title('战斗机模拟器（YBC_GAME）')
sky = ybc_game.actor('蓝天')
sky.width = 2000
sky.height = 1000
sky.left = 0
sky.top  = 0
shang = ybc_game.actor('shang',[1720,50])
shang.height = 65
shang.width = 65
teach = ybc_game.actor("teach",[1600,50])
line = ybc_game.actor('跑道',[5000,950])
line.height = 200
line.width = 10000
logo = ybc_game.actor('我机',[500,200])
logo2 = ybc_game.actor('敌机',[1500,200])
logo3 = ybc_game.actor('白云',[0,300])
start = ybc_game.actor('开始游戏',[1000,750])
sky.width = 2000
sky.height = 1000
me = ybc_game.actor('我机',[600,850])
TNT = ybc_game.actor("TNT",[me.x,me.y])
TNT.width = 50
TNT.height = 50
TNT.chuxian = False
me.speed = 1
me.dong = 0
me.heigh = 0
me.state = '开始'
me.way = 1000
dj = ybc_game.actor('敌机',[2100,600])#英文不好,请谅解
sea = ybc_game.actor('大海',[1000,1100])
sea.height = 400
sea.width = 2000
me.sd = 0.001
me.cnt = 0
me.fbs = 0
line.No = sea
xingshi = ybc_game.actor('行驶条',[1000,50])
xingshi.width = 1000
yun = ybc_game.actor('白云',[2300,700])
win = ybc_game.actor('胜利',[1000,500])
fail = ybc_game.actor('失败',[1000,500])
me_dark = ybc_game.actor('我军子弹',[me.x,me.y])
dj_dark = ybc_game.actor('敌军子弹',[dj.x,dj.y])
DHP = ybc_game.actor('敌机血量',[dj.x,dj.y-100])
way = ybc_game.actor('angle')
way.angle = 135
HP = ybc_game.actor('血量',[me.x,me.y - 100])
class setting:
    fbs = False
    add = False
    com = True
    bgm = True
    afbs = ybc_game.actor("off",[1500,300])
    aadd = ybc_game.actor("off",[1500,500])
    acom = ybc_game.actor('on',[1500,400])
    abgm = ybc_game.actor('on',[1500,600])
    aset = ybc_game.actor("setting",[1800,50])
    last_click_time = 0
    ret = ybc_game.actor('return',[100,100])
an = ybc_game.actor('angle(1)',[1800,200])
dj.blood = 20
me.blood = 50
me.win = 0
me.range = 1000
me.away = 4000
me.tip = '暂时没有消息'
me.score = True
me.dark_list = []
dj.dark_list=[]
me.mode = {'L1':[40,1],
           'L2':[55,3],
           'L3':[75,5]}
me.sty = ['L1','L1','L1','L2','L2','L3']
me.can_add_bull = True
dj.cx = False
if setting.bgm: ybc_game.play_sound('bgm2',-1)
dj.pos_y = random.randint(300,500)
showbgm = ybc_game.actor('show_BGM',[1950,50])
showbgm.width = 75
showbgm.height = 75
boom = ybc_game.actor('boom',[me.x,me.y])
me.play_bgm = 'bgm2'
boom.cx = False
me.trun_xing = True
me.cnt = 0
me.money = 0
me.level = 0
me.maxcnt = 5
me.maxmon = 50000
me.way = 4000
keys = ''
text = ''
me.tim = time()
on_key = False
me.t = time()
wrong = None
me.rw = 0
target_fps = 60
wind = ybc_game.actor('winds',[1500,500])
def update():
    #print(setting.com)
    global setting,text,keys,wrong
    me.cnt+=1
    if setting.fbs: ybc_game.timer(fbs,1)
    way.center = mouse.pos
    if not setting.bgm: ybc_game.stop_sound(me.play_bgm)
    if me.state == '开始':
        sky.draw()
        logo3.draw()
        start.draw()
        logo3.x += 5
        way.draw()
        if logo3.x >= 2000:
            logo3.x = 0
        logo.draw()
        logo2.draw()
        ybc_game.text('战斗机模拟器II',[1000,200],'red',50,'simsum')
        ybc_game.text('Fighter jet simulator 2',[1000,300],'yellow',50,'English.ttf')
        ybc_game.text('作品由@松松独立开发并原创，请勿抄袭，感谢各位的配合',[1000,900],'green',30,'Chinese.ttf')
        ybc_game.text('The work is independently developed and original by @SongSong\n please don\'t plagiarize, thank you for your cooperation',[1000,950],'white',30,'English.ttf')
        ybc_game.text('版本：2.5.0',[100,950],'yellow',30,'simsum.ttf')
        teach.width = 75
        teach.height = 75
        teach.x = 1800
        teach.draw()
        setting.aset.x = 1870
        setting.aset.draw()
        if mouse_collide(setting.aset) and mouse.left:
            me.state = 'set'
        if mouse_collide(teach) and mouse.left:
            ybc_game.stop_sound(me.play_bgm)
            ybc_ui.message('操作步骤\n640×360\n太高显示不出来\n(部分细节及音乐可能显示不出来，如帧率等)','MV.mp4')
            ybc_game.play_sound(me.play_bgm)
        shang.draw()
        if mouse_collide(shang) and mouse.left:
            me.state = 'shang'
        if mouse.left and mouse_collide(start) :
            me.tim = time()
            me.state = '运行'
        dj.blood += me.win/10
    if me.state == 'shang':
        sky.draw()
        setting.ret.draw()
        setting.ret.x = 100
        mobile_key_type7()
        try:
            ma = str(oct(me.win)[2:][::-1]) + 'g' + str(hex(me.money)[2:][::-1])+'g'+os.environ['OPEN_ID'][::-1]
        except:
            ma = str(oct(me.win)[2:][::-1]) + 'g' + str(hex(me.money)[2:][::-1])
        ybc_game.text('您的数据与存档码',[1000,100],'yellow',40,'Chinese.ttf')
        try:
            ybc_game.text('你好！我是战斗机模拟器的开发者松松,今天过着怎么样？',[1000,200],'#FFFFFF',30,'simsum.ttf')
        except:
            ybc_game.text('你好！我是战斗机模拟器的开发者松松,今天过着怎么样？',[1000,200],'#FFFFFF',30,'simsum.ttf')
        ybc_game.text('您的存档码是:'+ma,[1000,300],'orange',50,'simsum.ttf')
        ybc_game.text('录入存档码(左键删除字母)',[1000,400],'red',30,'Microsoft.ttf')
        listt = ['1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','0']
        if on_key and time() - me.t > 0.2:
            if keys == 'left':
                text = text[:-1]
            if len(keys) == 1: text += keys
            if keys == 'space': text += '█'
            me.t = time()
            try:
                l = text.split('g')
                me.win = int('0o'+l[0][::-1],8)
                me.money = int('0x'+l[1][::-1],16)
                if int(os.environ['OPEN_ID']) == int(l[2][::-1]):
                    ybc_game.text('永远永远')
                else:
                    worng = True
                    me.win = 0
                    me.money = 0
                    print(1+'1')
                wrong = False
            except Exception as e:
                wrong = True
                me.win = 0
                me.money = 0
                print(e)
        if wrong: ybc_game.text('tips:您的存档码是坏的或者是别人的，只能用你自己的存档码哦\n(可能你还没输完，你可以继续输入，此程序不影响你的数据)',[1000,550],'red',30,'Chinese.ttf')
        if not wrong: ybc_game.text('tips:恭喜你！你的数据录入成功！\n(可能你还没有输入)',[1000,550],'red',30,'Chinese.ttf')
        me.level = int(min(me.win / 5 , me.money / 50000))
        if me.level >= 10:
            me.level = -1
        lv = '  L '+str(me.level)
        if me.level == -1:
            lv = '已满级'
        ybc_game.text(text,[1000,500],'green',50,'b.TTF')
        ybc_game.text('您的💴💰:'+str(me.money),[600,700],'yellow',40,'simsum.ttf')
        ybc_game.text('您赢的次数:'+str(me.win),[1400,700],'yellow',40,'simsum.ttf')
        ybc_game.text('等级'+lv,[1000,800],'green',50,'simsum.ttf')
        if mouse_collide(setting.ret) and mouse.left:
            mobile_key_type6()
            me.state = '开始'
    if me.state == 'set':
        sky.draw()
        setting.aadd.draw()
        setting.afbs.draw()
        setting.ret.draw()
        setting.acom.draw()
        setting.abgm.draw()
        ybc_game.text("游戏设置\nGame setting",[1000,150],'black',45,'Microsoft.ttf')
        ybc_game.text("帧率开关（建议关闭）",[500,300],'grey',30,'simsum.ttf')
        ybc_game.text("电脑模式:",[500,400],'grey',30,'simsum.ttf')
        ybc_game.text("游戏模式:",[500,500],'grey',30,'simsum.ttf')
        ybc_game.text("音乐设置:",[500,600],'grey',30,'simsum.ttf')
        ybc_game.text("*如果你的设备是手机平板这些设备，建议把游戏模式打开",[1000,700],'orange',30,'Dengl.ttf')
        ybc_game.text(f"当前: {'开启' if setting.fbs else '关闭'}",[900,300],'red',30,'Chinese.ttf')
        ybc_game.text(f"当前: {'开启' if setting.com else '关闭'}",[900,400],'red',30,'Chinese.ttf')
        ybc_game.text(f"当前: {'开启' if setting.add else '关闭'}",[900,500],'red',30,'Chinese.ttf')
        ybc_game.text(f"当前: {'开启' if setting.bgm else '关闭'}",[900,600],'red',30,'Chinese.ttf')
        setting.ret.x = 300
        ybc_game.text(f"今天是 {datetime.now().strftime('%Y-%m-%d')}",[1000,800],'black',30,'simsum.ttf')
        ybc_game.text(f'距离游戏开服已经有：{year}年{months}月{day}天了',[1000,870],'yellow',30,'simsum.ttf')
        if day == 0 and mouths == 0:
            ybc_game.text('🎆今天是周年庆🎆',[1000,950],'yellow',30,'simsum.ttf')
        elif day == 0:
            ybc_game.text('🎉今天是周月庆🎉',[1000,950],'yellow',30,'simsum.ttf')
        if mouse_collide(setting.ret) and mouse.left:
            me.state = '运行'
    if me.state == '运行':
        c_pz()
        dark_bj()
        dark_pz()
        way.angle = 135
        if me.way > 300:
            dark()
            dj_dark_bj()
            dj_dark_pz()
        sky.left = 0
        sky.top  = 0
        sky.draw()
        line.draw()
        for i in me.dark_list:
            i.draw()
            i.y += 0.1
        if me.way > 300:
            for i in dj.dark_list:
                i.draw()
                i.y += 1/(me.fbs+1)
                i.x += cos(radians(i.a))*30
                i.y += -sin(radians(i.a))*30
        if (me.way > 300 and me.heigh <= 300) and me.way < 3950:
            line.y = 1500
        if (me.way < 300 and me.heigh <= 300):
            line.y = 950
        if me.blood < 40 and me.image == 'L1':
            ybc_game.timer(add_me_blood,60)
        if me.blood < 55 and me.image == '我机':
            ybc_game.timer(add_me_blood,60)
        if me.blood < 70 and me.image == 'L3':
            ybc_game.timer(add_me_blood,60)
        if keyboard.right:
            me.dong += 1
        ybc_game.timer(djdraw,2.5)
        line.x -= me.speed
        me.speed += (me.dong/5)
        if me.dong >= 30 and me.image == 'L1':
            me.dong=30
        elif me.dong >= 40 and me.image == '我机':
            me.dong=40
        elif me.dong >= 50 and me.image == 'L3':
            me.dong = 50
        me.speed -= 0.5
        xingshi.width = me.way/4.0086
        xingshi.left = 500
        way.draw()
        HP.draw()
        if setting.fbs: ybc_game.text(str(me.fbs),[50,970],'orange',20,'simsum.ttf')
        if not setting.add:
            xingshi.draw()
            an.draw()
            DHP.draw()
            ybc_game.text('高度：'+str(round(me.heigh,1))+"m",[200,150],'red',30,'simsum.ttf')
            ybc_game.text('飞机属性\n 角度:'+str(round(me.angle,1))+"°",[200,100],'red',30,'simsum.ttf')
            ybc_game.text("动力："+str(round(me.dong,1)),[200,200],'yellow',30,'simsum.ttf')
            ybc_game.text('速度:\t\t\t\t'+str(round(me.speed,1))+"km/h",[1650,100],'yellow',30,'Microsoft.ttf')
            an.angle = me.speed
            ybc_game.text('路程:',[450,50],'red',30,'Chinese.ttf')
            ybc_game.text(str(round(me.way,1))+'/ 4008.6km',[1000,50],'black',20,'simsum.ttf')
            ybc_game.text('TNT冷却：'+str(bool(me.score)),[200,250],'yellow',30,'simsum.ttf')
        me.draw()
        ybc_game.text(me.tip,[1000,150],'green',30)
        HP.center = [me.x,me.y-100]
        HP.width = me.blood*2
        if me.way >= 4000:
            me.tip = '请尽快起飞'
            ybc_game.delay(tip_clear,5)
        if me.way <= 300:
            me.tip = '现在可以降下去了'
            ybc_game.delay(tip_clear,5)
        HP.left = me.x - 50
        if keyboard.d and not TNT.chuxian and me.score:
            TNT.chuxian = True
            TNT.y = me.y
            TNT.x = me.x
            TNT.angle = int(TNT.angle_to(way))
        if line.right <= 2000:
            line.left = 0
        if mouse_collide(setting.ret) and mouse.left:
            me.state = '开始'
        setting.ret.draw()
        setting.ret.x = 100
        '''以后要用，会更新，请耐心等待
        if abs(me.way-1086) <= 3 or abs(me.way-2086) <= 3:
            me.up = True
        else: me.up = False
        if me.way <= 3000 and me.way >= 2000 and me.up:
            dj.blood = 40
            me.tip = '难度加大!敌机血量40滴!'
            ybc_game.delay(tip_clear,5)
        if me.way < 2000 and me.up:
            dj.blood = 50
            me.tip = '难度再次加大!敌机血量50滴'
            ybc_game.delay(tip_clear,5)
        '''
        if TNT.chuxian:
            me.tip = '发射器冷却中，请稍后'
            ybc_game.delay(tip_clear,5)
            TNT.draw()
            a = TNT.angle
            TNT.x += cos(radians(a))*70
            TNT.y += -sin(radians(a))*70
            if TNT.collide(dj):
                TNT.chuxian = False
                ybc_game.play_sound('boom',1)
                me.score = False
                TNT.x = me.x
                TNT.y = me.y
                dj.blood = 30
                boom.cx = True
                boom.x = dj.x
                boom.y = dj.y
                ybc_game.delay(boom_cx,3)
                dj.x = 3000
            if not TNT.collide(sky):
                TNT.chuxian = False
                me.score -= 1
                TNT.x = me.x
                TNT.y = me.y
        if dj.blood <= 0:
            dj.blood = 20
            dj.x = 2100
        if me.dong <= 0: me.dong = 0
        me.dong -= 0.1
        if me.speed < 0:
            me.speed = 0
        if me.way > 300:
            dj.draw()
        if setting.add:
            ybc_game.title('剩余路程:'+str(round(me.way,1)))
        ybc_game.timer(dj_cx,3)
        if dj.cx:
            if dj.x > me.x:
                dj.x -= 2
                #对于现代化设备的电脑可能有点不太友好
            if dj.y > me.y:
                dj.y -= 0.1
            if dj.y < me.y:
                dj.y += 0.1
            if dj.x <= -100:
                dj.x = 2000
                dj.y = dj.pos_y
            dj.angle = radians(-dj.angle_to(me))
        if not setting.com:
            if mouse.pos[0] > me.x:
                me.dong += 1
            if mouse.pos[0] < me.x:
                me.dong -= 3
                me.speed -= 5
            if me.speed <= 0:
                me.speed = 0
            if mouse.pos[1] < me.y and me.dong > 20:
                line.y += 10
                sea.y += 10
                TNT.y += 10
                me.heigh += me.angle/20
            if mouse.pos[1] > me.y and not me.collide(line):
                if(me.way > 300 and me.heigh <= 300):line.y -= 10
                sea.y -= 10
                TNT.y -= 10
                me.heigh -= me.angle/20
            if me.angle_to(way) < 30 and me.angle_to(way) > -30:me.angle = me.angle_to(way)
            if me.heigh >= 300 or me.way > me.away - 100:
                sea.y = 1500
            else:
                sea.draw()
                sea.y = 1000
                line.y = 2000
            if me.angle_to(way) > -30 and me.angle_to(way) < 30:
                me.angle = me.angle_to(way)
        if setting.com:
            if keyboard.right:
                me.dong += 1
            if keyboard.left:
                me.dong -= 3
                me.speed -= 5
            if me.speed <= 0:
                me.speed = 0
            if keyboard.up and me.dong > 20 and me.angle < 32:
                line.y += 10
                me.angle += 2
                sea.y += 10
                TNT.y += 10
                me.heigh += me.angle/20
            if keyboard.down and not me.collide(line) and me.angle > -32:
                if(me.way > 300 and me.heigh <= 300):line.y -= 10
                sea.y -= 10
                me.angle -= 2
                TNT.y -= 10
                me.heigh -= me.angle/20
            if me.heigh >= 300 or me.way > me.away - 200:
                sea.y = 1500
            else:
                sea.draw()
                sea.y = 1000
                line.y = 2000
            setting.aset.x = 1870
            setting.aset.draw()
            if mouse_collide(setting.aset) and mouse.left:
                me.state = 'set'
        me.y += 0.036
        if me.y >= 900:me.y = 900
        if me.heigh >= 20000 and me.image == '我机': 
            me.heigh -= round(me.speed/1000,1)*round(me.angle/20,1)
        if me.height >= 16000 and me.image == 'L1':
            me.heigh -= round(me.speed/1000,1)*round(me.angle/20,1)
        if me.height >= 24000 and me.image == 'L3':
            me.heigh -= round(me.speed/1000,1)*round(me.angle/20,1)
        if me.heigh >= 3000 and me.heigh <= 6000:
            yun.draw()
            yun.x -= me.speed/500
            if yun.x <= 0:
                yun.x = 2000
        if not me.collide(line): me.heigh += round(me.speed/1000,1)*round(me.angle/20,1)
        me.y -= me.angle/10
        if me.heigh >= 8000: me.heigh == 7900
        if me.heigh > 0 and not me.collide(line): me.heigh -= 0.3
        if me.speed >= 3200 and me.image == 'L1':
            me.speed = 3200
        if me.speed >= 3600 and me.image == '我机':
            me.speed = 3600
        if me.speed >= 4000 and me.image == 'L3':
            me.speed = 4000
        if me.y <= 300:
            me.y = 300
        if not me.collide(line): me.way -= round(me.speed/3600,1)
        if line.right < 0 and me.heigh <= 300 and me.way > 300:
            sea.draw()
            sea.y = 1500#if me.heigh <= 0 and line.right < 0 and me.way > 300:#   sea.y = me.y
        if me.rw == 1 or me.rw == 2:
            wind.draw()
            me.angle += random.randint(-5,5)
            for i in me.dark_list:
                i.angle += random.randint(-5,5)
            for i in dj.dark_list:
                i.x = random.randint(-10,10)
            dj.x += random.randint(-10,10)
            dj.y += random.randint(-10,10)
            ybc_game.timer(show_r,1)
            ybc_game.cancel(show_s)
        else:
            ybc_game.timer(show_s,1)
            ybc_game.cancel(show_r)
        if sea.collide(me) and me.way > 300:
            me.state = '失败' 
            print('400')
            boom.cx = True
            boom.x = me.x
            boom.y = me.y
            ybc_game.play_sound('boom',1)
            ybc_game.delay(boom_cx,3)
            sea.draw()
            sea.y = 1000
        if dj.collide(me) and me.way > 300:
            me.state = '失败'
            boom.cx = True
            print('401')
            boom.x = me.x
            boom.y = me.y
            ybc_game.play_sound('boom',1)
            ybc_game.delay(boom_cx,3)
            dj.y = 3000
        if me.blood <= 0:
            me.state = '失败'
            boom.cx = True
            print(402)
            boom.x = me.x
            boom.y = me.y
            ybc_game.play_sound('boom',1)
            ybc_game.delay(boom_cx,3)
        if me.way <= 300 and me.heigh <= 350:
            line.y = 950
            me.x+=me.sd
            if line.right <= 2000:
                line.left = 0
            sea.y = 1200
        if line.collide(me) and me.way <= 300:
            me.angle = 0
            me.y = 850
        ybc_game.timer(random_weather,10)
        ybc_game.timer(aaaaasupport,30)
        if me.way <= 0 and me.collide(line) and me.speed <= 0:
            me.state = '胜利'
    if me.state == '胜利': 
        win.draw()
        if me.image == 'L1':
            me.blood = me.mode['L1'][0]
            me.score = me.mode['L1'][1]
        elif me.image == '我机':
            me.blood = me.mode['L2'][0]
            me.score = me.mode['L2'][1]
        elif me.image == 'L3':
            me.blood = me.mode['L3'][0]
            me.score = me.mode['L3'][1]
        me.way = me.away
        line.x = 5000
        line.y = 950
        dj.x = 2100
        dj.y = 500
        xingshi.width = 1000
        me.x = 400
        sea.y = 1500
        me.dong = 0
        me.speed = 0
        me.y = 850
        dj.cx = True
        dj.dark_list.clear()
        me.dark_list.clear()
        me.win += 1
        me.cnt+=1
        me.money += 10000
        me.state = '开始'
    if boom.cx:
        boom.draw()
    elif me.state == '失败': 
        sky.draw()
        fail.draw()
        ybc_game.text('飞机可不防水，你下次不要掉下去，不要那么晚起飞',[1000,300],'red',40,'simsum.ttf')
        ybc_game.text('飞机很脆弱的，请不要和敌机相撞',[1000,500],'red',40,'simsum.ttf')
        ybc_game.text('飞机很脆弱的，下次请远离敌机子弹',[1000,700],'red',40,'simsum.ttf')
        ybc_game.text('重生中...',[1000,500],'yellow',50,'simsum.ttf')
        ybc_game.delay(chongsheng,5)
    if me.state == '重生':
        sky.draw()
        r1 = random.randint(0,5)
        print(r1)
        r = me.sty[r1]
        ybc_game.text('重生中，请稍后...',[1000,400],'yellow',50,'simsum.ttf')
        if r == 'L1':
            me.blood = me.mode['L1'][0]
            me.score = me.mode['L1'][1]
            me.image = 'L1'
        elif r == 'L2':
            me.blood = me.mode['L2'][0]
            me.score = me.mode['L2'][1]
            me.image = '我机'
        elif r == 'L3':
            me.blood = me.mode['L3'][0]
            me.score = me.mode['L3'][1]
            me.image = 'L3'
        me.way = 4008.6
        line.x = 5000
        line.y = 950
        dj.x = 2100
        dj.y = 500
        sea.y = 1500
        me.dong = 0
        me.heigh = 0
        me.speed = 0
        me.y = 850
        dj.cx = True
        dj.dark_list.clear()
        me.state = '开始'
    showbgm.draw()
    if showbgm.collide(way) and mouse.left and setting.bgm:
        ybc_game.stop_sound(me.play_bgm)
        r = random.randint(1,3)
        ybc_game.play_sound('bgm'+str(r),-1)
        me.play_bgm = 'bgm'+str(r)
    ybc_game.text('作者提示🔈:\n无不良引导，请仔细甄别',[1800,950],'orange',30)
def tip_clear():
    me.tip = ''
def fbs():
    me.fbs = me.cnt
    me.cnt = 0
def add_me_blood():
    if me.blood < 50:
        me.blood += 2
def aaaaasupport():
    me.score = True
def random_weather():
    me.rw = random.randint(1,10)
    print(me.rw)
def chongsheng():#英文不好，请谅解
    me.state = '重生'
def show_r():
    sky.image = 'rain'
def show_s():
    sky.image = '蓝天'
def djdraw():
    if me.state == '运行':
        d1 = ybc_game.actor('敌军子弹',[dj.x,dj.y])
        d1.width = 30
        d1.height = 10
        d1.a = d1.angle_to(me)
        d1.angle = radians(-d1.angle_to(me))
        dj.dark_list.append(d1) 
    else:
        dj.center = [2100,400]
def dj_cx():
    dj.draw()
    dj.cx = True
def mouse_collide(actor1):
    if actor1.right > mouse.pos[0] and actor1.left < mouse.pos[0] and actor1.bottom > mouse.pos[1] and actor1.top < mouse.pos[1]:
        return True
    else:
        return False
def pos_pzt(p,top,bottom,left,right):
    if p[0] > left and p[0] < right and p[1] > top and p[1] < bottom and mouse.left:
        return True 
    else:
        return False
def on_mouse_up(pos):
    current_time = time()
    if me.state == 'set' and current_time - setting.last_click_time > 0.3:  # 点击冷却
        if setting.afbs.collidepoint(pos):
            setting.fbs = not setting.fbs
            setting.afbs.image = 'on' if setting.fbs else 'off'
            setting.last_click_time = current_time
            
        elif setting.aadd.collidepoint(pos):
            setting.add = not setting.add
            setting.aadd.image = 'on' if setting.add else 'off'
            setting.last_click_time = current_time
        elif setting.acom.collidepoint(pos):
            setting.com = not setting.com
            setting.acom.image = 'on' if setting.com else 'off'
            setting.last_click_time = current_time
        elif setting.abgm.collidepoint(pos):
            setting.bgm = not setting.bgm
            setting.abgm.image = 'on' if setting.bgm else 'off'
            setting.last_click_time = current_time
def on_key_down(key):
    global keys,on_key
    keys = key
    on_key = True
    if me.state == '运行':
        if key == 'space' and me.can_add_bull:
            d = ybc_game.actor('我军子弹',[me.x,me.y])
            d.width = 30
            d.height = 10
            d.angle = d.angle_to(way)
            me.dark_list.append(d)
            me.can_add_bull = False
            ybc_game.delay(clock_add_bull,0.2)
def on_key_up():
    global on_key
    on_key = False
def clock_add_bull():
    me.can_add_bull = True
def c_pz():
    pass
def dark_bj():
    for i in me.dark_list:
        if i.x >= 2000:
            me.dark_list.remove(i)
def dark():
    for i in me.dark_list:
        a = i.angle
        i.x += cos(radians(a))*20
        i.y += -sin(radians(a))*20
def dark_pz():
    for i in me.dark_list:
        if dj.collide(i):
            dj.blood -= 2
            i.x = 3000
        if dj.blood <= 0 and me.way > 300:
            dj.pos_y = random.randint(500,800)
            dj.blood = 30
            boom.cx = True
            boom.x = dj.x
            boom.y = dj.y
            ybc_game.play_sound('boom',1)
            ybc_game.delay(boom_cx,3)
            dj.x = 2100
def dj_dark_bj():
    for i in dj.dark_list:
        if i.x <= 0:
            dj.dark_list.remove(i)
def dj_dark():
    for i in dj.dark_list:
        a = i.angle_to(me)
        i.x += cos(radians(a))*10
        i.y += -sin(radians(a))*10
def dj_dark_pz():
    for i in dj.dark_list:
        if me.collide(i):
            me.blood -= 2
            i.x = 3000
        if me.blood <= 0:
            me.state = '失败'
def boom_cx(): 
    boom.cx = False
ybc_game.timer(update,1/1000)
ybc_game.go()