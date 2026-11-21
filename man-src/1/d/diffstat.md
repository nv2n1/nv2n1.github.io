---

title: "diffstat(1)"
name: "diffstat"
section: "1"
letter: "d"
url: "/docs/linux/man/1-diffstat/"
description: "diffstat – make histogram from diff-output"
---

<p> <code>diffstat</code> &#8211; make histogram from diff-output </p>
<h2>SYNOPSIS</h2>
<p> <code>diffstat</code><i> [options] [file-specifications]</i></p>
<h2>DESCRIPTION</h2>
<p> This program reads the output of <code>diff</code> and displays a histogram of the insertions, deletions, and modifications per-file. <code>Diffstat</code> is a program that is useful for reviewing large, complex patch files. It reads from one or more input files which contain output from <code>diff</code>, producing a histogram of the total lines changed for each file referenced. </p>
<p> If the input filename ends with &#8220;.bz2&#8221;, &#8220;.gz&#8221;, &#8220;.lzma&#8221;, &#8220;.xz&#8221;, &#8220;.z&#8221; or &#8220;.Z&#8221;, <code>diffstat</code> will read the uncompressed data via a pipe from the corresponding program. It also can infer the compression type from files piped via the standard input. </p>
<p> <code>Diffstat</code> recognizes the most popular types of output from <code>diff</code>:</p>
<dl>
<dl>
<dt>unified</dt>
<dd> preferred by the <code>patch</code> utility.</dd>
<dt>context</dt>
<dd> best for readability, but not very compact.</dd>
<dt>default</dt>
<dd> not good for much, but simple to generate.</dd></dl>
</dl>
<p> <code>Diffstat</code> detects the lines that are output by <code>diff</code> to tell which files are compared, and then counts the markers in the first column that denote the type of change (insertion, deletion or modification). These are shown in the histogram as &quot;+&quot;, &quot;-&quot; and &quot;!&quot; characters. </p>
<p> If no filename is given on the command line, <code>diffstat</code> reads the differences from the standard input.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-b</code></dt>
<dd> ignore lines matching &quot;Binary files XXX and YYY differ&quot; in the <code>diff</code></dd>
<dt><code>-c</code></dt>
<dd> prefix each line of output with &quot;#&quot;, making it a comment-line for shell scripts.</dd>
<dt><code>-C</code></dt>
<dd> add SGR color escape sequences to highlight the histogram.</dd>
<dt><code>-D</code><i> destination</i></dt>
<dd> specify a directory containing files which can be referred to as the result of applying the differences. <code>diffstat</code> will count the lines in the corresponding files (after adjusting the names by the <code>-p</code> option) to obtain the total number of lines in each file.</dd>
<dt>
</dt><dd> The remainder, after subtracting modified and deleted lines, is shown as &quot;unchanged lines&quot;.</dd>
<dt><code>-d</code></dt>
<dd> The debug prints a lot of information. It is normally compiled-in, but can be suppressed.</dd>
<dt><code>-e</code><i> file</i></dt>
<dd> redirect standard error to <i>file</i>.</dd>
<dt><code>-E</code></dt>
<dd> strip out ANSI escape sequences on each line before parsing the differences. This allows <code>diffstat</code> to be used with <code>colordiff</code>.</dd>
<dt><code>-f</code><i> format</i></dt>
<dd> specify the format of the histogram.</dd>
<dl>
<dl>
<dt>0</dt>
<dd> for concise, which shows only the value and a single histogram code for each of insert (+), delete (-) or modify (!)</dd>
<dt>1</dt>
<dd> for normal output,</dd>
<dt>2</dt>
<dd> to fill in the histogram with dots,</dd>
<dt>4</dt>
<dd> to print each value with the histogram.</dd></dl>
</dl>
<dt>
</dt><dd> Any nonzero value gives a histogram. The dots and individual values can be combined, e.g., <code>-f6</code> gives both.</dd>
<dt><code>-h</code></dt>
<dd> prints the usage message and exits.</dd>
<dt><code>-k</code></dt>
<dd> suppress the merging of filenames in the report.</dd>
<dt><code>-K</code></dt>
<dd> attempt to improve the annotation of &quot;only&quot; files by looking for a match in the resulting set of files and inferring whether the file was added or removed.</dd>
<dt>
</dt><dd> This does not currently work in combination with <code>-R</code> because <code>diffstat</code> maintains only the resulting set of files.</dd>
<dt><code>-l</code></dt>
<dd> lists only the filenames. No histogram is generated.</dd>
<dt><code>-m</code></dt>
<dd> merge insert/delete counts from each &quot;chunk&quot; of the patch file to approximate a count of the modified lines.</dd>
<dt><code>-n</code><i> number</i></dt>
<dd> specify the minimum width used for filenames. If you do not specify this, <code>diffstat</code> uses the length of the longest filename, after stripping common prefixes.</dd>
<dt><code>-N</code><i> number</i></dt>
<dd> specify the maximum width used for filenames. Names longer than this limit are truncated on the left. If you do not specify this, <code>diffstat</code> next checks the <code>-n</code> option.</dd>
<dt><code>-o</code><i> file</i></dt>
<dd> redirect standard output to <i>file</i>.</dd>
<dt><code>-p</code><i> number</i></dt>
<dd> override the logic that strips common pathnames, simulating the <code>patch</code> &quot;-p&quot; option.</dd>
<dt>
</dt><dd> If you do not give a <code>-p</code> option, <code>diffstat</code> examines the differences and strips the common prefix from the pathnames. This is not what <code>patch</code> does.</dd>
<dt><code>-q</code></dt>
<dd> suppress the &quot;0 files changed&quot; message for empty diffs.</dd>
<dt><code>-r code</code></dt>
<dd> provides optional rounding of the data shown in histogram, rather than truncating with error adjustments.</dd>
<dl>
<dl>
<dt>0</dt>
<dd> is the default. No rounding is performed, but accumulated errors are added to following columns.</dd>
<dt>1</dt>
<dd> rounds the data</dd>
<dt>2</dt>
<dd> rounds the data and adjusts the histogram to ensure that it displays something if there are any differences even if those would normally be rounded to zero.</dd></dl>
</dl>
<dt><code>-R</code></dt>
<dd> Assume patch was created with old and new files swapped.</dd>
<dt><code>-s</code></dt>
<dd> show only the summary line, e.g., number of insertions and deletions.</dd>
<dt><code>-S</code><i> source</i></dt>
<dd> this is like the <code>-D</code> option, but specifies a location where the original files (before applying differences) can be found.</dd>
<dt><code>-t</code></dt>
<dd> overrides the histogram, generates output of comma separated values for the number of changed lines found in the differences for each file: inserted, deleted and modified.</dd>
<dt>
</dt><dd> If <code>-S</code> or <code>-D</code> options are given, the number of unchanged lines precedes the number of changes.</dd>
<dt><code>-T</code></dt>
<dd> prints the numbers that the <code>-t</code> option would show, between the pathname and histogram.</dd>
<dt>
</dt><dd> The width of the number of changes is determined by the largest value (but at least 3). The width given in the <code>-w</code> option is separate from the width of these numbers.</dd>
<dt><code>-u</code></dt>
<dd> suppress the sorting of filenames in the report.</dd>
<dt><code>-v</code></dt>
<dd> show progress, e.g., if the output is redirected to a file, write progress messages to the standard error.</dd>
<dt><code>-V</code></dt>
<dd> prints the current version number and exits.</dd>
<dt><code>-w</code><i> number</i></dt>
<dd> specify the maximum width of the histogram. The histogram will never be shorter than 10 columns, just in case the filenames get too large.</dd>
<dt>
</dt><dd> The default is 80 columns, unless the output is to a terminal. In that case, the default width is the terminal&#8217;s width.</dd></dl>
<h2>ENVIRONMENT</h2>
<p> <code>Diffstat</code> runs in a POSIX environment. </p>
<p> You can override the compiled-in paths of programs used for decompressing input files by setting environment variables corresponding to their name: </p>
<dl>
<dt>
</dt><dd>
<pre>
DIFFSTAT_BZCAT_PATH
DIFFSTAT_BZIP2_PATH
DIFFSTAT_COMPRESS_PATH
DIFFSTAT_GZIP_PATH
DIFFSTAT_LZCAT_PATH
DIFFSTAT_PCAT_PATH
DIFFSTAT_UNCOMPRESS_PATH
DIFFSTAT_XZ_PATH
DIFFSTAT_ZCAT_PATH
</pre>
</dd></dl>
<p> However, <code>diffstat</code> assumes that the resulting program uses the same command-line options, e.g., &quot;-c&quot; to decompress to the standard output.</p>
<h2>FILES</h2>
<p> <code>Diffstat</code> is a single binary module, which uses no auxiliary files.</p>
<h2>BUGS</h2>
<p> <code>Diffstat</code> makes a lot of assumptions about the format of <code>diff</code>&#8216;s output. </p>
<p> There is no way to obtain a filename from the standard <code>diff</code> between two files with no options. Context diffs work, as well as unified diffs. </p>
<p> There&#8217;s no easy way to determine the degree of overlap between the &quot;before&quot; and &quot;after&quot; displays of modified lines. <code>diffstat</code> simply counts the number of inserted and deleted lines to approximate modified lines for the <code>-m</code> option.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-diff/">diff</a></code>(1), <code><a href="/docs/linux/man/1-patch/">patch</a></code>(1).</p>
<h2>AUTHOR</h2>
<p> Thomas Dickey &lt;dickey [at] invisible-island.net&gt;. </p>
