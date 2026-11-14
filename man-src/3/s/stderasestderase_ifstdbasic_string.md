---
title: "stderasestderase_ifstdbasic_string(3)"
name: "stderasestderase_ifstdbasic_string"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stderasestderase_ifstdbasic_string/"
---

std::erase,std::erase_if(std::basic_string) - std::erase,std::erase_if(std::basic_string)

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;string&gt;

    template &lt;class CharT, class Traits, class Alloc, class U&gt;
    (1)(since C++ 20)

        void erase(std::basic_string&lt;CharT, Traits, Alloc&gt; &amp;c, const U &amp;value);

template &lt;class CharT, class Traits, class Alloc, class Pred&gt;
(2)(since C++ 20)

    void erase_if(std::basic_string&lt;CharT, Traits, Alloc&gt; &amp;c, Pred pred);
1) Erases all elements that compare equal to value from the container. Equivalent to c.erase(std::remove(c.begin(), c.end(), value), c.end());

2) Erases all elements that satisfy the predicate pred from the container. Equivalent to c.erase(std::remove_if(c.begin(), c.end(), pred), c.end());
</code></pre>

<h2>Parameters</h2>

c - container from which to erase 
value - value to be removed 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unary predicate which returns true if the element should be erased. 
pred - The expression pred(v) must be convertible to bool for every argument v of type (possibly const) CharT, regardless of value_category, and must not modify v. Thus, a parameter type of CharT&amp;is not allowed 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;, nor is CharT unless for CharT a move is equivalent to a copy 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(since C++11)</i>.

<h2>Complexity</h2>

Linear.

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;removes elements satisfying specific criteria 
remove <i>(function template)</i> 
remove_if 
