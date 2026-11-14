---
title: "amstar(8)"
name: "amstar"
section: "8"
letter: "a"
url: "/docs/linux/man/8-amstar/"
description: "amstar – Amanda Application to interface with star"
---

<p>amstar &#8211; Amanda Application to interface with star</p>
<h2>Description</h2>
<p>Amstar is an Amanda Application API script. It should not be run by users directly. It uses star to backup and restore data. </p>
<p> The <code>diskdevice</code> in the disklist (DLE) must be the directory to backup.</p>
<h2>Include &#8211; Exclude</h2>
<p>amstar doesn&#8217;t support include. Both &#8216;exclude list&#8217; and &#8216;exclude file&#8217; are supported. There is a maximum of 100 patterns (limit of star). </p>
<p> Moving directories into and out of directories on the exclude list causes incremental backups to not contain the files in the moved directories until the next full backup unless the moved files are modified after the move.</p>
<h2>Properties</h2>
<p>This section lists the properties that control amstar&#8217;s functionality. See <code><a href="/docs/linux/man/7-amanda-applications/">amanda-applications</a></code>(7) for information on application properties and how they are configured. </p>
<p> ACL</p>
<dl>
<dd>If &quot;YES&quot; (the default), amstar will store files acl by passing the <i>-acl</i> argument to star. If &quot;NO&quot;, then the <i>-acl</i> option is not given to star, and it will not try to backup the acl.</dl>
<p> COMMAND-OPTIONS</p>
<dl>
<dd>If set, theses options are passed asis to star. Each option must be a different value of the property. Some option can break how amanda do backup, use it with care. </p>
<p> Use: </p>
<pre> property &quot;COMMAND-OPTIONS&quot; &quot;--foo&quot; &quot;bar&quot;</pre>
<p>Do not use: </p>
<pre> property &quot;COMMAND-OPTIONS&quot; &quot;--foo bar&quot;</pre>
</dl>
<p> DIRECTORY</p>
<dl>
<dd>If set, gnutar will backup from that directory instead of the <i>diskdevice</i> set by the DLE. On restore, the data is restore in that directpory instead of the current working directory.</dl>
<p> ONE-FILE-SYSTEM</p>
<dl>
<dd>The default is &quot;YES&quot;. This property is deprecated and the default value can&#8217;t be changed. star requires it when it works in dump mode. This corresponds to the <i>-xdev</i> option of star.</dl>
<p> SPARSE</p>
<dl>
<dd>If &quot;YES&quot; (the default), star will store sparse files efficiently. If &quot;NO&quot;, then the <i>-sparse</i> option is not given to star, and it will not try to detect sparse files.</dl>
<p> STAR-DLE-TARDUMP</p>
<dl>
<dd>If &quot;YES&quot;, amstar will use a different tardump file for each DLE. The default is &quot;NO&quot;. This property is needed with older versions of star doing many dumps in parallel, because of a race condition in updating the tardump file.</dl>
<p> STAR-PATH</p>
<dl>
<dd>The path to the star binary. The default is set when Amanda is built by the &#8211;with-star configure option.</dl>
<p> STAR-TARDUMP</p>
<dl>
<dd>The directory where star stores the database it uses to generate incremental dumps. The default is /etc/tardumps.</dl>
<p> NORMAL</p>
<dl>
<dd>List all regex (POSIX Extended Regular Expression syntax) that are normal output from star. These output are in the &quot;FAILED DUMP DETAILS&quot; section of the email report if the dump result is STRANGE or FAILED. Default values: </p>
<pre> &quot;^could not open conf file&quot;
 &quot;^Type of this level &quot;
 &quot;^Date of this level &quot;
 &quot;^Date of last level &quot;
 &quot;^Dump record level &quot;
 &quot;^Throughput&quot;
 &quot;^.*is sparse$&quot;
 &quot;^star: dumped [0-9][0-9]* (tar )?files&quot;
 &quot;^.*The following problems occurred during .* processing.*$&quot;
 &quot;^.*Processed all possible files, despite earlier errors.*$&quot;
 &quot;^.*not written due to problems during backup.*$&quot;</pre>
<p>To treat one of these default patterns differently, specify it explicitly in a different property.</dl>
<p> IGNORE</p>
<dl>
<dd>List all regex (POSIX Extended Regular Expression syntax) that amanda ignore. These output are never in the email report.</dl>
<p> STRANGE</p>
<dl>
<dd>List all regex (POSIX Extended Regular Expression syntax) that are strange output from star. All star output that doesn&#8217;t match a normal or ignore regex are strange by default. The result of the dump is STRANGE if star produce a strange output. These output are in the &quot;FAILED DUMP DETAILS&quot; section of the email report. </p>
<pre> &quot;^Perform a level 0 dump first.*$&quot;</pre>
<p>To treat one of these default patterns differently, specify it explicitly in a different property.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-amanda/">amanda</a></code>(8), <code><a href="/docs/linux/man/5-amanda-conf/">amanda.conf</a></code>(5), <code><a href="/docs/linux/man/7-amanda-applications/">amanda-applications</a></code>(7) </p>
<p> The Amanda Wiki: : <a rel="nofollow" href="http://wiki.zmanda.com/">http://wiki.zmanda.com/</a></p>
<h2>Authors</h2>
<p><code>Jean-Louis Martineau</code> &lt;martineau [at] zmanda.com&gt;</p>
<dl>
<dd>Zmanda, Inc. (<a rel="nofollow" href="http://www.zmanda.com)">http://www.zmanda.com)</a></dl>
<p> <code>Dustin J. Mitchell</code> &lt;dustin [at] zmanda.com&gt;</p>
<dl>
<dd>Zmanda, Inc. (<a rel="nofollow" href="http://www.zmanda.com)">http://www.zmanda.com)</a></dl>
