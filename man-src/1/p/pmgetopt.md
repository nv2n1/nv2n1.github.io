---
title: "pmgetopt(1)"
name: "pmgetopt"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmgetopt/"
description: "pmgetopt – Performance Co-Pilot shell script option parser"
---

<h2>NAME</h2>
<p> <code>pmgetopt</code> &#8211; Performance Co-Pilot shell script option parser</p>
<h2>SYNOPSIS</h2>
<p> <code>$PCP_BINADM_DIR/pmgetopt</code> [<code>-c</code>|<code>&#8211;config</code> <i>file</i>] [<code>-p</code>|<code>&#8211;progname</code> <i>name</i>] [<code>-u</code>|<code>&#8211;usage</code>] [<code>&#8212;</code>] [<i>parameters</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>pmgetopt</code> is used to perform command line option parsing for shell scripts used in the Performance Co-Pilot (PCP toolkit). It is also used to generate usage messages for those scripts. </p>
<p> The parameters given to <code>pmgetopt</code> take two forms: initially, options specific to <code>pmgetopt</code> itself are passed in, and terminated using the &#8212; mechanism. Thereafter, all of the parameters passed into the shell script should be passed (usually this is simply the &quot;$@&quot; variable). </p>
<p> The options specific to <code>pmgetopt</code> are as follows:</p>
<dl>
<dt><code>-c</code>,<code>&#8211;config</code></p>
<dd> A configuration <i>file</i> in the format described below is passed to <code>pmconfig </code> using this option. If this option is omitted, then <code>pmconfig </code> will read its configuration from the standard input stream.</p>
<dt><code>-p</code>,<code>&#8211;progname</code></p>
<dd> When parsing the calling shell scripts parameters, error and usage messages will contain the given program <i>name</i> rather than referring to <code>pmgetopt</code> itself as the source of the error.</p>
<dt><code>-u</code>,<code>&#8211;usage</code></p>
<dd> A usage message appropriate for the calling shell script to present as its own can be generated using the option.</dl>
<p> <code>pmgetopt</code> parses the given parameters, and produces output in a format suitable for sourcing in the calling shell script. When both short and long forms of an argument are allowed by the specification, <code>pmgetopt</code> will always indicate the short form for simpler shell processing. If arguments are presented that do not match the configuration, a request for a usage message (-?) will be generated for the calling script to respond to. Any non-option parameters will be echoed back to the calling script preceded by the double-hyphen delimiter. Thus a script should stop handling options when this delimiter is detected, and begin the handling of any non-option arguments. </p>
<p> Unlike with the shell built-in <i>getopt</i> command, variables like $OPTARG are not set and the calling script will typically employ use of the shell built-in <i>eval</i>, <i>set</i> and positional <i>shift</i> commands to ensure option processing occurs correctly.</p>
<h2>CONFIGURATION</h2>
<p> The configuration format used by <code>pmgetopt</code> is intended to closely reflect the usage message which would be generated in the presence of invalid arguments (or the <code>-?</code>,<code>&#8211;help</code> option). </p>
<p> There are primarily two types of configuration line &#8211; commands and options. Commands allow metadata to be passed into the option processing process, and options are the allowable command line options that the shell script will accept. Command lines are preceded by the hash character, whereas option lines will always begin with a hyphen (either single or double). Any other line in the configuration, which may include usage headers or descriptive text, has no impact on the option parsing and will be copied unmodified into the usage message. </p>
<p> The set of commands is: <i>getopt</i> (provide short-argument option specification manually, if not present this will be generated from the options presented), <i>usage</i> (provide short one-line summary used at the head of the usage message, which will be prefixed by the <i>progname</i> before reporting), and <i>end</i> which informs <code>pmgetopt</code> to stop processing further commands and options &#8211; any subsequent text encountered will be simply appended to the usage message. </p>
<p> A short-hand notation exists for each of the standard PCP options, as described in <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1). If any of these options (e.g <code>&#8211;host</code>) appears as a single word on any line, it will be transformed into the appropriate option for the shell script, including all metadata about that option (whether it accepts an argument, both short and long option forms, and so on). </p>
<p> Use of the equals symbol (&quot;=&quot;) indicates the presence of a required argument to any option, for both short and long forms. Any non-standard option must be accompanied by a non-empty description of that argument.</p>
<h2>EXAMPLES</h2>
<p> As an example, the following is a valid configuration: <code> </p>
<p> </code></p>
<pre><code>
#Usage : [options] node...
Options:
    --archive
    -d, --delay            pause between updates for archive replay
    --host
    --interval
    -i=INST, --insts=INST  comma-separated metrics instance list
    -r                     output raw counters (no rate conversion)
    --width=N              set the width of each column of output
    --timezone
    --help
</code></pre>
<p> This configuration will produce the following usage message, when run as shown. <code> </p>
<p> </code></p>
<pre><code>
$ pmgetopt --usage --progname=clusterstat -- "$@"
Usage: clusterstat [options] node...
Options:
  -a FILE, --archive=FILE
                        metrics source is a PCP log archive
  -d, --delay           pause between updates for archive replay
  -h HOST, --host=HOST  metrics source is PMCD on host
  -t DELTA, --interval=DELTA
                        sampling interval
  -i INST, --insts=INST comma-separated metrics instance list
  -r                    output raw counters (no rate conversion)
  --width=N             set the width of each column of output
  -Z TZ, --timezone=TZ  set reporting timezone
  -?, --help            show this usage message and exit
</code></pre>
<p> Several examples of <code>pmgetopt</code> use form part of the PCP toolkit, in particular the <code><a href="/docs/linux/man/1-pcp/">pcp</a></code>(1) and <code><a href="/docs/linux/man/1-pmlogmv/">pmlogmv</a></code>(1) scripts provide good reference examples.</p>
<h2>PCP ENVIRONMENT</h2>
<p> Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by PCP. On each installation, the file <i>/etc/pcp.conf</i> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pcp/">pcp</a></code>(1), <code><a href="/docs/linux/man/1-pmlogmv/">pmlogmv</a></code>(1), <code><a href="/docs/linux/man/3-pmgetopt_r/">pmgetopt_r</a></code>(3), <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5) and <code><a href="/docs/linux/man/5-pcp-env/">pcp.env</a></code>(5). </p>
<h2>Index</h2>
