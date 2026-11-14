---
title: "musetup(1)"
name: "musetup"
section: "1"
letter: "m"
url: "/docs/linux/man/1-musetup/"
description: "Musetup – Configuration script for Museekd"
---

<h2>NAME</h2>
<p> <code>Musetup</code> &#8211; Configuration script for Museekd</p>
<h2>SYNOPSIS</h2>
<p> <code>musetup</code> &lt;<i>config-filename</i>&gt; [-h] [&#8211;help]</p>
<h2>DESCRIPTION</h2>
<p> Musetup is command-line Python script that configures <i><a href="/docs/linux/man/1-museekd/">museekd</a></i>(1). Configuration options are selected by entering one of the numbers displayed. Modifying those options are done by choosing an option&#8217;s number or by inputing text. </p>
<h2>OPTIONS</h2>
<p> Musetup accepts the following options:</p>
<dl>
<dt>&lt;<i>config-filename</i>&gt;</p>
<dd> Selected Config&#8217;s path and filename.</p>
<dt><code>-h, &#8211;help</code></p>
<dd> Display Help and exit.</dl>
<h2>EXAMPLE</h2>
<p> To run this program the standard way type: </p>
<p> musetup </p>
<p> Alternativly you use a different config file with: </p>
<p> musetup config.xml </p>
<h2>FILES</h2>
<dl>
<dt>
&nbsp;<wbr><i>~/.museekd/config.xml</i></p>
<dd> The default location for the <code>museekd</code> config file.</p>
<dt>
&nbsp;<wbr><i>/usr/share/museek/museekd/config.xml.tmpl</i></p>
<dd> Config file template that&#8217;s used if no config exists.</dl>
<h2>AUTHORS</h2>
<p> Hyriand &lt;hyriand [at] thegraveyard.org&gt; </p>
<p> daelstorm &lt;daelstorm [at] gmail.com&gt;</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-mucous/">mucous</a></i>(1) <i><a href="/docs/linux/man/1-mulog/">mulog</a></i>(1) <i><a href="/docs/linux/man/1-murmur/">murmur</a></i>(1) <i><a href="/docs/linux/man/1-muscan/">muscan</a></i>(1) <i><a href="/docs/linux/man/1-muscand/">muscand</a></i>(1) <i><a href="/docs/linux/man/1-museekcontrol/">museekcontrol</a></i>(1) <i><a href="/docs/linux/man/1-museekd/">museekd</a></i>(1) <i><a href="/docs/linux/man/1-museeq/">museeq</a></i>(1) <i><a href="/docs/linux/man/1-musetup-gtk/">musetup-gtk</a></i>(1) </p>
<h2>Index</h2>
