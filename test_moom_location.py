from skyfield.api import PlanetaryConstants, load

ts = load.timescale()
t = ts.utc(2019, 12, 20, 11, 5)

eph = load('de421.bsp')
earth, moon = eph['earth'], eph['moon']

pc = PlanetaryConstants()
pc.read_text(load('moon_080317.tf'))
pc.read_text(load('pck00008.tpc'))
pc.read_binary(load('moon_pa_de421_1900-2050.bpc'))

frame = pc.build_frame_named('MOON_ME_DE421')
aristarchus = moon + pc.build_latlon_degrees(frame, 26.3, -46.8)

apparent = earth.at(t).observe(aristarchus).apparent()
ra, dec, distance = apparent.radec(epoch='date')
print(ra)
print(dec)