def view(data):
    try:
        count = 1
        if len(data) > 0:
            for d in data:
                print(f'{count} :', end=" ")
                for i in d:
                    print(i, end=' ')
                count += 1
                print()
        else:
            print('Empty List')
    except Exception as e:
        print(f'Error {e}')



