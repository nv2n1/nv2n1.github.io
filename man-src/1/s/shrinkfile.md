---
title: "shrinkfile(1)"
name: "shrinkfile"
section: "1"
letter: "s"
url: "/docs/linux/man/1-shrinkfile/"
description: "shrinkfile – shrink a file on a line boundary"
---

<h2>NAME</h2>
<p> shrinkfile &#8211; shrink a file on a line boundary</p>
<h2>SYNOPSIS</h2>
<p> <code>shrinkfile</code> [ <code>-n</code> ] [ <code>-m</code><i> maxsize</i> ] [ <code>-s</code><i> size</i> ] [ <code>-v</code> ] <i>file&#8230;</i></p>
<h2>DESCRIPTION</h2>
<p> The <i>shrinkfile</i> program shrinks files to a given <i>size</i> if the size is larger than <i>maxsize</i>, preserving the data at the end of the file. Truncation is performed on line boundaries, where a line is a series of bytes ending with a newline, &#8220;
&#8221;. There is no line length restriction and files may contain any binary data. </p>
<p> Temporary files are created in the <i>&lt;pathtmp in inn.conf&gt;</i> directory. The &#8220;TMPDIR&#8221; environment variable may be used to specify a different directory. </p>
<p> A newline will be added to any non-empty file that does not end with a newline. The maximum file size will not be exceeded by this addition.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-s</code></p>
<dd> By default, <i>size</i> is assumed to be zero and files are truncated to zero bytes. By default, <i>maxsize</i> is the same as <i>size</i>. If <i>maxsize</i> is less than <i>size</i>, <i>maxsize</i> is reset to <i>size</i>. The &#8220;<code>-s</code>&#8221; flag may be used to change the truncation size. Because the program truncates only on line boundaries, the final size may be smaller then the specified truncation size. The <i>size</i> and <i>maxsize</i> parameter may end with a &#8220;k&#8221;, &#8220;m&#8221;, or &#8220;g&#8221;, indicating kilobyte (1024), megabyte (1048576) or gigabyte (1073741824) lengths. Uppercase letters are also allowed. The maximum file size is 2147483647 bytes.</p>
<dt><code>-v</code></p>
<dd> If the &#8220;<code>-v</code>&#8221; flag is used, then <i>shrinkfile</i> will print a status line if a file was shrunk.</p>
<dt><code>-n</code></p>
<dd> If the &#8220;<code>-n</code>&#8221; flag is used, then <i>shrinkfile</i> will exit 0 if any file is larger than <i>maxsize</i> and exit 1 otherwise. No files will be altered.</dl>
<h2>EXAMPLES</h2>
<p> Example usage: </p>
<dl>
<dt>
<dd>
<pre>
shrinkfile -s 4m curds
shrinkfile -s 1g -v whey
shrinkfile -s 500k -m 4m -v curds whey
if shrinkfile -n -s 100m whey; then echo whey is way too big; fi
</pre>
</dl>
<h2>HISTORY</h2>
<p> Written by Landon Curt Noll &lt;chongo [at] toad.com&gt; and Rich $alz &lt;rsalz [at] uunet.uu.net&gt; for InterNetNews.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/5-inn-conf/">inn.conf</a>(5) </p>
<h2>Index</h2>
