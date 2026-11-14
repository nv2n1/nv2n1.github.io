---
title: "beakerlib(1)"
name: "beakerlib"
section: "1"
letter: "b"
url: "/docs/linux/man/1-beakerlib/"
description: "BeakerLib – a shell-level integration testing library"
---

<h2 class="name">NAME</h2>
<p> BeakerLib &#8211; a shell-level integration testing library </p>
<h2>DESCRIPTION</h2>
<p> BeakerLib is a shell-level integration testing library, providing convenience functions which simplify writing, running and analysis of integration and blackbox tests. </p>
<p> The essential features include:</p>
<dl>
<dt>&bull;</p>
<dd> <code>Journal</code> &#8211; uniform logging mechanism (logs &amp; results saved in flexible <font SIZE="-1">XML</font> format, easy to compare results &amp; generate reports)</p>
<dt>&bull;</p>
<dd> <code>Phases</code> &#8211; logical grouping of test actions, clear separation of setup / test / cleanup (preventing false fails)</p>
<dt>&bull;</p>
<dd> <code>Asserts</code> &#8211; common checks affecting the overall results of the individual phases (checking for exit codes, file existence &amp; content&#8230;)</p>
<dt>&bull;</p>
<dd> <code>Helpers</code> &#8211; convenience functions for common operations such as managing services, backup &amp; restore</dl>
<p> The main script sets the <tt>&quot;BEAKERLIB&quot;</tt> variable and sources other scripts where the actual functions are defined. You should source it at the beginning of your test with: </p>
<pre>
    . /usr/share/beakerlib/beakerlib.sh
</pre>
<p> See the <font SIZE="-1">EXAMPLES</font> section for quick start inspiration. </p>
<p> See the <font SIZE="-1">BKRDOC</font> section for more information about Automated documentation generator for BeakerLib tests.</p>
<h2>FUNCTIONS</h2>
<h3>Journalling</h3>
<p> <i>rlJournalStart</i> </p>
<p> Initialize the journal file. </p>
<pre>
    rlJournalStart
</pre>
<p> Run on the very beginning of your script to initialize journalling functionality. </p>
<p> <i>rlJournalEnd</i> </p>
<p> Summarize the test run and upload the journal file. </p>
<pre>
    rlJournalEnd
</pre>
<p> Run on the very end of your script to print summary of the whole test run, generate <font SIZE="-1">OUTPUTFILE</font> and include journal in Beaker logs. </p>
<p> <i>rlJournalPrint</i> </p>
<p> Print the content of the journal in pretty xml format. </p>
<pre>
    rlJournalPrint [type]
</pre>
<dl>
<dt>type</p>
<dd> Can be either &#8216;raw&#8217; or &#8216;pretty&#8217;, with the latter as a default. Raw: xml is in raw form, no indentation etc Pretty: xml is pretty printed, indented, with one record per line</dl>
<p> Example: </p>
<pre><code>
    &lt;?xml version="1.0"?&gt;
    &lt;BEAKER_TEST&gt;
      &lt;test_id&gt;debugging&lt;/test_id&gt;
      &lt;package&gt;setup&lt;/package&gt;
      &lt;pkgdetails&gt;setup-2.8.9-1.fc12.noarch&lt;/pkgdetails&gt;
      &lt;starttime&gt;2010-02-08 15:17:47&lt;/starttime&gt;
      &lt;endtime&gt;2010-02-08 15:17:47&lt;/endtime&gt;
      &lt;testname&gt;/examples/beakerlib/Sanity/simple&lt;/testname&gt;
      &lt;release&gt;Fedora release 12 (Constantine)&lt;/release&gt;
      &lt;hostname&gt;localhost&lt;/hostname&gt;
      &lt;arch&gt;i686&lt;/arch&gt;
      &lt;purpose&gt;PURPOSE of /examples/beakerlib/Sanity/simple
        Description: Minimal BeakerLib sanity test
        Author: Petr Splichal &amp;lt;psplicha [at] redhat.com&amp;gt;
        This is a minimal sanity test for BeakerLib. It contains a single
        phase with a couple of asserts. We Just check that the "setup"
        package is installed and that there is a sane /etc/passwd file.
      &lt;/purpose&gt;
      &lt;log&gt;
        &lt;phase endtime="2010-02-08 15:17:47" name="Test" result="PASS"
                score="0" starttime="2010-02-08 15:17:47" type="FAIL"&gt;
          &lt;test message="Checking for the presence of setup rpm"&gt;PASS&lt;/test&gt;
          &lt;test message="File /etc/passwd should exist"&gt;PASS&lt;/test&gt;
          &lt;test message="File '/etc/passwd' should contain 'root'"&gt;PASS&lt;/test&gt;
        &lt;/phase&gt;
      &lt;/log&gt;
    &lt;/BEAKER_TEST&gt;
</code></pre>
<p> <i>rlJournalPrintText</i> </p>
<p> Print the content of the journal in pretty text format. </p>
<pre>
    rlJournalPrintText [--full-journal]
</pre>
<dl>
<dt>&#8211;full-journal</p>
<dd> With this option, additional items like some <font SIZE="-1">HW</font> information will be printed in the journal.</dl>
<p> Example: </p>
<p>    ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::<br />
    :: [   LOG    ] :: TEST PROTOCOL<br />
    ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::<br />
    :: [   LOG    ] :: Test run ID   : debugging<br />
    :: [   LOG    ] :: Package       : debugging<br />
    :: [   LOG    ] :: Test started  : 2010-02-08 14:45:57<br />
    :: [   LOG    ] :: Test finished : 2010-02-08 14:45:58<br />
    :: [   LOG    ] :: Test name     :<br />
    :: [   LOG    ] :: Distro:       : Fedora release 12 (Constantine)<br />
    :: [   LOG    ] :: Hostname      : localhost<br />
    :: [   LOG    ] :: Architecture  : i686<br />
    ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::<br />
    :: [   LOG    ] :: Test description<br />
    ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::<br />
    PURPOSE of /examples/beakerlib/Sanity/simple<br />
    Description: Minimal BeakerLib sanity test<br />
    Author: Petr Splichal &lt;psplicha [at] redhat.com&gt;<br />
    This is a minimal sanity test for BeakerLib. It contains a single<br />
    phase with a couple of asserts. We Just check that the &#8220;setup&#8221;<br />
    package is installed and that there is a sane /etc/passwd file.<br />
    ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::<br />
    :: [   LOG    ] :: Test<br />
    ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::<br />
    :: [   PASS   ] :: Checking for the presence of setup rpm<br />
    :: [   PASS   ] :: File /etc/passwd should exist<br />
    :: [   PASS   ] :: File &#8216;/etc/passwd&#8217; should contain &#8216;root&#8217;<br />
    :: [   LOG    ] :: Duration: 1s<br />
    :: [   LOG    ] :: Assertions: 3 good, 0 bad<br />
    :: [   PASS   ] :: RESULT: Test</p>
<p> <i>rlGetTestState</i> </p>
<p> Returns number of failed asserts in so far, 255 if there are more then 255 failures. </p>
<pre>
    rlGetTestState
</pre>
<p> <i>rlGetPhaseState</i> </p>
<p> Returns number of failed asserts in current phase so far, 255 if there are more then 255 failures. </p>
<pre>
    rlGetPhaseState
</pre>
<h3>Logging</h3>
<p> <i>rlLog</i> </p>
<p> <i>rlLogDebug</i> </p>
<p> <i>rlLogInfo</i> </p>
<p> <i>rlLogWarning</i> </p>
<p> <i>rlLogError</i> </p>
<p> <i>rlLogFatal</i> </p>
<p> Create a time/priority-labelled message in the log. There is a bunch of aliases which can create messages formated as <font SIZE="-1">DEBUG/INFO/WARNING/ERROR</font> or <font SIZE="-1">FATAL </font>(but you would probably want to use rlDie instead of the last one). </p>
<p>rlLog message[logfile][priority][label]</p>
<dl>
<dt>message</p>
<dd> Message you want to show (use quotes when invoking).</p>
<dt>logfile</p>
<dd> Log file. If not supplied, <font SIZE="-1">OUTPUTFILE</font> is assumed.</p>
<dt>priority</p>
<dd> Priority of the log.</p>
<dt>label</p>
<dd> Print this text instead of time in log label.</dl>
<p> <i>rlDie</i> </p>
<p> Create a time-labelled message in the log, report test result, upload logs, close unfinished phase and terminate the test. </p>
<pre>
    rlDie message [file...]
