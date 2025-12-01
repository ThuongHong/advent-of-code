#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main()
{
    ifstream fi("day1.txt");
    string line;

    int cur = 50;
    int password = 0;
    while (fi >> line)
    {
        int rotated = 0; // 0 ~ left, 1 ~ right
        if (line[0] == 'R')
            rotated = 1;

        line[0] = '0';
        int dist = stoi(line);

        // password += dist / 100;
        dist %= 100;
        if (!rotated)
        {
            if (cur - dist >= 0)
                cur -= dist;
            else if (cur != 0)
            {
                cur = 100 - (dist - cur);
                // if (cur != 0)
                // {
                //     // cout << "here";
                //     password += 1;
                // }
            }
            else
                cur = 100 - dist;
        }
        else
        {
            if (dist + cur <= 99)
                cur += dist;
            else
            {
                // cout << "here";
                cur = cur + dist - 100;
                // password += 1 * (cur != 0);
            }
        }
        if (cur == 0)
            password += 1;

        cout << cur << "\n";
    }
    cout << "Password: " << password;

    fi.close();
}