---
title: "git-scp(1)"
name: "git-scp"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-scp/"
description: "git-scp – Copy files to SSH compatible git-remote"
---

<h2>NAME</h2>
<p> <code>git-scp</code> &#8211; Copy files to SSH compatible <code>git-remote</code></p>
<h2>SYNOPSIS</h2>
<pre>
`git scp` -h|help|?
`git scp` &lt;remote&gt; [&lt;commits&gt;...|&lt;path&gt;...]
`git rscp` &lt;remote&gt; &lt;path&gt;
</pre>
<h2>DESCRIPTION</h2>
<p> A convenient way to copy files from the current working tree to the working directory of a remote repository. If a <code>&lt;commits&gt;&#8230;</code> is provided, only files that has changed within the commit range will be copied. </p>
<p> Internally this script uses <code>rsync</code> and not <code>scp</code> as the name suggests. </p>
<p> <code>git-rscp</code> &#8211; The reverse of <code>git-scp</code>. Copies specific files from the working directory of a remote repository to the current working directory.</p>
<h2>OPTIONS</h2>
<p> &lt;remote&gt;</p>
<dl>
<dt>
<dd>
<pre>
The git remote where you want to copy your files.
</pre>
<dt>
<dd></dl>
<p> &lt;commits&gt;&#8230;</p>
<dl>
<dt>
<dd>
<pre>
Any commit, commit range or tree. Uses `git-diff`(1)
</pre>
<dt>
<dd></dl>
<p> &lt;path&gt;&#8230;</p>
<dl>
<dt>
<dd>
<pre>
The &lt;paths&gt; parameters, when given, are used to limit the diff to the named paths (you can give directory names and get diff for all files under them).
</pre>
<dt>
<dd></dl>
<h2>GIT CONFIGS</h2>
<p> To sanitize files using <code>dos2unix</code> before copying files</p>
<dl>
<dt>
<dd>
<pre>
$ git config --global --add extras.scp.sanitize dos2unix
</pre>
<dt>
<dd></dl>
<p> You can run the files through PHP lint (i.e. <code>php -l</code>) before copying files</p>
<dl>
<dt>
<dd>
<pre>
$ git config --global --add extras.scp.sanitize php_lint
</pre>
<dt>
<dd></dl>
<h2>EXAMPLES</h2>
<p> Make sure you have <code><a href="/docs/linux/man/1-git-remote/">git-remote</a></code>(1) setup</p>
<dl>
<dt>
<dd>
<pre>
$ git remote add staging myStagingServer:/var/www/html
</pre>
<dt>
<dd></dl>
<p> Copy unstaged files to remote. Useful when you want to make quick test without making any commits</p>
<dl>
<dt>
<dd>
<pre>
$ git scp staging
</pre>
<dt>
<dd></dl>
<p> Copy staged and unstaged files to remote</p>
<dl>
<dt>
<dd>
<pre>
$ git scp staging HEAD
</pre>
<dt>
<dd></dl>
<p> Copy files that has been changed in the last commit, plus any staged or unstaged files to remote</p>
<dl>
<dt>
<dd>
<pre>
$ git scp staging HEAD~1
</pre>
<dt>
<dd></dl>
<p> Copy files that has been changed between now and a tag</p>
<dl>
<dt>
<dd>
<pre>
$ git scp staging v1.2.3
</pre>
<dt>
<dd></dl>
<p> Copy specific files</p>
<dl>
<dt>
<dd>
<pre>
$ git scp staging index.html .gitignore .htaccess
</pre>
<dt>
<dd></dl>
<p> Copy specific directory</p>
<dl>
<dt>
<dd>
<pre>
$ git scp staging js/vendor/
</pre>
<dt>
<dd></dl>
<p> Copy files from specific directory to multiple servers</p>
<dl>
<dt>
<dd>
<pre><code>
$ for dest in web1 web2 web3;
do
    git diff-- name - only 4.8.3 4.8.2 app / code / community app / design skin / | xargs git scp $dest
                                                                                        done;
</code></pre>
<dt>
<dd></dl>
<h2>AUTHOR</h2>
<p> Written by Chern Jie &lt;<i>lim [at] chernjie.com</i>&gt;</p>
<h2>REPORTING BUGS</h2>
<p> &lt;<i><a rel="nofollow" href="https://github.com/chernjie/git-extras/issues">https://github.com/chernjie/git-extras/issues</a></i>&gt;</p>
<h2>SEE ALSO</h2>
<p> &lt;<i><a rel="nofollow" href="https://github.com/tj/git-extras">https://github.com/tj/git-extras</a></i>&gt; </p>
<h2>Index</h2>
