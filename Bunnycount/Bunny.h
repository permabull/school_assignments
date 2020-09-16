#pragma once
#include "enums.h"
#include <vector>
#include "randomNumber.h"

class Bunny
{
public:
	std::string randomBunnyName();
	Bunny();
	~Bunny();
	std::string getName() { return this->bunnyName; }
	int getAge() { return this->age; }
	int getColor() { return this->bunnyColor; }
	int getSex() { return this->bunnySex; }
	int getVampireStatus() { return this->bunnyRace; }
	void setName(std::string bunnyName) { this->bunnyName = bunnyName; }
	void increaseAgeByOne() { this->age++; }
	void setBunnycolor(int bunnyColor) { this->bunnyColor = bunnyColor; }
	void setVampireStatus(int vampireStatus) { this->bunnyRace = vampireStatus; }
	//int randomNumber(int min, int max);

private:
	int bunnyRace{};
	int age{};
	int bunnySex{};
	int bunnyColor{};
	std::string bunnyName{};
	std::vector<std::string> bunnyNames{ "Skutte", "Hoppe","Charlie","Stampe","Lilleskutt","Lillan","Lillen" };
};