</pre>
<dl>
<dt>message</p>
<dd> Message you want to show (use quotes when invoking) &#8211; this option is mandatory.</p>
<dt>file</p>
<dd> Files (logs) you want to upload as well. <tt>&quot;rlBundleLogs&quot;</tt> will be used for it. Files which are not readable will be excluded before calling <tt>&quot;rlBundleLogs&quot;</tt>, so it is safe to call even with possibly not existent logs and it will succeed.</dl>
<p> <i>rlBundleLogs</i> </p>
<p> Create a tarball of files (e.g. logs) and attach them to the test result. </p>
<pre>
    rlBundleLogs package file [file...]
</pre>
<dl>
<dt>package</p>
<dd> Name of the package. Will be used as a part of the tar-ball name.</p>
<dt>file</p>
<dd> File(s) to be packed and submitted.</dl>
<p> Returns result of submiting the tarball. </p>
<p> <i>rlFileSubmit</i> </p>
<p> Resolves absolute path to the file, replaces / for &#8211; and uploads this renamed file using rhts-submit-log. It also allows you to specify your custom name for the uploaded file. </p>
<p>rlFileSubmit[-s sep] path_to_file[required_name]</p>
<dl>
<dt>-s sep</p>
<dd> Sets separator (i.e. the replacement of the /) to sep.</p>
<dt>path_to_file</p>
<dd> Either absolute or relative path to file. Relative path is converted to absolute.</p>
<dt>required_name</p>
<dd> Default behavior renames file to full_path_to_file with / replaced for -, if this does not suit your needs, you can specify the name using this option. </p>
<p> Examples: </p>
<p> rlFileSubmit logfile.txt -&gt; logfile.txt cd /etc; rlFileSubmit ./passwd -&gt; etc-passwd rlFileSubmit /etc/passwd -&gt; etc-passwd rlFileSubmit /etc/passwd my-top-secret_file -&gt; my-top-secret-file rlFileSubmit -s &#8216;_&#8217; /etc/passwd -&gt; etc_passwd</dl>
<h3>Info</h3>
<p> <i>rlShowPackageVersion</i> </p>
<p> Shows a message about version of packages. </p>
<pre>
    rlShowPackageVersion package [package...]
</pre>
<dl>
<dt>package</p>
<dd> Name of a package(s) you want to log.</dl>
<p> <i>rlGetArch</i> </p>
<p> This function is deprecated. Use rlGetPrimaryArch or rlGetSecondaryArch instead, or use uname. This function will be only kept for compatibility. </p>
<p> Return base arch for the current system (good when you need base arch on a multilib system). </p>
<pre>
    rlGetArch
</pre>
<p> On an i686 system you will get i386, on a ppc64 you will get ppc. </p>
<p> <i>rlGetPrimaryArch</i> </p>
<p> Return primary arch for the current system (good when you need base arch on a multilib system). </p>
<pre>
    rlGetPrimaryArch
</pre>
<p> <i>rlGetSecondaryArch</i> </p>
<p> Return base arch for the current system (good when you need base arch on a multilib system). </p>
<pre>
    rlGetSecondaryArch
</pre>
<p> <i>rlGetDistroRelease</i> </p>
<p> <i>rlGetDistroVariant</i> </p>
<p> Return release or variant of the distribution on the system. </p>
<pre>
    rlGetDistroRelease
    rlGetDistroVariant
</pre>
<p> For example on the <font SIZE="-1">RHEL-4-AS</font> you will get release 4 and variant <font SIZE="-1">AS,</font> on the RHEL-5-Client you will get release 5 and variant Client. </p>
<p> <i>rlShowRunningKernel</i> </p>
<p> Log a message with version of the currently running kernel. </p>
<pre>
    rlShowRunningKernel
</pre>
<h3>Phases</h3>
<p> <i>rlPhaseStart</i> </p>
<p> Starts a phase of a specific type. The final phase result is based on all asserts included in the phase. Do not forget to end phase with <tt>&quot;rlPhaseEnd&quot;</tt> when you are done. </p>
<pre>
    rlPhaseStart type [name]
</pre>
<dl>
<dt>type</p>
<dd> Type of the phase, one of the following:</p>
<dl>
<dt>
<dd>
<dl>
<dt><font SIZE="-1">FAIL</font></p>
<dd> When assert fails here, phase will report a <font SIZE="-1">FAIL.</font></p>
<dt><font SIZE="-1">WARN</font></p>
<dd> When assert fails here, phase will report a <font SIZE="-1">WARN.</font></dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>name</p>
<dd> Optional name of the phase (if not provided, one will be generated).</dl>
<p> If all asserts included in the phase pass, phase reports <font SIZE="-1">PASS.</font> </p>
<p> <i>rlPhaseEnd</i> </p>
<p> End current phase, summarize asserts included and report phase result. </p>
<pre>
    rlPhaseEnd
</pre>
<p> Final phase result is based on included asserts and phase type. </p>
<p> <i>rlPhaseStartSetup</i> </p>
<p> <i>rlPhaseStartTest</i> </p>
<p> <i>rlPhaseStartCleanup</i> </p>
<p> Start a phase of the specified type: Setup -&gt; <font SIZE="-1">WARN,</font> Test -&gt; <font SIZE="-1">FAIL,</font> Cleanup -&gt; <font SIZE="-1">WARN.</font> </p>
<p>rlPhaseStartSetup[name] rlPhaseStartTest[name] rlPhaseStartCleanup[name]</p>
<dl>
<dt>name</p>
<dd> Optional name of the phase. If not specified, default Setup/Test/Cleanup are used.</dl>
<p> If you do not want these shortcuts, use plain <tt>&quot;rlPhaseStart&quot;</tt> function.</p>
<h3>Metric</h3>
<p> <i>rlLogMetricLow</i> </p>
<p> Log a metric, which should be as low as possible to the journal. (Example: memory consumption, run time) </p>
<pre>
    rlLogMetricLow name value [tolerance]
</pre>
<dl>
<dt>name</p>
<dd> Name of the metric. It has to be unique in a phase.</p>
<dt>value</p>
<dd> Value of the metric.</p>
<dt>tolerance</p>
<dd> It is used when comparing via rcw. It means how larger can the second value be to not trigger a <font SIZE="-1">FAIL.</font> Default is 0.2</dl>
<p> When comparing <font SIZE="-1">FIRST, SECOND,</font> then: </p>
<pre>
    FIRST &gt;= SECOND means PASS
    FIRST+FIRST*tolerance &gt;= SECOND means WARN
    FIRST+FIRST*tolerance &lt; SECOND means FAIL
</pre>
<p> <code>Example:</code> Simple benchmark is compared via this metric type in rcw. It has a tolerance of 0.2. First run had 1 second. So: </p>
<pre>
    For PASS, second run has to be better or equal to first.
            So any value of second or less is a PASS.
    For WARN, second run can be a little worse than first.
            Tolerance is 0.2, so anything lower than 1.2 means WARN.
    For FAIL, anything worse than 1.2 means FAIL.
</pre>
<p> <i>rlLogMetricHigh</i> </p>
<p> Log a metric, which should be as high as possible to the journal. (Example: number of executions per second) </p>
<pre>
    rlLogMetricHigh name value [tolerance]
</pre>
<dl>
<dt>name</p>
<dd> Name of the metric. It has to be unique in a phase.</p>
<dt>value</p>
<dd> Value of the metric.</p>
<dt>tolerance</p>
<dd> It is used when comparing via rcw. It means how lower can the second value be to not trigger a <font SIZE="-1">FAIL.</font> Default is 0.2</dl>
<p> When comparing <font SIZE="-1">FIRST, SECOND,</font> then: </p>
<pre>
    FIRST &lt;= SECOND means PASS
    FIRST+FIRST*tolerance &lt;= SECOND means WARN
    FIRST+FIRST*tolerance &gt; SECOND means FAIL
</pre>
<h3>Manual Asserts</h3>
<p> <i>rlPass</i> </p>
<p> Manual assertion, asserts and logs <font SIZE="-1">PASS.</font> </p>
<pre>
    rlPass comment
</pre>
<dl>
<dt>comment</p>
<dd> Short test summary.</dl>
<p> Returns 0 and asserts <font SIZE="-1">PASS.</font> </p>
<p> <i>rlFail</i> </p>
<p> Manual assertion, asserts and logs <font SIZE="-1">FAIL.</font> </p>
<pre>
    rlFail comment
