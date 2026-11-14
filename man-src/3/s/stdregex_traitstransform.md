---
title: "stdregex_traitstransform(3)"
name: "stdregex_traitstransform"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdregex_traitstransform/"
---

std::regex_traits&lt;CharT&gt;::transform - std::regex_traits&lt;CharT&gt;::transform

<h2>Synopsis</h2>

<pre><code>template &lt;class ForwardIt&gt;

string_type transform(ForwardIt first, ForwardIt last) const;
Obtains the sort key for the character sequence [first, last), such that if a sort key compares less than another sort key with operator&lt;, then the character sequence that produced the first sort key comes before the character sequence that produced the second sort key, in the currently imbued locale's collation order.

For example when the regex flag std::regex_constants::collate is set, then the sequence [a-b] would match some character c1 if traits.transform(&quot;a&quot;) &lt;= traits.transform(c1) &lt;= traits.transform(&quot;b&quot;). Note that this function takes a character sequence as the argument to accomodate to the ranges defined like [[.ae.]-d].

Standard library specializations of std::regex_traits return std::use_facet&lt;std::collate&lt;CharT&gt;&gt;(getloc()).transform(str.data(), str.data() + str.length()) for some temporary string str constructed as string_type str(first, last).
</code></pre>

<h2>Parameters</h2>

first, last - a pair of LegacyForwardIterators which determines the sequence of characters to compare

<h2>Type requirements</h2>

- 
ForwardIt must meet the requirements of LegacyForwardIterator.

<h2>Return value</h2>

The collation key for the character sequence [first, last) in the currently imbued locale. 

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 
