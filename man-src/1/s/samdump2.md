---

title: "samdump2(1)"
name: "samdump2"
section: "1"
letter: "s"
url: "/docs/linux/man/1-samdump2/"
description: "samdump2 retrieves syskey and extract hashes from Windows 2k/NT/XP/Vista SAM."
---

<p> <code>samdump2</code> retrieves syskey and extract hashes from Windows 2k/NT/XP/Vista SAM. </p>
<h2>SYNOPSIS</h2>
<p> samdump2 [-d] [-o file] &lt;system hive&gt; &lt;sam hive&gt;</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-d</code></dt>
<dd> enable debugging</dd>
<dt><code>-h</code></dt>
<dd> display this help</dd>
<dt><code>-o file</code></dt>
<dd> write output to file</dd></dl>
<h2>EXAMPLE</h2>
<p> samdump2 -o out /mnt/ntfs/WINDOWS/system32/config/SYSTEM /mnt/ntfs/WINDOWS/system32/config/sam</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Adam Cecile &lt;gandalf [at] le-vert.net&gt; for the Debian system (but may be used by others) and modified by Objectif Securite &lt;info [at] objectif-securite.ch&gt; Permission is granted to copy, distribute and/or modify this document under the terms of the GNU General Public License, Version 2 or any later version published by the Free Software Foundation On Debian systems, the complete text of the GNU General Public License can be found in /usr/share/common-licenses/GPL.</p>
<h2>SEE ALSO</h2>
<p> <code>ophcrack(1)</code> </p>
