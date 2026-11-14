---
title: "git-pull-request(1)"
name: "git-pull-request"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-pull-request/"
description: "git-pull-request – Create pull request for GitHub project"
---

<h2>NAME</h2>
<p> <code>git-pull-request</code> &#8211; Create pull request for GitHub project</p>
<h2>SYNOPSIS</h2>
<p> <code>git-pull-request</code> [&lt;target branch&gt;]</p>
<h2>DESCRIPTION</h2>
<p> Create pull request for a project on GitHub via commandline. </p>
<p> Uses the email from <code>git config user.email</code> to open the pull request.</p>
<h2>OPTIONS</h2>
<p> &lt;target branch&gt; </p>
<p> The target branch you want to send pull request to.</p>
<h2>EXAMPLES</h2>
<pre><code>
$ git pull-request master
Everything up-to-date
  create pull-request for spacewander/spacewander-toolbox 'master'
  title: test
  body:
  base [master]:
Enter host password for user 'spacewanderlzx [at] gmail.com':
...
</code></pre>
<h2>AUTHOR</h2>
<p> Written by Tj Holowaychuk &lt;<i>tj [at] vision-media.ca</i>&gt;</p>
<h2>REPORTING BUGS</h2>
<p> &lt;<i><a rel="nofollow" href="https://github.com/tj/git-extras/issues">https://github.com/tj/git-extras/issues</a></i>&gt;</p>
<h2>SEE ALSO</h2>
<p> &lt;<i><a rel="nofollow" href="https://github.com/tj/git-extras">https://github.com/tj/git-extras</a></i>&gt; </p>
<h2>Index</h2>
