---
title: "yumdownloader(1)"
name: "yumdownloader"
section: "1"
letter: "y"
url: "/docs/linux/man/1-yumdownloader/"
description: "yumdownloader – download RPM packages from Yum repositories"
---

<h2>NAME</h2>
<p> yumdownloader &#8211; download RPM packages from Yum repositories</p>
<h2>SYNOPSIS</h2>
<p> <code>yumdownloader</code> [options] package1 [package2&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>yumdownloader</code> is a program for downloading RPMs from Yum repositories. </p>
<h2>GENERAL OPTIONS</h2>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Help; display a help message and then quit.</p>
<dt><code>&#8211;destdir DIR</code></p>
<dd> Specify a destination directory for the download. Defaults to the current directory.</p>
<dt><code>&#8211;urls</code></p>
<dd> Instead of downloading RPMs, list the URLs that would be downloaded.</p>
<dt><code>&#8211;resolve</code></p>
<dd> When downloading RPMs, resolve dependencies and also download the required packages.</p>
<dt><code>&#8211;source</code></p>
<dd> Instead of downloading the binary RPMs, download the source RPMs.</p>
<dt><code>&#8211;archlist=ARCH1[,ARCH2&#8230;]</code></p>
<dd> Limit the query to packages of given and compatible architectures. Valid values are all architectures known to rpm/yum such as &#8216;i386&#8217; and &#8216;src&#8217; for source RPMS. Note that repoquery will now change yum&#8217;s &quot;arch&quot; to the first value in the archlist. So &quot;&#8211;archlist=i386,i686&quot; will change yum&#8217;s canonical arch to i386, but allow packages of i386 and i686.</dl>
<h2>ADDITIONAL OPTIONS</h2>
<p> Yumdownloader inherits all other options from yum. See the <a href="/docs/linux/man/8-yum/">yum</a>(8) man page for more information </p>
<h2>EXAMPLES</h2>
<dl>
<dt>Download the kernel RPM to /var/tmp:</p>
<dd> <code>yumdownloader &#8211;destdir /var/tmp kernel</code></p>
<dt>List the URL for the kernel and kernel-smp RPMs:</p>
<dd> <code>yumdownloader &#8211;urls kernel kernel-smp</code></dl>
<h2>FILES</h2>
<p> As yumdownloader uses YUM libraries for retrieving all the information, it relies on YUM configuration for its default values like which repositories to use. Consult YUM documentation for details: </p>
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
