#include <iostream>
#include <array>
#include <vector>
#include <memory>
#include <string>

#ifndef AMJ_DICT.H
#define AMJ_DICT.H

class wordict {

	// A ==> 1, a ==> 1, maps letters to dict index
	std::unordered_map<char, int> index; // A ==> 1, a ==> 1, maps letters to dict index
	std::array<std::vector<std::string>, 26> dict;
	// following string contains all the letters we know to be in the target word
	std::string known; // max length of 5
	public:
		wordict(std::string known);	
};













#endif
