import yaml

from sqla_filters.filter import SqlaFilterTree
from sqla_filters.parser.base import BaseSqlaParser


class YAMLFiltersParser(BaseSqlaParser):
    def __init__(self, json_str: str, attr_sep: str = '.') -> None:
        super(YAMLFiltersParser, self).__init__(json_str, attr_sep)

    def _generate_filters_tree(self) -> SqlaFilterTree:
        yaml_dict = yaml.load(self._raw_data)
        print(yaml_dict)
        return SqlaFilterTree()
