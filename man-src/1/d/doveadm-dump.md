---
title: "doveadm-dump(1)"
name: "doveadm-dump"
section: "1"
letter: "d"
url: "/docs/linux/man/1-doveadm-dump/"
description: "doveadm-dump – Dump the content of Dovecot’s binary mailbox index/log"
---

<h2>NAME</h2>
<p> doveadm-dump &#8211; Dump the content of Dovecot&#8217;s binary mailbox index/log</p>
<h2>SYNOPSIS</h2>
<p> <code>doveadm</code> [<code>-Dv</code>] <code>dump</code> [<code>-t</code> <i>type</i>] <i>path</i></p>
<h2>DESCRIPTION</h2>
<p> Dovecot uses several binary index and log files in order to improve performance for accessing mails. For some mailbox formats, such as sdbox and mdbox, the index files are part of the format itself. For details about index files, see also: <a rel="nofollow" href="http://wiki2.dovecot.org/IndexFiles">http://wiki2.dovecot.org/IndexFiles</a> </p>
<p> <code>doveadm dump</code> is used to show the contents of those mailbox index/log files, in human readable format. This is mainly useful for Dovecot developers when debugging some problem.</p>
<h2>OPTIONS</h2>
<p> Global <code><a href="/docs/linux/man/1-doveadm/">doveadm</a></code>(1) <i>options</i>:</p>
<dl>
<dt><code>-D</code></dt>
<dd> Enables verbosity and debug messages.</dd>
<dt><code>-v</code></dt>
<dd> Enables verbosity, including progress counter.</dd></dl>
<p> Command specific <i>options</i>:</p>
<dl>
<dt><code>-t&nbsp;<wbr></code><i>type</i></dt>
<dd> the file type of the file to be dumped. If the <i>type</i> was omitted, <code><a href="/docs/linux/man/1-doveadm/">doveadm</a></code>(1) tries to detect the type of <i>path</i>. <i>type</i> can be:</dd>
<dl>
<dl>
<dt><code>dbox</code></dt>
<dd> &rArr; m.<i>n</i> (sdbox or mdbox mailbox file)</dd>
<dt><code>index</code></dt>
<dd> &rArr; dovecot.index, dovecot.map.index</dd>
<dt><code>log</code></dt>
<dd> &rArr; dovecot.index.log, dovecot.map.index.log</dd>
<dt><code>mailboxlog</code></dt>
<dd> &rArr; dovecot.mailbox.log</dd>
<dt><code>thread</code></dt>
<dd> &rArr; dovecot.index.thread</dd></dl>
</dl>
</dl>
<h2>ARGUMENTS</h2>
<dl>
<dt><i>path</i></dt>
<dd> The path to the corresponding dbox storage, index or log file. If only a directory is specified, doveadm tries to detect the type of files under it and dumps them.</dd></dl>
<h2>EXAMPLE</h2>
<p> Look at the contents of a mailbox&#8217;s index: </p>
<pre>
<code>doveadm dump ~/Maildir/.work/</code>
</pre>
<h2>REPORTING BUGS</h2>
<p> Report bugs, including <i>doveconf -n</i> output, to the Dovecot Mailing List &lt;dovecot [at] dovecot.org&gt;. Information about reporting bugs is available at: <a rel="nofollow" href="http://dovecot.org/bugreport.html">http://dovecot.org/bugreport.html</a></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-doveadm/">doveadm</a></code>(1) </p>
