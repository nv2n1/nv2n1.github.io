---
title: "git-changelog(1)"
name: "git-changelog"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-changelog/"
description: "git-changelog – Generate a changelog report"
---

<h2>NAME</h2>
<p> <code>git-changelog</code> &#8211; Generate a changelog report</p>
<h2>SYNOPSIS</h2>
<p> <code>git-changelog</code> [options] [&lt;file&gt;]<br />
 <code>git-changelog</code> {-h | &#8211;help | ?}</p>
<h2>DESCRIPTION</h2>
<p> Generates a changelog from <a href="/docs/linux/man/1-git/">git</a>(1) tags (annotated or lightweight) and commit messages. Existing changelog files with filenames that begin with <i>Change</i> or <i>History</i> will be identified automatically with a case insensitive match pattern and existing content will be appended to the new output generated&#8211;this behavior can be disabled by specifying the prune option (-p|&#8211;prune-old). The generated file will be opened in <code>$EDITOR</code> when set. </p>
<p> If no tags exist, then all commits are output; if tags exist, then only the most-recent commits are output up to the last identified tag. This behavior can be changed by specifing one or both of the range options (-f|&#8211;final-tag and -s|&#8211;start-tag).</p>
<h2>OPTIONS</h2>
<p> &lt;file&gt; </p>
<p> The name of the output file. By default the new file will be <i>History.md</i> unless an existing changelog is detected in which case the existing file will be updated. </p>
<p> -a, &#8211;all </p>
<p> Retrieve all commits. Ignores -s|&#8211;start-tag and -f|&#8211;final-tag options (if set). </p>
<p> -l, &#8211;list </p>
<p> Show commits in list format (without titles, dates). </p>
<p> -t, &#8211;tag </p>
<p> Specify a tag label to use for most-recent (untagged) commits. </p>
<p> -f, &#8211;final-tag </p>
<p> When specifying a range, the newest tag at which point commit retrieval will end. Commits will be returned from the very first commit until the final tag unless a start tag is also specified. </p>
<p> -s, &#8211;start-tag </p>
<p> When specifying a range, the oldest tag to retrieve commits from. Commits will be returned from the start tag to now unless a final tag is also specified. </p>
<p> -n, &#8211;no-merges </p>
<p> Filters out merge commits (commits with more than 1 parent) from generated changelog. </p>
<p> -m, &#8211;merges-only </p>
<p> Uses only merge commits (commits with more than 1 parent) for generated changelog. It also changes the default format to include the merge commit messages body, as on github the commits subject line only contains the branch name but no information about the content of the merge. </p>
<p> -p, &#8211;prune-old </p>
<p> Replace existing changelog entirely with newly generated content, thereby disabling the default behavior of appending the content of any detected changelog to the end of newly generated content. </p>
<p> -x, &#8211;stdout </p>
<p> Write output to stdout instead of to a new changelog file. </p>
<p> -h, &#8211;help, ? </p>
<p> Show a help message with basic usage information.</p>
<h2>EXAMPLES</h2>
<dl>
<dt>Updating existing file or creating a new <i>History.md</i> file with pretty formatted output:</p>
<dd>
<dt>
<dd> $ git changelog</p>
<dt>Listing commits from the current version:</p>
<dd>
<dt>
<dd> $ git changelog &#8211;list</p>
<dt>Listing a range of commits from 2.1.0 to now:</p>
<dd>
<dt>
<dd> $ git changelog &#8211;list &#8211;start-tag 2.1.0</p>
<dt>Listing a pretty formatted version of the same:</p>
<dd>
<dt>
<dd> $ git changelog &#8211;start-tag 2.1.0</p>
<dt>Listing a range of commits from initial commit to 2.1.0:</p>
<dd>
<dt>
<dd> $ git changelog &#8211;list &#8211;final-tag 2.1.0</p>
<dt>Listing a pretty formatted range of commits between 0.5.0 and 1.0.0:</p>
<dd>
<dt>
<dd> $ git changelog &#8211;start-tag 0.5.0 &#8211;final-tag 1.0.0</p>
<dt>Specifying a file for output:</p>
<dd>
<dt>
<dd> $ git changelog ChangeLog.md</p>
<dt>And if an existing Changelog exists, replace its contents entirely:</p>
<dd>
<dt>
<dd> $ git changelog &#8211;prune-old</dl>
<h2>AUTHOR</h2>
<p> Written by Mark Eissler &lt;<i>mark [at] mixtur.com</i>&gt;</p>
<h2>REPORTING BUGS</h2>
<p> &lt;<i><a rel="nofollow" href="https://github.com/tj/git-extras/issues">https://github.com/tj/git-extras/issues</a></i>&gt;</p>
<h2>SEE ALSO</h2>
<p> &lt;<i><a rel="nofollow" href="https://github.com/tj/git-extras">https://github.com/tj/git-extras</a></i>&gt; </p>
<h2>Index</h2>
