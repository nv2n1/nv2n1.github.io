---
title: "git-whatchanged(1)"
name: "git-whatchanged"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-whatchanged/"
description: "git-whatchanged – Show logs with difference each commit introduces"
---

<h2 class="name">NAME</h2>
<p> git-whatchanged &#8211; Show logs with difference each commit introduces </p>
<h2>SYNOPSIS</h2>
<pre>
<i>git whatchanged</i> &lt;option&gt;...
</pre>
<h2>DESCRIPTION</h2>
<p> Shows commit logs and diff output each commit introduces. </p>
<p> New users are encouraged to use <code><a href="/docs/linux/man/1-git-log/">git-log</a></code>(1) instead. The <code>whatchanged</code> command is essentially the same as <code><a href="/docs/linux/man/1-git-log/">git-log</a></code>(1) but defaults to show the raw format diff output and to skip merges. </p>
<p> The command is kept primarily for historical reasons; fingers of many people who learned Git long before <code>git log</code> was invented by reading Linux kernel mailing list are trained to type it.</p>
<h2>EXAMPLES</h2>
<p> <code>git whatchanged -p v2.6.12.. include/scsi drivers/scsi</code></p>
<dl>
<dt>
<dd> Show as patches the commits since version <i>v2.6.12</i> that changed any file in the include/scsi or drivers/scsi subdirectories</dl>
<p> <code>git whatchanged &#8211;since=&quot;2 weeks ago&quot; &#8212; gitk</code></p>
<dl>
<dt>
<dd> Show the changes during the last two weeks to the file <i>gitk</i>. The &quot;&#8211;&quot; is necessary to avoid confusion with the <code>branch</code> named <i>gitk</i></dl>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>
