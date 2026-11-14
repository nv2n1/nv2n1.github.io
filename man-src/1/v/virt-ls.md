---
title: "virt-ls(1)"
name: "virt-ls"
section: "1"
letter: "v"
url: "/docs/linux/man/1-virt-ls/"
description: "virt-ls – List files in a virtual machine"
---

<h2 class="name">NAME</h2>
<p> virt-ls &#8211; List files in a virtual machine </p>
<h2>SYNOPSIS</h2>
<pre><code>
virt - ls[--options] - d domname directory[directory...] virt - ls[--options] - a disk.img[-a disk.img...] directory[directory...]
</code></pre>
<p> Old style: </p>
<pre><code>
virt - ls[--options] domname directory virt - ls[--options] disk.img[disk.img...] directory
</code></pre>
<h2>DESCRIPTION</h2>
<p> <tt>&quot;virt-ls&quot;</tt> lists filenames, file sizes, checksums, extended attributes and more from a virtual machine or disk image. </p>
<p> Multiple directory names can be given, in which case the output from each is concatenated. </p>
<p> To list directories from a libvirt guest use the <i>-d</i> option to specify the name of the guest. For a disk image, use the <i>-a</i> option. </p>
<p> <tt>&quot;virt-ls&quot;</tt> can do many simple file listings. For more complicated cases you may need to use <i><a href="/docs/linux/man/1-guestfish/">guestfish</a></i>(1), or write a program directly to the <i><a href="/docs/linux/man/3-guestfs/">guestfs</a></i>(3) <font SIZE="-1">API.</font></p>
<h2>EXAMPLES</h2>
<p> Get a list of all files and directories in a virtual machine: </p>
<pre>
 virt-ls -R -d guest /
</pre>
<p> List all setuid or setgid programs in a Linux virtual machine: </p>
<pre>
 virt-ls -lR -d guest / | grep '^- [42]'
</pre>
<p> List all public-writable directories in a Linux virtual machine: </p>
<pre>
 virt-ls -lR -d guest / | grep '^d ...7'
</pre>
<p> List all Unix domain sockets in a Linux virtual machine: </p>
<pre>
 virt-ls -lR -d guest / | grep '^s'
</pre>
<p> List all regular files with filenames ending in &#8216;.png&#8217;: </p>
<pre>
 virt-ls -lR -d guest / | grep -i '^-.*\.png$'
</pre>
<p> To display files larger than 10MB in home directories: </p>
<pre>
 virt-ls -lR -d guest /home | awk '$3 &gt; 10*1024*1024'
</pre>
<p> Find everything modified in the last 7 days: </p>
<pre>
 virt-ls -lR -d guest --time-days / | awk '$6 &lt;= 7'
</pre>
<p> Find regular files modified in the last 24 hours: </p>
<pre>
 virt-ls -lR -d guest --time-days / | grep '^-' | awk '$6 &lt; 1'
</pre>
<h3><font SIZE="-1">DIFFERENCES IN SNAPSHOTS AND BACKING FILES</font></h3>
<p> Although it is possible to use virt-ls to look for differences, since libguestfs ≥ 1.26 a new tool is available called <i><a href="/docs/linux/man/1-virt-diff/">virt-diff</a></i>(1).</p>
<h2>OUTPUT MODES</h2>
<p> <tt>&quot;virt-ls&quot;</tt> has four output modes, controlled by different combinations of the <i>-l</i> and <i>-R</i> options.</p>
<h3><font SIZE="-1">SIMPLE LISTING</font></h3>
<p> A simple listing is like the ordinary <i><a href="/docs/linux/man/1-ls/">ls</a></i>(1) command: </p>
<pre>
 $ virt-ls -d guest /
 bin
 boot
 [etc.]
</pre>
<h3><font SIZE="-1">LONG LISTING</font></h3>
<p> With the <i>-l</i> (<i>&#8211;long</i>) option, the output is like the <tt>&quot;ls -l&quot;</tt> command (more specifically, like the <tt>&quot;guestfs_ll&quot;</tt> function). </p>
<pre>
 $ virt-ls -l -d guest /
 total 204
 dr-xr-xr-x.   2 root root   4096 2009-08-25 19:06 bin
 dr-xr-xr-x.   5 root root   3072 2009-08-25 19:06 boot
 [etc.]
</pre>
<p> Note that while this is useful for displaying a directory, do not try parsing this output in another program. Use &#8220;<font SIZE="-1">RECURSIVE LONG LISTING&#8221;</font> instead.</p>
<h3><font SIZE="-1">RECURSIVE LISTING</font></h3>
<p> With the <i>-R</i> (<i>&#8211;recursive</i>) option, <tt>&quot;virt-ls&quot;</tt> lists the names of files and directories recursively: </p>
<pre>
 $ virt-ls -R -d guest /tmp
 foo
 foo/bar
 [etc.]
</pre>
<p> To generate this output, <tt>&quot;virt-ls&quot;</tt> runs the <tt>&quot;guestfs_find0&quot;</tt> function and converts <tt>&quot;
