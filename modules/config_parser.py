from configparser import ConfigParser


def config(filename='database/database.ini', section='postgresql'):
    parser = ConfigParser()
    parser.read(filename)

    database_login = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            database_login[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return database_login