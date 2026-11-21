---
title: "cloc(1)"
name: "cloc"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cloc/"
description: "cloc – Count, and compute differences of, lines of source code and comments."
---

<h2>SYNOPSIS</h2>
<pre>
  cloc [options] &lt;FILE|DIR&gt; ...
</pre>
<h2>DESCRIPTION</h2>
<p> Count, or compute differences of, physical lines of source code in the given files (may be archives such as compressed tarballs or zip files) and/or recursively below the given directories. It is written entirely in Perl, using only modules from the standard distribution.</p>
<h2>OPTIONS</h2>
<h3>Input Options</h3>
<p> To count standard input, use the special filename <code>&#8211;</code> and either <code>&#8211;stdin-name=FILE</code> to tell cloc the name of the file being piped in, or <code>&#8211;force-lang=LANG</code> to apply the <font SIZE="-1">LANG</font> counter to all input.</p>
<dl>
<dt><code>&#8211;extract-with=CMD</code></dt>
<dd> This option is only needed if cloc is unable to figure out how to extract the contents of the input file(s) by itself. Use <font SIZE="-1">CMD</font> to extract binary archive files (e.g.: .tar.gz, .zip, .Z). Use the literal &#8216;&gt;FILE&lt;&#8216; as a stand-in for the actual file(s) to be extracted. For example, to count lines of code in the input files gcc-4.2.tar.gz perl-5.8.8.tar.gz on Unix use: </dd>
<pre>
    --extract-with='gzip -dc &gt;FILE&lt; | tar xf -
</pre>
<p> or, if you have <font SIZE="-1">GNU</font> tar: </p>
<pre>
    --extract-with='tar zxf &gt;FILE&lt;'
</pre>
<p> and on Windows, use, for example: </p>
<pre>
    --extract-with=&quot;\&quot;c:\Program Files\WinZip\WinZip32.exe\&quot; -e -o &gt;FILE&lt;
</pre>
<dt><code>&#8211;list-file=FILE</code></dt>
<dd> Take the list of file and/or directory names to process from <font SIZE="-1">FILE,</font> which has one file/directory name per line. Only exact matches are counted; relative path names will be resolved starting from the directory where cloc is invoked. See also <code>&#8211;exclude-list-file</code></dd>
<dt><code>&#8211;vcs=VCS</code></dt>
<dd> Invoke a system call to <font SIZE="-1">VCS</font> to obtain a list of files to work on. If <font SIZE="-1">VCS</font> is &#8216;git&#8217;, then will invoke &#8216;git ls-files&#8217;. If <font SIZE="-1">VCS</font> is &#8216;svn&#8217; then will invoke &#8216;svn list -R&#8217;. The primary benefit is that cloc will then skip files explicitly excluded by the versioning tool in question, ie, those in .gitignore or have the svn:ignore property. Alternatively <font SIZE="-1">VCS</font> may be any system command that generates a list of files. Note: cloc must be in a directory which can read the files as they are returned by <font SIZE="-1">VCS. </font> cloc will not download files from remote repositories. &#8216;svn list -R&#8217; may refer to a remote repository to obtain file names (and therefore may require authentication to the remote repository), but the files themselves must be local.</dd>
<dt><code>&#8211;unicode</code></dt>
<dd> Check binary files to see if they contain Unicode expanded <font SIZE="-1">ASCII</font> text. This causes performance to drop noticeably.</dd></dl>
<h3>Processing Options</h3>
<dl>
<dt><code>&#8211;autoconf</code></dt>
<dd> Count .in files (as processed by <font SIZE="-1">GNU</font> autoconf) of recognized languages.</dd>
<dt><code>&#8211;by-file</code></dt>
<dd> Report results for every source file encountered.</dd>
<dt><code>&#8211;by-file-by-lang</code></dt>
<dd> Report results for every source file encountered in addition to reporting by language.</dd>
<dt><code>&#8211;count-and-diff </code><font SIZE="-1"><code>SET1 SET2</code></font></dt>
<dd> First perform direct code counts of source file(s) of <font SIZE="-1">SET1</font> and <font SIZE="-1">SET2</font> separately, then perform a diff of these. Inputs may be pairs of files, directories, or archives. See also <code>&#8211;diff</code>, <code>&#8211;diff-alignment</code>, <code>&#8211;diff-timeout</code>, <code>&#8211;ignore-case</code>, <code>&#8211;ignore-whitespace</code>.</dd>
<dt><code>&#8211;diff </code><font SIZE="-1"><code>SET1 SET2</code></font></dt>
<dd> Compute differences in code and comments between source file(s) of <font SIZE="-1">SET1</font> and <font SIZE="-1">SET2. </font> The inputs may be pairs of files, directories, or archives. Use <code>&#8211;diff-alignment</code> to generate a list showing which file pairs where compared. See also <code>&#8211;count-and-diff</code>, <code>&#8211;diff-alignment</code>, <code>&#8211;diff-timeout</code>, <code>&#8211;ignore-case</code>, <code>&#8211;ignore-whitespace</code>.</dd>
<dt><code>&#8211;diff-timeout N</code></dt>
<dd> Ignore files which take more than N seconds to process. Default is 10 seconds. (Large files with many repeated lines can cause <i>Algorithm::Diff::sdiff()</i> to take hours.)</dd>
<dt><code>&#8211;follow-links</code></dt>
<dd> [Unix only] Follow symbolic links to directories (sym links to files are always followed).</dd>
<dt><code>&#8211;force-lang=LANG[,EXT]</code></dt>
<dd> Process all files that have a <font SIZE="-1">EXT</font> extension with the counter for language <font SIZE="-1">LANG.</font> For example, to count all .f files with the Fortran 90 counter (which expects files to end with .f90) instead of the default Fortran 77 counter, use: </dd>
<pre>
        --force-lang=&quot;Fortran 90&quot;,f
