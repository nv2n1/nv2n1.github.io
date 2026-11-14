---
title: "reposync(1)"
name: "reposync"
section: "1"
letter: "r"
url: "/docs/linux/man/1-reposync/"
description: "reposync – synchronize yum repositories to a local directory"
---

<h2>NAME</h2>
<p> reposync &#8211; synchronize yum repositories to a local directory</p>
<h2>SYNOPSIS</h2>
<p> <code>reposync</code> [options]</p>
<h2>DESCRIPTION</h2>
<p> <code>reposync</code> is used to synchronize a remote yum repository to a local directory, using yum to retrieve the packages.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Display a help message, and then quit.</p>
<dt><code>-c CONFIG, &#8211;config=CONFIG</code></p>
<dd> Config file to use (defaults to /etc/yum.conf).</p>
<dt><code>-a ARCH, &#8211;arch=ARCH</code></p>
<dd> Act as if running the specified arch (default: current arch, note: does not override $releasever. x86_64 is a superset for i*86.).</p>
<dt><code>&#8211;source</code></p>
<dd> Also download .src.rpm files.</p>
<dt><code>-r REPOID, &#8211;repoid=REPOID</code></p>
<dd> Specify repo ids to query, can be specified multiple times (default is all enabled).</p>
<dt><code>-e CACHEDIR, &#8211;cachedir CACHEDIR</code></p>
<dd> Directory in which to store metadata.</p>
<dt><code>-t, &#8211;tempcache</code></p>
<dd> Use a temp dir for storing/accessing yum-cache.</p>
<dt><code>-d, &#8211;delete</code></p>
<dd> Delete local packages no longer present in repository.</p>
<dt><code>-p DESTDIR, &#8211;download_path=DESTDIR</code></p>
<dd> Path to download packages to: defaults to current directory.</p>
<dt><code>&#8211;norepopath</code></p>
<dd> Don&#8217;t add the reponame to the download path. Can only be used when syncing a single repository (default is to add the reponame).</p>
<dt><code>-g, &#8211;gpgcheck</code></p>
<dd> Remove packages that fail GPG signature checking after downloading. exit status is &#8216;1&#8217; if at least one package was removed.</p>
<dt><code>-u, &#8211;urls</code></p>
<dd> Just list urls of what would be downloaded, don&#8217;t download.</p>
<dt><code>-l, &#8211;plugins</code></p>
<dd> Enable yum plugin support.</p>
<dt><code>-m, &#8211;downloadcomps</code></p>
<dd> Also download comps.xml.</p>
<dt><code>&#8211;download-metadata</code></p>
<dd> Download all the non-default metadata.</p>
<dt><code>-n, &#8211;newest-only</code></p>
<dd> Download only newest packages per-repo.</p>
<dt><code>-q, &#8211;quiet</code></p>
<dd> Output as little information as possible.</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>Sync all packages from the &#8216;updates&#8217; repo to the current directory:</p>
<dd> <code> reposync &#8211;repoid=updates</code></p>
<dt>Sync only the newest packages from the &#8216;updates&#8217; repo to the current directory:</p>
<dd> <code> reposync -n &#8211;repoid=updates</code></p>
<dt>Sync packages from the &#8216;updates&#8217; and &#8216;extras&#8217; repos to the current directory:</p>
<dd> <code> reposync &#8211;repoid=updates &#8211;repoid=extras</code></p>
<dt>Sync all packages from the &#8216;updates&#8217; repo to the <code>repos</code> directory:</p>
<dd> <code> reposync -p repos &#8211;repoid=updates</code></p>
<dt>Sync all packages from the &#8216;updates&#8217; repo to the <code>repos</code> directory excluding x86_64 arch. Edit <i>/etc/yum.conf</i> adding option <code>exclude=*.x86_64</code>. Then:</p>
<dd> <code>reposync -p repos &#8211;repoid=updates</code></dl>
<h2>FILES</h2>
<p> <code>reposync</code> uses the yum libraries for retrieving information and packages. If no configuration file is specified, the default yum configuration will be used. </p>
<pre>
/etc/yum.conf
/etc/yum/repos.d/
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
