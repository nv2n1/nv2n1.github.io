---
title: "csgrep(1)"
name: "csgrep"
section: "1"
letter: "c"
url: "/docs/linux/man/1-csgrep/"
description: "csgrep – filter the list of defects by the specified regex-based predicates"
---

<h2>NAME</h2>
<p> csgrep &#8211; filter the list of defects by the specified regex-based predicates</p>
<h2>SYNOPSIS</h2>
<p> <code>csgrep</code> [<i>options</i>] [<i>file1.err </i>[&#8230;]]<i>, where options are:</i></p>
<h2>DESCRIPTION</h2>
<dl>
<dt><code>&#8211;checker</code> arg</p>
<dd> defect matches if its checker matches the given regex (each defect has assigned exactly one checker)</p>
<dt><code>&#8211;path</code> arg</p>
<dd> defect matches if the path of its key event matches the given regex</p>
<dt><code>&#8211;event</code> arg</p>
<dd> defect matches if its key event matches the given regex (each defect has exactly one key event, which determines its location in the code)</p>
<dt><code>&#8211;error</code> arg</p>
<dd> defect matches if the message of its key event matches the given regex</p>
<dt><code>&#8211;msg</code> arg</p>
<dd> defect matches if any of its messages matches the given regex</p>
<dt><code>&#8211;annot</code> arg</p>
<dd> defect matches if its annotation matches the given regex</p>
<dt><code>&#8211;src-annot</code> arg</p>
<dd> defect matches if an annotation in the _source_ file matches the given regex</p>
<dt><code>-U</code> [ <code>&#8211;embed-context</code> ] arg</p>
<dd> embed a number of lines of context from the source file for the key event</p>
<dt><code>&#8211;prune-events</code> arg</p>
<dd> event is preserved if its verbosity level is below the given number</p>
<dt><code>-u</code> [ <code>&#8211;remove-duplicates</code> ]</p>
<dd> remove defects that are not unique by their key event</p>
<dt><code>&#8211;strip-path-prefix</code> arg</p>
<dd> string prefix to strip from path (applied after all filters)</p>
<dt><code>-i</code> [ <code>&#8211;ignore-case</code> ]</p>
<dd> ignore case when matching regular expressions</p>
<dt><code>-v</code> [ <code>&#8211;invert-match</code> ]</p>
<dd> select defects that do not match the selected criteria</p>
<dt><code>-n</code> [ <code>&#8211;invert-regex</code> ]</p>
<dd> invert regular expressions in all predicates</p>
<dt><code>&#8211;color</code></p>
<dd> use colorized console output (default if connected to a terminal)</p>
<dt><code>&#8211;no-color</code></p>
<dd> do not use colorized console output</p>
<dt><code>-q</code> [ <code>&#8211;quiet</code> ]</p>
<dd> do not report any parsing errors</p>
<dt><code>&#8211;mode</code> arg (=grep)</p>
<dd> grep, json, stat, grouped, files, filestat, or dig_key_events</p>
<dt><code>&#8211;help</code></p>
<dd> print the usage of csgrep</p>
<dt><code>&#8211;version</code></p>
<dd> print the version of csgrep</dl>
<h2>EXAMPLE &#8211; CHECKERS, EVENTS, MESSAGES</h2>
<pre>
Error: FORWARD_NULL (CWE-476):
libhsm.c:1168: assign_zero: Assigning: key_handles = NULL.
libhsm.c:1210: var_deref_op: Dereferencing null pointer key_handles.
</pre>
<p> In the above example, FORWARD_NULL is the <code>checker</code> , assign_zero and var_deref_op are <code>events</code> , where var_deref_op is the key event and &quot;Dereferencing null pointer key_handles.&quot; is the <code>message</code> associated with the key event.</p>
<h2>DESCRIPTION OF AVAILABLE MODES</h2>
<p> <code>dig_key_events</code> &#8211; for each defect, print only the checker and key event </p>
<p> <code>evtstat</code> &#8211; print overall checker/key_event statistics for the matched defects </p>
<p> <code>files</code> &#8211; print only names of error files that contain the matched defects </p>
<p> <code>filestat</code> &#8211; print statistics of matched defects per individual source files </p>
<p> <code>grep</code> &#8211; print matched defects using the same format as expected on the input </p>
<p> <code>grouped</code> &#8211; print matched defects, grouped by error files they originate from </p>
<p> <code>json</code> &#8211; print matched defects in a JSON format </p>
<p> <code>stat</code> &#8211; print overall statistics of the matched defects in given error files </p>
<h2>Index</h2>
