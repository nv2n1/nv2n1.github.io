---
title: "texfot(1)"
name: "texfot"
section: "1"
letter: "t"
url: "/docs/linux/man/1-texfot/"
---

<h2 class="name">NAME</h2>
 

 texfot - run TeX, filtering online transcript for interesting messages 

<h2>SYNOPSIS</h2>

 texfot [<i>option</i>]... <i>texcmd</i> [<i>texarg</i>...]

<h2>DESCRIPTION</h2>

 <tt>&quot;texfot&quot;</tt> invokes <i>texcmd</i> with the given <i>texarg</i> arguments, filtering the online output for ``interesting'' messages. Its exit value is that of <i>texcmd</i>. Examples: 

 <pre>
  # Sample basic invocation:
  texfot pdflatex file.tex
  
  # Ordinarily all output is copied to /tmp/fot before filtering,
  # but that can be omitted:
  texfot --tee=/dev/null lualatex file.tex
  
  # Example of more complex engine invocation:
  texfot xelatex --recorder '\nonstopmode\input file'
</pre> 

 Aside from its own options, described below, <tt>&quot;texfot&quot;</tt> just runs the given command with the given arguments (same approach to command line syntax as <tt>&quot;env&quot;</tt>, <tt>&quot;nice&quot;</tt>, <tt>&quot;time&quot;</tt>, <tt>&quot;timeout&quot;</tt>, etc.). Thus, <tt>&quot;texfot&quot;</tt> works with any engine and any command line options. 

 <tt>&quot;texfot&quot;</tt> does not look at the log file or any other possible output file(s); it only looks at the standard output and standard error from the command. stdout is processed first, then stderr. Lines from stderr have an identifying prefix. <tt>&quot;texfot&quot;</tt> writes all accepted lines to its stdout. 

 The messages shown are intended to be those which likely need action by the author: error messages, overfull and underfull boxes, undefined citations, missing characters from fonts, etc.

<h2>FLOW OF OPERATION</h2>

 Here is the order in which lines of output are checked:
<dl>
<dt>1.
<dd> If the ``next line'' needs to be printed (see below), print it.
<dt>2.
<dd> Otherwise, if the line matches the built-in list of regexps to ignore, or any user-supplied list of regexps to ignore (given with <tt>&quot;--ignore&quot;</tt>, see below), in that order, ignore it.
<dt>3.
<dd> Otherwise, if the line matches the list of regexps for which the next line (two lines in all) should be shown, show this line and set the ``next line'' flag for the next time around the loop. Examples are the common <tt>&quot;!&quot;</tt> and <tt>&quot;filename:lineno:&quot;</tt> error messages, which are generally followed by a line with specific detail about the error.
<dt>4.
<dd> Otherwise, if the line matches the list of regexps to show, show it.
<dt>5.
<dd> Otherwise, the default: if the line came from stdout, ignore it; if the line came from stderr, print it (to stdout). This distinction is made because TeX engines write relatively few messages to stderr, and it's likely that any such should be considered. 

 It would be easy to add more options to allow for user additions to the various regex lists, if that ever seems useful. Or email me (see end).</dl>
 

 Once a particular check matches, the program moves on to process the next line. 

 Don't hesitate to peruse the source to the script, which is essentially a straightforward loop matching against the different lists as above. You can see the exact regexps being matched in the different categories in the source. 

 Incidentally, although nothing in this basic operation is specific to TeX engines, all the regular expressions included in the program are specific to TeX. So in practice the program isn't useful except with TeX engines, although it would be easy enough to adapt it (if there was anything else as verbose as TeX to make that useful).

