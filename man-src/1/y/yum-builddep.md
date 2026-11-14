---
title: "yum-builddep(1)"
name: "yum-builddep"
section: "1"
letter: "y"
url: "/docs/linux/man/1-yum-builddep/"
description: "yum-builddep – install missing dependencies for building an RPM package"
---

<h2>NAME</h2>
<p> yum-builddep &#8211; install missing dependencies for building an RPM package</p>
<h2>SYNOPSIS</h2>
<p> <code>yum-builddep</code> package </p>
<p> <code>yum-builddep</code> /path/to/local/package.src.rpm </p>
<p> <code>yum-builddep</code> /path/to/local/package.spec</p>
<h2>DESCRIPTION</h2>
<p> <code>yum-builddep</code> is a program which installs the RPMs needed to build the specified package. The source RPM for the specified package must be available in a Yum repository (which will be automatically enabled, if it is disabled) or it can be a local source RPM or a spec file. </p>
<p> Note, that only the BuildRequires information within the SRPM header information is used to determine build dependencies. This will specifically omit any dependencies that are required only for specific architectures. </p>
<h2>EXAMPLES</h2>
<dl>
<dt>Download and install all the RPMs needed to build the kernel RPM:</p>
<dd> <code>yumdownloader &#8211;source kernel &amp;&amp; rpm2cpio kernel*src.rpm | cpio -i kernel.spec &amp;&amp; \ </code><br />
 <code>yum-builddep kernel.spec</code></dl>
<p> The kernel includes specific BuildRequires dependencies for different architectures. In order to make sure that those dependencies are downloaded and installed, the SRPM should be downloaded, the .spec file extracted from it and used to determine the full dependency list. </p>
<h2>FILES</h2>
<p> As yum-builddep uses YUM libraries for retrieving all the information, it relies on YUM configuration for its default values like which repositories to use. Consult YUM documentation for details: </p>
<pre>
/etc/yum.conf
/etc/yum/repos.d/
/var/cache/yum/
</pre>
<h2>SEE ALSO</h2>
<pre>
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
