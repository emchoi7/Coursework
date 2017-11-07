//Board.cpp
//Maru Choi

#include "Board.h"
#include <iostream>
using namespace std;

Board::Board(){
	for(int i = 0; i <= 8; i++ ) //iterate through the rows
	{
		for(int j = 0; j <= 8; j++ ) //iterate through the cols
		{
			cells[i][j].value = 0; //initiate the array by filling in 0's

			for(int n = 0; n <= 8; n++)
			{
				cells[i][j].pos[n] = 1;
			}
		}
	}
}

Board::Board(const Board &B){
	for(int i = 0; i <= 8; i++ ) //iterate through the rows
	{
		for(int j = 0; j <= 8; j++ ) //iterate through the cols
		{
			cells[i][j].value = B.cells[i][j].value; //initiate the array by filling in 0's
		}
	}
}

Board::~Board(){}

int Board::isEmpty(int x, int y){
	if(cells[x][y].value == 0)
	{	
		return 1;
	}
	else
		return 0;
}

void Board::insert(int x, int y, int n){
	cells[x][y].value = n;
}

int Board::getVal(int x, int y){
	return cells[x][y].value;
}

void Board::getPos(int x, int y){
	for(int i = 0; i <= 8; i++)
		cout << cells[x][y].pos[i] << endl;
}

int Board::isFull(){
	int fill = 0;
	for(int i = 0; i <= 8; i++)
	{
		for(int j = 0; j <= 8; j++)
		{
			if(isEmpty(i,j) != 1)
			{
				fill++;
			}
		}
	}


	if(fill == 81)
		return 1;
	else
		return 0;

}

void Board::display(){
	for(int i = 0; i <= 8; i++)
	{
		for(int j = 0; j <= 8; j++)
		{
			cout << cells[i][j].value << " ";
		}
		cout << endl;
	}
}

void Board::checkPos(int x, int y){
	if(isEmpty(x,y) == 1) //checks only the empty cells
	{
		for(int i = 1; i <= 9; i++) 
		{
			for(int n = 0; n <= 8; n++)
			{
				if(cells[n][y].value == i) //checks if any of the cells within the current row have a particular value
					cells[x][y].pos[i - 1] = 0; //makes sure possibility of getting that same value is 0

				if(cells[x][n].value == i) //checks if any of the cells within the column has a particular value
					cells[x][y].pos[i - 1] = 0;
			}

			//check grid
			if( x >= 0 && x <= 2 ) //Checking first 3 rows
			{
				for(int k = 0; k <= 2; k++) //iterate through the rows
				{
						if( y >= 0 && y <= 2 ) //Checking first 3 cols
						{
							for(int j = 0; j <= 2; j++) //iterate through the cols
							{
								if(cells[k][j].value == i) //checks if any of the cells within the grid has a certain value
									cells[x][y].pos[i - 1] = 0; //makes sure the possibility of getting that particular value is 0
							}
						}

						else if( y >= 3 && y <= 5 ) //Checking second 3 cols
						{
							for(int j = 3; j <= 5; j++) //iterate through the cols
							{
								if(cells[k][j].value == i)
									cells[x][y].pos[i - 1] = 0;
							}
						}

						else if( y >= 6 && y <= 8 ) //Checking third 3 cols
						{
							for(int j = 6; j <= 8; j++) //iterate through the cols
							{
								if(cells[k][j].value == i)
									cells[x][y].pos[i - 1] = 0;
							}
						}
				}
			}

			else if( x >= 3 && x <= 5 ) //Checking second 3 rows
			{
				for(int k = 3; k <= 5; k++)
				{
						if( y >= 0 && y <= 2 ) //Checking first 3 cols
						{
							for(int j = 0; j <= 2; j++)
							{
								if(cells[k][j].value == i)
									cells[x][y].pos[i - 1] = 0;
							}
						}
						else if( y >= 3 && y <= 5 ) //Checking second 3 cols
						{
							for(int j = 3; j <= 5; j++)
							{
								if(cells[k][j].value == i)
									cells[x][y].pos[i - 1] = 0;
							}
						}
						else if( y >= 6 && y <= 8 ) //Checking third 3 cols
						{
							for(int j = 6; j <= 8; j++)
							{
								if(cells[k][j].value == i)
									cells[x][y].pos[i - 1] = 0;
							}
						}
				}
			}

			else if( x >= 6 && x <= 8 ) //Checking third 3 rows
			{
				for(int k = 6; k <= 8; k++) //iterate through the rows
				{
						if( y >= 0 && y <= 2 ) //Checking first 3 cols
						{
							for(int j = 0; j <= 2; j++) //iterate through the cols
							{
								if(cells[k][j].value == i) //checks if any of the cells within the grid has a certain value
									cells[x][y].pos[i - 1] = 0; //makes sure the possibility of getting that particular value is 0
							}
						}

						else if( y >= 3 && y <= 5 ) //Checking second 3 cols
						{
							for(int j = 3; j <= 5; j++) //iterate through the cols
							{
								if(cells[k][j].value == i)
									cells[x][y].pos[i - 1] = 0;
							}
						}
						else if( x >= 6 && x <= 8 ) //Checking third 3 cols
						{
							for(int j = 6; j <= 8; j++) //iterate through the cols
							{
								if(cells[k][j].value == i)
									cells[x][y].pos[i - 1] = 0;
							}
						}
				}
			}

		}
	}
}

