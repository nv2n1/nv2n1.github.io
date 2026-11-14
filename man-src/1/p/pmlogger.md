---
title: "pmlogger(1)"
name: "pmlogger"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmlogger/"
description: "pmlogger – create archive log for performance metrics"
---

<h2>NAME</h2>
<p> <code>pmlogger</code> &#8211; create archive log for performance metrics</p>
<h2>SYNOPSIS</h2>
<p> <code>pmlogger</code> [<code>-c</code> <i>configfile</i>] [<code>-h</code> <i>host</i>] [<code>-K</code> <i>spec</i>] [<code>-l</code> <i>logfile</i>] [<code>-L</code>] [<code>-m</code> <i>note</i>] [<code>-n</code> <i>pmnsfile</i>] [<code>-o</code>] [<code>-p</code> <i>pid</i>] [<code>-P</code>] [<code>-r</code>] [<code>-s</code> <i>endsize</i>] [<code>-t</code> <i>interval</i>] [<code>-T</code> <i>endtime</i>] [<code>-u</code>] [<code>-U</code> <i>username</i>] [<code>-v</code> <i>volsize</i>] [<code>-V</code> <i>version</i>] [<code>-x</code> <i>fd</i>] [<code>-y</code>] <i>archive</i></p>
<h2>DESCRIPTION</h2>
<p> <code>pmlogger</code> creates the archive logs of performance metric values that may be &#8220;played back&#8221; by other Performance Co-Pilot (see <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1)) tools. These logs form the basis of the VCR paradigm and retrospective performance analysis services common to the PCP toolkit. </p>
<p> The mandatory argument <i>archive</i> is the base name for the physical files that constitute an archive log. </p>
<p> The <code>-V</code> option specifies the version for the archive that is generated. By default a version 2 archive is generated, and the only value currently supported for <i>version</i> is 2. </p>
<p> Unless directed to another host by the <code>-h</code> option or when directly using PMDAs via the <code>-o</code> option, <code>pmlogger</code> will contact the Performance Metrics Collector Daemon (PMCD) on the local host and use that as the source of the metric values to be logged. </p>
<p> To support the required flexibility and control over what is logged and when, <code>pmlogger</code> maintains an independent two level logging state for each instance of each performance metric. At the first (mandatory) level, logging is allowed to be <code>on</code> (with an associated interval between samples), or <code>off</code> or <code>maybe</code>. In the latter case, the second (advisory) level logging is allowed to be <code>on</code> (with an associated interval between samples), or <code>off</code>. </p>
<p> The mandatory level allows universal specification that some metrics must be logged, or must <code>not</code> be logged. The default state for all instances of all metrics when <code>pmlogger</code> starts is mandatory maybe and advisory off. </p>
<p> Use <code><a href="/docs/linux/man/1-pmlc/">pmlc</a></code>(1) to interrogate and change the logging state once <code>pmlogger</code> is running. </p>
<p> If a metric&#8217;s state is mandatory (on or off) and a request is made to change it to mandatory maybe, the new state is mandatory maybe and advisory off. If a metric&#8217;s state is already advisory (on or off) and a request is made to change it to mandatory maybe, the current state is retained. </p>
<p> It is not possible for <code>pmlogger</code> to log specific instances of a metric and all instances of the same metric concurrently. If specific instances are being logged and a request to log all instances is made, then all instances of the metric will be logged according to the new request, superseding any prior logging request for the metric. A request to log all instances of a metric will supersede any previous request to log all instances. A request to log specific instances of a metric when all instances are already being logged is refused. To do this one must turn off logging for all instances of the metric first. In each case, the validity of the request is checked first; for example a request to change a metric&#8217;s logging state to advisory on when it is currently mandatory off is never permitted (it is necessary to change the state to mandatory maybe first). </p>
<p> Optionally, each system running <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) may also be configured to run a &#8220;primary&#8221; <code>pmlogger</code> instance. This <code>pmlogger</code> instance is launched by <code>$PCP_RC_DIR/pmlogger</code>, and is affected by the files <i>$PCP_SYSCONF_DIR/pmlogger/control</i>, <i>$PCP_SYSCONF_DIR/pmlogger/control</i>.d (use <code><a href="/docs/linux/man/8-chkconfig/">chkconfig</a></code>(8) or similar platform-specific commands to activate or disable the primary <code>pmlogger </code> instance), <i>$PCP_SYSCONFIG_DIR/pmlogger</i> (environment variable settings for the primary <code>pmlogger</code>) <i>$PCP_SYSCONF_DIR/pmlogger/pmlogger.options</i> (command line options passed to the primary <code>pmlogger</code>) and <i>$PCP_VAR_DIR/config/pmlogger/config.default</i> (the default initial configuration file for the primary <code>pmlogger</code>). </p>
<p> The primary <code>pmlogger</code> instance is identified by the <code>-P</code> option. There may be at most one &#8220;primary&#8221; <code>pmlogger</code> instance on each system. The primary <code>pmlogger</code> instance (if any) must be running on the same host as the <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) to which it connects (if any), so the <code>-h</code> and <code>-P</code> options are mutually exclusive. </p>
<p> Logging of some metrics is possible even in the absence of a local <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1), using the &quot;local context&quot; mode of operation. This is activated using the <code>-o</code> option, and causes <code>pmlogger</code> to make use of local DSO PMDAs instead of communicating with <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1). When operating using a local context, the <code>-K</code> option may be used to control the DSO PMDAs that should be made accessible. The <i>spec</i> argument conforms to the syntax described in <code><a href="/docs/linux/man/3-__pmspeclocalpmda/">__pmSpecLocalPMDA</a></code>(3). More than one <code>-K</code> option may be used. </p>
<p> When launched as a non-primary instance, <code>pmlogger</code> will exit immediately if the configuration file causes no metric logging to be scheduled. The <code>-L</code> option overrides this behavior, and causes a non-primary <code>pmlogger</code> instance to &#8220;linger&#8221;, presumably pending some future dynamic re-configuration and state change via <code><a href="/docs/linux/man/1-pmlc/">pmlc</a></code>(1). <code>pmlogger</code> will also linger without the <code>-L</code> option being used if all the metrics to be logged are logged as once only metrics. When the once only metrics have been logged, a warning message will be generated stating that the event queue is empty and no more events will be scheduled. </p>
<p> By default all diagnostics and errors from <code>pmlogger</code> are written to the file <i>pmlogger.log</i> in the directory where <code>pmlogger</code> is launched. The <code>-l</code> option may be used to override the default behavior. If the log file cannot be created or is not writable, output is written to standard error instead. </p>
<p> If specified, the <code>-s</code> option instructs <code>pmlogger</code> to terminate after a certain size in records, bytes or time units has been accumulated. If <i>endsize</i> is an integer then <i>endsize</i> records will be written to the log. If <i>endsize</i> is an integer suffixed by <code>b </code> or <code>bytes</code> then <i>endsize</i> bytes of the archive data will be written out (note, however, that archive log record boundaries will not be broken and so this limit may be slightly surpassed). Other viable file size units include: <code>K</code>, <code>Kb</code>, <code>Kbyte</code>, <code>Kilobyte</code> for kilobytes and <code>M</code>, <code>Mb</code>, <code>Mbyte</code>, <code>Megabyte</code> for megabytes and <code>G</code>, <code>Gb</code>, <code>Gbyte</code>, <code>Gigabyte</code> for gigabytes. These units may be optionally suffixed by an <code>s </code> and may be of mixed case. Alternatively <i>endsize</i> may be an integer or a floating point number suffixed using a time unit as described in <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1) for the <i>interval</i> argument (to the standard PCP <code>-t</code> command line option). </p>
<pre>
Some examples of different formats:
<code>-s 100 </code>
<code>-s 100bytes</code>
<code>-s 100K </code>
<code>-s 100Mb</code>
<code>-s 10Gbyte</code>
<code>-s 10mins</code>
<code>-s 1.5hours</code>
</pre>
<p> The default is for <code>pmlogger</code> to run forever. </p>
<p> The <code>-r</code> option causes the size of the physical record(s) for each group of metrics and the expected contribution of the group to the size of the PCP archive for one full day of collection to be reported in the log file. This information is reported the first time each group is successfully written to the archive. </p>
<p> The <code>-U</code> option specifies the user account under which to run <code>pmlogger</code>. The default is the current user account for interactive use. When run as a daemon, the unprivileged &quot;pcp&quot; account is used in current versions of PCP, but in older versions the superuser account (&quot;root&quot;) was used by default. </p>
<p> The log file is potentially a multi-volume data set, and the <code>-v</code> option causes <code>pmlogger</code> to start a new volume after a certain size in records, bytes, or time units has been accumulated for the current volume. The format of this size specification is identical to that of the <code>-s</code> option (see above). The default is for <code>pmlogger</code> to create a single volume log. Additional volume switches can also be forced asynchronously by either using <code><a href="/docs/linux/man/1-pmlc/">pmlc</a></code>(1) or sending <code>pmlogger</code> a SIGHUP signal (see below). Note, if a scheduled volume switch is in operation due to the <code>-v</code> option, then its counters will be reset after an asynchronous switch. </p>
<p> Independent of any <code>-v</code> option, each volume of an archive is limited to no more than 2^31 bytes, so <i>pmlogger</i> will automatically create a new volume for the archive before this limit is reached. </p>
<p> Normally <code>pmlogger</code> operates on the distributed Performance Metrics Name Space (PMNS), however if the <code>-n</code> option is specified an alternative local PMNS is loaded from the file <i>pmnsfile.</i> </p>
<p> Under normal circumstances, <code>pmlogger</code> will run forever (except for a <code>-s </code> option or a termination signal). The <code>-T</code> option may be used to limit the execution time using the format of time as prescribed by <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1). The time is interpreted within the time zone of the PMCD server, unless the <code>-y</code> option is given, within which case the time zone at this logger host is used. </p>
<pre>
Some examples of different formats:
<code>-T 10mins </code>
<code>-T '@ 11:30' </code>
</pre>
<p> From this it can be seen that <code>-T 10mins</code> and <code>-s 10mins</code> perform identical actions. </p>
<p> Alternatively, <code>pmlogger</code> runtime may be limited to the lifetime of another process by using the <code>-p</code> or <code>&#8211;PID</code> option to nominate the PID of the process of interest. In this case the <code>pmlogger</code> will exit when the other process no longer exists. </p>
<p> When <code>pmlogger</code> receives a SIGHUP signal, the current volume of the log is closed, and a new volume is opened. This mechanism (or the alternative mechanism via <code><a href="/docs/linux/man/1-pmlc/">pmlc</a></code>(1)) may be used to manage the growth of the log files &#8211; once a log volume is closed, that file may be archived without ill-effect on the continued operation of <code>pmlogger</code>. See also the <code>-v</code> option above. </p>
<p> Historically the buffers for the current log may be flushed to disk using the <code>flush</code> command of <code><a href="/docs/linux/man/1-pmlc/">pmlc</a></code>(1), or by sending <code>pmlogger</code> a SIGUSR1 signal or by using the <code>-u</code> option. The current version of <i>pmlogger</i> and the <i>libpcp</i> routines that underpin <i>pmlogger</i> unconditionally use unbuffered writes and a single <code><a href="/docs/linux/man/3-fwrite/">fwrite</a></code>(3) for each logical record written, and so &#8220;flushing&#8221; does not force any additional data to be written to the file system. The <code>-u</code> option, the SIGUSR1 handling and the <code><a href="/docs/linux/man/1-pmlc/">pmlc</a></code>(1) <code>flush</code> command are retained for backwards compatibility. </p>
<p> When launched with the <code>-x </code> option, pmlogger will accept asynchronous control requests on the file descriptor <i>fd</i>. This option is only expected to be used internally by PCP applications that support &#8220;live record mode&#8221;. </p>
<p> The <code>-m</code> option allows the string <i>note</i> to be appended to the map file for this instance of <code>pmlogger</code> in the <code>$PCP_TMP_DIR/pmlogger</code> directory. This is currently used internally to document the file descriptor (<i>fd</i>) when the <code>-x</code> option is used, or to indicate that this <code>pmlogger</code> instance was started under the control of <code><a href="/docs/linux/man/1-pmlogger_check/">pmlogger_check</a></code>(1).</p>
<h2>CONFIGURATION FILE SYNTAX</h2>
<p> The configuration file may be specified with the <code>-c</code> option. If it is not, configuration specifications are read from standard input. </p>
<p> If <i>configfile</i> does not exist, then a search is made in the directory <i>$PCP_VAR_DIR/config/pmlogger</i> for a file of the same name, and if found that file is used, e.g. if <i>config.mumble</i> does not exist in the current directory and the file <i>$PCP_VAR_DIR/config/pmlogger/config.mumble</i> does exist, then <code>-c config.mumble</code> and <code>-c $PCP_VAR_DIR/config/pmlogger/config.mumble</code> are equivalent. </p>
<p> The syntax for the configuration file is as follows.</p>
<dl>
<dt>1.</p>
<dd> Words are separated by white space (space, tab or newline).</p>
<dt>2.</p>
<dd> The symbol &#8220;#&#8221; (hash) introduces a comment, and all text up to the next newline is ignored.</p>
<dt>3.</p>
<dd> Keywords (shown in <code>bold</code> below) must appear literally (i.e. in lower case).</p>
<dt>4.</p>
<dd> Each specification begins with the optional keyword <code>log</code>, followed by one of the states <code>mandatory on</code>, <code>mandatory off</code>, <code>mandatory maybe</code>, <code>advisory on</code> or <code>advisory off</code>.</p>
<dt>5.</p>
<dd> For the <code>on</code> states, a logging interval must follow using the syntax &#8220;<code>once</code>&#8221;, or &#8220;<code>default</code>&#8221;, or &#8220;<code>every</code> <i>N timeunits</i>&#8221;, or simply &#8220;<i>N timeunits</i>&#8221; &#8211; <i>N</i> is an unsigned integer, and <i>timeunits</i> is one of the keywords <code>msec</code>, <code>millisecond</code>, <code>sec</code>, <code>second</code>, <code>min</code>, <code>minute</code>, <code>hour</code> or the plural form of one of the above. </p>
<p> Internal limitations require the interval to be smaller than (approximately) 74 hours. An interval value of zero is a synonym for <code>once</code>. An interval of <code>default</code> means to use the default logging interval of 60 seconds; this default value may be changed to <i>interval</i> with the <code>-t</code> command line option.</p>
<dt>
<dd> The <i>interval</i> argument follows the syntax described in <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1), and in the simplest form may be an unsigned integer (the implied units in this case are seconds).</p>
<dt>6.</p>
<dd> Following the state and possible interval specifications comes a &#8220;{&#8221;, followed by a list of one or more metric specifications and a closing &#8220;}&#8221;. The list is white space (or comma) separated. If there is only one metric specification in the list, the braces are optional.</p>
<dt>7.</p>
<dd> A metric specification consists of a metric name optionally followed by a set of instance names. The metric name follows the standard PCP naming conventions, see <code><a href="/docs/linux/man/5-pmns/">pmns</a></code>(5), and if the metric name is a non-leaf node in the PMNS (see <code><a href="/docs/linux/man/5-pmns/">pmns</a></code>(5)), then <code>pmlogger</code> will recursively descend the PMNS and apply the logging specification to all descendent metric names that are leaf nodes in the PMNS. The set of instance names is a &#8220;[&#8221;, followed by a list of one or more space (or comma) separated names, numbers or strings, and a closing &#8220;]&#8221;. Elements in the list that are numbers are assumed to be internal instance identifiers, other elements are assumed to be external instance identifiers &#8211; see <code><a href="/docs/linux/man/3-pmgetindom/">pmGetInDom</a></code>(3) for more information.</p>
<dl>
<dt>
<dd>
<p> If no instances are given, then the logging specification is applied to all instances of the associated metric.</dl>
<dt>8.</p>
<dd> There may be an arbitrary number of logging specifications.</p>
<dt>9.</p>
<dd> Following all of the logging specifications, there may be an optional access control section, introduced by the literal token <code>[access]</code>. Thereafter come access control rules that allow or disallow operations from particular hosts or groups of hosts.</p>
<dl>
<dt>
<dd>
<p> The operations may be used to interrogate or control a running <code>pmlogger</code> using <code><a href="/docs/linux/man/1-pmlc/">pmlc</a></code>(1) and fall into the following classes:</p>
<dl>
<dt><code>enquire</code></p>
<dd> interrogate the status of <code>pmlogger</code> and the metrics it is logging</p>
<dt><code>advisory</code></p>
<dd> Change advisory logging.</p>
<dt><code>mandatory</code></p>
<dd> Change mandatory logging.</p>
<dt><code>all</code></p>
<dd> All of the above.</dl>
<p> Access control rules are of the form &#8220;<code>allow</code> <i>hostlist</i> <code>:</code> <i>operationlist</i> <code>;</code>&#8221; and &#8220;<code>disallow</code> <i>hostlist</i> <code>:</code> <i>operationlist</i> <code>;</code>&#8221;. </p>
<p> The <i>hostlist</i> follows the syntax and semantics for the access control mechanisms used by PMCD and are fully documented in <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1). An <i>operationslist</i> is a comma separated list of the operations <code>advisory</code>, <code>mandatory</code>, <code>enquire</code> and <code>all</code>. </p>
<p> A missing <code>[access]</code> section allows all access and is equivalent to <code>allow * : all;</code>.</dl>
</dl>
<p> The configuration (either from standard input or <i>configfile</i>) is initially scanned by <code><a href="/docs/linux/man/1-pmcpp/">pmcpp</a></code>(1) with the options <code>-rs</code> and <code>-I </code><i>$PCP_VAR_DIR/config/pmlogger</i>. This extends the configuration file syntax with include file processing (<code>%include</code>), a common location to search for include files (<i>$PCP_VAR_DIR/config/pmlogger</i>), macro definitions (<code>%define</code>), macro expansion (<code>%</code><i>name</i> and <code>%{</code><i>name</i><code>}</code>) and conditional inclusion of lines (<code>%ifdef </code><i>name</i> &#8230; <code>%else</code> &#8230; <code>%endif</code> and <code>%ifndef </code><i>name</i> &#8230; <code>%else</code> &#8230; <code>%endif</code>).</p>
<h2>EXAMPLES</h2>
<p> For each PCP utility, there is a sample <code>pmlogger</code> configuration file that could be used to create an archive log suitable for replaying with that tool (i.e. includes all of the performance metrics used by the tool). For a tool named <i>foo</i> this configuration file is located in <i>$PCP_VAR_DIR/config/pmlogger/config.foo</i>. </p>
<p> The following is a simple default configuration file for a primary <code>pmlogger</code> instance, and demonstrates most of the capabilities of the configuration specification language. </p>
<pre><code>
log mandatory on once{hinv.ncpu hinv.ndisk} log mandatory on every 10 minutes{
    disk.all.write
        disk.all.read
            network.interface.in.packets["et0"] network.interface.out.packets["et0"] nfs.server.reqs["lookup"
                                                                                                     "getattr"
                                                                                                     "read"
                                                                                                     "write"]} log advisory on every 30 minutes{
    environ.temp
        pmcd.pdu_in.total
            pmcd.pdu_out.total} %
    include "macros.default" % ifdef % disk_detail log mandatory on % disk_detail_freq{disk.dev} % endif[access] disallow * : all except enquire;
allow localhost : mandatory, advisory;
</code></pre>
<h2>FILES</h2>
<dl>
<dt><i>archive</i><code>.meta</p>
<dd> metadata (metric descriptions, instance domains, etc.) for the archive log</p>
<dt></code><i>archive</i><code>.0</p>
<dd> initial volume of metrics values (subsequent volumes have suffixes 1</code>, <code>2</code>, &#8230;)</p>
<dt><i>archive</i><code>.index</p>
<dd> temporal index to support rapid random access to the other files in the archive log</p>
<dt>$PCP_TMP_DIR/pmlogger</code></p>
<dd> <code>pmlogger</code> maintains the files in this directory as the map between the process id of the <code>pmlogger</code> instance and the IPC port that may be used to control each <code>pmlogger</code> instance (as used by <code><a href="/docs/linux/man/1-pmlc/">pmlc</a></code>(1))</p>
<dt><code>$PCP_VAR_DIR/config/pmlogger/config.default</code></p>
<dd> default configuration file for the primary logger instance launched from <code>$PCP_RC_DIR/pmlogger</code></p>
<dt><code>$PCP_VAR_DIR/config/pmlogger/config.</code>*</p>
<dd> assorted configuration files suitable for creating logs that may be subsequently replayed with the PCP visualization and monitoring tools</p>
<dt><code>$PCP_LOG_DIR/pmlogger/</code><i>hostname</i></p>
<dd> Default directory for PCP archive files for performance metric values collected from the host <i>hostname</i>.</p>
<dt><code>$PCP_SYSCONFIG_DIR/pmlogger</code></p>
<dd> additional environment variables that will be set when the primary <code>pmlogger</code> instance executes. Only settings of the form &quot;PMLOGGER_VARIABLE=value&quot; will be honoured.</p>
<dt><i>./pmlogger.log</i></p>
<dd> (or <code>$PCP_LOG_DIR/pmlogger/</code><i>hostname</i><code>/pmlogger.log</code> when started automatically by either <code>$PCP_RC_DIR/pmlogger</code> or one of the <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1) monitoring scripts such as <code><a href="/docs/linux/man/1-pmlogger_check/">pmlogger_check</a></code>(1))<br />
 all messages and diagnostics are directed here</dl>
<h2>ENVIRONMENT</h2>
<p> Normally <code>pmlogger</code> creates a socket to receive control messages from <code><a href="/docs/linux/man/1-pmlc/">pmlc</a></code>(1) on the first available TCP/IP port numbered 4330 or higher. The environment variable <code>PMLOGGER_PORT</code> may be used to specify an alternative starting port number. </p>
<p> If set to the value 1, the <code>PMLOGGER_LOCAL</code> environment variable will cause <code>pmlogger</code> to run in a localhost-only mode of operation, where it binds only to the loopback interface. </p>
<p> The <code>PMLOGGER_MAXPENDING</code> variable can be set to indicate the maximum length to which the queue of pending <code>pmlc</code> connections may grow.</p>
<h2>PCP ENVIRONMENT</h2>
<p> Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by PCP. On each installation, the file <i>/etc/pcp.conf</i> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1), <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1), <code><a href="/docs/linux/man/1-pmdumplog/">pmdumplog</a></code>(1), <code><a href="/docs/linux/man/1-pmlc/">pmlc</a></code>(1), <code><a href="/docs/linux/man/1-pmlogger_check/">pmlogger_check</a></code>(1), <code><a href="/docs/linux/man/3-__pmspeclocalpmda/">__pmSpecLocalPMDA</a></code>(3), <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5), <code><a href="/docs/linux/man/5-pcp-env/">pcp.env</a></code>(5), <code><a href="/docs/linux/man/5-pmns/">pmns</a></code>(5) and <code><a href="/docs/linux/man/8-chkconfig/">chkconfig</a></code>(8).</p>
<h2>DIAGNOSTICS</h2>
<p> The archive logs are sufficiently precious that <code>pmlogger</code> will not truncate an existing physical file. A message of the form<br />
 __pmLogNewFile: &quot;foo.index&quot; already exists, not over-written<br />
 __pmLogCreate: File exists indicates this situation has arisen. You must explicitly remove the files and launch <code>pmlogger</code> again. </p>
<p> There may be at most one primary <code>pmlogger</code> instance per monitored host; attempting to bend this rule produces the error:<br />
 pmlogger: there is already a primary pmlogger running </p>
<p> Various other messages relating to the creation and/or deletion of files in <i>$PCP_TMP_DIR/pmlogger</i> suggest a permission problem on this directory, or some feral files have appeared therein. </p>
<h2>Index</h2>
