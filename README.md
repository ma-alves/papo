# papo
papo é um chat app desenvolvido com o intuito de explorar as possibilidades de WebSockets com entrega de mensagens em tempo real e monitoramento de status online, utilizando código assíncrono em seus consumidores através do Django Channels e Redis como Pub/Sub. O foco é o desenvolvimento do back-end, enquanto o front-end possui uma interface simples construída utilizando Tailwind.

### Tech Stack
- [Django](https://github.com/django) - Web Framework
- [Channels](https://github.com/django/channels) - Extensão do Django para código assíncrono e WebSockets
- [Daphne](https://github.com/django/daphne) - Servidor HTTPS/Websocket
- [PostgreSQL](https://www.postgresql.org) - Banco de Dados SQL
- [Redis](https://redis.io/) - Channel Layer
- [Tailwind](https://tailwindcss.com/) - CSS Framework
- [Docker Compose](https://docs.docker.com/compose/) - Multi-container

### Configuração
1. Clone o repositório:
```bash
git clone https://github.com/ma-alves/papo.git
```
2. Ajuste as variáveis de ambiente:
```bash
cp .env.example .env
```
3. Utilize o Docker Compose para iniciar os serviços:
```bash
docker compose up --build
```
4. A aplicação estará disponível em 0.0.0.0:8000

### Acesso
A aplicação também está disponível em [papo](https://papo.onrender.com/), fique a vontade para me enviar uma mensagem! Meu usuário: [matheus](https://papo.onrender.com/chat/profile/matheus/)