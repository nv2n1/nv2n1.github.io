---

title: "detex(1)"
name: "detex"
section: "1"
letter: "d"
url: "/docs/linux/man/1-detex/"
description: "detex – a filter to strip TeX commands from a .tex file."
---

<p> detex &#8211; a filter to strip <i>TeX</i> commands from a .tex file. </p>
<p> <code>detex</code> [ <code>-clnstw</code> ] [ <code>-e</code><i> environment-list</i> ] [ <i>filename</i>[.tex] &#8230; ]</p>
<p> <i>Detex</i> reads each file in sequence, removes all comments and <i>TeX</i> control sequences and writes the remainder on the standard output. All text in math mode and display mode is removed. By default, <i>detex</i> follows \input commands. If a file cannot be opened, a warning message is printed and the command is ignored. If the <code>-n</code> option is used, no \input or \include commands will be processed. This allows single file processing. If no input file is given on the command line, <i>detex</i> reads from standard input. </p>
<p> If the magic sequence &#8220;egin{document}&#8221; appears in the text, <i>detex</i> assumes it is dealing with <i>LaTeX</i> source and <i>detex</i> recognizes additional constructs used in <i>LaTeX</i>. These include the \include and \includeonly commands. The <code>-l</code> option can be used to force <i>LaTeX</i> mode and the <code>-t</code> option can be used to force <i>TeX</i> mode regardless of input content. </p>
<p> Text in various environment modes of <i>LaTeX</i> is ignored. The default modes are array, eqnarray, equation, longtable, picture, tabular and verbatim. The <code>-e</code> option can be used to specify a comma separated <i>environment-list</i> of environments to ignore. The list replaces the defaults so specifying an empty list effectively causes no environments to be ignored. </p>
<p> The <code>-c</code> option can be used in <i>LaTeX</i> mode to have detex echo the arguments to \cite, \ref, and \pageref macros. This can be useful when sending the output to a style checker. </p>
<p> <i>Detex</i> assumes the standard character classes are being used for <i>TeX</i>. <i>Detex</i> allows white space between control sequences and magic characters like `{&#8216; when recognizing things like <i>LaTeX</i> environments. </p>
<p> The <code>-r</code> option tries to naively replace $..$, $$..$$, \(..\) and \[..\] with nouns and verbs (in particular, &quot;noun&quot; and &quot;verbs&quot;) in a way that keeps sentences readable. </p>
<p> If the <code>-w</code> flag is given, the output is a word list, one `word&#8217; (string of two or more letters and apostrophes beginning with a letter) per line, and all other characters ignored. Without <code>-w</code> the output follows the original, with the deletions mentioned above. Newline characters are preserved where possible so that the lines of output match the input as closely as possible. </p>
<p> The <code>-1</code> option will prefix each printed line with `filename:linenumber:` indicating where that line is coming from in terms of the original (La)TeX document. </p>
<p> The TEXINPUTS environment variable is used to find \input and \include files. Like <i>TeX</i>, it interprets a leading or trailing `:&#8216; as the default TEXINPUTS. It does <i>not</i> support the `//&#8216; directory expansion magic sequence. </p>
<p> Detex now handles the basic <i>TeX</i> ligatures as a special case, replacing the ligatures with acceptable charater substitutes. This eliminates spelling errors introduced by merely removing them. The ligatures are \aa, \ae, \oe, \ss, \o, \l (and their upper-case equivalents). The special &quot;dotless&quot; characters \i and \j are also replaced with i and j respectively. </p>
<p> Note that previous versions of <i>detex</i> would replace control sequences with a space character to prevent words from running together. However, this caused accents in the middle of words to break words, generating &quot;spelling errors&quot; that were not desirable. Therefore, the new version merely removes these accents. The old functionality can be essentially duplicated by using the <code>-s</code> option.  </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-tex/">tex</a>(1)  </p>
<h2>DIAGNOSTICS</h2>
<p> Nesting of \input is allowed but the number of opened files must not exceed the system&#8217;s limit on the number of simultaneously opened files. <i>Detex</i> ignores unrecognized option characters after printing a warning message.  </p>
<h2>AUTHOR</h2>
<p> Originally written by Daniel Trinkle, Computer Science Department, Purdue University </p>
<p> Maintained by Piotr Kubowicz &lt;<a rel="nofollow" href="https://github.com/pkubowicz/opendetex">https://github.com/pkubowicz/opendetex</a>&gt;.  </p>
<h2>BUGS</h2>
<p> <i>Detex</i> is not a complete <i>TeX</i> interpreter, so it can be confused by some constructs. Most errors result in too much rather than too little output. </p>
<p> Running <i>LaTeX</i> source without a ``\begin{document}&#8216;&#8216; through <i>detex</i> may produce errors. </p>
<p> Suggestions for improvements are (mildly) encouraged. </p>
