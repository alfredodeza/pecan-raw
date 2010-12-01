from unittest import TestCase
from pecanraw import RawHook
from pecan import make_app, expose
from webtest import TestApp


class TestHooks(TestCase):
    
    def test_basic_single_hook(self):
        run_hook = []
        
        class RootController(object):
            @expose()
            def index(self):
                return 'Hello, World!'
        
        import sys
        from StringIO import StringIO
        out = StringIO()
        sys.stdout = out
        app = TestApp(make_app(RootController(), hooks=[RawHook()]))
        response = app.get('/')
        self.assertEqual(response.status_int, 200)
        self.assertEqual(response.body, 'Hello, World!')
        expected = ['method:', 'GET', 
                'response:', '200', 'OK', 
                'url:', '/', 
                'method:', 'RootController.index', 
                'context:', '{}', 
                'params:', 'NestedMultiDict([])', 
                'hooks:', '[<pecanraw.RawHook', 'object', 'at',]
        self.assertEqual(out.getvalue().split()[:-1], expected)

