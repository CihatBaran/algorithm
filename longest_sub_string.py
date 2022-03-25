# Input: String="aabccbb"
# Output: 3
# Explanation: The longest substring with distinct characters is "abc".

class DistinctCharMap(dict):
    def __missing__(self, v):
        return 0


def find_the_longest_substring_distinct(string, k=1):
    distinct_char_map = DistinctCharMap()
    temp_substring = ""
    longest_substring = ""

    for i in range(len(string)):
        char = string[i]
        distinct_char_map[char]+=1
        temp_substring+=char

        if distinct_char_map[char] > k:
            temp_substring = char
        else:
            if len(temp_substring) > len(longest_substring):
                longest_substring = temp_substring
    
    return longest_substring

def find_the_longest_substring_length_distinct(string):
    return len(find_the_longest_substring_distinct(string))

v = find_the_longest_substring_length_distinct("aabccddaefghigkbb")
print(v)


def main():
  print("Length of the longest substring: " + str(find_the_longest_substring_length_distinct("aabccbb")))
  print("Length of the longest substring: " + str(find_the_longest_substring_length_distinct("abbbb")))
  print("Length of the longest substring: " + str(find_the_longest_substring_length_distinct("abccde")))

main()

my_dict = dict(a=5, b=10)
print(my_dict)