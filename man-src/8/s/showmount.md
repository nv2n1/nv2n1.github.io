---
title: "showmount(8)"
name: "showmount"
section: "8"
letter: "s"
url: "/docs/linux/man/8-showmount/"
description: "showmount – show mount information for an NFS server"
---

<p>showmount &#8211; show mount information for an NFS server</p>
<h2>Synopsis</h2>
<p><code>showmount</code> <code>[&nbsp;<wbr>-adehv&nbsp;<wbr>]</code> <code>[&nbsp;<wbr>&#8211;all&nbsp;<wbr>]</code> <code>[&nbsp;<wbr>&#8211;directories&nbsp;<wbr>]</code> <code>[&nbsp;<wbr>&#8211;exports&nbsp;<wbr>]</code> <code>[&nbsp;<wbr>&#8211;help&nbsp;<wbr>]</code> <code>[&nbsp;<wbr>&#8211;version&nbsp;<wbr>]</code> <code>[&nbsp;<wbr>host&nbsp;<wbr>]</code></p>
<h2>Description</h2>
<p><code>showmount</code> queries the mount daemon on a remote host for information about the state of the NFS server on that machine. With no options <code>showmount</code> lists the set of clients who are mounting from that host. The output from <code>showmount</code> is designed to appear as though it were processed through &#8220;sort -u&#8221;.</p>
<h2>Options</h2>
<dl>
<dt><code>-a</code> or <code>&#8211;all</code></dt>
<dd>List both the client hostname or IP address and mounted directory in host:dir format. This info should not be considered reliable. See the notes on rmtab in <code>rpc.mountd</code>(8).</dd>
<dt><code>-d</code> or <code>&#8211;directories</code></dt>
<dd>List only the directories mounted by some client.</dd>
<dt><code>-e</code> or <code>&#8211;exports</code></dt>
<dd>Show the NFS server&#8217;s export list.</dd>
<dt><code>-h</code> or <code>&#8211;help</code></dt>
<dd>Provide a short help summary.</dd>
<dt><code>-v</code> or <code>&#8211;version</code></dt>
<dd>Report the current version number of the program.</dd>
<dt><code>&#8211;no-headers</code></dt>
<dd>Suppress the descriptive headings from the output.</dd></dl>
<h2>See Also</h2>
<p><code>rpc.mountd</code>(8), <code>rpc.nfsd</code>(8)</p>
<h2>Bugs</h2>
<p>The completeness and accuracy of the information that <code>showmount</code> displays varies according to the NFS server&#8217;s implementation. </p>
<p> Because <code>showmount</code> sorts and uniqs the output, it is impossible to determine from the output whether a client is mounting the same directory more than once.</p>
<h2>Author</h2>
<p>Rick Sladkey &lt;jrs [at] world.std.com&gt;</p>
