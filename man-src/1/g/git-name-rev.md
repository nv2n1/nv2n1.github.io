---
title: "git-name-rev(1)"
name: "git-name-rev"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-name-rev/"
description: "git-name-rev – Find symbolic names for given revs"
---

<h2 class="name">NAME</h2>
<p> git-name-rev &#8211; Find symbolic names for given revs </p>
<h2>SYNOPSIS</h2>
<pre><code>
git name - rev[--tags][--refs = &lt;pattern&gt;](--all | --stdin | &lt;commit - ish&gt;...)
</code></pre>
<h2>DESCRIPTION</h2>
<p> Finds symbolic names suitable for human digestion for revisions given in any format parsable by <i>git rev-parse</i>.</p>
<h2>OPTIONS</h2>
<p> &#8211;tags</p>
<dl>
<dt>
<dd> Do not use branch names, but only tags to name the commits</dl>
<p> &#8211;refs=&lt;pattern&gt;</p>
<dl>
<dt>
<dd> Only use refs whose names match a given shell pattern. The pattern can be one of branch name, tag name or fully qualified ref name. If given multiple times, use refs whose names match any of the given shell patterns. Use <code>&#8211;no-refs</code> to clear any previous ref patterns given.</dl>
<p> &#8211;exclude=&lt;pattern&gt;</p>
<dl>
<dt>
<dd> Do not use any ref whose name matches a given shell pattern. The pattern can be one of branch name, tag name or fully qualified ref name. If given multiple times, a ref will be excluded when it matches any of the given patterns. When used together with &#8211;refs, a ref will be used as a match only when it matches at least one &#8211;refs pattern and does not match any &#8211;exclude patterns. Use <code>&#8211;no-exclude</code> to clear the list of exclude patterns.</dl>
<p> &#8211;all</p>
<dl>
<dt>
<dd> List all commits reachable from all refs</dl>
<p> &#8211;stdin</p>
<dl>
<dt>
<dd> Transform stdin by substituting all the 40-character SHA-1 hexes (say $hex) with &quot;$hex ($rev_name)&quot;. When used with &#8211;name-only, substitute with &quot;$rev_name&quot;, omitting $hex altogether. Intended for the scripter&#8217;s use.</dl>
<p> &#8211;name-only</p>
<dl>
<dt>
<dd> Instead of printing both the SHA-1 and the name, print only the name. If given with &#8211;tags the usual tag prefix of &quot;tags/&quot; is also omitted from the name, matching the output of <code>git-describe</code> more closely.</dl>
<p> &#8211;no-undefined</p>
<dl>
<dt>
<dd> Die with error code != 0 when a reference is undefined, instead of printing <code>undefined</code>.</dl>
<p> &#8211;always</p>
<dl>
<dt>
<dd> Show uniquely abbreviated commit object as fallback.</dl>
<h2>EXAMPLES</h2>
<p> Given a commit, find out where it is relative to the local refs. Say somebody wrote you about that fantastic commit 33db5f4d9027a10e477ccf054b2c1ab94f74c85a. Of course, you look into the commit, but that only tells you what happened, but not the context. </p>
<p> Enter <i>git name-rev</i>: </p>
<dl>
<dt>
<dd>
<pre>
% git name-rev 33db5f4d9027a10e477ccf054b2c1ab94f74c85a
33db5f4d9027a10e477ccf054b2c1ab94f74c85a tags/v0.99~940
</pre>
</dl>
<p> Now you are wiser, because you know that it happened 940 revisions before v0.99. </p>
<p> Another nice thing you can do is: </p>
<dl>
<dt>
<dd>
<pre>
% git log | git name-rev --stdin
</pre>
</dl>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>