<h2>OPTIONS</h2>

 The following are the options to <tt>&quot;texfot&quot;</tt> itself (not the TeX engine being invoked; consult the TeX documentation or the engine's <tt>&quot;--help&quot;</tt> output for that). 

 The first non-option terminates <tt>&quot;texfot&quot;</tt>'s option parsing, and the remainder of the command line is invoked as the TeX command, without further parsing. For example, <tt>&quot;texfot --debug tex --debug&quot;</tt> will output debugging information from both <tt>&quot;texfot&quot;</tt> and <tt>&quot;tex&quot;</tt>. 

 Options may start with either - or --, and may be unambiguously abbreviated. It is best to use the full option name in scripts, though, to avoid possible collisions with new options in the future.
<dl>
<dt>&quot;--debug&quot;
<dd>
<dt>&quot;--no-debug&quot;
<dd> Output (or not) what is being done on standard error. Off by default.
<dt>&quot;--ignore&quot; <i>regexp</i>
<dd> Ignore lines in the TeX output matching (Perl) <i>regexp</i>. Can be repeated. Adds to the default set of ignore regexps rather than replacing. These regexps are not automatically anchored (or otherwise altered), simply used as-is.
<dt>&quot;--interactive&quot;
<dd>
<dt>&quot;--no-interactive&quot;
<dd> By default, standard input to the TeX process is closed so that TeX's interactive mode (waiting for input upon error, the <tt>&quot;*&quot;</tt> prompt, etc.) is never entered. Giving <tt>&quot;--interactive&quot;</tt> allows interaction to happen.
<dt>&quot;--quiet&quot;
<dd>
<dt>&quot;--no-quiet&quot;
<dd> By default, the TeX command being invoked is reported on standard output. <tt>&quot;--quiet&quot;</tt> omits that reporting. To get a completely silent run, redirect standard output: <tt>&quot;texfot ...&nbsp;&gt;/dev/null&quot;</tt>. (The only messages to standard error should be errors from <tt>&quot;texfot&quot;</tt> itself, so it shouldn't be necessary to redirect that, but of course that can be done as well.)
<dt>&quot;--stderr&quot;
<dd>
<dt>&quot;--no-stderr&quot;
<dd> The default is for <tt>&quot;texfot&quot;</tt> to report everything written to stderr by the TeX command (on stdout). <tt>&quot;--no-stderr&quot;</tt> omits that reporting. (Some programs, <tt>&quot;dvisvgm&quot;</tt> is one, can be rather verbose on stderr.)
<dt>&quot;--tee&quot; <i>file</i>
<dd> By default, the output being filtered is <tt>&quot;tee&quot;</tt>-ed, before filtering, to <tt>&quot;$TMPDIR/fot&quot;</tt> (or <tt>&quot;$TMP/fot&quot;</tt> if <tt>&quot;TMP&quot;</tt> is set, or <tt>&quot;/tmp/fot&quot;</tt> if neither environment variable is set), to make it easy to check the full output when the filtering seems suspect. This option allows specifying a different file. Use <tt>&quot;--tee&nbsp;/dev/null&quot;</tt> if you don't want the original output at all.
<dt>&quot;--version&quot;
<dd> Output version information and exit successfully.
<dt>&quot;--help&quot;
<dd> Display this help and exit successfully.</dl>

<h2>RATIONALE</h2>

 I wrote this because, in my work as a TUGboat editor (&lt;<a rel="nofollow" HREF="https://tug.org/TUGboat">https://tug.org/TUGboat</a>&gt;, journal submissions always welcome!), I run and rerun many documents, many times each. It was too easy to lose warnings I needed to see in the mass of unvarying and uninteresting output from TeX, such as style files being read and fonts being used. I wanted to see all and only those messages which needed some action by me. 

 I found some other programs of a similar nature, the LaTeX package <tt>&quot;silence&quot;</tt>, and plenty of other (La)TeX wrappers, but it seemed none of them did what I wanted. Either they read the log file (I wanted the online output only), or they output more or less than I wanted, or they required invoking TeX differently (I wanted to keep my build process exactly the same, most critically the TeX invocation, which can get complicated). Hence I wrote this. 

 Here are some keywords if you want to explore other options: texloganalyser, pydflatex, logfilter, latexmk, rubber, arara, and searching for <tt>&quot;log&quot;</tt> at &lt;<a rel="nofollow" HREF="https://ctan.org/search">https://ctan.org/search</a>&gt;. 

 <tt>&quot;texfot&quot;</tt> is written in Perl, and runs on Unix. It may work on Windows if Perl and other software is installed, but I don't use Windows and don't support C,texfot&gt; there. 

 The name comes from the <tt>&quot;trip.fot&quot;</tt> and <tt>&quot;trap.fot&quot;</tt> files that are part of Knuth's trip and trap torture tests, which record the online output from the programs. I am not sure what ``fot'' stands for in trip and trap, but I can pretend that it stands for ``filter online transcript'' in the present case :).

<h2>AUTHORS AND COPYRIGHT</h2>

 This script and its documentation were written by Karl Berry and both are released to the public domain. Email <tt>&quot;karl [at] freefriends.org&quot;</tt> with bug reports. It has no home page beyond the package on <font SIZE="-1">CTAN:</font> &lt;<a rel="nofollow" HREF="https://ctan.org/pkg/texfot">https://ctan.org/pkg/texfot</a>&gt;. 

<h2>Index</h2>


