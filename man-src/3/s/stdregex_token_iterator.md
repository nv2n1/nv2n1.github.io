---
title: "stdregex_token_iterator(3)"
name: "stdregex_token_iterator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdregex_token_iterator/"
---

std::regex_token_iterator&lt;BidirIt,CharT,Traits&gt;::regex_token_iterator - std::regex_token_iterator&lt;BidirIt,CharT,Traits&gt;::regex_token_iterator

<h2>Synopsis</h2>

<pre><code>regex_token_iterator();
(1)(since C++ 11)

    regex_token_iterator(BidirectionalIterator a, BidirectionalIterator b,

                         const regex_type &amp;re,

                         int submatch = 0, (2)(since C++ 11)

                                               std::regex_constants::match_flag_type m =

                                                   std::regex_constants::match_default);

regex_token_iterator(BidirectionalIterator a, BidirectionalIterator b,

                     const regex_type &amp;re,

                     const std::vector&lt;int&gt; &amp;submatches, (3)(since C++ 11)

                                                             std::regex_constants::match_flag_type m =

                                                                 std::regex_constants::match_default);

regex_token_iterator(BidirectionalIterator a, BidirectionalIterator b,

                     const regex_type &amp;re,

                     std::initializer_list&lt;int&gt; submatches, (4)(since C++ 11)

                                                                std::regex_constants::match_flag_type m =

                                                                    std::regex_constants::match_default);

template &lt;std::size_t N&gt;

regex_token_iterator(BidirectionalIterator a, BidirectionalIterator b,

                     const regex_type &amp;re, (5)(since C++ 11)

                                               const int (&amp;submatches)[N],

                     std::regex_constants::match_flag_type m =

                         std::regex_constants::match_default);

regex_token_iterator(const regex_token_iterator &amp;other);
(6)(since C++ 11)

    regex_token_iterator(BidirectionalIterator a, BidirectionalIterator b,

                         const regex_type &amp;&amp;re,

                         int submatch = 0, (7)(since C++ 14)

                                               std::regex_constants::match_flag_type m =

                                                   std::regex_constants::match_default) = delete;

regex_token_iterator(BidirectionalIterator a, BidirectionalIterator b,

                     const regex_type &amp;&amp;re,

                     const std::vector&lt;int&gt; &amp;submatches, (8)(since C++ 14)

                                                             std::regex_constants::match_flag_type m =

                                                                 std::regex_constants::match_default) = delete;

regex_token_iterator(BidirectionalIterator a, BidirectionalIterator b,

                     const regex_type &amp;&amp;re,

                     std::initializer_list&lt;int&gt; submatches, (9)(since C++ 14)

                                                                std::regex_constants::match_flag_type m =

                                                                    std::regex_constants::match_default) = delete;

template &lt;std::size_t N&gt;

regex_token_iterator(BidirectionalIterator a, BidirectionalIterator b,

                     const regex_type &amp;&amp;re, (10)(since C++ 14)

                                                const int (&amp;submatches)[N],

                     std::regex_constants::match_flag_type m =

                         std::regex_constants::match_default) = delete;</code></pre> 
Constructs a new regex_token_iterator: 
1) Default constructor. Constructs the end-of-sequence iterator. 
2-5) First, copies the list of the requested submatch out of the submatches or submatch argument into the member list stored in the iterator and constructs the member std::regex_iterator by passing a, b, re, and m to its four-argument constructor (that constructor performs the initial call to std::regex_search) and sets the internal counter of submatches to zero. 
* If, after construction, the member regex_iterator is not an end-of-sequence iterator, sets the member pointer to the address of the current std::sub_match. 
* Otherwise (if the member regex_iterator is an end-of-sequence iterator), but the value -1 is one of the values in submatches/submatch, turns *this into a suffix iterator pointing at the range [a,b) (the entire string is the non-matched suffix) 
* Otherwise (if -1 is not in the list of submatches), turns *this into the end-of-sequence iterator. 
The behavior is undefined if any value in submatches is less than -1. 
6) Copy constructor: performs member-wise copy (including making a copy of the member regex_iterator and the member pointer to current sub_match). 
7-10) The overloads 2-5 are prohibited from being called with a temporary regex since otherwise the returned iterator would be immediately invalidated 

<h2>Parameters</h2>

a - LegacyBidirectionalIterator to the beginning of the target character sequence 
b - LegacyBidirectionalIterator to the end of the target character sequence 
re - regular expression used to search the target character sequence 
submatch - the index of the submatch that should be returned. &quot;0&quot; represents the entire match, and &quot;-1&quot; represents the parts that are not matched (e.g, the stuff between matches). 
submatches - the sequence of submatch indices that should be iterated over within each match, may include the special value -1 for the non-matched fragments 
m - flags that govern the behavior of re

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 
