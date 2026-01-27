#ifndef BOTTLE
#define BOTTLE

#include <iostream>
#include <array>
#include <string>
#include <unordered_map>

struct Dictionary {
		std::array<std::string, 142> a;
		std::array<std::string, 175> b;
		std::array<std::string, 198> c;
		std::array<std::string, 111> d;
		std::array<std::string, 72>  e;
		std::array<std::string, 136> f;
		std::array<std::string, 116> g;
		std::array<std::string, 69>  h;
		std::array<std::string, 35>  i;
		std::array<std::string, 20>  j;
		std::array<std::string, 21>  k;
		std::array<std::string, 89>  l;
		std::array<std::string, 108> m;
		std::array<std::string, 37>  n;
		std::array<std::string, 41>  o;
		std::array<std::string, 144> p;
		std::array<std::string, 23>  q;
		std::array<std::string, 105> r;
		std::array<std::string, 368> s;
		std::array<std::string, 149> t;
		std::array<std::string, 34>  u;
		std::array<std::string, 43>  v;
		std::array<std::string, 83>  w;
		// NO LETTERS STARTING WITH X
		std::array<std::string, 6>   y;
		std::array<std::string, 3>   z;
};

class Bottle {

	// A ==> 1, a ==> 1, maps letters to dict index
	std::unordered_map<char, int> index; // A ==> 1, a ==> 1, maps letters to dict index
	Dictionary dictionary;

	// -2 if unknown, -1 if not in word
	// 0 if in word but unknown position, char gets added to zeroes array
	// [1,5] denotes position
	std::unordered_map<char, int> letter_state;

	// zeros[char] returns an array of position we KNOW char isn't in
	// always check this array AFTER checking letter_state
	std::unordered_map<char, std::array<int, 5>> zeros;

	bool matches_constraints(std::string word);

	public:
		Bottle();
		
		// python file calls this func 5 times, once for each letter
		void update_letter(char l, int state, int position);
		std::string next_guess();

};











#endif
