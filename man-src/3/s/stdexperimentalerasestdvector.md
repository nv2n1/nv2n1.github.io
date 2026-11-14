---
title: "stdexperimentalerasestdvector(3)"
name: "stdexperimentalerasestdvector"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalerasestdvector/"
---

std::experimental::erase(std::vector) - std::experimental::erase(std::vector)

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;experimental / vector&gt;

    template &lt;class T, class A, class U&gt;
    (library fundamentals TS v2)

        void erase(std::vector&lt;T, A&gt; &amp;c, const U &amp;value);
Erases all elements that compare equal to value from the container.Equivalent to c.erase(std::remove(c.begin(), c.end(), value), c.end());
</code></pre>

<h2>Parameters</h2>

c - container from which to erase 
value - value to be removed

<h2>Complexity</h2>

Linear.

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;removes elements satisfying specific criteria 
remove <i>(function template)</i> 
remove_if 
erase_if_(std::vector) Erases all elements satisfying a predicate from a std::vector 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
(library fundamentals 2 TS) 
