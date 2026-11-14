---
title: "vorbiscomment(1)"
name: "vorbiscomment"
section: "1"
letter: "v"
url: "/docs/linux/man/1-vorbiscomment/"
description: "vorbiscomment – List or edit comments in Ogg Vorbis files"
---

<h2 class="name">NAME</h2>
<p> vorbiscomment &#8211; List or edit comments in Ogg Vorbis files</p>
<h2>SYNOPSIS</h2>
<p> <code>vorbiscomment</code> <code>[-l]</code> [<code>-R</code>] [<code>-e</code>] <i>file.ogg</i><br />
 <code>vorbiscomment</code> <code>-a</code> <code>[ -c commentfile | -t &#8220;name=value&#8221; ]</code> [<code>-q</code>] [<code>-R</code>] [<code>-e</code>] <i>in.ogg</i> <i>[out.ogg]</i><br />
 <code>vorbiscomment</code> <code>-w</code> <code>[ -c commentfile | -t &#8220;name=value&#8221; ]</code> [<code>-q</code>] [<code>-R</code>] [<code>-e</code>] <i>in.ogg</i> <i>[out.ogg]</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>vorbiscomment</code> Reads, modifies, and appends Ogg Vorbis audio file metadata tags. </p>
<h2>OPTIONS</h2>
<dl>
<dt>-a, &#8211;append</p>
<dd> Append comments.</p>
<dt>-c file, &#8211;commentfile file</p>
<dd> Take comments from a file. The file is the same format as is output by the -l option or given to the -t option: one element per line in &#8216;tag=value&#8217; format. If the file is /dev/null and -w was passed, the existing comments will be removed.</p>
<dt>-h, &#8211;help</p>
<dd> Show command help.</p>
<dt>-l, &#8211;list</p>
<dd> List the comments in the Ogg Vorbis file.</p>
<dt>-t &#8216;name=value&#8217;, &#8211;tag &#8216;name=value&#8217;</p>
<dd> Specify a new tag on the command line. Each tag is given as a single string. The part before the &#8216;=&#8217; is treated as the tag name and the part after as the value.</p>
<dt>-w, &#8211;write</p>
<dd> Replace comments with the new set given either on the command line with -t or from a file with -c. If neither -c nor -t is given, the new set will be read from the standard input.</p>
<dt>-R, &#8211;raw</p>
<dd> Read and write comments in UTF-8, rather than converting to the user&#8217;s character set.</p>
<dt>-e, &#8211;escapes</p>
<dd> Quote/unquote newlines and backslashes in the comments. This ensures every comment is exactly one line in the output (or input), allowing to filter and round-trip them. Without it, you can only write multi-line comments by using -t and you can&#8217;t reliably distinguish them from multiple one-line comments. </p>
<p> Supported escapes are c-style &quot;
&quot;, &quot;&quot;, &quot;\&quot; and &quot;
