---
title: "stderase_ifstdunordered_set(3)"
name: "stderase_ifstdunordered_set"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stderase_ifstdunordered_set/"
---

std::erase_if(std::unordered_set) - std::erase_if(std::unordered_set)

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;unordered_set&gt;

    template &lt;class Key, class Hash, class KeyEqual, class Alloc, class Pred&gt;
    (1)(since C++ 20)

        void erase_if(std::unordered_set&lt;Key, Hash, KeyEqual, Alloc&gt; &amp;c, Pred pred);</code></pre> 
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
pred - predicate that returns true if the element should be erased

<h2>Complexity</h2>

Linear.

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;removes elements satisfying specific criteria 
remove <i>(function template)</i> 
remove_if 
