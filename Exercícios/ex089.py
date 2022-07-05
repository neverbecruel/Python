todos = []
alunos = []
notas = []


while True:
    aluno = str(input('Nome: ')).strip()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    notas.append(nota1)
    notas.append(nota2)
    alunos.append(aluno)
    alunos.append(notas[:])
    todos.append(alunos[:])
    alunos.clear()
    notas.clear()
    resp = str(input('Quer continuar? [S/N] ')).lower().strip()[0]
    if resp == 'n':
        break
print(todos)
print('=-=' * 30)
print('Nº  NOME     MÉDIA ')
print('-' * 20)
for c in range(0, len(todos)):
    print(f'{c}   {todos[c][0]:<8} {(todos[c][1][0] + todos[c][1][1]) / 2:<8}', end='\n')
print('-' * 20)
while True:
    qual_aluno = int(input('Quer mostrar os dados de qual aluno? (999 para encerrar) '))
    if qual_aluno > len(todos):
        print('Aluno não encontrado!')
        break
    print(f'Notas de {todos[qual_aluno][0]}: {todos[qual_aluno][1]}')
    if qual_aluno == 999:
        break
