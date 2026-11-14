---
title: "dconf-editor(1)"
name: "dconf-editor"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dconf-editor/"
description: "dconf-editor – Graphical editor for gsettings and dconf"
---

<h2 class="name">NAME</h2>
<p> dconf-editor &#8211; Graphical editor for gsettings and dconf </p>
<h2>SYNOPSIS</h2>
<p> <code>dconf-editor [OPTIONS&#8230;]</code> <code>dconf-editor [OPTIONS&#8230;] [PATH]</code> <code>dconf-editor [OPTIONS&#8230;] [FIXED_SCHEMA | RELOCATABLE_SCHEMA:PATH] [KEY]</code></p>
<h2>DESCRIPTION</h2>
<p> The <code>dconf-editor</code> program provides a graphical interface for editing settings that are stored by other applications using the <i>gsettings</i> functions of the <i>glib</i> library, or in the <i>dconf</i> database. The <code><a href="/docs/linux/man/1-gsettings/">gsettings</a></code>(1) and <code><a href="/docs/linux/man/1-dconf/">dconf</a></code>(1) utilities provides similar functionality on the commandline.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code>,<code>&nbsp;&#8211;help</code></p>
<dd> Prints the command-line options and exits.</p>
<dt><code>-v</code>,<code>&nbsp;&#8211;version</code></p>
<dd> Prints the release version and exits.</p>
<dt><code>&#8211;list-relocatable-schemas</code></p>
<dd> Prints the list of relocatable schemas and exits.</p>
<dt><code>&#8211;I-understand-that-changing-options-can-break-applications</code></p>
<dd> Launchs application without showing initial warning.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-dconf/">dconf</a></code>(7) <code><a href="/docs/linux/man/1-dconf/">dconf</a></code>(1) <code><a href="/docs/linux/man/1-gsettings/">gsettings</a></code>(1) </p>
<h2>Index</h2>
