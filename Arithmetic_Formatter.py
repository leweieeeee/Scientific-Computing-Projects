def arithmetic_arranger(problems, show_answers=False):
    if len(problems) <= 5:
        return format_output(problems,show_answers)
    else:
        return('Error: Too many problems.')
        

def separate_values(problems):
    num_1, operator, num_2 = problems.split()
    if operator not in ["+","-"]:
        return("Error: Operator must be '+' or '-'.")
    if len(num_1)>4 or len(num_2)>4:
        return('Error: Numbers cannot be more than four digits.')
    if not num_1.isdigit() or not num_2.isdigit():
        return ('Error: Numbers must only contain digits.')
    else:   
        num_1 = int(num_1)
        num_2 = int(num_2)
        return([num_1,operator,num_2])

def output_row_1(index,num_1,max_len):
    string = spacing(index)
    string += f'{num_1}'.rjust(max_len)
    return string

def output_row_2(index,operator,num_2,max_len):
    string =spacing(index)
    string += f'{operator}'+f'{num_2}'.rjust(max_len-1)
    return string

def output_row_3(index,max_len):
    string =spacing(index)
    for i in range(max_len):
        string += "-" 
    return string

def output_row_4(index,num_1,operator,num_2,max_len):
    string = spacing(index)
    if operator == '+':
        answer = (num_1) + (num_2) 
    if operator == '-':
        answer = (num_1) - (num_2)  
    string += f'{answer}'.rjust(max_len)
    return(string)

def spacing(index):
    string = ''
    if index != 0:
        string += ' '*4
    return string

def format_output(problems,show_answers):
    row_1 = ''
    row_2 = ''
    row_3 = ''
    row_4 = ''
    for index, question in enumerate(problems):
        question = separate_values(question)
        if type(question) == str:
            return(question)
        else:
            num_1,operator,num_2 = question
            max_len = max(len(str(num_1)),len(str(num_2))) + 2
            row_1 += output_row_1(index, num_1,max_len)
            row_2 += output_row_2(index, operator,num_2,max_len)
            row_3 += output_row_3(index, max_len)
            if show_answers:
                row_4+= output_row_4(index,num_1,operator,num_2,max_len)
    string = row_1 + '\n' + row_2 + '\n' + row_3
    if show_answers:
        string +='\n' + row_4
    return string

print(arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True))