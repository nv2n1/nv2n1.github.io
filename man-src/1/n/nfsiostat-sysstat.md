---
title: "nfsiostat-sysstat(1)"
name: "nfsiostat-sysstat"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nfsiostat-sysstat/"
description: "nfsiostat-sysstat (the nfsiostat command from the sysstat package) – Report input/output statistics for network filesystems (NFS)."
---

<h2>NAME</h2>
<p> nfsiostat-sysstat (the nfsiostat command from the sysstat package) &#8211; Report input/output statistics for network filesystems (NFS).</p>
<h2>SYNOPSIS</h2>
<p> <code>nfsiostat-sysstat [ -h ] [ -k | -m ] [ -t ] [ -V ] [</code> <i>interval</i> <code>[</code> <i>count</i> <code>] ]</code></p>
<h2>DESCRIPTION</h2>
<p> The <code>nfsiostat-sysstat</code> command displays statistics about read and write operations on NFS filesystems. </p>
<p> The <i>interval</i> parameter specifies the amount of time in seconds between each report. The first report contains statistics for the time since system startup (boot). Each subsequent report contains statistics collected during the interval since the previous report. A report consists of an NFS header row followed by a line of statistics for each network filesystem that is mounted. The <i>count</i> parameter can be specified in conjunction with the <i>interval</i> parameter. If the <i>count</i> parameter is specified, the value of <i>count</i> determines the number of reports generated at <i>interval</i> seconds apart. If the <i>interval</i> parameter is specified without the <i>count</i> parameter, the <code>nfsiostat-sysstat</code> command generates reports continuously. </p>
<h2>REPORT</h2>
<p> The Network Filesystem (NFS) report provides statistics for each mounted network filesystem. Transfer rates are shown in 1K blocks by default, unless the environment variable POSIXLY_CORRECT is set, in which case 512-byte blocks are used. The report shows the following fields: </p>
<p> <code>Filesystem:</code></p>
<dl>
<dt>
<dd> This columns shows the hostname of the NFS server followed by a colon and by the directory name where the network filesystem is mounted. </p>
</dl>
<p> <code>rBlk_nor/s (rkB_nor/s, rMB_nor)</code></p>
<dl>
<dt>
<dd> Indicate the number of blocks (kilobytes, megabytes) read by applications via the <a href="/docs/linux/man/2-read/">read</a>(2) system call interface. A block has a size of 512 bytes. </p>
</dl>
<p> <code>wBlk_nor/s (wkB_nor/s, wMB_nor/s)</code></p>
<dl>
<dt>
<dd> Indicate the number of blocks (kilobytes, megabytes) written by applications via the <a href="/docs/linux/man/2-write/">write</a>(2) system call interface. </p>
</dl>
<p> <code>rBlk_dir/s (rkB_dir/s, rMB_dir/s)</code></p>
<dl>
<dt>
<dd> Indicate the number of blocks (kilobytes, megabytes) read from files opened with the O_DIRECT flag. </p>
</dl>
<p> <code>wBlk_dir/s (wkB_dir/s, wMB_dir/s)</code></p>
<dl>
<dt>
<dd> Indicate the number of blocks (kilobytes, megabytes) written to files opened with the O_DIRECT flag. </p>
</dl>
<p> <code>rBlk_svr/s (rkB_svr/s, rMB_svr/s)</code></p>
<dl>
<dt>
<dd> Indicate the number of blocks (kilobytes, megabytes) read from the server by the NFS client via an NFS READ request. </p>
</dl>
<p> <code>wBlk_svr/s (wkB_svr/s, wMB_svr/s)</code></p>
<dl>
<dt>
<dd> Indicate the number of blocks (kilobytes, megabytes) written to the server by the NFS client via an NFS WRITE request. </p>
</dl>
<p> <code>ops/s</code></p>
<dl>
<dt>
<dd> Indicate the number of operations that were issued to the filesystem per second. </p>
</dl>
<p> <code>rops/s</code></p>
<dl>
<dt>
<dd> Indicate the number of &#8216;read&#8217; operations that were issued to the filesystem per second. </p>
</dl>
<p> <code>wops/s</code></p>
<dl>
<dt>
<dd> Indicate the number of &#8216;write&#8217; operations that were issued to the filesystem per second.</dl>
<h2>OPTIONS</h2>
<dl>
<dt>-h</p>
<dd> Make the NFS report easier to read by a human.</p>
<dt>-k</p>
<dd> Display statistics in kilobytes per second.</p>
<dt>-m</p>
<dd> Display statistics in megabytes per second.</p>
<dt>-t</p>
<dd> Print the time for each report displayed. The timestamp format may depend on the value of the S_TIME_FORMAT environment variable (see below).</p>
<dt>-V</p>
<dd> Print version number then exit. </p>
</dl>
<h2>ENVIRONMENT</h2>
<p> The <code>nfsiostat-sysstat</code> command takes into account the following environment variables: </p>
<dl>
<dt>S_TIME_FORMAT</p>
<dd> If this variable exists and its value is <code>ISO</code> then the current locale will be ignored when printing the date in the report header. The <code>nfsiostat-sysstat</code> command will use the ISO 8601 format (YYYY-MM-DD) instead. The timestamp displayed with option -t will also be compliant with ISO 8601 format. </p>
<dt>POSIXLY_CORRECT</p>
<dd> When this variable is set, transfer rates are shown in 512-byte blocks instead of the default 1K blocks. </p>
</dl>
<h2>BUG</h2>
<p> <i>/proc</i> filesystem must be mounted for <code>nfsiostat-sysstat</code> to work. </p>
<h2>FILE</h2>
<p> <i>/proc/self/mountstats</i> contains statistics for network filesystems. </p>
<h2>WARNING</h2>
<p> The nfsiostat command from the sysstat package (nfsiostat-sysstat) is now obsolete and is no longer maintained. It will be removed in a future sysstat version. Please use now the <code>nfsiostat</code> command from the <i>nfs-utils</i> package. </p>
<h2>AUTHORS</h2>
<p> Written by Ivana Varekova (varekova &lt;at&gt; redhat.com) </p>
<p> Maintained by Sebastien Godard (sysstat &lt;at&gt; orange.fr)</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-nfsiostat/">nfsiostat</a></code>(8), <code><a href="/docs/linux/man/1-sar/">sar</a></code>(1), <code><a href="/docs/linux/man/1-pidstat/">pidstat</a></code>(1), <code><a href="/docs/linux/man/1-mpstat/">mpstat</a></code>(1), <code><a href="/docs/linux/man/8-vmstat/">vmstat</a></code>(8), <code><a href="/docs/linux/man/1-iostat/">iostat</a></code>(1), <code><a href="/docs/linux/man/1-cifsiostat/">cifsiostat</a></code>(1) </p>
<p> <i><a rel="nofollow" href="http://pagesperso-orange.fr/sebastien.godard/">http://pagesperso-orange.fr/sebastien.godard/</a></i> </p>
<h2>Index</h2>
