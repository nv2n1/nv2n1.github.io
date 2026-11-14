---
title: "git-show-branch(1)"
name: "git-show-branch"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-show-branch/"
description: "git-show-branch – Show branches and their commits"
---

<h2 class="name">NAME</h2>
<p> git-show-branch &#8211; Show branches and their commits </p>
<h2>SYNOPSIS</h2>
<pre><code>
git show - branch[-a | --all][-r | --remotes][--topo - order | --date - order][--current][--color[=&lt;when&gt;] | --no - color][--sparse][--more = &lt;n&gt; | --list | --independent | --merge - base][--no - name | --sha1 - name][--topics][(&lt;rev&gt; | &lt;glob&gt;)...] git show - branch(-g | --reflog)[=&lt;n&gt;[, &lt;base&gt;]][--list][&lt;ref&gt;]
</code></pre>
<h2>DESCRIPTION</h2>
<p> Shows the commit ancestry graph starting from the commits named with &lt;rev&gt;s or &lt;glob&gt;s (or all refs under refs/heads and/or refs/tags) semi-visually. </p>
<p> It cannot show more than 29 branches and commits at a time. </p>
<p> It uses <code>showbranch.default</code> multi-valued configuration items if no &lt;rev&gt; or &lt;glob&gt; is given on the command line.</p>
<h2>OPTIONS</h2>
<p> &lt;rev&gt;</p>
<dl>
<dt>
<dd> Arbitrary extended SHA-1 expression (see <code><a href="/docs/linux/man/7-gitrevisions/">gitrevisions</a></code>(7)) that typically names a branch head or a tag.</dl>
<p> &lt;glob&gt;</p>
<dl>
<dt>
<dd> A glob pattern that matches branch or tag names under refs/. For example, if you have many topic branches under refs/heads/topic, giving <code>topic/*</code> would show all of them.</dl>
<p> -r, &#8211;remotes</p>
<dl>
<dt>
<dd> Show the remote-tracking branches.</dl>
<p> -a, &#8211;all</p>
<dl>
<dt>
<dd> Show both remote-tracking branches and local branches.</dl>
<p> &#8211;current</p>
<dl>
<dt>
<dd> With this option, the command includes the current branch to the list of revs to be shown when it is not given on the command line.</dl>
<p> &#8211;topo-order</p>
<dl>
<dt>
<dd> By default, the branches and their commits are shown in reverse chronological order. This option makes them appear in topological order (i.e., descendant commits are shown before their parents).</dl>
<p> &#8211;date-order</p>
<dl>
<dt>
<dd> This option is similar to <code>&#8211;topo-order</code> in the sense that no parent comes before all of its children, but otherwise commits are ordered according to their commit date.</dl>
<p> &#8211;sparse</p>
<dl>
<dt>
<dd> By default, the output omits merges that are reachable from only one tip being shown. This option makes them visible.</dl>
<p> &#8211;more=&lt;n&gt;</p>
<dl>
<dt>
<dd> Usually the command stops output upon showing the commit that is the common ancestor of all the branches. This flag tells the command to go &lt;n&gt; more common commits beyond that. When &lt;n&gt; is negative, display only the &lt;reference&gt;s given, without showing the commit ancestry tree.</dl>
<p> &#8211;list</p>
<dl>
<dt>
<dd> Synonym to <code>&#8211;more=-1</code></dl>
<p> &#8211;merge-base</p>
<dl>
<dt>
<dd> Instead of showing the commit list, determine possible merge bases for the specified commits. All merge bases will be contained in all specified commits. This is different from how <code><a href="/docs/linux/man/1-git-merge-base/">git-merge-base</a></code>(1) handles the case of three or more commits.</dl>
<p> &#8211;independent</p>
<dl>
<dt>
<dd> Among the &lt;reference&gt;s given, display only the ones that cannot be reached from any other &lt;reference&gt;.</dl>
<p> &#8211;no-name</p>
<dl>
<dt>
<dd> Do not show naming strings for each commit.</dl>
<p> &#8211;sha1-name</p>
<dl>
<dt>
<dd> Instead of naming the commits using the path to reach them from heads (e.g. &quot;master~2&quot; to mean the grandparent of &quot;master&quot;), name them with the unique prefix of their object names.</dl>
<p> &#8211;topics</p>
<dl>
<dt>
<dd> Shows only commits that are NOT on the first branch given. This helps track topic branches by hiding any commit that is already in the main line of development. When given &quot;git show-branch &#8211;topics master topic1 topic2&quot;, this will show the revisions given by &quot;git rev-list ^master topic1 topic2&quot;</dl>
<p> -g, &#8211;reflog[=&lt;n&gt;[,&lt;base&gt;]] [&lt;ref&gt;]</p>
<dl>
<dt>
<dd> Shows &lt;n&gt; most recent ref-log entries for the given ref. If &lt;base&gt; is given, &lt;n&gt; entries going back from that entry. &lt;base&gt; can be specified as count or date. When no explicit &lt;ref&gt; parameter is given, it defaults to the current branch (or <code>HEAD</code> if it is detached).</dl>
<p> &#8211;color[=&lt;when&gt;]</p>
<dl>
<dt>
<dd> Color the status sign (one of these: <code>*</code> <code>!</code> <code>+</code> <code>&#8211;</code>) of each commit corresponding to the branch it&#8217;s in. The value must be always (the default), never, or auto.</dl>
<p> &#8211;no-color</p>
<dl>
<dt>
<dd> Turn off colored output, even when the configuration file gives the default to color output. Same as <code>&#8211;color=never</code>.</dl>
<p> Note that &#8211;more, &#8211;list, &#8211;independent and &#8211;merge-base options are mutually exclusive.</p>
<h2>OUTPUT</h2>
<p> Given N &lt;references&gt;, the first N lines are the one-line description from their commit message. The branch head that is pointed at by $GIT_DIR/HEAD is prefixed with an asterisk <code>*</code> character while other heads are prefixed with a <code>!</code> character. </p>
<p> Following these N lines, one-line log for each commit is displayed, indented N places. If a commit is on the I-th branch, the I-th indentation character shows a <code>+</code> sign; otherwise it shows a space. Merge commits are denoted by a <code>&#8211;</code> sign. Each commit shows a short name that can be used as an extended SHA-1 to name that commit. </p>
<p> The following example shows three branches, &quot;master&quot;, &quot;fixes&quot; and &quot;mhf&quot;: </p>
<dl>
<dt>
<dd>
<pre><code>
$ git show - branch master fixes mhf *[master] Add 'git show-branch'.![fixes] Introduce "reset type" flag to "git reset" ![mhf] Allow "+remote:local" refspec to cause-- force when fetching.-- -+[mhf] Allow "+remote:local" refspec to cause-- force when fetching.+ [mhf ~1] Use git - octopus when pulling more than one heads.+ [fixes] Introduce "reset type" flag to "git reset" + [mhf ~2] "git fetch --force".+ [mhf ~3] Use.git / remote / origin, not .git / branches / origin.+ [mhf ~4] Make "git pull" and "git fetch" default to origin + [mhf ~5] Infamous 'octopus merge' + [mhf ~6] Retire git - parse - remote.+ [mhf ~7] Multi - head fetch.+ [mhf ~8] Start adding the $GIT_DIR / remotes / support.* ++[master] Add 'git show-branch'.
</code></pre>
</dl>
<p> These three branches all forked from a common commit, [master], whose commit message is &quot;Add &#8216;git show-branch&#8217;&quot;. The &quot;fixes&quot; branch adds one commit &quot;Introduce &quot;reset type&quot; flag to &quot;git reset&quot;&quot;. The &quot;mhf&quot; branch adds many other commits. The current branch is &quot;master&quot;.</p>
<h2>EXAMPLES</h2>
<p> If you keep your primary branches immediately under <code>refs/heads</code>, and topic branches in subdirectories of it, having the following in the configuration file may help: </p>
<dl>
<dt>
<dd>
<pre>
[showbranch]
        default = --topo-order
        default = heads/*
</pre>
</dl>
<p> With this, <code>git show-branch</code> without extra parameters would show only the primary branches. In addition, if you happen to be on your topic branch, it is shown as well. </p>
<dl>
<dt>
<dd>
<pre>
$ git show-branch --reflog=&quot;10,1 hour ago&quot; --list master
</pre>
</dl>
<p> shows 10 reflog entries going back from the tip as of 1 hour ago. Without <code>&#8211;list</code>, the output also shows how these tips are topologically related with each other.</p>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>
