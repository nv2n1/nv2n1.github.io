---
title: "buffindexed(5)"
name: "buffindexed"
section: "5"
letter: "b"
url: "/docs/linux/man/5-buffindexed/"
description: "buffindexed.conf – Configuration for the buffindexed overview method"
---

<p>buffindexed.conf &#8211; Configuration for the buffindexed overview method</p>
<h2>Description</h2>
<p><i>buffindexed.conf</i>, found in <i>pathetc</i>, specifies the buffers that the buffindexed overview method should use. It is required if the server uses buffindexed (as configured by the <i>ovmethod</i> parameter in <i>inn.conf</i>). </p>
<p> Buffindexed uses pre-built buffer files to store overview data and indexes to that data. The buffers are divided into 8&nbsp;<wbr><font SIZE="-1">KB</font> internally, and a given block is used either for overview data or for index data. A block is always allocated to a single newsgroup and is never shared among newsgroups. </p>
<p> In addition to the buffers, buffindexed also stores information in a file named <i>group.index</i> in <i>pathdb</i>. (This file should not be mistaken for the one named <i>group.index</i> in <i>pathoverview</i> which is used by the tradindexed overview method.) It contains information about each newsgroup: the pointer to the index block for the newsgroup, the high mark, the low mark, the flag of the group, the number of articles, and so forth. This file is created automatically when all buffers are initialized and should not be manually edited. </p>
<p> Buffindexed buffers are of fixed size, so buffindexed will never use more space than what is available in those buffers. If all buffers are full, <code>innd</code> will throttle when it attempts to store overview information for any additional articles until space is freed (with <code>expireover</code>, for instance) or another buffer is added. This is unlike the <font SIZE="-1">CNFS</font> storage method. </p>
<p> You can see the current usage of the buffers with the <code>-o</code> option to <code>inndf</code>. </p>
<p> In the <i>buffindexed.conf</i> file, blank lines and lines beginning with a number sign (<tt>&quot;#&quot;</tt>) are ignored. All other lines must be of the format: </p>
<pre> &lt;index&gt;:&lt;filename&gt;:&lt;size&gt;</pre>
<p>The order of lines is not significant. </p>
<p> &lt;index&gt; is the index of this overview buffer and must be unique. Other than that constraint, it can be any number between 0 and 65535. </p>
<p> &lt;filename&gt; is the path to the buffer. The length of the path should not be longer than 63 characters. </p>
<p> &lt;size&gt; is the length of the buffer in kilobytes (1&nbsp;<wbr><font SIZE="-1">KB</font>&nbsp;<wbr>=&nbsp;<wbr>1024 bytes). If &lt;filename&gt; does not specify a special device, the file size of the buffer must be &lt;size&gt;&nbsp;<wbr>*&nbsp;<wbr>1024 bytes. If it does specify a special device, that device must have at least &lt;size&gt; space available. For more information on setting up the buffers, see &#8220;<font SIZE="-1">CREATING</font> <font SIZE="-1">BUFFERS</font>&#8221;. </p>
<p> An example of <i>buffindexed.conf</i> file can be: </p>
<pre> 0:&lt;pathoverview in inn.conf&gt;/OV1:1536000
 1:&lt;pathoverview in inn.conf&gt;/OV2:1536000</pre>
<p>When you first start <code>innd</code> with everything configured properly, you should see messages like this in <i>pathlog</i>/news.notice: </p>
<pre> Aug 27 00:00:00 kevlar innd: buffindexed: No magic cookie found
 for buffindexed 0, initializing</pre>
<p>You <font SIZE="-1">MUST</font> recreate overview completely using <code>makehistory</code> if you remove or replace buffers. However, new buffers can be added without any special care (other than restarting <code>innd</code> after modifying <i>buffindexed.conf</i>). If you need to rebuild overview, you should zero all of the buffers first.</p>
<h2>Creating Buffers</h2>
<p>There are two methods to create a new buffindexed buffer:</p>
<dl>
<dt>1.</p>
<dd>Create a large file on top of a regular file system. The easiest way to do this is probably with <i><a href="/docs/linux/man/1-dd/">dd</a></i>(1), using a command like: </p>
<pre> dd if=/dev/zero of=/path/to/cycbuff bs=1024 count=&lt;size&gt;</pre>
<p>where &lt;size&gt; is the size from the relevant line in <i>buffindexed.conf</i>. </p>
<p> This is the simplest method, but has the disadvantage that very large files on regular file systems can be fairly slow to access, particularly at the end of the file, and <font SIZE="-1">INN</font> incurs unnecessary file system overhead when accessing the buffer.</p>
<dt>2.</p>
<dd>Use block devices directly. If your operating system allows you to call <i>mmap()</i> on block devices (Solaris and recent versions of Linux do, FreeBSD at last report does not), this method can avoid all of the native file system overhead. Note, however, that Solaris has problems with byte range locking on block devices, and therefore this method should not be used on Solaris. </p>
<p> Partition the disk. If you&#8217;re using Solaris, set up your partitions to avoid the first cylinder of the disk (or otherwise the buffindexed header will overwrite the disk partition table and render the buffers inaccessible). Then, create device files for each block device you&#8217;re going to use. </p>
<p> It&#8217;s not recommended to use the block device files in <i>/dev</i>, since the news system doesn&#8217;t have permission to write to them and changing the permissions of the system device files may affect something else. Instead, use <i><a href="/docs/linux/man/1-mknod/">mknod</a></i>(1) to create a new set of block devices (in somewhere like <i>pathspool</i>/overview that&#8217;s only writable by the news user). To do this, run <tt>&quot;ls -Ll&quot;</tt> on the devices in <i>/dev</i> that correspond to the block devices that you want to use. The major and minor device numbers are in the fifth and sixth columns (right before the date), respectively. Then run mknod like: </p>
<pre> mknod &lt;filename&gt; b &lt;major&gt; &lt;minor&gt;</pre>
<p>where &lt;filename&gt; is the path to the device to create (matching the &lt;filename&gt; part of the buffindexed configuration line) and &lt;major&gt; and &lt;minor&gt; are the major and minor device numbers as discovered above. </p>
<p> Here&#8217;s a short script to do this when given the path to the system device file as an argument: </p>
<pre> #!/bin/sh
 base=`echo &quot;$1&quot; | sed 's%.*/%%'`
 major=`ls -Ll &quot;$1&quot; | awk '{print $5}' | tr -d ,`
 minor=`ls -Ll &quot;$1&quot; | awk '{print $6}`
 mkdir -p &lt;pathoverview in inn.conf&gt;
 mknod &lt;pathoverview&gt;/&quot;$base&quot; b &quot;$major&quot; &quot;$minor&quot;
 chown news:news &lt;pathoverview&gt;/&quot;$base&quot;
 chmod 644 &lt;pathoverview&gt;/&quot;$base&quot;</pre>
<p>Make sure that the created files are owned by the news user and news group, as specified at configure time (the default being <tt>&quot;news&quot;</tt> for both). Also make sure that the permissions on the devices allow the news user to read and write.</dl>
<h2>History</h2>
<p>Written by Katsuhiro Kondou &lt;kondou [at] nec.co.jp&gt; for InterNetNews. Converted to <font SIZE="-1">POD</font> by Russ Allbery &lt;rra [at] stanford.edu&gt;. </p>
<p> $Id: buffindexed.conf.pod 8195 2008-11-29 11:07:02Z iulius $</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/8-expireover/">expireover</a></i>(8), <i><a href="/docs/linux/man/5-inn-conf/">inn.conf</a></i>(5), <i><a href="/docs/linux/man/8-inndf/">inndf</a></i>(8), <i><a href="/docs/linux/man/8-makehistory/">makehistory</a></i>(8). </p>
