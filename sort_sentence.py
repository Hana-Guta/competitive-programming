class Solution(object):
    def sortSentence(self, s):
        output = ""
        se = s.split()
        for i in range(1, 10):
            for j in se:
                if j[-1] == str(i):
                    output += " " + j[:-1]
        return output.strip()





       


      
    



       
