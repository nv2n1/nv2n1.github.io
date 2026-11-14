---
title: "stdregex_traitstranslate_nocase(3)"
name: "stdregex_traitstranslate_nocase"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdregex_traitstranslate_nocase/"
---

std::regex_traits&lt;CharT&gt;::translate_nocase - std::regex_traits&lt;CharT&gt;::translate_nocase

<h2>Synopsis</h2>

<pre><code>CharT translate_nocase(CharT c) const;</code></pre> 
Obtains the comparison key for the character c, such that all characters that are equivalent to this character in the imbued locale, ignoring the case differences, if any, produce the same key. 
When the regex library needs to match two characters c1 and c2 and the flag std::regex_constants::icase is true, it executes regex_traits&lt;&gt;::translate_nocase(c1) == regex_traits&lt;&gt;::translate_nocase(c2). 
Standard library specializations of std::regex_traits return std::use_facet&lt;std::ctype&lt;CharT&gt;&gt;(getloc()).tolower(c), that is, convert c to lowercase, using the currently imbued locale. 

<h2>Parameters</h2>

c - character that needs to be examined for equivalence, ignoring case

<h2>Return value</h2>

The case-insensitive comparison key for c in the currently imbued locale. 

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 
