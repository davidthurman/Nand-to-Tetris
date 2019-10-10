// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.

(READKBD)
	@KBD
	D=M //GET INPUT OF KEYBOARD

	@BLACKSCREEN  
	D;JGT  //IF KEYBOARD IS PRESSED BLACKEN SCREEN

	@WHITENSCREEN
	D;JEQ

	@READKBD
	0;JMP


(BLACKSCREEN)

@SCREEN
D=A
M=-1

@Index
M=D

(BLACKLINE)  //Run line by line blackening the screen
@Index
D=M  //Keep track of which pixel you are on


A=D+1
M=-1  //Blacken the next line

@Index
D=M
@24574
D=A-D //Check if all pixels are blackened

@READKBD
D;JEQ //If so return to start

@Index
D=M
M=D+1

@BLACKLINE
0;JMP 

//END OF BLACKEN

(WHITENSCREEN)

@SCREEN
D=A
M=0

@Index
M=D

(WHITELINE)  //Run line by line whitening the screen
@Index
D=M  //Keep track of which pixel you are on


A=D+1
M=0  //Whiten the next line

@Index
D=M
@24574
D=A-D //Check if all pixels are whitened

@READKBD
D;JEQ //If so return to start

@Index
D=M
M=D+1

@WHITELINE
0;JMP 

@READKBD
0;JMP