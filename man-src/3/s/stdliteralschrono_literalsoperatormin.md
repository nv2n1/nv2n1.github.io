---
title: "stdliteralschrono_literalsoperatormin(3)"
name: "stdliteralschrono_literalsoperatormin"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdliteralschrono_literalsoperatormin/"
---

std::literals::chrono_literals::operator&quot;&quot;min - std::literals::chrono_literals::operator&quot;&quot;min

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;chrono&gt;

constexpr chrono::minutes operator &quot;&quot; min(unsigned long long mins); (1) (since C++14)

constexpr chrono::duration&lt;/*unspecified*/, ratio&lt;60,1&gt;&gt;            (2) (since C++14)

operator &quot;&quot; min(long double mins);</code></pre> 
Forms a std::chrono::duration literal representing minutes. 
1) integer literal, returns exactly std::chrono::minutes(mins) 
2) floating-point literal, returns a floating-point duration equivalent to std::chrono::minutes 

<h2>Parameters</h2>

minutes - the number of minutes

<h2>Return value</h2>

The std::chrono::duration literal. 

<h2>Possible implementation</h2>

&nbsp;<wbr>&nbsp;constexpr std::chrono::minutes operator &quot;&quot;min(unsigned long long m) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return std::chrono::minutes(m); 
&nbsp;<wbr>&nbsp;} 
&nbsp;<wbr>&nbsp;constexpr std::chrono::duration&lt;long double, 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::ratio&lt;60,1&gt;&gt; operator &quot;&quot;min(long double m) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return std::chrono::duration&lt;long double, ratio&lt;60,1&gt;&gt; (m); 
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
    auto lesson = 45min;
    auto halfmin = 0.5min;
    std::cout &lt;&lt; &quot;one lesson is &quot; &lt;&lt; lesson.count() &lt;&lt; &quot; minutes\n&quot;
              &lt;&lt; &quot;half a minute is &quot; &lt;&lt; halfmin.count() &lt;&lt; &quot; minutes\n&quot;;
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;one lesson is 45 minutes 
&nbsp;<wbr>&nbsp;half a minute is 0.5 minutes

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs new duration 
constructor <i>(public member function of std::chrono::duration&lt;Rep,Period&gt;)</i> 
