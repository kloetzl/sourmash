import pytest
from sourmash.nodegraph import Nodegraph

from . import sourmash_tst_utils as utils


def test_nodegraph_to_khmer():
    khmer = pytest.importorskip('khmer')

    ng_file = utils.get_test_data('.sbt.v3/internal.0')

    sourmash_ng = Nodegraph.load(ng_file)
    khmer_sm_ng = sourmash_ng.to_khmer_nodegraph()

    assert sourmash_ng.ksize == khmer_ng.ksize()

    khmer_ng = khmer.load_nodegraph(ng_file)
