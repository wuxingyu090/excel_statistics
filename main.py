from src.data_interaction.os_path import OsPathClass
from src.excel_process.excel_general import ExcelGeneralClass
import src.match_process.match_keycount as keycount
import click

def chart_product(config_keycount,rule_table):
    input_file = config_keycount + '.xlsx'
    output_file = rule_table + '.xlsx'
    # 获取配置数据
    ospath = OsPathClass(input_file=input_file,
                         output_file=output_file)
    input_file = ospath.input_path()
    output_file = ospath.output_path()
    input_data = ExcelGeneralClass(
        file=input_file, sheet=rule_table).read_data()

    # 获取统计数据
    data = keycount.cycle_statistics(input_data)

    # 统计数据整合
    detail_sheet = [{item['count_name']: item['count_data']} for item in data]
    count = [{'count_name': item['count_name'], 'count_row': item['count_row'],
              'count_num': item['count_num']} for item in data]
    count_sheet = [{'计数统计': count}]
    all_sheet = count_sheet + detail_sheet
    Archive = ExcelGeneralClass(file=output_file)
    Archive.write_data(all_sheet)

    # 图表制作
    Graph = ExcelGeneralClass(file=output_file, sheet='计数统计')
    Graph.chart_data()


def show_chart(rule_table):
    output_file = rule_table + '.xlsx'
    # 获取配置数据
    ospath = OsPathClass(output_file=output_file)
    file = ospath.output_path()
    Graph = ExcelGeneralClass(file=file, sheet='计数统计')
    # 绘制折线图
    Graph.show_graph(rule_table)


@click.command()
@click.option('--show', default=False, help='show 参数，默认False，不直接输出图表' ,type=bool)
def run(show):
    rule_table_list = ['count_rule', 'count_rule1', 'count_rule2']
    config_keycount = 'config-keycount'
    for rule_table in rule_table_list:
        chart_product(config_keycount, rule_table)
        if show:
            show_chart(rule_table)
        else:
            pass
        
def main():
    run()

if __name__ == "__main__":
    main()
