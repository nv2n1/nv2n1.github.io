---
title: "stdchronoweekday_indexedok(3)"
name: "stdchronoweekday_indexedok"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronoweekday_indexedok/"
---

std::chrono::weekday_indexed::ok - std::chrono::weekday_indexed::ok

<h2>Synopsis</h2>

constexpr bool ok() const noexcept; <i>(since C++20)</i> 
Checks if the weekday object and the index stored in *this are both valid. 

<h2>Return value</h2>

true if weekday().ok() == true and index() is in the range [1, 5]. Otherwise false. 
