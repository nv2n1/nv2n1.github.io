---
title: "esd-config(1)"
name: "esd-config"
section: "1"
letter: "e"
url: "/docs/linux/man/1-esd-config/"
description: "esd-config – The Enlightened Sound Daemon"
---

<h2 class="name">NAME</h2>
<p> esd-config &#8211; The Enlightened Sound Daemon </p>
<h2>DESCRIPTION</h2>
<p> esd-config is a tool that is used to configure to determine the compiler and linker flags that should be used to compile and link programs that use EsounD. It is also used internally to the .m4 macros for <font SIZE="-1">GNU</font> autoconf that are included with EsounD.</p>
<h2>USAGE</h2>
<p> esd-config [&#8211;prefix[=DIR]] [&#8211;exec-prefix[=DIR]] [&#8211;version] [&#8211;libs] [&#8211;cflags] </p>
<p> <code>&#8212;version</code> Print the currently installed version of EsounD on the standard output. </p>
<p> <code>&#8212;libs</code> Print the linker flags that are necessary to link an EsounD program. </p>
<p> <code>&#8212;cflags</code> Print the compiler flags that are necessary to compile an EsounD program. </p>
<p> <code>&#8212;prefix=PREFIX</code> If specified, use <font SIZE="-1">PREFIX</font> instead of the installation prefix that EsounD was built with when computing the output for the &#8211;cflags and &#8211;libs options. This option is also used for the exec prefix if &#8211;exec-prefix was not specified. This option must be specified before any &#8211;libs or &#8211;cflags options. </p>
<p> <code>&#8212;exec-prefix=PREFIX</code> If specified, use <font SIZE="-1">PREFIX</font> instead of the installation exec prefix that EsounD was built with when computing the output for the &#8211;cflags and &#8211;libs options. This option must be specified before any &#8211;libs or &#8211;cflags options.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-esd/">esd</a></i>(1), <i><a href="/docs/linux/man/1-esdcat/">esdcat</a></i>(1), <i><a href="/docs/linux/man/1-esddsp/">esddsp</a></i>(1), <i><a href="/docs/linux/man/1-esdloop/">esdloop</a></i>(1), <i><a href="/docs/linux/man/1-esdplay/">esdplay</a></i>(1), <i><a href="/docs/linux/man/1-esdsample/">esdsample</a></i>(1), <i><a href="/docs/linux/man/1-esdctl/">esdctl</a></i>(1), <i><a href="/docs/linux/man/1-esdfilt/">esdfilt</a></i>(1), <i><a href="/docs/linux/man/1-esdmon/">esdmon</a></i>(1), <i><a href="/docs/linux/man/1-esdrec/">esdrec</a></i>(1) </p>
<h2>Index</h2>
