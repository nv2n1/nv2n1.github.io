---
title: "lsar(1)"
name: "lsar"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lsar/"
description: "lsar – list archive file contents"
---

<h2>NAME</h2>
<p> lsar &#8211; list archive file contents</p>
<h2>SYNOPSIS</h2>
<p> <code>lsar</code> [<i>OPTION</i>]&#8230; <i>ARCHIVE</i>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> List the contents of <i>ARCHIVE</i>s.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-l</code>, <code>-long</code></p>
<dd> Print more information about each file in the archive.</p>
<dt><code>-t</code>, <code>-test</code></p>
<dd> Test the integrity of the files in the archive, if possible.</p>
<dt><code>-p</code>, <code>-password</code> <i>PASSWORD</i></p>
<dd> The password to use for decrypting protected archives.</p>
<dt><code>-e</code>, <code>-encoding</code> <i>ENCODING</i></p>
<dd> The encoding to use for filenames in the archive, when it is not known. If not specified, the program attempts to auto-detect the encoding used. Use &quot;help&quot; or &quot;list&quot; as the argument to give a listing of all supported encodings.</p>
<dt><code>-E</code>, <code>-password-encoding</code> <i>ENCODING</i></p>
<dd> The encoding to use for the password for the archive, when it is not known. If not specified, then either the encoding given by the -encoding option or the auto-detected encoding is used.</p>
<dt><code>-pe</code>, <code>-print-encoding</code></p>
<dd> Print the auto-detected encoding and the confidence factor after the file list.</p>
<dt><code>-i</code>, <code>-indexes</code></p>
<dd> Instead of specifying the files to list as filenames or wildcard patterns, specify them as indexes.</p>
<dt><code>-j</code>, <code>-json</code></p>
<dd> Print the listing in JSON format.</p>
<dt><code>-ja</code>, <code>-json-ascii</code></p>
<dd> Print the listing in JSON format, encoded as pure ASCII text.</p>
<dt><code>-nr</code>, <code>-no-recursion</code></p>
<dd> Do not attempt to list the contents of archives contained in other archives. For instance, when listing a .tar.gz file, only list the .tar file and not its contents.</p>
<dt><code>-h</code>, <code>-help</code></p>
<dd> Display help information.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-unar/">unar</a></code>(1) </p>
<h2>Index</h2>
