---
title: "nbd-trdump(1)"
name: "nbd-trdump"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nbd-trdump/"
description: "nbd-trdump – translate an nbd transaction log into human readable form"
---

<h2>SYNOPSIS</h2>
<p> <code>nbd-trdump</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>nbd-trdump</code> translates a transaction log produced by <code>nbd-server</code> (specifically by the <code>transactionlog</code> configuration directive) into human readable form. </p>
<p> The command acts as a traditional UNIX filter, i.e. the transaction log must be supplied on standard input, and the human readable output is sent to standard output.</p>
<h2>OUTPUT</h2>
<p> The following may be output:</p>
<dl>
<dt><code>&gt;</code></dt>
<dd> A request packet sent from the client to the server.</dd>
<dt><code>&lt;</code></dt>
<dd> A reply packet sent from the server to the client.</dd>
<dt><code>H</code></dt>
<dd> The handle of the packet.</dd>
<dt><code>C</code></dt>
<dd> The command sent.</dd>
<dt><code>O</code></dt>
<dd> The offet from the start of the disk.</dd>
<dt><code>L</code></dt>
<dd> The length of data.</dd>
<dt><code>E</code></dt>
<dd> The error returned.</dd></dl>
<h2>SEE ALSO</h2>
<p> nbd-server (1).</p>
<h2>AUTHOR</h2>
<p> The NBD kernel module and the NBD tools have been written by Pavel Macheck (pavel [at] ucw.cz). </p>
<p> The kernel module is now maintained by Paul Clements (Paul.Clements [at] steeleye.com), while the userland tools are maintained by Wouter Verhelst (wouter [at] debian.org) </p>
<p> This manual page was written by Wouter Verhelst (&lt;wouter [at] debian.org&gt;) for the Debian GNU/Linux system (but may be used by others). Permission is granted to copy, distribute and/or modify this document under the terms of the GNU General Public License, version 2, as published by the Free Software Foundation. </p>
