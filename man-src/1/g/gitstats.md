---
title: "gitstats(1)"
name: "gitstats"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gitstats/"
description: "gitstats – git history statistics generator"
---

<h2 class="name">NAME</h2>
<p> gitstats &#8211; git history statistics generator </p>
<h2>SYNOPSIS</h2>
<p> <code>gitstats</code> [options] &lt;repository dir&gt; &lt;output dir&gt;</p>
<h2>DESCRIPTION</h2>
<p> <code>gitstats</code> is a statistics generator for <i><a href="/docs/linux/man/1-git/">git</a></i>(1) repositories. It examines the repository and produces some interesting statistics from the history of it. Currently <font SIZE="-1">HTML</font> is the only output format.</p>
<h2>OPTIONS</h2>
<p> -c option=value </p>
<p> Override a default configuration value. Defaults can be seen by running <code>gitstats</code> without parameters.</p>
<h3>Values:</h3>
<dl>
<dt>authors_top</p>
<dd> How many top authors to show.</p>
<dt>commit_begin, commit_end</p>
<dd> Specify a commit range to generate statistics from. You can specify only commit_end limit statistics to a certain commit or another branch.</p>
<dt>linear_linestats</p>
<dd> When enabled, the lines of code statistics are collected from linear history. The downside is that commits of long feature branches appear only at the point where a merge commit is made. </p>
<p> If disabled (old behaviour), the problem is that if two branches contain the same changes (for example, removal of same lines), the statistics get skewed. </p>
<p> Defaults to on.</p>
<dt>max_authors</p>
<dd> How many authors to show in the list of authors.</p>
<dt>max_domains</p>
<dd> How many domains to show in domains by commits.</p>
<dt>max_ext_length</p>
<dd> Maximum file extension length.</p>
<dt>project_name</p>
<dd> Project name to show on the generated pages. Default is to use basename of the repository directory.</p>
<dt>style</p>
<dd> <font SIZE="-1">CSS</font> stylesheet to use.</dl>
<h2>FAQ</h2>
<p> Q: How do I generate statistics of a non-master branch? </p>
<p> A: Use <tt>&quot;-c commit_end=web&quot;</tt> parameter. </p>
<p> Q: I have files in my git repository that I would like to exclude from the statistics, how do I do that? </p>
<p> A: At the moment the only way is to use <i><a href="/docs/linux/man/1-git-filter-branch/">git-filter-branch</a></i>(1) to create a temporary repository and generate the statistics from that.</p>
<h2>EXAMPLES</h2>
<dl>
<dt>Generates statistics from a git repository in &quot;foo&quot; and outputs the result in a directory &quot;foo_stats&quot;:</p>
<dd>
<pre>
  gitstats foo foo_stats
</pre>
<dt>As above, but only analyzes the last 10 commits:</p>
<dd>
<pre>
  gitstats -c commit_begin='HEAD~10' foo foo_stats
</pre>
</dl>
<h2>AUTHORS</h2>
<p> <code>gitstats</code> was written by Heikki Hokkanen and others. </p>
<p> See the git repository at <a rel="nofollow" href="http://repo.or.cz/w/gitstats.git">http://repo.or.cz/w/gitstats.git</a> for an up-to-date full list of contributors.</p>
<h2>WWW</h2>
<p> <a rel="nofollow" href="http://gitstats.sourceforge.net/">http://gitstats.sourceforge.net/</a></p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-git/">git</a></i>(1) </p>
<h2>Index</h2>