</pre>
<dl>
<dt>comment</p>
<dd> Short test summary.</dl>
<p> Returns 1 and asserts <font SIZE="-1">FAIL.</font></p>
<h3>Arithmetic Asserts</h3>
<p> <i>rlAssert0</i> </p>
<p> Assertion checking for the equality of parameter to zero. </p>
<pre>
    rlAssert0 comment value
</pre>
<dl>
<dt>comment</p>
<dd> Short test summary, e.g. &#8220;Test if compilation ended successfully&#8221;.</p>
<dt>value</p>
<dd> Integer value (usually return code of a command).</dl>
<p> Returns 0 and asserts <font SIZE="-1">PASS</font> when <tt>&quot;value == 0&quot;</tt>. </p>
<p> <i>rlAssertEquals</i> </p>
<p> Assertion checking for the equality of two parameters. </p>
<pre>
    rlAssertEquals comment value1 value2
</pre>
<dl>
<dt>comment</p>
<dd> Short test summary, e.g. &#8220;Test if all 3 packages have been downloaded&#8221;.</p>
<dt>value1</p>
<dd> First parameter to compare, can be a number or a string</p>
<dt>value2</p>
<dd> Second parameter to compare, can be a number or a string</dl>
<p> Returns 0 and asserts <font SIZE="-1">PASS</font> when <tt>&quot;value1 == value2&quot;</tt>. </p>
<p> <i>rlAssertNotEquals</i> </p>
<p> Assertion checking for the non-equality of two parameters. </p>
<pre>
    rlAssertNotEquals comment value1 value2
</pre>
<dl>
<dt>comment</p>
<dd> Short test summary, e.g. &#8220;Test if return code is not 139&#8221;.</p>
<dt>value1</p>
<dd> First parameter to compare, can be a number or a string</p>
<dt>value2</p>
<dd> Second parameter to compare, can be a number or a string</dl>
<p> Returns 0 and asserts <font SIZE="-1">PASS</font> when <tt>&quot;value1 != value2&quot;</tt>. </p>
<p> <i>rlAssertGreater</i> </p>
<p> Assertion checking whether first parameter is greater than the second one. </p>
<pre>
    rlAssertGreater comment value1 value2
</pre>
<dl>
<dt>comment</p>
<dd> Short test summary, e.g. &#8220;Test whether there are running more instances of program.&#8221;</p>
<dt>value1</p>
<dd> Integer value.</p>
<dt>value2</p>
<dd> Integer value.</dl>
<p> Returns 0 and asserts <font SIZE="-1">PASS</font> when <tt>&quot;value1 &gt; value2&quot;</tt>. </p>
<p> <i>rlAssertGreaterOrEqual</i> </p>
<p> Assertion checking whether first parameter is greater or equal to the second one. </p>
<pre>
    rlAssertGreaterOrEqual comment value1 value2
