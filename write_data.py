from start import Cat, Dog

cat_of_mine = Cat('Молі', 3)
dog_of_mine = Cat('Жучка', 5)


with open('cat.txt', 'a') as f_cat:
    data = cat_of_mine.log_cat()
    f_cat.write(f'{data.get('name')} - {data.get('age')}')

with open('dog.txt', 'a') as f_dog:
    data = cat_of_mine.log_cat()
    f_dog.write(f'{data.get('name')} - {data.get('age')}')
