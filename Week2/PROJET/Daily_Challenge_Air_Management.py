from datetime import date
# The Airline Class
class Airline:
    def __init__(self, id: str, name: str):
        self.id = id
        self.name = name
        self.planes = []

# The Airplane Class
class Airplane:
    def __init__(self, id: int, current_location, company):
        self.id = id
        self.current_location = current_location
        self.company = company
        self.next_flights = []

    def location_on_date(self, flight_date):
        location = self.current_location
        for flight in sorted(self.next_flights, key=lambda f: f.date):
            if flight.date > flight_date:
                break
            location = flight.destination
        return location

    def available_on_date(self, flight_date, location):
        if self.location_on_date(flight_date) != location:
            return False

        for flight in self.next_flights:
            if flight.date == flight_date:
                return False  # un seul vol par jour
        return True

    def fly(self, destination):
        for flight in self.next_flights:
            if flight.destination == destination:
                flight.take_off()
                flight.land()
                self.next_flights.remove(flight)
                return
        raise Exception("No scheduled flight for this destination")


# The Flight Class
class Flight:
    def __init__(self, flight_date, origin, destination, plane):
        self.date = flight_date
        self.origin = origin
        self.destination = destination
        self.plane = plane
        self.id = f"{destination.city}-{plane.company.id}-{flight_date}"

    def take_off(self):
        if self.plane in self.origin.planes:
            self.origin.planes.remove(self.plane)

    def land(self):
        self.plane.current_location = self.destination
        self.destination.planes.append(self.plane)


class Airport:
    def __init__(self, city: str):
        self.city = city
        self.planes = []
        self.scheduled_departures = []
        self.scheduled_arrivals = []

    def schedule_flight(self, destination, flight_date):
        for plane in self.planes:
            if plane.available_on_date(flight_date, self):
                flight = Flight(flight_date, self, destination, plane)

                plane.next_flights.append(flight)
                plane.next_flights.sort(key=lambda f: f.date)

                self.scheduled_departures.append(flight)
                self.scheduled_departures.sort(key=lambda f: f.date)

                destination.scheduled_arrivals.append(flight)
                destination.scheduled_arrivals.sort(key=lambda f: f.date)

                return flight
        raise Exception("No available airplane")

    def info(self, start_date, end_date):
        for flight in self.scheduled_departures:
            if start_date <= flight.date <= end_date:
                print(f"Flight {flight.id} from {flight.origin.city} to {flight.destination.city} on {flight.date}")




# =========================
# Example usage
# =========================

# Airlines
royal_air = Airline("RA", "Royal Air")

# Airports
casablanca = Airport("CMN")
paris = Airport("CDG")

# Airplanes
plane1 = Airplane(1, casablanca, royal_air)

royal_air.planes.append(plane1)
casablanca.planes.append(plane1)

# Schedule flight
flight_date = date(2026, 1, 10)
flight = casablanca.schedule_flight(paris, flight_date)

# Display info
casablanca.info(date(2026, 1, 1), date(2026, 1, 31))

# Fly the plane
plane1.fly(paris)

print("Plane current location:", plane1.current_location.city)
