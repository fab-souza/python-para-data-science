from random import randrange
livre = randrange(0, 11)

def atendimento_fora_de_horario(orientacao):
  if orientacao == 'sim':
    resposta_amanha = input('\nCerto!\nGostaria de verificar se podemos te atender amanhã?\n\n').lower()
    if resposta_amanha == 'sim':
      numero_cliente = int(input('\nPerfeito!\nPor favor, digite a quantidade total de pessoas para a reserva:\n'))
      if numero_cliente < livre:
        print('\nTemos vaga(s) para esta quantidade de pessoas.\nPor favor, faça sua reserva pelo número\n\n(99) 99999-9999\n\nA partir das 99:00\n Aguardamos seu agendamento :)')

      else:
        print('\nInfelizmente, não temos mais vaga(s) para este número de pessoas.\nPor favor, entre em contato com número\n\n(99) 99999-9999\n\nA partir das 99:00 para agendar um horário. Agradecemos sua compreensão.')

    else:
      print('Ok. Entre em contato com número\n\n(99) 99999-9999\n\nA partir das 99:00\n\nPara ter um atendimento com um de nossos colaboradores. Agradecemos a compreensão e aguardamos seu agendamento.')

  else:
    print('Ok. Para ser atendido por um de nossos colaboradores, entre em contato com número:\n\n(99) 99999-9999\n\nA partir das 99:00. Agradecemos a compreensão.')


print('Olá, cliente! Como vai?\n\nNo momento, estamos fechados.\n')
orientacao = input('Gostaria de alguma orientação sobre nosso atendimento?\n').lower()

atendimento_fora_de_horario(orientacao)
