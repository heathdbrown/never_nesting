# Never Nesting

From https://www.youtube.com/watch?v=CFRhGnuXG-4

## Original

```
int calculate(int bottom, int top)
{
    if (top > bottom)
    {
        int sum = 0;

        for (int number = bottom; number <= top; number ++>)
        {
            if (number % 2 == 0)
            {
                sum += number;
            }
        }
        return sum;
    }
    else
    {
        return 0;
    }
}
```

## Extraction
- pull out parts that can to functions

## invert
- move the negative results out of 'else' conditions