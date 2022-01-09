# write tests for parsers

from seqparser import (FastaParser, FastqParser)


def test_freebie_parser_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True


def test_freebie_parser_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_FastaParser():
    """
    Write your unit test for your FastaParser
    class here. You should generate an instance of
    your FastaParser class and assert that it properly
    reads in the example Fasta File.
    """
    parser = FastaParser("data/test.fa")
    record_count = 0
    for record in parser:
        assert len(record) == 2
        assert record[0][:3] == "seq"
        assert len(record[1]) == 100
        record_count += 1
    assert record_count == 100


def test_FastqParser():
    """
    Write your unit test for your FastqParser
    class here. You should generate an instance of
    your FastqParser class and assert that it properly
    reads in the example Fastq File.
    """
    parser = FastqParser("data/test.fq")
    record_count = 0
    for record in parser:
        assert len(record) == 3
        assert record[0][:3] == "seq"
        assert len(record[1]) == 100
        assert len(record[2]) == 100
        record_count += 1
    assert record_count == 100