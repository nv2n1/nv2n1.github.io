---
title: "fcat(1)"
name: "fcat"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fcat/"
description: "fcat – Output the contents of a file based on its name."
---

<h2 class="name">NAME</h2>
<p> <code>fcat </code>&#8211; Output the contents of a file based on its name. </p>
<h2>SYNOPSIS</h2>
<pre><code>
fcat[-hRsvV][-f fstype][-i imgtype][-o imgoffset][-b dev_sector_size] path_of_file image[images]
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>fcat</code> opens the named <code>image</code>(s) and copies the file at the path <i>path_of_file</i> to standard output.</p>
<h2>ARGUMENTS</h2>
<dl>
<dt><code>-f</code> <i>fstype</i></p>
<dd> Specifies the file system type. Use <code>-f</code> &#8216;list&#8217; to list the supported file system types. If not given, autodetection methods are used.</p>
<dt><code>-h</code></p>
<dd> Skip over holes in sparse files, so that absolute address information is lost. This option saves space when copying sparse files.</p>
<dt><code>-R</code></p>
<dd> Suppress errors if a deleted file is being recovered.</p>
<dt><code>-s</code></p>
<dd> Include the slack space in the output.</p>
<dt><code>-i</code> <i>imgtype</i></p>
<dd> Identify the type of <i>image</i> file, such as raw. Use &#8216;<code>-i</code> list&#8217; to list the supported types. If not given, autodetection methods are used.</p>
<dt><code>-o</code> <i>imgoffset</i></p>
<dd> The sector offset where the file system starts in the <i>image</i>.</p>
<dt><code>-b</code> <i>dev_sector_size</i></p>
<dd> The size, in bytes, of the underlying device sectors. If not given, the value in the <i>image</i> format is used (if it exists) or 512-bytes is assumed.</p>
<dt><code>-v</code></p>
<dd> Enable verbose mode, output to stderr.</p>
<dt><code>-V</code></p>
<dd> Display version</p>
<dt><i>image</i> [<i>images</i>]</p>
<dd> The disk or partition <i>image</i> to read, whose format is given with &#8216;<code>-i</code>&#8216;. Multiple <i>image</i> file names can be given if the <i>image</i> is split into multiple segments. If only one <i>image</i> file is given, and its name is the first in a sequence (e.g., as indicated by ending in ’.001’), subsequent <i>image</i> segments will be included automatically.</p>
<dt><i>path_of_file</i></p>
<dd> Path of file to extract the contents of. Surround the path in quotes if there is a space in a file or directory name. Use forward slashes.</dl>
<h2>AUTHOR</h2>
<p> The Sleuth Kit was written by Brian Carrier &lt;carrier [at] sleuthkit.org&gt;. </p>
<p> This manual page was written by Joao Eriberto Mota Filho &lt;eriberto [at] debian.org&gt; for the Debian project (but may be used by others). </p>
<h2>Index</h2>
