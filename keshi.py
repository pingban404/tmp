import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patheffects as path_effects

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False

def clean_and_convert_data(df, x_column=None):
    """
    清理和转换数据
    
    参数:
    df: DataFrame - 原始数据
    x_column: str - X轴列名
    
    返回:
    DataFrame - 清理后的数据
    """
    df_cleaned = df.copy()
    
    print("=== 数据清理和转换 ===")
    print(f"原始数据形状：{df_cleaned.shape}")
    
    # 1. 处理空值 - 如果某行除了时间列都为空，则删除该行
    if x_column and x_column in df_cleaned.columns:
        # 获取除了时间列外的所有列
        other_columns = [col for col in df_cleaned.columns if col != x_column]
        
        # 检查每行是否除了时间列外都为空
        rows_to_drop = []
        for idx, row in df_cleaned.iterrows():
            # 检查除了时间列外的所有列是否都为空
            other_values = row[other_columns]
            if other_values.isna().all() or (other_values == '').all():
                rows_to_drop.append(idx)
        
        if rows_to_drop:
            print(f"删除 {len(rows_to_drop)} 行空数据：{rows_to_drop}")
            df_cleaned = df_cleaned.drop(rows_to_drop)
    
    # 2. 数据类型转换 - 尝试将非数值列转换为数值类型
    converted_columns = []
    for column in df_cleaned.columns:
        if column != x_column:  # 跳过时间列
            if df_cleaned[column].dtype == 'object':
                # 尝试转换为数值类型
                try:
                    # 处理可能的特殊字符（如逗号、百分号等）
                    temp_series = df_cleaned[column].astype(str)
                    temp_series = temp_series.str.replace(',', '').str.replace('%', '').str.replace('¥', '')
                    temp_series = temp_series.str.strip()
                    
                    # 尝试转换为数值
                    converted = pd.to_numeric(temp_series, errors='coerce')
                    
                    # 如果转换成功且不是全部为空，则应用转换
                    if not converted.isna().all():
                        df_cleaned[column] = converted
                        converted_columns.append(column)
                        print(f"列 '{column}' 已转换为数值类型")
                    else:
                        print(f"列 '{column}' 无法转换为数值类型（全部为空或无效值）")
                except Exception as e:
                    print(f"列 '{column}' 转换失败：{e}")
    
    print(f"转换了 {len(converted_columns)} 个列为数值类型：{converted_columns}")
    print(f"清理后数据形状：{df_cleaned.shape}")
    
    return df_cleaned

