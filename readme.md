Objetivo: Criar um sistema usando Python 2.7 e Django 1.8.

Considere dois usuários. Requerer cadastro com email e senha.

    Empresa deve criar uma (ou várias) vagas.

    Candidato deve se candidatar a uma (ou mais) vagas.

A vaga que a empresa vai criar deve ter:

    Nome da vaga
    Faixa salarial - valor mínimo e máximo
    Experiência: exemplo, 3 anos de experiência
    Escolaridade
    Distância máxima entre casa e trabalho

O candidato deve informar:

    Pretensão salarial
    Experiência
    Escolaridade
    Distância

Objetivo:

    Você deve gerar um relatório informando quantos e quais candidatos se encaixam no perfil da vaga.

    Na mesma tela, mostrar apenas um número de quantos candidatos não se encaixam no perfil da vaga.

    Considere que a empresa tem o poder de editar ou deletar os candidatos, faça isso usando Ajax.

    Coloque todo seu código no GitHub e me envie o link e as instruções de como rodar a aplicação.

O que será considerado

    Sistema funcionando e sem bugs.
    Não faltar nenhum dos requisitos citados acima.
    Organização do código
    Se tiver TDD melhor ainda
    Se tiver BDD melhor também


# Rodando o projeto
```
git clone git@github.com:olivx/desafio.git project 
cd project 
pyenv local system 
virtualenv .venv 
source .venv/bin/activate 
pip install -r riqueriments.tx 
python contrib/generate_.env.py
python manage.py migrate 
python manage.py runserver

```
# configurando Token para o api google distance matrix
 - Vá até o link [clicando aqui](https://developers.google.com/maps/documentation/distance-matrix/intro?hl=pt-br) e faça o login com uma conta google
 - Clique em obter uma chave 
 - Selecione um projeto ou crie um novo
 - CLick em Enable API
 - copie a nova chave 
 - vá até o arquivo .env 
 - substitua o valor de configuração da chave API_TOKEN
  

# Acessando o sistema 
#### Usuario adimin
- oliveiravicente.net@gmailcom 
- senha vaiquevai123

##### Usuario Empresa
 - debora@email.com.br , sonia@email.com
 - senha vaiquevai123
### Usuario Candidato 
 - almeida@email.com , carlos@email.com, thiago@email.com
 - senha vaiquevai123