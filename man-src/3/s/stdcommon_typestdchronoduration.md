---
title: "stdcommon_typestdchronoduration(3)"
name: "stdcommon_typestdchronoduration"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdcommon_typestdchronoduration/"
---

std::common_type(std::chrono::duration) - std::common_type(std::chrono::duration)

<h2>Synopsis</h2>

<pre><code>template &lt;class Rep1, class Period1, class Rep2, class Period2&gt;

struct common_type&lt;std::chrono::duration&lt;Rep1, Period1&gt;,

                   std::chrono::duration&lt;Rep2, Period2&gt;&gt; {
    (since C++ 11)

        typedef std::chrono::duration&lt;

            typename std::common_type&lt;Rep1, Rep2&gt;::type, /*see note*/&gt; type;
};</code></pre> 
Exposes the type named type, which is the common type of two std::chrono::durations. 

<h2>Note</h2>

The period of the resulting duration is the greatest common divisor of Period1 and Period2.

<h2>Example</h2>

// Run this code #include &lt;iostream&gt;

#include &lt;chrono&gt; 
&nbsp;<wbr>&nbsp;// std::chrono already finds the greatest common divisor, 
&nbsp;<wbr>&nbsp;// likely using std::common_type&lt;&gt;. We make the type 
&nbsp;<wbr>&nbsp;// deduction externally. <pre><code>template &lt;typename T, typename S&gt;

auto durationDiff(const T &amp;t, const S &amp;s) -&gt; typename std::common_type&lt;T, S&gt;::type

{
    typedef typename std::common_type&lt;T, S&gt;::type Common;
    return Common(t) - Common(s);
}

int main()

{
    typedef std::chrono::milliseconds milliseconds;
    typedef std::chrono::microseconds microseconds;
    auto ms = milliseconds(30);
    auto us = microseconds(1100);
    std::cout &lt;&lt; ms.count() &lt;&lt; &quot;ms - &quot; &lt;&lt; us.count() &lt;&lt; &quot;us = &quot;
              &lt;&lt; durationDiff(ms, us).count() &lt;&lt; &quot;\n&quot;;
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;30ms - 1100us = 28900

<h2>See also</h2>

common_type determines the common type of a group of types 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++11)</i> 
