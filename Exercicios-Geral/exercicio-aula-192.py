# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']
import json
import os


def listar(tarefas):
    print()
    if not tarefas:
        print('Nenhuma tarefa para listar')
        return

    print('Tarefas:')
    for tarefa in tarefas:
        print(f'\t{tarefa}')
    print()


def desfazer(tarefas, tarefas_refazer):
    print()
    if not tarefas:
        print('Nenhuma tarefa para desfazer')
        return

    tarefa = tarefas.pop()
    print(f'{tarefa=} removida da lista de tarefas.')
    tarefas_refazer.append(tarefa)
    print()


def refazer(tarefas, tarefas_refazer):
    print()
    if not tarefas_refazer:
        print('Nenhuma tarefa para refazer')
        return

    tarefa = tarefas_refazer.pop()
    print(f'{tarefa=} adicionada na lista de tarefas.')
    tarefas.append(tarefa)
    print()


def adicionar(tarefa, tarefas):
    print()
    tarefa = tarefa.strip()
    if not tarefa:
        print('Você não digitou uma tarefa.')
        return
    print(f'{tarefa=} adicionada na lista de tarefas.')
    tarefas.append(tarefa)
    print()

def ler(caminho_arquivo):
    dados = []
    try:
        with open(caminho_arquivo, 'r', enconding='utf8') as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        print('arquivo não existe')
        salvar(tarefas, caminho_arquivo)

    
def salvar(tarefas, caminho_arquivo):
   dados = tarefas
   with open(caminho_arquivo, 'w', enconding='utf-8') as arquivo:
       dados = json.dump(tarefas, arquivo, indent=2, ensure_ascii=False)
   return dados

CAMINHO_ARQUIVO = 'aula119.json'
tarefas = ler([], CAMINHO_ARQUIVO)
tarefas_refazer = []

while True:
    print('Comandos: listar, desfazer e refazer')
    tarefa = input('Digite uma tarefa ou comando: ')

    comandos = {
        'listar': lambda: listar(tarefas),
        'desfazer': lambda: desfazer(tarefas,tarefas_refazer),
        'refazer': lambda: refazer(tarefas,tarefas_refazer),
        'clear': lambda: os.system('clear'),
        'adicionar': lambda: adicionar(tarefas,tarefas_refazer),
    }

    comando = comando.get(tarefa) if comando.get(tarefa) is not None else \
        comandos['adicionar']
    comando()
    salvar(tarefas, CAMINHO_ARQUIVO)


#    if tarefa == 'listar':
#        listar(tarefas)
#        continue
#    elif tarefa == 'desfazer':
#        desfazer(tarefas, tarefas_refazer)
#        listar(tarefas)
#        continue
#    elif tarefa == 'refazer':
#        refazer(tarefas, tarefas_refazer)
#        listar(tarefas)
#        continue
#    elif tarefa == 'clear':
#        os.system('clear')
#        continue
#    else:
#        adicionar(tarefa, tarefas)
#        listar(tarefas)
#        continue
#