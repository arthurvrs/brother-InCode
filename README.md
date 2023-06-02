# Brother-InCode
O Brother-InCode tem como objetivo facilitar o contato entre tutores e alunos visando uma melhora em seu aprendizado. De maneira prática e ágil, é possível criar usuários (Aluno/Tutor), procurar tutores disponíveis com especialidades em diversas áreas, marcar aulas de assuntos específicos, entre outros.

## Como utilizar?

> ### Para executar o programa:

- Certifique-se de ter feito o download dos arquivos corretamente.
- Uma vez dentro do diretório, é necessário criar um **Virtual Environment** (Ambiente Virtual), para isolar as modificações e instalações de Python/Django do projeto com outros arquivos e diretórios do seu computador.
  > **Dica:** realizar todos os passos a seguir estando, dentro do terminal, no diretório em que o arquivo `manage.py` se encontra.

- Para criar um **Virtual Environment**, vamos utilizar o seguinte código:
  > **Dica:** o `nome-do-ambiente-virtual` pode ser qualquer um de sua preferência, porém geralmente utiliza-se `venv`.
  
	- No Windows:
	```sh
    python -m venv nome-do-ambiente-virtual
    ```
    - No Linux e OS X
	```sh
    python3 -m venv nome-do-ambiente-virtual
    ```
- Após isso, vamos ativar seu ambiente:

	- No Windows:
    ```sh
    .\nome-do-ambiente-virtual\Scripts\activate.ps1
    ```
    > Caso o Windows aponte um erro, é necessário executar o PowerShell como admin e rodar a seguinte linha e dar um `[Y] Yes` ao final:
    >```sh
    >C:\WINDOWS\system32> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned
   > ```
    
	- No Linux e OS X:
    ```sh
    source nome_do_ambiente_virtual/bin/activate
    ```

- Agora, é necessário fazer a instalação dos requisitos da aplicação, presentes no arquivo `requirements.txt`:
    ```sh
    pip install -r requirements.txt
    ```

- E então, basta executar as duas próximas funções respectivamente:
    ```sh
    py manage.py migrate
    ```
    ```sh
    py manage.py runserver
    ```

- Tutorial concluído! Neste momento, o servidor da aplicação deverá estar ligado, permitindo o acesso pela url `http://127.0.0.1:8000/`.

## Equipe
- Arthur Santos (Desenvolvedor Full Stack)
- Carlos Aleandro (Gerente de Projeto)
- Eduardo Serpa (Desenvolvedor Front-End)
- José Victor(Desenvolvedor Full Stack)
- Paulo Victor (Desenvolvedor Back-End)
