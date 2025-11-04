from bs4 import BeautifulSoup

def html_data(str1):
    soup = BeautifulSoup(str1, 'html.parser')
    table = soup.find('table')
    if not table:
        return []

    headers = ["商品名称", "价格", "商品状态"]

    # 提取行数据
    data = [headers]
    for j, row in table.find_all('tr')[1:]:  # 跳过表头行
        cells = row.find_all('td')
        row_data = []
        for i, cell in enumerate(cells):
            cell_str = cell.text.strip()
            if "￥" in cell_str:
                cell_str = format_price(cell_str)
            row_data.append(cell_str)
        data.append(row_data)

    return data

def format_price(price_str, price_format = "￥"):

    if price_format in price_str:

        price_str = price_str.replace(",", "")
        price_str = price_str.replace(price_format, "")

        if not price_str.isdigit():

            number = 0
            if "万" in price_str:
                number = 10000
                price_str = price_str.replace("万", "")
            if "千" in price_str:
                number = 1000
                price_str = price_str.replace("千", "")
            price_str = int(price_str)
            price = price_str * number

        else:

            price = int(price_str)

        return price

    else:
        return price_str