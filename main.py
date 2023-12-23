from Compare import sql, main


if __name__ == '__main__':
    with sql.SQL() as mysql:
        mysql.tables('CellCirculation')
        mysql.info = '3'
        mysql + main(folder='/Volumes/home/Experiment/定量/细胞环流/数据/正式数据/2023.12.19/3/照片')
