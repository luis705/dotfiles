from datetime import datetime
import os
import sys

def gera_capa(autores, cidade, materia, professores):
	capa = r"""\begin{center}
    \textbf{
        Instituto Federal de Educação Ciência e Tecnologia de São Paulo \\
        Curso de Graduação em Engenharia Eletrônica
    }
    \vspace{4cm}

    """ + titulo.upper()

	capa += r"""
\end{center}
\vspace{1.5cm}
\begin{tabular}{p{10cm}p{5cm}}
    & """
	if len(professores) == 1:
		capa += f'RELATÓRIO DA DISCIPLINA {materia.upper()} COM O PROF. {professores[0].upper()}.'
	else:
		capa += f"RELATÓRIO DA DISCIPLINA {materia.upper()} COM OS PROFESSORES "
		for professor in professores:
			if professor == professores[-1]:
				capa += f'E {professor.upper()}.'
			elif professor == professores[0]:
				capa += f'{professor.upper()} '
			else:
				capa += f'{professor.upper()}, '
	capa += r"""
\end{tabular}
\vspace{2cm}

\begin{tabular}{p{0,5cm}p{5cm}p{3cm}p{2cm}p{0,5cm}}"""

	for autor in autores:
		capa += f"\n\t & {autor[0]} & & {autor[1]}"

	capa += r"""
\end{tabular}
\vspace*{\fill}
\begin{center}""" + cidade + '\n\n' + str(datetime.now().year) + r"""
\end{center}
\pagebreak
"""
	return capa

def gera_principal(capitulos):
	principal = r"""\documentclass[	12pt, oneside, a4paper, chapter=TITLE, english, french, spanish, brazil]{abntex2}

% ---------------------------------------------------------------------------------
%                                   PACOTES
% ---------------------------------------------------------------------------------
\usepackage{lmodern}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{lastpage}
\usepackage{indentfirst}
\usepackage{xcolor,colortbl}
\usepackage{graphicx}
\usepackage{microtype}
\usepackage{hyperref}
\usepackage{subfig}
\usepackage{epigraph}
\usepackage{url}
\usepackage{placeins}
\usepackage{multirow}
\usepackage[figuresright]{rotating}
\usepackage{chemfig}
\usepackage{amsmath}
\usepackage{listings}
\usepackage{tabularx}
\usepackage{booktabs}
\usepackage{lastpage}
\usepackage{amssymb}
\usepackage{enumitem}
\usepackage{bigints}
\usepackage{listings}
\usepackage{etoolbox}
\usepackage[final]{pdfpages}
\usepackage{bigstrut}
\usepackage{lipsum}
\usepackage[brazilian,hyperpageref]{backref}	 % Paginas com as citações na bibl
\usepackage[alf,abnt-emphasize=bf]{abntex2cite}  % Citações padrão ABNT
\usepackage[top=2cm,left=2cm,  bottom=3cm, right=2cm]{geometry}
\usepackage{xcolor}
\usepackage{array}

% ---------------------------------------------------------------------------------
%                          CONFIGURAÇÕES DOS PACOTES
% ---------------------------------------------------------------------------------
\newcolumntype{P}[1]{>{\centering\arraybackslash}p{#1}}
\renewcommand{\backrefpagesname}{Citado na(s) página(s):~}
\renewcommand{\backref}{}
\renewcommand*{\backrefalt}[4]{
	\ifcase #1 %
	Nenhuma citação no texto.%
	\or
	Citado na página #2.%
	\else
	Citado #1 vezes nas páginas #2.%
	\fi}

% listagens
\definecolor{corComentario}{RGB}{150,150,150}
\definecolor{corString}{RGB}{206,123,0}
\definecolor{corPalavraChave}{RGB}{0,0,230}

\lstset{
	numbers=left,
	stepnumber=1,
	firstnumber=1,
	numberstyle=\footnotesize,
	extendedchars=true,
	breaklines=true,
	lineskip=0pt,
	frame=tb,
	basicstyle=\ttfamily\footnotesize,
	showstringspaces=false,
	stringstyle=\color{corString},
	commentstyle=\color{corComentario},
	keywordstyle=\color{corPalavraChave}
}

\newcolumntype{Y}{>{\centering\arraybackslash}X}
\newcommand{\ano}[1]{\def \oano {#1}}
\newcommand{\imprimirano}{\oano}
\newcommand{\mes}[1]{\def \omes {#1}}
\newcommand{\imprimirmes}{\omes}
\newcommand{\subtitulo}[1]{\def \osubtitulo {#1}}
\newcommand{\imprimirsubtitulo}{\osubtitulo}
\newcommand{\area}[1]{\def \aarea {#1}}
\newcommand{\imprimirarea}{\aarea}
\renewcommand{\coorientador}[1]{\def \ocoorientador {#1}}
\renewcommand{\imprimircoorientador}{\ocoorientador}
\newcommand{\grau}[1]{\def \ograu {#1}}
\newcommand{\imprimirgrau}{\ograu}
\newcommand{\curso}[1]{\def \ocurso {#1}}
\newcommand{\imprimircurso}{\ocurso}

% ---
% Configurações de aparência do PDF final
% ---
% alterando o aspecto da cor azul
\definecolor{blue}{RGB}{41,5,195}
% informações do PDF
\makeatletter
\hypersetup{
	%pagebackref=true,
	pdftitle={\@title},
	pdfauthor={\@author},
	pdfsubject={\imprimirpreambulo},
	pdfcreator={Nome Completo},
	pdfkeywords={Palavra chave 1}{Palavra chave 2}{Palavra chave 3}{Palavra chave n},
	colorlinks=true,       		% false: boxed links; true: colored links
	linkcolor=black,          	% color of internal links
	citecolor=black,       		% color of links to bibliography
	filecolor=black,      		% color of file links
	urlcolor=black,
	bookmarksdepth=4
}
\makeatother
% ---

% ---
% Comandos do autor
% ---
% comando para inserir autor e ano
\newcommand{\citeauthorandyear}[1]{\citeauthoronline{#1} (\citeyear{#1})}

% ---
% Novo list of (listings) para Quadros
% ---
\newcommand{\quadroname}{Quadro}
\newcommand{\listofquadrosname}{Lista de Quadros}
\newfloat[chapter]{quadro}{loq}{\quadroname}
\newlistof{listofquadros}{loq}{\listofquadrosname}
\newlistentry{quadro}{loq}{0}
% configurações para atender às regras da ABNT
\setfloatadjustment{quadro}{\centering}
\counterwithout{quadro}{chapter}
\renewcommand{\cftquadroname}{\quadroname\space}
\renewcommand*{\cftquadroaftersnum}{\hfill--\hfill}
% Configuração de posicionamento padrão:
\setfloatlocations{quadro}{hbtp}
% ---
% Novo list of (listings) para Figuras
% ---
\newcommand{\figuraname}{Figura}
\newcommand{\listoffigurasname}{Lista de Figuras}
\newfloat[chapter]{figura}{lof}{\figuraname}
\newlistof{listoffiguras}{lof}{\listoffigurasname}
\newlistentry{figura}{lof}{0}
% configurações para atender às regras da ABNT
\setfloatadjustment{figura}{\centering}
\counterwithout{figura}{chapter}
\renewcommand{\cftfiguraname}{\figuraname\space}
\renewcommand*{\cftfiguraaftersnum}{\hfill--\hfill}
% Configuração de posicionamento padrão:
\setfloatlocations{figura}{hbtp}
% ---
% Novo list of (listings) para Tabelas
% ---
\newcommand{\tabelaname}{Tabela}
\newcommand{\listoftabelasname}{Lista de Tabelas}
\newfloat[chapter]{tabela}{lot}{\tabelaname}
\newlistof{listoftabelas}{lot}{\listoftabelasname}
\newlistentry{tabela}{lot}{0}
% configurações para atender às regras da ABNT
\setfloatadjustment{tabela}{\centering}
\counterwithout{tabela}{chapter}
\renewcommand{\cfttabelaname}{\tabelaname\space}
\renewcommand*{\cfttabelaaftersnum}{\hfill--\hfill}
% Configuração de posicionamento padrão:
\setfloatlocations{tabela}{hbtp}
% ---
% Espaçamentos entre linhas e parágrafos
% ---
% O tamanho do parágrafo é dado por:
\setlength{\parindent}{1.3cm}
% Controle do espaçamento entre um parágrafo e outro:
\setlength{\parskip}{0.2cm}  % tente também \onelineskip
% ---------------------------------------------------------------------------------
%                                   INÍCIO DO DOCUMENTO
% ---------------------------------------------------------------------------------
\begin{document}
\selectlanguage{brazil}
\frenchspacing
\pretextual
\input{Capa}
% ---
% inserir o sumário
% ---
\pdfbookmark[0]{\contentsname}{toc}
\tableofcontents*
\cleardoublepage
% ---

% ---
% inserir listas
% --
\pdfbookmark[0]{\listoffigurasname}{loq}
\listoffiguras*
\cleardoublepage
\pdfbookmark[0]{\listoftabelasname}{lot}
\listoftabelas*
\cleardoublepage
% ---

\textual
	"""

	for capitulo in capitulos:
		principal += r"""
\input{%s}""" % (capitulo)

	principal += r"""
% ----------------------------------------------------------
% Referências bibliográficas
% ----------------------------------------------------------
\postextual
\bibliography{referencias}

\end{document}
"""
	return principal


