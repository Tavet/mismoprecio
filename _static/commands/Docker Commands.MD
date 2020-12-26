# Docker Commands
- Creating a new PostgreSQL Container
docker run --name best-deal-db-dev -e POSTGRES_PASSWORD=admin -d -p 5432:5432 postgres