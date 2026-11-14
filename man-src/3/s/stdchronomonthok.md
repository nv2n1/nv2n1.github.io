---
title: "stdchronomonthok(3)"
name: "stdchronomonthok"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronomonthok/"
---

std::chrono::month::ok - std::chrono::month::ok

<h2>Synopsis</h2>

constexpr bool ok() const noexcept; <i>(since C++20)</i> 
Checks if the month value stored in *this is in the valid range, i.e., [1, 12]. 

<h2>Return value</h2>

true if the month value stored in *this is in the range [1, 12]. Otherwise false. 