def cria_arquivos(capitulos, autores, cidade, materia, professores):
	projeto = sys.argv[1]
	os.mkdir(projeto)
	os.chdir(projeto)
	os.mkdir('Imagens')
	for capitulo in capitulos:
		texto = r"""\chapter{%s}
\label{chap:%s}""" % (capitulo, capitulo)

		with open(capitulo + '.tex', mode='w', encoding='utf-8') as f:
			f.write(texto)

	capa = gera_capa(autores, cidade, materia, professores)
	with open('Capa.tex', mode='w', encoding='utf-8') as f:
		f.write(capa)

	principal = gera_principal(capitulos)
	with open(sys.argv[2] + '.tex', mode='w', encoding='utf-8') as f:
		f.write(principal)


if __name__ == '__main__':
	if len(sys.argv) != 3:
		print('Usage: python3 criação-de-relatório.py caminho-do-relatorio nome-do-projeto')
		sys.exit()


	titulo = input('Qual o título do relatório: ')
	cidade = input('Digite o nome da cidade: ')

	n_autores = int(input('Quantos alunos escreveram: '))
	autores = list()
	for i in range(n_autores):
		nome = input(f'Digite o nome do {i+1} autor: ')
		prontuario = input(f'Digite o prontuário do {i+1} autor: ')
		autores.append([nome, prontuario])

	n_capitulos = int(input('Insira o número de capítulos: '))
	capitulos = list()
	for i in range(n_capitulos):
		capitulos.append(input(f'Insira o nome do capítulo número {i+1}: '))

	materia = input('Digite o nome da matéria: ')
	n_prof = int(input('Digite o número de professores: '))
	professores = list()
	for i in range(n_prof):
		professores.append(input(f'Digite o nome completo do professor número {i+1}: '))

	cria_arquivos(capitulos, autores, cidade, materia, professores)
