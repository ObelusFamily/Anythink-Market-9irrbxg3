import asyncio

import asyncpg
import faker

from app.core.config import get_app_settings
from app.db.events import close_db_connection, connect_to_db
from app.models.domain.users import User
from app.models.domain.items import Item
from app.db.repositories.users import UsersRepository
from app.db.repositories.items import ItemsRepository
from app.db.repositories.comments import CommentsRepository


async def connect_to_db():
    settings = get_app_settings()
    # SQLAlchemy >= 1.4 deprecated the use of `postgres://` in favor of `postgresql://`
    # for the database connection url
    database_url = settings.database_url.replace("postgres://", "postgresql://")

    return await asyncpg.connect(str(database_url))


async def main():
    conn = await connect_to_db()
    fake = faker.Faker()

    users_repo = UsersRepository(conn)
    items_repo = ItemsRepository(conn)
    comments_repo = CommentsRepository(conn)

    item = await items_repo.get_item_by_slug(slug='own-sing-or-energy-throw-similar')
    user = await users_repo.get_user_by_username(username='djoume')
    for _ in range(100):
        comment = await comments_repo.create_comment_for_item(
            body=fake.sentence(50),
            item=item,
            user=user
        )
        print(f"Created Comment: {comment}")


if __name__ == '__main__':
    asyncio.run(main())