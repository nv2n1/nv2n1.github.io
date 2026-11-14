---
title: "git-merge-file(1)"
name: "git-merge-file"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-merge-file/"
description: "git-merge-file – Run a three-way file merge"
---

<h2 class="name">NAME</h2>
<p> git-merge-file &#8211; Run a three-way file merge </p>
<h2>SYNOPSIS</h2>
<pre><code>
git merge - file[-L&lt;current - name&gt;[-L&lt;base - name&gt;[-L&lt;other - name&gt;]]]
                [--ours | --theirs | --union][-p | --stdout][-q | --quiet][--marker - size = &lt;n&gt;]
                [--[no - ] diff3]&lt;current - file&gt;&lt;base - file&gt;&lt;other - file&gt;
</code></pre>
<h2>DESCRIPTION</h2>
<p> <i>git merge-file</i> incorporates all changes that lead from the <code>&lt;base-file&gt;</code> to <code>&lt;other-file&gt;</code> into <code>&lt;current-file&gt;</code>. The result ordinarily goes into <code>&lt;current-file&gt;</code>. <i>git merge-file</i> is useful for combining separate changes to an original. Suppose <code>&lt;base-file&gt;</code> is the original, and both <code>&lt;current-file&gt;</code> and <code>&lt;other-file&gt;</code> are modifications of <code>&lt;base-file&gt;</code>, then <i>git merge-file</i> combines both changes. </p>
<p> A conflict occurs if both <code>&lt;current-file&gt;</code> and <code>&lt;other-file&gt;</code> have changes in a common segment of lines. If a conflict is found, <i>git merge-file</i> normally outputs a warning and brackets the conflict with lines containing &lt;&lt;&lt;&lt;&lt;&lt;&lt; and &gt;&gt;&gt;&gt;&gt;&gt;&gt; markers. A typical conflict will look like this: </p>
<dl>
<dt>
<dd>
<pre>
&lt;&lt;&lt;&lt;&lt;&lt;&lt; A
lines in file A
=======
lines in file B
&gt;&gt;&gt;&gt;&gt;&gt;&gt; B
</pre>
</dl>
<p> If there are conflicts, the user should edit the result and delete one of the alternatives. When <code>&#8211;ours</code>, <code>&#8211;theirs</code>, or <code>&#8211;union</code> option is in effect, however, these conflicts are resolved favouring lines from <code>&lt;current-file&gt;</code>, lines from <code>&lt;other-file&gt;</code>, or lines from both respectively. The length of the conflict markers can be given with the <code>&#8211;marker-size</code> option. </p>
<p> The exit value of this program is negative on error, and the number of conflicts otherwise (truncated to 127 if there are more than that many conflicts). If the merge was clean, the exit value is 0. </p>
<p> <i>git merge-file</i> is designed to be a minimal clone of RCS <i>merge</i>; that is, it implements all of RCS <i>merge</i>&#8216;s functionality which is needed by <code><a href="/docs/linux/man/1-git/">git</a></code>(1).</p>
<h2>OPTIONS</h2>
<p> -L &lt;label&gt;</p>
<dl>
<dt>
<dd> This option may be given up to three times, and specifies labels to be used in place of the corresponding file names in conflict reports. That is, <code>git merge-file -L x -L y -L z a b c</code> generates output that looks like it came from files x, y and z instead of from files a, b and c.</dl>
<p> -p</p>
<dl>
<dt>
<dd> Send results to standard output instead of overwriting <code>&lt;current-file&gt;</code>.</dl>
<p> -q</p>
<dl>
<dt>
<dd> Quiet; do not warn about conflicts.</dl>
<p> &#8211;diff3</p>
<dl>
<dt>
<dd> Show conflicts in &quot;diff3&quot; style.</dl>
<p> &#8211;ours, &#8211;theirs, &#8211;union</p>
<dl>
<dt>
<dd> Instead of leaving conflicts in the file, resolve conflicts favouring our (or their or both) side of the lines.</dl>
<h2>EXAMPLES</h2>
<p> <code>git merge-file README.my README README.upstream</code></p>
<dl>
<dt>
<dd> combines the changes of README.my and README.upstream since README, tries to merge them and writes the result into README.my.</dl>
<p> <code>git merge-file -L a -L b -L c tmp/a123 tmp/b234 tmp/c345</code></p>
<dl>
<dt>
<dd> merges tmp/a123 and tmp/c345 with the base tmp/b234, but uses labels <code>a</code> and <code>c</code> instead of <code>tmp/a123</code> and <code>tmp/c345</code>.</dl>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>
