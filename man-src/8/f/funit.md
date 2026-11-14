---
title: "funit(8)"
name: "funit"
section: "8"
letter: "f"
url: "/docs/linux/man/8-funit/"
description: "funit – runs frysk’s JUnit testsuite"
---

<p>funit &#8211; runs frysk&#8217;s JUnit testsuite</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>funit</code> [<code>-r&nbsp;<wbr></code><i>repeat-count</i>] [<code>&#8211;console&nbsp;<wbr></code><i>CONSOLE_LOG=LEVEL</i>] [<code>&#8211;log&nbsp;<wbr></code><i>LOG=LEVEL</i>] [<code>&#8211;arch&nbsp;<wbr></code><i>arch</i>] [<code>-n</code>] [<code>&#8211;stress</code>] [<code>&#8211;all</code>] [<code>-e&nbsp;<wbr></code><i>test-spec</i>] [<code>-i&nbsp;<wbr></code><i>test-spec</i>] [<i>test-class</i><code>&nbsp;<wbr>&#8230;</code>] [<code>-timeout&nbsp;<wbr></code><i>timeout</i>]</dl>
<h2>Description</h2>
<p><code>funit</code></p>
<dd>runs frysk&#8217;s entire JUnit testsuite, or just the specified <i>test-class</i>s. </p>
<p> Frysk&#8217;s JUnit testsuite, in addition to testing frysk&#8217;s internals, tests the stability of the underlying kernel. </p>
<p> -r <i>repeat-count</i></p>
<dl>
<dd>Run the JUnit tests <i>repeat-count</i> times.</dl>
<p> &#8211;console <i>CONSOLE_LOG=LEVEL</i></p>
<dl>
<dd>Set the log CONSOLE_LOG to level LEVEL. Can set multiple logs. The LEVEL can be [ OFF | SEVERE | WARNING | INFO | CONFIG | FINE | FINER | FINEST | ALL]</dl>
<p> &#8211;log <i>LOG</i></p>
<dl>
<dd>Set the log LOG to level LEVEL. Can set multiple logs. The LEVEL can be [ OFF | SEVERE | WARNING | INFO | CONFIG | FINE | FINER | FINEST | ALL]</dl>
<p> &#8211;arch <i>arch</i></p>
<dl>
<dd>Specify the test cases&#8217; arch. The ARCH can be 64 or 32. If no arch is specified, arch-64 cases will be run. When the arch-32 cases are ready, all cases will be run be default.The option will take no effect in 32-bit machine.</dl>
<p> -n</p>
<dl>
<dd>No not run any tests, instead list the classes that would have been tested.</dl>
<p> &#8211;stress</p>
<dl>
<dd>Run only stress tests (by default stress tests are excluded).</dl>
<p> &#8211;all</p>
<dl>
<dd>Run all tests (by default stress tests are excluded).</dl>
<p> -e <i>test-spec</i></p>
<dl>
<dd>Specify a test to exclude. Each passed option will be interpreted as the regex specification of a test to omit This option may be used multiple times.</dl>
<p> -i <i>test-spec</i></p>
<dl>
<dd>Specify a test to include, overriding an omit specification. Each passed option will be interpreted as the regex specification of a test to include. This option may be used multiple times.</dl>
<p> -timeout <i>timeout</i></p>
<dl>
<dd>Specify the test timeout value in seconds. Default is 5.</dl>
<h3>Standard Frysk Options</h3>
<p><code>-exe</code></p>
<dl>
<dd>The full path of the executable to read.</dl>
<p> <code>-noexe</code></p>
<dl>
<dd>Do not attempt to read the corresponding executable when loading a core file.</dl>
<p> <code>-sysroot </code><i>directory</i></p>
<dl>
<dd>The system root directory under which all executables, libraries, and source are located.</dl>
<p> <code>-debug </code><i>class</i><code>=</code><i>level</i><code>&#8230;</code></p>
<dl>
<dd>Set internal debug-tracing of the specified Java <i>class</i> to <i>level</i> (level can be NONE, INFO, WARNING, FINE, and FINEST). If the <i>level</i> is absent, FINE is assumed; if the <i>class</i> is absent, the global level is set.</dl>
<h2>Example</h2>
<p>Run the <code>frysk</code> testsuite as a 32-bit process. </p>
<dl>
<dd>
<pre>/usr/lib/frysk/funit</pre>
</dl>
<p> Run the <code>frysk</code> testsuite as 64-bit process. </p>
<dl>
<dd>
<pre>/usr/lib64/frysk/funit</pre>
</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/7-frysk/">frysk</a>(7) <a href="/docs/linux/man/8-funit-child/">funit-child</a>(8) <a href="/docs/linux/man/8-funit-exec/">funit-exec</a>(8) <a href="/docs/linux/man/8-funit-exit/">funit-exit</a>(8) <a href="/docs/linux/man/8-funit-threads/">funit-threads</a>(8)</p>
<h2>Bugs</h2>
<p>Report bugs to m[blue]<code>http:/sources.redhat.com/frysk</code>m[] </p>
