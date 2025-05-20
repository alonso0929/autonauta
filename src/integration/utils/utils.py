def extract_table_data(table, keys):
    rows = table.find_all("tr")[1:]
    data = []

    for row in rows:
        cells = row.find_all("td")

        if len(cells) == len(keys):
            data.append({key: cell.text.strip() for key, cell in zip(keys, cells)})

    return data