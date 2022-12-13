my_fave_songs = {
    "Alice In Chains":"Sunshine",
    "Ghost":"Square Hammer",
    "Type O Negative":"Red Water",
    "Twin Temple":"Wicked",
    "Ice Nine Kills":"IT Is the End",
    "Rammstein":"Deutschland",
    "The Mission":"Love Me to Death",
    "Koza Mostra":"Alcohol is Free"
}

def song_titles(dict):
    values = dict.values()    
    print("My favourite songs are " + ', '.join(values))

song_titles(my_fave_songs)

my_fave_bands = ["Ghost", "Type O Negative", "Ice Nine Kills", "Alice In Chains", "Rammstein", "Twin Temple", "The Mission"]

def not_like_the_others(dict, bands):
    keys = dict.keys()
    keys = list(keys)
    bands.sort()
    keys.sort()
    different = [string for string in keys if string not in bands]
    print((" ".join(different) + " is not my favourite band, but I love one of their songs!"))


not_like_the_others(my_fave_songs, my_fave_bands)
