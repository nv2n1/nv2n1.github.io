---
title: "stdexperimentalerase_ifstdset(3)"
name: "stdexperimentalerase_ifstdset"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalerase_ifstdset/"
---

std::experimental::erase_if(std::set) - std::experimental::erase_if(std::set)

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;experimental / set&gt;

    template &lt;class Key, class Compare, class Alloc, class Pred&gt;
    (library fundamentals TS v2)

        void erase_if(std::set&lt;Key, Compare, Alloc&gt; &amp;c, Pred pred);</code></pre> 
Erases all elements that satisfy the predicate pred from the container. Equivalent to <pre><code>for (auto i = c.begin(), last = c.end(); i != last;) {
    if (pred(*i)) {
        i = c.erase(i);
    } else {
        ++i;
    }
}
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

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;removes elements satisfying specific criteria 
remove <i>(function template)</i> 
remove_if 
