---
title: "fusesmb(1)"
name: "fusesmb"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fusesmb/"
description: "fusesmb – Mount network neighbourhood"
---

<h2 class="name">NAME</h2>
<p> fusesmb &#8211; Mount network neighbourhood</p>
<h2>SYNOPSIS</h2>
<p> <code>fusesmb</code> <i>mountpoint</i> [options]</p>
<h2>DESCRIPTION</h2>
<p> <code>fusesmb</code> is a Network Neighborhood (Samba shares) filesystem. It works like smbfs, but instead of accessing one share at a time, all computers and workgroups are accessible at once from a single filesystem mount. </p>
<h2>OPTIONS</h2>
<p> <code>fusesmb</code> accepts the following options:</p>
<dl>
<dt><code>-h</code></p>
<dd> Show summary of options. </p>
</dl>
<h2>FILES</h2>
<dl>
<dt><i>~/.smb/fusesmb.conf</i></p>
<dd> Configuration file for <code>fusesmb</code>. Make sure that this file is only readable by the owner or else fusesmb will not start. </p>
<dt><i>~/.smb/fusesmb.cache</i></p>
<dd> A sorted list of all workgroups, servers and shares found on your network. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-fusesmb-conf/">fusesmb.conf</a></code>(5) </p>
<h2>AUTHOR</h2>
<p> Vincent Wagelaar &lt;vincent [at] ricardis.tudelft.nl&gt;. </p>
<h2>Index</h2>
