---
title: "perltidy(1)"
name: "perltidy"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perltidy/"
description: "perltidy – a perl script indenter and reformatter"
---

<h2 class="name">NAME</h2>
<p> perltidy &#8211; a perl script indenter and reformatter </p>
<h2>SYNOPSIS</h2>
<pre><code>
perltidy[options] file1 file2 file3...(output goes to file1.tdy, file2.tdy, file3.tdy, ...)
            perltidy[options] file1
        - o outfile perltidy[options] file1 - st
    &gt; outfile
    perltidy[options]&lt;infile&gt; outfile
</code></pre>
<h2>DESCRIPTION</h2>
<p> Perltidy reads a perl script and writes an indented, reformatted script. </p>
<p> Many users will find enough information in &#8220;<font SIZE="-1">EXAMPLES&#8221;</font> to get started. New users may benefit from the short tutorial which can be found at <a rel="nofollow" href="http://perltidy.sourceforge.net/tutorial.html">http://perltidy.sourceforge.net/tutorial.html</a> </p>
<p> A convenient aid to systematically defining a set of style parameters can be found at <a rel="nofollow" href="http://perltidy.sourceforge.net/stylekey.html">http://perltidy.sourceforge.net/stylekey.html</a> </p>
<p> Perltidy can produce output on either of two modes, depending on the existence of an <code>-html</code> flag. Without this flag, the output is passed through a formatter. The default formatting tries to follow the recommendations in <i><a href="/docs/linux/man/1-perlstyle/">perlstyle</a></i>(1), but it can be controlled in detail with numerous input parameters, which are described in &#8220;<font SIZE="-1">FORMATTING OPTIONS&#8221;</font>. </p>
<p> When the <code>-html</code> flag is given, the output is passed through an <font SIZE="-1">HTML</font> formatter which is described in &#8220;<font SIZE="-1">HTML OPTIONS&#8221;</font>.</p>
<h2>EXAMPLES</h2>
<pre>
  perltidy somefile.pl
</pre>
<p> This will produce a file <i>somefile.pl.tdy</i> containing the script reformatted using the default options, which approximate the style suggested in <i><a href="/docs/linux/man/1-perlstyle/">perlstyle</a></i>(1). The source file <i>somefile.pl</i> is unchanged. </p>
<pre>
  perltidy *.pl
</pre>
<p> Execute perltidy on all <i>.pl</i> files in the current directory with the default options. The output will be in files with an appended <i>.tdy</i> extension. For any file with an error, there will be a file with extension <i>.ERR</i>. </p>
<pre>
  perltidy -b file1.pl file2.pl
</pre>
<p> Modify <i>file1.pl</i> and <i>file2.pl</i> in place, and backup the originals to <i>file1.pl.bak</i> and <i>file2.pl.bak</i>. If <i>file1.pl.bak</i> and/or <i>file2.pl.bak</i> already exist, they will be overwritten. </p>
<pre>
  perltidy -b -bext='/' file1.pl file2.pl
</pre>
<p> Same as the previous example except that the backup files <i>file1.pl.bak</i> and <i>file2.pl.bak</i> will be deleted if there are no errors. </p>
<pre>
  perltidy -gnu somefile.pl
</pre>
<p> Execute perltidy on file <i>somefile.pl</i> with a style which approximates the <font SIZE="-1">GNU</font> Coding Standards for C programs. The output will be <i>somefile.pl.tdy</i>. </p>
<pre>
  perltidy -i=3 somefile.pl
</pre>
<p> Execute perltidy on file <i>somefile.pl</i>, with 3 columns for each level of indentation (<code>-i=3</code>) instead of the default 4 columns. There will not be any tabs in the reformatted script, except for any which already exist in comments, pod documents, quotes, and here documents. Output will be <i>somefile.pl.tdy</i>. </p>
<pre>
  perltidy -i=3 -et=8 somefile.pl
</pre>
<p> Same as the previous example, except that leading whitespace will be entabbed with one tab character per 8 spaces. </p>
<pre>
  perltidy -ce -l=72 somefile.pl
</pre>
<p> Execute perltidy on file <i>somefile.pl</i> with all defaults except use &#8220;cuddled elses&#8221; (<code>-ce</code>) and a maximum line length of 72 columns (<code>-l=72</code>) instead of the default 80 columns. </p>
<pre>
  perltidy -g somefile.pl
</pre>
<p> Execute perltidy on file <i>somefile.pl</i> and save a log file <i>somefile.pl.LOG</i> which shows the nesting of braces, parentheses, and square brackets at the start of every line. </p>
<pre>
  perltidy -html somefile.pl
</pre>
<p> This will produce a file <i>somefile.pl.html</i> containing the script with html markup. The output file will contain an embedded style sheet in the &lt;<font SIZE="-1">HEAD</font>&gt; section which may be edited to change the appearance. </p>
<pre>
  perltidy -html -css=mystyle.css somefile.pl
</pre>
<p> This will produce a file <i>somefile.pl.html</i> containing the script with html markup. This output file will contain a link to a separate style sheet file <i>mystyle.css</i>. If the file <i>mystyle.css</i> does not exist, it will be created. If it exists, it will not be overwritten. </p>
<pre>
  perltidy -html -pre somefile.pl
</pre>
<p> Write an html snippet with only the <font SIZE="-1">PRE</font> section to <i>somefile.pl.html</i>. This is useful when code snippets are being formatted for inclusion in a larger web page. No style sheet will be written in this case. </p>
<pre>
  perltidy -html -ss &gt;mystyle.css
</pre>
<p> Write a style sheet to <i>mystyle.css</i> and exit. </p>
<pre>
  perltidy -html -frm mymodule.pm
</pre>
<p> Write html with a frame holding a table of contents and the source code. The output files will be <i>mymodule.pm.html</i> (the frame), <i>mymodule.pm.toc.html</i> (the table of contents), and <i>mymodule.pm.src.html</i> (the source code).</p>
<h2>OPTIONS &#8211; OVERVIEW</h2>
<p> The entire command line is scanned for options, and they are processed before any files are processed. As a result, it does not matter whether flags are before or after any filenames. However, the relative order of parameters is important, with later parameters overriding the values of earlier parameters. </p>
<p> For each parameter, there is a long name and a short name. The short names are convenient for keyboard input, while the long names are self-documenting and therefore useful in scripts. It is customary to use two leading dashes for long names, but one may be used. </p>
<p> Most parameters which serve as on/off flags can be negated with a leading &#8220;n&#8221; (for the short name) or a leading &#8220;no&#8221; or &#8220;no-&#8221; (for the long name). For example, the flag to outdent long quotes is is <code>-olq</code> or <code>&#8211;outdent-long-quotes</code>. The flag to skip this is <code>-nolq</code> or <code>&#8211;nooutdent-long-quotes</code> or <code>&#8211;no-outdent-long-quotes</code>. </p>
<p> Options may not be bundled together. In other words, options <code>-q</code> and <code>-g</code> may <font SIZE="-1">NOT</font> be entered as <code>-qg</code>. </p>
<p> Option names may be terminated early as long as they are uniquely identified. For example, instead of <code>&#8211;dump-token-types</code>, it would be sufficient to enter <code>&#8211;dump-tok</code>, or even <code>&#8211;dump-t</code>, to uniquely identify this command.</p>
<h3>I/O control</h3>
<p> The following parameters concern the files which are read and written.</p>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Show summary of usage and exit.</p>
<dt><code>-o</code>=filename, <code>&#8211;outfile</code>=filename</p>
<dd> Name of the output file (only if a single input file is being processed). If no output file is specified, and output is not redirected to the standard output, the output will go to <i>filename.tdy</i>.</p>
<dt><code>-st</code>, <code>&#8211;standard-output</code></p>
<dd> Perltidy must be able to operate on an arbitrarily large number of files in a single run, with each output being directed to a different output file. Obviously this would conflict with outputting to the single standard output device, so a special flag, <code>-st</code>, is required to request outputting to the standard output. For example, </p>
<pre>
  perltidy somefile.pl -st &gt;somefile.new.pl
