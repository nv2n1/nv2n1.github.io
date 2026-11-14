---
title: "blkmapd(8)"
name: "blkmapd"
section: "8"
letter: "b"
url: "/docs/linux/man/8-blkmapd/"
description: "blkmapd – pNFS block layout mapping daemon"
---

<p>blkmapd &#8211; pNFS block layout mapping daemon</p>
<h2>Synopsis</h2>
<p><code>blkmapd [-h] [-d] [-f]</code></p>
<h2>Description</h2>
<p>The <code>blkmapd</code> daemon performs device discovery and mapping for the parallel NFS (pNFS) block layout client [RFC5663]. </p>
<p> The pNFS block layout protocol builds a complex storage hierarchy from a set of <i>simple volumes.</i> These simple volumes are addressed by content, using a signature on the volume to uniquely name each one. The daemon locates a volume by examining each block device in the system for the given signature. </p>
<p> The topology typically consists of a hierarchy of volumes built by striping, slicing, and concatenating the simple volumes. The <code>blkmapd</code> daemon uses the device-mapper driver to construct logical devices that reflect the server topology, and passes these devices to the kernel for use by the pNFS block layout client.</p>
<h2>Options</h2>
<dl>
<dt><code>-h</code></p>
<dd>Display usage message.</p>
<dt><code>-d</code></p>
<dd>Performs device discovery only then exits.</p>
<dt><code>-f</code></p>
<dd>Runs <code>blkmapd</code> in the foreground and sends output to stderr (as opposed to syslogd)</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-nfs/">nfs</a></code>(5), <code><a href="/docs/linux/man/8-dmsetup/">dmsetup</a></code>(8) </p>
<p> RFC 5661 for the NFS version 4.1 specification.<br />
 RFC 5663 for the pNFS block layout specification.</p>
<h2>Authors</h2>
<p>Haiying Tang &lt;Tang_Haiying [at] emc.com&gt;<br />
 Jim Rees &lt;rees [at] umich.edu&gt;</p>
