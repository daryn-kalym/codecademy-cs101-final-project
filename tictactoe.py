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
game = TTTMap()
game.printMap()
game.player1move([1,1])
game.player2move([1,1])
game.player2move([1,2])