---
title: "cycbuff(5)"
name: "cycbuff"
section: "5"
letter: "c"
url: "/docs/linux/man/5-cycbuff/"
description: "cycbuff.conf – Configuration file for INN CNFS storage method"
---

<p>cycbuff.conf &#8211; Configuration file for INN CNFS storage method</p>
<h2>Description</h2>
<p>This file defines the cyclical buffers that make up the storage pools for <font SIZE="-1">CNFS</font> (Cyclic News File System). Some options controlling the behavior of the <font SIZE="-1">CNFS</font> storage system can also be set here. <i>cycbuff.conf</i> is required if the <font SIZE="-1">CNFS</font> (Cyclic News File System) storage method is used. <font SIZE="-1">INN</font> will look for it in <i>pathetc</i> (as set in <i>inn.conf</i>). </p>
<p> <font SIZE="-1">CNFS</font> stores articles in logical objects called <i>metacycbuffs</i>. Each metacycbuff is in turn composed of one or more physical buffers called <i>cycbuffs</i>. As articles are written to the metacycbuff, each article is written to the next cycbuff in the list in a round-robin fashion (unless <tt>&quot;sequential&quot;</tt> mode is specified, in which case each cycbuff is filled before moving on to the next). This is so that you can distribute the individual cycbuffs across multiple physical disks and balance the load between them. Note that in order to use any cycbuff larger than 2&nbsp;<wbr><font SIZE="-1">GB</font>, you need to build <font SIZE="-1">INN</font> with the <code>&#8211;enable-largefiles</code> option. </p>
<p> For information about how to configure <font SIZE="-1">INN</font> to use <font SIZE="-1">CNFS</font>, see <i><a href="/docs/linux/man/5-storage-conf/">storage.conf</a></i>(5). </p>
<p> Blank lines and lines beginning with a hash sign (<tt>&quot;#&quot;</tt>) are ignored. All other lines must be of one of the following forms: </p>
<pre> cycbuffupdate:&lt;interval&gt;
 refreshinterval:&lt;interval&gt;
 cycbuff:&lt;name&gt;:&lt;file&gt;:&lt;size&gt;
 metacycbuff:&lt;name&gt;:&lt;buffer&gt;[,&lt;buffer&gt;,...][:&lt;mode&gt;]</pre>
<p>(where items enclosed in [] are optional). Order is mostly not significant, but all <i>cycbuff</i> lines must occur before all <i>metacycbuff</i> lines. Long lines can be continued on the next line by ending the line with a backslash (<tt>&quot;\&quot;</tt>).</p>
<dl>
<dt><i>cycbuffupdate</i>:&lt;interval&gt;</p>
<dd>Sets the number of articles written before the cycbuff header is written back to disk to &lt;interval&gt;. Under most operating systems, the header doesn&#8217;t have to be written to disk for the updated data to be available to other processes on the same system that are reading articles out of <font SIZE="-1">CNFS</font>, but any accesses to the <font SIZE="-1">CNFS</font> cycbuffs over <font SIZE="-1">NFS</font> will only see the data present at the last write of the header. After a system crash, all updates since the last write of the <font SIZE="-1">CNFS</font> header may be lost. The default value, if this line is omitted, is <tt>25</tt>, meaning that the header is written to disk after every 25 articles stored in that cycbuff.</p>
<dt><i>refreshinterval</i>:&lt;interval&gt;</p>
<dd>Sets the interval (in seconds) between re-reads of the cycbuff header to &lt;interval&gt;. This primarily affects <code>nnrpd</code> and controls the frequency with which it updates its knowledge of the current contents of the <font SIZE="-1">CNFS</font> cycbuffs. The default value, if this line is omitted, is <tt>30</tt>.</p>
<dt><i>cycbuff</i>:&lt;name&gt;:&lt;file&gt;:&lt;size&gt;</p>
<dd>Configures a particular <font SIZE="-1">CNFS</font> cycbuff. &lt;name&gt; is a symbolic name for the buffer, to be used later in a metacycbuff line. It must be no longer than seven characters. &lt;file&gt; is the full path to the buffer file or block device, and must be no longer than 63 characters. &lt;size&gt; is the length of the buffer in kilobytes (1&nbsp;<wbr><font SIZE="-1">KB</font> is 1024 bytes). If &lt;file&gt; is not a block device, it should be &lt;size&gt;&nbsp;<wbr>*&nbsp;<wbr>1024 bytes long. </p>
<p> If you&#8217;re trying to stay under 2&nbsp;<wbr><font SIZE="-1">GB</font>, keep your sizes below <tt>2097152</tt>.</p>
<dt><i>metacycbuff</i>:&lt;name&gt;:&lt;buffer&gt;[,&lt;buffer&gt;,&#8230;][:&lt;mode&gt;]</p>
<dd>Specifies a collection of <font SIZE="-1">CNFS</font> buffers that make up a single logical storage location from the perspective of <font SIZE="-1">INN</font>. Metacycbuffs are referred to in <i>storage.conf</i> as storage locations for articles, so in order to actually put articles in a cycbuff, it has to be listed as part of some metacycbuff which is then referenced in <i>storage.conf</i>. </p>
<p> &lt;name&gt; is the symbolic name of the metacycbuff, referred to in the options: field of <tt>&quot;cnfs&quot;</tt> entries in <i>storage.conf</i>. It must be no longer than eight characters. &lt;buffer&gt; is the name of a cycbuff (the &lt;name&gt; part of a cycbuff line), and any number of cycbuffs may be specified, separated by commas. </p>
<p> If there is more than one cycbuff in a metacycbuff, there are two ways that <font SIZE="-1">INN</font> can distribute articles between the cycbuffs. The default mode, <tt>&quot;INTERLEAVE&quot;</tt>, stores the articles in each cycbuff in a round-robin fashion, one article per cycbuff in the order listed. If the cycbuffs are of wildly different sizes, this can cause some of them to roll over much faster than others, and it may not give the best performance depending on your disk layout. The other storage mode, <tt>&quot;SEQUENTIAL&quot;</tt>, instead writes to each cycbuff in turn until that cycbuff is full and then moves on to the next one, returning to the first and starting a new cycle when the last one is full. To specify a mode rather than leaving it at the default, add a colon and the mode (<tt>&quot;INTERLEAVE&quot;</tt> or <tt>&quot;SEQUENTIAL&quot;</tt>) at the end of the metacycbuff line.</dl>
<p> <code>innd</code> only reads <i>cycbuff.conf</i> on startup, so if you change anything in this file and want <code>innd</code> to pick up the changes, you have to use <tt>&quot;ctlinnd xexec innd&quot;</tt>; <tt>&quot;ctlinnd reload all ''&quot;</tt> is not sufficient. </p>
<p> When articles are stored, the cycbuff into which they&#8217;re stored is saved as part of the article token. In order for <font SIZE="-1">INN</font> to retrieve articles from a cycbuff, that cycbuff must be listed in <i>cycbuff.conf</i>. However, if <font SIZE="-1">INN</font> should not write to a cycbuff, it doesn&#8217;t need to be (and shouldn&#8217;t be) listed in a metacycbuff. </p>
<p> This provides an easy way to retire a cycbuff. Just remove it from its metacycbuff, leaving in the cycbuff line, and restart <code>innd</code> (with, for example, <tt>&quot;ctlinnd xexec innd&quot;</tt>). No new articles will be put into the cycbuff, but neither will any articles expire from it. After you no longer need the articles in the cycbuff, just remove it entirely from <i>cycbuff.conf</i>. Then all of the articles will appear to have been deleted to <font SIZE="-1">INN</font>, and the next nightly expire run will clean up any remaining references to them. </p>
<p> Adding a new cycbuff just requires creating it (see below), adding a cycbuff line, adding it to a metacycbuff, and then restarting <code>innd</code>.</p>
<h2>Creating Cycbuffs</h2>
<p>When creating a new cycbuff, there are two different methods for creating the buffers in which the articles will be stored.</p>
<dl>
<dt>1.</p>
<dd>Create a large file on top of a regular file system. The easiest way to do this is probably with <i><a href="/docs/linux/man/1-dd/">dd</a></i>(1), using a command like: </p>
<pre> dd if=/dev/zero of=/path/to/cycbuff bs=1024 count=&lt;size&gt;</pre>
<p>where &lt;size&gt; is the size from the cycbuff line in <i>cycbuff.conf</i>. <i></i><font SIZE="-1"><i>INSTALL</i></font><i></i> contains a script that will generate these commands for you from your <i>cycbuff.conf</i> file. </p>
<p> This is the simplest method, but has the disadvantage that very large files on regular file systems can be fairly slow to access, particularly at the end of the file, and <font SIZE="-1">INN</font> incurs unnecessary file system overhead when accessing the cycbuff.</p>
<dt>2.</p>
<dd>Use block devices directly. If your operating system allows you to call <i>mmap()</i> on block devices (Solaris and recent versions of Linux do, FreeBSD at last report does not), this is the recommended method since you can avoid all of the native file system overhead. Note, however, that each cycbuff cannot be larger than 2&nbsp;<wbr><font SIZE="-1">GB</font> with this method, so if you need a lot of spool space, you may have to go back to disk files. </p>
<p> Partition the disk to make each partition equal to or smaller than 2&nbsp;<wbr><font SIZE="-1">GB</font>. If you&#8217;re using Solaris, set up your partitions to avoid the first cylinder of the disk (or otherwise the cycbuff header will overwrite the disk partition table and render the cycbuffs inaccessible). Then, create device files for each block device you&#8217;re going to use. </p>
<p> It&#8217;s not recommended to use the block device files in <i>/dev</i>, since the news system doesn&#8217;t have permission to write to them and changing the permissions of the system device files may affect something else. Instead, use <i><a href="/docs/linux/man/1-mknod/">mknod</a></i>(1) to create a new set of block devices (in somewhere like <i>pathspool</i>/cycbuffs that&#8217;s only writable by the news user). To do this, run <tt>&quot;ls -Ll&quot;</tt> on the devices in <i>/dev</i> that correspond to the block devices that you want to use. The major and minor device numbers are in the fifth and sixth columns (right before the date), respectively. Then run mknod like: </p>
<pre> mknod &lt;file&gt; b &lt;major&gt; &lt;minor&gt;</pre>
<p>where &lt;file&gt; is the path to the device to create (matching the &lt;file&gt; part of the cycbuff line) and &lt;major&gt; and &lt;minor&gt; are the major and minor device numbers as discovered above. </p>
<p> Here&#8217;s a short script to do this when given the path to the system device file as an argument: </p>
<pre> #!/bin/sh
 base=`echo &quot;$1&quot; | sed 's%.*/%%'`
 major=`ls -Ll &quot;$1&quot; | awk '{print $5}' | tr -d ,`
 minor=`ls -Ll &quot;$1&quot; | awk '{print $6}`
 mkdir -p &lt;pathspool in inn.conf&gt;/cycbuffs
 mknod &lt;pathspool&gt;/cycbuffs/&quot;$base&quot; b &quot;$major&quot; &quot;$minor&quot;
 chown news:news &lt;pathspool&gt;/cycbuffs/&quot;$base&quot;
 chmod 644 &lt;pathspool&gt;/cycbuffs/&quot;$base&quot;</pre>
<p>Make sure that the created files are owned by the news user and news group, as specified at configure time (the default being <tt>&quot;news&quot;</tt> for both). Also make sure that the permissions on the devices allow the news user to read and write, and if you want other users on the system to be able to use <code>sm</code> to retrieve articles, make sure they&#8217;re world-readable.</dl>
<p> Once you have everything configured properly and you start <code>innd</code>, you should see messages in <i>news.notice</i> that look like: </p>
<pre> innd: CNFS-sm No magic cookie found for cycbuff ONE, initializing</pre>
<p>where <tt>&quot;ONE&quot;</tt> will be whatever you called your cycbuff.</p>
<h2>History</h2>
<p>Written by Katsuhiro Kondou &lt;kondou [at] nec.co.jp&gt; for InterNetNews. Rewritten into <font SIZE="-1">POD</font> by Russ Allbery &lt;rra [at] stanford.edu&gt;. </p>
<p> $Id: cycbuff.conf.pod 7859 2008-06-07 12:44:17Z iulius $</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/8-ctlinnd/">ctlinnd</a></i>(8), <i><a href="/docs/linux/man/8-innd/">innd</a></i>(8), <i><a href="/docs/linux/man/8-nnrpd/">nnrpd</a></i>(8), <i><a href="/docs/linux/man/1-sm/">sm</a></i>(1), <i><a href="/docs/linux/man/5-storage-conf/">storage.conf</a></i>(5). </p>
