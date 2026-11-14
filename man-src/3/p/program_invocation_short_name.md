---
title: "program_invocation_short_name(3)"
name: "program_invocation_short_name"
section: "3"
letter: "p"
url: "/docs/linux/man/3-program_invocation_short_name/"
description: "program_invocation_name, program_invocation_short_name – obtain name used to invoke calling program"
---

<p>program_invocation_name, program_invocation_short_name &#8211; obtain name used to invoke calling program</p>
<h2>Synopsis</h2>
<pre><code>#define _GNU_SOURCE /* See feature_test_macros(7) */
#include &lt;errno.h&gt;

extern char *program_invocation_name;
extern char *program_invocation_short_name;</code></pre>
<h2>Description</h2>
<p><i>program_invocation_name</i> contains the name that was used to invoke the calling program. This is the same as the value of <i>argv[0]</i> in <i>main</i>(), with the difference that the scope of <i>program_invocation_name</i> is global. </p>
<p> <i>program_invocation_short_name</i> contains the basename component of name that was used to invoke the calling program. That is, it is the same value as <i>program_invocation_name</i>, with all text up to and including the final slash (/), if any, removed. </p>
<p> These variables are automatically initialized by the glibc run-time startup code.</p>
<h2>Conforming To</h2>
<p>These variables are GNU extensions, and should not be used in programs intended to be portable.</p>
<h2>Notes</h2>
<p>The Linux-specific <i>/proc/[number]/cmdline</i> file provides access to similar information.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-proc/">proc</a></code>(5)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
