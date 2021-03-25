import PIL
import math
def checkmovevalid(move):
    # TODO validate if a move is formatted correctly. Does NOT check if a move is possible.
    # Moves must be provided in algebraic notation.
    
    # Valid numbers and letters for locations.
    LCLetters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    Numbers = ['1', '2', '3', '4', '5', '6', '7', '8']
    
    # Pawn moves
    # Pawn advancement.
    if(len(move) == 2 and move[0] in LCLetters and move[1] in Numbers):
        return True
    # Pawn promotion.
    elif(len(move)==4 and move[2]=='=' and move[3] in ['Q','B','R','N']):
            return True
    # Pawn Captures
    elif(len(move) == 4 and move[1]=='x' and move[2] in LCLetters and move[3] in Numbers):
        return True
    # Pawn Capture and Promotion
    elif(len(move) == 6 and move[1]=='x' and move[2] in LCLetters and move[3] in Numbers and move[4]=='=' and move[5] in ['Q','B','R','N']):
        return True
    
    # Castling
    if(move[0] == '0'):
        if(move == "0-0" or move == "0-0-0"):
            return True
        else:
            return False
    
    
    # King or Queen moves.
    if(move[0] in ['Q', 'K']):
        if(len(move) == 4 and move[1]=='x' and move[2] in LCLetters and move[3] in Numbers):
            return True
        elif(len(move)==3 and move[1] in LCLetters and move[2] in Numbers):
            return True
        else:
            return False
    
    
    # Rook, Bishop, or Knight moves separated out due to multiple potential originating locations.
    if(move[0] in ['R', 'B', 'N']):
        if(len(move) == 4 and move[1]=='x' and move[2] in LCLetters and move[3] in Numbers):
            return True
        elif(len(move) == 3 and move[1] in LCLetters and move[2] in Numbers):
            return True
        elif(move[1] in LCLetters or move[1] in Numbers):
            if(len(move) == 5 and move[2]=='x' and move[3] in LCLetters and move[4] in Numbers):
                return True
            else:
                return False
        else:
            return False
    
    # Generic invalid return.
    return False

def checkmovelegal(move):
    print('borked')
    # TODO check if a move is legal.
    # Unfinished lmao.
    
def executemove(move, chessboard):
    # TODO alter a given chessboard based on a provided move.
    return
    
def renderboard (chessboard):
    # TODO: Create a png of a chessboard from an array in the format defined below.
    from PIL import Image
    
    # Importing / Creating Images
    # The base image on which everything else is built.
    builder = Image.new('RGB', (1000,1000))
    # Board + Pieces
    board = Image.open("Chessboard.png")
    wp = Image.open("WP.png")
    bp = Image.open("BP.png")
    wk = Image.open("WK.png")
    bk = Image.open("BK.png")
    wq = Image.open("WQ.png")
    bq = Image.open("BQ.png")
    wr = Image.open("WR.png")
    br = Image.open("BR.png")
    wn = Image.open("WN.png")
    bn = Image.open("BN.png")
    wb = Image.open("WB.png")
    bb = Image.open("BB.png")
    
    # Adding the base board to the builder image.
    builder.paste(board)
    
    # Dictionary because python doesn't have switch statements :(
    # Serves to map different pieces stored in chessboard to their respective images for the for loop below.
    fakeswitch = {
        "wp": wp,
        "bp": bp,
        "wk": wk,
        "bk": bk,
        "wq": wq,
        "bq": bq,
        "wr": wr,
        "br": br,
        "wn": wn,
        "bn": bn,
        "wb": wb,
        "bb": bb
    }
    
    # Iterate through the list of squares, pasting the appropriate piece on the square. Quick maths.
    for i, piece in enumerate(chessboard):
        # Skipping null strings which represent empty squares.
        if(piece==""):
            pass
        else:
            # This one gets a little complicated.
            # First argument is the image to be pasted, which is fetched via the dictionary defined above.
            # Second argument is the left, upper, right, and lower pixel coordinates. The only weird thing is the lower coordinate which needs a little bump up because math.ceil rounds 0 to 0.
            # Third argument tells PIL to use the transparency on the image as its own mask when pasting it onto the board.
            builder.paste(fakeswitch.get(piece), ((125*(i%8)),(125*math.floor(i/8)),(125*(1+(i%8))),int((125*(math.ceil(0.01 + i/8))))), mask = fakeswitch.get(piece))
    # Saving the final image as a PNG
    builder.save("test", format="PNG")
    return

# Array with each position representing one square on the chessboard.
# Snakes from left to right going from A to H and from top to bottom from 8 to 1.
# Pieces are designated with w / b indicating white or black and then a letter representing the piece.
chessboard = [ 
"br", "bn", "bb", "bq", "bk", "bb", "bn", "br",
"bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp", 
"", "", "", "", "", "", "", "", 
"", "", "", "", "", "", "", "", 
"", "", "", "", "", "", "", "", 
"", "", "", "", "", "", "", "", 
"wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp",
"wr", "wn", "wb", "wq", "wk", "wb", "wn", "wr",
]


# Tracks whether castling is possible for white and black, kingside and queenside (in that order).
castling = [True, True, True, True]

# Tracks whether the game has ended, whether through a resignation, an accepted draw, or a checkmate.
game = True
# Tracks whether the entered move is impossible.
impossiblemove = True

# Taking move inputs.
renderboard(chessboard)
while(game):
    while(impossiblemove):
        move = input("Enter a move: ")
        if(checkmovevalid(move)):
            print('valid')
        else:
            print('invalid')
    

    
