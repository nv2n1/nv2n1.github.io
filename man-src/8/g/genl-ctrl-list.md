---
title: "genl-ctrl-list(8)"
name: "genl-ctrl-list"
section: "8"
letter: "g"
url: "/docs/linux/man/8-genl-ctrl-list/"
description: "genl-ctrl-list – List available kernel-side Generic Netlink families"
---

<p>genl-ctrl-list &#8211; List available kernel-side Generic Netlink families</p>
<h2>Synopsis</h2>
<p><code>genl-ctrl-list [-d]</code> </p>
<h2>Description</h2>
<p>Queries the Generic Netlink controller in kernel and prints a list of all registered Generic Netlink families including the version of the interface that has been registered. </p>
<h2>Options</h2>
<dl>
<dt><code>-h</code> or <code>&#8211;help</code></p>
<dd>Print help text to console and exit.</p>
<dt><code>-v</code> or <code>&#8211;version</code></p>
<dd>Print versioning information to console and exit.</p>
<dt><code>-d</code> or <code>&#8211;details</code></p>
<dd>Include additional detailed information for each Generic Netlink family that is printed. </p>
<p> The information includes: </p>
<dl>
<dd>
<dl>
<dt><code>hdrsize N</code></p>
<dd>The size of the user specific header. </p>
<dt><code>maxattr N</code></p>
<dd>The maximum Netlink attribute identifier expected by the interface. </p>
<dt><code>op NAME (ID) &lt;FLAGS&gt;</code></p>
<dd>A list of available operations including their name, numeric identifier and the flags indicating the capabilities of the opertion. </p>
<p> Available flags:</p>
<dl>
<dd>
<dl>
<dt><i>admin-perm</i></p>
<dd>Requires administrative privileges </p>
<dt><i>has-doit</i></p>
<dd>Command can handle request </p>
<dt><i>has-dump</i></p>
<dd>Command can handle a dump request </p>
<dt><i>has-policy</i></p>
<dd>Command enforces attribute validation policy</dl>
</dl>
<dt><code>grp NAME (ID)</code></p>
<dd>A list of registered multicast groups including name (if available) and identifier.</dl>
</dl>
<dl>
<dd><code>Example:</code></p>
<dl>
<dd>0x0010 nlctrl version 2</p>
<dl>
<dd>&nbsp;<wbr>hdrsize 0 maxattr 7</p>
<dl>
<dd>op GETFAMILY&nbsp;<wbr>(0x03)&nbsp;<wbr>&lt;has-doit,has-dump,has-policy&gt;</p>
<dl>
<dd>grp notify&nbsp;<wbr>(0x10)</dl>
</dl>
</dl>
</dl>
</dl>
</dl>
<h2>Example</h2>
<dl>
<dd>$ genl-ctrl-list</p>
<dl>
<dd>0x0010 nlctrl version 2</p>
<dl>
<dd>0x0011 NLBL_MGMT version 3</p>
<dl>
<dd>0x0012 NLBL_CIPSOv4 version 3</p>
<dl>
<dd>0x0013 NLBL_UNLBL version 3</p>
<dl>
<dd>0x0014 acpi_event version 1</p>
<dl>
<dd>0x0015 thermal_event version 1</p>
<dl>
<dd>0x0016 VFS_DQUOT version 1</p>
<dl>
<dd>0x0017 TASKSTATS version 1</p>
<dl>
<dd>0x0018 NET_DM version 2 </p>
<h2>Author</h2>
<p>Thomas Graf is the original author and current maintainer of libnl and libnl tools. Many people have contributed to it since.</p>