</pre>
<p> If <font SIZE="-1">EXT</font> is omitted, every file will be counted with the <font SIZE="-1">LANG</font> counter. This option can be specified multiple times (but that is only useful when <font SIZE="-1">EXT</font> is given each time). See also <code>&#8211;script-lang</code>, <code>&#8211;lang-no-ext</code>.</p>
<dt><code>&#8211;force-lang-def=FILE</code></dt>
<dd> Load language processing filters from <font SIZE="-1">FILE,</font> then use these filters instead of the built-in filters. Note: languages which map to the same file extension (for example: MATLAB/Objective C/MUMPS; Pascal/PHP; Lisp/OpenCL; Lisp/Julia; Perl/Prolog) will be ignored as these require additional processing that is not expressed in language definition files. Use <code>&#8211;read-lang-def</code> to define new language filters without replacing built-in filters (see also <code>&#8211;write-lang-def</code>).</dd>
<dt><code>&#8211;ignore-whitespace</code></dt>
<dd> Ignore horizontal white space when comparing files with <code>&#8211;diff</code>. See also <code>&#8211;ignore-case</code>.</dd>
<dt><code>&#8211;ignore-case</code></dt>
<dd> Ignore changes in case; consider upper- and lowercase letters equivalent when comparing files with <code>&#8211;diff</code>. See also <code>&#8211;ignore-whitespace</code>.</dd>
<dt><code>&#8211;lang-no-ext=LANG</code></dt>
<dd> Count files without extensions using the <font SIZE="-1">LANG</font> counter. This option overrides internal logic for files without extensions (where such files are checked against known scripting languages by examining the first line for <tt>&quot;#!&quot;</tt>). See also <code>&#8211;force-lang</code>, <code>&#8211;script-lang</code>.</dd>
<dt><code>&#8211;max-file-size=MB</code></dt>
<dd> Skip files larger than <tt>&quot;MB&quot;</tt> megabytes when traversing directories. By default, <tt>&quot;MB&quot;</tt>=100. cloc&#8217;s memory requirement is roughly twenty times larger than the largest file so running with files larger than 100 <font SIZE="-1">MB</font> on a computer with less than 2 <font SIZE="-1">GB</font> of memory will cause problems. Note: this check does not apply to files explicitly passed as command line arguments.</dd>
<dt><code>&#8211;read-binary-files</code></dt>
<dd> Process binary files in addition to text files. This is usually a bad idea and should only be attempted with text files that have embedded binary data.</dd>
<dt><code>&#8211;read-lang-def=FILE</code></dt>
<dd> Load new language processing filters from <font SIZE="-1">FILE</font> and merge them with those already known to cloc. If <font SIZE="-1">FILE</font> defines a language cloc already knows about, cloc&#8217;s definition will take precedence. Use <code>&#8211;force-lang-def</code> to over-ride cloc&#8217;s definitions. (see also <code>&#8211;write-lang-def</code>).</dd>
<dt><code>&#8211;script-lang=LANG,S</code></dt>
<dd> Process all files that invoke <tt>&quot;S&quot;</tt> as a <tt>&quot;#!&quot;</tt> scripting language with the counter for language <font SIZE="-1">LANG.</font> For example, files that begin with <tt>&quot;#!/usr/local/bin/perl5.8.8&quot;</tt> will be counted with the Perl counter by using </dd>
<pre>
        --script-lang=Perl,perl5.8.8
</pre>
<p> The language name is case insensitive but the name of the script language executable, <tt>&quot;S&quot;</tt>, must have the right case. This option can be specified multiple times. See also <code>&#8211;force-lang</code>.</p>
<dt><code>&#8211;sdir=DIR</code></dt>
<dd> Use <font SIZE="-1">DIR</font> as the scratch directory instead of letting <i>File::Temp</i> chose the location. Files written to this location are not removed at the end of the run (as they are with <i>File::Temp</i>).</dd>
<dt><code>&#8211;skip-uniqueness</code></dt>
<dd> Skip the file uniqueness check. This will give a performance boost at the expense of counting files with identical contents multiple times (if such duplicates exist).</dd>
<dt><code>&#8211;stdin-name=FILE</code></dt>
<dd> Count lines streamed via <i></i><font SIZE="-1"><i>STDIN</i></font><i></i> as if they came from a file named <font SIZE="-1">FILE.</font></dd>
<dt><code>&#8211;strip-comments=EXT</code></dt>
<dd> For each file processed, write to the current directory a version of the file which has blank lines and comments removed. The name of each stripped file is the original file name with <tt>&quot;.EXT&quot;</tt> appended to it. It is written to the current directory unless <code>&#8211;original-dir</code> is on.</dd>
<dt><code>&#8211;original-dir</code></dt>
<dd> Write the stripped files the same directory as the original files. Only effective in combination with <code>&#8211;strip-comments</code>.</dd>
<dt><code>&#8211;sum-reports</code></dt>
<dd> Input arguments are report files previously created with the <code>&#8211;report-file</code> option. Makes a cumulative set of results containing the sum of data from the individual report files.</dd>
<dt><code>&#8211;unix</code></dt>
<dd> Over-ride the operating system detection logic and run in <font SIZE="-1">UNIX</font> mode. See also <code>&#8211;windows</code>, <code>&#8211;show-os</code>.</dd>
<dt><code>&#8211;use-sloccount</code></dt>
<dd> If SLOCCount is installed, use its compiled executables c_count, java_count, pascal_count, php_count, and xml_count instead of cloc&#8217;s counters. SLOCCount&#8217;s compiled counters are substantially faster than cloc&#8217;s and may give a performance improvement when counting projects with large files. However, these cloc-specific features will not be available: <code>&#8211;diff</code>, <code>&#8211;count-and-diff</code>, <code>&#8211;strip-comments</code>, <code>&#8211;unicode</code>.</dd>
<dt><code>&#8211;windows</code></dt>
<dd> Over-ride the operating system detection logic and run in Microsoft Windows mode. See also <code>&#8211;unix</code>, <code>&#8211;show-os</code>.</dd></dl>
<h3>Filter Options</h3>
<dl>
<dt><code>&#8211;exclude-dir=DIR1[,DIR2 &#8230;]</code></dt>
<dd> Exclude the given comma separated directories from being scanned. For example: </dd>
<pre>
        --exclude-dir=.cache,test
</pre>
<p> will skip all files that match <tt>&quot;/.cache/&quot;</tt> or <tt>&quot;/test/&quot;</tt> as part of their path. Directories named <tt>&quot;.bzr&quot;</tt>, <tt>&quot;.cvs&quot;</tt>, <tt>&quot;.hg&quot;</tt>, <tt>&quot;.git&quot;</tt>, and <tt>&quot;.svn&quot;</tt> are always excluded.</p>
<dt><code>&#8211;exclude-ext=EXT1[,EXT2 &#8230;]</code></dt>
<dd> Do not count files having the given file name extensions.</dd>
<dt><code>&#8211;exclude-lang=L1[,L2 &#8230;]</code></dt>
<dd> Exclude the given comma separated languages from being counted.</dd>
<dt><code>&#8211;exclude-list-file=FILE</code> Ignore files and/or directories whose names appear in <font SIZE="-1">FILE. FILE</font> should have one file name per line. Only exact matches are ignored; relative path names will be resolved starting from the directory where cloc is invoked. See also <code>&#8211;list-file</code>.</dt>
<dd>
</dd><dt><code>&#8211;fullpath</code> Modifies the behavior of <code>&#8211;match-f</code> or <code>&#8211;not-match-f</code> to include the file&#8217;s path in the regex, not just the file&#8217;s basename. (This does not expand each file to include its absolute path, instead it uses as much of the path as is passed in to cloc.)</dt>
<dd>
</dd><dt><code>&#8211;include-lang=L1[,L2 &#8230;]</code></dt>
<dd> Count only the given comma separated languages L1, L2, L3, et cetera.</dd>
<dt><code>&#8211;match-d=REGEX</code></dt>
<dd> Only count files in directories matching the Perl regex. For example </dd>
<pre>
     --match-d='/(src|include)/'
</pre>
<p> only counts files in directory paths containing <tt>&quot;/src/&quot;</tt> or <tt>&quot;/include/&quot;</tt>.</p>
<dt><code>&#8211;not-match-d=REGEX</code></dt>
<dd> Count all files except in directories matching the Perl regex.</dd>
<dt><code>&#8211;match-f=REGEX</code></dt>
<dd> Only count files whose basenames match the Perl regex. For example this only counts files at start with Widget or widget: </dd>
<pre>
     --match-f='^[Ww]idget'
</pre>
<dt><code>&#8211;not-match-f=REGEX</code></dt>
<dd> Count all files except those whose basenames match the Perl regex.</dd>
<dt><code>&#8211;skip-archive=REGEX</code></dt>
<dd> Ignore files that end with the given Perl regular expression. For example, if given<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;skip-archive='(zip|tar(\.(gz|Z|bz2|xz|7z))?)&#8217; the code will skip files that end with .zip, .tar, .tar.gz, .tar.Z, .tar.bz2, .tar.xz, and .tar.7z.</dd>
<dt><code>&#8211;skip-win-hidden</code></dt>
<dd> On Windows, ignore hidden files.</dd></dl>
<h3>Debug Options</h3>
<dl>
<dt><code>&#8211;categorized=FILE</code></dt>
<dd> Save names of categorized files to <font SIZE="-1">FILE.</font></dd>
<dt><code>&#8211;counted=FILE</code></dt>
<dd> Save names of processed source files to <font SIZE="-1">FILE.</font></dd>
<dt><code>&#8211;diff-alignment=FILE</code></dt>
<dd> Write to <font SIZE="-1">FILE</font> a list of files and file pairs showing which files were added, removed, and/or compared during a run with <code>&#8211;diff</code>. This switch forces the <code>&#8211;diff</code> mode on.</dd>
<dt><code>&#8211;explain=LANG</code></dt>
<dd> Print the filters used to remove comments for language <font SIZE="-1">LANG</font> and exit. In some cases the filters refer to Perl subroutines rather than regular expressions. An examination of the source code may be needed for further explanation.</dd>
<dt><code>&#8211;help</code></dt>
<dd> Print this usage information and exit.</dd>
<dt><code>&#8211;found=FILE</code></dt>
<dd> Save names of every file found to <font SIZE="-1">FILE.</font></dd>
<dt><code>&#8211;ignored=FILE</code></dt>
<dd> Save names of ignored files and the reason they were ignored to <font SIZE="-1">FILE.</font></dd>
<dt><code>&#8211;print-filter-stages</code></dt>
<dd> Print to <i></i><font SIZE="-1"><i>STDOUT</i></font><i></i> processed source code before and after each filter is applied.</dd>
<dt><code>&#8211;show-ext[=EXT]</code></dt>
<dd> Print information about all known (or just the given) file extensions and exit.</dd>
<dt><code>&#8211;show-lang[=LANG]</code></dt>
<dd> Print information about all known (or just the given) languages and exit.</dd>
<dt><code>&#8211;show-os</code></dt>
<dd> Print the value of the operating system mode and exit. See also <code>&#8211;unix</code>, <code>&#8211;windows</code>.</dd>
<dt><code>-v[=N]</code></dt>
<dd> Turn on verbose with optional numeric value.</dd>
<dt><code>&#8211;verbose[=N]</code></dt>
<dd> Long form of <code>-v</code>.</dd>
<dt><code>&#8211;version</code></dt>
<dd> Print the version of this program and exit.</dd>
<dt><code>&#8211;write-lang-def=FILE</code></dt>
<dd> Writes to <font SIZE="-1">FILE</font> the language processing filters then exits. Useful as a first step to creating custom language definitions. See also <code>&#8211;force-lang-def</code>, <code>&#8211;read-lang-def</code>.</dd></dl>
<h3>Output Options</h3>
<dl>
<dt><code>&#8211;3</code></dt>
<dd> Print third-generation language output. (This option can cause report summation to fail if some reports were produced with this option while others were produced without it.)</dd>
<dt><code>&#8211;by-percent X</code></dt>
<dd> Instead of comment and blank line counts, show these values as percentages based on the value of X in the denominator: </dd>
<pre><code>
X = 'c'-&gt;#lines of code
        X = 'cm'-&gt;#lines of code + comments
                                       X = 'cb'-&gt;#lines of code + blanks
                                                                      X = 'cmb'-&gt;#lines of code + comments + blanks
</code></pre>
<p> For example, if using method &#8216;c&#8217; and your code has twice as many lines of comments as lines of code, the value in the comment column will be 200%. The code column remains a line count.</p>
<dt><code>&#8211;csv</code></dt>
<dd> Write the results as comma separated values.</dd>
<dt><code>&#8211;csv-delimiter=C</code></dt>
<dd> Use the character C as the delimiter for comma separated files instead of ,. This switch forces <code>&#8211;csv</code> to be on.</dd>
<dt><code>&#8211;json</code></dt>
<dd> Write the results in JavaScript Object Notation (<font SIZE="-1">JSON</font>).</dd>
<dt><code>&#8211;md</code></dt>
<dd> Write the results as Markdown-formatted text.</dd>
<dt><code>&#8211;out=FILE</code></dt>
<dd> Synonym for <code>&#8211;report-file=FILE</code>.</dd>
<dt><code>&#8211;progress-rate=N</code></dt>
<dd> Show progress update after every N files are processed (default N=100). Set N to 0 to suppress progress output; useful when redirecting output to <i></i><font SIZE="-1"><i>STDOUT</i></font><i></i>.</dd>
<dt><code>&#8211;quiet</code></dt>
<dd> Suppress all information messages except for the final report.</dd>
<dt><code>&#8211;report-file=FILE</code></dt>
<dd> Write the results to <font SIZE="-1">FILE</font> instead of standard output.</dd>
<dt><code>&#8211;sql=FILE</code></dt>
<dd> Write results as <font SIZE="-1">SQL CREATE</font> and <font SIZE="-1">INSERT</font> statements which can be read by a database program such as SQLite. If <font SIZE="-1">FILE</font> is <code>&#8211;</code>, output is sent to <i></i><font SIZE="-1"><i>STDOUT</i></font><i></i>.</dd>
<dt><code>&#8211;sql-append</code></dt>
<dd> Append <font SIZE="-1">SQL</font> insert statements to the file specified by <code>&#8211;sql</code> and do not generate table creation option.</dd>
<dt><code>&#8211;sql-project=NAME</code></dt>
<dd> Use &lt;name&gt; as the project identifier for the current run. Only valid with the <code>&#8211;sql</code> option.</dd>
<dt><code>&#8211;sql-style=STYLE</code></dt>
<dd> Write <font SIZE="-1">SQL</font> statements in the given style instead of the default SQLite format. Currently, the only style option is Oracle.</dd>
<dt><code>&#8211;sum-one</code></dt>
<dd> For plain text reports, show the <font SIZE="-1">SUM:</font> output line even if only one input file is processed.</dd>
<dt><code>&#8211;xml</code></dt>
<dd> Write the results in <font SIZE="-1">XML.</font></dd>
<dt><code>&#8211;xsl[=FILE]</code></dt>
<dd> Reference <font SIZE="-1">FILE</font> as an <font SIZE="-1">XSL</font> stylesheet within the <font SIZE="-1">XML</font> output. If <font SIZE="-1">FILE</font> is not given, writes a default stylesheet, cloc.xsl. This switch forces <code>&#8211;xml</code> to be on.</dd>
<dt><code>&#8211;yaml</code></dt>
<dd> Write the results in <font SIZE="-1">YAML.</font></dd></dl>
<h2>EXAMPLES</h2>
<p> Count the lines of code in the Perl 5.10.0 compressed tar file on a UNIX-like operating system: </p>
<pre>
  cloc perl-5.10.0.tar.gz
</pre>
<p> Count the changes in files, code, and comments between Python releases 2.6.6 and 2.7: </p>
<pre>
  cloc --diff Python-2.6.6.tar.bz  Python-2.7.tar.bz2
</pre>
<p> To see how cloc aligns files for comparison between two code bases, use the <code>&#8211;diff-alignment=FILE</code> option. Here the alignment information is written to <tt>&quot;align.txt&quot;</tt>: </p>
<pre>
  cloc --diff-aligment=align.txt gcc-4.4.0.tar.bz2  gcc-4.5.0.tar.bz2
</pre>
<p> Print the recognized languages </p>
<pre>
  cloc --show-lang
</pre>
<p> Remove comments from <tt>&quot;foo.c&quot;</tt> and save the result in <tt>&quot;foo.c.nc&quot;</tt> </p>
<pre>
  cloc --strip-comments=nc foo.c
</pre>
<p> Additional examples can be found at &lt;<a rel="nofollow" href="http://cloc.sourceforge.net">http://cloc.sourceforge.net</a>&gt;.</p>
<h2>ENVIRONMENT</h2>
<p> None.</p>
<h2>FILES</h2>
<p> None.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-sloccount/">sloccount</a></i>(1)</p>
<h2>AUTHORS</h2>
<p> The cloc program was written by Al Danial &lt;al.danial [at] gmail.com&gt; and is Copyright (C) 2006-2016 &lt;al.danial [at] gmail.com&gt;. </p>
<p> The manual page was originally written by Jari Aalto &lt;jari.aalto [at] cante.net&gt;. </p>
<p> Both the code and documentation is released under the <font SIZE="-1">GNU GPL</font> version 2 or (at your option) any later version. For more information about license, visit &lt;<a rel="nofollow" href="http://www.gnu.org/copyleft/gpl.html">http://www.gnu.org/copyleft/gpl.html</a>&gt;. </p>
