---
title: "stdchronoweekdayweekday(3)"
name: "stdchronoweekdayweekday"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronoweekdayweekday/"
---

std::chrono::weekday::weekday - std::chrono::weekday::weekday

<h2>Synopsis</h2>

<pre><code>weekday() = default;
(1)(since C++ 20)

    explicit constexpr weekday(unsigned wd) noexcept;
(2)(since C++ 20)

    constexpr weekday(const std::chrono::sys_days &amp;dp) noexcept;
(3)(since C++ 20)

    explicit constexpr weekday(const std::chrono::local_days &amp;dp) noexcept;
(4)(since C++ 20)</code></pre> 
Constructs a weekday object. 
1) Default constructor leaves the weekday value uninitialized. 
2) Constructs a weekday object holding the weekday value wd. If wd &gt; 255, the value held is unspecified. 
3) Constructs a weekday object representing the day of the week dp corresponds to. This constructor defines an implicit conversion from std::chrono::sys_days to weekday. 
4) Constructs a weekday object representing the day of the week dp corresponds to, as if by weekday(std::chrono::sys_days(dp.time_since_epoch())). 
