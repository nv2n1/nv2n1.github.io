---
title: "stdchronoyearis_leap(3)"
name: "stdchronoyearis_leap"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronoyearis_leap/"
---

std::chrono::year::is_leap - std::chrono::year::is_leap

<h2>Synopsis</h2>

constexpr bool is_leap() const noexcept; <i>(since C++20)</i> 
Determines if *this represents a leap year in the proleptic Gregorian calendar. 
*this represents a leap year if the stored year value 
* is divisible by 4 and not divisible by 100; or 
* is divisible by 400. 

<h2>Return value</h2>

true if *this represents a leap year, otherwise false. 
