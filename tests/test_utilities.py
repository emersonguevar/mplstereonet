import pytest
import mplstereonet
import numpy as np

class TestParseStrikes:
    def test_parse_strike(self):
        data = [
                [('N30E', '45NW'), (210, 45)],
                [('210', '45'),    (210, 45)],
                [('E10N', '20NW'), (260, 20)],
                [('350', '40W'),   (170, 40)],
                [('280', '30SW'),  (100, 30)],
                [('280', '30 SW'),  (100, 30)],
               ]
        for test, correct in data:
            result = mplstereonet.parse_strike_dip(*test)
            assert np.allclose(result, correct)

class TestParseQuadrant:
    def test_parse_quadrant(self):
        data = [('N30E', 30),
                ('E30N', 60),
                ('E30S', 120),
                ('S80E', 100),
                ('S10W', 190),
                ('W10S', 260),
                ('W30N', 300),
                ('N10E', 10),
                ('N10W', 350),
                ('N 10 W', 350),
                ]
        for strike, azi in data:
            assert azi == mplstereonet.parse_quadrant_measurement(strike)

    def test_parse_quadrant_errors(self):
        data = ['N10S', 'S80N', 'E10W', 'W30E']
        for quad in data:
            with pytest.raises(ValueError):
                mplstereonet.parse_quadrant_measurement(quad)

class TestParseRakes:
    def test_parse_rake(self):
        data = [
                [('N30E', '45NW', '10NE'),  (210, 45, -10)],
                [('N30E', '45NW', '10SW'),  (210, 45, 10)],
                [('210', '45', '10'),       (210, 45, 10)],
                [('210', '45', '-10'),      (210, 45, -10)],
                [('210', '45', '170'),      (210, 45, -10)],
                [('E10N', '20NW', '80E'),   (260, 20, -80)],
                [('E10N', '20NW', '100'),   (260, 20, -80)],
                [('E10N', '20NW', '80W'),   (260, 20, 80)],
                [('350', '40W', '45N'),     (170, 40, -45)],
                [('350', '40W', '45S'),     (170, 40, 45)],
                [('280', '30SW', '30E'),    (100, 30, 30)],
                [('280', '30SW', '30W'),    (100, 30, -30)],
               ]
        for test, correct in data:
            result = mplstereonet.parse_rake(*test)
            assert np.allclose(result, correct)
