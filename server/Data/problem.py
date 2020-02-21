from hashlib import md5

path_checked_file = './DB/Problems/Checked'
path_not_checked_file = './DB/Problems/Not Checked'
checked_problem = {}
not_checked_problem = {}


def get_file_name(text):
    name = text.replace('\n', ' ').strip()
    return md5(name.encode('utf8')).hexdigest() + '.json'


def add_problem(obj):
    global all_problem
    file_name = get_file_name(obj['text'])
    if file_name in all_problem:
        return None

    pass


def get_problem(my_filter):
    pass
