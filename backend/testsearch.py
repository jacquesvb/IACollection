from api.utility import Utility

# Can focus the search. Ex: collection:computermagazines AND title:byte

# amigaworld = Utility.search_archive('collection:computermagazines AND title:amiga world')
# print(amigaworld)

amiga_meta = Utility.get_meta_data('amiga-world-1990-06')
print(amiga_meta)