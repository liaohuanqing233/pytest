import html_to_array as hta

if __name__ == '__main__':
    str11 = """
    <table>
    <tr><td>商品名称</td><td>价格</td><td>商品状态</td></tr>
    <tr><td>哈哈哈11</td><td>￥5,000</td><td>已上架</td></tr>
    <tr><td>哈哈哈12</td><td>￥1万5千</td><td>已下架</td></tr>
    </table>
    """
    data2 = hta.html_data(str11)
    print(data2)