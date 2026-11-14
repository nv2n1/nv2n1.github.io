---
title: "shtool-rotate(1)"
name: "shtool-rotate"
section: "1"
letter: "s"
url: "/docs/linux/man/1-shtool-rotate/"
description: "shtool rotate – GNU shtool log file rotation"
---

<h2 class="name">NAME</h2>
<p> shtool rotate &#8211; GNU shtool log file rotation </p>
<h2>SYNOPSIS</h2>
<p> <code>shtool rotate</code> [<code>-v</code>|<code>&#8211;verbose</code>] [<code>-t</code>|<code>&#8211;trace</code>] [<code>-f</code>|<code>&#8211;force</code>] [<code>-n</code>|<code>&#8211;num-files</code> <i>count</i>] [<code>-s</code>|<code>&#8211;size</code> <i>size</i>] [<code>-c</code>|<code>&#8211;copy</code>] [<code>-r</code>|<code>&#8211;remove</code>] [<code>-a</code>|<code>&#8211;archive-dir</code> <i>dir</i>] [<code>-z</code>|<code>&#8211;compress</code> [<i>tool</i>:]<i>level</i>] [<code>-b</code>|<code>&#8211;background</code>] [<code>-d</code>|<code>&#8211;delay</code>] [<code>-p</code>|<code>&#8211;pad</code> <i>len</i>] [<code>-m</code>|<code>&#8211;mode</code> <i>mode</i>] [<code>-o</code>|<code>&#8211;owner</code> <i>owner</i>] [<code>-g</code>|<code>&#8211;group</code> <i>group</i>] [<code>-M</code>|<code>&#8211;migrate</code> <i>cmd</i>] [<code>-P</code>|<code>&#8211;prolog</code> <i>cmd</i>] [<code>-E</code>|<code>&#8211;epilog</code> <i>cmd</i>] <i>file</i> [<i>file</i> &#8230;]</p>
<h2>DESCRIPTION</h2>
<p> This command rotates a logfile <i>file</i> by subsequently creating up to <i>count</i> (optionally compressed) archive files of it. Archive files are named &quot;<i>file</i>.<i>number</i>[<i>compress-suffix]</i>&quot; where <i>number</i> is the version number, 0 being the newest and &quot;<i>count</i>-1&quot; the oldest. </p>
<p> A rotation step consists of the following steps </p>
<p> 1. remove last archive file 2. shift archive file numbers 3. create archive file 0 from <i>file</i> 4. truncate/recreate <i>file</i></p>
<h2>OPTIONS</h2>
<p> The following command line options are available.</p>
<dl>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> Display some processing information.</p>
<dt><code>-t</code>, <code>&#8211;trace</code></p>
<dd> Enable the output of the essential shell commands which are executed.</p>
<dt><code>-f</code>, <code>&#8211;force</code></p>
<dd> Force silent creation of archive directory if it does not exists. Also skip missing intermediate logfiles in the rotation step. Default is to exit with error in both cases. <font SIZE="-1">FIXME</font></p>
<dt><code>-n</code>, <code>&#8211;num-files</code> <i>count</i></p>
<dd> Create <i>count</i> archive files. Default is 10.</p>
<dt><code>-s</code>, <code>&#8211;size</code> <i>size</i></p>
<dd> Only rotate if logfile exceeds <i>size</i>. The argument <i>size</i> can be specified also with the trailing units <tt>&quot;K&quot;</tt> (kilo), <tt>&quot;M&quot;</tt> (mega) or <tt>&quot;G&quot;</tt> (giga). The &#8220;prolog&#8221; and &#8220;epilog&#8221; are only executed if rotation actually takes place.</p>
<dt><code>-c</code>, <code>&#8211;copy</code></p>
<dd> Copy <i>file</i> to archive then truncate original. The default is to move <i>file</i> to archive. </p>
<p> Unless an application reopens its logfile it will continue to write to the same file. In the default move case the application will write to the archive which it had previously opened as <i>file</i>. In the copy case the application will write to the original <i>file</i>. The drawback of the copy approach is that logfile entries are lost when they are written to <i>file</i> between the execution of the copy and the truncation operation. The drawback of the move approach is that the application needs to detect the move or must be triggered to reopen its log (i.e. through epilog).</p>
<dt><code>-r</code>, <code>&#8211;remove</code></p>
<dd> Removes <i>file</i> after rotation instead of providing a new empty file.</p>
<dt><code>-a</code>, <code>&#8211;archive-dir</code> <i>dir</i></p>
<dd> Specify the archive directory. Default is to create archives in the same directory as <i>file</i> is located.</p>
<dt><code>-z</code>, <code>&#8211;compress</code> [<i>tool</i>:]<i>level</i></p>
<dd> Enables compression of archive files with compression level <i>level</i> By default, the tools <i><a href="/docs/linux/man/1-bzip2/">bzip2</a></i>(1), <i><a href="/docs/linux/man/1-gzip/">gzip</a></i>(1) and <i><a href="/docs/linux/man/1-compress/">compress</a></i>(1) are searched for in <tt>$PATH</tt>, but one also can override this by prefixing the compression level with one of the three particular tool names.</p>
<dt><code>-b</code>, <code>&#8211;background</code></p>
<dd> Enable background compression.</p>
<dt><code>-d</code>, <code>&#8211;delay</code></p>
<dd> Delays the compression of archive file number 0. This is useful if &#8220;<code>-c</code>&#8221; is not used, because an application might continue to write to archive file 0 through an already open file handle.</p>
<dt><code>-p</code>, <code>&#8211;pad</code> <i>len</i></p>
<dd> Enables padding with leading zeros in the <i>number</i> part of the filename &quot;<i>file</i>.<i>number</i><i>compress-suffix</i>&quot;. The default padding <i>len</i> is 1. This is interesting if more than 10 archive files are used, because it leads to still sorted directory listings.</p>
<dt><code>-m</code>, <code>&#8211;mode</code> <i>mode</i></p>
<dd> The file mode applied to the created files, see <i><a href="/docs/linux/man/1-chmod/">chmod</a></i>(1). Setting mode to <tt>&quot;-&quot;</tt> skips this step and leaves the operating system default which is usually based on <i><a href="/docs/linux/man/1-umask/">umask</a></i>(1). Some file modes require superuser privileges to be set. Default is 0755.</p>
<dt><code>-o</code>, <code>&#8211;owner</code> <i>owner</i></p>
<dd> The file owner name or id applied to the created files, see <i><a href="/docs/linux/man/1-chown/">chown</a></i>(1). This option requires superuser privileges to execute. Default is to skip this step and leave the operating system default which is usually based on the executing uid or the parent setuid directory.</p>
<dt><code>-g</code>, <code>&#8211;group</code> <i>group</i></p>
<dd> The file group name or id applied to the created files, see <i><a href="/docs/linux/man/1-chgrp/">chgrp</a></i>(1). This option requires superuser privileges to execute to the fullest extend, otherwise the choice of <i>group</i> is limited on most operating systems. Default is to skip this step and leave the operating system default which is usually based on the executing gid or the parent setgid directory.</p>
<dt><code>-M</code>, <code>&#8211;migrate</code> <i>cmd</i></p>
<dd> Execute a &#8220;migration&#8221; command just before the archive file number <i>count</i>-1 is removed from the filesystem. The specified <i>cmd</i> receives the archive filename as command line argument.</p>
<dt><code>-P</code>, <code>&#8211;prolog</code> <i>cmd</i></p>
<dd> Execute a &#8220;prolog&#8221; command before the rotation step. Useful in conjunction with <code>-s</code>.</p>
<dt><code>-E</code>, <code>&#8211;epilog</code> <i>cmd</i></p>
<dd> Execute a &#8220;epilog&#8221; command after the rotation step. Useful in conjunction with <code>-s</code>.</dl>
<h2>EXAMPLE</h2>
<pre>
 #   shell script
 shtool rotate -n10 -s1M -zbzip2:9 -d -r /var/log/ap.access.log
 shtool rotate -n5 -s128K -zbzip2:9 -d -r /var/log/ap.error.log
 apachectl graceful
</pre>
<h2>HISTORY</h2>
<p> The <font SIZE="-1"><code>GNU</code></font><code> shtool</code> <code>rotate</code> command was originally written by Ralf S. Engelschall &lt;rse [at] engelschall.com&gt; in 2001 for <font SIZE="-1"><code>GNU</code></font><code> shtool</code>. Its development was prompted by the need to have a flexible logfile rotation facility in the <code>OpenPKG</code> project.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-shtool/">shtool</a></i>(1), <font SIZE="-1">BSD</font> <i><a href="/docs/linux/man/8-newsyslog/">newsyslog</a></i>(8). </p>
<h2>Index</h2>
