class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]
:
        dic = collections.defaultdict(list)

        for word in strs:
            sorted_word = ''.join(sorted(word))
            dic[sorted_word].append(word)
        
        return list(dic.values())
            
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]
:
        dic = collections.defaultdict(list)

        for word in strs:
            sorted_word = ''.join(sorted(word))
            dic[sorted_word].append(word)
        
        return list(dic.values())
            