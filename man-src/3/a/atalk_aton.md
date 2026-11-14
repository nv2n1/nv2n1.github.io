---
title: "atalk_aton(3)"
name: "atalk_aton"
section: "3"
letter: "a"
url: "/docs/linux/man/3-atalk_aton/"
description: "atalk_aton – AppleTalk address parsing"
---

<h2 class="name">NAME</h2>
<p> atalk_aton &#8211; AppleTalk address parsing </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;netatalk/at.h&gt;
#include &lt;sys/types.h&gt;
</code></pre>
<dl>
<dt> <code>atalk_aton(char&nbsp;<wbr>*&nbsp;<wbr></code><i>cp</i><code>, struct at_addr&nbsp;<wbr>*&nbsp;<wbr></code><i>ata</i><code>);</code></dl>
<h2>DESCRIPTION</h2>
<dd>The <code>atalk_aton()</code> routine converts an ASCII representation of an AppleTalk address to a format appropriate for system calls. Acceptable ASCII representations include both hex and base 10, in triples or doubles. For instance, the address `0x1f6b.77&#8242; has a network part of `8043&#8242; and a node part of `119&#8242;. This same address could be written `8043.119&#8242;, `31.107.119&#8242;, or `0x1f.6b.77&#8242;. If the address is in hex and the first digit is one of `A-F&#8217;, a leading `0x&#8217; is redundant.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/4-atalk/">atalk</a></code>(4). </p>
<h2>Index</h2>
