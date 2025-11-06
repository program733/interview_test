temp_str = """

#1234 

I know? what i like, and i Like What I KNOW.

A sleep I shall Have

A rest I shall have!"""

#insert these lines into file , read using opps ,  get the frequecy of each word,
file_name = 'plain.txt'
with open(file_name,'w') as file:
    file.write(temp_str)

class ReadFile:
    def __init__(self,file_name):
        self.file_name = file_name

    @privatemethod
    def read_and_process(self):
        lines = []
        with open(file_name,'r') as file:
            line=file.readlines()
            lines.append(line)

        result = {}
        res = []
        for word in lines[0]:
            for subword in word.split(" "):
                if subword != "\n":
                    res.append(subword)


        temp_set = set(res)
        for i in temp_set:
            result[i]= res.count(i)
        print(result)

r = ReadFile('plain.txt')
r.read_and_process(r.file_name)

#https://leetcode.com/problems/word-search/
#https://leetcode.com/problems/linked-list-cycle/