// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Put your code here.

@Index
M=0

@Sum
M=0

(LOOP)
	@R0	//Get first num
	D=M

	@Sum //Add first num and sum together and get new sum
	M=D+M

	@Index //Up Index and assign to D
	M=M+1
	D=M

	@R1
	D=D-M //Subtract the second num from index. If its 0 then all increments are done

	@END
	D;JEQ

	@LOOP
	0;JMP


(END)
@END
0;JMP
