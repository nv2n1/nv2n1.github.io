---
title: "yum-debug-dump(1)"
name: "yum-debug-dump"
section: "1"
letter: "y"
url: "/docs/linux/man/1-yum-debug-dump/"
description: "yum-debug-dump – write system RPM configuration to a debug-dump file"
---

<h2>NAME</h2>
<p> yum-debug-dump &#8211; write system RPM configuration to a debug-dump file</p>
<h2>SYNOPSIS</h2>
<p> <code>yum-debug-dump</code></p>
<h2>DESCRIPTION</h2>
<p> <code>yum-debug-dump</code> is a program which creates a gzipped file containing a lot of information useful to developers trying to debug a problem. </p>
<p> By default it will output a file to the current working directory named yum_debug_dump-&lt;hostname&gt;-&lt;time&gt;.txt.gz. This file contains no private information but does contain a complete list of all packages you have installed, all packages available in any repository, important configuration and system information. You can view this file using the &#8216;zless&#8217; command. </p>
<p> You can use the coresponding program <code>yum-debug-restore</code> to act on this file and restore a set of packages (much like dump/restore). </p>
<h2>FILES</h2>
<p> As yum-debug-dump uses YUM libraries for retrieving all the information, it relies on YUM configuration for its default values like which repositories to use. Consult YUM documentation for details: </p>
<pre>
/etc/yum.conf
/etc/yum/repos.d/
/var/cache/yum/
</pre>
<h2>SEE ALSO</h2>
<pre>
<i>yum-debug-restore (1)</i>
<i>yum.conf (5)</i>
<a rel="nofollow" href="http://yum.baseurl.org/">http://yum.baseurl.org/</a>
</pre>
<h2>AUTHORS</h2>
<pre>
See the Authors file included with this program.
</pre>
<h2>BUGS</h2>
<p> There are of course no bugs, but should you find any, you should first consult the FAQ section on <a rel="nofollow" href="http://yum.baseurl.org/wiki/Faq">http://yum.baseurl.org/wiki/Faq</a> and if unsuccessful in finding a resolution contact the mailing list: yum-devel [at] lists.baseurl.org. To file a bug use <a rel="nofollow" href="http://bugzilla.redhat.com">http://bugzilla.redhat.com</a> for Fedora/RHEL/Centos related bugs and <a rel="nofollow" href="http://yum.baseurl.org/report">http://yum.baseurl.org/report</a> for all other bugs. </p>
<h2>Index</h2>
