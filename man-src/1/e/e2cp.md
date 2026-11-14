---
title: "e2cp(1)"
name: "e2cp"
section: "1"
letter: "e"
url: "/docs/linux/man/1-e2cp/"
description: "e2cp – copies files from/to an e2fs filesystem"
---

<h2 class="name">NAME</h2>
<p> e2cp &#8211; copies files from/to an e2fs filesystem </p>
<h2>SYNOPSIS</h2>
<p> <code>e2cp</code> [<i>options</i>]<i> files&#8230; dest</i></p>
<h2>DESCRIPTION</h2>
<p> The <code>e2cp</code> command copies files to/from an e2fs filesystem from/to the machine&#8217;s filesystem.</p>
<h2>OPTIONS</h2>
<p> A single `-&#8216; (dash) can be used instead of a file name to indicate standard input/output.</p>
<dl>
<dt><code>-0</code></p>
<dd> Input lines terminated by a null character.</p>
<dt><code>-a</code></p>
<dd> Absolute directory names &#8211; create directories instead of just copying into the destination. Only valid for copying into an ext2fs filesystem.</p>
<dt><code>-d </code><i>dest_dir</i></p>
<dd> Destination of files to be copied. May be in the ext2fs filesystem or the host filesystem.</p>
<dt><code>-G </code><i>gid</i></p>
<dd> Set the default group to gid.</p>
<dt><code>-O </code><i>uid</i></p>
<dd> Set the default file owner to uid.</p>
<dt><code>-p</code></p>
<dd> Preserve host file attributes (permissions, times, etc.) when copying files.</p>
<dt><code>-P </code><i>mode</i></p>
<dd> Set the file permissions (ie 755, 666).</p>
<dt><code>-s </code><i>src_dir</i></p>
<dd> The source of the files to be copied.</p>
<dt><code>-v</code></p>
<dd> Be verbose.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-e2tools/">e2tools</a></code>(7), <code><a href="/docs/linux/man/1-e2ln/">e2ln</a></code>(1), <code><a href="/docs/linux/man/1-e2ls/">e2ls</a></code>(1), <code><a href="/docs/linux/man/1-e2mkdir/">e2mkdir</a></code>(1), <code><a href="/docs/linux/man/1-e2mv/">e2mv</a></code>(1), <code><a href="/docs/linux/man/1-e2rm/">e2rm</a></code>(1), <code><a href="/docs/linux/man/1-e2tail/">e2tail</a></code>(1).</p>
<h2>AUTHOR</h2>
<p> The <code>e2tools</code> were written by Keith Sheffield &lt;sheff [at] pobox.com&gt;. </p>
<p> This manual page was written by Lucas Wall &lt;lwall [at] debian.org&gt;, for the Debian project (but may be used by others). </p>
<h2>Index</h2>
