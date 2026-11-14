---
title: "pmlc(1)"
name: "pmlc"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmlc/"
description: "pmlc – configure active Performance Co-Pilot pmlogger(s) interactively"
---

<h2>NAME</h2>
<p> <code>pmlc</code> &#8211; configure active Performance Co-Pilot pmlogger(s) interactively</p>
<h2>SYNOPSIS</h2>
<p> <code>pmlc</code> [<code>-e</code>] [<code>-h</code> <i>host</i>] [<code>-i</code>] [<code>-n</code> <i>pmnsfile</i>] [<code>-P</code>] [<code>-p</code> <i>port</i>] [<code>-Z</code> <i>timezone</i>] [<code>-z</code>] [<code>pid</code>]</p>
<h2>DESCRIPTION</h2>
<p> <code>pmlc</code> may be used to change those metrics and instances which a <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1) writes to a Performance Co-Pilot archive (see <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1)), the frequency with which the metrics are collected and whether the logging is mandatory, advisory, on or off. It also reports the current logging status of metrics and instances. <code>pmlc</code> may be used to control pmlogger instances on remote hosts as well as those on the local host. </p>
<p> Normally <code>pmlc</code> operates on the distributed Performance Metrics Name Space (PMNS), however if the <code>-n</code> option is specified an alternative local PMNS is loaded from the file <i>pmnsfile</i>. </p>
<p> If the <code>-P</code> option is specified, <code>pmlc</code> will attempt to start with a connection to the primary pmlogger on the local host. If the <code>-p</code> option is specified, then <code>pmlc</code> will attempt to start with a connection to the pmlogger on this TCP/IP <i>port</i>. Alternatively, if <i>pid</i> is specified, a connection to the pmlogger instance with that process id will be attempted on startup. The <code>-h</code> option may only be used if <code>-P,</code> <code>-p</code> <i>port</i> or a <i>pid</i> is also specified. In that case <code>pmlc</code> will initially connect to the specified (remote) pmlogger instance on <i>host</i> rather than the local host. If the connection to the specified pmlogger instance cannot be established, <code>pmlc</code> will start with no connection. These options typically allow the same file of <code>pmlc</code> commands to be directed to multiple pmlogger instances by varying the command line arguments. Note that <code>-P</code>, <code>-p</code> <i>port</i>, <i>pid</i> and <code>-h</code> are used only when making an initial connection to a pmlogger instance. They are not used as defaults if subsequent connections are made interactively (see the <code>connect</code> command below). </p>
<p> By default, <code>pmlc</code> reports the time of day according to the local timezone on the system where <code>pmlc</code> is run. The <code>-Z</code> option changes the timezone to <i>timezone</i> in the format of the environment variable <code>TZ</code> as described in <code><a href="/docs/linux/man/7-environ/">environ</a></code>(7). The <code>-z</code> option changes the timezone to the timezone of the pmlogger instance from which information is being obtained. Only one of <code>-z</code> or <code>-Z</code> may be specified. </p>
<p> If standard input is from a tty, <code>pmlc</code> is interactive, with prompts. The <code>-i</code> flag may be used to force interactive behavior, and is typically used in conjunction with <code>-e</code> to echo all command input on standard output. </p>
<p> The following commands may be used: </p>
<dl>
<dt><code>show</code> [ <code>loggers</code> ] [ <code>@</code><i>host</i> ]</p>
<dd> Displays the process identities of all pmlogger instances running on the local host (or <i>host</i>, if specified). The primary pmlogger pid is parenthesized because it can be referred to as &quot;primary&quot; as well as by its pid.</p>
<dt><code>connect</code> <i>pid</i> [ <code>@</code><i>host</i> ]</p>
<dd>
 <code>connect</code> <code>primary</code> [ <code>@</code><i>host</i> ] Connects <code>pmlc</code> to the specified pmlogger process. Any existing connection to a pmlogger instance is closed first. Each pmlogger instance will accept at most one connection at a time, so if the connection is successfully established, your <code>pmlc</code> will be the only one controlling the pmlogger instance it is connected to.</p>
