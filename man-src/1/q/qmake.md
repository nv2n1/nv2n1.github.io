---
title: "qmake(1)"
name: "qmake"
section: "1"
letter: "q"
url: "/docs/linux/man/1-qmake/"
description: "qmake – distributed parallel make, scheduling by xxQS_NAMExx."
---

<h2 class="name">NAME</h2>
<p> qmake &#8211; distributed parallel make, scheduling by xxQS_NAMExx.</p>
<h2>SYNTAX</h2>
<p> <code>qmake</code> [<i>options</i>] &#8212; [<i>gmake options</i>]</p>
<h2>DESCRIPTION</h2>
<p> <i>Qmake</i> is a parallel, distributed <i><a href="/docs/linux/man/1-make/">make</a></i>(1) utility. Scheduling of the parallel <i>make</i> tasks is done by xxQS_NAMExx. It is based on GNU make, version 3.82 ( gmake ). Both xxQS_NAMExx and GNU make command line options can be specified. They are separated by &quot;&#8211;&quot;. </p>
<p> All xxQS_NAMExx options valid with or can be specified with <i>qmake</i>. See for a description of all xxQS_NAMExx command line options. The GNU Make manual (via <i>info</i>) or the <i><a href="/docs/linux/man/1-make/">make</a></i>(1) manual page describes the <i>gmake</i> command line syntax. </p>
<p> The syntax of <i>qmake</i> makefiles corresponds to <i>gmake</i> and is described in the &quot;GNU Make Manual&quot;. </p>
<p> A typical qmake call will use the xxQS_NAMExx command line options <code>-cwd</code> to have a scheduled make started in the current working directory on the execution host, <code>-v PATH</code> if the xxQS_NAMExx environment is not set up in the user&#8217;s <i>.cshrc</i> Or <i>.profile</i> shell resource file, and also request slots in a parallel environment (see </p>
<p> If no resource request (xxQS_NAMExx command line option <code>-l</code>) is specified, <i>qmake</i> will use the environment variable SGE_ARCH to request the same architecture as the submit host for task execution. If SGE_ARCH is set, the architecture specified in SGE_ARCH will be requested by inserting the option <code>-l arch=$SGE_ARCH</code> into the command line options. If SGE_ARCH is not set, the make tasks can be executed on any available architecture. As this is critical for typical make (compile) jobs, a warning will be output. </p>
<p> <i>qmake </i> has two different modes for allocating xxQS_NAMExx resources for the parallel execution of tasks:</p>
<dl>
<dt>1.</p>
<dd> Allocation of resources using a parallel environment. If the <code>-pe</code> option is used on the qmake command line, a parallel job is scheduled by xxQS_NAMExx. The make rules are executed as tasks within this parallel job.</p>
<dt>2.</p>
<dd> Dynamic allocation of resources. If no parallel environment is requested when submitting a qmake job, each make rule will generate an individual xxQS_NAMExx qrsh job. All resource requests given to <i>qmake</i> will be inherited by the jobs processing the make rules.</dl>
<p> In dynamic allocation mode, additional resource requests for individual rules can be specified by preceding the rule by the definition of an environment variable SGE_RREQ. The rule then takes the form</p>
<dl>
<dt>
<dd> SGE_RREQ=&quot;<i>request</i>&quot; <i>rule</i></dl>
<p> e.g.</p>
<dl>
<dt>
<dd> SGE_RREQ=&quot;-l lic=1&quot; cc -c &#8230;</dl>
<p> If such makefile rules are executed in a make utility other than <i>qmake</i>, the environment variable SGE_RREQ will be set in the environment established for the rule&#8217;s execution &#8211; presumably without any effect.</p>
<h2>EXAMPLES</h2>
<pre>
<dl><dt><dd>qmake -cwd -v PATH -pe compiling 1-10 --
</dl>
</pre>
<p> will request between 1 and 10 slots in parallel environment &quot;compiling&quot;. If the SGE_ARCH environment variable is set to the machine architecture, a resource request will be inserted into the qmake command line to start the qmake job on the same architecture as the submit host. The <i>make</i> tasks will inherit the complete environment of the calling shell, and as as many parallel tasks will execute as slots have been granted by xxQS_NAMExx. </p>
<pre>
<dl><dt><dd>qmake -l arch=sol-sparc -cwd -v PATH -- -j 4
</dl>
</pre>
<p> will submit each make rule as an individual qrsh job. A maximum of 4 tasks will be processed in parallel. The qmake job will be started on a machine of architecture sol-sparc. This resource request will also be inherited by the make tasks, i.e. all jobs created for the execution of make tasks will request the architecture sol-sparc. </p>
<p> If the following Makefile is submitted with the above command line, additional resource requests will be made for individual rules: For the compile and link rules, compiler licenses (comp) and linker licenses (link) will be requested, in addition to the resource request made for the whole job (-l arch=sol-sparc) on the command line. </p>
<pre>
<dl><dt><dd>all: test
clean:
        rm -f test main.o functions.o
