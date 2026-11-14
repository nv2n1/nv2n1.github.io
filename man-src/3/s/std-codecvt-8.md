---
title: "std-codecvt-8(3)"
name: "std-codecvt-8"
section: "3"
letter: "s"
url: "/docs/linux/man/3-std-codecvt-8/"
description: "std::wctomb – std::wctomb"
---

<h2 class="name">NAME</h2>
<p> std::wctomb &#8211; std::wctomb</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;cstdlib&gt;<br />
int wctomb( char *s, wchar_t wc ); </p>
<p>Converts a wide character wc to multibyte encoding and stores it (including any shift sequences) in the char array whose first element is pointed to by s. No more than MB_CUR_MAX characters are stored.<br />
If wc is the null character, the null byte is written to s, preceded by any shift sequences necessary to restore the initial shift state.<br />
If s is a null pointer, resets the global conversion state and determines whether shift sequences are used. </p>
<h2>Parameters</h2>
<p>s &#8211; pointer to the character array for output<br />
wc &#8211; wide character to convert </p>
<h2>Return value</h2>
<p>If s is not a null pointer, returns the number of bytes that are contained in the multibyte representation of wc or -1 if wc is not a valid character.<br />
If s is a null pointer, resets its internal conversion state to represent the initial shift state and returns 0 if the current multibyte encoding is not state-dependent (does not use shift sequences) or a non-zero value if the current multibyte encoding is state-dependent (uses shift sequences). </p>
<h2>Notes</h2>
<p>Each call to wctomb updates the internal global conversion state (a static object of type std::mbstate_t, only known to this function). If the multibyte encoding uses shift states, this function is not reentrant. In any case, multiple threads should not call wctomb without synchronization: std::wcrtomb may be used instead. </p>
<h2>Example</h2>
<p> // Run this code </p>
<p>&nbsp;<wbr>&nbsp;#include &lt;iostream&gt;<br />
&nbsp;<wbr>&nbsp;#include &lt;clocale&gt;<br />
&nbsp;<wbr>&nbsp;#include &lt;string&gt;<br />
&nbsp;<wbr>&nbsp;#include &lt;cstdlib&gt; </p>
<p>&nbsp;<wbr>&nbsp;void print_wide(const std::wstring&amp; wstr)<br />
&nbsp;<wbr>&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;bool shifts = std::wctomb(nullptr, 0); // reset the conversion state<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::cout &lt;&lt; &quot;shift sequences &quot; &lt;&lt; (shifts ? &quot;are&quot; : &quot;not&quot; ) &lt;&lt; &quot; used
&quot;;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for (wchar_t wc : wstr) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::string mb(MB_CUR_MAX, &#8216;
