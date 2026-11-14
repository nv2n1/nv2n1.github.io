---
title: "amdump_client(8)"
name: "amdump_client"
section: "8"
letter: "a"
url: "/docs/linux/man/8-amdump_client/"
description: "amdump_client – back up all disks in an Amanda configuration"
---

<p>amdump_client &#8211; back up all disks in an Amanda configuration</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>amdump_client</code> [<code>-o</code>&nbsp;<wbr><i>configoption</i>&#8230;] [<code>&#8211;config</code>&nbsp;<wbr><i>config</i>] <i>CMD</i> [<i>diskname</i>&#8230;]</dl>
<h2>Description</h2>
<p><code>Amdump_client</code></p>
<dd>initiate backup on the client. There are three commands (CMD): </p>
<p> <code>list</code></p>
<dl>
<dd>list all diskname that can be dumped.</dl>
<p> <code>check</code></p>
<dl>
<dd>Check the configuration of the client and disk.</dl>
<p> <code>dump</code></p>
<dl>
<dd>Start a backup of the specified diskname, or all diskname if none are specified.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-amanda/">amanda</a></code>(8), <code><a href="/docs/linux/man/8-amdump/">amdump</a></code>(8), <code><a href="/docs/linux/man/7-amanda-match/">amanda-match</a></code>(7) </p>
<p> The Amanda Wiki: : <a rel="nofollow" href="http://wiki.zmanda.com/">http://wiki.zmanda.com/</a></p>
<h2>Author</h2>
<p><code>Jean-Louis Martineau</code> &lt;martineau [at] zmanda.com&gt;</p>
<dl>
<dd>Zmanda, Inc. (<a rel="nofollow" href="http://www.zmanda.com)">http://www.zmanda.com)</a></dl>
