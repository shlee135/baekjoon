#if 1
#include <stdio.h>
#include <stdlib.h>
int main(void)
{
	int N, M, i, j, k;
	scanf("%d %d", &N, &M);
	int *pa = (int *)calloc(N, sizeof(int));
	if (pa == NULL) exit(1);

	for (int l = 0; l < M; l++)
	{
		scanf("%d %d %d", &i, &j, &k);
		for (int b = i - 1; b <= j - 1; b++)
		{
			pa[b] = k;
		}
	}
	for (int i = 0; i < N; i++) printf("%d ", pa[i]);

	free(pa);

	return 0;
}
#endif