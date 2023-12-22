from Compare import compare, sql


if __name__ == '__main__':
    with sql.SQL() as mysql:
        mysql.tables('CellCirculation')
        mysql + compare(folder='/Volumes/home/Experiment/定量/细胞环流/数据/校准数据/', point=['speed-plus', 'speed-pro'])
