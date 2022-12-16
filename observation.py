import datetime
import skyfield
from pytz import timezone
from skyfield import almanac
from skyfield.api import N, W, wgs84, load
from skyfield.magnitudelib import planetary_magnitude


zone = timezone('US/Eastern')
now = zone.localize(datetime.datetime.now())
midnight = now.replace(hour=0, minute=0, second=0, microsecond=0)
next_midnight = midnight + datetime.timedelta(days=1)

ts = load.timescale()
t0 = ts.from_datetime(midnight)
t1 = ts.from_datetime(next_midnight)
eph = load('de421.bsp')
bluffton = wgs84.latlon(40.8939 * N, 83.8917 * W)

eph = load('de421.bsp')
def sun_location(observer_location, query_time=None, zone_name='Asia/Shanghai', eph=eph):
    assert type(query_time) is datetime.datetime or query_time is None, "time should be datetime.datetime"
    assert type(observer_location) is skyfield.toposlib.GeographicPosition
    zone = timezone(zone_name)
    query_time = datetime.datetime.now() if query_time is None else query_time 
    now = zone.localize(datetime.datetime.now())
    ts = load.timescale()
    t0 = ts.from_datetime(now)
    astrometric = eph['earth'].at(t0).observe(eph['jupiter barycenter'])
    print(astrometric.position)


if __name__=="__main__":
    shanghai = wgs84.latlon(31.256 * N, 121.547 * W)
    sun_location(shanghai)