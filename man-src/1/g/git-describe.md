---
title: "git-describe(1)"
name: "git-describe"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-describe/"
description: "git-describe – Give an object a human readable name based on an available ref"
---

<h2 class="name">NAME</h2>
<p> git-describe &#8211; Give an object a human readable name based on an available ref </p>
<h2>SYNOPSIS</h2>
<pre><code>
git describe[--all][--tags][--contains][--abbrev = &lt;n&gt;][&lt;commit - ish&gt;...] git describe[--all][--tags][--contains][--abbrev = &lt;n&gt;]-- dirty[=&lt;mark&gt;] git describe&lt;blob&gt;
</code></pre>
<h2>DESCRIPTION</h2>
<p> The command finds the most recent tag that is reachable from a commit. If the tag points to the commit, then only the tag is shown. Otherwise, it suffixes the tag name with the number of additional commits on top of the tagged object and the abbreviated object name of the most recent commit. The result is a &quot;human-readable&quot; object name which can also be used to identify the commit to other git commands. </p>
<p> By default (without &#8211;all or &#8211;tags) <code>git describe</code> only shows annotated tags. For more information about creating annotated tags see the -a and -s options to <code><a href="/docs/linux/man/1-git-tag/">git-tag</a></code>(1). </p>
<p> If the given object refers to a blob, it will be described as <code>&lt;commit-ish&gt;:&lt;path&gt;</code>, such that the blob can be found at <code>&lt;path&gt;</code> in the <code>&lt;commit-ish&gt;</code>, which itself describes the first commit in which this blob occurs in a reverse revision walk from HEAD.</p>
<h2>OPTIONS</h2>
<p> &lt;commit-ish&gt;&#8230;</p>
<dl>
<dt>
<dd> Commit-ish object names to describe. Defaults to HEAD if omitted.</dl>
<p> &#8211;dirty[=&lt;mark&gt;], &#8211;broken[=&lt;mark&gt;]</p>
<dl>
<dt>
<dd> Describe the state of the working tree. When the working tree matches HEAD, the output is the same as &quot;git describe HEAD&quot;. If the working tree has local modification &quot;-dirty&quot; is appended to it. If a repository is corrupt and Git cannot determine if there is local modification, Git will error out, unless &#8216;&#8211;broken&#8217; is given, which appends the suffix &quot;-broken&quot; instead.</dl>
<p> &#8211;all</p>
<dl>
<dt>
<dd> Instead of using only the annotated tags, use any ref found in <code>refs/</code> namespace. This option enables matching any known branch, remote-tracking branch, or lightweight tag.</dl>
<p> &#8211;tags</p>
<dl>
<dt>
<dd> Instead of using only the annotated tags, use any tag found in <code>refs/tags</code> namespace. This option enables matching a lightweight (non-annotated) tag.</dl>
<p> &#8211;contains</p>
<dl>
<dt>
<dd> Instead of finding the tag that predates the commit, find the tag that comes after the commit, and thus contains it. Automatically implies &#8211;tags.</dl>
<p> &#8211;abbrev=&lt;n&gt;</p>
<dl>
<dt>
<dd> Instead of using the default number of hexadecimal digits (which will vary according to the number of objects in the repository with a default of 7) of the abbreviated object name, use &lt;n&gt; digits, or as many digits as needed to form a unique object name. An &lt;n&gt; of 0 will suppress long format, only showing the closest tag.</dl>
<p> &#8211;candidates=&lt;n&gt;</p>
<dl>
<dt>
<dd> Instead of considering only the 10 most recent tags as candidates to describe the input commit-ish consider up to &lt;n&gt; candidates. Increasing &lt;n&gt; above 10 will take slightly longer but may produce a more accurate result. An &lt;n&gt; of 0 will cause only exact matches to be output.</dl>
<p> &#8211;exact-match</p>
<dl>
<dt>
<dd> Only output exact matches (a tag directly references the supplied commit). This is a synonym for &#8211;candidates=0.</dl>
<p> &#8211;debug</p>
<dl>
<dt>
<dd> Verbosely display information about the searching strategy being employed to standard error. The tag name will still be printed to standard out.</dl>
<p> &#8211;long</p>
<dl>
<dt>
<dd> Always output the long format (the tag, the number of commits and the abbreviated commit name) even when it matches a tag. This is useful when you want to see parts of the commit object name in &quot;describe&quot; output, even when the commit in question happens to be a tagged version. Instead of just emitting the tag name, it will describe such a commit as v1.2-0-gdeadbee (0th commit since tag v1.2 that points at object deadbee&#8230;.).</dl>
<p> &#8211;match &lt;pattern&gt;</p>
<dl>
<dt>
<dd> Only consider tags matching the given <code><a href="/docs/linux/man/7-glob/">glob</a>(7)</code> pattern, excluding the &quot;refs/tags/&quot; prefix. If used with <code>&#8211;all</code>, it also considers local branches and remote-tracking references matching the pattern, excluding respectively &quot;refs/heads/&quot; and &quot;refs/remotes/&quot; prefix; references of other types are never considered. If given multiple times, a list of patterns will be accumulated, and tags matching any of the patterns will be considered. Use <code>&#8211;no-match</code> to clear and reset the list of patterns.</dl>
<p> &#8211;exclude &lt;pattern&gt;</p>
<dl>
<dt>
<dd> Do not consider tags matching the given <code><a href="/docs/linux/man/7-glob/">glob</a>(7)</code> pattern, excluding the &quot;refs/tags/&quot; prefix. If used with <code>&#8211;all</code>, it also does not consider local branches and remote-tracking references matching the pattern, excluding respectively &quot;refs/heads/&quot; and &quot;refs/remotes/&quot; prefix; references of other types are never considered. If given multiple times, a list of patterns will be accumulated and tags matching any of the patterns will be excluded. When combined with &#8211;match a tag will be considered when it matches at least one &#8211;match pattern and does not match any of the &#8211;exclude patterns. Use <code>&#8211;no-exclude</code> to clear and reset the list of patterns.</dl>
<p> &#8211;always</p>
<dl>
<dt>
<dd> Show uniquely abbreviated commit object as fallback.</dl>
<p> &#8211;first-parent</p>
<dl>
<dt>
<dd> Follow only the first parent commit upon seeing a merge commit. This is useful when you wish to not match tags on branches merged in the history of the target commit.</dl>
<h2>EXAMPLES</h2>
<p> With something like git.git current tree, I get: </p>
<dl>
<dt>
<dd>
<pre>
[torvalds@g5 git]$ git describe parent
v1.0.4-14-g2414721
</pre>
</dl>
<p> i.e. the current head of my &quot;parent&quot; branch is based on v1.0.4, but since it has a few commits on top of that, describe has added the number of additional commits (&quot;14&quot;) and an abbreviated object name for the commit itself (&quot;2414721&quot;) at the end. </p>
<p> The number of additional commits is the number of commits which would be displayed by &quot;git log v1.0.4..parent&quot;. The hash suffix is &quot;-g&quot; + an unambigous abbreviation for the tip commit of parent (which was <code>2414721b194453f058079d897d13c4e377f92dc6</code>). The length of the abbreviation scales as the repository grows, using the approximate number of objects in the repository and a bit of math around the birthday paradox, and defaults to a minimum of 7. The &quot;g&quot; prefix stands for &quot;git&quot; and is used to allow describing the version of a software depending on the SCM the software is managed with. This is useful in an environment where people may use different SCMs. </p>
<p> Doing a <i>git describe</i> on a tag-name will just show the tag name: </p>
<dl>
<dt>
<dd>
<pre>
[torvalds@g5 git]$ git describe v1.0.4
v1.0.4
</pre>
</dl>
<p> With &#8211;all, the command can use branch heads as references, so the output shows the reference path as well: </p>
<dl>
<dt>
<dd>
[torvalds @g5 git] $ git describe&#8211; all&#8211; abbrev = 4 v1 .0.5 ^ 2 tags / v1 .0.0 &#8211; 21 &#8211; g975b
</dl>
<dl>
<dt>
<dd>
<pre><code>
[torvalds @g5 git] $ git describe-- all-- abbrev = 4 HEAD ^
                                                   heads / lt / describe - 7 - g975b
</code></pre>
</dl>
<p> With &#8211;abbrev set to 0, the command can be used to find the closest tagname without any suffix: </p>
<dl>
<dt>
<dd>
<pre>
[torvalds@g5 git]$ git describe --abbrev=0 v1.0.5^2
tags/v1.0.0
</pre>
</dl>
<p> Note that the suffix you get if you type these commands today may be longer than what Linus saw above when he ran these commands, as your Git repository may have new commits whose object names begin with 975b that did not exist back then, and &quot;-g975b&quot; suffix alone may not be sufficient to disambiguate these commits.</p>
<h2>SEARCH STRATEGY</h2>
<p> For each commit-ish supplied, <i>git describe</i> will first look for a tag which tags exactly that commit. Annotated tags will always be preferred over lightweight tags, and tags with newer dates will always be preferred over tags with older dates. If an exact match is found, its name will be output and searching will stop. </p>
<p> If an exact match was not found, <i>git describe</i> will walk back through the commit history to locate an ancestor commit which has been tagged. The ancestor&#8217;s tag will be output along with an abbreviation of the input commit-ish&#8217;s SHA-1. If <code>&#8211;first-parent</code> was specified then the walk will only consider the first parent of each commit. </p>
<p> If multiple tags were found during the walk then the tag which has the fewest commits different from the input commit-ish will be selected and output. Here fewest commits different is defined as the number of commits which would be shown by <code>git log tag..input</code> will be the smallest number of commits possible.</p>
<h2>BUGS</h2>
<p> Tree objects as well as tag objects not pointing at commits, cannot be described. When describing blobs, the lightweight tags pointing at blobs are ignored, but the blob is still described as &lt;committ-ish&gt;:&lt;path&gt; despite the lightweight tag being favorable.</p>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>
