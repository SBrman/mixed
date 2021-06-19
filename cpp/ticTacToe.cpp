#include<iostream>
using namespace std;

void tool_selection(char &p_1, char &p_2);
void table(char b[3][3]);
void inputs(int input, char p ,char b[3][3]);
int restriction(int input, int a[8],int x,int &take_input_again);
void check(char b[3][3],char p_1,char p_2,int  &result);

int main()
{
start:
    int input, a[8]={0}, stop=0, result=0, take_input_again=false;
    char p_1, p_2, p, play_again;
    char b[3][3]={'_', '_', '_', '_', '_', '_', '_', '_', '_'};
                                //declaration

    tool_selection(p_1, p_2);
    cout  <<"\n  _    _    _\n\n  _    _    _\n\n  _    _    _\n\n\n";

    for(int x=1; x<=9; x++)
    {
    lineA:
        if(x%2!=0)
        {
            cout<<"Player 1 input(any number within 1-9)"<<endl;
            p=p_1;
        }
        else if(x%2==0)
        {
            cout<<"Player 2 input(any number within 1-9)"<<endl;
            p=p_2;
        }

        cin>>input;
        restriction(input, a, x, take_input_again);
        if(take_input_again==true)
        {
            take_input_again=false;
            goto lineA;
        }
        inputs(input, p, b);
        table(b);
        if(x>4)
            {
                check(b ,p_1 ,p_2 ,result);
                if(result==1 || result==2) goto line2;
            }
        a[x]=input;                                                  //storing input.
    }

    table(b);
    line2:
        switch(result)
        {
            case 1:cout<<"Player 1 who played with "<<p_1<<" wins"<<endl;  break;
            case 2:cout<<"Player 2 who played with "<<p_2<<" wins"<<endl;  break;
            default:cout<<"DRAW\a\n";
        }

    cout<<"Do you want to play again ?\nPress y for yes and n for no :";
    cin>>play_again;
    if(play_again=='y'){goto start;};

    return 0;
}



void tool_selection(char &p_1, char &p_2)
{
    //char p_1,p_2;
start:
    cout<<"Player 1 enter O or X"<<endl;
    cin>>p_1;
    if(p_1=='O'||p_1=='o'||p_1=='0'){p_1='O';p_2='X';}                       //O looks better in output
    else if(p_1=='X'||p_1=='x') {p_2='O';}
    else {goto start;};                                                      //choosing O or X

}

void table(char b[3][3])
{
    for(int row=0;row<3;row++)
    {
        for(int col=0;col<3;col++)
        {
            cout<<"  "<<b[row][col]<<"   ";
        }
        cout<<endl<<endl;
    }
}

void inputs(int input,char p ,char b[3][3])
{
    switch(input)
    {
        case 1:    b[2][0]=p        ;break;
        case 2:    b[2][1]=p        ;break;
        case 3:    b[2][2]=p        ;break;
        case 4:    b[1][0]=p        ;break;
        case 5:    b[1][1]=p        ;break;
        case 6:    b[1][2]=p        ;break;
        case 7:    b[0][0]=p        ;break;
        case 8:    b[0][1]=p        ;break;
        case 9:    b[0][2]=p        ;break;
    }
}

int restriction(int input,int a[8],int x,int &take_input_again)
{
    for(int n=0;n<x;n++)
        {
            if(input==a[n] || input>9 || input<0)
                {
                    cout<<"Enter only number(1-9) that is not previously entered o";   take_input_again=true;
                }
        }
}

void check(char b[3][3], char p_1, char p_2, int &result)
{
    int s;
    //diagonal
    if(b[2][0]==b[1][1] && b[1][1]==b[0][2])
    {
        result=(b[2][0]==p_1? 1:2);
    }
    else if(b[2][2]==b[1][1] && b[1][1]==b[0][0])
    {
        result=(b[2][2]==p_1? 1:2);
    }

    for(s =0 ;s<3 ;s++ )
    {
        //horizontal
        if(b[s][0]==b[s][1] && b[s][1]==b[s][2])
        {
            if(b[s][0]==p_1)    result=1;
            else if(b[s][0]==p_2)   result=2;
        }
        //vertical
        else if (b[2][s]==b[1][s] && b[1][s]==b[0][s])
        {
            if(b[2][s]==p_1)    result=1;
            else if(b[2][s]==p_2)   result=2;
        }
    }
                                                                                         //winning conditions will be checked after the 5th turn
}
