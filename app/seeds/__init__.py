from flask.cli import AppGroup
from .users import seed_users, undo_users
from .categories import seed_categories, undo_categories
from .category_details import seed_category_details, undo_category_details
from .items import seed_items, undo_items
from .menu_sections import seed_menu_sections, undo_menu_sections
from .restaurants import seed_restaurants, undo_restaurants

# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')


# Creates the `flask seed all` command
@seed_commands.command('all')
def seed():
    seed_users()
    seed_restaurants()
    seed_menu_sections()
    seed_items()
    seed_categories()
    # Add other seed functions here


# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
    undo_categories()
    undo_items()
    undo_menu_sections()
    undo_restaurants()
    undo_users()
    # Add other undo functions here
