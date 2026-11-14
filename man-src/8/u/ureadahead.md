---
title: "ureadahead(8)"
name: "ureadahead"
section: "8"
letter: "u"
url: "/docs/linux/man/8-ureadahead/"
description: "ureadahead – Read files in advance during boot"
---

<p>ureadahead &#8211; Read files in advance during boot</p>
<h2>Synopsis</h2>
<p><code>ureadahead</code> [<i>OPTIONS</i>]&#8230; [<i>PACK</i>]</p>
<h2>Description</h2>
<p><code>ureadahead</code> (&uuml;ber-readahead) is used during boot to read files in advance of when they are needed such that they are already in the page cache, improving boot performance. </p>
<p> When started without any arguments, it checks for the existance and age of the default pack file <i>/var/lib/ureadahead/pack</i>, and if not present or older than a month, will discard it and retrace the boot sequence. The pack will then contain information about the files opened during boot, and the blocks that were in memory at the completion of the boot. </p>
<p> If the file exists and is newer than a month old, or an alternate <i>PACK</i> path is given on the command-line, the files listed in the pack are opened and the blocks read into the page cache using the <code><a href="/docs/linux/man/2-readahead/">readahead</a></code>(2) system call. </p>
<p> Pack files are automatically optimised for Solid-State Disks or rotational Hard Drives, depending on which you have.</p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;verbose</code></p>
<dd>May be used to report on <code>ureadahead</code>&#8216;s operation. In particular, this causes information about the size of the pack file to be output when reading and a complete dump of the contents of the pack file after tracing.</p>
<dt><code>&#8211;daemon</code></p>
<dd>Places <code>ureadahead</code> into the background once the pack file has been read, or once tracing has been enabled. </p>
<p> This is ignored when reading on rotational hard drives, since it&#8217;s important for performance reasons not to contend with other processes for I/O.</p>
<dt><code>&#8211;force-trace</code></p>
<dd>Discards all pack files and forces re-tracing.</p>
<dt><code>&#8211;timeout</code>=<i>SECONDS</i></p>
<dd>Normally when tracing, <code>ureadahead</code> will wait for a <i>TERM</i> or <i>INT</i> signal before concluding and generating the pack file. This option instead sets a timeout after which tracing is terminated.</p>
<dt><code>&#8211;dump</code></p>
<dd>Dump the contents of the pack file to standard output in a pretty format, does not trace or read the contents into memory.</p>
<dt><code>&#8211;sort</code>=<i>SORT</i></p>
<dd>Used with <code>&#8211;dump</code> to sort the output. </p>
<p> The default is <i>open</i>, which is the order that the files will be opened. <i>path</i> sorts by path name, <i>disk</i> sorts by on-disk location, and <i>size</i> sorts by the amount of data that will be read for that file.</dl>
<h2>Other Mount Points</h2>
<p><i>PACK</i> need not be the filename of a pack, instead it may be the name of a mount point (or indeed any non-file within the filesystem), in which case the pack for that device is read instead. This allows <code>ureadahead</code> to be called in the style <code>ureadahead</code><i> /usr</i> for filesystems split across multiple devices. </p>
<p> Pack files for these other devices are also stored under <i>/var/lib/ureadahead</i> and are named <code>mountpoint</code><i>.pack</i> </p>
<p> When tracing, these will be automatically generated.</p>
<h2>Files</h2>
<p><i>/var/lib/ureadahead/pack</i></p>
<h2>Author</h2>
<p>Written by Scott James Remnant &lt;<code>scott [at] netsplit.com</code>&gt;</p>
<h2>Bugs</h2>
<p>Report bugs at &lt;<code><a rel="nofollow" href="https://launchpad.net/ubuntu/+source/ureadahead/+bugs">https://launchpad.net/ubuntu/+source/ureadahead/+bugs</a></code>&gt;</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2009 Canonical Ltd. </p>
<p> This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/2-readahead/">readahead</a></code>(2) </p>
