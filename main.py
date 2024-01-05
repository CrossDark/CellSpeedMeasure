from Compare import sql, main


if __name__ == '__main__':
    with sql.SQL() as mysql:
        mysql.tables('CellCirculation')
        mysql.info = 'Perfect'
        mysql + main(folder='/Volumes/home/Experiment/定量/细胞环流/数据/正式数据/2024.1.3/', point=['30.6'])
