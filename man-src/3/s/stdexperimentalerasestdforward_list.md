---
title: "stdexperimentalerasestdforward_list(3)"
name: "stdexperimentalerasestdforward_list"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalerasestdforward_list/"
---

std::experimental::erase(std::forward_list) - std::experimental::erase(std::forward_list)

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;experimental / forward_list&gt;

    template &lt;class T, class A, class U&gt;
    (library fundamentals TS v2)

        void erase(std::forward_list&lt;T, A&gt; &amp;c, const U &amp;value);
Erases all elements that compare equal to value from the container.Equivalent to c.remove_if([&amp;](auto &amp;elem) { return elem == value; });
</code></pre>

<h2>Parameters</h2>

c - container from which to erase 
value - value to be removed

<h2>Complexity</h2>

Linear.

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>Notes</h2>

Unlike std::forward_list::remove, this function template accepts heterogenous types and does not force a conversion to the container's value type before invoking the == operator. 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;removes elements satisfying specific criteria 
remove <i>(function template)</i> 
remove_if 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;removes elements satisfying specific criteria 
remove <i>(public member function of std::forward_list&lt;T,Allocator&gt;)</i> 
remove_if 
erase_if_(std::forward_list) Erases all elements satisfying a predicate from a std::forward_list 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
(library fundamentals 2 TS) 
