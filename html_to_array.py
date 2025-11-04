from bs4 import BeautifulSoup

str1 = """
<table>
    <tr><td>商品名称</td><td>价格</td><td>商品状态</td></tr>
    <tr><td>哈哈哈11</td><td>￥5,000</td><td>已上架</td></tr>
    <tr><td>哈哈哈12</td><td>￥1万5千</td><td>已下架</td></tr>
    </table>
"""
soup = BeautifulSoup(str1, 'html.parser')
table = soup.find('table')
headers = ["商品名称", "价格", "商品状态"]
price_format = "￥"
# 提取行数据
table_data = [headers]
# 跳过表头行
for row in table.find_all('tr')[1:]:
    cells = row.find_all('td')
    row_data = []
    for i, cell in enumerate(cells):
        # 去掉前后空格
        cell_str = cell.text.strip()
        if price_format in cell_str:
            # 字符替换
            cell_str = cell_str.replace(",", "")
            cell_str = cell_str.replace(price_format, "")
            # 判断金额是否为纯数字
            if not cell_str.isdigit():
                number = 0
                # 包含万的话就乘10000
                if "万" in cell_str:
                    number = 10000
                    cell_str = cell_str.replace("万", "")
                # 包含千的话就乘1000，覆盖掉万
                if "千" in cell_str:
                    number = 1000
                    cell_str = cell_str.replace("千", "")
                cell_str = int(cell_str)
                price = cell_str * number
            else:
                # 纯数字直接int化
                price = int(cell_str)
            cell_str = price
        # 将td内容添加在tr内容下
        row_data.append(cell_str)
    # 将tr一列数据添加到数据列表
    table_data.append(row_data)
print(table_data)
