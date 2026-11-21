---

title: "stg-reset(1)"
name: "stg-reset"
section: "1"
letter: "s"
url: "/docs/linux/man/1-stg-reset/"
description: "stg-reset – Reset the patch stack to an earlier state"
---

<pre><code>
stg reset[options][--][&lt;state&gt;[&lt;patchnames&gt;]]
</code></pre>
<p> Reset the patch stack to an earlier state. If no state is specified, reset only the changes in the worktree. </p>
<p> The state is specified with a commit id from a stack log; &quot;stg log&quot; lets you view this log, and &quot;stg reset&quot; lets you reset to any state you see in the log. If one or more patch names are given, reset only those patches, and leave the rest alone.</p>
<h2>OPTIONS</h2>
<p> &#8211;hard</p>
<dl>
<dt>
</dt><dd> Discard changes in your index/worktree.</dd></dl>
<h2>STGIT</h2>
<p> Part of the StGit suite &#8211; see <code><a href="/docs/linux/man/1-stg/">stg</a></code>(1) </p>
