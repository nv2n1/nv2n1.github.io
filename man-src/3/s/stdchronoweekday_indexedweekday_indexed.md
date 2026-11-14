---
title: "stdchronoweekday_indexedweekday_indexed(3)"
name: "stdchronoweekday_indexedweekday_indexed"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronoweekday_indexedweekday_indexed/"
---

std::chrono::weekday_indexed::weekday_indexed - std::chrono::weekday_indexed::weekday_indexed

<h2>Synopsis</h2>

<pre><code>weekday_indexed() = default;
(since C++ 20)

    constexpr weekday_indexed(const std::chrono::weekday &amp;wd, unsigned index) noexcept;
(since C++ 20)</code></pre> 
Constructs a weekday_indexed. 
1) Default constructor leaves both the std::chrono::weekday and the index value uninitialized. 
2) Constructs a weekday_indexed storing the weekday wd and the index index. The values held are unspecified if !wd.ok() || index == 0 || index &gt; 5. 

<h2>Notes</h2>

A more convenient way to construct a weekday_indexed is with weekday's operator[], i.e., wd[index]. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;chrono&gt;

#include &lt;iostream&gt;

using namespace std::chrono;
int main()
{
    auto wdi = Tuesday[2]; // wdi is weekday_indexed representing the 2nd tuesday
    std::cout &lt;&lt; year_month_day{wdi / October / 2019y};
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;2019-10-08

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;convenience syntax for constructing a weekday_indexed or weekday_last from this weekday 
operator[] <i>(public member function of std::chrono::weekday)</i> 
