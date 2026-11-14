---
title: "pmlogconf(1)"
name: "pmlogconf"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmlogconf/"
description: "pmlogconf – create/edit a pmlogger configuration file"
---

<h2>NAME</h2>
<p> <code>pmlogconf</code> &#8211; create/edit a pmlogger configuration file</p>
<h2>SYNOPSIS</h2>
<p> <code>pmlogconf</code> [<code>-cqrv</code>] [<code>-d</code><i> groupsdir</i>] [<code>-h</code><i> hostname</i>] <i>configfile</i></p>
<h2>DESCRIPTION</h2>
<p> <code>pmlogconf</code> may be used to create and modify a generic configuration file for the PCP archive logger, <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1). </p>
<p> If <i>configfile</i> does not exist, <code>pmlogconf</code> will create a generic configuration file with a default set of enabled metrics and logging intervals. </p>
<p> Once created, <i>configfile</i> may be used with the <code>-c</code> option to <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1) to select performance metrics and specify logging intervals for a PCP archive. </p>
<p> If <i>configfile</i> does exist, <code>pmlogconf</code> will prompt for input from the user to enable or disable groups of related performance metrics and to control the logging interval for each enabled group. </p>
<p> Group selection requires a simple <code>y</code> (yes) or <code>n</code> (no) response to the prompt <code>Log this group?</code>. </p>
<p> Other responses at this point may be used to select additional control functions as follows:</p>
<dl>
<dt><code>m</code></p>
<dd> Report the names of the metrics in the current group.</p>
<dt><code>q</code></p>
<dd> Finish with group selection (quit) and make no further changes to this group or any subsequent group.</p>
<dt><code>/</code><i>pattern</i></p>
<dd> Make no change to this group but search for a group containing <i>pattern</i> in the description of the group or the names of the associated metrics.</dl>
<p> A logging interval is specified by responding to the <code>Logging interval?</code> prompt with the keywords <code>once</code> or <code>default</code> or a valid <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1) interval specification of the form &#8220;<code>every</code> <i>N timeunits</i>&#8221; or simply &#8220;<i>N timeunits &#8221;</i> (the <code>every</code> is optional) where <i>N</i> is an unsigned integer and <i>timeunits</i> is one of the keywords <code>msec</code>, <code>millisecond</code>, <code>sec</code>, <code>second</code>, <code>min</code>, <code>minute</code>, <code>hour</code> or the plural form of one of the keywords. </p>
<p> When run from automated logging setup processes, the <code>-c</code> option is used to add a message and timestamp indicating this fact. This option is not appropriate for interactive use of the tool. </p>
<p> The <code>-q</code> option suppresses the logging interval dialog and preserves the current interval from <i>configfile</i>. </p>
<p> More verbose output may be enabled with the <code>-v</code> option.</p>
<h2>SETUP GROUP FILES</h2>
<p> When an initial <i>configfile</i> is created, the default specifications come from a set of group files below the <i>groupsdir</i> specified with the <code>-d</code> option (the default <i>groupsdir</i> is <code>$PCP_VAR_DIR/config/pmlogconf</code> which is most commonly correct, so the <code>-d</code> option is rarely used in practice). </p>
<p> The directory structure below <i>groupsdir</i> is arbitrary as all regular files will be found by recursive descent and considered, so add-on products and PMDA developers can easily extend the available defaults to <code>pmlogconf</code> by adding new directories and/or group files below <i>groupsdir</i>. </p>
<p> These group files are processed in the following ways:</p>
<dl>
<dt>&bull;</p>
<dd> When a new <i>configfile</i> is created, all group files are processed.</p>
<dt>&bull;</p>
<dd> Whenever <code>pmlogconf</code> is run with an existing <i>configfile</i>, <i>groupsdir</i> is traversed to see if any new groups have been defined and should be considered for inclusion in <i>configfile</i>.</p>
<dt>&bull;</p>
<dd> When <code>pmlogconf</code> processes a group in <i>configfile</i> that is enabled, the list of metrics associated with the group is taken from the group file (and replaces any previous list of metrics associated with this group in <i>configfile</i>).</p>
<dt>&bull;</p>
<dd> When the <code>-r</code> (reprobe) command line option is specified, every group (not just newly discovered ones) is reprocessed to see if it should be considered for inclusion in <i>configfile</i>.</dl>
<p> Each group file is structured as follows:</p>
<dl>
<dt>&bull;</p>
<dd> The first line must contain <code>#pmlogconf-setup 2.0</code></p>
<dt>&bull;</p>
<dd> Other lines beginning with <code>#</code> are treated as comments.</p>
<dt>&bull;</p>
<dd> Blank lines are ignored.</p>
<dt>&bull;</p>
<dd> One or more lines starting with the keyword <code>ident </code> are used to provide the human-readable description of the group.</p>
<dt>&bull;</p>
<dd> Non-blank lines beginning with white space define metrics to be associated with this group, one per line. Each metric specification follows the rules for a <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1) configuration, namely either the name of a non-leaf node in the PMNS (implying all descendent names in the PMNS), or the name of a leaf node in the PMNS optionally followed by one or more instance names enclosed by &#8220;[&#8221; and &#8220;]&#8221;.</p>
<dt>&bull;</p>
<dd> A control line starting with one of the keywords <code>probe</code> or <code>force</code> must be present.</p>
<dt>&bull;</p>
<dd> An optional logging interval control line begins with the keyword <code>delta</code> followed by one of the <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1) interval specification described above.</p>
<dt>&bull;</p>
<dd> <code>probe</code> control lines have the format:</p>
<dl>
<dt>
<dd>
 <center> <code>probe</code> <i>metric</i> [<i>condition</i> [<i>state_rule</i>] ]<br />
 </center><br />
 where <i>metric</i> is the name of a PCP metric (must be a leaf node in the PMNS and no instance specification is allowed) and the optional <i>condition</i> is the keyword <code>exists</code> (true if <i>metric</i> exists, i.e. is defined in the PMNS) or the keyword <code>values</code> (true if <i>metric</i> exists in the PMNS and has one or more current values) or an expression of the form<br />
 <center> <i>op</i> <i>val</i><br />
 </center> where <i>op</i> is one of the <code><a href="/docs/linux/man/1-awk/">awk</a></code>(1) operators (<code>==</code>, <code>!=</code>, <code>&gt;</code>, <code>&gt;=</code>, <code>&lt;</code>, <code>&lt;=</code>, <code>~</code> (regular expression match) or <code>!~</code> (negated regular expression match)) and <i>val</i> is a value (arbitrary sequence of characters, excluding a space) and the <i>condition</i> is true if there is some instance of <i>metric</i> that makes the expression true. </p>
