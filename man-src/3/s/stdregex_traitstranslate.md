---
title: "stdregex_traitstranslate(3)"
name: "stdregex_traitstranslate"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdregex_traitstranslate/"
---

std::regex_traits&lt;CharT&gt;::translate - std::regex_traits&lt;CharT&gt;::translate

<h2>Synopsis</h2>

<pre><code>CharT translate(CharT c) const;</code></pre> 
Obtains the comparison key for the character c, such that all characters that are equivalent to this character in the imbued locale produce the same key. 
When the regex library needs to match two characters c1 and c2 and the flag std::regex_constants::collate is true, it executes regex_traits&lt;&gt;::translate(c1) == regex_traits&lt;&gt;::translate(c2). 
Standard library specializations of std::regex_traits return c unmodified. 

<h2>Parameters</h2>

c - character that needs to be examined for equivalence

<h2>Return value</h2>

The comparison key for c in the currently imbued locale. 

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 
