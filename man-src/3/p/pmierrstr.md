---
title: "pmierrstr(3)"
name: "pmierrstr"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pmierrstr/"
description: "pmiErrStr – convert a LOGIMPORT error code into a string"
---

<p><code>pmiErrStr</code> &#8211; convert a LOGIMPORT error code into a string</p>
<h2>C Synopsis</h2>
<p><code> #include &lt;pcp/pmapi.h&gt;<br />
 #include &lt;pcp/import.h&gt; </p>
<p> const char *pmiErrStr(int </code><i>code</i>);<br />
 char *pmiErrStr_r(int <i>code</i>, char <i>buf</i>, int <i>buflen</i>); </p>
<p> cc &#8230; -lpcp_import -lpcp</p>
<h2>Perl SYNOPSIS</h2>
<p><code> use PCP::LogImport; </p>
<p> pmiErrStr($</code><i>code</i>);</p>
<h2>Description</h2>
<p>As part of the Performance Co-Pilot Log Import API (see <code><a href="/docs/linux/man/3-logimport/">LOGIMPORT</a></code>(3)), <code>pmiErrStr</code> translates error codes returned from the other routines in the Log Import library into printable error messages. </p>
<p> <i>code</i> would normally have a negative value. As a special case, if <i>code</i> is -1 then the error code returned from the last routine called in the LOGIMPORT library for this context will be used. </p>
<p> The <code>pmiErrStr_r</code> function does the same, but stores the result in a user-supplied buffer <i>buf</i> of length <i>buflen</i>, which should have room for at least <code>PMI_MAXERRMSGLEN</code> bytes. </p>
<p> The set of possible error codes and messages is all those defined by <code><a href="/docs/linux/man/3-pmerrstr/">pmErrStr</a></code>(3) and <code><a href="/docs/linux/man/3-pcpintro/">PCPIntro</a></code>(3), plus the additonal ones defined in <code>&lt;pcp/import.h&gt;</code> with error code names of the form <code>PMI_ERR_&#8230;.</code></p>
<h2>Diagnostics</h2>
<p>None.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-logimport/">LOGIMPORT</a></code>(3), <code><a href="/docs/linux/man/3-pcpintro/">PCPIntro</a></code>(3) and <code><a href="/docs/linux/man/3-pmerrstr/">pmErrStr</a></code>(3). </p>
