---
title: "yum-versionlock(1)"
name: "yum-versionlock"
section: "1"
letter: "y"
url: "/docs/linux/man/1-yum-versionlock/"
description: "yum-versionlock – Version lock rpm packages"
---

<h2>NAME</h2>
<p> yum-versionlock &#8211; Version lock rpm packages</p>
<h2>SYNOPSIS</h2>
<p> <code>yum-versionlock</code> [ package-name [ package-name]] &#8230;</p>
<h2>DESCRIPTION</h2>
<p> <code><a href="/docs/linux/man/1-yum-versionlock/">yum-versionlock</a>(1)</code> is a Yum plugin that takes a set of name/versions for packages and excludes all other versions of those packages (including optionally following obsoletes). This allows you to protect packages from being updated by newer versions. </p>
<p> The plugin provides a command &quot;versionlock&quot; which allows you to view and edit the list of locked packages easily.<br />
 <i></i> yum versionlock add &lt;package-wildcard&gt;&#8230; </p>
<p> Add a versionlock for all of the packages in the rpmdb matching the given wildcards. <i></i> yum versionlock exclude &lt;package-wildcard&gt;&#8230; </p>
<p> Add a exclude (within versionlock) for the latest versions of the packages in the available repos. matching the given wildcards. <i></i> yum versionlock list </p>
<p> List the current versionlock entries. <i></i> yum versionlock delete &lt;entry-wildcard&gt;&#8230; </p>
<p> Remove any matching versionlock entries. <i></i> yum versionlock clear </p>
<p> Remove all versionlock entries. </p>
<h2>FILES</h2>
<p> <i>/etc/yum/pluginconf.d/versionlock.conf</i></p>
<dl>
<dt>
<dd> The system wide configuration file. See <code><a href="/docs/linux/man/5-yum-versionlock-conf/">yum-versionlock.conf</a>(5)</code> for more information.</dl>
<p> <i>/etc/yum/pluginconf.d/versionlock.list</i></p>
<dl>
<dt>
<dd> The default place to put package version lock information (one package and version per. line). The file takes entries in the following format <code>EPOCH:NAME-VERSION-RELEASE.ARCH</code> See <code><a href="/docs/linux/man/8-rpm/">rpm</a>(8)</code> for more information on custom query formats. If the package does not have an EPOCH the number will default to 0.</dl>
<h2>BUGS</h2>
<p> There are of course no bugs, but should you find any, you should first consult the FAQ section on <a rel="nofollow" href="http://yum.baseurl.org/wiki/Faq">http://yum.baseurl.org/wiki/Faq</a> and if unsuccessful in finding a resolution contact the mailing list: yum-devel [at] lists.baseurl.org. To file a bug use <a rel="nofollow" href="http://bugzilla.redhat.com">http://bugzilla.redhat.com</a> for Fedora/RHEL/Centos related bugs and <a rel="nofollow" href="http://yum.baseurl.org/report">http://yum.baseurl.org/report</a> for all other bugs. </p>
<h2>AVAILABILITY</h2>
<p> yum-versionlock is available via: </p>
<pre>
# yum install yum-versionlock
</pre>
<h2>AUTHORS</h2>
<p> Panu Matilainen &lt;pmatilai [at] laiskiainen.org&gt;<br />
 James Antill &lt;james [at] and.org&gt;<br />
 Documentation modified by:<br />
 Gerhardus Geldenhuis &lt;gerhardus.geldenhuis [at] gmail.com&gt;</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-yum/">yum</a>(1)</code> </p>
<h2>Index</h2>
