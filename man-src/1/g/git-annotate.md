---
title: "git-annotate(1)"
name: "git-annotate"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-annotate/"
description: "git-annotate – Annotate file lines with commit information"
---

<h2 class="name">NAME</h2>
<p> git-annotate &#8211; Annotate file lines with commit information </p>
<h2>SYNOPSIS</h2>
<pre><code>
git annotate[&lt;options&gt;]&lt;file&gt;[&lt;revision&gt;]
</code></pre>
<h2>DESCRIPTION</h2>
<p> Annotates each line in the given file with information from the commit which introduced the line. Optionally annotates from a given revision. </p>
<p> The only difference between this command and <code><a href="/docs/linux/man/1-git-blame/">git-blame</a></code>(1) is that they use slightly different output formats, and this command exists only for backward compatibility to support existing scripts, and provide a more familiar command name for people coming from other SCM systems.</p>
<h2>OPTIONS</h2>
<p> -b</p>
<dl>
<dt>
<dd> Show blank SHA-1 for boundary commits. This can also be controlled via the <code>blame.blankBoundary</code> config option.</dl>
<p> &#8211;root</p>
<dl>
<dt>
<dd> Do not treat root commits as boundaries. This can also be controlled via the <code>blame.showRoot</code> config option.</dl>
<p> &#8211;show-stats</p>
<dl>
<dt>
<dd> Include additional statistics at the end of blame output.</dl>
<p> -L &lt;start&gt;,&lt;end&gt;, -L :&lt;funcname&gt;</p>
<dl>
<dt>
<dd> Annotate only the line range given by <i>&lt;start&gt;,&lt;end&gt;</i>, or by the function name regex <i>&lt;funcname&gt;</i>. May be specified multiple times. Overlapping ranges are allowed. </p>
<p> <i>&lt;start&gt;</i> and <i>&lt;end&gt;</i> are optional. <code>-L &lt;start&gt;</code> or <code>-L &lt;start&gt;,</code> spans from <i>&lt;start&gt;</i> to end of file. <code>-L ,&lt;end&gt;</code> spans from start of file to <i>&lt;end&gt;</i>. </p>
<p> <i>&lt;start&gt;</i> and <i>&lt;end&gt;</i> can take one of these forms: </p>
<dl>
<dt>
<dd> &bull; number </p>
<p> If <i>&lt;start&gt;</i> or <i>&lt;end&gt;</i> is a number, it specifies an absolute line number (lines count from 1).</dl>
<dl>
<dt>
<dd> &bull; <code>/regex/</code> </p>
<p> This form will use the first line matching the given POSIX regex. If <i>&lt;start&gt;</i> is a regex, it will search from the end of the previous <code>-L</code> range, if any, otherwise from the start of file. If <i>&lt;start&gt;</i> is <code>^/regex/</code>, it will search from the start of file. If <i>&lt;end&gt;</i> is a regex, it will search starting at the line given by <i>&lt;start&gt;</i>.</dl>
<dl>
<dt>
<dd> &bull; +offset or -offset </p>
<p> This is only valid for <i>&lt;end&gt;</i> and will specify a number of lines before or after the line given by <i>&lt;start&gt;</i>.</dl>
<p> If <code>:&lt;funcname&gt;</code> is given in place of <i>&lt;start&gt;</i> and <i>&lt;end&gt;</i>, it is a regular expression that denotes the range from the first funcname line that matches <i>&lt;funcname&gt;</i>, up to the next funcname line. <code>:&lt;funcname&gt;</code> searches from the end of the previous <code>-L</code> range, if any, otherwise from the start of file. <code>^:&lt;funcname&gt;</code> searches from the start of file. The function names are determined in the same way as <code>git diff</code> works out patch hunk headers (see <i>Defining a custom hunk-header</i> in <code><a href="/docs/linux/man/5-gitattributes/">gitattributes</a></code>(5)).</dl>
<p> -l</p>
<dl>
<dt>
<dd> Show long rev (Default: off).</dl>
<p> -t</p>
<dl>
<dt>
<dd> Show raw timestamp (Default: off).</dl>
<p> -S &lt;revs-file&gt;</p>
<dl>
<dt>
<dd> Use revisions from revs-file instead of calling <code><a href="/docs/linux/man/1-git-rev-list/">git-rev-list</a></code>(1).</dl>
<p> &#8211;reverse &lt;rev&gt;..&lt;rev&gt;</p>
<dl>
<dt>
<dd> Walk history forward instead of backward. Instead of showing the revision in which a line appeared, this shows the last revision in which a line has existed. This requires a range of revision like START..END where the path to blame exists in START. <code>git blame &#8211;reverse START</code> is taken as <code>git blame &#8211;reverse START..HEAD</code> for convenience.</dl>
<p> &#8211;first-parent</p>
<dl>
<dt>
<dd> Follow only the first parent commit upon seeing a merge commit. This option can be used to determine when a line was introduced to a particular integration branch, rather than when it was introduced to the history overall.</dl>
<p> -p, &#8211;porcelain</p>
<dl>
<dt>
<dd> Show in a format designed for machine consumption.</dl>
<p> &#8211;line-porcelain</p>
<dl>
<dt>
<dd> Show the porcelain format, but output commit information for each line, not just the first time a commit is referenced. Implies &#8211;porcelain.</dl>
<p> &#8211;incremental</p>
<dl>
<dt>
<dd> Show the result incrementally in a format designed for machine consumption.</dl>
<p> &#8211;encoding=&lt;encoding&gt;</p>
<dl>
<dt>
<dd> Specifies the encoding used to output author names and commit summaries. Setting it to <code>none</code> makes blame output unconverted data. For more information see the discussion about encoding in the <code><a href="/docs/linux/man/1-git-log/">git-log</a></code>(1) manual page.</dl>
<p> &#8211;contents &lt;file&gt;</p>
<dl>
<dt>
<dd> When &lt;rev&gt; is not specified, the command annotates the changes starting backwards from the working tree copy. This flag makes the command pretend as if the working tree copy has the contents of the named file (specify <code>&#8211;</code> to make the command read from the standard input).</dl>
<p> &#8211;date &lt;format&gt;</p>
<dl>
<dt>
<dd> Specifies the format used to output dates. If &#8211;date is not provided, the value of the blame.date config variable is used. If the blame.date config variable is also not set, the iso format is used. For supported values, see the discussion of the &#8211;date option at <code><a href="/docs/linux/man/1-git-log/">git-log</a></code>(1).</dl>
<p> &#8211;[no-]progress</p>
<dl>
<dt>
<dd> Progress status is reported on the standard error stream by default when it is attached to a terminal. This flag enables progress reporting even if not attached to a terminal. Can&#8217;t use <code>&#8211;progress</code> together with <code>&#8211;porcelain</code> or <code>&#8211;incremental</code>.</dl>
<p> -M[&lt;num&gt;]</p>
<dl>
<dt>
<dd> Detect moved or copied lines within a file. When a commit moves or copies a block of lines (e.g. the original file has A and then B, and the commit changes it to B and then A), the traditional <i>blame</i> algorithm notices only half of the movement and typically blames the lines that were moved up (i.e. B) to the parent and assigns blame to the lines that were moved down (i.e. A) to the child commit. With this option, both groups of lines are blamed on the parent by running extra passes of inspection. </p>
<p> &lt;num&gt; is optional but it is the lower bound on the number of alphanumeric characters that Git must detect as moving/copying within a file for it to associate those lines with the parent commit. The default value is 20.</dl>
<p> -C[&lt;num&gt;]</p>
<dl>
<dt>
<dd> In addition to <code>-M</code>, detect lines moved or copied from other files that were modified in the same commit. This is useful when you reorganize your program and move code around across files. When this option is given twice, the command additionally looks for copies from other files in the commit that creates the file. When this option is given three times, the command additionally looks for copies from other files in any commit. </p>
<p> &lt;num&gt; is optional but it is the lower bound on the number of alphanumeric characters that Git must detect as moving/copying between files for it to associate those lines with the parent commit. And the default value is 40. If there are more than one <code>-C</code> options given, the &lt;num&gt; argument of the last <code>-C</code> will take effect.</dl>
<p> &#8211;ignore-rev &lt;rev&gt;</p>
<dl>
<dt>
<dd> Ignore changes made by the revision when assigning blame, as if the change never happened. Lines that were changed or added by an ignored commit will be blamed on the previous commit that changed that line or nearby lines. This option may be specified multiple times to ignore more than one revision. If the <code>blame.markIgnoredLines</code> config option is set, then lines that were changed by an ignored commit and attributed to another commit will be marked with a <code>?</code> in the blame output. If the <code>blame.markUnblamableLines</code> config option is set, then those lines touched by an ignored commit that we could not attribute to another revision are marked with a <i>*</i>.</dl>
<p> &#8211;ignore-revs-file &lt;file&gt;</p>
<dl>
<dt>
<dd> Ignore revisions listed in <code>file</code>, which must be in the same format as an <code>fsck.skipList</code>. This option may be repeated, and these files will be processed after any files specified with the <code>blame.ignoreRevsFile</code> config option. An empty file name, <code>&quot;&quot;</code>, will clear the list of revs from previously processed files.</dl>
<p> &#8211;color-lines</p>
<dl>
<dt>
<dd> Color line annotations in the default format differently if they come from the same commit as the preceding line. This makes it easier to distinguish code blocks introduced by different commits. The color defaults to cyan and can be adjusted using the <code>color.blame.repeatedLines</code> config option.</dl>
<p> &#8211;color-by-age</p>
<dl>
<dt>
<dd> Color line annotations depending on the age of the line in the default format. The <code>color.blame.highlightRecent</code> config option controls what color is used for each range of age.</dl>
<p> -h</p>
<dl>
<dt>
<dd> Show help message.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-git-blame/">git-blame</a></code>(1)</p>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>
