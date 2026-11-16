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
<dt><code>-h</code> or <code>&#8211;help</code></dt>
<dd>Print help text to console and exit.</dd>
<dt><code>-v</code> or <code>&#8211;version</code></dt>
<dd>Print versioning information to console and exit.</dd>
<dt><code>-d</code> or <code>&#8211;details</code></dt>
<dd>Include additional detailed information for each Generic Netlink family that is printed. </dd>
<p> The information includes: </p>
<dl>
<dd>
</dd><dl>
<dt><code>hdrsize N</code></dt>
<dd>The size of the user specific header. </dd>
<dt><code>maxattr N</code></dt>
<dd>The maximum Netlink attribute identifier expected by the interface. </dd>
<dt><code>op NAME (ID) &lt;FLAGS&gt;</code></dt>
<dd>A list of available operations including their name, numeric identifier and the flags indicating the capabilities of the opertion. </dd>
<p> Available flags:</p>
<dl>
<dd>
</dd><dl>
<dt><i>admin-perm</i></dt>
<dd>Requires administrative privileges </dd>
<dt><i>has-doit</i></dt>
<dd>Command can handle request </dd>
<dt><i>has-dump</i></dt>
<dd>Command can handle a dump request </dd>
<dt><i>has-policy</i></dt>
<dd>Command enforces attribute validation policy</dd></dl>
</dl>
<dt><code>grp NAME (ID)</code></dt>
<dd>A list of registered multicast groups including name (if available) and identifier.</dd></dl>
</dl>
<dl>
<dd><code>Example:</code></dd>
<dl>
<dd>0x0010 nlctrl version 2</dd>
<dl>
<dd>&nbsp;<wbr>hdrsize 0 maxattr 7</dd>
<dl>
<dd>op GETFAMILY&nbsp;<wbr>(0x03)&nbsp;<wbr>&lt;has-doit,has-dump,has-policy&gt;</dd>
<dl>
<dd>grp notify&nbsp;<wbr>(0x10)</dd></dl>
</dl>
</dl>
</dl>
</dl>
</dl>
<h2>Example</h2>
<dl>
<dd>$ genl-ctrl-list</dd>
<dl>
<dd>0x0010 nlctrl version 2</dd>
<dl>
<dd>0x0011 NLBL_MGMT version 3</dd>
<dl>
<dd>0x0012 NLBL_CIPSOv4 version 3</dd>
<dl>
<dd>0x0013 NLBL_UNLBL version 3</dd>
<dl>
<dd>0x0014 acpi_event version 1</dd>
<dl>
<dd>0x0015 thermal_event version 1</dd>
<dl>
<dd>0x0016 VFS_DQUOT version 1</dd>
<dl>
<dd>0x0017 TASKSTATS version 1</dd>
<dl>
<dd>0x0018 NET_DM version 2 </dd>
<h2>Author</h2>
<p>Thomas Graf is the original author and current maintainer of libnl and libnl tools. Many people have contributed to it since.</p>
</dl></dl></dl></dl></dl></dl></dl></dl></dl></dl>