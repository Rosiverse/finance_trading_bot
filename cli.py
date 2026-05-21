#!/usr/bin/env python3
import sys
import questionary
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

from bot.orders import OrderManager
from bot.logging_config import logger

console = Console()

def display_order_summary(order_data: dict, success: bool):
    if success:
        console.print(Panel("[bold green]Order Successfully Placed![/bold green]", expand=False))
        
        table = Table(show_header=True, header_style="bold cyan")
        table.add_column("Order ID", style="dim")
        table.add_column("Status")
        table.add_column("Executed Qty", justify="right")
        table.add_column("Avg Price / Price", justify="right")

        order_id = str(order_data.get("orderId", "N/A"))
        status = order_data.get("status", "N/A")
        executed_qty = str(order_data.get("executedQty", "0"))
        
        price = order_data.get("avgPrice")
        if not price or float(price) == 0:
            price = order_data.get("price", "N/A")

        table.add_row(order_id, status, executed_qty, str(price))
        console.print(table)
    else:
        console.print(f"[bold red]Order Failed:[/bold red] {order_data}")

def main():
    console.print("[bold yellow]Welcome to the Binance Futures Trading Bot (Testnet)[/bold yellow]")
    
    try:
        symbol = questionary.text("Enter trading symbol (e.g., BTCUSDT):", default="BTCUSDT").ask()
        if not symbol: return

        side = questionary.select(
            "Select order side:",
            choices=["BUY", "SELL"]
        ).ask()
        if not side: return

        order_type = questionary.select(
            "Select order type:",
            choices=["MARKET", "LIMIT"]
        ).ask()
        if not order_type: return

        quantity_str = questionary.text("Enter quantity:").ask()
        if not quantity_str: return
        
        try:
            quantity = float(quantity_str)
        except ValueError:
            console.print("[bold red]Invalid quantity format.[/bold red]")
            return

        price = None
        if order_type == "LIMIT":
            price_str = questionary.text("Enter limit price:").ask()
            if not price_str: return
            try:
                price = float(price_str)
            except ValueError:
                console.print("[bold red]Invalid price format.[/bold red]")
                return

        console.print("\n[bold cyan]Order Preview:[/bold cyan]")
        preview_table = Table(show_header=False)
        preview_table.add_column("Field", style="bold")
        preview_table.add_column("Value")
        preview_table.add_row("Symbol", symbol)
        preview_table.add_row("Side", side)
        preview_table.add_row("Type", order_type)
        preview_table.add_row("Quantity", str(quantity))
        if order_type == "LIMIT":
            preview_table.add_row("Price", str(price))
        
        console.print(preview_table)
        
        confirm = questionary.confirm("Execute this order?").ask()
        if not confirm:
            console.print("[yellow]Order cancelled.[/yellow]")
            return
        
        order_manager = OrderManager()
        console.print("[dim]Sending order to Binance Testnet...[/dim]")
        
        response = order_manager.place_order(
            symbol=symbol,
            side=side,
            order_type=order_type,
            quantity=quantity,
            price=price
        )
        
        display_order_summary(response, success=True)

    except KeyboardInterrupt:
        console.print("\n[yellow]Exiting trading bot...[/yellow]")
        sys.exit(0)
    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {str(e)}")
        logger.exception("A runtime error occurred.")

if __name__ == "__main__":
    main()
