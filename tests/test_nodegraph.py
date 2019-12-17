import pytest
from sourmash.nodegraph import Nodegraph

from . import sourmash_tst_utils as utils


def test_nodegraph_to_khmer():
    pytest.importorskip('khmer')

    ng_file = utils.get_test_data('.sbt.v3/internal.0')

    ng = Nodegraph.load(ng_file)
    khmer_ng = ng.to_khmer_nodegraph()

    assert ng.ksize == khmer_ng.ksize()
