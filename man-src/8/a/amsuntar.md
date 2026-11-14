---
title: "amsuntar(8)"
name: "amsuntar"
section: "8"
letter: "a"
url: "/docs/linux/man/8-amsuntar/"
description: "amsuntar – Amanda Application to interface with native tar utility available on solaris platforms"
---

<p>amsuntar &#8211; Amanda Application to interface with native tar utility available on solaris platforms</p>
<h2>Description</h2>
<p>Amsuntar is an Amanda Application API script. It should not be run by users directly. It uses Solaris bundled tar utility to backup and restore data. Currenty ACLs from ZFS file system can only be backed up using the solaris supplied tar utility. </p>
<p> The <code>diskdevice</code> in the disklist (DLE) must be the directory to backup. </p>
<p> Solaris 10 supports Role Based Access Control(RBAC) which is enabled by default. To run backup operations using sun tar utility by under privileged user like amandabackup, amandabackup user need to have proper roles and profiles, specially &quot;Media Backup&quot; profile/role. This can be done using &#8216;usermod -P &quot;Media Backup&quot; amandabackup&#8217; command.</p>
<h2>Properties</h2>
<p>This section lists the properties that control amsuntar&#8217;s functionality. See <code><a href="/docs/linux/man/7-amanda-applications/">amanda-applications</a></code>(7) for information on application properties and how they are configured. </p>
<p> BLOCK-SIZE</p>
<dl>
<dd>Optional tar read or write block size. The default is 256.</dl>
<p> DIRECTORY</p>
<dl>
<dd>If set, suntar will backup from that directory instead of the <i>diskdevice</i> set by the DLE. On restore, the data is restore in that directory instead of the current working directory.</dl>
<p> EXTENDED-ATTRIBUTES</p>
<dl>
<dd>Include extended attributes in archive. The default is YES.</dl>
<p> EXTENDED-HEADERS</p>
<dl>
<dd>Write tar file with extended headers. With this optiion the modification time is maintained with a granularity of microseconds,Long file names and file sizes greater than 8GB can be archived. The default is YES.</dl>
<p> SUNTAR-PATH</p>
<dl>
<dd>The path to the suntar binary. The default is set when Amanda is built.</dl>
<p> LANG</p>
<dl>
<dd>Default LANG is &quot;C&quot;. suntar require an UTF-8 LANG if you have UTF-8 filename and it is configured for extended headers. A good value can be &quot;en_US.UTF-8&quot; if that locale is installed on your machine.</dl>
<p> NORMAL</p>
<dl>
<dd>List all regex (Perl Regular Expression syntax) that are normal output from sun tar. These output are in the &quot;FAILED DUMP DETAILS&quot; section of the email report if the dump result is STRANGE or FAILED. Default values: </p>
<pre>is not a file. Not dumped\$
same as archive file\$</pre>
<p>To treat one of these default patterns differently, specify it explicitly in a different property.</dl>
<p> IGNORE</p>
<dl>
<dd>List all regex (Perl Regular Expression syntax) that amanda ignore. These output are never in the email report.</dl>
<p> STRANGE</p>
<dl>
<dd>List all regex (Perl Regular Expression syntax) that are strange output from sun tar. The result of the dump is STRANGE if sun tar produce a strange output. These output are in the &quot;FAILED DUMP DETAILS&quot; section of the email report. Default values: </p>
<pre>: invalid character in UTF-8 conversion of 
: UTF-8 conversion failed.\$</pre>
<p>To treat one of these default patterns differently, specify it explicitly in a different property.</dl>
<p> ERROR</p>
<dl>
<dd>List all regex (perl Regular Expression syntax) that are error output from sun tar. All sun tar output that doesn&#8217;t match a normal, ignore or strange regex are error by default. The result of the dump is FAILED if sun tar produce an error output. These output are in the &quot;FAILED DUMP DETAILS&quot; section of the email report. Default values: </p>
<pre>: Permission denied\$</pre>
<p>To treat one of these default patterns differently, specify it explicitly in a different property.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-amanda/">amanda</a></code>(8), <code><a href="/docs/linux/man/5-amanda-conf/">amanda.conf</a></code>(5), <code><a href="/docs/linux/man/7-amanda-applications/">amanda-applications</a></code>(7) </p>
<p> The Amanda Wiki: : <a rel="nofollow" href="http://wiki.zmanda.com/">http://wiki.zmanda.com/</a></p>
<h2>Authors</h2>
<p><code>Satya Ganga</code> &lt;gast [at] zmanda.com&gt;</p>
<dl>
<dd>Zmanda, Inc. (<a rel="nofollow" href="http://www.zmanda.com)">http://www.zmanda.com)</a></dl>
<p> <code>Jean-Louis Martineau</code> &lt;martineau [at] zmanda.com&gt;</p>
<dl>
<dd>Zmanda, Inc. (<a rel="nofollow" href="http://www.zmanda.com)">http://www.zmanda.com)</a></dl>
<p> <code>Dustin J. Mitchell</code> &lt;dustin [at] zmanda.com&gt;</p>
<dl>
<dd>Zmanda, Inc. (<a rel="nofollow" href="http://www.zmanda.com)">http://www.zmanda.com)</a></dl>
