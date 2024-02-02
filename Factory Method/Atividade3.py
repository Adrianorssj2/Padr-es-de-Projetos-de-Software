from abc import ABC, abstractmethod

class ConfigReader(ABC):
    @property
    @abstractmethod
    def file_format(self):
        pass

    def read_config(self, file_name):
        print(f"Lendo arquivo de configuração {file_name} no formato {self.file_format}")

class JSONConfigReader(ConfigReader):
    @property
    def file_format(self):
        return "JSON"

class XMLConfigReader(ConfigReader):
    @property
    def file_format(self):
        return "XML"

class YAMLConfigReader(ConfigReader):
    @property
    def file_format(self):
        return "YAML"

class ConfigReaderFactory:
    def __init__(self):
        self._readers = {
            "json": JSONConfigReader(),
            "xml": XMLConfigReader(),
            "yaml": YAMLConfigReader()
        }

    def create_config_reader(self, file_type):
        reader = self._readers.get(file_type.lower())
        if reader is None:
            raise ValueError("Tipo de arquivo inválido")
        return reader

def test_system(factory, file_name, file_type):
    reader = factory.create_config_reader(file_type)
    reader.read_config(file_name)

print("Testando o sistema com diferentes tipos de arquivos de configuração")
factory = ConfigReaderFactory()
file_names = ["config.json", "config.xml", "config.yaml"]
file_types = ["json", "xml", "yaml"]
for file_name, file_type in zip(file_names, file_types):
    test_system(factory, file_name, file_type)
