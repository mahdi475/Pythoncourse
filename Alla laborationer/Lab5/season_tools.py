from datetime import date, timedelta

def spring_start_date(temperatures):
    """
    Bestämmer datumet för vårens ankomst.
    
    Temperaturen ska vara över 0°C sju dagar i följd för att våren ska räknas som kommen.
    Temperaturen börjar från 15 februari 2024.
    """
    if len(temperatures) < 7:
        raise ValueError("Minst sju dygnsmedeltemperaturer behövs")

    start_date = date(2024, 2, 15)
    for i in range(len(temperatures) - 6):
        # Kontrollera om det finns 7 dagar i rad med temperatur > 0
        if all(temp > 0 for temp in temperatures[i:i + 7]):
            arrival_date = start_date + timedelta(days=i)
            if arrival_date > date(2024, 7, 31):
                raise ValueError("Vårens ankomst kan inte vara senare än 31 juli")

            return arrival_date

    # Om inga 7 dagar i följd hittas
    raise ValueError("Våren är inte här än")
