class NationalPark:
    def __init__(self, name):
        self.name = name

    # NationalPark - name getter/setter:
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not hasattr(self, "_name") and isinstance(name, str) and len(name) >= 3:
            self._name = name

    # Returns a list of all trips at a particular national park. Trips must be of type Trip:
    def trips(self):
        return [trip for trip in Trip.all if trip.national_park is self]

    # Returns a unique list of all visitors a particular national park has welcomed. Visitors must be of type Visitor:
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
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        Trip.all.append(self)

    # Trip - start_date getter/setter:
    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        if isinstance(value, str) and len(value) >= 7:
            self._start_date = value

    # Trip - end_date getter/setter:
    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        if isinstance(value, str) and len(value) >= 7:
            self._end_date = value

    # Trip - visitor getter/setter. Returns the Visitor object for that trip. Must be of type Visitor:
    @property
    def visitor(self):
        return self._visitor

    @visitor.setter
    def visitor(self, visitor):
        if isinstance(visitor, Visitor):
            self._visitor = visitor

    # Trip - national_park getter/setter. Returns the NationalPark object for that trip. Must be of type NationalPark:
    @property
    def national_park(self):
        return self._national_park

    @national_park.setter
    def national_park(self, national_park):
        if isinstance(national_park, NationalPark):
            self._national_park = national_park


class Visitor:
    def __init__(self, name):
        self.name = name

    # Visitor - name getter/setter:
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name

    # Returns a list of all trips for that visitor. Trips must be of type Trip:
    def trips(self):
        return [trip for trip in Trip.all if trip.visitor is self]

    # Returns a unique list of all parks that visitor has visited. Parks must be of type NationalPark:
    def national_parks(self):
        return list({trip.national_park for trip in self.trips()})

    # Receives a NationalPark object as argument. Returns the total number of times a visitor visited the park passed in as argument. Returns 0 if the visitor has never visited the park:
    def total_visits_at_park(self, park):
        return len([trip for trip in self.trips() if trip.national_park is park])
