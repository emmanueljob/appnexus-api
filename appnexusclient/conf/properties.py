import os
import yaml
from yaml import Loader 

class Properties():

    props = None

    def __init__(self, env):
        conf_dir = os.path.dirname(os.path.realpath(__file__))
        with open("{0}/{1}.yaml".format(conf_dir, env)) as stream:
            self.props = yaml.load(stream.read(), Loader=Loader)

    def __getattr__(self, name):
        return self.props.get(name, None)
