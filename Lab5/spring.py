from season_tools import spring_start_date

def main():
    try:
        # Läser in temperaturer från användaren
        temperatures = input("Ange dygnsmedeltemperaturer: ").split()
        temperatures = [float(temp) for temp in temperatures]  # Konvertera till flyttal

        # Beräknar vårens ankomstdatum
        spring_date = spring_start_date(temperatures)
        print(f"Vårens ankomst: {spring_date}")

    except ValueError as e:
        # Hanterar fel och skriver ut ett användarvänligt meddelande
        print(e)
    except Exception as e:
        # Hanterar oväntade fel
        print(f"Ett oväntat fel inträffade: {e}")

if __name__ == "__main__":
    main()
