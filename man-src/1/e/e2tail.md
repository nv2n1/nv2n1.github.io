---
title: "e2tail(1)"
name: "e2tail"
section: "1"
letter: "e"
url: "/docs/linux/man/1-e2tail/"
description: "e2tail – a basic version of the tail command for an ext2 filesystem"
---

<h2 class="name">NAME</h2>
<p> e2tail &#8211; a basic version of the tail command for an ext2 filesystem </p>
<h2>SYNOPSIS</h2>
<p> <code>e2tail</code> [<i>options</i>]<i> file</i></p>
<h2>DESCRIPTION</h2>
<p> The <code>e2tail</code> command implements a basic version of the tail command.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-n </code><i>num_lines</i></p>
<dd> The number of lines to display</p>
<dt><code>-f</code></p>
<dd> Output appended data as the file grows. This is inode dependent, so if the file is renamed, it will keep checking it.</p>
<dt><code>-F</code></p>
<dd> Output appended data as the file grows. This is file name dependent, so if the file is renamed, it will check on any new files with the same name as the original. This is useful for watching log files that may be rotated out occasionally. This was requested by a person in the computer security field for monitoring &#8216;honeypot&#8217; type machines.</p>
<dt><code>-s </code><i>sleep_interval</i></p>
<dd> The number of seconds to sleep before checking if the file has grown while in &#8216;follow&#8217; mode. The default is 1.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-e2tools/">e2tools</a></code>(7), <code><a href="/docs/linux/man/1-e2ln/">e2ln</a></code>(1), <code><a href="/docs/linux/man/1-e2ls/">e2ls</a></code>(1), <code><a href="/docs/linux/man/1-e2mkdir/">e2mkdir</a></code>(1), <code><a href="/docs/linux/man/1-e2cp/">e2cp</a></code>(1), <code><a href="/docs/linux/man/1-e2rm/">e2rm</a></code>(1), <code><a href="/docs/linux/man/1-e2mv/">e2mv</a></code>(1).</p>
<h2>AUTHOR</h2>
<p> The <code>e2tools</code> were written by Keith Sheffield &lt;sheff [at] pobox.com&gt;. </p>
<p> This manual page was written by Lucas Wall &lt;lwall [at] debian.org&gt;, for the Debian project (but may be used by others). </p>
<h2>Index</h2>
