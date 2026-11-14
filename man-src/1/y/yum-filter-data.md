---
title: "yum-filter-data(1)"
name: "yum-filter-data"
section: "1"
letter: "y"
url: "/docs/linux/man/1-yum-filter-data/"
description: "yum filter data plugin"
---

<h2>NAME</h2>
<p> yum filter data plugin</p>
<h2>SYNOPSIS</h2>
<p> <code>yum</code> [options] [command] [package &#8230;]</p>
<h2>DESCRIPTION</h2>
<p> This plugin extends <code>yum</code> with some options, currently just for &quot;update&quot; and &quot;list update&quot; type commands, to allow filters to be placed on which packages should be used based on the data in those packages. Note that due to some of the data being unknown, and thus could possibly match, all unknown data is treated as a match. </p>
<h2>GENERAL OPTIONS</h2>
<p> These are the options added to yum that are available in the &quot;list updates&quot;, &quot;info updates&quot;, &quot;check-update&quot; and &quot;update&quot; commands. They are: </p>
<dl>
<dt><code>&#8211;filter-vendors</code></p>
<dd> This option includes packages which have a vendor which matches one of the passed vendor wildcard strings, or is unknown. Note that vendors can have spaces in their value, so &quot;,&quot; is the only way to specify multiple vendors as one option argument.</p>
<dt><code>&#8211;filter-rpm-groups</code></p>
<dd> This option includes packages which have a group which matches one of the passed rpm group wildcard strings, or is unknown. Note that rpm groups can have spaces in their value, so &quot;,&quot; is the only way to specify multiple rpm groups as one option argument.</p>
<dt><code>&#8211;filter-packagers</code></p>
<dd> This option includes packages which have a packager which matches one of the passed packager wildcard strings, or is unknown. Note that vendors can have spaces in their value, so &quot;,&quot; is the only way to specify multiple packagers as one option argument.</p>
<dt><code>&#8211;filter-licenses</code></p>
<dd> This option includes packages which have a license which matches one of the passed license wildcard strings, or is unknown. Note that licenses can have spaces in their value, so &quot;,&quot; is the only way to specify multiple licenses as one option argument.</p>
<dt><code>&#8211;filter-arches</code></p>
<dd> This option includes packages which have a arch which matches one of the passed arch wildcard strings, or is unknown.</p>
<dt><code>&#8211;filter-committers</code></p>
<dd> This option includes packages which have a committer which matches one of the passed committer wildcard strings, or is unknown. Note that committers can have spaces in their value, so &quot;,&quot; is the only way to specify multiple committers as one option argument. Also, committer values are so loosely formed that they could contain commas too, it is recommended to not do that but you can work around it by using &quot;?&quot;.</p>
<dt><code>&#8211;filter-buildhosts</code></p>
<dd> This option includes packages which have a buildhost which matches one of the passed buildhost wildcard strings, or is unknown.</p>
<dt><code>&#8211;filter-urls</code></p>
<dd> This option includes packages which have a url which matches one of the passed url wildcard strings, or is unknown.</p>
<dt><code>&#8211;filter-package-sizes</code></p>
<dd> This option includes packages which have a packagesize which is within one of the passed packagesize ranges, or is unknown.</p>
<dt><code>&#8211;filter-archive-sizes</code></p>
<dd> This option includes packages which have a archivesize which is within one of the passed archivesize ranges, or is unknown.</p>
<dt><code>&#8211;filter-installed-sizes</code></p>
<dd> This option includes packages which have a installedsize which is within one of the passed installedsize ranges, or is unknown.</p>
<dt><code>&#8211;filter-groups</code></p>
<dd> This option includes packages which are in a yum group which matches one of the passed yum group id strings, or is unknown. Note that yum groups can have spaces in their value, so &quot;,&quot; is the only way to specify multiple yum groups as one option argument.</dl>
<h2>EXAMPLES</h2>
<p> To list all updates that are 1 MB or less use:</p>
<dl>
<dt>
<dd> yum &#8211;filter-package-sizes=-1m check-update</dl>
<p> To apply updates that Dan Walsh has committed use:</p>
<dl>
<dt>
<dd> yum &#8211;filter-committers=&#8217;Dan Walsh *&#8217; update</dl>
<p> To list updates for a specific group use:</p>
<dl>
<dt>
<dd> yum &#8211;filter-rpm-groups=&#8217;App*/Sys*&#8217; list updates</dl>
<p> To apply updates to a specific set of groups use:</p>
<dl>
<dt>
<dd> yum &#8211;filter-rpm-groups=&#8217;App*/System,Devel*/Lib*,System Environment/Base&#8217; update</dl>
<p> To list updates for a set of yum groups use:</p>
<dl>
<dt>
<dd> yum &#8211;filter-groups=&#8217;PostgreSQL Database,Web Server&#8217; list updates</dl>
<p> To apply updates to a specific set of yum groups use:</p>
<dl>
<dt>
<dd> yum &#8211;filter-groups=&#8217;KDE,Core,Printing Support&#8217; update </p>
</dl>
<h2>SEE ALSO</h2>
<pre>
<i>yum-list-data (1)</i>
<i>yum (8)</i>
<i>yum.conf (5)</i>
</pre>
<h2>AUTHORS</h2>
<pre>
James Antill &lt;james.antill [at] redhat.com&gt;.
</pre>
<h2>BUGS</h2>
<p> Currently yum can&#8217;t filter packages in all of the commands, so for instance &quot;yum list &#8216;yum*&#8217;&quot; doesn&#8217;t get the results filtered. </p>
<p> Apart from that there are no bugs, but should you find any, you should first consult the FAQ section on <a rel="nofollow" href="http://yum.baseurl.org/wiki/Faq">http://yum.baseurl.org/wiki/Faq</a> and if unsuccessful in finding a resolution contact the mailing list: yum-devel [at] lists.baseurl.org. To file a bug use <a rel="nofollow" href="http://bugzilla.redhat.com">http://bugzilla.redhat.com</a> for Fedora/RHEL/Centos related bugs and <a rel="nofollow" href="http://yum.baseurl.org/report">http://yum.baseurl.org/report</a> for all other bugs. </p>
<h2>Index</h2>
