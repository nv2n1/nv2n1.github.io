---
title: "stdchronoweekdayoperator(3)"
name: "stdchronoweekdayoperator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronoweekdayoperator/"
description: "std::chrono::weekday::operator[] – std::chrono::weekday::operator[]"
---

<p>std::chrono::weekday::operator[] &#8211; std::chrono::weekday::operator[]</p>
<h2>Synopsis</h2>
<p>constexpr std::chrono::weekday_indexed operator[](unsigned index) const noexcept; <code>(1)</code> <i>(since C++20)</i><br />
constexpr std::chrono::weekday_last operator[](std::chrono::last_spec) const noexcept; <code>(2)</code> <i>(since C++20)</i><br />
1) Constructs a weekday_indexed from *this and index. The result represents the index-th weekday in some yet-to-be-specified month. If index is not in the range [1, 5] or if !ok() the values held in the result is unspecified.<br />
2) Constructs a weekday_last from *this. The result represents the last weekday in some yet-to-be-specified month. </p>
<h2>Return value</h2>
<p>1) std::chrono::weekday_indexed(*this, index)<br />
2) std::chrono::weekday_last(*this) </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;chrono&gt;

#include &lt;iostream&gt;

using namespace std::chrono;
int main()

{
    // second tuesday in October 2019
    std::cout &lt;&lt; year_month_day{Tuesday[2] / October / 2019y} &lt;&lt; '
'
              // last tuesday in October 2019
              &lt;&lt; year_month_day{Tuesday[last] / October / 2019y} &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;2019-10-08<br />
&nbsp;<wbr>&nbsp;2019-10-29</p>
