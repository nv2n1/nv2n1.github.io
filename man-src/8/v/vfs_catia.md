---
title: "vfs_catia(8)"
name: "vfs_catia"
section: "8"
letter: "v"
url: "/docs/linux/man/8-vfs_catia/"
description: "vfs_catia – translate illegal characters in Catia filenames"
---

<p>vfs_catia &#8211; translate illegal characters in Catia filenames</p>
<h2>Synopsis</h2>
<dl>
<dd>vfs objects = catia</dl>
<h2>Description</h2>
<p>This VFS module is part of the <code><a href="/docs/linux/man/7-samba/">samba</a></code>(7) suite. </p>
<p> The Catia CAD package commonly creates filenames that use characters that are illegal in CIFS filenames. The vfs_catia VFS module implements a character mapping so that these files can be shared with CIFS clients. </p>
<p> This module is stackable. </p>
<p> The parameter &quot;catia:mappings&quot; specifies the mapping on a per-character basis, see below.</p>
<h2>Options</h2>
<p>catia:mappings = SERVER_HEX_CHAR:CLIENT_HEX_CHAR</p>
<dl>
<dd>SERVER_HEX_CHAR specifies a 0x prefixed hexedecimal character code that, when included in a Samba server-side filename, will be mapped to CLIENT_HEX_CHAR for the CIFS client. </p>
<p> The same mapping occurs in the opposite direction. Multiple character mappings are separated by a comma.</dl>
<h2>Examples</h2>
<p>Map server-side quotation-marks (&quot;) to client-side diaeresis (ad) on filenames in the [CAD] share: </p>
<dl>
<dd>
<pre> <i>[CAD]</i>
 m[blue]<code>path = /data/cad</code>m[]
 m[blue]<code>vfs objects = catia</code>m[]
 m[blue]<code>catia:mappings = 0x22:0xa8</code>m[]</pre>
</dl>
<p> Perform comprehensive mapping of common Catia filename characters: </p>
<dl>
<dd>
<pre> <i>[CAD]</i>
 m[blue]<code>path = /data/cad</code>m[]
 m[blue]<code>vfs objects = catia</code>m[]
 m[blue]<code>catia:mappings = 0x22:0xa8,0x2a:0xa4,0x2f:0xf8,0x3a:0xf7,0x3c:0xab,0x3e:0xbb,0x3f:0xbf,0x5c:0xff,0x7c:0xa6</code>m[]</pre>
</dl>
<p> Server-side filename to be translated (Note that the path delimiter &quot;/&quot; is not used here): </p>
<p> a:a*a?a&quot;a&lt;a&gt;a|a </p>
<p> Resulting filename, as seen by the client: </p>
<p> aÿa&#247;a&curren;a&iquest;aada&laquo;a&raquo;a|a</p>
<h2>Caveats</h2>
<p>Character mapping must work in BOTH directions (server -&gt; client and client -&gt; server) to get unique and existing file names! </p>
<p> A NOT working example: </p>
<dl>
<dd>
<pre> <i>[CAD]</i>
 m[blue]<code>path = /data/cad</code>m[]
 m[blue]<code>vfs objects = catia</code>m[]
 m[blue]<code>catia:mappings = 0x3a:0x5f</code>m[]</pre>
</dl>
<p> Here the colon &quot;:&quot; is mapped to the underscore &quot;_&quot;. </p>
<p> Assuming a server-side filename &quot;a:should_work&quot;, which is translated to &quot;a_should_work&quot; for the client. </p>
<p> BUT the reverse mapping from client &quot;a_should_work&quot; to server will result in &quot;a:should:work&quot; &#8211; something like &quot;file not found&quot; will be returned.</p>
<h2>Version</h2>
<p>This man page is correct for Samba versions from 3.5.0 to 4.0.6.</p>
<h2>Author</h2>
<p>The original Samba software and related utilities were created by Andrew Tridgell. Samba is now developed by the Samba Team as an Open Source project similar to the way the Linux kernel is developed. </p>
<p> New version written by Guenter Kukkukk kukks [at] samba.org</p>
