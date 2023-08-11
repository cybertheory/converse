from schema import Skill, Thread

class Web(Thread):
      
    _web: Thread

    def __init__(self) -> None:
        pass

    def thread(self, thread) -> Thread :
        assert isinstance(thread , Thread)
        if self._web:
            thread.input = thread
            self._web = thread
        else:
            self._web = thread

    def weave(self, input) -> str:
        
        assert isinstance(input, str)
        return self._web.run(input)