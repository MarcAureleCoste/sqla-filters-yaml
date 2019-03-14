import os
from typing import Dict

from sqla_filters.parser.yaml import YAMLFiltersParser
from sqla_filters.nodes.logical import AndNode
from sqla_filters.nodes.operational import (
    EqNode,
    NotEqNode,
    NullNode,
    NotNullNode,
    GtNode,
    GteNode,
    LtNode,
    LteNode,
    InNode,
    NotInNode,
    ContainsNode,
    LikeNode
)


class TestParserBase(object):
    _resources: Dict = {}

    def _get_parser(self, key: str) -> YAMLFiltersParser:
        """Return a parser instance."""
        file_path = os.path.join(
            os.path.dirname(__file__),
            self._resources[key]
        )
        json_data = open(file_path).read()
        return YAMLFiltersParser(json_data)


class TestYamlEquality(TestParserBase):
    def setup_class(self):
        self._resources['eq'] = 'resources/eq/eq.yml'
        self._resources['noteq'] = 'resources/eq/noteq.yml'
        self._resources['eq_rel'] = 'resources/eq/eq_rel.yml'
        self._resources['noteq_rel'] = 'resources/eq/noteq_rel.yml'

    def test_01_eq(self):
        parser = self._get_parser('eq')
        assert isinstance(parser.tree.root, AndNode)
        assert len(parser.tree.root.childs) == 1
        assert isinstance(parser.tree.root.childs[0], EqNode)
        assert parser.tree.root.childs[0].attribute == 'name'
        assert parser.tree.root.childs[0].value == 'Toto'

    def test_02_noteq(self):
        parser = self._get_parser('noteq')
        assert isinstance(parser.tree.root, AndNode)
        assert len(parser.tree.root.childs) == 1
        assert isinstance(parser.tree.root.childs[0], NotEqNode)
        assert parser.tree.root.childs[0].attribute == 'name'
        assert parser.tree.root.childs[0].value == 'Toto'

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