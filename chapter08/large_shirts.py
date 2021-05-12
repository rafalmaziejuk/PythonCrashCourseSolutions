def make_shirt(size='L', message='I love Python'):
    """Display shirt's size and a message printed on it."""
    print(f"\nSize: {size.upper()}")
    print(f"Message: {message}")

make_shirt()
make_shirt(size='M')
make_shirt(message='Le lapin', size='S')