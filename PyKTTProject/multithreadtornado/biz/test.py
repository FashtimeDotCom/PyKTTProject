from util.route import Router

class Test(object):
    @Router.route(url = r"me/world", method = Router._GET|Router._POST)
    def test_hello(self,handler):
        return "hello world" 
