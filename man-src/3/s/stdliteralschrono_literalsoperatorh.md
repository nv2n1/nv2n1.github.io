---
title: "stdliteralschrono_literalsoperatorh(3)"
name: "stdliteralschrono_literalsoperatorh"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdliteralschrono_literalsoperatorh/"
---

std::literals::chrono_literals::operator&quot;&quot;h - std::literals::chrono_literals::operator&quot;&quot;h

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;chrono&gt;

constexpr chrono::hours operator &quot;&quot; h(unsigned long long hrs);  (1) (since C++14)

constexpr chrono::duration&lt;/*unspecified*/, std::ratio&lt;3600,1&gt;&gt; (2) (since C++14)

operator &quot;&quot; h(long double hrs);</code></pre> 
Forms a std::chrono::duration literal representing hours. 
1) integer literal, returns exactly std::chrono::hours(hrs) 
2) floating-point literal, returns a floating-point duration equivalent to std::chrono::hours 

<h2>Parameters</h2>

hrs - the number of hours

<h2>Return value</h2>

The std::chrono::duration literal. 

<h2>Possible implementation</h2>

&nbsp;<wbr>&nbsp;constexpr std::chrono::hours operator &quot;&quot;h(unsigned long long h) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return std::chrono::hours(h); 
&nbsp;<wbr>&nbsp;} 
&nbsp;<wbr>&nbsp;constexpr std::chrono::duration&lt;long double, ratio&lt;3600,1&gt;&gt; operator &quot;&quot;h(long double h) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return std::chrono::duration&lt;long double, std::ratio&lt;3600,1&gt;&gt;(h); 
&nbsp;<wbr>&nbsp;}

<h2>Notes</h2>

These operators are declared in the namespace std::literals::chrono_literals, where both literals and chrono_literals are inline namespaces. Access to these operators can be gained with using namespace std::literals, using namespace std::chrono_literals, and using namespace std::literals::chrono_literals. 
In addition, within the namespace std::chrono, the directive using namespace literals::chrono_literals; is provided by the standard library, so that if a programmer uses using namespace std::chrono; to gain access to the classes in the chrono library, the corresponding literal operators become visible as well. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;chrono&gt;
int main()

{
    using namespace std::chrono_literals;
    auto day = 24h;
    auto halfhour = 0.5h;
    std::cout &lt;&lt; &quot;one day is &quot; &lt;&lt; day.count() &lt;&lt; &quot; hours\n&quot;
              &lt;&lt; &quot;half an hour is &quot; &lt;&lt; halfhour.count() &lt;&lt; &quot; hours\n&quot;;
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;one day is 24 hours 
&nbsp;<wbr>&nbsp;half an hour is 0.5 hours

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs new duration 
constructor <i>(public member function of std::chrono::duration&lt;Rep,Period&gt;)</i> 
