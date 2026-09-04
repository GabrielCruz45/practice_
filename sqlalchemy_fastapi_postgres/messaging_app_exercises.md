# SQLAlchemy + FastAPI — Messaging App Exercises

Built for **async SQLAlchemy 2.0** (`AsyncSession`) + **PostgreSQL**, since that's the stack you'll actually ship a FastAPI app with.

**What this covers:** single-table CRUD → constraints & column design → one-to-many → many-to-many (association objects) → self-referential many-to-many → cascades → eager loading & advanced querying → transactions → wiring it all into FastAPI (schemas, dependencies, endpoints) → migrations.

---

## Before you start

**Install:**
```bash
pip install fastapi "uvicorn[standard]" "sqlalchemy[asyncio]" asyncpg python-dotenv "passlib[bcrypt]" alembic
```

**Database:** create an empty Postgres database (e.g. `messaging_db`). No local Postgres? Spin one up with Docker:
```bash
docker run --name messaging-pg -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=messaging_db -p 5432:5432 -d postgres
```
Connection string format: `postgresql+asyncpg://postgres:postgres@localhost:5432/messaging_db`

**Project structure** (you'll build this up piece by piece — don't create it all upfront):
```
messaging_app/
├── app/
│   ├── __init__.py
│   ├── database.py     # engine, session, Base, get_db
│   ├── models.py       # ORM models
│   ├── schemas.py      # Pydantic schemas
│   ├── crud.py         # DB operations
│   └── main.py         # FastAPI app + routes
├── .env
└── requirements.txt
```

**How to use this:** work top to bottom — later tiers assume earlier ones are done. These are task descriptions, not solutions. When you want a specific one checked, or want to see one worked example before attempting similar ones, just ask for that exercise by number.

---

## Tier 0 — Environment & project setup

**1. Project skeleton.** Create the folder structure above and a `requirements.txt` with the packages listed.

**2. Connection string.** In `.env`, add `DATABASE_URL=postgresql+asyncpg://...`. In `app/database.py`, load it with `python-dotenv` and `os.getenv()`.

**3. Engine & Base.** In `app/database.py`, create an async engine with `create_async_engine(DATABASE_URL, echo=True)` and a `Base` class using SQLAlchemy 2.0's `DeclarativeBase`.

**4. Session factory + FastAPI dependency.** In `app/database.py`, create an `async_sessionmaker` called `AsyncSessionLocal`, then write an async generator `get_db()` that yields a session — this becomes your `Depends()` later.

---

## Tier 1 — Your first model: create & read

**5. The `User` model.** In `app/models.py`: `id` (PK), `username` (unique string), `email` (unique string), `hashed_password` (string), `created_at` (datetime). Use `Mapped[]` / `mapped_column()` — not the old `Column()` style.

**6. `__repr__`.** Give `User` a `__repr__` like `<User id=1 username='gxbs_'>`.

**7. Create the tables.** Write `async def init_models()` using `engine.begin()` + `conn.run_sync(Base.metadata.create_all)`.

**8. Insert a user.** In `app/crud.py`: `async def create_user(session, username, email, hashed_password) -> User` — build it, `add()`, `commit()`, `refresh()`, return it.

**9. Read all users.** `async def get_users(session) -> list[User]` using `select(User)` + `session.execute()`.

**10. Read one by id.** `async def get_user_by_id(session, user_id) -> User | None` using `.where(User.id == user_id)` and `scalar_one_or_none()`.

---

## Tier 2 — Filtering, sorting, pagination

**11. Find by username or email.** `get_user_by_username(session, username)` and `get_user_by_email(session, email)`.

**12. Existence check.** `async def username_exists(session, username) -> bool` — check existence efficiently, don't fetch the whole row.

**13. Pagination.** `async def get_users_paginated(session, skip: int = 0, limit: int = 10)` using `.offset()` / `.limit()`.

**14. Sorting.** Add a sorted variant using `.order_by(User.created_at.desc())`.

