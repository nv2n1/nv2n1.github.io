---
title: "repoview(8)"
name: "repoview"
section: "8"
letter: "r"
url: "/docs/linux/man/8-repoview/"
description: "repoview – Make YUM repositories browseable"
---

<p><code>repoview</code> &#8211; Make YUM repositories browseable</p>
<h2>Synopsis</h2>
<p><code>repoview</code> [options] repodir </p>
<h2>Description</h2>
<p>RepoView allows one to easily create a set of static HTML pages in a YUM repository, allowing simple browsing of available packages. It uses kid templating engine to create the pages and is therefore easily customizeable. </p>
<h2>Options</h2>
<dl>
<dt><code>-i, &#8211;ignore-package NAME</code></dt>
<dd>Optionally ignore this package &#8212; can be a shell-style glob. This is useful for excluding debuginfo packages:<br />
 -i *debuginfo* -i *doc*<br />
 The globbing will be done against name-epoch-version-release, e.g. foo-0-1.0-1</dd>
<dt><code>-x, &#8211;exclude-arch ARCH</code></dt>
<dd>Optionally exclude this arch. E.g.:<br />
 -x src -x ia64</dd>
<dt><code>-k, &#8211;template-dir DIR</code></dt>
<dd>Use an alternative directory with kid templates instead of the default: ./templates. The template directory must contain four required template files: index.kid, group.kid, package.kid, rss.kid and the &quot;layout&quot; dir which will be copied into the repoview directory.</dd>
<dt><code>-o, &#8211;output-dir DIR</code></dt>
<dd>Create the repoview pages in this subdirectory inside the repository (default: &quot;repoview&quot;)</dd>
<dt><code>-s, &#8211;state-dir DIR</code></dt>
<dd>Create the state-tracking db in this directory (default: store in output directory)</dd>
<dt><code>-t, &#8211;title TITLE</code></dt>
<dd>Describe the repository in a few words. By default &quot;RepoView&quot; is used. E.g.:<br />
 -t &quot;Extras for Fedora Core 3 x86&quot;</dd>
<dt><code>-u, &#8211;url URL</code></dt>
<dd>Repository URL to use when generating the RSS feed. E.g.:<br />
 -u &quot;<a rel="nofollow" href="http://fedoraproject.org/extras/5/i386">http://fedoraproject.org/extras/5/i386</a>&quot;<br />
 Not providing a url will disable RSS feed generation.</dd>
<dt><code>-f, &#8211;force</code></dt>
<dd>Regenerate the pages even if the repomd checksum has not changed.</dd>
<dt><code>-q, &#8211;quiet</code></dt>
<dd>Do not output anything except fatal errors.</dd>
<dt><code>-c, &#8211;comps</code></dt>
<dd>Use an alternative comps.xml file, instead of the one specified in repomd.</dd>
<dt><code>-V, &#8211;version</code></dt>
<dd>Print version number and exit.</dd>
<dt><code>-h, &#8211;help</code></dt>
<dd>Print usage message and exit.</dd>
<dt><code>repodir</code></dt>
<dd>Where to look for the &quot;repodata&quot; directory. </dd>
</dl>
<h2>Files</h2>
<p><i>/usr/bin/repoview</i><br />
 <i>/usr/share/repoview/templates/*</i></p>
<h2>Examples</h2>
<p>The simplest invocation is: <code>repoview /path/to/repository</code><br />
 <code>repoview -t &#8216;Fedora Extras 4 ix86&#8217; /path/to/repository</code> When running from cron, you want to use the -q switch: <code>repoview -q /path/to/repository</code><br />
 This will generate an RSS feed: <code>repoview -u <a rel="nofollow" href="http://example.com/repo/i386">http://example.com/repo/i386</a> /path/to/repository</code> </p>
<h2>Authors</h2>
<p>Konstantin Ryabitsev &lt;icon [at] fedoraproject.org&gt;</p>
<h2>See Also</h2>
<p><a rel="nofollow" href="http://createrepo.baseurl.org/">http://createrepo.baseurl.org/</a> </p>
