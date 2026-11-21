---

title: "git-fork(1)"
name: "git-fork"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-fork/"
description: "git-fork – Fork a repo on github"
---

<p> <code>git-fork</code> &#8211; Fork a repo on github</p>
<h2>SYNOPSIS</h2>
<p> <code>git-fork</code> [&lt;github-repo-url&gt;]</p>
<h2>DESCRIPTION</h2>
<p> If a github repo url is given, fork the repo. Like clone but forks first.</p>
<dl>
<dt>1.</dt>
<dd> forks the repo on github</dd>
<dt>2.</dt>
<dd> clones the repo into the current dir</dd>
<dt>3.</dt>
<dd> adds the original repo as a remote called <code>upstream</code></dd>
</dl>
<p> If a url is not given and the current dir is a github repo, fork the repo.</p>
<dl>
<dt>1.</dt>
<dd> forks the current repo</dd>
<dt>2.</dt>
<dd> rename the <code>origin</code> remote repo to <code>upstream</code></dd>
<dt>3.</dt>
<dd> adds the forked repo as a remote called <code>origin</code></dd>
</dl>
<p> Remotes will use ssh if you have it configured with GitHub, if not, https will be used.</p>
<h2>EXAMPLE</h2>
<p> Fork expect.js:</p>
<dl>
<dt>
</dt><dd>
<pre>
$ git fork <a rel="nofollow" href="https://github.com/LearnBoost/expect.js">https://github.com/LearnBoost/expect.js</a>
</pre>
</dd></dl>
<p> or just:</p>
<dl>
<dt>
</dt><dd>
<pre>
$ git fork LearnBoost/expect.js
</pre>
</dd></dl>
<p> Then:</p>
<dl>
<dt>
</dt><dd>
<pre><code>
$..&lt;forks into your github profile and clones repo locally to expect.js dir&gt;... $ cd expect.js &amp;&amp;git remote - v
                                                                                                                      origin git[at] github.com : &lt;user&gt; /
                                                                                                                  expect.js(fetch)
                                                                                                                      origin git[at] github.com : &lt;user&gt; /
                                                                                                                  expect.js(push)
                                                                                                                      upstream git[at] github.com : LearnBoost
                                                                                                                  / expect.js(fetch) upstream git[at] github.com : LearnBoost / expect.js(push)
</code></pre>
</dd></dl>
<p> If the current dir is a clone of expect.js, this has the same effect:</p>
<dl>
<dt>
</dt><dd>
<pre>
$ git fork
</pre>
</dd></dl>
<h2>AUTHOR</h2>
<p> Written by Andrew Griffiths &lt;<i>mail [at] andrewgriffithsonline.com</i>&gt;</p>
<h2>REPORTING BUGS</h2>
<p> &lt;<i><a rel="nofollow" href="https://github.com/tj/git-extras/issues">https://github.com/tj/git-extras/issues</a></i>&gt;</p>
<h2>SEE ALSO</h2>
<p> &lt;<i><a rel="nofollow" href="https://github.com/tj/git-extras">https://github.com/tj/git-extras</a></i>&gt; </p>
