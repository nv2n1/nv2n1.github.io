---
title: "git-info(1)"
name: "git-info"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-info/"
description: "git-info – Returns information on current repository"
---

<h2>NAME</h2>
<p> <code>git-info</code> &#8211; Returns information on current repository</p>
<h2>SYNOPSIS</h2>
<p> <code>git-info</code></p>
<h2>DESCRIPTION</h2>
<p> Shows the following information about a repository:</p>
<dl>
<dt>1.</p>
<dd> Remote Url(s)</p>
<dt>2.</p>
<dd> Remote Branches</p>
<dt>3.</p>
<dd> Local Branches</p>
<dt>4.</p>
<dd> Most recent commit</p>
<dt>5.</p>
<dd> Configuration Info</p>
<dt>
<dd></dl>
<h2>OPTIONS</h2>
<p> N/A</p>
<h2>EXAMPLES</h2>
<p> Outputs info about a repo:</p>
<dl>
<dt>
<dd>
<pre><code>
$ git info
## Remote URLs:
origin      git [at] github.com:sampleAuthor/git-extras.git (fetch)
origin      git [at] github.com:sampleAuthor/git-extras.git (push)
## Remote Branches:
origin/HEAD -&gt; origin/master
origin/myBranch
## Local Branches:
myBranch
* master
## Most Recent Commit:
commit e3952df2c172c6f3eb533d8d0b1a6c77250769a7
Author: Sample Author &lt;sampleAuthor [at] gmail.com&gt;
Added git-info command.
Type 'git log' for more commits, or 'git show &lt;commit id&gt;' for full commit details.
## Configuration (.git/config):
color.diff=auto
color.status=auto
color.branch=auto
user.name=Sample Author
user.email=sampleAuthor [at] gmail.com
core.repositoryformatversion=0
core.filemode=true
core.bare=false
core.logallrefupdates=true
core.ignorecase=true
remote.origin.fetch=+refs/heads/*:refs/remotes/origin/*
remote.origin.url=git [at] github.com:mub/git-extras.git
branch.master.remote=origin
branch.master.merge=refs/heads/master
</code></pre>
<dt>
<dd></dl>
<h2>AUTHOR</h2>
<p> Written by Leila Muhtasib &lt;<i>muhtasib [at] gmail.com</i>&gt;</p>
<h2>REPORTING BUGS</h2>
<p> &lt;<i><a rel="nofollow" href="https://github.com/tj/git-extras/issues">https://github.com/tj/git-extras/issues</a></i>&gt;</p>
<h2>SEE ALSO</h2>
<p> &lt;<i><a rel="nofollow" href="https://github.com/tj/git-extras">https://github.com/tj/git-extras</a></i>&gt; </p>
<h2>Index</h2>
