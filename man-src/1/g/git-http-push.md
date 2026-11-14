---
title: "git-http-push(1)"
name: "git-http-push"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-http-push/"
description: "git-http-push – Push objects over HTTP/DAV to another repository"
---

<h2 class="name">NAME</h2>
<p> git-http-push &#8211; Push objects over HTTP/DAV to another repository </p>
<h2>SYNOPSIS</h2>
<pre><code>
git http - push[--all][--dry - run][--force][--verbose]&lt;url&gt;&lt;ref&gt;[&lt;ref&gt;...]
</code></pre>
<h2>DESCRIPTION</h2>
<p> Sends missing objects to remote repository, and updates the remote branch. </p>
<p> <code>NOTE</code>: This command is temporarily disabled if your libcurl is older than 7.16, as the combination has been reported not to work and sometimes corrupts repository.</p>
<h2>OPTIONS</h2>
<p> &#8211;all</p>
<dl>
<dt>
<dd> Do not assume that the remote repository is complete in its current state, and verify all objects in the entire local ref&#8217;s history exist in the remote repository.</dl>
<p> &#8211;force</p>
<dl>
<dt>
<dd> Usually, the command refuses to update a remote ref that is not an ancestor of the local ref used to overwrite it. This flag disables the check. What this means is that the remote repository can lose commits; use it with care.</dl>
<p> &#8211;dry-run</p>
<dl>
<dt>
<dd> Do everything except actually send the updates.</dl>
<p> &#8211;verbose</p>
<dl>
<dt>
<dd> Report the list of objects being walked locally and the list of objects successfully sent to the remote repository.</dl>
<p> -d, -D</p>
<dl>
<dt>
<dd> Remove &lt;ref&gt; from remote repository. The specified branch cannot be the remote HEAD. If -d is specified the following other conditions must also be met: </p>
<dl>
<dt>
<dd> &bull; Remote HEAD must resolve to an object that exists locally</dl>
<dl>
<dt>
<dd> &bull; Specified branch resolves to an object that exists locally</dl>
<dl>
<dt>
<dd> &bull; Specified branch is an ancestor of the remote HEAD</dl>
</dl>
<p> &lt;ref&gt;&#8230;</p>
<dl>
<dt>
<dd> The remote refs to update.</dl>
<h2>SPECIFYING THE REFS</h2>
<p> A <i>&lt;ref&gt;</i> specification can be either a single pattern, or a pair of such patterns separated by a colon &quot;:&quot; (this means that a ref name cannot have a colon in it). A single pattern <i>&lt;name&gt;</i> is just a shorthand for <i>&lt;name&gt;:&lt;name&gt;</i>. </p>
<p> Each pattern pair consists of the source side (before the colon) and the destination side (after the colon). The ref to be pushed is determined by finding a match that matches the source side, and where it is pushed is determined by using the destination side. </p>
<dl>
<dt>
<dd> &bull; It is an error if &lt;src&gt; does not match exactly one of the local refs.</dl>
<dl>
<dt>
<dd> &bull; If &lt;dst&gt; does not match any remote ref, either </p>
<dl>
<dt>
<dd> &bull; it has to start with &quot;refs/&quot;; &lt;dst&gt; is used as the destination literally in this case.</dl>
<dl>
<dt>
<dd> &bull; &lt;src&gt; == &lt;dst&gt; and the ref that matched the &lt;src&gt; must not exist in the set of remote refs; the ref matched &lt;src&gt; locally is used as the name of the destination.</dl>
</dl>
<p> Without &#8216;&#8211;force`, the &lt;src&gt; ref is stored at the remote only if &lt;dst&gt; does not exist, or &lt;dst&gt; is a proper subset (i.e. an ancestor) of &lt;src&gt;. This check, known as &quot;fast-forward check&quot;, is performed in order to avoid accidentally overwriting the remote ref and lose other peoples&#8217; commits from there. </p>
<p> With <code>&#8211;force</code>, the fast-forward check is disabled for all refs. </p>
<p> Optionally, a &lt;ref&gt; parameter can be prefixed with a plus <i>+</i> sign to disable the fast-forward check only on that ref.</p>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>
