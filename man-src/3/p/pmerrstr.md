---
title: "pmerrstr(3)"
name: "pmerrstr"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pmerrstr/"
description: "pmErrStr, pmErrStr_r – convert a PMAPI error code into a string"
---

<p><code>pmErrStr</code>, <code>pmErrStr_r</code> &#8211; convert a PMAPI error code into a string</p>
<h2>C Synopsis</h2>
<p><code> #include &lt;pcp/pmapi.h&gt; </p>
<p> const char *pmErrStr(int </code><i>code</i>);<br />
 char *pmErrStr_r(int <i>code</i>, char *<i>buf</i>, int <i>buflen</i>); </p>
<p> cc &#8230; -lpcp</p>
<h2>Description</h2>
<p>Translate an error code into a text string, suitable for generating a diagnostic message. The <code>pmErrStr_r</code> function does the same, but stores the result in a user-supplied buffer <i>buf</i> of length <i>buflen</i>, which should have room for at least <code>PM_MAXERRMSGLEN</code> bytes. </p>
<p> By convention, all error codes are negative. The small values are assumed to be negated versions of the Unix error codes as defined in <code>&lt;errno.h&gt;</code> and the strings returned are as per <code><a href="/docs/linux/man/3-strerror/">strerror</a></code>(3). The larger, negative error codes are Performance Metrics Application Programming Interface (PMAPI) error conditions and <code><a href="/docs/linux/man/3-pmerrstr/">pmErrStr</a></code>(3) returns an appropriate PMAPI error string, as determined by <i>code</i>.</p>
<h2>Notes</h2>
<p><code>pmErrStr</code> returns a pointer to a static buffer, so the returned value is only valid until the next call to <code>pmErrStr</code> and hence is not thread-safe. Multi-threaded applications should use <code>pmErrStr_r</code> instead.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-pmerr/">pmerr</a></code>(1), <code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3) and <code><a href="/docs/linux/man/3-perror/">perror</a></code>(3). </p>