</pre>
<p> This option may only be used if there is just a single input file. The default is <code>-nst</code> or <code>&#8211;nostandard-output</code>.</p>
<dt><code>-se</code>, <code>&#8211;standard-error-output</code></p>
<dd> If perltidy detects an error when processing file <i>somefile.pl</i>, its default behavior is to write error messages to file <i>somefile.pl.ERR</i>. Use <code>-se</code> to cause all error messages to be sent to the standard error output stream instead. This directive may be negated with <code>-nse</code>. Thus, you may place <code>-se</code> in a <i>.perltidyrc</i> and override it when desired with <code>-nse</code> on the command line.</p>
<dt><code>-oext</code>=ext, <code>&#8211;output-file-extension</code>=ext</p>
<dd> Change the extension of the output file to be <i>ext</i> instead of the default <i>tdy</i> (or <i>html</i> in case the &#8211;<code>-html</code> option is used). See &#8220;Specifying File Extensions&#8221;.</p>
<dt><code>-opath</code>=path, <code>&#8211;output-path</code>=path</p>
<dd> When perltidy creates a filename for an output file, by default it merely appends an extension to the path and basename of the input file. This parameter causes the path to be changed to <i>path</i> instead. </p>
<p> The path should end in a valid path separator character, but perltidy will try to add one if it is missing. </p>
<p> For example </p>
<pre>
 perltidy somefile.pl -opath=/tmp/
</pre>
<p> will produce <i>/tmp/somefile.pl.tdy</i>. Otherwise, <i>somefile.pl.tdy</i> will appear in whatever directory contains <i>somefile.pl</i>. </p>
<p> If the path contains spaces, it should be placed in quotes. </p>
<p> This parameter will be ignored if output is being directed to standard output, or if it is being specified explicitly with the <code>-o=s</code> parameter.</p>
<dt><code>-b</code>, <code>&#8211;backup-and-modify-in-place</code></p>
<dd> Modify the input file or files in-place and save the original with the extension <i>.bak</i>. Any existing <i>.bak</i> file will be deleted. See next item for changing the default backup extension, and for eliminating the backup file altogether. </p>
<p> A <code>-b</code> flag will be ignored if input is from standard input or goes to standard output, or if the <code>-html</code> flag is set. </p>
<p> In particular, if you want to use both the <code>-b</code> flag and the <code>-pbp</code> (&#8211;perl-best-practices) flag, then you must put a <code>-nst</code> flag after the <code>-pbp</code> flag because it contains a <code>-st</code> flag as one of its components, which means that output will go to the standard output stream.</p>
<dt><code>-bext</code>=ext, <code>&#8211;backup-file-extension</code>=ext</p>
<dd> This parameter serves two purposes: (1) to change the extension of the backup file to be something other than the default <i>.bak</i>, and (2) to indicate that no backup file should be saved. </p>
<p> To change the default extension to something other than <i>.bak</i> see &#8220;Specifying File Extensions&#8221;. </p>
<p> A backup file of the source is always written, but you can request that it be deleted at the end of processing if there were no errors. This is risky unless the source code is being maintained with a source code control system. </p>
<p> To indicate that the backup should be deleted include one forward slash, <code>/</code>, in the extension. If any text remains after the slash is removed it will be used to define the backup file extension (which is always created and only deleted if there were no errors). </p>
<p> Here are some examples: </p>
<pre>
  Parameter           Extension          Backup File Treatment
  &lt;-bext=bak&gt;         F&lt;.bak&gt;            Keep (same as the default behavior)
  &lt;-bext='/'&gt;         F&lt;.bak&gt;            Delete if no errors
  &lt;-bext='/backup'&gt;   F&lt;.backup&gt;         Delete if no errors
  &lt;-bext='original/'&gt; F&lt;.original&gt;       Delete if no errors
</pre>
<dt><code>-w</code>, <code>&#8211;warning-output</code></p>
<dd> Setting <code>-w</code> causes any non-critical warning messages to be reported as errors. These include messages about possible pod problems, possibly bad starting indentation level, and cautions about indirect object usage. The default, <code>-nw</code> or <code>&#8211;nowarning-output</code>, is not to include these warnings.</p>
<dt><code>-q</code>, <code>&#8211;quiet</code></p>
<dd> Deactivate error messages and syntax checking (for running under an editor). </p>
<p> For example, if you use a vi-style editor, such as vim, you may execute perltidy as a filter from within the editor using something like </p>
<pre>
 :n1,n2!perltidy -q
</pre>
<p> where <tt>&quot;n1,n2&quot;</tt> represents the selected text. Without the <code>-q</code> flag, any error message may mess up your screen, so be prepared to use your &#8220;undo&#8221; key.</p>
<dt><code>-log</code>, <code>&#8211;logfile</code></p>
<dd> Save the <i>.LOG</i> file, which has many useful diagnostics. Perltidy always creates a <i>.LOG</i> file, but by default it is deleted unless a program bug is suspected. Setting the <code>-log</code> flag forces the log file to be saved.</p>
<dt><code>-g=n</code>, <code>&#8211;logfile-gap=n</code></p>
<dd> Set maximum interval between input code lines in the logfile. This purpose of this flag is to assist in debugging nesting errors. The value of <tt>&quot;n&quot;</tt> is optional. If you set the flag <code>-g</code> without the value of <tt>&quot;n&quot;</tt>, it will be taken to be 1, meaning that every line will be written to the log file. This can be helpful if you are looking for a brace, paren, or bracket nesting error. </p>
<p> Setting <code>-g</code> also causes the logfile to be saved, so it is not necessary to also include <code>-log</code>. </p>
<p> If no <code>-g</code> flag is given, a value of 50 will be used, meaning that at least every 50th line will be recorded in the logfile. This helps prevent excessively long log files. </p>
<p> Setting a negative value of <tt>&quot;n&quot;</tt> is the same as not setting <code>-g</code> at all.</p>
<dt><code>-npro</code> <code>&#8211;noprofile</code></p>
<dd> Ignore any <i>.perltidyrc</i> command file. Normally, perltidy looks first in your current directory for a <i>.perltidyrc</i> file of parameters. (The format is described below). If it finds one, it applies those options to the initial default values, and then it applies any that have been defined on the command line. If no <i>.perltidyrc</i> file is found, it looks for one in your home directory. </p>
<p> If you set the <code>-npro</code> flag, perltidy will not look for this file.</p>
<dt><code>-pro=filename</code> or <code>&#8211;profile=filename</code></p>
<dd> To simplify testing and switching .perltidyrc files, this command may be used to specify a configuration file which will override the default name of .perltidyrc. There must not be a space on either side of the &#8216;=&#8217; sign. For example, the line </p>
<pre>
   perltidy -pro=testcfg
</pre>
<p> would cause file <i>testcfg</i> to be used instead of the default <i>.perltidyrc</i>. </p>
<p> A pathname begins with three dots, e.g. &#8220;&#8230;/.perltidyrc&#8221;, indicates that the file should be searched for starting in the current directory and working upwards. This makes it easier to have multiple projects each with their own .perltidyrc in their root directories.</p>
<dt><code>-opt</code>, <code>&#8211;show-options</code></p>
<dd> Write a list of all options used to the <i>.LOG</i> file. Please see <code>&#8211;dump-options</code> for a simpler way to do this.</p>
<dt><code>-f</code>, <code>&#8211;force-read-binary</code></p>
<dd> Force perltidy to process binary files. To avoid producing excessive error messages, perltidy skips files identified by the system as non-text. However, valid perl scripts containing binary data may sometimes be identified as non-text, and this flag forces perltidy to process them.</dl>
<h2>FORMATTING OPTIONS</h2>
<h3>Basic Options</h3>
<dl>
<dt><code>&#8211;notidy</code></p>
<dd> This flag disables all formatting and causes the input to be copied unchanged to the output except for possible changes in line ending characters and any pre- and post-filters. This can be useful in conjunction with a hierarchical set of <i>.perltidyrc</i> files to avoid unwanted code tidying. See also &#8220;Skipping Selected Sections of Code&#8221; for a way to avoid tidying specific sections of code.</p>
<dt><code>-i=n</code>, <code>&#8211;indent-columns=n</code></p>
<dd> Use n columns per indentation level (default n=4).</p>
<dt><code>-l=n</code>, <code>&#8211;maximum-line-length=n</code></p>
<dd> The default maximum line length is n=80 characters. Perltidy will try to find line break points to keep lines below this length. However, long quotes and side comments may cause lines to exceed this length. Setting <code>-l=0</code> is equivalent to setting <code>-l=(a large number)</code>.</p>
<dt><code>-vmll</code>, <code>&#8211;variable-maximum-line-length</code></p>
<dd> A problem arises using a fixed maximum line length with very deeply nested code and data structures because eventually the amount of leading whitespace used for indicating indation takes up most or all of the available line width, leaving little or no space for the actual code or data. One solution is to use a vary long line length. Another solution is to use the <code>-vmll</code> flag, which basically tells perltidy to ignore leading whitespace when measuring the line length. </p>
<p> To be precise, when the <code>-vmll</code> parameter is set, the maximum line length of a line of code will be M+L*I, where </p>
<pre>
      M is the value of --maximum-line-length=M (-l=M), default 80,
      I is the value of --indent-columns=I (-i=I), default 4,
      L is the indentation level of the line of code
</pre>
<p> When this flag is set, the choice of breakpoints for a block of code should be essentially independent of its nesting depth. However, the absolute line lengths, including leading whitespace, can still be arbitrarily large. This problem can be avoided by including the next parameter. </p>
<p> The default is not to do this (<code>-nvmll</code>).</p>
<dt><code>-wc=n</code>, <code>&#8211;whitespace-cycle=n</code></p>
<dd> This flag also addresses problems with very deeply nested code and data structures. When the nesting depth exceeds the value <code>n</code> the leading whitespace will be reduced and start at a depth of 1 again. The result is that blocks of code will shift back to the left rather than moving arbitrarily far to the right. This occurs cyclically to any depth. </p>
<p> For example if one level of indentation equals 4 spaces (<code>-i=4</code>, the default), and one uses <code>-wc=15</code>, then if the leading whitespace on a line exceeds about 4*15=60 spaces it will be reduced back to 4*1=4 spaces and continue increasing from there. If the whitespace never exceeds this limit the formatting remains unchanged. </p>
<p> The combination of <code>-vmll</code> and <code>-wc=n</code> provides a solution to the problem of displaying arbitrarily deep data structures and code in a finite window, although <code>-wc=n</code> may of course be used without <code>-vmll</code>. </p>
<p> The default is not to use this, which can also be indicated using <code>-wc=0</code>.</p>
<dt>tabs</p>
<dd> Using tab characters will almost certainly lead to future portability and maintenance problems, so the default and recommendation is not to use them. For those who prefer tabs, however, there are two different options. </p>
<p> Except for possibly introducing tab indentation characters, as outlined below, perltidy does not introduce any tab characters into your file, and it removes any tabs from the code (unless requested not to do so with <code>-fws</code>). If you have any tabs in your comments, quotes, or here-documents, they will remain.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>-et=n</code>, <code>&#8211;entab-leading-whitespace</code></p>
<dd> This flag causes each <code>n</code> initial space characters to be replaced by one tab character. Note that the integer <code>n</code> is completely independent of the integer specified for indentation parameter, <code>-i=n</code>.</p>
<dt><code>-t</code>, <code>&#8211;tabs</code></p>
<dd> This flag causes one leading tab character to be inserted for each level of indentation. Certain other features are incompatible with this option, and if these options are also given, then a warning message will be issued and this flag will be unset. One example is the <code>-lp</code> option.</p>
<dt><code>-dt=n</code>, <code>&#8211;default-tabsize=n</code></p>
<dd> If the the first line of code passed to perltidy contains leading tabs but no tab scheme is specified for the output stream then perltidy must guess how many spaces correspond to each leading tab. This number of spaces <code>n</code> corresponding to each leading tab of the input stream may be specified with <code>-dt=n</code>. The default is <code>n=8</code>. </p>
<p> This flag has no effect if a tab scheme is specified for the output stream, because then the input stream is assumed to use the same tab scheme and indentation spaces as for the output stream (any other assumption would lead to unstable editing).</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>-syn</code>, <code>&#8211;check-syntax</code></p>
<dd> This flag causes perltidy to run <tt>&quot;perl -c -T&quot;</tt> to check syntax of input and output. (To change the flags passed to perl, see the next item, <code>-pscf</code>). The results are written to the <i>.LOG</i> file, which will be saved if an error is detected in the output script. The output script is not checked if the input script has a syntax error. Perltidy does its own checking, but this option employs perl to get a &#8220;second opinion&#8221;. </p>
<p> If perl reports errors in the input file, they will not be reported in the error output unless the <code>&#8211;warning-output</code> flag is given. </p>
<p> The default is <font SIZE="-1"><code>NOT</code></font> to do this type of syntax checking (although perltidy will still do as much self-checking as possible). The reason is that it causes all code in <font SIZE="-1">BEGIN</font> blocks to be executed, for all modules being used, and this opens the door to security issues and infinite loops when running perltidy.</p>
<dt><code>-pscf=s</code>, <code>-perl-syntax-check-flags=s</code></p>
<dd> When perl is invoked to check syntax, the normal flags are <tt>&quot;-c -T&quot;</tt>. In addition, if the <code>-x</code> flag is given to perltidy, then perl will also be passed a <code>-x</code> flag. It should not normally be necessary to change these flags, but it can be done with the <code>-pscf=s</code> flag. For example, if the taint flag, <tt>&quot;-T&quot;</tt>, is not wanted, the flag could be set to be just <code>-pscf=-c</code>. </p>
<p> Perltidy will pass your string to perl with the exception that it will add a <code>-c</code> and <code>-x</code> if appropriate. The <i>.LOG</i> file will show exactly what flags were passed to perl.</p>
<dt><code>-io</code>, <code>&#8211;indent-only</code></p>
<dd> This flag is used to deactivate all formatting and line break changes within non-blank lines of code. When it is in effect, the only change to the script will be to the indentation and blank lines. And any flags controlling whitespace and newlines will be ignored. You might want to use this if you are perfectly happy with your whitespace and line breaks, and merely want perltidy to handle the indentation. (This also speeds up perltidy by well over a factor of two, so it might be useful when perltidy is merely being used to help find a brace error in a large script). </p>
<p> Setting this flag is equivalent to setting <code>&#8211;freeze-newlines</code> and <code>&#8211;freeze-whitespace</code>. </p>
<p> If you also want to keep your existing blank lines exactly as they are, you can add <code>&#8211;freeze-blank-lines</code>.</p>
<dt><code>-ole=s</code>, <code>&#8211;output-line-ending=s</code></p>
<dd> where s=<tt>&quot;win&quot;</tt>, <tt>&quot;dos&quot;</tt>, <tt>&quot;unix&quot;</tt>, or <tt>&quot;mac&quot;</tt>. This flag tells perltidy to output line endings for a specific system. Normally, perltidy writes files with the line separator character of the host system. The <tt>&quot;win&quot;</tt> and <tt>&quot;dos&quot;</tt> flags have an identical result.</p>
<dt><code>-ple</code>, <code>&#8211;preserve-line-endings</code></p>
<dd> This flag tells perltidy to write its output files with the same line endings as the input file, if possible. It should work for <code>dos</code>, <code>unix</code>, and <code>mac</code> line endings. It will only work if perltidy input comes from a filename (rather than stdin, for example). If perltidy has trouble determining the input file line ending, it will revert to the default behavior of using the line ending of the host system.</p>
<dt><code>-it=n</code>, <code>&#8211;iterations=n</code></p>
<dd> This flag causes perltidy to do <code>n</code> complete iterations. The reason for this flag is that code beautification is an iterative process and in some cases the output from perltidy can be different if it is applied a second time. For most purposes the default of <code>n=1</code> should be satisfactory. However <code>n=2</code> can be useful when a major style change is being made, or when code is being beautified on check-in to a source code control system. It has been found to be extremely rare for the output to change after 2 iterations. If a value <code>n</code> is greater than 2 is input then a convergence test will be used to stop the iterations as soon as possible, almost always after 2 iterations. See the next item for a simplified iteration control. </p>
<p> This flag has no effect when perltidy is used to generate html.</p>
<dt><code>-conv</code>, <code>&#8211;converge</code></p>
<dd> This flag is equivalent to <code>-it=4</code> and is included to simplify iteration control. For all practical purposes one either does or does not want to be sure that the output is converged, and there is no penalty to using a large iteration limit since perltidy will check for convergence and stop iterating as soon as possible. The default is <code>-nconv</code> (no convergence check). Using <code>-conv</code> will approximately double run time since normally one extra iteration is required to verify convergence.</dl>
<h3>Code Indentation Control</h3>
<dl>
<dt><code>-ci=n</code>, <code>&#8211;continuation-indentation=n</code></p>
<dd> Continuation indentation is extra indentation spaces applied when a long line is broken. The default is n=2, illustrated here: </p>
<pre>
 my $level =   # -ci=2      
   ( $max_index_to_go &gt;= 0 ) ? $levels_to_go[0] : $last_output_level;
</pre>
<p> The same example, with n=0, is a little harder to read: </p>
<pre>
 my $level =   # -ci=0    
 ( $max_index_to_go &gt;= 0 ) ? $levels_to_go[0] : $last_output_level;
</pre>
<p> The value given to <code>-ci</code> is also used by some commands when a small space is required. Examples are commands for outdenting labels, <code>-ola</code>, and control keywords, <code>-okw</code>. </p>
<p> When default values are not used, it is suggested that the value <code>n</code> given with <code>-ci=n</code> be no more than about one-half of the number of spaces assigned to a full indentation level on the <code>-i=n</code> command.</p>
<dt><code>-sil=n</code> <code>&#8211;starting-indentation-level=n</code></p>
<dd> By default, perltidy examines the input file and tries to determine the starting indentation level. While it is often zero, it may not be zero for a code snippet being sent from an editing session. </p>
<p> To guess the starting indentation level perltidy simply assumes that indentation scheme used to create the code snippet is the same as is being used for the current perltidy process. This is the only sensible guess that can be made. It should be correct if this is true, but otherwise it probably won&#8217;t. For example, if the input script was written with -i=2 and the current peltidy flags have -i=4, the wrong initial indentation will be guessed for a code snippet which has non-zero initial indentation. Likewise, if an entabbing scheme is used in the input script and not in the current process then the guessed indentation will be wrong. </p>
<p> If the default method does not work correctly, or you want to change the starting level, use <code>-sil=n</code>, to force the starting level to be n.</p>
<dt>List indentation using <code>-lp</code>, <code>&#8211;line-up-parentheses</code></p>
<dd> By default, perltidy indents lists with 4 spaces, or whatever value is specified with <code>-i=n</code>. Here is a small list formatted in this way: </p>
<pre>
    # perltidy (default)
    @month_of_year = (
        'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
        'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
    );
</pre>
<p> Use the <code>-lp</code> flag to add extra indentation to cause the data to begin past the opening parentheses of a sub call or list, or opening square bracket of an anonymous array, or opening curly brace of an anonymous hash. With this option, the above list would become: </p>
<pre>
    # perltidy -lp
    @month_of_year = (
                       'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                       'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
    );
</pre>
<p> If the available line length (see <code>-l=n</code> ) does not permit this much space, perltidy will use less. For alternate placement of the closing paren, see the next section. </p>
<p> This option has no effect on code <font SIZE="-1">BLOCKS,</font> such as if/then/else blocks, which always use whatever is specified with <code>-i=n</code>. Also, the existence of line breaks and/or block comments between the opening and closing parens may cause perltidy to temporarily revert to its default method. </p>
<p> Note: The <code>-lp</code> option may not be used together with the <code>-t</code> tabs option. It may, however, be used with the <code>-et=n</code> tab method. </p>
<p> In addition, any parameter which significantly restricts the ability of perltidy to choose newlines will conflict with <code>-lp</code> and will cause <code>-lp</code> to be deactivated. These include <code>-io</code>, <code>-fnl</code>, <code>-nanl</code>, and <code>-ndnl</code>. The reason is that the <code>-lp</code> indentation style can require the careful coordination of an arbitrary number of break points in hierarchical lists, and these flags may prevent that.</p>
<dt><code>-cti=n</code>, <code>&#8211;closing-token-indentation</code></p>
<dd> The <code>-cti=n</code> flag controls the indentation of a line beginning with a <tt>&quot;)&quot;</tt>, <tt>&quot;]&quot;</tt>, or a non-block <tt>&quot;}&quot;</tt>. Such a line receives: </p>
<p> -cti = 0 no extra indentation (default)<br />
 -cti = 1 extra indentation such that the closing token<br />
        aligns with its opening token.<br />
 -cti = 2 one extra indentation level if the line looks like:<br />
        );  or  ];<br />
 or<br />
 }<br />
 ;<br />
 &#8211; cti = 3 one extra indentation level always</p>
<p> The flags <code>-cti=1</code> and <code>-cti=2</code> work well with the <code>-lp</code> flag (previous section). </p>
<pre>
    # perltidy -lp -cti=1
    @month_of_year = (
                       'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                       'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
                     );
    # perltidy -lp -cti=2
    @month_of_year = (
                       'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                       'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
                       );
