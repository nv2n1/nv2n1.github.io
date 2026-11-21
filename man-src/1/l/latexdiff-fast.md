---

title: "latexdiff-fast(1)"
name: "latexdiff-fast"
section: "1"
letter: "l"
url: "/docs/linux/man/1-latexdiff-fast/"
description: "latexdiff – determine and markup differences between two latex files"
---

<p> <code>latexdiff</code> [ <font SIZE="-1"><code>OPTIONS</code></font> ] <i>old.tex</i> <i>new.tex</i> &gt; <i>diff.tex</i></p>
<p> Briefly, <i>latexdiff</i> is a utility program to aid in the management of revisions of latex documents. It compares two valid latex files, here called <tt>&quot;old.tex&quot;</tt> and <tt>&quot;new.tex&quot;</tt>, finds significant differences between them (i.e., ignoring the number of white spaces and position of line breaks), and adds special commands to highlight the differences. Where visual highlighting is not possible, e.g. for changes in the formatting, the differences are nevertheless marked up in the source. Note that old.tex and new.tex need to be real files (not pipes or similar) as they are opened twice (unless <tt>&quot;--encoding&quot;</tt> option is used) </p>
<p> The program treats the preamble differently from the main document. Differences between the preambles are found using line-based differencing (similarly to the Unix diff command, but ignoring white spaces). A comment, &quot;<tt>&quot;%DIF&nbsp;&gt;&quot;</tt>&quot; is appended to each added line, i.e. a line present in <tt>&quot;new.tex&quot;</tt> but not in <tt>&quot;old.tex&quot;</tt>. Discarded lines<br />
&nbsp;are deactivated by prepending&nbsp;&quot;<tt>&quot;%DIF&nbsp;&lt;&quot;</tt>&quot;. Changed blocks are preceded&nbsp;<wbr>&nbsp;by comment lines giving information about line numbers in the original files. Where there are insignificant differences, the resulting file <tt>&quot;diff.tex&quot;</tt> will be similar to <tt>&quot;new.tex&quot;</tt>. At the end of the preamble, the definitions for <i>latexdiff</i> markup commands are inserted. In differencing the main body of the text, <i>latexdiff</i> attempts to satisfy the following guidelines (in order of priority):</p>
<dl>
<dt>1.</dt>
<dd> If both <tt>&quot;old.tex&quot;</tt> and <tt>&quot;new.tex&quot;</tt> are valid LaTeX, then the resulting <tt>&quot;diff.tex&quot;</tt> should also be valid LateX. (<font SIZE="-1">NB</font> If a few plain TeX commands are used within <tt>&quot;old.tex&quot;</tt> or <tt>&quot;new.tex&quot;</tt> then <tt>&quot;diff.tex&quot;</tt> is not guaranteed to work but usually will).</dd>
<dt>2.</dt>
<dd> Significant differences are determined on the level of individual words. All significant differences, including differences between comments should be clearly marked in the resulting source code <tt>&quot;diff.tex&quot;</tt>.</dd>
<dt>3.</dt>
<dd> If a changed passage contains text or text-producing commands, then running <tt>&quot;diff.tex&quot;</tt> through LateX should produce output where added and discarded passages are highlighted.</dd>
<dt>4.</dt>
<dd> Where there are insignificant differences, e.g. in the positioning of line breaks, <tt>&quot;diff.tex&quot;</tt> should follow the formatting of <tt>&quot;new.tex&quot;</tt></dd></dl>
<p> For differencing the same algorithm as <i>diff</i> is used but words instead of lines are compared. An attempt is made to recognize blocks which are completely changed such that they can be marked up as a unit. Comments are differenced line by line but the number of spaces within comments is ignored. Commands including all their arguments are generally compared as one unit, i.e., no mark-up is inserted into the arguments of commands. However, for a selected number of commands (for example, <tt>&quot;</tt>\caption&quot;</code> and all sectioning commands) the last argument is known to be text. This text is split into words and differenced just as ordinary text (use options to show and change the list of text commands, see below). As the algorithm has no detailed knowledge of LaTeX, it assumes all pairs of curly braces immediately following a command (i.e. a sequence of letters beginning with a backslash) are arguments for that command. As a restriction to condition 1 above it is thus necessary to surround all arguments with curly braces, and to not insert extraneous spaces. For example, write </p>
<pre><code>  \section{\textem{This is an emphasized section title}}
</code></pre>
<p> and not </p>
<pre><code>  \section {\textem{This is an emphasized section title}}
</code></pre>
<p> or </p>
<pre><code>  \section\textem{This is an emphasized section title}
</code></pre>
<p> even though all varieties are the same to LaTeX (but see <code>--allow-spaces</code> option which allows the second variety). </p>
<p> For environments whose content does not conform to standard LaTeX or where graphical markup does not make sense all markup commands can be removed by setting the <font SIZE="-1">PICTUREENV</font> configuration variable, set by default to <code>&quot;picture&quot;</code> and <code>&quot;DIFnomarkup&quot;</code> environments; see <code>--config</code> option). The latter environment (<code>&quot;DIFnomarkup&quot;</code>) can be used to protect parts of the latex file where the markup results in illegal markup. You have to surround the offending passage in both the old and new file by <code>&quot;\begin{DIFnomarkup}&quot;</code> and <code>&quot;\end{DIFnomarkup}&quot;</code>. You must define the environment in the preambles of both old and new documents. I prefer to define it as a null-environment, </p>
<p> <code>&quot;\newenvironment{DIFnomarkup}{}{}&quot;</code> </p>
<p> but the choice is yours. Any markup within the environment will be removed, and generally everything within the environment will just be taken from the new file. </p>
<p> It is also possible to difference files which do not have a preamble. <br />
&nbsp;In this case, the file is processed in the main document mode, but the definitions of the markup commands are not inserted. </p>
<p> All markup commands inserted by <i>latexdiff</i> begin with &quot;<code>&quot;\DIF&quot;</code>&quot;. Added blocks containing words, commands or comments which are in <code>&quot;new.tex&quot;</code> but not in <code>&quot;old.tex&quot;</code> are marked by <code>&quot;\DIFaddbegin&quot;</code> and <code>&quot;\DIFaddend&quot;</code>. Discarded blocks are marked by <code>&quot;\DIFdelbegin&quot;</code> and <code>&quot;\DIFdelend&quot;</code>. Within added blocks all text is highlighted with <code>&quot;\DIFadd&quot;</code> like this: <code>&quot;\DIFadd{Added text block}&quot;</code> Selected `safe&#8217; commands can be contained in these text blocks as well (use options to show and change the list of safe commands, see below). All other commands as well as braces ``{&#8216;&#8216; and ``}&#8216;&#8216; are never put within the scope of <code>&quot;\DIFadd&quot;</code>. Added comments are marked by prepending &quot;<code>&quot;%DIF&nbsp;&gt;&nbsp;&quot;</code>&quot;. </p>
<p> Within deleted blocks text is highlighted with <code>&quot;\DIFdel&quot;</code>. Deleted comments are marked by prepending &quot;<code>&quot;%DIF&nbsp;&lt;&nbsp;&quot;</code>``. Non-safe command and curly braces within deleted blocks are commented out with &#8216;&#8216;<code>&quot;%DIFDELCMD&nbsp;&lt;&nbsp;&quot;</code>&quot;.  </p>
<h2>OPTIONS</h2>
<h3>Preamble</h3>
<p> The following options determine the visual markup style by adding the appropriate command definitions to the preamble. See the end of this section for a description of available styles. </p>
<dl>
<dt><code>--type=markupstyle</code> or <code>-t markupstyle</code></dt>
<dd> <p> Add code to preamble for selected markup style. This option defines <code>&quot;\DIFadd&quot;</code> and <code>&quot;\DIFdel&quot;</code> commands. Available styles: </p>
<p> <code>&quot;UNDERLINE CTRADITIONAL TRADITIONAL CFONT FONTSTRIKE INVISIBLE CHANGEBAR CCHANGEBAR CULINECHBAR CFONTCHBAR BOLD PDFCOMMENT&quot;</code> </p>
<p> [ Default: <code>&quot;UNDERLINE&quot;</code> ] </p>
 </dd>
<dt><code>--subtype=markstyle</code> or <code>-s markstyle</code></dt>
<dd> <p> Add code to preamble for selected style for bracketing commands (e.g. to mark changes in margin). This option defines <code>&quot;\DIFaddbegin&quot;</code>, <code>&quot;\DIFaddend&quot;</code>, <code>&quot;\DIFdelbegin&quot;</code> and <code>&quot;\DIFdelend&quot;</code> commands. Available styles: <code>&quot;SAFE MARGIN COLOR DVIPSCOL ZLABEL ONLYCHANGEDPAGE (LABEL)*&quot;</code> </p>
<p> [ Default: <code>&quot;SAFE&quot;</code> ] * Subtype <code>&quot;LABEL&quot;</code> is deprecated </p>
 </dd>
<dt><code>--floattype=markstyle</code> or <code>-f markstyle</code></dt>
<dd> <p> Add code to preamble for selected style which replace standard marking and markup commands within floats (e.g., marginal remarks cause an error within floats so marginal marking can be disabled thus). This option defines all <code>&quot;\DIF...FL&quot;</code> commands. Available styles: <code>&quot;FLOATSAFE TRADITIONALSAFE IDENTICAL&quot;</code> </p>
<p> [ Default: <code>&quot;FLOATSAFE&quot;</code> ] </p>
 </dd>
<dt><code>--encoding=enc</code> or <code>-e enc</code></dt>
<dd> <p> Specify encoding of old.tex and new.tex. Typical encodings are <code>&quot;ascii&quot;</code>, <code>&quot;utf8&quot;</code>, <code>&quot;latin1&quot;</code>, <code>&quot;latin9&quot;</code>. A list of available encodings can be obtained by executing </p>
<p> <code>&quot;perl -MEncode -e &#8216;print join (&quot;\n&quot;,Encode-&quot;</code>encodings( ``:all&#8217;&#8216; )) ;&#8216; &gt; </p>
<p> If this option is used, then old.tex, new.tex are only opened once. [Default encoding is utf8 unless the first few lines of the preamble contain an invocation <code>&quot;\usepackage[..]{inputenc}&quot;</code> in which case the encoding chosen by this command is asssumed. Note that <font SIZE="-1">ASCII</font> (standard latex) is a subset of utf8] </p>
 </dd>
<dt><code>--preamble=file</code> or <code>-p file</code></dt>
<dd> <p> Insert file at end of preamble instead of generating preamble. The preamble must define the following commands <code>&quot;\DIFaddbegin, \DIFaddend, \DIFadd{..}, \DIFdelbegin,\DIFdelend,\DIFdel{..},&quot;</code> and varieties for use within floats <code>&quot;\DIFaddbeginFL, \DIFaddendFL, \DIFaddFL{..}, \DIFdelbeginFL, \DIFdelendFL, \DIFdelFL{..}&quot;</code> (If this option is set <code>-t</code>, <code>-s</code>, and <code>-f</code> options are ignored.) </p>
 </dd>
<dt><code>--packages=pkg1,pkg2,..</code></dt>
<dd> <p> Tell latexdiff that .tex file is processed with the packages in list loaded. This is normally not necessary if the .tex file includes the preamble, as the preamble is automatically scanned for <code>&quot;\usepackage&quot;</code> commands. Use of the <code>--packages</code> option disables automatic scanning, so if for any reason package specific parsing needs to be switched off, use <code>--packages=none</code>. The following packages trigger special behaviour: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt>&quot;amsmath&quot;</dt>
<dd> <p> Configuration variable <font SIZE="-1">MATHARRREPL</font> is set to <code>&quot;align*&quot;</code> (Default: <code>&quot;eqnarray*&quot;</code>). (Note that many of the amsmath array environments are already recognised by default as such) </p>
 </dd>
<dt>&quot;endfloat&quot;</dt>
<dd> <p> Ensure that <code>&quot;\begin{figure}&quot;</code> and <code>&quot;\end{figure}&quot;</code> always appear by themselves on a line. </p>
 </dd>
<dt>&quot;hyperref&quot;</dt>
<dd> <p> Change name of <code>&quot;\DIFadd&quot;</code> and <code>&quot;\DIFdel&quot;</code> commands to <code>&quot;\DIFaddtex&quot;</code> and <code>&quot;\DIFdeltex&quot;</code> and define new <code>&quot;\DIFadd&quot;</code> and <code>&quot;\DIFdel&quot;</code> commands, which provide a wrapper for these commands, using them for the text but not for the link defining command (where any markup would cause errors). </p>
 </dd>
<dt>&quot;apacite&quot;, &quot;biblatex&quot;</dt>
<dd> <p> Redefine the commands recognised as citation commands. </p>
 </dd>
<dt>&quot;siunitx&quot;</dt>
<dd> <p> Treat <code>&quot;\SI&quot;</code> as equivalent to citation commands (i.e. protect with <code>&quot;\mbox&quot;</code> if markup style uses ulem package. </p>
 </dd>
<dt>&quot;cleveref&quot;</dt>
<dd> <p> Treat <code>&quot;\cref,\Cref&quot;</code>, etc as equivalent to citation commands (i.e. protect with <code>&quot;\mbox&quot;</code> if markup style uses ulem package. </p>
 </dd>
<dt>&quot;glossaries&quot;</dt>
<dd> <p> Define most of the glossaries commands as safe, protecting them with \mbox&#8217;es where needed </p>
 </dd>
<dt>&quot;mhchem&quot;</dt>
<dd> <p> Treat <code>&quot;\ce&quot;</code> as a safe command, i.e. it will be highlighted (note that <code>&quot;\cee&quot;</code> will not be highlighted in equations as this leads to processing errors) </p>
 </dd>
<dt>&quot;chemformula&quot; or &quot;chemmacros&quot;</dt>
<dd> <p> Treat <code>&quot;\ch&quot;</code> as a safe command outside equations, i.e. it will be highlighted (note that <code>&quot;\ch&quot;</code> will not be highlighted in equations as this leads to processing errors) </p>
 </dd></dl>
</dl>
<dl>
<dd> <p> [ Default: scan the preamble for <code>&quot;\usepackage&quot;</code> commands to determine <br />
&nbsp;<wbr>&nbsp;loaded packages.&nbsp;] </p>
 </dd></dl>
<dt><code>--show-preamble</code></dt>
<dd> <p> Print generated or included preamble commands to stdout. </p>
 </dd></dl>
<h3>Configuration</h3>
<dl>
<dt><code>--exclude-safecmd=exclude-file</code> or <code>-A exclude-file</code> or <code>--exclude-safecmd=&quot;cmd1,cmd2,...&quot;</code></dt>
<dd>  </dd>
<dt><code>--replace-safecmd=replace-file</code></dt>
<dd>  </dd>
<dt><code>--append-safecmd=append-file</code> or <code>-a append-file</code> or <code>--append-safecmd=&quot;cmd1,cmd2,...&quot;</code></dt>
<dd> <p> Exclude from, replace or append to the list of regular expressions (RegEx) matching commands which are safe to use within the scope of a <code>&quot;\DIFadd&quot;</code> or <code>&quot;\DIFdel&quot;</code> command. The file must contain one Perl-RegEx per line (Comment lines beginning with # or % are ignored). Note that the RegEx needs to match the whole of the token, i.e., /^regex$/ is implied and that the initial ``\&#8216;&#8216; of the command is not included. The <code>--exclude-safecmd</code> and <code>--append-safecmd</code> options can be combined with the -<code>--replace-safecmd</code> option and can be used repeatedly to add cumulatively to the lists. <br />
&nbsp;<code>--exclude-safecmd</code> and <code>--append-safecmd</code> can also take a comma separated list as input. If a comma for one of the regex is required, escape it thus ``\,&#8216;&#8216;. In most cases it will be necessary to protect the comma-separated list from the shell by putting it in quotation marks. </p>
 </dd>
<dt><code>--exclude-textcmd=exclude-file</code> or <code>-X exclude-file</code> or <code>--exclude-textcmd=&quot;cmd1,cmd2,...&quot;</code></dt>
<dd>  </dd>
<dt><code>--replace-textcmd=replace-file</code></dt>
<dd>  </dd>
<dt><code>--append-textcmd=append-file</code> or <code>-x append-file</code> or <code>--append-textcmd=&quot;cmd1,cmd2,...&quot;</code></dt>
<dd> <p> Exclude from, replace or append to the list of regular expressions matching commands whose last argument is text. See entry for <code>--exclude-safecmd</code> directly above for further details. </p>
 </dd>
<dt><code>--replace-context1cmd=replace-file</code></dt>
<dd>  </dd>
<dt><code>--append-context1cmd=append-file</code> or</dt>
<dd>  </dd>
<dt><code>--append-context1cmd=&quot;cmd1,cmd2,...&quot;</code></dt>
<dd> <p> Replace or append to the list of regex matching commands whose last argument is text but which require a particular context to work, e.g. <code>&quot;\caption&quot;</code> will only work within a figure or table. These commands behave like text commands, except when they occur in a deleted section, when they are disabled, but their argument is shown as deleted text. </p>
 </dd>
<dt><code>--replace-context2cmd=replace-file</code></dt>
<dd>  </dd>
<dt><code>--append-context2cmd=append-file</code> or</dt>
<dd>  </dd>
<dt><code>--append-context2cmd=&quot;cmd1,cmd2,...&quot;</code></dt>
<dd> <p> As corresponding commands for context1. The only difference is that context2 commands are completely disabled in deleted sections, including their arguments. </p>
<p> context2 commands are also the only commands in the preamble, whose argument will be processed in word-by-word mode (which only works, if they occur no more than once in the preamble). The algorithm currently cannot cope with repeated context2 commands in the preamble, as they occur e.g. for the <code>&quot;\author&quot;</code> argument in some journal styles (not in the standard styles, though If such a repetition is detected, the whole preamble will be processed in line-by-line mode. In such a case, use <code>&quot;--replace-context2cmd&quot;</code> option to just select the commands, which should be processed and are not used repeatedly in the preamble. </p>
 </dd>
<dt><code>--exclude-mboxsafecmd=exclude-file</code> or <code>--exclude-mboxsafecmd=&quot;cmd1,cmd2,...&quot;</code></dt>
<dd>  </dd>
<dt><code>--append-mboxsafecmd=append-file</code> or <code>--append-mboxsafecmd=&quot;cmd1,cmd2,...&quot;</code></dt>
<dd> <p> Define safe commands, which additionally need to be protected by encapsulating in an <code>&quot;\mbox{..}&quot;</code>. This is sometimes needed to get around incompatibilities between external packages and the ulem package, which is used for highlighting in the default style <font SIZE="-1">UNDERLINE</font> as well as <font SIZE="-1">CULINECHBAR CFONTSTRIKE</font> </p>
 </dd>
<dt><code>--config var1=val1,var2=val2,...</code> or <code>-c var1=val1,..</code></dt>
<dd>  </dd>
<dt><code>-c configfile</code></dt>
<dd> <p> Set configuration variables. The option can be repeated to set different variables (as an alternative to the comma-separated list). Available variables (see below for further explanations): </p>
<p> <code>&quot;ARRENV&quot;</code> (RegEx) </p>
<p> <code>&quot;COUNTERCMD&quot;</code> (RegEx) </p>
<p> <code>&quot;CUSTODIFCMD&quot;</code> (RegEx) </p>
<p> <code>&quot;FLOATENV&quot;</code> (RegEx) </p>
<p> <code>&quot;ITEMCMD&quot;</code> (RegEx) </p>
<p> <code>&quot;LISTENV&quot;</code> (RegEx) </p>
<p> <code>&quot;MATHARRENV&quot;</code> (RegEx) </p>
<p> <code>&quot;MATHARRREPL&quot;</code> (String) </p>
<p> <code>&quot;MATHENV&quot;</code> (RegEx) </p>
<p> <code>&quot;MATHREPL&quot;</code> (String) </p>
<p> <code>&quot;MINWORDSBLOCK&quot;</code> (Integer) </p>
<p> <code>&quot;PICTUREENV&quot;</code> (RegEx) </p>
<p> <code>&quot;SCALEDELGRAPHICS&quot;</code> (Float) </p>
 </dd>
<dt><code>--add-to-config varenv1=pattern1,varenv2=pattern2,...</code></dt>
<dd> <p> For configuration variables, which are a regular expression (essentially those ending in <font SIZE="-1">ENV, COUNTERCMD</font> and <font SIZE="-1">CUSTOMDIFCMD,</font> see list above) this option provides an alternative way to modify the configuration variables. Instead of setting the complete pattern, with this option it is possible to add an alternative pattern. <code>&quot;varenv&quot;</code> must be one of the variables listed above that take a regular expression as argument, and pattern is any regular expression (which might need to be protected from the shell by quotation). Several patterns can be added at once by using semi-colons to separate them, e.g. <code>&quot;--add-to-config &quot;LISTENV=myitemize;myenumerate,COUNTERCMD=endnote&quot;&quot;</code> </p>
 </dd>
<dt><code>--show-safecmd</code></dt>
<dd> <p> Print list of RegEx matching and excluding safe commands. </p>
 </dd>
<dt><code>--show-textcmd</code></dt>
<dd> <p> Print list of RegEx matching and excluding commands with text argument. </p>
 </dd>
<dt><code>--show-config</code></dt>
<dd> <p> Show values of configuration variables. </p>
 </dd>
<dt><code>--show-all</code></dt>
<dd> <p> Combine all --show commands. </p>
<p> <font SIZE="-1">NB</font> For all --show commands, no <code>&quot;old.tex&quot;</code> or <code>&quot;new.tex&quot;</code> file needs to be specified, and no differencing takes place. </p>
 </dd></dl>
<h3>Other configuration options:</h3>
<dl>
<dt><code>--allow-spaces</code></dt>
<dd> <p> Allow spaces between bracketed or braced arguments to commands. Note that this option might have undesirable side effects (unrelated scope might get lumpeded with preceding commands) so should only be used if the default produces erroneous results. (Default requires arguments to directly follow each other without intervening spaces). </p>
 </dd>
<dt><code>--math-markup=level</code></dt>
<dd> <p> Determine granularity of markup in displayed math environments: Possible values for level are (both numerical and text labels are acceptable): </p>
<p> <code>&quot;off&quot;</code> or <code>0</code>: suppress markup for math environments. Deleted equations will not appear in diff file. This mode can be used if all the other modes cause invalid latex code. </p>
<p> <code>&quot;whole&quot;</code> or <code>1</code>: Differencing on the level of whole equations. Even trivial changes to equations cause the whole equation to be marked changed. This mode can be used if processing in coarse or fine mode results in invalid latex code. </p>
<p> <code>&quot;coarse&quot;</code> or <code>2</code>: Detect changes within equations marked up with a coarse granularity; changes in equation type (e.g.displaymath to equation) appear as a change to the complete equation. This mode is recommended for situations where the content and order of some equations are still being changed. [Default] </p>
<p> <code>&quot;fine&quot;</code> or <code>3</code>: Detect small change in equations and mark up at fine granularity. This mode is most suitable, if only minor changes to equations are expected, e.g. correction of typos. </p>
 </dd>
<dt><code>--graphics-markup=level</code></dt>
<dd> <pre><code> Change highlight style for graphics embedded with C&lt;\includegraphics&gt; commands.
</code></pre>
<p> Possible values for level: </p>
<p> <code>&quot;none&quot;</code>, <code>&quot;off&quot;</code> or <code>0</code>: no highlighting for figures </p>
<p> <code>&quot;new-only&quot;</code> or <code>1</code>: surround newly added or changed figures with a blue frame [Default if graphicx package loaded] </p>
<p> <code>&quot;both&quot;</code> or <code>2</code>: highlight new figures with a blue frame and show deleted figures at reduced scale, and crossed out with a red diagonal cross. Use configuration variable <font SIZE="-1">SCALEDELGRAPHICS</font> to set size of deleted figures. </p>
<p> Note that changes to the optional parameters will make the figure appear as changed to latexdiff, and this figure will thus be highlighted </p>
 </dd>
<dt><code>--disable-citation-markup</code> or <code>--disable-auto-mbox</code></dt>
<dd> <p> Suppress citation markup and markup of other vulnerable commands in styles using ulem (<font SIZE="-1">UNDERLINE,FONTSTRIKE, CULINECHBAR</font>) (the two options are identical and are simply aliases) </p>
 </dd>
<dt><code>--enable-citation-markup</code> or <code>--enforce-auto-mbox</code></dt>
<dd> <p> Protect citation commands and other vulnerable commands in changed sections with <code>&quot;\mbox&quot;</code> command, i.e. use default behaviour for ulem package for other packages (the two options are identical and are simply aliases) </p>
 </dd></dl>
<h3>Miscellaneous</h3>
<dl>
<dt><code>--verbose</code> or <code>-V</code></dt>
<dd> <p> Output various status information to stderr during processing. Default is to work silently. </p>
 </dd>
<dt><code>--driver=type</code></dt>
<dd> <p> Choose driver for changebar package (only relevant for styles using <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;changebar:&nbsp;<font SIZE="-1">CCHANGEBAR CFONTCHBAR CULINECHBAR CHANGEBAR</font>). Possible drivers are listed in changebar manual, e.g. pdftex,dvips,dvitops <br />
&nbsp;<wbr>&nbsp;[Default: dvips] </p>
 </dd>
<dt><code>--ignore-warnings</code></dt>
<dd> <p> Suppress warnings about inconsistencies in length between input and parsed strings and missing characters. These warning messages are often related to non-standard latex or latex constructions with a syntax unknown to <code>&quot;latexdiff&quot;</code> but the resulting difference argument is often fully functional anyway, particularly if the non-standard latex only occurs in parts of the text which have not changed. </p>
 </dd>
<dt><code>--label=label</code> or <code>-L label</code></dt>
<dd> <p> Sets the labels used to describe the old and new files. The first use of this option sets the label describing the old file and the second use of the option sets the label for the new file, i.e. set both labels like this <code>&quot;-L labelold -L labelnew&quot;</code>. [Default: use the filename and modification dates for the label] </p>
 </dd>
<dt><code>--no-label</code></dt>
<dd> <p> Suppress inclusion of old and new file names as comment in output file </p>
 </dd>
<dt><code>--visible-label</code></dt>
<dd> <p> Include old and new filenames (or labels set with <code>&quot;--label&quot;</code> option) as visible output. </p>
 </dd>
<dt><code>--flatten</code></dt>
<dd> <p> Replace <code>&quot;\input&quot;</code> and <code>&quot;\include&quot;</code> commands within body by the content of the files in their argument. If <code>&quot;\includeonly&quot;</code> is present in the preamble, only those files are expanded into the document. However, no recursion is done, i.e. <code>&quot;\input&quot;</code> and <code>&quot;\include&quot;</code> commands within included sections are not expanded. The included files are assumed to <br />
&nbsp;be located in the same directories as the old and new master files, respectively, making it possible to organise files into old and new directories. --flatten is applied recursively, so inputted files can contain further <code>&quot;\input&quot;</code> statements. Also handles files included by the import package (<code>&quot;\import&quot;</code> and <code>&quot;\subimport&quot;</code>), and <code>&quot;\subfile&quot;</code> command. </p>
<p> Use of this option might result in prohibitive processing times for larger documents, and the resulting difference document no longer reflects the structure of the input documents. </p>
 </dd>
<dt><code>--filter-script=filterscript</code></dt>
<dd> <p> Run files through this filterscript (full path preferred) before processing. The filterscript must take <font SIZE="-1">STDIN</font> input and output to <font SIZE="-1">STDOUT.</font> When coupled with --flatten, each file will be run through the filter as it is brought in. </p>
 </dd>
<dt><code>--ignore-filter-stderr</code></dt>
<dd> <p> When running with --filter-script, <font SIZE="-1">STDERR</font> from the script may cause readability issues. Turn this flag on to ignore <font SIZE="-1">STDERR</font> from the filter script. </p>
 </dd>
<dt><code>--help</code> or <code>-h</code></dt>
<dd> <p> Show help text </p>
 </dd>
<dt><code>--version</code></dt>
<dd> <p> Show version number </p>
 </dd></dl>
<h3>Internal options</h3>
<p> These options are mostly for automated use by latexdiff-vc. They can be used directly, but the <font SIZE="-1">API</font> should be considered less stable than for the other options. </p>
<dl>
<dt><code>--no-links</code></dt>
<dd> <p> Suppress generation of hyperreferences, used for minimal diffs (option --only-changes of latexdiff-vc) </p>
 </dd></dl>
<h3>Predefined styles</h3>
<h3>Major types</h3>
<p> The major type determine the markup of plain text and some selected latex commands outside floats by defining the markup commands <code>&quot;\DIFadd{...}&quot;</code> and <code>&quot;\DIFdel{...}&quot;</code> . </p>
<dl>
<dt>&quot;UNDERLINE&quot;</dt>
<dd> <p> Added text is wavy-underlined and blue, discarded text is struck out and red (Requires color and ulem packages). Overstriking does not work in displayed math equations such that deleted parts of equation are underlined, not struck out (this is a shortcoming inherent to the ulem package). </p>
 </dd>
<dt>&quot;CTRADITIONAL&quot;</dt>
<dd> <p> Added text is blue and set in sans-serif, and a red footnote is created for each discarded piece of text. (Requires color package) </p>
 </dd>
<dt>&quot;TRADITIONAL&quot;</dt>
<dd> <p> Like <code>&quot;CTRADITIONAL&quot;</code> but without the use of color. </p>
 </dd>
<dt>&quot;CFONT&quot;</dt>
<dd> <p> Added text is blue and set in sans-serif, and discarded text is red and very small size. </p>
 </dd>
<dt>&quot;FONTSTRIKE&quot;</dt>
<dd> <p> Added tex is set in sans-serif, discarded text small and struck out </p>
 </dd>
<dt>&quot;CCHANGEBAR&quot;</dt>
<dd> <p> Added text is blue, and discarded text is red. Additionally, the changed text is marked with a bar in the margin (Requires color and changebar packages). </p>
 </dd>
<dt>&quot;CFONTCHBAR&quot;</dt>
<dd> <p> Like <code>&quot;CFONT&quot;</code> but with additional changebars (Requires color and changebar packages). </p>
 </dd>
<dt>&quot;CULINECHBAR&quot;</dt>
<dd> <p> Like <code>&quot;UNDERLINE&quot;</code> but with additional changebars (Requires color, ulem and changebar packages). </p>
 </dd>
<dt>&quot;CHANGEBAR&quot;</dt>
<dd> <p> No mark up of text, but mark margins with changebars (Requires changebar package). </p>
 </dd>
<dt>&quot;INVISIBLE&quot;</dt>
<dd> <p> No visible markup (but generic markup commands will still be inserted. </p>
 </dd>
<dt>&quot;BOLD&quot;</dt>
<dd> <p> Added text is set in bold face, discarded is not shown. </p>
 </dd>
<dt>&quot;PDFCOMMENT&quot;</dt>
<dd> <p> The pdfcomment package is used to underline new text, and mark deletions with a <font SIZE="-1">PDF</font> comment. Note that this markup might appear differently or not at all based on the pdf viewer used. The viewer with best support for pdf markup is probably acroread. This style is only recommended if the number of differences is small. </p>
 </dd></dl>
<h3>Subtypes</h3>
<p> The subtype defines the commands that are inserted at the begin and end of added or discarded blocks, irrespectively of whether these blocks contain text or commands (Defined commands: <code>&quot;\DIFaddbegin, \DIFaddend, \DIFdelbegin, \DIFdelend&quot;</code>) </p>
<dl>
<dt>&quot;SAFE&quot;</dt>
<dd> <p> No additional markup (Recommended choice) </p>
 </dd>
<dt>&quot;MARGIN&quot;</dt>
<dd> <p> Mark beginning and end of changed blocks with symbols in the margin nearby (using the standard <code>&quot;\marginpar&quot;</code> command &#8211; note that this sometimes moves somewhat from the intended position. </p>
 </dd>
<dt>&quot;COLOR&quot;</dt>
<dd> <p> An alternative way of marking added passages in blue, and deleted ones in red. (It is recommeneded to use instead the main types to effect colored markup, although in some cases coloring with dvipscol can be more complete, for example with citation commands). </p>
 </dd>
<dt>&quot;DVIPSCOL&quot;</dt>
<dd> <p> An alternative way of marking added passages in blue, and deleted ones in red. Note that <code>&quot;DVIPSCOL&quot;</code> only works with the dvips converter, e.g. not pdflatex. (it is recommeneded to use instead the main types to effect colored markup, although in some cases coloring with dvipscol can be more complete). </p>
 </dd>
<dt>&quot;ZLABEL&quot;</dt>
<dd> <p> can be used to highlight only changed pages, but requires post-processing. It is recommend to not call this option manually but use <code>&quot;latexdiff-vc&quot;</code> with <code>&quot;--only-changes&quot;</code> option. Alternatively, use the script given within preamble of diff files made using this style. </p>
 </dd>
<dt>&quot;ONLYCHANGEDPAGE&quot;</dt>
<dd> <p> also highlights changed pages, without the need for post-processing, but might not work reliably if there is floating material (figures, tables). </p>
 </dd>
<dt>&quot;LABEL&quot;</dt>
<dd> <p> is similar to <code>&quot;ZLABEL&quot;</code>, but does not need the zref package and works less reliably (deprecated). </p>
 </dd></dl>
<h3>Float Types</h3>
<p> Some of the markup used in the main text might cause problems when used within floats (e.g. figures or tables). For this reason alternative versions of all markup commands are used within floats. The float type defines these alternative commands. </p>
<dl>
<dt>&quot;FLOATSAFE&quot;</dt>
<dd> <p> Use identical markup for text as in the main body, but set all commands marking the begin and end of changed blocks to null-commands. You have to choose this float type if your subtype is <code>&quot;MARGIN&quot;</code> as <code>&quot;\marginpar&quot;</code> does not work properly within floats. </p>
 </dd>
<dt>&quot;TRADITIONALSAFE&quot;</dt>
<dd> <p> Mark additions the same way as in the main text. Deleted environments are marked by angular brackets \[ and \] and the deleted text is set in scriptscript size. This float type should always be used with the <code>&quot;TRADITIONAL&quot;</code> and <code>&quot;CTRADITIONAL&quot;</code> markup types as the \footnote command does not work properly in floating environments. </p>
 </dd>
<dt>&quot;IDENTICAL&quot;</dt>
<dd> <p> Make no difference between the main text and floats. </p>
 </dd></dl>
<h3>Configuration Variables</h3>
<dl>
<dt>&quot;ARRENV&quot;</dt>
<dd> <p> If a match to <code>&quot;ARRENV&quot;</code> is found within an inline math environment within a deleted or added block, then the inlined math is surrounded by <code>&quot;\mbox{&quot;</code>...<code>&quot;}&quot;</code>. This is necessary as underlining does not work within inlined array environments. </p>
<p> [ Default: <code>&quot;ARRENV&quot;</code>=<code>&quot;(?:array|[pbvBV]matrix)&quot;</code>&nbsp; </p>
 </dd>
<dt>&quot;COUNTERCMD&quot;</dt>
<dd> <p> If a command in a deleted block which is also in the textcmd list matches <code>&quot;COUNTERCMD&quot;</code> then an additional command <code>&quot;\addtocounter{&quot;</code><i>cntcmd</i><code>&quot;}{-1}&quot;</code>, where <i>cntcmd</i> is the matching command, is appended in the diff file such that the numbering in the diff file remains synchronized with the numbering in the new file. </p>
<p> [ Default: <code>&quot;COUNTERCMD&quot;</code>=<code>&quot;(?:footnote|part|section|subsection&quot;</code> ... </p>
<p> <code>&quot;|subsubsection|paragraph|subparagraph)&quot;</code> ] </p>
 </dd>
<dt>&quot;CUSTOMDIFCMD&quot;</dt>
<dd> <p> This option is for advanced users and allows definition of special versions of commands, which do not work as safe commands. </p>
<p> Commands in <code>&quot;CUSTOMDIFCMD&quot;</code> that occur in added or deleted blocks will be given an <font SIZE="-1">ADD</font> or <font SIZE="-1">DEL</font> prefix. The prefixed versions of the command must be defined in the preamble, either by putting them in the preamble of at least the new file, or by creating a custom preamble file (Option --preamble). For example the command <code>&quot;\blindtext&quot;</code> (from package blindtext) does not interact well with underlining, so that for the standard markup type, it is not satisfactory to define it as a safe command. Instead, a customised versions without underlining can be defined in the preamble: </p>
<p> <code>&quot;\newcommand{\DELblindtext}{{\color{red}\blindtext}}&quot;</code> </p>
<p> <code>&quot;\newcommand{\ADDblindtext}{{\color{blue}\blindtext}}&quot;</code> </p>
<p> and then latexdiff should be invoked with the option <code>&quot;-c CUSTOMDIFCMD=blindtext&quot;</code>. </p>
<p> [ Default: none ] </p>
 </dd>
<dt>&quot;FLOATENV&quot;</dt>
<dd> <p> Environments whose name matches the regular expression in <code>&quot;FLOATENV&quot;</code> are considered floats. Within these environments, the <i>latexdiff</i> markup commands are replaced by their <font SIZE="-1">FL</font> variaties. </p>
<p> [ Default: <code>&quot;(?:figure|table|plate)[\w\d*@]*&quot;</code>&nbsp;] </p>
 </dd>
<dt>&quot;ITEMCMD&quot;</dt>
<dd> <p> Commands representing new item line with list environments. </p>
<p> [ Default: \<code>&quot;item&quot;</code> ] </p>
 </dd>
<dt>&quot;LISTENV&quot;</dt>
<dd> <p> Environments whose name matches the regular expression in <code>&quot;LISTENV&quot;</code> are list environments. </p>
<p> [ Default: <code>&quot;(?:itemize|enumerate|description)&quot;</code>&nbsp;] </p>
 </dd>
<dt>&quot;MATHENV&quot;,&quot;MATHREPL&quot;</dt>
<dd> <p> If both \begin and \end for a math environment (environment name matching <code>&quot;MATHENV&quot;</code> or \[ and \]) are within the same deleted block, they are replaced by a \begin and \end commands for <code>&quot;MATHREPL&quot;</code> rather than being commented out. </p>
<p> [ Default: <code>&quot;MATHENV&quot;</code>=<code>&quot;(?:displaymath|equation)&quot;</code>&nbsp;, <code>&quot;MATHREPL&quot;</code>=<code>&quot;displaymath&quot;</code>&nbsp;] </p>
 </dd>
<dt>&quot;MATHARRENV&quot;,&quot;MATHARRREPL&quot;</dt>
<dd> <p> as <code>&quot;MATHENV&quot;</code>,<code>&quot;MATHREPL&quot;</code> but for equation arrays </p>
<p> [ Default: <code>&quot;MATHARRENV&quot;</code>=<code>&quot;eqnarray\*?&quot;</code>&nbsp;, <code>&quot;MATHREPL&quot;</code>=<code>&quot;eqnarray&quot;</code>&nbsp;] </p>
 </dd>
<dt>&quot;MINWORDSBLOCK&quot;</dt>
<dd> <p> Minimum number of tokens required to form an independent block. This value is used in the algorithm to detect changes of complete blocks by merging identical text parts of less than <code>&quot;MINWORDSBLOCK&quot;</code> to the preceding added and discarded parts. </p>
<p> [ Default: 3 ] </p>
 </dd>
<dt>&quot;PICTUREENV&quot;</dt>
<dd> <p> Within environments whose name matches the regular expression in <code>&quot;PICTUREENV&quot;</code> all latexdiff markup is removed (in pathologic cases this might lead to inconsistent markup but this situation should be rare). </p>
<p> [ Default: <code>&quot;(?:picture|DIFnomarkup)[\w\d*@]*&quot;</code>&nbsp;] </p>
 </dd>
<dt>&quot;SCALEDELGRAPHICS&quot;</dt>
<dd> <p> If <code>&quot;--graphics-markup=both&quot;</code> is chosen, <code>&quot;SCALEDELGRAPHICS&quot;</code> is the factor, by which deleted figures will be scaled (i.e. 0.5 implies they are shown at half linear size). </p>
<p> [ Default: 0.5 ] </p>
 </dd>
<dt>&quot;VERBATIMENV&quot;</dt>
<dd> <p> RegEx describing environments like verbatim, whose contents should be taken verbatim. The content of these environments will not be processed in any way: deleted content is commented out, new content is not marked up </p>
<p> [ Default: <code>&quot;comment&quot;</code>&nbsp; ] </p>
 </dd>
<dt>&quot;VERBATIMLINEENV&quot;</dt>
<dd> <p> RegEx describing environments like verbatim, whose contents should be taken verbatim. The content of environments described by <font SIZE="-1">VERBATIMLINEENV</font> are compared in line mode, and changes are marked up using the listings package. The markup style is set based on the chosen mains markup type (Option -t), or on an analysis of the preamble. Note that ``listings.sty&#8217;&#8216; must be installed. If this file is not found the fallback solution is to treat <font SIZE="-1">VERBATIMLINEENV</font> environments treated exactly the same way as <font SIZE="-1">VERBATIMENV</font> environments. </p>
<p> [ Default: <code>&quot;(?:verbatim[*]?|lstlisting&quot;</code>&nbsp; ] </p>
 </dd></dl>
<h2>COMMON PROBLEMS AND FAQ</h2>
<dl>
<dt>Citations result in overfull boxes</dt>
<dd> <p> There is an incompatibility between the <code>&quot;ulem&quot;</code> package, which <code>&quot;latexdiff&quot;</code> uses for underlining and striking out in the <font SIZE="-1">UNDERLINE</font> style, the default style, and the way citations are generated. In order to be able to mark up citations properly, they are enclosed with an <code>&quot;\mbox&quot;</code> command. As mboxes cannot be broken across lines, this procedure frequently results in overfull boxes, possibly obscuring the content as it extends beyond the right margin. The same occurs for some other packages (e.g., siunitx). If this is a problem, you have two possibilities. </p>
<p> 1. Use <code>&quot;CFONT&quot;</code> type markup (option <code>&quot;-t CFONT&quot;</code>): If this markup is chosen, then changed citations are no longer marked up with the wavy line (additions) or struck out (deletions), but are still highlighted in the appropriate color, and deleted text is shown with a different font. Other styles not using the <code>&quot;ulem&quot;</code> package will also work. </p>
<p> 2. Choose option <code>&quot;--disable-citation-markup&quot;</code> which turns off the marking up of citations: deleted citations are no longer shown, and added citations are shown without markup. (This was the default behaviour of latexdiff at versions 0.6 and older) </p>
<p> For custom packages you can define the commands which need to be protected by <code>&quot;\mbox&quot;</code> with <code>&quot;--append-mboxsafecmd&quot;</code> and <code>&quot;--excludemboxsafecmd&quot;</code> options (submit your lists of command as feature request at github page to set the default behaviour of future versions, see section 6) </p>
 </dd>
<dt>Changes in complicated mathematical equations result in latex processing errors</dt>
<dd> <p> Try options <code>&quot;--math-markup=whole&quot;</code>. If even that fails, you can turn off mark up for equations with <code>&quot;--math-markup=off&quot;</code>. </p>
 </dd>
<dt>How can I just show the pages where changes had been made</dt>
<dd> <p> Use options -<code>&quot;-s ZLABEL&quot;</code> (some postprocessing required) or <code>&quot;-s ONLYCHANGEDPAGE&quot;</code>. <code>&quot;latexdiff-vc --ps|--pdf&quot;</code> with <code>&quot;--only-changes&quot;</code> option takes care of the post-processing for you (requires zref package to be installed). </p>
 </dd></dl>
<h2>BUGS</h2>
<dl>
<dt>Option allow-spaces not implemented entirely consistently. It breaks the rules that number and type of white space does not matter, as different numbers of inter-argument spaces are treated as significant.</dt>
<dd>  </dd></dl>
<p> Please submit bug reports using the issue tracker of the github repository page <i><a rel="nofollow" href="https://github.com/ftilmann/latexdiff.git">https://github.com/ftilmann/latexdiff.git</a></i>, or send them to <i>tilmann --- </i><font SIZE="-1"><i>AT</i></font><i> --- gfz-potsdam.de</i>. Include the version number of <i>latexdiff</i> (from comments at the top of the source or use <code>--version</code>). If you come across latex files that are error-free and conform to the specifications set out above, and whose differencing still does not result in error-free latex, please send me those files, ideally edited to only contain the offending passage as long as that still reproduces the problem. If your file relies on non-standard class files, you must include those. I will not look at examples where I have trouble to latex the original files.  </p>
<h2>SEE ALSO</h2>
<p> latexrevise, latexdiff-vc  </p>
<h2>PORTABILITY</h2>
<p> <i>latexdiff</i> does not make use of external commands and thus should run on any platform supporting Perl 5.6 or higher. If files with encodings other than <font SIZE="-1">ASCII</font> or <font SIZE="-1">UTF-8</font> are processed, Perl 5.8 or higher is required. </p>
<p> The standard version of <i>latexdiff</i> requires installation of the Perl package <code>&quot;Algorithm::Diff&quot;</code> (available from <i><a rel="nofollow" href="http://www.cpan.org">www.cpan.org</a></i> &#8211; <i><a rel="nofollow" href="http://search.cpan.org/~nedkonz/Algorithm-Diff-1.15">http://search.cpan.org/~nedkonz/Algorithm-Diff-1.15</a></i>) but a stand-alone version, <i>latexdiff-so</i>, which has this package inlined, is available, too. <i>latexdiff-fast</i> requires the <i>diff</i> command to be present.  </p>
<h2>AUTHOR</h2>
<p> Version 1.3.0 Copyright (C) 2004-2018 Frederik Tilmann </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the <font SIZE="-1">GNU</font> General Public License Version 3 </p>
<p> Contributors of fixes and additions: V. Kuhlmann, J. Paisley, N. Becker, T. Doerges, K. Huebner, T. Connors, Sebastian Gouezel and many others. Thanks to the many people who sent in bug reports, feature suggestions, and other feedback. </p>
