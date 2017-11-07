//Board.h
//Maru Choi
#ifndef BOARD_H
#define BOARD_H



class Board {

public:

	struct Cell{
	int value; //stores value of cell
	int pos[9]; //stores possible numbers that the cell can be
	};

	Board(); //constructor
	Board(const Board &); // copy constructor 
	~Board(); //destructor
	int isEmpty(int, int); //checks if cell is 0 (empty); if it is not empty, then it clears out pos vector
	void insert(int, int, int); //inserts a value in a specified cell
	int getVal(int, int); //gets the value of the specified cell
	void getPos(int, int); //displays the possibilities of a cell
	int isFull(); //checks if board is full
	void display();
	void checkPos(int, int); //checks the particular row, column, and grid 
	void single(int, int); //checks if there is a cell that has only one possibility
	void singletonRow(int); //uses the pos vector to figure out the best value to put in each cell based on pos array of the row
	void singletonCol(int); //uses the pos vector to figure out the best value to put in each cell based on pos array of the col


private:
	Cell cells[9][9]; //2D array of Cell to store the value of each cell

};

#endif