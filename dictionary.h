#ifndef AMJ_DICT.H
#define AMJ_DICT.H

#include <iostream>
#include <array>
#include <vector>
#include <memory>
#include <string>


class wordict {

	// A ==> 1, a ==> 1, maps letters to dict index
	std::unordered_map<char, int> index; // A ==> 1, a ==> 1, maps letters to dict index
	struct Letters {
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
	// following string contains all the letters we know to be in the target word
	std::string known; // max length of 5
	public:
		wordict();	
};













#endif
