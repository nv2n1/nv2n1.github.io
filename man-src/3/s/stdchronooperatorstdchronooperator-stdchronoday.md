---
title: "stdchronooperatorstdchronooperator-stdchronoday(3)"
name: "stdchronooperatorstdchronooperator-stdchronoday"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronooperatorstdchronooperator-stdchronoday/"
---

std::chrono::operator+,std::chrono::operator-(std::chrono::day) - std::chrono::operator+,std::chrono::operator-(std::chrono::day)

<h2>Synopsis</h2>

<pre><code>constexpr std::chrono::day operator+(const std::chrono::day &amp;d, (1)(since C++ 20)

                                                                    const std::chrono::days &amp;ds) noexcept;

constexpr std::chrono::day operator+(const std::chrono::days &amp;ds, (2)(since C++ 20)

                                                                      const std::chrono::day &amp;d) noexcept;

constexpr std::chrono::day operator-(const std::chrono::day &amp;d, (3)(since C++ 20)

                                                                    const std::chrono::days &amp;ds) noexcept;

constexpr std::chrono::days operator-(const std::chrono::day &amp;x, (4)(since C++ 20)

                                                                     const std::chrono::day &amp;y) noexcept;</code></pre> 
1-2) Adds ds.count() days to d. 
3) Subtracts ds.count() days from d. 
4) Calculate the difference, in days, between two day x and y. 

<h2>Return value</h2>

1-2) std::chrono::day(unsigned(d) + ds.count()) 
3) std::chrono::day(unsigned(d) - ds.count()) 
4) std::chrono::days(int(unsigned(x)) - int(unsigned(y))) 

<h2>Notes</h2>

For (1-3), if the result would be outside the range [0, 255], the actual stored value is unspecified. 

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

<pre><code>operator++      increments or decrements the day

operator++(int) (public member function)

operator--

operator--(int)
adds or subtracts a number of days

operator+=      (public member function)

operator-=




</code></pre>
