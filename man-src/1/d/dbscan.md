---

title: "dbscan(1)"
name: "dbscan"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dbscan/"
description: "dbscan – scans a Directory Server database index file and dumps the contents"
---

<p> dbscan &#8211; scans a Directory Server database index file and dumps the contents </p>
<h2>SYNOPSIS</h2>
<p> <code>dbscan</code> <code>-f &lt;filename&gt;</code> [<i>-R</i>] [<i>-t &lt;size&gt;</i>] [<i>-K &lt;entry_id&gt;</i>] [<i>-k &lt;key&gt;</i>] [<i>-l &lt;size&gt;</i>] [<i>-G &lt;n&gt;</i>] [<i>-n</i>] [<i>-r</i>] [<i>-s</i>] </p>
<h2>DESCRIPTION</h2>
<p> Scans a Directory Server database index file and dumps the contents. </p>
<h2>OPTIONS</h2>
<p> A summary of options is included below:</p>
<dl>
<dt><code>-f</code> &lt;filename&gt;</dt>
<dd> specify db file</dd>
<dt><code>-R</code></dt>
<dd> dump as raw data</dd>
<dt><code>-t</code> &lt;size&gt;</dt>
<dd> entry truncate size (bytes)</dd>
<dt>
</dt><dd> entry file options:</dd>
<dt><code>-K</code> &lt;entry_id&gt;</dt>
<dd> lookup only a specific entry id index file options:</dd>
<dt><code>-k</code> &lt;key&gt;</dt>
<dd> lookup only a specific key</dd>
<dt><code>-l</code> &lt;size&gt;</dt>
<dd> max length of dumped id list (default 4096; 40 bytes &lt;= size &lt;= 1048576 bytes)</dd>
<dt><code>-G</code> &lt;n&gt;</dt>
<dd> only display index entries with more than &lt;n&gt; ids</dd>
<dt><code>-n</code></dt>
<dd> display ID list lengths</dd>
<dt><code>-r</code></dt>
<dd> display the conents of ID list</dd>
<dt><code>-s</code></dt>
<dd> Summary of index counts</dd>
</dl>
<h2>USAGE</h2>
<p> Sample usages:</p>
<dl>
<dt>Dump the entry file:</dt>
<dd> <code>dbscan -f</code> id2entry.db4</dd>
<dt>Display index keys in cn.db4:</dt>
<dd> <code>dbscan -f</code> cn.db4</dd>
<dt>Display index keys and the count of entries having the key in mail.db4:</dt>
<dd> <code>dbscan -r</code> <code>-f</code> mail.db4</dd>
<dt>Display index keys and the IDs having more than 20 IDs in sn.db4:</dt>
<dd> <code>dbscan -r</code> <code>-G</code> 20 <code>-f</code> sn.db4</dd>
<dt>Display summary of objectclass.db4:</dt>
<dd> <code>dbscan -f</code> objectclass.db4
</dd></dl>
<h2>AUTHOR</h2>
<p> dbscan was written by the 389 Project.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to <a rel="nofollow" href="https://fedorahosted.org/389/newticket.">https://fedorahosted.org/389/newticket.</a></p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2001 Sun Microsystems, Inc. Used by permission.<br/>
 Copyright &#169; 2008 Red Hat, Inc.<br/>
 This manual page was written by Michele Baldessari &lt;michele [at] pupazzo.org&gt;, for the Debian project (but may be used by others).<br/>
 This is free software. You may redistribute copies of it under the terms of the Directory Server license found in the LICENSE file of this software distribution. This license is essentially the GNU General Public License version 2 with an exception for plug-in distribution. </p>
