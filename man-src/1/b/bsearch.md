---
title: "bsearch(1)"
name: "bsearch"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bsearch/"
description: "bsearch – manages one-time passwords"
---

<h2 class="name">NAME</h2>
<p> <code>bsearch</code> &#8211; manages one-time passwords </p>
<h2>SYNOPSIS</h2>
<p> <code>bsearch</code> [-<code>KVvh</code> ] [-<code>b </code><i>block-size</i> ] [-<code>m </code><i>max-cache-size</i> ] <i>file</i> <i>[key &#8230;]</i></p>
<h2>DESCRIPTION</h2>
<p> The <code>bsearch</code> program performs binary searches of <i>file</i> which must be a sorted flat text file. </p>
<p> Each line is a record. Each record starts with a key that is optionally followed by whitespace and a value. Whitespace may be quoted with a backslash, but newline and carriage-return characters must be quoted in some other manner (e.g., as backslash-n and backslash-r). Escapes are not interpreted nor removed. </p>
<p> If no key arguments are given on the comman-line, then keys will be read from standard input. </p>
<p> By default only values are printed to standard output. Use the -K option to also print keys. The exit status will be non-zero if any key lookups fail. </p>
<p> Options are:</p>
<dl>
<dt><code>-K</code></p>
<dd> Print keys.</p>
<dt><code>-V</code></p>
<dd> Don&#8217;t print values.</p>
<dt><code>-h</code></p>
<dd> Print usage and exit.</p>
<dt><code>-v</code></p>
<dd> Print statistic and debug information to standard error. <i>file</i> A sorted flat text file. NOTE: use the &quot;C&quot; locale for sorting this file, as in &quot;LC_ALL=C sort -u -o file file&quot;.</p>
<dt><code>-h</code></p>
<dd> For getting a help message.</p>
<dt><code>-m</code></p>
<dd> Set <i>max-cache-size</i> as the maximum cache size. If the <i>file</i> is smaller than this size then the whole file will be read into memory, else the program will read blocks. Defaults to 1MB.</p>
<dt><code>-b</code></p>
<dd> Set <i>block-size</i> as the block size for block-wise I/O. This must be a power of 2, must be no smaller than 512 and no larger than 1MB. Defaults to the <i>file&#8217;s</i> filesystem&#8217;s preferred blocksize.</dl>
<h2>EXAMPLES</h2>
<blockquote>
<pre>
$ env LC_ALL=C sort -o /tmp/words /usr/share/dict/words
$ bsearch -Kv /tmp/words day
Using whole-file method
Key day found at offset 327695 in 12 loops and 0 reads
day
$ 
</pre>
<h2>NOTES</h2>
<p> Records must not be longer than one block&#8217;s size. </p>
<p> Flat text files must be sorted in the &quot;C&quot; locale. In some systems the default locale may result in case-insensitive sorting by the sort command.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-sort/">sort</a>(1) </p>
<h2>Index</h2>
