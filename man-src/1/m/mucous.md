---
title: "mucous(1)"
name: "mucous"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mucous/"
description: "Mucous – Python / Curses client for museek"
---

<h2>NAME</h2>
<p> <code>Mucous</code> &#8211; Python / Curses client for museek</p>
<h2>SYNOPSIS</h2>
<p> <code>mucous </code> [-c &lt;<i>filename</i>&gt;] [&#8211;config &lt;<i>filename</i>&gt;] [-l &lt;<i>directory</i>&gt;] [&#8211;log &lt;<i>directory</i>&gt;] [-v] [&#8211;version] [-h] [&#8211;help]</p>
<h2>DESCRIPTION</h2>
<p> Mucous provides a interface for the Museek Daemon for chatting, transferring files, managing users and browsing shares on the Soulseek P2P network and Soulfind Servers. </p>
<p> You will need a configured <i><a href="/docs/linux/man/1-museekd/">museekd</a></i>(1).</p>
<h2>OPTIONS</h2>
<p> Mucous accepts the following options:</p>
<dl>
<dt><code>-c &lt;</code><i>filename</i>&gt;, &#8211;config &lt;<i>filename</i>&gt;</p>
<dd> Use a different config file.</p>
<dt><code>-l &lt;</code><i>directory</i>&gt;, &#8211;log &lt;<i>directory</i>&gt;</p>
<dd> Use a different chat log directory.</p>
<dt><code>-v, &#8211;version</code></p>
<dd> Display Version and exit.</p>
<dt><code>-h, &#8211;help</code></p>
<dd> Display Help and exit. </p>
</dl>
<h2>EXAMPLE</h2>
<p> To run this program the standard way type: </p>
<p> mucous </p>
<p> Alternativly you use a different config file with: </p>
<p> mucous &#8211;config config </p>
<p> Or a different chat logging directory with: </p>
<p> mucous &#8211;log logdir</p>
<h2>ENVIRONMENTAL VARIABLES</h2>
<dl>
<dt><code>TERM</code></p>
<dd> Specifies the type of Terminal; changes the way mucous displays color.</dl>
<p> For XTerm: xterm-color </p>
<p> For aterm or rxvt: rxvt </p>
<p> For urxvt: rxvt-unicode</p>
<h2>FILES</h2>
<dl>
<dt>
&nbsp;<wbr><i>~/.mucous/config</i></p>
<dd> The default location for the <code>mucous</code> config file.</p>
<dt>
&nbsp;<wbr><i>~/.mucous/logs/</i></p>
<dd> The default directory for chat logs.</p>
<dt>
&nbsp;<wbr><i>~/.mucous/logs/room/</i></p>
<dd> The directory where chat room logs are stored.</p>
<dt>
&nbsp;<wbr><i>~/.mucous/logs/private/</i></p>
<dd> The directory where private chat logs are stored.</p>
<dt>
&nbsp;<wbr><i>~/.mucous/$USER.image</i></p>
<dd> The file where a user&#8217;s userinfo image is saved.</dl>
<h2>AUTHORS</h2>
<p> daelstorm &lt;daelstorm [at] gmail.com&gt;</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-mulog/">mulog</a></i>(1) <i><a href="/docs/linux/man/1-murmur/">murmur</a></i>(1) <i><a href="/docs/linux/man/1-muscan/">muscan</a></i>(1) <i><a href="/docs/linux/man/1-muscand/">muscand</a></i>(1) <i><a href="/docs/linux/man/1-museekcontrol/">museekcontrol</a></i>(1) <i><a href="/docs/linux/man/1-museekd/">museekd</a></i>(1) <i><a href="/docs/linux/man/1-museeq/">museeq</a></i>(1) <i><a href="/docs/linux/man/1-musetup/">musetup</a></i>(1) <i><a href="/docs/linux/man/1-musetup-gtk/">musetup-gtk</a></i>(1) </p>
<h2>Index</h2>
