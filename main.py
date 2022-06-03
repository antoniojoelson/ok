import requests
import time
import json
import os

class TelegramBot:
    def __init__(self):
        iTOKEN  = '5493038263:AAEpNn_UmDkO7ideugK02Bc1-fN-PnfPCgI'
        self.iURL = f'https://api.telegram.org/bot{iTOKEN}/'

    def Iniciar(self):
      
        iUPDATE_ID = None
        
        while True:
            iATUALIZACAO = self.ler_novas_mensagens(iUPDATE_ID)
            IDADOS = iATUALIZACAO["result"]
            if IDADOS:
                for dado in IDADOS:
                    iUPDATE_ID = dado['update_id']
                    mensagem = str(dado["message"]["text"])
                    chat_id = dado["message"]["from"]["id"]
                    primeira_mensagem = int(dado["message"]["message_id"]) == 1
                    resposta = self.gerar_respostas(mensagem, primeira_mensagem)
                    self.responder(resposta, chat_id)

    def ler_novas_mensagens(self, iUPDATE_ID):
        iLINK_REQ = f'{self.iURL}getUpdates?timeout=5'
        if iUPDATE_ID:
            iLINK_REQ = f'{iLINK_REQ}&offset={iUPDATE_ID + 1}'
        iRESULT = requests.get(iLINK_REQ)
        return json.loads(iRESULT.content)

    def gerar_respostas(self, mensagem, primeira_mensagem):
        print('mensagem do cliente: ' + str(mensagem))
        
        
        if primeira_mensagem == True or mensagem.lower() in ('menu','cardapio'):
            return f'''Olá seja bem vindo a  Lanches e Pizzas SP  informe o codigo do item que deseja pedir:{os.linesep}1 - Pizza Calabresa{os.linesep}2 - Pizza Mussarela{os.linesep}3 - Pizza Frango{os.linesep}4 - X- Burger{os.linesep}5 - X-Calabresa{os.linesep}6 - X-Tudo{os.linesep}7 - Agua{os.linesep}8 - Suco{os.linesep}9 - Refrigerante'''
          
        if mensagem == '1':
            
            return f'''Pizza Calabresa - R$25,00{os.linesep}Confirmar pedido?(s/n)
            '''
        elif mensagem == '2':
            
            return f'''Pizza Mussarela - R$25,00{os.linesep}Confirmar pedido?(s/n)
            '''
        elif mensagem == '3':
            
            return f'''Pizza Frango - R$30,00{os.linesep}Confirmar pedido?(s/n) ''' 
        elif mensagem == '4':
            return f'''X-Burger - R$10,00{os.linesep}Confirmar pedido?(s/n)'''
        elif mensagem == '5':
            return f'''X-Calabresa - R$12,00{os.linesep}Confirmar pedido?(s/n)'''
        elif mensagem == '6':
            return f'''X-Tudo - R$18,00{os.linesep}Confirmar pedido?(s/n)'''
        elif mensagem == '7':
            return f'''Agua - R$5,00{os.linesep}Confirmar pedido?(s/n)'''
        elif mensagem == '8':
            return f'''Suco - R$6,00{os.linesep}Confirmar pedido?(s/n)'''
        elif mensagem == '9':
            return f'''Refrigerante - R$7,00{os.linesep}Confirmar pedido?(s/n)'''        
        elif mensagem == 'pagar':
           return  f'''Escolha uma  forma de pagamento:{os.linesep}D - Dinheiro{os.linesep}C - Cartão{os.linesep}P - Pix'''
        elif mensagem == 'Pagar':
           return  f'''Escolha uma  forma de pagamento:{os.linesep}D - Dinheiro{os.linesep}C - Cartão{os.linesep}P - Pix'''
        elif mensagem.lower() in ('d', 'dinheiro'):
            return f'''tudo bem em 30 min seu pedido chegara'''
        elif mensagem.lower() in ('c', 'cartao'):
            return f'''tudo bem em 30 min seu pedido chegara'''
        elif mensagem.lower() in ('p', 'pix'):
            return f'''tudo bem em 30 min seu pedido chegara'''
        elif mensagem.lower() in ('s', 'sim'):
            return f''' Pedido Confirmado!{os.linesep}digite "pagar" terminar ou "menu" para mais itens '''
        elif mensagem.lower() in ('n', 'não'):
            return ''' Item não incluso! Informe o codigo do item: '''
        else:
            return 'Para acessar o cardapio digite "menu"'
        


    def responder(self, resposta, chat_id):
        iLINK_REQ = f'{self.iURL}sendMessage?chat_id={chat_id}&text={resposta}'
        requests.get(iLINK_REQ)
        print("respondi: " + str(resposta))


bot = TelegramBot()
bot.Iniciar()