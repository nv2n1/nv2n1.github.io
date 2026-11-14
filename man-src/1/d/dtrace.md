---
title: "dtrace(1)"
name: "dtrace"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dtrace/"
description: "dtrace – Dtrace compatible user application static probe generation tool."
---

<h2>NAME</h2>
<p> dtrace &#8211; Dtrace compatible user application static probe generation tool. </p>
<h2>SYNOPSIS</h2>
<p> <code>dtrace -s </code><i>file</i> [<code>OPTIONS</code>] </p>
<h2>DESCRIPTION</h2>
<p> The dtrace command converts probe descriptions defined in <i>file.d</i> into a probe header file via the <code>-h</code> option or a probe description file via the <code>-G</code> option. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code></p>
<dd> generate a systemtap header file. </p>
<dt><code>-G</code></p>
<dd> generate a systemtap probe definition object file. </p>
<dt><code>-o </code><i>file</i></p>
<dd> is the name of the output file. If the <code>-G</code> option is given then the output file will be called <i>file.o</i>; if the <code>-h</code> option is given then the output file will be called <i>file.h</i>. </p>
<dt><code>-C</code></p>
<dd> run the cpp preprocessor on the input file when the <code>-h</code> option is given. </p>
<dt><code>-I </code><i>file</i></p>
<dd> give this include path to cpp when the <code>-C</code> option is given. </p>
<dt><code>-k</code></p>
<dd> keep temporary files, for example the C language source for the <code>-G</code> option. </p>
</dl>
<h2>EXAMPLES</h2>
<p> Systemtap is source compatible with dtrace user application static probe support. Given a file <i>test.d</i> containing: </p>
<dl>
<dt>
<dd>
<pre><code>
provider sdt_probes
{
    probe test_0(int type);
    probe test_1(struct astruct node);
};
struct astruct {
    int a;
    int b;
};
</code></pre>
</dl>
<p> Then the command <i>&quot;dtrace -s test.d -G&quot;</i> will create the probe definition file <i>test.o</i> and the command <i>&quot;dtrace -stest.d -h&quot;</i> will create the probe header file <i>test.h</i> Subsequently the application can use the generated macros this way: </p>
<dl>
<dt>
<dd>
#include &#8220;test.h&#8221;<br />
&#8230; struct astruct s;<br />
&#8230; SDT_PROBES_TEST_0(value);<br />
&#8230; if (SDT_PROBES_TEST_1_ENABLED())<br />
    SDT_PROBES_TEST_1(expensive_function(s));
</dl>
<h2>SEMAPHORES</h2>
<p> Semaphores are flag variables used by probes as a way of bypassing potentially costly processing to prepare arguments for probes that may not even be active. They are automatically set/cleared by systemtap when a relevant script is running, so the argument setup cost is only paid when necessary. These semaphore variables are defined within the the <i>&quot;test.o&quot;</i> object file, which must therefore be linked into an application. </p>
<p> Sometimes, semaphore variables are not necessary nor helpful. Skipping them can simplify the build process, by omitting the extra <i>&quot;test.o&quot;</i> file. To skip dependence upon semaphore variables, include <i>&quot;&lt;sys/sdt.h&gt;&quot;</i> within the application before <i>&quot;test.h&quot;</i>: </p>
<dl>
<dt>
<dd>
<pre><code>
#include "test.h"
#include &lt;sys/sdt.h&gt;
... struct astruct s;
... SDT_PROBES_TEST_0(value);
... if (SDT_PROBES_TEST_1_ENABLED())
    SDT_PROBES_TEST_1(cheap_function(s));
</code></pre>
</dl>
<p> In this mode, the ENABLED() test is fixed at 1. </p>
<h2>SEE ALSO</h2>
<pre>
<i><a href="//www.systutorials.com/docs/linux/man/1-stap/">stap</a></i>(1),
<i><a href="//www.systutorials.com/docs/linux/man/7-stappaths/">stappaths</a></i>(7)
</pre>
<h2>BUGS</h2>
<p> Use the Bugzilla link of the project web page or our mailing list. <code><a rel="nofollow" href="http://sourceware.org/systemtap/">http://sourceware.org/systemtap/</a></code>, <code>&lt;systemtap [at] sourceware.org&gt;</code>. </p>
<p> <i><a href="//www.systutorials.com/docs/linux/man/7stap-error::reporting/">error::reporting</a></i>(7stap), <code><a rel="nofollow" href="https://sourceware.org/systemtap/wiki/HowToReportBugs">https://sourceware.org/systemtap/wiki/HowToReportBugs</a></code> </p>
<h2>Index</h2>