</pre>
<p> These flags are merely hints to the formatter and they may not always be followed. In particular, if -lp is not being used, the indentation for <code>cti=1</code> is constrained to be no more than one indentation level. </p>
<p> If desired, this control can be applied independently to each of the closing container token types. In fact, <code>-cti=n</code> is merely an abbreviation for <code>-cpi=n -csbi=n -cbi=n</code>, where: <code>-cpi</code> or <code>&#8211;closing-paren-indentation</code> controls <code>)</code>&#8216;s, <code>-csbi</code> or <code>&#8211;closing-square-bracket-indentation</code> controls <code>]</code>&#8216;s, <code>-cbi</code> or <code>&#8211;closing-brace-indentation</code> controls non-block <code>}</code>&#8216;s.</p>
<dt><code>-icp</code>, <code>&#8211;indent-closing-paren</code></p>
<dd> The <code>-icp</code> flag is equivalent to <code>-cti=2</code>, described in the previous section. The <code>-nicp</code> flag is equivalent <code>-cti=0</code>. They are included for backwards compatibility.</p>
<dt><code>-icb</code>, <code>&#8211;indent-closing-brace</code></p>
<dd> The <code>-icb</code> option gives one extra level of indentation to a brace which terminates a code block . For example, </p>
<p>if ($task) {<br />
    yyy();<br />
}<br />
#- icb else<br />
{<br />
    zzz();<br />
}</p>
<p> The default is not to do this, indicated by <code>-nicb</code>.</p>
<dt><code>-olq</code>, <code>&#8211;outdent-long-quotes</code></p>
<dd> When <code>-olq</code> is set, lines which is a quoted string longer than the value <code>maximum-line-length</code> will have their indentation removed to make them more readable. This is the default. To prevent such out-denting, use <code>-nolq</code> or <code>&#8211;nooutdent-long-lines</code>.</p>
<dt><code>-oll</code>, <code>&#8211;outdent-long-lines</code></p>
<dd> This command is equivalent to <code>&#8211;outdent-long-quotes</code> and <code>&#8211;outdent-long-comments</code>, and it is included for compatibility with previous versions of perltidy. The negation of this also works, <code>-noll</code> or <code>&#8211;nooutdent-long-lines</code>, and is equivalent to setting <code>-nolq</code> and <code>-nolc</code>.</p>
<dt>Outdenting Labels: <code>-ola</code>, <code>&#8211;outdent-labels</code></p>
<dd> This command will cause labels to be outdented by 2 spaces (or whatever <code>-ci</code> has been set to), if possible. This is the default. For example: </p>
<p>my $i;<br />
LOOP : while ($i = &lt;FOTOS&gt;)<br />
{<br />
    chomp($i);<br />
    next unless $i;<br />
    fixit($i);<br />
}</p>
<p> Use <code>-nola</code> to not outdent labels.</p>
<dt>Outdenting Keywords</p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt><code>-okw</code>, <code>&#8211;outdent-keywords</code></p>
<dd> The command <code>-okw</code> will will cause certain leading control keywords to be outdented by 2 spaces (or whatever <code>-ci</code> has been set to), if possible. By default, these keywords are <tt>&quot;redo&quot;</tt>, <tt>&quot;next&quot;</tt>, <tt>&quot;last&quot;</tt>, <tt>&quot;goto&quot;</tt>, and <tt>&quot;return&quot;</tt>. The intention is to make these control keywords easier to see. To change this list of keywords being outdented, see the next section. </p>
<p> For example, using <tt>&quot;perltidy -okw&quot;</tt> on the previous example gives: </p>
<p>my $i;<br />
LOOP : while ($i = &lt;FOTOS&gt;)<br />
{<br />
    chomp($i);<br />
    next unless $i;<br />
    fixit($i);<br />
}</p>
<p> The default is not to do this.</p>
<dt>Specifying Outdented Keywords: <code>-okwl=string</code>, <code>&#8211;outdent-keyword-list=string</code></p>
<dd> This command can be used to change the keywords which are outdented with the <code>-okw</code> command. The parameter <code>string</code> is a required list of perl keywords, which should be placed in quotes if there are more than one. By itself, it does not cause any outdenting to occur, so the <code>-okw</code> command is still required. </p>
<p> For example, the commands <tt>&quot;-okwl=&quot;next last redo goto&quot; -okw&quot;</tt> will cause those four keywords to be outdented. It is probably simplest to place any <code>-okwl</code> command in a <i>.perltidyrc</i> file.</dl>
</dl>
<dl>
<dt>
<dd></dl>
</dl>
<h3>Whitespace Control</h3>
<p> Whitespace refers to the blank space between variables, operators, and other code tokens.</p>
<dl>
<dt><code>-fws</code>, <code>&#8211;freeze-whitespace</code></p>
<dd> This flag causes your original whitespace to remain unchanged, and causes the rest of the whitespace commands in this section, the Code Indentation section, and the Comment Control section to be ignored.</p>
<dt>Tightness of curly braces, parentheses, and square brackets.</p>
<dd> Here the term &#8220;tightness&#8221; will mean the closeness with which pairs of enclosing tokens, such as parentheses, contain the quantities within. A numerical value of 0, 1, or 2 defines the tightness, with 0 being least tight and 2 being most tight. Spaces within containers are always symmetric, so if there is a space after a <tt>&quot;(&quot;</tt> then there will be a space before the corresponding <tt>&quot;)&quot;</tt>. </p>
<p> The <code>-pt=n</code> or <code>&#8211;paren-tightness=n</code> parameter controls the space within parens. The example below shows the effect of the three possible values, 0, 1, and 2: </p>
<p>if ((my $len_tab = length($tabstr)) &gt; 0) {<br />
#- pt = 0 if ((my $len_tab = length($tabstr))&gt; 0)<br />
    {<br />
#- pt = 1(default) if ((my $len_tab = length($tabstr))&gt; 0)<br />
        {<br />
#- pt = 2</p>
<p> When n is 0, there is always a space to the right of a &#8216;(&#8216; and to the left of a &#8216;)&#8217;. For n=2 there is never a space. For n=1, the default, there is a space unless the quantity within the parens is a single token, such as an identifier or quoted string. </p>
<p> Likewise, the parameter <code>-sbt=n</code> or <code>&#8211;square-bracket-tightness=n</code> controls the space within square brackets, as illustrated below. </p>
<p>$width = $col[$j + $k] &#8211; $col[$j];<br />
#- sbt = 0 $width = $col[$j + $k] &#8211; $col[$j];<br />
#- sbt = 1(default)<br />
    $width = $col[$j + $k] &#8211; $col[$j];<br />
#- sbt = 2</p>
<p> Curly braces which do not contain code blocks are controlled by the parameter <code>-bt=n</code> or <code>&#8211;brace-tightness=n</code>. </p>
<p>$obj-&gt;{$parsed_sql-&gt;{&#8216;table&#8217;}[0]};<br />
#- bt = 0 $obj-&gt;{$parsed_sql-&gt;{&#8216;table&#8217; }[0] };<br />
#- bt = 1(default)<br />
              $obj-&gt;{$parsed_sql-&gt;{&#8216;table&#8217; }[0] };<br />
#- bt = 2</p>
<p> And finally, curly braces which contain blocks of code are controlled by the parameter <code>-bbt=n</code> or <code>&#8211;block-brace-tightness=n</code> as illustrated in the example below. </p>
<p>% bf = map{$_ = &gt; -M $_} grep{ /\.deb$ / } dirents &#8216;.&#8217;;<br />
#- bbt = 0(default) % bf = map{$_ =&gt; &#8211; M $_ } grep{/\.deb$ / } dirents &#8216;.&#8217;;<br />
#- bbt = 1 % bf = map{$_ =&gt; &#8211; M $_ } grep{/\.deb$ / } dirents &#8216;.&#8217;;<br />
#- bbt = 2</p>
<p> To simplify input in the case that all of the tightness flags have the same value &lt;n&gt;, the parameter &lt;-act=n&gt; or <code>&#8211;all-containers-tightness=n</code> is an abbreviation for the combination &lt;-pt=n -sbt=n -bt=n -bbt=n&gt;.</p>
<dt><code>-tso</code>, <code>&#8211;tight-secret-operators</code></p>
<dd> The flag <code>-tso</code> causes certain perl token sequences (secret operators) which might be considered to be a single operator to be formatted &#8220;tightly&#8221; (without spaces). The operators currently modified by this flag are: </p>
<pre>
     0+  +0  ()x!! ~~&lt;&gt;  ,=&gt;   =( )=
</pre>
<p> For example the sequence <code>0 +</code>, which converts a string to a number, would be formatted without a space: <code>0+</code> when the <code>-tso</code> flag is set. This flag is off by default.</p>
<dt><code>-sts</code>, <code>&#8211;space-terminal-semicolon</code></p>
<dd> Some programmers prefer a space before all terminal semicolons. The default is for no such space, and is indicated with <code>-nsts</code> or <code>&#8211;nospace-terminal-semicolon</code>. </p>
<pre>
        $i = 1 ;     #  -sts
        $i = 1;      #  -nsts   (default)
</pre>
<dt><code>-sfs</code>, <code>&#8211;space-for-semicolon</code></p>
<dd> Semicolons within <code>for</code> loops may sometimes be hard to see, particularly when commas are also present. This option places spaces on both sides of these special semicolons, and is the default. Use <code>-nsfs</code> or <code>&#8211;nospace-for-semicolon</code> to deactivate it. </p>
<p>for (@a = @$ap, $u = shift @a; @a; $u = $v) {<br />
#- sfs(default) for (@a = @$ap, $u = shift @a; @a; $u = $v)<br />
    {<br />
#- nsfs</p>
<dt><code>-asc</code>, <code>&#8211;add-semicolons</code></p>
<dd> Setting <code>-asc</code> allows perltidy to add any missing optional semicolon at the end of a line which is followed by a closing curly brace on the next line. This is the default, and may be deactivated with <code>-nasc</code> or <code>&#8211;noadd-semicolons</code>.</p>
<dt><code>-dsm</code>, <code>&#8211;delete-semicolons</code></p>
<dd> Setting <code>-dsm</code> allows perltidy to delete extra semicolons which are simply empty statements. This is the default, and may be deactivated with <code>-ndsm</code> or <code>&#8211;nodelete-semicolons</code>. (Such semicolons are not deleted, however, if they would promote a side comment to a block comment).</p>
<dt><code>-aws</code>, <code>&#8211;add-whitespace</code></p>
<dd> Setting this option allows perltidy to add certain whitespace improve code readability. This is the default. If you do not want any whitespace added, but are willing to have some whitespace deleted, use <code>-naws</code>. (Use <code>-fws</code> to leave whitespace completely unchanged).</p>
<dt><code>-dws</code>, <code>&#8211;delete-old-whitespace</code></p>
<dd> Setting this option allows perltidy to remove some old whitespace between characters, if necessary. This is the default. If you do not want any old whitespace removed, use <code>-ndws</code> or <code>&#8211;nodelete-old-whitespace</code>.</p>
<dt>Detailed whitespace controls around tokens</p>
<dd> For those who want more detailed control over the whitespace around tokens, there are four parameters which can directly modify the default whitespace rules built into perltidy for any token. They are: </p>
<p> <code>-wls=s</code> or <code>&#8211;want-left-space=s</code>, </p>
<p> <code>-nwls=s</code> or <code>&#8211;nowant-left-space=s</code>, </p>
<p> <code>-wrs=s</code> or <code>&#8211;want-right-space=s</code>, </p>
<p> <code>-nwrs=s</code> or <code>&#8211;nowant-right-space=s</code>. </p>
<p> These parameters are each followed by a quoted string, <code>s</code>, containing a list of token types. No more than one of each of these parameters should be specified, because repeating a command-line parameter always overwrites the previous one before perltidy ever sees it. </p>
<p> To illustrate how these are used, suppose it is desired that there be no space on either side of the token types <code>= + &#8211; / *</code>. The following two parameters would specify this desire: </p>
<pre>
  -nwls=&quot;= + - / *&quot;    -nwrs=&quot;= + - / *&quot;
</pre>
<p> (Note that the token types are in quotes, and that they are separated by spaces). With these modified whitespace rules, the following line of math: </p>
<pre>
  $root = -$b + sqrt( $b * $b - 4. * $a * $c ) / ( 2. * $a );
</pre>
<p> becomes this: </p>
<pre>
  $root=-$b+sqrt( $b*$b-4.*$a*$c )/( 2.*$a );
</pre>
<p> These parameters should be considered to be hints to perltidy rather than fixed rules, because perltidy must try to resolve conflicts that arise between them and all of the other rules that it uses. One conflict that can arise is if, between two tokens, the left token wants a space and the right one doesn&#8217;t. In this case, the token not wanting a space takes priority. </p>
<p> It is necessary to have a list of all token types in order to create this type of input. Such a list can be obtained by the command <code>&#8211;dump-token-types</code>. Also try the <code>-D</code> flag on a short snippet of code and look at the .DEBUG file to see the tokenization. </p>
<p> <font SIZE="-1"><code>WARNING</code></font> Be sure to put these tokens in quotes to avoid having them misinterpreted by your command shell.</p>
<dt>Space between specific keywords and opening paren</p>
<dd> When an opening paren follows a Perl keyword, no space is introduced after the keyword, unless it is (by default) one of these: </p>
<p>   my local our and or eq ne if else elsif until unless<br />
   while for foreach return switch case given when</p>
<p> These defaults can be modified with two commands: </p>
<p> <code>-sak=s</code> or <code>&#8211;space-after-keyword=s</code> adds keywords. </p>
<p> <code>-nsak=s</code> or <code>&#8211;nospace-after-keyword=s</code> removes keywords. </p>
<p> where <code>s</code> is a list of keywords (in quotes if necessary). For example, </p>
<p>my($a, $b, $c) = @_;<br />
#default my($a, $b, $c) = @_;<br />
#- nsak = &#8220;my local our&#8221;</p>
<p> The abbreviation <code>-nsak=&#8217;*&#8217;</code> is equivalent to including all of the keywords in the above list. </p>
<p> When both <code>-nsak=s</code> and <code>-sak=s</code> commands are included, the <code>-nsak=s</code> command is executed first. For example, to have space after only the keywords (my, local, our) you could use <code>-nsak=&#8220;*&#8221; -sak=&#8220;my local our&#8221;</code>. </p>
<p> To put a space after all keywords, see the next item.</p>
<dt>Space between all keywords and opening parens</p>
<dd> When an opening paren follows a function or keyword, no space is introduced after the keyword except for the keywords noted in the previous item. To always put a space between a function or keyword and its opening paren, use the command: </p>
<p> <code>-skp</code> or <code>&#8211;space-keyword-paren</code> </p>
<p> You will probably also want to use the flag <code>-sfp</code> (next item) too.</p>
<dt>Space between all function names and opening parens</p>
<dd> When an opening paren follows a function the default is not to introduce a space. To cause a space to be introduced use: </p>
<p> <code>-sfp</code> or <code>&#8211;space-function-paren</code> </p>
<p>myfunc($a, $b, $c);<br />
#default myfunc($a, $b, $c);<br />
#- sfp</p>
<p> You will probably also want to use the flag <code>-skp</code> (previous item) too.</p>
<dt>Trimming whitespace around &quot;qw&quot; quotes</p>
<dd> <code>-tqw</code> or <code>&#8211;trim-qw</code> provide the default behavior of trimming spaces around multi-line <tt>&quot;qw&quot;</tt> quotes and indenting them appropriately. </p>
<p> <code>-ntqw</code> or <code>&#8211;notrim-qw</code> cause leading and trailing whitespace around multi-line <tt>&quot;qw&quot;</tt> quotes to be left unchanged. This option will not normally be necessary, but was added for testing purposes, because in some versions of perl, trimming <tt>&quot;qw&quot;</tt> quotes changes the syntax tree.</dl>
<h3>Comment Controls</h3>
<p> Perltidy has a number of ways to control the appearance of both block comments and side comments. The term <code>block comment</code> here refers to a full-line comment, whereas <code>side comment</code> will refer to a comment which appears on a line to the right of some code.</p>
<dl>
<dt><code>-ibc</code>, <code>&#8211;indent-block-comments</code></p>
<dd> Block comments normally look best when they are indented to the same level as the code which follows them. This is the default behavior, but you may use <code>-nibc</code> to keep block comments left-justified. Here is an example: </p>
<p>#this comment is indented(-ibc, default)<br />
if ($task) {<br />
    yyy();<br />
}</p>
<p> The alternative is <code>-nibc</code>: </p>
<p>#this comment is not indented(-nibc)<br />
if ($task) {<br />
    yyy();<br />
}</p>
<p> See also the next item, <code>-isbc</code>, as well as <code>-sbc</code>, for other ways to have some indented and some outdented block comments.</p>
<dt><code>-isbc</code>, <code>&#8211;indent-spaced-block-comments</code></p>
<dd> If there is no leading space on the line, then the comment will not be indented, and otherwise it may be. </p>
<p> If both <code>-ibc</code> and <code>-isbc</code> are set, then <code>-isbc</code> takes priority.</p>
<dt><code>-olc</code>, <code>&#8211;outdent-long-comments</code></p>
<dd> When <code>-olc</code> is set, lines which are full-line (block) comments longer than the value <code>maximum-line-length</code> will have their indentation removed. This is the default; use <code>-nolc</code> to prevent outdenting.</p>
<dt><code>-msc=n</code>, <code>&#8211;minimum-space-to-comment=n</code></p>
<dd> Side comments look best when lined up several spaces to the right of code. Perltidy will try to keep comments at least n spaces to the right. The default is n=4 spaces.</p>
<dt><code>-fpsc=n</code>, <code>&#8211;fixed-position-side-comment=n</code></p>
<dd> This parameter tells perltidy to line up side comments in column number <code>n</code> whenever possible. The default, n=0, is not do do this.</p>
<dt><code>-iscl</code>, <code>&#8211;ignore-side-comment-lengths</code></p>
<dd> This parameter causes perltidy to ignore the length of side comments when setting line breaks. The default, <code>-niscl</code>, is to include the length of side comments when breaking lines to stay within the length prescribed by the <code>-l=n</code> maximum line length parameter. For example, the following long single line would remain intact with -l=80 and -iscl: </p>
<p>perltidy &#8211; l = 80 &#8211; iscl<br />
                        $vmsfile = ~s /<br />
    ;<br />
[\d\- ] * $ //; # Clip off version number; we can use a newer version as well</p>
<p> whereas without the -iscl flag the line will be broken: </p>
<p>perltidy &#8211; l = 80 $vmsfile = ~s / ;<br />
[\d\- ] * $ //<br />
    ;<br />
#Clip off version number;<br />
we can use a newer version as well</p>
<dt><code>-hsc</code>, <code>&#8211;hanging-side-comments</code></p>
<dd> By default, perltidy tries to identify and align &#8220;hanging side comments&#8221;, which are something like this: </p>
<pre>
        my $IGNORE = 0;    # This is a side comment
                           # This is a hanging side comment
                           # And so is this
</pre>
<p> A comment is considered to be a hanging side comment if (1) it immediately follows a line with a side comment, or another hanging side comment, and (2) there is some leading whitespace on the line. To deactivate this feature, use <code>-nhsc</code> or <code>&#8211;nohanging-side-comments</code>. If block comments are preceded by a blank line, or have no leading whitespace, they will not be mistaken as hanging side comments.</p>
<dt>Closing Side Comments</p>
<dd> A closing side comment is a special comment which perltidy can automatically create and place after the closing brace of a code block. They can be useful for code maintenance and debugging. The command <code>-csc</code> (or <code>&#8211;closing-side-comments</code>) adds or updates closing side comments. For example, here is a small code snippet </p>
<p>sub message<br />
{<br />
    if (!defined($_[0])) {<br />
        print(&#8220;Hello, World
&#8221;);<br />
    } else {<br />
        print($_[0], &#8220;
&#8221;);<br />
    }<br />
}</p>
<p> And here is the result of processing with <tt>&quot;perltidy -csc&quot;</tt>: </p>
<p>sub message<br />
{<br />
    if (!defined($_[0])) {<br />
        print(&#8220;Hello, World
&#8221;);<br />
    } else {<br />
        print($_[0], &#8220;
&#8221;);<br />
    }<br />
}<br />
##end sub message</p>
<p> A closing side comment was added for <tt>&quot;sub message&quot;</tt> in this case, but not for the <tt>&quot;if&quot;</tt> and <tt>&quot;else&quot;</tt> blocks, because they were below the 6 line cutoff limit for adding closing side comments. This limit may be changed with the <code>-csci</code> command, described below. </p>
<p> The command <code>-dcsc</code> (or <code>&#8211;delete-closing-side-comments</code>) reverses this process and removes these comments. </p>
<p> Several commands are available to modify the behavior of these two basic commands, <code>-csc</code> and <code>-dcsc</code>:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>-csci=n</code>, or <code>&#8211;closing-side-comment-interval=n</code></p>
<dd> where <tt>&quot;n&quot;</tt> is the minimum number of lines that a block must have in order for a closing side comment to be added. The default value is <tt>&quot;n=6&quot;</tt>. To illustrate: </p>
<p>#perltidy &#8211; csci = 2 &#8211; csc<br />
sub message<br />
{<br />
    if (!defined($_[0])) {<br />
        print(&#8220;Hello, World
&#8221;);<br />
    }<br />
    ##end if (!defined($_[0])) else<br />
    {<br />
        print($_[0], &#8220;
&#8221;);<br />
    } ## end else [ if ( !defined( $_[0] ))<br />
}<br />
##end sub message</p>
<p> Now the <tt>&quot;if&quot;</tt> and <tt>&quot;else&quot;</tt> blocks are commented. However, now this has become very cluttered.</p>
<dt><code>-cscp=string</code>, or <code>&#8211;closing-side-comment-prefix=string</code></p>
<dd> where string is the prefix used before the name of the block type. The default prefix, shown above, is <tt>&quot;## end&quot;</tt>. This string will be added to closing side comments, and it will also be used to recognize them in order to update, delete, and format them. Any comment identified as a closing side comment will be placed just a single space to the right of its closing brace.</p>
<dt><code>-cscl=string</code>, or <code>&#8211;closing-side-comment-list-string</code></p>
<dd> where <tt>&quot;string&quot;</tt> is a list of block types to be tagged with closing side comments. By default, all code block types preceded by a keyword or label (such as <tt>&quot;if&quot;</tt>, <tt>&quot;sub&quot;</tt>, and so on) will be tagged. The <code>-cscl</code> command changes the default list to be any selected block types; see &#8220;Specifying Block Types&#8221;. For example, the following command requests that only <tt>&quot;sub&quot;</tt>&#8216;s, labels, <tt>&quot;BEGIN&quot;</tt>, and <tt>&quot;END&quot;</tt> blocks be affected by any <code>-csc</code> or <code>-dcsc</code> operation: </p>
<pre>
   -cscl=&quot;sub : BEGIN END&quot;
</pre>
<dt><code>-csct=n</code>, or <code>&#8211;closing-side-comment-maximum-text=n</code></p>
<dd> The text appended to certain block types, such as an <tt>&quot;if&quot;</tt> block, is whatever lies between the keyword introducing the block, such as <tt>&quot;if&quot;</tt>, and the opening brace. Since this might be too much text for a side comment, there needs to be a limit, and that is the purpose of this parameter. The default value is <tt>&quot;n=20&quot;</tt>, meaning that no additional tokens will be appended to this text after its length reaches 20 characters. Omitted text is indicated with <tt>&quot;...&quot;</tt>. (Tokens, including sub names, are never truncated, however, so actual lengths may exceed this). To illustrate, in the above example, the appended text of the first block is <tt>&quot; ( !defined( $_[0] )...&quot;</tt>. The existing limit of <tt>&quot;n=20&quot;</tt> caused this text to be truncated, as indicated by the <tt>&quot;...&quot;</tt>. See the next flag for additional control of the abbreviated text.</p>
<dt><code>-cscb</code>, or <code>&#8211;closing-side-comments-balanced</code></p>
<dd> As discussed in the previous item, when the closing-side-comment-maximum-text limit is exceeded the comment text must be truncated. Older versions of perltidy terminated with three dots, and this can still be achieved with -ncscb: </p>
<pre>
  perltidy -csc -ncscb
  } ## end foreach my $foo (sort { $b cmp $a ...
</pre>
<p> However this causes a problem with editors editors which cannot recognize comments or are not configured to do so because they cannot &#8220;bounce&#8221; around in the text correctly. The <code>-cscb</code> flag has been added to help them by appending appropriate balancing structure: </p>
<pre>
  perltidy -csc -cscb
  } ## end foreach my $foo (sort { $b cmp $a ... })
</pre>
<p> The default is <code>-cscb</code>.</p>
<dt><code>-csce=n</code>, or <code>&#8211;closing-side-comment-else-flag=n</code></p>
<dd> The default, <code>n=0</code>, places the text of the opening <tt>&quot;if&quot;</tt> statement after any terminal <tt>&quot;else&quot;</tt>. </p>
<p> If <code>n=2</code> is used, then each <tt>&quot;elsif&quot;</tt> is also given the text of the opening <tt>&quot;if&quot;</tt> statement. Also, an <tt>&quot;else&quot;</tt> will include the text of a preceding <tt>&quot;elsif&quot;</tt> statement. Note that this may result some long closing side comments. </p>
<p> If <code>n=1</code> is used, the results will be the same as <code>n=2</code> whenever the resulting line length is less than the maximum allowed. =item <code>-cscb</code>, or <code>&#8211;closing-side-comments-balanced</code> </p>
<p> When using closing-side-comments, and the closing-side-comment-maximum-text limit is exceeded, then the comment text must be abbreviated. It is terminated with three dots if the <code>-cscb</code> flag is negated: </p>
<pre>
  perltidy -csc -ncscb
  } ## end foreach my $foo (sort { $b cmp $a ...
</pre>
<p> This causes a problem with older editors which do not recognize comments because they cannot &#8220;bounce&#8221; around in the text correctly. The <code>-cscb</code> flag tries to help them by appending appropriate terminal balancing structures: </p>
<pre>
  perltidy -csc -cscb
  } ## end foreach my $foo (sort { $b cmp $a ... })
</pre>
<p> The default is <code>-cscb</code>.</p>
<dt><code>-cscw</code>, or <code>&#8211;closing-side-comment-warnings</code></p>
<dd> This parameter is intended to help make the initial transition to the use of closing side comments. It causes two things to happen if a closing side comment replaces an existing, different closing side comment: first, an error message will be issued, and second, the original side comment will be placed alone on a new specially marked comment line for later attention. </p>
<p> The intent is to avoid clobbering existing hand-written side comments which happen to match the pattern of closing side comments. This flag should only be needed on the first run with <code>-csc</code>.</dl>
</dl>
<dl>
<dt>
<dd>
<p> <code>Important Notes on Closing Side Comments:</code></p>
<dl>
<dt>&bull;</p>
<dd> Closing side comments are only placed on lines terminated with a closing brace. Certain closing styles, such as the use of cuddled elses (<code>-ce</code>), preclude the generation of some closing side comments.</p>
<dt>&bull;</p>
<dd> Please note that adding or deleting of closing side comments takes place only through the commands <code>-csc</code> or <code>-dcsc</code>. The other commands, if used, merely modify the behavior of these two commands.</p>
<dt>&bull;</p>
<dd> It is recommended that the <code>-cscw</code> flag be used along with <code>-csc</code> on the first use of perltidy on a given file. This will prevent loss of any existing side comment data which happens to have the csc prefix.</p>
<dt>&bull;</p>
<dd> Once you use <code>-csc</code>, you should continue to use it so that any closing side comments remain correct as code changes. Otherwise, these comments will become incorrect as the code is updated.</p>
<dt>&bull;</p>
<dd> If you edit the closing side comments generated by perltidy, you must also change the prefix to be different from the closing side comment prefix. Otherwise, your edits will be lost when you rerun perltidy with <code>-csc</code>. For example, you could simply change <tt>&quot;## end&quot;</tt> to be <tt>&quot;## End&quot;</tt>, since the test is case sensitive. You may also want to use the <code>-ssc</code> flag to keep these modified closing side comments spaced the same as actual closing side comments.</p>
<dt>&bull;</p>
<dd> Temporarily generating closing side comments is a useful technique for exploring and/or debugging a perl script, especially one written by someone else. You can always remove them with <code>-dcsc</code>.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>Static Block Comments</p>
<dd> Static block comments are block comments with a special leading pattern, <tt>&quot;##&quot;</tt> by default, which will be treated slightly differently from other block comments. They effectively behave as if they had glue along their left and top edges, because they stick to the left edge and previous line when there is no blank spaces in those places. This option is particularly useful for controlling how commented code is displayed.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>-sbc</code>, <code>&#8211;static-block-comments</code></p>
<dd> When <code>-sbc</code> is used, a block comment with a special leading pattern, <tt>&quot;##&quot;</tt> by default, will be treated specially. </p>
<p> Comments so identified are treated as follows:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> If there is no leading space on the line, then the comment will not be indented, and otherwise it may be,</p>
<dt>&bull;</p>
<dd> no new blank line will be inserted before such a comment, and</p>
<dt>&bull;</p>
<dd> such a comment will never become a hanging side comment.</dl>
</dl>
<dl>
<dt>
<dd>
<p> For example, assuming <tt>@month_of_year</tt> is left-adjusted: </p>
<pre>
    @month_of_year = (    # -sbc (default)
        'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct',
    ##  'Dec', 'Nov'
        'Nov', 'Dec');
</pre>
<p> Without this convention, the above code would become </p>
<pre>
    @month_of_year = (   # -nsbc
        'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct',
  
        ##  'Dec', 'Nov'
        'Nov', 'Dec'
    );
</pre>
<p> which is not as clear. The default is to use <code>-sbc</code>. This may be deactivated with <code>-nsbc</code>.</dl>
<dt><code>-sbcp=string</code>, <code>&#8211;static-block-comment-prefix=string</code></p>
<dd> This parameter defines the prefix used to identify static block comments when the <code>-sbc</code> parameter is set. The default prefix is <tt>&quot;##&quot;</tt>, corresponding to <tt>&quot;-sbcp=##&quot;</tt>. The prefix is actually part of a perl pattern used to match lines and it must either begin with <tt>&quot;#&quot;</tt> or <tt>&quot;^#&quot;</tt>. In the first case a prefix ^\s* will be added to match any leading whitespace, while in the second case the pattern will match only comments with no leading whitespace. For example, to identify all comments as static block comments, one would use <tt>&quot;-sbcp=#&quot;</tt>. To identify all left-adjusted comments as static block comments, use <tt>&quot;-sbcp='^#'&quot;</tt>. </p>
<p> Please note that <code>-sbcp</code> merely defines the pattern used to identify static block comments; it will not be used unless the switch <code>-sbc</code> is set. Also, please be aware that since this string is used in a perl regular expression which identifies these comments, it must enable a valid regular expression to be formed. </p>
<p> A pattern which can be useful is: </p>
<p>&#8211; sbcp = ^#{<br />
    2,<br />
}[^\s #]</p>
<p> This pattern requires a static block comment to have at least one character which is neither a # nor a space. It allows a line containing only &#8216;#&#8217; characters to be rejected as a static block comment. Such lines are often used at the start and end of header information in subroutines and should not be separated from the intervening comments, which typically begin with just a single &#8216;#&#8217;.</p>
<dt><code>-osbc</code>, <code>&#8211;outdent-static-block-comments</code></p>
<dd> The command <code>-osbc</code> will will cause static block comments to be outdented by 2 spaces (or whatever <code>-ci=n</code> has been set to), if possible.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>Static Side Comments</p>
<dd> Static side comments are side comments with a special leading pattern. This option can be useful for controlling how commented code is displayed when it is a side comment.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>-ssc</code>, <code>&#8211;static-side-comments</code></p>
<dd> When <code>-ssc</code> is used, a side comment with a static leading pattern, which is <tt>&quot;##&quot;</tt> by default, will be be spaced only a single space from previous character, and it will not be vertically aligned with other side comments. </p>
<p> The default is <code>-nssc</code>.</p>
<dt><code>-sscp=string</code>, <code>&#8211;static-side-comment-prefix=string</code></p>
<dd> This parameter defines the prefix used to identify static side comments when the <code>-ssc</code> parameter is set. The default prefix is <tt>&quot;##&quot;</tt>, corresponding to <tt>&quot;-sscp=##&quot;</tt>. </p>
<p> Please note that <code>-sscp</code> merely defines the pattern used to identify static side comments; it will not be used unless the switch <code>-ssc</code> is set. Also, note that this string is used in a perl regular expression which identifies these comments, so it must enable a valid regular expression to be formed.</dl>
</dl>
<dl>
<dt>
<dd></dl>
</dl>
<h3>Skipping Selected Sections of Code</h3>
<p> Selected lines of code may be passed verbatim to the output without any formatting. This feature is enabled by default but can be disabled with the <code>&#8211;noformat-skipping</code> or <code>-nfs</code> flag. It should be used sparingly to avoid littering code with markers, but it might be helpful for working around occasional problems. For example it might be useful for keeping the indentation of old commented code unchanged, keeping indentation of long blocks of aligned comments unchanged, keeping certain list formatting unchanged, or working around a glitch in perltidy.</p>
<dl>
<dt><code>-fs</code>, <code>&#8211;format-skipping</code></p>
<dd> This flag, which is enabled by default, causes any code between special beginning and ending comment markers to be passed to the output without formatting. The default beginning marker is #&lt;&lt;&lt; and the default ending marker is #&gt;&gt;&gt; but they may be changed (see next items below). Additional text may appear on these special comment lines provided that it is separated from the marker by at least one space. For example </p>
<pre>
 #&lt;&lt;&lt;  do not let perltidy touch this
    my @list = (1,
                1, 1,
                1, 2, 1,
                1, 3, 3, 1,
                1, 4, 6, 4, 1,);
 #&gt;&gt;&gt;
</pre>
<p> The comment markers may be placed at any location that a block comment may appear. If they do not appear to be working, use the -log flag and examine the <i>.LOG</i> file. Use <code>-nfs</code> to disable this feature.</p>
<dt><code>-fsb=string</code>, <code>&#8211;format-skipping-begin=string</code></p>
<dd> The <code>-fsb=string</code> parameter may be used to change the beginning marker for format skipping. The default is equivalent to -fsb=&#8217;#&lt;&lt;&lt;&#8216;. The string that you enter must begin with a # and should be in quotes as necessary to get past the command shell of your system. It is actually the leading text of a pattern that is constructed by appending a &#8216;\s&#8217;, so you must also include backslashes for characters to be taken literally rather than as patterns. </p>
<p> Some examples show how example strings become patterns: </p>
<p>&#8211; fsb = &#8216;#\{\{\{&#8216; becomes / ^#\<br />
{<br />
    \<br />
    {<br />
        \<br />
        {<br />
            \s / which matches #<br />
            {<br />
                {<br />
                    {<br />
                        but not #<br />
                        {<br />
                            {<br />
                                {<br />
                                    {<br />
                                        -fsb = &#8216;#\*\*&#8217; becomes / ^#\*\*\s / which matches #**but not #** *<br />
                                               -fsb = &#8216;#\*{2,}&#8217; becomes / ^#\*<br />
                                        {<br />
                                            2,<br />
                                        }<br />
                                        \s / which matches #**and#*****</p>
<dt><code>-fse=string</code>, <code>&#8211;format-skipping-end=string</code></p>
<dd> The <code>-fsb=string</code> is the corresponding parameter used to change the ending marker for format skipping. The default is equivalent to -fse=&#8217;#&lt;&lt;&lt;&#8216;.</dl>
<h3>Line Break Control</h3>
<p> The parameters in this section control breaks after non-blank lines of code. Blank lines are controlled separately by parameters in the section &#8220;Blank Line Control&#8221;.</p>
<dl>
<dt><code>-fnl</code>, <code>&#8211;freeze-newlines</code></p>
<dd> If you do not want any changes to the line breaks within lines of code in your script, set <code>-fnl</code>, and they will remain fixed, and the rest of the commands in this section and sections &#8220;Controlling List Formatting&#8221;, &#8220;Retaining or Ignoring Existing Line Breaks&#8221;. You may want to use <code>-noll</code> with this. </p>
<p> Note: If you also want to keep your blank lines exactly as they are, you can use the <code>-fbl</code> flag which is described in the section &#8220;Blank Line Control&#8221;.</p>
<dt><code>-ce</code>, <code>&#8211;cuddled-else</code></p>
<dd> Enable the &#8220;cuddled else&#8221; style, in which <tt>&quot;else&quot;</tt> and <tt>&quot;elsif&quot;</tt> are follow immediately after the curly brace closing the previous block. The default is not to use cuddled elses, and is indicated with the flag <code>-nce</code> or <code>&#8211;nocuddled-else</code>. Here is a comparison of the alternatives: </p>
<p>if ($task) {<br />
    yyy();<br />
} else {<br />
#- ce zzz();<br />
}<br />
if ($task) {<br />
    yyy();<br />
} else {<br />
#- nce(default)<br />
        zzz();<br />
}</p>
<dt><code>-bl</code>, <code>&#8211;opening-brace-on-new-line</code></p>
<dd> Use the flag <code>-bl</code> to place the opening brace on a new line: </p>
<p>if ($input_file eq &#8216;-&#8216;)<br />
#- bl<br />
    {<br />
        important_function();<br />
    }</p>
<p> This flag applies to all structural blocks, including named sub&#8217;s (unless the <code>-sbl</code> flag is set &#8212; see next item). </p>
<p> The default style, <code>-nbl</code>, places an opening brace on the same line as the keyword introducing it. For example, </p>
<pre>
  if ( $input_file eq '-' ) {   # -nbl (default)
</pre>
<dt><code>-sbl</code>, <code>&#8211;opening-sub-brace-on-new-line</code></p>
<dd> The flag <code>-sbl</code> can be used to override the value of <code>-bl</code> for the opening braces of named sub&#8217;s. For example, </p>
<pre>
 perltidy -sbl
</pre>
<p> produces this result: </p>
<p>sub message<br />
{<br />
    if (!defined($_[0])) {<br />
        print(&#8220;Hello, World
&#8221;);<br />
    } else {<br />
        print($_[0], &#8220;
&#8221;);<br />
    }<br />
}</p>
<p> This flag is negated with <code>-nsbl</code>. If <code>-sbl</code> is not specified, the value of <code>-bl</code> is used.</p>
<dt><code>-asbl</code>, <code>&#8211;opening-anonymous-sub-brace-on-new-line</code></p>
<dd> The flag <code>-asbl</code> is like the <code>-sbl</code> flag except that it applies to anonymous sub&#8217;s instead of named subs. For example </p>
<pre>
 perltidy -asbl
</pre>
<p> produces this result: </p>
<p>$a = sub<br />
{<br />
    if (!defined($_[0])) {<br />
        print(&#8220;Hello, World
&#8221;);<br />
    } else {<br />
        print($_[0], &#8220;
&#8221;);<br />
    }<br />
};</p>
<p> This flag is negated with <code>-nasbl</code>, and the default is <code>-nasbl</code>.</p>
<dt><code>-bli</code>, <code>&#8211;brace-left-and-indent</code></p>
<dd> The flag <code>-bli</code> is the same as <code>-bl</code> but in addition it causes one unit of continuation indentation ( see <code>-ci</code> ) to be placed before an opening and closing block braces. </p>
<p> For example, </p>
<p>if ($input_file eq &#8216;-&#8216;)<br />
#- bli<br />
    {<br />
        important_function();<br />
    }</p>
<p> By default, this extra indentation occurs for blocks of type: <code>if</code>, <code>elsif</code>, <code>else</code>, <code>unless</code>, <code>for</code>, <code>foreach</code>, <code>sub</code>, <code>while</code>, <code>until</code>, and also with a preceding label. The next item shows how to change this.</p>
<dt><code>-blil=s</code>, <code>&#8211;brace-left-and-indent-list=s</code></p>
<dd> Use this parameter to change the types of block braces for which the <code>-bli</code> flag applies; see &#8220;Specifying Block Types&#8221;. For example, <code>-blil=&#8217;if elsif else&#8217;</code> would apply it to only <tt>&quot;if/elsif/else&quot;</tt> blocks.</p>
<dt><code>-bar</code>, <code>&#8211;opening-brace-always-on-right</code></p>
<dd> The default style, <code>-nbl</code> places the opening code block brace on a new line if it does not fit on the same line as the opening keyword, like this: </p>
<p>if ($bigwasteofspace1 &amp;&amp; $bigwasteofspace2 || $bigwasteofspace3 &amp;&amp; $bigwasteofspace4) {<br />
    big_waste_of_time();<br />
}</p>
<p> To force the opening brace to always be on the right, use the <code>-bar</code> flag. In this case, the above example becomes </p>
<p>if ($bigwasteofspace1 &amp;&amp; $bigwasteofspace2 || $bigwasteofspace3 &amp;&amp; $bigwasteofspace4) {<br />
    big_waste_of_time();<br />
}</p>
<p> A conflict occurs if both <code>-bl</code> and <code>-bar</code> are specified.</p>
<dt><code>-otr</code>, <code>&#8211;opening-token-right</code> and related flags</p>
<dd> The <code>-otr</code> flag is a hint that perltidy should not place a break between a comma and an opening token. For example: </p>
<p>#default formatting<br />
push @{$self-&gt;{$module} {$key}},<br />
    {accno = &gt; $ref-&gt;{accno},<br />
     description = &gt; $ref-&gt;{description}};<br />
#perltidy &#8211; otr<br />
push @{$self-&gt;{$module} {$key}}, {accno = &gt; $ref-&gt;{accno},<br />
                                  description = &gt; $ref-&gt;{description}};</p>
<p> The flag <code>-otr</code> is actually an abbreviation for three other flags which can be used to control parens, hash braces, and square brackets separately if desired: </p>
<pre>
  -opr  or --opening-paren-right
  -ohbr or --opening-hash-brace-right
  -osbr or --opening-square-bracket-right
</pre>
<dt>Vertical tightness of non-block curly braces, parentheses, and square brackets.</p>
<dd> These parameters control what shall be called vertical tightness. Here are the main points:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Opening tokens (except for block braces) are controlled by <code>-vt=n</code>, or <code>&#8211;vertical-tightness=n</code>, where </p>
<pre>
 -vt=0 always break a line after opening token (default). 
 -vt=1 do not break unless this would produce more than one 
         step in indentation in a line.
 -vt=2 never break a line after opening token
</pre>
<dt>&bull;</p>
<dd> You must also use the <code>-lp</code> flag when you use the <code>-vt</code> flag; the reason is explained below.</p>
<dt>&bull;</p>
<dd> Closing tokens (except for block braces) are controlled by <code>-vtc=n</code>, or <code>&#8211;vertical-tightness-closing=n</code>, where </p>
<pre>
 -vtc=0 always break a line before a closing token (default), 
 -vtc=1 do not break before a closing token which is followed 
        by a semicolon or another closing token, and is not in 
        a list environment.
 -vtc=2 never break before a closing token.
</pre>
<p> The rules for <code>-vtc=1</code> are designed to maintain a reasonable balance between tightness and readability in complex lists.</p>
<dt>&bull;</p>
<dd> Different controls may be applied to to different token types, and it is also possible to control block braces; see below.</p>
<dt>&bull;</p>
<dd> Finally, please note that these vertical tightness flags are merely hints to the formatter, and it cannot always follow them. Things which make it difficult or impossible include comments, blank lines, blocks of code within a list, and possibly the lack of the <code>-lp</code> parameter. Also, these flags may be ignored for very small lists (2 or 3 lines in length).</dl>
</dl>
<dl>
<dt>
<dd>
<p> Here are some examples: </p>
<pre>
    # perltidy -lp -vt=0 -vtc=0
    %romanNumerals = (
                       one   =&gt; 'I',
                       two   =&gt; 'II',
                       three =&gt; 'III',
                       four  =&gt; 'IV',
    );
    # perltidy -lp -vt=1 -vtc=0
    %romanNumerals = ( one   =&gt; 'I',
                       two   =&gt; 'II',
                       three =&gt; 'III',
                       four  =&gt; 'IV',
    );
    # perltidy -lp -vt=1 -vtc=1
    %romanNumerals = ( one   =&gt; 'I',
                       two   =&gt; 'II',
                       three =&gt; 'III',
                       four  =&gt; 'IV', );
</pre>
<p> The difference between <code>-vt=1</code> and <code>-vt=2</code> is shown here: </p>
<p>#perltidy &#8211; lp &#8211; vt = 1<br />
$init-&gt;add(<br />
    mysprintf(&#8220;(void)find_threadsv(%s);&#8221;,<br />
              cstring($threadsv_names[$op-&gt;targ])));<br />
#perltidy &#8211; lp &#8211; vt = 2<br />
$init-&gt;add(mysprintf(&#8220;(void)find_threadsv(%s);&#8221;,<br />
                     cstring($threadsv_names[$op-&gt;targ])));</p>
<p> With <code>-vt=1</code>, the line ending in <tt>&quot;add(&quot;</tt> does not combine with the next line because the next line is not balanced. This can help with readability, but <code>-vt=2</code> can be used to ignore this rule. </p>
<p> The tightest, and least readable, code is produced with both <tt>&quot;-vt=2&quot;</tt> and <tt>&quot;-vtc=2&quot;</tt>: </p>
<p>#perltidy &#8211; lp &#8211; vt = 2 &#8211; vtc = 2<br />
$init-&gt;add(mysprintf(&#8220;(void)find_threadsv(%s);&#8221;,<br />
                     cstring($threadsv_names[$op-&gt;targ])));</p>
<p> Notice how the code in all of these examples collapses vertically as <code>-vt</code> increases, but the indentation remains unchanged. This is because perltidy implements the <code>-vt</code> parameter by first formatting as if <code>-vt=0</code>, and then simply overwriting one output line on top of the next, if possible, to achieve the desired vertical tightness. The <code>-lp</code> indentation style has been designed to allow this vertical collapse to occur, which is why it is required for the <code>-vt</code> parameter. </p>
<p> The <code>-vt=n</code> and <code>-vtc=n</code> parameters apply to each type of container token. If desired, vertical tightness controls can be applied independently to each of the closing container token types. </p>
<p> The parameters for controlling parentheses are <code>-pvt=n</code> or <code>&#8211;paren-vertical-tightness=n</code>, and <code>-pcvt=n</code> or <code>&#8211;paren-vertical-tightness-closing=n</code>. </p>
<p> Likewise, the parameters for square brackets are <code>-sbvt=n</code> or <code>&#8211;square-bracket-vertical-tightness=n</code>, and <code>-sbcvt=n</code> or <code>&#8211;square-bracket-vertical-tightness-closing=n</code>. </p>
<p> Finally, the parameters for controlling non-code block braces are <code>-bvt=n</code> or <code>&#8211;brace-vertical-tightness=n</code>, and <code>-bcvt=n</code> or <code>&#8211;brace-vertical-tightness-closing=n</code>. </p>
<p> In fact, the parameter <code>-vt=n</code> is actually just an abbreviation for <code>-pvt=n -bvt=n sbvt=n</code>, and likewise <code>-vtc=n</code> is an abbreviation for <code>-pvtc=n -bvtc=n sbvtc=n</code>.</dl>
<dt><code>-bbvt=n</code> or <code>&#8211;block-brace-vertical-tightness=n</code></p>
<dd> The <code>-bbvt=n</code> flag is just like the <code>-vt=n</code> flag but applies to opening code block braces. </p>
<pre>
 -bbvt=0 break after opening block brace (default). 
 -bbvt=1 do not break unless this would produce more than one 
         step in indentation in a line.
 -bbvt=2 do not break after opening block brace.
</pre>
<p> It is necessary to also use either <code>-bl</code> or <code>-bli</code> for this to work, because, as with other vertical tightness controls, it is implemented by simply overwriting a line ending with an opening block brace with the subsequent line. For example: </p>
<p>#perltidy &#8211; bli &#8211; bbvt = 0<br />
if (open(FILE, &#8220;&lt; $File&#8221;)) {<br />
    while ($File = &lt;FILE&gt;) {<br />
        $In.= $File;<br />
        $count++;<br />
    }<br />
    close(FILE);<br />
}<br />
#perltidy &#8211; bli &#8211; bbvt = 1<br />
if (open(FILE, &#8220;&lt; $File&#8221;)) {<br />
    while ($File = &lt;FILE&gt;) {<br />
        $In.= $File;<br />
        $count++;<br />
    }<br />
    close(FILE);<br />
}</p>
<p> By default this applies to blocks associated with keywords <code>if</code>, <code>elsif</code>, <code>else</code>, <code>unless</code>, <code>for</code>, <code>foreach</code>, <code>sub</code>, <code>while</code>, <code>until</code>, and also with a preceding label. This can be changed with the parameter <code>-bbvtl=string</code>, or <code>&#8211;block-brace-vertical-tightness-list=string</code>, where <code>string</code> is a space-separated list of block types. For more information on the possible values of this string, see &#8220;Specifying Block Types&#8221; </p>
<p> For example, if we want to just apply this style to <tt>&quot;if&quot;</tt>, <tt>&quot;elsif&quot;</tt>, and <tt>&quot;else&quot;</tt> blocks, we could use <tt>&quot;perltidy -bli -bbvt=1 -bbvtl='if elsif else'&quot;</tt>. </p>
<p> There is no vertical tightness control for closing block braces; with one exception they they will be placed on separate lines. The exception is that a cascade of closing block braces may be stacked on a single line. See <code>-scbb</code>.</p>
<dt><code>-sot</code>, <code>&#8211;stack-opening-tokens</code> and related flags</p>
<dd> The <code>-sot</code> flag tells perltidy to &#8220;stack&#8221; opening tokens when possible to avoid lines with isolated opening tokens. </p>
<p> For example: </p>
<p>#default<br />
$opt_c = Text::CSV_XS-&gt;new (<br />
    {<br />
        binary = &gt; 1,<br />
        sep_char = &gt; $opt_c,<br />
        always_quote = &gt; 1,<br />
    });<br />
#- sot<br />
$opt_c = Text::CSV_XS-&gt;new ({<br />
    binary = &gt; 1,<br />
    sep_char = &gt; $opt_c,<br />
    always_quote = &gt; 1,<br />
});</p>
<p> For detailed control of individual closing tokens the following controls can be used: </p>
<p>&#8211; sop or &#8211;stack &#8211; opening &#8211; paren &#8211; sohb or &#8211;stack &#8211; opening &#8211; hash &#8211; brace &#8211; sosb or &#8211;stack &#8211; opening &#8211; square &#8211; bracket &#8211; sobb or &#8211;stack &#8211; opening &#8211; block &#8211; brace</p>
<p> The flag <code>-sot</code> is an abbreviation for <code>-sop -sohb -sosb</code>. </p>
<p> The flag <code>-sobb</code> is a abbreviation for <code>-bbvt=2 -bbvtl=&#8217;*&#8217;</code>. This will case a cascade of opening block braces to appear on a single line, although this an uncommon occurrence except in test scripts.</p>
<dt><code>-sct</code>, <code>&#8211;stack-closing-tokens</code> and related flags</p>
<dd> The <code>-sct</code> flag tells perltidy to &#8220;stack&#8221; closing tokens when possible to avoid lines with isolated closing tokens. </p>
<p> For example: </p>
<p>#default<br />
$opt_c = Text::CSV_XS-&gt;new (<br />
    {<br />
        binary = &gt; 1,<br />
        sep_char = &gt; $opt_c,<br />
        always_quote = &gt; 1,<br />
    });<br />
#- sct<br />
$opt_c = Text::CSV_XS-&gt;new (<br />
    {<br />
        binary = &gt; 1,<br />
        sep_char = &gt; $opt_c,<br />
        always_quote = &gt; 1,<br />
    });</p>
<p> The <code>-sct</code> flag is somewhat similar to the <code>-vtc</code> flags, and in some cases it can give a similar result. The difference is that the <code>-vtc</code> flags try to avoid lines with leading opening tokens by &#8220;hiding&#8221; them at the end of a previous line, whereas the <code>-sct</code> flag merely tries to reduce the number of lines with isolated closing tokens by stacking them but does not try to hide them. For example: </p>
<p>#- vtc = 2<br />
$opt_c = Text::CSV_XS-&gt;new (<br />
    {<br />
        binary = &gt; 1,<br />
        sep_char = &gt; $opt_c,<br />
        always_quote = &gt; 1,<br />
    });</p>
<p> For detailed control of the stacking of individual closing tokens the following controls can be used: </p>
<p>&#8211; scp or &#8211;stack &#8211; closing &#8211; paren &#8211; schb or &#8211;stack &#8211; closing &#8211; hash &#8211; brace &#8211; scsb or &#8211;stack &#8211; closing &#8211; square &#8211; bracket &#8211; scbb or &#8211;stack &#8211; closing &#8211; block &#8211; brace</p>
<p> The flag <code>-sct</code> is an abbreviation for stacking the non-block closing tokens, <code>-scp -schb -scsb</code>. </p>
<p> Stacking of closing block braces, <code>-scbb</code>, causes a cascade of isolated closing block braces to be combined into a single line as in the following example: </p>
<p>#- scbb:<br />
    for<br />
        $w1(@w1)<br />
        {<br />
        for<br />
            $w2(@w2)<br />
            {<br />
            for<br />
                $w3(@w3)<br />
                {<br />
                for<br />
                    $w4(@w4)<br />
                    {<br />
                        push(@lines, &#8220;$w1 $w2 $w3 $w4
&#8221;);<br />
                    }<br />
                }<br />
            }<br />
        }</p>
<p> To simplify input even further for the case in which both opening and closing non-block containers are stacked, the flag <code>-sac</code> or <code>&#8211;stack-all-containers</code> is an abbreviation for <code>-sot -sot</code>.</p>
<dt><code>-dnl</code>, <code>&#8211;delete-old-newlines</code></p>
<dd> By default, perltidy first deletes all old line break locations, and then it looks for good break points to match the desired line length. Use <code>-ndnl</code> or <code>&#8211;nodelete-old-newlines</code> to force perltidy to retain all old line break points.</p>
<dt><code>-anl</code>, <code>&#8211;add-newlines</code></p>
<dd> By default, perltidy will add line breaks when necessary to create continuations of long lines and to improve the script appearance. Use <code>-nanl</code> or <code>&#8211;noadd-newlines</code> to prevent any new line breaks. </p>
<p> This flag does not prevent perltidy from eliminating existing line breaks; see <code>&#8211;freeze-newlines</code> to completely prevent changes to line break points.</p>
<dt>Controlling whether perltidy breaks before or after operators</p>
<dd> Four command line parameters provide some control over whether a line break should be before or after specific token types. Two parameters give detailed control: </p>
<p> <code>-wba=s</code> or <code>&#8211;want-break-after=s</code>, and </p>
<p> <code>-wbb=s</code> or <code>&#8211;want-break-before=s</code>. </p>
<p> These parameters are each followed by a quoted string, <code>s</code>, containing a list of token types (separated only by spaces). No more than one of each of these parameters should be specified, because repeating a command-line parameter always overwrites the previous one before perltidy ever sees it. </p>
<p> By default, perltidy breaks <code>after</code> these token types:<br />
&nbsp;<wbr>&nbsp;<wbr>%&nbsp;<wbr>+&nbsp;<wbr>&#8211;&nbsp;<wbr>*&nbsp;<wbr>/&nbsp;<wbr>x&nbsp;<wbr>!=&nbsp;<wbr>==&nbsp;<wbr>&gt;=&nbsp;<wbr>&lt;=&nbsp;<wbr>=~&nbsp;<wbr>!~&nbsp;<wbr>&lt;&nbsp;<wbr>&gt;&nbsp;<wbr>&nbsp;<wbr>|&nbsp;<wbr>&amp;&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr>**=&nbsp;<wbr>+=&nbsp;<wbr>*=&nbsp;<wbr>&amp;=&nbsp;<wbr>&lt;&lt;=&nbsp;<wbr>&amp;&amp;=&nbsp;<wbr>-=&nbsp;<wbr>/=&nbsp;<wbr>|=&nbsp;<wbr>&gt;&gt;=&nbsp;<wbr>||=&nbsp;<wbr>//=&nbsp;<wbr>.=&nbsp;<wbr>%=&nbsp;<wbr>^=&nbsp;<wbr>x= </p>
<p> And perltidy breaks <code>before</code> these token types by default:<br />
&nbsp;<wbr>&nbsp;<wbr>.&nbsp;<wbr>&lt;&lt;&nbsp;<wbr>&gt;&gt;&nbsp;<wbr>-&gt;&nbsp;<wbr>&amp;&amp;&nbsp;<wbr>||&nbsp;<wbr>// </p>
<p> To illustrate, to cause a break after a concatenation operator, <tt>'.'</tt>, rather than before it, the command line would be </p>
<pre>
  -wba=&quot;.&quot;
</pre>
<p> As another example, the following command would cause a break before math operators <tt>'+'</tt>, <tt>'-'</tt>, <tt>'/'</tt>, and <tt>'*'</tt>: </p>
<pre>
  -wbb=&quot;+ - / *&quot;
</pre>
<p> These commands should work well for most of the token types that perltidy uses (use <code>&#8211;dump-token-types</code> for a list). Also try the <code>-D</code> flag on a short snippet of code and look at the .DEBUG file to see the tokenization. However, for a few token types there may be conflicts with hardwired logic which cause unexpected results. One example is curly braces, which should be controlled with the parameter <code>bl</code> provided for that purpose. </p>
<p> <font SIZE="-1"><code>WARNING</code></font> Be sure to put these tokens in quotes to avoid having them misinterpreted by your command shell. </p>
<p> Two additional parameters are available which, though they provide no further capability, can simplify input are: </p>
<p> <code>-baao</code> or <code>&#8211;break-after-all-operators</code>, </p>
<p> <code>-bbao</code> or <code>&#8211;break-before-all-operators</code>. </p>
<p> The -baao sets the default to be to break after all of the following operators: </p>
<p>% +-* / x != == &gt;= &lt;= = ~!~&lt;&gt; | &amp; = * *= += *= &amp;= &lt;&lt;= &amp;&amp; = -= /= |= &gt;&gt;= || = //= .= %= ^= x=<br />
                                                                               . : ? &amp;&amp; || and or err xor</p>
<p> and the <code>-bbao</code> flag sets the default to break before all of these operators. These can be used to define an initial break preference which can be fine-tuned with the <code>-wba</code> and <code>-wbb</code> flags. For example, to break before all operators except an <code>=</code> one could use &#8211;bbao -wba=&#8217;=&#8217; rather than listing every single perl operator except <code>=</code> on a -wbb flag.</dl>
<h3>Controlling List Formatting</h3>
<p> Perltidy attempts to place comma-separated arrays of values in tables which look good. Its default algorithms usually work well, and they have been improving with each release, but several parameters are available to control list formatting.</p>
<dl>
<dt><code>-boc</code>, <code>&#8211;break-at-old-comma-breakpoints</code></p>
<dd> This flag tells perltidy to try to break at all old commas. This is not the default. Normally, perltidy makes a best guess at list formatting, and seldom uses old comma breakpoints. Usually this works well, but consider: </p>
<pre>
    my @list = (1,
                1, 1,
                1, 2, 1,
                1, 3, 3, 1,
                1, 4, 6, 4, 1,);
</pre>
<p> The default formatting will flatten this down to one line: </p>
<pre>
    # perltidy (default)
    my @list = ( 1, 1, 1, 1, 2, 1, 1, 3, 3, 1, 1, 4, 6, 4, 1, );
</pre>
<p> which hides the structure. Using <code>-boc</code>, plus additional flags to retain the original style, yields </p>
<pre>
    # perltidy -boc -lp -pt=2 -vt=1 -vtc=1
    my @list = (1,
                1, 1,
                1, 2, 1,
                1, 3, 3, 1,
                1, 4, 6, 4, 1,);
</pre>
<p> A disadvantage of this flag is that all tables in the file must already be nicely formatted. For another possibility see the -fs flag in &#8220;Skipping Selected Sections of Code&#8221;.</p>
<dt><code>-mft=n</code>, <code>&#8211;maximum-fields-per-table=n</code></p>
<dd> If the computed number of fields for any table exceeds <code>n</code>, then it will be reduced to <code>n</code>. The default value for <code>n</code> is a large number, 40. While this value should probably be left unchanged as a general rule, it might be used on a small section of code to force a list to have a particular number of fields per line, and then either the <code>-boc</code> flag could be used to retain this formatting, or a single comment could be introduced somewhere to freeze the formatting in future applications of perltidy. </p>
<pre>
    # perltidy -mft=2
    @month_of_year = (    
        'Jan', 'Feb',
        'Mar', 'Apr',
        'May', 'Jun',
        'Jul', 'Aug',
        'Sep', 'Oct',
        'Nov', 'Dec'
    );
</pre>
<dt><code>-cab=n</code>, <code>&#8211;comma-arrow-breakpoints=n</code></p>
<dd> A comma which follows a comma arrow, &#8216;=&gt;&#8217;, is given special consideration. In a long list, it is common to break at all such commas. This parameter can be used to control how perltidy breaks at these commas. (However, it will have no effect if old comma breaks are being forced because <code>-boc</code> is used). The possible values of <code>n</code> are: </p>
<p>n = 0 break at all commas after = &gt;<br />
                                  n = 1 stable : break at all commas after = &gt; if container is open,<br />
                          EXCEPT FOR one &#8211; line containers<br />
                                               n = 2 break at all commas after = &gt;<br />
    , BUT try to form the maximum maximum one &#8211; line container lengths n = 3 do not treat commas after = &gt; specially at all n = 4 break everything : like n = 0 but ALSO break a short container with a = &gt; not followed by a comma when &#8211; vt = 0 is used n = 5 stable : like n = 1 but ALSO break at open one &#8211; line containers when &#8211; vt = 0 is used(default)</p>
<p> For example, given the following single line, perltidy by default will not add any line breaks because it would break the existing one-line container: </p>
<pre>
    bless { B =&gt; $B, Root =&gt; $Root } =&gt; $package;
</pre>
<p> Using <code>-cab=0</code> will force a break after each comma-arrow item: </p>
<pre>
    # perltidy -cab=0:
    bless {
        B    =&gt; $B,
        Root =&gt; $Root
    } =&gt; $package;
</pre>
<p> If perltidy is subsequently run with this container broken, then by default it will break after each &#8216;=&gt;&#8217; because the container is now broken. To reform a one-line container, the parameter <code>-cab=2</code> could be used. </p>
<p> The flag <code>-cab=3</code> can be used to prevent these commas from being treated specially. In this case, an item such as &#8220;01&#8221; =&gt; 31 is treated as a single item in a table. The number of fields in this table will be determined by the same rules that are used for any other table. Here is an example. </p>
<pre>
    # perltidy -cab=3
    my %last_day = (
        &quot;01&quot; =&gt; 31, &quot;02&quot; =&gt; 29, &quot;03&quot; =&gt; 31, &quot;04&quot; =&gt; 30,
        &quot;05&quot; =&gt; 31, &quot;06&quot; =&gt; 30, &quot;07&quot; =&gt; 31, &quot;08&quot; =&gt; 31,
        &quot;09&quot; =&gt; 30, &quot;10&quot; =&gt; 31, &quot;11&quot; =&gt; 30, &quot;12&quot; =&gt; 31
    );
</pre>
</dl>
<h3>Retaining or Ignoring Existing Line Breaks</h3>
<p> Several additional parameters are available for controlling the extent to which line breaks in the input script influence the output script. In most cases, the default parameter values are set so that, if a choice is possible, the output style follows the input style. For example, if a short logical container is broken in the input script, then the default behavior is for it to remain broken in the output script. </p>
<p> Most of the parameters in this section would only be required for a one-time conversion of a script from short container lengths to longer container lengths. The opposite effect, of converting long container lengths to shorter lengths, can be obtained by temporarily using a short maximum line length.</p>
<dl>
<dt><code>-bol</code>, <code>&#8211;break-at-old-logical-breakpoints</code></p>
<dd> By default, if a logical expression is broken at a <tt>&quot;&amp;&amp;&quot;</tt>, <tt>&quot;||&quot;</tt>, <tt>&quot;and&quot;</tt>, or <tt>&quot;or&quot;</tt>, then the container will remain broken. Also, breaks at internal keywords <tt>&quot;if&quot;</tt> and <tt>&quot;unless&quot;</tt> will normally be retained. To prevent this, and thus form longer lines, use <code>-nbol</code>.</p>
<dt><code>-bok</code>, <code>&#8211;break-at-old-keyword-breakpoints</code></p>
<dd> By default, perltidy will retain a breakpoint before keywords which may return lists, such as <tt>&quot;sort&quot;</tt> and &lt;map&gt;. This allows chains of these operators to be displayed one per line. Use <code>-nbok</code> to prevent retaining these breakpoints.</p>
<dt><code>-bot</code>, <code>&#8211;break-at-old-ternary-breakpoints</code></p>
<dd> By default, if a conditional (ternary) operator is broken at a <tt>&quot;:&quot;</tt>, then it will remain broken. To prevent this, and thereby form longer lines, use <code>-nbot</code>.</p>
<dt><code>-boa</code>, <code>&#8211;break-at-old-attribute-breakpoints</code></p>
<dd> By default, if an attribute list is broken at a <tt>&quot;:&quot;</tt> in the source file, then it will remain broken. For example, given the following code, the line breaks at the &#8216;:&#8217;s will be retained: </p>
<pre>
                    my @field
                      : field
                      : <a href="//www.systutorials.com/docs/linux/man/1-Default/">Default</a>(1)
                      : Get('Name' =&gt; 'foo') : Set('Name');
</pre>
<p> If the attributes are on a single line in the source code then they will remain on a single line if possible. </p>
<p> To prevent this, and thereby always form longer lines, use <code>-nboa</code>.</p>
<dt><code>-iob</code>, <code>&#8211;ignore-old-breakpoints</code></p>
<dd> Use this flag to tell perltidy to ignore existing line breaks to the maximum extent possible. This will tend to produce the longest possible containers, regardless of type, which do not exceed the line length limit.</p>
<dt><code>-kis</code>, <code>&#8211;keep-interior-semicolons</code></p>
<dd> Use the <code>-kis</code> flag to prevent breaking at a semicolon if there was no break there in the input file. Normally perltidy places a newline after each semicolon which terminates a statement unless several statements are contained within a one-line brace block. To illustrate, consider the following input lines: </p>
<p>dbmclose(% verb_delim);<br />
undef % verb_delim;<br />
dbmclose(% expanded);<br />
undef % expanded;</p>
<p> The default is to break after each statement, giving </p>
<p>dbmclose(% verb_delim);<br />
undef % verb_delim;<br />
dbmclose(% expanded);<br />
undef % expanded;</p>
<p> With <code>perltidy -kis</code> the multiple statements are retained: </p>
<p>dbmclose(% verb_delim);<br />
undef % verb_delim;<br />
dbmclose(% expanded);<br />
undef % expanded;</p>
<p> The statements are still subject to the specified value of <code>maximum-line-length</code> and will be broken if this maximum is exceeed.</dl>
<h3>Blank Line Control</h3>
<p> Blank lines can improve the readability of a script if they are carefully placed. Perltidy has several commands for controlling the insertion, retention, and removal of blank lines.</p>
<dl>
<dt><code>-fbl</code>, <code>&#8211;freeze-blank-lines</code></p>
<dd> Set <code>-fbl</code> if you want to the blank lines in your script to remain exactly as they are. The rest of the parameters in this section may then be ignored. (Note: setting the <code>-fbl</code> flag is equivalent to setting <code>-mbl=0</code> and <code>-kbl=2</code>).</p>
<dt><code>-bbc</code>, <code>&#8211;blanks-before-comments</code></p>
<dd> A blank line will be introduced before a full-line comment. This is the default. Use <code>-nbbc</code> or <code>&#8211;noblanks-before-comments</code> to prevent such blank lines from being introduced.</p>
<dt><code>-blbs=n</code>, <code>&#8211;blank-lines-before-subs=n</code></p>
<dd> The parameter <code>-blbs=n</code> requests that least <code>n</code> blank lines precede a sub definition which does not follow a comment and which is more than one-line long. The default is &lt;-blbs=1&gt;. <font SIZE="-1"><code>BEGIN</code></font> and <font SIZE="-1"><code>END</code></font> blocks are included. </p>
<p> The requested number of blanks statement will be inserted regardless of of the value of <code>&#8211;maximum-consecutive-blank-lines=n</code> (<code>-mbl=n</code>) with the exception that if <code>-mbl=0</code> then no blanks will be output. </p>
<p> This parameter interacts with the value <code>k</code> of the parameter <code>&#8211;maximum-consecutive-blank-lines=k</code> (<code>-mbl=k</code>) as follows: </p>
<p> 1. If <code>-mbl=0</code> then no blanks will be output. This allows all blanks to be suppressed with a single parameter. Otherwise, </p>
<p> 2. If the number of old blank lines in the script is less than <code>n</code> then additional blanks will be inserted to make the total <code>n</code> regardless of the value of <code>-mbl=k</code>. </p>
<p> 3. If the number of old blank lines in the script equals or exceeds <code>n</code> then this parameter has no effect, however the total will not exceed value specified on the <code>-mbl=k</code> flag.</p>
<dt><code>-blbp=n</code>, <code>&#8211;blank-lines-before-packages=n</code></p>
<dd> The parameter <code>-blbp=n</code> requests that least <code>n</code> blank lines precede a package which does not follow a comment. The default is &lt;-blbp=1&gt;. </p>
<p> This parameter interacts with the value <code>k</code> of the parameter <code>&#8211;maximum-consecutive-blank-lines=k</code> (<code>-mbl=k</code>) in the same way as described for the previous item <code>-blbs=n</code>.</p>
<dt><code>-bbs</code>, <code>&#8211;blanks-before-subs</code></p>
<dd> For compatibility with previous versions, <code>-bbs</code> or <code>&#8211;blanks-before-subs</code> is equivalent to <i>-blbp=1</i> and <i>-blbs=1</i>. </p>
<p> Likewise, <code>-nbbs</code> or <code>&#8211;noblanks-before-subs</code> is equivalent to <i>-blbp=0</i> and <i>-blbs=0</i>.</p>
<dt><code>-bbb</code>, <code>&#8211;blanks-before-blocks</code></p>
<dd> A blank line will be introduced before blocks of coding delimited by <code>for</code>, <code>foreach</code>, <code>while</code>, <code>until</code>, and <code>if</code>, <code>unless</code>, in the following circumstances:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> The block is not preceded by a comment.</p>
<dt>&bull;</p>
<dd> The block is not a one-line block.</p>
<dt>&bull;</p>
<dd> The number of consecutive non-blank lines at the current indentation depth is at least <code>-lbl</code> (see next section).</dl>
</dl>
<dl>
<dt>
<dd>
<p> This is the default. The intention of this option is to introduce some space within dense coding. This is negated with <code>-nbbb</code> or <code>&#8211;noblanks-before-blocks</code>.</dl>
<dt><code>-lbl=n</code> <code>&#8211;long-block-line-count=n</code></p>
<dd> This controls how often perltidy is allowed to add blank lines before certain block types (see previous section). The default is 8. Entering a value of <code>0</code> is equivalent to entering a very large number.</p>
<dt><code>-mbl=n</code> <code>&#8211;maximum-consecutive-blank-lines=n</code></p>
<dd> This parameter specifies the maximum number of consecutive blank lines which will be output within code sections of a script. The default is n=1. If the input file has more than n consecutive blank lines, the number will be reduced to n except as noted above for the <code>-blbp</code> and <code>-blbs</code> parameters. If <code>n=0</code> then no blank lines will be output (unless all old blank lines are retained with the <code>-kbl=2</code> flag of the next section). </p>
<p> This flag obviously does not apply to pod sections, here-documents, and quotes.</p>
<dt><code>-kbl=n</code>, <code>&#8211;keep-old-blank-lines=n</code></p>
<dd> The <code>-kbl=n</code> flag gives you control over how your existing blank lines are treated. </p>
<p> The possible values of <code>n</code> are: </p>
<pre>
 n=0 ignore all old blank lines
 n=1 stable: keep old blanks, but limited by the value of the B&lt;-mbl=n&gt; flag
 n=2 keep all old blank lines, regardless of the value of the B&lt;-mbl=n&gt; flag
</pre>
<p> The default is <code>n=1</code>.</p>
<dt><code>-sob</code>, <code>&#8211;swallow-optional-blank-lines</code></p>
<dd> This is equivalent to <code>kbl=0</code> and is included for compatibility with previous versions.</p>
<dt><code>-nsob</code>, <code>&#8211;noswallow-optional-blank-lines</code></p>
<dd> This is equivalent to <code>kbl=1</code> and is included for compatibility with previous versions.</dl>
<h3>Styles</h3>
<p> A style refers to a convenient collection of existing parameters.</p>
<dl>
<dt><code>-gnu</code>, <code>&#8211;gnu-style</code></p>
<dd> <code>-gnu</code> gives an approximation to the <font SIZE="-1">GNU</font> Coding Standards (which do not apply to perl) as they are sometimes implemented. At present, this style overrides the default style with the following parameters: </p>
<pre>
    -lp -bl -noll -pt=2 -bt=2 -sbt=2 -icp
</pre>
<dt><code>-pbp</code>, <code>&#8211;perl-best-practices</code></p>
<dd> <code>-pbp</code> is an abbreviation for the parameters in the book <code>Perl Best Practices</code> by Damian Conway: </p>
<p>&#8211; l = 78 &#8211; i = 4 &#8211; ci = 4 &#8211; st &#8211; se &#8211; vt = 2 &#8211; cti = 0 &#8211; pt = 1 &#8211; bt = 1 &#8211; sbt = 1 &#8211; bbt = 1 &#8211; nsfs &#8211; nolq &#8211; wbb = &#8220;% + &#8211; * / x != == &gt;= &lt;= =~ !~ &lt; &gt; | &amp; =<br />
                                                                                               * *= += *= &amp;= &lt;&lt;= &amp;&amp; = -= /= |= &gt;&gt;= ||<br />
    = //= .= %= ^= x=&#8221;</p>
<p> Please note that this parameter set includes -st and -se flags, which make perltidy act as a filter on one file only. These can be overridden by placing <code>-nst</code> and/or <code>-nse</code> after the -pbp parameter. </p>
<p> Also note that the value of continuation indentation, -ci=4, is equal to the value of the full indentation, -i=4. In some complex statements perltidy will produce nicer results with -ci=2. This can be implemented by including -ci=2 after the -pbp parameter. For example, </p>
<p>#perltidy &#8211; pbp<br />
$self-&gt;{_text} = (!$section         ? &#8221;<br />
                  : $type eq &#8216;item&#8217; ? &#8220;the $section entry&#8221;<br />
                                    : &#8220;the section on $section&#8221;)<br />
                     .(<br />
                         $page<br />
                             ? ($section ? &#8216; in &#8216; : &#8221; ).&#8221;the $page$page_ext manpage&#8221;<br />
                             : &#8216; elsewhere in this document&#8217;);<br />
#perltidy &#8211; pbp &#8211; ci = 2<br />
$self-&gt;{_text} = (!$section         ? &#8221;<br />
                  : $type eq &#8216;item&#8217; ? &#8220;the $section entry&#8221;<br />
                                    : &#8220;the section on $section&#8221;)<br />
                     .(<br />
                         $page<br />
                             ? ($section ? &#8216; in &#8216; : &#8221; ).&#8221;the $page$page_ext manpage&#8221;<br />
                             : &#8216; elsewhere in this document&#8217;);
</dl>
<h3>Other Controls</h3>
<dl>
<dt>Deleting selected text</p>
<dd> Perltidy can selectively delete comments and/or pod documentation. The command <code>-dac</code> or <code>&#8211;delete-all-comments</code> will delete all comments <code>and</code> all pod documentation, leaving just code and any leading system control lines. </p>
<p> The command <code>-dp</code> or <code>&#8211;delete-pod</code> will remove all pod documentation (but not comments). </p>
<p> Two commands which remove comments (but not pod) are: <code>-dbc</code> or <code>&#8211;delete-block-comments</code> and <code>-dsc</code> or <code>&#8211;delete-side-comments</code>. (Hanging side comments will be deleted with block comments here.) </p>
<p> The negatives of these commands also work, and are the defaults. When block comments are deleted, any leading &#8216;hash-bang&#8217; will be retained. Also, if the <code>-x</code> flag is used, any system commands before a leading hash-bang will be retained (even if they are in the form of comments).</p>
<dt>Writing selected text to a file</p>
<dd> When perltidy writes a formatted text file, it has the ability to also send selected text to a file with a <i>.TEE</i> extension. This text can include comments and pod documentation. </p>
<p> The command <code>-tac</code> or <code>&#8211;tee-all-comments</code> will write all comments <code>and</code> all pod documentation. </p>
<p> The command <code>-tp</code> or <code>&#8211;tee-pod</code> will write all pod documentation (but not comments). </p>
<p> The commands which write comments (but not pod) are: <code>-tbc</code> or <code>&#8211;tee-block-comments</code> and <code>-tsc</code> or <code>&#8211;tee-side-comments</code>. (Hanging side comments will be written with block comments here.) </p>
<p> The negatives of these commands also work, and are the defaults.</p>
<dt>Using a <i>.perltidyrc</i> command file</p>
<dd> If you use perltidy frequently, you probably won&#8217;t be happy until you create a <i>.perltidyrc</i> file to avoid typing commonly-used parameters. Perltidy will first look in your current directory for a command file named <i>.perltidyrc</i>. If it does not find one, it will continue looking for one in other standard locations. </p>
<p> These other locations are system-dependent, and may be displayed with the command <tt>&quot;perltidy -dpro&quot;</tt>. Under Unix systems, it will first look for an environment variable <font SIZE="-1"><code>PERLTIDY</code></font>. Then it will look for a <i>.perltidyrc</i> file in the home directory, and then for a system-wide file <i>/usr/local/etc/perltidyrc</i>, and then it will look for <i>/etc/perltidyrc</i>. Note that these last two system-wide files do not have a leading dot. Further system-dependent information will be found in the <font SIZE="-1">INSTALL</font> file distributed with perltidy. </p>
<p> Under Windows, perltidy will also search for a configuration file named perltidy.ini since Windows does not allow files with a leading period (.). Use <tt>&quot;perltidy -dpro&quot;</tt> to see the possbile locations for your system. An example might be <i>C:\Documents and Settings\All Users\perltidy.ini</i>. </p>
<p> Another option is the use of the <font SIZE="-1">PERLTIDY</font> environment variable. The method for setting environment variables depends upon the version of Windows that you are using. Instructions for Windows 95 and later versions can be found here: </p>
<p> <a rel="nofollow" href="http://www.netmanage.com/000/20021101_005_tcm21-6336.pdf">http://www.netmanage.com/000/20021101_005_tcm21-6336.pdf</a> </p>
<p> Under Windows <font SIZE="-1">NT / 2000 / XP</font> the <font SIZE="-1">PERLTIDY</font> environment variable can be placed in either the user section or the system section. The later makes the configuration file common to all users on the machine. Be sure to enter the full path of the configuration file in the value of the environment variable. Ex. PERLTIDY=C:\Documents and Settings\perltidy.ini </p>
<p> The configuation file is free format, and simply a list of parameters, just as they would be entered on a command line. Any number of lines may be used, with any number of parameters per line, although it may be easiest to read with one parameter per line. Comment text begins with a #, and there must also be a space before the # for side comments. It is a good idea to put complex parameters in either single or double quotes. </p>
<p> Here is an example of a <i>.perltidyrc</i> file: </p>
<pre>
  # This is a simple of a .perltidyrc configuration file
  # This implements a highly spaced style
  -se    # errors to standard error output
  -w     # show all warnings
  -bl    # braces on new lines
  -pt=0  # parens not tight at all
  -bt=0  # braces not tight
  -sbt=0 # square brackets not tight
</pre>
<p> The parameters in the <i>.perltidyrc</i> file are installed first, so any parameters given on the command line will have priority over them. </p>
<p> To avoid confusion, perltidy ignores any command in the .perltidyrc file which would cause some kind of dump and an exit. These are: </p>
<pre>
 -h -v -ddf -dln -dop -dsn -dtt -dwls -dwrs -ss
</pre>
<p> There are several options may be helpful in debugging a <i>.perltidyrc</i> file:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> A very helpful command is <code>&#8211;dump-profile</code> or <code>-dpro</code>. It writes a list of all configuration filenames tested to standard output, and if a file is found, it dumps the content to standard output before exiting. So, to find out where perltidy looks for its configuration files, and which one if any it selects, just enter </p>
<pre>
  perltidy -dpro
</pre>
<dt>&bull;</p>
<dd> It may be simplest to develop and test configuration files with alternative names, and invoke them with <code>-pro=filename</code> on the command line. Then rename the desired file to <i>.perltidyrc</i> when finished.</p>
<dt>&bull;</p>
<dd> The parameters in the <i>.perltidyrc</i> file can be switched off with the <code>-npro</code> option.</p>
<dt>&bull;</p>
<dd> The commands <code>&#8211;dump-options</code>, <code>&#8211;dump-defaults</code>, <code>&#8211;dump-long-names</code>, and <code>&#8211;dump-short-names</code>, all described below, may all be helpful.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>Creating a new abbreviation</p>
<dd> A special notation is available for use in a <i>.perltidyrc</i> file for creating an abbreviation for a group of options. This can be used to create a shorthand for one or more styles which are frequently, but not always, used. The notation is to group the options within curly braces which are preceded by the name of the alias (without leading dashes), like this: </p>
<pre>
        newword {
        -opt1
        -opt2
        }
</pre>
<p> where <code>newword</code> is the abbreviation, and <code>opt1</code>, etc, are existing parameters <i>or other abbreviations</i>. The main syntax requirement is that the new abbreviation must begin on a new line. Space before and after the curly braces is optional. For a specific example, the following line </p>
<pre>
        airy {-bl -pt=0 -bt=0 -sbt=0}
</pre>
<p> could be placed in a <i>.perltidyrc</i> file, and then invoked at will with </p>
<pre>
        perltidy -airy somefile.pl
</pre>
<p> (Either <tt>&quot;-airy&quot;</tt> or <tt>&quot;--airy&quot;</tt> may be used).</p>
<dt>Skipping leading non-perl commands with <code>-x</code> or <code>&#8211;look-for-hash-bang</code></p>
<dd> If your script has leading lines of system commands or other text which are not valid perl code, and which are separated from the start of the perl code by a &#8220;hash-bang&#8221; line, ( a line of the form <tt>&quot;#!...perl&quot;</tt> ), you must use the <code>-x</code> flag to tell perltidy not to parse and format any lines before the &#8220;hash-bang&#8221; line. This option also invokes perl with a -x flag when checking the syntax. This option was originally added to allow perltidy to parse interactive <font SIZE="-1">VMS</font> scripts, but it should be used for any script which is normally invoked with <tt>&quot;perl -x&quot;</tt>.</p>
<dt>Making a file unreadable</p>
<dd> The goal of perltidy is to improve the readability of files, but there are two commands which have the opposite effect, <code>&#8211;mangle</code> and <code>&#8211;extrude</code>. They are actually merely aliases for combinations of other parameters. Both of these strip all possible whitespace, but leave comments and pod documents, so that they are essentially reversible. The difference between these is that <code>&#8211;mangle</code> puts the fewest possible line breaks in a script while <code>&#8211;extrude</code> puts the maximum possible. Note that these options do not provided any meaningful obfuscation, because perltidy can be used to reformat the files. They were originally developed to help test the tokenization logic of perltidy, but they have other uses. One use for <code>&#8211;mangle</code> is the following: </p>
<pre>
  perltidy --mangle myfile.pl -st | perltidy -o myfile.pl.new
</pre>
<p> This will form the maximum possible number of one-line blocks (see next section), and can sometimes help clean up a badly formatted script. </p>
<p> A similar technique can be used with <code>&#8211;extrude</code> instead of <code>&#8211;mangle</code> to make the minimum number of one-line blocks. </p>
<p> Another use for <code>&#8211;mangle</code> is to combine it with <code>-dac</code> to reduce the file size of a perl script.</p>
<dt>One-line blocks</p>
<dd> There are a few points to note regarding one-line blocks. A one-line block is something like this, </p>
<pre>
        if ($x &gt; 0) { $y = 1 / $x }
</pre>
<p> where the contents within the curly braces is short enough to fit on a single line. </p>
<p> With few exceptions, perltidy retains existing one-line blocks, if it is possible within the line-length constraint, but it does not attempt to form new ones. In other words, perltidy will try to follow the one-line block style of the input file. </p>
<p> If an existing one-line block is longer than the maximum line length, however, it will be broken into multiple lines. When this happens, perltidy checks for and adds any optional terminating semicolon (unless the <code>-nasc</code> option is used) if the block is a code block. </p>
<p> The main exception is that perltidy will attempt to form new one-line blocks following the keywords <tt>&quot;map&quot;</tt>, <tt>&quot;eval&quot;</tt>, and <tt>&quot;sort&quot;</tt>, because these code blocks are often small and most clearly displayed in a single line. </p>
<p> One-line block rules can conflict with the cuddled-else option. When the cuddled-else option is used, perltidy retains existing one-line blocks, even if they do not obey cuddled-else formatting. </p>
<p> Occasionally, when one-line blocks get broken because they exceed the available line length, the formatting will violate the requested brace style. If this happens, reformatting the script a second time should correct the problem.</p>
<dt>Debugging</p>
<dd> The following flags are available for debugging: </p>
<p> <code>&#8211;dump-defaults</code> or <code>-ddf</code> will write the default option set to standard output and quit </p>
<p> <code>&#8211;dump-profile</code> or <code>-dpro</code> will write the name of the current configuration file and its contents to standard output and quit. </p>
<p> <code>&#8211;dump-options</code> or <code>-dop</code> will write current option set to standard output and quit. </p>
<p> <code>&#8211;dump-long-names</code> or <code>-dln</code> will write all command line long names (passed to Get_options) to standard output and quit. </p>
<p> <code>&#8211;dump-short-names</code> or <code>-dsn</code> will write all command line short names to standard output and quit. </p>
<p> <code>&#8211;dump-token-types</code> or <code>-dtt</code> will write a list of all token types to standard output and quit. </p>
<p> <code>&#8211;dump-want-left-space</code> or <code>-dwls</code> will write the hash <tt>%want_left_space</tt> to standard output and quit. See the section on controlling whitespace around tokens. </p>
<p> <code>&#8211;dump-want-right-space</code> or <code>-dwrs</code> will write the hash <tt>%want_right_space</tt> to standard output and quit. See the section on controlling whitespace around tokens. </p>
<p> <code>&#8211;no-memoize</code> or <code>-nmem</code> will turn of memoizing. Memoization can reduce run time when running perltidy repeatedly in a single process. It is on by default but can be deactivated for testing with <code>-nmem</code>. </p>
<p> <code>-DEBUG</code> will write a file with extension <i>.DEBUG</i> for each input file showing the tokenization of all lines of code.</p>
<dt>Working with MakeMaker, AutoLoader and SelfLoader</p>
<dd> The first <tt>$VERSION</tt> line of a file which might be eval&#8217;d by MakeMaker is passed through unchanged except for indentation. Use <code>&#8211;nopass-version-line</code>, or <code>-npvl</code>, to deactivate this feature. </p>
<p> If the AutoLoader module is used, perltidy will continue formatting code after seeing an __END__ line. Use <code>&#8211;nolook-for-autoloader</code>, or <code>-nlal</code>, to deactivate this feature. </p>
<p> Likewise, if the SelfLoader module is used, perltidy will continue formatting code after seeing a __DATA__ line. Use <code>&#8211;nolook-for-selfloader</code>, or <code>-nlsl</code>, to deactivate this feature.</p>
<dt>Working around problems with older version of Perl</p>
<dd> Perltidy contains a number of rules which help avoid known subtleties and problems with older versions of perl, and these rules always take priority over whatever formatting flags have been set. For example, perltidy will usually avoid starting a new line with a bareword, because this might cause problems if <tt>&quot;use strict&quot;</tt> is active. </p>
<p> There is no way to override these rules.</dl>
<h2>HTML OPTIONS</h2>
<dl>
<dt>The <code>-html</code> master switch</p>
<dd> The flag <code>-html</code> causes perltidy to write an html file with extension <i>.html</i>. So, for example, the following command </p>
<pre>
        perltidy -html somefile.pl
</pre>
<p> will produce a syntax-colored html file named <i>somefile.pl.html</i> which may be viewed with a browser. </p>
<p> <code>Please Note</code>: In this case, perltidy does not do any formatting to the input file, and it does not write a formatted file with extension <i>.tdy</i>. This means that two perltidy runs are required to create a fully reformatted, html copy of a script.</p>
<dt>The <code>-pre</code> flag for code snippets</p>
<dd> When the <code>-pre</code> flag is given, only the pre-formatted section, within the &lt;<font SIZE="-1">PRE</font>&gt; and &lt;/PRE&gt; tags, will be output. This simplifies inclusion of the output in other files. The default is to output a complete web page.</p>
<dt>The <code>-nnn</code> flag for line numbering</p>
<dd> When the <code>-nnn</code> flag is given, the output lines will be numbered.</p>
<dt>The <code>-toc</code>, or <code>&#8211;html-table-of-contents</code> flag</p>
<dd> By default, a table of contents to packages and subroutines will be written at the start of html output. Use <code>-ntoc</code> to prevent this. This might be useful, for example, for a pod document which contains a number of unrelated code snippets. This flag only influences the code table of contents; it has no effect on any table of contents produced by pod2html (see next item).</p>
<dt>The <code>-pod</code>, or <code>&#8211;pod2html</code> flag</p>
<dd> There are two options for formatting pod documentation. The default is to pass the pod through the Pod::Html module (which forms the basis of the pod2html utility). Any code sections are formatted by perltidy, and the results then merged. Note: perltidy creates a temporary file when Pod::Html is used; see &#8220;<font SIZE="-1">FILES&#8221;</font>. Also, Pod::Html creates temporary files for its cache. </p>
<p> <font SIZE="-1">NOTE:</font> Perltidy counts the number of <tt>&quot;=cut&quot;</tt> lines, and either moves the pod text to the top of the html file if there is one <tt>&quot;=cut&quot;</tt>, or leaves the pod text in its original order (interleaved with code) otherwise. </p>
<p> Most of the flags accepted by pod2html may be included in the perltidy command line, and they will be passed to pod2html. In some cases, the flags have a prefix <tt>&quot;pod&quot;</tt> to emphasize that they are for the pod2html, and this prefix will be removed before they are passed to pod2html. The flags which have the additional <tt>&quot;pod&quot;</tt> prefix are: </p>
<p>&#8211;[no] podheader&#8211;[no] podindex&#8211;[no] podrecurse&#8211;[no] podquiet&#8211;[no] podverbose&#8211; podflush</p>
<p> The flags which are unchanged from their use in pod2html are: </p>
<p>&#8211;backlink = s&#8211; cachedir = s&#8211; htmlroot = s&#8211; libpods = s&#8211; title = s&#8211; podpath = s&#8211; podroot = s</p>
<p> where &#8216;s&#8217; is an appropriate character string. Not all of these flags are available in older versions of Pod::Html. See your Pod::Html documentation for more information. </p>
<p> The alternative, indicated with <code>-npod</code>, is not to use Pod::Html, but rather to format pod text in italics (or whatever the stylesheet indicates), without special html markup. This is useful, for example, if pod is being used as an alternative way to write comments.</p>
<dt>The <code>-frm</code>, or <code>&#8211;frames</code> flag</p>
<dd> By default, a single html output file is produced. This can be changed with the <code>-frm</code> option, which creates a frame holding a table of contents in the left panel and the source code in the right side. This simplifies code browsing. Assume, for example, that the input file is <i>MyModule.pm</i>. Then, for default file extension choices, these three files will be created: </p>
<pre>
 MyModule.pm.html      - the frame
 MyModule.pm.toc.html  - the table of contents
 MyModule.pm.src.html  - the formatted source code
</pre>
<p> Obviously this file naming scheme requires that output be directed to a real file (as opposed to, say, standard output). If this is not the case, or if the file extension is unknown, the <code>-frm</code> option will be ignored.</p>
<dt>The <code>-text=s</code>, or <code>&#8211;html-toc-extension</code> flag</p>
<dd> Use this flag to specify the extra file extension of the table of contents file when html frames are used. The default is &#8220;toc&#8221;. See &#8220;Specifying File Extensions&#8221;.</p>
<dt>The <code>-sext=s</code>, or <code>&#8211;html-src-extension</code> flag</p>
<dd> Use this flag to specify the extra file extension of the content file when html frames are used. The default is &#8220;src&#8221;. See &#8220;Specifying File Extensions&#8221;.</p>
<dt>The <code>-hent</code>, or <code>&#8211;html-entities</code> flag</p>
<dd> This flag controls the use of Html::Entities for html formatting. By default, the module Html::Entities is used to encode special symbols. This may not be the right thing for some browser/language combinations. Use &#8211;nohtml-entities or -nhent to prevent this.</p>
<dt>Style Sheets</p>
<dd> Style sheets make it very convenient to control and adjust the appearance of html pages. The default behavior is to write a page of html with an embedded style sheet. </p>
<p> An alternative to an embedded style sheet is to create a page with a link to an external style sheet. This is indicated with the <code>-css=filename</code>, where the external style sheet is <i>filename</i>. The external style sheet <i>filename</i> will be created if and only if it does not exist. This option is useful for controlling multiple pages from a single style sheet. </p>
<p> To cause perltidy to write a style sheet to standard output and exit, use the <code>-ss</code>, or <code>&#8211;stylesheet</code>, flag. This is useful if the style sheet could not be written for some reason, such as if the <code>-pre</code> flag was used. Thus, for example, </p>
<pre>
  perltidy -html -ss &gt;mystyle.css
</pre>
<p> will write a style sheet with the default properties to file <i>mystyle.css</i>. </p>
<p> The use of style sheets is encouraged, but a web page without a style sheets can be created with the flag <code>-nss</code>. Use this option if you must to be sure that older browsers (roughly speaking, versions prior to 4.0 of Netscape Navigator and Internet Explorer) can display the syntax-coloring of the html files.</p>
<dt>Controlling <font SIZE="-1">HTML</font> properties</p>
<dd> Note: It is usually more convenient to accept the default properties and then edit the stylesheet which is produced. However, this section shows how to control the properties with flags to perltidy. </p>
<p> Syntax colors may be changed from their default values by flags of the either the long form, <code>-html-color-xxxxxx=n</code>, or more conveniently the short form, <code>-hcx=n</code>, where <code>xxxxxx</code> is one of the following words, and <code>x</code> is the corresponding abbreviation: </p>
<pre><code>
Token Type xxxxxx x-- -- -- -- -- -- -- -- -- --comment comment c
    number numeric n
        identifier identifier i
            bareword,
    function bareword w
        keyword keyword k
            quite,
    pattern quote q
            here doc text here -
        doc - text h here doc target here - doc - target hh punctuation punctuation pu parentheses paren p structural braces structure s semicolon semicolon sc colon colon co comma comma cm label label j sub definition name subroutine m pod text pod - text pd
</code></pre>
<p> A default set of colors has been defined, but they may be changed by providing values to any of the following parameters, where <code>n</code> is either a 6 digit hex <font SIZE="-1">RGB</font> color value or an ascii name for a color, such as &#8216;red&#8217;. </p>
<p> To illustrate, the following command will produce an html file <i>somefile.pl.html</i> with &#8220;aqua&#8221; keywords: </p>
<pre>
        perltidy -html -hck=00ffff somefile.pl
</pre>
<p> and this should be equivalent for most browsers: </p>
<pre>
        perltidy -html -hck=aqua somefile.pl
</pre>
<p> Perltidy merely writes any non-hex names that it sees in the html file. The following 16 color names are defined in the <font SIZE="-1">HTML 3.2</font> standard: </p>
<pre>
        black   =&gt; 000000,
        silver  =&gt; c0c0c0,
        gray    =&gt; 808080,
        white   =&gt; ffffff,
        maroon  =&gt; 800000,
        red     =&gt; ff0000,
        purple  =&gt; 800080,
        fuchsia =&gt; ff00ff,
        green   =&gt; 008000,
        lime    =&gt; 00ff00,
        olive   =&gt; 808000,
        yellow  =&gt; ffff00
        navy    =&gt; 000080,
        blue    =&gt; 0000ff,
        teal    =&gt; 008080,
        aqua    =&gt; 00ffff,
</pre>
<p> Many more names are supported in specific browsers, but it is safest to use the hex codes for other colors. Helpful color tables can be located with an internet search for &#8220;<font SIZE="-1">HTML</font> color tables&#8221;. </p>
<p> Besides color, two other character attributes may be set: bold, and italics. To set a token type to use bold, use the flag <code>&#8211;html-bold-xxxxxx</code> or <code>-hbx</code>, where <code>xxxxxx</code> or <code>x</code> are the long or short names from the above table. Conversely, to set a token type to <font SIZE="-1">NOT</font> use bold, use <code>&#8211;nohtml-bold-xxxxxx</code> or <code>-nhbx</code>. </p>
<p> Likewise, to set a token type to use an italic font, use the flag <code>&#8211;html-italic-xxxxxx</code> or <code>-hix</code>, where again <code>xxxxxx</code> or <code>x</code> are the long or short names from the above table. And to set a token type to <font SIZE="-1">NOT</font> use italics, use <code>&#8211;nohtml-italic-xxxxxx</code> or <code>-nhix</code>. </p>
<p> For example, to use bold braces and lime color, non-bold, italics keywords the following command would be used: </p>
<pre>
        perltidy -html -hbs -hck=00FF00 -nhbk -hik somefile.pl
</pre>
<p> The background color can be specified with <code>&#8211;html-color-background=n</code>, or <code>-hcbg=n</code> for short, where n is a 6 character hex <font SIZE="-1">RGB</font> value. The default color of text is the value given to <code>punctuation</code>, which is black as a default. </p>
<p> Here are some notes and hints: </p>
<p> 1. If you find a preferred set of these parameters, you may want to create a <i>.perltidyrc</i> file containing them. See the perltidy man page for an explanation. </p>
<p> 2. Rather than specifying values for these parameters, it is probably easier to accept the defaults and then edit a style sheet. The style sheet contains comments which should make this easy. </p>
<p> 3. The syntax-colored html files can be very large, so it may be best to split large files into smaller pieces to improve download times.</dl>
<h2>SOME COMMON INPUT CONVENTIONS</h2>
<h3>Specifying Block Types</h3>
<p> Several parameters which refer to code block types may be customized by also specifying an associated list of block types. The type of a block is the name of the keyword which introduces that block, such as <code>if</code>, <code>else</code>, or <code>sub</code>. An exception is a labeled block, which has no keyword, and should be specified with just a colon. To specify all blocks use <code>&#8216;*&#8217;</code>. </p>
<p> For example, the following parameter specifies <tt>&quot;sub&quot;</tt>, labels, <tt>&quot;BEGIN&quot;</tt>, and <tt>&quot;END&quot;</tt> blocks: </p>
<pre>
   -cscl=&quot;sub : BEGIN END&quot;
</pre>
<p> (the meaning of the -cscl parameter is described above.) Note that quotes are required around the list of block types because of the spaces. For another example, the following list specifies all block types for vertical tightness: </p>
<pre>
   -bbvtl='*'
</pre>
<h3>Specifying File Extensions</h3>
<p> Several parameters allow default file extensions to be overridden. For example, a backup file extension may be specified with <code>-bext=ext</code>, where <code>ext</code> is some new extension. In order to provides the user some flexibility, the following convention is used in all cases to decide if a leading &#8216;.&#8217; should be used. If the extension <tt>&quot;ext&quot;</tt> begins with <tt>&quot;A-Z&quot;</tt>, <tt>&quot;a-z&quot;</tt>, or <tt>&quot;0-9&quot;</tt>, then it will be appended to the filename with an intermediate &#8216;.&#8217; (or perhaps an &#8216;_&#8217; on <font SIZE="-1">VMS</font> systems). Otherwise, it will be appended directly. </p>
<p> For example, suppose the file is <i>somefile.pl</i>. For <tt>&quot;-bext=old&quot;</tt>, a &#8216;.&#8217; is added to give <i>somefile.pl.old</i>. For <tt>&quot;-bext=.old&quot;</tt>, no additional &#8216;.&#8217; is added, so again the backup file is <i>somefile.pl.old</i>. For <tt>&quot;-bext=~&quot;</tt>, then no dot is added, and the backup file will be <i>somefile.pl~</i> .</p>
<h2>SWITCHES WHICH MAY BE NEGATED</h2>
<p> The following list shows all short parameter names which allow a prefix &#8216;n&#8217; to produce the negated form: </p>
<pre>
 D    anl asc  aws  b    bbb bbc bbs  bl   bli  boc bok  bol  bot  ce
 csc  dac dbc  dcsc ddf  dln dnl dop  dp   dpro dsc dsm  dsn  dtt  dwls
 dwrs dws f    fll  frm  fs  hsc html ibc  icb  icp iob  isbc lal  log
 lp   lsl ohbr okw  ola  oll opr opt  osbr otr  ple ple  pod  pvl  q
 sbc  sbl schb scp  scsb sct se  sfp  sfs  skp  sob sohb sop  sosb sot
 ssc  st  sts  syn  t    tac tbc toc  tp   tqw  tsc w    x    bar  kis
</pre>
<p> Equivalently, the prefix &#8216;no&#8217; or &#8216;no-&#8216; on the corresponding long names may be used.</p>
<h2>LIMITATIONS</h2>
<dl>
<dt>Parsing Limitations</p>
<dd> Perltidy should work properly on most perl scripts. It does a lot of self-checking, but still, it is possible that an error could be introduced and go undetected. Therefore, it is essential to make careful backups and to test reformatted scripts. </p>
<p> The main current limitation is that perltidy does not scan modules included with &#8216;use&#8217; statements. This makes it necessary to guess the context of any bare words introduced by such modules. Perltidy has good guessing algorithms, but they are not infallible. When it must guess, it leaves a message in the log file. </p>
<p> If you encounter a bug, please report it.</p>
<dt>What perltidy does not parse and format</p>
<dd> Perltidy indents but does not reformat comments and <tt>&quot;qw&quot;</tt> quotes. Perltidy does not in any way modify the contents of here documents or quoted text, even if they contain source code. (You could, however, reformat them separately). Perltidy does not format &#8216;format&#8217; sections in any way. And, of course, it does not modify pod documents.</dl>
<h2>FILES</h2>
<dl>
<dt>Temporary files</p>
<dd> Under the -html option with the default &#8211;pod2html flag, a temporary file is required to pass text to Pod::Html. Unix systems will try to use the <font SIZE="-1">POSIX</font> <i>tmpnam()</i> function. Otherwise the file <i>perltidy.TMP</i> will be temporarily created in the current working directory.</p>
<dt>Special files when standard input is used</p>
<dd> When standard input is used, the log file, if saved, is <i>perltidy.LOG</i>, and any errors are written to <i>perltidy.ERR</i> unless the <code>-se</code> flag is set. These are saved in the current working directory.</p>
<dt>Files overwritten</p>
<dd> The following file extensions are used by perltidy, and files with these extensions may be overwritten or deleted: <i>.ERR</i>, <i>.LOG</i>, <i>.TEE</i>, and/or <i>.tdy</i>, <i>.html</i>, and <i>.bak</i>, depending on the run type and settings.</p>
<dt>Files extensions limitations</p>
<dd> Perltidy does not operate on files for which the run could produce a file with a duplicated file extension. These extensions include <i>.LOG</i>, <i>.ERR</i>, <i>.TEE</i>, and perhaps <i>.tdy</i> and <i>.bak</i>, depending on the run type. The purpose of this rule is to prevent generating confusing filenames such as <i>somefile.tdy.tdy.tdy</i>.</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-perlstyle/">perlstyle</a></i>(1), <i><a href="/docs/linux/man/3-perl--tidy/">Perl::Tidy</a></i>(3)</p>
<h2>VERSION</h2>
<p> This man page documents perltidy version 20121207.</p>
<h2>CREDITS</h2>
<p> Michael Cartmell supplied code for adaptation to <font SIZE="-1">VMS</font> and helped with v-strings. </p>
<p> Yves Orton supplied code for adaptation to the various versions of Windows. </p>
<p> Axel Rose supplied a patch for MacPerl. </p>
<p> Hugh S. Myers designed and implemented the initial Perl::Tidy module interface. </p>
<p> Many others have supplied key ideas, suggestions, and bug reports; see the <font SIZE="-1">CHANGES</font> file.</p>
<h2>AUTHOR</h2>
<pre>
  Steve Hancock
  email: perltidy at users.sourceforge.net
  <a rel="nofollow" href="http://perltidy.sourceforge.net">http://perltidy.sourceforge.net</a>
</pre>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2000-2012 by Steve Hancock</p>
<h2>LICENSE</h2>
<p> This package is free software; you can redistribute it and/or modify it under the terms of the &#8220;<font SIZE="-1">GNU</font> General Public License&#8221;. </p>
<p> Please refer to the file &#8220;<font SIZE="-1">COPYING&#8221;</font> for details.</p>
<h2>DISCLAIMER</h2>
<p> This package is distributed in the hope that it will be useful, but <font SIZE="-1">WITHOUT ANY WARRANTY</font>; without even the implied warranty of <font SIZE="-1">MERCHANTABILITY</font> or <font SIZE="-1">FITNESS FOR A PARTICULAR PURPOSE.</font> </p>
<p> See the &#8220;<font SIZE="-1">GNU</font> General Public License&#8221; for more details. </p>
<h2>Index</h2>
