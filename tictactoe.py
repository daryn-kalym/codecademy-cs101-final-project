class TTTMap:
    
    def __init__(self) -> None:
        """
        It creates a 3x3 matrix of strings, each string being a space
        """
        self.map = [[" " for i in range(3)] for j in range(3)]
    
    def checkMove(self,coords):
        """
        It checks if the move is valid
        
        :param coords: The coordinates of the move
        :return: a boolean value.
        """
        i,j = coords
        if self.map[i][j] != " ":
            print("You cannot move here!")
            return False
        else:
            return True
    
    def player1move(self,coords):
        """
        The function takes in a coordinate and checks if it's a valid move. If it is, it places an "o"
        on the map at the coordinate
        
        :param coords: a tuple of the coordinates of the move
        """
        if self.checkMove(coords):
            i,j = coords
            self.map[i][j] = "o"
            print("\nPlayer 1 made a move on {}.\nThe Map loks like this:".format(coords))
            self.printMap()
            if self.checkResult():
                print("Player 1 Wins!")
                exit()
            return True
        else:
            return False
    
    def player2move(self,coords):
        """
        The function takes in a coordinate and checks if it's a valid move. If it is, it changes the
        value of the coordinate to "x" and prints the map
        
        :param coords: a tuple of the coordinates of the move
        """
        if self.checkMove(coords):
            i,j = coords
            self.map[i][j] = "x"
            print("\nPlayer 2 made a move on {}.\nThe Map loks like this:".format(coords))
            self.printMap()
            if self.checkResult():
                print("Player 2 Wins!")
                exit()
            return True
        else:
            return False
    
    def printMap(self):
        """
        It prints the map
        """
        for i in self.map:
            print(i)
    
    def checkResult(self):
        for i in self.map:
            if "".join(i)=="ooo" or "".join(i)=="xxx":
                return True
        temp = [[self.map[j][i] for j in range(len(self.map[i]))] for i in range(len(self.map))]
        for i in temp:
            if "".join(i)=="ooo" or "".join(i)=="xxx":
                return True
        temp1 = ""
        temp2 = ""
        for i in range(len(self.map)):
            temp1 += self.map[i][i]
            temp2 += self.map[len(self.map)-1-i][i]
        if temp1 == "ooo" or temp2 == "ooo" or temp1 == "xxx" or temp2 == "xxx":
            return True
        return False

g = TTTMap()
g.player1move([0,0])
g.player2move([0,1])
g.player1move([1,1])
g.player2move([0,2])
g.player1move([2,2])
g.player2move([1,2])
g.player1move([2,0])
g.player2move([2,1])
g.player1move([2,2])