from airflow.decorators import task, dag
from datetime import datetime


@task
def one():
    return "1"


@task
def two():
    return "2"


@task
def double(it):
    return 2 * it


@task
def add(one, other):
    return one + other


@task
def print_it(it):
    print(it)


@dag(start_date=datetime(1970, 1, 1), schedule_interval=None)
def my_dag():
    print_it(add(double(two()), double(one())))


the_dag = my_dag()
