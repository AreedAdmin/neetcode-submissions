class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        adictionary={}
        seen=set()
        result=[]
        for word in strs:
            encoded=[0]*26
            for char in word:
                
                encoded_char_index=ord(char)-97
                encoded[encoded_char_index]+=1


            if str(encoded) in seen:
                adictionary[str(encoded)].append(word)

            else:
                adictionary[str(encoded)]=[word]
                seen.add(str(encoded))
            
        for value in adictionary.values():
            result.append(value)
            
        return result

        