</pre>
<dl>
<dt>comment</p>
<dd> Short test summary (e.g. &#8220;There should present at least one&#8230;&#8221;)</p>
<dt>value1</p>
<dd> Integer value.</p>
<dt>value2</p>
<dd> Integer value.</dl>
<p> Returns 0 and asserts <font SIZE="-1">PASS</font> when <tt>&quot;value1 &gt;= value2&quot;</tt>.</p>
<h3>File Asserts</h3>
<p> <i>rlAssertExists</i> </p>
<p> Assertion checking for the existence of a file or a directory. </p>
<pre>
    rlAssertExists file|directory
</pre>
<dl>
<dt>file|directory</p>
<dd> Path to the file or directory.</dl>
<p> Returns 0 and asserts <font SIZE="-1">PASS</font> when <tt>&quot;file&quot;</tt> exists. </p>
<p> <i>rlAssertNotExists</i> </p>
<p> Assertion checking for the non-existence of a file or a directory. </p>
<pre>
    rlAssertNotExists file|directory
</pre>
<dl>
<dt>file|directory</p>
<dd> Path to the file or directory.</dl>
<p> Returns 0 and asserts <font SIZE="-1">PASS</font> when <tt>&quot;file&quot;</tt> does not exist. </p>
<p> <i>rlAssertGrep</i> </p>
<p> Assertion checking if the file contains a pattern. </p>
<pre>
    rlAssertGrep pattern file [options]
</pre>
<dl>
<dt>pattern</p>
<dd> Regular expression to be searched for.</p>
<dt>file</p>
<dd> Path to the file.</p>
<dt>options</p>
<dd> Optional parameters to be passed to grep, default is <tt>&quot;-q&quot;</tt>. Can be used to perform case insensitive matches (-i), or using extended (-E) or perl (-P) regular expressions.</dl>
<p> Returns 0 and asserts <font SIZE="-1">PASS</font> when <tt>&quot;file&quot;</tt> exists and contains given <tt>&quot;pattern&quot;</tt>. </p>
<p> <i>rlAssertNotGrep</i> </p>
<p> Assertion checking that the file does not contain a pattern. </p>
<pre>
    rlAssertNotGrep pattern file [options]
</pre>
<dl>
<dt>pattern</p>
<dd> Regular expression to be searched for.</p>
<dt>file</p>
<dd> Path to the file.</p>
<dt>options</p>
<dd> Optional parameters to be passed to grep, default is <tt>&quot;-q&quot;</tt>. Can be used to perform case insensitive matches (-i), or using extended (-E) or perl (-P) regular expressions.</dl>
<p> Returns 0 and asserts <font SIZE="-1">PASS</font> when <tt>&quot;file&quot;</tt> exists and does not contain given <tt>&quot;pattern&quot;</tt>. </p>
<p> <i>rlAssertDiffer</i> </p>
<p> Assertion checking that two files differ (are not identical). </p>
<pre>
    rlAssertDiffer file1 file2
</pre>
<dl>
<dt>file1</p>
<dd> Path to first file1</p>
<dt>file2</p>
<dd> Path to second file</dl>
<p> Returns 0 and asserts <font SIZE="-1">PASS</font> when <tt>&quot;file1&quot;</tt> and <tt>&quot;file2&quot;</tt> differs. </p>
<p> <i>rlAssertNotDiffer</i> </p>
<p> Assertion checking that two files do not differ (are identical). </p>
<pre>
    rlAssertNotDiffer file1 file2
</pre>
<dl>
<dt>file1</p>
<dd> Path to first file1</p>
<dt>file2</p>
<dd> Path to second file</dl>
<p> Returns 0 and asserts <font SIZE="-1">PASS</font> when <tt>&quot;file1&quot;</tt> and <tt>&quot;file2&quot;</tt> do not differ.</p>
<h3>Run, Watch, Report</h3>
<p> <i>rlRun</i> </p>
<p> Run command with optional comment and make sure its exit code matches expectations. </p>
<p>rlRun[-t][-l][-c][-s] command[status[, status&#8230;]][comment]</p>
<dl>
<dt>-t</p>
<dd> If specified, stdout and stderr of the command output will be tagged with strigs &#8216;<font SIZE="-1">STDOUT: </font>&#8216; and &#8216;<font SIZE="-1">STDERR: </font>&#8216;.</p>
<dt>-l</p>
<dd> If specified, output of the command (tagged, if -t was specified) is logged using rlLog function. This is intended for short outputs, and therefore only last 50 lines are logged this way. Longer outputs should be analysed separately, or uploaded via rlFileSubmit or rlBundleLogs.</p>
<dt>-c</p>
<dd> Same as <tt>&quot;-l&quot;</tt>, but only log the commands output if it failed.</p>
<dt>-s</p>
<dd> Store stdout and stderr to a file (mixed together, as the user would see it on a terminal) and set <tt>$rlRun_LOG</tt> variable to name of the file. Caller is responsible for removing the file. When -t option is used, the content of the file becomes tagged too. </p>
<p> If the -s option is not used, <tt>$rlRun_LOG</tt> is not modified and keeps its content from the last &#8220;rlRun -s&#8221;.</p>
<dt>command</p>
<dd> Command to run.</p>
<dt>status</p>
<dd> Expected exit code(s). Optional, default 0. If you expect more exit codes, separate them with comma (e.g. &#8220;0,1&#8221; when both 0 and 1 are <font SIZE="-1">OK</font> and expected), or use from-to notation (i.e. &#8220;2-5&#8221; for &#8220;2,3,4,5&#8221;), or combine them (e.g. &#8220;2-4,26&#8221; for &#8220;2,3,4,26&#8221;).</p>
<dt>comment</p>
<dd> Short summary describing the action (optional, but recommended &#8211; explain what are you doing here).</dl>
<p> Returns the exit code of the command run. Asserts <font SIZE="-1">PASS</font> when command\&#8217;s exit status is in the list of expected exit codes. </p>
<p> Note:</p>
<dl>
<dt>&bull;</p>
<dd> The output of rlRun is buffered when using <tt>&quot;-t&quot;</tt>, <tt>&quot;-l&quot;</tt> or <tt>&quot;-s&quot;</tt> option (they use unix pipes, which are buffered by nature). If you need an unbuffered output just make sure that <tt>&quot;expect&quot;</tt> package is installed on your system (its &#8220;unbuffer&#8221; tool will automatically be used to produce unbuffered output).</p>
<dt>&bull;</p>
<dd> Be aware that there are some variables which can collide with your code executed within rlRun. You should avoid using __INTERNAL_rlRun_* variables.</dl>
<p> <code>Warning:</code> using <tt>&quot;unbuffer&quot;</tt> tool is now disabled because of bug 547686. </p>
<p> <i>rlWatchdog</i> </p>
<p> Run <tt>&quot;command&quot;</tt>. If it does not finish in specified time, then kill it using <tt>&quot;signal&quot;</tt>. </p>
<p>rlWatchdog command timeout[signal][callback]</p>
<dl>
<dt>command</p>
<dd> Command to run.</p>
<dt>timeout</p>
<dd> Timeout to wait, in seconds.</p>
<dt>signal</p>
<dd> Signal to use (optional, default <font SIZE="-1">KILL</font>).</p>
<dt>callback</p>
<dd> Callback function to be called before the signal is send (optional, none by default). The callback function will have one argument available &#8212; <font SIZE="-1">PGID</font> of the process group.</dl>
<p> Returns 0 if the command ends normally, without need to be killed. </p>
<p> <i>rlReport</i> </p>
<p> Report test result to the test harness. The command to be used for reporting is set by the respective plugin. You can also use the <tt>$BEAKERLIB_COMMAND_REPORT_RESULT</tt> variable to use your custom command. </p>
<p>rlReport name result[score][log]</p>
<dl>
<dt>name</p>
<dd> Name of the test result.</p>
<dt>result</p>
<dd> Result (one of <font SIZE="-1">PASS, WARN, FAIL</font>). If called with something else, will use <font SIZE="-1">WARN.</font></p>
<dt>score</p>
<dd> Test score (optional).</p>
<dt>log</p>
<dd> Optional log file to be submitted instead of default <tt>&quot;OUTPUTFILE&quot;</tt>.</dl>
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
<dt>op</p>
<dd> Operator definitng the logical expression. It can be &#8216;=&#8217;, &#8216;==&#8217;, &#8216;!=&#8217;, &#8216;&lt;&#8216;, &#8216;&lt;=&#8217;, &#8216;=&lt;&#8216;, &#8216;&gt;&#8217;, &#8216;&gt;=&#8217;, or &#8216;=&gt;&#8217;.</dl>
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
<h3>Rpm Handling</h3>
<p> <i>rlCheckRpm</i> </p>
<p> Check whether a package is installed. </p>
<p>rlCheckRpm name[version][release][arch]</p>
<dl>
<dt>name</p>
<dd> Package name like <tt>&quot;kernel&quot;</tt></p>
<dt>version</p>
<dd> Package version like <tt>2.6.25.6</tt></p>
<dt>release</p>
<dd> Package release like <tt>&quot;55.fc9&quot;</tt></p>
<dt>arch</p>
<dd> Package architucture like <tt>&quot;i386&quot;</tt></dl>
<p> Returns 0 if the specified package is installed. </p>
<p> <i>rlAssertRpm</i> </p>
<p> Assertion making sure that a package is installed. </p>
<p>rlAssertRpm name[version][release][arch] &gt;<br />
    rlAssertRpm&#8211; all</p>
<dl>
<dt>name</p>
<dd> Package name like <tt>&quot;kernel&quot;</tt></p>
<dt>version</p>
<dd> Package version like <tt>2.6.25.6</tt></p>
<dt>release</p>
<dd> Package release like <tt>&quot;55.fc9&quot;</tt></p>
<dt>arch</p>
<dd> Package architucture like <tt>&quot;i386&quot;</tt></p>
<dt>&#8211;all</p>
<dd> Assert all packages listed in the <tt>$PACKAGES</tt> <tt>$REQUIRES</tt> and <tt>$COLLECTIONS</tt> environment variables.</dl>
<p> Returns 0 and asserts <font SIZE="-1">PASS</font> if the specified package is installed. </p>
<p> <i>rlAssertNotRpm</i> </p>
<p> Assertion making sure that a package is not installed. This is just inverse of <tt>&quot;rlAssertRpm&quot;</tt>. </p>
<p>rlAssertNotRpm name[version][release][arch] &gt;</p>
<dl>
<dt>name</p>
<dd> Package name like <tt>&quot;kernel&quot;</tt></p>
<dt>version</p>
<dd> Package version like <tt>2.6.25.6</tt></p>
<dt>release</p>
<dd> Package release like <tt>&quot;55.fc9&quot;</tt></p>
<dt>arch</p>
<dd> Package architucture like <tt>&quot;i386&quot;</tt></dl>
<p> Returns 0 and asserts <font SIZE="-1">PASS</font> if the specified package is not installed. </p>
<p> <i>Example</i> </p>
<p> Function <tt>&quot;rlAssertRpm&quot;</tt> is useful especially in prepare phase where it causes abort if a package is missing, while <tt>&quot;rlCheckRpm&quot;</tt> is handy when doing something like: </p>
<pre>
    if ! rlCheckRpm package; then
         yum install package
         rlAssertRpm package
    fi
</pre>
<p> <i>rlAssertBinaryOrigin</i> </p>
<p> Assertion making sure that given binary is owned by (one of) the given package(s). </p>
<p>rlAssertBinaryOrigin binary package[package2[&#8230;]] PACKAGES = &#8230; rlAssertBinaryOrigin binary</p>
<dl>
<dt>binary</p>
<dd> Binary name like <tt>&quot;ksh&quot;</tt> or <tt>&quot;/bin/ksh&quot;</tt></p>
<dt>package</p>
<dd> List of packages like <tt>&quot;ksh mksh&quot;</tt>. The parameter is optional. If missing, contents of environment variable <tt>$PACKAGES</tt> are taken into account.</dl>
<p> Returns 0 and asserts <font SIZE="-1">PASS</font> if the specified binary belongs to (one of) the given package(s). Returns 1 and asserts <font SIZE="-1">FAIL</font> if the specified binary does not belong to (any of) the given package(s). Returns 2 and asserts <font SIZE="-1">FAIL</font> if the specified binary is not found. Returns 3 and asserts <font SIZE="-1">FAIL</font> if no packages are given. Returns 100 and asserts <font SIZE="-1">FAIL</font> if invoked with no parameters. </p>
<p> <i>Example</i> </p>
<p> Function <tt>&quot;rlAssertBinaryOrigin&quot;</tt> is useful especially in prepare phase where it causes abort if a binary is missing or is owned by different package: </p>
<pre>
    PACKAGES=mksh rlAssertBinaryOrigin ksh
    or
    rlAssertBinaryOrigin ksh mksh
</pre>
<p> Returns true if ksh is owned by the mksh package (in this case: /bin/ksh is a symlink pointing to /bin/mksh). </p>
<p> <i>rlGetMakefileRequires</i> </p>
<p> Prints comma separated list of requirements defined in Makefile using &#8216;Requires&#8217; attribute. </p>
<p> Return 0 if success. </p>
<p> <i>rlCheckRequirements</i> </p>
<p> Check that all given requirements are covered eigther by installed package or by binary available in PATHs or by some package&#8217;s provides. </p>
<pre>
    rlRun &quot;rlCheckRequirements REQ...&quot;
</pre>
<dl>
<dt><font SIZE="-1">REQ</font></p>
<dd> Requirement to be checked. It can be package name, provides string or binary name.</dl>
<p> Returns number of unsatisfied requirements. </p>
<p> <i>rlCheckMakefileRequires</i> </p>
<p> This is just a bit smarted wrapper of </p>
<p> <tt>&quot;rlCheckRequirements $(rlGetMakefileRequires)&quot;</tt> </p>
<p> <i>Example</i> </p>
<pre>
    rlRun &quot;rlCheckMakefileRequires&quot;
</pre>
<p> Return 255 if requirements could not be retrieved, 0 if all requirements are satisfied or number of unsatisfied requirements.</p>
<h3>Mounting</h3>
<p> <i>rlMount</i> </p>
<p> Create mount point (if neccessary) and mount a <font SIZE="-1">NFS</font> share. </p>
<pre>
    rlMount [-o MOUNT_OPTS] server share mountpoint
</pre>
<dl>
<dt>server</p>
<dd> <font SIZE="-1">NFS</font> server hostname.</p>
<dt>share</p>
<dd> Shared directory name.</p>
<dt>mountpoint</p>
<dd> Local mount point.</p>
<dt><font SIZE="-1">MOUNT_OPTS</font></p>
<dd> Mount options.</dl>
<p> Returns 0 if mounting the share was successful. </p>
<p> <i>rlCheckMount</i> </p>
<p> Check either if a directory is a mountpoint, if it is a mountpoint to a specific server, or if it is a mountpoint to a specific export on a specific server and if it uses specific mount options. </p>
<p>rlCheckMount[-o MOUNT_OPTS] mountpoint<br />
    rlCheckMount[-o MOUNT_OPTS] server mountpoint<br />
        rlCheckMount[-o MOUNT_OPTS] server share mountpoint</p>
<dl>
<dt>mountpoint</p>
<dd> Local mount point.</p>
<dt>server</p>
<dd> <font SIZE="-1">NFS</font> server hostname</p>
<dt>share</p>
<dd> Shared directory name</p>
<dt><font SIZE="-1">MOUNT_OPTS</font></p>
<dd> Mount options to check (comma separated list)</dl>
<p> With one parameter, returns 0 when specified directory exists and is a mountpoint. With two parameters, returns 0 when specific directory exists, is a mountpoint and an export from specific server is mounted there. With three parameters, returns 0 if a specific shared directory is mounted on a given server on a given mountpoint </p>
<p> If the -o option is provided, returns 0 if the mountpoint uses all the given options, 2 otherwise. </p>
<p> <i>rlAssertMount</i> </p>
<p> Assertion making sure that given directory is a mount point, if it is a mountpoint to a specific server, or if it is a mountpoint to a specific export on a specific server and if it uses specific mount options. </p>
<p>rlAssertMount[-o MOUNT_OPTS] mountpoint<br />
    rlAssertMount[-o MOUNT_OPTS] server mountpoint<br />
        rlAssertMount[-o MOUNT_OPTS] server share mountpoint</p>
<dl>
<dt>mountpoint</p>
<dd> Local mount point.</p>
<dt>server</p>
<dd> <font SIZE="-1">NFS</font> server hostname</p>
<dt>share</p>
<dd> Shared directory name</p>
<dt><font SIZE="-1">MOUNT_OPTS</font></p>
<dd> Mount options to check (comma separated list)</dl>
<p> With one parameter, returns 0 when specified directory exists and is a mountpoint. With two parameters, returns 0 when specific directory exists, is a mountpoint and an export from specific server is mounted there. With three parameters, returns 0 if a specific shared directory is mounted on a given server on a given mountpoint. Asserts <font SIZE="-1">PASS</font> when the condition is true. </p>
<p> If the -o option is provided, asserts <font SIZE="-1">PASS</font> if the above conditions are met and the mountpoint uses all the given options. </p>
<p> <i>rlHash, rlUnhash</i> </p>
<p> Hashes/Unhashes given string. </p>
<p>rlHash[&#8211;decode][&#8211;algorithm HASH_ALG]&#8211; stdin | STRING rlUnhash[&#8211;algorithm HASH_ALG]&#8211; stdin | STRING</p>
<dl>
<dt>&#8211;decode</p>
<dd> Unhash given string.</p>
<dt>&#8211;algorithm</p>
<dd> Use given hash algorithm. Currently supported algorithms:<br />
&nbsp;<wbr>&nbsp;<wbr>base64<br />
&nbsp;<wbr>&nbsp;<wbr>base64_&nbsp;<wbr>&#8211; this is standard base64 where&nbsp;<wbr>&#8216;=&#8217;&nbsp;<wbr>is replaced by&nbsp;<wbr>&#8216;_&#8217;<br />
&nbsp;<wbr>&nbsp;<wbr>hex </p>
<p> Defaults to hex. Default algorithm can be override using global variable rlHashAlgorithm.</p>
<dt>&#8211;stdin</p>
<dd> Get the string from stdin.</p>
<dt><font SIZE="-1">STRING</font></p>
<dd> String to be hashed/unhashed.</dl>
<p> Returns 0 if success. </p>
<p> Example with &#8211;clean: </p>
<pre>
    hash=rlHash &quot;text&quot;
</pre>
<h3>Backup and Restore</h3>
<p> <i>rlFileBackup</i> </p>
<p> Create a backup of files or directories (recursive). Can be used multiple times to add more files to backup. Backing up an already backed up file overwrites the original backup. </p>
<p>rlFileBackup[&#8211;clean][&#8211;namespace name][&#8211;missing &#8211; ok | &#8211;no &#8211; missing &#8211; ok] file[file&#8230;]</p>
<p> You can use <tt>&quot;rlRun&quot;</tt> for asserting the result but keep in mind meaning of exit codes, especialy exit code 8, if using without &#8211;clean option.</p>
<dl>
<dt>&#8211;clean</p>
<dd> If this option is provided (have to be first option of the command), then file/dir backuped using this command (provided in next options) will be (recursively) removed before we will restore it. This option implies &#8211;missing-ok, this can be overridden by &#8211;no-missing-ok.</p>
<dt>&#8211;namespace name</p>
<dd> Specifies the namespace to use. Namespaces can be used to separate backups and their restoration.</p>
<dt>&#8211;missing-ok</p>
<dd> Do not raise an error in case of missing file to backup.</p>
<dt>&#8211;no-missing-ok</p>
<dd> Do raise an error in case of missing file to backup. This is useful with &#8211;clean. This behaviour can be globally set by global variable BEAKERLIB_FILEBACKUP_MISSING_OK=false.</p>
<dt>file</p>
<dd> Files and/or directories to be backed up.</dl>
<p> Returns 0 if the backup was successful. Returns 1 if parsing of parameters was not successful. Returns 2 if no files specification was provided. Returns 3 if <font SIZE="-1">BEAKERLIB_DIR</font> variable is not set, e.g. rlJournalStart was not executed. Returns 4 if creating of main backup destination directories was not successful. Returns 5 if creating of file specific backup destination directories was not successful. Returns 6 if the copy of backed up files was not successful. Returns 7 if attributes of backedup files were not successfuly copied. Returns 8 if backed up files does not exist. This can be suppressed based on other options. </p>
<p> Example with &#8211;clean: </p>
<pre>
    touch cleandir/aaa
    rlRun &quot;rlFileBackup --clean cleandir/&quot;
    touch cleandir/bbb
    ls cleandir/
    aaa   bbb
    rlRun &quot;rlFileRestore&quot;
    ls cleandir/
    aaa
</pre>
<p> <i>rlFileRestore</i> </p>
<p> Restore backed up files to their original location. <tt>&quot;rlFileRestore&quot;</tt> does not remove new files appearing after backup has been made. If you don&#8217;t want to leave anything behind just remove the whole original tree before running <tt>&quot;rlFileRestore&quot;</tt>, or see <tt>&quot;--clean&quot;</tt> option of <tt>&quot;rlFileBackup&quot;</tt>. </p>
<pre>
    rlFileRestore [--namespace name]
</pre>
<p> You can use <tt>&quot;rlRun&quot;</tt> for asserting the result.</p>
<dl>
<dt>&#8211;namespace name</p>
<dd> Specifies the namespace to use. Namespaces can be used to separate backups and their restoration.</dl>
<p> Returns 0 if backup dir is found and files are restored successfully. </p>
<p> Return code bits meaning <font SIZE="-1">XXXXX<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></font>&nbsp;<wbr>|||||<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>||||\_&nbsp;<wbr>error parsing parameters<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|||\__&nbsp;<wbr>could not find backup directory<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>||\___&nbsp;<wbr>files cleanup failed<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>|\____&nbsp;<wbr>files restore failed<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>\_____&nbsp;<wbr>no files were restored nor cleaned</p>
<h3>Services</h3>
<p> Following routines implement comfortable way how to start/stop system services with the possibility to restore them to their original state after testing. </p>
<p> <i>rlServiceStart</i> </p>
<p> Make sure the given <tt>&quot;service&quot;</tt> is running with fresh configuration. (Start it if it is stopped and restart if it is already running.) In addition, when called for the first time, the current state is saved so that the <tt>&quot;service&quot;</tt> can be restored to its original state when testing is finished, see <tt>&quot;rlServiceRestore&quot;</tt>. </p>
<pre>
    rlServiceStart service [service...]
</pre>
<dl>
<dt>service</p>
<dd> Name of the service(s) to start.</dl>
<p> Returns number of services which failed to start/restart; thus zero is returned when everything is <font SIZE="-1">OK.</font> </p>
<p> <i>rlServiceStop</i> </p>
<p> Make sure the given <tt>&quot;service&quot;</tt> is stopped. Stop it if it is running and do nothing when it is already stopped. In addition, when called for the first time, the current state is saved so that the <tt>&quot;service&quot;</tt> can be restored to its original state when testing is finished, see <tt>&quot;rlServiceRestore&quot;</tt>. </p>
<pre>
    rlServiceStop service [service...]
</pre>
<dl>
<dt>service</p>
<dd> Name of the service(s) to stop.</dl>
<p> Returns number of services which failed to become stopped; thus zero is returned when everything is <font SIZE="-1">OK.</font> </p>
<p> <i>rlServiceRestore</i> </p>
<p> Restore given <tt>&quot;service&quot;</tt> into its original state (before the first <tt>&quot;rlServiceStart&quot;</tt> or <tt>&quot;rlServiceStop&quot;</tt> was called). </p>
<pre>
    rlServiceRestore [service...]
</pre>
<dl>
<dt>service</p>
<dd> Name of the service(s) to restore to original state. All services will be restored in reverse order if no service name is given.</dl>
<p> Returns number of services which failed to get back to their original state; thus zero is returned when everything is <font SIZE="-1">OK.</font> </p>
<p> <i>rlServiceEnable</i> </p>
<p> Enables selected services if needed, or does nothing if already enabled. In addition, when called for the first time, the current state is saved so that the <tt>&quot;service&quot;</tt> can be restored to its original state when testing is finished, see <tt>&quot;rlServiceRestore&quot;</tt>. </p>
<pre>
    rlServiceEnable service [service...]
</pre>
<dl>
<dt>service</p>
<dd> Name of the service(s) to enable.</dl>
<p> Returns number of services which failed enablement; thus zero is returned when everything is <font SIZE="-1">OK.</font> </p>
<p> <i>rlServiceDisable</i> </p>
<p> Disables selected services if needed, or does nothing if already disabled. In addition, when called for the first time, the current state is saved so that the <tt>&quot;service&quot;</tt> can be restored to its original state when testing is finished, see <tt>&quot;rlServiceRestore&quot;</tt>. </p>
<pre>
    rlServiceDisable service [service...]
</pre>
<dl>
<dt>service</p>
<dd> Name of the service(s) to disable.</dl>
<p> Returns number of services which failed disablement; thus zero is returned when everything is <font SIZE="-1">OK.</font></p>
<h3>Sockets</h3>
<p> Following routines implement comfortable way how to start/stop system sockets with the possibility to restore them to their original state after testing. </p>
<p> <i>rlSocketStart</i> </p>
<p> Make sure the given <tt>&quot;socket&quot;</tt> is running. (Start it if stopped, leave it if already running.) In addition, when called for the first time, the current state is saved so that the <tt>&quot;socket&quot;</tt> can be restored to its original state when testing is finished, see <tt>&quot;rlSocketRestore&quot;</tt>. </p>
<pre>
    rlSocketStart socket [socket...]
</pre>
<dl>
<dt>socket</p>
<dd> Name of the socket(s) to start.</dl>
<p> Returns number of sockets which failed to start/restart; thus zero is returned when everything is <font SIZE="-1">OK.</font> </p>
<p> <i>rlSocketStop</i> </p>
<p> Make sure the given <tt>&quot;socket&quot;</tt> is stopped. Stop it if it is running and do nothing when it is already stopped. In addition, when called for the first time, the current state is saved so that the <tt>&quot;socket&quot;</tt> can be restored to its original state when testing is finished, see <tt>&quot;rlSocketRestore&quot;</tt>. </p>
<pre>
    rlSocketStop socket [socket...]
</pre>
<dl>
<dt>socket</p>
<dd> Name of the socket(s) to stop.</dl>
<p> Returns number of sockets which failed to become stopped; thus zero is returned when everything is <font SIZE="-1">OK.</font> </p>
<p> <i>rlSocketRestore</i> </p>
<p> Restore given <tt>&quot;socket&quot;</tt> into its original state (before the first <tt>&quot;rlSocketStart&quot;</tt> or <tt>&quot;rlSocketStop&quot;</tt> was called). </p>
<p> Warning !!! Xinetd process [even though it might have been used] is <font SIZE="-1">NOT</font> restored. It is recommended to call rlServiceRestore xinetd as well. </p>
<pre>
    rlSocketRestore socket [socket...]
</pre>
<dl>
<dt>socket</p>
<dd> Name of the socket(s) to restore to original state.</dl>
<p> Returns number of sockets which failed to get back to their original state; thus zero is returned when everything is <font SIZE="-1">OK.</font></p>
<h3>Cleanup management</h3>
<p> Cleanup management works with a so-called cleanup buffer, which is a temporary representation of what should be run at cleanup time, and a final cleanup script (executable), which is generated from this buffer and wraps it using BeakerLib essentials (journal initialization, cleanup phase, &#8230;). The cleanup script must always be updated on an atomic basis (filesystem-wise) to allow an asynchronous execution by a third party (ie. test watcher). </p>
<p> The test watcher usage is mandatory for the cleanup management system to work properly as it is the test watcher that executes the actual cleanup script. Limited, catastrophe-avoiding mechanism is in place even when the test is not run in test watcher, but that should be seen as a backup and such situation is to be avoided whenever possible. </p>
<p> The cleanup script shares all environment (variables, exported or not, and functions) with the test itself &#8211; the cleanup append/prepend functions &#8220;sample&#8221; or &#8220;snapshot&#8221; the environment at the time of their call, <font SIZE="-1">IOW</font> any changes to the test environment are synchronized to the cleanup script only upon calling append/prepend. When the append/prepend functions are called within a function which has local variables, these will appear as global in the cleanup. </p>
<p> While the cleanup script receives <tt>$PWD</tt> from the test, its working dir is set to the initial test execution dir even if <tt>$PWD</tt> contains something else. It is impossible to use relative paths inside cleanup reliably &#8211; certain parts of the cleanup might have been added under different current directories (CWDs). Therefore always use absolute paths in append/prepend cleanup or make sure you never &#8216;cd&#8217; elsewhere (ie. to a TmpDir). </p>
<p> <i>rlCleanupAppend</i> </p>
<p> Appends a string to the cleanup buffer and recreates the cleanup script. </p>
<pre>
    rlCleanupAppend string
</pre>
<p> Returns 0 if the operation was successful, 1 otherwise. </p>
<p> <i>rlCleanupPrepend</i> </p>
<p> Prepends a string to the cleanup buffer and recreates the cleanup script. </p>
<pre>
    rlCleanupPrepend string
</pre>
<p> Returns 0 if the operation was successful, 1 otherwise.</p>
<h3>Time Performance</h3>
<p> <i>rlPerfTime_RunsInTime</i> </p>
<p> Measures, how many runs of some commands can be done in specified time. This approach is suitable for short-time running tasks (up to few seconds), where averaging few runs is not precise. This is done several times, and the final result is the average of all runs. It prints the number on stdout, so it has to be captured. </p>
<p>rlPerfTime_RunsInTime command[time][runs]</p>
<dl>
<dt>command</p>
<dd> Command to run.</p>
<dt>time</p>
<dd> Time in seconds (optional, default=30).</p>
<dt>runs</p>
<dd> Number of averaged runs (optional, default=3).</dl>
<p> <i>rlPerfTime_AvgFromRuns</i> </p>
<p> Measures the average time of running some task. This approach is suitable for long-time running tasks (tens of seconds and more), where it is precise enough. Measured runs can be preceded by dry run, which is not measured and it&#8217;s purpose is to warm up various caches. It prints the number on stdout, so it has to be captured. Or, result is then stored in special rl_retval variable. </p>
<p>rlPerfTime_AvgFromRuns command[count][warmup]</p>
<dl>
<dt>command</p>
<dd> Command to run.</p>
<dt>count</p>
<dd> Times to run (optional, default=3).</p>
<dt>warmup</p>
<dd> Warm-up run, run if this option is not &#8220;warmup&#8221; (optional, default=&#8220;warmup&#8221;)</dl>
<h3>Analyze</h3>
<p> <i>rlDejaSum</i> </p>
<p> <font SIZE="-1">TODO</font> description </p>
<pre>
    rlDejaSum par1 par2
</pre>
<dl>
<dt>par1</p>
<dd> <font SIZE="-1">TODO</font> description</p>
<dt>par2</p>
<dd> <font SIZE="-1">TODO</font> description</dl>
<p> Return 0 if&#8230; <font SIZE="-1">TODO</font> </p>
<p> <i>rlImport</i> </p>
<p> Imports code provided by one or more libraries into the test namespace. The library search mechanism is based on Beaker test hierarchy system, i.e.: </p>
<p> /component/type/test-name/test-file </p>
<p> When test-file calls rlImport with &#8216;foo/bar&#8217; parameter, the directory path is traversed upwards, and a check for presence of the test /foo/Library/bar/ will be performed. This means this function needs to be called from the test hierarchy, not e.g. the /tmp directory. </p>
<p> Once library is found, it is sourced and a verifier function is called. The verifier function is cunstructed by composing the library prefix and LibraryLoaded. Library prefix can be defined in the library itself. If the verifier passes the library is ready to use. Also variable <code>&lt;</code><font SIZE="-1"><code>PREFIX</code></font><code>&gt;LibraryDir</code> is created and it points to the library folder. </p>
<p> Usage: </p>
<pre>
    rlImport --all
    rlImport LIBRARY [LIBRARY2...]
</pre>
<dl>
<dt>&#8211;all</p>
<dd> Read Makefile in current/original directory, pick library requirements up and import them all.</p>
<dt><font SIZE="-1">LIBRARY</font></p>
<dd> Must have &#8216;component/library&#8217; format. Identifies the library to import.</dl>
<p> Returns 0 if the import of all libraries was successful. Returns non-zero if one or more library failed to import.</p>
<h3>Process Synchronisation</h3>
<p> <i>rlWaitForCmd</i> </p>
<p> Pauses script execution until command exit status is the expeced value. Logs a <font SIZE="-1">WARNING</font> and returns 1 if the command didn&#8217;t exit successfully before timeout elapsed or a maximum number of invocations has been reached. </p>
<p>rlWaitForCmd command[-p PID][-t time][-m count][-d delay][-r retval]</p>
<dl>
<dt>command</p>
<dd> Command that will be executed until its return code is equal 0 or value speciefied as option to `-r&#8217;.</p>
<dt>-t time</p>
<dd> Timeout in seconds, default=120. If the command doesn&#8217;t return 0 before time elapses, the command will be killed.</p>
<dt>-p <font SIZE="-1">PID</font></p>
<dd> <font SIZE="-1">PID</font> of the process to check before running command. If the process exits before the socket is opened, the command will log a <font SIZE="-1">WARNING.</font></p>
<dt>-m count</p>
<dd> Maximum number of `command&#8217; executions before continuing anyway. Default is infite. Returns 1 if the maximum was reached.</p>
<dt>-d delay</p>
<dd> Delay between `command&#8217; invocations. Default 1.</p>
<dt>-r retval</p>
<dd> Expected return value of command. Default 0.</dl>
<p> <i>rlWaitForFile</i> </p>
<p> Pauses script execution until specified file or directory starts existing. Returns 0 if file started existing, 1 if timeout was reached or <font SIZE="-1">PID</font> exited. Return code is greater than 1 in case of error. </p>
<p>rlWaitForFile path[-p PID][-t time][-d delay]</p>
<dl>
<dt>path</p>
<dd> Path to file that should start existing.</p>
<dt>-t time</p>
<dd> Timeout in seconds (optional, default=120). If the file isn&#8217;t opened before the time elapses the command returns 1.</p>
<dt>-p <font SIZE="-1">PID</font></p>
<dd> <font SIZE="-1">PID</font> of the process that should also be running. If the process exits before the file is created, the command returns with status code of 1.</p>
<dt>-d delay</p>
<dd> Delay between subsequent checks for existence of file. Default 1.</dl>
<p> <i>rlWaitForSocket</i> </p>
<p> Pauses script execution until socket starts listening. Returns 0 if socket started listening, 1 if timeout was reached or <font SIZE="-1">PID</font> exited. Return code is greater than 1 in case of error. </p>
<p>rlWaitForSocket{port | path}[-p PID][-t time][-d delay][&#8211;close]</p>
<dl>
<dt>port|path</p>
<dd> Network port to wait for opening or a path to <font SIZE="-1">UNIX</font> socket. Regular expressions are also supported.</p>
<dt>-t time</p>
<dd> Timeout in seconds (optional, default=120). If the socket isn&#8217;t opened before the time elapses the command returns 1.</p>
<dt>-p <font SIZE="-1">PID</font></p>
<dd> <font SIZE="-1">PID</font> of the process that should also be running. If the process exits before the socket is opened, the command returns with status code of 1.</p>
<dt>-d delay</p>
<dd> Delay between subsequent checks for availability of socket. Default 1.</p>
<dt>&#8211;close</p>
<dd> Wait for the socket to stop listening.</dl>
<p> <i>rlWait</i> </p>
<p> Wrapper around bash builtin `wait&#8217; command. See <i><a href="/docs/linux/man/1-bash_builtins/">bash_builtins</a></i>(1) man page. Kills the process and all its children if the timeout elapses. </p>
<p>rlWaitFor[n&#8230;][-s SIGNAL][-t time]</p>
<dl>
<dt>n</p>
<dd> List of PIDs to wait for. They need to be background tasks of current shell. See <i><a href="/docs/linux/man/1-bash_builtins/">bash_builtins</a></i>(1) section for `wait&#8217; command/</p>
<dt>-t time</p>
<dd> Timeout in seconds (optional, default=30). If the wait isn&#8217;t successful before the time elapses then all specified tasks are killed.</p>
<dt>-s <font SIZE="-1">SIGNAL</font></p>
<dd> Signal used to kill the process, optional <font SIZE="-1">SIGTERM</font> by default.</dl>
<h3>Virtual X Server</h3>
<p> Functions providing simple way how to start and stop virtual X server. </p>
<p> <i>rlVirtualXStart</i> </p>
<p> Start a virtual X server on a first free display. Tries only first N displays, so you can run out of them. </p>
<pre>
    rlVirtualXStart name
</pre>
<dl>
<dt>name</p>
<dd> String identifying the X server.</dl>
<p> Returns 0 when the server is started successfully. </p>
<p> <i>rlVirtualXGetDisplay</i> </p>
<p> Get the <font SIZE="-1">DISPLAY</font> variable for specified virtual X server. </p>
<pre>
    rlVirtualXGetDisplay name
</pre>
<dl>
<dt>name</p>
<dd> String identifying the X server.</dl>
<p> Displays the number of display where specified virtual X server is running to standard output. Returns 0 on success. </p>
<p> <i>rlVirtualXStop</i> </p>
<p> Kill the specified X server. </p>
<pre>
    rlVirtualXStop name
</pre>
<dl>
<dt>name</p>
<dd> String identifying the X server.</dl>
<p> Returns 0 when the server is stopped successfully. </p>
<p> <i>Example</i> </p>
<p> Below is a simple example of usage. Note that a lot of usefull debugging information is reported on the <font SIZE="-1">DEBUG</font> level, so you can run your test with <tt>&quot;DEBUG=1 make run&quot;</tt> to get them. </p>
<pre>
    rlVirtualXStart $TEST
    rlAssert0 &quot;Virtual X server started&quot; $?
    export DISPLAY=&quot;$( rlVirtualXGetDisplay $TEST )&quot;
    # ...your test which needs X...
    rlVirtualXStop $TEST
    rlAssert0 &quot;Virtual X server killed&quot; $?
</pre>
<p> These are &#8220;Requires&#8221; lines for your scripts &#8211; note different package names for different <font SIZE="-1">RHEL</font> versions: </p>
<pre>
    @echo &quot;Requires: xorg-x11-server-Xvfb&quot; &gt;&gt; $(METADATA) # RHEL-5
    @echo &quot;Requires: xorg-x11-Xvfb&quot;        &gt;&gt; $(METADATA) # RHEL-4
    @echo &quot;Requires: XFree86-Xvfb&quot;         &gt;&gt; $(METADATA) # RHEL-3
</pre>
<h2>EXAMPLES</h2>
<h3>Simple</h3>
<p> A minimal BeakerLib test can look like this: </p>
<pre>
    . /usr/share/beakerlib/beakerlib.sh
    rlJournalStart
        rlPhaseStartTest
            rlAssertRpm &quot;setup&quot;
            rlAssertExists &quot;/etc/passwd&quot;
            rlAssertGrep &quot;root&quot; &quot;/etc/passwd&quot;
        rlPhaseEnd
    rlJournalEnd
</pre>
<h3>Phases</h3>
<p> Here comes a bit more interesting example of a test which sets all the recommended variables and makes use of the phases: </p>
<pre>
    # Include the BeakerLib environment
    . /usr/share/beakerlib/beakerlib.sh
    # Set the full test name
    TEST=&quot;/examples/beakerlib/Sanity/phases&quot;
    # Package being tested
    PACKAGE=&quot;coreutils&quot;
    rlJournalStart
        # Setup phase: Prepare test directory
        rlPhaseStartSetup
            rlAssertRpm $PACKAGE
            rlRun 'TmpDir=$(mktemp -d)' 0 'Creating tmp directory' # no-reboot
            rlRun &quot;pushd $TmpDir&quot;
        rlPhaseEnd
        # Test phase: Testing touch, ls and rm commands
        rlPhaseStartTest
            rlRun &quot;touch foo&quot; 0 &quot;Creating the foo test file&quot;
            rlAssertExists &quot;foo&quot;
            rlRun &quot;ls -l foo&quot; 0 &quot;Listing the foo test file&quot;
            rlRun &quot;rm foo&quot; 0 &quot;Removing the foo test file&quot;
            rlAssertNotExists &quot;foo&quot;
            rlRun &quot;ls -l foo&quot; 2 &quot;Listing foo should now report an error&quot;
        rlPhaseEnd
        # Cleanup phase: Remove test directory
        rlPhaseStartCleanup
            rlRun &quot;popd&quot;
            rlRun &quot;rm -r $TmpDir&quot; 0 &quot;Removing tmp directory&quot;
        rlPhaseEnd
    rlJournalEnd
    # Print the test report
    rlJournalPrintText
</pre>
<p> The ouput of the rlJournalPrintText command would produce an output similar to the following: </p>
<p>    ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::<br />
    :: [   LOG    ] :: TEST PROTOCOL<br />
    ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::<br />
    :: [   LOG    ] :: Test run ID   : debugging<br />
    :: [   LOG    ] :: Package       : coreutils<br />
    :: [   LOG    ] :: Installed:    : coreutils-7.6-9.fc12.i686<br />
    :: [   LOG    ] :: Test started  : 2010-02-08 14:55:44<br />
    :: [   LOG    ] :: Test finished : 2010-02-08 14:55:50<br />
    :: [   LOG    ] :: Test name     : /examples/beakerlib/Sanity/phases<br />
    :: [   LOG    ] :: Distro:       : Fedora release 12 (Constantine)<br />
    :: [   LOG    ] :: Hostname      : localhost<br />
    :: [   LOG    ] :: Architecture  : i686<br />
    ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::<br />
    :: [   LOG    ] :: Test description<br />
    ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::<br />
    PURPOSE of /examples/beakerlib/Sanity/phases<br />
    Description: Testing BeakerLib phases<br />
    Author: Petr Splichal &lt;psplicha [at] redhat.com&gt;<br />
    This example shows how the phases work in the BeakerLib on a<br />
    trivial smoke test for the &#8220;touch&#8221;, &#8220;ls&#8221; and &#8220;rm&#8221; commands from<br />
    the coreutils package.<br />
    ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::<br />
    :: [   LOG    ] :: Setup<br />
    ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::<br />
    :: [   PASS   ] :: Checking for the presence of coreutils rpm<br />
    :: [   PASS   ] :: Creating tmp directory<br />
    :: [   PASS   ] :: Running &#8216;pushd /tmp/tmp.IcluQu5GVS&#8217; # no-reboot<br />
    :: [   LOG    ] :: Duration: 0s<br />
    :: [   LOG    ] :: Assertions: 3 good, 0 bad<br />
    :: [   PASS   ] :: RESULT: Setup<br />
    ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::<br />
    :: [   LOG    ] :: Test<br />
    ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::<br />
    :: [   PASS   ] :: Creating the foo test file<br />
    :: [   PASS   ] :: File foo should exist<br />
    :: [   PASS   ] :: Listing the foo test file<br />
    :: [   PASS   ] :: Removing the foo test file<br />
    :: [   PASS   ] :: File foo should not exist<br />
    :: [   PASS   ] :: Listing foo should now report an error<br />
    :: [   LOG    ] :: Duration: 1s<br />
    :: [   LOG    ] :: Assertions: 6 good, 0 bad<br />
    :: [   PASS   ] :: RESULT: Test<br />
    ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::<br />
    :: [   LOG    ] :: Cleanup<br />
    ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::<br />
    :: [   PASS   ] :: Running &#8216;popd&#8217;<br />
    :: [   PASS   ] :: Removing tmp directory<br />
    :: [   LOG    ] :: Duration: 1s<br />
    :: [   LOG    ] :: Assertions: 2 good, 0 bad<br />
    :: [   PASS   ] :: RESULT: Cleanup</p>
<p> Note that the detailed test description is read from a separate file <font SIZE="-1">PURPOSE</font> placed in the same directory as the test itself. </p>
<p> A lot of useful debugging information is reported on the <font SIZE="-1">DEBUG</font> level. You can run your test with <tt>&quot;DEBUG=1 make run&quot;</tt> to get them. </p>
<p> Verbosity of the test logging may be altered also by setting the <font SIZE="-1">LOG_LEVEL</font> variable. Possible values are &#8220;<font SIZE="-1">ERROR&#8221;, &#8220;WARNING&#8221;, &#8220;INFO&#8221;</font> and &#8220;<font SIZE="-1">DEBUG&#8221;.</font> You will see messages like the ones below. </p>
<pre><code>
::[WARNING] ::rlGetArch : Update test to use rlGetPrimaryArch / rlGetSecondaryArch ::[DEBUG] ::rlGetArch : This is architecture 'x86_64' ::[ERROR] ::this function was dropped as its development is completely moved to the beaker library ::[INFO] ::if you realy on this function and you really need to have it present in core beakerlib, file a RFE, please
</code></pre>
<p> Setting LOG_LEVEL=&#8220;<font SIZE="-1">DEBUG&#8221;</font> is equivalent to DEBUG=1.</p>
<h2>BKRDOC</h2>
<dl>
<dt>Description</p>
<dd> Bkrdoc is a documentation generator from tests written using BeakerLib library. This generator makes documentation from test code with and also without any documentation markup.</p>
<dt>What it&#8217;s good for</p>
<dd> For fast, brief and reliable documentation creation. It`s good for quick start with unknown BeakerLib test. Created documentations provides information about the documentation credibility. Also created documentations shows environmental variables and helps reader to run test script from which was documentation created.</p>
<dt>Bkrdoc project page</p>
<dd> <a rel="nofollow" href="https://github.com/rh-lab-q/bkrdoc">https://github.com/rh-lab-q/bkrdoc</a></dl>
<h2>LINKS</h2>
<dl>
<dt>Project Page</p>
<dd> <a rel="nofollow" href="https://fedorahosted.org/beakerlib/">https://fedorahosted.org/beakerlib/</a></p>
<dt>Manual</p>
<dd> <a rel="nofollow" href="https://fedorahosted.org/beakerlib/wiki/Manual">https://fedorahosted.org/beakerlib/wiki/Manual</a></p>
<dt>Reporting bugs</p>
<dd> <a rel="nofollow" href="https://bugzilla.redhat.com/enter_bug.cgi?product=Fedora">https://bugzilla.redhat.com/enter_bug.cgi?product=Fedora</a>&amp;component=beakerlib</dl>
<h2>AUTHORS</h2>
<dl>
<dt>&bull;</p>
<dd> Petr Muller &lt;pmuller [at] redhat.com&gt;</p>
<dt>&bull;</p>
<dd> Ondrej Hudlicky &lt;ohudlick [at] redhat.com&gt;</p>
<dt>&bull;</p>
<dd> Jan Hutar &lt;jhutar [at] redhat.com&gt;</p>
<dt>&bull;</p>
<dd> Petr Splichal &lt;psplicha [at] redhat.com&gt;</p>
<dt>&bull;</p>
<dd> Ales Zelinka &lt;azelinka [at] redhat.com&gt;</p>
<dt>&bull;</p>
<dd> Dalibor Pospisil &lt;dapospis [at] redhat.com&gt;</p>
<dt>&bull;</p>
<dd> Martin Kyral &lt;mkyral [at] redhat.com&gt;</p>
<dt>&bull;</p>
<dd> Jakub Prokes &lt;jprokes [at] redhat.com&gt; </p>
</dl>
<h2>Index</h2>
