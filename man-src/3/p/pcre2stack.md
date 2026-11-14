---
title: "pcre2stack(3)"
name: "pcre2stack"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pcre2stack/"
description: "PCRE2 – Perl-compatible regular expressions (revised API)"
---

<p>PCRE2 &#8211; Perl-compatible regular expressions (revised API)</p>
<h2>Pcre2 Discussion Of Stack Usage</h2>
<p>When you call <code>pcre2_match()</code>, it makes use of an internal function called <code>match()</code>. This calls itself recursively at branch points in the pattern, in order to remember the state of the match so that it can back up and try a different alternative after a failure. As matching proceeds deeper and deeper into the tree of possibilities, the recursion depth increases. The <code>match()</code> function is also called in other circumstances, for example, whenever a parenthesized sub-pattern is entered, and in certain cases of repetition. </p>
<p> Not all calls of <code>match()</code> increase the recursion depth; for an item such as a* it may be called several times at the same level, after matching different numbers of a&#8217;s. Furthermore, in a number of cases where the result of the recursive call would immediately be passed back as the result of the current call (a &quot;tail recursion&quot;), the function is just restarted instead. </p>
<p> Each time the internal <code>match()</code> function is called recursively, it uses memory from the process stack. For certain kinds of pattern and data, very large amounts of stack may be needed, despite the recognition of &quot;tail recursion&quot;. Note that if PCRE2 is compiled with the -fsanitize=address option of the GCC compiler, the stack requirements are greatly increased. </p>
<p> The above comments apply when <code>pcre2_match()</code> is run in its normal interpretive manner. If the compiled pattern was processed by <code>pcre2_jit_compile()</code>, and just-in-time compiling was successful, and the options passed to <code>pcre2_match()</code> were not incompatible, the matching process uses the JIT-compiled code instead of the <code>match()</code> function. In this case, the memory requirements are handled entirely differently. See the <code>pcre2jit</code> documentation for details. </p>
<p> The <code>pcre2_dfa_match()</code> function operates in a different way to <code>pcre2_match()</code>, and uses recursion only when there is a regular expression recursion or subroutine call in the pattern. This includes the processing of assertion and &quot;once-only&quot; subpatterns, which are handled like subroutine calls. Normally, these are never very deep, and the limit on the complexity of <code>pcre2_dfa_match()</code> is controlled by the amount of workspace it is given. However, it is possible to write patterns with runaway infinite recursions; such patterns will cause <code>pcre2_dfa_match()</code> to run out of stack. At present, there is no protection against this. </p>
<p> The comments that follow do NOT apply to <code>pcre2_dfa_match()</code>; they are relevant only for <code>pcre2_match()</code> without the JIT optimization.</p>
<h3>Reducing <code>pcre2_match()</code>&#8216;s stack usage</h3>
<p>You can often reduce the amount of recursion, and therefore the amount of stack used, by modifying the pattern that is being matched. Consider, for example, this pattern: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>([^&lt;]|&lt;(?!inet))+ </p>
<p> It matches from wherever it starts until it encounters &quot;&lt;inet&quot; or the end of the data, and is the kind of pattern that might be used when processing an XML file. Each iteration of the outer parentheses matches either one character that is not &quot;&lt;&quot; or a &quot;&lt;&quot; that is not followed by &quot;inet&quot;. However, each time a parenthesis is processed, a recursion occurs, so this formulation uses a stack frame for each matched character. For a long string, a lot of stack is required. Consider now this rewritten pattern, which matches exactly the same strings: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>([^&lt;]++|&lt;(?!inet))+ </p>
<p> This uses very much less stack, because runs of characters that do not contain &quot;&lt;&quot; are &quot;swallowed&quot; in one item inside the parentheses. Recursion happens only when a &quot;&lt;&quot; character that is not followed by &quot;inet&quot; is encountered (and we assume this is relatively rare). A possessive quantifier is used to stop any backtracking into the runs of non-&quot;&lt;&quot; characters, but that is not related to stack usage. </p>
<p> This example shows that one way of avoiding stack problems when matching long subject strings is to write repeated parenthesized subpatterns to match more than one character whenever possible.</p>
<h3>Compiling PCRE2 to use heap instead of stack for <code>pcre2_match()</code></h3>
<p>In environments where stack memory is constrained, you might want to compile PCRE2 to use heap memory instead of stack for remembering back-up points when <code>pcre2_match()</code> is running. This makes it run more slowly, however. Details of how to do this are given in the <code>pcre2build</code> documentation. When built in this way, instead of using the stack, PCRE2 gets memory for remembering backup points from the heap. By default, the memory is obtained by calling the system <code>malloc()</code> function, but you can arrange to supply your own memory management function. For details, see the section entitled &quot;The match context&quot; in the <code>pcre2api</code> documentation. Since the block sizes are always the same, it may be possible to implement customized a memory handler that is more efficient than the standard function. The memory blocks obtained for this purpose are retained and re-used if possible while <code>pcre2_match()</code> is running. They are all freed just before it exits.</p>
<h3>Limiting <code>pcre2_match()</code>&#8216;s stack usage</h3>
<p>You can set limits on the number of times the internal <code>match()</code> function is called, both in total and recursively. If a limit is exceeded, <code>pcre2_match()</code> returns an error code. Setting suitable limits should prevent it from running out of stack. The default values of the limits are very large, and unlikely ever to operate. They can be changed when PCRE2 is built, and they can also be set when <code>pcre2_match()</code> is called. For details of these interfaces, see the <code>pcre2build</code> documentation and the section entitled &quot;The match context&quot; in the <code>pcre2api</code> documentation. </p>
<p> As a very rough rule of thumb, you should reckon on about 500 bytes per recursion. Thus, if you want to limit your stack usage to 8Mb, you should set the limit at 16000 recursions. A 64Mb stack, on the other hand, can support around 128000 recursions. </p>
<p> The <code>pcre2test</code> test program has a modifier called &quot;find_limits&quot; which, if applied to a subject line, causes it to find the smallest limits that allow a a pattern to match. This is done by calling <code>pcre2_match()</code> repeatedly with different limits.</p>
<h3>Changing stack size in Unix-like systems</h3>
<p>In Unix-like environments, there is not often a problem with the stack unless very long strings are involved, though the default limit on stack size varies from system to system. Values from 8Mb to 64Mb are common. You can find your default limit by running the command: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>ulimit -s </p>
<p> Unfortunately, the effect of running out of stack is often SIGSEGV, though sometimes a more explicit error message is given. You can normally increase the limit on stack size by code such as this: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>struct rlimit rlim;<br />
&nbsp;<wbr>&nbsp;<wbr>getrlimit(RLIMIT_STACK,&nbsp;<wbr>&amp;rlim);<br />
&nbsp;<wbr>&nbsp;<wbr>rlim.rlim_cur&nbsp;<wbr>=&nbsp;<wbr>100*1024*1024;<br />
&nbsp;<wbr>&nbsp;<wbr>setrlimit(RLIMIT_STACK,&nbsp;<wbr>&amp;rlim); </p>
<p> This reads the current limits (soft and hard) using <code>getrlimit()</code>, then attempts to increase the soft limit to 100Mb using <code>setrlimit()</code>. You must do this before calling <code>pcre2_match()</code>.</p>
<h3>Changing stack size in Mac OS X</h3>
<p>Using <code>setrlimit()</code>, as described above, should also work on Mac OS X. It is also possible to set a stack size when linking a program. There is a discussion about stack sizes in Mac OS X at this web site: <a rel="nofollow" href="http://developer.apple.com/qa/qa2005/qa1419.html.">http://developer.apple.com/qa/qa2005/qa1419.html.</a></p>
<h2>Author</h2>
<pre>Philip Hazel
University Computing Service
Cambridge, England.</pre>
<h2>Revision</h2>
<pre>Last updated: 21 November 2014
Copyright (c) 1997-2014 University of Cambridge.</pre>
