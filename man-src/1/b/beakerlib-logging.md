---
title: "beakerlib-logging(1)"
name: "beakerlib-logging"
section: "1"
letter: "b"
url: "/docs/linux/man/1-beakerlib-logging/"
description: "BeakerLib – logging – phase support, logging functions and metrics"
---

<h2>DESCRIPTION</h2>
<p> Routines for creating various types of logs inside BeakerLib tests. Implements also phase support with automatic assert evaluation.</p>
<h2>FUNCTIONS</h2>
<h3>Logging</h3>
<p> <i>rlLog</i> </p>
<p> <i>rlLogDebug</i> </p>
<p> <i>rlLogInfo</i> </p>
<p> <i>rlLogWarning</i> </p>
<p> <i>rlLogError</i> </p>
<p> <i>rlLogFatal</i> </p>
<p> Create a time/priority-labelled message in the log. There is a bunch of aliases which can create messages formated as <font SIZE="-1">DEBUG/INFO/WARNING/ERROR</font> or <font SIZE="-1">FATAL </font>(but you would probably want to use rlDie instead of the last one). </p>
<pre><code>
rlLog message[logfile][priority][label]
</code></pre>
<dl>
<dt>message</dt>
<dd> Message you want to show (use quotes when invoking).</dd>
<dt>logfile</dt>
<dd> Log file. If not supplied, <font SIZE="-1">OUTPUTFILE</font> is assumed.</dd>
<dt>priority</dt>
<dd> Priority of the log.</dd>
<dt>label</dt>
<dd> Print this text instead of time in log label.</dd></dl>
<p> <i>rlDie</i> </p>
<p> Create a time-labelled message in the log, report test result, upload logs, close unfinished phase and terminate the test. </p>
<pre>
    rlDie message [file...]
</pre>
<dl>
<dt>message</dt>
<dd> Message you want to show (use quotes when invoking) &#8211; this option is mandatory.</dd>
<dt>file</dt>
<dd> Files (logs) you want to upload as well. <tt>&quot;rlBundleLogs&quot;</tt> will be used for it. Files which are not readable will be excluded before calling <tt>&quot;rlBundleLogs&quot;</tt>, so it is safe to call even with possibly not existent logs and it will succeed.</dd></dl>
<p> <i>rlBundleLogs</i> </p>
<p> Create a tarball of files (e.g. logs) and attach them to the test result. </p>
<pre>
    rlBundleLogs package file [file...]
</pre>
<dl>
<dt>package</dt>
<dd> Name of the package. Will be used as a part of the tar-ball name.</dd>
<dt>file</dt>
<dd> File(s) to be packed and submitted.</dd></dl>
<p> Returns result of submiting the tarball. </p>
<p> <i>rlFileSubmit</i> </p>
<p> Resolves absolute path to the file, replaces / for &#8211; and uploads this renamed file using rhts-submit-log. It also allows you to specify your custom name for the uploaded file. </p>
<p>rlFileSubmit[-s sep] path_to_file[required_name]</p>
<dl>
<dt>-s sep</dt>
<dd> Sets separator (i.e. the replacement of the /) to sep.</dd>
<dt>path_to_file</dt>
<dd> Either absolute or relative path to file. Relative path is converted to absolute.</dd>
<dt>required_name</dt>
<dd> Default behavior renames file to full_path_to_file with / replaced for -, if this does not suit your needs, you can specify the name using this option. </dd>
<p> Examples: </p>
<p> rlFileSubmit logfile.txt -&gt; logfile.txt cd /etc; rlFileSubmit ./passwd -&gt; etc-passwd rlFileSubmit /etc/passwd -&gt; etc-passwd rlFileSubmit /etc/passwd my-top-secret_file -&gt; my-top-secret-file rlFileSubmit -s &#8216;_&#8217; /etc/passwd -&gt; etc_passwd</dl>
<h3>Info</h3>
<p> <i>rlShowPackageVersion</i> </p>
<p> Shows a message about version of packages. </p>
<pre>
    rlShowPackageVersion package [package...]
</pre>
<dl>
<dt>package</dt>
<dd> Name of a package(s) you want to log.</dd></dl>
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
<dt>type</dt>
<dd> Type of the phase, one of the following:</dd>
<dl>
<dl>
<dt><font SIZE="-1">FAIL</font></dt>
<dd> When assert fails here, phase will report a <font SIZE="-1">FAIL.</font></dd>
<dt><font SIZE="-1">WARN</font></dt>
<dd> When assert fails here, phase will report a <font SIZE="-1">WARN.</font></dd></dl>
</dl>
<dl>
</dl>
<dt>name</dt>
<dd> Optional name of the phase (if not provided, one will be generated).</dd></dl>
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
<pre><code>
rlPhaseStartSetup[name] rlPhaseStartTest[name] rlPhaseStartCleanup[name]
</code></pre>
<dl>
<dt>name</dt>
<dd> Optional name of the phase. If not specified, default Setup/Test/Cleanup are used.</dd></dl>
<p> If you do not want these shortcuts, use plain <tt>&quot;rlPhaseStart&quot;</tt> function.</p>
<h3>Metric</h3>
<p> <i>rlLogMetricLow</i> </p>
<p> Log a metric, which should be as low as possible to the journal. (Example: memory consumption, run time) </p>
<pre>
    rlLogMetricLow name value [tolerance]
</pre>
<dl>
<dt>name</dt>
<dd> Name of the metric. It has to be unique in a phase.</dd>
<dt>value</dt>
<dd> Value of the metric.</dd>
<dt>tolerance</dt>
<dd> It is used when comparing via rcw. It means how larger can the second value be to not trigger a <font SIZE="-1">FAIL.</font> Default is 0.2</dd></dl>
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
<dt>name</dt>
<dd> Name of the metric. It has to be unique in a phase.</dd>
<dt>value</dt>
<dd> Value of the metric.</dd>
<dt>tolerance</dt>
<dd> It is used when comparing via rcw. It means how lower can the second value be to not trigger a <font SIZE="-1">FAIL.</font> Default is 0.2</dd></dl>
<p> When comparing <font SIZE="-1">FIRST, SECOND,</font> then: </p>
<pre>
    FIRST &lt;= SECOND means PASS
    FIRST+FIRST*tolerance &lt;= SECOND means WARN
    FIRST+FIRST*tolerance &gt; SECOND means FAIL
</pre>
<h2>AUTHORS</h2>
<dl>
<dt>&bull;</dt>
<dd> Petr Muller &lt;pmuller [at] redhat.com&gt;</dd>
<dt>&bull;</dt>
<dd> Jan Hutar &lt;jhutar [at] redhat.com&gt;</dd>
<dt>&bull;</dt>
<dd> Ales Zelinka &lt;azelinka [at] redhat.com&gt;</dd>
<dt>&bull;</dt>
<dd> Petr Splichal &lt;psplicha [at] redhat.com&gt; </dd>
</dl>
