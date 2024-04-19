import json
from pathlib import Path


class SchemaLoader:
    base_path = Path.cwd().joinpath('schemas')

    @classmethod
    def _get_json_file(cls, schema_name):
        if '.json' in schema_name:
            path = cls.base_path.joinpath(schema_name)
        else:
            path = cls.base_path.joinpath(f'{schema_name}.json')
        return path

    @classmethod
    def read_file(cls, schema_name):
        path = cls._get_json_file(schema_name)
        with path.open(mode='r') as f:
            return json.load(f)
