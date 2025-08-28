#if 1
#include <stdio.h>
#include <stdlib.h>
void swap(int *pa, int i, int j)
{
	int temp;
	temp = pa[i - 1];
	pa[i - 1] = pa[j - 1];
	pa[j - 1] = temp;
}

int main(void)
{
	int N, M, i, j;
	scanf("%d %d", &N, &M);
	int *pa = (int *)malloc(sizeof(int) * N);
	if (pa == NULL) exit(1);
	for (int a = 0; a < N; a++) pa[a] = a + 1;
	for (int b = 0; b < M; b++)
	{
		scanf("%d %d", &i, &j);
		swap(pa, i, j);
	}
	for (int d = 0; d < N; d++) printf("%d ", pa[d]);

	free(pa);
	return 0;
}
#endif