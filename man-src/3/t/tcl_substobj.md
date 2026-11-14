---
title: "tcl_substobj(3)"
name: "tcl_substobj"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tcl_substobj/"
description: "Tcl_SubstObj – perform substitutions on Tcl objects"
---

<p>Tcl_SubstObj &#8211; perform substitutions on Tcl objects </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tcl.h&gt;</code>
Tcl_Obj *
<code>Tcl_SubstObj</code>(<i>interp, objPtr, flags</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tcl_Interp <i>*interp</i> (in) Interpreter in which to execute Tcl scripts and lookup variables. If an error occurs, the interpreter&#8217;s result is modified to hold an error message.</p>
<dd>Tcl_Obj <i>*objPtr</i> (in) A Tcl object containing the string to perform substitutions on.</p>
<dd>int <i>flags</i> (in) ORed combination of flag bits that specify which substitutions to perform. The flags <code>TCL_SUBST_COMMANDS</code>, <code>TCL_SUBST_VARIABLES</code> and <code>TCL_SUBST_BACKSLASHES</code> are currently supported, and <code>TCL_SUBST_ALL</code> is provided as a convenience for the common case where all substitutions are desired.
</dl>
<h2>Description</h2>
<p>The <code>Tcl_SubstObj</code> function is used to perform substitutions on strings in the fashion of the <code>subst</code> command. It gets the value of the string contained in <i>objPtr</i> and scans it, copying characters and performing the chosen substitutions as it goes to an output object which is returned as the result of the function. In the event of an error occurring during the execution of a command or variable substitution, the function returns NULL and an error message is left in <i>interp</i>&#8216;s result. </p>
<p> Three kinds of substitutions are supported. When the <code>TCL_SUBST_BACKSLASHES</code> bit is set in <i>flags</i>, sequences that look like backslash substitutions for Tcl commands are replaced by their corresponding character. </p>
<p> When the <code>TCL_SUBST_VARIABLES</code> bit is set in <i>flags</i>, sequences that look like variable substitutions for Tcl commands are replaced by the contents of the named variable. </p>
<p> When the <code>TCL_SUBST_COMMANDS</code> bit is set in <i>flags</i>, sequences that look like command substitutions for Tcl commands are replaced by the result of evaluating that script. Where an uncaught &#8220;continue exception&#8221; occurs during the evaluation of a command substitution, an empty string is substituted for the command. Where an uncaught &#8220;break exception&#8221; occurs during the evaluation of a command substitution, the result of the whole substitution on <i>objPtr</i> will be truncated at the point immediately before the start of the command substitution, and no characters will be added to the result or substitutions performed after that point.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/n-subst/">subst</a>(n)</p>
<h2>Keywords</h2>
<p>backslash substitution, command substitution, variable substitution</p>
