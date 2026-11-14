---
title: "grepdiff(1)"
name: "grepdiff"
section: "1"
letter: "g"
url: "/docs/linux/man/1-grepdiff/"
description: "grepdiff – show files modified by a diff containing a regex"
---

<h2 class="name">NAME</h2>
<p> grepdiff &#8211; show files modified by a diff containing a regex </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>grepdiff</code> [[-n] | [&#8211;line-number]] [[-N] | [&#8211;number-files]] [[-p&nbsp;<i>n</i>] | [&#8211;strip-match=<i>n</i>]] [&#8211;strip=<i>n</i>] [&#8211;addprefix=<i>PREFIX</i>] [&#8211;addoldprefix=<i>PREFIX</i>] [&#8211;addnewprefix=<i>PREFIX</i>] [[-s] | [&#8211;status]] [[-i&nbsp;<i>PATTERN</i>] | [&#8211;include=<i>PATTERN</i>]] [[-I&nbsp;<i>FILE</i>] | [&#8211;include-from-file=<i>FILE</i>]] [[-x&nbsp;<i>PATTERN</i>] | [&#8211;exclude=<i>PATTERN</i>]] [[-X&nbsp;<i>FILE</i>] | [&#8211;exclude-from-file=<i>FILE</i>]] [[-#&nbsp;<i>RANGE</i>] | [&#8211;hunks=<i>RANGE</i>]] [&#8211;lines=<i>RANGE</i>] [[-F<i>RANGE</i>] | [&#8211;files=<i>RANGE</i>]] [&#8211;annotate] [&#8211;as-numbered-lines=<i>WHEN</i>] [&#8211;format=<i>FORMAT</i>] [&#8211;remove-timestamps] [[-v] | [&#8211;verbose]] [[-z] | [&#8211;decompress]] [[-E] | [&#8211;extended-regexp]] [[-H] | [&#8211;with-filename]] [[-h] | [&#8211;no-filename]] [&#8211;output-matching=<i>WHAT</i>] {[<i>REGEX</i>] | [-f&nbsp;<i>FILE</i>]} [<i>file</i>&#8230;]</p>
<dt> <code>grepdiff</code> {[&#8211;help] | [&#8211;version] | [&#8211;list] | [&#8211;filter &#8230;]}</dl>
<h2>DESCRIPTION</h2>
<dd>For each file modified by a patch, if the patch hunk contains the <i>REGEX</i> then the file&#8217;s name is printed. </p>
<p> The regular expression is treated as POSIX Basic Regular Expression syntax, unless the <code>-E</code> option is given in which case POSIX Extended Regular Expression syntax is used. </p>
<p> For example, to see the patches in my.patch which contain the regular expression &#8220;pf_gfp_mask&#8221;, use: </p>
<dl>
<dt>
<dd>
<pre>
grepdiff pf_gfp_mask my.patch | \
  xargs -rn1 filterdiff my.patch -i
</pre>
</dl>
<p> You can use both unified and context format diffs with this program.</p>
<h2>OPTIONS</h2>
<p> <code>-n</code>, <code>&#8211;line-number</code></p>
<dl>
<dt>
<dd> Display the line number that each patch begins at. If verbose output is requested, each matching hunk is listed as well. </p>
<p> For a description of the output format see <code><a href="/docs/linux/man/1-lsdiff/">lsdiff</a></code>(1).</dl>
<p> <code>-N</code>, <code>&#8211;number-files</code></p>
<dl>
<dt>
<dd> File numbers are listed, beginning at 1, before each filename.</dl>
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
<dd> Prefix the pathname with <i>PREFIX</i> before displaying it. This will override any individual settings specified with the <code>&#8211;addoldprefix</code> or <code>&#8211;addnewprefix</code> options.</dl>
<p> <code>&#8211;addoldprefix</code>=<i>PREFIX</i></p>
<dl>
<dt>
<dd> Prefix pathnames for old or original files in the output by <i>PREFIX</i>.</dl>
<p> <code>&#8211;addnewprefix</code>=<i>PREFIX</i></p>
<dl>
<dt>
<dd> Prefix pathnames for updated or new files in the output by <i>PREFIX</i>.</dl>
<p> <code>-s</code></p>
<dl>
<dt>
<dd> Show file additions, modifications and removals. A file addition is indicated by a &#8220;+&#8221;, a removal by a &#8220;-&#8220;, and a modification by a &#8220;!&#8221;.</dl>
<p> <code>-i</code> <i>PATTERN</i>, <code>&#8211;include=</code><i>PATTERN</i></p>
<dl>
<dt>
<dd> Include only files matching <i>PATTERN</i>.</dl>
<p> <code>-I</code> <i>FILE</i>, <code>&#8211;include-from-file=</code><i>FILE</i></p>
<dl>
<dt>
<dd> Include only files matching any pattern listed in <i>FILE</i>, one pattern per line. All other lines in the input are suppressed.</dl>
<p> <code>-x</code> <i>PATTERN</i> <code>&#8211;exclude=</code><i>PATTERN</i></p>
<dl>
<dt>
<dd> Exclude files matching <i>PATTERN</i>.</dl>
<p> <code>-X</code> <i>FILE</i>, <code>&#8211;exclude-from-file=</code><i>FILE</i></p>
<dl>
<dt>
<dd> Exclude files matching any pattern listed in <i>FILE</i>, one pattern per line. All other lines in the input are displayed.</dl>
<p> <code>-#</code> <i>RANGE</i>, <code>&#8211;hunks</code>=<i>RANGE</i></p>
<dl>
<dt>
<dd> Only include hunks within the specified <i>RANGE</i>. Hunks are numbered from 1, and the range is a comma-separated list of numbers or &#8220;first-last&#8221; spans, optionially preceeded by a modifier &#8216;x&#8217; which inverts the entire range; either the first or the last in the span may be omitted to indicate no limit in that direction.</dl>
<p> <code>&#8211;lines</code>=<i>RANGE</i></p>
<dl>
<dt>
<dd> Only list hunks that contain lines from the original file that lie within the specified <i>RANGE</i>. Lines are numbered from 1, and the range is a comma-separated list of numbers or &#8220;first-last&#8221; spans, optionially preceeded by a modifier &#8216;x&#8217; which inverts the entire range; either the first or the last in the span may be omitted to indicate no limit in that direction.</dl>
<p> <code>-F</code>=<i>RANGE</i>, <code>&#8211;files</code>=<i>RANGE</i></p>
<dl>
<dt>
<dd> Only list files indicated by the specified <i>RANGE</i>. Files are numbered from 1 in the order they appear in the patch input, and the range is a comma-separated list of numbers or &#8220;first-last&#8221; spans, optionially preceeded by a modifier &#8216;x&#8217; which inverts the entire range; either the first or the last in the span may be omitted to indicate no limit in that direction.</dl>
<p> <code>&#8211;annotate</code></p>
<dl>
<dt>
<dd> Annotate each hunk with the filename and hunk number.</dl>
<p> <code>&#8211;as-numbered-lines</code>=before|after</p>
<dl>
<dt>
<dd> Instead of a patch fragment, display the lines of the selected hunks with the line number of the file before (or after) the patch is applied, followed by a TAB character and a colon, at the beginning of each line. Each hunk except the first will have a line consisting of &#8220;&#8230;&#8221; before it.</dl>
<p> <code>&#8211;format</code>=unified|context</p>
<dl>
<dt>
<dd> Use specified output format.</dl>
<p> <code>&#8211;remove-timestamps</code></p>
<dl>
<dt>
<dd> Do not include file timestamps in the output.</dl>
<p> <code>-z</code>, <code>&#8211;decompress</code></p>
<dl>
<dt>
<dd> Decompress files with extensions .gz and .bz2.</dl>
<p> <code>-E</code>, <code>&#8211;extended-regexp</code></p>
<dl>
<dt>
<dd> Use POSIX Extended Regular Expression syntax.</dl>
<p> <code>-H</code>, <code>&#8211;with-filename</code></p>
<dl>
<dt>
<dd> Print the name of the patch file containing each match.</dl>
<p> <code>-h</code>, <code>&#8211;no-filename</code></p>
<dl>
<dt>
<dd> Suppress the name of the patch file containing each match.</dl>
<p> <code>-f</code> <i>FILE</i>, <code>&#8211;file=</code><i>FILE</i></p>
<dl>
<dt>
<dd> Read regular expressions from <i>FILE</i>, one per line.</dl>
<p> <code>&#8211;output-matching</code>=hunk|file</p>
<dl>
<dt>
<dd> Display the matching hunk-level or file-level diffs.</dl>
<p> <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Display a short usage message.</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Display the version number of grepdiff.</dl>
<p> <code>&#8211;filter</code></p>
<dl>
<dt>
<dd> Behave like <code><a href="/docs/linux/man/1-filterdiff/">filterdiff</a></code>(1) instead.</dl>
<p> <code>&#8211;list</code></p>
<dl>
<dt>
<dd> Behave like <code><a href="/docs/linux/man/1-lsdiff/">lsdiff</a></code>(1) instead.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-filterdiff/">filterdiff</a></code>(1), <code><a href="/docs/linux/man/1-lsdiff/">lsdiff</a></code>(1)</p>
<h2>AUTHOR</h2>
<p> <code>Tim Waugh</code> &lt;twaugh [at] redhat.com&gt;</p>
<dl>
<dt>
<dd> Package maintainer</dl>
<h2>Index</h2>
