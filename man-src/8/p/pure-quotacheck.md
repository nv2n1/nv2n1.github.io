---
title: "pure-quotacheck(8)"
name: "pure-quotacheck"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pure-quotacheck/"
description: "pure-quotacheck – Update virtual quota files for Pure-FTPd"
---

<p>pure-quotacheck &#8211; Update virtual quota files for Pure-FTPd</p>
<h2>Syntax</h2>
<p>pure-quotacheck <i>-u username/gid</i> <i>-d home directory</i> [<i>-g group/gid</i>]</p>
<h2>Description</h2>
<p>pure-quotacheck create a <code>.ftpquota</code> file in the specified directory.<br />
 This file contains the current file and size of the directory, and it is used by Pure-FTPd when virtual quotas are enabled.<br />
 It&#8217;s recommended to periodically run pure-quotacheck for every user, in crontabs.</p>
<h2>Options</h2>
<dl>
<dt><code>-d</code> &lt;<i>directory</i>&gt;</p>
<dd>Scans the specified &lt;<i>directory</i>&gt;.</p>
<dt><code>-g</code> &lt;<i>group or gid</i>&gt;</p>
<dd>Sets the group files will be scanned as. This is optional : if a user name is passed to <code>-u&lt;/fR&gt;, group are automatically retrieved.</p>
<dt>-u</code> &lt;<i>user or uid</i>&gt;</p>
<dd>Set the user name files will be scanned as. This is mandatory, and it can&#8217;t be &quot;root&quot;.</p>
<dt><code>-h</code></p>
<dd>Output usage information and exit.</dl>
<h2>Files</h2>
<p><i>.ftpquota</i></p>
<h2>Examples</h2>
<p>To run this program the standard way type: </p>
<p> pure-quotacheck -u john -d /home/john</p>
<h2>Authors</h2>
<p>Frank DENIS &lt;j at pureftpd dot org&gt;</p>
<h2>Security</h2>
<p>pure-quotacheck switches real and effective uids/gids as soon as possible. Root privileges are never given back.<br />
 pure-quotacheck refuses to scan directories with uid = 0 (root) or gid = 0 (wheel/root) .<br />
 pure-quotacheck performs a chroot() call to the home directory. It never traverses parent directories.<br />
 pure-quotacheck only scans real files (no socket, no pipe, etc) .<br />
 pure-quotacheck enforces read access on directories to prevent against people doing chmod 0 before a quota scan.<br />
 pure-quotacheck enforces write access on the home directory to properly write the .ftpquota file.<br />
 pure-quotacheck never scans the same inode/device pair twice.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-ftp/">ftp</a>(1)</code>, <code><a href="/docs/linux/man/8-pure-ftpd/">pure-ftpd</a>(8)</code> <code><a href="/docs/linux/man/8-pure-ftpwho/">pure-ftpwho</a>(8)</code> <code><a href="/docs/linux/man/8-pure-mrtginfo/">pure-mrtginfo</a>(8)</code> <code><a href="/docs/linux/man/8-pure-uploadscript/">pure-uploadscript</a>(8)</code> <code><a href="/docs/linux/man/8-pure-statsdecode/">pure-statsdecode</a>(8)</code> <code><a href="/docs/linux/man/8-pure-pw/">pure-pw</a>(8)</code> <code><a href="/docs/linux/man/8-pure-quotacheck/">pure-quotacheck</a>(8)</code> <code><a href="/docs/linux/man/8-pure-authd/">pure-authd</a>(8)</code> <code>RFC 959,</code> <code>RFC 2228,</code> <code>RFC 2389</code> and <code>RFC 2428</code>. </p>
