#include <iostream>

class Person {
    public:
        void add_name(int a)
        {
            a = 1;
        }
};


class Room {
public:
    void add_person(Person person)
    {
        // do stuff
    }

private:
    Person* people_in_room;
};


template <class T, int N> class Bag {
};


int main()
{
top:
    Person* p = new Person();
    Bag<Person, 42> bagofpersons;
    p->add_name(2);
    int num = 5;
    num = 2;
    num++;
    num += 1;
    num *= 1;
    num <<= 1;
    num != 1;

    if(num == 1) {
        return 2;
    } else {

    }

    for (size_t i = 0; i < 5; i++)
    {
        /* code */
    }

    while (num == !true)
    {
        /* 
        code
        */
    }
    
    goto top;

    try {
        num = 1;
        throw(num);
    }
    catch(int num) {
    }

    switch (num)
    {
    case 1:
        break;
    
    case 2:
        break;

    default:
        break;
    }

    return 0;
}

// This is a comment
int second_main(int a, int b)
{
    std::cout << "Hello" << std::endl;
    main();
    int *p = new int;
    delete p;
}