---
title: "sensible-editor(1)"
name: "sensible-editor"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sensible-editor/"
description: "sensible-editor – sensible editing"
---

<h2 class="name">NAME</h2>
<p> sensible-editor &#8211; sensible editing </p>
<h2>SYNOPSIS</h2>
<p> <code>sensible-editor</code> [OPTIONS&#8230;] </p>
<h2>DESCRIPTION</h2>
<p> <code>sensible-editor</code> makes sensible decisions on which editor to call. Programs in Debian can use this script as their default editor. <code>sensible-editor</code> try to do in the following order:</p>
<dl>
<dt>step]</p>
<dd> if <code>VISUAL</code> environment variable exists, execute <code>VISUAL [OPTIONS]</code></p>
<dt>step]</p>
<dd> if <code>EDITOR</code> environment variable exists, execute <code>EDITOR [OPTIONS]</code></p>
<dt>step]</p>
<dd> source the contents of file <i>~/.selected_editor</i> and, if <code>SELECTED_EDITOR</code> environment variable exists execute <code>SELECTED_EDITOR [OPTIONS]</code></p>
<dt>step]</p>
<dd> run <code>editor [OPTIONS]</code> command</p>
<dt>step]</p>
<dd> finally run <code>nano-tiny [OPTIONS]</code> command</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-environ/">environ</a></code>(7) for documentation of the EDITOR, VISUAL variables<br />
 <code><a href="/docs/linux/man/1-select-editor/">select-editor</a></code>(1) for changing a user&#8217;s default editor.<br />
 <code><a href="/docs/linux/man/1-editor/">editor</a></code>(1) for default system wide editor.</p>
<h2>BUGS</h2>
<p> This command is protected against trivial fork bomb, when user set <code>EDITOR=sensible-editor</code> wider loops are still possible.</p>
<h2>STANDARD</h2>
<p> Documentation of behavior of sensible-utils under a debian system is available under section 11.4 of debian-policy usually installed under /usr/share/doc/debian-policy (you might need to install debian-policy) </p>
<h2>Index</h2>
