from faker import Faker
from airium import Airium
import random

fake = Faker()

def generate_names(size):
    return [fake.name() for i in range(size)]

def generate_scores(metric_list):
    return[random.randint(1, 100) for i in range(len(metric_list))]

def save_file(html):
    with open('that/file/path.html', 'wb') as f:
        f.write(bytes(html))

def generate_cma_table(cma_names, cma_table_list, names):
    a = Airium()
    a('<!DOCTYPE html>')
    with a.html():
        with a.head():
            a.title(_t="CMA Table")

        with a.body():
            with a.table(id='table_1'):
                with a.tr(klass='header_row'):
                    a.td(_t='CMA Table')
                    for i in range(len(cma_names)):
                        a.td(_t='')
                with a.tr(klass='header_row'):
                    a.td(_t='Student Name')
                    for i in range(len(cma_names)):
                        a.td(_t=cma_names[i])
                for i in range(len(names)):
                    with a.tr():
                        a.td(_t=names[i])
                        for j in range(len(cma_table_list[0])):
                            a.td(_t=cma_table_list[i+1][j])
    html = str(a)  # casting to string extracts the value
    print(html)

def generate_qma_table(qma_names, qma_table_list, names):
    a = Airium()
    a('<!DOCTYPE html>')
    with a.html():
        with a.head():
            a.title(_t="QMA Table")
        with a.body():
            with a.table(id='table_2'):
                with a.tr(klass='header_row'):
                    a.td(_t='QMA Table')
                    for i in range(len(qma_names)):
                        a.td(_t='')
                with a.tr(klass='header_row'):
                    a.td(_t='Student Name')
                    for i in range(len(qma_names)):
                        a.td(_t=qma_names[i])
                for i in range(len(names)):
                    with a.tr():
                        a.td(_t=names[i])
                        for j in range(len(qma_table_list[0])):
                            a.td(_t=qma_table_list[i + 1][j])
    html = str(a)  # casting to string extracts the value
    print(html)

def generate_main_report(qma_names, qma_table_list, cma_names, cma_table_list, names):
    a = Airium()
    a('<!DOCTYPE html>')
    with a.html():
        with a.head():
            a.title(_t="Main Report")
        with a.body():
            with a.table(id='table_2'):
                with a.tr(klass='header_row'):
                    a.td(_t='Quality Metric Analysis (QMA)')
                    a.td(_t='')
                with a.tr():
                    a.td(_t='Name')
                    a.td(_t='')
                for i in range(len(qma_names)):
                    with a.tr():
                        a.td(_t=qma_names[i])
                        a.td(_t='Threshold bar here')

            with a.table(id='table_2'):
                with a.tr(klass='header_row'):
                    a.td(_t='Convention Metric Analysis (CMA)')
                    a.td(_t='')
                with a.tr():
                    a.td(_t='Name')
                    a.td(_t='')
                for i in range(len(cma_names)):
                    with a.tr():
                        a.td(_t=cma_names[i])
                        a.td(_t='Threshold bar here')

    html = str(a)  # casting to string extracts the value
    print(html)

def main():
    names = generate_names(20)

    qma_names = ['CC', 'SLOC', 'CP', 'WMC', 'DIT', 'CBO']
    cma_names = ['Class naming', 'Method Naming', 'Source Naming', 'Javadoc']

    qma_table_list = []
    cma_table_list = []

    qma_table_list.append(qma_names)
    for i in range(len(names)):
        qma_table_list.append(generate_scores(qma_names))

    cma_table_list.append(cma_names)
    for i in range(len(names)):
        cma_table_list.append(generate_scores(cma_names))

    # generate_qma_table(qma_names, qma_table_list, names)
    # generate_cma_table(cma_names, cma_table_list, names)
    generate_main_report(qma_names, qma_table_list, cma_names, cma_table_list, names)

    method_name = 'public ClassName methodName(){'
    var_name = 'int varName;'
    class_name = 'Class ClassName{'

if __name__ == '__main__':
    main()
