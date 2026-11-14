---
title: "cshost(1)"
name: "cshost"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cshost/"
---

<h2>NAMES</h2>
<p> cshost &#8211; Server access control program for canna</p>
<h2>SYNOPSIS</h2>
<p> <code>cshost [{-cs|-cannaserver} </code><i>cannaserver</i>]</p>
<h2>DESCRIPTION</h2>
<p> the <i><a href="/docs/linux/man/1-cshost/">cshost</a></i>(1) prints the list of machines that are allowed to make connections to <i><a href="//www.systutorials.com/docs/linux/man/1M-cannaserver/">cannaserver</a></i>(1M). </p>
<p> <i><a href="//www.systutorials.com/docs/linux/man/1M-cannaserver/">cannaserver</a></i>(1M) allows network connections only from programs running on the same machine or machines listed in the file /etc/hosts.canna. If /etc/hosts.canna does not exist or the file is empty, access is granted to everyone.</p>
<h2>OPTIONS</h2>
<dl>
<dt>-cs <i>cannaserver</i> (or -cannaserver <i>cannaserver</i>)</p>
<dd> Specifies the name of the host under which the Kana-Kanji conversion server is in operation. </p>
</dl>
<h2>Index</h2>
