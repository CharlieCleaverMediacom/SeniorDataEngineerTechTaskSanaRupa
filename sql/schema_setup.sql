-- SQL queries to set up schemas in BigQuery

CREATE TABLE IF NOT EXISTS srk.users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        username TEXT,
        email TEXT,
        phone TEXT,
        website TEXT,
        address.street TEXT,
        address.suite TEXT,
        address.city TEXT,
        address.zipcode TEXT,
        address.geo.lat TEXT,
        address.geo.lng TEXT,
        company.name TEXT,
        company.catchPhrase TEXT,
        company.bs TEXT
    )

CREATE TABLE IF NOT EXISTS srk.posts (
        userId INTEGER,
        id INTEGER,
        text TEXT,
        body TEXT
    )

CREATE TABLE IF NOT EXISTS srk.enriched.posts (
            userId INTEGER,
            id_post INTEGER,
            text TEXT,
            body TEXT,
            id_user INTEGER,
            name TEXT,
            username TEXT,
            email TEXT,
            phone TEXT,
            website TEXT,
            address.street TEXT,
            address.suite TEXT,
            address.city TEXT,
            address.zipcode TEXT,
            address.geo.lat TEXT,
            address.geo.lng TEXT,
            company.name TEXT,
            company.catchPhrase TEXT,
            company.bs TEXT
        )
