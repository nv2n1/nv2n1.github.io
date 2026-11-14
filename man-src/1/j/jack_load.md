---
title: "jack_load(1)"
name: "jack_load"
section: "1"
letter: "j"
url: "/docs/linux/man/1-jack_load/"
description: "jack_load – JACK toolkit client for loading in-process clients"
---

<h2>NAME</h2>
<p> jack_load &#8211; JACK toolkit client for loading in-process clients</p>
<h2>SYNOPSIS</h2>
<p> <code>jack_load</code> [ <i>-i</i> initstring ] [ <i>-s</i> servername ] [<i>-w</i> ] client-name so-name [ initstring ]</p>
<h2>DESCRIPTION</h2>
<p> <code>jack_load</code> is a JACK toolkit client. It loads the specified plugin and creates an in-process client.</p>
<h2>ARGUMENTS</h2>
<p> The client-name must be a currently unused client name. </p>
<p> The so-name is the name of file that client code is stored in (typically, <i>clientname.so</i>)</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-i</code>, <code>&#8211;init</code> init-string</p>
<dd>
 initialization string passed to the in-process client. Note that this can also be specified as the last argument on the command line.</p>
<dt><code>-s</code>, <code>&#8211;server</code> servername</p>
<dd>
 Name of JACK server to connect to</p>
<dt><code>-w</code>, <code>&#8211;wait</code></p>
<dd> Wait for a signal (eg. from Ctrl-c) and then unload the client.</dl>
<h2>AUTHOR</h2>
<p> Jeremy Hall </p>
<h2>Index</h2>
