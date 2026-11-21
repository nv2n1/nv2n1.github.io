---
title: "vboxbeep(1)"
name: "vboxbeep"
section: "1"
letter: "v"
url: "/docs/linux/man/1-vboxbeep/"
description: "vboxbeep – isdn voice box (beeper)"
---

<h2>NAME</h2>
<p> vboxbeep &#8211; isdn voice box (beeper)</p>
<h2>SYNOPSIS</h2>
<p> <code>vboxbeep</code> <i>[OPTION] [OPTION] [&#8230;]</i></p>
<h2>DESCRIPTION</h2>
<p> vboxbeep is a daemon, that watches several message directories. If new messages are found it will beep. Vboxbeep does not use vboxd, it can only watch local directories. </p>
<p> Vboxbeep is also used to stop this annoying beep.</p>
<h2>OPTIONS</h2>
<p> Without any options, vboxbeep will signal an already running vboxbeep to stop its beep. Only root can start it as daemon.</p>
<dl>
<dt><code>-s, &#8211;sound HOURS</code></dt>
<dd> Hours to play beep signal. Use 24 hour format, like 0-23. Multiple hours can be given separated by commas, a &quot;*&quot; is used for always, &quot;-&quot; for never.</dd>
<dt><code>-m, &#8211;messagebox DIR</code></dt>
<dd> Message directory to scan. You can use this option several times.</dd>
<dt><code>-p, &#8211;pause SECS</code></dt>
<dd> Time to wait between every check. Default is 5 seconds.</dd>
<dt><code>-k, &#8211;kill</code></dt>
<dd> Kill a running vboxbeep. This option can only be used by root.</dd>
<dt><code>-h, &#8211;help</code></dt>
<dd> Show summary of options.</dd>
<dt><code>-v, &#8211;version</code></dt>
<dd> Show version of program.</dd></dl>
<h2>NOTE</h2>
<p> vboxbeep will only work if it is installed suid root. This may be a security hole, so many distributions do not install it suid root, and thus it&#8217;s useless. If you want to enable vboxbeep, please read the distribution-specific documentation how to do that (e.g. with debian gnu/linux read /usr/doc/isdnutils/README.debian).</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Andreas Jellinghaus &lt;aj [at] dungeon.inka.de&gt;, for Debian GNU/Linux and isdn4linux. </p>
