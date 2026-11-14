---
title: "git-merge-index(1)"
name: "git-merge-index"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-merge-index/"
---

<h2 class="name">NAME</h2>
 

 git-merge-index - Run a merge for files needing merging 

<h2>SYNOPSIS</h2>

 

 <pre><code>
git merge - index[-o][-q]&lt;merge - program&gt;(-a | [--]&lt;file&gt; *)
</code></pre> 

<h2>DESCRIPTION</h2>

 

 This looks up the &lt;file&gt;(s) in the index and, if there are any merge entries, passes the SHA-1 hash for those files as arguments 1, 2, 3 (empty argument if no file), and &lt;file&gt; as argument 4. File modes for the three files are passed as arguments 5, 6 and 7.

<h2>OPTIONS</h2>

 

 --
<dl>
<dt>
<dd> Do not interpret any more arguments as options.</dl>
 

 -a
<dl>
<dt>
<dd> Run merge against all files in the index that need merging.</dl>
 

 -o
<dl>
<dt>
<dd> Instead of stopping at the first failed merge, do all of them in one shot - continue with merging even when previous merges returned errors, and only return the error code after all the merges.</dl>
 

 -q
<dl>
<dt>
<dd> Do not complain about a failed merge program (a merge program failure usually indicates conflicts during the merge). This is for porcelains which might want to emit custom messages.</dl>
 

 If <i>git merge-index</i> is called with multiple &lt;file&gt;s (or -a) then it processes them in turn only stopping if merge returns a non-zero exit code. 

 Typically this is run with a script calling Git's imitation of the <i>merge</i> command from the RCS package. 

 A sample script called <i>git merge-one-file</i> is included in the distribution. 

 ALERT ALERT ALERT! The Git &quot;merge object order&quot; is different from the RCS <i>merge</i> program merge object order. In the above ordering, the original is first. But the argument order to the 3-way merge program <i>merge</i> is to have the original in the middle. Don't ask me why. 

 Examples: 

<dl>
<dt>
<dd> <pre>
torvalds [at] ppc970:~/merge-test&gt; git merge-index cat MM
This is MM from the original tree.              # original
This is modified MM in the branch A.            # merge1
This is modified MM in the branch B.            # merge2
This is modified MM in the branch B.            # current contents
</pre></dl>
 

 

 or 

<dl>
<dt>
<dd> <pre>
torvalds [at] ppc970:~/merge-test&gt; git merge-index cat AA MM
cat: : No such file or directory
This is added AA in the branch A.
This is added AA in the branch B.
This is added AA in the branch B.
fatal: merge program failed
</pre></dl>
 

 

 where the latter example shows how <i>git merge-index</i> will stop trying to merge once anything has returned an error (i.e., <b>cat</b> returned an error for the AA file, because it didn't exist in the original, and thus <i>git merge-index</i> didn't even try to merge the MM thing).

<h2>GIT</h2>

 

 Part of the <b><a HREF="/docs/linux/man/1-git/">git</a></b>(1) suite 

<h2>Index</h2>


