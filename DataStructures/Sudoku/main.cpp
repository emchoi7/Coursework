//main.cpp
//Maru Choi
//Uses Board class to implement a sudoku solver
#include <iostream>
#include <fstream>
#include <string>
#include "Board.h"
using namespace std;

void possibility(Board &);
void single(Board &);
void singletonRow(Board &);
void singletonCol(Board &);

int main(int argc, char *argv[]){

	Board sudoku; //initializes a Board object

	//read in from a text file
	if(argc > 1) //reads in text file
	{
		char Object;
		fstream ifs(argv[1]);
		if(!ifs)
		{
			cout << "Error: Bad File Name" << endl;
			return 1;
		}

		ifs.get(Object); //first strObject
		int i = 0; //counter variable for row
		int j = 0; //counter variable for col

		while(!ifs.eof())
		{
			if(!isspace(Object))
			{
				if(j > 8) //resets col number j back to 0 and increases the row number i
				{
					j = 0;
					i++;
				}
				int temp = Object - '0'; //temporary variable that stores the int version of the character
				sudoku.insert(i, j, temp);
				j++;
			}
			ifs.get(Object);
		}

		sudoku.display();
		cout << endl;
	}

	//Solve sudoku
	int full = sudoku.isFull();
	possibility(sudoku);
	while(full != 1)
	{
		single(sudoku);
		possibility(sudoku);
		singletonRow(sudoku);
		possibility(sudoku);
		single(sudoku);
		possibility(sudoku);
		singletonCol(sudoku);
		possibility(sudoku);

		full = sudoku.isFull();
	}

	sudoku.display();

	return 0;
}


void possibility(Board &sudoku){
	for(int i = 0; i <= 8; i++) //iterate through the rows
	{
		for(int j = 0; j <= 8; j++) //iterate through the cols
		{
			sudoku.checkPos(i, j); //check the possibilities of each empty cell
		}
	}
}

void single(Board &sudoku){
	for(int i = 0; i <= 8; i++) //iterate through the rows
	{
		for(int j = 0; j <= 8; j++) //iterate through the cols
		{
			sudoku.single(i, j); //check the possibilities of each empty cell
		}
	}
}

void singletonRow(Board &sudoku){
	for(int i = 0; i <= 8; i++) //iterate through the rows
	{
		sudoku.singletonRow(i); //finds singleton of each row
	}
	
}

void singletonCol(Board &sudoku){
	for(int i = 0; i <= 8; i++) //iterate through the rows
	{
		sudoku.singletonCol(i); //finds singleton of each row
	}
	
}

















