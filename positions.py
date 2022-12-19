from skyfield.api import N, W, wgs84, load

eph = load('de421.bsp')
class Stars(object):
    all_stars = ['sun',    'moon',   'earth', 'mars', 'mercury', 'venus']
    labelss   = ['sun',    'moon',   'earth', 'mars', 'mercury', 'venus']
    colors    = ['Orange', 'yellow', 'blue',  'Red',  'black',   'silver' ]
    sizes     = [100,       50,       50,      50,     50,       50 ]
    positions = []

    def __init__(self, time, observer) -> None:
        '''
        :param TimeScale time
        '''
        self.earth = eph['earth']
        self.time  = time
        self.observer = observer
        self.observe_all()

    def observe(self, target, only_azimuth=True):
        pos = (self.earth + self.observer).at(self.time).observe(target).apparent().altaz()
        if only_azimuth:
            return pos[0]
        else:
            return pos

    def get_positions(self):
        pass

    def observe_all(self, form="rad"):
        star_positions = {}
        self.positions = []
        for star in self.all_stars:
            if form=="rad":
                star_positions[star] = self.observe(target=eph[star]).radians
            elif form=="degree":
                star_positions[star] = self.observe(target=eph[star]).degrees
            else:
                raise "Star not found."
            self.positions.append(star_positions[star])
        self.star_positions = star_positions
        return self.positions
