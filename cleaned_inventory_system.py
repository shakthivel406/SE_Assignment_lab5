"""
Inventory management system module.
Provides functions to add, remove, and inspect stock items.
"""

import json
from datetime import datetime
from typing import Dict, List


class InventorySystem:
    """Class to manage inventory stock data."""

    def __init__(self) -> None:
        """Initialize the inventory with empty stock storage."""
        self.stock_data: Dict[str, int] = {}
        self.logs: List[str] = []

    def add_item(self, item: str, qty: int = 0) -> None:
        """Add quantity to an item, creating it if missing."""
        if not isinstance(item, str) or not isinstance(qty, int):
            raise ValueError("Item must be a string n qty as str")
        self.stock_data[item] = self.stock_data.get(item, 0) + qty
        timestamp = datetime.now().isoformat()
        self.logs.append(f"{timestamp}: Added {qty} of {item}")

    def remove_item(self, item: str, qty: int) -> None:
        """Remove a given quantity from an item if it exists."""
        try:
            self.stock_data[item] -= qty
            if self.stock_data[item] <= 0:
                del self.stock_data[item]
        except KeyError:
            print(f"Item '{item}' not found. Nothing removed.")

    def get_qty(self, item: str) -> int:
        """Return the quantity of a given item."""
        return self.stock_data.get(item, 0)

    def load_data(self, file: str = "inventory.json") -> None:
        """Load inventory data from JSON file."""
        try:
            with open(file, "r", encoding="utf-8") as f:
                self.stock_data = json.load(f)
        except FileNotFoundError:
            print("No saved data found. Starting with empty inventory.")

    def save_data(self, file: str = "inventory.json") -> None:
        """Save inventory data to JSON file."""
        with open(file, "w", encoding="utf-8") as f:
            json.dump(self.stock_data, f, indent=4)

    def print_data(self) -> None:
        """Print the current inventory."""
        print("Items Report")
        for item, qty in self.stock_data.items():
            print(f"{item} -> {qty}")

    def check_low_items(self, thresh: int = 5) -> List[str]:
        """Return a list of items with quantity below threshold."""
        return [item for item, qty in self.stock_data.items() if qty < thresh]


def main() -> None:
    """Example usage of the inventory system."""
    inventory = InventorySystem()
    inventory.add_item("apple", 10)
    inventory.add_item("banana", 2)
    inventory.remove_item("apple", 3)
    inventory.print_data()
    print("Low items:", inventory.check_low_items())
    inventory.save_data()
    inventory.load_data()
    inventory.print_data()


if __name__ == "__main__":
    main()
