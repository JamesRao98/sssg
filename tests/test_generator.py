from unittest import TestCase 
from argparse import Namespace
from random import randint
from os import path
from shutil import rmtree

from src.sssg_James_Rao.generator import Generator
from src.sssg_James_Rao.schemas import Page


class TestGenerator(TestCase):
    def setUp(self):
        args = Namespace(
            pages='./example/pages.json',
            templates='./example/templates/',
            output='./example/output/',
            content='./example/content/'
        )
        self.generator = Generator(args)

    def tearDown(self):
        if not path.isdir(self.generator.output_base_path):
            return
        rmtree(self.generator.output_base_path)

    def test_load_pages(self):
        self.generator.load_pages()
        
        assert isinstance(self.generator.pages, list)
        assert len(self.generator.pages) > 0

        for page in self.generator.pages:
            assert isinstance(page, Page)
    
    def test_generate_page(self):
        target_path = './index.html'
        page = Page(
            template='./home.html', 
            target=target_path,
            content={
                'title': './title.txt'
            }
        )
        
        self.generator.generate_page(page)

        target_path = path.join(self.generator.output_base_path, target_path)
        assert path.isfile(target_path)
        target_file = open(target_path)
        target = target_file.read()
        assert '<title>Example Title</title>' in target 

        target_file.close()
        
    def test_generate(self):
        self.generator.generate()

        assert path.isfile(path.join(self.generator.output_base_path, './index.html'))
        assert path.isfile(path.join(self.generator.output_base_path, './page2.html'))

