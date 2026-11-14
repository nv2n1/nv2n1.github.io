---
title: "dpkg-preconfigure(8)"
name: "dpkg-preconfigure"
section: "8"
letter: "d"
url: "/docs/linux/man/8-dpkg-preconfigure/"
description: "dpkg-preconfigure – let packages ask questions prior to their installation"
---

<p>dpkg-preconfigure &#8211; let packages ask questions prior to their installation</p>
<h2>Synopsis</h2>
<pre> dpkg-preconfigure [options] package.deb
 dpkg-preconfigure --apt</pre>
<h2>Description</h2>
<p><code>dpkg-preconfigure</code> lets packages ask questions before they are installed. It operates on a set of debian packages, and all packages that use debconf will have their config script run so they can examine the system and ask questions.</p>
<h2>Options</h2>
<dl>
<dt><code>-f</code><i>type</i>, <code>&#8211;frontend=</code><i>type</i></p>
<dd>Select the frontend to use.</p>
<dt><code>-p</code><i>value</i>, <code>&#8211;priority=</code><i>value</i></p>
<dd>Set the lowest priority of questions you are interested in. Any questions with a priority below the selected priority will be ignored and their default answers will be used.</p>
<dt><code>&#8211;terse</code></p>
<dd>Enables terse output mode. This affects only some frontends.</p>
<dt><code>&#8211;apt</code></p>
<dd>Run in apt mode. It will expect to read a set of package filenames from stdin, rather than getting them as parameters. Typically this is used to make apt run dpkg-preconfigure on all packages before they are installed. To do this, add something like this to /etc/apt/apt.conf: </p>
<pre> // Pre-configure all packages before
 // they are installed.
 DPkg::Pre-Install-Pkgs {
 &quot;dpkg-preconfigure --apt --priority=low&quot;;
 };</pre>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>Display usage help.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-debconf/">debconf</a></code>(7)</p>
<h2>Author</h2>
<p>Joey Hess &lt;joeyh [at] debian.org&gt;</p>
