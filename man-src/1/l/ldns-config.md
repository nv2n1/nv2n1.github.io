---

title: "ldns-config(1)"
name: "ldns-config"
section: "1"
letter: "l"
url: "/docs/linux/man/1-ldns-config/"
description: "ldns-config – show compiler and linker flags for ldns usage."
---

<h2>NAME</h2>
<p> ldns-config &#8211; show compiler and linker flags for ldns usage.</p>
<p> <code>ldns-config</code> [ <i>OPTIONS</i> ] </p>
<p> When writing programs using ldns, you have to tell the compiler where to look for include files and what libraries from which location to link to. <code>ldns-config</code> can be used to find out what flags to use with the C compiler and the linker. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;cflags</code></dt>
<dd> Show the C compiler flags needed to compile with ldns </dd>
<dt><code>&#8211;libs</code></dt>
<dd> Show the flags to be used to link with ldns </dd>
<dt><code>&#8211;libs_sec</code></dt>
<dd> Show the flags to be used to link with ldns compiled for secondary architecture. </dd>
<dt><code>&#8211;version</code></dt>
<dd> Shows the version of the installed ldns library </dd>
<dt><code>&#8211;help</code></dt>
<dd> Show <code>ldns-config</code> usage description </dd>
</dl>
<h2>AUTHOR</h2>
<p> Written by the ldns team. </p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;ldns-team [at] nlnetlabs.nl&gt;. </p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2011 NLnet Labs. This is free software. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
