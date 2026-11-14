---
title: "operf(1)"
name: "operf"
section: "1"
letter: "o"
url: "/docs/linux/man/1-operf/"
description: "operf – Performance profiler tool for Linux"
---

<h2>NAME</h2>
<p> operf &#8211; Performance profiler tool for Linux </p>
<h2>SYNOPSIS</h2>
<p> <code>operf</code> [ <i>options</i> ] [ &#8211;system-wide | &#8211;pid &lt;pid&gt; | [ command [ args ] ] ] </p>
<h2>DESCRIPTION</h2>
<p> Operf is an OProfile tool that can be used in place of opcontrol for profiling. Operf uses the Linux Performance Events Subsystem, and hence, does not require the use of the opcontrol daemon &#8212; in fact, operf and opcontrol usage are mutually exclusive. </p>
<p> By default, operf uses &lt;current_dir&gt;/oprofile_data as the session-dir and stores profiling data there. You can change this by way of the <i>&#8211;session-dir</i> option. </p>
<p> The usual post-profiling analysis tools such as <code><a href="/docs/linux/man/1-opreport/">opreport</a>(1)</code> and <code><a href="/docs/linux/man/1-opannotate/">opannotate</a>(1)</code> can be used to generate profile reports. The post-processing analysis tools will search for samples in <i>&lt;current_dir&gt;/oprofile_data</i> first. If that directory does not exist, the post-processing tools use the standard session-dir of /var/lib/oprofile. </p>
<p> Statistics, such as total samples received and lost samples, are written to the operf.log file that can be found in the &lt;session_dir&gt;/samples directory. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>command</code><i>[args]</i></p>
<dd> The command or application to be profiled. <i>args</i> are the input arguments that the command or application requires. One (and only one) of either <i>command</i> , <i>&#8211;pid</i> or <i>&#8211;system-wide</i> is required. </p>
<dt><code>&#8211;pid / -p </code><i>PID</i></p>
<dd> This option enables operf to profile a running application. <i>PID</i> should be the process ID of the process you wish to profile. When finished profiling (e.g., when the profiled process ends), press Ctrl-c to stop operf. If you run <code>operf</code> <code>&#8211;pid</code> as a background job (i.e., with the &amp;), you <code>must</code> stop it in a controlled manner in order for it to process the profile data it has collected. Use <code>kill</code> <code>-SIGINT</code> <code>&lt;operf-PID&gt;</code> for this purpose. </p>
<dt><code>&#8211;system-wide / -s</code></p>
<dd> This option is for performing a system-wide profile. You must have root authority to run operf in this mode. When finished profiling, Ctrl-c to stop operf. If you run <code>operf</code> <code>&#8211;system-wide</code> as a background job (i.e., with the &amp;), you <code>must</code> stop it in a controlled manner in order for it to process the profile data it has collected. Use <code>kill</code> <code>-SIGINT</code> <code>&lt;operf-PID&gt;</code> for this purpose. It is recommended that when running operf with this option, the user&#8217;s current working directory should be /root or a subdirectory of /root to avoid storing sample data files in locations accessible by regular users. </p>
<dt><code>&#8211;vmlinux / k </code><i>vmlinux_path</i></p>
<dd> A vmlinux file that matches the running kernel that has symbol and/or debuginfo. Kernel samples will be attributed to this binary, allowing post-processing tools (like opreport) to attribute samples to the appropriate kernel symbols.</p>
<dt><code>&#8211;events / -e </code><i>event1[,event2[,&#8230;]]</i></p>
<dd> This option is for passing a comma-separated list of event specifications for profiling. Each event spec is of the form:<br />
 <i> name:count[:unitmask[:kernel[:user]]]</i><br />
 You can specify unit mask values using either a numerical value (hex values <i>must</i> begin with &quot;0x&quot;) or a symbolic name (if the <i>name=&lt;um_name&gt;</i> field is shown in the <code>ophelp</code> output). For some named unit masks, the hex value is not unique; thus, OProfile tools enforce specifying such unit masks value by name.</dl>
<dl>
<dt>
<dd> Event names for some IBM PowerPC systems include a <i>_GRP&lt;n&gt;</i> (group number) suffix. You can pass either the full event name or the base event name (i.e., without the suffix) to <code>operf.</code> If the base event name is passed, <code>operf</code> will automatically choose an appropriate group number suffix for the event; thus, OProfile post-processing tools will always show real event names that include the group number suffix. </p>
<p> When no event specification is given, the default event for the running processor type will be used for profiling. Use <code>ophelp</code> to list the available events for your processor type.</dl>
<dl>
<dt><code>&#8211;callgraph / -g</code></p>
<dd> This option enables the callgraph to be saved during profiling. NOTE: The full callchain is recorded, so there is no depth limit. </p>
<dt><code>&#8211;separate-thread / -t</code></p>
<dd> This option categorizes samples by thread group ID (tgid) and thread ID (tid). The &#8216;&#8211;separate-thread&#8217; option is useful for seeing per-thread samples in multi-threaded applications. When used in conjunction with the &#8216;&#8211;system-wide&#8217; option, the &#8216;&#8211;separate-thread&#8217; option is also useful for seeing per-process (i.e., per-thread group) samples for the case where multiple processes are executing the same program during a profiling run. </p>
<dt><code>&#8211;separate-cpu / -c</code></p>
<dd> This option categorizes samples by cpu. </p>
<dt><code>&#8211;session-dir / -d </code><i>path</i></p>
<dd> This option specifies the session path to hold the sample data. If not specified, the data is saved in the <i>oprofile_data</i> directory on the current path. </p>
<dt><code>&#8211;lazy-conversion / -l</code></p>
<dd> Use this option to reduce the overhead of <code>operf</code> during profiling. Normally, profile data received from the kernel is converted to OProfile format during profiling time. This is typically not an issue when profiling a single application. But when using the <i>&#8211;system-wide</i> option, this on-the-fly conversion process can cause noticeable overhead, particularly on busy multi-processor systems. The <i>&#8211;lazy-conversion</i> option directs <code>operf</code> to wait until profiling is completed to do the conversion of profile data. </p>
<dt><code>&#8211;append / -a</code></p>
<dd> By default, <i>operf</i> moves old profile data from &lt;session_dir&gt;/samples/current to &lt;session_dir&gt;/samples/previous. If a &#8216;previous&#8217; profile already existed, it will be replaced. If the <i>&#8211;append</i> option is passed, old profile data is left in place and new profile data will be added to it, and the &#8216;previous&#8217; profile (if one existed) will remain untouched. To access the &#8216;previous&#8217; profile, simply add a session specification to the normal invocation of oprofile post-processing tools. For example:<br />
 <code> opreport</code> <code>session:previous</code> </p>
<dt><code>&#8211;verbose / -V </code><i>level</i></p>
<dd> A comma-separated list of debugging control values, used to increase the verbosity of the output. Valid values are: debug, record, convert, misc, sfile, arcs, or the special value, &#8216;all&#8217;. </p>
<dt><code>&#8211;version / -v</code></p>
<dd> Show operf version. </p>
<dt><code>&#8211;help / -h</code></p>
<dd> Display brief usage message. </p>
<dt><code>&#8211;usage / -u</code></p>
<dd> Display brief usage message. </p>
</dl>
<h2>EXAMPLE</h2>
<p> $ operf make </p>
<h2>VERSION</h2>
<p> This man page is current for oprofile-0.9.9. </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-opreport/">opreport</a>(1), <a href="/docs/linux/man/1-opannotate/">opannotate</a>(1). </p>
<h2>Index</h2>
