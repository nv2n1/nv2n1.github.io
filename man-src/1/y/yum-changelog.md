---
title: "yum-changelog(1)"
name: "yum-changelog"
section: "1"
letter: "y"
url: "/docs/linux/man/1-yum-changelog/"
description: "yum-changelog"
---

<h2>NAME</h2>
<p> <code>yum-changelog</code></p>
<h2>SYNOPSIS</h2>
<p> The <code>yum-changelog</code> package</p>
<h2>DESCRIPTION</h2>
<p> <code><a href="/docs/linux/man/1-yum-changelog/">yum-changelog</a>(1)</code> is a Yum plugin for viewing package changelogs before/after updating. yum will invoke <code><a href="/docs/linux/man/1-yum-changelog/">yum-changelog</a>(1)</code> plugin if the <code>&#8211;changelog</code> option or the <code>changelog</code> command is used with yum.</p>
<h2>OPTIONS</h2>
<dl>
<dt>&#8211;changelog</p>
<dd> Show changelog delta of updated packages</dl>
<h2>COMMANDS</h2>
<dl>
<dt>changelog</p>
<dd> Show changelog data of packages listed (same format as the list command). The first argument is required and is either &quot;all&quot; for all the changelog entries, a date for the changelog entries since a specified point in time or a number for a given number of changelog entries.</dl>
<h2>FILES</h2>
<p> <i>/etc/yum/pluginconf.d/changelog.conf</i></p>
<dl>
<dt>
<dd> The system wide configuration file. See <code><a href="/docs/linux/man/5-yum-changelog-conf/">yum-changelog.conf</a>(5)</code> for more information.</dl>
<h2>EXAMPLES</h2>
<p> # yum <code>changelog</code> 2008-Jan yum\*<br />
 Listing changelogs since: 2008-01-18 </p>
<p> yum-versionlock-1.1.11-1.fc8.noarch installed<br />
 * Wed Jan 30 17:00:00 2008 Tim Lauridsen &lt;timlau [at] fedoraproject.org&gt;<br />
 &#8211; mark as 1.1.11 </p>
<p> changelog stats. 33 pkgs, 12 source pkgs, 1 changelog </p>
<p> # yum update ktechlab <code>&#8211;changelog</code><br />
 Loading &quot;changelog&quot; plugin<br />
 Setting up Update Process<br />
 Setting up repositories<br />
 [..]<br />
 Resolving Dependencies<br />
 &#8211;&gt; Populating transaction set with selected packages. Please wait.<br />
 &#8212;&gt; Package ktechlab.i386 0:0.3-6 set to be updated<br />
 &#8211;&gt; Running transaction check </p>
<p> Changes in packages about to be updated: </p>
<p> ktechlab &#8211; 0.3-6.i386<br />
 * Wed Nov 22 23:00:00 2006 Chitlesh Goorah &#8211; 0.3-6<br />
 &#8211; Rebuilt due to new gpsim-devel release </p>
<h2>BUGS</h2>
<p> There are of course no bugs, but should you find any, you should first consult the FAQ section on <a rel="nofollow" href="http://yum.baseurl.org/wiki/Faq">http://yum.baseurl.org/wiki/Faq</a> and if unsuccessful in finding a resolution contact the mailing list: yum-devel [at] lists.baseurl.org. To file a bug use <a rel="nofollow" href="http://bugzilla.redhat.com">http://bugzilla.redhat.com</a> for Fedora/RHEL/Centos related bugs and <a rel="nofollow" href="http://yum.baseurl.org/report">http://yum.baseurl.org/report</a> for all other bugs. </p>
<h2>AVAILABILITY</h2>
<p> yum-changelog is available via: </p>
<pre>
# yum install yum-changelog
</pre>
<h2>AUTHORS</h2>
<dl>
<dt>
<dd> Chitlesh Goorah &lt;chitlesh [at] fedoraproject.org&gt;<br />
 Panu Matilainen &lt;pmatilai [at] laiskiainen.org&gt;<br />
 James Antill &lt;james [at] and.org&gt;</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-yum/">yum</a>(1)</code> </p>
<h2>Index</h2>
