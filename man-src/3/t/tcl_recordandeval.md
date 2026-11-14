---
title: "tcl_recordandeval(3)"
name: "tcl_recordandeval"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tcl_recordandeval/"
description: "Tcl_RecordAndEval – save command on history list before evaluating"
---

<p>Tcl_RecordAndEval &#8211; save command on history list before evaluating </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tcl.h&gt;</code>
int
<code>Tcl_RecordAndEval</code>(<i>interp, cmd, flags</i>)</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dd>Tcl_Interp <i>*interp</i> (in) Tcl interpreter in which to evaluate command.</p>
<dd>const char <i>*cmd</i> (in) Command (or sequence of commands) to execute.</p>
<dd>int <i>flags</i> (in) An OR&#8217;ed combination of flag bits. <code>TCL_NO_EVAL</code> means record the command but do not evaluate it. <code>TCL_EVAL_GLOBAL</code> means evaluate the command at global level instead of the current stack level. </p>
</dl>
<h2>Description</h2>
<p><code>Tcl_RecordAndEval</code> is invoked to record a command as an event on the history list and then execute it using <code>Tcl_Eval</code> (or <code>Tcl_GlobalEval</code> if the <code>TCL_EVAL_GLOBAL</code> bit is set in <i>flags</i>). It returns a completion code such as <code>TCL_OK</code> just like <code>Tcl_Eval</code> and it leaves information in the interpreter&#8217;s result. If you do not want the command recorded on the history list then you should invoke <code>Tcl_Eval</code> instead of <code>Tcl_RecordAndEval</code>. Normally <code>Tcl_RecordAndEval</code> is only called with top-level commands typed by the user, since the purpose of history is to allow the user to re-issue recently-invoked commands. If the <i>flags</i> argument contains the <code>TCL_NO_EVAL</code> bit then the command is recorded without being evaluated. </p>
<p> Note that <code>Tcl_RecordAndEval</code> has been largely replaced by the object-based procedure <code>Tcl_RecordAndEvalObj</code>. That object-based procedure records and optionally executes a command held in a Tcl object instead of a string. </p>
<h2>See Also</h2>
<p>Tcl_RecordAndEvalObj </p>
<h2>Keywords</h2>
<p>command, event, execute, history, interpreter, record</p>
