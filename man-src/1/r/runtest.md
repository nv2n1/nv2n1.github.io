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
<p> <code>runtest</code> [OPTION]&#8230;</p>
<p> <i>DejaGnu</i> is a framework for testing programs using Expect. <code>runtest</code> is the driver program for <i>DejaGnu.</i> It controls what tests to run and how to run them.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;all</code></dt>
<dd> Output all test results. By default, only unexpected results are displayed.</dd>
<dt><code>&#8211;debug</code></dt>
<dd> Turn on <code>expect</code> internal debugging output. The output is logged to a file called <code>dbg.out</code>.</dd>
<dt><code>&#8211;build</code><i>&nbsp;<wbr>TRIPLET</i></dt>
<dd> The configuration TRIPLET for the build system.</dd>
<dt><code>&#8211;directory</code><i>&nbsp;<wbr>DIRECTORY</i></dt>
<dd> Run only tests in the specified DIRECTORY.</dd>
<dt><code>&#8211;help</code></dt>
<dd> Prints out a help screen and then exits.</dd>
<dt><code>&#8211;host</code><i>&nbsp;<wbr>TRIPLET</i></dt>
<dd> The configuration TRIPLET for the host system.</dd>
<dt><code>&#8211;host_board</code><i>&nbsp;<wbr>NAME</i></dt>
<dd> The host board defintion to use.</dd>
<dt><code>&#8211;ignore</code><i>&nbsp;<wbr>test1.exp test2.exp &#8230;</i></dt>
<dd> Do not run the specified tests.</dd>
<dt><code>&#8211;mail</code><i>&nbsp;<wbr>&#8216;name1 name2 &#8230;&#8217;</i></dt>
<dd> Electronic mail addresses to receive test results.</dd>
<dt><code>&#8211;name</code><i>&nbsp;<wbr>HOSTNAME</i></dt>
<dd> The network HOSTNAME of the target board.</dd>
<dt><code>&#8211;objdir</code><i>&nbsp;<wbr>PATH</i></dt>
<dd> <i>PATH</i> is a directory containing compiled test code.</dd>
<dt><code>&#8211;outdir</code><i>&nbsp;<wbr>DIRECTORY</i></dt>
<dd> The name of a DIRECTORY for test log output.</dd>
<dt><code>&#8211;reboot</code></dt>
<dd> Reboot the target board when <code>runtest</code> initializes (if supported).</dd>
<dt><code>&#8211;srcdir</code><i>&nbsp;<wbr>PATH</i></dt>
<dd> <i>PATH</i> is a directory containing test directories.</dd>
<dt><code>&#8211;status</code></dt>
<dd> Set the exit status to fail on Tcl errors.</dd>
<dt><code>&#8211;strace</code><i>&nbsp;<wbr>N</i></dt>
<dd> Turns on <code>expect</code> internal tracing to <i>N</i> levels deep. The output is logged to a file called <code>dbg.out</code>.</dd>
<dt><code>&#8211;target</code><i>&nbsp;<wbr>TRIPLET</i></dt>
<dd> The configuration TRIPLET for the target.</dd>
<dt><code>&#8211;target_board</code><i>&nbsp;<wbr>NAME</i></dt>
<dd> A list of target board NAMEs to run tests on.</dd>
<dt><code>&#8211;tool</code><i>&nbsp;<wbr>TOOLNAME</i></dt>
<dd> Specify the tool to be tested. <i>TOOLNAME</i> controls the test suite applied, and the associated initialization module.</dd>
<dt><code>&#8211;tool_exec</code><i>&nbsp;<wbr>PATH</i></dt>
<dd> Specify the PATH to the executable to test.</dd>
<dt><code>&#8211;tool_opts</code><i>&nbsp;<wbr>OPTIONS</i></dt>
<dd> Additional OPTIONS to pass to the tool.</dd>
<dt><code>&#8211;verbose, -v</code></dt>
<dd> Turns on more debugging output from test cases and DejaGnu utility code. Use more than once to increase output further.</dd>
<dt><code>&#8211;version, -V</code></dt>
<dd> Prints out the versions of DejaGnu, Expect and Tcl.</dd>
<dt><code>&#8211;xml, -x</code></dt>
<dd> Generate XML output.</dd>
<dt><code>-D[number]</code></dt>
<dd> Activate the Tcl debugger. <code>number</code> can be either 1 or 0. If it is 1, then the expect shell will break when it starts to run. The interrupt key will cause DejaGnu to drop to the debugger prompt. If it is 0, DejaGnu starts as usual, but a ^C drops to the debugger prompt.</dd>
<dt>Any file name on the command line is assumed to be a subset of the</dt>
<dd> test names to run. Usually these are the names of the test scripts (eg. foo.exp). </dd>
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
</dt><dd> <code>info dejagnu</code></dd></dl>
<p> should give you access to the complete manual. </p>
