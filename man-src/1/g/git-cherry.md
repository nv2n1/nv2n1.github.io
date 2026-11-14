---
title: "git-cherry(1)"
name: "git-cherry"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-cherry/"
description: "git-cherry – Find commits yet to be applied to upstream"
---

<h2 class="name">NAME</h2>
<p> git-cherry &#8211; Find commits yet to be applied to upstream </p>
<h2>SYNOPSIS</h2>
<pre><code>
git cherry[-v][&lt;upstream&gt;[&lt;head&gt;[&lt;limit&gt;]]]
</code></pre>
<h2>DESCRIPTION</h2>
<p> Determine whether there are commits in <code>&lt;head&gt;..&lt;upstream&gt;</code> that are equivalent to those in the range <code>&lt;limit&gt;..&lt;head&gt;</code>. </p>
<p> The equivalence test is based on the diff, after removing whitespace and line numbers. git-cherry therefore detects when commits have been &quot;copied&quot; by means of <code><a href="/docs/linux/man/1-git-cherry-pick/">git-cherry-pick</a></code>(1), <code><a href="/docs/linux/man/1-git-am/">git-am</a></code>(1) or <code><a href="/docs/linux/man/1-git-rebase/">git-rebase</a></code>(1). </p>
<p> Outputs the SHA1 of every commit in <code>&lt;limit&gt;..&lt;head&gt;</code>, prefixed with <code>&#8211;</code> for commits that have an equivalent in &lt;upstream&gt;, and <code>+</code> for commits that do not.</p>
<h2>OPTIONS</h2>
<p> -v</p>
<dl>
<dt>
<dd> Show the commit subjects next to the SHA1s.</dl>
<p> &lt;upstream&gt;</p>
<dl>
<dt>
<dd> Upstream branch to search for equivalent commits. Defaults to the upstream branch of HEAD.</dl>
<p> &lt;head&gt;</p>
<dl>
<dt>
<dd> Working branch; defaults to HEAD.</dl>
<p> &lt;limit&gt;</p>
<dl>
<dt>
<dd> Do not report commits up to (and including) limit.</dl>
<h2>EXAMPLES</h2>
<h3>Patch workflows</h3>
<p> git-cherry is frequently used in patch-based workflows (see <code><a href="/docs/linux/man/7-gitworkflows/">gitworkflows</a></code>(7)) to determine if a series of patches has been applied by the upstream maintainer. In such a workflow you might create and send a topic branch like this: </p>
<dl>
<dt>
<dd>
<pre>
$ git checkout -b topic origin/master
# work and create some commits
$ git format-patch origin/master
$ git send-email ... 00*
</pre>
</dl>
<p> Later, you can see whether your changes have been applied by saying (still on <code>topic</code>): </p>
<dl>
<dt>
<dd>
<pre>
$ git fetch  # update your notion of origin/master
$ git cherry -v
</pre>
</dl>
<h3>Concrete example</h3>
<p> In a situation where topic consisted of three commits, and the maintainer applied two of them, the situation might look like: </p>
<dl>
<dt>
<dd>
$ git log&#8211; graph&#8211; oneline&#8211; decorate&#8211; boundary origin / master&#8230; topic * 7654321(origin / master) upstream tip commit[&#8230; snip some other commits&#8230;] * cccc111 cherry &#8211; pick of C *aaaa111 cherry &#8211; pick of A[&#8230; snip a lot more that has happened&#8230;] | *cccc000(topic)<br />
commit C | *bbbb000 commit B | *aaaa000 commit A | /<br />
                                                       o 1234567 branch point
</dl>
<p> In such cases, git-cherry shows a concise summary of what has yet to be applied: </p>
<dl>
<dt>
<dd>
<pre>
$ git cherry origin/master topic
- cccc000... commit C
+ bbbb000... commit B
- aaaa000... commit A
</pre>
</dl>
<p> Here, we see that the commits A and C (marked with <code>&#8211;</code>) can be dropped from your <code>topic</code> branch when you rebase it on top of <code>origin/master</code>, while the commit B (marked with <code>+</code>) still needs to be kept so that it will be sent to be applied to <code>origin/master</code>.</p>
<h3>Using a limit</h3>
<p> The optional &lt;limit&gt; is useful in cases where your topic is based on other work that is not in upstream. Expanding on the previous example, this might look like: </p>
<dl>
<dt>
<dd>
<pre><code>
$ git log-- graph-- oneline-- decorate-- boundary origin / master... topic * 7654321(origin / master) upstream tip commit[... snip some other commits...] * cccc111 cherry - pick of C *aaaa111 cherry - pick of A[... snip a lot more that has happened...] | *cccc000(topic)
commit C | *bbbb000 commit B | *aaaa000 commit A | *0000fff(base)unpublished stuff F[... snip...] | *0000aaa unpublished stuff A
    | /
              o 1234567 merge
          - base between upstream and topic
</code></pre>
</dl>
<p> By specifying <code>base</code> as the limit, you can avoid listing commits between <code>base</code> and <code>topic</code>: </p>
<dl>
<dt>
<dd>
<pre>
$ git cherry origin/master topic base
- cccc000... commit C
+ bbbb000... commit B
- aaaa000... commit A
</pre>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-git-patch-id/">git-patch-id</a></code>(1)</p>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>
