---
title: "pcrestack(3)"
name: "pcrestack"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pcrestack/"
description: "PCRE – Perl-compatible regular expressions"
---

<p>PCRE &#8211; Perl-compatible regular expressions</p>
<h2>Pcre Discussion Of Stack Usage</h2>
<p>When you call <code>pcre[16|32]_exec()</code>, it makes use of an internal function called <code>match()</code>. This calls itself recursively at branch points in the pattern, in order to remember the state of the match so that it can back up and try a different alternative if the first one fails. As matching proceeds deeper and deeper into the tree of possibilities, the recursion depth increases. The <code>match()</code> function is also called in other circumstances, for example, whenever a parenthesized sub-pattern is entered, and in certain cases of repetition. </p>
<p> Not all calls of <code>match()</code> increase the recursion depth; for an item such as a* it may be called several times at the same level, after matching different numbers of a&#8217;s. Furthermore, in a number of cases where the result of the recursive call would immediately be passed back as the result of the current call (a &quot;tail recursion&quot;), the function is just restarted instead. </p>
<p> The above comments apply when <code>pcre[16|32]_exec()</code> is run in its normal interpretive manner. If the pattern was studied with the PCRE_STUDY_JIT_COMPILE option, and just-in-time compiling was successful, and the options passed to <code>pcre[16|32]_exec()</code> were not incompatible, the matching process uses the JIT-compiled code instead of the <code>match()</code> function. In this case, the memory requirements are handled entirely differently. See the <code>pcrejit</code> documentation for details. </p>
<p> The <code>pcre[16|32]_dfa_exec()</code> function operates in an entirely different way, and uses recursion only when there is a regular expression recursion or subroutine call in the pattern. This includes the processing of assertion and &quot;once-only&quot; subpatterns, which are handled like subroutine calls. Normally, these are never very deep, and the limit on the complexity of <code>pcre[16|32]_dfa_exec()</code> is controlled by the amount of workspace it is given. However, it is possible to write patterns with runaway infinite recursions; such patterns will cause <code>pcre[16|32]_dfa_exec()</code> to run out of stack. At present, there is no protection against this. </p>
<p> The comments that follow do NOT apply to <code>pcre[16|32]_dfa_exec()</code>; they are relevant only for <code>pcre[16|32]_exec()</code> without the JIT optimization.</p>
<h3>Reducing <code>pcre[16|32]_exec()</code>&#8216;s stack usage</h3>
<p>Each time that <code>match()</code> is actually called recursively, it uses memory from the process stack. For certain kinds of pattern and data, very large amounts of stack may be needed, despite the recognition of &quot;tail recursion&quot;. You can often reduce the amount of recursion, and therefore the amount of stack used, by modifying the pattern that is being matched. Consider, for example, this pattern: </p>
<p>&nbsp;<wbr>&nbsp;([^&lt;]|&lt;(?!inet))+ </p>
<p> It matches from wherever it starts until it encounters &quot;&lt;inet&quot; or the end of the data, and is the kind of pattern that might be used when processing an XML file. Each iteration of the outer parentheses matches either one character that is not &quot;&lt;&quot; or a &quot;&lt;&quot; that is not followed by &quot;inet&quot;. However, each time a parenthesis is processed, a recursion occurs, so this formulation uses a stack frame for each matched character. For a long string, a lot of stack is required. Consider now this rewritten pattern, which matches exactly the same strings: </p>
<p>&nbsp;<wbr>&nbsp;([^&lt;]++|&lt;(?!inet))+ </p>
<p> This uses very much less stack, because runs of characters that do not contain &quot;&lt;&quot; are &quot;swallowed&quot; in one item inside the parentheses. Recursion happens only when a &quot;&lt;&quot; character that is not followed by &quot;inet&quot; is encountered (and we assume this is relatively rare). A possessive quantifier is used to stop any backtracking into the runs of non-&quot;&lt;&quot; characters, but that is not related to stack usage. </p>
<p> This example shows that one way of avoiding stack problems when matching long subject strings is to write repeated parenthesized subpatterns to match more than one character whenever possible.</p>
<h3>Compiling PCRE to use heap instead of stack for <code>pcre[16|32]_exec()</code></h3>
<p>In environments where stack memory is constrained, you might want to compile PCRE to use heap memory instead of stack for remembering back-up points when <code>pcre[16|32]_exec()</code> is running. This makes it run a lot more slowly, however. Details of how to do this are given in the <code>pcrebuild</code> documentation. When built in this way, instead of using the stack, PCRE obtains and frees memory by calling the functions that are pointed to by the <code>pcre[16|32]_stack_malloc</code> and <code>pcre[16|32]_stack_free</code> variables. By default, these point to <code>malloc()</code> and <code>free()</code>, but you can replace the pointers to cause PCRE to use your own functions. Since the block sizes are always the same, and are always freed in reverse order, it may be possible to implement customized memory handlers that are more efficient than the standard functions.</p>
<h3>Limiting <code>pcre[16|32]_exec()</code>&#8216;s stack usage</h3>
<p>You can set limits on the number of times that <code>match()</code> is called, both in total and recursively. If a limit is exceeded, <code>pcre[16|32]_exec()</code> returns an error code. Setting suitable limits should prevent it from running out of stack. The default values of the limits are very large, and unlikely ever to operate. They can be changed when PCRE is built, and they can also be set when <code>pcre[16|32]_exec()</code> is called. For details of these interfaces, see the <code>pcrebuild</code> documentation and the section on extra data for <code>pcre[16|32]_exec()</code> in the <code>pcreapi</code> documentation. </p>
<p> As a very rough rule of thumb, you should reckon on about 500 bytes per recursion. Thus, if you want to limit your stack usage to 8Mb, you should set the limit at 16000 recursions. A 64Mb stack, on the other hand, can support around 128000 recursions. </p>
<p> In Unix-like environments, the <code>pcretest</code> test program has a command line option (<code>-S</code>) that can be used to increase the size of its stack. As long as the stack is large enough, another option (<code>-M</code>) can be used to find the smallest limits that allow a particular pattern to match a given subject string. This is done by calling <code>pcre[16|32]_exec()</code> repeatedly with different limits.</p>
<h3>Obtaining an estimate of stack usage</h3>
<p>The actual amount of stack used per recursion can vary quite a lot, depending on the compiler that was used to build PCRE and the optimization or debugging options that were set for it. The rule of thumb value of 500 bytes mentioned above may be larger or smaller than what is actually needed. A better approximation can be obtained by running this command: </p>
<p>&nbsp;<wbr>&nbsp;pcretest -m -C </p>
<p> The <code>-C</code> option causes <code>pcretest</code> to output information about the options with which PCRE was compiled. When <code>-m</code> is also given (before <code>-C</code>), information about stack use is given in a line like this: </p>
<p>&nbsp;<wbr>&nbsp;Match recursion uses stack: approximate frame size&nbsp;=&nbsp;640 bytes </p>
<p> The value is approximate because some recursions need a bit more (up to perhaps 16 more bytes). </p>
<p> If the above command is given when PCRE is compiled to use the heap instead of the stack for recursion, the value that is output is the size of each block that is obtained from the heap.</p>
<h3>Changing stack size in Unix-like systems</h3>
<p>In Unix-like environments, there is not often a problem with the stack unless very long strings are involved, though the default limit on stack size varies from system to system. Values from 8Mb to 64Mb are common. You can find your default limit by running the command: </p>
<p>&nbsp;<wbr>&nbsp;ulimit -s </p>
<p> Unfortunately, the effect of running out of stack is often SIGSEGV, though sometimes a more explicit error message is given. You can normally increase the limit on stack size by code such as this: </p>
<p>&nbsp;<wbr>&nbsp;struct rlimit rlim;<br />
&nbsp;<wbr>&nbsp;getrlimit(RLIMIT_STACK,&nbsp;&amp;rlim);<br />
&nbsp;<wbr>&nbsp;rlim.rlim_cur&nbsp;=&nbsp;100*1024*1024;<br />
&nbsp;<wbr>&nbsp;setrlimit(RLIMIT_STACK,&nbsp;&amp;rlim); </p>
<p> This reads the current limits (soft and hard) using <code>getrlimit()</code>, then attempts to increase the soft limit to 100Mb using <code>setrlimit()</code>. You must do this before calling <code>pcre[16|32]_exec()</code>.</p>
<h3>Changing stack size in Mac OS X</h3>
<p>Using <code>setrlimit()</code>, as described above, should also work on Mac OS X. It is also possible to set a stack size when linking a program. There is a discussion about stack sizes in Mac OS X at this web site: <a rel="nofollow" href="http://developer.apple.com/qa/qa2005/qa1419.html.">http://developer.apple.com/qa/qa2005/qa1419.html.</a></p>
<h2>Author</h2>
<pre>Philip Hazel
University Computing Service
Cambridge CB2 3QH, England.</pre>
<h2>Revision</h2>
<pre>Last updated: 24 June 2012
Copyright (c) 1997-2012 University of Cambridge.</pre>
