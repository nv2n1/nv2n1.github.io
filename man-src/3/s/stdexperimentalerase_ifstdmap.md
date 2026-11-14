---
title: "stdexperimentalerase_ifstdmap(3)"
name: "stdexperimentalerase_ifstdmap"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalerase_ifstdmap/"
---

std::experimental::erase_if(std::map) - std::experimental::erase_if(std::map)

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;experimental / map&gt;

    template &lt;class Key, class T, class Compare, class Alloc, class Pred&gt;
    (library fundamentals TS v2)

        void erase_if(std::map&lt;Key, T, Compare, Alloc&gt; &amp;c, Pred pred);</code></pre> 
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
