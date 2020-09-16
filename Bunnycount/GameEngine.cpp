#include "GameEngine.h"
#include <algorithm>
#include <Windows.h>

void GameEngine::initializeGame()
{
	int startRabbits{ 5 };

	for (int i = 0; i < startRabbits; i++) {
		addNewBunny();
	}
}
void GameEngine::newTurn()
{
	for (int i = 0; i < allBunnys.size(); i++) {
		allBunnys.at(i)->increaseAgeByOne();
	}
}
void GameEngine::newBunnyBabies()
{
	int loop = allBunnys.size();
	bool foundmale{ false };
	for (int i = 0; i < allBunnys.size(); i++) {
		if (allBunnys.at(i)->getSex() == MALE && allBunnys.at(i)->getAge() >= 2 && allBunnys.at(i)->getVampireStatus() == NORMAL) {
			foundmale = true;
			break;
		}
	}
	for (int i = 0; i < loop; i++) {
		if (allBunnys.at(i)->getSex() == FEMALE && allBunnys.at(i)->getAge() >= 2 && allBunnys.at(i)->getVampireStatus() == NORMAL && foundmale == true) {
			addNewBunny();
		}
	}
}
void GameEngine::killOldBunnys()
{
	for (int i = 0; i < allBunnys.size(); i++) {
		if (allBunnys.at(i)->getAge() >= 10 && allBunnys.at(i)->getVampireStatus() == NORMAL) {
			std::cout << allBunnys.at(i)->getName() << " died at age : " << allBunnys.at(i)->getAge() << std::endl;
			allBunnys.erase(allBunnys.begin() + i);
		}
	}
	for (int i = 0; i < allBunnys.size(); i++) {
		if (allBunnys.at(i)->getAge() >= 50 && allBunnys.at(i)->getVampireStatus() == VAMPIRE) {
			std::cout << allBunnys.at(i)->getName() << " died at age : " << allBunnys.at(i)->getAge() << std::endl;
			allBunnys.erase(allBunnys.begin() + i);
		}
	}
}
void GameEngine::killHalfOfThePopulaton()
{
	int halfOfTheBunnies = allBunnys.size() / 2;
	for (int i = 0; i < halfOfTheBunnies; i++) {
		int killThisOne = randomNumber(0, halfOfTheBunnies);
		allBunnys.erase(allBunnys.begin() + killThisOne);
	}
}
void GameEngine::printAllBunnys()
{
	for (int i = 0; i < allBunnys.size(); i++) {
		std::cout << allBunnys.at(i)->getName() << std::endl;
		std::cout << allBunnys.at(i)->getAge() << std::endl;
	}
}
bool GameEngine::GameOver()
{
	if (allBunnys.size() == 0) {
		std::cout << "Game Over" << std::endl;
		Sleep(3000);
		return false;
	}
}
void GameEngine::radioActiveBunnys()
{
	int numberOfRadioActiveBunnies{};
	for (int i = 0; i < allBunnys.size(); i++) {
		if (allBunnys.at(i)->getVampireStatus() == VAMPIRE)
			numberOfRadioActiveBunnies++;
	}
	for (int i = 0; i <numberOfRadioActiveBunnies; i++) {
		int makeBunnyVampire = randomNumber(0, allBunnys.size() - 1);
		if (allBunnys.at(makeBunnyVampire)->getVampireStatus() == NORMAL) {
			allBunnys.at(makeBunnyVampire)->setVampireStatus(VAMPIRE);
			std::cout << allBunnys.at(makeBunnyVampire)->getName() << " turned in to a vampire !" << std::endl;
			Sleep(1000);
		}
	}
}
void GameEngine::addNewBunny()
{
	Bunny *newBunny = { nullptr };
	newBunny = new Bunny;
	allBunnys.push_back(newBunny);
	std::cout << newBunny->getName() << " was born! " << std::endl;
}
