---
title: "yum-debug-restore(1)"
name: "yum-debug-restore"
section: "1"
letter: "y"
url: "/docs/linux/man/1-yum-debug-restore/"
description: "yum-debug-restore – replay Yum transactions captured in a debug-dump file"
---

<h2>NAME</h2>
<p> yum-debug-restore &#8211; replay Yum transactions captured in a debug-dump file</p>
<h2>SYNOPSIS</h2>
<p> <code>yum-debug-restore</code></p>
<h2>DESCRIPTION</h2>
<p> <code>yum-debug-restore</code> is a program which takes a gzipped file created by <code>yum-debug-dump</code> and acts on the information about installed packages contained within. </p>
<h2>GENERAL OPTIONS</h2>
<dl>
<dt><code>&#8211;output</code></p>
<dd> Output the commands that would be run to stdout.</p>
<dt><code>&#8211;shell=&lt;file&gt;</code></p>
<dd> Output the commands that would be run to a file.</p>
<dt><code>&#8211;install-latest</code></p>
<dd> Ask yum to install the latest version of the given packages, instead of the version that was installed in the debug-dump file.</p>
<dt><code>&#8211;ignore-arch</code></p>
<dd> Ignore the architecture of the packages, so you can &quot;restore&quot; an i386 debug-dump on an x86_64 machine.</p>
<dt><code>&#8211;filter-types=[install,remove,update,downgrade]</code></p>
<dd> Only perform the given types of commands, so you can filter to just upgrades and installs. </p>
</dl>
<h2>FILES</h2>
<p> As yum-debug-restore uses YUM libraries for retrieving all the information, it relies on YUM configuration for its default values like which repositories to use. Consult YUM documentation for details: </p>
<pre>
/etc/yum.conf
/etc/yum/repos.d/
/var/cache/yum/
</pre>
<h2>SEE ALSO</h2>
<pre>
<i>yum-debug-dump (1)</i>
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
