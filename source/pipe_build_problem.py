# coding:utf-8

# python序列化存储
try:
    import cPickle as pickle
except ImportError:
    import pickle
# python json
import json
import sys
# python draw
import drawGraph as dg
# Graph class
import graph

# -------------------coding begin------------------- #

MAX = sys.maxsize

# 结构化graphData图的信息
graphData = {
    'nodeW': []  # 存储图的邻接矩阵
}
# 用户输入图信息
print 'Please input the community number:'
communityNum = raw_input()

print 'Pealse input the community relation(-1 means infinite or itself):'
communityRelation = []
for i in range(int(communityNum)):
    print 'The', i+1, 'line'
    line = []
    for j in range(int(communityNum)):
        graphW = raw_input()
        if(int(graphW) == -1):
            line.append(MAX)
        else:
            line.append(int(graphW))
    graphData['nodeW'].append(line)

# graphData['nodeW'] = [[MAX,  10, MAX, MAX, MAX,  11, MAX, MAX, MAX],
#                       [10,  MAX,  18, MAX, MAX, MAX,  16, MAX,  12],
#                       [MAX,  18, MAX,  22, MAX, MAX, MAX, MAX,   8],
#                       [MAX, MAX,  22, MAX,  20, MAX, MAX,  16,  21],
#                       [MAX, MAX, MAX,  20, MAX,  26,   7,  19, MAX],
#                       [11,  MAX, MAX, MAX,  26, MAX,  17, MAX, MAX],
#                       [MAX,  16, MAX, MAX,   7,  17, MAX,  19, MAX],
#                       [MAX, MAX, MAX,  16,  19, MAX,  19, MAX, MAX],
#                       [MAX,  12,   8,  21, MAX, MAX, MAX, MAX, MAX]]

# 创建图对象
communityGraph = graph.Graph(graphData)
# 调用 Graph class 的 prime 方法
communityGraph.prime()
# 结构化存储到文件
inputFile = {
    'graphData': communityGraph.getGraphData(),
    'primeResult': {
        'sum': communityGraph.getSum(),
        'mid': communityGraph.getMid()
    }
}
# 将数据存入文件
with open('data.json', 'w') as f:
    json.dump(inputFile, f) # 序列化保存

# 从文件读取结构化数据
with open('data.json', 'r') as f:
    # fromFile = pickle.load(f)  # 反序列化读取
    fromFile = json.load(f)
    print '--------------------from file---------------------'
    print fromFile

# 询问是否作图
print 'Draw the graph?(Y/N):'
ans = raw_input()
if (ans == 'Y'):
    dg.t.hideturtle()
    communityGraph.drawGraph()
