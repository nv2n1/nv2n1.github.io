---

title: "beakerlib-testing(1)"
name: "beakerlib-testing"
section: "1"
letter: "b"
url: "/docs/linux/man/1-beakerlib-testing/"
description: "BeakerLib – testing – asserting functions, watchdog and report"
---

<p> This file contains functions related directly to testing. These functions are various asserts affecting final result of the phase. Watchdog and the report result function is included as well.</p>
<h2>FUNCTIONS</h2>
<h3>Manual Asserts</h3>
<p> <i>rlPass</i> </p>
<p> Manual assertion, asserts and logs <font SIZE="-1">PASS.</font> </p>
<pre>
    rlPass comment
</pre>
<dl>
<dt>comment</dt>
<dd> Short test summary.</dd></dl>
<p> Returns 0 and asserts <font SIZE="-1">PASS.</font> </p>
<p> <i>rlFail</i> </p>
<p> Manual assertion, asserts and logs <font SIZE="-1">FAIL.</font> </p>
<pre>
    rlFail comment
</pre>
<dl>
<dt>comment</dt>
<dd> Short test summary.</dd></dl>
<p> Returns 1 and asserts <font SIZE="-1">FAIL.</font></p>
<h3>Arithmetic Asserts</h3>
<p> <i>rlAssert0</i> </p>
<p> Assertion checking for the equality of parameter to zero. </p>
<pre>
    rlAssert0 comment value
</pre>
<dl>
<dt>comment</dt>
<dd> Short test summary, e.g. &#8220;Test if compilation ended successfully&#8221;.</dd>
<dt>value</dt>
<dd> Integer value (usually return code of a command).</dd></dl>
<p> Returns 0 and asserts <font SIZE="-1">PASS</font> when <tt>&quot;value == 0&quot;</tt>. </p>
<p> <i>rlAssertEquals</i> </p>
<p> Assertion checking for the equality of two parameters. </p>
<pre>
    rlAssertEquals comment value1 value2
</pre>
<dl>
<dt>comment</dt>
<dd> Short test summary, e.g. &#8220;Test if all 3 packages have been downloaded&#8221;.</dd>
<dt>value1</dt>
<dd> First parameter to compare, can be a number or a string</dd>
<dt>value2</dt>
<dd> Second parameter to compare, can be a number or a string</dd></dl>
<p> Returns 0 and asserts <font SIZE="-1">PASS</font> when <tt>&quot;value1 == value2&quot;</tt>. </p>
<p> <i>rlAssertNotEquals</i> </p>
<p> Assertion checking for the non-equality of two parameters. </p>
<pre>
    rlAssertNotEquals comment value1 value2
</pre>
<dl>
<dt>comment</dt>
<dd> Short test summary, e.g. &#8220;Test if return code is not 139&#8221;.</dd>
<dt>value1</dt>
<dd> First parameter to compare, can be a number or a string</dd>
<dt>value2</dt>
<dd> Second parameter to compare, can be a number or a string</dd></dl>
<p> Returns 0 and asserts <font SIZE="-1">PASS</font> when <tt>&quot;value1 != value2&quot;</tt>. </p>
<p> <i>rlAssertGreater</i> </p>
<p> Assertion checking whether first parameter is greater than the second one. </p>
<pre>
    rlAssertGreater comment value1 value2
</pre>
<dl>
<dt>comment</dt>
<dd> Short test summary, e.g. &#8220;Test whether there are running more instances of program.&#8221;</dd>
<dt>value1</dt>
<dd> Integer value.</dd>
<dt>value2</dt>
<dd> Integer value.</dd></dl>
<p> Returns 0 and asserts <font SIZE="-1">PASS</font> when <tt>&quot;value1 &gt; value2&quot;</tt>. </p>
<p> <i>rlAssertGreaterOrEqual</i> </p>
<p> Assertion checking whether first parameter is greater or equal to the second one. </p>
<pre>
    rlAssertGreaterOrEqual comment value1 value2
