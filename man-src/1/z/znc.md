---
title: "znc(1)"
name: "znc"
section: "1"
letter: "z"
url: "/docs/linux/man/1-znc/"
description: "znc – An advanced IRC bouncer"
---

<h2>NAME</h2>
<p> znc &#8211; An advanced IRC bouncer</p>
<h2>SYNOPSIS</h2>
<p> <code>znc &#8211;help</code><br />
 <code>znc &#8211;version</code><br />
 <code>znc &#8211;makepass</code><br />
 <code>znc</code> [<code>-n</code>] [<code>-d</code> <i>datadir</i>] [<code>-D</code>] [<code>-f</code>]<br />
 <code>znc</code> [<code>-n</code>] [<code>-d</code> <i>datadir</i>] [<code>-D</code>] [<code>-f</code>] <code>&#8211;makeconf</code><br />
 <code>znc</code> [<code>-n</code>] [<code>-d</code> <i>datadir</i>] [<code>-D</code>] [<code>-f</code>] <code>&#8211;makepem</code></p>
<h2>DESCRIPTION</h2>
<p> <code>znc</code> is an IRC proxy. It runs as a daemon and connects to IRC server, then allows you to connect from a workstation and work as the user that is logged in to the IRC server. After you disconnect, it maintains the connection to the server. It acts like any normal IRC server, so you can use any IRC client to connect to it.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Output a brief help message.</p>
<dt><code>-v</code>, <code>&#8211;version</code></p>
<dd> Show the full version number.</p>
<dt><code>-n</code>, <code>&#8211;no-color</code></p>
<dd> Don&#8217;t use any color escape sequences.</p>
<dt><code>-f</code>, <code>&#8211;foreground</code></p>
<dd> Don&#8217;t fork the ZNC process into the background.</p>
<dt><code>-D</code>, <code>&#8211;debug</code></p>
<dd> Print debug output to the console. Implies <code>&#8211;foreground</code>.</p>
<dt><code>-d</code><i> DATADIR</i>, &#8211;datadir=<i>DATADIR</i></p>
<dd> Specify another datadir. This is where <code>znc</code> saves everything.</p>
<dt><code>-c</code>, <code>&#8211;makeconf</code></p>
<dd> Interactively create a new configuration.</p>
<dt><code>-s</code>, <code>&#8211;makepass</code></p>
<dd> Hash a password for use in <i>znc.conf</i>.</p>
<dt><code>-p</code>, <code>&#8211;makepem</code></p>
<dd> Generate <i>znc.pem</i>. This is the server certificate <code>znc</code> uses. You need this for SSL.</p>
<dt><code>-r</code>, <code>&#8211;allow-root</code></p>
<dd> Don&#8217;t complain if ZNC is run with root privilegies.</dl>
<h2>SIGNALS</h2>
<p> This section explains how <code>znc</code> reacts to different signals:</p>
<dl>
<dt><code>SIGINT</code></p>
<dd> Exit ZNC. This is equivalent to <i>/znc shutdown</i></p>
<dt><code>SIGHUP</code></p>
<dd> Reload znc.conf. This is equivalent to <i>/znc rehash.</i> <code>DO NOT</code> do this very often, things can break badly!</p>
<dt><code>SIGUSR1</code></p>
<dd> Rewrite znc.conf. This is equivalent to <i>/znc saveconfig</i></dl>
<h2>FILES</h2>
<dl>
<dt><i>/usr/local/share/znc/</i></p>
<dd> Static module data like webadmin skins</p>
<dt><i>/usr/local/lib/znc/</i></p>
<dd> <code>znc</code> installs its modules to this directory.</p>
<dt><i>/usr/local/include/znc/</i></p>
<dd> These are the headers needed for compiling own modules.</p>
<dt><i>~/.znc</i></p>
<dd> This is the default datadir. The following paths assume that you use this. If you change this via <i>&#8211;datadir</i> then the following lines are relative to that dir.</p>
<dt><i>~/.znc/znc.pem</i></p>
<dd> This is the server certificate <code>znc</code> uses for listening on SSL ports. You can generate this via <i>&#8211;makepem</i> and you may replace this with your own certificate, if you want to.</p>
<dt><i>~/.znc/modules/</i></p>
<dd> If you compile your own modules, you can save them here.</p>
<dt><i>~/.znc/configs/znc.conf</i></p>
<dd> This is the path to <i>znc.conf</i>. Use <i>&#8211;makeconf</i> for an easy way to generate it.</p>
<dt><i>~/.znc/users/</i><code>USERNAME</code><i>/</i></p>
<dd> The data for every user is saved in this dir. <code>USERNAME</code> refers to the user name of that user.</p>
<dt><i>~/.znc/users/</i><code>USERNAME</code><i>/moddata/</i><code>MODULENAME</code><i>/</i></p>
<dd> This is where each module can save some stuff. This is mainly used for remembering module settings that are not part of <i>znc.conf</i>.</p>
<dt><i>~/.znc/moddata/</i><code>MODULENAME</code><i>/</i></p>
<dd> This is where global modules may save their settings. </p>
</dl>
<h2>Index</h2>
