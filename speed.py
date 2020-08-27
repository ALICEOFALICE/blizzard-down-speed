# 帮下憨批暴雪算一下还有多久下载完毕
# 使用1024进率
# 初始化全局变量
GBMB = "1024"
# 请求用户输入对应参数
finish = input("您还需要下载的总量（单位为GB，允许小数点）")
speed = input("您的下载速度（单位为MB，允许小数点")
# 计算还有多久下载完毕
finishmb = float(finish) * float(GBMB)
time = float(finishmb) / float(speed)
print("还剩下", time,  "秒")
timemin = float(time) / 60
timeminmin = ('%.3f' % timemin)
print("还剩下", timeminmin, "分钟")
