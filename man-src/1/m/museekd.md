---
title: "museekd(1)"
name: "museekd"
section: "1"
letter: "m"
url: "/docs/linux/man/1-museekd/"
description: "Museekd – C++ Daemon/Client for Soulseek"
---

<h2>NAME</h2>
<p> <code>Museekd</code> &#8211; C++ Daemon/Client for Soulseek</p>
<h2>SYNOPSIS</h2>
<p> <code>museek</code> [-c &lt;<i>filename</i>&gt;] [&#8211;config &lt;<i>filename</i>&gt;] [-V] [&#8211;version] [-h] [&#8211;help]</p>
<h2>DESCRIPTION</h2>
<p> Museekd is a headless client (daemon) for the Soulseek P2P network and for Soulfind Servers. It is configured with musetup and can be controlled with variety of interfaces and GUIs, such as Museeq and Mucous. It handles any chatting, transferring files, searching, managing of users or browsing of shares requested by the various interfaces or GUIs. </p>
<p> Before running, you will need a configure it with <i><a href="/docs/linux/man/1-musetup/">musetup</a></i>(1).</p>
<h2>OPTIONS</h2>
<p> Museekd accepts the following options:</p>
<dl>
<dt><code>-c &lt;</code><i>filename</i>&gt;, &#8211;config &lt;<i>filename</i>&gt;</dt>
<dd> Use a different config file.</dd>
<dt><code>-V, &#8211;version</code></dt>
<dd> Display Version and exit.</dd>
<dt><code>-d, &#8211;debug</code></dt>
<dd> Show debugging messages.</dd>
<dt><code>-h, &#8211;help</code></dt>
<dd> Display Help and exit. </dd>
</dl>
<h2>EXAMPLE</h2>
<p> To run this program the standard way type: </p>
<p> museekd </p>
<p> Alternativly you use a different config file with: </p>
<p> museekd &#8211;config config.xml</p>
<h2>FILES</h2>
<dl>
<dt>
&nbsp;<wbr><i>~/.museekd/config.xml</i></dt>
<dd> The default location for the <code>museekd</code> config file.</dd></dl>
<h2>AUTHORS</h2>
<p> Hyriand &lt;hyriand [at] thegraveyard.org&gt; </p>
<p> daelstorm &lt;daelstorm [at] gmail.com&gt;</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-mucous/">mucous</a></i>(1) <i><a href="/docs/linux/man/1-mulog/">mulog</a></i>(1) <i><a href="/docs/linux/man/1-murmur/">murmur</a></i>(1) <i><a href="/docs/linux/man/1-muscan/">muscan</a></i>(1) <i><a href="/docs/linux/man/1-muscand/">muscand</a></i>(1) <i><a href="/docs/linux/man/1-museekcontrol/">museekcontrol</a></i>(1) <i><a href="/docs/linux/man/1-museeq/">museeq</a></i>(1) <i><a href="/docs/linux/man/1-musetup/">musetup</a></i>(1) <i><a href="/docs/linux/man/1-musetup-gtk/">musetup-gtk</a></i>(1) </p>
<h2>Index</h2>
