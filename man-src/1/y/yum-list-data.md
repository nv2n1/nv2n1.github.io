---
title: "yum-list-data(1)"
name: "yum-list-data"
section: "1"
letter: "y"
url: "/docs/linux/man/1-yum-list-data/"
description: "yum list data plugin"
---

<h2>NAME</h2>
<p> yum list data plugin</p>
<h2>SYNOPSIS</h2>
<p> <code>yum</code> [options] [command] [package &#8230;]</p>
<h2>DESCRIPTION</h2>
<p> This plugin extends <code>yum</code> for some commands that give aggregate package data based on lists of packages </p>
<p> added yum <i>command</i>s are:<br />
 <i></i> * list-vendors<br />
 <i></i> * info-vendors<br />
 <i></i> * list-rpm-groups<br />
 <i></i> * info-rpm-groups<br />
 <i></i> * list-packagers<br />
 <i></i> * info-packagers<br />
 <i></i> * list-licenses<br />
 <i></i> * info-licenses<br />
 <i></i> * list-arches<br />
 <i></i> * info-arches<br />
 <i></i> * list-committers<br />
 <i></i> * info-committers<br />
 <i></i> * list-buildhosts<br />
 <i></i> * info-buildhosts<br />
 <i></i> * list-baseurls<br />
 <i></i> * info-baseurls<br />
 <i></i> * list-package-sizes<br />
 <i></i> * info-package-sizes<br />
 <i></i> * list-archive-sizes<br />
 <i></i> * info-archive-sizes<br />
 <i></i> * list-installed-sizes<br />
 <i></i> * info-installed-sizes<br />
 <i></i> * list-groups<br />
 <i></i> * info-groups </p>
<p> all of which take the same arguments as the list and info yum commands. The difference between the list and info varieties is that the info versions lists all the packages under each aggregation. </p>
<dl>
<dt><code>list-vendors</code>, <code>info-vendors</code></p>
<dd> Is used to list the aggregate of the vendor attribute on the packages, examples are &quot;Fedora Project&quot; and &quot;Red Hat, Inc.&quot;.</p>
<dt>
<dd>
<dt><code>list-rpm-groups</code>, <code>info-rpm-groups</code></p>
<dd> Is used to list the aggregate of the group attribute on the packages, examples are &quot;Applications/System&quot;, &quot;Development/Tools&quot; and &quot;System Environment/Base&quot;</p>
<dt>
<dd>
<dt><code>list-packagers</code>, <code>info-packagers</code></p>
<dd> Is used to list the aggregate of the packager attribute on the packages, examples are &quot;Fedora Project&quot; and &quot;Red Hat, Inc.&quot;.</p>
<dt>
<dd>
<dt><code>list-licenses</code>, <code>info-licenses</code></p>
<dd> Is used to list the aggregate of the license attribute on the packages, examples are &quot;GPL&quot; and &quot;MIT&quot;</p>
<dt>
<dd>
<dt><code>list-arches</code>, <code>info-arches</code></p>
<dd> Is used to list the aggregate of the arch attribute on the packages, examples are &quot;i386&quot; and &quot;x86_64&quot;</p>
<dt>
<dd>
<dt><code>list-committers</code>, <code>info-committers</code></p>
<dd> Is used to list the aggregate of the committer attribute on the packages, this is taken from the most recent changelog entry of the package.</p>
<dt>
<dd>
<dt><code>list-buildhosts</code>, <code>info-buildhosts</code></p>
<dd> Is used to list the aggregate of the buildhost attribute on the packages, examples are &quot;mybuilder.example.com&quot; and &quot;xenbuilder1.fedora.redhat.com&quot;</p>
<dt>
<dd>
<dt><code>list-baseurls</code>, <code>info-baseurls</code></p>
<dd> Is used to list the aggregate of the url attribute on the packages after discarding the path of the URL, examples are &quot;<a rel="nofollow" href="http://yum.baseurl.org/">http://yum.baseurl.org/</a>&quot; and &quot;<a rel="nofollow" href="http://www.and.org/">http://www.and.org/</a>&quot;</p>
<dt>
<dd>
<dt><code>list-package-sizes</code>, <code>info-package-sizes</code></p>
<dd> Is used to list the aggregate of specified ranges the packagesize attribute on the packages, examples are &quot;[ 1B &#8211; 10KB ]&quot; and &quot;[ 750KB &#8211; 1MB ]&quot;.</p>
<dt>
<dd>
<dt><code>list-archive-sizes</code>, <code>info-archive-sizes</code></p>
<dd> Is used to list the aggregate of specified ranges the archivesize attribute on the packages, examples are &quot;[ 1B &#8211; 10KB ]&quot; and &quot;[ 750KB &#8211; 1MB ]&quot;.</p>
<dt>
<dd>
<dt><code>list-installed-sizes</code>, <code>info-installed-sizes</code></p>
<dd> Is used to list the aggregate of specified ranges the installedsize attribute on the packages, examples are &quot;[ 1B &#8211; 10KB ]&quot; and &quot;[ 750KB &#8211; 1MB ]&quot;.</p>
<dt>
<dd>
<dt><code>list-groups</code>, <code>info-groups</code></p>
<dd> Is used to list the aggregate of the yum groups that the packages are in, examples are in &quot;yum grouplist&quot;. Note that in yum groups a package can be in more than one group at a time.</p>
<dt>
<dd></dl>
<p> It is worth noting that some of the above data can be &quot;unknown&quot;, to yum, at which point a separate aggregation called &quot;&#8211; Unknown &#8211;&quot; is listed.</p>
<h2>EXAMPLES</h2>
<p> To list all the groups that have an update, along with the number of packages in each group, use:</p>
<dl>
<dt>
<dd> yum list-rpm-groups updates</dl>
<p> To list all the committers to packages that have yum in their name, use:</p>
<dl>
<dt>
<dd> yum list-committers &#8216;yum*&#8217;</dl>
<p> To list ranges of the sizes of packages installed or available, use:</p>
<dl>
<dt>
<dd> yum list-package-sizes</dl>
<p> To list yum groups that have an update, use:</p>
<dl>
<dt>
<dd> yum list-groups </p>
</dl>
<h2>SEE ALSO</h2>
<pre>
<i>yum-filter-data (1)</i>
<i>yum (8)</i>
<i>yum.conf (5)</i>
</pre>
<h2>AUTHORS</h2>
<pre>
James Antill &lt;james.antill [at] redhat.com&gt;.
</pre>
<h2>Index</h2>
