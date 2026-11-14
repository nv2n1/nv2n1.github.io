---
title: "git-fork(1)"
name: "git-fork"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-fork/"
description: "git-fork – Fork a repo on github"
---

<h2>NAME</h2>
<p> <code>git-fork</code> &#8211; Fork a repo on github</p>
<h2>SYNOPSIS</h2>
<p> <code>git-fork</code> [&lt;github-repo-url&gt;]</p>
<h2>DESCRIPTION</h2>
<p> If a github repo url is given, fork the repo. Like clone but forks first.</p>
<dl>
<dt>1.</p>
<dd> forks the repo on github</p>
<dt>2.</p>
<dd> clones the repo into the current dir</p>
<dt>3.</p>
<dd> adds the original repo as a remote called <code>upstream</code></p>
<dt>
<dd></dl>
<p> If a url is not given and the current dir is a github repo, fork the repo.</p>
<dl>
<dt>1.</p>
<dd> forks the current repo</p>
<dt>2.</p>
<dd> rename the <code>origin</code> remote repo to <code>upstream</code></p>
<dt>3.</p>
<dd> adds the forked repo as a remote called <code>origin</code></p>
<dt>
<dd></dl>
<p> Remotes will use ssh if you have it configured with GitHub, if not, https will be used.</p>
<h2>EXAMPLE</h2>
<p> Fork expect.js:</p>
<dl>
<dt>
<dd>
<pre>
$ git fork <a rel="nofollow" href="https://github.com/LearnBoost/expect.js">https://github.com/LearnBoost/expect.js</a>
</pre>
<dt>
<dd></dl>
<p> or just:</p>
<dl>
<dt>
<dd>
<pre>
$ git fork LearnBoost/expect.js
</pre>
<dt>
<dd></dl>
<p> Then:</p>
<dl>
<dt>
<dd>
<pre><code>
$..&lt;forks into your github profile and clones repo locally to expect.js dir&gt;... $ cd expect.js &amp;&amp;git remote - v
                                                                                                                      origin git[at] github.com : &lt;user&gt; /
                                                                                                                  expect.js(fetch)
                                                                                                                      origin git[at] github.com : &lt;user&gt; /
                                                                                                                  expect.js(push)
                                                                                                                      upstream git[at] github.com : LearnBoost
                                                                                                                  / expect.js(fetch) upstream git[at] github.com : LearnBoost / expect.js(push)
</code></pre>
<dt>
<dd></dl>
<p> If the current dir is a clone of expect.js, this has the same effect:</p>
<dl>
<dt>
<dd>
<pre>
$ git fork
</pre>
<dt>
<dd></dl>
<h2>AUTHOR</h2>
<p> Written by Andrew Griffiths &lt;<i>mail [at] andrewgriffithsonline.com</i>&gt;</p>
<h2>REPORTING BUGS</h2>
<p> &lt;<i><a rel="nofollow" href="https://github.com/tj/git-extras/issues">https://github.com/tj/git-extras/issues</a></i>&gt;</p>
<h2>SEE ALSO</h2>
<p> &lt;<i><a rel="nofollow" href="https://github.com/tj/git-extras">https://github.com/tj/git-extras</a></i>&gt; </p>
<h2>Index</h2>
