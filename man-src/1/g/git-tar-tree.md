---
title: "git-tar-tree(1)"
name: "git-tar-tree"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-tar-tree/"
description: "git-tar-tree – Create a tar archive of the files in the named tree object"
---

<h2 class="name">NAME</h2>
<p> git-tar-tree &#8211; Create a tar archive of the files in the named tree object </p>
<h2>SYNOPSIS</h2>
<pre><code>
git tar - tree[--remote = &lt;repo&gt;]&lt;tree - ish&gt;[&lt;base&gt;]
</code></pre>
<h2>DESCRIPTION</h2>
<p> THIS COMMAND IS DEPRECATED. Use <i>git archive</i> with &#8211;format=tar option instead (and move the &lt;base&gt; argument to &#8211;prefix=base/). </p>
<p> Creates a tar archive containing the tree structure for the named tree. When &lt;base&gt; is specified it is added as a leading path to the files in the generated tar archive. </p>
<p> <i>git tar-tree</i> behaves differently when given a tree ID versus when given a commit ID or tag ID. In the first case the current time is used as modification time of each file in the archive. In the latter case the commit time as recorded in the referenced commit object is used instead. Additionally the commit ID is stored in a global extended pax header. It can be extracted using <i>git get-tar-commit-id</i>.</p>
<h2>OPTIONS</h2>
<p> &lt;tree-ish&gt;</p>
<dl>
<dt>
<dd> The tree or commit to produce tar archive for. If it is the object name of a commit object.</dl>
<p> &lt;base&gt;</p>
<dl>
<dt>
<dd> Leading path to the files in the resulting tar archive.</dl>
<p> &#8211;remote=&lt;repo&gt;</p>
<dl>
<dt>
<dd> Instead of making a tar archive from local repository, retrieve a tar archive from a remote repository.</dl>
<h2>CONFIGURATION</h2>
<p> tar.umask</p>
<dl>
<dt>
<dd> This variable can be used to restrict the permission bits of tar archive entries. The default is 0002, which turns off the world write bit. The special value &quot;user&quot; indicates that the archiving user&#8217;s umask will be used instead. See <a href="/docs/linux/man/2-umask/">umask</a>(2) for details.</dl>
<h2>EXAMPLES</h2>
<p> git tar-tree HEAD junk | (cd /var/tmp/ &amp;&amp; tar xf -)</p>
<dl>
<dt>
<dd> Create a tar archive that contains the contents of the latest commit on the current branch, and extracts it in /var/tmp/junk directory.</dl>
<p> git tar-tree v1.4.0 git-1.4.0 | gzip &gt;git-1.4.0.tar.gz</p>
<dl>
<dt>
<dd> Create a tarball for v1.4.0 release.</dl>
<p> git tar-tree v1.4.0^{tree} git-1.4.0 | gzip &gt;git-1.4.0.tar.gz</p>
<dl>
<dt>
<dd> Create a tarball for v1.4.0 release, but without a global extended pax header.</dl>
<p> git tar-tree &#8211;remote=example.com:git.git v1.4.0 &gt;git-1.4.0.tar</p>
<dl>
<dt>
<dd> Get a tarball v1.4.0 from example.com.</dl>
<p> git tar-tree HEAD:Documentation/ git-docs &gt; git-1.4.0-docs.tar</p>
<dl>
<dt>
<dd> Put everything in the current head&#8217;s Documentation/ directory into <i>git-1.4.0-docs.tar</i>, with the prefix <i>git-docs/</i>.</dl>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>
