---
title: "stdchronoyearoperatorstdchronoyearoperator-2(3)"
name: "stdchronoyearoperatorstdchronoyearoperator-2"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronoyearoperatorstdchronoyearoperator-2/"
description: "std::chrono::year::operator+,std::chrono::year::operator- – std::chrono::year::operator+,std::chrono::year::operator-"
---

<p>std::chrono::year::operator+,std::chrono::year::operator- &#8211; std::chrono::year::operator+,std::chrono::year::operator-</p>
<h2>Synopsis</h2>
<p>constexpr std::chrono::year operator+() noexcept; <code>(1)</code> <i>(since C++20)</i><br />
constexpr std::chrono::year operator-() noexcept; <code>(2)</code> <i>(since C++20)</i><br />
Applies the unary operators to the year value.<br />
1) Returns a copy of *this.<br />
2) Returns a year whose year value is the negation of that of *this. </p>
<h2>Return value</h2>
<p>1) *this<br />
2) std::chrono::year(-int(*this)) </p>
<h2>Example</h2>
<p>&nbsp;This section is incomplete<br />
&nbsp;Reason: no example </p>
