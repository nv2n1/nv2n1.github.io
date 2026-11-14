---
title: "musetup-gtk(1)"
name: "musetup-gtk"
section: "1"
letter: "m"
url: "/docs/linux/man/1-musetup-gtk/"
description: "Musetup-GTK – PyGTK2 Configuration app for Museekd"
---

<h2>NAME</h2>
<p> <code>Musetup-GTK</code> &#8211; PyGTK2 Configuration app for Museekd</p>
<h2>SYNOPSIS</h2>
<p> <code>musetup-gtk </code> [-c | &#8211;config &lt;<i>config-filename</i>&gt;] [-h | &#8211;help]</p>
<h2>DESCRIPTION</h2>
<p> Musetup-GTK is PyGTK2 GUI that configures <i><a href="/docs/linux/man/1-museekd/">museekd</a></i>(1). There are two configuration modes: </p>
<p> Dialogs &#8211; under General Settings &#8211; that provide the most commonly configured options, including the adding of shared directories, via a muscan frontend (add/removing &amp; rescanning take effect immediately). </p>
<p> The Settings Tree allows you to modify all options and even remove entire settings nodes, so it is quite dangerous, and should be used with much care. </p>
<p> After changes to settings you need to Save them from them be written to the config file.</p>
<h2>OPTIONS</h2>
<p> Musetup-GTK accepts the following options:</p>
<dl>
<dt>-c, &#8211;config &lt;<i>config-filename</i>&gt;</p>
<dd> Selected Config&#8217;s path and filename.</p>
<dt><code>-h, &#8211;help</code></p>
<dd> Display Help and exit.</dl>
<h2>EXAMPLE</h2>
<p> To run this program the standard way type: </p>
<p> musetup-gtk </p>
<p> Alternativly you use a different config file with: </p>
<p> musetup-gtk -c config.xml </p>
<h2>FILES</h2>
<dl>
<dt>
&nbsp;<wbr><i>~/.museekd/config.xml</i></p>
<dd> The default location for the <code>museekd</code> config file.</p>
<dt>
&nbsp;<wbr><i>/usr/share/museek/museekd/config.xml.tmpl</i></p>
<dd> Config file template that&#8217;s used if no config exists.</dl>
<h2>AUTHORS</h2>
<p> Code taken from musetup by Hyriand &lt;hyriand [at] thegraveyard.org&gt; </p>
<p> daelstorm &lt;daelstorm [at] gmail.com&gt;</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-mucous/">mucous</a></i>(1) <i><a href="/docs/linux/man/1-mulog/">mulog</a></i>(1) <i><a href="/docs/linux/man/1-murmur/">murmur</a></i>(1) <i><a href="/docs/linux/man/1-muscan/">muscan</a></i>(1) <i><a href="/docs/linux/man/1-muscand/">muscand</a></i>(1) <i><a href="/docs/linux/man/1-museekcontrol/">museekcontrol</a></i>(1) <i><a href="/docs/linux/man/1-museekd/">museekd</a></i>(1) <i><a href="/docs/linux/man/1-museeq/">museeq</a></i>(1) <i><a href="/docs/linux/man/1-musetup/">musetup</a></i>(1) </p>
<h2>Index</h2>
