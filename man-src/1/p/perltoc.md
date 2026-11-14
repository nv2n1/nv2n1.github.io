---
title: "perltoc(1)"
name: "perltoc"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perltoc/"
description: "perltoc – perl documentation table of contents"
---

<p>perltoc &#8211; perl documentation table of contents </p>
<h2>Description</h2>
<p>This page provides a brief table of contents for the rest of the Perl documentation set. It is meant to be scanned quickly or grepped through to locate the proper section you&#8217;re looking for.</p>
<h2>Basic Documentation</h2>
<h3>perl &#8211; The Perl 5 language interpreter</h3>
<dl COMPACT>
<dt><font SIZE="-1">SYNOPSIS</font></p>
<dd>
<dt><font SIZE="-1">GETTING HELP</font></p>
<dd>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>Overview</p>
<dd>
<dt>Tutorials</p>
<dd>
<dt>Reference Manual</p>
<dd>
<dt>Internals and C Language Interface</p>
<dd>
<dt>Miscellaneous</p>
<dd>
<dt>Language-Specific</p>
<dd>
<dt>Platform-Specific</p>
<dd>
<dt>Stubs for Deleted Documents</p>
<dd></dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt><font SIZE="-1">DESCRIPTION</font></p>
<dd>
<dt><font SIZE="-1">AVAILABILITY</font></p>
<dd>
<dt><font SIZE="-1">ENVIRONMENT</font></p>
<dd>
<dt><font SIZE="-1">AUTHOR</font></p>
<dd>
<dt><font SIZE="-1">FILES</font></p>
<dd>
<dt><font SIZE="-1">SEE ALSO</font></p>
<dd>
<dt><font SIZE="-1">DIAGNOSTICS</font></p>
<dd>
<dt><font SIZE="-1">BUGS</font></p>
<dd>
<dt><font SIZE="-1">NOTES</font></p>
<dd></dl>
<h3>perlintro &#8212; a brief introduction and overview of Perl</h3>
<dl COMPACT>
<dt><font SIZE="-1">DESCRIPTION</font></p>
<dd>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>What is Perl?</p>
<dd>
<dt>Running Perl programs</p>
<dd>
<dt>Safety net</p>
<dd>
<dt>Basic syntax overview</p>
<dd>
<dt>Perl variable types</p>
<dd>Scalars, Arrays, Hashes</p>
<dt>Variable scoping</p>
<dd>
<dt>Conditional and looping constructs</p>
<dd>if, while, for, foreach</p>
<dt>Builtin operators and functions</p>
<dd>Arithmetic, Numeric comparison, String comparison, Boolean logic, Miscellaneous</p>
<dt>Files and I/O</p>
<dd>
<dt>Regular expressions</p>
<dd>Simple matching, Simple substitution, More complex regular expressions, Parentheses for capturing, Other regexp features</p>
<dt>Writing subroutines</p>
<dd>
<dt><font SIZE="-1">OO</font> Perl</p>
<dd>
<dt>Using Perl modules</p>
<dd></dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt><font SIZE="-1">AUTHOR</font></p>
<dd></dl>
<h3>perlrun &#8211; how to execute the Perl interpreter</h3>
<dl COMPACT>
<dt><font SIZE="-1">SYNOPSIS</font></p>
<dd>
<dt><font SIZE="-1">DESCRIPTION</font></p>
<dd>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>#! and quoting on non-Unix systems</p>
<dd><font SIZE="-1">OS/2,</font> MS-DOS, Win95/NT, <font SIZE="-1">VMS</font></p>
<dt>Location of Perl</p>
<dd>
<dt>Command Switches</p>
<dd><code>-0</code>[<i>octal/hexadecimal</i>] , <code>-a</code> , <code>-C [</code>number/list<code>]</code> , <code>-c</code> , <code>-d</code> , <code>-dt</code>, <code>-d:</code><i>MOD[=bar,baz]</i> , <code>-dt:</code><i>MOD[=bar,baz]</i>, <code>-D</code><i>letters</i> , <code>-D</code><i>number</i>, <code>-e</code> <i>commandline</i> , <code>-E</code> <i>commandline</i> , <code>-f</code><br />
&nbsp;,&nbsp;<code>-F</code><i>pattern</i>&nbsp;,&nbsp;<code>-h</code>&nbsp;, <code>-i</code>[<i>extension</i>] , <code>-I</code><i>directory</i> , <code>-l</code>[<i>octnum</i>] , <code>-m</code>[<code>&#8211;</code>]<i>module</i> , <code>-M</code>[<code>&#8211;</code>]<i>module</i>, <code>-M</code>[<code>&#8211;</code>]<i>&#8216;module &#8230;&#8217;</i>, <code>-[mM]</code>[<code>&#8211;</code>]<i>module=arg[,arg]&#8230;</i>, <code>-n</code> , <code>-p</code> , <code>-s</code> , <code>-S</code> , <code>-t</code> , <code>-T</code> , <code>-u</code> , <code>-U</code> , <code>-v</code> , <code>-V</code> , <code>-V:</code><i>configvar</i>, <code>-w</code> , <code>-W</code> , <code>-X</code> , <code>-x</code> , <code>-x</code><i>directory</i></dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt><font SIZE="-1">ENVIRONMENT</font></p>
<dd><font SIZE="-1">HOME</font> , <font SIZE="-1">LOGDIR</font> , <font SIZE="-1">PATH</font> , <font SIZE="-1">PERL5LIB</font> , <font SIZE="-1">PERL5OPT</font> , <font SIZE="-1">PERLIO</font> , :bytes , :crlf , :mmap , :perlio , :pop , :raw , :stdio , :unix , :utf8 , :win32 , <font SIZE="-1">PERLIO_DEBUG</font> , <font SIZE="-1">PERLLIB</font> , <font SIZE="-1">PERL5DB</font> , <font SIZE="-1">PERL5DB_THREADED</font> , <font SIZE="-1">PERL5SHELL</font> (specific to the Win32 port) , <font SIZE="-1">PERL_ALLOW_NON_IFS_LSP</font> (specific to the Win32 port) , <font SIZE="-1">PERL_DEBUG_MSTATS</font> , <font SIZE="-1">PERL_DESTRUCT_LEVEL</font> , <font SIZE="-1">PERL_DL_NONLAZY</font> , <font SIZE="-1">PERL_ENCODING</font> , <font SIZE="-1">PERL_HASH_SEED</font> , <font SIZE="-1">PERL_PERTURB_KEYS</font> , <font SIZE="-1">PERL_HASH_SEED_DEBUG</font> , <font SIZE="-1">PERL_MEM_LOG</font> , <font SIZE="-1">PERL_ROOT</font> (specific to the <font SIZE="-1">VMS</font> port) , <font SIZE="-1">PERL_SIGNALS</font> , <font SIZE="-1">PERL_UNICODE</font> , <font SIZE="-1">PERL_USE_UNSAFE_INC</font> , <font SIZE="-1">SYS$LOGIN</font> (specific to the <font SIZE="-1">VMS</font> port) , <font SIZE="-1">PERL_INTERNAL_RAND_SEED</font></dl>
<h3>perlreftut &#8211; Mark&#8217;s very short tutorial about references</h3>
<dl COMPACT>
<dt><font SIZE="-1">DESCRIPTION</font></p>
<dd>
<dt>Who Needs Complicated Data Structures?</p>
<dd>
<dt>The Solution</p>
<dd>
<dt>Syntax</p>
<dd>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>Making References</p>
<dd>
<dt>Using References</p>
<dd>
<dt>An Example</p>
<dd>
<dt>Arrow Rule</p>
<dd></dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt>Solution</p>
<dd>
<dt>The Rest</p>
<dd>
<dt>Summary</p>
<dd>
<dt>Credits</p>
<dd>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>Distribution Conditions</p>
<dd></dl>
</dl>
<dl COMPACT>
<dd></dl>
</dl>
<h3>perldsc &#8211; Perl Data Structures Cookbook</h3>
<dl COMPACT>
<dt><font SIZE="-1">DESCRIPTION</font></p>
<dd>arrays of arrays, hashes of arrays, arrays of hashes, hashes of hashes, more elaborate constructs</p>
<dt><font SIZE="-1">REFERENCES</font></p>
<dd>
<dt><font SIZE="-1">COMMON MISTAKES</font></p>
<dd>
<dt><font SIZE="-1">CAVEAT ON PRECEDENCE</font></p>
<dd>
<dt><font SIZE="-1">WHY YOU SHOULD ALWAYS</font> &quot;use strict&quot;</p>
<dd>
<dt><font SIZE="-1">DEBUGGING</font></p>
<dd>
<dt><font SIZE="-1">CODE EXAMPLES</font></p>
<dd>
<dt><font SIZE="-1">ARRAYS OF ARRAYS</font></p>
<dd>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>Declaration of an <font SIZE="-1">ARRAY OF ARRAYS</font></p>
<dd>
<dt>Generation of an <font SIZE="-1">ARRAY OF ARRAYS</font></p>
<dd>
<dt>Access and Printing of an <font SIZE="-1">ARRAY OF ARRAYS</font></p>
<dd></dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt><font SIZE="-1">HASHES OF ARRAYS</font></p>
<dd>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>Declaration of a <font SIZE="-1">HASH OF ARRAYS</font></p>
<dd>
<dt>Generation of a <font SIZE="-1">HASH OF ARRAYS</font></p>
<dd>
<dt>Access and Printing of a <font SIZE="-1">HASH OF ARRAYS</font></p>
<dd></dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt><font SIZE="-1">ARRAYS OF HASHES</font></p>
<dd>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>Declaration of an <font SIZE="-1">ARRAY OF HASHES</font></p>
<dd>
<dt>Generation of an <font SIZE="-1">ARRAY OF HASHES</font></p>
<dd>
<dt>Access and Printing of an <font SIZE="-1">ARRAY OF HASHES</font></p>
<dd></dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt><font SIZE="-1">HASHES OF HASHES</font></p>
<dd>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>Declaration of a <font SIZE="-1">HASH OF HASHES</font></p>
<dd>
<dt>Generation of a <font SIZE="-1">HASH OF HASHES</font></p>
<dd>
<dt>Access and Printing of a <font SIZE="-1">HASH OF HASHES</font></p>
<dd></dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt><font SIZE="-1">MORE ELABORATE RECORDS</font></p>
<dd>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>Declaration of <font SIZE="-1">MORE ELABORATE RECORDS</font></p>
<dd>
<dt>Declaration of a <font SIZE="-1">HASH OF COMPLEX RECORDS</font></p>
<dd>
<dt>Generation of a <font SIZE="-1">HASH OF COMPLEX RECORDS</font></p>
<dd></dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt>Database Ties</p>
<dd>
<dt><font SIZE="-1">SEE ALSO</font></p>
<dd>
<dt><font SIZE="-1">AUTHOR</font></p>
<dd></dl>
<h3>perllol &#8211; Manipulating Arrays of Arrays in Perl</h3>
<dl COMPACT>
<dt><font SIZE="-1">DESCRIPTION</font></p>
<dd>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>Declaration and Access of Arrays of Arrays</p>
<dd>
<dt>Growing Your Own</p>
<dd>
<dt>Access and Printing</p>
<dd>
<dt>Slices</p>
<dd></dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt><font SIZE="-1">SEE ALSO</font></p>
<dd>
<dt><font SIZE="-1">AUTHOR</font></p>
<dd></dl>
<h3>perlrequick &#8211; Perl regular expressions quick start</h3>
<dl COMPACT>
<dt><font SIZE="-1">DESCRIPTION</font></p>
<dd>
<dt>The Guide</p>
<dd>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>Simple word matching</p>
<dd>
<dt>Using character classes</p>
<dd>
<dt>Matching this or that</p>
<dd>
<dt>Grouping things and hierarchical matching</p>
<dd>
<dt>Extracting matches</p>
<dd>
<dt>Matching repetitions</p>
<dd>
<dt>More matching</p>
<dd>
<dt>Search and replace</p>
<dd>
<dt>The split operator</p>
<dd>
<dt>&quot;use re &#8216;strict&#8217;&quot;</p>
<dd></dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt><font SIZE="-1">BUGS</font></p>
<dd>
<dt><font SIZE="-1">SEE ALSO</font></p>
<dd>
<dt><font SIZE="-1">AUTHOR AND COPYRIGHT</font></p>
<dd>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>Acknowledgments</p>
<dd></dl>
</dl>
<dl COMPACT>
<dd></dl>
</dl>
<h3>perlretut &#8211; Perl regular expressions tutorial</h3>
<dl COMPACT>
<dt><font SIZE="-1">DESCRIPTION</font></p>
<dd>
<dt>Part 1: The basics</p>
<dd>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>Simple word matching</p>
<dd>
<dt>Using character classes</p>
<dd>
<dt>Matching this or that</p>
<dd>
<dt>Grouping things and hierarchical matching</p>
<dd>0. Start with the first letter in the string <tt>'a'</tt>, 1. Try the first alternative in the first group <tt>'abd'</tt>, 2.<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Match <tt>'a'</tt> followed by<br />
 <tt>'b'</tt>. So far so good, 3. <tt>'d'</tt> in the regexp doesn&#8217;t match <tt>'c'</tt> in the string &#8211; a dead end. So backtrack two characters and pick the second alternative in the first group <tt>'abc'</tt>, 4.<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Match <tt>'a'</tt> followed by<br />
 <tt>'b'</tt> followed by <tt>'c'</tt>. We are on a roll and have satisfied the first group. Set <tt>$1</tt> to <tt>'abc'</tt>, 5 Move on to the second group and pick the first alternative <tt>'df'</tt>, 6 Match the <tt>'d'</tt>, 7. <tt>'f'</tt> in the regexp doesn&#8217;t match <tt>'e'</tt> in the string, so a dead end. Backtrack one character and pick the second alternative in the second group <tt>'d'</tt>, 8.<br />
&nbsp;<tt>'d'</tt>&nbsp;matches. The second grouping is satisfied, so set&nbsp;<tt>$2</tt>&nbsp;to&nbsp;<tt>'d'</tt>, 9. We are at the end of the regexp, so we are done! We have matched <tt>'abcd'</tt> out of the string <tt>&quot;abcde&quot;</tt></p>
<dt>Extracting matches</p>
<dd>
<dt>Backreferences</p>
<dd>
<dt>Relative backreferences</p>
<dd>
<dt>Named backreferences</p>
<dd>
<dt>Alternative capture group numbering</p>
<dd>
<dt>Position information</p>
<dd>
<dt>Non-capturing groupings</p>
<dd>
<dt>Matching repetitions</p>
<dd>0. Start with the first letter in the string <tt>'t'</tt>, 1.<tt>&nbsp;</tt>The first<br />
 quantifier <tt>'.*'</tt> starts out by matching the whole string &quot;<tt>&quot;the cat in the hat&quot;</tt>&quot;, 2. <tt>'a'</tt> in the regexp element <tt>'at'</tt> doesn&#8217;t match the end of the string. Backtrack one character, 3. <tt>'a'</tt> in the regexp element <tt>'at'</tt> still doesn&#8217;t match the last letter of the string <tt>'t'</tt>, so backtrack one more character, 4.<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>Now we can match the <tt>'a'</tt> and the<br />
 <tt>'t'</tt>, 5. Move on to the third element <tt>'.*'</tt>. Since we are at the end of the string and <tt>'.*'</tt> can match 0 times, assign it the empty string, 6. We are done!</p>
<dt>Possessive quantifiers</p>
<dd>
<dt>Building a regexp</p>
<dd>
<dt>Using regular expressions in Perl</p>
<dd></dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt>Part 2: Power tools</p>
<dd>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>More on characters, strings, and character classes</p>
<dd>
<dt>Compiling and saving regular expressions</p>
<dd>
<dt>Composing regular expressions at runtime</p>
<dd>
<dt>Embedding comments and modifiers in a regular expression</p>
<dd>
<dt>Looking ahead and looking behind</p>
<dd>
<dt>Using independent subexpressions to prevent backtracking</p>
<dd>
<dt>Conditional expressions</p>
<dd>
<dt>Defining named patterns</p>
<dd>
<dt>Recursive patterns</p>
<dd>
<dt>A bit of magic: executing Perl code in a regular expression</p>
<dd>
<dt>Backtracking control verbs</p>
<dd>
<dt>Pragmas and debugging</p>
<dd></dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt><font SIZE="-1">SEE ALSO</font></p>
<dd>
<dt><font SIZE="-1">AUTHOR AND COPYRIGHT</font></p>
<dd>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>Acknowledgments</p>
<dd></dl>
</dl>
<dl COMPACT>
<dd></dl>
</dl>
<h3>perlootut &#8211; Object-Oriented Programming in Perl Tutorial</h3>
<dl COMPACT>
<dt><font SIZE="-1">DATE</font></p>
<dd>
<dt><font SIZE="-1">DESCRIPTION</font></p>
<dd>
<dt>OBJECT-ORIENTED <font SIZE="-1">FUNDAMENTALS</font></p>
<dd>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>Object</p>
<dd>
<dt>Class</p>
<dd>
<dt>Methods</p>
<dd>
<dt>Attributes</p>
<dd>
<dt>Polymorphism</p>
<dd>
<dt>Inheritance</p>
<dd>
<dt>Encapsulation</p>
<dd>
<dt>Composition</p>
<dd>
<dt>Roles</p>
<dd>
<dt>When to Use <font SIZE="-1">OO</font></p>
<dd></dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt><font SIZE="-1">PERL OO SYSTEMS</font></p>
<dd>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>Moose</p>
<dd>Declarative sugar, Roles built-in, A miniature type system, Full introspection and manipulation, Self-hosted and extensible, Rich ecosystem, Many more features</p>
<dt>Class::Accessor</p>
<dd>
<dt>Class::Tiny</p>
<dd>
<dt>Role::Tiny</p>
<dd>
<dt><font SIZE="-1">OO</font> System Summary</p>
<dd>Moose, Class::Accessor, Class::Tiny, Role::Tiny</p>
<dt>Other <font SIZE="-1">OO</font> Systems</p>
<dd></dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt><font SIZE="-1">CONCLUSION</font></p>
<dd></dl>
<h3>perlperf &#8211; Perl Performance and Optimization Techniques</h3>
<dl COMPACT>
<dt><font SIZE="-1">DESCRIPTION</font></p>
<dd>
<dt><font SIZE="-1">OVERVIEW</font></p>
<dd>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><font SIZE="-1">ONE STEP SIDEWAYS</font></p>
<dd>
<dt><font SIZE="-1">ONE STEP FORWARD</font></p>
<dd>
<dt><font SIZE="-1">ANOTHER STEP SIDEWAYS</font></p>
<dd></dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt><font SIZE="-1">GENERAL GUIDELINES</font></p>
<dd>
<dt><font SIZE="-1">BENCHMARKS</font></p>
<dd>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>Assigning and Dereferencing Variables.</p>
<dd>
<dt>Search and replace or tr</p>
<dd></dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt><font SIZE="-1">PROFILING TOOLS</font></p>
<dd>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>Devel::DProf</p>
<dd>
<dt>Devel::Profiler</p>
<dd>
<dt>Devel::SmallProf</p>
<dd>
<dt>Devel::FastProf</p>
<dd>
<dt>Devel::NYTProf</p>
<dd></dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt><font SIZE="-1">SORTING</font></p>
<dd>Elapsed Real Time, User <font SIZE="-1">CPU</font> Time, System <font SIZE="-1">CPU</font> Time</p>
<dt><font SIZE="-1">LOGGING</font></p>
<dd>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>Logging if <font SIZE="-1">DEBUG</font> (constant)</p>
<dd></dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt><font SIZE="-1">POSTSCRIPT</font></p>
<dd>
<dt><font SIZE="-1">SEE ALSO</font></p>
<dd>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><font SIZE="-1">PERLDOCS</font></p>
<dd>
<dt><font SIZE="-1">MAN PAGES</font></p>
<dd>
<dt><font SIZE="-1">MODULES</font></p>
<dd>
<dt><font SIZE="-1">URLS</font></p>
<dd></dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt><font SIZE="-1">AUTHOR</font></p>
<dd></dl>
<h3>perlstyle &#8211; Perl style guide</h3>
<dl COMPACT>
<dt><font SIZE="-1">DESCRIPTION</font></p>
<dd></dl>
<h3>perlcheat &#8211; Perl 5 Cheat Sheet</h3>
<dl COMPACT>
<dt><font SIZE="-1">DESCRIPTION</font></p>
<dd>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>The sheet</p>
<dd></dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt><font SIZE="-1">ACKNOWLEDGEMENTS</font></p>
<dd>
<dt><font SIZE="-1">AUTHOR</font></p>
<dd>
<dt><font SIZE="-1">SEE ALSO</font></p>
<dd></dl>
<h3>perltrap &#8211; Perl traps for the unwary</h3>
<dl COMPACT>
<dt><font SIZE="-1">DESCRIPTION</font></p>
<dd>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>Awk Traps</p>
<dd>
<dt>C/C<font SIZE="-2">++</font> Traps</p>
<dd>
<dt>JavaScript Traps</p>
<dd>
<dt>Sed Traps</p>
<dd>
<dt>Shell Traps</p>
<dd>
<dt>Perl Traps</p>
<dd></dl>
</dl>
<dl COMPACT>
<dd></dl>
</dl>
<h3>perldebtut &#8211; Perl debugging tutorial</h3>
<dl COMPACT>
<dt><font SIZE="-1">DESCRIPTION</font></p>
<dd>
<dt>use strict</p>
<dd>
<dt>Looking at data and -w and v</p>
<dd>
<dt>help</p>
<dd>
<dt>Stepping through code</p>
<dd>
<dt>Placeholder for a, w, t, T</p>
<dd>
<dt><font SIZE="-1">REGULAR EXPRESSIONS</font></p>
<dd>
<dt><font SIZE="-1">OUTPUT TIPS</font></p>
<dd>
<dt><font SIZE="-1">CGI</font></p>
<dd>
<dt>GUIs</p>
<dd>
<dt><font SIZE="-1">SUMMARY</font></p>
<dd>
<dt><font SIZE="-1">SEE ALSO</font></p>
<dd>
<dt><font SIZE="-1">AUTHOR</font></p>
<dd>
<dt><font SIZE="-1">CONTRIBUTORS</font></p>
<dd></dl>
<h3>perlfaq &#8211; Frequently asked questions about Perl</h3>
<dl COMPACT>
<dt><font SIZE="-1">VERSION</font></p>
<dd>
<dt><font SIZE="-1">DESCRIPTION</font></p>
<dd>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>Where to find the perlfaq</p>
<dd>
<dt>How to use the perlfaq</p>
<dd>
<dt>How to contribute to the perlfaq</p>
<dd>
<dt>What if my question isn&#8217;t answered in the <font SIZE="-1">FAQ</font>?</p>
<dd></dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt><font SIZE="-1">TABLE OF CONTENTS</font></p>
<dd>perlfaq1 &#8211; General Questions About Perl, perlfaq2 &#8211; Obtaining and Learning about Perl, perlfaq3 &#8211; Programming Tools, perlfaq4 &#8211; Data Manipulation, perlfaq5 &#8211; Files and Formats, perlfaq6 &#8211; Regular Expressions, perlfaq7 &#8211; General Perl Language Issues, perlfaq8 &#8211; System Interaction, perlfaq9 &#8211; Web, Email and Networking</p>
<dt><font SIZE="-1">THE QUESTIONS</font></p>
<dd>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>perlfaq1: General Questions About Perl</p>
<dd>
<dt>perlfaq2: Obtaining and Learning about Perl</p>
<dd>
<dt>perlfaq3: Programming Tools</p>
<dd>
<dt>perlfaq4: Data Manipulation</p>
<dd>
<dt>perlfaq5: Files and Formats</p>
<dd>
<dt>perlfaq6: Regular Expressions</p>
<dd>
<dt>perlfaq7: General Perl Language Issues</p>
<dd>
<dt>perlfaq8: System Interaction</p>
<dd>
<dt>perlfaq9: Web, Email and Networking</p>
<dd></dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt><font SIZE="-1">CREDITS</font></p>
<dd>
<dt><font SIZE="-1">AUTHOR AND COPYRIGHT</font></p>
<dd></dl>
<h3>perlfaq1 &#8211; General Questions About Perl</h3>
<dl COMPACT>
<dt><font SIZE="-1">VERSION</font></p>
<dd>
<dt><font SIZE="-1">DESCRIPTION</font></p>
<dd>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>What is Perl?</p>
<dd>
<dt>Who supports Perl? Who develops it? Why is it free?</p>
<dd>
<dt>Which version of Perl should I use?</p>
<dd>
<dt>What are Perl 4, Perl 5, or Perl 6?</p>
<dd>
<dt>What is Perl 6?</p>
<dd>
<dt>How stable is Perl?</p>
<dd>
<dt>How often are new versions of Perl released?</p>
<dd>
<dt>Is Perl difficult to learn?</p>
<dd>
<dt>How does Perl compare with other languages like Java, Python, <font SIZE="-1">REXX,</font> Scheme, or Tcl?</p>
<dd>
<dt>Can I do [task] in Perl?</p>
<dd>
<dt>When shouldn&#8217;t I program in Perl?</p>
<dd>
<dt>What&#8217;s the difference between &quot;perl&quot; and &quot;Perl&quot;?</p>
<dd>
<dt>What is a <font SIZE="-1">JAPH</font>?</p>
<dd>
<dt>How can I convince others to use Perl?</p>
<dd>&lt;<a rel="nofollow" href="http://www.perl.org/about.html">http://www.perl.org/about.html</a>&gt;, &lt;<a rel="nofollow" href="http://perltraining.com.au/whyperl.html">http://perltraining.com.au/whyperl.html</a>&gt;</dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt><font SIZE="-1">AUTHOR AND COPYRIGHT</font></p>
<dd></dl>
<h3>perlfaq2 &#8211; Obtaining and Learning about Perl</h3>
<dl COMPACT>
<dt><font SIZE="-1">VERSION</font></p>
<dd>
<dt><font SIZE="-1">DESCRIPTION</font></p>
<dd>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>What machines support Perl? Where do I get it?</p>
<dd>
<dt>How can I get a binary version of Perl?</p>
<dd>
<dt>I don&#8217;t have a C compiler. How can I build my own Perl interpreter?</p>
<dd>
<dt>I copied the Perl binary from one machine to another, but scripts don&#8217;t work.</p>
<dd>
<dt>I grabbed the sources and tried to compile but gdbm/dynamic loading/malloc/linking/&#8230; failed. How do I make it work?</p>
<dd>
<dt>What modules and extensions are available for Perl? What is <font SIZE="-1">CPAN</font>?</p>
<dd>
<dt>Where can I get information on Perl?</p>
<dd>&lt;<a rel="nofollow" href="http://www.perl.org/">http://www.perl.org/</a>&gt;, &lt;<a rel="nofollow" href="http://perldoc.perl.org/">http://perldoc.perl.org/</a>&gt;, &lt;<a rel="nofollow" href="http://learn.perl.org/">http://learn.perl.org/</a>&gt;</p>
<dt>What is perl.com? Perl Mongers? pm.org? perl.org? cpan.org?</p>
<dd>&lt;<a rel="nofollow" href="http://www.perl.org/">http://www.perl.org/</a>&gt;, &lt;<a rel="nofollow" href="http://learn.perl.org/">http://learn.perl.org/</a>&gt;, &lt;<a rel="nofollow" href="http://jobs.perl.org/">http://jobs.perl.org/</a>&gt;, &lt;<a rel="nofollow" href="http://lists.perl.org/">http://lists.perl.org/</a>&gt;</p>
<dt>Where can I post questions?</p>
<dd>
<dt>Perl Books</p>
<dd>
<dt>Which magazines have Perl content?</p>
<dd>
<dt>Which Perl blogs should I read?</p>
<dd>
<dt>What mailing lists are there for Perl?</p>
<dd>
<dt>Where can I buy a commercial version of Perl?</p>
<dd>
<dt>Where do I send bug reports?</p>
<dd></dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt><font SIZE="-1">AUTHOR AND COPYRIGHT</font></p>
<dd></dl>
<h3>perlfaq3 &#8211; Programming Tools</h3>
<dl COMPACT>
<dt><font SIZE="-1">VERSION</font></p>
<dd>
<dt><font SIZE="-1">DESCRIPTION</font></p>
<dd>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>How do I do (anything)?</p>
<dd>Basics, perldata &#8211; Perl data types, perlvar &#8211; Perl pre-defined variables, perlsyn &#8211; Perl syntax, perlop &#8211; Perl operators and precedence, perlsub &#8211; Perl subroutines, Execution, perlrun &#8211; how to execute the Perl interpreter, perldebug &#8211; Perl debugging, Functions, perlfunc &#8211; Perl builtin functions, Objects, perlref &#8211; Perl references and nested data structures, perlmod &#8211; Perl modules (packages and symbol tables), perlobj &#8211; Perl objects, perltie &#8211; how to hide an object class in a simple variable, Data Structures, perlref &#8211; Perl references and nested data structures, perllol &#8211; Manipulating arrays of arrays in Perl, perldsc &#8211; Perl Data Structures Cookbook, Modules, perlmod &#8211; Perl modules (packages and symbol tables), perlmodlib &#8211; constructing new Perl modules and finding existing ones, Regexes, perlre &#8211; Perl regular expressions, perlfunc &#8211; Perl builtin functions&gt;, perlop &#8211; Perl operators and precedence, perllocale &#8211; Perl locale handling (internationalization and localization), Moving to perl5, perltrap &#8211; Perl traps for the unwary, perl, Linking with C, perlxstut &#8211; Tutorial for writing XSUBs, perlxs &#8211; <font SIZE="-1">XS</font> language reference manual, perlcall &#8211; Perl calling conventions from C, perlguts &#8211; Introduction to the Perl <font SIZE="-1">API,</font> perlembed &#8211; how to embed perl in your C program, Various</p>
<dt>How can I use Perl interactively?</p>
<dd>
<dt>How do I find which modules are installed on my system?</p>
<dd>
<dt>How do I debug my Perl programs?</p>
<dd>
<dt>How do I profile my Perl programs?</p>
<dd>
<dt>How do I cross-reference my Perl programs?</p>
<dd>
<dt>Is there a pretty-printer (formatter) for Perl?</p>
<dd>
<dt>Is there an <font SIZE="-1">IDE</font> or Windows Perl Editor?</p>
<dd>Eclipse, Enginsite, IntelliJ <font SIZE="-1">IDEA,</font> Kephra, Komodo, Notepad++, Open Perl <font SIZE="-1">IDE,</font> OptiPerl, Padre, PerlBuilder, visiPerl+, Visual Perl, Zeus, <font SIZE="-1">GNU</font> Emacs, MicroEMACS, XEmacs, Jed, Vim, Vile, MultiEdit, SlickEdit, ConTEXT, bash, zsh, BBEdit and TextWrangler</p>
<dt>Where can I get Perl macros for vi?</p>
<dd>
<dt>Where can I get perl-mode or cperl-mode for emacs?</p>
<dd>
<dt>How can I use curses with Perl?</p>
<dd>
<dt>How can I write a <font SIZE="-1">GUI</font> (X, Tk, Gtk, etc.) in Perl?</p>
<dd>Tk, Wx, Gtk and Gtk2, Win32::GUI, CamelBones, Qt, Athena</p>
<dt>How can I make my Perl program run faster?</p>
<dd>
<dt>How can I make my Perl program take less memory?</p>
<dd>Don&#8217;t slurp!, Use map and grep selectively, Avoid unnecessary quotes and stringification, Pass by reference, Tie large variables to disk</p>
<dt>Is it safe to return a reference to local or lexical data?</p>
<dd>
<dt>How can I free an array or hash so my program shrinks?</p>
<dd>
<dt>How can I make my <font SIZE="-1">CGI</font> script more efficient?</p>
<dd>
<dt>How can I hide the source for my Perl program?</p>
<dd>
<dt>How can I compile my Perl program into byte code or C?</p>
<dd>
<dt>How can I get &quot;#!perl&quot; to work on [<font SIZE="-1">MS-DOS,NT,&#8230;</font>]?</p>
<dd>
<dt>Can I write useful Perl programs on the command line?</p>
<dd>
<dt>Why don&#8217;t Perl one-liners work on my DOS/Mac/VMS system?</p>
<dd>
<dt>Where can I learn about <font SIZE="-1">CGI</font> or Web programming in Perl?</p>
<dd>
<dt>Where can I learn about object-oriented Perl programming?</p>
<dd>
<dt>Where can I learn about linking C with Perl?</p>
<dd>
<dt>I&#8217;ve read perlembed, perlguts, etc., but I can&#8217;t embed perl in my C program; what am I doing wrong?</p>
<dd>
<dt>When I tried to run my script, I got this message. What does it mean?</p>
<dd>
<dt>What&#8217;s MakeMaker?</p>
<dd></dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt><font SIZE="-1">AUTHOR AND COPYRIGHT</font></p>
<dd></dl>
<h3>perlfaq4 &#8211; Data Manipulation</h3>
<dl COMPACT>
<dt><font SIZE="-1">VERSION</font></p>
<dd>
<dt><font SIZE="-1">DESCRIPTION</font></p>
<dd>
<dt>Data: Numbers</p>
<dd>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>Why am I getting long decimals (eg, 19.9499999999999) instead of the numbers I should be getting (eg, 19.95)?</p>
<dd>
<dt>Why is <code>int()</code> broken?</p>
<dd>
<dt>Why isn&#8217;t my octal data interpreted correctly?</p>
<dd>
<dt>Does Perl have a <code>round()</code> function? What about <code>ceil()</code> and <code>floor()</code>? Trig functions?</p>
<dd>
<dt>How do I convert between numeric representations/bases/radixes?</p>
<dd>How do I convert hexadecimal into decimal, How do I convert from decimal to hexadecimal, How do I convert from octal to decimal, How do I convert from decimal to octal, How do I convert from binary to decimal, How do I convert from decimal to binary</p>
<dt>Why doesn&#8217;t &amp; work the way I want it to?</p>
<dd>
<dt>How do I multiply matrices?</p>
<dd>
<dt>How do I perform an operation on a series of integers?</p>
<dd>
<dt>How can I output Roman numerals?</p>
<dd>
<dt>Why aren&#8217;t my random numbers random?</p>
<dd>
<dt>How do I get a random number between X and Y?</p>
<dd></dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt>Data: Dates</p>
<dd>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>How do I find the day or week of the year?</p>
<dd>
<dt>How do I find the current century or millennium?</p>
<dd>
<dt>How can I compare two dates and find the difference?</p>
<dd>
<dt>How can I take a string and turn it into epoch seconds?</p>
<dd>
<dt>How can I find the Julian Day?</p>
<dd>
<dt>How do I find yesterday&#8217;s date?</p>
<dd>
<dt>Does Perl have a Year 2000 or 2038 problem? Is Perl Y2K compliant?</p>
<dd></dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt>Data: Strings</p>
<dd>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>How do I validate input?</p>
<dd>
<dt>How do I unescape a string?</p>
<dd>
<dt>How do I remove consecutive pairs of characters?</p>
<dd>
<dt>How do I expand function calls in a string?</p>
<dd>
<dt>How do I find matching/nesting anything?</p>
<dd>
<dt>How do I reverse a string?</p>
<dd>
<dt>How do I expand tabs in a string?</p>
<dd>
<dt>How do I reformat a paragraph?</p>
<dd>
<dt>How can I access or change N characters of a string?</p>
<dd>
<dt>How do I change the Nth occurrence of something?</p>
<dd>
<dt>How can I count the number of occurrences of a substring within a string?</p>
<dd>
<dt>How do I capitalize all the words on one line?</p>
<dd>
<dt>How can I split a [character]-delimited string except when inside [character]?</p>
<dd>
<dt>How do I strip blank space from the beginning/end of a string?</p>
<dd>
<dt>How do I pad a string with blanks or pad a number with zeroes?</p>
<dd>
<dt>How do I extract selected columns from a string?</p>
<dd>
<dt>How do I find the soundex value of a string?</p>
<dd>
<dt>How can I expand variables in text strings?</p>
<dd>
<dt>What&#8217;s wrong with always quoting &quot;$vars&quot;?</p>
<dd>
<dt>Why don&#8217;t my &lt;&lt;<font SIZE="-1">HERE</font> documents work?</p>
<dd>There must be no space after the &lt;&lt; part, There (probably) should be a semicolon at the end of the opening token, You can&#8217;t (easily) have any space in front of the tag, There needs to be at least a line separator after the end token</dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt>Data: Arrays</p>
<dd>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>What is the difference between a list and an array?</p>
<dd>
<dt>What is the difference between $array[1] and @array[1]?</p>
<dd>
<dt>How can I remove duplicate elements from a list or array?</p>
<dd>
<dt>How can I tell whether a certain element is contained in a list or array?</p>
<dd>
<dt>How do I compute the difference of two arrays? How do I compute the intersection of two arrays?</p>
<dd>
<dt>How do I test whether two arrays or hashes are equal?</p>
<dd>
<dt>How do I find the first array element for which a condition is true?</p>
<dd>
<dt>How do I handle linked lists?</p>
<dd>
<dt>How do I handle circular lists?</p>
<dd>
<dt>How do I shuffle an array randomly?</p>
<dd>
<dt>How do I process/modify each element of an array?</p>
<dd>
<dt>How do I select a random element from an array?</p>
<dd>
<dt>How do I permute N elements of a list?</p>
<dd>
<dt>How do I sort an array by (anything)?</p>
<dd>
<dt>How do I manipulate arrays of bits?</p>
<dd>
<dt>Why does <code>defined()</code> return true on empty arrays and hashes?</p>
<dd></dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt>Data: Hashes (Associative Arrays)</p>
<dd>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>How do I process an entire hash?</p>
<dd>
<dt>How do I merge two hashes?</p>
<dd>
<dt>What happens if I add or remove keys from a hash while iterating over it?</p>
<dd>
<dt>How do I look up a hash element by value?</p>
<dd>
<dt>How can I know how many entries are in a hash?</p>
<dd>
<dt>How do I sort a hash (optionally by value instead of key)?</p>
<dd>
<dt>How can I always keep my hash sorted?</p>
<dd>
<dt>What&#8217;s the difference between &quot;delete&quot; and &quot;undef&quot; with hashes?</p>
<dd>
<dt>Why don&#8217;t my tied hashes make the defined/exists distinction?</p>
<dd>
<dt>How do I reset an <code>each()</code> operation part-way through?</p>
<dd>
<dt>How can I get the unique keys from two hashes?</p>
<dd>
<dt>How can I store a multidimensional array in a <font SIZE="-1">DBM</font> file?</p>
<dd>
<dt>How can I make my hash remember the order I put elements into it?</p>
<dd>
<dt>Why does passing a subroutine an undefined element in a hash create it?</p>
<dd>
<dt>How can I make the Perl equivalent of a C structure/C<font SIZE="-2">++</font> class/hash or array of hashes or arrays?</p>
<dd>
<dt>How can I use a reference as a hash key?</p>
<dd>
<dt>How can I check if a key exists in a multilevel hash?</p>
<dd>
<dt>How can I prevent addition of unwanted keys into a hash?</p>
<dd></dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt>Data: Misc</p>
<dd>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>How do I handle binary data correctly?</p>
<dd>
<dt>How do I determine whether a scalar is a number/whole/integer/float?</p>
<dd>
<dt>How do I keep persistent data across program calls?</p>
<dd>
<dt>How do I print out or copy a recursive data structure?</p>
<dd>
<dt>How do I define methods for every class/object?</p>
<dd>
<dt>How do I verify a credit card checksum?</p>
<dd>
<dt>How do I pack arrays of doubles or floats for <font SIZE="-1">XS</font> code?</p>
<dd></dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt><font SIZE="-1">AUTHOR AND COPYRIGHT</font></p>
<dd></dl>
<h3>perlfaq5 &#8211; Files and Formats</h3>
<dl COMPACT>
<dt><font SIZE="-1">VERSION</font></p>
<dd>
<dt><font SIZE="-1">DESCRIPTION</font></p>
<dd>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>How do I flush/unbuffer an output filehandle? Why must I do this?</p>
<dd>
<dt>How do I change, delete, or insert a line in a file, or append to the beginning of a file?</p>
<dd>
<dt>How do I count the number of lines in a file?</p>
<dd>
<dt>How do I delete the last N lines from a file?</p>
<dd>
<dt>How can I use Perl&#8217;s &quot;-i&quot; option from within a program?</p>
<dd>
<dt>How can I copy a file?</p>
<dd>
<dt>How do I make a temporary file name?</p>
<dd>
<dt>How can I manipulate fixed-record-length files?</p>
<dd>
<dt>How can I make a filehandle local to a subroutine? How do I pass filehandles between subroutines? How do I make an array of filehandles?</p>
<dd>
<dt>How can I use a filehandle indirectly?</p>
<dd>
<dt>How can I open a filehandle to a string?</p>
<dd>
<dt>How can I set up a footer format to be used with <code>write()</code>?</p>
<dd>
<dt>How can I <code>write()</code> into a string?</p>
<dd>
<dt>How can I output my numbers with commas added?</p>
<dd>
<dt>How can I translate tildes (~) in a filename?</p>
<dd>
<dt>How come when I open a file read-write it wipes it out?</p>
<dd>
<dt>Why do I sometimes get an &quot;Argument list too long&quot; when I use &lt;*&gt;?</p>
<dd>
<dt>How can I open a file named with a leading &quot;&gt;&quot; or trailing blanks?</p>
<dd>
<dt>How can I reliably rename a file?</p>
<dd>
<dt>How can I lock a file?</p>
<dd>
<dt>Why can&#8217;t I just open(<font SIZE="-1">FH, &quot;</font>&gt;file.lock&quot;)?</p>
<dd>
<dt>I still don&#8217;t get locking. I just want to increment the number in the file. How can I do this?</p>
<dd>
<dt>All I want to do is append a small amount of text to the end of a file. Do I still have to use locking?</p>
<dd>
<dt>How do I randomly update a binary file?</p>
<dd>
<dt>How do I get a file&#8217;s timestamp in perl?</p>
<dd>
<dt>How do I set a file&#8217;s timestamp in perl?</p>
<dd>
<dt>How do I print to more than one file at once?</p>
<dd>
<dt>How can I read in an entire file all at once?</p>
<dd>
<dt>How can I read in a file by paragraphs?</p>
<dd>
<dt>How can I read a single character from a file? From the keyboard?</p>
<dd>
<dt>How can I tell whether there&#8217;s a character waiting on a filehandle?</p>
<dd>
<dt>How do I do a &quot;tail -f&quot; in perl?</p>
<dd>
<dt>How do I <code>dup()</code> a filehandle in Perl?</p>
<dd>
<dt>How do I close a file descriptor by number?</p>
<dd>
<dt>Why can&#8217;t I use &quot;C:	empoo&quot; in <font SIZE="-1">DOS</font> paths? Why doesn&#8217;t `C:	empoo.exe` work?</p>
<dd>
<dt>Why doesn&#8217;t glob(&quot;*.*&quot;) get all the files?</p>
<dd>
<dt>Why does Perl let me delete read-only files? Why does &quot;-i&quot; clobber protected files? Isn&#8217;t this a bug in Perl?</p>
<dd>
<dt>How do I select a random line from a file?</p>
<dd>
<dt>Why do I get weird spaces when I print an array of lines?</p>
<dd>
<dt>How do I traverse a directory tree?</p>
<dd>
<dt>How do I delete a directory tree?</p>
<dd>
<dt>How do I copy an entire directory?</p>
<dd></dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt><font SIZE="-1">AUTHOR AND COPYRIGHT</font></p>
<dd></dl>
<h3>perlfaq6 &#8211; Regular Expressions</h3>
<dl COMPACT>
<dt><font SIZE="-1">VERSION</font></p>
<dd>
<dt><font SIZE="-1">DESCRIPTION</font></p>
<dd>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>How can I hope to use regular expressions without creating illegible and unmaintainable code?</p>
<dd>Comments Outside the Regex, Comments Inside the Regex, Different Delimiters</p>
<dt>I&#8217;m having trouble matching over more than one line. What&#8217;s wrong?</p>
<dd>
<dt>How can I pull out lines between two patterns that are themselves on different lines?</p>
<dd>
<dt>How do I match <font SIZE="-1">XML, HTML,</font> or other nasty, ugly things with a regex?</p>
<dd>
<dt>I put a regular expression into $/ but it didn&#8217;t work. What&#8217;s wrong?</p>
<dd>
<dt>How do I substitute case-insensitively on the <font SIZE="-1">LHS</font> while preserving case on the <font SIZE="-1">RHS</font>?</p>
<dd>
<dt>How can I make &quot;\w&quot; match national character sets?</p>
<dd>
<dt>How can I match a locale-smart version of &quot;/[a-zA-Z]/&quot;?</p>
<dd>
<dt>How can I quote a variable to use in a regex?</p>
<dd>
<dt>What is &quot;/o&quot; really for?</p>
<dd>
<dt>How do I use a regular expression to strip C-style comments from a file?</p>
<dd>
<dt>Can I use Perl regular expressions to match balanced text?</p>
<dd>
<dt>What does it mean that regexes are greedy? How can I get around it?</p>
<dd>
<dt>How do I process each word on each line?</p>
<dd>
<dt>How can I print out a word-frequency or line-frequency summary?</p>
<dd>
<dt>How can I do approximate matching?</p>
<dd>
<dt>How do I efficiently match many regular expressions at once?</p>
<dd>
<dt>Why don&#8217;t word-boundary searches with &quot;&quot; work for me?</p>
<dd>
<dt>Why does using $&amp;, $`, or $&#8217; slow my program down?</p>
<dd>
<dt>What good is &quot;\G&quot; in a regular expression?</p>
<dd>
<dt>Are Perl regexes DFAs or NFAs? Are they <font SIZE="-1">POSIX</font> compliant?</p>
<dd>
<dt>What&#8217;s wrong with using grep in a void context?</p>
<dd>
<dt>How can I match strings with multibyte characters?</p>
<dd>
<dt>How do I match a regular expression that&#8217;s in a variable?</p>
<dd></dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt><font SIZE="-1">AUTHOR AND COPYRIGHT</font></p>
<dd></dl>
<h3>perlfaq7 &#8211; General Perl Language Issues</h3>
<dl COMPACT>
<dt><font SIZE="-1">VERSION</font></p>
<dd>
<dt><font SIZE="-1">DESCRIPTION</font></p>
<dd>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>Can I get a BNF/yacc/RE for the Perl language?</p>
<dd>
<dt>What are all these $@%&amp;* punctuation signs, and how do I know when to use them?</p>
<dd>
<dt>Do I always/never have to quote my strings or use semicolons and commas?</p>
<dd>
<dt>How do I skip some return values?</p>
<dd>
<dt>How do I temporarily block warnings?</p>
<dd>
<dt>What&#8217;s an extension?</p>
<dd>
<dt>Why do Perl operators have different precedence than C operators?</p>
<dd>
<dt>How do I declare/create a structure?</p>
<dd>
<dt>How do I create a module?</p>
<dd>
<dt>How do I adopt or take over a module already on <font SIZE="-1">CPAN</font>?</p>
<dd>
<dt>How do I create a class?</p>
<dd>
<dt>How can I tell if a variable is tainted?</p>
<dd>
<dt>What&#8217;s a closure?</p>
<dd>
<dt>What is variable suicide and how can I prevent it?</p>
<dd>
<dt>How can I pass/return a {Function, FileHandle, Array, Hash, Method, Regex}?</p>
<dd>Passing Variables and Functions, Passing Filehandles, Passing Regexes, Passing Methods</p>
<dt>How do I create a static variable?</p>
<dd>
<dt>What&#8217;s the difference between dynamic and lexical (static) scoping? Between <code>local()</code> and <code>my()</code>?</p>
<dd>
<dt>How can I access a dynamic variable while a similarly named lexical is in scope?</p>
<dd>
<dt>What&#8217;s the difference between deep and shallow binding?</p>
<dd>
<dt>Why doesn&#8217;t &quot;my($foo) = &lt;$fh&gt;;&quot; work right?</p>
<dd>
<dt>How do I redefine a builtin function, operator, or method?</p>
<dd>
<dt>What&#8217;s the difference between calling a function as &amp;foo and <code>foo()</code>?</p>
<dd>
<dt>How do I create a switch or case statement?</p>
<dd>
<dt>How can I catch accesses to undefined variables, functions, or methods?</p>
<dd>
<dt>Why can&#8217;t a method included in this same file be found?</p>
<dd>
<dt>How can I find out my current or calling package?</p>
<dd>
<dt>How can I comment out a large block of Perl code?</p>
<dd>
<dt>How do I clear a package?</p>
<dd>
<dt>How can I use a variable as a variable name?</p>
<dd>
<dt>What does &quot;bad interpreter&quot; mean?</p>
<dd>
<dt>Do I need to recompile <font SIZE="-1">XS</font> modules when there is a change in the C library?</p>
<dd></dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt><font SIZE="-1">AUTHOR AND COPYRIGHT</font></p>
<dd></dl>
<h3>perlfaq8 &#8211; System Interaction</h3>
<dl COMPACT>
<dt><font SIZE="-1">VERSION</font></p>
<dd>
<dt><font SIZE="-1">DESCRIPTION</font></p>
<dd>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>How do I find out which operating system I&#8217;m running under?</p>
<dd>
<dt>How come <code>exec()</code> doesn&#8217;t return?</p>
<dd>
<dt>How do I do fancy stuff with the keyboard/screen/mouse?</p>
<dd>Keyboard, Screen, Mouse</p>
<dt>How do I print something out in color?</p>
<dd>
<dt>How do I read just one key without waiting for a return key?</p>
<dd>
<dt>How do I check whether input is ready on the keyboard?</p>
<dd>
<dt>How do I clear the screen?</p>
<dd>
<dt>How do I get the screen size?</p>
<dd>
<dt>How do I ask the user for a password?</p>
<dd>
<dt>How do I read and write the serial port?</p>
<dd>lockfiles, open mode, end of line, flushing output, non-blocking input</p>
<dt>How do I decode encrypted password files?</p>
<dd>
<dt>How do I start a process in the background?</p>
<dd><font SIZE="-1">STDIN, STDOUT,</font> and <font SIZE="-1">STDERR</font> are shared, Signals, Zombies</p>
<dt>How do I trap control characters/signals?</p>
<dd>
<dt>How do I modify the shadow password file on a Unix system?</p>
<dd>
<dt>How do I set the time and date?</p>
<dd>
<dt>How can I <code>sleep()</code> or <code>alarm()</code> for under a second?</p>
<dd>
<dt>How can I measure time under a second?</p>
<dd>
<dt>How can I do an <code>atexit()</code> or <code>setjmp()</code>/<code>longjmp()</code>? (Exception handling)</p>
<dd>
<dt>Why doesn&#8217;t my sockets program work under System V (Solaris)? What does the error message &quot;Protocol not supported&quot; mean?</p>
<dd>
<dt>How can I call my system&#8217;s unique C functions from Perl?</p>
<dd>
<dt>Where do I get the include files to do <code>ioctl()</code> or <code>syscall()</code>?</p>
<dd>
<dt>Why do setuid perl scripts complain about kernel problems?</p>
<dd>
<dt>How can I open a pipe both to and from a command?</p>
<dd>
<dt>Why can&#8217;t I get the output of a command with <code>system()</code>?</p>
<dd>
<dt>How can I capture <font SIZE="-1">STDERR</font> from an external command?</p>
<dd>
<dt>Why doesn&#8217;t <code>open()</code> return an error when a pipe open fails?</p>
<dd>
<dt>What&#8217;s wrong with using backticks in a void context?</p>
<dd>
<dt>How can I call backticks without shell processing?</p>
<dd>
<dt>Why can&#8217;t my script read from <font SIZE="-1">STDIN</font> after I gave it <font SIZE="-1">EOF</font> (^D on Unix, ^Z on MS-DOS)?</p>
<dd>
<dt>How can I convert my shell script to perl?</p>
<dd>
<dt>Can I use perl to run a telnet or ftp session?</p>
<dd>
<dt>How can I write expect in Perl?</p>
<dd>
<dt>Is there a way to hide perl&#8217;s command line from programs such as &quot;ps&quot;?</p>
<dd>
<dt>I {changed directory, modified my environment} in a perl script. How come the change disappeared when I exited the script? How do I get my changes to be visible?</p>
<dd>Unix</p>
<dt>How do I close a process&#8217;s filehandle without waiting for it to complete?</p>
<dd>
<dt>How do I fork a daemon process?</p>
<dd>
<dt>How do I find out if I&#8217;m running interactively or not?</p>
<dd>
<dt>How do I timeout a slow event?</p>
<dd>
<dt>How do I set <font SIZE="-1">CPU</font> limits?</p>
<dd>
<dt>How do I avoid zombies on a Unix system?</p>
<dd>
<dt>How do I use an <font SIZE="-1">SQL</font> database?</p>
<dd>
<dt>How do I make a <code>system()</code> exit on control-C?</p>
<dd>
<dt>How do I open a file without blocking?</p>
<dd>
<dt>How do I tell the difference between errors from the shell and perl?</p>
<dd>
<dt>How do I install a module from <font SIZE="-1">CPAN</font>?</p>
<dd>
<dt>What&#8217;s the difference between require and use?</p>
<dd>
<dt>How do I keep my own module/library directory?</p>
<dd>
<dt>How do I add the directory my program lives in to the module/library search path?</p>
<dd>
<dt>How do I add a directory to my include path (@INC) at runtime?</p>
<dd>the <tt>&quot;PERLLIB&quot;</tt> environment variable, the <tt>&quot;PERL5LIB&quot;</tt> environment variable, the <tt>&quot;perl -Idir&quot;</tt> command line flag, the <tt>&quot;lib&quot;</tt> pragma:, the local::lib module:</p>
<dt>Where are modules installed?</p>
<dd>
<dt>What is socket.ph and where do I get it?</p>
<dd></dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt><font SIZE="-1">AUTHOR AND COPYRIGHT</font></p>
<dd></dl>
<h3>perlfaq9 &#8211; Web, Email and Networking</h3>
<dl COMPACT>
<dt><font SIZE="-1">VERSION</font></p>
<dd>
<dt><font SIZE="-1">DESCRIPTION</font></p>
<dd>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>Should I use a web framework?</p>
<dd>
<dt>Which web framework should I use?</p>
<dd>Catalyst, Dancer2, Mojolicious, Web::Simple</p>
<dt>What is Plack and <font SIZE="-1">PSGI</font>?</p>
<dd>
<dt>How do I remove <font SIZE="-1">HTML</font> from a string?</p>
<dd>
<dt>How do I extract URLs?</p>
<dd>
<dt>How do I fetch an <font SIZE="-1">HTML</font> file?</p>
<dd>
<dt>How do I automate an <font SIZE="-1">HTML</font> form submission?</p>
<dd>
<dt>How do I decode or create those %-encodings on the web?</p>
<dd>
<dt>How do I redirect to another page?</p>
<dd>
<dt>How do I put a password on my web pages?</p>
<dd>
<dt>How do I make sure users can&#8217;t enter values into a form that causes my <font SIZE="-1">CGI</font> script to do bad things?</p>
<dd>
<dt>How do I parse a mail header?</p>
<dd>
<dt>How do I check a valid mail address?</p>
<dd>
<dt>How do I decode a <font SIZE="-1">MIME/BASE64</font> string?</p>
<dd>
<dt>How do I find the user&#8217;s mail address?</p>
<dd>
<dt>How do I send email?</p>
<dd>Email::Sender::Transport::Sendmail, Email::Sender::Transport::SMTP</p>
<dt>How do I use <font SIZE="-1">MIME</font> to make an attachment to a mail message?</p>
<dd>
<dt>How do I read email?</p>
<dd>
<dt>How do I find out my hostname, domainname, or <font SIZE="-1">IP</font> address?</p>
<dd>
<dt>How do I fetch/put an (S)FTP file?</p>
<dd>
<dt>How can I do <font SIZE="-1">RPC</font> in Perl?</p>
<dd></dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt><font SIZE="-1">AUTHOR AND COPYRIGHT</font></p>
<dd></dl>
<h3>perlsyn &#8211; Perl syntax</h3>
<dl COMPACT>
<dt><font SIZE="-1">DESCRIPTION</font></p>
<dd>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>Declarations</p>
<dd>
<dt>Comments</p>
<dd>
<dt>Simple Statements</p>
<dd>
<dt>Statement Modifiers</p>
<dd>
<dt>Compound Statements</p>
<dd>
<dt>Loop Control</p>
<dd>
<dt>For Loops</p>
<dd>
<dt>Foreach Loops</p>
<dd>
<dt>Basic BLOCKs</p>
<dd>
<dt>Switch Statements</p>
<dd>
<dt>Goto</p>
<dd>
<dt>The Ellipsis Statement</p>
<dd>
<dt>PODs: Embedded Documentation</p>
<dd>
<dt>Plain Old Comments (Not!)</p>
<dd>
<dt>Experimental Details on given and when</p>
<dd>1, 2, 3, 4, 5, 6, 7, 8, 9, 10</dl>
</dl>
<dl COMPACT>
<dd></dl>
</dl>
<h3>perldata &#8211; Perl data types</h3>
<dl COMPACT>
<dt><font SIZE="-1">DESCRIPTION</font></p>
<dd>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>Variable names</p>
<dd>
<dt>Identifier parsing</p>
<dd>
<dt>Context</p>
<dd>
<dt>Scalar values</p>
<dd>
<dt>Scalar value constructors</p>
<dd>
<dt>List value constructors</p>
<dd>
<dt>Subscripts</p>
<dd>
<dt>Multi-dimensional array emulation</p>
<dd>
<dt>Slices</p>
<dd>
<dt>Typeglobs and Filehandles</p>
<dd></dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt><font SIZE="-1">SEE ALSO</font></p>
<dd></dl>
<h3>perlop &#8211; Perl operators and precedence</h3>
<dl COMPACT>
<dt><font SIZE="-1">DESCRIPTION</font></p>
<dd>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>Operator Precedence and Associativity</p>
<dd>
<dt>Terms and List Operators (Leftward)</p>
<dd>
<dt>The Arrow Operator</p>
<dd>
<dt>Auto-increment and Auto-decrement</p>
<dd>
<dt>Exponentiation</p>
<dd>
<dt>Symbolic Unary Operators</p>
<dd>
<dt>Binding Operators</p>
<dd>
<dt>Multiplicative Operators</p>
<dd>
<dt>Additive Operators</p>
<dd>
<dt>Shift Operators</p>
<dd>
<dt>Named Unary Operators</p>
<dd>
<dt>Relational Operators</p>
<dd>
<dt>Equality Operators</p>
<dd>
<dt>Smartmatch Operator</p>
<dd>1. Empty hashes or arrays match, 2. That is, each element smartmatches the element of the same index in the other array.[3], 3. If a circular reference is found, fall back to referential equality, 4. Either an actual number, or a string that looks like one</p>
<dt>Bitwise And</p>
<dd>
<dt>Bitwise Or and Exclusive Or</p>
<dd>
<dt>C-style Logical And</p>
<dd>
<dt>C-style Logical Or</p>
<dd>
<dt>Logical Defined-Or</p>
<dd>
<dt>Range Operators</p>
<dd>
<dt>Conditional Operator</p>
<dd>
<dt>Assignment Operators</p>
<dd>
<dt>Comma Operator</p>
<dd>
<dt>List Operators (Rightward)</p>
<dd>
<dt>Logical Not</p>
<dd>
<dt>Logical And</p>
<dd>
<dt>Logical or and Exclusive Or</p>
<dd>
<dt>C Operators Missing From Perl</p>
<dd>unary &amp;, unary *, (<font SIZE="-1">TYPE</font>)</p>
<dt>Quote and Quote-like Operators</p>
<dd>[1], [2], [3], [4], [5], [6], [7], [8]</p>
<dt>Regexp Quote-Like Operators</p>
<dd><tt>&quot;qr/</tt>STRING<tt>/msixpodualn&quot;</tt> , <tt>&quot;m/</tt>PATTERN<tt>/msixpodualngc&quot;</tt><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<br />
&nbsp;,&nbsp;<tt>&quot;/</tt>PATTERN<tt>/msixpodualngc&quot;</tt>, The empty pattern&nbsp;<tt>&quot;//&quot;</tt>, Matching in list context, <tt>&quot;\G </tt>assertion<tt>&quot;</tt>, <tt>&quot;m?</tt>PATTERN<tt>?msixpodualngc&quot;</tt><br />
&nbsp;, <tt>&quot;s/</tt>PATTERN<tt>/</tt>REPLACEMENT<tt>/msixpodualngcer&quot;</tt></p>
<dt>Quote-Like Operators</p>
<dd><tt>&quot;q/</tt>STRING<tt>/&quot;</tt> , <tt>'</tt>STRING<tt>'</tt>, <tt>&quot;qq/</tt>STRING<tt>/&quot;</tt> , &quot;<i></i><font SIZE="-1"><i>STRING</i></font><i></i>&quot;, <tt>&quot;qx/</tt>STRING<tt>/&quot;</tt> , <tt>&quot;`</tt>STRING<tt>`&quot;</tt>, <tt>&quot;qw/</tt>STRING<tt>/&quot;</tt> , <tt>&quot;tr/</tt>SEARCHLIST<tt>/</tt>REPLACEMENTLIST<tt>/cdsr&quot;</tt><br />
&nbsp;<wbr>&nbsp;,&nbsp;<tt>&quot;y/</tt>SEARCHLIST<tt>/</tt>REPLACEMENTLIST<tt>/cdsr&quot;</tt>,&nbsp;<tt>&quot;&lt;&lt;</tt>EOF<tt>&quot;</tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;, Double Quotes, Single Quotes, Backticks, Indented Here-docs</p>
<dt>Gory details of parsing quoted constructs</p>
<dd>Finding the end, Interpolation , <tt>&quot;&lt;&lt;'EOF'&quot;</tt>, <tt>&quot;m''&quot;</tt>, the pattern of <tt>&quot;s'''&quot;</tt>, <tt>''</tt>, <tt>&quot;q//&quot;</tt>, <tt>&quot;tr'''&quot;</tt>, <tt>&quot;y'''&quot;</tt>, the replacement of <tt>&quot;s'''&quot;</tt>, <tt>&quot;tr///&quot;</tt>, <tt>&quot;y///&quot;</tt>, <tt>&quot;&quot;</tt>, <tt>&quot;``&quot;</tt>, <tt>&quot;qq//&quot;</tt>, <tt>&quot;qx//&quot;</tt>, <tt>&quot;&lt;file*glob&gt;&quot;</tt>, <tt>&quot;&lt;&lt;&quot;EOF&quot;&quot;</tt>, the replacement of <tt>&quot;s///&quot;</tt>, <tt>&quot;RE&quot;</tt> in <tt>&quot;m?RE?&quot;</tt>, <tt>&quot;/RE/&quot;</tt>, <tt>&quot;m/RE/&quot;</tt>, <tt>&quot;s/RE/foo/&quot;</tt>,, parsing regular expressions , Optimization of regular expressions</p>
<dt>I/O Operators</p>
<dd>
<dt>Constant Folding</p>
<dd>
<dt>No-ops</p>
<dd>
<dt>Bitwise String Operators</p>
<dd>
<dt>Integer Arithmetic</p>
<dd>
<dt>Floating-point Arithmetic</p>
<dd>
<dt>Bigger Numbers</p>
<dd></dl>
</dl>
<dl COMPACT>
<dd></dl>
</dl>
<h3>perlsub &#8211; Perl subroutines</h3>
<dl COMPACT>
<dt><font SIZE="-1">SYNOPSIS</font></p>
<dd>
<dt><font SIZE="-1">DESCRIPTION</font></p>
<dd>documented later in this document, documented in perlmod, documented in perlobj, documented in perltie, documented in PerlIO::via, documented in perlfunc, documented in <font SIZE="-1">UNIVERSAL</font>, documented in perldebguts, undocumented, used internally by the overload feature</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>Signatures</p>
<dd>
<dt>Private Variables via <code>my()</code></p>
<dd>
<dt>Persistent Private Variables</p>
<dd>
<dt>Temporary Values via <code>local()</code></p>
<dd>
<dt>Lvalue subroutines</p>
<dd>
<dt>Lexical Subroutines</p>
<dd>
<dt>Passing Symbol Table Entries (typeglobs)</p>
<dd>
<dt>When to Still Use <code>local()</code></p>
<dd>
<dt>Pass by Reference</p>
<dd>
<dt>Prototypes</p>
<dd>
<dt>Constant Functions</p>
<dd>
<dt>Overriding Built-in Functions</p>
<dd>
<dt>Autoloading</p>
<dd>
<dt>Subroutine Attributes</p>
<dd></dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt><font SIZE="-1">SEE ALSO</font></p>
<dd></dl>
<h3>perlfunc &#8211; Perl builtin functions</h3>
<dl COMPACT>
<dt><font SIZE="-1">DESCRIPTION</font></p>
<dd>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>Perl Functions by Category</p>
<dd>Functions for SCALARs or strings , Regular expressions and pattern matching , Numeric functions , Functions for real <tt>@ARRAYs</tt> , Functions for list data , Functions for real <tt>%HASHes</tt> , Input and output functions<br />
&nbsp;<wbr>&nbsp;, Functions for fixed-length data or records, Functions for filehandles, files, or directories<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;, Keywords related to the control flow of your Perl program , Keywords related to scoping, Miscellaneous functions, Functions for processes and process groups<br />
&nbsp;<wbr>&nbsp;, Keywords related to Perl modules , Keywords related to classes and object-orientation<br />
&nbsp;, Low-level socket functions&nbsp;<wbr>&nbsp;, System V interprocess communication functions<br />
&nbsp;<wbr>&nbsp;, Fetching user and group info&nbsp;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;, Fetching network info , Time-related functions , Non-function keywords</p>
<dt>Portability</p>
<dd>
<dt>Alphabetical Listing of Perl Functions</p>
<dd>&#8211;<i>X</i> <font SIZE="-1">FILEHANDLE</font> </p>
<p> , &#8211;<i>X</i> <font SIZE="-1">EXPR,</font> &#8211;<i>X</i> <font SIZE="-1">DIRHANDLE,</font> &#8211;<i>X</i>, abs <font SIZE="-1">VALUE</font> , abs, accept <font SIZE="-1">NEWSOCKET,GENERICSOCKET</font> , alarm <font SIZE="-1">SECONDS</font> , alarm, atan2 Y,X , bind <font SIZE="-1">SOCKET,NAME</font> , binmode <font SIZE="-1">FILEHANDLE, LAYER</font><br />
&nbsp;, binmode&nbsp;<font SIZE="-1">FILEHANDLE,</font>&nbsp;bless&nbsp;<font SIZE="-1">REF,CLASSNAME</font>&nbsp;, bless <font SIZE="-1">REF,</font> break, caller <font SIZE="-1">EXPR</font> , caller, chdir <font SIZE="-1">EXPR</font> , chdir <font SIZE="-1">FILEHANDLE,</font> chdir <font SIZE="-1">DIRHANDLE,</font> chdir, chmod <font SIZE="-1">LIST</font> , chomp <font SIZE="-1">VARIABLE</font> , chomp( <font SIZE="-1">LIST</font> ), chomp, chop <font SIZE="-1">VARIABLE</font> , chop( <font SIZE="-1">LIST</font> ), chop, chown <font SIZE="-1">LIST</font><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;, chr&nbsp;<font SIZE="-1">NUMBER</font>&nbsp;<wbr>&nbsp;<wbr>&nbsp; , chr, chroot <font SIZE="-1">FILENAME</font> , chroot, close <font SIZE="-1">FILEHANDLE</font> , close, closedir <font SIZE="-1">DIRHANDLE</font> , connect <font SIZE="-1">SOCKET,NAME</font> , continue <font SIZE="-1">BLOCK</font> , continue, cos <font SIZE="-1">EXPR</font><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;, cos, crypt&nbsp;<font SIZE="-1">PLAINTEXT,SALT</font>&nbsp;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<br />
&nbsp;<wbr>&nbsp;, dbmclose&nbsp;<font SIZE="-1">HASH</font>&nbsp;, dbmopen <font SIZE="-1">HASH,DBNAME,MASK</font> , defined <font SIZE="-1">EXPR</font><br />
&nbsp;<wbr>&nbsp;, defined, delete&nbsp;<font SIZE="-1">EXPR</font>&nbsp;, die&nbsp;<font SIZE="-1">LIST</font><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;, do&nbsp;<font SIZE="-1">BLOCK</font>&nbsp; , do <font SIZE="-1">EXPR</font> , dump <font SIZE="-1">LABEL</font> , dump <font SIZE="-1">EXPR,</font> dump, each <font SIZE="-1">HASH</font> , each <font SIZE="-1">ARRAY</font> , eof <font SIZE="-1">FILEHANDLE</font> , eof (), eof, eval <font SIZE="-1">EXPR</font><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp; , eval <font SIZE="-1">BLOCK,</font> eval, String eval, Under the <tt>&quot;unicode_eval&quot;</tt> feature, Outside the <tt>&quot;unicode_eval&quot;</tt> feature, Block eval, evalbytes <font SIZE="-1">EXPR</font> , evalbytes, exec <font SIZE="-1">LIST</font> , exec <font SIZE="-1">PROGRAM LIST,</font> exists <font SIZE="-1">EXPR</font> , exit <font SIZE="-1">EXPR</font><br />
&nbsp;, exit, exp&nbsp;<font SIZE="-1">EXPR</font>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<br />
&nbsp;, exp, fc&nbsp;<font SIZE="-1">EXPR</font>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<br />
&nbsp;, fc, fcntl&nbsp;<font SIZE="-1">FILEHANDLE,FUNCTION,SCALAR</font>&nbsp;, __FILE__ , fileno <font SIZE="-1">FILEHANDLE</font> , fileno <font SIZE="-1">DIRHANDLE,</font> flock <font SIZE="-1">FILEHANDLE,OPERATION</font> , fork , format , formline <font SIZE="-1">PICTURE,LIST</font> , getc <font SIZE="-1">FILEHANDLE</font> , getc, getlogin<br />
&nbsp;, getpeername&nbsp;<font SIZE="-1">SOCKET</font>&nbsp;<wbr>&nbsp;, getpgrp <font SIZE="-1">PID</font> , getppid , getpriority <font SIZE="-1">WHICH,WHO</font> , getpwnam <font SIZE="-1">NAME</font><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;, getgrnam <font SIZE="-1">NAME,</font> gethostbyname <font SIZE="-1">NAME,</font> getnetbyname <font SIZE="-1">NAME,</font> getprotobyname <font SIZE="-1">NAME,</font> getpwuid <font SIZE="-1">UID,</font> getgrgid <font SIZE="-1">GID,</font> getservbyname <font SIZE="-1">NAME,PROTO,</font> gethostbyaddr <font SIZE="-1">ADDR,ADDRTYPE,</font> getnetbyaddr <font SIZE="-1">ADDR,ADDRTYPE,</font> getprotobynumber <font SIZE="-1">NUMBER,</font> getservbyport <font SIZE="-1">PORT,PROTO,</font> getpwent, getgrent, gethostent, getnetent, getprotoent, getservent, setpwent, setgrent, sethostent <font SIZE="-1">STAYOPEN,</font> setnetent <font SIZE="-1">STAYOPEN,</font> setprotoent <font SIZE="-1">STAYOPEN,</font> setservent <font SIZE="-1">STAYOPEN,</font> endpwent, endgrent, endhostent, endnetent, endprotoent, endservent, getsockname <font SIZE="-1">SOCKET</font> , getsockopt <font SIZE="-1">SOCKET,LEVEL,OPTNAME</font> , glob <font SIZE="-1">EXPR</font><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;, glob, gmtime&nbsp;<font SIZE="-1">EXPR</font><br />
&nbsp;<wbr>&nbsp;, gmtime, goto&nbsp;<font SIZE="-1">LABEL</font>&nbsp;<wbr>&nbsp;<wbr>&nbsp;, goto <font SIZE="-1">EXPR,</font> goto &amp;NAME, grep <font SIZE="-1">BLOCK LIST</font> , grep <font SIZE="-1">EXPR,LIST,</font> hex <font SIZE="-1">EXPR</font><br />
&nbsp;, hex, import&nbsp;<font SIZE="-1">LIST</font>&nbsp;, index <font SIZE="-1">STR,SUBSTR,POSITION</font> , index <font SIZE="-1">STR,SUBSTR,</font> int <font SIZE="-1">EXPR</font> , int, ioctl <font SIZE="-1">FILEHANDLE,FUNCTION,SCALAR</font> , join <font SIZE="-1">EXPR,LIST</font> , keys <font SIZE="-1">HASH</font><br />
&nbsp;, keys&nbsp;<font SIZE="-1">ARRAY,</font>&nbsp;kill&nbsp;<font SIZE="-1">SIGNAL, LIST,</font>&nbsp;kill&nbsp;<font SIZE="-1">SIGNAL</font>&nbsp; , last <font SIZE="-1">LABEL</font> , last <font SIZE="-1">EXPR,</font> last, lc <font SIZE="-1">EXPR</font> , lc, If <tt>&quot;use bytes&quot;</tt> is in effect:, Otherwise, if <tt>&quot;use locale&quot;</tt> for <tt>&quot;LC_CTYPE&quot;</tt> is in effect:, Otherwise, If <font SIZE="-1">EXPR</font> has the <font SIZE="-1">UTF8</font> flag set:, Otherwise, if <tt>&quot;use feature 'unicode_strings'&quot;</tt> or <tt>&quot;use locale ':not_characters'&quot;</tt> is in effect:, Otherwise:, lcfirst <font SIZE="-1">EXPR</font> , lcfirst, length <font SIZE="-1">EXPR</font> , length, __LINE__ , link <font SIZE="-1">OLDFILE,NEWFILE</font> , listen <font SIZE="-1">SOCKET,QUEUESIZE</font> , local <font SIZE="-1">EXPR</font> , localtime <font SIZE="-1">EXPR</font> , localtime, lock <font SIZE="-1">THING</font> , log <font SIZE="-1">EXPR</font> , log, lstat <font SIZE="-1">FILEHANDLE</font> , lstat <font SIZE="-1">EXPR,</font> lstat <font SIZE="-1">DIRHANDLE,</font> lstat, m//, map <font SIZE="-1">BLOCK LIST</font> , map <font SIZE="-1">EXPR,LIST,</font> mkdir <font SIZE="-1">FILENAME,MODE</font><br />
&nbsp;<wbr>&nbsp;, mkdir&nbsp;<font SIZE="-1">FILENAME,</font>&nbsp;mkdir, msgctl <font SIZE="-1">ID,CMD,ARG</font> , msgget <font SIZE="-1">KEY,FLAGS</font> , msgrcv <font SIZE="-1">ID,VAR,SIZE,TYPE,FLAGS</font> , msgsnd <font SIZE="-1">ID,MSG,FLAGS</font> , my <font SIZE="-1">VARLIST</font> , my <font SIZE="-1">TYPE VARLIST,</font> my <font SIZE="-1">VARLIST : ATTRS,</font> my <font SIZE="-1">TYPE VARLIST : ATTRS,</font> next <font SIZE="-1">LABEL</font> , next <font SIZE="-1">EXPR,</font> next, no <font SIZE="-1">MODULE VERSION LIST</font> , no <font SIZE="-1">MODULE VERSION,</font> no <font SIZE="-1">MODULE LIST,</font> no <font SIZE="-1">MODULE,</font> no <font SIZE="-1">VERSION,</font> oct <font SIZE="-1">EXPR</font> , oct, open <font SIZE="-1">FILEHANDLE,EXPR</font> , open <font SIZE="-1">FILEHANDLE,MODE,EXPR,</font> open <font SIZE="-1">FILEHANDLE,MODE,EXPR,LIST,</font> open <font SIZE="-1">FILEHANDLE,MODE,REFERENCE,</font> open <font SIZE="-1">FILEHANDLE,</font> opendir <font SIZE="-1">DIRHANDLE,EXPR</font> , ord <font SIZE="-1">EXPR</font> , ord, our <font SIZE="-1">VARLIST</font> , our <font SIZE="-1">TYPE VARLIST,</font> our <font SIZE="-1">VARLIST : ATTRS,</font> our <font SIZE="-1">TYPE VARLIST : ATTRS,</font> pack <font SIZE="-1">TEMPLATE,LIST</font> , package <font SIZE="-1">NAMESPACE,</font> package <font SIZE="-1">NAMESPACE VERSION</font><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;, package&nbsp;<font SIZE="-1">NAMESPACE BLOCK,</font> package <font SIZE="-1">NAMESPACE VERSION BLOCK</font> , __PACKAGE__ , pipe <font SIZE="-1">READHANDLE,WRITEHANDLE</font> , pop <font SIZE="-1">ARRAY</font> , pop, pos <font SIZE="-1">SCALAR</font> , pos, print <font SIZE="-1">FILEHANDLE LIST</font> , print <font SIZE="-1">FILEHANDLE,</font> print <font SIZE="-1">LIST,</font> print, printf <font SIZE="-1">FILEHANDLE FORMAT, LIST</font> , printf <font SIZE="-1">FILEHANDLE,</font> printf <font SIZE="-1">FORMAT, LIST,</font> printf, prototype <font SIZE="-1">FUNCTION</font> , prototype, push <font SIZE="-1">ARRAY,LIST</font> , q/STRING/, qq/STRING/, qw/STRING/, qx/STRING/, qr/STRING/, quotemeta <font SIZE="-1">EXPR</font> , quotemeta, rand <font SIZE="-1">EXPR</font> , rand, read <font SIZE="-1">FILEHANDLE,SCALAR,LENGTH,OFFSET</font> , read <font SIZE="-1">FILEHANDLE,SCALAR,LENGTH,</font> readdir <font SIZE="-1">DIRHANDLE</font> , readline <font SIZE="-1">EXPR,</font> readline , readlink <font SIZE="-1">EXPR</font> , readlink, readpipe <font SIZE="-1">EXPR,</font> readpipe , recv <font SIZE="-1">SOCKET,SCALAR,LENGTH,FLAGS</font> , redo <font SIZE="-1">LABEL</font> , redo <font SIZE="-1">EXPR,</font> redo, ref <font SIZE="-1">EXPR</font> , ref, rename <font SIZE="-1">OLDNAME,NEWNAME</font> , require <font SIZE="-1">VERSION</font> , require <font SIZE="-1">EXPR,</font> require, reset <font SIZE="-1">EXPR</font> , reset, return <font SIZE="-1">EXPR</font> , return, reverse <font SIZE="-1">LIST</font> , rewinddir <font SIZE="-1">DIRHANDLE</font> , rindex <font SIZE="-1">STR,SUBSTR,POSITION</font> , rindex <font SIZE="-1">STR,SUBSTR,</font> rmdir <font SIZE="-1">FILENAME</font> , rmdir, s///, say <font SIZE="-1">FILEHANDLE LIST</font> , say <font SIZE="-1">FILEHANDLE,</font> say <font SIZE="-1">LIST,</font> say, scalar <font SIZE="-1">EXPR</font> , seek <font SIZE="-1">FILEHANDLE,POSITION,WHENCE</font> , seekdir <font SIZE="-1">DIRHANDLE,POS</font> , select <font SIZE="-1">FILEHANDLE</font> , select, select <font SIZE="-1">RBITS,WBITS,EBITS,TIMEOUT</font> , semctl <font SIZE="-1">ID,SEMNUM,CMD,ARG</font> , semget <font SIZE="-1">KEY,NSEMS,FLAGS</font> , semop <font SIZE="-1">KEY,OPSTRING</font> , send <font SIZE="-1">SOCKET,MSG,FLAGS,TO</font> , send <font SIZE="-1">SOCKET,MSG,FLAGS,</font> setpgrp <font SIZE="-1">PID,PGRP</font><br />
&nbsp;, setpriority&nbsp;<font SIZE="-1">WHICH,WHO,PRIORITY</font>&nbsp;<br />
&nbsp;<wbr>&nbsp;, setsockopt&nbsp;<font SIZE="-1">SOCKET,LEVEL,OPTNAME,OPTVAL</font> , shift <font SIZE="-1">ARRAY</font> , shift, shmctl <font SIZE="-1">ID,CMD,ARG</font> , shmget <font SIZE="-1">KEY,SIZE,FLAGS</font> , shmread <font SIZE="-1">ID,VAR,POS,SIZE</font> , shmwrite <font SIZE="-1">ID,STRING,POS,SIZE,</font> shutdown <font SIZE="-1">SOCKET,HOW</font> , sin <font SIZE="-1">EXPR</font> , sin, sleep <font SIZE="-1">EXPR</font> , sleep, socket <font SIZE="-1">SOCKET,DOMAIN,TYPE,PROTOCOL</font> , socketpair <font SIZE="-1">SOCKET1,SOCKET2,DOMAIN,TYPE,PROTOCOL</font> , sort <font SIZE="-1">SUBNAME LIST</font> , sort <font SIZE="-1">BLOCK LIST,</font> sort <font SIZE="-1">LIST,</font> splice <font SIZE="-1">ARRAY,OFFSET,LENGTH,LIST</font> , splice <font SIZE="-1">ARRAY,OFFSET,LENGTH,</font> splice <font SIZE="-1">ARRAY,OFFSET,</font> splice <font SIZE="-1">ARRAY,</font> split /PATTERN/,EXPR,LIMIT , split /PATTERN/,EXPR, split /PATTERN/, split, sprintf <font SIZE="-1">FORMAT, LIST</font> , format parameter index, flags, vector flag, (minimum) width, precision, or maximum width , size, order of arguments, sqrt <font SIZE="-1">EXPR</font> , sqrt, srand <font SIZE="-1">EXPR</font> , srand, stat <font SIZE="-1">FILEHANDLE</font><br />
&nbsp;, stat&nbsp;<font SIZE="-1">EXPR,</font>&nbsp;stat&nbsp;<font SIZE="-1">DIRHANDLE,</font>&nbsp;stat, state&nbsp;<font SIZE="-1">VARLIST</font> , state <font SIZE="-1">TYPE VARLIST,</font> state <font SIZE="-1">VARLIST : ATTRS,</font> state <font SIZE="-1">TYPE VARLIST : ATTRS,</font> study <font SIZE="-1">SCALAR</font> , study, sub <font SIZE="-1">NAME BLOCK</font> , sub <font SIZE="-1">NAME</font> (<font SIZE="-1">PROTO</font>) <font SIZE="-1">BLOCK,</font> sub <font SIZE="-1">NAME : ATTRS BLOCK,</font> sub <font SIZE="-1">NAME</font> (<font SIZE="-1">PROTO</font>) : <font SIZE="-1">ATTRS BLOCK,</font> __SUB__ , substr <font SIZE="-1">EXPR,OFFSET,LENGTH,REPLACEMENT</font><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;, substr&nbsp;<font SIZE="-1">EXPR,OFFSET,LENGTH,</font>&nbsp;substr <font SIZE="-1">EXPR,OFFSET,</font> symlink <font SIZE="-1">OLDFILE,NEWFILE</font> , syscall <font SIZE="-1">NUMBER, LIST</font> , sysopen <font SIZE="-1">FILEHANDLE,FILENAME,MODE</font> , sysopen <font SIZE="-1">FILEHANDLE,FILENAME,MODE,PERMS,</font> sysread <font SIZE="-1">FILEHANDLE,SCALAR,LENGTH,OFFSET</font> , sysread <font SIZE="-1">FILEHANDLE,SCALAR,LENGTH,</font> sysseek <font SIZE="-1">FILEHANDLE,POSITION,WHENCE</font> , system <font SIZE="-1">LIST</font> , system <font SIZE="-1">PROGRAM LIST,</font> syswrite <font SIZE="-1">FILEHANDLE,SCALAR,LENGTH,OFFSET</font> , syswrite <font SIZE="-1">FILEHANDLE,SCALAR,LENGTH,</font> syswrite <font SIZE="-1">FILEHANDLE,SCALAR,</font> tell <font SIZE="-1">FILEHANDLE</font> , tell, telldir <font SIZE="-1">DIRHANDLE</font> , tie <font SIZE="-1">VARIABLE,CLASSNAME,LIST</font> , tied <font SIZE="-1">VARIABLE</font> , time , times , tr///, truncate <font SIZE="-1">FILEHANDLE,LENGTH</font> , truncate <font SIZE="-1">EXPR,LENGTH,</font> uc <font SIZE="-1">EXPR</font> , uc, ucfirst <font SIZE="-1">EXPR</font> , ucfirst, umask <font SIZE="-1">EXPR</font> , umask, undef <font SIZE="-1">EXPR</font> , undef, unlink <font SIZE="-1">LIST</font><br />
&nbsp;, unlink, unpack&nbsp;<font SIZE="-1">TEMPLATE,EXPR</font>&nbsp;, unpack&nbsp;<font SIZE="-1">TEMPLATE,</font> unshift <font SIZE="-1">ARRAY,LIST</font> , untie <font SIZE="-1">VARIABLE</font> , use Module <font SIZE="-1">VERSION LIST</font> , use Module <font SIZE="-1">VERSION,</font> use Module <font SIZE="-1">LIST,</font> use Module, use <font SIZE="-1">VERSION,</font> utime <font SIZE="-1">LIST</font> , values <font SIZE="-1">HASH</font> , values <font SIZE="-1">ARRAY,</font> vec <font SIZE="-1">EXPR,OFFSET,BITS</font> , wait , waitpid <font SIZE="-1">PID,FLAGS</font> , wantarray , warn <font SIZE="-1">LIST</font><br />
&nbsp;<wbr>&nbsp;, write&nbsp;<font SIZE="-1">FILEHANDLE</font>&nbsp;, write&nbsp;<font SIZE="-1">EXPR,</font>&nbsp;write, y///</p>
<dt>Non-function Keywords by Cross-reference</p>
<dd>__DATA__, __END__, <font SIZE="-1">BEGIN, CHECK, END, INIT, UNITCHECK, DESTROY,</font> and, cmp, eq, ge, gt, le, lt, ne, not, or, x, xor, <font SIZE="-1">AUTOLOAD,</font> else, elsif, for, foreach, if, unless, until, while, elseif, default, given, when</dl>
</dl>
<dl COMPACT>
<dd></dl>
</dl>
<h3>perlopentut &#8211; simple recipes for opening files and pipes in Perl</h3>
<dl COMPACT>
<dt><font SIZE="-1">DESCRIPTION</font></p>
<dd><i></i><font SIZE="-1"><i>OK</i></font><i></i>, <i></i><font SIZE="-1"><i>HANDLE</i></font><i></i>, <i></i><font SIZE="-1"><i>MODE</i></font><i></i>, <i></i><font SIZE="-1"><i>PATHNAME</i></font><i></i></p>
<dt>Opening Text Files</p>
<dd>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>Opening Text Files for Reading</p>
<dd>
<dt>Opening Text Files for Writing</p>
<dd></dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt>Opening Binary Files</p>
<dd>
<dt>Opening Pipes</p>
<dd>
<dt>Low-level File Opens via sysopen</p>
<dd>
<dt><font SIZE="-1">SEE ALSO</font></p>
<dd>
<dt><font SIZE="-1">AUTHOR</font> and <font SIZE="-1">COPYRIGHT</font></p>
<dd></dl>
<h3>perlpacktut &#8211; tutorial on pack and unpack</h3>
<dl COMPACT>
<dt><font SIZE="-1">DESCRIPTION</font></p>
<dd>
<dt>The Basic Principle</p>
<dd>
<dt>Packing Text</p>
<dd>
<dt>Packing Numbers</p>
<dd>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>Integers</p>
<dd>
<dt>Unpacking a Stack Frame</p>
<dd>
<dt>How to Eat an Egg on a Net</p>
<dd>
<dt>Byte-order modifiers</p>
<dd>
<dt>Floating point Numbers</p>
<dd></dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt>Exotic Templates</p>
<dd>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>Bit Strings</p>
<dd>
<dt>Uuencoding</p>
<dd>
<dt>Doing Sums</p>
<dd>
<dt>Unicode</p>
<dd>
<dt>Another Portable Binary Encoding</p>
<dd></dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt>Template Grouping</p>
<dd>
<dt>Lengths and Widths</p>
<dd>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>String Lengths</p>
<dd>
<dt>Dynamic Templates</p>
<dd>
<dt>Counting Repetitions</p>
<dd>
<dt>Intel <font SIZE="-1">HEX</font></p>
<dd></dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt>Packing and Unpacking C Structures</p>
<dd>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>The Alignment Pit</p>
<dd>
<dt>Dealing with Endian-ness</p>
<dd>
<dt>Alignment, Take 2</p>
<dd>
<dt>Alignment, Take 3</p>
<dd>
<dt>Pointers for How to Use Them</p>
<dd></dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt>Pack Recipes</p>
<dd>
<dt>Funnies Section</p>
<dd>
<dt>Authors</p>
<dd></dl>
<h3>perlpod &#8211; the Plain Old Documentation format</h3>
<dl COMPACT>
<dt><font SIZE="-1">DESCRIPTION</font></p>
<dd>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>Ordinary Paragraph</p>
<dd>
<dt>Verbatim Paragraph</p>
<dd>
<dt>Command Paragraph</p>
<dd><tt>&quot;=head1 </tt>Heading Text<tt>&quot;</tt><br />
&nbsp;<wbr>&nbsp;,&nbsp;<tt>&quot;=head2&nbsp;</tt>Heading Text<tt>&quot;</tt>,&nbsp;<tt>&quot;=head3&nbsp;</tt>Heading Text<tt>&quot;</tt>, <tt>&quot;=head4 </tt>Heading Text<tt>&quot;</tt>, <tt>&quot;=over </tt>indentlevel<tt>&quot;</tt><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;,&nbsp;<tt>&quot;=item&nbsp;</tt>stuff&#8230;<tt>&quot;</tt>,&nbsp;<tt>&quot;=back&quot;</tt>, <tt>&quot;=cut&quot;</tt> , <tt>&quot;=pod&quot;</tt> , <tt>&quot;=begin </tt>formatname<tt>&quot;</tt><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;,&nbsp;<tt>&quot;=end&nbsp;</tt>formatname<tt>&quot;</tt>, <tt>&quot;=for </tt>formatname<tt> </tt>text&#8230;<tt>&quot;</tt>, <tt>&quot;=encoding </tt>encodingname<tt>&quot;</tt></p>
<dt>Formatting Codes</p>
<dd><tt>&quot;I&lt;text&gt;&quot;</tt> &#8212; italic text , <tt>&quot;B&lt;text&gt;&quot;</tt> &#8212; bold text<br />
&nbsp;,&nbsp;<tt>&quot;C&lt;code&gt;&quot;</tt>&nbsp;&#8212; code text&nbsp;<br />
&nbsp;<wbr>&nbsp;,&nbsp;<tt>&quot;L&lt;name&gt;&quot;</tt>&nbsp;&#8212; a hyperlink , <tt>&quot;E&lt;escape&gt;&quot;</tt> &#8212; a character escape<br />
&nbsp;,&nbsp;<tt>&quot;F&lt;filename&gt;&quot;</tt>&nbsp;&#8212; used for filenames , <tt>&quot;S&lt;text&gt;&quot;</tt> &#8212; text contains non-breaking spaces<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;,&nbsp;<tt>&quot;X&lt;topic name&gt;&quot;</tt>&nbsp;&#8212; an index entry&nbsp;<wbr>&nbsp;<br />
&nbsp;,&nbsp;<tt>&quot;Z&lt;&gt;&quot;</tt>&nbsp;&#8212; a null (zero-effect) formatting code</p>
<dt>The Intent</p>
<dd>
<dt>Embedding Pods in Perl Modules</p>
<dd>
<dt>Hints for Writing Pod</p>
<dd></dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt><font SIZE="-1">SEE ALSO</font></p>
<dd>
<dt><font SIZE="-1">AUTHOR</font></p>
<dd></dl>
<h3>perlpodspec &#8211; Plain Old Documentation: format specification and notes</h3>
<dl COMPACT>
<dt><font SIZE="-1">DESCRIPTION</font></p>
<dd>
<dt>Pod Definitions</p>
<dd>
<dt>Pod Commands</p>
<dd>&#8220;=head1&#8221;, &#8220;=head2&#8221;, &#8220;=head3&#8221;, &#8220;=head4&#8221;, &#8220;=pod&#8221;, &#8220;=cut&#8221;, &#8220;=over&#8221;, &#8220;=item&#8221;, &#8220;=back&#8221;, &#8220;=begin formatname&#8221;, &#8220;=begin formatname parameter&#8221;, &#8220;=end formatname&#8221;, &#8220;=for formatname text&#8230;&#8221;, &#8220;=encoding encodingname&#8221;</p>
<dt>Pod Formatting Codes</p>
<dd><tt>&quot;I&lt;text&gt;&quot;</tt> &#8212; italic text, <tt>&quot;B&lt;text&gt;&quot;</tt> &#8212; bold text, <tt>&quot;C&lt;code&gt;&quot;</tt> &#8212; code text, <tt>&quot;F&lt;filename&gt;&quot;</tt> &#8212; style for filenames, <tt>&quot;X&lt;topic name&gt;&quot;</tt> &#8212; an index entry, <tt>&quot;Z&lt;&gt;&quot;</tt> &#8212; a null (zero-effect) formatting code, <tt>&quot;L&lt;name&gt;&quot;</tt> &#8212; a hyperlink, <tt>&quot;E&lt;escape&gt;&quot;</tt> &#8212; a character escape, <tt>&quot;S&lt;text&gt;&quot;</tt> &#8212; text contains non-breaking spaces</p>
<dt>Notes on Implementing Pod Processors</p>
<dd>
<dt>About L&lt;&#8230;&gt; Codes</p>
<dd>First:, Second:, Third:, Fourth:, Fifth:, Sixth:</p>
<dt>About =over&#8230;=back Regions</p>
<dd>
<dt>About Data Paragraphs and &quot;=begin/=end&quot; Regions</p>
<dd>
<dt><font SIZE="-1">SEE ALSO</font></p>
<dd>
<dt><font SIZE="-1">AUTHOR</font></p>
<dd></dl>
<h3>perlpodstyle &#8211; Perl <font SIZE="-1">POD</font> style guide</h3>
<dl COMPACT>
<dt><font SIZE="-1">DESCRIPTION</font></p>
<dd><font SIZE="-1">NAME, SYNOPSIS, DESCRIPTION, OPTIONS, RETURN VALUE, ERRORS, DIAGNOSTICS, EXAMPLES, ENVIRONMENT, FILES, CAVEATS, BUGS, RESTRICTIONS, NOTES, AUTHOR, HISTORY, COPYRIGHT AND LICENSE, SEE ALSO</font></p>
<dt><font SIZE="-1">AUTHOR</font></p>
<dd>
<dt><font SIZE="-1">COPYRIGHT AND LICENSE</font></p>
<dd>
<dt><font SIZE="-1">SEE ALSO</font></p>
<dd></dl>
<h3>perldiag &#8211; various Perl diagnostics</h3>
<dl COMPACT>
<dt><font SIZE="-1">DESCRIPTION</font></p>
<dd>
<dt><font SIZE="-1">SEE ALSO</font></p>
<dd></dl>
<h3>perldeprecation &#8211; list Perl deprecations</h3>
<dl COMPACT>
<dt><font SIZE="-1">DESCRIPTION</font></p>
<dd>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>Perl 5.32</p>
<dd>
<dt>Perl 5.30</p>
<dd>
<dt>Perl 5.28</p>
<dd>
<dt>Perl 5.26</p>
<dd>
<dt>Perl 5.24</p>
<dd>
<dt>Perl 5.16</p>
<dd></dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt><font SIZE="-1">SEE ALSO</font></p>
<dd></dl>
<h3>perllexwarn &#8211; Perl Lexical Warnings</h3>
<dl COMPACT>
<dt><font SIZE="-1">DESCRIPTION</font></p>
<dd></dl>
<h3>perldebug &#8211; Perl debugging</h3>
<dl COMPACT>
<dt><font SIZE="-1">DESCRIPTION</font></p>
<dd>
<dt>The Perl Debugger</p>
<dd>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>Calling the Debugger</p>
<dd>perl -d program_name, perl -d -e 0, perl -d:ptkdb program_name, perl -dt threaded_program_name</p>
<dt>Debugger Commands</p>
<dd>h , h [command], h h, p expr , x [maxdepth] expr , V [pkg [vars]] , X [vars] , y [level [vars]] , T , s [expr] , n [expr] , r , &lt;<font SIZE="-1">CR</font>&gt;, c [line|sub] , l , l min+incr, l min-max, l line, l subname, &#8211; , v [line] , . , f filename , /pattern/, ?pattern?, L [abw] , S [[!]regex] , t [n] , t [n] expr , b , b [line] [condition] , b [file]:[line] [condition] , b subname [condition] , b postpone subname [condition] , b load filename<br />
&nbsp;, b compile subname&nbsp; , B line , B *<br />
&nbsp;, disable&nbsp;[file]:[line]&nbsp;<br />
&nbsp;, disable&nbsp;[line]&nbsp;<br />
&nbsp;, enable&nbsp;[file]:[line]&nbsp;<br />
&nbsp;, enable&nbsp;[line]&nbsp;<br />
&nbsp;, a&nbsp;[line]&nbsp;command , A line , A&nbsp;*&nbsp;, w expr , W expr , W * , o , o booloption &#8230; , o anyoption? &#8230; , o option=value &#8230; , &lt; ? , &lt; [ command ] , &lt; * , &lt;&lt; command , &gt; ? , &gt; command , &gt; * , &gt;&gt; command , { ? , { [ command ], { * , &#123;&#123; command , ! number , ! -number , ! pattern , !! cmd , source file , H -number , q or ^D , R , |dbcmd , ||dbcmd , command, m expr , M , man [manpage]</p>
<dt>Configurable Options</p>
<dd><tt>&quot;recallCommand&quot;</tt>, <tt>&quot;ShellBang&quot;</tt> , <tt>&quot;pager&quot;</tt> , <tt>&quot;tkRunning&quot;</tt> , <tt>&quot;signalLevel&quot;</tt>, <tt>&quot;warnLevel&quot;</tt>, <tt>&quot;dieLevel&quot;</tt><br />
&nbsp;<wbr>&nbsp;,&nbsp;<tt>&quot;AutoTrace&quot;</tt>&nbsp;,&nbsp;<tt>&quot;LineInfo&quot;</tt> , <tt>&quot;inhibit_exit&quot;</tt> , <tt>&quot;PrintRet&quot;</tt> , <tt>&quot;ornaments&quot;</tt> , <tt>&quot;frame&quot;</tt> , <tt>&quot;maxTraceLen&quot;</tt> , <tt>&quot;windowSize&quot;</tt> , <tt>&quot;arrayDepth&quot;</tt>, <tt>&quot;hashDepth&quot;</tt> , <tt>&quot;dumpDepth&quot;</tt> , <tt>&quot;compactDump&quot;</tt>, <tt>&quot;veryCompact&quot;</tt> , <tt>&quot;globPrint&quot;</tt> , <tt>&quot;DumpDBFiles&quot;</tt> , <tt>&quot;DumpPackages&quot;</tt> , <tt>&quot;DumpReused&quot;</tt> , <tt>&quot;quote&quot;</tt>, <tt>&quot;HighBit&quot;</tt>, <tt>&quot;undefPrint&quot;</tt><br />
&nbsp;,&nbsp;<tt>&quot;UsageOnly&quot;</tt> , <tt>&quot;HistFile&quot;</tt> , <tt>&quot;HistSize&quot;</tt> , <tt>&quot;TTY&quot;</tt> , <tt>&quot;noTTY&quot;</tt> , <tt>&quot;ReadLine&quot;</tt> , <tt>&quot;NonStop&quot;</tt></p>
<dt>Debugger Input/Output</p>
<dd>Prompt, Multiline commands, Stack backtrace , Line Listing Format, Frame listing</p>
<dt>Debugging Compile-Time Statements</p>
<dd>
<dt>Debugger Customization</p>
<dd>
<dt>Readline Support / History in the Debugger</p>
<dd>
<dt>Editor Support for Debugging</p>
<dd>
<dt>The Perl Profiler</p>
<dd></dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt>Debugging Regular Expressions</p>
<dd>
<dt>Debugging Memory Usage</p>
<dd>
<dt><font SIZE="-1">SEE ALSO</font></p>
<dd>
<dt><font SIZE="-1">BUGS</font></p>
<dd></dl>
<h3>perlvar &#8211; Perl predefined variables</h3>
<dl COMPACT>
<dt><font SIZE="-1">DESCRIPTION</font></p>
<dd>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>The Syntax of Variable Names</p>
<dd></dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt><font SIZE="-1">SPECIAL VARIABLES</font></p>
<dd>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>General Variables</p>
<dd><tt>$ARG</tt>, <tt>$_</tt> , <tt>@ARG</tt>, <tt>@_</tt> , <tt>$LIST_SEPARATOR</tt>, $&quot; , <tt>$PROCESS_ID</tt>, <tt>$PID</tt>, $$ , <tt>$PROGRAM_NAME</tt>, <tt>$0</tt> , <tt>$REAL_GROUP_ID</tt>, <tt>$GID</tt>, $(<br />
&nbsp;,&nbsp;<tt>$EFFECTIVE_GROUP_ID</tt>,&nbsp;<tt>$EGID</tt>,&nbsp;$)&nbsp;<wbr>&nbsp; , <tt>$REAL_USER_ID</tt>, <tt>$UID</tt>, $&lt; , <tt>$EFFECTIVE_USER_ID</tt>, <tt>$EUID</tt>, $&gt; , <tt>$SUBSCRIPT_SEPARATOR</tt>, <tt>$SUBSEP</tt>, $; , <tt>$a</tt>, <tt>$b</tt> , <tt>%ENV</tt> , <tt>$OLD_PERL_VERSION</tt>, $] , <tt>$SYSTEM_FD_MAX</tt>, $^F<br />
&nbsp;,&nbsp;<tt>@F</tt>&nbsp;,&nbsp;<tt>@INC</tt>&nbsp;,&nbsp;<tt>%INC</tt>&nbsp;, <tt>$INPLACE_EDIT</tt>, $^I , <tt>@ISA</tt> , $^M , <tt>$OSNAME</tt>, $^O , <tt>%SIG</tt> , <tt>$BASETIME</tt>, $^T , <tt>$PERL_VERSION</tt>, $^V , ${^WIN32_SLOPPY_STAT} , <tt>$EXECUTABLE_NAME</tt>, $^X</p>
<dt>Variables related to regular expressions</p>
<dd>$&lt;<i>digits</i>&gt; ($1, <tt>$2</tt>, &#8230;) , @{^CAPTURE}<br />
&nbsp;,&nbsp;<tt>$MATCH</tt>,&nbsp;$&amp;&nbsp;<wbr>&nbsp;,&nbsp;${^MATCH} , <tt>$PREMATCH</tt>, $` , ${^PREMATCH} , <tt>$POSTMATCH</tt>, $&#8217;<br />
&nbsp;,&nbsp;${^POSTMATCH}&nbsp;<wbr>&nbsp;<wbr>&nbsp;, <tt>$LAST_PAREN_MATCH</tt>, $+ , <tt>$LAST_SUBMATCH_RESULT</tt>, $^N , <tt>@LAST_MATCH_END</tt>, @+ , %{^CAPTURE}, <tt>%LAST_PAREN_MATCH</tt>, %+<br />
&nbsp;,&nbsp;<tt>@LAST_MATCH_START</tt>,&nbsp;@-&nbsp; , <tt>&quot;$`&quot;</tt> is the same as <tt>&quot;substr($var, 0, $-[0])&quot;</tt>, <tt>$&amp;</tt> is the same as <tt>&quot;substr($var, $-[0], $+[0] - $-[0])&quot;</tt>, <tt>&quot;$'&quot;</tt> is the same as <tt>&quot;substr($var, $+[0])&quot;</tt>, <tt>$1</tt> is the same as <tt>&quot;substr($var, $-[1], $+[1] - $-[1])&quot;</tt>, <tt>$2</tt> is the same as <tt>&quot;substr($var, $-[2], $+[2] - $-[2])&quot;</tt>, <tt>$3</tt> is the same as <tt>&quot;substr($var, $-[3], $+[3] - $-[3])&quot;</tt>, %{^CAPTURE_ALL} , %- , <tt>$LAST_REGEXP_CODE_RESULT</tt>, $^R , ${^RE_COMPILE_RECURSION_LIMIT} , ${^RE_DEBUG_FLAGS} , ${^RE_TRIE_MAXBUF}</p>
<dt>Variables related to filehandles</p>
<dd><tt>$ARGV</tt> , <tt>@ARGV</tt> , <font SIZE="-1">ARGV</font> , <font SIZE="-1">ARGVOUT</font> , IO::Handle-&gt;output_field_separator( <font SIZE="-1">EXPR</font> ), <tt>$OUTPUT_FIELD_SEPARATOR</tt>, <tt>$OFS</tt>, $, , <font SIZE="-1">HANDLE-</font>&gt;input_line_number( <font SIZE="-1">EXPR</font> ), <tt>$INPUT_LINE_NUMBER</tt>, <tt>$NR</tt>, $. , IO::Handle-&gt;input_record_separator( <font SIZE="-1">EXPR</font> ), <tt>$INPUT_RECORD_SEPARATOR</tt>, <tt>$RS</tt>, $/ , IO::Handle-&gt;output_record_separator( <font SIZE="-1">EXPR</font> ), <tt>$OUTPUT_RECORD_SEPARATOR</tt>, <tt>$ORS</tt>, $\ , <font SIZE="-1">HANDLE-</font>&gt;autoflush( <font SIZE="-1">EXPR</font> ), <tt>$OUTPUT_AUTOFLUSH</tt>, $| , ${^LAST_FH} , <tt>$ACCUMULATOR</tt>, $^A , IO::Handle-&gt;format_formfeed(<font SIZE="-1">EXPR</font>), <tt>$FORMAT_FORMFEED</tt>, $^L , <font SIZE="-1">HANDLE-</font>&gt;format_page_number(<font SIZE="-1">EXPR</font>), <tt>$FORMAT_PAGE_NUMBER</tt>, $% , <font SIZE="-1">HANDLE-</font>&gt;format_lines_left(<font SIZE="-1">EXPR</font>), <tt>$FORMAT_LINES_LEFT</tt>, $- , IO::Handle-&gt;format_line_break_characters <font SIZE="-1">EXPR, <tt>$FORMAT_LINE_BREAK_CHARACTERS</tt>, <tt>$:</tt></font> , <font SIZE="-1">HANDLE-</font>&gt;format_lines_per_page(<font SIZE="-1">EXPR</font>), <tt>$FORMAT_LINES_PER_PAGE</tt>, $= , <font SIZE="-1">HANDLE-</font>&gt;format_top_name(<font SIZE="-1">EXPR</font>), <tt>$FORMAT_TOP_NAME</tt>, $^ , <font SIZE="-1">HANDLE-</font>&gt;format_name(<font SIZE="-1">EXPR</font>), <tt>$FORMAT_NAME</tt>, $~</p>
<dt>Error Variables</p>
<dd>${^CHILD_ERROR_NATIVE} , <tt>$EXTENDED_OS_ERROR</tt>, $^E<br />
&nbsp;,&nbsp;<tt>$EXCEPTIONS_BEING_CAUGHT</tt>,&nbsp;$^S&nbsp; , <tt>$WARNING</tt>, $^W , ${^WARNING_BITS} , <tt>$OS_ERROR</tt>, <tt>$ERRNO</tt>, $! , <tt>%OS_ERROR</tt>, <tt>%ERRNO</tt>, %! , <tt>$CHILD_ERROR</tt>, $? , <tt>$EVAL_ERROR</tt>, $@</p>
<dt>Variables related to the interpreter state</p>
<dd><tt>$COMPILING</tt>, $^C , <tt>$DEBUGGING</tt>, $^D , ${^ENCODING} , ${^GLOBAL_PHASE} , <font SIZE="-1">CONSTRUCT, START, CHECK, INIT, RUN, END, DESTRUCT,</font> $^H , %^H , ${^OPEN} , <tt>$PERLDB</tt>, $^P , 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x100, 0x200, 0x400, 0x800, 0x1000, ${^TAINT} , ${^SAFE_LOCALES} , ${^UNICODE} , ${^UTF8CACHE} , ${^UTF8LOCALE}</p>
<dt>Deprecated and removed variables</p>
<dd>$# , $* , $[</dl>
</dl>
<dl COMPACT>
<dd></dl>
</dl>
<h3>perlre &#8211; Perl regular expressions</h3>
<dl COMPACT>
<dt><font SIZE="-1">DESCRIPTION</font></p>
<dd>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>The Basics</p>
<dd>
<dt>Modifiers</p>
<dd>&quot;m&quot; , &quot;s&quot; , &quot;i&quot; , &quot;x&quot; and &quot;xx&quot; , &quot;p&quot; , &quot;a&quot;, &quot;d&quot;, &quot;l&quot;, and &quot;u&quot;<br />
&nbsp;<wbr>&nbsp;,&nbsp;&quot;n&quot;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;, Other Modifiers</p>
<dt>Regular Expressions</p>
<dd>[1], [2], [3], [4], [5], [6], [7], [8]</p>
<dt>Quoting metacharacters</p>
<dd>
<dt>Extended Patterns</p>
<dd><tt>&quot;(?#</tt>text<tt>)&quot;</tt> , <tt>&quot;(?adlupimnsx-imnsx)&quot;</tt>, <tt>&quot;(?^alupimnsx)&quot;</tt> , <tt>&quot;(?:</tt>pattern<tt>)&quot;</tt> , <tt>&quot;(?adluimnsx-imnsx:</tt>pattern<tt>)&quot;</tt>, <tt>&quot;(?^aluimnsx:</tt>pattern<tt>)&quot;</tt> , <tt>&quot;(?|</tt>pattern<tt>)&quot;</tt> , Lookaround Assertions , <tt>&quot;(?=</tt>pattern<tt>)&quot;</tt>, <tt>&quot;(*pla:</tt>pattern<tt>)&quot;</tt>, <tt>&quot;(*positive_lookahead:</tt>pattern<tt>)&quot;</tt><br />
&nbsp;<wbr>&nbsp;, <tt>&quot;(?!</tt>pattern<tt>)&quot;</tt>, <tt>&quot;(*nla:</tt>pattern<tt>)&quot;</tt>, <tt>&quot;(*negative_lookahead:</tt>pattern<tt>)&quot;</tt><br />
&nbsp;<wbr>&nbsp;, <tt>&quot;(?&lt;=</tt>pattern<tt>)&quot;</tt>, <tt>&quot;\K&quot;</tt>, <tt>&quot;(*plb:</tt>pattern<tt>)&quot;</tt>, <tt>&quot;(*positive_lookbehind:</tt>pattern<tt>)&quot;</tt><br />
&nbsp;<wbr>&nbsp; , <tt>&quot;(?&lt;!</tt>pattern<tt>)&quot;</tt>, <tt>&quot;(*nlb:</tt>pattern<tt>)&quot;</tt>, <tt>&quot;(*negative_lookbehind:</tt>pattern<tt>)&quot;</tt><br />
&nbsp;<wbr>&nbsp;, <tt>&quot;(?&lt;</tt>NAME<tt>&gt;</tt>pattern<tt>)&quot;</tt>, <tt>&quot;(?'</tt>NAME<tt>'</tt>pattern<tt>)&quot;</tt><br />
&nbsp;<wbr>&nbsp;,&nbsp;<tt>&quot;\k&lt;</tt>NAME<tt>&gt;&quot;</tt>,&nbsp;<tt>&quot;\k'</tt>NAME<tt>'&quot;</tt>,&nbsp;<tt>&quot;(?{&nbsp;</tt>code<tt>&nbsp;})&quot;</tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;,&nbsp;<tt>&quot;(??{&nbsp;</tt>code<tt>&nbsp;})&quot;</tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;, <tt>&quot;(?</tt>PARNO<tt>)&quot;</tt> <tt>&quot;(?-</tt>PARNO<tt>)&quot;</tt> <tt>&quot;(?+</tt>PARNO<tt>)&quot;</tt> <tt>&quot;(?R)&quot;</tt> <tt>&quot;(?0)&quot;</tt><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<br />
&nbsp;<wbr>&nbsp;<br />
&nbsp;<wbr>&nbsp;,&nbsp;<tt>&quot;(?&amp;</tt>NAME<tt>)&quot;</tt> , <tt>&quot;(?(</tt>condition<tt>)</tt>yes-pattern<tt>|</tt>no-pattern<tt>)&quot;</tt> , <tt>&quot;(?(</tt>condition<tt>)</tt>yes-pattern<tt>)&quot;</tt>, an integer in parentheses, a lookahead/lookbehind/evaluate zero-width assertion;, a name in angle brackets or single quotes, the special symbol <tt>&quot;(R)&quot;</tt>, <tt>&quot;(1)&quot;</tt> <tt>&quot;(2)&quot;</tt> .., <tt>&quot;(&lt;</tt>NAME<tt>&gt;)&quot;</tt> <tt>&quot;('</tt>NAME<tt>')&quot;</tt>, <tt>&quot;(?=...)&quot;</tt> <tt>&quot;(?!...)&quot;</tt> <tt>&quot;(?&lt;=...)&quot;</tt> <tt>&quot;(?&lt;!...)&quot;</tt>, <tt>&quot;(?{ </tt>CODE<tt> })&quot;</tt>, <tt>&quot;(R)&quot;</tt>, <tt>&quot;(R1)&quot;</tt> <tt>&quot;(R2)&quot;</tt> .., <tt>&quot;(R&amp;</tt>NAME<tt>)&quot;</tt>, <tt>&quot;(DEFINE)&quot;</tt>, <tt>&quot;(?&gt;</tt>pattern<tt>)&quot;</tt>, <tt>&quot;(*atomic:</tt>pattern<tt>)&quot;</tt><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp; , <tt>&quot;(?[ ])&quot;</tt></p>
<dt>Backtracking</p>
<dd>
<dt>Script Runs</p>
<dd>
<dt>Special Backtracking Control Verbs</p>
<dd>Verbs, <tt>&quot;(*PRUNE)&quot;</tt> <tt>&quot;(*PRUNE:</tt>NAME<tt>)&quot;</tt> , <tt>&quot;(*SKIP)&quot;</tt> <tt>&quot;(*SKIP:</tt>NAME<tt>)&quot;</tt> , <tt>&quot;(*MARK:</tt>NAME<tt>)&quot;</tt> <tt>&quot;(*:</tt>NAME<tt>)&quot;</tt><br />
&nbsp;<wbr>&nbsp;,&nbsp;<tt>&quot;(*THEN)&quot;</tt>&nbsp;<tt>&quot;(*THEN:</tt>NAME<tt>)&quot;</tt>, <tt>&quot;(*COMMIT)&quot;</tt> <tt>&quot;(*COMMIT:</tt>arg<tt>)&quot;</tt> , <tt>&quot;(*FAIL)&quot;</tt> <tt>&quot;(*F)&quot;</tt> <tt>&quot;(*FAIL:</tt>arg<tt>)&quot;</tt> , <tt>&quot;(*ACCEPT)&quot;</tt> <tt>&quot;(*ACCEPT:</tt>arg<tt>)&quot;</tt></p>
<dt>Warning on &quot;\1&quot; Instead of $1</p>
<dd>
<dt>Repeated Patterns Matching a Zero-length Substring</p>
<dd>
<dt>Combining <font SIZE="-1">RE</font> Pieces</p>
<dd><tt>&quot;ST&quot;</tt>, <tt>&quot;S|T&quot;</tt>, <tt>&quot;S{REPEAT_COUNT}&quot;</tt>, <tt>&quot;S{min,max}&quot;</tt>, <tt>&quot;S{min,max}?&quot;</tt>, <tt>&quot;S?&quot;</tt>, <tt>&quot;S*&quot;</tt>, <tt>&quot;S+&quot;</tt>, <tt>&quot;S??&quot;</tt>, <tt>&quot;S*?&quot;</tt>, <tt>&quot;S+?&quot;</tt>, <tt>&quot;(?&gt;S)&quot;</tt>, <tt>&quot;(?=S)&quot;</tt>, <tt>&quot;(?&lt;=S)&quot;</tt>, <tt>&quot;(?!S)&quot;</tt>, <tt>&quot;(?&lt;!S)&quot;</tt>, <tt>&quot;(??{ </tt>EXPR<tt> })&quot;</tt>, <tt>&quot;(?</tt>PARNO<tt>)&quot;</tt>, <tt>&quot;(?(</tt>condition<tt>)</tt>yes-pattern<tt>|</tt>no-pattern<tt>)&quot;</tt></p>
<dt>Creating Custom <font SIZE="-1">RE</font> Engines</p>
<dd>
<dt>Embedded Code Execution Frequency</p>
<dd>
<dt>PCRE/Python Support</p>
<dd><tt>&quot;(?P&lt;</tt>NAME<tt>&gt;</tt>pattern<tt>)&quot;</tt>, <tt>&quot;(?P=</tt>NAME<tt>)&quot;</tt>, <tt>&quot;(?P&gt;</tt>NAME<tt>)&quot;</tt></dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt><font SIZE="-1">BUGS</font></p>
<dd>
<dt><font SIZE="-1">SEE ALSO</font></p>
<dd></dl>
<h3>perlrebackslash &#8211; Perl Regular Expression Backslash Sequences and Escapes</h3>
<dl COMPACT>
<dt><font SIZE="-1">DESCRIPTION</font></p>
<dd>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>The backslash</p>
<dd>[1]</p>
<dt>All the sequences and escapes</p>
<dd>
<dt>Character Escapes</p>
<dd>[1], [2]</p>
<dt>Modifiers</p>
<dd>
<dt>Character classes</p>
<dd>
<dt>Referencing</p>
<dd>
<dt>Assertions</p>
<dd>\A, \z, \Z, \G, {}, , \B{}, \B, <tt>&quot;{gcb}&quot;</tt> or <tt>&quot;{g}&quot;</tt>, <tt>&quot;{lb}&quot;</tt>, <tt>&quot;{sb}&quot;</tt>, <tt>&quot;{wb}&quot;</tt></p>
<dt>Misc</p>
<dd>\K, \N, \R , \X</dl>
</dl>
<dl COMPACT>
<dd></dl>
</dl>
<h3>perlrecharclass &#8211; Perl Regular Expression Character Classes</h3>
<dl COMPACT>
<dt><font SIZE="-1">DESCRIPTION</font></p>
<dd>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>The dot</p>
<dd>
<dt>Backslash sequences</p>
<dd>If the <tt>&quot;/a&quot;</tt> modifier is in effect .., otherwise .., For code points above 255 .., For code points below 256 .., if locale rules are in effect .., if, instead, Unicode rules are in effect .., otherwise .., If the <tt>&quot;/a&quot;</tt> modifier is in effect .., otherwise .., For code points above 255 .., For code points below 256 .., if locale rules are in effect .., if, instead, Unicode rules are in effect .., otherwise .., [1], [2]</p>
<dt>Bracketed Character Classes</p>
<dd>[1], [2], [3], [4], [5], [6], [7], If the <tt>&quot;/a&quot;</tt> modifier, is in effect .., otherwise .., For code points above 255 .., For code points below 256 .., if locale rules are in effect .., <tt>&quot;word&quot;</tt>, <tt>&quot;ascii&quot;</tt>, <tt>&quot;blank&quot;</tt>, if, instead, Unicode rules are in effect .., otherwise ..</dl>
</dl>
<dl COMPACT>
<dd></dl>
</dl>
<h3>perlreref &#8211; Perl Regular Expressions Reference</h3>
<dl COMPACT>
<dt><font SIZE="-1">DESCRIPTION</font></p>
<dd>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><font SIZE="-1">OPERATORS</font></p>
<dd>
<dt><font SIZE="-1">SYNTAX</font></p>
<dd>
<dt><font SIZE="-1">ESCAPE SEQUENCES</font></p>
<dd>
<dt><font SIZE="-1">CHARACTER CLASSES</font></p>
<dd>
<dt><font SIZE="-1">ANCHORS</font></p>
<dd>
<dt><font SIZE="-1">QUANTIFIERS</font></p>
<dd>
<dt><font SIZE="-1">EXTENDED CONSTRUCTS</font></p>
<dd>
<dt><font SIZE="-1">VARIABLES</font></p>
<dd>
<dt><font SIZE="-1">FUNCTIONS</font></p>
<dd>
<dt><font SIZE="-1">TERMINOLOGY</font></p>
<dd></dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt><font SIZE="-1">AUTHOR</font></p>
<dd>
<dt><font SIZE="-1">SEE ALSO</font></p>
<dd>
<dt><font SIZE="-1">THANKS</font></p>
<dd></dl>
<h3>perlref &#8211; Perl references and nested data structures</h3>
<dl COMPACT>
<dt><font SIZE="-1">NOTE</font></p>
<dd>
<dt><font SIZE="-1">DESCRIPTION</font></p>
<dd>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>Making References</p>
<dd>1. , 2.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;, 3.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<br />
&nbsp;<wbr>&nbsp;, 4.&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;, 5.&nbsp;<wbr>&nbsp;, 6. , 7.</p>
<dt>Using References</p>
<dd>
<dt>Circular References</p>
<dd>
<dt>Symbolic references</p>
<dd>
<dt>Not-so-symbolic references</p>
<dd>
<dt>Pseudo-hashes: Using an array as a hash</p>
<dd>
<dt>Function Templates</p>
<dd></dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt><font SIZE="-1">WARNING:</font> Don&#8217;t use references as hash keys</p>
<dd>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>Postfix Dereference Syntax</p>
<dd>
<dt>Postfix Reference Slicing</p>
<dd>
<dt>Assigning to References</p>
<dd></dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt>Declaring a Reference to a Variable</p>
<dd>
<dt><font SIZE="-1">SEE ALSO</font></p>
<dd></dl>
<h3>perlform &#8211; Perl formats</h3>
<dl COMPACT>
<dt><font SIZE="-1">DESCRIPTION</font></p>
<dd>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>Text Fields</p>
<dd>
<dt>Numeric Fields</p>
<dd>
<dt>The Field @* for Variable-Width Multi-Line Text</p>
<dd>
<dt>The Field ^* for Variable-Width One-line-at-a-time Text</p>
<dd>
<dt>Specifying Values</p>
<dd>
<dt>Using Fill Mode</p>
<dd>
<dt>Suppressing Lines Where All Fields Are Void</p>
<dd>
<dt>Repeating Format Lines</p>
<dd>
<dt>Top of Form Processing</p>
<dd>
<dt>Format Variables</p>
<dd></dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt><font SIZE="-1">NOTES</font></p>
<dd>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>Footers</p>
<dd>
<dt>Accessing Formatting Internals</p>
<dd></dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt><font SIZE="-1">WARNINGS</font></p>
<dd></dl>
<h3>perlobj &#8211; Perl object reference</h3>
<dl COMPACT>
<dt><font SIZE="-1">DESCRIPTION</font></p>
<dd>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>An Object is Simply a Data Structure</p>
<dd>
<dt>A Class is Simply a Package</p>
<dd>
<dt>A Method is Simply a Subroutine</p>
<dd>
<dt>Method Invocation</p>
<dd>
<dt>Inheritance</p>
<dd>
<dt>Writing Constructors</p>
<dd>
<dt>Attributes</p>
<dd>
<dt>An Aside About Smarter and Safer Code</p>
<dd>
<dt>Method Call Variations</p>
<dd>
<dt>Invoking Class Methods</p>
<dd>
<dt>&quot;bless&quot;, &quot;blessed&quot;, and &quot;ref&quot;</p>
<dd>
<dt>The <font SIZE="-1">UNIVERSAL</font> Class</p>
<dd>isa($class) , <font SIZE="-1">DOES</font>($role) , can($method) , <font SIZE="-1">VERSION</font>($need)</p>
<dt><font SIZE="-1">AUTOLOAD</font></p>
<dd>
<dt>Destructors</p>
<dd>
<dt>Non-Hash Objects</p>
<dd>
<dt>Inside-Out objects</p>
<dd>
<dt>Pseudo-hashes</p>
<dd></dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt><font SIZE="-1">SEE ALSO</font></p>
<dd></dl>
<h3>perltie &#8211; how to hide an object class in a simple variable</h3>
<dl COMPACT>
<dt><font SIZE="-1">SYNOPSIS</font></p>
<dd>
<dt><font SIZE="-1">DESCRIPTION</font></p>
<dd>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>Tying Scalars</p>
<dd><font SIZE="-1">TIESCALAR</font> classname, <font SIZE="-1">LIST</font> , <font SIZE="-1">FETCH</font> this , <font SIZE="-1">STORE</font> this, value , <font SIZE="-1">UNTIE</font> this , <font SIZE="-1">DESTROY</font> this</p>
<dt>Tying Arrays</p>
<dd><font SIZE="-1">TIEARRAY</font> classname, <font SIZE="-1">LIST</font> , <font SIZE="-1">FETCH</font> this, index , <font SIZE="-1">STORE</font> this, index, value , <font SIZE="-1">FETCHSIZE</font> this , <font SIZE="-1">STORESIZE</font> this, count , <font SIZE="-1">EXTEND</font> this, count , <font SIZE="-1">EXISTS</font> this, key , <font SIZE="-1">DELETE</font> this, key , <font SIZE="-1">CLEAR</font> this , <font SIZE="-1">PUSH</font> this, <font SIZE="-1">LIST</font><br />
&nbsp;,&nbsp;<font SIZE="-1">POP</font>&nbsp;this ,&nbsp;<font SIZE="-1">SHIFT</font>&nbsp;this ,&nbsp;<font SIZE="-1">UNSHIFT</font>&nbsp;this,&nbsp;<font SIZE="-1">LIST</font>&nbsp; , <font SIZE="-1">SPLICE</font> this, offset, length, <font SIZE="-1">LIST</font> , <font SIZE="-1">UNTIE</font> this , <font SIZE="-1">DESTROY</font> this</p>
<dt>Tying Hashes</p>
<dd><font SIZE="-1">USER, HOME, CLOBBER, LIST, TIEHASH</font> classname, <font SIZE="-1">LIST</font> , <font SIZE="-1">FETCH</font> this, key , <font SIZE="-1">STORE</font> this, key, value , <font SIZE="-1">DELETE</font> this, key , <font SIZE="-1">CLEAR</font> this , <font SIZE="-1">EXISTS</font> this, key , <font SIZE="-1">FIRSTKEY</font> this , <font SIZE="-1">NEXTKEY</font> this, lastkey , <font SIZE="-1">SCALAR</font> this , <font SIZE="-1">UNTIE</font> this , <font SIZE="-1">DESTROY</font> this</p>
<dt>Tying FileHandles</p>
<dd><font SIZE="-1">TIEHANDLE</font> classname, <font SIZE="-1">LIST</font> , <font SIZE="-1">WRITE</font> this, <font SIZE="-1">LIST</font> , <font SIZE="-1">PRINT</font> this, <font SIZE="-1">LIST</font> , <font SIZE="-1">PRINTF</font> this, <font SIZE="-1">LIST</font> , <font SIZE="-1">READ</font> this, <font SIZE="-1">LIST</font> , <font SIZE="-1">READLINE</font> this , <font SIZE="-1">GETC</font> this , <font SIZE="-1">EOF</font> this , <font SIZE="-1">CLOSE</font> this , <font SIZE="-1">UNTIE</font> this , <font SIZE="-1">DESTROY</font> this</p>
<dt><font SIZE="-1">UNTIE</font> this</p>
<dd>
<dt>The &quot;untie&quot; Gotcha</p>
<dd></dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt><font SIZE="-1">SEE ALSO</font></p>
<dd>
<dt><font SIZE="-1">BUGS</font></p>
<dd>
<dt><font SIZE="-1">AUTHOR</font></p>
<dd></dl>
<h3>perldbmfilter &#8211; Perl <font SIZE="-1">DBM</font> Filters</h3>
<dl COMPACT>
<dt><font SIZE="-1">SYNOPSIS</font></p>
<dd>
<dt><font SIZE="-1">DESCRIPTION</font></p>
<dd><code>filter_store_key</code>, <code>filter_store_value</code>, <code>filter_fetch_key</code>, <code>filter_fetch_value</code></p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>The Filter</p>
<dd>
<dt>An Example: the <font SIZE="-1">NULL</font> termination problem.</p>
<dd>
<dt>Another Example: Key is a C int.</p>
<dd></dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt><font SIZE="-1">SEE ALSO</font></p>
<dd>
<dt><font SIZE="-1">AUTHOR</font></p>
<dd></dl>
<h3>perlipc &#8211; Perl interprocess communication (signals, fifos, pipes, safe subprocesses, sockets, and semaphores)</h3>
<dl COMPACT>
<dt><font SIZE="-1">DESCRIPTION</font></p>
<dd>
<dt>Signals</p>
<dd>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>Handling the <font SIZE="-1">SIGHUP</font> Signal in Daemons</p>
<dd>
<dt>Deferred Signals (Safe Signals)</p>
<dd>Long-running opcodes, Interrupting <font SIZE="-1">IO,</font> Restartable system calls, Signals as &#8220;faults&#8221;, Signals triggered by operating system state</dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt>Named Pipes</p>
<dd>
<dt>Using <code>open()</code> for <font SIZE="-1">IPC</font></p>
<dd>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>Filehandles</p>
<dd>
<dt>Background Processes</p>
<dd>
<dt>Complete Dissociation of Child from Parent</p>
<dd>
<dt>Safe Pipe Opens</p>
<dd>
<dt>Avoiding Pipe Deadlocks</p>
<dd>
<dt>Bidirectional Communication with Another Process</p>
<dd>
<dt>Bidirectional Communication with Yourself</p>
<dd></dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt>Sockets: Client/Server Communication</p>
<dd>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>Internet Line Terminators</p>
<dd>
<dt>Internet <font SIZE="-1">TCP</font> Clients and Servers</p>
<dd>
<dt>Unix-Domain <font SIZE="-1">TCP</font> Clients and Servers</p>
<dd></dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt><font SIZE="-1">TCP</font> Clients with IO::Socket</p>
<dd>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>A Simple Client</p>
<dd><tt>&quot;Proto&quot;</tt>, <tt>&quot;PeerAddr&quot;</tt>, <tt>&quot;PeerPort&quot;</tt></p>
<dt>A Webget Client</p>
<dd>
<dt>Interactive Client with IO::Socket</p>
<dd></dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt><font SIZE="-1">TCP</font> Servers with IO::Socket</p>
<dd>Proto, LocalPort, Listen, Reuse</p>
<dt><font SIZE="-1">UDP:</font> Message Passing</p>
<dd>
<dt>SysV <font SIZE="-1">IPC</font></p>
<dd>
<dt><font SIZE="-1">NOTES</font></p>
<dd>
<dt><font SIZE="-1">BUGS</font></p>
<dd>
<dt><font SIZE="-1">AUTHOR</font></p>
<dd>
<dt><font SIZE="-1">SEE ALSO</font></p>
<dd></dl>
<h3>perlfork &#8211; Perl&#8217;s <code>fork()</code> emulation</h3>
<dl COMPACT>
<dt><font SIZE="-1">SYNOPSIS</font></p>
<dd>
<dt><font SIZE="-1">DESCRIPTION</font></p>
<dd>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>Behavior of other Perl features in forked pseudo-processes</p>
<dd>$$ or <tt>$PROCESS_ID</tt>, <tt>%ENV</tt>, <code>chdir()</code> and all other builtins that accept filenames, <code>wait()</code> and <code>waitpid()</code>, <code>kill()</code>, <code>exec()</code>, <code>exit()</code>, Open handles to files, directories and network sockets</p>
<dt>Resource limits</p>
<dd>
<dt>Killing the parent process</p>
<dd>
<dt>Lifetime of the parent process and pseudo-processes</p>
<dd></dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt><font SIZE="-1">CAVEATS AND LIMITATIONS</font></p>
<dd><font SIZE="-1">BEGIN</font> blocks, Open filehandles, Open directory handles, Forking pipe <code>open()</code> not yet implemented, Global state maintained by XSUBs, Interpreter embedded in larger application, Thread-safety of extensions</p>
<dt><font SIZE="-1">PORTABILITY CAVEATS</font></p>
<dd>
<dt><font SIZE="-1">BUGS</font></p>
<dd>
<dt><font SIZE="-1">AUTHOR</font></p>
<dd>
<dt><font SIZE="-1">SEE ALSO</font></p>
<dd></dl>
<h3>perlnumber &#8211; semantics of numbers and numeric operations in Perl</h3>
<dl COMPACT>
<dt><font SIZE="-1">SYNOPSIS</font></p>
<dd>
<dt><font SIZE="-1">DESCRIPTION</font></p>
<dd>
<dt>Storing numbers</p>
<dd>
<dt>Numeric operators and numeric conversions</p>
<dd>
<dt>Flavors of Perl numeric operations</p>
<dd>Arithmetic operators, ++, Arithmetic operators during <tt>&quot;use integer&quot;</tt>, Other mathematical operators, Bitwise operators, Bitwise operators during <tt>&quot;use integer&quot;</tt>, Operators which expect an integer, Operators which expect a string</p>
<dt><font SIZE="-1">AUTHOR</font></p>
<dd>
<dt><font SIZE="-1">SEE ALSO</font></p>
<dd></dl>
<h3>perlthrtut &#8211; Tutorial on threads in Perl</h3>
<dl COMPACT>
<dt><font SIZE="-1">DESCRIPTION</font></p>
<dd>
<dt>What Is A Thread Anyway?</p>
<dd>
<dt>Threaded Program Models</p>
<dd>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>Boss/Worker</p>
<dd>
<dt>Work Crew</p>
<dd>
<dt>Pipeline</p>
<dd></dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt>What kind of threads are Perl threads?</p>
<dd>
<dt>Thread-Safe Modules</p>
<dd>
<dt>Thread Basics</p>
<dd>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>Basic Thread Support</p>
<dd>
<dt>A Note about the Examples</p>
<dd>
<dt>Creating Threads</p>
<dd>
<dt>Waiting For A Thread To Exit</p>
<dd>
<dt>Ignoring A Thread</p>
<dd>
<dt>Process and Thread Termination</p>
<dd></dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt>Threads And Data</p>
<dd>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>Shared And Unshared Data</p>
<dd>
<dt>Thread Pitfalls: Races</p>
<dd></dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt>Synchronization and control</p>
<dd>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>Controlling access: <code>lock()</code></p>
<dd>
<dt>A Thread Pitfall: Deadlocks</p>
<dd>
<dt>Queues: Passing Data Around</p>
<dd>
<dt>Semaphores: Synchronizing Data Access</p>
<dd>
<dt>Basic semaphores</p>
<dd>
<dt>Advanced Semaphores</p>
<dd>
<dt>Waiting for a Condition</p>
<dd>
<dt>Giving up control</p>
<dd></dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt>General Thread Utility Routines</p>
<dd>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>What Thread Am I In?</p>
<dd>
<dt>Thread IDs</p>
<dd>
<dt>Are These Threads The Same?</p>
<dd>
<dt>What Threads Are Running?</p>
<dd></dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt>A Complete Example</p>
<dd>
<dt>Different implementations of threads</p>
<dd>
<dt>Performance considerations</p>
<dd>
<dt>Process-scope Changes</p>
<dd>
<dt>Thread-Safety of System Libraries</p>
<dd>
<dt>Conclusion</p>
<dd>
<dt><font SIZE="-1">SEE ALSO</font></p>
<dd>
<dt>Bibliography</p>
<dd>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>Introductory Texts</p>
<dd>
<dt>OS-Related References</p>
<dd>
<dt>Other References</p>
<dd></dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt>Acknowledgements</p>
<dd>
<dt><font SIZE="-1">AUTHOR</font></p>
<dd>
<dt>Copyrights</p>
<dd></dl>
<h3>perlport &#8211; Writing portable Perl</h3>
<dl COMPACT>
<dt><font SIZE="-1">DESCRIPTION</font></p>
<dd>Not all Perl programs have to be portable, Nearly all of Perl already <i>is</i> portable</p>
<dt><font SIZE="-1">ISSUES</font></p>
<dd>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>Newlines</p>
<dd>
<dt>Numbers endianness and Width</p>
<dd>
<dt>Files and Filesystems</p>
<dd>
<dt>System Interaction</p>
<dd>
<dt>Command names versus file pathnames</p>
<dd>
<dt>Networking</p>
<dd>
<dt>Interprocess Communication (<font SIZE="-1">IPC</font>)</p>
<dd>
<dt>External Subroutines (<font SIZE="-1">XS</font>)</p>
<dd>
<dt>Standard Modules</p>
<dd>
<dt>Time and Date</p>
<dd>
<dt>Character sets and character encoding</p>
<dd>
<dt>Internationalisation</p>
<dd>
<dt>System Resources</p>
<dd>
<dt>Security</p>
<dd>
<dt>Style</p>
<dd></dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt><font SIZE="-1">CPAN</font> Testers</p>
<dd>
<dt><font SIZE="-1">PLATFORMS</font></p>
<dd>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>Unix</p>
<dd>
<dt><font SIZE="-1">DOS</font> and Derivatives</p>
<dd>
<dt><font SIZE="-1">VMS</font></p>
<dd>
<dt><font SIZE="-1">VOS</font></p>
<dd>
<dt><font SIZE="-1">EBCDIC</font> Platforms</p>
<dd>
<dt>Acorn <font SIZE="-1">RISC OS</font></p>
<dd>
<dt>Other perls</p>
<dd></dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt><font SIZE="-1">FUNCTION IMPLEMENTATIONS</font></p>
<dd>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>Alphabetical Listing of Perl Functions</p>
<dd>&#8211;<i>X</i>, alarm, atan2, binmode, chmod, chown, chroot, crypt, dbmclose, dbmopen, dump, exec, exit, fcntl, flock, fork, getlogin, getpgrp, getppid, getpriority, getpwnam, getgrnam, getnetbyname, getpwuid, getgrgid, getnetbyaddr, getprotobynumber, getpwent, getgrent, gethostbyname, gethostent, getnetent, getprotoent, getservent, seekdir, sethostent, setnetent, setprotoent, setservent, endpwent, endgrent, endhostent, endnetent, endprotoent, endservent, getsockopt, glob, gmtime, ioctl, kill, link, localtime, lstat, msgctl, msgget, msgsnd, msgrcv, open, readlink, rename, rewinddir, select, semctl, semget, semop, setgrent, setpgrp, setpriority, setpwent, setsockopt, shmctl, shmget, shmread, shmwrite, sleep, socketpair, stat, symlink, syscall, sysopen, system, telldir, times, truncate, umask, utime, wait, waitpid</dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt>Supported Platforms</p>
<dd>Linux (x86, <font SIZE="-1">ARM, IA64</font>), HP-UX, <font SIZE="-1">AIX,</font> Win32, Windows 2000, Windows <font SIZE="-1">XP,</font> Windows Server 2003, Windows Vista, Windows Server 2008, Windows 7, Cygwin, Solaris (x86, <font SIZE="-1">SPARC</font>), OpenVMS, Alpha (7.2 and later), I64 (8.2 and later), Symbian, NetBSD, FreeBSD, Debian GNU/kFreeBSD, Haiku, Irix (6.5. What else?), OpenBSD, Dragonfly <font SIZE="-1">BSD,</font> Midnight <font SIZE="-1">BSD, QNX</font> Neutrino <font SIZE="-1">RTOS</font> (6.5.0), MirOS <font SIZE="-1">BSD,</font> Stratus OpenVOS (17.0 or later), time_t issues that may or may not be fixed, Symbian (Series 60 v3, 3.2 and 5 &#8211; what else?), Stratus <font SIZE="-1">VOS /</font> OpenVOS, <font SIZE="-1">AIX,</font> Android, FreeMINT</p>
<dt><font SIZE="-1">EOL</font> Platforms</p>
<dd>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>(Perl 5.20)</p>
<dd><font SIZE="-1">AT&amp;T</font> 3b1</p>
<dt>(Perl 5.14)</p>
<dd>Windows 95, Windows 98, Windows <font SIZE="-1">ME,</font> Windows <font SIZE="-1">NT4</font></p>
<dt>(Perl 5.12)</p>
<dd>Atari MiNT, Apollo Domain/OS, Apple Mac <font SIZE="-1">OS 8/9,</font> Tenon Machten</dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt>Supported Platforms (Perl 5.8)</p>
<dd>
<dt><font SIZE="-1">SEE ALSO</font></p>
<dd>
<dt><font SIZE="-1">AUTHORS / CONTRIBUTORS</font></p>
<dd></dl>
<h3>perllocale &#8211; Perl locale handling (internationalization and localization)</h3>
<dl COMPACT>
<dt><font SIZE="-1">DESCRIPTION</font></p>
<dd>
<dt><font SIZE="-1">WHAT IS A LOCALE</font></p>
<dd>Category <tt>&quot;LC_NUMERIC&quot;</tt>: Numeric formatting, Category <tt>&quot;LC_MONETARY&quot;</tt>: Formatting of monetary amounts, Category <tt>&quot;LC_TIME&quot;</tt>: Date/Time formatting, Category <tt>&quot;LC_MESSAGES&quot;</tt>: Error and other messages, Category <tt>&quot;LC_COLLATE&quot;</tt>: Collation, Category <tt>&quot;LC_CTYPE&quot;</tt>: Character Types, Other categories</p>
<dt><font SIZE="-1">PREPARING TO USE LOCALES</font></p>
<dd>
<dt><font SIZE="-1">USING LOCALES</font></p>
<dd>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>The &quot;use locale&quot; pragma</p>
<dd><code>Not within the scope of </code>&quot;use locale&quot;, <code>Lingering effects of </code>&quot;use locale&quot;, <code>Under </code>&quot;&quot;use locale&quot;;&quot;</p>
<dt>The setlocale function</p>
<dd>
<dt>Multi-threaded operation</p>
<dd>
<dt>Finding locales</p>
<dd>
<dt><font SIZE="-1">LOCALE PROBLEMS</font></p>
<dd>
<dt>Testing for broken locales</p>
<dd>
<dt>Temporarily fixing locale problems</p>
<dd>
<dt>Permanently fixing locale problems</p>
<dd>
<dt>Permanently fixing your system&#8217;s locale configuration</p>
<dd>
<dt>Fixing system locale configuration</p>
<dd>
<dt>The localeconv function</p>
<dd>
<dt>I18N::Langinfo</p>
<dd></dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt><font SIZE="-1">LOCALE CATEGORIES</font></p>
<dd>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>Category &quot;LC_COLLATE&quot;: Collation: Text Comparisons and Sorting</p>
<dd>
<dt>Category &quot;LC_CTYPE&quot;: Character Types</p>
<dd>
<dt>Category &quot;LC_NUMERIC&quot;: Numeric Formatting</p>
<dd>
<dt>Category &quot;LC_MONETARY&quot;: Formatting of monetary amounts</p>
<dd>
<dt>Category &quot;LC_TIME&quot;: Respresentation of time</p>
<dd>
<dt>Other categories</p>
<dd></dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt><font SIZE="-1">SECURITY</font></p>
<dd>
<dt><font SIZE="-1">ENVIRONMENT</font></p>
<dd><font SIZE="-1">PERL_SKIP_LOCALE_INIT, PERL_BADLANG, DPKG_RUNNING_VERSION,</font> <tt>&quot;LC_ALL&quot;</tt>, <tt>&quot;LANGUAGE&quot;</tt>, <tt>&quot;LC_CTYPE&quot;</tt>, <tt>&quot;LC_COLLATE&quot;</tt>, <tt>&quot;LC_MONETARY&quot;</tt>, <tt>&quot;LC_NUMERIC&quot;</tt>, <tt>&quot;LC_TIME&quot;</tt>, <tt>&quot;LANG&quot;</tt></p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>Examples</p>
<dd></dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt><font SIZE="-1">NOTES</font></p>
<dd>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>String &quot;eval&quot; and &quot;LC_NUMERIC&quot;</p>
<dd>
<dt>Backward compatibility</p>
<dd>
<dt>I18N:Collate obsolete</p>
<dd>
<dt>Sort speed and memory use impacts</p>
<dd>
<dt>Freely available locale definitions</p>
<dd>
<dt>I18n and l10n</p>
<dd>
<dt>An imperfect standard</p>
<dd></dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt>Unicode and <font SIZE="-1">UTF-8</font></p>
<dd>
<dt><font SIZE="-1">BUGS</font></p>
<dd>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>Collation of strings containing embedded &quot;NUL&quot; characters</p>
<dd>
<dt>Multi-threaded</p>
<dd>
<dt>Broken systems</p>
<dd></dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt><font SIZE="-1">SEE ALSO</font></p>
<dd>
<dt><font SIZE="-1">HISTORY</font></p>
<dd></dl>
<h3>perluniintro &#8211; Perl Unicode introduction</h3>
<dl COMPACT>
<dt><font SIZE="-1">DESCRIPTION</font></p>
<dd>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>Unicode</p>
<dd>
<dt>Perl&#8217;s Unicode Support</p>
<dd>
<dt>Perl&#8217;s Unicode Model</p>
<dd>
<dt>Unicode and <font SIZE="-1">EBCDIC</font></p>
<dd>
<dt>Creating Unicode</p>
<dd>
<dt>Handling Unicode</p>
<dd>
<dt>Legacy Encodings</p>
<dd>
<dt>Unicode I/O</p>
<dd>
<dt>Displaying Unicode As Text</p>
<dd>
<dt>Special Cases</p>
<dd>
<dt>Advanced Topics</p>
<dd>
<dt>Miscellaneous</p>
<dd>
<dt>Questions With Answers</p>
<dd>
<dt>Hexadecimal Notation</p>
<dd>
<dt>Further Resources</p>
<dd></dl>
</dl>
<dl COMPACT>
<dd></dl>
<dt><font SIZE="-1">UNICODE IN OLDER PERLS</font></p>
<dd>
<dt><font SIZE="-1">SEE ALSO</font></p>
<dd>
<dt><font SIZE="-1">ACKNOWLEDGMENTS</font></p>
<dd>
<dt><font SIZE="-1">AUTHOR, COPYRIGHT, AND LICENSE</font></p>
<dd></dl>
<h3>perlunicode &#8211; Unicode support in Perl</h3>
<dl COMPACT>
<dt><font SIZE="-1">DESCRIPTION</font></p>
<dd>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>Important Caveats</p>
<dd>Safest if you <tt>&quot;use feature 'unicode_strings'&quot;</tt>, Input and Output Layers, You must convert your non-ASCII, non-UTF-8 Perl scripts to be <font SIZE="-1">UTF-8,</font> <tt>&quot;use utf8&quot;</tt> still needed to enable <font SIZE="-1">UTF-8</font> in scripts, <font SIZE="-1">UTF-16</font> scripts autodetected</p>
<dt>Byte and Character Semantics</p>
<dd>
<dt><font SIZE="-1">ASCII</font> Rules versus Unicode Rules</p>
<dd>When the string has been upgraded to <font SIZE="-1">UTF-8,</font> There are additional methods for regular expression patterns</p>
<dt>Extended Grapheme Clusters (Logical characters)</p>
<dd>
<dt>Unicode Character Properties</p>
<dd>&quot;\p{All}&quot;, &quot;\p{Alnum}&quot;, &quot;\p{Any}&quot;, &quot;\p{ASCII}&quot;, &quot;\p{Assigned}&quot;, &quot;\p{Blank}&quot;, &quot;\p{Decomposition_Type: Non_Canonical}&quot; (Short: <tt>&quot;\p{Dt=NonCanon}&quot;</tt>), &quot;\p{Graph}&quot;, &quot;\p{HorizSpace}&quot;, &quot;\p{In=*}&quot;, &quot;\p{PerlSpace}&quot;, &quot;\p{PerlWord}&quot;, &quot;\p{Posix&#8230;}&quot;, &quot;\p{Present_In: *}&quot; (Short: <tt>&quot;\p{In=*}&quot;</tt>), &quot;\p{Print}&quot;, &quot;\p{SpacePerl}&quot;, &quot;\p{Title}&quot; and &quot;\p{Titlecase}&quot;, &quot;\p{Unicode}&quot;, &quot;\p{VertSpace}&quot;, &quot;\p{Word}&quot;, &quot;\p{XPosix&#8230;}&quot;</p>
<dt>Wildcards in Property Values</p>
<dd>
<dt>User-Defined Character Properties</p>
<dd>
<dt>User-Defined Case Mappings (for serious hackers only)</p>
<dd>
<dt>Character Encodings for Input and Output</p>
<dd>
<dt>Unicode Regular Expression Support Level</p>
<dd>[1] <tt>&quot;\N{U+...}&quot;</tt> and <tt>&quot;
