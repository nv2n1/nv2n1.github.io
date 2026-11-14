---
title: "tsocks(1)"
name: "tsocks"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tsocks/"
description: "tsocks – Shell wrapper to simplify the use of the"
---

<h2 class="name">NAME</h2>
<p> <code>tsocks</code> &#8211; Shell wrapper to simplify the use of the </p>
<p><a href="/docs/linux/man/8-tsocks/">tsocks</a>(8) library to transparently allow an application to use a SOCKS proxy</p>
<h2>SYNOPSIS</h2>
<p> <code>tsocks</code> [application&nbsp;<wbr>[application&#8217;s arguments]]<br />
 or <code>tsocks</code> [on|off]<br />
 or <code>tsocks</code></p>
<h2>DESCRIPTION</h2>
<p> <code>tsocks</code> is a wrapper between the tsocks library and the application what you would like to run socksified.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>[application&nbsp;<wbr>[application&#8217;s arguments]]</p>
<dd> run the application as specified with the environment (LD_PRELOAD) set such that <a href="/docs/linux/man/8-tsocks/">tsocks</a>(8) will transparently proxy SOCKS connections in that program</p>
<dt>[on|off]</p>
<dd> this option adds or removes <a href="/docs/linux/man/8-tsocks/">tsocks</a>(8) from the LD_PRELOAD environment variable. When <a href="/docs/linux/man/8-tsocks/">tsocks</a>(8) is in this variable all executed applications are automatically socksified. If you want to use this function, you HAVE to source the shell script from yours, like this: &quot;source /usr/bin/tsocks&quot; or &quot;. /usr/bin/tsocks&quot;<br />
 Example:<br />
 &quot;. tsocks on&quot; &#8212; add the tsocks lib to LD_PRELOAD<br />
 &quot;. tsocks off&quot; &#8212; remove the tsocks lib from LD_PRELOAD</p>
<dt>[show|sh]</p>
<dd> show the current value of the LD_PRELOAD variable</p>
<dt>&lt;without any argument&gt;</p>
<dd> create a new shell with LD_PRELOAD including <a href="/docs/linux/man/8-tsocks/">tsocks</a>(8).</dl>
<p> </code></p>
<h2>AUTHOR</h2>
<p> This script was created by Tamas SZERB &lt;toma [at] rulez.org&gt; for the debian package of tsocks. It (along with this manual page) have since been adapted into the main tsocks project and modified. </p>
<h2>Index</h2>
