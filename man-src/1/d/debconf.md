---
title: "debconf(1)"
name: "debconf"
section: "1"
letter: "d"
url: "/docs/linux/man/1-debconf/"
description: "debconf – run a debconf-using program"
---

<h2 class="name">NAME</h2>
<p> debconf &#8211; run a debconf-using program </p>
<h2>SYNOPSIS</h2>
<pre><code>
debconf[options] command[args]
</code></pre>
<h2>DESCRIPTION</h2>
<p> Debconf is a configuration system for Debian packages. For a debconf overview and documentation for sysadmins, see <code><a href="/docs/linux/man/7-debconf/">debconf</a></code>(7) (in the debconf-doc package). </p>
<p> The <code>debconf</code> program runs a program under debconf&#8217;s control, setting it up to talk with debconf on stdio. The program&#8217;s output is expected to be debconf protocol commands, and it is expected to read result codes on stdin. See <code><a href="/docs/linux/man/7-debconf-devel/">debconf-devel</a></code>(7) for details about the debconf protocol. </p>
<p> The command to be run under debconf must be specified in a way that will let your <font SIZE="-1">PATH</font> find it. </p>
<p> This command is not the usual way that debconf is used. It&#8217;s more typical for debconf to be used via <code><a href="/docs/linux/man/8-dpkg-preconfigure/">dpkg-preconfigure</a></code>(8) or <code><a href="/docs/linux/man/8-dpkg-reconfigure/">dpkg-reconfigure</a></code>(8).</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-o</code><i>package</i>, <code>&#8211;owner=</code><i>package</i></p>
<dd> Tell debconf what package the command it is running is a part of. This is necessary to get ownership of registered questions right, and to support unregister and purge commands properly.</p>
<dt><code>-f</code><i>type</i>, <code>&#8211;frontend=</code><i>type</i></p>
<dd> Select the frontend to use.</p>
<dt><code>-p</code><i>value</i>, <code>&#8211;priority=</code><i>value</i></p>
<dd> Specify the minimum priority of question that will be displayed.</p>
<dt><code>&#8211;terse</code></p>
<dd> Enables terse output mode. This affects only some frontends.</dl>
<h2>EXAMPLES</h2>
<p> To debug a shell script that uses debconf, you might use: </p>
<pre>
 DEBCONF_DEBUG=developer debconf my-shell-prog
</pre>
<p> Or, you might use this: </p>
<pre>
 debconf --frontend=readline sh -x my-shell-prog
</pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-debconf-devel/">debconf-devel</a></code>(7), <code><a href="/docs/linux/man/7-debconf/">debconf</a></code>(7)</p>
<h2>AUTHOR</h2>
<p> Joey Hess &lt;joeyh [at] debian.org&gt; </p>
<h2>Index</h2>
