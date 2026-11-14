---
title: "tcl_wrongnumargs(3)"
name: "tcl_wrongnumargs"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tcl_wrongnumargs/"
description: "Tcl_WrongNumArgs – generate standard error message for wrong number of arguments"
---

<p>Tcl_WrongNumArgs &#8211; generate standard error message for wrong number of arguments </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tcl.h&gt;</code>
<code>Tcl_WrongNumArgs</code>(<i>interp, objc, objv, message</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tcl_Interp <i>interp</i> (in) Interpreter in which error will be reported: error message gets stored in its result object.</p>
<dd>int <i>objc</i> (in) Number of leading arguments from <i>objv</i> to include in error message.</p>
<dd>Tcl_Obj *const <i>objv[]</i> (in) Arguments to command that had the wrong number of arguments.</p>
<dd>const char <i>*message</i> (in) Additional error information to print after leading arguments from <i>objv</i>. This typically gives the acceptable syntax of the command. This argument may be NULL. </p>
</dl>
<h2>Description</h2>
<p><code>Tcl_WrongNumArgs</code> is a utility procedure that is invoked by command procedures when they discover that they have received the wrong number of arguments. <code>Tcl_WrongNumArgs</code> generates a standard error message and stores it in the result object of <i>interp</i>. The message includes the <i>objc</i> initial elements of <i>objv</i> plus <i>message</i>. For example, if <i>objv</i> consists of the values <code>foo</code> and <code>bar</code>, <i>objc</i> is 1, and <i>message</i> is &#8220;<code>fileName count</code>&#8221; then <i>interp</i>&#8216;s result object will be set to the following string:</p>
<dl COMPACT>
<dd>
<pre>wrong # args: should be &quot;foo fileName count&quot;</pre>
</dl>
<p> If <i>objc</i> is 2, the result will be set to the following string:</p>
<dl COMPACT>
<dd>
<pre>wrong # args: should be &quot;foo bar fileName count&quot;</pre>
</dl>
<p> <i>Objc</i> is usually 1, but may be 2 or more for commands like <code>string</code> and the Tk widget commands, which use the first argument as a subcommand. </p>
<p> Some of the objects in the <i>objv</i> array may be abbreviations for a subcommand. The command <code>Tcl_GetIndexFromObj</code> will convert the abbreviated string object into an <i>indexObject</i>. If an error occurs in the parsing of the subcommand we would like to use the full subcommand name rather than the abbreviation. If the <code>Tcl_WrongNumArgs</code> command finds any <i>indexObjects</i> in the <i>objv</i> array it will use the full subcommand name in the error message instead of the abbreviated name that was originally passed in. Using the above example, let us assume that <i>bar</i> is actually an abbreviation for <i>barfly</i> and the object is now an indexObject because it was passed to <code>Tcl_GetIndexFromObj</code>. In this case the error message would be:</p>
<dl COMPACT>
<dd>
<pre>wrong # args: should be &quot;foo barfly fileName count&quot;</pre>
</dl>
<h2>See Also</h2>
<p>Tcl_GetIndexFromObj </p>
<h2>Keywords</h2>
<p>command, error message, wrong number of arguments</p>
