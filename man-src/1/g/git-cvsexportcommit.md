---
title: "git-cvsexportcommit(1)"
name: "git-cvsexportcommit"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-cvsexportcommit/"
description: "git-cvsexportcommit – Export a single commit to a CVS checkout"
---

<h2 class="name">NAME</h2>
<p> git-cvsexportcommit &#8211; Export a single commit to a CVS checkout </p>
<h2>SYNOPSIS</h2>
<pre><code>
git cvsexportcommit[-h][-u][-v][-c][-P][-p][-a][-d cvsroot]
                   [-w cvsworkdir][-W][-f][-m msgprefix][PARENTCOMMIT] COMMITID
</code></pre>
<h2>DESCRIPTION</h2>
<p> Exports a commit from Git to a CVS checkout, making it easier to merge patches from a Git repository into a CVS repository. </p>
<p> Specify the name of a CVS checkout using the -w switch or execute it from the root of the CVS working copy. In the latter case GIT_DIR must be defined. See examples below. </p>
<p> It does its best to do the safe thing, it will check that the files are unchanged and up to date in the CVS checkout, and it will not autocommit by default. </p>
<p> Supports file additions, removals, and commits that affect binary files. </p>
<p> If the commit is a merge commit, you must tell <i>git cvsexportcommit</i> what parent the changeset should be done against.</p>
<h2>OPTIONS</h2>
<p> -c</p>
<dl>
<dt>
<dd> Commit automatically if the patch applied cleanly. It will not commit if any hunks fail to apply or there were other problems.</dl>
<p> -p</p>
<dl>
<dt>
<dd> Be pedantic (paranoid) when applying patches. Invokes patch with &#8211;fuzz=0</dl>
<p> -a</p>
<dl>
<dt>
<dd> Add authorship information. Adds Author line, and Committer (if different from Author) to the message.</dl>
<p> -d</p>
<dl>
<dt>
<dd> Set an alternative CVSROOT to use. This corresponds to the CVS -d parameter. Usually users will not want to set this, except if using CVS in an asymmetric fashion.</dl>
<p> -f</p>
<dl>
<dt>
<dd> Force the merge even if the files are not up to date.</dl>
<p> -P</p>
<dl>
<dt>
<dd> Force the parent commit, even if it is not a direct parent.</dl>
<p> -m</p>
<dl>
<dt>
<dd> Prepend the commit message with the provided prefix. Useful for patch series and the like.</dl>
<p> -u</p>
<dl>
<dt>
<dd> Update affected files from CVS repository before attempting export.</dl>
<p> -k</p>
<dl>
<dt>
<dd> Reverse CVS keyword expansion (e.g. $Revision: 1.2.3.4$ becomes $Revision$) in working CVS checkout before applying patch.</dl>
<p> -w</p>
<dl>
<dt>
<dd> Specify the location of the CVS checkout to use for the export. This option does not require GIT_DIR to be set before execution if the current directory is within a Git repository. The default is the value of <i>cvsexportcommit.cvsdir</i>.</dl>
<p> -W</p>
<dl>
<dt>
<dd> Tell cvsexportcommit that the current working directory is not only a Git checkout, but also the CVS checkout. Therefore, Git will reset the working directory to the parent commit before proceeding.</dl>
<p> -v</p>
<dl>
<dt>
<dd> Verbose.</dl>
<h2>CONFIGURATION</h2>
<p> cvsexportcommit.cvsdir</p>
<dl>
<dt>
<dd> The default location of the CVS checkout to use for the export.</dl>
<h2>EXAMPLES</h2>
<p> Merge one patch into CVS</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre>
$ export GIT_DIR=~/project/.git
$ cd ~/project_cvs_checkout
$ git cvsexportcommit -v &lt;commit-sha1&gt;
$ cvs commit -F .msg &lt;files&gt;
</pre>
</dl>
</dl>
<p> Merge one patch into CVS (-c and -w options). The working directory is within the Git Repo</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre>
        $ git cvsexportcommit -v -c -w ~/project_cvs_checkout &lt;commit-sha1&gt;
</pre>
</dl>
</dl>
<p> Merge pending patches into CVS automatically &#8212; only if you really know what you are doing</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre>
$ export GIT_DIR=~/project/.git
$ cd ~/project_cvs_checkout
$ git cherry cvshead myhead | sed -n 's/^+ //p' | xargs -l1 git cvsexportcommit -c -p -v
</pre>
</dl>
</dl>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>
