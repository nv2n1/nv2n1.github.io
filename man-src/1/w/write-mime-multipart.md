---

title: "write-mime-multipart(1)"
name: "write-mime-multipart"
section: "1"
letter: "w"
url: "/docs/linux/man/1-write-mime-multipart/"
description: "write-mime-multipart – utilty for creating mime-multipart files, likely for use via user data and cloud-init."
---

<h2>NAME</h2>
<p> <code>write-mime-multipart</code> &#8211; utilty for creating mime-multipart files, likely for use via user data and cloud-init. </p>
<p> <code>write-mime-multipart [options]</code> </p>
<p> This program is intended to help write data that can be consumed by cloud-init. cloud-init reads mime multipart as user-data. </p>
<dl>
<dt><code>-h | &#8211;help</code></dt>
<dd> Show usage message </dd>
<dt><code>-o | &#8211;output FILE</code></dt>
<dd> write output to FILE [default is stdout] </dd>
<dt><code>-z | &#8211;gzip</code></dt>
<dd> compress output with gzip </dd>
<dt><code>-d | &#8211;default DEFTYPE</code></dt>
<dd> if not provided assume mime-type of DEFTYPE [default is &#8216;text/plain&#8217;] </dd>
<dt><code>&#8211;delim DELIM</code></dt>
<dd> use delimiter DELIM [default is &#8216;:&#8217;] </dd>
</dl>
<h2>EXAMPLES</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>write-mime-multipart &#8211;gzip &#8211;output=combined-userdata.txt boothook.txt:text/cloud-boothook include-file.txt:text/x-include-url </p>
<h2>AUTHOR</h2>
<p> This manpage and the utility was written by Scott Moser &lt;scott.moser [at] canonical.com&gt;. Permission is granted to copy, distribute and/or modify this document under the terms of the GNU General Public License, Version 3 published by the Free Software Foundation. </p>
<p> On Debian systems, the complete text of the GNU General Public License can be found in /usr/share/common-licenses/GPL. </p>
