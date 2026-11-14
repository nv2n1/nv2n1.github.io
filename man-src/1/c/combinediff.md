---
title: "combinediff(1)"
name: "combinediff"
section: "1"
letter: "c"
url: "/docs/linux/man/1-combinediff/"
description: "combinediff – create a cumulative unified patch from two incremental patches"
---

<h2 class="name">NAME</h2>
<p> combinediff &#8211; create a cumulative unified patch from two incremental patches </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>combinediff</code> [[-p&nbsp;<i>n</i>] | [&#8211;strip-match=<i>n</i>]] [[-U&nbsp;<i>n</i>] | [&#8211;unified=<i>n</i>]] [[-d&nbsp;<i>PAT</i>] | [&#8211;drop-context=<i>PAT</i>]] [[-q] | [&#8211;quiet]] [[-z] | [&#8211;decompress]] [[-b] | [&#8211;ignore-space-change]] [[-B] | [&#8211;ignore-blank-lines]] [[-i] | [&#8211;ignore-case]] [[-w] | [&#8211;ignore-all-space]] [[&#8211;interpolate] | [&#8211;combine]] <i>diff1</i> <i>diff2</i></p>
<dt> <code>combinediff</code> {[&#8211;help] | [&#8211;version]}</dl>
<h2>DESCRIPTION</h2>
<dd>combinediff creates a unified diff that expresses the sum of two diffs. The diff files must be listed in the order that they are to be applied. For best results, the diffs must have at least three lines of context. </p>
<p> Since <code>combinediff</code> doesn&#8217;t have the advantage of being able to look at the files that are to be modified, it has stricter requirements on the input format than <code><a href="/docs/linux/man/1-patch/">patch</a></code>(1) does. The output of GNU diff will be okay, even with extensions, but if you intend to use a hand-edited patch it might be wise to clean up the offsets and counts using <code><a href="/docs/linux/man/1-recountdiff/">recountdiff</a></code>(1) first. </p>
<p> Note, however, that the two patches must be in strict incremental order. In other words, the second patch must be relative to the state of the original set of files after the first patch was applied. </p>
<p> The diffs may be in context format. The output, however, will be in unified format.</p>
<h2>OPTIONS</h2>
<p> <code>-p</code> <i>n</i>, <code>&#8211;strip-match=</code><i>n</i></p>
<dl>
<dt>
<dd> When comparing filenames, ignore the first <i>n</i> pathname components from both patches. (This is similar to the <code>-p</code> option to GNU <code><a href="/docs/linux/man/1-patch/">patch</a></code>(1).)</dl>
<p> <code>-q</code>, <code>&#8211;quiet</code></p>
<dl>
<dt>
<dd> Quieter output. Don&#8217;t emit rationale lines at the beginning of each patch.</dl>
<p> <code>-U</code> <i>n</i>, <code>&#8211;unified=</code><i>n</i></p>
<dl>
<dt>
<dd> Attempt to display <i>n</i> lines of context (requires at least <i>n</i> lines of context in both input files). (This is similar to the <code>-U</code> option to GNU <code><a href="/docs/linux/man/1-diff/">diff</a></code>(1).)</dl>
<p> <code>-d</code> <i>pattern</i>, <code>&#8211;drop-context=</code><i>PATTERN</i></p>
<dl>
<dt>
<dd> Don&#8217;t display any context on files that match the shell wildcard <i>pattern</i>. This option can be given multiple times. </p>
<p> Note that the interpretation of the shell wildcard pattern does not count slash characters or periods as special (in other words, no flags are given to <code>fnmatch</code>). This is so that &#8220;*/basename&#8221;-type patterns can be given without limiting the number of pathname components.</dl>
<p> <code>-i</code>, <code>&#8211;ignore-case</code></p>
<dl>
<dt>
<dd> Consider upper- and lower-case to be the same.</dl>
<p> <code>-w</code>, <code>&#8211;ignore-all-space</code></p>
<dl>
<dt>
<dd> Ignore whitespace changes in patches.</dl>
<p> <code>-b</code>, <code>&#8211;ignore-space-change</code></p>
<dl>
<dt>
<dd> Ignore changes in the amount of whitespace.</dl>
<p> <code>-B</code>, <code>&#8211;ignore-blank-lines</code></p>
<dl>
<dt>
<dd> Ignore changes whose lines are all blank.</dl>
<p> <code>-z</code>, <code>&#8211;decompress</code></p>
<dl>
<dt>
<dd> Decompress files with extensions .gz and .bz2.</dl>
<p> <code>&#8211;interpolate</code></p>
<dl>
<dt>
<dd> Run as &#8220;interdiff&#8221;. See <code><a href="/docs/linux/man/1-interdiff/">interdiff</a></code>(1) for more information about how the behaviour is altered in this mode.</dl>
<p> <code>&#8211;combine</code></p>
<dl>
<dt>
<dd> Run as &#8220;combinediff&#8221;. This is the default.</dl>
<p> <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Display a short usage message.</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Display the version number of combinediff.</dl>
<h2>BUGS</h2>
<p> The <code>-U</code> option is a bit erratic: it can control the amount of context displayed for files that are modified in both patches, but not for files that only appear in one patch (which appear with the same amount of context in the output as in the input).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-interdiff/">interdiff</a></code>(1)</p>
<h2>AUTHOR</h2>
<p> <code>Tim Waugh</code> &lt;twaugh [at] redhat.com&gt;</p>
<dl>
<dt>
<dd> Package maintainer</dl>
<h2>Index</h2>
