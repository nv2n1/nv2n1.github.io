---
title: "pmisethostname(3)"
name: "pmisethostname"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pmisethostname/"
description: "pmiSetHostname – set the source host name for a LOGIMPORT archive"
---

<p><code>pmiSetHostname</code> &#8211; set the source host name for a LOGIMPORT archive</p>
<h2>C Synopsis</h2>
<p><code> #include &lt;pcp/pmapi.h&gt;<br />
 #include &lt;pcp/impl.h&gt;<br />
 #include &lt;pcp/import.h&gt; </p>
<p> int pmiSetHostname(const char *</code><i>value</i>); </p>
<p> cc &#8230; -lpcp_import -lpcp</p>
<h2>Perl SYNOPSIS</h2>
<p><code> use PCP::LogImport; </p>
<p> pmiSetHostname($</code><i>value</i>);</p>
<h2>Description</h2>
<p>As part of the Performance Co-Pilot Log Import API (see <code><a href="/docs/linux/man/3-logimport/">LOGIMPORT</a></code>(3)), <code>pmiSetHostname</code> sets the source hostname in the current context to be <i>value</i>. </p>
<p> In the absence of a call to <code>pmiSetHostname</code> the source hostname defaults to the hostname of the localhost.</p>
<h2>Diagnostics</h2>
<p><code>pmiSetHostname</code> returns zero on success else a negative value that can be turned into an error message by calling <code><a href="/docs/linux/man/3-pmierrstr/">pmiErrStr</a></code>(3).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-logimport/">LOGIMPORT</a></code>(3), <code><a href="/docs/linux/man/3-pmierrstr/">pmiErrStr</a></code>(3), <code><a href="/docs/linux/man/3-pmisettimezone/">pmiSetTimezone</a></code>(3) and <code><a href="/docs/linux/man/3-pmistart/">pmiStart</a></code>(3). </p>
