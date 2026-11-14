---
title: "stdliteralschrono_literalsoperatorns(3)"
name: "stdliteralschrono_literalsoperatorns"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdliteralschrono_literalsoperatorns/"
---

std::literals::chrono_literals::operator&quot;&quot;ns - std::literals::chrono_literals::operator&quot;&quot;ns

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;chrono&gt;

constexpr std::chrono::nanoseconds operator &quot;&quot; ns(unsigned long long nsec); (1) (since C++14)

constexpr std::chrono::duration&lt;/*unspecified*/,                            (2) (since C++14)

std::nano&gt; operator &quot;&quot; ns(long double nsec);</code></pre> 
Forms a std::chrono::duration literal representing nanoseconds. 
1) integer literal, returns exactly std::chrono::nanoseconds(nsec) 
2) floating-point literal, returns a floating-point duration equivalent to std::chrono::nanoseconds 

<h2>Parameters</h2>

nsec - the number of nanoseconds

<h2>Return value</h2>

The std::chrono::duration literal. 

<h2>Possible implementation</h2>

&nbsp;<wbr>&nbsp;constexpr std::chrono::nanoseconds operator &quot;&quot;ns(unsigned long long ns) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return chrono::nanoseconds(ns); 
&nbsp;<wbr>&nbsp;} 
&nbsp;<wbr>&nbsp;constexpr std::chrono::duration&lt;long double, std::nano&gt; operator &quot;&quot;ns(long double ns) 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return std::chrono::duration&lt;long double, std::nano&gt;(ns); 
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
    auto d1 = 250ns;
    std::chrono::nanoseconds d2 = 1us;
    std::cout &lt;&lt; &quot;250ns = &quot; &lt;&lt; d1.count() &lt;&lt; &quot; nanoseconds\n&quot;
              &lt;&lt; &quot;1us = &quot; &lt;&lt; d2.count() &lt;&lt; &quot; nanoseconds\n&quot;;
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;250ns = 250 nanoseconds 
&nbsp;<wbr>&nbsp;1us = 1000 nanoseconds

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs new duration 
constructor <i>(public member function of std::chrono::duration&lt;Rep,Period&gt;)</i> 
