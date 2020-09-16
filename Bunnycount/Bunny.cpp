#include "Bunny.h"
#include <Windows.h>
#include <iostream>
#include <fstream>
#include <string>


Bunny::Bunny()
{
	int bunnySex = randomNumber(0, 1);
	int bunnyColor = randomNumber(0, 4);
	int VampireBunny = randomNumber(1, 100);

	if (bunnySex == 0)
		this->bunnySex = MALE;
	else
		this->bunnySex = FEMALE;
	if (bunnyColor == 0)
		this->bunnyColor = WHITE;
	if (bunnyColor == 1)
		this->bunnyColor = BROWN;
	if (bunnyColor == 2)
		this->bunnyColor = BLACK;
	if (bunnyColor == 3)
		this->bunnyColor = SPOTTED;
	if (VampireBunny == 10)
		this->bunnyRace = VAMPIRE;
	if (VampireBunny == 20)
		this->bunnyRace = VAMPIRE;
	else
		this->bunnyRace = NORMAL;
	this->age = 1;
	this->bunnyName = randomBunnyName();
}
std::string Bunny::randomBunnyName()
{
	std::ifstream in_file{ "C:/Users/tomten/Desktop/Bunnycount/Bunnycount/names.txt" };
	int randomRow = randomNumber(1, 80);
	int currentRow{};
	std::string line;

	while (getline(in_file, line)) {
		++currentRow;
		if (currentRow == randomRow) {
			in_file.close();
			return line;
		}
	}
}
Bunny::~Bunny()
{
}
