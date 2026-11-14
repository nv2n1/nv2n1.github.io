---
title: "pcreprecompile(3)"
name: "pcreprecompile"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pcreprecompile/"
description: "PCRE – Perl-compatible regular expressions"
---

<p>PCRE &#8211; Perl-compatible regular expressions</p>
<h2>Saving And Re-Using Precompiled Pcre Patterns</h2>
<p>If you are running an application that uses a large number of regular expression patterns, it may be useful to store them in a precompiled form instead of having to compile them every time the application is run. If you are not using any private character tables (see the <code>pcre_maketables()</code> documentation), this is relatively straightforward. If you are using private tables, it is a little bit more complicated. However, if you are using the just-in-time optimization feature, it is not possible to save and reload the JIT data. </p>
<p> If you save compiled patterns to a file, you can copy them to a different host and run them there. If the two hosts have different endianness (byte order), you should run the <code>pcre[16|32]_pattern_to_host_byte_order()</code> function on the new host before trying to match the pattern. The matching functions return PCRE_ERROR_BADENDIANNESS if they detect a pattern with the wrong endianness. </p>
<p> Compiling regular expressions with one version of PCRE for use with a different version is not guaranteed to work and may cause crashes, and saving and restoring a compiled pattern loses any JIT optimization data.</p>
<h2>Saving A Compiled Pattern</h2>
<p>The value returned by <code>pcre[16|32]_compile()</code> points to a single block of memory that holds the compiled pattern and associated data. You can find the length of this block in bytes by calling <code>pcre[16|32]_fullinfo()</code> with an argument of PCRE_INFO_SIZE. You can then save the data in any appropriate manner. Here is sample code for the 8-bit library that compiles a pattern and writes it to a file. It assumes that the variable <i>fd</i> refers to a file that is open for output: </p>
<p>&nbsp;<wbr>&nbsp;int erroroffset, rc, size;<br />
&nbsp;<wbr>&nbsp;char&nbsp;*error;<br />
&nbsp;<wbr>&nbsp;pcre&nbsp;*re; </p>
<p>&nbsp;<wbr>&nbsp;re&nbsp;=&nbsp;pcre_compile(&quot;my pattern&quot;, 0,&nbsp;&amp;error,&nbsp;&amp;erroroffset, NULL);<br />
&nbsp;<wbr>&nbsp;if&nbsp;(re&nbsp;==&nbsp;NULL)&nbsp;{&nbsp;&#8230; handle errors &#8230;&nbsp;}<br />
&nbsp;<wbr>&nbsp;rc&nbsp;=&nbsp;pcre_fullinfo(re, NULL, PCRE_INFO_SIZE,&nbsp;&amp;size);<br />
&nbsp;<wbr>&nbsp;if&nbsp;(rc&nbsp;&lt;&nbsp;0)&nbsp;{&nbsp;&#8230; handle errors &#8230;&nbsp;}<br />
&nbsp;<wbr>&nbsp;rc&nbsp;=&nbsp;fwrite(re, 1, size, fd);<br />
&nbsp;<wbr>&nbsp;if&nbsp;(rc&nbsp;!=&nbsp;size)&nbsp;{&nbsp;&#8230; handle errors &#8230;&nbsp;} </p>
<p> In this example, the bytes that comprise the compiled pattern are copied exactly. Note that this is binary data that may contain any of the 256 possible byte values. On systems that make a distinction between binary and non-binary data, be sure that the file is opened for binary output. </p>
<p> If you want to write more than one pattern to a file, you will have to devise a way of separating them. For binary data, preceding each pattern with its length is probably the most straightforward approach. Another possibility is to write out the data in hexadecimal instead of binary, one pattern to a line. </p>
<p> Saving compiled patterns in a file is only one possible way of storing them for later use. They could equally well be saved in a database, or in the memory of some daemon process that passes them via sockets to the processes that want them. </p>
<p> If the pattern has been studied, it is also possible to save the normal study data in a similar way to the compiled pattern itself. However, if the PCRE_STUDY_JIT_COMPILE was used, the just-in-time data that is created cannot be saved because it is too dependent on the current environment. When studying generates additional information, <code>pcre[16|32]_study()</code> returns a pointer to a <code>pcre[16|32]_extra</code> data block. Its format is defined in the section on matching a pattern in the <code>pcreapi</code> documentation. The <i>study_data</i> field points to the binary study data, and this is what you must save (not the <code>pcre[16|32]_extra</code> block itself). The length of the study data can be obtained by calling <code>pcre[16|32]_fullinfo()</code> with an argument of PCRE_INFO_STUDYSIZE. Remember to check that <code>pcre[16|32]_study()</code> did return a non-NULL value before trying to save the study data.</p>
<h2>Re-Using A Precompiled Pattern</h2>
<p>Re-using a precompiled pattern is straightforward. Having reloaded it into main memory, called <code>pcre[16|32]_pattern_to_host_byte_order()</code> if necessary, you pass its pointer to <code>pcre[16|32]_exec()</code> or <code>pcre[16|32]_dfa_exec()</code> in the usual way. </p>
<p> However, if you passed a pointer to custom character tables when the pattern was compiled (the <i>tableptr</i> argument of <code>pcre[16|32]_compile()</code>), you must now pass a similar pointer to <code>pcre[16|32]_exec()</code> or <code>pcre[16|32]_dfa_exec()</code>, because the value saved with the compiled pattern will obviously be nonsense. A field in a <code>pcre[16|32]_extra()</code> block is used to pass this data, as described in the section on matching a pattern in the <code>pcreapi</code> documentation. </p>
<p> <code>Warning:</code> The tables that <code>pcre_exec()</code> and <code>pcre_dfa_exec()</code> use must be the same as those that were used when the pattern was compiled. If this is not the case, the behaviour is undefined. </p>
<p> If you did not provide custom character tables when the pattern was compiled, the pointer in the compiled pattern is NULL, which causes the matching functions to use PCRE&#8217;s internal tables. Thus, you do not need to take any special action at run time in this case. </p>
<p> If you saved study data with the compiled pattern, you need to create your own <code>pcre[16|32]_extra</code> data block and set the <i>study_data</i> field to point to the reloaded study data. You must also set the PCRE_EXTRA_STUDY_DATA bit in the <i>flags</i> field to indicate that study data is present. Then pass the <code>pcre[16|32]_extra</code> block to the matching function in the usual way. If the pattern was studied for just-in-time optimization, that data cannot be saved, and so is lost by a save/restore cycle.</p>
<h2>Compatibility With Different Pcre Releases</h2>
<p>In general, it is safest to recompile all saved patterns when you update to a new PCRE release, though not all updates actually require this.</p>
<h2>Author</h2>
<pre>Philip Hazel
University Computing Service
Cambridge CB2 3QH, England.</pre>
<h2>Revision</h2>
<pre>Last updated: 12 November 2013
Copyright (c) 1997-2013 University of Cambridge.</pre>
