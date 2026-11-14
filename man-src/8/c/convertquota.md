---
title: "convertquota(8)"
name: "convertquota"
section: "8"
letter: "c"
url: "/docs/linux/man/8-convertquota/"
description: "convertquota – convert quota from old file format to new one"
---

<p>convertquota &#8211; convert quota from old file format to new one</p>
<h2>Synopsis</h2>
<p><code>convertquota</code> [ <code>-ug</code> ] <code>-e</code> <i>filesystem</i> </p>
<p> <code>convertquota</code> [ <code>-ug</code> ] <code>-f</code> <i>oldformat</i>,<i>newformat</i> <i>filesystem</i></p>
<h2>Description</h2>
<p><code>convertquota</code> converts old quota files <code>quota.user</code> and <code>quota.group</code> to files <code>aquota.user</code> and <code>aquota.group</code> in new format currently used by 2.4.0-ac? and newer or by SuSE or Red Hat Linux 2.4 kernels on <i>filesystem</i>. </p>
<p> New file format allows using quotas for 32-bit uids / gids, setting quotas for root, accounting used space in bytes (and so allowing use of quotas in ReiserFS) and it is also architecture independent. This format introduces Radix Tree (a simple form of tree structure) to quota file.</p>
<h2>Options</h2>
<dl>
<dt><code>-u, &#8211;user</code></p>
<dd>convert user quota file. This is the default.</p>
<dt><code>-g, &#8211;group</code></p>
<dd>convert group quota file.</p>
<dt><code>-f, &#8211;convert-format </code><i>oldformat,newformat</i></p>
<dd>convert quota file from <i>oldformat</i> to <i>newformat</i>.</p>
<dt><code>-e, &#8211;convert-endian</code></p>
<dd>convert vfsv0 file format from big endian to little endian (old kernels had a bug and did not store quota files in little endian format).</p>
<dt><code>-V, &#8211;version</code></p>
<dd>print version information.</dl>
<h2>Files</h2>
<dl>
<dt><code>aquota.user</code></p>
<dd>new user quota file</p>
<dt><code>aquota.group</code></p>
<dd>new group quota file</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-quota/">quota</a></code>(1), <code><a href="/docs/linux/man/8-setquota/">setquota</a></code>(8), <code><a href="/docs/linux/man/8-edquota/">edquota</a></code>(8), <code><a href="/docs/linux/man/8-quotacheck/">quotacheck</a></code>(8), <code><a href="/docs/linux/man/8-quotaon/">quotaon</a></code>(8), <code><a href="/docs/linux/man/8-repquota/">repquota</a></code>(8)</p>
<h2>Author</h2>
<p>Jan Kara &lt;jack [at] suse.cz&gt;</p>
