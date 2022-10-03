
# Linear Search is defined as a sequential search algorithm that starts at one end and goes through each element of a list until the desired element is found.
# Time complexity: O(N)


void linearSearch(int arr[], int n, int search)
{
    int i;
    for (i = 0; i < n; i++)
    {
        if (arr[i] == search)
        {
            printf("Element found at location: %d\n", i + 1);
            break;
        }
    }
    if (i == n)
    {
        printf("Not Found!\n");
    }
}
