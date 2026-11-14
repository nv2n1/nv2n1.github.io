---
title: "unar(1)"
name: "unar"
section: "1"
letter: "u"
url: "/docs/linux/man/1-unar/"
description: "unar – extract archive file contents"
---

<h2>NAME</h2>
<p> unar &#8211; extract archive file contents</p>
<h2>SYNOPSIS</h2>
<p> <code>unar</code> [<i>OPTION</i>]&#8230; <i>ARCHIVE</i> [<i>FILE</i>]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> Extract <i>FILE</i>s or the contents of <i>ARCHIVE</i>.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-o</code>, <code>-output-directory</code> <i>DIRECTORY</i></p>
<dd> The directory to write the contents of the archive to. Defaults to the current directory.</p>
<dt><code>-f</code>, <code>-force-overwrite</code></p>
<dd> Always overwrite files when a file to be unpacked already exists on disk. By default, the program asks the user if possible, otherwise skips the file.</p>
<dt><code>-r</code>, <code>-force-rename</code></p>
<dd> Always rename files when a file to be unpacked already exists on disk.</p>
<dt><code>-s</code>, <code>-force-skip</code></p>
<dd> Always skip files when a file to be unpacked already exists on disk.</p>
<dt><code>-d</code>, <code>-force-directory</code></p>
<dd> Always create a containing directory for the contents of the unpacked archive. By default, a directory is created if there is more than one top-level file or folder.</p>
<dt><code>-D</code>, <code>-no-directory</code></p>
<dd> Never create a containing directory for the contents of the unpacked archive.</p>
<dt><code>-p</code>, <code>-password</code> <i>PASSWORD</i></p>
<dd> The password to use for decrypting protected archives.</p>
<dt><code>-e</code>, <code>-encoding</code> <i>ENCODING</i></p>
<dd> The encoding to use for filenames in the archive, when it is not known. If not specified, the program attempts to auto-detect the encoding used. Use &quot;help&quot; or &quot;list&quot; as the argument to give a listing of all supported encodings.</p>
<dt><code>-E</code>, <code>-password-encoding</code> <i>ENCODING</i></p>
<dd> The encoding to use for the password for the archive, when it is not known. If not specified, then either the encoding given by the -encoding option or the auto-detected encoding is used.</p>
<dt><code>-i</code>, <code>-indexes</code></p>
<dd> Instead of specifying the files to list as filenames or wildcard patterns, specify them as indexes, as output by lsar.</p>
<dt><code>-nr</code>, <code>-no-recursion</code></p>
<dd> Do not attempt to extract archives contained in other archives. For instance, when unpacking a .tar.gz file, only unpack the .tar file and not its contents.</p>
<dt><code>-t</code>, <code>-copy-time</code></p>
<dd> Copy the file modification time from the archive file to the containing directory, if one is created.</p>
<dt><code>-k</code>, <code>-forks visible</code>|<code>hidden</code>|<code>skip</code></p>
<dd> How to handle Mac OS resource forks. <code>visible</code> creates AppleDouble files with the extension &quot;.rsrc&quot;, <code>hidden</code> creates AppleDouble files with the prefix &quot;._&quot;, and <code>skip</code> discards all resource forks. Defaults to <code>visible</code>.</p>
<dt><code>-q</code>, <code>-quiet</code></p>
<dd> Run in quiet mode.</p>
<dt><code>-h</code>, <code>-help</code></p>
<dd> Display help information.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-lsar/">lsar</a></code>(1) </p>
<h2>Index</h2>
