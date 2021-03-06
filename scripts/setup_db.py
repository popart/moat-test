from neo4j.v1 import GraphDatabase, basic_auth

driver = GraphDatabase.driver("bolt://localhost:7687",
        auth=basic_auth("<username>", "<password>"))
session = driver.session()

session.run(""" create index on :Page(id) """)
session.run(""" create index on :Page(title_index) """)

session.close()
