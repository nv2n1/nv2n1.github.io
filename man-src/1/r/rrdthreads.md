---
title: "rrdthreads(1)"
name: "rrdthreads"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rrdthreads/"
---

<h2 class="name">NAME</h2>
 

 rrdthreads - Provisions for linking the RRD library to use in multi-threaded programs 

<h2>SYNOPSIS</h2>

 Using librrd in multi-threaded programs requires some extra precautions, as the <font SIZE="-1">RRD</font> library in its original form was not thread-safe at all. This document describes requirements and pitfalls on the way to use the multi-threaded version of librrd in your own programs. It also gives hints for future <font SIZE="-1">RRD</font> development to keep the library thread-safe. 

 Currently only some <font SIZE="-1">RRD</font> operations are implemented in a thread-safe way. They all end in the usual &quot;<tt>&quot;_r&quot;</tt>&quot; suffix.

<h2>DESCRIPTION</h2>

 In order to use librrd in multi-threaded programs you must:
<dl>
<dt>&bull;
<dd> Link with <i>librrd_th</i> instead of <i>librrd</i> (use <tt>&quot;-lrrd_th&quot;</tt> when linking)
<dt>&bull;
<dd> Use the &quot;<tt>&quot;_r&quot;</tt>&quot; functions instead of the normal API-functions
<dt>&bull;
<dd> Do not use any at-style time specifications. Parsing of such time specifications is terribly non-thread-safe.
<dt>&bull;
<dd> Never use non *<tt>&quot;_r&quot;</tt> functions unless it is explicitly documented that the function is tread-safe.
<dt>&bull;
<dd> Every thread <font SIZE="-1">SHOULD</font> call <tt>&quot;rrd_get_context()&quot;</tt> before its first call to any <tt>&quot;librrd_th&quot;</tt> function in order to set up thread specific data. This is not strictly required, but it is the only way to test if memory allocation can be done by this function. Otherwise the program may die with a <font SIZE="-1">SIGSEGV</font> in a low-memory situation.
<dt>&bull;
<dd> Always call <tt>&quot;rrd_error_clear()&quot;</tt> before any call to the library. Otherwise the call might fail due to some earlier error.</dl>

<h3><font SIZE="-1">NOTES</font> <font SIZE="-1">FOR</font> <font SIZE="-1">RRD</font> <font SIZE="-1">CONTRIBUTORS</font></h3>

 Some precautions must be followed when developing <font SIZE="-1">RRD</font> from now on:
<dl>
<dt>&bull;
<dd> Only use thread-safe functions in library code. Many often used libc functions aren't thread-safe. Take care in the following situations or when using the following library functions:
<dl>
<dt>
<dd>
<dl>
<dt>&bull;
<dd> Direct calls to <tt>&quot;strerror()&quot;</tt> must be avoided: use <tt>&quot;rrd_strerror()&quot;</tt> instead, it provides a per-thread error message.
<dt>&bull;
<dd> The <tt>&quot;getpw*&quot;</tt>, <tt>&quot;getgr*&quot;</tt>, <tt>&quot;gethost*&quot;</tt> function families (and some more <tt>&quot;get*&quot;</tt> functions) are not thread-safe: use the *<tt>&quot;_r&quot;</tt> variants
<dt>&bull;
<dd> Time functions: <tt>&quot;asctime&quot;</tt>, <tt>&quot;ctime&quot;</tt>, <tt>&quot;gmtime&quot;</tt>, <tt>&quot;localtime&quot;</tt>: use *<tt>&quot;_r&quot;</tt> variants
<dt>&bull;
<dd> <tt>&quot;strtok&quot;</tt>: use <tt>&quot;strtok_r&quot;</tt>
<dt>&bull;
<dd> <tt>&quot;tmpnam&quot;</tt>: use <tt>&quot;tmpnam_r&quot;</tt>
<dt>&bull;
<dd> Many others (lookup documentation)</dl>
</dl>

<dl>
<dt>
<dd></dl>

<dt>&bull;
<dd> A header file named <i>rrd_is_thread_safe.h</i> is provided that works with the <font SIZE="-1">GNU</font> C-preprocessor to ``poison'' some of the most common non-thread-safe functions using the <tt>&quot;#pragma GCC poison&quot;</tt> directive. Just include this header in source files you want to keep thread-safe.
<dt>&bull;
<dd> Do not introduce global variables! 

 If you really, really have to use a global variable you may add a new field to the <tt>&quot;rrd_context&quot;</tt> structure and modify <i>rrd_error.c</i>, <i>rrd_thread_safe.c</i> and <i>rrd_non_thread_safe.c</i>
<dt>&bull;
<dd> Do not use <tt>&quot;getopt&quot;</tt> or <tt>&quot;getopt_long&quot;</tt> in *<tt>&quot;_r&quot;</tt> (neither directly nor indirectly). 

 <tt>&quot;getopt&quot;</tt> uses global variables and behaves badly in a multi-threaded application when called concurrently. Instead provide a *_r function taking all options as function parameters. You may provide argc and **argv arguments for variable length argument lists. See <tt>&quot;rrd_update_r&quot;</tt> as an example.
<dt>&bull;
<dd> Do not use the <tt>&quot;rrd_parsetime&quot;</tt> function! 

 It uses lots of global variables. You may use it in functions not designed to be thread-safe, like in functions wrapping the <tt>&quot;_r&quot;</tt> version of some operation (e.g., <tt>&quot;rrd_create&quot;</tt>, but not in <tt>&quot;rrd_create_r&quot;</tt>)</dl>

<h3><font SIZE="-1">CURRENTLY</font> <font SIZE="-1">IMPLEMENTED</font> <font SIZE="-1">THREAD</font> <font SIZE="-1">SAFE</font> <font SIZE="-1">FUNCTIONS</font></h3>

 Currently there exist thread-safe variants of <tt>&quot;rrd_update&quot;</tt>, <tt>&quot;rrd_create&quot;</tt>, <tt>&quot;rrd_dump&quot;</tt>, <tt>&quot;rrd_info&quot;</tt>, <tt>&quot;rrd_last&quot;</tt>, and <tt>&quot;rrd_fetch&quot;</tt>.

<h2>AUTHOR</h2>

 Peter Stamfest &lt;peter [at] stamfest.at&gt; 

<h2>Index</h2>



<dt><a HREF="#lbAG">AUTHOR</a>
<dd></dl>
