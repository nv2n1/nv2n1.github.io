---
title: "dh_suidregister(1)"
name: "dh_suidregister"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dh_suidregister/"
description: "dh_suidregister – suid registration program (deprecated)"
---

<h2 class="name">NAME</h2>
<p> dh_suidregister &#8211; suid registration program (deprecated) </p>
<h2>SYNOPSIS</h2>
<p> Do not run!</p>
<h2>DESCRIPTION</h2>
<p> This program used to register suid and sgid files with <i><a href="/docs/linux/man/1-suidregister/">suidregister</a></i>(1), but with the introduction of <i><a href="/docs/linux/man/8-dpkg-statoverride/">dpkg-statoverride</a></i>(8), registration of files in this way is unnecessary, and even harmful, so this program is deprecated and should not be used.</p>
<h2>CONVERTING TO STATOVERRIDE</h2>
<p> Converting a package that uses this program to use the new statoverride mechanism is easy. Just remove the call to <code>dh_suidregister</code> from <i>debian/rules</i>, and add a versioned conflicts into your <i>control</i> file, as follows: </p>
<pre>
  Conflicts: suidmanager (&lt;&lt; 0.50)
</pre>
<p> The conflicts is only necessary if your package used to register things with suidmanager; if it did not, you can just remove the call to this program from your rules file.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/7-debhelper/">debhelper</a></i>(7) </p>
<p> This program is a part of debhelper.</p>
<h2>AUTHOR</h2>
<p> Joey Hess &lt;joeyh [at] debian.org&gt; </p>
<h2>Index</h2>
