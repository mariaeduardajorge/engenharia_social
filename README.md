# Vértice Digital — site educativo de cibersegurança

Site responsivo baseado na pesquisa acadêmica do Grupo 02 sobre engenharia social, assédio direcionado, phishing pessoal e ciberbullying.

## Estrutura
- `app.py`: aplicação Flask e endpoint do simulador.
- `templates/index.html`: página principal.
- `static/style.css`: identidade visual e responsividade.
- `static/script.js`: simulador, estudo de caso e checklist interativos.
- `requirements.txt`: dependências.

## Como executar no VS Code
1. Extraia o ZIP e abra a pasta `site_engenharia_social` no VS Code.
2. Abra o terminal integrado (`Terminal > Novo Terminal`).
3. (Opcional, recomendado) Crie um ambiente virtual:
   - Windows: `py -m venv .venv`
   - PowerShell: `.\.venv\Scripts\Activate.ps1`
   - CMD: `.\.venv\Scripts\activate.bat`
4. Instale as dependências: `pip install -r requirements.txt`
5. Execute: `python app.py`
6. Abra o endereço exibido no terminal, normalmente `http://127.0.0.1:5000`.

## Observações
- Os cenários do simulador são fictícios, não coletam dados pessoais e não usam links reais.
- O endpoint Flask retorna explicações educativas; a interação principal também tem tratamento no navegador.
- Fontes externas estão listadas na página. O site é um recurso educativo, não substitui apoio técnico, jurídico ou especializado.
