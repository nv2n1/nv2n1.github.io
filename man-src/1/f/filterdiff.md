---
title: "filterdiff(1)"
name: "filterdiff"
section: "1"
letter: "f"
url: "/docs/linux/man/1-filterdiff/"
description: "filterdiff – extract or exclude diffs from a diff file"
---

<h2 class="name">NAME</h2>
<p> filterdiff &#8211; extract or exclude diffs from a diff file </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>filterdiff</code> [[-i&nbsp;<i>PATTERN</i>] | [&#8211;include=<i>PATTERN</i>]] [[-I&nbsp;<i>FILE</i>] | [&#8211;include-from-file=<i>FILE</i>]] [[-p&nbsp;<i>n</i>] | [&#8211;strip-match=<i>n</i>]] [&#8211;strip=<i>n</i>] [&#8211;addprefix=<i>PREFIX</i>] [&#8211;addoldprefix=<i>PREFIX</i>] [&#8211;addnewprefix=<i>PREFIX</i>] [[-x&nbsp;<i>PATTERN</i>] | [&#8211;exclude=<i>PATTERN</i>]] [[-X&nbsp;<i>FILE</i>] | [&#8211;exclude-from-file=<i>FILE</i>]] [[-v] | [&#8211;verbose]] [&#8211;clean] [[-z] | [&#8211;decompress]] [[-#&nbsp;<i>RANGE</i>] | [&#8211;hunks=<i>RANGE</i>]] [&#8211;lines=<i>RANGE</i>] [[-F<i>RANGE</i>] | [&#8211;files=<i>RANGE</i>]] [&#8211;annotate] [&#8211;format=<i>FORMAT</i>] [&#8211;as-numbered-lines=<i>WHEN</i>] [&#8211;remove-timestamps] [<i>file</i>&#8230;]</p>
<dt> <code>filterdiff</code> {[&#8211;help] | [&#8211;version] | [&#8211;list] | [&#8211;grep &#8230;]}</dl>
<h2>DESCRIPTION</h2>
<dd>You can use filterdiff to obtain a patch that applies to files matching the shell wildcard <i>PATTERN</i> from a larger collection of patches. For example, to see the patches in patch-2.4.3.gz that apply to all files called lp.c: </p>
<dl>
<dt>
<dd>
<pre>
filterdiff -z -i '*/lp.c' patch-2.4.3.gz
</pre>
</dl>
<p> If neither <code>-i</code> nor <code>-x</code> options are given, <code>-i &#8216;*&#8217;</code> is assumed. This way <code>filterdiff</code> can be used to clean up an existing diff file, removing redundant lines from the beginning (eg. the text from the mail body) or between the chunks (eg. in CVS diffs). To extract pure patch data, use a command like this: </p>
<dl>
<dt>
<dd>
<pre>
filterdiff message-with-diff-in-the-body &gt; patch
</pre>
</dl>
<p> Note that the interpretation of the shell wildcard pattern does not count slash characters or periods as special (in other words, no flags are given to <code>fnmatch</code>). This is so that &#8220;*/basename&#8221;-type patterns can be given without limiting the number of pathname components. </p>
<p> You can use both unified and context format diffs with this program.</p>
<h2>OPTIONS</h2>
<p> <code>-i</code> <i>PATTERN</i>, <code>&#8211;include=</code><i>PATTERN</i></p>
<dl>
<dt>
<dd> Include only files matching <i>PATTERN</i>. All other lines in the input are suppressed.</dl>
<p> <code>-I</code> <i>FILE</i>, <code>&#8211;include-from-file=</code><i>FILE</i></p>
<dl>
<dt>
<dd> Include only files matching any pattern listed in <i>FILE</i>, one pattern per line. All other lines in the input are suppressed.</dl>
<p> <code>-x</code> <i>PATTERN</i>, <code>&#8211;exclude=</code><i>PATTERN</i></p>
<dl>
<dt>
<dd> Exclude files matching <i>PATTERN</i>. All other lines in the input are displayed.</dl>
<p> <code>-X</code> <i>FILE</i>, <code>&#8211;exclude-from-file=</code><i>FILE</i></p>
<dl>
<dt>
<dd> Exclude files matching any pattern listed in <i>FILE</i>, one pattern per line. All other lines in the input are displayed.</dl>
<p> <code>-p</code> <i>n</i>, <code>&#8211;strip-match=</code><i>n</i></p>
<dl>
<dt>
<dd> When matching, ignore the first <i>n</i> components of the pathname.</dl>
<p> <code>-#</code> <i>RANGE</i>, <code>&#8211;hunks</code>=<i>RANGE</i></p>
<dl>
<dt>
<dd> Only include hunks within the specified <i>RANGE</i>. Hunks are numbered from 1, and the range is a comma-separated list of numbers or &#8220;first-last&#8221; spans, optionially preceeded by a modifier &#8216;x&#8217; which inverts the entire range; either the first or the last in the span may be omitted to indicate no limit in that direction.</dl>
<p> <code>&#8211;lines</code>=<i>RANGE</i></p>
<dl>
<dt>
<dd> Only include hunks that contain lines from the original file that lie within the specified <i>RANGE</i>. Lines are numbered from 1, and the range is a comma-separated list of numbers or &#8220;first-last&#8221; spans, optionially preceeded by a modifier &#8216;x&#8217; which inverts the entire range; either the first or the last in the span may be omitted to indicate no limit in that direction.</dl>
<p> <code>-F</code>=<i>RANGE</i>, <code>&#8211;files</code>=<i>RANGE</i></p>
<dl>
<dt>
<dd> Only include files indicated by the specified <i>RANGE</i>. Files are numbered from 1 in the order they appear in the patch input, and the range is a comma-separated list of numbers or &#8220;first-last&#8221; spans, optionially preceeded by a modifier &#8216;x&#8217; which inverts the entire range; either the first or the last in the span may be omitted to indicate no limit in that direction.</dl>
<p> <code>&#8211;annotate</code></p>
<dl>
<dt>
<dd> Annotate each hunk with the filename and hunk number.</dl>
<p> <code>&#8211;format</code>=unified|context</p>
<dl>
<dt>
<dd> Use specified output format.</dl>
<p> <code>&#8211;strip</code>=<i>n</i></p>
<dl>
<dt>
<dd> Remove the first <i>n</i> components of pathnames in the output.</dl>
<p> <code>&#8211;addprefix</code>=<i>PREFIX</i></p>
<dl>
<dt>
<dd> Prefix pathnames in the output by <i>PREFIX</i>. This will override any individual settings specified with the <code>&#8211;addoldprefix</code> or <code>&#8211;addnewprefix</code> options.</dl>
<p> <code>&#8211;addoldprefix</code>=<i>PREFIX</i></p>
<dl>
<dt>
<dd> Prefix pathnames for old or original files in the output by <i>PREFIX</i>.</dl>
<p> <code>&#8211;addnewprefix</code>=<i>PREFIX</i></p>
<dl>
<dt>
<dd> Prefix pathnames for updated or new files in the output by <i>PREFIX</i>.</dl>
<p> <code>&#8211;as-numbered-lines</code>=before|after</p>
<dl>
<dt>
<dd> Instead of a patch fragment, display the lines of the selected hunks with the line number of the file before (or after) the patch is applied, followed by a TAB character and a colon, at the beginning of each line. Each hunk except the first will have a line consisting of &#8220;&#8230;&#8221; before it.</dl>
<p> <code>&#8211;remove-timestamps</code></p>
<dl>
<dt>
<dd> Do not include file timestamps in the output.</dl>
<p> <code>-v</code>, <code>&#8211;verbose</code></p>
<dl>
<dt>
<dd> Always show non-diff lines in the output. By default, non-diff lines are only shown when excluding a filename pattern.</dl>
<p> <code>&#8211;clean</code></p>
<dl>
<dt>
<dd> Always remove all non-diff lines from the output. Even when excluding a filename pattern.</dl>
<p> <code>-z</code>, <code>&#8211;decompress</code></p>
<dl>
<dt>
<dd> Decompress files with extensions .gz and .bz2.</dl>
<p> <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Display a short usage message.</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Display the version number of filterdiff.</dl>
<p> <code>&#8211;list</code></p>
<dl>
<dt>
<dd> Behave like <code><a href="/docs/linux/man/1-lsdiff/">lsdiff</a></code>(1) instead.</dl>
<p> <code>&#8211;grep</code></p>
<dl>
<dt>
<dd> Behave like <code><a href="/docs/linux/man/1-grepdiff/">grepdiff</a></code>(1) instead.</dl>
<h2>EXAMPLES</h2>
<p> To see all patch hunks that affect the first five lines of a C file: </p>
<dl>
<dt>
<dd>
<pre>
filterdiff -i '*.c' --lines=-5 &lt; patch
</pre>
</dl>
<p> To see the first hunk of each file patch, use: </p>
<dl>
<dt>
<dd>
<pre>
filterdiff -#1 patchfile
</pre>
</dl>
<p> To see patches modifying a ChangeLog file in a subdirectory, use: </p>
<dl>
<dt>
<dd>
<pre>
filterdiff -p1 Changelog
</pre>
</dl>
<p> To see the complete patches for each patch that modifies line 1 of the original file, use: </p>
<dl>
<dt>
<dd>
<pre>
filterdiff --lines=1 patchfile | lsdiff | \
  xargs -rn1 filterdiff patchfile -i
</pre>
</dl>
<p> To see all but the first hunk of a particular patch, you might use: </p>
<dl>
<dt>
<dd>
<pre>
filterdiff -p1 -i file.c -#2- foo-patch
</pre>
</dl>
<p> If you have a very specific list of hunks in a patch that you want to see, list them: </p>
<dl>
<dt>
<dd>
<pre>
filterdiff -#1,2,5-8,10,12,27-
</pre>
</dl>
<p> To see the lines of the files that would be patched as they will appear after the patch is applied, use: </p>
<dl>
<dt>
<dd>
<pre>
filterdiff --as-numbered-lines=after patch.file
</pre>
</dl>
<p> You can see the same context before the patch is applied with: </p>
<dl>
<dt>
<dd>
<pre>
filterdiff --as-numbered-lines=before
patch.file
</pre>
</dl>
<p> Filterdiff can also be used to convert between unified and context format diffs: </p>
<dl>
<dt>
<dd>
<pre>
filterdiff -v --format=unified context.diff
</pre>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-lsdiff/">lsdiff</a></code>(1), <code><a href="/docs/linux/man/1-grepdiff/">grepdiff</a></code>(1)</p>
<h2>AUTHOR</h2>
<p> <code>Tim Waugh</code> &lt;twaugh [at] redhat.com&gt;</p>
<dl>
<dt>
<dd> Package maintainer</dl>
<h2>Index</h2>
