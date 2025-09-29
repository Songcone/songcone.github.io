#include <iostream>
#include <bits/stdc++.h>
#include <unistd.h>
void CLEAR()
{
	system("cls");
}
using namespace std;
//本程序在猿编程代码实验室有点卡，建议在专业编译器上运行（如：Dev-C++、VSCode等）
string m[32][32] = {};
int x = 11;
int y = 11;
int score;
int hp = 3;
bool flag = 0;
int main()
{
    srand(time(0));
    int a = rand() % 30 + 1;
    int b = rand() % 30 + 1;
    int mx = rand() % 30 + 1;
    int my = rand() % 30 + 1;
    int mx1 = rand() % 30 + 1;
    int my1 = rand() % 30 + 1;
    int bx = rand() % 30 + 1;
    int by = rand() % 30 + 1;
    while(true)
    {
        for(int i = 0; i <= 31; i++)
        {
            for(int j = 0; j <= 31; j++)
            {
                m[i][j] = "   ";
            }
        }
        m[a][b] = "?? ";
        m[bx][by] = "?? ";
        m[y][x] = "?? ";
        m[mx][my] = "?? ";
        m[mx1][my1] = "?? ";
        if (hp == 0)
        {
            flag = 1;
            break;
        }
        if (y == a && x == b)
        {
            a = rand() % 30+1;
            b = rand() % 30+1;
            score++;
            cout << "You eat food\n";
        }
        if (y == mx && x == my)
        {
            hp -= 1;
            mx = rand() % 30 + 1;
            my = rand() % 30 + 1;
            cout << "You and ghose corrected\n";
        }
        if (y == mx1 && x == my1)
        {
            hp -= 1;
            mx = rand() % 30 + 1;
            my = rand() % 30 + 1;
            cout << "You and ghose corrected\n";
        }
        if (y == bx && x == by)
        {
            hp+=1;
            bx = rand() % 30 + 1;
            by = rand() % 30 + 1;
            cout << "You and booldbag corrected\n";
        }
        if (hp > 5){
            hp = 5;
            cout << "Your boold is max\n";
        }
        // Ghost movement with bounds clamping（鬼移动）
        mx += rand() % 3 - 1;  // Now between -1 to +1
        my += rand() % 3 - 1;
        mx = max(1, min(30, mx));
        my = max(1, min(30, my));
        mx1 += rand() % 3 - 1;  // Now between -1 to +1
        my1 += rand() % 3 - 1;
        mx1 = max(1, min(30, mx1));
        my1 = max(1, min(30, my1));
        // Draw borders画边界
        for(int i = 1; i <= 30; i++) m[i][0] = "|";
        for(int i = 0; i <= 30; i++) m[0][i] = "___";
        for(int i = 31; i >= 1; i--) m[i][31] = "|";
        for(int i = 30; i >= 0; i--) m[31][i] = "￣￣￣";
        // Output grid输出“世界”
        for(int i = 0; i <= 31; i++)
        {
            for(int j = 0; j <= 31; j++)
            {
                cout << m[i][j];
            }
            cout << endl;
        }
        // Corrected coordinate display
        char k;
        cout << "x:" << x << ' ' << "y:" << x << " Fy:" << a << " Fx:" << b << " MX:" << mx << " MY:" << my << " MX2:" << mx1 << " MY2:" << my1 << " BX:" << bx <<" BY:" << by << endl << "Game score:" << score << '\n' << "health point:" << hp << endl;
        cin >> k;
        if(k == 'w' && y > 1) y -= 1;
        if(k == 'a' && x > 1) x -= 1;
        if(k == 'd' && x < 30) x += 1;
        if(k == 's' && y < 30) y += 1;
        if(k == 'q') {
            system("clear");
            return 0;
        }
        cout << endl;
        if (score == 20)
        {
            flag = 0;
            break;
        }
        //system("clear");
        CLEAR();
    }
    CLEAR();
    //system("clear");
    //几乎所有的手机系统都是luxin为基础编（除了HarmonyO5.0以上版本或Harmony NEXT版本）的，所以要用system("clear");
    //如果你是Windows版的，那么你只需要把“clear”改成“cls”
    if (flag) cout << "Game over！\n\nYou die!!!\n\nPlay again!";
    else cout << "You win";
    return 0;
}
