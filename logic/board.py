class Board:
    def __init__(self):
        self.whitepawn = 0b0000000000000000000000000000000000000000000000001111111100000000
        self.whiterook = 0b0000000000000000000000000000000000000000000000000000000010000001
        self.whiteknight = 0b0000000000000000000000000000000000000000000000000000000001000010
        self.whitebishop = 0b0000000000000000000000000000000000000000000000000000000000100100
        self.whitequeen = 0b0000000000000000000000000000000000000000000000000000000000010000
        self.whiteking = 0b0000000000000000000000000000000000000000000000000000000000001000

        self.blackpawn = 0b0000000011111111000000000000000000000000000000000000000000000000
        self.blackrook = 0b1000000100000000000000000000000000000000000000000000000000000000
        self.blackknight = 0b0100001000000000000000000000000000000000000000000000000000000000
        self.blackbishop = 0b001001000000000000000000000000000000000000000000000000000000000
        self.blackqueen = 0b0001000000000000000000000000000000000000000000000000000000000000
        self.blackking = 0b0000100000000000000000000000000000000000000000000000000000000000

    def printboard(self):
        print(f"white pawns:    {bin(self.whitepawn)}")
        print(f"white rooks:    {bin(self.whiterook)}")
        print(f"white knights:  {bin(self.whiteknight)}")
        print(f"white bishops:  {bin(self.whitebishop)}")
        print(f"white queen:    {bin(self.whitequeen)}")
        print(f"white king:     {bin(self.whiteking)}")
        
        print(f"black pawns:    {bin(self.blackpawn)}")
        print(f"black rooks:    {bin(self.blackrook)}")
        print(f"black knights:  {bin(self.blackknight)}")
        print(f"black bishops:  {bin(self.blackbishop)}")
        print(f"black queen:    {bin(self.blackqueen)}")
        print(f"black king:     {bin(self.blackking)}")
