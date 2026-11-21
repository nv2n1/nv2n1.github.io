---
title: "mpaste(1)"
name: "mpaste"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mpaste/"
description: "mpaste – command-line client for https://paste.mate-desktop.org"
---

<h2>NAME</h2>
<p> mpaste &#8211; command-line client for <a rel="nofollow" href="https://paste.mate-desktop.org">https://paste.mate-desktop.org</a></p>
<h2>SYNOPSIS</h2>
<p> <code>mpaste [&lt;OPTIONS&gt;] [&lt;INFILE&gt;]</code></p>
<h2>DESCRIPTION</h2>
<p> The <code>mpaste</code> program reads text from file or STDIN and sends it to </p>
<p>&nbsp;<wbr><i><a rel="nofollow" href="https://paste.mate-desktop.org">https://paste.mate-desktop.org</a></i>,&nbsp;<wbr> </p>
<p> a pastebin site run by the MATE Desktop project. After pasting some text, <code>mpaste</code> returns the URL of the pasted text to the user. </p>
<p> If <i>&lt;INFILE&gt;</i> is omitted, <code>mpaste</code> waits for incoming text on STDIN. </p>
<h2>OPTIONS</h2>
<p> The following options are supported:</p>
<dl>
<dt><i>-t, &#8211;title &lt;TITLE&gt;</i></dt>
<dd> Title of the paste.</dd>
<dt><i>-p, &#8211;private</i></dt>
<dd> Should this paste be private?</dd>
<dt><i>-pwd, &#8211;password &lt;PASSWORD&gt;</i></dt>
<dd> Protect paste with a given password.</dd>
<dt><i>-lang, &#8211;language &lt;LANG&gt;</i></dt>
<dd> Language that the paste is in.</dd>
<dt><i>-ll, &#8211;language-list</i></dt>
<dd> List all supported languages.</dd>
<dt><i>-e, &#8211;expire &lt;MINUTES&gt;</i></dt>
<dd> Paste expires in a given number of minutes. </dd>
</dl>
<h2>BUGS</h2>
<p> If you find bugs in the <i>mpaste</i> program, please report these on <a rel="nofollow" href="https://github.com/mate-desktop/mate-desktop/issues.">https://github.com/mate-desktop/mate-desktop/issues.</a> </p>
<h2>AUTHOR</h2>
<p> This manual page has been written for the Debian project by Mike Gabriel &lt;mike.gabriel [at] das-netzwerkteam.de&gt; and maybe used by others. </p>
