---

title: "find-repos-of-install(1)"
name: "find-repos-of-install"
section: "1"
letter: "f"
url: "/docs/linux/man/1-find-repos-of-install/"
description: "find-repos-of-install – report which Yum repository a package was installed from"
---

<h2>NAME</h2>
<p> find-repos-of-install &#8211; report which Yum repository a package was installed from</p>
<p> <code>find-repos-of-install</code> [options] package1 [package2&#8230;]</p>
<p> <code>find-repos-of-install</code> is a program which reports the Yum repository that a specified package was installed from. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;version</code></dt>
<dd> Report program version and exit.</dd>
<dt><code>-h, &#8211;help</code></dt>
<dd> Display a help message, and then quit.</dd>
<dt><code>&#8211;repoid=REPOID</code></dt>
<dd> Specify repo ids to query, can be specified multiple times (default is all enabled).</dd>
<dt><code>&#8211;enablerepo=ENABLEREPOS</code></dt>
<dd> In addition to the default set, query the given additional repository, even if it is disabled in YUM configuration. Can be used multiple times.</dd>
<dt><code>&#8211;disablerepo=DISABLEREPOS</code></dt>
<dd> Do not query the given repository, even if it is enabled in YUM configuration. Can be used multiple times.</dd>
<dt><code>&#8211;repofrompath=REPOID,PATH/URL</code></dt>
<dd> Specify a path or url to a repository (same path as in a baseurl) to add to the repositories for this query. This option can be used multiple times. If you want to view only the pkgs from this repository combine this with &#8211;repoid. The repoid for the repository is specified by REPOID.</dd>
<dt><code>-C, &#8211;cache</code></dt>
<dd> Tells repoquery to run entirely from YUM cache &#8211; does not download any metadata or update the cache. Queries in this mode can fail or give partial/incorrect results if the cache isn&#8217;t fully populated beforehand with eg &quot;yum makecache&quot;.</dd>
<dt><code>&#8211;tempcache</code></dt>
<dd> Use a temp dir for storing/accessing yum-cache.</dd>
<dt><code>&#8211;sync2yumdb</code></dt>
<dd> Sync anything that is found to the yumdb, if available. </dd>
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