</pre>
<dl>
<dt>comment</dt>
<dd> Short test summary (e.g. &#8220;There should present at least one&#8230;&#8221;)</dd>
<dt>value1</dt>
<dd> Integer value.</dd>
<dt>value2</dt>
<dd> Integer value.</dd></dl>
<p> Returns 0 and asserts <font SIZE="-1">PASS</font> when <tt>&quot;value1 &gt;= value2&quot;</tt>.</p>
<h3>File Asserts</h3>
<p> <i>rlAssertExists</i> </p>
<p> Assertion checking for the existence of a file or a directory. </p>
<pre>
    rlAssertExists file|directory
</pre>
<dl>
<dt>file|directory</dt>
<dd> Path to the file or directory.</dd></dl>
<p> Returns 0 and asserts <font SIZE="-1">PASS</font> when <tt>&quot;file&quot;</tt> exists. </p>
<p> <i>rlAssertNotExists</i> </p>
<p> Assertion checking for the non-existence of a file or a directory. </p>
<pre>
    rlAssertNotExists file|directory
</pre>
<dl>
<dt>file|directory</dt>
<dd> Path to the file or directory.</dd></dl>
<p> Returns 0 and asserts <font SIZE="-1">PASS</font> when <tt>&quot;file&quot;</tt> does not exist. </p>
<p> <i>rlAssertGrep</i> </p>
<p> Assertion checking if the file contains a pattern. </p>
<pre>
    rlAssertGrep pattern file [options]
</pre>
<dl>
<dt>pattern</dt>
<dd> Regular expression to be searched for.</dd>
<dt>file</dt>
<dd> Path to the file.</dd>
<dt>options</dt>
<dd> Optional parameters to be passed to grep, default is <tt>&quot;-q&quot;</tt>. Can be used to perform case insensitive matches (-i), or using extended (-E) or perl (-P) regular expressions.</dd></dl>
<p> Returns 0 and asserts <font SIZE="-1">PASS</font> when <tt>&quot;file&quot;</tt> exists and contains given <tt>&quot;pattern&quot;</tt>. </p>
<p> <i>rlAssertNotGrep</i> </p>
<p> Assertion checking that the file does not contain a pattern. </p>
<pre>
    rlAssertNotGrep pattern file [options]
</pre>
<dl>
<dt>pattern</dt>
<dd> Regular expression to be searched for.</dd>
<dt>file</dt>
<dd> Path to the file.</dd>
<dt>options</dt>
<dd> Optional parameters to be passed to grep, default is <tt>&quot;-q&quot;</tt>. Can be used to perform case insensitive matches (-i), or using extended (-E) or perl (-P) regular expressions.</dd></dl>
<p> Returns 0 and asserts <font SIZE="-1">PASS</font> when <tt>&quot;file&quot;</tt> exists and does not contain given <tt>&quot;pattern&quot;</tt>. </p>
<p> <i>rlAssertDiffer</i> </p>
<p> Assertion checking that two files differ (are not identical). </p>
<pre>
    rlAssertDiffer file1 file2
</pre>
<dl>
<dt>file1</dt>
<dd> Path to first file1</dd>
<dt>file2</dt>
<dd> Path to second file</dd></dl>
<p> Returns 0 and asserts <font SIZE="-1">PASS</font> when <tt>&quot;file1&quot;</tt> and <tt>&quot;file2&quot;</tt> differs. </p>
<p> <i>rlAssertNotDiffer</i> </p>
<p> Assertion checking that two files do not differ (are identical). </p>
<pre>
    rlAssertNotDiffer file1 file2
</pre>
<dl>
<dt>file1</dt>
<dd> Path to first file1</dd>
<dt>file2</dt>
<dd> Path to second file</dd></dl>
<p> Returns 0 and asserts <font SIZE="-1">PASS</font> when <tt>&quot;file1&quot;</tt> and <tt>&quot;file2&quot;</tt> do not differ.</p>
<h3>Run, Watch, Report</h3>
<p> <i>rlRun</i> </p>
<p> Run command with optional comment and make sure its exit code matches expectations. </p>
<pre><code>
rlRun[-t][-l][-c][-s] command[status[, status...]][comment]
</code></pre>
<dl>
<dt>-t</dt>
<dd> If specified, stdout and stderr of the command output will be tagged with strigs &#8216;<font SIZE="-1">STDOUT: </font>&#8216; and &#8216;<font SIZE="-1">STDERR: </font>&#8216;.</dd>
<dt>-l</dt>
<dd> If specified, output of the command (tagged, if -t was specified) is logged using rlLog function. This is intended for short outputs, and therefore only last 50 lines are logged this way. Longer outputs should be analysed separately, or uploaded via rlFileSubmit or rlBundleLogs.</dd>
<dt>-c</dt>
<dd> Same as <tt>&quot;-l&quot;</tt>, but only log the commands output if it failed.</dd>
<dt>-s</dt>
<dd> Store stdout and stderr to a file (mixed together, as the user would see it on a terminal) and set <tt>$rlRun_LOG</tt> variable to name of the file. Caller is responsible for removing the file. When -t option is used, the content of the file becomes tagged too. </dd>
<p> If the -s option is not used, <tt>$rlRun_LOG</tt> is not modified and keeps its content from the last &#8220;rlRun -s&#8221;.</p>
<dt>command</dt>
<dd> Command to run.</dd>
<dt>status</dt>
<dd> Expected exit code(s). Optional, default 0. If you expect more exit codes, separate them with comma (e.g. &#8220;0,1&#8221; when both 0 and 1 are <font SIZE="-1">OK</font> and expected), or use from-to notation (i.e. &#8220;2-5&#8221; for &#8220;2,3,4,5&#8221;), or combine them (e.g. &#8220;2-4,26&#8221; for &#8220;2,3,4,26&#8221;).</dd>
<dt>comment</dt>
<dd> Short summary describing the action (optional, but recommended &#8211; explain what are you doing here).</dd></dl>
<p> Returns the exit code of the command run. Asserts <font SIZE="-1">PASS</font> when command\&#8217;s exit status is in the list of expected exit codes. </p>
<p> Note:</p>
<dl>
<dt>&bull;</dt>
<dd> The output of rlRun is buffered when using <tt>&quot;-t&quot;</tt>, <tt>&quot;-l&quot;</tt> or <tt>&quot;-s&quot;</tt> option (they use unix pipes, which are buffered by nature). If you need an unbuffered output just make sure that <tt>&quot;expect&quot;</tt> package is installed on your system (its &#8220;unbuffer&#8221; tool will automatically be used to produce unbuffered output).</dd>
<dt>&bull;</dt>
<dd> Be aware that there are some variables which can collide with your code executed within rlRun. You should avoid using __INTERNAL_rlRun_* variables.</dd></dl>
<p> <code>Warning:</code> using <tt>&quot;unbuffer&quot;</tt> tool is now disabled because of bug 547686. </p>
<p> <i>rlWatchdog</i> </p>
<p> Run <tt>&quot;command&quot;</tt>. If it does not finish in specified time, then kill it using <tt>&quot;signal&quot;</tt>. </p>
<p>rlWatchdog command timeout[signal][callback]</p>
<dl>
<dt>command</dt>
<dd> Command to run.</dd>
<dt>timeout</dt>
<dd> Timeout to wait, in seconds.</dd>
<dt>signal</dt>
<dd> Signal to use (optional, default <font SIZE="-1">KILL</font>).</dd>
<dt>callback</dt>
<dd> Callback function to be called before the signal is send (optional, none by default). The callback function will have one argument available &#8212; <font SIZE="-1">PGID</font> of the process group.</dd></dl>
<p> Returns 0 if the command ends normally, without need to be killed. </p>
<p> <i>rlReport</i> </p>
<p> Report test result to the test harness. The command to be used for reporting is set by the respective plugin. You can also use the <tt>$BEAKERLIB_COMMAND_REPORT_RESULT</tt> variable to use your custom command. </p>
<pre><code>
rlReport name result[score][log]
</code></pre>
<dl>
<dt>name</dt>
<dd> Name of the test result.</dd>
<dt>result</dt>
<dd> Result (one of <font SIZE="-1">PASS, WARN, FAIL</font>). If called with something else, will use <font SIZE="-1">WARN.</font></dd>
<dt>score</dt>
<dd> Test score (optional).</dd>
<dt>log</dt>
<dd> Optional log file to be submitted instead of default <tt>&quot;OUTPUTFILE&quot;</tt>.</dd></dl>
<p> <i>rlCmpVersion</i> </p>
<p> Compare two given versions composed by numbers and letters divided by dot (.), underscore (_), or dash (-). </p>
<pre>
    rlCmpVersion ver1 ver2
</pre>
<p> If ver1 = ver2, sign &#8216;=&#8217; is printed to stdout and 0 is returned. If ver1 &gt; ver2, sign &#8216;&gt;&#8217; is printed to stdout and 1 is returned. If ver1 &lt; ver2, sign &#8216;&lt;&#8216; is printed to stdout and 2 is returned. </p>
<p> <i>rlTestVersion</i> </p>
<p> Test releation between two given versions based on given operator. </p>
<pre>
    rlTestVersion ver1 op ver2
</pre>
<dl>
<dt>op</dt>
<dd> Operator definitng the logical expression. It can be &#8216;=&#8217;, &#8216;==&#8217;, &#8216;!=&#8217;, &#8216;&lt;&#8216;, &#8216;&lt;=&#8217;, &#8216;=&lt;&#8216;, &#8216;&gt;&#8217;, &#8216;&gt;=&#8217;, or &#8216;=&gt;&#8217;.</dd></dl>
<p> Returns 0 if the expresison ver1 op ver2 is true; 1 if the expression is false and 2 if something went wrong.</p>
<h3>Release Info</h3>
<p> <i>rlIsRHEL</i> </p>
<p> Check whether we&#8217;re running on <font SIZE="-1">RHEL.</font> With given number of version as parameter returns 0 if the particular <font SIZE="-1">RHEL</font> version is running. Multiple arguments can be passed separated with space as well as any particular release (5.1 5.2 5.3). Each version can have a prefix consisting of &#8216;&lt;&#8216;, &#8216;&lt;=&#8217;, &#8216;=&#8217;, &#8216;&gt;=&#8217;, &#8216;&gt;&#8217;, matching whenever the currently installed version is lesser, lesser or equal, equal, equal or greater, greater than the version specified as argument. Note that ie. &#8216;=5&#8217; (unlike just &#8216;5&#8217;) matches exactly 5 (5.0), not 5.N, where N &gt; 0. </p>
<pre>
    rlIsRHEL
</pre>
<p> Returns 0 if we are running on <font SIZE="-1">RHEL.</font> </p>
<pre>
    rlIsRHEL 4.8 5
</pre>
<p> Returns 0 if we are running <font SIZE="-1">RHEL 4.8</font> or any <font SIZE="-1">RHEL 5.</font> </p>
<p> <i>rlIsFedora</i> </p>
<p> Check whether we&#8217;re running on Fedora. With given number of version as parameter returns 0 if the particular Fedora version is running. Range matching can be used in the form used by rlIsRHEL. </p>
<pre>
    rlIsFedora
</pre>
<p> Returns 0 if we are running on Fedora. </p>
<pre>
    rlIsFedora 9 10
</pre>
<p> Returns 0 if we are running Fedora 9 or 10.</p>
<h3>Release Info</h3>
<p> <i>rlIsCentOS</i> </p>
<p> Check whether we&#8217;re running on CentOS. With given number of version as parameter returns 0 if the particular CentOS version is running. Multiple arguments can be passed separated with space as well as any particular release (5.1 5.2 5.3). Each version can have a prefix consisting of &#8216;&lt;&#8216;, &#8216;&lt;=&#8217;, &#8216;=&#8217;, &#8216;&gt;=&#8217;, &#8216;&gt;&#8217;, matching whenever the currently installed version is lesser, lesser or equal, equal, equal or greater, greater than the version specified as argument. Note that ie. &#8216;=5&#8217; (unlike just &#8216;5&#8217;) matches exactly 5 (5.0), not 5.N, where N &gt; 0. </p>
<pre>
    rlIsCentOS
</pre>
<p> Returns 0 if we are running on CentOS. </p>
<pre>
    rlIsCentOS 7.1 6
</pre>
<p> Returns 0 if we are running CentOS 7.1 or any CentOS 6.</p>
<h2>AUTHORS</h2>
<dl>
<dt>&bull;</dt>
<dd> Ondrej Hudlicky &lt;ohudlick [at] redhat.com&gt;</dd>
<dt>&bull;</dt>
<dd> Petr Muller &lt;pmuller [at] redhat.com&gt;</dd>
<dt>&bull;</dt>
<dd> Jan Hutar &lt;jhutar [at] redhat.com&gt;</dd>
<dt>&bull;</dt>
<dd> Petr Splichal &lt;psplicha [at] redhat.com&gt;</dd>
<dt>&bull;</dt>
<dd> Ales Zelinka &lt;azelinka [at] redhat.com&gt; </dd>
</dl>
