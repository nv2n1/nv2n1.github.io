---

title: "interdiff(1)"
name: "interdiff"
section: "1"
letter: "i"
url: "/docs/linux/man/1-interdiff/"
description: "interdiff – show differences between two diff files"
---

<p> interdiff &#8211; show differences between two diff files </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>interdiff</code> [[-p&nbsp;<i>n</i>] | [&#8211;strip-match=<i>n</i>]] [[-U&nbsp;<i>n</i>] | [&#8211;unified=<i>n</i>]] [[-d&nbsp;<i>PAT</i>] | [&#8211;drop-context=<i>PAT</i>]] [[-q] | [&#8211;quiet]] [[-z] | [&#8211;decompress]] [[-b] | [&#8211;ignore-space-change]] [[-B] | [&#8211;ignore-blank-lines]] [[-i] | [&#8211;ignore-case]] [[-w] | [&#8211;ignore-all-space]] [[&#8211;interpolate] | [&#8211;combine] | [&#8211;flip]] [&#8211;no-revert-omitted] <i>diff1</i> <i>diff2</i></dt>
<dt> <code>interdiff</code> {[&#8211;help] | [&#8211;version]}</dt></dl>
<h2>DESCRIPTION</h2>
<p> <code>interdiff</code></p>
<dd>creates a unified format diff that expresses the difference between two diffs. The diffs must both be relative to the same files. For best results, the diffs must have at least three lines of context. </dd>
<p> To reverse a patch, use /dev/null for <i>diff2</i>. </p>
<p> To reduce the amount of context in a patch, use: </p>
<dl>
<dt>
</dt><dd>
<pre>
interdiff -U1 /dev/null patchfile
</pre>
</dd></dl>
<p> Since <code>interdiff</code> doesn&#8217;t have the advantage of being able to look at the files that are to be modified, it has stricter requirements on the input format than <code><a href="/docs/linux/man/1-patch/">patch</a></code>(1) does. The output of GNU diff will be okay, even with extensions, but if you intend to use a hand-edited patch it might be wise to clean up the offsets and counts using <code><a href="/docs/linux/man/1-recountdiff/">recountdiff</a></code>(1) first. </p>
<p> Note, however, that the two patches must both be relative to the versions of the same original set of files. </p>
<p> The diffs may be in context format. The output, however, will be in unified format.</p>
<h2>OPTIONS</h2>
<p> <code>-h</code></p>
<dl>
<dt>
</dt><dd> Ignored, for compatibility with older versions of interdiff. This option will go away soon.</dd></dl>
<p> <code>-p</code> <i>n</i>, <code>&#8211;strip-match=</code><i>n</i></p>
<dl>
<dt>
</dt><dd> When comparing filenames, ignore the first <i>n</i> pathname components from both patches. (This is similar to the <code>-p</code> option to GNU <code><a href="/docs/linux/man/1-patch/">patch</a></code>(1).)</dd></dl>
<p> <code>-q</code>, <code>&#8211;quiet</code></p>
<dl>
<dt>
</dt><dd> Quieter output. Don&#8217;t emit rationale lines at the beginning of each patch.</dd></dl>
<p> <code>-U</code> <i>n</i>, <code>&#8211;unified=</code><i>n</i></p>
<dl>
<dt>
</dt><dd> Attempt to display <i>n</i> lines of context (requires at least <i>n</i> lines of context in both input files). (This is similar to the <code>-U</code> option to GNU <code><a href="/docs/linux/man/1-diff/">diff</a></code>(1).)</dd></dl>
<p> <code>-d</code> <i>PATTERN</i>, <code>&#8211;drop-context=</code><i>PATTERN</i></p>
<dl>
<dt>
</dt><dd> Don&#8217;t display any context on files that match the shell wildcard <i>PATTERN</i>. This option can be given multiple times. </dd>
<p> Note that the interpretation of the shell wildcard pattern does not count slash characters or periods as special (in other words, no flags are given to <code>fnmatch</code>). This is so that &#8220;*/basename&#8221;-type patterns can be given without limiting the number of pathname components.</dl>
<p> <code>-i</code>, <code>&#8211;ignore-case</code></p>
<dl>
<dt>
</dt><dd> Consider upper- and lower-case to be the same.</dd></dl>
<p> <code>-w</code>, <code>&#8211;ignore-all-space</code></p>
<dl>
<dt>
</dt><dd> Ignore whitespace changes in patches.</dd></dl>
<p> <code>-b</code>, <code>&#8211;ignore-space-change</code></p>
<dl>
<dt>
</dt><dd> Ignore changes in the amount of whitespace.</dd></dl>
<p> <code>-B</code>, <code>&#8211;ignore-blank-lines</code></p>
<dl>
<dt>
</dt><dd> Ignore changes whose lines are all blank.</dd></dl>
<p> <code>-z</code>, <code>&#8211;decompress</code></p>
<dl>
<dt>
</dt><dd> Decompress files with extensions .gz and .bz2.</dd></dl>
<p> <code>&#8211;interpolate</code></p>
<dl>
<dt>
</dt><dd> Run as &#8220;interdiff&#8221;. This is the default.</dd></dl>
<p> <code>&#8211;combine</code></p>
<dl>
<dt>
</dt><dd> Run as &#8220;combinediff&#8221;. See <code><a href="/docs/linux/man/1-combinediff/">combinediff</a></code>(1) for more information about how the behaviour is altered in this mode.</dd></dl>
<p> <code>&#8211;no-revert-omitted</code></p>
<dl>
<dt>
</dt><dd> (For interpolation mode only) When a file is changed by the first patch but not by the second, don&#8217;t revert that change.</dd></dl>
<p> <code>&#8211;help</code></p>
<dl>
<dt>
</dt><dd> Display a short usage message.</dd></dl>
<p> <code>&#8211;version</code></p>
<dl>
<dt>
</dt><dd> Display the version number of interdiff.</dd></dl>
<h2>EXAMPLES</h2>
<p> Basic usage: </p>
<dl>
<dt>
</dt><dd>
<pre>
interdiff -z 3.2pre1.patch.gz 3.2pre2.patch.gz
</pre>
</dd></dl>
<p> Reversing a patch: </p>
<dl>
<dt>
</dt><dd>
<pre>
interdiff patch /dev/null
</pre>
</dd></dl>
<p> Reversing part of a patch (and ignoring the rest): </p>
<dl>
<dt>
</dt><dd>
<pre>
filterdiff -i file.c patchfile | \
  interdiff /dev/stdin /dev/null
</pre>
</dd></dl>
<h2>BUGS</h2>
<p> There are currently no known bugs in interdiff; but there are some caveats. If you find a bug, please report it (along with a minimal test case) to Tim Waugh &lt;twaugh [at] redhat.com&gt;. </p>
<p> There are some sets of patches in which there is just not enough information to produce a proper interdiff. In this case, the strategy employed is to revert the original patch and apply the new patch. This, unfortunately, means that interdiffs are not guaranteed to be reversible.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-combinediff/">combinediff</a></code>(1)</p>
<h2>AUTHORS</h2>
<p> <code>Tim Waugh</code> &lt;twaugh [at] redhat.com&gt;</p>
<dl>
<dt>
</dt><dd> Package maintainer</dd></dl>
<p> <code>Michael K. Johnson</code> &lt;johnsonm [at] redhat.com&gt;</p>
<dl>
<dt>
</dt><dd> Original man page contributor</dd></dl>
