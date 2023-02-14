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

    for _ in range(100):
        user = await users_repo.create_user(
            username=fake.user_name(),
            email=fake.email(),
            password=fake.password(),
        )
        print(f"Created USer: {user}")
        for _ in range(1):
            title = fake.text(50)
            item = await items_repo.create_item(
                slug=fake.slug(title),
                title=title,
                description=fake.sentence(50),
                seller=user,
            )
            print(f"Created Item: {item}")
            for _ in range(1):
                comment = await comments_repo.create_comment_for_item(
                    body=fake.sentence(50),
                    item=item,
                    user=user
                )
                print(f"Created Comment: {comment}")


if __name__ == '__main__':
    asyncio.run(main())