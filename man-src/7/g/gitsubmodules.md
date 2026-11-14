---
title: "gitsubmodules(7)"
name: "gitsubmodules"
section: "7"
letter: "g"
url: "/docs/linux/man/7-gitsubmodules/"
description: "gitsubmodules – Mounting one repository inside another"
---

<p>gitsubmodules &#8211; Mounting one repository inside another</p>
<h2>Synopsis</h2>
<pre>.gitmodules, $GIT_DIR/config</pre>
<pre>git submodule
git &lt;command&gt; --recurse-submodules</pre>
<h2>Description</h2>
<p>A submodule is a repository embedded inside another repository. The submodule has its own history; the repository it is embedded in is called a superproject. </p>
<p> On the filesystem, a submodule usually (but not always &#8211; see FORMS below) consists of (i) a Git directory located under the <code>$GIT_DIR/modules/</code> directory of its superproject, (ii) a working directory inside the superproject&#8217;s working directory, and a <code>.git</code> file at the root of the submodule&#8217;s working directory pointing to (i). </p>
<p> Assuming the submodule has a Git directory at <code>$GIT_DIR/modules/foo/</code> and a working directory at <code>path/to/bar/</code>, the superproject tracks the submodule via a <code>gitlink</code> entry in the tree at <code>path/to/bar</code> and an entry in its <code>.gitmodules</code> file (see <code><a href="/docs/linux/man/5-gitmodules/">gitmodules</a></code>(5)) of the form <code>submodule.foo.path = path/to/bar</code>. </p>
<p> The <code>gitlink</code> entry contains the object name of the commit that the superproject expects the submodule&#8217;s working directory to be at. </p>
<p> The section <code>submodule.foo.*</code> in the <code>.gitmodules</code> file gives additional hints to Git&#8217;s porcelain layer. For example, the <code>submodule.foo.url</code> setting specifies where to obtain the submodule. </p>
<p> Submodules can be used for at least two different use cases: </p>
<dl>
<dd>1. Using another project while maintaining independent history. Submodules allow you to contain the working tree of another project within your own working tree while keeping the history of both projects separate. Also, since submodules are fixed to an arbitrary version, the other project can be independently developed without affecting the superproject, allowing the superproject project to fix itself to new versions only when desired.</dl>
<dl>
<dd>2. Splitting a (logically single) project into multiple repositories and tying them back together. This can be used to overcome current limitations of Git&#8217;s implementation to have finer grained access: </p>
<dl>
<dd>&bull; Size of the Git repository: In its current form Git scales up poorly for large repositories containing content that is not compressed by delta computation between trees. For example, you can use submodules to hold large binary assets and these repositories can be shallowly cloned such that you do not have a large history locally.</dl>
<dl>
<dd>&bull; Transfer size: In its current form Git requires the whole working tree present. It does not allow partial trees to be transferred in fetch or clone. If the project you work on consists of multiple repositories tied together as submodules in a superproject, you can avoid fetching the working trees of the repositories you are not interested in.</dl>
<dl>
<dd>&bull; Access control: By restricting user access to submodules, this can be used to implement read/write policies for different users.</dl>
</dl>
<h2>The Configuration Of Submodules</h2>
<p>Submodule operations can be configured using the following mechanisms (from highest to lowest precedence): </p>
<dl>
<dd>&bull; The command line for those commands that support taking submodules as part of their pathspecs. Most commands have a boolean flag <code>&#8211;recurse-submodules</code> which specify whether to recurse into submodules. Examples are <code>grep</code> and <code>checkout</code>. Some commands take enums, such as <code>fetch</code> and <code>push</code>, where you can specify how submodules are affected.</dl>
<dl>
<dd>&bull; The configuration inside the submodule. This includes <code>$GIT_DIR/config</code> in the submodule, but also settings in the tree such as a <code>.gitattributes</code> or <code>.gitignore</code> files that specify behavior of commands inside the submodule. </p>
<p> For example an effect from the submodule&#8217;s <code>.gitignore</code> file would be observed when you run <code>git status &#8211;ignore-submodules=none</code> in the superproject. This collects information from the submodule&#8217;s working directory by running <code>status</code> in the submodule while paying attention to the <code>.gitignore</code> file of the submodule. </p>
<p> The submodule&#8217;s <code>$GIT_DIR/config</code> file would come into play when running <code>git push &#8211;recurse-submodules=check</code> in the superproject, as this would check if the submodule has any changes not published to any remote. The remotes are configured in the submodule as usual in the <code>$GIT_DIR/config</code> file.</dl>
<dl>
<dd>&bull; The configuration file <code>$GIT_DIR/config</code> in the superproject. Git only recurses into active submodules (see &quot;ACTIVE SUBMODULES&quot; section below). </p>
<p> If the submodule is not yet initialized, then the configuration inside the submodule does not exist yet, so where to obtain the submodule from is configured here for example.</dl>
<dl>
<dd>&bull; The <code>.gitmodules</code> file inside the superproject. A project usually uses this file to suggest defaults for the upstream collection of repositories for the mapping that is required between a submodule&#8217;s name and its path. </p>
<p> This file mainly serves as the mapping between the name and path of submodules in the superproject, such that the submodule&#8217;s Git directory can be located. </p>
<p> If the submodule has never been initialized, this is the only place where submodule configuration is found. It serves as the last fallback to specify where to obtain the submodule from.</dl>
<h2>Forms</h2>
<p>Submodules can take the following forms: </p>
<dl>
<dd>&bull; The basic form described in DESCRIPTION with a Git directory, a working directory, a <code>gitlink</code>, and a <code>.gitmodules</code> entry.</dl>
<dl>
<dd>&bull; &quot;Old-form&quot; submodule: A working directory with an embedded <code>.git</code> directory, and the tracking <code>gitlink</code> and <code>.gitmodules</code> entry in the superproject. This is typically found in repositories generated using older versions of Git. </p>
<p> It is possible to construct these old form repositories manually. </p>
<p> When deinitialized or deleted (see below), the submodule&#8217;s Git directory is automatically moved to <code>$GIT_DIR/modules/&lt;name&gt;/</code> of the superproject.</dl>
<dl>
<dd>&bull; Deinitialized submodule: A <code>gitlink</code>, and a <code>.gitmodules</code> entry, but no submodule working directory. The submodule&#8217;s Git directory may be there as after deinitializing the Git directory is kept around. The directory which is supposed to be the working directory is empty instead. </p>
<p> A submodule can be deinitialized by running <code>git submodule deinit</code>. Besides emptying the working directory, this command only modifies the superproject&#8217;s <code>$GIT_DIR/config</code> file, so the superproject&#8217;s history is not affected. This can be undone using <code>git submodule init</code>.</dl>
<dl>
<dd>&bull; Deleted submodule: A submodule can be deleted by running <code>git rm &lt;submodule path&gt; &amp;&amp; git commit</code>. This can be undone using <code>git revert</code>. </p>
<p> The deletion removes the superproject&#8217;s tracking data, which are both the <code>gitlink</code> entry and the section in the <code>.gitmodules</code> file. The submodule&#8217;s working directory is removed from the file system, but the Git directory is kept around as it to make it possible to checkout past commits without requiring fetching from another repository. </p>
<p> To completely remove a submodule, manually delete <code>$GIT_DIR/modules/&lt;name&gt;/</code>.</dl>
<h2>Active Submodules</h2>
<p>A submodule is considered active, </p>
<dl>
<dd>1. if <code>submodule.&lt;name&gt;.active</code> is set to <code>true</code> </p>
<p> or</dl>
<dl>
<dd>2. if the submodule&#8217;s path matches the pathspec in <code>submodule.active</code> </p>
<p> or</dl>
<dl>
<dd>3. if <code>submodule.&lt;name&gt;.url</code> is set.</dl>
<p> and these are evaluated in this order. </p>
<p> For example: </p>
<dl>
<dd>
<pre>[submodule &quot;foo&quot;]
 active = false
 url = <a rel="nofollow" href="https://example.org/foo">https://example.org/foo</a>
[submodule &quot;bar&quot;]
 active = true
 url = <a rel="nofollow" href="https://example.org/bar">https://example.org/bar</a>
[submodule &quot;baz&quot;]
 url = <a rel="nofollow" href="https://example.org/baz">https://example.org/baz</a></pre>
</dl>
<p> In the above config only the submodule <i>bar</i> and <i>baz</i> are active, <i>bar</i> due to (1) and <i>baz</i> due to (3). <i>foo</i> is inactive because (1) takes precedence over (3) </p>
<p> Note that (3) is a historical artefact and will be ignored if the (1) and (2) specify that the submodule is not active. In other words, if we have a <code>submodule.&lt;name&gt;.active</code> set to <code>false</code> or if the submodule&#8217;s path is excluded in the pathspec in <code>submodule.active</code>, the url doesn&#8217;t matter whether it is present or not. This is illustrated in the example that follows. </p>
<dl>
<dd>
<pre>[submodule &quot;foo&quot;]
 active = true
 url = <a rel="nofollow" href="https://example.org/foo">https://example.org/foo</a>
[submodule &quot;bar&quot;]
 url = <a rel="nofollow" href="https://example.org/bar">https://example.org/bar</a>
[submodule &quot;baz&quot;]
 url = <a rel="nofollow" href="https://example.org/baz">https://example.org/baz</a>
[submodule &quot;bob&quot;]
 ignore = true
[submodule]
 active = b*
 active = :(exclude) baz</pre>
</dl>
<p> In here all submodules except <i>baz</i> (foo, bar, bob) are active. <i>foo</i> due to its own active flag and all the others due to the submodule active pathspec, which specifies that any submodule starting with <i>b</i> except <i>baz</i> are also active, regardless of the presence of the .url field.</p>
<h2>Workflow For A Third Party Library</h2>
<dl>
<dd>
<pre># Add a submodule
git submodule add &lt;url&gt; &lt;path&gt;</pre>
</dl>
<dl>
<dd>
<pre># Occasionally update the submodule to a new version:
git -C &lt;path&gt; checkout &lt;new version&gt;
git add &lt;path&gt;
git commit -m &quot;update submodule to new version&quot;</pre>
</dl>
<dl>
<dd>
<pre># See the list of submodules in a superproject
git submodule status</pre>
</dl>
<dl>
<dd>
<pre># See FORMS on removing submodules</pre>
</dl>
<h2>Workflow For An Artificially Split Repo</h2>
<dl>
<dd>
<pre># Enable recursion for relevant commands, such that
# regular commands recurse into submodules by default
git config --global submodule.recurse true</pre>
</dl>
<dl>
<dd>
<pre># Unlike most other commands below, clone still needs
# its own recurse flag:
git clone --recurse &lt;URL&gt; &lt;directory&gt;
cd &lt;directory&gt;</pre>
</dl>
<dl>
<dd>
<pre># Get to know the code:
git grep foo
git ls-files --recurse-submodules</pre>
</dl>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font> </p>
<p> <code>git ls-files</code> also requires its own <code>&#8211;recurse-submodules</code> flag. </p>
</dl>
<dl>
<dd>
<pre># Get new code
git fetch
git pull --rebase</pre>
</dl>
<dl>
<dd>
<pre># Change worktree
git checkout
git reset</pre>
</dl>
<h2>Implementation Details</h2>
<p>When cloning or pulling a repository containing submodules the submodules will not be checked out by default; you can instruct <code>clone</code> to recurse into submodules. The <code>init</code> and <code>update</code> subcommands of <code>git submodule</code> will maintain submodules checked out and at an appropriate revision in your working tree. Alternatively you can set <code>submodule.recurse</code> to have <code>checkout</code> recursing into submodules (note that <code>submodule.recurse</code> also affects other Git commands, see <code><a href="/docs/linux/man/1-git-config/">git-config</a></code>(1) for a complete list).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-git-submodule/">git-submodule</a></code>(1), <code><a href="/docs/linux/man/5-gitmodules/">gitmodules</a></code>(5).</p>
<h2>Git</h2>
<p>Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite</p>
