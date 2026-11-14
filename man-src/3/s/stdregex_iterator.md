---
title: "stdregex_iterator(3)"
name: "stdregex_iterator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdregex_iterator/"
---

std::regex_iterator&lt;BidirIt,CharT,Traits&gt;::regex_iterator - std::regex_iterator&lt;BidirIt,CharT,Traits&gt;::regex_iterator

<h2>Synopsis</h2>

<pre><code>regex_iterator();
(1)(since C++ 11)

    regex_iterator(BidirIt a, BidirIt b,

                   const regex_type &amp;re, (2)(since C++ 11)

                                             std::regex_constants::match_flag_type m =

                                                 std::regex_constants::match_default);

regex_iterator(const regex_iterator &amp;);
(3)(since C++ 11)

    regex_iterator(BidirIt, BidirIt,

                   const regex_type &amp;&amp;, (4)(since C++ 14)

                                            std::regex_constants::match_flag_type =

                                                std::regex_constants::match_default) = delete;</code></pre> 
Constructs a new regex_iterator: 
1) Default constructor. Constructs an end-of-sequence iterator. 
2) Constructs a regex_iterator from the sequence of characters [a, b), the regular expression re, and a flag m that governs matching behavior. This constructor performs an initial call to std::regex_search with this data. If the result of this initial call is false, *this is set to an end-of-sequence iterator. 
3) Copies a regex_iterator. 
4) The overload 2 is not allowed to be called with a temporary regex, since the returned iterator would be immediately invalidated. 

<h2>Parameters</h2>

a - BidirIt to the beginning of the target character sequence 
b - BidirIt to the end of the target character sequence 
re - regular expression used to search the target character sequence 
m - flags that govern the behavior of re

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 
