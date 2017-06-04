import cProfile, pstats, io
class Profiler:
    profile = None
    profile_stats = None
    profile_stream = None
    stats = ''
    def __init__(self):
        self.profile = cProfile.Profile()
                                
    def __enter__(self):
        if(self.profile_stream == None):
            self.profile_stream = io.StringIO()
        self.profile.clear()
        self.profile.enable()
        
    def __exit__(self, exc_type, exc_value, traceback):
        self.profile.disable()
        self.profile_stats = pstats.Stats(self.profile, stream = self.profile_stream)
        self.change_ordering('cumulative')
        
    def change_ordering(self, new_ordering):
        self.profile_stats.sort_stats(new_ordering)
        
    def report(self):
        if(self.profile_stream == None):
            #self.profile.print_stats()
            return self.stats
        self.profile.print_stats()
        self.stats = self.profile_stream.getvalue()
        self.profile_stream.close()
        self.profile_stream = None
        return self.stats
    
p = Profiler()
with p:
    print('cupcake')
p.profile_stats.sort_stats('cumulative')
print(p.report())
with p:
    print('zero')
print(p.report())
print(p.report())