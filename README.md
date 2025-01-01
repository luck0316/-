# 东北三省城市天气预报可视化项目

## 项目概述
本项目通过模拟东北三省主要城市的天气数据，并使用 Python 的数据可视化库 `pyecharts` 和图计算库 `easygraph` 来生成和展示天气数据的折线图、柱状图和网络图。

## 实现过程

### 数据模拟
我们首先模拟了东北三省主要城市的天气数据，包括每个城市的最高气温、最低气温和平均气温。这些数据是使用 Python 的 `random` 模块生成的，以模拟冬季的温度范围。

### 数据处理
使用 `pandas` 库将模拟的天气数据转换为 DataFrame，这使得数据的组织和后续分析变得更加方便。

### 折线图生成
利用 `pyecharts` 的 `Line` 类创建折线图，展示各城市的最高气温和最低气温。图表的全局配置包括标题、工具箱和 X 轴标签的旋转。

### 柱状图生成
计算每个省份的平均气温，并使用 `pyecharts` 的 `Bar` 类创建柱状图。图表的全局配置包括标题、Y 轴和 X 轴的名称以及图例的位置。

### 网络图生成
使用 `easygraph` 创建城市网络图，展示城市间的气温相似性。节点代表城市，边代表城市间的气温差异。

### 图表渲染
将生成的图表渲染为 HTML 文件，方便在浏览器中查看。

## 技术细节

- **数据模拟**：使用 `random` 库生成随机温度数据。
- **数据处理**：使用 `pandas` 库进行数据的组织和计算。
- **数据可视化**：
  - 使用 `pyecharts` 创建折线图和柱状图，展示城市的天气数据。
  - 使用 `easygraph` 创建网络图，展示城市间的气温相似性。
- **图表渲染**：将图表保存为 HTML 文件，便于在 Web 环境中展示。

## 结论
本项目通过模拟数据和数据可视化技术，成功展示了东北三省城市的天气情况，并通过图表的形式直观地呈现了数据。这种方法可以应用于实际的天气数据分析，为决策提供支持。
