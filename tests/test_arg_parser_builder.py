from unittest import TestCase

from src.sssg.argument_parser_builder import ArgumentParserBuilder

class TestArgumentParserBuilder(TestCase):
    def test_add_arguments(self):
        apb = ArgumentParserBuilder()
        apb.add_arguments()
        assert len(apb.parser._actions) == 5