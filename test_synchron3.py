# creattion temp table

extisting
table: a, fill
data
into
table
b;

project: dataset: table: a:
temp
table:

query = ' select * from project.dataset.a'

bq_client = b

###################################################################################################


select
sal
from eemployee

order
by
sal
desc
limit
1
offset
2

select
sal
from

(select sal,

dese rank()(oder
by
sal
desc) as sal_rank

from employee)

where
sal_rank = 2

##############################################################################################################3

table
size in bq.

sentence = 'most coomon in a senetence'

lsen = sentence.split(" ")
ssen = set(lsen)
max_count = 0
for i in ssen:
    temp_count = lsen.count(i)
    if temp_count > max_count:
        max_count = temp_count

print(max_count)

from threading import thread

thread1 = threading.thread(target=abc)
thread2 = threading.thread(target=xyz)

thread.join()
thread.next()
########################################################################################

decorator
to
show
function
name and execution
time


def dec_gettime_func(func):
    def inner(name):
        startime = datetime.time.now()
        val = func(name)
        return val + sarttime

    return inner


@dec_gettime_func
def print_name(name):
    end_time = datetime.time.now()
    print(end_time)
    return name


#############################################3

merge
sort:

--------------------------------------------------------------------------------------------------

higher
order
function

write
a
program
to

dag1
task1, dag2, task2
ymdhms
** *1 **








