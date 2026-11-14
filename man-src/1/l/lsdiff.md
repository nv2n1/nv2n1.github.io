---
title: "lsdiff(1)"
name: "lsdiff"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lsdiff/"
description: "lsdiff – show which files are modified by a patch"
---

<h2 class="name">NAME</h2>
<p> lsdiff &#8211; show which files are modified by a patch </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>lsdiff</code> [[-n] | [&#8211;line-number]] [[-p&nbsp;<i>n</i>] | [&#8211;strip-match=<i>n</i>]] [&#8211;strip=<i>n</i>] [&#8211;addprefix=<i>PREFIX</i>] [[-s] | [&#8211;status]] [[-E] | [&#8211;empty-files-as-removed]] [[-i&nbsp;<i>PATTERN</i>] | [&#8211;include=<i>PATTERN</i>]] [[-x&nbsp;<i>PATTERN</i>] | [&#8211;exclude=<i>PATTERN</i>]] [[-z] | [&#8211;decompress]] [[-#&nbsp;<i>RANGE</i>] | [&#8211;hunks=<i>RANGE</i>]] [&#8211;lines=<i>RANGE</i>] [[-F<i>RANGE</i>] | [&#8211;files=<i>RANGE</i>]] [[-H] | [&#8211;with-filename]] [[-h] | [&#8211;no-filename]] [[-v] | [&#8211;verbose]&#8230;] [<i>file</i>&#8230;]</p>
<dt> <code>lsdiff</code> {[&#8211;help] | [&#8211;version] | [&#8211;filter &#8230;] | [&#8211;grep &#8230;]}</dl>
<h2>DESCRIPTION</h2>
<dd>List the files modified by a patch. </p>
<p> You can use both unified and context format diffs with this program.</p>
<h2>OPTIONS</h2>
<p> <code>-n</code>, <code>&#8211;line-number</code></p>
<dl>
<dt>
<dd> Display the line number that each patch begins at. If verbose output is requested (using <code>-nv</code>), each hunk of each patch is listed as well. </p>
<p> For each file that is modified, a line is generated containing the line number of the beginning of the patch, followed by a Tab character, followed by the name of the file that is modified. If <code>-v</code> is given once, following each of these lines will be one line for each hunk, consisting of a Tab character, the line number that the hunk begins at, another Tab character, the string &#8220;Hunk #&#8221;, and the hunk number (starting at 1). </p>
<p> If the <code>-v</code> is given twice in conjunction with <code>-n</code> (i.e. <code>-nvv</code>), the format is slightly different: hunk-level descriptive text is shown after each hunk number, and the <code>&#8211;number-files</code> option is enabled.</dl>
<p> <code>-N</code>, <code>&#8211;number-files</code></p>
<dl>
<dt>
<dd> File numbers are listed, beginning at 1, before each filename.</dl>
<p> <code>-#</code> <i>RANGE</i>, <code>&#8211;hunks</code>=<i>RANGE</i></p>
<dl>
<dt>
<dd> Only list hunks within the specified <i>RANGE</i>. Hunks are numbered from 1, and the range is a comma-separated list of numbers or &#8220;first-last&#8221; spans, optionially preceeded by a modifier &#8216;x&#8217; which inverts the entire range; either the first or the last in the span may be omitted to indicate no limit in that direction.</dl>
<p> <code>&#8211;lines</code>=<i>RANGE</i></p>
<dl>
<dt>
<dd> Only list hunks that contain lines from the original file that lie within the specified <i>RANGE</i>. Lines are numbered from 1, and the range is a comma-separated list of numbers or &#8220;first-last&#8221; spans, optionially preceeded by a modifier &#8216;x&#8217; which inverts the entire range; either the first or the last in the span may be omitted to indicate no limit in that direction.</dl>
<p> <code>-F</code>=<i>RANGE</i>, <code>&#8211;files</code>=<i>RANGE</i></p>
<dl>
<dt>
<dd> Only list files indicated by the specified <i>RANGE</i>. Files are numbered from 1 in the order they appear in the patch input, and the range is a comma-separated list of numbers or &#8220;first-last&#8221; spans, optionially preceeded by a modifier &#8216;x&#8217; which inverts the entire range; either the first or the last in the span may be omitted to indicate no limit in that direction.</dl>
<p> <code>-p</code> <i>n</i>, <code>&#8211;strip-match=</code><i>n</i></p>
<dl>
<dt>
<dd> When matching, ignore the first <i>n</i> components of the pathname.</dl>
<p> <code>&#8211;strip</code>=<i>n</i></p>
<dl>
<dt>
<dd> Remove the first <i>n</i> components of the pathname before displaying it.</dl>
<p> <code>&#8211;addprefix</code>=<i>PREFIX</i></p>
<dl>
<dt>
<dd> Prefix the pathname with <i>PREFIX</i> before displaying it.</dl>
<p> <code>-s</code>, <code>&#8211;status</code></p>
<dl>
<dt>
<dd> Show file additions, modifications and removals. A file addition is indicated by a &#8220;+&#8221;, a removal by a &#8220;-&#8220;, and a modification by a &#8220;!&#8221;.</dl>
<p> <code>-E</code>, <code>&#8211;empty-files-as-removed</code></p>
<dl>
<dt>
<dd> Treat empty files as absent for the purpose of displaying file additions, modifications and removals.</dl>
<p> <code>-i</code> <i>PATTERN</i>, <code>&#8211;include=</code><i>PATTERN</i></p>
<dl>
<dt>
<dd> Include only files matching <i>PATTERN</i>.</dl>
<p> <code>-x</code> <i>PATTERN</i>, <code>&#8211;exclude=</code><i>PATTERN</i></p>
<dl>
<dt>
<dd> Exclude files matching <i>PATTERN</i>.</dl>
<p> <code>-z</code>, <code>&#8211;decompress</code></p>
<dl>
<dt>
<dd> Decompress files with extensions .gz and .bz2.</dl>
<p> <code>-H</code>, <code>&#8211;with-filename</code></p>
<dl>
<dt>
<dd> Print the name of the patch file containing each patch.</dl>
<p> <code>-h</code>, <code>&#8211;no-filename</code></p>
<dl>
<dt>
<dd> Suppress the name of the patch file containing each patch.</dl>
<p> <code>-v</code>, <code>&#8211;verbose</code></p>
<dl>
<dt>
<dd> Verbose output.</dl>
<p> <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Display a short usage message.</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Display the version number of lsdiff.</dl>
<p> <code>&#8211;filter</code></p>
<dl>
<dt>
<dd> Behave like <code><a href="/docs/linux/man/1-filterdiff/">filterdiff</a></code>(1) instead.</dl>
<p> <code>&#8211;grep</code></p>
<dl>
<dt>
<dd> Behave like <code><a href="/docs/linux/man/1-grepdiff/">grepdiff</a></code>(1) instead.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-filterdiff/">filterdiff</a></code>(1), <code><a href="/docs/linux/man/1-grepdiff/">grepdiff</a></code>(1)</p>
<h2>EXAMPLES</h2>
<p> To sort the order of touched files in a patch, you can use: </p>
<dl>
<dt>
<dd>
<pre>
lsdiff patch | sort -u | \
  xargs -rn1 filterdiff patch -i
</pre>
</dl>
<p> To show only added files in a patch: </p>
<dl>
<dt>
<dd>
<pre>
lsdiff -s patch | grep '^+' | \
  cut -c2- | xargs -rn1 filterdiff patch -i
</pre>
</dl>
<p> To show the headers of all file hunks: </p>
<dl>
<dt>
<dd>
<pre>
lsdiff -n patch | (while read n file
  do sed -ne &quot;$n,$(($n+1))p&quot; patch
done)
</pre>
</dl>
<h2>AUTHOR</h2>
<p> <code>Tim Waugh</code> &lt;twaugh [at] redhat.com&gt;</p>
<dl>
<dt>
<dd> Package maintainer</dl>
<h2>Index</h2>
