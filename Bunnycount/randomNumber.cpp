#include "randomNumber.h"
int randomNumber(int min, int max)
{
	std::random_device r;
	std::seed_seq seed{ r(), r(), r(), r(), r(), r(), r(), r() };
	std::mt19937 eng{ seed };
	std::uniform_int_distribution<> dist(min, max);
	return dist(eng);
}