test: main.o functions.o
        SGE_RREQ=&quot;-l link=1&quot; ld -o test main.o functions.o
main.o: main.c
        SGE_RREQ=&quot;-l comp=1&quot; cc -c -DALIASPATH=
functions.o: functions.c
        SGE_RREQ=&quot;-l comp=1&quot; cc -c -DALIASPATH=</dl>
</pre>
<p> The command line</p>
<pre>
<dl><dt><dd>qmake -cwd -v PATH -l arch=sol-sparc64 -pe make 3 --
</dl>
</pre>
<p> will request 3 parallel <i>make</i> tasks to be executed on hosts of architecture &quot;sol-sparc64&quot;. The submit may be done on a host of any architecture. </p>
<p> The shell script </p>
<pre>
<dl><dt><dd>#!/bin/sh
qmake -inherit --
</dl>
</pre>
<p> can be submitted by </p>
<pre>
<dl><dt><dd>qsub -cwd -v PATH -pe make 1-10 [further xxqs_name_sxx options] &lt;script&gt;
</dl>
</pre>
<p> <i>Qmake</i> will inherit the resources granted for the job submitted above under parallel environment &quot;make&quot;.</p>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt><code>xxQS_NAME_Sxx_ROOT</code></p>
<dd> Specifies the location of the xxQS_NAMExx standard configuration files.</p>
<dt><code>xxQS_NAME_Sxx_CELL</code></p>
<dd> If set, specifies the default xxQS_NAMExx cell. To address a xxQS_NAMExx cell <i>qmake</i> uses (in the order of precedence): </p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> The name of the cell specified in the environment variable xxQS_NAME_Sxx_CELL, if it is set. </p>
<p> The name of the default cell, i.e. <code>default</code>. </p>
</dl>
</dl>
<dt><code>xxQS_NAME_Sxx_DEBUG_LEVEL</code></p>
<dd> If set, specifies that debug information should be written to stderr. In addition the level of detail in which debug information is generated is defined.</p>
<dt><code>SGE_ARCH</code></p>
<dd> The architecture of the submit host. If this variable is set in the submission environment, qmake will request the given architecture for job execution (see DESCRIPTION above).</dl>
<h2>KNOWN PROBLEMS</h2>
<h3>Slow NFS server</h3>
<p> Very low file server performance may lead to problems on dependent files. </p>
<p> Example: Host a compiles a.c to a.o, host b compiles b.c to b.o, host c shall link program c from a.o and b.o. In case of very bad NFS performance, host c might not yet see files a.o and b.o.</p>
<h3>Multiple commands in one rule</h3>
<p> If multiple commands are executed in one rule, the makefile has to ensure that they are handled as one command line. </p>
<p> Example: </p>
<pre>
<dl><dt><dd>libx.a:
<dl><dt><dd>cc -c x.c
ar ru libx.a x.o
</dl>
</dl>
</pre>
<p> Building libx.a will fail if the commands are executed in parallel (and possibly on different hosts). Write the following instead: </p>
<pre>
<dl><dt><dd>libx.a:
<dl><dt><dd>cc -c x.c ; ar ru libx.a x.o
</dl>
</dl>
</pre>
<p> or </p>
<pre>
<dl><dt><dd>libx.a:
<dl><dt><dd>cc -c x.c ; \
ar ru libx.a x.o
</dl>
</dl>
</pre>
<h2>SEE ALSO</h2>
<p> as well as <i><a href="/docs/linux/man/1-make/">make</a></i>(1) (GNU make manpage) and <i>The</i>GNU<i>Make</i>Manual via <i><a href="/docs/linux/man/1-info/">info</a></i>(1).</p>
<h2>COPYRIGHT</h2>
<p> <i>Qmake</i> Is based on GNU Make (<i>gmake</i>), which is copyright by the Free Software Foundation, Inc., Boston, MA, and is protected by the GNU General Public License.<br />
 See and the information provided in <i>&lt;xxqs_name_sxx_root&gt;/doc/LICENCES</i> for a statement of further rights and permissions. </p>
<h2>Index</h2>
