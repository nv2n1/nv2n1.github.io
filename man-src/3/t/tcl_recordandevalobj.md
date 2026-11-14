---
title: "tcl_recordandevalobj(3)"
name: "tcl_recordandevalobj"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tcl_recordandevalobj/"
description: "Tcl_RecordAndEvalObj – save command on history list before evaluating"
---

<p>Tcl_RecordAndEvalObj &#8211; save command on history list before evaluating </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tcl.h&gt;</code>
int
<code>Tcl_RecordAndEvalObj</code>(<i>interp, cmdPtr, flags</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tcl_Interp <i>*interp</i> (in) Tcl interpreter in which to evaluate command.</p>
<dd>Tcl_Obj <i>*cmdPtr</i> (in) Points to a Tcl object containing a command (or sequence of commands) to execute.</p>
<dd>int <i>flags</i> (in) An OR&#8217;ed combination of flag bits. <code>TCL_NO_EVAL</code> means record the command but do not evaluate it. <code>TCL_EVAL_GLOBAL</code> means evaluate the command at global level instead of the current stack level. </p>
</dl>
<h2>Description</h2>
<p><code>Tcl_RecordAndEvalObj</code> is invoked to record a command as an event on the history list and then execute it using <code>Tcl_EvalObjEx</code> (or <code>Tcl_GlobalEvalObj</code> if the <code>TCL_EVAL_GLOBAL</code> bit is set in <i>flags</i>). It returns a completion code such as <code>TCL_OK</code> just like <code>Tcl_EvalObjEx</code>, as well as a result object containing additional information (a result value or error message) that can be retrieved using <code>Tcl_GetObjResult</code>. If you do not want the command recorded on the history list then you should invoke <code>Tcl_EvalObjEx</code> instead of <code>Tcl_RecordAndEvalObj</code>. Normally <code>Tcl_RecordAndEvalObj</code> is only called with top-level commands typed by the user, since the purpose of history is to allow the user to re-issue recently invoked commands. If the <i>flags</i> argument contains the <code>TCL_NO_EVAL</code> bit then the command is recorded without being evaluated. </p>
<h2>See Also</h2>
<p>Tcl_EvalObjEx, Tcl_GetObjResult </p>
<h2>Keywords</h2>
<p>command, event, execute, history, interpreter, object, record</p>
