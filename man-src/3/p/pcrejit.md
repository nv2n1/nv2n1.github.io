---
title: "pcrejit(3)"
name: "pcrejit"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pcrejit/"
description: "PCRE – Perl-compatible regular expressions"
---

<p>PCRE &#8211; Perl-compatible regular expressions</p>
<h2>Pcre Just-In-Time Compiler Support</h2>
<p>Just-in-time compiling is a heavyweight optimization that can greatly speed up pattern matching. However, it comes at the cost of extra processing before the match is performed. Therefore, it is of most benefit when the same pattern is going to be matched many times. This does not necessarily mean many calls of a matching function; if the pattern is not anchored, matching attempts may take place many times at various positions in the subject, even for a single call. Therefore, if the subject string is very long, it may still pay to use JIT for one-off matches. </p>
<p> JIT support applies only to the traditional Perl-compatible matching function. It does not apply when the DFA matching function is being used. The code for this support was written by Zoltan Herczeg.</p>
<h2>8-Bit, 16-Bit And 32-Bit Support</h2>
<p>JIT support is available for all of the 8-bit, 16-bit and 32-bit PCRE libraries. To keep this documentation simple, only the 8-bit interface is described in what follows. If you are using the 16-bit library, substitute the 16-bit functions and 16-bit structures (for example, <i>pcre16_jit_stack</i> instead of <i>pcre_jit_stack</i>). If you are using the 32-bit library, substitute the 32-bit functions and 32-bit structures (for example, <i>pcre32_jit_stack</i> instead of <i>pcre_jit_stack</i>).</p>
<h2>Availability Of Jit Support</h2>
<p>JIT support is an optional feature of PCRE. The &quot;configure&quot; option &#8211;enable-jit (or equivalent CMake option) must be set when PCRE is built if you want to use JIT. The support is limited to the following hardware platforms: </p>
<p>&nbsp;<wbr>&nbsp;ARM v5, v7, and Thumb2<br />
&nbsp;<wbr>&nbsp;Intel x86 32-bit and 64-bit<br />
&nbsp;<wbr>&nbsp;MIPS 32-bit<br />
&nbsp;<wbr>&nbsp;Power PC 32-bit and 64-bit<br />
&nbsp;<wbr>&nbsp;SPARC 32-bit&nbsp;(experimental) </p>
<p> If &#8211;enable-jit is set on an unsupported platform, compilation fails. </p>
<p> A program that is linked with PCRE 8.20 or later can tell if JIT support is available by calling <code>pcre_config()</code> with the PCRE_CONFIG_JIT option. The result is 1 when JIT is available, and 0 otherwise. However, a simple program does not need to check this in order to use JIT. The normal API is implemented in a way that falls back to the interpretive code if JIT is not available. For programs that need the best possible performance, there is also a &quot;fast path&quot; API that is JIT-specific. </p>
<p> If your program may sometimes be linked with versions of PCRE that are older than 8.20, but you want to use JIT when it is available, you can test the values of PCRE_MAJOR and PCRE_MINOR, or the existence of a JIT macro such as PCRE_CONFIG_JIT, for compile-time control of your code.</p>
<h2>Simple Use Of Jit</h2>
<p>You have to do two things to make use of the JIT support in the simplest way: </p>
<p>&nbsp;<wbr>&nbsp;(1)&nbsp;Call&nbsp;<code>pcre_study()</code>&nbsp;with the PCRE_STUDY_JIT_COMPILE option for<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;each compiled pattern, and pass the resulting&nbsp;<code>pcre_extra</code>&nbsp;block to<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>pcre_exec()</code>. </p>
<p>&nbsp;<wbr>&nbsp;(2)&nbsp;Use&nbsp;<code>pcre_free_study()</code>&nbsp;to free the&nbsp;<code>pcre_extra</code>&nbsp;block when it is<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;no longer needed, instead of just freeing it yourself. This ensures that<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;any JIT data is also freed. </p>
<p> For a program that may be linked with pre-8.20 versions of PCRE, you can insert </p>
<p>&nbsp;<wbr>&nbsp;#ifndef PCRE_STUDY_JIT_COMPILE<br />
&nbsp;<wbr>&nbsp;#define PCRE_STUDY_JIT_COMPILE 0<br />
&nbsp;<wbr>&nbsp;#endif </p>
<p> so that no option is passed to <code>pcre_study()</code>, and then use something like this to free the study data: </p>
<p>&nbsp;<wbr>&nbsp;#ifdef PCRE_CONFIG_JIT<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pcre_free_study(study_ptr);<br />
&nbsp;<wbr>&nbsp;#else<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pcre_free(study_ptr);<br />
&nbsp;<wbr>&nbsp;#endif </p>
<p> PCRE_STUDY_JIT_COMPILE requests the JIT compiler to generate code for complete matches. If you want to run partial matches using the PCRE_PARTIAL_HARD or PCRE_PARTIAL_SOFT options of <code>pcre_exec()</code>, you should set one or both of the following options in addition to, or instead of, PCRE_STUDY_JIT_COMPILE when you call <code>pcre_study()</code>: </p>
<p>&nbsp;<wbr>&nbsp;PCRE_STUDY_JIT_PARTIAL_HARD_COMPILE<br />
&nbsp;<wbr>&nbsp;PCRE_STUDY_JIT_PARTIAL_SOFT_COMPILE </p>
<p> The JIT compiler generates different optimized code for each of the three modes (normal, soft partial, hard partial). When <code>pcre_exec()</code> is called, the appropriate code is run if it is available. Otherwise, the pattern is matched using interpretive code. </p>
<p> In some circumstances you may need to call additional functions. These are described in the section entitled &quot;Controlling the JIT stack&quot; below. </p>
<p> If JIT support is not available, PCRE_STUDY_JIT_COMPILE etc. are ignored, and no JIT data is created. Otherwise, the compiled pattern is passed to the JIT compiler, which turns it into machine code that executes much faster than the normal interpretive code. When <code>pcre_exec()</code> is passed a <code>pcre_extra</code> block containing a pointer to JIT code of the appropriate mode (normal or hard/soft partial), it obeys that code instead of running the interpreter. The result is identical, but the compiled JIT code runs much faster. </p>
<p> There are some <code>pcre_exec()</code> options that are not supported for JIT execution. There are also some pattern items that JIT cannot handle. Details are given below. In both cases, execution automatically falls back to the interpretive code. If you want to know whether JIT was actually used for a particular match, you should arrange for a JIT callback function to be set up as described in the section entitled &quot;Controlling the JIT stack&quot; below, even if you do not need to supply a non-default JIT stack. Such a callback function is called whenever JIT code is about to be obeyed. If the execution options are not right for JIT execution, the callback function is not obeyed. </p>
<p> If the JIT compiler finds an unsupported item, no JIT data is generated. You can find out if JIT execution is available after studying a pattern by calling <code>pcre_fullinfo()</code> with the PCRE_INFO_JIT option. A result of 1 means that JIT compilation was successful. A result of 0 means that JIT support is not available, or the pattern was not studied with PCRE_STUDY_JIT_COMPILE etc., or the JIT compiler was not able to handle the pattern. </p>
<p> Once a pattern has been studied, with or without JIT, it can be used as many times as you like for matching different subject strings.</p>
<h2>Unsupported Options And Pattern Items</h2>
<p>The only <code>pcre_exec()</code> options that are supported for JIT execution are PCRE_NO_UTF8_CHECK, PCRE_NO_UTF16_CHECK, PCRE_NO_UTF32_CHECK, PCRE_NOTBOL, PCRE_NOTEOL, PCRE_NOTEMPTY, PCRE_NOTEMPTY_ATSTART, PCRE_PARTIAL_HARD, and PCRE_PARTIAL_SOFT. </p>
<p> The only unsupported pattern items are \C (match a single data unit) when running in a UTF mode, and a callout immediately before an assertion condition in a conditional group.</p>
<h2>Return Values From Jit Execution</h2>
<p>When a pattern is matched using JIT execution, the return values are the same as those given by the interpretive <code>pcre_exec()</code> code, with the addition of one new error code: PCRE_ERROR_JIT_STACKLIMIT. This means that the memory used for the JIT stack was insufficient. See &quot;Controlling the JIT stack&quot; below for a discussion of JIT stack usage. For compatibility with the interpretive <code>pcre_exec()</code> code, no more than two-thirds of the <i>ovector</i> argument is used for passing back captured substrings. </p>
<p> The error code PCRE_ERROR_MATCHLIMIT is returned by the JIT code if searching a very large pattern tree goes on for too long, as it is in the same circumstance when JIT is not used, but the details of exactly what is counted are not the same. The PCRE_ERROR_RECURSIONLIMIT error code is never returned by JIT execution.</p>
<h2>Saving And Restoring Compiled Patterns</h2>
<p>The code that is generated by the JIT compiler is architecture-specific, and is also position dependent. For those reasons it cannot be saved (in a file or database) and restored later like the bytecode and other data of a compiled pattern. Saving and restoring compiled patterns is not something many people do. More detail about this facility is given in the <code>pcreprecompile</code> documentation. It should be possible to run <code>pcre_study()</code> on a saved and restored pattern, and thereby recreate the JIT data, but because JIT compilation uses significant resources, it is probably not worth doing this; you might as well recompile the original pattern.</p>
<h2>Controlling The Jit Stack</h2>
<p>When the compiled JIT code runs, it needs a block of memory to use as a stack. By default, it uses 32K on the machine stack. However, some large or complicated patterns need more than this. The error PCRE_ERROR_JIT_STACKLIMIT is given when there is not enough stack. Three functions are provided for managing blocks of memory for use as JIT stacks. There is further discussion about the use of JIT stacks in the section entitled &quot;JIT stack FAQ&quot; below. </p>
<p> The <code>pcre_jit_stack_alloc()</code> function creates a JIT stack. Its arguments are a starting size and a maximum size, and it returns a pointer to an opaque structure of type <code>pcre_jit_stack</code>, or NULL if there is an error. The <code>pcre_jit_stack_free()</code> function can be used to free a stack that is no longer needed. (For the technically minded: the address space is allocated by mmap or VirtualAlloc.) </p>
<p> JIT uses far less memory for recursion than the interpretive code, and a maximum stack size of 512K to 1M should be more than enough for any pattern. </p>
<p> The <code>pcre_assign_jit_stack()</code> function specifies which stack JIT code should use. Its arguments are as follows: </p>
<p>&nbsp;<wbr>&nbsp;pcre_extra&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*extra<br />
&nbsp;<wbr>&nbsp;pcre_jit_callback&nbsp;<wbr>&nbsp;callback<br />
&nbsp;<wbr>&nbsp;void&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*data </p>
<p> The <i>extra</i> argument must be the result of studying a pattern with PCRE_STUDY_JIT_COMPILE etc. There are three cases for the values of the other two options: </p>
<p>&nbsp;<wbr>&nbsp;(1)&nbsp;If&nbsp;<i>callback</i>&nbsp;is NULL and&nbsp;<i>data</i>&nbsp;is NULL, an internal 32K block<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;on the machine stack is used. </p>
<p>&nbsp;<wbr>&nbsp;(2)&nbsp;If&nbsp;<i>callback</i>&nbsp;is NULL and&nbsp;<i>data</i>&nbsp;is not NULL,&nbsp;<i>data</i>&nbsp;must be<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;a valid JIT stack, the result of calling&nbsp;<code>pcre_jit_stack_alloc()</code>. </p>
<p>&nbsp;<wbr>&nbsp;(3)&nbsp;If&nbsp;<i>callback</i>&nbsp;is not NULL, it must point to a function that is<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;called with&nbsp;<i>data</i>&nbsp;as an argument at the start of matching, in<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;order to set up a JIT stack. If the return from the callback<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;function is NULL, the internal 32K stack is used;&nbsp;otherwise the<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return value must be a valid JIT stack, the result of calling<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>pcre_jit_stack_alloc()</code>. </p>
<p> A callback function is obeyed whenever JIT code is about to be run; it is not obeyed when <code>pcre_exec()</code> is called with options that are incompatible for JIT execution. A callback function can therefore be used to determine whether a match operation was executed by JIT or by the interpreter. </p>
<p> You may safely use the same JIT stack for more than one pattern (either by assigning directly or by callback), as long as the patterns are all matched sequentially in the same thread. In a multithread application, if you do not specify a JIT stack, or if you assign or pass back NULL from a callback, that is thread-safe, because each thread has its own machine stack. However, if you assign or pass back a non-NULL JIT stack, this must be a different stack for each thread so that the application is thread-safe. </p>
<p> Strictly speaking, even more is allowed. You can assign the same non-NULL stack to any number of patterns as long as they are not used for matching by multiple threads at the same time. For example, you can assign the same stack to all compiled patterns, and use a global mutex in the callback to wait until the stack is available for use. However, this is an inefficient solution, and not recommended. </p>
<p> This is a suggestion for how a multithreaded program that needs to set up non-default JIT stacks might operate: </p>
<p>&nbsp;<wbr>&nbsp;During thread initalization<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;thread_local_var&nbsp;=&nbsp;pcre_jit_stack_alloc(&#8230;) </p>
<p>&nbsp;<wbr>&nbsp;During thread exit<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pcre_jit_stack_free(thread_local_var) </p>
<p>&nbsp;<wbr>&nbsp;Use a one-line callback function<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return thread_local_var </p>
<p> All the functions described in this section do nothing if JIT is not available, and <code>pcre_assign_jit_stack()</code> does nothing unless the <code>extra</code> argument is non-NULL and points to a <code>pcre_extra</code> block that is the result of a successful study with PCRE_STUDY_JIT_COMPILE etc.</p>
<h2>Jit Stack Faq</h2>
<p>(1) Why do we need JIT stacks? </p>
<p> PCRE (and JIT) is a recursive, depth-first engine, so it needs a stack where the local data of the current node is pushed before checking its child nodes. Allocating real machine stack on some platforms is difficult. For example, the stack chain needs to be updated every time if we extend the stack on PowerPC. Although it is possible, its updating time overhead decreases performance. So we do the recursion in memory. </p>
<p> (2) Why don&#8217;t we simply allocate blocks of memory with <code>malloc()</code>? </p>
<p> Modern operating systems have a nice feature: they can reserve an address space instead of allocating memory. We can safely allocate memory pages inside this address space, so the stack could grow without moving memory data (this is important because of pointers). Thus we can allocate 1M address space, and use only a single memory page (usually 4K) if that is enough. However, we can still grow up to 1M anytime if needed. </p>
<p> (3) Who &quot;owns&quot; a JIT stack? </p>
<p> The owner of the stack is the user program, not the JIT studied pattern or anything else. The user program must ensure that if a stack is used by <code>pcre_exec()</code>, (that is, it is assigned to the pattern currently running), that stack must not be used by any other threads (to avoid overwriting the same memory area). The best practice for multithreaded programs is to allocate a stack for each thread, and return this stack through the JIT callback function. </p>
<p> (4) When should a JIT stack be freed? </p>
<p> You can free a JIT stack at any time, as long as it will not be used by <code>pcre_exec()</code> again. When you assign the stack to a pattern, only a pointer is set. There is no reference counting or any other magic. You can free the patterns and stacks in any order, anytime. Just <i>do not</i> call <code>pcre_exec()</code> with a pattern pointing to an already freed stack, as that will cause SEGFAULT. (Also, do not free a stack currently used by <code>pcre_exec()</code> in another thread). You can also replace the stack for a pattern at any time. You can even free the previous stack before assigning a replacement. </p>
<p> (5) Should I allocate/free a stack every time before/after calling <code>pcre_exec()</code>? </p>
<p> No, because this is too costly in terms of resources. However, you could implement some clever idea which release the stack if it is not used in let&#8217;s say two minutes. The JIT callback can help to achieve this without keeping a list of the currently JIT studied patterns. </p>
<p> (6) OK, the stack is for long term memory allocation. But what happens if a pattern causes stack overflow with a stack of 1M? Is that 1M kept until the stack is freed? </p>
<p> Especially on embedded sytems, it might be a good idea to release memory sometimes without freeing the stack. There is no API for this at the moment. Probably a function call which returns with the currently allocated memory for any stack and another which allows releasing memory (shrinking the stack) would be a good idea if someone needs this. </p>
<p> (7) This is too much of a headache. Isn&#8217;t there any better solution for JIT stack handling? </p>
<p> No, thanks to Windows. If POSIX threads were used everywhere, we could throw out this complicated API.</p>
<h2>Example Code</h2>
<p>This is a single-threaded example that specifies a JIT stack without using a callback. </p>
<p>&nbsp;<wbr>&nbsp;int rc;<br />
&nbsp;<wbr>&nbsp;int ovector[30];<br />
&nbsp;<wbr>&nbsp;pcre&nbsp;*re;<br />
&nbsp;<wbr>&nbsp;pcre_extra&nbsp;*extra;<br />
&nbsp;<wbr>&nbsp;pcre_jit_stack&nbsp;*jit_stack; </p>
<p>&nbsp;<wbr>&nbsp;re&nbsp;=&nbsp;pcre_compile(pattern, 0,&nbsp;&amp;error,&nbsp;&amp;erroffset, NULL);<br />
&nbsp;<wbr>&nbsp;/*&nbsp;Check for errors&nbsp;*/<br />
&nbsp;<wbr>&nbsp;extra&nbsp;=&nbsp;pcre_study(re, PCRE_STUDY_JIT_COMPILE,&nbsp;&amp;error);<br />
&nbsp;<wbr>&nbsp;jit_stack&nbsp;=&nbsp;pcre_jit_stack_alloc(32*1024, 512*1024);<br />
&nbsp;<wbr>&nbsp;/*&nbsp;Check for error&nbsp;(NULL)&nbsp;*/<br />
&nbsp;<wbr>&nbsp;pcre_assign_jit_stack(extra, NULL, jit_stack);<br />
&nbsp;<wbr>&nbsp;rc&nbsp;=&nbsp;pcre_exec(re, extra, subject, length, 0, 0, ovector, 30);<br />
&nbsp;<wbr>&nbsp;/*&nbsp;Check results&nbsp;*/<br />
&nbsp;<wbr>&nbsp;pcre_free(re);<br />
&nbsp;<wbr>&nbsp;pcre_free_study(extra);<br />
&nbsp;<wbr>&nbsp;pcre_jit_stack_free(jit_stack);</p>
<h2>Jit Fast Path Api</h2>
<p>Because the API described above falls back to interpreted execution when JIT is not available, it is convenient for programs that are written for general use in many environments. However, calling JIT via <code>pcre_exec()</code> does have a performance impact. Programs that are written for use where JIT is known to be available, and which need the best possible performance, can instead use a &quot;fast path&quot; API to call JIT execution directly instead of calling <code>pcre_exec()</code> (obviously only for patterns that have been successfully studied by JIT). </p>
<p> The fast path function is called <code>pcre_jit_exec()</code>, and it takes exactly the same arguments as <code>pcre_exec()</code>, plus one additional argument that must point to a JIT stack. The JIT stack arrangements described above do not apply. The return values are the same as for <code>pcre_exec()</code>. </p>
<p> When you call <code>pcre_exec()</code>, as well as testing for invalid options, a number of other sanity checks are performed on the arguments. For example, if the subject pointer is NULL, or its length is negative, an immediate error is given. Also, unless PCRE_NO_UTF[8|16|32] is set, a UTF subject string is tested for validity. In the interests of speed, these checks do not happen on the JIT fast path, and if invalid data is passed, the result is undefined. </p>
<p> Bypassing the sanity checks and the <code>pcre_exec()</code> wrapping can give speedups of more than 10%.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pcreapi/">pcreapi</a></code>(3)</p>
<h2>Author</h2>
<pre>Philip Hazel (FAQ by Zoltan Herczeg)
University Computing Service
Cambridge CB2 3QH, England.</pre>
<h2>Revision</h2>
<pre>Last updated: 17 March 2013
Copyright (c) 1997-2013 University of Cambridge.</pre>
