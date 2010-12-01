from pecan.hooks import PecanHook
from pecan.routing  import lookup_controller

class RawHook(PecanHook):
    """Simple Pecan Hook to have some information about what is 
    going on in a single request. 
    No errors need to happen to get it triggered.
    """

    def after(self, state):
        try:
            print "\nmethod:  \t %s" % state.request.method
            print "response:  \t %s" % state.response.status
            print "url:       \t %s" % state.request.path
            print "method:    \t %s" % self.get_controller(state)
            print "context:   \t %s" % state.request.context
            print "params:    \t %s" % state.request.str_params
            print "hooks:     \t %s" % state.app.hooks

        except Exception, error:
            print error

    def get_controller(self, state):
        path = state.request.path.split('/')[1:]
        controller, reminder = lookup_controller(state.app.root, path)
        return controller.__str__().split()[2]

