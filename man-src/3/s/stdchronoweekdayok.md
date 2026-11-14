---
title: "stdchronoweekdayok(3)"
name: "stdchronoweekdayok"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronoweekdayok/"
---

std::chrono::weekday::ok - std::chrono::weekday::ok

<h2>Synopsis</h2>

constexpr bool ok() const noexcept; <i>(since C++20)</i> 
Checks if the weekday value stored in *this is in the valid range, i.e., [0, 6]. 

<h2>Return value</h2>

true if the weekday value stored in *this is in the range [0, 6]. Otherwise false. 
