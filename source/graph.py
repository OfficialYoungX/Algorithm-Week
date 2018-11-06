# coding:utf-8
import sys
import drawGraph as dg

MAX = sys.maxsize

class Graph(object):

    def __init__(self, graphData={'nodeW': []}):
        self.__graphData = graphData
        self.__nodeW = self.__graphData['nodeW']
        self.__nodeNum = len(graphData['nodeW'])
        self.__mid = []  # 存储生成最小代价生成树的信息
        self.__sum = 0  # 最小代价
        self.__charArray = []
        for i in range(self.__nodeNum):
            self.__charArray.append(str(i))

    def prime(self):
        if(self.__nodeNum<=0):
            return;
        charArray = self.__charArray
        primgraph = self.__nodeW

        mid = self.__mid
        mid.append(0)

        charlist = []
        charlist.append(charArray[0])

        lowcost = []  # lowcost[i]表示生成树集合中与点i最近的点构成的边最小权值 ，-1表示i已经在生成树集合中
        lowcost.append(-1)

        n = self.__nodeNum
        for i in range(1, n):  # 初始化mid数组和lowcost数组
            lowcost.append(primgraph[0][i])
            mid.append(0)

        for _ in range(1, n):  # 插入n-1个结点
            minid = 0
            min = MAX
            for j in range(1, n):  # 寻找每次插入生成树的权值最小的结点
                if(lowcost[j] != -1 and lowcost[j] < min):
                    minid = j
                    min = lowcost[j]
            # charlist.append(charArray[minid])
            print(charArray[mid[minid]]+'——' +
                  charArray[minid]+'权值：'+str(lowcost[minid]))
            self.__sum += min
            lowcost[minid] = -1 # 标记为在生成树中
            for j in range(1, n):  # 更新插入结点后lowcost数组和mid数组值
                if(lowcost[j] != -1 and lowcost[j] > primgraph[minid][j]):
                    lowcost[j] = primgraph[minid][j]
                    mid[j] = minid
        print "sum=", str(self.__sum)

    def getMid(self):
        return self.__mid

    def getGraphData(self):
        return self.__graphData
      
    def getSum(self):
      return self.__sum

    # 将图可视化
    def drawGraph(self):
        if(self.__nodeNum<=0):
            return;
        mid = self.__mid
        graphData = self.__graphData
        nodeNum = self.__nodeNum
        # 坐标点的定义
        pos = [(-300, 0), (-260, 150), (-150, 260), (0, 300),
               (150, 260), (260, 150), (300, 0), (260, -150),
               (150, -260), (0, -300), (-150, -260), (-260, -150),
               (-130, 130),(0, 180),(130, 130),(180, 0),
               (130, -130),(0, -180),(-130, -130),(-180, 0)]
        # 节点绘制
        for i in range(nodeNum):
            dg.drawNode(pos[i][0], pos[i][1], str(i))
        # 连线、权值
        for i in range(nodeNum):
            for j in range(nodeNum):
                if(graphData['nodeW'][i][j] != MAX):
                    dg.drawLine(pos[i], pos[j], '#10316B')
                    dg.drawText(
                        (pos[i][0]+pos[j][0])/2, (pos[i][1]+pos[j][1])/2, str(graphData['nodeW'][i][j]))
        # 最小代价生成树
        for i in range(1, len(mid)):
            dg.t.pensize(2)
            dg.drawLine(pos[i], pos[mid[i]], '#E4AD14')
            dg.drawText((pos[i][0]+pos[mid[i]][0])/2, (pos[i][1] +
                                                       pos[mid[i]][1])/2, str(graphData['nodeW'][i][mid[i]]), "#10316B")
        # 打印总费用
        Str = "sum="+str(self.__sum)
        dg.drawText(-450, -300, Str)
        dg.t.done()
