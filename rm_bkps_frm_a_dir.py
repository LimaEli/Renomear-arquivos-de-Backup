'''
Programa para renomaear os arquivos que contém a substring 'Cópia' em seu nome,
para o formato <nome do arquivo>+' - BKP '+<data e hora de modificação do arquivo(data e hora no formato YYYYmmddhhmm)>

'''


import datetime
import numpy as np
import os




pasta_bkp = '<caminho da pasta>' #Digite aqui o caminho da pasta onde se encontram os arquivos que deseja renomear

arquivos_bkps = os.listdir(pasta_bkp)  # retorna uma lista de todos os arquivos do diretório

bkps = np.array(arquivos_bkps)	# transforma uma lista em um array
vf_eh_bkp_rm = '- Copia'  		# Parâmetro auxiliar para retornar a posição onde será feita a Subtituição
aux_ind_ext = '.' 				#Caractere "Ponto" para auxiliar na procura do índice da exetenção
vf_eh_bkp_rmd = 'BKP' 			#Caractere auxiliar para indentificar se o Back-Up já foi nenomeado

for x in range(len(bkps)):

    bkps_nome = bkps[x]
    if bkps_nome.find(vf_eh_bkp_rm, 0, len(bkps_nome)) != -1: 																	#Só renomeia se tiver o Nome "Cópia" no nome
        ind_ext = bkps_nome.find(aux_ind_ext, 0, len(bkps_nome)) 																#Índice da extenção do arquivo
        f_ext = bkps_nome[ind_ext:len(bkps_nome)] 																				#Extenção do Arquivo
        bkps_path = pasta_bkp + '/' + bkps_nome																					#Caminho do arquivo
        ind_sufixo = bkps_nome.find(vf_eh_bkp_rm, 0, len(bkps_nome)) - 1														#Índice do "sufixo" do arquivo
        dt_modif_lg = datetime.datetime.fromtimestamp(os.stat(bkps_path).st_mtime)												#Data e hora da modificação do arquivo
        dt_modif = dt_modif_lg.strftime("%Y%m%d%H%M") 																			#TimeStamp da modificação do arquivo
        sufixo = ' - BKP ' + dt_modif 																							#Forma nome do Arquivo
        old_nm = bkps_path 																										#Antigo nome do Arquivo(camiho completo)
        new_nm = pasta_bkp + '/' + bkps_nome[:ind_sufixo] + sufixo + f_ext 														#Novo nome do arquivo (camiho completo)
        print('Nome antigo: ' + old_nm + ' -> Nome novo: ' + new_nm) 															#Impressão para verificação do nome antigo e novo nome do arquivo
        #os.rename(old_nm, new_nm) 																								#Renomeia o arquivo
    elif (bkps_nome.find(vf_eh_bkp_rm, 0, len(bkps_nome)) == -1) and (bkps_nome.find(vf_eh_bkp_rmd, 0, len(bkps_nome)) != -1):	#Verifica se o arquivo já foi renomeado
        print(bkps_nome+' é um BKP já renomeado!')
    elif bkps_nome.find(vf_eh_bkp_rm, 0, len(bkps_nome)) == -1 and (bkps_nome.find(vf_eh_bkp_rmd, 0, len(bkps_nome)) == -1):	#Verifica se o arquivo não é um Back-Up do Tipo "Cópia"
        print(bkps_nome+' Não é BKP!')
