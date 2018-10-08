import os

from sqla_filters.parser.yaml import YAMLFiltersParser


class TestYamlFilterParser(object):
    def test_1_raw_data(self):
        path = os.path.join(
            os.path.dirname(__file__),
            'resources/sample_1.yml'
        )
        with open(path) as f:
            data = f.read()
            yaml_parser = YAMLFiltersParser(data)
            assert yaml_parser.raw_data == data

    def test_2_parse_data_sample_1(self):
        path = os.path.join(
            os.path.dirname(__file__),
            'resources/sample_1.yml'
        )
        with open(path) as f:
            data = f.read()
            yaml_parser = YAMLFiltersParser(data)
            print(yaml_parser.tree)

    def test_2_parse_data_sample_2(self):
        path = os.path.join(
            os.path.dirname(__file__),
            'resources/sample_2.yml'
        )
        with open(path) as f:
            data = f.read()
            yaml_parser = YAMLFiltersParser(data)
            print(yaml_parser.tree)

    def test_3_parse_data_sample_3(self):
        path = os.path.join(
            os.path.dirname(__file__),
            'resources/sample_3.yml'
        )
        with open(path) as f:
            data = f.read()
            yaml_parser = YAMLFiltersParser(data)
            print(yaml_parser.tree)