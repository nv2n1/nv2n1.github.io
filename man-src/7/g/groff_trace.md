---
title: "groff_trace(7)"
name: "groff_trace"
section: "7"
letter: "g"
url: "/docs/linux/man/7-groff_trace/"
description: "groff_trace – groff macro package trace.tmac"
---

<p>groff_trace &#8211; groff macro package trace.tmac</p>
<h2>Synopsis</h2>
<p>[<i>option</i> &#8230;] [<i>input-file</i> &#8230;]</p>
<h2>Description</h2>
<p>The <i>trace</i> macro package of <code><a href="/docs/linux/man/1-groff/">groff</a></code>(1) can be a valuable tool for debugging documents written in the roff formatting language. A call stack trace is protocolled on standard error, this is, a diagnostic message is emitted on entering and exiting of a macro call. This greatly eases to track down an error in some macro. </p>
<p> This tracing process is activated by specifying the groff or troff command-line option <code>-m trace</code>. This works also with the <code><a href="/docs/linux/man/1-groffer/">groffer</a></code>(1) viewer program. A finer control can be obtained by including the macro file within the document by the groff macro call <code>.mso trace.tmac</code>. Only macros that are defined after this line are traced. </p>
<p> If the command-line option <code>-r trace-full=1</code> is given (or if this register is set in the document), number and string register assignments together with some other requests are traced also. </p>
<p> If some other macro package should be traced as well it must be specified after <code>-m trace</code> on the command line. </p>
<p> The macro file <code>trace.tmac</code> is unusual because it does not contain any macros to be called by a user. Instead, the existing macro definition and appending facilities are modified such that they display diagnostic messages.</p>
<h2>Examples</h2>
<p>In the following examples, a roff fragment is fed into groff via standard input. As we are only interested in the diagnostic messages (standard error) on the terminal, the normal formatted output (standard output) is redirected to the nirvana device <i>/dev/null</i>. The resulting diagnostic messages are displayed directly below the corresponding example.</p>
<h3>Command line option</h3>
<p>Example:</p>
<dl>
<dd><i>sh#</i> echo &#8216;. &gt; .de test_macro &gt; .. &gt; .test_macro &gt; .test_macro some dummy arguments &gt; &#8216; | groff -m trace &gt; /dev/null </p>
<p> *** .de test_macro *** de trace enter: .test_macro *** trace exit: .test_macro *** de trace enter: .test_macro &quot;some&quot; &quot;dummy&quot; &quot;arguments&quot; *** trace exit: .test_macro &quot;some&quot; &quot;dummy&quot; &quot;arguments&quot;</dl>
<p> The entry and the exit of each macro call is displayed on the terminal (standard output) &#8212; together with the arguments (if any).</p>
<h3>Nested macro calls</h3>
<p>Example:</p>
<dl>
<dd><i>sh#</i> echo &#8216;. &gt; .de child &gt; .. &gt; .de parent &gt; .child &gt; .. &gt; .parent &gt; &#8216; | groff -m trace &gt; /dev/null </p>
<p> *** .de child *** .de parent *** de trace enter: .parent<br />
&nbsp;***&nbsp;de trace enter: .child<br />
&nbsp;***&nbsp;trace exit: .child *** trace exit: .parent</dl>
<p> This shows that macro calls can be nested. This powerful feature can help to tack down quite complex call stacks.</p>
<h3>Activating with .mso</h3>
<p>Example:</p>
<dl>
<dd><i>sh#</i> echo &#8216;. &gt; .de before &gt; .. &gt; .mso trace.tmac &gt; .de after &gt; .. &gt; .before &gt; .after &gt; .before &gt; &#8216; | groff &gt; /dev/null </p>
<p> *** de trace enter: .after *** trace exit: .after</dl>
<p> Here, the tracing is activated within the document, not by a command-line option. As tracing was not active when macro <i>before</i> was defined, no call of this macro is protocolled; on the other hand, the macro <i>after</i> is fully protocolled.</p>
<h2>Problems</h2>
<p>Because <code>trace.tmac</code> wraps the <code>.de</code> request (and its cousins), macro arguments are expanded one level more. This causes problems if an argument contains four backslashes or more to prevent too early expansion of the backslash. For example, this macro call</p>
<dl>
<dd>.foo \\n[bar]</dl>
<p> normally passes &#8216;\n[bar]&#8217; to macro &#8216;.foo&#8217;, but with the redefined <code>.de</code> request it passes &#8216;
[bar]&#8217; instead. </p>
<p> The solution to this problem is to use groff&#8217;s <code>\E</code> escape which is an escape character not interpreted in copy mode, for example</p>
<dl>
<dd>.foo \En[bar]</dl>
<h2>Files</h2>
<p>The <i>trace</i> macros are kept in the file <code>trace.tmac</code> located in the <i>tmac directory</i>; see <code><a href="/docs/linux/man/5-groff_tmac/">groff_tmac</a></code>(5) for details.</p>
<h2>Environment</h2>
<dl>
<dt><i>GROFF_TMAC_PATH</i></p>
<dd>A colon-separated list of additional tmac directories in which to search for macro files; see <code><a href="/docs/linux/man/5-groff_tmac/">groff_tmac</a></code>(5) for details.</dl>
<h2>Authors</h2>
<p>The <i>trace</i> macro packages was written by James Clark. This document was written by Bernd Warken</p>
<h2>See Also</h2>
<p><i>Groff: The GNU Implementation of troff</i>, by Trent A. Fisher and Werner Lemberg, is the primary <i>groff</i> manual. You can browse it interactively with &#8220;info groff&#8221;.</p>
<dl>
<dt><code><a href="/docs/linux/man/1-groff/">groff</a></code>(1)</p>
<dd>An overview of the groff system.</p>
<dt><code><a href="/docs/linux/man/1-troff/">troff</a></code>(1)</p>
<dd>For details on option <code>-m</code>.</p>
<dt><code><a href="/docs/linux/man/1-groffer/">groffer</a></code>(1)</p>
<dd>A viewer program for all kinds of roff documents.</p>
<dt><code><a href="/docs/linux/man/5-groff_tmac/">groff_tmac</a></code>(5)</p>
<dd>A general description of groff macro packages.</p>
<dt><code><a href="/docs/linux/man/7-groff/">groff</a></code>(7)</p>
<dd>A short reference for the groff formatting language. </p>
