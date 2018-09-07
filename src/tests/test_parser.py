from sqla_filters.parser.yaml import YAMLFiltersParser


class TestYamlFilterParser(object):
    def test_1_raw_data(self):
        with open('./resources/sample_1.yml') as f:
            data = f.read()
            yaml_parser = YAMLFiltersParser(data)
            assert yaml_parser.raw_data == data

    def test_2_parse_data(self):
        with open('./resources/sample_1.yml') as f:
            data = f.read()
            yaml_parser = YAMLFiltersParser(data)

        with open('./resources/sample_2.yml') as f:
            data = f.read()
            yaml_parser = YAMLFiltersParser(data)

        with open('./resources/sample_3.yml') as f:
            data = f.read()
            yaml_parser = YAMLFiltersParser(data)
