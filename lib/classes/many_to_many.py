import datetime


class NationalPark:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not hasattr(self, "_name") and isinstance(name, str) and len(name) >= 3:
            self._name = name

    def trips(self):
        return [trip for trip in Trip.all if trip.national_park is self]

    def visitors(self):
        return list(set([trip.visitor for trip in self.trips()]))

    def total_visits(self):
        return len(self.trips())

    def best_visitor(self):
        visitors_list = self.visitors()
        if not visitors_list:
            return None

        best = visitors_list[0]
        times = best.total_visits_at_park(self)

        for visitor in visitors_list:
            current_visits = visitor.total_visits_at_park(self)
            if current_visits > times:
                best = visitor
                times = current_visits
        return best


class Trip:
    all = []

    def __init__(self, visitor, national_park, start_date, end_date):
        self._visitor = visitor
        self._national_park = national_park
        self._start_date = start_date
        self._end_date = end_date
        Trip.all.append(self)

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        if isinstance(value, str) and len(value) >= 7:
            self._start_date = value

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        if isinstance(value, str) and len(value) >= 7:
            self._end_date = value

    @property
    def visitor(self):
        return self._visitor

    @visitor.setter
    def visitor(self, visitor):
        if isinstance(visitor, Visitor):
            self._visitor = visitor

    @property
    def national_park(self):
        return self._national_park

    @national_park.setter
    def national_park(self, park):
        if isinstance(park, NationalPark):
            self._national_park = park


class Visitor:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name

    def trips(self):
        return [trip for trip in Trip.all if trip.visitor is self]

    def national_parks(self):
        return list({trip.national_park for trip in self.trips()})

    def total_visits_at_park(self, park):
        return len([trip for trip in self.trips() if trip.national_park is park])
