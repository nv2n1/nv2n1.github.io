---
title: "stdchronoyear_month_weekdayyearstdchronoyear_month_weekdaymonth(3)"
name: "stdchronoyear_month_weekdayyearstdchronoyear_month_weekdaymonth"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronoyear_month_weekdayyearstdchronoyear_month_weekdaymonth/"
---

std::chrono::year_month_weekday::year,std::chrono::year_month_weekday::month, - std::chrono::year_month_weekday::year,std::chrono::year_month_weekday::month,

<h2>Synopsis</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>std::chrono::year_month_weekday::weekday_indexed <pre><code>constexpr std::chrono::year year() const noexcept;
(1)(since C++ 20)

    constexpr std::chrono::month month() const noexcept;
(2)(since C++ 20)

    constexpr std::chrono::weekday weekday() const noexcept;
(3)(since C++ 20)

    constexpr unsigned index() const noexcept;
(4)(since C++ 20)

    constexpr std::chrono::weekday_indexed weekday_indexed() const(5)(since C++ 20)

        noexcept;</code></pre> 
Retrieves the field values stored in this year_month_weekday object. 

<h2>Return values</h2>

1)&nbsp;<wbr>Returns the stored std::chrono::year value. 
2)&nbsp;<wbr>Returns the stored std::chrono::month value. 
3)&nbsp;<wbr>Returns the stored std::chrono::weekday value. 
4)&nbsp;<wbr>Returns the stored weekday index. 
5)&nbsp;<wbr>weekday()[index()].
