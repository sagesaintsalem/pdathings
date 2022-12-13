my_fave_bands = ["Ghost", "Type O Negative", "Ice Nine Kills", "Alice In Chains", "Rammstein", "Twin Temple", "The Mission"]

def sorted_and_pretty(list):
    list.sort()
    position = 1
    for i in list:
        print(str(position) + ': ' + i)
        position += 1


sorted_and_pretty(my_fave_bands)