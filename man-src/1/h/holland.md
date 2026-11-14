---
title: "holland(1)"
name: "holland"
section: "1"
letter: "h"
url: "/docs/linux/man/1-holland/"
description: "holland – pluggable database backup agent"
---

<h2>NAME</h2>
<p> holland &#8211; pluggable database backup agent </p>
<h2>SYNOPSIS</h2>
<p> holland [global-options] command [command-options] </p>
<h2>DESCRIPTION</h2>
<p> Holland provides a pluggable framework through which to perform database backups. </p>
<p> This framework primarily targets MySQL, but there are plans to support other database platforms such as PostgreSQL in the future </p>
<p> Holland supports three kinds of plugins currently: </p>
<dl>
<dt>&bull;</p>
<dd> Backup plugins </p>
<dt>&bull;</p>
<dd> Command plugins </p>
<dt>&bull;</p>
<dd> Library plugins </p>
<p> Backup plugins are used for defined backup jobs in order to perform some task. The currently available backup plugins include: </p>
<dt>&bull;</p>
<dd> mysqldump </p>
<dt>&bull;</p>
<dd> mysqlhotcopy (raw file backups for non-transactional tables) </p>
<dt>&bull;</p>
<dd> mysql-lvm (raw file backups using LVM filesystem snasphots) </p>
<dt>&bull;</p>
<dd> maatkit (mk-parallel-dump) </p>
<p> Command plugins are used to add additional commands to the holland shell. Currently available commands include: </p>
<dt>&bull;</p>
<dd> backup &#8211; run one or more backup jobs </p>
<dt>&bull;</p>
<dd> list-plugins &#8211; show known plugins </p>
<dt>&bull;</p>
<dd> list-backups &#8211; show completed backup jobs </p>
<dt>&bull;</p>
<dd> mk-config &#8211; generate a job config for a given backup plugin </p>
<p> Library plugins simply provide support for other plugins. Currently available library plugins include: </p>
<dt>&bull;</p>
<dd> holland.lib.mysql &#8211; Core MySQL support </p>
<dt>&bull;</p>
<dd> holland.lib.archive &#8211; Standardized access to multiple archive formats </p>
<dt>&bull;</p>
<dd> holland.lib.compression &#8211; Standardized access to compression streams </p>
</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;config</code>=<i>&lt;file&gt;</i></p>
<dd> Read configuration settings from &lt;file&gt;, if it exists. </p>
<dt><code>bk &#8211;ry-run</code></p>
<dd> Performs a dry run of one of more backup jobs. </p>
<dt><code>&#8211;version , -V</code></p>
<dd> Show this program&#8217;s version number and exit. </p>
<dt><code>&#8211;help , -h</code></p>
<dd> Show this help message and exit. </p>
</dl>
<h2>PROBLEMS</h2>
<dl>
<dt>1.</p>
<dd> restore is still a manual process </p>
</dl>
<h2>SEE ALSO</h2>
<dl>
<dt>&bull;</p>
<dd> <i>Python Eggs &lt;<a rel="nofollow" href="http://peak.telecommunity.com/DevCenter/PythonEggs">http://peak.telecommunity.com/DevCenter/PythonEggs</a>&gt;</i> </p>
<dt>&bull;</p>
<dd> <i>pkg_resources &lt;<a rel="nofollow" href="http://peak.telecommunity.com/DevCenter/PkgResources">http://peak.telecommunity.com/DevCenter/PkgResources</a>&gt;</i> </p>
<dt>&bull;</p>
<dd> <i>Plugins Using Eggs &lt;<a rel="nofollow" href="http://ianbicking.org/docs/pycon2006/plugins.html">http://ianbicking.org/docs/pycon2006/plugins.html</a>&gt;</i> </p>
<dt>&bull;</p>
<dd> <code>man holland-mysqlhotcopy</code> </p>
<dt>&bull;</p>
<dd> <code>man holland-mysqldump</code> </p>
<dt>&bull;</p>
<dd> <code>man holland-mysqllvm</code> </p>
</dl>
<h2>AUTHOR</h2>
<p> Andrew Garner &lt;andrew.garner [at] rackspace.com&gt; </p>
<h2>COPYRIGHT</h2>
<p> Other/Proprietary </p>
<h2>Index</h2>
