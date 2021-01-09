class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        
        >>> Input: command = "G()(al)"
        Output: "Goal"
        
        >>> Input: command = "G()()()()(al)"
        Output: "Gooooal"
        
        >>> Input: command = "(al)G(al)()()G"
        Output: "alGalooG"
        """

        interpretation = ""
        
        for i in range(len(command)):
            if command[i] == "G":
                interpretation += "G"
            elif command[i] == "(" and command[i+1] == ")":
                interpretation += "o"
                i += 2
            elif command[i] == "(" and command[i+1] == "a":
                interpretation += "al"
                i += 4
        return interpretation
