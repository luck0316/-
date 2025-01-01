import random
from datetime import datetime
from pyecharts.charts import Line, Bar, Graph
from pyecharts import options as opts
import easygraph as eg
import pandas as pd
import itertools

# 模拟东北三省主要城市的天气数据
cities = {
    '哈尔滨': {'province': '黑龙江'},
    '牡丹江': {'province': '黑龙江'},
    '齐齐哈尔': {'province': '黑龙江'},
    '佳木斯': {'province': '黑龙江'},
    '大庆': {'province': '黑龙江'},
    '长春': {'province': '吉林'},
    '吉林市': {'province': '吉林'},
    '沈阳': {'province': '辽宁'},
    '大连': {'province': '辽宁'},
    '鞍山': {'province': '辽宁'}
}

# 生成模拟天气数据
weather_data = []

for city, info in cities.items():
    # 模拟最高温度和最低温度
    high_temp = random.randint(-20, 10)  # 冬季温度范围
    low_temp = random.randint(-30, -10)  # 冬季温度范围
    avg_temp = (high_temp + low_temp) / 2

    weather_data.append({
        'city': city,
        'province': info['province'],
        'high_temp': high_temp,
        'low_temp': low_temp,
        'avg_temp': avg_temp
    })

# 将天气数据转换为DataFrame
df_weather = pd.DataFrame(weather_data)

# 打印模拟数据
print("模拟的天气数据：")
print(df_weather)

# 创建折线图
line_chart = (
    Line()
    .add_xaxis([row['city'] for _, row in df_weather.iterrows()])
    .add_yaxis("最高气温", [row['high_temp'] for _, row in df_weather.iterrows()], is_smooth=True)
    .add_yaxis("最低气温", [row['low_temp'] for _, row in df_weather.iterrows()], is_smooth=True)
    .set_global_opts(
        title_opts=opts.TitleOpts(title="东北三省城市天气预报"),
        toolbox_opts=opts.ToolboxOpts(is_show=True),
        xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-15))
    )
)

# 创建柱状图
average_temps = df_weather.groupby('province')['avg_temp'].mean().reset_index()

# 确保 avg_temp 是数值型
average_temps['avg_temp'] = pd.to_numeric(average_temps['avg_temp'], errors='coerce')

# 打印各省平均温度
print("各省平均温度：")
print(average_temps)

# 创建柱状图
bar_chart = (
    Bar()
    .add_xaxis([row['province'] for _, row in average_temps.iterrows()])
    .add_yaxis("平均气温", [row['avg_temp'] for _, row in average_temps.iterrows()])
    .set_global_opts(
        title_opts=opts.TitleOpts(title="东北三省平均温度"),
        yaxis_opts=opts.AxisOpts(name="温度 (°C)", axislabel_opts=opts.LabelOpts(formatter="{value}°C")),
        xaxis_opts=opts.AxisOpts(name="省份"),
        legend_opts=opts.LegendOpts(pos_top="5%"),
    )
    .set_series_opts(
        label_opts=opts.LabelOpts(is_show=True, position="insideTop", formatter="{c}°C")
    )
)

# 渲染图表
line_chart.render('line_chart.html')
bar_chart.render('bar_chart.html')

print("图表已生成并保存为HTML文件。")

# 如果需要生成城市网络图，可以使用以下代码
# 创建城市网络图
G = eg.Graph()

# 添加节点
for index, row in df_weather.iterrows():
    G.add_node(row['city'], temperature=row['avg_temp'])

# 计算城市间温度差并添加边
edges = []
for (i, row1), (j, row2) in itertools.combinations(df_weather.iterrows(), 2):
    temp_diff = abs(row1['avg_temp'] - row2['avg_temp'])
    edges.append((row1['city'], row2['city'], {'weight': temp_diff}))
    G.add_edge(row1['city'], row2['city'], weight=temp_diff)

# 绘制城市网络图
nodes = [{"name": node, "symbolSize": abs(G.nodes[node]['temperature']) * 5} for node in G.nodes]

links = [
    {"source": edge[0], "target": edge[1], "value": edge[2]['weight']}
    for edge in edges
]

graph_chart = (
    Graph()
    .add("", nodes, links, repulsion=8000)
    .set_global_opts(title_opts=opts.TitleOpts(title="东北三省城市气温相似性网络"))
)

# 渲染城市网络图
graph_chart.render('graph_chart.html')

print("城市网络图已生成并保存为HTML文件。")
