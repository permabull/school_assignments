#include <iostream>
#include "Bunny.h"
#include "enums.h"
#include "GameEngine.h"
#include <sstream>
#include <Windows.h>
#include <time.h>

int main()
{
	GameEngine bunnyGame;
	bunnyGame.initializeGame();
	int year{};
	bool gameOver = true;

	while (gameOver != false)
	{
		year++;
		bunnyGame.newBunnyBabies();
		bunnyGame.newTurn();
		bunnyGame.killOldBunnys();
		std::cout << "BunnyCount : " << bunnyGame.bunnyCount() << std::endl;
		std::cout << "Year : " << year << std::endl;
		Sleep(1000);
		if (bunnyGame.bunnyCount() > 150) {
			bunnyGame.killHalfOfThePopulaton();
			std::cout << "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$" << std::endl;
			std::cout << "M-m-m-uuuultiiKIiiiiiiiiiLL!" << std::endl;
			std::cout << "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$" << std::endl;
			std::cout << "BunnyCount : " << bunnyGame.bunnyCount() << std::endl;
			Sleep(500);
		}
		bunnyGame.radioActiveBunnys();
		gameOver = bunnyGame.GameOver();
	}
}





















//
//std::string Bunny::randomBunnyName()
//{
//	std::ifstream in_file{ "C:/Users/tomten/Desktop/Bunnycount/Bunnycount/names.txt" };
//	int randomRow = randomNumber(1, 80);
//	int currentRow{};
//	std::string line;
//	if (!in_file) {
//		std::cerr << "File open error" << std::endl;
//	}
//	while (getline(in_file, line)) {
//		++currentRow;
//		if (currentRow == randomRow) {
//			in_file.close();
//			return line;
//		}
//	}
//}