---
title: "nodeusers(1)"
name: "nodeusers"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nodeusers/"
description: "nodeusers – LinuxNode user information lookup program"
---

<h2>NAME</h2>
<p> nodeusers &#8211; LinuxNode user information lookup program</p>
<h2>SYNOPSIS</h2>
<p> <code>nodeusers [-a] [-i] [-l]</code></p>
<h2>DESCRIPTION</h2>
<p> <code>Nodeusers </code> displays information about current LinuxNode users.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a</code></p>
<dd> Tells nodeusers to use a plain &lt;CR&gt; as end-of-line. This is usefull if nodeusers is called from ax25d.</p>
<dt><code>-i</code></p>
<dd> Tells nodeusers to use a &lt;CR&gt;&lt;LF&gt; pair as end-of-line sequence and also to wait for one line of input before sending the user data. This should be used if nodeusers is used in an internet environment (eg. as a fingerd replacement). The received line is ignored.</p>
<dt><code>-l</code></p>
<dd> Enables logging of errors to the system logging facility.</dl>
<h2>FILES</h2>
<dl>
<dt><code>/var/ax25/node/loggedin</code></p>
<dd> Database of current users.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-node/">node</a></code>(8)</p>
<h2>AUTHOR</h2>
<p> Tomi Manninen OH2BNS &lt;tpmannin [at] cc.hut.fi&gt; </p>
<h2>Index</h2>
