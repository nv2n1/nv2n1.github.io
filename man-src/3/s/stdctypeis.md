---
title: "stdctypeis(3)"
name: "stdctypeis"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdctypeis/"
description: "std::ctype<char>::is – std::ctype<char>::is"
---

<p>std::ctype&lt;char&gt;::is &#8211; std::ctype&lt;char&gt;::is</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;locale&gt;<br />
bool is(mask m, char c) const; <code>(1)</code><br />
const char* is(const char* low, const char* high, mask* vec) const; <code>(2)</code><br />
1) Checks if the character c is classified by the mask m according to the classification table returned by the member function table(). Effectively calculates table()[(unsigned char)c] &amp; m<br />
2) For every character in the character array [low, high), reads its full classification mask from the classification table returned by the member function table() (that is, evaluates table()[ (unsigned char)*p] and stores it in the corresponding element of the array pointed to by vec<br />
If (unsigned char)c &gt;= std::ctype&lt;char&gt;::table_size, then an implementation-defined value is substituted instead of table()[(unsigned char)c], possibly different for different values of c. </p>
<h2>Parameters</h2>
<p>c &#8211; character to classify<br />
m &#8211; mask to use for classifying a single character<br />
low &#8211; pointer to the first character in an array of characters to classify<br />
high &#8211; one past the end pointer for the array of characters to classify<br />
vec &#8211; pointer to the first element of the array of masks to fill</p>
<h2>Return value</h2>
<p>1) true if c is classified by m in table()<br />
2) high </p>
<h2>Notes</h2>
<p>Unlike the primary template std::ctype, this specialization does not perform a virtual function call when classifying characters. To customize the behavior, a derived class may provide a non-default classification table to the base class constructor. </p>
<h2>Example</h2>
<p>&nbsp;This section is incomplete<br />
&nbsp;Reason: no example </p>
<h2>See also</h2>
<p>do_is classifies a character or a character sequence<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual protected member function of std::ctype&lt;CharT&gt;)</i><br />
<code>[virtual]</code> </p>
