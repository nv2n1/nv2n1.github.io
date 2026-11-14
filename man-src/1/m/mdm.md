---
title: "mdm(1)"
name: "mdm"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mdm/"
description: "MDM – The MDM Display Manager"
---

<h2 class="name">NAME</h2>
<p> MDM &#8211; The MDM Display Manager </p>
<h2>SYNOPSIS</h2>
<p> <code>mdm [options]</code><br />
 <code>mdmsetup [options]</code></p>
<h2>DESCRIPTION</h2>
<p> MDM is a replacement for XDM, the X Display Manager. Unlike its competitors (X3DM, KDM, WDM) MDM was written from scratch and does not contain any original XDM / X Consortium code. MDM runs and manages the X servers for both local and remote logins (using XDMCP). See <a rel="nofollow" href="http://www.gnome.org/projects/mdm/">http://www.gnome.org/projects/mdm/</a> for more details. </p>
<p> <code>mdm</code> is main executable. <code>mdmsetup</code> is a graphical tool for easily changing the most commonly used options. </p>
<p> For full documentation see the GNOME help browser under the <code>Applications / System Tools</code> section.</p>
<h2>OPTIONS</h2>
<p> <code>mdm</code> and thus also <code>mdm</code> accept the following options:</p>
<dl>
<dt><code>-nodaemon</code></p>
<dd> Do not fork into the background</p>
<dt><code>&#8211;no-console</code></p>
<dd> No console (local) servers to be run</p>
<dt><code>&#8211;preserve-ld-vars</code></p>
<dd> Preserve LD_* variables</p>
<dt><code>&#8211;version</code></p>
<dd> Print the MDM version</p>
<dt><code>&#8211;help</code></p>
<dd> Print simple description of accepted options</dl>
<p> <code>mdmsetup</code> accepts all standard GNOME options.</p>
<h2>CONFIGURATION</h2>
<p> Configuration is done either by running <code>mdmsetup</code> or by editting the /etc/X11/mdm/mdm.conf (usually, could also be /etc/mdm/mdm.conf) file. The graphical tool does not support all the options possible so editting the configuration file is sometimes necessary.</p>
<h2>AUTHOR</h2>
<p> <code>MDM</code> is being written and maintained by George (Jiri) Lebl &lt;jirka [at] 5z.com&gt; based on the original codebase by Martin K. Peterson &lt;mkp [at] mkp.net&gt;.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="//www.systutorials.com/docs/linux/man/7x-X/">X</a></code>(7x), <code><a href="/docs/linux/man/1-xdm/">xdm</a></code>(1), <code><a href="//www.systutorials.com/docs/linux/man/7x-Xsecurity/">Xsecurity</a></code>(7x), <code><a href="/docs/linux/man/1-xserver/">Xserver</a></code>(1), </p>
<h2>Index</h2>
