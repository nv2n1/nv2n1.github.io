---
title: "murmur(1)"
name: "murmur"
section: "1"
letter: "m"
url: "/docs/linux/man/1-murmur/"
description: "Murmur – PyGTK2 client for museek"
---

<h2>NAME</h2>
<p> <code>Murmur</code> &#8211; PyGTK2 client for museek</p>
<h2>SYNOPSIS</h2>
<p> <code>murmur</code> [-c &#8211;config &lt;<i>filename</i>&gt;] [-l &#8211;log &lt;<i>directory</i>&gt;] [-v] [&#8211;version] [-d] [-h] [&#8211;help]</p>
<h2>DESCRIPTION</h2>
<p> Murmur provides a GTK2 interface for the Museek Daemon for chatting, transferring files, managing users, viewing user info and browsing shares on the Soulseek P2P network and Soulfind Servers. </p>
<p> You will need a configured and running <i><a href="/docs/linux/man/1-museekd/">museekd</a></i>(1).</p>
<h2>OPTIONS</h2>
<p> Murmur accepts the following options:</p>
<dl>
<dt><code>-c &lt;</code><i>filename</i>&gt;, &#8211;config &lt;<i>filename</i>&gt;</dt>
<dd> Use a different config file.</dd>
<dt><code>-l &lt;</code><i>directory</i>&gt;, &#8211;log &lt;<i>directory</i>&gt;</dt>
<dd> Use a different chat log directory.</dd>
<dt><code>-v, &#8211;version</code></dt>
<dd> Display Version and exit.</dd>
<dt><code>-d</code></dt>
<dd> Display debug messages while running.</dd>
<dt><code>-h, &#8211;help</code></dt>
<dd> Display Help and exit. </dd>
</dl>
<h2>EXAMPLE</h2>
<p> To run this program the standard way type: </p>
<p> murmur </p>
<p> Alternativly you use a different config file with: </p>
<p> murmur &#8211;config config </p>
<p> Or a different chat logging directory with: </p>
<p> murmur &#8211;log logdir</p>
<h2>FILES</h2>
<dl>
<dt>
&nbsp;<wbr><i>~/.murmur/config</i></dt>
<dd> The default location for the <code>mucous</code> config file.</dd>
<dt>
&nbsp;<wbr><i>~/.murmur/logs/</i></dt>
<dd> The default directory for chat logs.</dd>
<dt>
&nbsp;<wbr><i>~/.murmur/logs/room/</i></dt>
<dd> The directory where chat room logs are stored.</dd>
<dt>
&nbsp;<wbr><i>~/.murmur/logs/private/</i></dt>
<dd> The directory where private chat logs are stored.</dd>
<dt>
&nbsp;<wbr><i>~/.murmur/$USER.$EXT</i></dt>
<dd> The file where a user&#8217;s userinfo image is saved.</dd></dl>
<h2>AUTHORS</h2>
<p> daelstorm &lt;daelstorm [at] gmail.com&gt;</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-mulog/">mulog</a></i>(1) <i><a href="/docs/linux/man/1-muscan/">muscan</a></i>(1) <i><a href="/docs/linux/man/1-muscand/">muscand</a></i>(1) <i><a href="/docs/linux/man/1-museekcontrol/">museekcontrol</a></i>(1) <i><a href="/docs/linux/man/1-museekd/">museekd</a></i>(1) <i><a href="/docs/linux/man/1-museeq/">museeq</a></i>(1) <i><a href="/docs/linux/man/1-musetup/">musetup</a></i>(1) <i><a href="/docs/linux/man/1-musetup-gtk/">musetup-gtk</a></i>(1) </p>
