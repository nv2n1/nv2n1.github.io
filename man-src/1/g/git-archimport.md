---
title: "git-archimport(1)"
name: "git-archimport"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-archimport/"
description: "git-archimport – Import an Arch repository into git"
---

<h2 class="name">NAME</h2>
<p> git-archimport &#8211; Import an Arch repository into git </p>
<h2>SYNOPSIS</h2>
<pre><code>
git archimport[-h][-v][-o][-a][-f][-T][-D depth][-t tempdir]&lt;archive / branch&gt;[:&lt;git - branch&gt;]...
</code></pre>
<h2>DESCRIPTION</h2>
<p> Imports a project from one or more Arch repositories. It will follow branches and repositories within the namespaces defined by the &lt;archive/branch&gt; parameters supplied. If it cannot find the remote branch a merge comes from it will just import it as a regular commit. If it can find it, it will mark it as a merge whenever possible (see discussion below). </p>
<p> The script expects you to provide the key roots where it can start the import from an <i>initial import</i> or <i>tag</i> type of Arch commit. It will follow and import new branches within the provided roots. </p>
<p> It expects to be dealing with one project only. If it sees branches that have different roots, it will refuse to run. In that case, edit your &lt;archive/branch&gt; parameters to define clearly the scope of the import. </p>
<p> <i>git archimport</i> uses tla extensively in the background to access the Arch repository. Make sure you have a recent version of tla available in the path. tla must know about the repositories you pass to <i>git archimport</i>. </p>
<p> For the initial import, <i>git archimport</i> expects to find itself in an empty directory. To follow the development of a project that uses Arch, rerun <i>git archimport</i> with the same parameters as the initial import to perform incremental imports. </p>
<p> While <i>git archimport</i> will try to create sensible branch names for the archives that it imports, it is also possible to specify git branch names manually. To do so, write a git branch name after each &lt;archive/branch&gt; parameter, separated by a colon. This way, you can shorten the Arch branch names and convert Arch jargon to git jargon, for example mapping a &quot;PROJECT&#8212;devo&#8212;VERSION&quot; branch to &quot;master&quot;. </p>
<p> Associating multiple Arch branches to one git branch is possible; the result will make the most sense only if no commits are made to the first branch, after the second branch is created. Still, this is useful to convert Arch repositories that had been rotated periodically.</p>
<h2>MERGES</h2>
<p> Patch merge data from Arch is used to mark merges in git as well. git does not care much about tracking patches, and only considers a merge when a branch incorporates all the commits since the point they forked. The end result is that git will have a good idea of how far branches have diverged. So the import process does lose some patch-trading metadata. </p>
<p> Fortunately, when you try and merge branches imported from Arch, git will find a good merge base, and it has a good chance of identifying patches that have been traded out-of-sequence between the branches.</p>
<h2>OPTIONS</h2>
<p> -h</p>
<dl>
<dt>
<dd> Display usage.</dl>
<p> -v</p>
<dl>
<dt>
<dd> Verbose output.</dl>
<p> -T</p>
<dl>
<dt>
<dd> Many tags. Will create a tag for every commit, reflecting the commit name in the Arch repository.</dl>
<p> -f</p>
<dl>
<dt>
<dd> Use the fast patchset import strategy. This can be significantly faster for large trees, but cannot handle directory renames or permissions changes. The default strategy is slow and safe.</dl>
<p> -o</p>
<dl>
<dt>
<dd> Use this for compatibility with old-style branch names used by earlier versions of <i>git archimport</i>. Old-style branch names were category&#8212;branch, whereas new-style branch names are archive,category&#8212;branch&#8212;version. In both cases, names given on the command-line will override the automatically-generated ones.</dl>
<p> -D &lt;depth&gt;</p>
<dl>
<dt>
<dd> Follow merge ancestry and attempt to import trees that have been merged from. Specify a depth greater than 1 if patch logs have been pruned.</dl>
<p> -a</p>
<dl>
<dt>
<dd> Attempt to auto-register archives at m[blue]<code><a rel="nofollow" href="http://mirrors.sourcecontrol.net">http://mirrors.sourcecontrol.net</a></code>m[] This is particularly useful with the -D option.</dl>
<p> -t &lt;tmpdir&gt;</p>
<dl>
<dt>
<dd> Override the default tempdir.</dl>
<p> &lt;archive/branch&gt;</p>
<dl>
<dt>
<dd> Archive/branch identifier in a format that tla log understands.</dl>
<h2>AUTHOR</h2>
<p> Written by Martin Langhoff &lt;m[blue]<code>martin [at] catalyst.net.nz</code>m[]<font SIZE="-2">[1]</font>&gt;.</p>
<h2>DOCUMENTATION</h2>
<p> Documentation by Junio C Hamano, Martin Langhoff and the git-list &lt;m[blue]<code>git [at] vger.kernel.org</code>m[]<font SIZE="-2">[2]</font>&gt;.</p>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite</p>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> martin [at] catalyst.net.nz</p>
<dl>
<dt>
<dd> mailto:martin [at] catalyst.net.nz</dl>
<dt> 2.</p>
<dd> git [at] vger.kernel.org</p>
<dl>
<dt>
<dd> mailto:git [at] vger.kernel.org</dl>
</dl>
<h2>Index</h2>
