---
title: "package-cleanup(1)"
name: "package-cleanup"
section: "1"
letter: "p"
url: "/docs/linux/man/1-package-cleanup/"
description: "package-cleanup – clean up locally installed, duplicate, or orphaned packages"
---

<h2>NAME</h2>
<p> package-cleanup &#8211; clean up locally installed, duplicate, or orphaned packages</p>
<h2>SYNOPSIS</h2>
<p> <code>package-cleanup</code> [options] &lt;item &#8230;&gt;</p>
<h2>DESCRIPTION</h2>
<p> <code>package-cleanup</code> is a program for cleaning up the locally-installed RPMs. </p>
<h2>GENERAL OPTIONS</h2>
<dl>
<dt><code>-c &lt;config file&gt;</code></p>
<dd> Use alternative config file (default is /etc/yum.conf).</p>
<dt><code>-h, &#8211;help</code></p>
<dd> Help; display a help message and then quit.</p>
<dt><code>-q, &#8211;quiet</code></p>
<dd> Print out nothing unnecessary.</p>
<dt><code>-v, &#8211;version</code></p>
<dd> Report program version and exit.</p>
<dt><code>-y</code></p>
<dd> Agree to anything asked.</p>
<dt><code>&#8211;leaves</code></p>
<dd> List leaf nodes in the local RPM database. Leaf nodes are RPMs that are not relied upon by any other RPM.</p>
<dt><code>&#8211;orphans</code></p>
<dd> List installed packages which are not available from currently configured repositories. This is identical to &quot;yum list extras&quot;, which may provide better output.</p>
<dt><code>&#8211;oldkernels</code></p>
<dd> Remove old kernel and kernel-devel packages.</p>
<dt><code>&#8211;problems</code></p>
<dd> List dependency problems in the local RPM database. If any problems are found it will exit with an exit code of 1.</p>
<dt><code>&#8211;dupes</code></p>
<dd> Scan for duplicates in the local RPM database.</p>
<dt><code>&#8211;cleandupes</code></p>
<dd> Scan for duplicates in the local RPM database and clean out the older versions.</p>
<dt><code>&#8211;count &lt;COUNT&gt;</code></p>
<dd> Number of duplicate/kernel packages to keep on the system (default 2)</dl>
<h2>LEAVES OPTIONS</h2>
<dl>
<dt><code>&#8211;all</code></p>
<dd> When listing leaf nodes also list leaf nodes that are not libraries.</p>
<dt><code>&#8211;leaf-regex</code></p>
<dd> A package name that matches this regular expression will be considered a leaf.</p>
<dt><code>&#8211;exclude-devel</code></p>
<dd> When listing leaf nodes do not list development packages.</p>
<dt><code>&#8211;exclude-bin</code></p>
<dd> When listing leaf nodes do not list packages with files in bin directories.</dl>
<h2>OLDKERNELS OPTIONS</h2>
<dl>
<dt><code>&#8211;keepdevel</code></p>
<dd> Do not remove kernel-devel packages when removing kernels </p>
</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>List all dependency problems:</p>
<dd> <code>package-cleanup &#8211;problems</code></p>
<dt>List all packages that are not in any Yum repository:</p>
<dd> <code>package-cleanup &#8211;orphans</code></p>
<dt>Remove old kernels keeping 3 and leaving old kernel-devel packages installed:</p>
<dd> <code>package-cleanup &#8211;oldkernels &#8211;count=3 &#8211;keepdevel</code></dl>
<dl>
<dt>List all leaf packages with no files in a bin directory whose name begins with either &#8216;perl&#8217; or &#8216;python&#8217;:</p>
<dd> <code>package-cleanup &#8211;leaves &#8211;exclude-bin &#8211;leaf-regex=&quot;^(perl)|(python)&quot;</code></dl>
<h2>FILES</h2>
<p> As package-cleanup uses YUM libraries for retrieving all the information, it relies on YUM configuration for its default values like which repositories to use. Consult YUM documentation for details: </p>
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
