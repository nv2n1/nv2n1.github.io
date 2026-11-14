---
title: "strtoul(3)"
name: "strtoul"
section: "3"
letter: "s"
url: "/docs/linux/man/3-strtoul/"
description: "strtoul, strtoull, strtouq – convert a string to an unsigned long integer"
---

<p>strtoul, strtoull, strtouq &#8211; convert a string to an unsigned long integer</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;stdlib.h&gt;

unsigned long strtoul(const char *nptr, char **endptr, int base);

unsigned long long strtoull(const char *nptr, char **endptr,
                            int base);</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): <code>strtoull</code>():</p>
<dl>
<dd>_ISOC99_SOURCE ||<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_SVID_SOURCE ||&nbsp;_BSD_SOURCE</dl>
<h2>Description</h2>
<p>The <code>strtoul</code>() function converts the initial part of the string in <i>nptr</i> to an <i>unsigned long</i> value according to the given <i>base</i>, which must be between 2 and 36 inclusive, or be the special value 0. </p>
<p> The string may begin with an arbitrary amount of white space (as determined by <code><a href="/docs/linux/man/3-isspace/">isspace</a></code>(3)) followed by a single optional &#8216;+&#8217; or &#8216;-&#8216; sign. If <i>base</i> is zero or 16, the string may then include a &quot;0x&quot; prefix, and the number will be read in base 16; otherwise, a zero <i>base</i> is taken as 10 (decimal) unless the next character is &#8216;0&#8217;, in which case it is taken as 8 (octal). </p>
<p> The remainder of the string is converted to an <i>unsigned long</i> value in the obvious manner, stopping at the first character which is not a valid digit in the given base. (In bases above 10, the letter &#8216;A&#8217; in either uppercase or lowercase represents 10, &#8216;B&#8217; represents 11, and so forth, with &#8216;Z&#8217; representing 35.) </p>
<p> If <i>endptr</i> is not NULL, <code>strtoul</code>() stores the address of the first invalid character in <i>*endptr</i>. If there were no digits at all, <code>strtoul</code>() stores the original value of <i>nptr</i> in <i>*endptr</i> (and returns 0). In particular, if <i>*nptr</i> is not &#8216;
