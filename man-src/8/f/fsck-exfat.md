---
title: "fsck-exfat(8)"
name: "fsck-exfat"
section: "8"
letter: "f"
url: "/docs/linux/man/8-fsck-exfat/"
description: "exfatfsck – check an exFAT file system"
---

<p><code>exfatfsck</code> &#8211; check an exFAT file system</p>
<h2>Synopsis</h2>
<p><code>exfatfsck</code> [ <code>-a</code> | <code>-n</code> | <code>-p</code> | <code>-y</code> ] <i>device</i><br/>
 <code>exfatfsck</code> [ <code>-V</code> ] </p>
<h2>Description</h2>
<p><code>exfatfsck</code> checks an exFAT file system for errors. It can repair some of them. </p>
<h2>Command Line Options</h2>
<p>Command line options available:</p>
<dl>
<dt><code>-a</code></dt>
<dd>Automatically repair the file system. No user intervention required.</dd>
<dt><code>-n</code></dt>
<dd>No-operation mode: non-interactively check for errors, but don&#8217;t write anything to the file system.</dd>
<dt><code>-p</code></dt>
<dd>Same as <code>-a</code> for compatibility with other *fsck.</dd>
<dt><code>-V</code></dt>
<dd>Print version and copyright.</dd>
<dt><code>-y</code></dt>
<dd>Same as <code>-a</code> for compatibility with other *fsck. </dd>
</dl>
<h2>Exit Codes</h2>
<p>Zero is returned if errors were not found. Any other code means an error.</p>
<h2>Author</h2>
<p>Andrew Nayenko</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-fsck/">fsck</a></code>(8) </p>
