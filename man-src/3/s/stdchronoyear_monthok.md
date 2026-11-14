---
title: "stdchronoyear_monthok(3)"
name: "stdchronoyear_monthok"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronoyear_monthok/"
---

std::chrono::year_month::ok - std::chrono::year_month::ok

<h2>Synopsis</h2>

constexpr bool ok() const noexcept; <i>(since C++20)</i> 
Checks if the year and month values stored in this object are valid. 

<h2>Return value</h2>

year().ok() &amp;&amp; month().ok() 
