---
title: "shtool-scpp(1)"
name: "shtool-scpp"
section: "1"
letter: "s"
url: "/docs/linux/man/1-shtool-scpp/"
description: "shtool scpp – GNU shtool C source file pre-processor"
---

<h2 class="name">NAME</h2>
<p> shtool scpp &#8211; GNU shtool C source file pre-processor </p>
<h2>SYNOPSIS</h2>
<p> <code>shtool scpp</code> [<code>-v</code>|<code>&#8211;verbose</code>] [<code>-p</code>|<code>&#8211;preserve</code>] [<code>-f</code>|<code>&#8211;filter</code> <i>filter</i>] [<code>-o</code>|<code>&#8211;output</code> <i>ofile</i>] [<code>-t</code>|<code>&#8211;template</code> <i>tfile</i>] [<code>-M</code>|<code>&#8211;mark</code> <i>mark</i>] [<code>-D</code>|<code>&#8211;define</code> <i>dname</i>] [<code>-C</code>|<code>&#8211;class</code> <i>cname</i>] <i>file</i> [<i>file</i> &#8230;]</p>
<h2>DESCRIPTION</h2>
<p> This command is an additional <font SIZE="-1">ANSI C</font> source file pre-processor for sharing <i><a href="/docs/linux/man/1-cpp/">cpp</a></i>(1) code segments, internal variables and internal functions. The intention for this comes from writing libraries in <font SIZE="-1">ANSI C.</font> Here a common shared internal header file is usually used for sharing information between the library source files. </p>
<p> The operation is to parse special constructs in <i>file</i>s, generate a few things out of these constructs and insert them at position <i>mark</i> in <i>tfile</i> by writing the output to <i>ofile</i>. Additionally the <i>file</i>s are never touched or modified. Instead the constructs are removed later by the <i><a href="/docs/linux/man/1-cpp/">cpp</a></i>(1) phase of the build process. The only prerequisite is that every <i>file</i> has a &#8220;<tt>&quot;#include &quot;&quot;</tt><i>ofile</i><tt>&quot;&quot;&quot;</tt>&#8221; at the top. </p>
<p> This command provides the following features: First it avoids namespace pollution and reduces prototyping efforts for internal symbols by recognizing functions and variables which are defined with the storage class identifier &#8220;<i>cname</i>&#8221;. For instance if <i>cname</i> is &#8220;intern&#8221;, a function &#8220;<tt>&quot;intern void *foobar(int quux)&quot;</tt>&#8221; in one of the <i>file</i>s is translated into both a &#8220;<tt>&quot;#define foobar __foobar&quot;</tt>&#8221; and a &#8220;<tt>&quot;extern void *foobar(int quux);&quot;</tt>&#8221; in <i>ofile</i>. Additionally a global &#8220;<tt>&quot;#define&quot;</tt> <i>cname</i> <tt>&quot;/**/&quot;</tt>&#8221; is also created in <i>ofile</i> to let the compiler silently ignore this additional storage class identifier. </p>
<p> Second, the library source files usually want to share <tt>&quot;typedef&quot;</tt>s, <tt>&quot;#define&quot;</tt>s, etc. over the source file boundaries. To achieve this one can either place this stuff manually into <i>tfile</i> or use the second feature of <code>scpp</code>: All code in <i>file</i>s encapsulated with &#8220;<tt>&quot;#if &quot;</tt><i>dname</i> &#8230; <tt>&quot;#endif&quot;</tt>&#8221; is automatically copied to <i>ofile</i>. Additionally a global &#8220;<tt>&quot;#define&quot;</tt> <i>dname</i> <tt>0</tt>&#8221; is also created in <i>ofile</i> to let the compiler silently skip this parts (because it was already found in the header).</p>
<h2>OPTIONS</h2>
<p> The following command line options are available.</p>
<dl>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> Display some processing information.</p>
<dt><code>-p</code>, <code>&#8211;preserve</code></p>
<dd> Preserves <i>ofile</i> independent of the generated &#8220;#line&#8221; lines. This is useful for Makefiles if the real contents of <i>ofile</i> will not change, just line numbers. Default is to overwrite.</p>
<dt><code>-f</code>, <code>&#8211;filter</code> <i>filter</i></p>
<dd> Apply one or more pre-processing <i><a href="/docs/linux/man/1-sed/">sed</a></i>(1) <i>filter</i> commands (usually of type &#8220;<tt>&quot;s/.../.../&quot;</tt>&#8221;) to each input file before their input is parsed. This option can occur multiple times.</p>
<dt><code>-o</code>, <code>&#8211;output</code> <i>ofile</i></p>
<dd> Output file name. Default is <tt>&quot;lib.h&quot;</tt>.</p>
<dt><code>-t</code>, <code>&#8211;template</code> <i>tfile</i></p>
<dd> Template file name. Default is <tt>&quot;lib.h.in&quot;</tt>.</p>
<dt><code>-M</code>, <code>&#8211;mark</code> <i>mark</i></p>
<dd> Mark to be replaced by generated constructs. Default is <tt>&quot;%%MARK%%&quot;</tt>.</p>
<dt><code>-D</code>, <code>&#8211;define</code> <i>dname</i></p>
<dd> <font SIZE="-1">FIXME.</font> Default is <tt>&quot;cpp&quot;</tt>.</p>
<dt><code>-C</code>, <code>&#8211;class</code> <i>cname</i></p>
<dd> <font SIZE="-1">FIXME.</font> Default is <tt>&quot;intern&quot;</tt>.</dl>
<h2>EXAMPLE</h2>
<pre><code>
#Makefile
SRCS = foo_bar.c foo_quux.c
           foo_p.h : foo_p.h.in
                         shtool scpp -
       o foo_p.h - t foo_p.h.in - M % % MARK % % -D cpp - C intern $(SRCS)
/* foo_p.h.in */
#ifndef FOO_P_H
#define FOO_P_H
                                                              % % MARK % %
#endif /* FOO_P_H */
/* foo_bar.c */
#include "foo_p.h"
#if cpp
#define OURS_INIT 4711
#endif
                                                              intern int ours;
static int myone = 0815;
intern int bar(void)
{
    ours += myone;
}
/* foo_quux.c */
#include "foo_p.h"
int main(int argc, char *argv[])
{
    int i;
    ours = OURS_INIT for (i = 0; i &lt; 10; i++)
    {
        bar();
        printf("ours now %d
", ours);
    }
    return 0;
}
</code></pre>
<h2>HISTORY</h2>
<p> The <font SIZE="-1"><code>GNU</code></font><code> shtool</code> <code>scpp</code> command was originally written by Ralf S. Engelschall &lt;rse [at] engelschall.com&gt; in 1999 for <font SIZE="-1"><code>GNU</code></font><code> shtool</code>. Its was prompted by the need to have a pre-processing facility in the <font SIZE="-1"><code>GNU</code></font><code> pth</code> project.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-shtool/">shtool</a></i>(1), <i><a href="/docs/linux/man/1-cpp/">cpp</a></i>(1). </p>
<h2>Index</h2>
