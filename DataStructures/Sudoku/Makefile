CMP = g++ -std=c++11
CLASS1 = Board
MAIN = main
EXEC = sudoku

$(EXEC): $(CLASS1).o $(MAIN).o
	$(CMP) $(CLASS1).o $(MAIN).o -o $(EXEC)

$(CLASS1).o: $(CLASS1).cpp $(CLASS1).h
	$(CMP) -c $(CLASS1).cpp -o $(CLASS1).o

$(MAIN).o: $(MAIN).cpp $(CLASS1).h
	$(CMP) -c $(MAIN).cpp -o $(MAIN).o

clean:
	rm *.o
	rm $(EXEC)