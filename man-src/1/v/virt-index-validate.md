---

title: "virt-index-validate(1)"
name: "virt-index-validate"
section: "1"
letter: "v"
url: "/docs/linux/man/1-virt-index-validate/"
description: "virt-index-validate – Validate virt-builder index file"
---

<p> virt-index-validate &#8211; Validate virt-builder index file </p>
<h2>SYNOPSIS</h2>
<pre>
 virt-index-validate index
</pre>
<h2>DESCRIPTION</h2>
<p> <i><a href="/docs/linux/man/1-virt-builder/">virt-builder</a></i>(1) uses an index file to store metadata about templates that it knows how to use. This index file has a specific format which virt-index-validate knows how to validate. </p>
<p> Note that virt-index-validate can validate either the signed or unsigned index file (ie. either <i>index</i> or <i>index.asc</i>). It can only validate a local file, not a <font SIZE="-1">URL.</font></p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;compat-1.24.0</code></dt>
<dd> Check for compatibility with virt-builder 1.24.0. (Using this option implies <i>&#8211;compat-1.24.1</i>, so you don&#8217;t need to use both.) </dd>
<p> In particular:</p>
<dl>
<dl>
<dt>&bull;</dt>
<dd> This version of virt-builder could not handle <tt>&quot;[...]&quot;</tt> (square brackets) in field names (eg. <tt>&quot;checksum[sha512]=...&quot;</tt>).</dd>
<dt>&bull;</dt>
<dd> It required detached signatures (<tt>&quot;sig=...&quot;</tt>).</dd></dl>
</dl>
<dl>
</dl>
<dt><code>&#8211;compat-1.24.1</code></dt>
<dd> Check for compatibility with virt-builder ≥ 1.24.1. </dd>
<p> In particular:</p>
<dl>
<dl>
<dt>&bull;</dt>
<dd> This version of virt-builder could not handle <tt>&quot;.&quot;</tt> (period) in field names or <tt>&quot;,&quot;</tt> (comma) in subfield names.</dd>
<dt>&bull;</dt>
<dd> It could not handle comments appearing in the file.</dd></dl>
</dl>
<dl>
</dl>
<dt><code>&#8211;help</code></dt>
<dd> Display help.</dd>
<dt><code>-V</code></dt>
<dd>
</dd><dt><code>&#8211;version</code></dt>
<dd> Display version number and exit.</dd></dl>
<h2>EXIT STATUS</h2>
<p> This program returns 0 if the index file validates, or non-zero if there was an error.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-virt-builder/">virt-builder</a></i>(1), <a rel="nofollow" href="http://libguestfs.org/.">http://libguestfs.org/.</a></p>
<h2>AUTHOR</h2>
<p> Richard W.M. Jones <a rel="nofollow" href="http://people.redhat.com/~rjones/">http://people.redhat.com/~rjones/</a></p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2013 Red Hat Inc.</p>
<h2>LICENSE</h2>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but <font SIZE="-1">WITHOUT ANY WARRANTY</font>; without even the implied warranty of <font SIZE="-1">MERCHANTABILITY</font> or <font SIZE="-1">FITNESS FOR A PARTICULAR PURPOSE. </font> See the <font SIZE="-1">GNU</font> General Public License for more details. </p>
<p> You should have received a copy of the <font SIZE="-1">GNU</font> General Public License along with this program; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, <font SIZE="-1">MA 02110-1301 USA.</font></p>
<h2>BUGS</h2>
<p> To get a list of bugs against libguestfs, use this link: <a rel="nofollow" href="https://bugzilla.redhat.com/buglist.cgi?component=libguestfs">https://bugzilla.redhat.com/buglist.cgi?component=libguestfs</a>&amp;product=Virtualization+Tools </p>
<p> To report a new bug against libguestfs, use this link: <a rel="nofollow" href="https://bugzilla.redhat.com/enter_bug.cgi?component=libguestfs">https://bugzilla.redhat.com/enter_bug.cgi?component=libguestfs</a>&amp;product=Virtualization+Tools </p>
<p> When reporting a bug, please supply:</p>
<dl>
<dt>&bull;</dt>
<dd> The version of libguestfs.</dd>
<dt>&bull;</dt>
<dd> Where you got libguestfs (eg. which Linux distro, compiled from source, etc)</dd>
<dt>&bull;</dt>
<dd> Describe the bug accurately and give a way to reproduce it.</dd>
<dt>&bull;</dt>
<dd> Run <i><a href="/docs/linux/man/1-libguestfs-test-tool/">libguestfs-test-tool</a></i>(1) and paste the <code>complete, unedited</code> output into the bug report. </dd>
</dl>
