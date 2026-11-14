---
title: "nemiver(1)"
name: "nemiver"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nemiver/"
description: "nemiver – graphical debugger for GNOME"
---

<h2>NAME</h2>
<p> nemiver &#8211; graphical debugger for GNOME</p>
<h2>SYNOPSIS</h2>
<p> <code>nemiver</code> [<i>options</i>]<i> [&lt;prog-to-debug&gt; [prog-args]]</i> </p>
<h2>DESCRIPTION</h2>
<p> This manual page documents briefly the <code>nemiver</code> command. </p>
<p> <code>nemiver</code> is a standalone graphical debugger that integrates well in the GNOME desktop environment. It currently features a backend which uses the well known GNU Debugger gdb to debug C/C++ programs.</p>
<h2>OPTIONS</h2>
<p> These programs follow the usual GNU command line syntax, with long options starting with two dashes (`-&#8216;). A summary of options is included below.</p>
<dl>
<dt><code>-?, &#8211;help</code></p>
<dd> Show help options.</p>
<dt><code>-v, &#8211;version</code></p>
<dd> Show version of program.</p>
<dt><code>&#8211;env=&nbsp;<wbr>var0=val0 var1=val1 var2=val2 &#8230;</code><i> </i></p>
<dd> Display the value of an expression.</p>
<dt><code>&#8211;attach=</code><i>&lt;pid|process_name&gt;</i></p>
<dd> Attach to a process.</p>
<dt><code>&#8211;listsessions</code></p>
<dd> List the saved debugging sessions.</p>
<dt><code>&#8211;purgesessions</code></p>
<dd> Erase the saved debugging sessions.</p>
<dt><code>&#8211;executesession=</code><i>N</i></p>
<dd> Debug the program that was of session number <i>N</i></p>
<dt><code>&#8211;log-domains=</code><i>DOMAINS</i></p>
<dd> Enable logging domains <i>DOMAINS</i></p>
<dt><code>&#8211;logdebuggeroutput</code></p>
<dd> Log the debugger output.</dl>
<h2>BUGS</h2>
<p> If you find a bug, please report it at <a rel="nofollow" href="http://bugzilla.gnome.org/enter_bug.cgi?product=nemiver.">http://bugzilla.gnome.org/enter_bug.cgi?product=nemiver.</a></p>
<h2>AUTHOR</h2>
<p> nemiver was written by Dodji Seketeli &lt;dodji [at] gnome.org&gt; and Jonathon Jongsma &lt;jjongsma [at] gnome.org&gt;. </p>
<p> This manual page was written by Luca Bruno &lt;lucab [at] debian.org&gt;, for the Debian project (but may be used by others). </p>
<h2>Index</h2>
