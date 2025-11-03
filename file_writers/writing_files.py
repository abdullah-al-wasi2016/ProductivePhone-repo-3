with open("disk_write2.TOG", "w") as file:
    data = """
    if [name] == ['main']:
        repos = {'rep-1', 'rep-2'}
        zipfile(repos)
        if zipfile(repos) == 'failed' or -1:
            print('Sorry')
    """
    file.write(data)
