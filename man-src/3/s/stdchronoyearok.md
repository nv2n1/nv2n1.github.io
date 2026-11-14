---
title: "stdchronoyearok(3)"
name: "stdchronoyearok"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronoyearok/"
---

std::chrono::year::ok - std::chrono::year::ok

<h2>Synopsis</h2>

constexpr bool ok() const noexcept; <i>(since C++20)</i> 
Checks if the year value stored in *this is in the valid range, i.e., [-32767, 32767]. 

<h2>Return value</h2>

true if the year value stored in *this is in the range [-32767, 32767]. Otherwise false. 
