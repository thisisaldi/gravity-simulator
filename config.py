WINDOW_SIZE = WINDOW_WIDTH, WINDOW_HEIGHT = 800, 800
FPS = 60
VEL_SCALE = 10**7

ONE_SECOND = 1
ONE_MINUTE = 60 * ONE_SECOND
ONE_HOUR = 60 * ONE_MINUTE
ONE_DAY = ONE_HOUR * 24
ONE_WEEK = ONE_DAY * 7
ONE_MONTH = ONE_DAY * 30
ONE_YEAR = ONE_DAY * 365

AU = 149.6e6 * 1000
G = 6.67428e-11
SCALE = 10 / AU

SUN = { 
    'x': 0,
    'y': 0,
    'radius': 3,
    'color': 'yellow',
    'mass': 1.98892 * 10**30,
    'sun': True,
}

PLANETS = {
    'mercury': {
        'x': -0.39,
        'y': 0,
        'radius': 1,
        'color': 'gray',
        'mass': 3.3011 * 10**23,  # mercury
        'y_vel': 47.87 * 1000
    },
    'venus': {
        'x': -0.72,
        'y': 0,
        'radius': 1,
        'color': 'orange',
        'mass': 4.8675 * 10**24,  # venus
        'y_vel': 35.02 * 1000
    },
    'earth': {
        'x': -1,
        'y': 0,
        'radius': 1,
        'color': 'blue',
        'mass': 5.9742 * 10**24,  # earth
        'y_vel': 29.783 * 1000
    },
    'mars': {
        'x': -1.52,
        'y': 0,
        'radius': 1,
        'color': 'red',
        'mass': 6.39 * 10**23,  # mars
        'y_vel': 24.077 * 1000
    },
    'jupiter': {
        'x': -5.2,
        'y': 0,
        'radius': 1,
        'color': 'orange',
        'mass': 1.898 * 10**27,  # jupiter
        'y_vel': 13.07 * 1000
    },
    'saturn': {
        'x': -9.58,
        'y': 0,
        'radius': 1,
        'color': 'yellow',
        'mass': 5.683 * 10**26,  # saturn
        'y_vel': 9.69 * 1000
    },
    'uranus': {
        'x': -19.22,
        'y': 0,
        'radius': 1,
        'color': 'cyan',
        'mass': 8.681 * 10**25,  # uranus
        'y_vel': 6.81 * 1000
    },
    'neptune': {
        'x': -30.05,
        'y': 0,
        'radius': 1,
        'color': 'blue',
        'mass': 1.024 * 10**26,  # neptune
        'y_vel': 5.43 * 1000
    }
}

OBJECTS = list(PLANETS.values()) + [SUN]
