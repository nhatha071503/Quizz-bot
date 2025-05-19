import aiosqlite
import asyncio

async def init_db():
    async with aiosqlite.connect("bot.db") as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                currency INTEGER DEFAULT 0,
                exp INTEGER DEFAULT 0,
                level INTEGER DEFAULT 1,
                achievements TEXT DEFAULT '[]',
                daily_tasks TEXT DEFAULT '[]',
                last_task_update TEXT
            )
        """)
        await db.execute("""
            CREATE TABLE IF NOT EXISTS quiz_questions (
                question_id INTEGER PRIMARY KEY AUTOINCREMENT,
                question TEXT,
                answer TEXT,
                difficulty INTEGER
            )
        """)
        await db.execute("""
            CREATE TABLE IF NOT EXISTS daily_tasks (
                user_id INTEGER,
                tasks TEXT DEFAULT '[]',
                FOREIGN KEY (user_id) REFERENCES users (user_id)
            )
        """)
        await db.commit()

async def add_user(user_id):
    async with aiosqlite.connect("bot.db") as db:
        await db.execute(
            "INSERT OR IGNORE INTO users (user_id) VALUES (?)", (user_id,)
        )
        await db.commit()

if __name__ == "__main__":
    asyncio.run(init_db())