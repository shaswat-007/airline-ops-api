import pandas as pd
from rich.console import Console
from rich.prompt import Prompt

EXCEL_FILE = "flights.xlsx"
console = Console()

def load_flights():
    try:
        return pd.read_excel(EXCEL_FILE)
    except FileNotFoundError:
        return pd.DataFrame(columns=["FlightNo", "Origin", "Destination", "Date"])

def save_flights(df):
    df.to_excel(EXCEL_FILE, index=False)

def add_flight():
    flight_no = Prompt.ask("Flight Number")
    origin = Prompt.ask("Origin")
    destination =  Prompt.ask("Destination")
    date = Prompt.ask("Date (YYYY-MM-DD)")
    df = load_flights()
    new_row = pd.DataFrame([{
        "FlightNo": flight_no,
        "Origin": origin,
        "Destination": destination,
        "Date": date
    }])
    df = pd.concat([df,new_row],ignore_index=True)
    save_flights(df)
    console.print("[green]Flight Added Successfully![/green]")

def view_flights():
    df = load_flights()    
    if df.empty:
        console.print("[yellow]No flights found.[/yellow]")
    else:
        console.print(df)

def menu():
    while True:
        console.print("\n[bold cyan]Airline Ops Manager[/bold cyan]")
        console.print("1. Add Flight")
        console.print("2. View Flights")
        console.print("3. Exit")
        choice = Prompt.ask("Choose an option", choices = ["1", "2", "3"])
        if choice == "1":
            add_flight()
        if choice == "2":
            view_flights()
        else:
            console.print("Saiyonara!!")
            break


if __name__ == "__main__":
    menu()