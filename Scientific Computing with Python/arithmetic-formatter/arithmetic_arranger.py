def arithmetic_arranger(problems,display=False):
  if len(problems) > 5:
    return 'Error: Too many problems.'
  problems = [i.split(' ') for i in problems]
  if not all([i[1] in ['+','-'] for i in problems]):
    return 'Error: Operator must be \'+\' or \'-\'.'
  if not all([i[0].isdigit() and i[2].isdigit() for i in problems]):
    return 'Error: Numbers must only contain digits.'
  if not all([len(str(i[0]))<5 and len(str(i[2]))<5 for i in problems]):
    return 'Error: Numbers cannot be more than four digits.'
  max_length = [max(len(i[0]),len(i[2])) for i in problems]
  arranged_problems = '    '.join([(2+max_length[i]-len(problems[i][0]))*' '+problems[i][0] for i in range(len(problems))])+'\n'
  arranged_problems = arranged_problems+'    '.join([problems[i][1]+' '+(max_length[i]-len(problems[i][2]))*' '+problems[i][2] for i in range(len(problems))])+'\n'
  arranged_problems = arranged_problems+'    '.join([(2+max_length[i])*'-' for i in range(len(problems))])
  if display:
    r = [str(int(i[0])+int(i[2])) if i[1]=='+' else str(int(i[0])-int(i[2])) for i in problems]
    arranged_problems = arranged_problems+'\n'+'    '.join([(2+max_length[i]-len(r[i]))*' '+r[i] for i in range(len(problems))])
  return arranged_problems