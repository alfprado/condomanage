# condomanage

## Passos para Configuração

### 1. Iniciar os Contêineres com Docker

```sh
docker-compose up minioserver
docker-compose up zookeeper
docker-compose up kafka
docker-compose up postgres
docker-compose up connect
docker-compose up kafka-ui
docker-compose up notebook
```

create an .env file

AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
AWS_S3_ENDPOINT=http://minioserver:9000
WAREHOUSE=s3a://condomanage/
PG_USER=user
PG_PASSWORD=admin
PG_DB=db

create access key on minio

### 2. Configurar Credenciais no MinIO

1. Acesse o MinIO em: [http://localhost:9001/](http://localhost:9001/)
   - **Usuário:** minioadmin
   - **Senha:** minioadmin

2. Crie uma nova Access Key:
   - Vá em **Access Key** -> **Create Access Key**
   - Copie a **Access Key** e **Secret Key** geradas e cole no arquivo `.env` na raiz do projeto.
   - Clique em **Create**.

### 3. Executar Todas as Células do Notebook

1. No log do contêiner do notebook, você encontrará o link para acessar o notebook.
2. Acesse o link e abra o arquivo `main.ipynb` dentro da pasta notebook
3. Execute todas as células do notebook.
   - Para acessar o log do notebook, abra um novo terminal e digite o comando:

   ```sh
   docker logs notebook
   ```

Visão Geral da Arquitetura

A arquitetura de ingestão e processamento de dados consiste em vários componentes integrados para garantir um fluxo contínuo e eficiente.

Kafka CDC (Change Data Capture):

Fonte de Dados: Utiliza o Kafka como um sistema de mensagens para capturar e transmitir mudanças em bancos de dados relacionais.
Conectores CDC: Debezium 

MinIO:

Armazenamento de Dados: Utilizado como armazenamento de objetos para dados brutos e processados. MinIO é compatível com o protocolo S3.

Spark Streaming:

Processamento de Dados: Spark Streaming é utilizado para processar dados em tempo real.

Monitoramento

Prometeus e Grafana para coletar métricas das ferramentas e logs.
