import os
import sys

# Dicionário com as mensagens em diferentes idiomas
MENSAGENS = {
    'ingles': {
        'nome': 'English',
        'moeda': 'USD $35',
        'titulo': '💰 PAID TOOL',
        'mensagem': '⚠️ THIS TOOL IS PAID!',
        'explicacao': 'To purchase this tool, contact us on WhatsApp:',
        'whatsapp': '📞 WhatsApp: +44 7341 998797',
        'como_comprar': '📌 HOW TO BUY:',
        'passo1': '1️⃣ Contact us on WhatsApp:',
        'passo2': '2️⃣ Inform which tool you want to buy',
        'passo3': '3️⃣ Make the payment of USD $35',
        'passo4': '4️⃣ Send the payment confirmation',
        'passo5': '5️⃣ Receive the valid activation code',
        'passo6': '6️⃣ Use the code to activate the tool',
        'aviso': '⚠️ WARNING: Only after payment confirmation you will receive the code!',
        'sair': 'Press Enter to exit...'
    },
    'espanhol': {
        'nome': 'Español',
        'moeda': 'USD $35',
        'titulo': '💰 HERRAMIENTA DE PAGO',
        'mensagem': '⚠️ ¡ESTA HERRAMIENTA ES PAGA!',
        'explicacao': 'Para comprar esta herramienta, contáctanos en WhatsApp:',
        'whatsapp': '📞 WhatsApp: +44 7341 998797',
        'como_comprar': '📌 CÓMO COMPRAR:',
        'passo1': '1️⃣ Contáctanos en WhatsApp:',
        'passo2': '2️⃣ Informa qué herramienta deseas comprar',
        'passo3': '3️⃣ Realiza el pago de USD $35',
        'passo4': '4️⃣ Envía la confirmación del pago',
        'passo5': '5️⃣ Recibe el código de activación válido',
        'passo6': '6️⃣ Usa el código para activar la herramienta',
        'aviso': '⚠️ ADVERTENCIA: ¡Solo después de confirmar el pago recibirás el código!',
        'sair': 'Presiona Enter para salir...'
    },
    'portugues': {
        'nome': 'Português',
        'moeda': 'R$ 200,00',
        'titulo': '💰 FERRAMENTA PAGA',
        'mensagem': '⚠️ ESTA FERRAMENTA É PAGA!',
        'explicacao': 'Para comprar esta ferramenta, chame no WhatsApp:',
        'whatsapp': '📞 WhatsApp: +55 15 98182-5685',
        'como_comprar': '📌 COMO COMPRAR:',
        'passo1': '1️⃣ Chame no WhatsApp:',
        'passo2': '2️⃣ Informe qual ferramenta deseja comprar',
        'passo3': '3️⃣ Faça o pagamento de R$ 200,00',
        'passo4': '4️⃣ Envie a confirmação do pagamento',
        'passo5': '5️⃣ Receba o código de ativação válido',
        'passo6': '6️⃣ Use o código para ativar a ferramenta',
        'aviso': '⚠️ ATENÇÃO: Somente após a confirmação do pagamento você receberá o código!',
        'sair': 'Pressione Enter para sair...'
    },
    'arabe': {
        'nome': 'العربية',
        'moeda': 'USD $35',
        'titulo': '💰 أداة مدفوعة',
        'mensagem': '⚠️ هذه الأداة مدفوعة!',
        'explicacao': 'لشراء هذه الأداة، اتصل بنا على واتساب:',
        'whatsapp': '📞 واتساب: +44 7341 998797',
        'como_comprar': '📌 كيفية الشراء:',
        'passo1': '1️⃣ اتصل بنا على واتساب:',
        'passo2': '2️⃣ أبلغ عن الأداة التي تريد شراءها',
        'passo3': '3️⃣ قم بدفع مبلغ USD $35',
        'passo4': '4️⃣ أرسل تأكيد الدفع',
        'passo5': '5️⃣ استلم رمز التفعيل الصحيح',
        'passo6': '6️⃣ استخدم الرمز لتفعيل الأداة',
        'aviso': '⚠️ تحذير: فقط بعد تأكيد الدفع ستحصل على الرمز!',
        'sair': 'اضغط Enter للخروج...'
    }
}

def limpar_tela():
    os.system('clear' if os.name == 'posix' else 'cls')

def selecionar_idioma():
    limpar_tela()
    
    print("=" * 50)
    print("  SELECIONE O IDIOMA / SELECT LANGUAGE")
    print("=" * 50)
    print("  1 - Inglês / English")
    print("  2 - Español / Spanish")
    print("  3 - Português / Portuguese")
    print("  4 - العربية / Arabic")
    print("=" * 50)
    
    while True:
        try:
            opcao = input("\n👉 Digite o número / Enter number: ")
            
            if opcao == '1':
                return 'ingles'
            elif opcao == '2':
                return 'espanhol'
            elif opcao == '3':
                return 'portugues'
            elif opcao == '4':
                return 'arabe'
            else:
                print("❌ Opção inválida! Tente novamente.")
        except KeyboardInterrupt:
            print("\n\n⚠️ Operação cancelada.")
            sys.exit()

def mostrar_informacoes(idioma):
    limpar_tela()
    
    msg = MENSAGENS[idioma]
    
    print("=" * 50)
    print(f"  {msg['titulo']}")
    print("=" * 50)
    print(f"  🌐 Idioma / Language: {msg['nome']}")
    print("=" * 50)
    
    print(f"\n  {msg['mensagem']}")
    print(f"\n  {msg['explicacao']}")
    print(f"  {msg['whatsapp']}\n")
    
    print("=" * 50)
    print(f"  {msg['como_comprar']}")
    print("=" * 50)
    print(f"  {msg['passo1']}")
    print(f"     {msg['whatsapp']}")
    print(f"  {msg['passo2']}")
    print(f"  {msg['passo3']}")
    print(f"  {msg['passo4']}")
    print(f"  {msg['passo5']}")
    print(f"  {msg['passo6']}")
    print("=" * 50)
    
    print(f"\n  {msg['aviso']}")
    print(f"\n  💡 {msg['passo1']} {msg['whatsapp']}\n")
    
    print("-" * 50)
    input(f"  {msg['sair']}")

def main():
    try:
        idioma = selecionar_idioma()
        mostrar_informacoes(idioma)
    except KeyboardInterrupt:
        print("\n\n⚠️ Operação cancelada pelo usuário.")
    except Exception as e:
        print(f"\n❌ Erro: {e}")

if __name__ == "__main__":
    main()
