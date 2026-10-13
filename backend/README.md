# Backend Django

O Django serve a página inicial e as páginas públicas a partir da raiz do site. Ofertas, dicas e marcas parceiras são lidas do MySQL e mantidas pelo admin.

## Onde editar o site

- As páginas servidas pelo Django ficam em `catalog/templates/catalog/`: `base.html` contém o cabeçalho e o rodapé compartilhados; os outros arquivos contêm o conteúdo de cada página.
- Os arquivos HTML diretamente em `docs/` são a versão estática de referência e não são usados pelas rotas do Django. Alterar esses HTMLs, por si só, não altera as páginas renderizadas pelo Django.
- O Django carrega CSS, JavaScript e imagens de `docs/`. Por isso, alterações em `docs/css/style.css` e nos arquivos de `docs/js/` são compartilhadas com o site Django. Se o navegador mantiver o estilo antigo, faça uma recarga forçada com `Ctrl+F5`.
- Ofertas, dicas e marcas exibidas nas páginas vêm do banco de dados; cadastre ou edite esses conteúdos pelo admin.
- Em hospedagem de produção, publique também os templates e os arquivos estáticos atualizados conforme o processo de deploy do servidor.

## Iniciar localmente

Na raiz do repositório, inicie o MySQL e o Django:

```powershell
docker compose up -d
Set-Location backend
..\.venv\Scripts\python.exe manage.py migrate
..\.venv\Scripts\python.exe manage.py createsuperuser
..\.venv\Scripts\python.exe manage.py runserver
```

Abra `http://127.0.0.1:8000/` para o site e `http://127.0.0.1:8000/admin/` para cadastrar conteúdo. O comando `createsuperuser` só é necessário na primeira configuração.

## Conteúdo no painel

- **Ofertas:** cadastre nome, preço, datas e, opcionalmente, imagem. A oferta pública aparece apenas quando está ativa e a data atual estiver entre o início e o fim.
- **Dicas:** cadastre título, categoria e conteúdo; marque **Publicada** para exibir no site. Resumo e imagem são opcionais.
- **Marcas parceiras:** cadastre nome e categoria; deixe **Ativa** marcada para exibir. Logotipo e site são opcionais.

Os arquivos enviados pelo painel ficam em `media/`, ignorado pelo Git. Em produção, configure armazenamento e entrega de mídia apropriados.

## Testes

O usuário MySQL de desenvolvimento tem acesso apenas ao banco da aplicação, sem permissão para criar bancos de teste. Para executar os testes isolados em SQLite em memória:

```powershell
Set-Location backend
..\.venv\Scripts\python.exe manage.py test catalog --settings=config.test_settings
```
