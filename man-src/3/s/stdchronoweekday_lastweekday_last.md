---
title: "stdchronoweekday_lastweekday_last(3)"
name: "stdchronoweekday_lastweekday_last"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronoweekday_lastweekday_last/"
---

std::chrono::weekday_last::weekday_last - std::chrono::weekday_last::weekday_last

<h2>Synopsis</h2>

explicit constexpr weekday_last(const chrono::weekday&amp; wd) noexcept; <i>(since C++20)</i> 
Constructs a weekday_last object storing the weekday wd. 

<h2>Notes</h2>

A more convenient way to construct a weekday_last is with weekday's operator[], i.e., wd[std::chrono::last]. 
