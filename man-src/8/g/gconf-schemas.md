---
title: "gconf-schemas(8)"
name: "gconf-schemas"
section: "8"
letter: "g"
url: "/docs/linux/man/8-gconf-schemas/"
description: "gconf-schemas – register gconf schemas with the gconf database"
---

<p>gconf-schemas &#8211; register gconf schemas with the gconf database</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>gconf-schemas</code> [<code>&#8211;register|unregister|register-all</code>] [<i>schema1</i>] [<i>schema2</i>] [<i>&#8230;</i>]</dl>
<h2>Description</h2>
<dd>This manual page documents briefly the <code>gconf-schemas</code> command. </p>
<p> <code>gconf-schemas</code> is used to register gconf schemas with the gconf database.</p>
<h2>Options</h2>
<p><code>&#8211;register</code></p>
<dl>
<dd>register schemas to the GConf database</dl>
<p> <code>&#8211;unregister</code></p>
<dl>
<dd>unregister schemas from the GConf database</dl>
<p> <code>&#8211;register-all</code></p>
<dl>
<dd>clean up the GConf database and register all schemas again. This might be neccessary if your gconf database becomes corrupted.</dl>
<p> <code>&#8211;no-signal</code></p>
<dl>
<dd>do not send SIGHUP to the running gconfd-2 processes.</dl>
<h2>Author</h2>
<p>This manual page was written by Patrick Schoenfeld &lt;schoenfeld [at] in-medias-res.com&gt; for the Debian(TM) system (but may be used by others). Permission is granted to copy, distribute and/or modify this document under the terms of the GNU General Public License, Version 2 any later version published by the Free Software Foundation. </p>
<p> On Debian systems, the complete text of the GNU General Public License can be found in /usr/share/common-licenses/GPL.</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2007 Patrick Schoenfeld</p>
