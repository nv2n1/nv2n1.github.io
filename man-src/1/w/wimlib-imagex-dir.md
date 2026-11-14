---
title: "wimlib-imagex-dir(1)"
name: "wimlib-imagex-dir"
section: "1"
letter: "w"
url: "/docs/linux/man/1-wimlib-imagex-dir/"
description: "wimlib-imagex-dir – Show the files contained in a WIM archive"
---

<h2>NAME</h2>
<p> wimlib-imagex-dir &#8211; Show the files contained in a WIM archive</p>
<h2>SYNOPSIS</h2>
<p> <code>wimlib-imagex dir</code> <i>WIMFILE</i> <i>IMAGE</i> [<i>OPTIONS</i>]</p>
<h2>DESCRIPTION</h2>
<p> Lists the files and directories contained in the specified image of the Windows Imaging (WIM) file <i>WIMFILE</i>. This command is also available as simply <code>wimdir</code> if the appropriate hard link or batch file has been installed. </p>
<p> <i>IMAGE</i> specifies the image in <i>WIMFILE</i> to show the files of. It may be a 1-based index of an image in <i>WIMFILE</i>, the name of an image in <i>WIMFILE</i>, or the keyword &quot;all&quot; to indicate that files from all images in <i>WIMFILE</i> are to be shown. Use the <code>wimlib-imagex info</code> (1) command to show what images a WIM file contains.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;path</code>=<i>PATH</i></p>
<dd> List the files recursively from the <i>PATH</i> directory instead of from the root directory.</p>
<dt><code>&#8211;detailed</code></p>
<dd> List detailed information about each file.</p>
<dt><code>&#8211;one-file-only</code></p>
<dd> Show information about one file only. Intended for use with both <code>&#8211;path</code> and <code>&#8211;detailed</code>.</p>
<dt><code>&#8211;ref</code>=&quot;<i>GLOB</i>&quot;</p>
<dd> File glob of additional WIMs or split WIM parts to reference resources from. This option can be specified multiple times. This option is only useful when <code>&#8211;detailed</code> is also specified.</dl>
<h2>NOTES</h2>
<p> <code>wimlib-imagex dir</code> supports split WIMs, but it will only work on the first part of the split WIM. </p>
<p> DOS names and alternate (named) data streams are not listed unless the <code>&#8211;detailed</code> mode is used.</p>
<h2>EXAMPLES</h2>
<p> List all files in the first image of &#8216;boot.wim&#8217;:</p>
<dl>
<dt>
<dd>
<p> wimlib-imagex dir boot.wim 1</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-wimlib-imagex/">wimlib-imagex</a></code>(1) <code><a href="/docs/linux/man/1-wimlib-imagex-info/">wimlib-imagex-info</a></code>(1) </p>
<h2>Index</h2>