<dt><code>new volume</code></p>
<dd> This command works only while a connection to a pmlogger instance is established. It tells the pmlogger to close the current volume of the log and open a new volume. Closed volumes may be archived, e.g. as part of a regular log management procedure to control the size of the physical log files.</p>
<dt><code>status</code></p>
<dd> This command works only while a connection to a pmlogger instance is established. It prints information about the state of the pmlogger instance and its associated log.</p>
<dt><code>timezone</code> <code>local</code> | <code>logger</code> | <code>&quot;</code><i>timezone</i><code>&quot;</code></p>
<dd> This command sets the time zone used when times are printed. <code>local</code> means use the time zone of the machine that <code>pmlc</code> is running on. <code>logger</code> means use the time zone of the machine where the pmlogger instance is running. Alternatively an explicit <i>timezone</i> enclosed in quotes may be supplied (refer to <code>TZ</code> in <code><a href="/docs/linux/man/7-environ/">environ</a></code>(7) for details). The default time zone is <code>local</code> unless one of the <code>-z</code> or <code>-Z</code> options has been supplied on the command line.</p>
<dt><code>flush</code></p>
<dd> This command works only while a connection to a pmlogger instance is established, and requests the pmlogger instance to flush to disk all buffers associated with the current archive. For old-timers, <code>sync</code> is a synonym for <code>flush</code>. In current versions of <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1) all writes are unbuffered and aligned with the logical records in the external files, so this command achieves nothing, but is retained for backwards compatibility.</p>
<dt><code>help</code></p>
<dd> Displays a summary of the available commands. </p>
<p> <code>h</code> and <code>?</code> are synonyms for <code>help</code>.</p>
<dt><code>quit</code></p>
<dd> Exits from <code>pmlc</code>.</dl>
<p> The remaining commands query and change the logging state of metrics and instances. They will work only if <code>pmlc</code> has a connection to a pmlogger instance. Metrics may be specified as fully qualified names (e.g. hinv.ncpu) or subtrees of the PMNS (e.g. hinv) which are expanded to include all metrics in the subtree (e.g. hinv.ncpu, hinv.cpuclock, etc.). Lists of metrics may be specified by enclosing them in braces with spaces or a comma between metrics (e.g. {hinv.ncpu hinv.ndisk}). Subtrees of metrics may be included in such lists. </p>
<p> Each individual metric specification may be further qualified with a space or comma separated list of instances in square brackets (e.g. kernel.all.load[&quot;1 minute&quot;, &quot;5 minute&quot;]). External instance names or numeric internal instance identifiers or both may be used in the same list (e.g. sample.colour.[red,1,&quot;blue&quot;]). If an instance qualification is applied to a subtree of the PMNS all of the metrics in the subtree must have the same instance domain. Instance qualifications may not be applied to entire lists of metrics but may appear inside such lists. </p>
<p> If no instances are specified for a metric, all instances are used. All instances means all instances available at the time the pmlogger instance in question fetches the metrics for logging. If an instance domain changes over time this is not always the same as the set of instances displayed by <code>pmlc</code>, which can only display the currently available instances. To prevent unintentional errors, only the instances that are currently available to <code>pmlc</code> may appear in instance specifications.</p>
<dl>
<dt><code>query</code><i> metriclist</i></p>
<dd> The current logging state of each metric (and instances, where applicable) in <i>metriclist</i> is displayed. This includes the logging state (e.g. on, maybe, off) and the logging interval for each metric (and instance) requested. The following abbreviations pertaining to metrics (and instances) may appear in the output: <code>adv</code>, advisory; <code>mand</code>, mandatory; <code>nl</code>, not in the log; <code>na</code>, in the log but not currently available from its Performance Metrics Domain Agent (PMDA). Where appropriate, an instance name will appear last on a line preceded by its numeric internal instance identifier.</p>
<dt>[ <code>log</code> ] <code>mandatory on</code><i> interval</i> <i>metriclist</i></p>
<dd> This form of the <code>log</code> command turns on logging for the metrics (and any instances) in <i>metriclist.</i> <i>interval</i> specifies how often the specified metrics/instances should be logged. <code>once</code> indicates that the metrics/instances should appear at most once in the log. More often one would use the optional keyword <code>every</code> followed by a positive number and one of <code>millisecond</code> (or <code>msec</code>), <code>second</code> (or <code>sec</code>), <code>minute</code> (or <code>min</code>), <code>hour</code> or their plurals. </p>
<p> Note that the keyword <code>default</code> which may be used for the default <i>interval</i> in a <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1) configuration file cannot be used in <code>pmlc</code>. </p>
<p> Internal limitations require the <i>interval</i> to be less than (approximately) 74 hours. An <i>interval</i> value of zero is a synonym for <code>once</code>.</p>
<dt>[ <code>log</code> ] <code>mandatory off</code> <i>metriclist</i></p>
<dd> This tells the pmlogger instance not to log any of the metrics/instances in <i>metriclist</i>.</p>
<dt>[ <code>log</code> ] <code>mandatory maybe</code> <i>metriclist</i></p>
<dd> This tells the pmlogger instance to honor any subsequent advisory logging requests for the metrics/instances in <i>metriclist</i>. If the current logging state of the metrics/instances is mandatory (either on or off) the new state will be set to maybe (effectively advisory off). If the current state of the metrics/instances is already advisory (either on or off) the state(s) for the metrics/instances will remain as they are.</p>
<dt>[ <code>log</code> ] <code>advisory on</code><i> interval</i> <i>metriclist</i></p>
<dd>
 [ <code>log</code> ] <code>advisory off</code> <i>metriclist</i> Advisory logging is only applicable if the last logging state specified for a metric/instance was &quot;mandatory maybe&quot; (which permits subsequent advisory logging control) or if the logging state is already advisory. These two statements turn advisory logging on or off (respectively) for the specified metrics/instances. </p>
