---
title: "show-changed-rco(1)"
name: "show-changed-rco"
section: "1"
letter: "s"
url: "/docs/linux/man/1-show-changed-rco/"
description: "show-changed-rco – show changes in an RPM package"
---

<h2>NAME</h2>
<p> show-changed-rco &#8211; show changes in an RPM package</p>
<h2>SYNOPSIS</h2>
<p> <code>show-changed-rco</code> [options]</p>
<h2>DESCRIPTION</h2>
<p> <code>show-changed-rco</code> gives a compact description of the changes to a packages Requires, Conflicts and Obsoletes data from the installed (or old) to a specified rpm file.</p>
<h2>OPTIONS</h2>
<dl>
<dt>
<dt><code>-h, &#8211;help</code></p>
<dd>
<dd> show this help message and exit</p>
<dt><code>-C, &#8211;cache</code></p>
<dd> Tells repoquery to run entirely from YUM cache &#8211; does not download any metadata or update the cache. Queries in this mode can fail or give partial/incorrect results if the cache isn&#8217;t fully populated beforehand with eg &quot;yum makecache&quot;.</p>
<dt><code>-c &lt;config file&gt;, &#8211;config=&lt;config file&gt;</code></p>
<dd> Use alternative config file (default is /etc/yum.conf). </p>
<dt><code>&#8211;repoid=&lt;repo&gt;</code></p>
<dd> Specify which repository to query. Using this option disables all repositories not explicitly enabled with &#8211;repoid option (can be used multiple times). By default repoquery uses whatever repositories are enabled in YUM configuration.</p>
<dt><code>&#8211;enablerepo=&lt;repo&gt;</code></p>
<dd> In addition to the default set, query the given additional repository, even if it is disabled in YUM configuration. Can be used multiple times.</p>
<dt><code>&#8211;disablerepo=&lt;repo&gt;</code></p>
<dd> Do not query the given repository, even if it is enabled in YUM configuration. Can be used multiple times.</p>
<dt><code>&#8211;repofrompath=&lt;repoid&gt;,&lt;path/url&gt;</code></p>
<dd> Specify a path or url to a repository (same path as in a baseurl) to add to the repositories for this query. This option can be used multiple times. If you want to view only the pkgs from this repository combine this with &#8211;repoid. The repoid for the repository is specified by &lt;repoid&gt;. </p>
<dt><code>&#8211;old-packages=&lt;pkg&gt;</code></p>
<dd> Explicitly list the valid old packages to match the new packages against.</p>
<dt><code>&#8211;ignore-arch</code></p>
<dd> Ignore arch. so you can compare foo-2.i686 to foo-1.x86_64.</p>
<dt><code>&#8211;skip-new</code></p>
<dd> Only give output for packages which we&#8217;ve found an old package for. </p>
</dl>
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
