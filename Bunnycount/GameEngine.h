#pragma once
#include <iostream>
#include <sstream>
#include <time.h>
#include "Bunny.h"
#include <vector>
#include "randomNumber.h"

class GameEngine : public Bunny
{
public:
	void initializeGame();
	void newTurn();
	void newBunnyBabies();
	void killOldBunnys();
	void printAllBunnys();
	void addNewBunny();
	bool GameOver();
	int bunnyCount() { int bunnyCount{}; return bunnyCount = allBunnys.size(); }
	void killHalfOfThePopulaton();
	void radioActiveBunnys();

private:
	std::vector<Bunny*>allBunnys{};
};

