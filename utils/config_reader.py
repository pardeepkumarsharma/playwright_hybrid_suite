import yaml

class Config_Reader:
    def __init__(self):
        with open("../config.yaml") as file:
            self.data=  yaml.safe_load(file)
            print(self.data)


    def get(self, key):
        environment = self.data["env"]
        env_f = self.data[environment]
        return env_f.get(key, self.data.get(key))

if __name__== "__main__":
    c = Config_Reader()
    print(c.get("url"))