**15. Counting.** `async def count_users(session) -> int` using `select(func.count()).select_from(User)`.

---

## Tier 3 — Update & delete

**16. Update a field.** Add a `display_name` column, then `update_display_name(session, user_id, new_name)`.

**17. Update with a duplicate check.** `update_email(session, user_id, new_email)` — catch `IntegrityError` and `await session.rollback()` if the email's taken.

**18. Soft delete.** Add `is_active` (default `True`). `deactivate_user(session, user_id)` flips it instead of deleting the row.

**19. Hard delete.** `async def delete_user(session, user_id) -> bool` — return whether a row actually existed to delete.

**20. Bulk update.** Deactivate users matching some rule (e.g. `created_at` older than X) in a single `update()` statement, not a Python loop.

---

## Tier 4 — Constraints & column design

**21. Tighten constraints.** `username`/`email` → `nullable=False, unique=True`; give `username` a sensible `String(50)` length.

**22. Server-side defaults.** Switch `created_at` to `server_default=func.now()` so Postgres sets it, not Python.

**23. Index.** Add an explicit index on `username`.

**24. Check constraint.** Add a `CheckConstraint` requiring `username` to be at least 3 characters.

**25. Enum column.** Add `status` (`ONLINE` / `OFFLINE` / `AWAY`) as a proper SQLAlchemy `Enum`, defaulting to `OFFLINE`.

---

## Tier 5 — A second entity: Messages (one-to-many)

**26. `Conversation` model.** `id`, `name` (nullable, group chats only), `is_group` (bool, default `False`), `created_at`.

**27. `Message` model.** `id`, `conversation_id` (FK), `sender_id` (FK → `users.id`), `content` (`Text`), `sent_at` (server default now).

**28. Relate `User` ↔ `Message`.** `messages_sent: Mapped[list["Message"]]` on `User`, `sender: Mapped["User"]` on `Message`, linked with `back_populates`.

**29. Relate `Conversation` ↔ `Message`.** Same pattern, with `cascade="all, delete-orphan"` on the `Conversation` side.

**30. Query via relationship.** `get_messages_by_sender(session, user_id)` — load `messages_sent` with `selectinload()` in the *same* query instead of a second round-trip.

---

## Tier 6 — Many-to-many: conversation participants

*Concept: an association **object** (not just a `secondary=` table), because membership needs extra columns.*

**31. `ConversationParticipant` model.** Composite PK of `conversation_id` + `user_id` (both FKs), plus `joined_at` and `is_admin` (default `False`).

**32. Wire up the relationships.** So you can go `user.conversation_links` → `.conversation`, and the reverse from `Conversation`.

**33. Add a participant.** `add_participant(session, conversation_id, user_id, is_admin=False)`.

**34. A user's conversations.** `get_user_conversations(session, user_id)` → every `Conversation` they're in.

**35. Leave a conversation.** `remove_participant(session, conversation_id, user_id)`.

---

## Tier 7 — Self-referential many-to-many: contacts

*Concept: both foreign keys point back to the same table, so SQLAlchemy needs help figuring out which is which.*

**36. `Contact` model.** `requester_id` + `addressee_id` (both FK → `users.id`, composite PK), `status` (`"pending"`/`"accepted"`), `created_at`.

**37. The tricky relationship.** Add a `relationship()` on `User` for outgoing requests using `primaryjoin` — SQLAlchemy can't infer which FK to use on a self-referential join by default.

**38. Send & accept a request.** `send_contact_request(session, requester_id, addressee_id)` and `accept_contact_request(session, requester_id, addressee_id)`.

**39. List accepted contacts.** `get_contacts(session, user_id)` — `status == "accepted"`, checking *both* directions (the user could be requester or addressee), returning whoever the "other person" is in each row.

---

## Tier 8 — Cascades

**40. Make deletes cascade for real.** Add `ondelete="CASCADE"` on the relevant `ForeignKey()`s (Postgres-side) **and** `passive_deletes=True` on the matching `relationship()`s (SQLAlchemy-side). Deleting a `User` should clean up their messages and memberships; deleting a `Conversation` should clean up its messages and participants.

