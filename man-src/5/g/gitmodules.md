---
title: "gitmodules(5)"
name: "gitmodules"
section: "5"
letter: "g"
url: "/docs/linux/man/5-gitmodules/"
description: "gitmodules – Defining submodule properties"
---

<p>gitmodules &#8211; Defining submodule properties</p>
<h2>Synopsis</h2>
<p>$GIT_WORK_TREE/.gitmodules</p>
<h2>Description</h2>
<p>The <code>.gitmodules</code> file, located in the top-level directory of a Git working tree, is a text file with a syntax matching the requirements of <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1). </p>
<p> The file contains one subsection per submodule, and the subsection value is the name of the submodule. The name is set to the path where the submodule has been added unless it was customized with the <code>&#8211;name</code> option of <i>git submodule add</i>. Each submodule section also contains the following required keys: </p>
<p> submodule.&lt;name&gt;.path</p>
<dl>
<dd>Defines the path, relative to the top-level directory of the Git working tree, where the submodule is expected to be checked out. The path name must not end with a <code>/</code>. All submodule paths must be unique within the <code>.gitmodules</code> file.</dl>
<p> submodule.&lt;name&gt;.url</p>
<dl>
<dd>Defines a URL from which the submodule repository can be cloned. This may be either an absolute URL ready to be passed to <code><a href="/docs/linux/man/1-git-clone/">git-clone</a></code>(1) or (if it begins with <code>./</code> or <code>../</code>) a location relative to the superproject&#8217;s origin repository.</dl>
<p> In addition, there are a number of optional keys: </p>
<p> submodule.&lt;name&gt;.update</p>
<dl>
<dd>Defines the default update procedure for the named submodule, i.e. how the submodule is updated by the <code>git submodule update</code> command in the superproject. This is only used by <code>git submodule init</code> to initialize the configuration variable of the same name. Allowed values here are <i>checkout</i>, <i>rebase</i>, <i>merge</i> or <i>none</i>. See description of <i>update</i> command in <code><a href="/docs/linux/man/1-git-submodule/">git-submodule</a></code>(1) for their meaning. For security reasons, the <i>!command</i> form is not accepted here.</dl>
<p> submodule.&lt;name&gt;.branch</p>
<dl>
<dd>A remote branch name for tracking updates in the upstream submodule. If the option is not specified, it defaults to the remote <code>HEAD</code>. A special value of <code>.</code> is used to indicate that the name of the branch in the submodule should be the same name as the current branch in the current repository. See the <code>&#8211;remote</code> documentation in <code><a href="/docs/linux/man/1-git-submodule/">git-submodule</a></code>(1) for details.</dl>
<p> submodule.&lt;name&gt;.fetchRecurseSubmodules</p>
<dl>
<dd>This option can be used to control recursive fetching of this submodule. If this option is also present in the submodule&#8217;s entry in <code>.git/config</code> of the superproject, the setting there will override the one found in <code>.gitmodules</code>. Both settings can be overridden on the command line by using the <code>&#8211;[no-]recurse-submodules</code> option to <code>git fetch</code> and <code>git pull</code>.</dl>
<p> submodule.&lt;name&gt;.ignore</p>
<dl>
<dd>Defines under what circumstances <code>git status</code> and the diff family show a submodule as modified. The following values are supported: </p>
<p> all</p>
<dl>
<dd>The submodule will never be considered modified (but will nonetheless show up in the output of status and commit when it has been staged).</dl>
<p> dirty</p>
<dl>
<dd>All changes to the submodule&#8217;s work tree will be ignored, only committed differences between the <code>HEAD</code> of the submodule and its recorded state in the superproject are taken into account.</dl>
<p> untracked</p>
<dl>
<dd>Only untracked files in submodules will be ignored. Committed differences and modifications to tracked files will show up.</dl>
<p> none</p>
<dl>
<dd>No modifications to submodules are ignored, all of committed differences, and modifications to tracked and untracked files are shown. This is the default option.</dl>
<p> If this option is also present in the submodule&#8217;s entry in <code>.git/config</code> of the superproject, the setting there will override the one found in <code>.gitmodules</code>. </p>
<p> Both settings can be overridden on the command line by using the <code>&#8211;ignore-submodules</code> option. The <code>git submodule</code> commands are not affected by this setting.</dl>
<p> submodule.&lt;name&gt;.shallow</p>
<dl>
<dd>When set to true, a clone of this submodule will be performed as a shallow clone (with a history depth of 1) unless the user explicitly asks for a non-shallow clone.</dl>
<h2>Notes</h2>
<p>Git does not allow the <code>.gitmodules</code> file within a working tree to be a symbolic link, and will refuse to check out such a tree entry. This keeps behavior consistent when the file is accessed from the index or a tree versus from the filesystem, and helps Git reliably enforce security checks of the file contents.</p>
<h2>Examples</h2>
<p>Consider the following <code>.gitmodules</code> file: </p>
<dl>
<dd>
<pre>[submodule &quot;libfoo&quot;]
 path = include/foo
 url = <a href="git://foo.com/git/lib.git">git://foo.com/git/lib.git</a>
[submodule &quot;libbar&quot;]
 path = include/bar
 url = <a href="git://bar.com/git/lib.git">git://bar.com/git/lib.git</a></pre>
</dl>
<p> This defines two submodules, <code>libfoo</code> and <code>libbar</code>. These are expected to be checked out in the paths <code>include/foo</code> and <code>include/bar</code>, and for both submodules a URL is specified which can be used for cloning the submodules.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-git-submodule/">git-submodule</a></code>(1), <code><a href="/docs/linux/man/7-gitsubmodules/">gitsubmodules</a></code>(7), <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1)</p>
<h2>Git</h2>
<p>Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite</p>
