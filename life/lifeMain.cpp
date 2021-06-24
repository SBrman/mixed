# include <iostream>
# include <vector>
# include <windows.h>

using namespace std;


// Constants
const int HEIGHT = 50;
const int WIDTH = 100;

class LifeBoard{
public:
    int rows;
    int columns;
    vector<vector<int>> board;

    LifeBoard(int height, int width){
        this->rows = height;
        this->columns = width;

        for (int row = 0; row < this -> rows; row++){
            vector<int> fullRow;
            for (int col = 0; col < this -> columns; col++){
                int randomBinaryNumber = (int) rand() % (1 + 1);
                fullRow.push_back(randomBinaryNumber);
            }
            this->board.push_back(fullRow);
        }
    }

    void printBoard(){
        for (int row = 0; row < this->rows; row++){
            for (int col = 0; col < this->columns; col++){
                int cellAlive = this->board[row][col];
                switch (cellAlive){
                    case 1: cout << '*' ; break;
                    default: cout << ' ' ;
                }
            }
            cout << endl;
        }
    }

    int getCell(int row, int col){
        return this->board[row][col];
    }

    int getAliveNeighbours(int row, int col){

        int aliveNeighbours = 0;

        int rowRange[] = {row - 1, row, row + 1};
        int colRange[] = {col - 1, col, col + 1};

        if ((row > 0 && row < this->rows) && (col > 0 && col < this->columns)){
            for (int r: rowRange){
                for (int c: colRange){
                    if (r == -1 || r == this->rows || c == -1 || c == this->columns){continue;}
                    else if (this->board[r][c] == 1){aliveNeighbours++;}
                }
            }
        }

        return aliveNeighbours;
    }

    void passTime(){

        vector<vector<int>> copyTable = this->board;

        for (int row = 0; row < this->rows; row++){
            for (int col = 0; col < this->columns; col++){

                int alive = this->getAliveNeighbours(row, col);

                if (this->board[row][col]){
                    alive--;
                    if (alive < 2 || alive >3){
                        copyTable[row][col] = 0;
                    }
                }
                else{
                    if (alive == 3){
                        copyTable[row][col] = 1;
                    }
                }
            }
        }

        this->board = copyTable;
    }


    ~LifeBoard();
};


int main(){
    LifeBoard *table = new LifeBoard(HEIGHT, WIDTH);

    for (int i=0; i < 100; i++){
        table->printBoard();
        Sleep(100);
        system("cls");
        table->passTime();
    }

    system("pause");
    return 0;
}
