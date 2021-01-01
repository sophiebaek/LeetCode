class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        
        >>> Input: address = "1.1.1.1"
        Output: "1[.]1[.]1[.]1"
        
        >>> Input: address = "255.100.50.0"
        Output: "255[.]100[.]50[.]0"
        """
        
        defanged_ip = ""
        
        for i in range(len(address)):
            if address[i] == ".":
                defanged_ip += "[.]"
            else:
                defanged_ip += address[i]
        return defanged_ip
