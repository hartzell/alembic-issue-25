# Why do I need to call `dispose`?

This is a simplified example of an application I'm working on.

My test suite creates a fresh database for each test, runs the test,
and tears it down.

The tests will fail unless I call `dispose` on the engine being used.

I stumbled on the "solution" of calling `dispose` in the discussion in
[alembic issue#25](https://github.com/sqlalchemy/alembic/issues/25),
when I mentioned my situation I was asked for a simple test case.

This is as simple as I can get it w/out a bit of feedback.


## Note

I don't think that there's anything too unusual here, although:

- I've configured poetry (via `poetry.toml`) to store its virtualenv
  within `./deps`.

## Running the tests

Prerequisites:

- Python, I'm using 3.7.6.
- Poetry, I'm using 1.0.5
- Postgres, I'm running 11.2 from the official Postgresql 11 image
  using this Docker compose configuration.

    ```yaml
    # Use postgres/example user/password credentials
    version: '3.1'

    services:
      db:
        image: postgres:11
        restart: always
        environment:
          POSTGRES_PASSWORD: example
        ports:
          - 5432:5432
    ```

Given the above:

- Use the `setup` target to install the poetry dependencies into a
  virtualenv that's located within `./deps` (I have NFS home directory
  issues):

    ``` shellsession
    make setup
    ```

- Run the tests, which should fail.

    ``` shellsession
    poetry run make test
    ```

Editing `alembic/env.py` and un-commenting the call to
`connectable.dispose()` on line 79 allows the test harness to drop the
database, which allows the test to pass.
