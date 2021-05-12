def make_shirt(size, message):
    """Display shirt's size and a message printed on it."""
    print(f"\nSize: {size.upper()}")
    print(f"Message: {message}")

make_shirt('L', 'Le lapin')
make_shirt(message='Le lapin', size='L')