---
title: "zipnote(1)"
name: "zipnote"
section: "1"
letter: "z"
url: "/docs/linux/man/1-zipnote/"
description: "zipnote – write the comments in zipfile to stdout, edit comments and rename files in zipfile"
---

<h2 class="name">NAME</h2>
<p> zipnote &#8211; write the comments in zipfile to stdout, edit comments and rename files in zipfile</p>
<h2>SYNOPSIS</h2>
<p> <i>zipnote</i> [<code>-w</code>] [<code>-b path</code>] [<code>-h</code>] [<code>-v</code>] [<code>-L</code>] zipfile </p>
<h2>ARGUMENTS</h2>
<p> zipfile Zipfile to read comments from or edit. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-w</code></p>
<dd> Write comments to a zipfile from stdin (see below).</p>
<dt><code>-b&nbsp;</code>path</p>
<dd> Use path for the temporary zip file.</p>
<dt><code>-h</code></p>
<dd> Show a short help.</p>
<dt><code>-v</code></p>
<dd> Show version information.</p>
<dt><code>-L</code></p>
<dd> Show software license. </p>
</dl>
<h2>DESCRIPTION</h2>
<p> <i>zipnote</i> writes the comments in a zipfile to stdout. This is the default mode. A second mode allows updating the comments in a zipfile as well as allows changing the names of the files in the zipfile. These modes are described below. </p>
<h2>EXAMPLES</h2>
<p> To write all comments in a zipfile to stdout use for example </p>
<pre>
     zipnote foo.zip &gt; foo.tmp
</pre>
<p> This writes all comments in the zipfile <i>foo.zip</i> to the file <i>foo.tmp</i> in a specific format. </p>
<p> If desired, this file can then be edited to change the comments and then used to update the zipfile. </p>
<pre>
     zipnote -w foo.zip &lt; foo.tmp
</pre>
<p> The names of the files in the zipfile can also be changed in this way. This is done by following lines like </p>
<pre>
     &quot;@ name&quot;
</pre>
<p> in the created temporary file (called <i>foo.tmp</i> here) with lines like </p>
<pre>
     &quot;@=newname&quot;
</pre>
<p> and then using the -w option as above. </p>
<h2>BUGS</h2>
<p> The temporary file format is rather specific and zipnote is rather picky about it. It should be easier to change file names in a script. </p>
<p> Does not yet support large (&gt; 2 GB) or split archives. </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-zip/">zip</a>(1), <a href="/docs/linux/man/1-unzip/">unzip</a>(1)</p>
<h2>AUTHOR</h2>
<p> Info-ZIP </p>
<h2>Index</h2>
