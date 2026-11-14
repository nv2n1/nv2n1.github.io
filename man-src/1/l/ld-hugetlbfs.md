---
title: "ld-hugetlbfs(1)"
name: "ld-hugetlbfs"
section: "1"
letter: "l"
url: "/docs/linux/man/1-ld-hugetlbfs/"
description: "ld.hugetlbfs – link a program for huge pages"
---

<p>ld.hugetlbfs &#8211; link a program for huge pages </p>
<h2>Synopsis</h2>
<p><code>ld.hugetlbfs [options]</code></p>
<h2>Description</h2>
<p><code>ld.hugetlbfs</code> replaces the normal <code>ld</code> command for linking programs to use hugepages. Under gcc, you should use the option <code>-B /usr/share/libhugetlbfs</code> which tells gcc to look in a non-standard location for the linker. This could be set in the <code>CFLAGS</code> environment variable. </p>
<dl>
<dt><code>-Wl,&#8211;hugetlbfs-align</code></p>
<dd>This method of linking an application permits greater flexibility at runtime. Using HUGETLB_ELFMAP, it is possible to control which program segments are placed in hugepages. The following four settings will cause the indicated segments to be placed in hugepages: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>HUGETLB_ELFMAP=R&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Read-only segments&nbsp;<wbr>(text)<br />
&nbsp;<wbr>&nbsp;<wbr>HUGETLB_ELFMAP=W&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Writable segments&nbsp;<wbr>(data/BSS)<br />
&nbsp;<wbr>&nbsp;<wbr>HUGETLB_ELFMAP=RW&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>All segments&nbsp;<wbr>(text/data/BSS)<br />
&nbsp;<wbr>&nbsp;<wbr>HUGETLB_ELFMAP=no&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>No segments </p>
<p> It is possible to select specific huge page sizes for read-only and writable segments by using the following advanced syntax: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>HUGETLB_ELFMAP=[R[=&lt;pagesize&gt;]:[W[=&lt;pagesize&gt;]] </p>
<p> <code>-Wl,&#8211;hugetlbfs-link=B</code> </p>
<p> Under binutils 2.16 or older, this option will link the application to store BSS data (only) into hugepages. </p>
<p> <code>-Wl,&#8211;hugetlbfs-link=BDT</code> </p>
<p> Under binutils 2.16 or older, this option will link the application to store text, initialized data and BSS data into hugepages. </p>
</dl>
<h2>Files</h2>
<p>[DESTDIR|/usr/share]/doc/libhugetlbfs/HOWTO </p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/7-libhugetlbfs/">libhugetlbfs</a>(7),</i> <i><a href="/docs/linux/man/8-hugectl/">hugectl</a>(8),</i> <i><a href="/docs/linux/man/8-hugeedit/">hugeedit</a>(8)</i> </p>
<h2>Authors</h2>
<p>libhugetlbfs was written by various people on the libhugetlbfs-devel mailing list.</p>
