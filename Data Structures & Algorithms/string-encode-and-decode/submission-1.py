class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string=''

        for word in strs:
            word_length=len(word)

            encoded_string+=str(word_length)+'#'+word
        return encoded_string

    def decode(self, s: str) -> List[str]:
        pointer=0
        decoded_string=[]

        while pointer < len(s):
                # Find hash index
            hash_index=s.find('#',pointer)
            #read string length in total

            word_length=int(s[pointer:hash_index])

            #define start and end indices
            start_index=hash_index+1
            end_index=start_index+word_length
            #pull the word via the length + pointer
            decoded_string.append(s[start_index:end_index])

            #readjust poointer to end index which is length+pointer
            pointer=end_index

        return decoded_string