def create_dynamic_combined_chart(df, x_column=None, output_filename="default.png", 
                                 width=15, height=8, transparent=True, show_markers=True,
                                 chart_type_dict=None):
    """
    创建通用的柱状图+折线图组合
    
    参数:
    df: DataFrame - 包含数据的DataFrame
    x_column: str - 用于X轴的列名，如果为None则使用索引
    output_filename: str - 输出文件名
    width: float - 图片宽度（英寸）
    height: float - 图片高度（英寸）
    transparent: bool - 是否使用透明背景
    show_markers: bool - 是否显示折线图的标记点
    chart_type_dict: dict - 指定每个列使用柱状图还是折线图，格式：{'列名': 'bar'/'line'/'both'}
                      'bar': 柱状图, 'line': 折线图, 'both': 柱状图+折线图, 未指定的列默认使用柱状图
    """
    
    # 清理和转换数据
    df = clean_and_convert_data(df, x_column)
    
    # 获取所有数值列（排除非数值类型）
    numeric_columns = df.select_dtypes(include=[np.number]).columns.tolist()
    
    if len(numeric_columns) == 0:
        print("错误：没有找到数值类型的列")
        return
    
    # 如果指定了X轴列，从数值列中移除它
    if x_column and x_column in numeric_columns:
        numeric_columns.remove(x_column)
    
    # 处理图表类型字典
    if chart_type_dict is None:
        chart_type_dict = {}
    
    # 分离柱状图和折线图的列
    bar_columns = []
    line_columns = []
    
    for column in numeric_columns:
        chart_type = chart_type_dict.get(column, 'bar')  # 默认使用柱状图
        chart_type = chart_type.lower()
        
        if chart_type == 'line':
            line_columns.append(column)
        elif chart_type == 'both':
            bar_columns.append(column)
            line_columns.append(column)
        else:  # 'bar' 或未指定
            bar_columns.append(column)
    
    print(f"检测到的数值列：{numeric_columns}")
    print(f"柱状图列：{bar_columns}")
    print(f"折线图列：{line_columns}")
    print(f"数据形状：{df.shape}")
    print(f"图片尺寸：{width} x {height} 英寸")
    print(f"透明背景：{'是' if transparent else '否'}")
    print(f"显示标记点：{'是' if show_markers else '否'}")
    
    # 创建图表
    fig, ax1 = plt.subplots(figsize=(width, height))
    ax2 = ax1.twinx()
    
    # 设置透明背景
    if transparent:
        fig.patch.set_alpha(0.0)
        ax1.patch.set_alpha(0.0)
        ax2.patch.set_alpha(0.0)
    
    # 设置柱状图参数
    x_pos = np.arange(len(df))
    width_bar = 0.8 / max(len(bar_columns), 1)  # 动态调整柱宽
    
    # 颜色列表
    colors = ['skyblue',  'orange', 'purple', 'brown', 'pink', 'gray', 'olive', 'cyan',
              'magenta', 'gold', 'lime', 'teal', 'indigo', 'violet', 'maroon', 'navy', 'coral', 'crimson',
              'darkgreen', 'plum', 'chocolate', 'steelblue', 'yellowgreen', 'salmon', 'turquoise', 'orchid',
              'khaki','sienna','red','lightgreen']
    
    # 绘制柱状图
    bars = []
    for i, column in enumerate(bar_columns):
        color = colors[i % len(colors)]
        bar = ax1.bar(x_pos + i * width_bar - (len(bar_columns) - 1) * width_bar / 2, 
                     df[column], width_bar, label=column, color=color, alpha=0.7)#柱状图透明度降低
        bars.append(bar)
    
    # 绘制折线图（在柱状图上面）
    lines = []
    #样式选择
    markers = ['o', 's', '^', 'd', 'v', '<', '>', 'p', '*', 'h']
    for i, column in enumerate(line_columns):
        color = colors[i % len(colors)]
        
        # 根据show_markers参数决定是否显示标记点
        if show_markers:
            marker = markers[i % len(markers)]
            markersize = 4
            markeredgecolor = 'white'
            markeredgewidth = 1.0
        else:
            marker = None
            markersize = 0
            markeredgecolor = None
            markeredgewidth = 0
        
        # 绘制折线图，使用更强的对比度
        line = ax2.plot(x_pos, df[column], color=color, marker=marker,
                       linewidth=3, markersize=markersize, label=f'{column}趋势',
                       markeredgecolor=markeredgecolor, markeredgewidth=markeredgewidth,  # 标记点描边
                       path_effects=[path_effects.withStroke(linewidth=5, foreground='white')])  # 更强的白色描边
        lines.append(line)
    
    # 设置标签和标题
    if x_column:
        ax1.set_xlabel(x_column)
    else:
        ax1.set_xlabel('数据点')
    ax1.set_ylabel('数值', color='black')
    ax2.set_ylabel('趋势值', color='gray')
    
    # 动态生成标题
    all_columns = list(set(bar_columns + line_columns))  # 去重
    if len(all_columns) <= 3:
        title = f"{'、'.join(all_columns)}数据分析 (柱状图+折线图)"
    else:
        title = f"多维度数据分析 (柱状图+折线图) - {len(all_columns)}个指标"
    
    plt.title(title)
    
    # 设置x轴标签
    if x_column and x_column in df.columns:
        # 使用指定的列作为X轴标签
        x_labels = df[x_column]
        if len(df) <= 20:  # 如果数据点不多，显示所有标签
            ax1.set_xticks(x_pos)
            ax1.set_xticklabels(x_labels, rotation=45, ha='right')
        else:  # 如果数据点很多，只显示部分标签
            step = max(1, len(df) // 10)  # 最多显示10个标签
            ax1.set_xticks(x_pos[::step])
            ax1.set_xticklabels(x_labels.iloc[::step], rotation=45, ha='right')
    else:
        # 使用索引作为X轴标签
        if len(df) <= 20:  # 如果数据点不多，显示所有标签
            ax1.set_xticks(x_pos)
            ax1.set_xticklabels(df.index, rotation=45, ha='right')
        else:  # 如果数据点很多，只显示部分标签
            step = max(1, len(df) // 10)  # 最多显示10个标签
            ax1.set_xticks(x_pos[::step])
            ax1.set_xticklabels(df.index[::step], rotation=45, ha='right')
    
    # 添加网格
    ax1.grid(True, alpha=0.3)
    
    # 添加图例
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    
    # 合并图例
    all_lines = lines1 + lines2
    all_labels = labels1 + labels2
    
    # 如果图例太长，分两行显示
    if len(all_labels) > 6:
        ax1.legend(all_lines, all_labels, loc='upper left', bbox_to_anchor=(0, 1), ncol=2)
    else:
        ax1.legend(all_lines, all_labels, loc='upper left', bbox_to_anchor=(0, 1))
    
    plt.tight_layout()
    
    # 保存图片，支持透明背景
    plt.savefig(output_filename, dpi=300, bbox_inches='tight', 
                transparent=transparent, facecolor='none' if transparent else 'white')
    plt.close()
    
    print(f"已生成图表：{output_filename}")
    print(f"包含 {len(all_columns)} 个指标：{all_columns}")
    if x_column:
        print(f"X轴使用列：{x_column}")


if __name__ == '__main__':
    # 读取数据
    df = pd.read_excel('./Data.xlsx')
    
    print("数据概览：")
    print(df.head())
    print(f"\n数据形状：{df.shape}")
    print(f"列名：{list(df.columns)}")
    print(f"索引类型：{type(df.index)}")
    
    # 显示第一列（时间列）的数据
    # print(f"\n第一列数据：")
    # print(df.iloc[:, 0])
    
    # 将第一列转换为字符串类型
    first_column_name = df.columns[0]
    df[first_column_name] = df[first_column_name].astype(str)
    
    print(f"\n转换后的第一列数据类型：{df[first_column_name].dtype}")
    # print(f"转换后的第一列数据：")
    # print(df[first_column_name])
    
    # 创建动态图表，使用第一列作为X轴，设置透明背景和自定义尺寸
    print(f"\n使用第一列 '{first_column_name}' 作为X轴")
    
    # 可以根据需要调整这些参数
    image_width = 12   # 图片宽度（英寸）
    image_height = 6   # 图片高度（英寸）
    use_transparent = True  # 是否使用透明背景
    show_markers = True  # 是否显示折线图的标记点
    
    # 指定图表类型字典
    chart_types = {
        'GDP价值': 'both',  # 柱状图+折线图
        '趋势': 'line',   # 折线图
        # '投资额': 'bar',    # 柱状图
        # '消费额': 'line'    # 折线图
    }
    
    create_dynamic_combined_chart(df, x_column=first_column_name, 
                                 width=image_width, height=image_height, 
                                 transparent=use_transparent, show_markers=show_markers,
                                 chart_type_dict=chart_types)