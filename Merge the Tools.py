def merge_the_tools(string, k):
    # your code goes here
    remaining_index = len(string)
    index_now = 0

    while remaining_index >= k:
        new_list = string[index_now:index_now+k]
        new_list = list(dict.fromkeys(new_list))
        print(''.join(new_list))
        index_now += k
        remaining_index -= k
    
    if remaining_index != 0:
        remaining_list = list(dict.fromkeys(string[index_now:]))
        print(''.join(remaining_list))
        
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
