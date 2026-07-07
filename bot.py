import telebot
from despesa import Despesas
from controle_despesa import ControleDespesas

controle=ControleDespesas()
dadosusuario={}

bot=telebot.TeleBot('SEU_TOKEN')

@bot.message_handler(['start','help'])
def start(msg:telebot.types.Message):
    bot.reply_to(msg,'Olá, vamos analisar seus gastos')


@bot.message_handler(['adicionar'])
def pedir_descricao(message):
    msg=bot.reply_to(message,'Qual a descrição da despesa:')
    bot.register_next_step_handler(msg,receber_descricao)

def receber_descricao(message):
    try:
        dadosusuario['descrição']=message.text

        msg=bot.reply_to(message,'Qual o valor da despesa:')
        bot.register_next_step_handler(msg,receber_valor)
    except:
        msg=bot.reply_to(message,'Digite apenas números:')
        bot.register_next_step_handler(msg,receber_valor)


def receber_valor(message):
    dadosusuario['valor']=float(message.text)

    msg=bot.reply_to(message,'Qual a categoria:')
    bot.register_next_step_handler(msg,receber_categoria)

def receber_categoria(message):
    dadosusuario['categoria']=message.text

    despesa=Despesas(dadosusuario['valor'],dadosusuario['categoria'],dadosusuario['descrição'])
    controle.adicionardespesas(despesa)
    bot.reply_to(message,'Despesa adicionada com sucesso!')

@bot.message_handler(['resumo'])
def resumo(message):

    categorias=controle.totalporcategoria()
    total=controle.totalgasto()

    texto='RESUMO DOS GASTOS:\n\n'

    for categoria,valor in categorias.items():
        texto+=f'{categoria}: R${valor:.2f}\n'

    texto+=f'\nTotal gastos:R${total}'
    bot.reply_to(message,texto)

bot.infinity_polling()