---
title: "repodiff(1)"
name: "repodiff"
section: "1"
letter: "r"
url: "/docs/linux/man/1-repodiff/"
description: "repodiff – list differences between two or more Yum repositories"
---

<h2>NAME</h2>
<p> repodiff &#8211; list differences between two or more Yum repositories</p>
<h2>SYNOPSIS</h2>
<p> <code>repodiff</code> &#8211;old=old_repo_baseurl &#8211;new=new_repo_baseurl</p>
<h2>DESCRIPTION</h2>
<p> <code>repodiff</code> is a program which will list differences between two sets of repositories. <code>Note</code> that by default only source packages are compared. </p>
<h2>GENERAL OPTIONS</h2>
<dl>
<dt><code>&#8211;old, -o</code></p>
<dd> Add a repo. as an old repo. Note that if you prefix the url with &quot;mirror:&quot; then the following url is treated as a mirror and not a baseurl.</p>
<dt><code>&#8211;new, -n</code></p>
<dd> Add a repo. as an new repo. Note that if you prefix the url with &quot;mirror:&quot; then the following url is treated as a mirror and not a baseurl.</p>
<dt><code>&#8211;archlist, -a</code></p>
<dd> Add architectures to change the default from just comparing source packages. Note that if you want the same as a native &quot;x86_64&quot; architecture machine you just need to pass &quot;x86_64&quot; (this is different from earlier versions where you needed to specify &quot;x86_64,athlon,i686,i586,i486,i386,noarch&quot; and you still got &quot;src&quot;).</p>
<dt><code>&#8211;size, -s</code></p>
<dd> Output additional data about the size of the changes.</p>
<dt><code>&#8211;compare-arch</code></p>
<dd> Normally packages are just compared based on their name, this flag makes the comparison also use the arch. So foo.i386 and foo.x86_64 are different.</p>
<dt><code>&#8211;simple</code></p>
<dd> Output a simple one line message for modified packages.</p>
<dt><code>&#8211;downgrade</code></p>
<dd> Split the data for modified packages between upgraded and downgraded packages.</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>Compare source pkgs in two local repos:</p>
<dd> <code>repodiff &#8211;old=/tmp/repo-old &#8211;new=/tmp/repo-new</code></p>
<dt>Compare x86_64 compat. binary pkgs in two remote repos, and two local one:</p>
<dd> <code>repodiff -a x86_64 &#8211;old=<a rel="nofollow" href="http://example.com/repo1-old">http://example.com/repo1-old</a> &#8211;old=/tmp/repo-old &#8211;new=<a href="http://example.com/repo1-new">http://example.com/repo1-new</a> &#8211;new=/tmp/repo-new</code></p>
<dt>Compare x86_64 compat. binary pkgs, but also compare arch:</p>
<dd> <code>repodiff -a x86_64 &#8211;compare-arch &#8211;old=<a rel="nofollow" href="http://example.com/repo1-old">http://example.com/repo1-old</a> &#8211;old=/tmp/repo-old &#8211;new=<a href="http://example.com/repo1-new">http://example.com/repo1-new</a> &#8211;new=/tmp/repo-new</code></p>
<dt>Compare two releases of Fedora (15 =&gt; 16):</p>
<dd> <code>repodiff &#8211;old=&#8217;mirror:<a rel="nofollow" href="https://mirrors.fedoraproject.org/metalink?repo=fedora-source-15">https://mirrors.fedoraproject.org/metalink?repo=fedora-source-15</a>&amp;arch=i386&#8242; &#8211;new=&#8217;mirror:<a href="https://mirrors.fedoraproject.org/metalink?repo=fedora-source-16">https://mirrors.fedoraproject.org/metalink?repo=fedora-source-16</a>&amp;arch=i386&#8242; &#8211;size &#8211;simple &#8211;downgrade</code></dl>
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
