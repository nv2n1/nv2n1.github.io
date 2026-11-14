---
title: "git-fmt-merge-msg(1)"
name: "git-fmt-merge-msg"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-fmt-merge-msg/"
description: "git-fmt-merge-msg – Produce a merge commit message"
---

<h2 class="name">NAME</h2>
<p> git-fmt-merge-msg &#8211; Produce a merge commit message </p>
<h2>SYNOPSIS</h2>
<pre><code>
git fmt - merge - msg[-m&lt;message&gt;][--log[=&lt;n&gt;] | --no - log] git fmt - merge - msg[-m&lt;message&gt;][--log[=&lt;n&gt;] | --no - log] - F&lt;file&gt;
</code></pre>
<h2>DESCRIPTION</h2>
<p> Takes the list of merged objects on stdin and produces a suitable commit message to be used for the merge commit, usually to be passed as the <i>&lt;merge-message&gt;</i> argument of <i>git merge</i>. </p>
<p> This command is intended mostly for internal use by scripts automatically invoking <i>git merge</i>.</p>
<h2>OPTIONS</h2>
<p> &#8211;log[=&lt;n&gt;]</p>
<dl>
<dt>
<dd> In addition to branch names, populate the log message with one-line descriptions from the actual commits that are being merged. At most &lt;n&gt; commits from each merge parent will be used (20 if &lt;n&gt; is omitted). This overrides the <code>merge.log</code> configuration variable.</dl>
<p> &#8211;no-log</p>
<dl>
<dt>
<dd> Do not list one-line descriptions from the actual commits being merged.</dl>
<p> &#8211;[no-]summary</p>
<dl>
<dt>
<dd> Synonyms to &#8211;log and &#8211;no-log; these are deprecated and will be removed in the future.</dl>
<p> -m &lt;message&gt;, &#8211;message &lt;message&gt;</p>
<dl>
<dt>
<dd> Use &lt;message&gt; instead of the branch names for the first line of the log message. For use with <code>&#8211;log</code>.</dl>
<p> -F &lt;file&gt;, &#8211;file &lt;file&gt;</p>
<dl>
<dt>
<dd> Take the list of merged objects from &lt;file&gt; instead of stdin.</dl>
<h2>CONFIGURATION</h2>
<p> merge.branchdesc</p>
<dl>
<dt>
<dd> In addition to branch names, populate the log message with the branch description text associated with them. Defaults to false.</dl>
<p> merge.log</p>
<dl>
<dt>
<dd> In addition to branch names, populate the log message with at most the specified number of one-line descriptions from the actual commits that are being merged. Defaults to false, and true is a synonym for 20.</dl>
<p> merge.suppressDest</p>
<dl>
<dt>
<dd> By adding a glob that matches the names of integration branches to this multi-valued configuration variable, the default merge message computed for merges into these integration branches will omit &quot;into &lt;branch name&gt;&quot; from its title. </p>
<p> An element with an empty value can be used to clear the list of globs accumulated from previous configuration entries. When there is no <code>merge.suppressDest</code> variable defined, the default value of <code>master</code> is used for backward compatibility.</dl>
<p> merge.summary</p>
<dl>
<dt>
<dd> Synonym to <code>merge.log</code>; this is deprecated and will be removed in the future.</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>
<dd>
<pre>
$ git fetch origin master
$ git fmt-merge-msg --log &lt;$GIT_DIR/FETCH_HEAD
</pre>
</dl>
<p> Print a log message describing a merge of the &quot;master&quot; branch from the &quot;origin&quot; remote.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-git-merge/">git-merge</a></code>(1)</p>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>
