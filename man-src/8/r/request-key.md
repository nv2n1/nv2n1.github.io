---
title: "request-key(8)"
name: "request-key"
section: "8"
letter: "r"
url: "/docs/linux/man/8-request-key/"
description: "request-key – Handle key instantiation callback requests from the kernel"
---

<p>request-key &#8211; Handle key instantiation callback requests from the kernel</p>
<h2>Synopsis</h2>
<p><code>/sbin/request-key </code>&lt;op&gt; &lt;key&gt; &lt;uid&gt; &lt;gid&gt; &lt;threadring&gt; &lt;processring&gt; <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>&lt;sessionring&gt; [&lt;info&gt;]</p>
<h2>Description</h2>
<p>This program is invoked by the kernel when the kernel is asked for a key that it doesn&#8217;t have immediately available. The kernel creates a partially set up key and then calls out to this program to instantiate it. It is not intended to be called directly.</p>
<h2>Errors</h2>
<p>All errors will be logged to the syslog.</p>
<h2>Files</h2>
<p>/etc/request-key.conf Instantiation handler configuration file. </p>
<p> /etc/request-key.d/&lt;keytype&gt;.conf Keytype specific configuration file.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-keyctl/">keyctl</a></code>(1), <code><a href="/docs/linux/man/5-request-key-conf/">request-key.conf</a></code>(5) </p>