void Board::single(int n, int m){
	if(isEmpty(n,m) == 1)//check only the empty cells
	{
		int count = 0; //temporary variable that keeps track of how many possibilities this cell has
		for(int i = 0; i <= 8; i++)
		{
			if(cells[n][m].pos[i] == 1)
				count++;
		}

		if(count == 1)
		{
			for(int i = 0; i <= 8; i++)
			{
				if(cells[n][m].pos[i] == 1)
					cells[n][m].value = i+1;
			}
		}
	}
}

void Board::singletonRow(int n){
	int count[9] = {0}; //temporary array of values to keep track of how many of each value is on the pos array of each row

	for(int i = 0; i <= 8; i++) //iterate through each value 
	{
		for(int j = 0; j <= 8; j++) //iterate through cols
		{
			if(isEmpty(n, j) == 1) //check only the empty cells
			{
				if(cells[n][j].pos[i] == 1) //increase count of certain value if the cell's possibility array has that value
					count[i] += 1;
			}
		}
	}

	for(int i = 0; i <= 8; i++) //iterate through each value
	{
		if(count[i] == 1) //if only one cell has a particular value
		{
			for(int j = 0; j <= 8; j++) //iterate through each col to find which cell has the possibility of this value
			{
				if(isEmpty(n,j) == 1)//check only the empty cells
				{
					if(cells[n][j].pos[i] == 1)
						cells[n][j].value = i+1; //set the value of the cell to the value
				}

			}
		}

	}

}

void Board::singletonCol(int n){
	int count[9] = {0}; //temporary array of values to keep track of how many of each value is on the pos array of each row

	for(int i = 0; i <= 8; i++) //iterate through each value 
	{
		for(int j = 0; j <= 8; j++) //iterate through cols
		{
			if(isEmpty(j, n) == 1) //check only the empty cells
			{
				if(cells[j][n].pos[i] == 1) //increase count of certain value if the cell's possibility array has that value
					count[i] += 1;
			}
		}
	}

	for(int i = 0; i <= 8; i++) //iterate through each value
	{
		if(count[i] == 1) //if only one cell has a particular value
		{
			for(int j = 0; j <= 8; j++) //iterate through each col to find which cell has the possibility of this value
			{
				if(isEmpty(j,n) == 1)//check only the empty cells
				{
					if(cells[j][n].pos[i] == 1)
						cells[j][n].value = i+1; //set the value of the cell to the value
				}

			}
		}

	}

}


