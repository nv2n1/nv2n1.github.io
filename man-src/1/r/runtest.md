---
title: "runtest(1)"
name: "runtest"
section: "1"
letter: "r"
url: "/docs/linux/man/1-runtest/"
description: "runtest – DejaGnu test driver"
---

<h2>NAME</h2>
<p> runtest &#8211; DejaGnu test driver</p>
<h2>SYNOPSIS</h2>
<p> <code>runtest</code> [OPTION]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> <i>DejaGnu</i> is a framework for testing programs using Expect. <code>runtest</code> is the driver program for <i>DejaGnu.</i> It controls what tests to run and how to run them.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;all</code></p>
<dd> Output all test results. By default, only unexpected results are displayed.</p>
<dt><code>&#8211;debug</code></p>
<dd> Turn on <code>expect</code> internal debugging output. The output is logged to a file called <code>dbg.out</code>.</p>
<dt><code>&#8211;build</code><i>&nbsp;<wbr>TRIPLET</i></p>
<dd> The configuration TRIPLET for the build system.</p>
<dt><code>&#8211;directory</code><i>&nbsp;<wbr>DIRECTORY</i></p>
<dd> Run only tests in the specified DIRECTORY.</p>
<dt><code>&#8211;help</code></p>
<dd> Prints out a help screen and then exits.</p>
<dt><code>&#8211;host</code><i>&nbsp;<wbr>TRIPLET</i></p>
<dd> The configuration TRIPLET for the host system.</p>
<dt><code>&#8211;host_board</code><i>&nbsp;<wbr>NAME</i></p>
<dd> The host board defintion to use.</p>
<dt><code>&#8211;ignore</code><i>&nbsp;<wbr>test1.exp test2.exp &#8230;</i></p>
<dd> Do not run the specified tests.</p>
<dt><code>&#8211;mail</code><i>&nbsp;<wbr>&#8216;name1 name2 &#8230;&#8217;</i></p>
<dd> Electronic mail addresses to receive test results.</p>
<dt><code>&#8211;name</code><i>&nbsp;<wbr>HOSTNAME</i></p>
<dd> The network HOSTNAME of the target board.</p>
<dt><code>&#8211;objdir</code><i>&nbsp;<wbr>PATH</i></p>
<dd> <i>PATH</i> is a directory containing compiled test code.</p>
<dt><code>&#8211;outdir</code><i>&nbsp;<wbr>DIRECTORY</i></p>
<dd> The name of a DIRECTORY for test log output.</p>
<dt><code>&#8211;reboot</code></p>
<dd> Reboot the target board when <code>runtest</code> initializes (if supported).</p>
<dt><code>&#8211;srcdir</code><i>&nbsp;<wbr>PATH</i></p>
<dd> <i>PATH</i> is a directory containing test directories.</p>
<dt><code>&#8211;status</code></p>
<dd> Set the exit status to fail on Tcl errors.</p>
<dt><code>&#8211;strace</code><i>&nbsp;<wbr>N</i></p>
<dd> Turns on <code>expect</code> internal tracing to <i>N</i> levels deep. The output is logged to a file called <code>dbg.out</code>.</p>
<dt><code>&#8211;target</code><i>&nbsp;<wbr>TRIPLET</i></p>
<dd> The configuration TRIPLET for the target.</p>
<dt><code>&#8211;target_board</code><i>&nbsp;<wbr>NAME</i></p>
<dd> A list of target board NAMEs to run tests on.</p>
<dt><code>&#8211;tool</code><i>&nbsp;<wbr>TOOLNAME</i></p>
<dd> Specify the tool to be tested. <i>TOOLNAME</i> controls the test suite applied, and the associated initialization module.</p>
<dt><code>&#8211;tool_exec</code><i>&nbsp;<wbr>PATH</i></p>
<dd> Specify the PATH to the executable to test.</p>
<dt><code>&#8211;tool_opts</code><i>&nbsp;<wbr>OPTIONS</i></p>
<dd> Additional OPTIONS to pass to the tool.</p>
<dt><code>&#8211;verbose, -v</code></p>
<dd> Turns on more debugging output from test cases and DejaGnu utility code. Use more than once to increase output further.</p>
<dt><code>&#8211;version, -V</code></p>
<dd> Prints out the versions of DejaGnu, Expect and Tcl.</p>
<dt><code>&#8211;xml, -x</code></p>
<dd> Generate XML output.</p>
<dt><code>-D[number]</code></p>
<dd> Activate the Tcl debugger. <code>number</code> can be either 1 or 0. If it is 1, then the expect shell will break when it starts to run. The interrupt key will cause DejaGnu to drop to the debugger prompt. If it is 0, DejaGnu starts as usual, but a ^C drops to the debugger prompt.</p>
<dt>Any file name on the command line is assumed to be a subset of the</p>
<dd> test names to run. Usually these are the names of the test scripts (eg. foo.exp). </p>
<p> Makefile-style variables are used to specify tool names and their flags; these and other configuration dependent values are saved in the file <code>site.exp</code>, created during configuration.</dl>
<h2>EXIT CODES</h2>
<p> <code>runtest</code> sets the exit code to 1 if any of the tests failed, or sets it to 0 if all the tests passed.</p>
<h2>AUTHOR</h2>
<p> Rob Savoye (rob [at] welcomehome.org)</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;bug-dejagnu [at] gnu.org&gt;.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2005, 2007, 2008 Free Software Foundation, Inc.<br />
 This is free software. You may redistribute copies of it under the terms of the GNU General Public License &lt;<a rel="nofollow" href="http://www.gnu.org/licenses/gpl.html">http://www.gnu.org/licenses/gpl.html</a>&gt;. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>DejaGnu</code> is maintained as a Docbook manual. If the <code>info</code> program is properly installed at your site, the command</p>
<dl>
<dt>
<dd> <code>info dejagnu</code></dl>
<p> should give you access to the complete manual. </p>
<h2>Index</h2>
