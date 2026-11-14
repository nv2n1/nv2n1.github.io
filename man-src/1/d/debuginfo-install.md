---
title: "debuginfo-install(1)"
name: "debuginfo-install"
section: "1"
letter: "d"
url: "/docs/linux/man/1-debuginfo-install/"
description: "debuginfo-install – install debuginfo packages and their dependencies"
---

<h2>NAME</h2>
<p> debuginfo-install &#8211; install debuginfo packages and their dependencies</p>
<h2>SYNOPSIS</h2>
<p> <code>debuginfo-install</code> package</p>
<h2>DESCRIPTION</h2>
<p> <code>debuginfo-install</code> is a program which installs the RPMs needed to debug the specified package. The package argument can be a wildcard, but will only match installed packages. <code>debuginfo-install</code> will then enable any debuginfo repositories, and install the relevant debuginfo rpm. </p>
<h2>EXAMPLES</h2>
<dl>
<dt>Download and install all the RPMs needed to debug the kernel RPM:</p>
<dd> <code>debuginfo-install</code> kernel</dl>
<h2>WARNING MESSAGES</h2>
<dl>
<dt>Could not find debuginfo for:</p>
<dd> You may sometimes see warning messages about certain packages not being found if you run debuginfo-install for a wildcard or glob. Debuginfo packages are not necessary for &quot;noarch&quot; RPMs; these will generate a warning message. Additionally, On 64-bit systems, no multilib debuginfo packages are published, so if you have 32-bit packages installed, these will also generate warning messages.</dl>
<h2>FILES</h2>
<p> As debuginfo-install uses YUM libraries for retrieving all the information, it relies on YUM configuration for its default values like which repositories to use. Consult YUM documentation for details: </p>
<pre>
/etc/yum.conf
/etc/yum/repos.d/
/var/cache/yum/
</pre>
<h2>SEE ALSO</h2>
<pre>
<i>yum.conf (5)</i>
<a rel="nofollow" href="http://yum-utils.baseurl.org/">http://yum-utils.baseurl.org/</a>
<a rel="nofollow" href="http://yum.baseurl.org/">http://yum.baseurl.org/</a>
</pre>
<h2>AUTHORS</h2>
<pre>
See the Authors file included with this program.
</pre>
<h2>BUGS</h2>
<p> There are of course no bugs, but should you find any, you should first consult the FAQ section on <a rel="nofollow" href="http://yum.baseurl.org/wiki/Faq">http://yum.baseurl.org/wiki/Faq</a> and if unsuccessful in finding a resolution contact the mailing list: yum-devel [at] lists.baseurl.org. To file a bug use <a rel="nofollow" href="http://bugzilla.redhat.com">http://bugzilla.redhat.com</a> for Fedora/RHEL/Centos related bugs and <a rel="nofollow" href="http://yum.baseurl.org/report">http://yum.baseurl.org/report</a> for all other bugs. </p>
<h2>Index</h2>
