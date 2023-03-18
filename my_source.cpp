bool foo()
{
    return true;
}

void bar()
{
    foo();
    for (int i = 0; i < 10; ++i)
        foo();
}

int main()
{
    for (int i = 0; i < 10; ++i)
        foo();
    bar();
    if (foo())
        bar();
}
if(a > c) {
    break;
    return a + b;
}
if (a + b)
 {
    d = c * (a + b);
}
class A {};