from nose.tools import *

from lctools.shortcuts import get_node_or_fail

class TestShortCuts(object):

    def setup(self):
        class MyNode(object):

            def __init__(self, id):
                self.id = id

        class MyConn(object):

            def __init__(self, nodes):
                self.nodes = nodes

            def list_nodes(self):
                return self.nodes

        self.node_cls = MyNode
        self.conn_cls = MyConn

    def test_that_get_node_or_fail_returns_node_object_for_existing_node(self):
        conn = self.conn_cls([self.node_cls("15"), self.node_cls("21")])

        node = get_node_or_fail(conn, "15")

        assert_equal(node.id, "15")

    def test_that_get_node_or_fail_returns_none_in_fail_case(self):
        conn = self.conn_cls([])

        node = get_node_or_fail(conn, "15")

        assert_true(node is None)

    def test_that_get_node_or_fail_calls_coroutine_in_fail_case(self):
        class CallableCheck(object):
            called = False
            args = None
            kwargs = None

            def __call__(self, *args, **kwargs):
                self.called = True
                self.args = args
                self.kwargs = kwargs

        coroutine = CallableCheck()
        cargs = ("Error happened",)
        ckwargs = {"node_id": "15"}

        conn = self.conn_cls([])

        node = get_node_or_fail(conn, "15",
                coroutine, cargs, ckwargs)

        assert_true(coroutine.called)
        assert_equal(coroutine.args, cargs)
        assert_equal(coroutine.kwargs, ckwargs)
