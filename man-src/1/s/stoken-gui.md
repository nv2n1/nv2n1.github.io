---
title: "stoken-gui(1)"
name: "stoken-gui"
section: "1"
letter: "s"
url: "/docs/linux/man/1-stoken-gui/"
description: "stoken-gui – GTK+ software token"
---

<h2 class="name">NAME</h2>
<p> stoken-gui &#8211; GTK+ software token </p>
<h2>SYNOPSIS</h2>
<p> <code>stoken-gui</code> [<i>opts</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>stoken-gui</code> is a software token compatible with RSA SecurID 128-bit (AES) tokens. The graphical user interface provides limited support for password entry and viewing the current token. Initial token importation and other configuration items are handled through the command-line interface, <code><a href="/docs/linux/man/1-stoken/">stoken</a>(1)</code>. </p>
<p> After using <code>stoken import</code> to populate <i>~/.stokenrc</i>, <code>stoken-gui</code> may be invoked to display the tokencode and counter. The tokencode changes once a minute; <code>stoken-gui</code> may be left running forever and will copy the current tokencode to the clipboard on demand. </p>
<p> If a password and/or PIN is required, <code>stoken-gui</code> will pop up a dialog box requesting the appropriate information.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;small</code></p>
<dd> Show a minimal window that only displays a tokencode and a progress bar. Clicking on the tokencode copies it to the clipboard.</p>
<dt><code>&#8211;rcfile=</code><i>file</i></p>
<dd> Use an alternate <i>.stokenrc</i> file. This is typically used to support multiple tokens on the same user account.</p>
<dt><code>&#8211;password=</code><i>password</i>, <code>-p</code> <i>password</i></p>
<dd> Use a password supplied from the command line, instead of prompting the user. See notes in <code>SECURITY CONSIDERATIONS</code> on the <code><a href="/docs/linux/man/1-stoken/">stoken</a>(1)</code> man page.</p>
<dt><code>&#8211;pin=</code><i>pin</i>, <code>-n</code> <i>pin</i></p>
<dd> Use a PIN supplied from the command line, instead of prompting the user. See notes in <code>SECURITY CONSIDERATIONS</code> on the <code><a href="/docs/linux/man/1-stoken/">stoken</a>(1)</code> man page.</p>
<dt><code>&#8211;force</code>, <code>-f</code></p>
<dd> Override token expiration date check.</p>
<dt><code>&#8211;file=</code><i>file</i></p>
<dd> Use a token from <i>file</i> instead of the <i>.stokenrc</i> file. For testing purposes only.</p>
<dt><code>&#8211;token=</code><i>token_string</i></p>
<dd> Use a token from the command line instead of the <i>.stokenrc</i> file. See above notes on <code>&#8211;file</code>.</p>
<dt><code>&#8211;random</code></p>
<dd> Generate a random token on the fly. Used for testing or demonstrations only. These tokens should <code>not</code> be used for real authentication.</p>
<dt><code>&#8211;help</code>, <code>-h</code></p>
<dd> Display basic usage information.</p>
<dt><code>&#8211;version</code>, <code>-v</code></p>
<dd> Display version information.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-stoken/">stoken</a></code>(1).</p>
<h2>FILES</h2>
<dl>
<dt>~/.stokenrc</p>
<dd> Default configuration file.</dl>
<h2>AUTHOR</h2>
<p> Kevin Cernekee &lt;cernekee [at] gmail.com&gt; </p>
<h2>Index</h2>
