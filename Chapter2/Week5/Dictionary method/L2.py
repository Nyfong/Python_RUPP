dic = {
    1:'1'
}
# dic.update( [ 
#              [1,
#                 [1,"apple"], 
#                 [2,"cocal"]
#              ],
#             [2,'2']
#             ] )
dic.update([
    # First item in the list is a list itself
    [
        1,              # Key
        [1, "apple"],   # Value (a list)
        [2, "cocal"]    # Value (a list)
    ],
    # Second item in the list is now a list instead of a tuple
    [2, '2']            # Key-value pair (list)
])
print(dic)