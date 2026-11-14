---
title: "stdexperimentalerase_ifstddeque(3)"
name: "stdexperimentalerase_ifstddeque"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalerase_ifstddeque/"
---

std::experimental::erase_if(std::deque) - std::experimental::erase_if(std::deque)

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;experimental / deque&gt;

    template &lt;class T, class Alloc, class Pred&gt;
    (library fundamentals TS v2)

        void erase_if(std::deque&lt;T, Alloc&gt; &amp;c, Pred pred);
Erases all elements that satisfy the predicate pred from the container.Equivalent to c.erase(std::remove_if(c.begin(), c.end(), pred), c.end());
</code></pre>

<h2>Parameters</h2>

c - container from which to erase 
pred - predicate that determines which elements should be erased

<h2>Complexity</h2>

Linear.

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;removes elements satisfying specific criteria 
remove <i>(function template)</i> 
remove_if 
erase_(std::deque) Erases all elements equal to a specific value from a std::deque 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
(library fundamentals 2 TS) 
