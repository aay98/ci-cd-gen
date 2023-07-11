import random
import psycopg2 

buzz = ('continuous testing', 'continuous integration',
    'continuous deployment', 'continuous improvement', 'devops')
adjectives = ('complete', 'modern', 'self-service', 'integrated', 'end-to-end')
adverbs = ('remarkably', 'enormously', 'substantially', 'significantly',
    'seriously')
verbs = ('accelerates', 'improves', 'enhances', 'revamps', 'boosts')

def sample(l, n = 1):
    result = random.sample(l, n)
    if n == 1:
        return result[0]
    return result

def insert_phrase(phrase_name):
    """ insert a new phrase into the phrases table """
    sql = """INSERT INTO phrases(phrase_name)
             VALUES(%s) RETURNING phrase_id;"""
    conn = None
    phrase_id = None

    create=f"CREATE TABLE IF NOT EXISTS phrases (phrase_id bigint,phrase_name varchar(128));"
    
    try:
        # connect to the PostgreSQL database
        conn = psycopg2.connect(database="bd", user="alpine",
                        password="alpine", host="db", port="5432")
        # create a new cursor
        cur = conn.cursor()
        # add tablename
        cur.execute(create)
        # execute the INSERT statement
        cur.execute(sql, (phrase_name,))
        # get the generated id back
        phrase_id = cur.fetchone()[0]
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return phrase_id

def generate_buzz():
    buzz_terms = sample(buzz, 2)
    phrase = ' '.join([sample(adjectives), buzz_terms[0], sample(adverbs),
        sample(verbs), buzz_terms[1]])
    insert_phrase(phrase.title())

    #close connection
    return phrase.title()

if __name__ == "__main__":
    print (generate_buzz())