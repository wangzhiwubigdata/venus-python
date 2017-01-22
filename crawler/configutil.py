import ConfigParser

def config_to_dict(config_file):
    cf = ConfigParser.ConfigParser()
    cf.read(config_file)
    result = {}
    for section in cf.sections():
        result[section] = dict(cf.items(section))
    return result

result = config_to_dict('config.ini')
print result
print result['main']['threads']