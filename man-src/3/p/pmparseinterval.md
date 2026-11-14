---
title: "pmparseinterval(3)"
name: "pmparseinterval"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pmparseinterval/"
description: "pmParseInterval – convert interval string to timeval structure"
---

<p><code>pmParseInterval</code> &#8211; convert interval string to <code>timeval</code> structure</p>
<h2>C Synopsis</h2>
<p><code> #include &lt;pcp/pmapi.h&gt; </p>
<p> int pmParseInterval(const char *</code><i>string</i>, struct timeval *<i>rslt</i>, char&nbsp;<wbr>**<i>errmsg</i>); </p>
<p> cc &#8230; -lpcp</p>
<h2>Description</h2>
<p><code>pmParseInterval</code> parses the argument <i>string</i> specifying an interval of time and fills in the <code>tv_sec</code> and <code>tv_usec</code> components of the <i>rslt</i> structure to represent that interval. </p>
<p> The input <i>string</i> is most commonly the argument following a <code>-t</code> command line option to a PCP application, and the syntax is fully described in <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1).</p>
<h2>Diagnostics</h2>
<p><code>pmParseInterval</code> returns 0 and <i>errmsg</i> is undefined if the parsing is successful. </p>
<p> If the given <i>string</i> does not conform to the required syntax <code>pmParseInterval</code> returns -1 and a dynamically allocated error message string in <i>errmsg</i>. The error message is terminated with a newline and includes the text of the input <i>string</i> along with an indicator of the position at which the error was detected, e.g.<br />
 <i>4minutes 30mumble</i><br />
 <i> ^ &#8212; unexpected value</i> </p>
<p> In the case of an error, the caller is responsible for calling <code><a href="/docs/linux/man/3-free/">free</a></code>(3) to release the space allocated for <i>errmsg</i>.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1), <code><a href="/docs/linux/man/3-free/">free</a></code>(3), <code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3) and <code><a href="/docs/linux/man/3-pmparsetimewindow/">pmParseTimeWindow</a></code>(3). </p>