<p> If the <i>condition</i> is missing, the default is <code>exists</code>. </p>
<p> When an explicit <i>condition</i> is provided, there may also be an optional <i>state_rule</i> of the form<br />
 <center> <code>?</code> <i>true_state</i> <code>:</code> <i>false_state</i><br />
 </center> where <i>true_state</i> (applies if <i>condition</i> is true) and <i>false_state</i> (applies if <i>condition</i> is false) are both taken from the keywords <code>include</code> (include and enable the group and the associated metrics in <i>configfile</i>), <code>available</code> (include and disable the group in <i>configfile</i> &#8211; a user action of <code>y</code> as described above is needed to enable the group and add the associated metrics into <i>configfile</i>) or <code>exclude</code> (the group is not considered for inclusion in <i>configfile</i>). </p>
<p> The default <i>state_rule</i> is<br />
 <center> <code><br />
 </center> ? available : exclude </code></dl>
<dt>&bull;</p>
<dd> <code>force</code> control lines begin with the keyword <code>force</code> followed by one of the states defined above, so one of the actions <code>include</code>, <code>exclude</code> or <code>available</code> is applied unconditionally to the group.</dl>
<p> Probing is only done when a new group is being added to <i>configfile</i> or when the <code>-r</code> command line option is specified. The evaluation of the probing conditions is done by contacting <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) on <i>hostname</i> (defaults to local:).</p>
<h2>EXAMPLE</h2>
<p> The following group file demonstrates all of the supported syntactic elements. </p>
<pre>
#pmlogconf-setup 2.0
ident   Example group file
ident   ... more description
delta   1 minute
probe   sample.secret.foo.one values ? include : exclude
        sample.secret.foo.one
        sample.secret.foo.bar   # non-leaf in the PMNS
        sample.colour [ red green ]
</pre>
<h2>MIGRATION</h2>
<p> The current version of <code>pmlogconf</code> (2.0) supports a slightly different format for <i>configfile</i> compared to earlier versions. If an old version <i>configfile</i> is presented to <code>pmlogconf</code> it will be converted to the new format.</p>
<h2>PCP ENVIRONMENT</h2>
<p> Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by PCP. On each installation, the file <i>/etc/pcp.conf</i> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1), <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1), <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5) and <code><a href="/docs/linux/man/5-pcp-env/">pcp.env</a></code>(5). </p>
<h2>Index</h2>
