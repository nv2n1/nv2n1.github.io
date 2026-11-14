---
title: "xfs_estimate(8)"
name: "xfs_estimate"
section: "8"
letter: "x"
url: "/docs/linux/man/8-xfs_estimate/"
description: "xfs_estimate – estimate the space that an XFS filesystem will take"
---

<p>xfs_estimate &#8211; estimate the space that an XFS filesystem will take</p>
<h2>Synopsis</h2>
<pre><code>xfs_estimate</code> [ <code>-h</code> ] [ <code>-b</code> blocksize ] [ <code>-i</code> logsize ]
 [ <code>-e</code> logsize ] [ <code>-v</code> ] directory ...
<br>
<code>xfs_estimate -V</code></pre>
<h2>Description</h2>
<p>For each <i>directory</i> argument, <i>xfs_estimate</i> estimates the space that directory would take if it were copied to an XFS filesystem. <i>xfs_estimate</i> does not cross mount points. The following definitions are used:</p>
<dl>
<dd>KB = *1024</p>
<dd>MB = *1024*1024</p>
<dd>GB = *1024*1024*1024</dl>
<p> The <i>xfs_estimate</i> options are:</p>
<dl>
<dt><code>-b</code> <i>blocksize</i></p>
<dd>Use <i>blocksize</i> instead of the default blocksize of 4096 bytes. The modifier <code>k</code> can be used after the number to indicate multiplication by 1024. For example, </p>
<dl>
<dd><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><tt>xfs_estimate -b 64k /</tt>
</dl>
<dd>requests an estimate of the space required by the directory / on an XFS filesystem using a blocksize of 64K (65536) bytes.</p>
<dt><code>-v</code></p>
<dd>Display more information, formatted.</p>
<dt><code>-h</code></p>
<dd>Display usage message.</p>
<dt><code>-i, -e</code> <i>logsize</i></p>
<dd>Use <i>logsize</i> instead of the default log size of 1000 blocks. <code>-i</code> refers to an internal log, while <code>-e</code> refers to an external log. The modifiers <code>k</code> or <code>m</code> can be used after the number to indicate multiplication by 1024 or 1048576, respectively.</p>
<dd>For example, </p>
<dl>
<dd><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><tt>xfs_estimate -i 1m /</tt>
</dl>
<dd>requests an estimate of the space required by the directory / on an XFS filesystem using an internal log of 1 megabyte.</p>
<dt><code>-V</code></p>
<dd>Print the version number and exits.</dl>
<h2>Examples</h2>
<pre>% <tt>xfs_estimate -e 10m /var/tmp</tt>
/var/tmp will take about 4.2 megabytes
 with the external log using 2560 blocks or about 10.0 megabytes</pre>
<pre>% <tt>xfs_estimate -v -e 10m /var/tmp</tt>
directory bsize blocks megabytes logsize
/var/tmp 4096 792 4.0MB 10485760</pre>
<pre>% <tt>xfs_estimate -v /var/tmp</tt>
directory bsize blocks megabytes logsize
/var/tmp 4096 3352 14.0MB 10485760</pre>
<pre>% <tt>xfs_estimate /var/tmp</tt>
/var/tmp will take about 14.0 megabytes</pre>
