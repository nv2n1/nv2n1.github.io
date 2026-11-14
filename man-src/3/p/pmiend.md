---
title: "pmiend(3)"
name: "pmiend"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pmiend/"
description: "pmiEnd – finish up a LOGIMPORT archive"
---

<p><code>pmiEnd</code> &#8211; finish up a LOGIMPORT archive</p>
<h2>C Synopsis</h2>
<p><code> #include &lt;pcp/pmapi.h&gt;<br />
 #include &lt;pcp/impl.h&gt;<br />
 #include &lt;pcp/import.h&gt; </p>
<p> int pmiEnd(void); </p>
<p> cc &#8230; -lpcp_import -lpcp </code></p>
<h2>Perl SYNOPSIS</h2>
<p><code> use PCP::LogImport; </p>
<p> pmiEnd(); </code></p>
<h2>Description</h2>
<p>As part of the Performance Co-Pilot Log Import API (see <code><a href="/docs/linux/man/3-logimport/">LOGIMPORT</a></code>(3)), <code>pmiEnd</code> closes the current context, forcing the trailer records to be written to the PCP archive files, and then these files are closed. </p>
<p> In normal operations, an application would include a call to <code>pmiEnd</code> at the end of processing for each context created with a call to <code><a href="/docs/linux/man/3-pmistart/">pmiStart</a></code>(3).</p>
<h2>Diagnostics</h2>
<p><code>pmiEnd</code> returns zero on success else a negative value that can be turned into an error message by calling <code><a href="/docs/linux/man/3-pmierrstr/">pmiErrStr</a></code>(3).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-logimport/">LOGIMPORT</a></code>(3) and <code><a href="/docs/linux/man/3-pmistart/">pmiStart</a></code>(3). </p>
