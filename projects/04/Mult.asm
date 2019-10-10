// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Put your code here.

@Index
M=0

@R0
D=M
@ZERONUM
D;JEQ //If the first number is 0 then go ahead and go to end

@R1
D=M
@ZERONUM
D;JEQ //If the second number is 0 then go ahead and go to end

@R2
M=0

(LOOP)
	@R0	//Get first num
	D=M

	@R2 //Add first num and sum together and get new sum
	M=D+M

	@Index //Up Index and assign to D
	M=M+1
	D=M

	@R1
	D=D-M //Subtract the second num from index. If its 0 then all increments are done

	@END
	D;JGE

	@LOOP
	0;JMP


(ZERONUM)
@R2
M=0
@END
0;JMP

(END)
@END
0;JMP
