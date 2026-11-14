---
title: "stdexperimentalmake_ostream_joiner(3)"
name: "stdexperimentalmake_ostream_joiner"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalmake_ostream_joiner/"
---

std::experimental::make_ostream_joiner - std::experimental::make_ostream_joiner

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;experimental/iterator&gt;

template &lt;class charT, class traits, class DelimT&gt;

std::experimental::ostream_joiner&lt;std::decay_t&lt;DelimT&gt;, charT, traits&gt;           (library fundamentals TS v2)

make_ostream_joiner(std::basic_ostream&lt;charT, traits&gt;&amp; os, DelimT&amp;&amp; delimiter);</code></pre> 
Creates an ostream_joiner object, deducing the template arguments from the types of the function arguments. 

<h2>Parameters</h2>

os - the basic_ostream object that the iterator is to be associated to 
delimiter - the delimiter

<h2>Return value</h2>

A ostream_joiner object, created as if by std::experimental::ostream_joiner&lt;std::decay_t&lt;DelimT&gt;, charT, traits&gt;(os, std::forward&lt;DelimT&gt;(delimiter)). 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;experimental/iterator&gt;

#include &lt;iostream&gt;

#include &lt;vector&gt;
int main()
{
    std::vector&lt;int&gt; x{1, 2, 3, 4};
    std::copy(x.begin(), x.end(),
              std::experimental::make_ostream_joiner(std::cout, &quot;, &quot;));
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;1, 2, 3, 4
