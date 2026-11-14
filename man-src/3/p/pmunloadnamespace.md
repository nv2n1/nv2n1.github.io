---
title: "pmunloadnamespace(3)"
name: "pmunloadnamespace"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pmunloadnamespace/"
description: "pmUnloadNameSpace – unload a local performance metrics name space for an application"
---

<p><code>pmUnloadNameSpace</code> &#8211; unload a local performance metrics name space for an application</p>
<h2>C Synopsis</h2>
<p><code> #include &lt;pcp/pmapi.h&gt; </p>
<p> void pmUnloadNameSpace(void); </p>
<p> cc &#8230; -lpcp </code></p>
<h2>Description</h2>
<p>If one has previously loaded a local Name Space using <code><a href="/docs/linux/man/3-pmloadnamespace/">pmLoadNameSpace</a></code>(3) or <code><a href="/docs/linux/man/3-pmloadasciinamespace/">pmLoadASCIINameSpace</a></code>(3), then calling <code><a href="/docs/linux/man/3-pmunloadnamespace/">pmUnloadNameSpace</a></code>(3) will free up the memory associated with the Name Space and force all subsequent PMNS routine calls to use the distributed PMNS. If <code><a href="/docs/linux/man/3-pmunloadnamespace/">pmUnloadNameSpace</a></code>(3) is called before calling <code><a href="/docs/linux/man/3-pmloadnamespace/">pmLoadNameSpace</a></code>(3) or <code><a href="/docs/linux/man/3-pmloadasciinamespace/">pmLoadASCIINameSpace</a></code>(3), then it will effectively do nothing.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3), <code><a href="/docs/linux/man/3-pmloadasciinamespace/">pmLoadASCIINameSpace</a></code>(3), <code><a href="/docs/linux/man/3-pmloadnamespace/">pmLoadNameSpace</a></code>(3) and <code><a href="/docs/linux/man/5-pmns/">pmns</a></code>(5). </p>
