---
title: "stdlocalecombine(3)"
name: "stdlocalecombine"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdlocalecombine/"
---

std::locale::combine - std::locale::combine

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;locale&gt;

    template &lt;class Facet&gt;

    locale combine(const locale &amp;other) const;</code></pre> 
Constructs a locale object which is a copy of *this except for the facet of type Facet, which is copied from other. 

<h2>Return value</h2>

The new, nameless, locale. 

<h2>Exceptions</h2>

std::runtime_error if other does not implement Facet

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;locale&gt;
int main()

{
    const double number = 1000.25;
    std::cout &lt;&lt; &quot;\&quot;C\&quot; locale: &quot; &lt;&lt; number &lt;&lt; '\n';
    std::locale loc = std::locale().combine&lt;std::numpunct&lt;char&gt;&gt;(std::locale(&quot;en_US.UTF8&quot;));
    std::cout.imbue(loc);
    std::cout &lt;&lt; &quot;\&quot;C\&quot; locale with en_US numpunct: &quot; &lt;&lt; number &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;&quot;C&quot; locale: 1000.25 
&nbsp;<wbr>&nbsp;&quot;C&quot; locale with en_US numpunct: 1,000.25

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs a new locale 
constructor <i>(public member function)</i> 
