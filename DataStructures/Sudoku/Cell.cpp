//Cell.cpp
//Maru Choi

#include "Cell.h"

Cell::Cell(int n) {
	value = n;
}

Cell::Cell(const Cell &c) {
	value = c.value;
}

Cell::~Cell() {}

int Cell::isEmpty() {
	if(value == 0)
		return 0;
	else
		return 1;
}

int Cell::getVal() {
	return value;
}
