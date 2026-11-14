---
title: "stap-prep(1)"
name: "stap-prep"
section: "1"
letter: "s"
url: "/docs/linux/man/1-stap-prep/"
description: "stap-prep – prepare system for systemtap use"
---

<h2>NAME</h2>
<p> stap-prep &#8211; prepare system for systemtap use </p>
<h2>SYNOPSIS</h2>
<p> <code>stap-prep</code> [ <i>KERNEL_VERSION</i> ] </p>
<h2>DESCRIPTION</h2>
<p> The stap-prep executable prepares the system for systemtap use by installing kernel headers, debug symbols and build tools that match the currently running kernel or optionally the kernel version given by the user. </p>
<p> The exact behavior of stap-prep may be customized by the distribution maintainers. It might for example only give suggestions and not actually install the required packages if that is difficult to automate. </p>
<h2>EXAMPLES</h2>
<dl>
<dt>
<dd>
<pre>
$ stap-prep
Please install linux-image-3.2.0-2-amd64-dbg
</pre>
</dl>
<h2>SEE ALSO</h2>
<pre>
<i><a href="//www.systutorials.com/docs/linux/man/1-stap/">stap</a></i>(1)
</pre>
<h2>BUGS</h2>
<p> Use the Bugzilla link of the project web page or our mailing list. <code><a rel="nofollow" href="http://sourceware.org/systemtap/">http://sourceware.org/systemtap/</a></code>,<code>&lt;systemtap [at] sourceware.org&gt;</code>. </p>
<h2>Index</h2>
