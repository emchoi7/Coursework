#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <ctype.h>
#include <string.h>
// ...................................................................... //
struct machine define_m(char * file); //return machine
struct str_input inputstr(char * file); //return array of input strings
void execution(struct machine M, struct str_input input); //print reject/accept
char * strip(char * string); //strip string of trailing whitespaces
// ...................................................................... //

struct machine
{
	char * name;
	char * start;
	char * accept[10]; //ASSUMPTION: no more than 10 states are accept states
	char * transition[30][3]; //ASSUMPTION: no more than 30 transitions //list of dict {state_p:{char:state_n}}
	int r; //how many rules there are
	int a; //how many accept states there are
};

struct str_input
{
	char * line[BUFSIZ];
	int c; //how many lines there are
};

// ...................................................................... //

//// *****     MAIN     ***** ////
int main(int argc, char *argv[])
{
	struct machine m;
	struct str_input input;
	m = define_m(argv[1]);
	input = inputstr(argv[2]);
	printf("%d\n", m.r);
	execution(m, input);
	return 0;
}
//// ***** End of MAIN ***** ////

// ...................................................................... //

// ***** Read in DFA file ***** //
struct machine define_m(char * file)
{
	FILE *fp;
	fp = fopen(file, "r");
	char *line = malloc(BUFSIZ);
	char *definition[30]; //ASSUMPTION: no more than 30 transitions
	int i = 0;
	if(fp == NULL)
	{
		perror("Error opening DFA file");
		exit(-1);
	}
	while(fgets(line, BUFSIZ, fp))
	{
		if(strlen(line) == 0)
			continue;
		else
		{
			//printf("%d: ", i);
			//printf("%s\n", line);
			definition[i] = strdup(line);
		}
		i++;
	}
	fclose(fp);

	//Define machine
	struct machine M; //initialize machine
	//Line 0: Name - echo
	M.name = strdup(definition[0]);
	printf("Machine: %s\n", M.name);
	//Line 1: Alphabet
	//Line 2: BLANK
	//Line 3: State names
	//Line 4: Start state

	M.start = strdup(definition[4]);
	//printf("%s\n", M.start);

	//Line 5: Accepting states
	int j = 0;
	char *pos = strchr(definition[5],',');

	if(pos!=NULL)//If there are multiple accept states
	{
		//printf("%s\n", definition[5]);
		char *str = strtok(definition[5], ",");
		while(str != NULL)
		{
			M.accept[j] = strdup(str);
			j++;
			str = strtok(NULL, ",");
		}
		M.a = j;
	}
	else //only one accept state
	{
		definition[5]=strip(definition[5]);
		M.accept[j] = strdup(definition[5]);
		M.a = 1;
	}
	//Line 6+: Transition rules 
	//[[q0][a][q2], [q0][a][q1], ...]
	//M.accept[k][l], where k is the rule #
	//each transition is in the format: q0, a, q1
	//q0, l=0
	//a, l=1
	//q1, l=2
	int k;

	for(k=6; k<i; k++) //i holds number of elems in definition[]
	{
		int l = 0;
		char *str2 = strtok(definition[k], ",");
		printf("Rule %d: ", k-6);
		while(str2 != NULL) //until line k is exhausted
		{
			str2 = strip(str2);
			M.transition[k-6][l] = strdup(str2);
			printf("%s ", M.transition[k-6][l]);
			l++;
			str2 = strtok(NULL, ",");
			
		}
		printf("\n");
	}
	M.r = k-6;

	return M;
}


// ***** Read in input string file ***** //
struct str_input inputstr(char * file)
{
	struct str_input str;
	FILE *fp;
	fp = fopen(file, "r");
	char *line = malloc(BUFSIZ);
	int i = 0;
	if(fp == NULL)
	{
		perror("Error opening DFA file");
		exit(-1);
	}
	while(fgets(line, BUFSIZ, fp))
	{
		if(strlen(line) == 0)
			continue;
		else
		{
			//printf("%d: ", i);
			//printf("%s\n", line);
			line = strip(line);
			str.line[i] = strdup(line);
		}
		i++;
	}
	fclose(fp);
	str.c = i;
	return str;
}


// ***** Run input string on machine ***** //
void execution(struct machine M, struct str_input input)
{
	int i;
	int j;
	int k;
	char *currstate;
	for(i=0; i<input.c; i++)//for each line of input
	{
		
		//char * endChar;
		M.start = strip(M.start);
		currstate = strdup(M.start); //reset current state
		printf("%s\n", currstate);
		char * line = strdup(input.line[i]);
		printf("%d: %s\n", i, input.line[i]);

		for(k=0; k<strlen(line); k++) //for each char in line of input
		{
			char * charac = malloc(sizeof(char)+1);
			sprintf(charac, "%c", line[k]);
			//printf("Charac: %s\n", charac);
			int moved = 0; //indicates if moved onto next state

			for(j=0; j<M.r; j++)//for each transition rule
			{
				//printf("Checking...\n");
				//printf("c%sc ", currstate);
				//printf("c%sc\n", M.transition[j][0]);

				if(strcmp(currstate, M.transition[j][0])==0) //check whether currstate and transition's initial state
				{
					//printf("t%st ", charac);
					//printf("t%st\n", M.transition[j][1]);

					if(strcmp(charac, M.transition[j][1])==0) //check if the input char is same as transition's input symbol
					{
						currstate = strdup(M.transition[j][2]); //move onto next state
						//printf("moved states: %s\n", currstate);
						moved = 1;
					}
				}

				if(moved == 1)
					continue;
			}
			if(moved == 0) //There was no corresponding rule! Move to TRAP
			{
				currstate = strdup("TRAP");
			}
		}

		//printf("%s\n", currstate);
		//Check for trap state
		if(strcmp(currstate, "TRAP") == 0)
		{
			printf("String Rejected\n");
		}

		else
		{
			int accept = 0;
			int l;
			for(l=0; l < M.a; l++)
			{
				if(strcmp(currstate, M.accept[l]) == 0)
				{
					printf("String Accepted\n");
					accept = 1;
					continue; //found an accept state, so kick out of loop
				}
			}
			if(accept != 1)
				printf("String Rejected\n");
		}
		
		
		//Compare currstate to the accept states
		//for //for each accept state
			//if currstate == an accept state
			//then print "Accept"
			//if after going through all, is not accept, then print reject
	}
	//while(input)
		//take next line, while(line)
			//var to keep track of curr state = start state
			//transition[currstate] --> dict of string:nextstate
			//transition[currstate][inputchar] --> currstate = nextstate
			//if transition[currstate][inputchar] != exist, then TRAP
			//check if currstate == TRAP; if so, return reject
			//if not return accept

}

// ***** Strip ***** //
char * strip(char * string)
{
	assert(string);
	char *pos;

	while(isspace(*string))
	{
		string++;
	}

	if((pos=strchr(string, '\n')) != NULL)
		*pos = '\0';
	return string;
}
