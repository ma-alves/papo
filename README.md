# clairo
Batizado em homenagem a cantora indie, clairo é um chat app desenvolvido com o intuito de explorar as possibilidades de WebSockets com entrega de mensagens em tempo real e monitoramento de status online, utilizando código assíncrono em seus consumidores através do Django Channels e Redis como Message Broker. O foco é o desenvolvimento do backend, enquanto o frontend possui uma interface simples e intuitiva construída utilizando Tailwind.

### Tech Stack
- [Django](https://github.com/django) - Web Framework
- [Channels](https://github.com/django/channels) - Extensão do Django para código assíncrono e WebSockets
- [Daphne](https://github.com/django/daphne) - Servidor HTTP/Websocket
- [PostgreSQL](https://www.postgresql.org) - Banco de Dados SQL
- [Redis](https://redis.io/) - Message Broker
- [Tailwind](https://tailwindcss.com/) - CSS Framework
- [Docker Compose](https://docs.docker.com/compose/) - Multi-container

### Configuração
1. Clone o repositório:
```bash
git clone https://github.com/ma-alves/clairo.git
```
2. Ajuste as variáveis de ambiente em `.env.example`
3. Utilize o Docker Compose para iniciar os serviços:
```bash
docker compose up --build
```
4. A aplicação estará disponível em 0.0.0.0:8000