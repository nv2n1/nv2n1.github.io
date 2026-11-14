---
title: "pmiusecontext(3)"
name: "pmiusecontext"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pmiusecontext/"
description: "pmiUseContext – change LOGIMPORT context"
---

<p><code>pmiUseContext</code> &#8211; change LOGIMPORT context</p>
<h2>C Synopsis</h2>
<p><code> #include &lt;pcp/pmapi.h&gt;<br />
 #include &lt;pcp/impl.h&gt;<br />
 #include &lt;pcp/import.h&gt; </p>
<p> int pmiUseContext(int </code><i>context</i>); </p>
<p> cc &#8230; -lpcp_import -lpcp</p>
<h2>Perl SYNOPSIS</h2>
<p><code> use PCP::LogImport; </p>
<p> pmiUseContext($</code><i>context</i>);</p>
<h2>Description</h2>
<p>As part of the Performance Co-Pilot Log Import API (see <code><a href="/docs/linux/man/3-logimport/">LOGIMPORT</a></code>(3)), <code>pmiUseContext</code> may be used by applications wishing to generate more than one PCP archive concurrently. </p>
<p> The <i>context</i> argument is a value returned from a previous call to <code><a href="/docs/linux/man/3-pmstart/">pmStart</a></code>(3) and on successful return from <code>pmiUseContext</code>, the current context will have been changed to the one identified by <i>context</i>.</p>
<h2>Diagnostics</h2>
<p><code>pmiUseContext</code> returns zero on success else a negative value that can be turned into an error message by calling <code><a href="/docs/linux/man/3-pmierrstr/">pmiErrStr</a></code>(3).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-logimport/">LOGIMPORT</a></code>(3), <code><a href="/docs/linux/man/3-pmierrstr/">pmiErrStr</a></code>(3) and <code><a href="/docs/linux/man/3-pmistart/">pmiStart</a></code>(3). </p>
