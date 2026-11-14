---
title: "stdmake_pair(3)"
name: "stdmake_pair"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdmake_pair/"
---

std::make_pair - std::make_pair

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;utility&gt;

template&lt; class T1, class T2 &gt;                           (until C++11)

std::pair&lt;T1,T2&gt; make_pair( T1 t, T2 u );

template&lt; class T1, class T2 &gt;                           (since C++11)

std::pair&lt;V1,V2&gt; make_pair( T1&amp;&amp; t, T2&amp;&amp; u );            (until C++14)

template&lt; class T1, class T2 &gt;                           (since C++14)

constexpr std::pair&lt;V1,V2&gt; make_pair( T1&amp;&amp; t, T2&amp;&amp; u );</code></pre> 
Creates a std::pair object, deducing the target type from the types of arguments. 
The deduced types V1 and V2 are std::decay&lt;T1&gt;::type and std::decay&lt;T2&gt;::type (the usual type transformations applied to arguments of functions passed by value) unless application of std::decay results in std::reference_wrapper&lt;X&gt; for some type X, in which case the deduced type is X&amp;. <i>(since C++11)</i> 

<h2>Parameters</h2>

t, u - the values to construct the pair from

<h2>Return value</h2>

An std::pair object containing the given values. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;utility&gt;

#include &lt;functional&gt;
int main()

{
    int n = 1;
    int a[5] = {1, 2, 3, 4, 5};
    // build a pair from two ints
    auto p1 = std::make_pair(n, a[1]);
    std::cout &lt;&lt; &quot;The value of p1 is &quot;
              &lt;&lt; &quot;(&quot; &lt;&lt; p1.first &lt;&lt; &quot;, &quot; &lt;&lt; p1.second &lt;&lt; &quot;)\n&quot;;
    // build a pair from a reference to int and an array (decayed to pointer)
    auto p2 = std::make_pair(std::ref(n), a);
    n = 7;
    std::cout &lt;&lt; &quot;The value of p2 is &quot;
              &lt;&lt; &quot;(&quot; &lt;&lt; p2.first &lt;&lt; &quot;, &quot; &lt;&lt; *(p2.second + 2) &lt;&lt; &quot;)\n&quot;;
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;The value of p1 is (1, 2) 
&nbsp;<wbr>&nbsp;The value of p2 is (7, 3)