**41. Prove it, then break it on purpose.** Delete a user with existing messages, confirm the messages are gone. Then comment out `passive_deletes=True` and see what actually happens — write a one-line comment explaining the difference.

---

## Tier 9 — Advanced querying

**42. Avoid N+1 (`selectinload`).** Load a `Conversation` plus all its `messages` in two queries total, not one-plus-N.

**43. Eager-load one level deeper (`joinedload`).** Load a `Message` and its `sender` in a single joined query.

**44. Aggregate.** `messages_per_user(session)` → `(username, message_count)` pairs via `.group_by()` + `func.count()`.

**45. Search.** `search_messages(session, keyword)` using `.ilike()` for case-insensitive substring search over `content`.

**46. Most recent message per conversation.** For every conversation, get *only* its latest message. This needs a subquery or window function (`row_number()` over `partition by conversation_id order by sent_at desc`). Genuinely hard — take your time.

**47. `exists()`.** `has_sent_messages(session, user_id) -> bool` using `select(exists().where(...))` instead of counting or fetching rows.

---

## Tier 10 — Transactions & bulk operations

**48. Atomic multi-step write.** Create a `Conversation` and add two participants in one transaction with `async with session.begin():` — if the second participant insert fails, the conversation shouldn't be created either.

**49. Bulk insert.** Insert a list of messages in one round-trip (`session.add_all()`, or `insert()` with a list of dicts) instead of looping individual `add()` + `commit()` calls.

---

## Tier 11 — FastAPI: schemas & dependency injection

**50. Pydantic schemas.** In `app/schemas.py`: `UserCreate` (username, email, password), `UserRead` (id, username, email, created_at, with `model_config = {"from_attributes": True}`), `UserUpdate` (all fields optional).

**51. A "public" schema.** `UserPublic` — safe to show other users: no email, definitely no `hashed_password`. Compare to `UserRead`, which is for viewing *your own* profile.

**52. Message schemas.** `MessageCreate` and `MessageRead` — have `MessageRead` nest a `UserPublic` for the sender, not just a raw `sender_id`.

**53. Use the dependency.** In `app/main.py`, create the FastAPI app and one throwaway endpoint taking `db: AsyncSession = Depends(get_db)` that returns `{"status": "connected"}` — just to prove the wiring works.

---

## Tier 12 — FastAPI: full CRUD endpoints

**54. `POST /users`.** Hash the password with `passlib`'s `bcrypt` before storing — never store it raw. Return `201` with a `UserRead`.

**55. `GET /users/{user_id}`.** Raise `HTTPException(404)` if nothing's found.

**56. `GET /users`.** Support `skip`/`limit` query params, reusing your Tier 2 pagination function.

**57. `PATCH /users/{user_id}`.** Partial update — only overwrite fields the client actually sent.

**58. `DELETE /users/{user_id}`.** `204` on success, `404` if the user didn't exist.

**59. The messaging flow.** `POST /conversations` (create + add the creator as a participant), `POST /conversations/{id}/messages` (send a message), `GET /conversations/{id}/messages` (paginated history — pick oldest- or newest-first, but be explicit about which).

---

## Tier 13 — Capstone

**60. Enforce a real business rule.** Before inserting a message, check that `sender_id` is actually a participant in `conversation_id` — reject with `403` if not. Now the endpoint combines a lookup *and* a write.

**61. Unread counts.** Add `last_read_at` to `ConversationParticipant`. Write a query returning, per conversation, how many messages were sent after that user's `last_read_at` — this is the core query behind every messaging app's unread badge.

**62. Your first migration.** Initialize Alembic for an async engine (`alembic init -t async migrations`), autogenerate a migration from your current models, apply it. Then add one new column to any model and generate a second migration for just that change.

---

That's 62. Want a worked solution for any of these, a review of your code, or should I expand a tier further (JWT auth, WebSockets for real-time delivery, testing with `pytest-asyncio`)?