<p> The interpretation for <i>interval</i> is as above for the <code>mandatory</code> case.</dl>
<p> There is no continuation character required for commands that span lines. </p>
<p> The word <code>at</code> may be used interchangeably with <code>@</code>. </p>
<p> A request to log all instances of a metric will supersede any prior request to log either all or specific instances of a metric (if the request specifies a permissible transition in the logging state). A request to log specific instances of a metric when all instances of a metric are already being logged is refused by <code>pmlogger</code>.</p>
<h2>ACCESS CONTROL</h2>
<p> <code>pmlc</code> may have restricted access to and control over <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1) processes. </p>
<p> If a <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1) is unable to export its control information to the local <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1), then that <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1) cannot cannot be connected to nor controlled by <code>pmlc</code>. In practice, this means the <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1) process has to be owned by the user &#8220;pcp&#8221; and/or the group &#8220;pcp&#8221;. If <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1) is running on the host &#8220;foo&#8221; then use &#8220;pminfo -f -h foo pmcd.pmlogger&#8221; to verify that the <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1) of interest is known to <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1), alternatively <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1) instances that are not reported from the <code>pmlc</code> <code>show loggers @foo</code> command are not known to <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) on the host &#8220;foo&#8221;. </p>
<p> If <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1) is launched with a configuration file that contains an <code>[access]</code> section, then <code>pmlc</code> will be unable to connect to that <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1) unless the access controls allow <code>some</code> access from the host where <code>pmlc</code> is being run. Minimally this requires the <code>enquire</code> access to be permitted in the <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1) access control section. </p>
<p> If <code>pmlc</code> is able to connect to the <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1) of interest, then the following table summarizes the permissions needed to perform different <code>pmlc</code> commands: <center></p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center><code>pmlc</code> command</td>
<td ALIGN=center>Required <code>pmlogger</code> access
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>show loggers</td>
<td>Any
</td>
</tr>
<tr VALIGN=top>
<td>connect</td>
<td>Any of <code>enquire</code>, <code>advisory</code> or <code>mandatory</code>
</td>
</tr>
<tr VALIGN=top>
<td>status</td>
<td>Any of <code>enquire</code>, <code>advisory</code> or <code>mandatory</code>
</td>
</tr>
<tr VALIGN=top>
<td>query &#8230;</td>
<td>Any of <code>enquire</code>, <code>advisory</code> or <code>mandatory</code>
</td>
</tr>
<tr VALIGN=top>
<td>log advisory &#8230;</td>
<td><code>advisory</code>
</td>
</tr>
<tr VALIGN=top>
<td>log mandatory &#8230;</td>
<td><code>mandatory</code>
</td>
</tr>
<tr VALIGN=top>
<td>new volume</td>
<td><code>mandatory</code>
</td>
</tr>
</table>
</table>
<p></center></p>
<h2>PCP ENVIRONMENT</h2>
<p> Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by PCP. On each installation, the file <i>/etc/pcp.conf</i> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1), <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1), <code><a href="/docs/linux/man/1-pmdumplog/">pmdumplog</a></code>(1), <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1), <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5), <code><a href="/docs/linux/man/5-pcp-env/">pcp.env</a></code>(5) and <code><a href="/docs/linux/man/7-environ/">environ</a></code>(7).</p>
<h2>DIAGNOSTICS</h2>
<p> Most error or warning messages are self-explanatory. A message of the form<br />
 Warning: unable to change logging state for&#8230; followed by a list of metrics (and possibly instances) indicates that <code>pmlogger</code> refused the request for the metrics (and instances) that appear. Any metrics (and instances) that were specified but do not appear in the message have had their logging state updated successfully (no news is good news). Usually this warning results from requesting advisory logging when a mandatory control is already in place, or requesting logging for specific instances when all instances are already being logged.</p>
<h2>CAVEAT</h2>
<p> If all instances of a metric are being logged and a request is made to log specific instances of the metric with the same state and frequency, the request may appear to succeed, even though <code>pmlogger</code> has refused the request. This is not normally a problem, as the required information will still be placed into the log by <code>pmlogger</code>. </p>
<p> However in the case where the metric is to be logged once, the outcome is not what might be expected. When <code>pmlogger</code> receives a request to log a metric once, it places the current value(s) of the metric into the log as soon as it can, regardless of whether the metric is already in the log. This may be used to force values into the log. When a request to log specific instances of a metric arrives and is refused because all instances of the metric are already being logged, <code>pmlogger</code> does not place values for the instances requested into the log. It returns the current logging state for each instance requested to <code>pmlc</code>. The requested and returned states are identical, so <code>pmlc</code> doesn&#8217;t raise an error as it should. </p>
<p> To ensure that only certain instances of a metric are being logged, one should always turn off logging for all instances of the metric prior to turning on logging for the specific instances required. </p>
<h2>Index</h2>
