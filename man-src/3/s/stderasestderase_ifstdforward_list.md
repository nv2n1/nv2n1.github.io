---
title: "stderasestderase_ifstdforward_list(3)"
name: "stderasestderase_ifstdforward_list"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stderasestderase_ifstdforward_list/"
---

std::erase,std::erase_if(std::forward_list) - std::erase,std::erase_if(std::forward_list)

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;forward_list&gt;

    template &lt;class T, class Alloc, class U&gt;
    (1)(since C++ 20)

        void erase(std::forward_list&lt;T, Alloc&gt; &amp;c, const U &amp;value);

template &lt;class T, class Alloc, class Pred&gt;
(2)(since C++ 20)

    void erase_if(std::forward_list&lt;T, Alloc&gt; &amp;c, Pred pred);
1) Erases all elements that compare equal to value from the container. Equivalent to c.remove_if([&amp;](auto&amp; elem) {
    return elem == value; });

2) Erases all elements that satisfy the predicate pred from the container. Equivalent to c.remove_if(pred);
</code></pre>

<h2>Parameters</h2>

c - container from which to erase 
value - value to be removed 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unary predicate which returns true if the element should be erased. 
pred - The expression pred(v) must be convertible to bool for every argument v of type (possibly const) T, regardless of value_category, and must not modify v. Thus, a parameter type of T&amp;is not allowed 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;, nor is T unless for T a move is equivalent to a copy 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(since C++11)</i>.

<h2>Complexity</h2>

Linear.

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>Notes</h2>

Unlike std::forward_list::remove, erase accepts heterogenous types and does not force a conversion to the container's value type before invoking the == operator. 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;removes elements satisfying specific criteria 
remove <i>(function template)</i> 
remove_if 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;removes elements satisfying specific criteria 
remove <i>(public member function)</i> 
remove_if 
