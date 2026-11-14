---
title: "zipsplit(1)"
name: "zipsplit"
section: "1"
letter: "z"
url: "/docs/linux/man/1-zipsplit/"
description: "zipsplit – split a zipfile into smaller zipfiles"
---

<h2 class="name">NAME</h2>
<p> zipsplit &#8211; split a zipfile into smaller zipfiles</p>
<h2>SYNOPSIS</h2>
<p> <i>zipsplit</i> [<code>-t</code>] [<code>-i</code>] [<code>-p</code>] [<code>-s</code>] [<code>-n size</code>] [<code>-r room</code>] [<code>-b path</code>] [<code>-h</code>] [<code>-v</code>] [<code>-L</code>] zipfile </p>
<h2>ARGUMENTS</h2>
<p> zipfile Zipfile to split. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-t</code></p>
<dd> Report how many files it will take, but don&#8217;t make them.</p>
<dt><code>-i</code></p>
<dd> Make index (zipsplit.idx) and count its size against first zip file.</p>
<dt><code>-n&nbsp;</code>size</p>
<dd> Make zip files no larger than &quot;size&quot; (default = 36000).</p>
<dt><code>-r&nbsp;</code>room</p>
<dd> Leave room for &quot;room&quot; bytes on the first disk (default = 0).</p>
<dt><code>-b&nbsp;</code>path</p>
<dd> Use path for the output zip files.</p>
<dt><code>-p</code></p>
<dd> Pause between output zip files.</p>
<dt><code>-s</code></p>
<dd> Do a sequential split even if it takes more zip files.</p>
<dt><code>-h</code></p>
<dd> Show a short help.</p>
<dt><code>-v</code></p>
<dd> Show version information.</p>
<dt><code>-L</code></p>
<dd> Show software license. </p>
</dl>
<h2>DESCRIPTION</h2>
<p> <i>zipsplit</i> reads a zipfile and splits it into smaller zipfiles. </p>
<h2>EXAMPLES</h2>
<p> To be filled in. </p>
<h2>BUGS</h2>
<p> Does not yet support large (&gt; 2 GB) or split archives. </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-zip/">zip</a>(1), <a href="/docs/linux/man/1-unzip/">unzip</a>(1)</p>
<h2>AUTHOR</h2>
<p> Info-ZIP </p>
<h2>Index</h2>
