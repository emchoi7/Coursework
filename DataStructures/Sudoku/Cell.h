//Cell.h
//Maru Choi

#ifndef CELL_H
#define CELL_H

class Cell {
public:
	Cell(int); //constructor
	Cell(const Cell &); //copy constructor
	~Cell(); //destructor
	int isEmpty(); //checks if the cell is empty; 0 is empty, 1 is filled
	int getVal(); //returns the value the cell holds


private:
	int value; //stores a value
}