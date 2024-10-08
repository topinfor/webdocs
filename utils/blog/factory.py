from random import randint

from faker import Faker

fake = Faker('pt-BR')

def rand_radio():
    return randint (840, 900), randint(473, 573)



def make_post():
    return {
        'post_number': fake.random_number(digits=2, fix_len=True),
        'title': fake.sentence(nb_words=4),
        'description': fake.sentence(nb_words=40),
        'post_tag': fake.sentence(nb_words=2),
        'post_sector': fake.sentence(nb_words=2),
        'post_content': fake.text(3000),
        'created_at': fake.date_time(),
        'author': {
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
        },
        'category': {
            'name': fake.word(),
            },
        'cover': {
            'url': 'https://loremflickr.com/%s/%s/network,internet' % rand_radio(),
        }
    }
if __name__ == '__main__':
    from pprint import pprint
    pprint(make_post())
    