DB_USER=$1
DB_ADMIN=$2

psql ${DATABASE_NAME} -p ${POSTGRES_SQL_SERVICE_PORT} -h ${POSTGRES_SQL_SERVICE_HOST} -U $DB_ADMIN -c "DROP USER ${DB_USER};" || true
