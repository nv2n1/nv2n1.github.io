---
title: "dh_dkms(1)"
name: "dh_dkms"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dh_dkms/"
description: "dh_dkms – correctly handle DKMS usage by a kernel module package"
---

<h2 class="name">NAME</h2>
<p> dh_dkms &#8211; correctly handle DKMS usage by a kernel module package </p>
<h2>SYNOPSIS</h2>
<p> <code>dh_dkms</code> [<i>debhelper options</i>] [<code>-l</code>] [<code>-V</code>[<i>version</i>]] [<code>&#8212;</code>&nbsp;<i>file</i>]</p>
<h2>DESCRIPTION</h2>
<p> dh_dkms is a debhelper program that is responsible for correctly setting postinst, postrm and dependencies in kernel module packages using <font SIZE="-1">DKMS</font>. </p>
<p> If a file named debian/package.dkms exists, then different actions are performed, depending on its contents.</p>
<h2>FILES</h2>
<dl>
<dt>debian/<i>package</i>.dkms</p>
<dd>
<dt>debian/dkms</p>
<dd> It can be a proper configuration file, and in this case it would be installed in the proper directory as dkms.conf. </p>
<p> It can also point to another file (this should be used when the configuration is provided by upstream), and in this case that file will be installed as dkms.conf in the proper directory. </p>
<p> This file can only miss if a filename is provided when calling dh_dkms.</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-l</code>, <code>&#8211;legacy</code></p>
<dd> Add code to also support <font SIZE="-1">DKMS</font> versions &lt; 2.1.0.0.</p>
<dt><code>-V</code>, <code>-V</code> <i>version</i></p>
<dd> If <tt>&quot;PACKAGE_VERSION&quot;</tt> in <i>dkms.conf</i> is set to <tt>&quot;#MODULE_VERSION#&quot;</tt>, set it to the given <i>version</i> or, if none is given, default to the upstream version of the current package. Otherwise, leave the value specified in <i>dkms.conf</i>.</p>
<dt><code>&#8212;</code> <i>file</i></p>
<dd> Don&#8217;t look for debian/<i>package</i>.dkms or debian/dkms, but install <i>file</i> as dkms.conf.</dl>
<h2>NOTES</h2>
<p> Note that this command is not idempotent. <i><a href="/docs/linux/man/1-dh_prep/">dh_prep</a></i>(1) should be called between invocations of this command. Otherwise, it may cause multiple instances of the same text to be added to maintainer scripts. </p>
<p> IMPORTANT: binary packages using dh_dkms must have a name that ends in &#8216;-dkms&#8217;.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-debhelper/">debhelper</a></i>(1) </p>
<p> This program is part of the Debian <font SIZE="-1">DKMS</font> package. </p>
<p> <i><a href="/docs/linux/man/8-dkms/">dkms</a></i>(8)</p>
<h2>AUTHOR</h2>
<p> David Paleino &lt;dapal [at] debian.org&gt; </p>
<h2>Index</h2>
