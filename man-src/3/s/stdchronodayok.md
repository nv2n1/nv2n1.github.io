---
title: "stdchronodayok(3)"
name: "stdchronodayok"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronodayok/"
---

std::chrono::day::ok - std::chrono::day::ok

<h2>Synopsis</h2>

constexpr bool ok() const noexcept; <i>(since C++20)</i> 
Checks if the day value stored in *this is in the valid range, i.e., [1, 31]. 

<h2>Return value</h2>

true if the day value stored in *this is in the range [1, 31]. Otherwise false. 
