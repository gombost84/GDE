### Használat

PostgreSQL indítása Dockerben


    docker pull postgres:latest
    docker run --name pg2 -e POSTGRES_PASSWORD=postgres -p 5488:5432 -d postgres:latest
    docker stop pg2
    docker start pg2
    docker exec -it pg2 psql -U postgres

    select version();

Ezután a repoban található sql scripteket lehet futtatni az adatbázison.

1_create_tables.sql - létrehozza a táblákat és a köztük lévő kapcsolatokat

2_insert_initial_data.sql - létrehoz néhány rekordot minden táblában tesztelés céljából

3_test_queries.sql - néhány teszt lekérdezés, hogy biztosan minden jól működik

4_update_stock_after_order_trig.sql - trigger a készlet módosításához egy vásárlás után

5_invoice_generate_proc.sql - procedure a számla generáláshoz vásárláskor

6_bestselling_proc.sql - procedure a legjobban fogyó könyvek lekérdezéséhez

7_test_query.sql - még egy lekérdezés teszteléshez