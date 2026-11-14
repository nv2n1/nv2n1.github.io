---
title: "febootstrap-minimize(8)"
name: "febootstrap-minimize"
section: "8"
letter: "f"
url: "/docs/linux/man/8-febootstrap-minimize/"
description: "febootstrap-minimize – Minimize an febootstrap image"
---

<p>febootstrap-minimize &#8211; Minimize an febootstrap image</p>
<h2>Synopsis</h2>
<pre> febootstrap-minimize [--options] DIR</pre>
<h2>Description</h2>
<p><i>febootstrap-minimize</i> minimizes an <i><a href="/docs/linux/man/8-febootstrap/">febootstrap</a></i>(8)-created filesystem. This means that unneeded files and cruft are removed from the image. </p>
<p> If no options are given, the default is to minimize the image as much as possible. This means, for example, that locales are removed so the image will only be usable in US-English, there will be no documentation or manual pages, and the image will only work in a <font SIZE="-1">UTC</font> timezone. </p>
<p> Note that image minimization involves deleting files that have been installed by <font SIZE="-1">RPM</font>. Thus after minimization, it is no longer guaranteed that <font SIZE="-1">RPM</font> will function correctly on the image. You should only do this as a final step for &#8220;throwaway&#8221; appliances that do not need to be modified or upgraded in future.</p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;all</code></p>
<dd>Perform all minimization operations, to produce the smallest possible image. Note in particular that locales are discarded. </p>
<p> You can perform all minimization operations <i>except</i> X, Y and Z by doing: </p>
<pre> febootstrap-minimize --all --keep-X --keep-Y --keep-Z ...</pre>
<p>(<tt>&quot;--all&quot;</tt> can be omitted since it is the default).</p>
<dt><code>&#8211;none</code></p>
<dd>Start with no minimization operations. You can specify <i>only</i> minimization operations X, Y and Z like this: </p>
<pre> febootstrap-minimize --none --drop-X --drop-Y --drop-Z ...</pre>
<dt><code>&#8211;keep-locales</code></p>
<dd>
<dt><code>&#8211;drop-locales</code></p>
<dd>Keep or drop locale support.</p>
<dt><code>&#8211;keep-docs</code></p>
<dd>
<dt><code>&#8211;drop-docs</code></p>
<dd>Keep or drop documentation, man pages and info files.</p>
<dt><code>&#8211;keep-cracklib</code></p>
<dd>
<dt><code>&#8211;drop-cracklib</code></p>
<dd>Keep or drop cracklib libraries.</p>
<dt><code>&#8211;keep-i18n</code></p>
<dd>
<dt><code>&#8211;drop-i18n</code></p>
<dd>Keep or drop <tt>&quot;/usr/share/i18n&quot;</tt>.</p>
<dt><code>&#8211;keep-zoneinfo</code></p>
<dd>
<dt><code>&#8211;drop-zoneinfo</code></p>
<dd>Keep or drop all timezones (except <font SIZE="-1">UTC</font> which is never deleted).</p>
<dt><code>&#8211;keep-rpmdb</code></p>
<dd>
<dt><code>&#8211;drop-rpmdb</code></p>
<dd>Keep or drop the <font SIZE="-1">RPM</font> and <font SIZE="-1">YUM</font> package databases. Obviously <font SIZE="-1">RPM</font> and <font SIZE="-1">YUM</font> will be completely non-functional if you drop these.</p>
<dt><code>&#8211;keep-yum-cache</code></p>
<dd>
<dt><code>&#8211;drop-yum-cache</code></p>
<dd>Keep or drop the yum cache. Note that <i><a href="/docs/linux/man/8-febootstrap/">febootstrap</a></i>(8) has already deleted this directory unless you ran it with the <tt>&quot;--no-clean&quot;</tt> option.</p>
<dt><code>&#8211;keep-services</code></p>
<dd>
<dt><code>&#8211;drop-services</code></p>
<dd>Keep or drop the <tt>&quot;/etc/services&quot;</tt> file. If dropped, this file is replaced with a very minimal one which just lists the most common services. For less common services you will have to refer to them by port number instead of name.</p>
<dt><code>&#8211;keep-sln</code></p>
<dd>
<dt><code>&#8211;drop-sln</code></p>
<dd>Keep or drop <tt>&quot;/sbin/sln&quot;</tt> (statically linked <tt>&quot;ln&quot;</tt>). This is not really required in minimal appliances.</p>
<dt><code>&#8211;keep-ldconfig</code></p>
<dd>
<dt><code>&#8211;drop-ldconfig</code></p>
<dd>Keep or drop <tt>&quot;/sbin/ldconfig&quot;</tt>, <tt>&quot;/etc/ld.so.cache&quot;</tt> and <tt>&quot;/var/cache/ldconfig&quot;</tt> (the dynamic linking cache). This is not needed. Dynamic linking during program execution will be marginally slower.</p>
<dt><code>&#8211;pack-executables</code></p>
<dd>This option has been removed in febootstrap 2.5. In previous versions it was used to pack executables using the external <tt>&quot;upx&quot;</tt> program. However it was not enabled by default and never worked very effectively.</dl>
<h2>Todo</h2>
<dl>
<dt>*</p>
<dd>Deduplicate files with the same content (by hardlinking them). See the program <i><a href="/docs/linux/man/1-hardlink/">hardlink</a></i>(1).</p>
<dt>*</p>
<dd>Remove unused binaries.</p>
<dt>*</p>
<dd>Remove unused libraries.</dl>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/8-febootstrap/">febootstrap</a></i>(8).</p>
<h2>Authors</h2>
<p>Richard W.M. Jones &lt;rjones @ redhat . com&gt;</p>
<h2>Copyright</h2>
<p>(C) Copyright 2009 Red Hat Inc., &lt;<a rel="nofollow" href="http://et.redhat.com/~rjones/febootstrap">http://et.redhat.com/~rjones/febootstrap</a>&gt;. </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but <font SIZE="-1">WITHOUT</font> <font SIZE="-1">ANY</font> <font SIZE="-1">WARRANTY</font>; without even the implied warranty of <font SIZE="-1">MERCHANTABILITY</font> or <font SIZE="-1">FITNESS</font> <font SIZE="-1">FOR</font> A <font SIZE="-1">PARTICULAR</font> <font SIZE="-1">PURPOSE</font>. See the <font SIZE="-1">GNU</font> General Public License for more details. </p>
<p> You should have received a copy of the <font SIZE="-1">GNU</font> General Public License along with this program; if not, write to the Free Software Foundation, Inc., 675 Mass Ave, Cambridge, <font SIZE="-1">MA</font> 02139, <font SIZE="-1">USA</font>.</p>
