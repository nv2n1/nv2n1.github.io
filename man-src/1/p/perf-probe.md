---
title: "perf-probe(1)"
name: "perf-probe"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perf-probe/"
description: "perf-probe – Define new dynamic tracepoints"
---

<h2 class="name">NAME</h2>
<p> perf-probe &#8211; Define new dynamic tracepoints </p>
<h2>SYNOPSIS</h2>
<pre><code>
perf probe[options]-- add = PROBE[...] or
                            perf probe[options] PROBE or
                            perf probe[options]-- del = [GROUP:] EVENT[...] or
                                                        perf probe-- list or
                                                        perf probe[options]-- line = LINE or
                                                                                     perf probe[options]-- vars = PROBEPOINT
</code></pre>
<h2>DESCRIPTION</h2>
<p> This command defines dynamic tracepoint events, by symbol and registers without debuginfo, or by C expressions (C line numbers, C function names, and C local variables) with debuginfo.</p>
<h2>OPTIONS</h2>
<p> -k, &#8211;vmlinux=PATH</p>
<dl>
<dt>
<dd> Specify vmlinux path which has debuginfo (Dwarf binary).</dl>
<p> -m, &#8211;module=MODNAME|PATH</p>
<dl>
<dt>
<dd> Specify module name in which perf-probe searches probe points or lines. If a path of module file is passed, perf-probe treat it as an offline module (this means you can add a probe on a module which has not been loaded yet).</dl>
<p> -s, &#8211;source=PATH</p>
<dl>
<dt>
<dd> Specify path to kernel source.</dl>
<p> -v, &#8211;verbose</p>
<dl>
<dt>
<dd> Be more verbose (show parsed arguments, etc).</dl>
<p> -a, &#8211;add=</p>
<dl>
<dt>
<dd> Define a probe event (see PROBE SYNTAX for detail).</dl>
<p> -d, &#8211;del=</p>
<dl>
<dt>
<dd> Delete probe events. This accepts glob wildcards(<i>*</i>, <i>?</i>) and character classes(e.g. [a-z], [!A-Z]).</dl>
<p> -l, &#8211;list</p>
<dl>
<dt>
<dd> List up current probe events.</dl>
<p> -L, &#8211;line=</p>
<dl>
<dt>
<dd> Show source code lines which can be probed. This needs an argument which specifies a range of the source code. (see LINE SYNTAX for detail)</dl>
<p> -V, &#8211;vars=</p>
<dl>
<dt>
<dd> Show available local variables at given probe point. The argument syntax is same as PROBE SYNTAX, but NO ARGs.</dl>
<p> &#8211;externs</p>
<dl>
<dt>
<dd> (Only for &#8211;vars) Show external defined variables in addition to local variables.</dl>
<p> -F, &#8211;funcs</p>
<dl>
<dt>
<dd> Show available functions in given module or kernel. With -x/&#8211;exec, can also list functions in a user space executable / shared library.</dl>
<p> &#8211;filter=FILTER</p>
<dl>
<dt>
<dd> (Only for &#8211;vars and &#8211;funcs) Set filter. FILTER is a combination of glob pattern, see FILTER PATTERN for detail. Default FILTER is &quot;!<i>k???tab_* &amp; !</i>crc_*&quot; for &#8211;vars, and &quot;!_*&quot; for &#8211;funcs. If several filters are specified, only the last filter is used.</dl>
<p> -f, &#8211;force</p>
<dl>
<dt>
<dd> Forcibly add events with existing name.</dl>
<p> -n, &#8211;dry-run</p>
<dl>
<dt>
<dd> Dry run. With this option, &#8211;add and &#8211;del doesn&#8217;t execute actual adding and removal operations.</dl>
<p> &#8211;max-probes</p>
<dl>
<dt>
<dd> Set the maximum number of probe points for an event. Default is 128.</dl>
<p> -x, &#8211;exec=PATH</p>
<dl>
<dt>
<dd> Specify path to the executable or shared library file for user space tracing. Can also be used with &#8211;funcs option.</dl>
<p> &#8211;demangle-kernel</p>
<dl>
<dt>
<dd> Demangle kernel symbols.</dl>
<p> In absence of -m/-x options, perf probe checks if the first argument after the options is an absolute path name. If its an absolute path, perf probe uses it as a target module/target user space binary to probe.</p>
<h2>PROBE SYNTAX</h2>
<p> Probe points are defined by following syntax. </p>
<dl>
<dt>
<dd>
1) Define event based on function name<br />
 [EVENT=]FUNC[@SRC][:RLN|+OFFS|%return|;PTN] [ARG &#8230;]
</dl>
<dl>
<dt>
<dd>
2) Define event based on source file with line number<br />
 [EVENT=]SRC:ALN [ARG &#8230;]
</dl>
<dl>
<dt>
<dd>
3) Define event based on source file with lazy pattern<br />
 [EVENT=]SRC;<br />
PTN[ARG&#8230;]
</dl>
<p> <i>EVENT</i> specifies the name of new event, if omitted, it will be set the name of the probed function. Currently, event group name is set as <i>probe</i>. <i>FUNC</i> specifies a probed function name, and it may have one of the following options; <i>+OFFS</i> is the offset from function entry address in bytes, <i>:RLN</i> is the relative-line number from function entry line, and <i>%return</i> means that it probes function return. And <i>;PTN</i> means lazy matching pattern (see LAZY MATCHING). Note that <i>;PTN</i> must be the end of the probe point definition. In addition, <i>@SRC</i> specifies a source file which has that function. It is also possible to specify a probe point by the source line number or lazy matching by using <i>SRC:ALN</i> or <i>SRC;PTN</i> syntax, where <i>SRC</i> is the source file path, <i>:ALN</i> is the line number and <i>;PTN</i> is the lazy matching pattern. <i>ARG</i> specifies the arguments of this probe point, (see PROBE ARGUMENT).</p>
<h2>PROBE ARGUMENT</h2>
<p> Each probe argument follows below syntax. </p>
<dl>
<dt>
<dd>
[NAME = ] LOCALVAR | $retval | % REG | @SYMBOL[:TYPE]
</dl>
<p> <i>NAME</i> specifies the name of this argument (optional). You can use the name of local variable, local data structure member (e.g. var&rarr;field, var.field2), local array with fixed index (e.g. array[1], var&rarr;array[0], var&rarr;pointer[2]), or kprobe-tracer argument format (e.g. $retval, %ax, etc). Note that the name of this argument will be set as the last member name if you specify a local data structure member (e.g. field2 for <i>var&rarr;field1.field2</i>.) <i>TYPE</i> casts the type of this argument (optional). If omitted, perf probe automatically set the type based on debuginfo. You can specify <i>string</i> type only for the local variable or structure member which is an array of or a pointer to <i>char</i> or <i>unsigned char</i> type. </p>
<p> On x86 systems %REG is always the short form of the register: for example %AX. %RAX or %EAX is not valid.</p>
<h2>LINE SYNTAX</h2>
<p> Line range is described by following syntax. </p>
<dl>
<dt>
<dd>
<pre><code>
"FUNC[@SRC][:RLN[+NUM|-RLN2]]|SRC[:ALN[+NUM|-ALN2]]"
</code></pre>
</dl>
<p> FUNC specifies the function name of showing lines. <i>RLN</i> is the start line number from function entry line, and <i>RLN2</i> is the end line number. As same as probe syntax, <i>SRC</i> means the source file path, <i>ALN</i> is start line number, and <i>ALN2</i> is end line number in the file. It is also possible to specify how many lines to show by using <i>NUM</i>. Moreover, <i>FUNC@SRC</i> combination is good for searching a specific function when several functions share same name. So, &quot;source.c:100-120&quot; shows lines between 100th to l20th in source.c file. And &quot;func:10+20&quot; shows 20 lines from 10th line of func function.</p>
<h2>LAZY MATCHING</h2>
<dl>
<dt>
<dd>
<pre>
The lazy line matching is similar to glob matching but ignoring spaces in both of pattern and target. So this accepts wildcards('*', '?') and character classes(e.g. [a-z], [!A-Z]).
</pre>
</dl>
<p> e.g. <i>a=*</i> can matches <i>a=b</i>, <i>a = b</i>, <i>a == b</i> and so on. </p>
<p> This provides some sort of flexibility and robustness to probe point definitions against minor code changes. For example, actual 10th line of schedule() can be moved easily by modifying schedule(), but the same line matching <i>rq=cpu_rq*</i> may still exist in the function.)</p>
<h2>FILTER PATTERN</h2>
<dl>
<dt>
<dd>
<pre>
The filter pattern is a glob matching pattern(s) to filter variables.
In addition, you can use &quot;!&quot; for specifying filter-out rule. You also can give several rules combined with &quot;&amp;&quot; or &quot;|&quot;, and fold those rules as one rule by using &quot;(&quot; &quot;)&quot;.
</pre>
</dl>
<p> e.g. With &#8211;filter &quot;foo* | bar*&quot;, perf probe -V shows variables which start with &quot;foo&quot; or &quot;bar&quot;. With &#8211;filter &quot;!foo* &amp; *bar&quot;, perf probe -V shows variables which don&#8217;t start with &quot;foo&quot; and end with &quot;bar&quot;, like &quot;fizzbar&quot;. But &quot;foobar&quot; is filtered out.</p>
<h2>EXAMPLES</h2>
<p> Display which lines in schedule() can be probed: </p>
<dl>
<dt>
<dd>
<pre>
./perf probe --line schedule
</pre>
</dl>
<p> Add a probe on schedule() function 12th line with recording cpu local variable: </p>
<dl>
<dt>
<dd>
<pre>
./perf probe schedule:12 cpu
or
./perf probe --add='schedule:12 cpu'
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
this will add one or more probes which has the name start with &quot;schedule&quot;.
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
Add probes on lines in schedule() function which calls update_rq_clock().
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
./perf probe 'schedule;update_rq_clock*'
or
./perf probe --add='schedule;update_rq_clock*'
</pre>
</dl>
<p> Delete all probes on schedule(). </p>
<dl>
<dt>
<dd>
<pre>
./perf probe --del='schedule*'
</pre>
</dl>
<p> Add probes at zfree() function on /bin/zsh </p>
<dl>
<dt>
<dd>
<pre>
./perf probe -x /bin/zsh zfree or ./perf probe /bin/zsh zfree
</pre>
</dl>
<p> Add probes at malloc() function on libc </p>
<dl>
<dt>
<dd>
<pre>
./perf probe -x /lib/libc.so.6 malloc or ./perf probe /lib/libc.so.6 malloc
</pre>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-perf-trace/">perf-trace</a></code>(1), <code><a href="/docs/linux/man/1-perf-record/">perf-record</a></code>(1) </p>
<h2>Index</h2>
