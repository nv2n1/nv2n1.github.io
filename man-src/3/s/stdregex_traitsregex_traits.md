---
title: "stdregex_traitsregex_traits(3)"
name: "stdregex_traitsregex_traits"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdregex_traitsregex_traits/"
---

std::regex_traits&lt;CharT&gt;::regex_traits - std::regex_traits&lt;CharT&gt;::regex_traits

<h2>Synopsis</h2>

<pre><code>regex_traits();</code></pre> 
Default-constructs the std::regex_traits object, including default-constructing the private std::locale member or any other internal state as necessary. 

<h2>Parameters</h2>

<i>(none)</i>

<h2>Return value</h2>

<i>(none)</i> 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;regex&gt;
int main()

{
    std::locale::global(std::locale(&quot;en_US.utf8&quot;));
    std::regex_traits&lt;char&gt; r1;
    std::regex_traits&lt;wchar_t&gt; r2;
    std::cout &lt;&lt; &quot;The regex locale is &quot; &lt;&lt; r1.getloc().name() &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;The regex locale is en_US.utf8
