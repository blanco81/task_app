from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool, create_engine
from alembic import context
from app.db.base import Base  # Importa los modelos para que Alembic los reconozca
from app.core.config import settings

# Interpretar la configuración del archivo .ini de alembic
config = context.config

# Configurar la conexión a la base de datos
config.set_main_option('sqlalchemy.url', str(settings.DATABASE_URL)+"?async_fallback=true")

# Configurar logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Agregar los modelos de SQLAlchemy
target_metadata = Base.metadata

def run_migrations_offline():
    """Correr migraciones en modo offline"""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url, target_metadata=target_metadata, literal_binds=True, dialect_opts={"paramstyle": "named"}
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Correr migraciones en modo online"""
    # Usar el motor síncrono create_engine
    connectable = create_engine(
        config.get_main_option('sqlalchemy.url'),
        poolclass=pool.NullPool
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
