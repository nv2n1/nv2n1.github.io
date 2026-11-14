---
title: "dbpmda(1)"
name: "dbpmda"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dbpmda/"
description: "dbpmda – debugger for Performance Co-Pilot PMDAs"
---

<h2>NAME</h2>
<p> <code>dbpmda</code> &#8211; debugger for Performance Co-Pilot PMDAs</p>
<h2>SYNOPSIS</h2>
<p> <code>dbpmda</code> [<code>-efi</code>] [<code>-n</code> <i>pmnsfile</i>] [<code>-q</code> <i>timeout</i>] [<code>-U</code> <i>username</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>dbpmda</code> is an interactive interface to the interactions between a Performance Metric Domain Agent (<code><a href="/docs/linux/man/3-pmda/">PMDA</a></code>(3)) and the Performance Metric Collector Daemon (<code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1)). This allows PMDAs to be attached, initialized and exercised to test for correctness. </p>
<p> <code>dbpmda</code> interactively prompts the user for commands, many of which emulate the Protocol Data Units (PDUs) that may be sent by a <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) process. After running <code>dbpmda</code>, enter the command <code>help</code> to get a list of the available commands. The example section below illustrates a session using <code>dbpmda</code> to test a PMDA. </p>
<p> To simplify repetitive testing of a PMDA, the file <i>.dbpmdarc</i> in the current working directory can contain a list of commands that will be executed by <code>dbpmda</code> on startup, before the user is prompted to enter further commands interactively. While processing the <i>.dbpmdarc</i> file, interactive mode and command echoing are enabled and then reset at the end of the <i>.dbpmdarc</i> file (see the <code>-i</code> and <code>-e</code> command line arguments below). </p>
<p> The <code>-f</code> command line option prevents startup processing of a <i>.dbpmdarc</i> file (if it exists). </p>
<p> If the system supports <code><a href="/docs/linux/man/3-readline/">readline</a></code>(3) then this will be used to read commands when input is from a tty device, so history and command line editing are available. </p>
<p> <code>dbpmda</code> accepts the following command line arguments:</p>
<dl>
<dt><code>-e</code></p>
<dd> Echo the input to <code>stdout</code>. This is useful when the input is redirected from a file.</p>
<dt><code>-i</code></p>
<dd> Emulate interactive behavior and prompt for new commands, even if standard input is not a tty device.</p>
<dt><code>-n</code> <i>pmnsfile</i></p>
<dd> Normally <code>dbpmda</code> operates on the distributed Performance Metrics Name Space (PMNS), however if the <code>-n</code> option is specified an alternative local PMNS is loaded from the file <i>pmnsfile</i>.</p>
<dt><code>-q</code> <i>timeout</i></p>
<dd> The pmcd to agent version exchange protocol (new in PCP 2.0 &#8211; introduced to provide backward compatibility) uses this timeout to specify how long <code>dbpmda</code> should wait before assuming that no version response is coming from an agent. If this timeout is reached, the agent is assumed to be an agent which does not understand the PCP 2.0 protocol. The default timeout interval is five seconds, but the <code>-q</code> option allows an alternative timeout interval (which must be greater than zero) to be specified. The unit of time is seconds.</p>
<dt><code>-U</code> <i>username</i></p>
<dd> User account under which to run <code>dbpmda</code>.</dl>
<p> As there are no timeout constraints on a PMDA while using <code>dbpmda</code> (as compared to <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1)), another debugger like <code><a href="/docs/linux/man/1-gdb/">gdb</a></code>(1) can be used on the PMDA process once it has been attached to <code>dbpmda</code>.</p>
<h2>EXAMPLE</h2>
<p> Below is a <code>dbpmda </code> session using the <i>simple</i> PMDA. A <code>.dbpmdarc</code> file is used to set the debugging flag, open the PMDA and display the current status of the debugger: </p>
<pre>
$ cat .dbpmdarc
debug libpmda
open dso pmda_simple.so simple_init 253
status
</pre>
<p> When <code>dbpmda</code> is run, the commands in the <code>.dbpmdarc</code> file are executed first: </p>
<pre><code>
$ dbpmda
        .dbpmdarc &gt; debug libpmda
                        .dbpmdarc &gt; open dso pmda_simple.so simple_init 253
                                        [Fri Sep 19 10:
                                                    19:55] dbpmda(11651) Debug : pmdaInit : PMDA simple DSO : Metric 0.0.1(1)matched to indom 253.0(0)
                                                                                                                  [Fri Sep 19 10:
                                                                                                                              19:55] dbpmda(11651) Debug : pmdaInit : PMDA simple DSO : help file $PCP_PMDAS_DIR
                                        / simple / help opened [Fri Sep 19 10:
                                                                           19:55] dbpmda(11651) Info : name = simple DSO
    [Fri Sep 19 10:
                19:55] dbpmda(11651) Info : domain = 253
                                            [Fri Sep 19 10:
                                                        19:55] dbpmda(11651) Info : num metrics = 4
                                                                                    [Fri Sep 19 10:
                                                                                                19:55] dbpmda(11651) Info : num indom = 1
                                                                                                                            [Fri Sep 19 10:
                                                                                                                                        19:55] dbpmda(11651) Info : direct map = 1
                                                                                                                                                                                     .dbpmdarc
                                                                                                                                                                                 &gt; status
                                                                                                                                                                                       Namespace : (default)
                                                                                                                                                                                                       PMDA :./
                                                                                                                                                                                       pmda_simple.so
                                                                                                                                                                                       Connection : dso
                                                                                                                                                                                                    DSO Interface Version : 2 PMDA PMAPI Version : 2 pmDebug : 32768(libpmda)
                                                                                                                                                                                                        Timer : off
                                                                                                                                                                                                                Getdesc : off
                                                                                                                                                                                                                          Dump Instance Profile state = INCLUDE,
                                                                                                       0 profiles
                                                                                                               .dbpmdarc
                                                                                                           &gt;
</code></pre>
<p> To examine the metric and instance descriptors, the <code>desc</code> and <code>instance</code> commands can be used. Metrics may be identified either by name, or using the &#8220;dotted&#8221; notation to specify the domain, cluster and item fields of a PMID. Instance domains must be identified using a &#8220;dotted&#8221; notation to specify the domain and serial fields. The syntax for most commands will be displayed if the command is given without any arguments: </p>
<p>dbpmda &gt; desc 253.0.0 PMID : 253.0.0 Data Type : 32 &#8211; bit unsigned int InDom : PM_INDOM_NULL 0xffffffff Semantics : instant Units : none<br />
                                                                                                                                        dbpmda &gt;<br />
    instance<br />
        instance indom #[number | name | &#8220;name&#8221;] dbpmda &gt; instance 253.0 pmInDom : 253.0<br />
                                                              [0] inst : 0 name : &#8220;red&#8221;<br />
                                                                                      [1] inst : 1 name : &#8220;green&#8221;<br />
                                                                                                              [2] inst : 2 name : &#8220;blue&#8221;</p>
<p> To test the most important component of a PMDA, the <code>fetch</code>, it is often useful to determine the time it takes the PMDA to respond. The <code>timer</code> may be turned on before giving a <code>fetch</code>: </p>
<p>dbpmda&gt; timer on<br />
dbpmda&gt; fetch simple.numfetch 253.0.1<br />
PMID(s): 253.0.0 253.0.1<br />
pmResult dump from 0x100078e0 timestamp: 0.000000 11:00:00.000 numpmid: 2<br />
  253.0.0 (simple.numfetch): numval: 1 valfmt: 0 vlist[]:<br />
   value 1 1.4012985e-45 0x1<br />
  253.0.1 (simple.color): numval: 3 valfmt: 0 vlist[]:<br />
    inst [0 or ???] value 1 1 1.4012985e-45 0x1<br />
    inst [1 or ???] value 101 1.4153114e-43 0x65<br />
    inst [2 or ???] value 201 2.8166099e-43 0xc9<br />
Timer: 0.003921 seconds<br />
dbpmda&gt; timer off</p>
<p> The integer, floating point and hex translations of the values in the <i>pmResult</i> structure are dumped if <code>getdesc</code> is set to <code>off</code> (the default). Setting <code>getdesc</code> to <code>on</code> would result in only integer values being dumped in the above fetch as the descriptor describes the metrics of 32-bit unsigned integers. </p>
<p> The simple PMDA also supports the <code>store</code> operation which can be tested with subsequent <code>fetch</code> commands: </p>
<pre>
dbpmda&gt; store simple.numfetch &quot;42&quot;
PMID: 253.0.0
Getting description...
Getting Result Structure...
253.0.0: 2 -&gt; 42
dbpmda&gt; fetch simple.numfetch
PMID(s): 253.0.0
pmResult dump from 0x100078e0 timestamp: 0.000000 11:00:00.000 numpmid: 1
  253.0.0 (simple.numfetch): numval: 1 valfmt: 0 vlist[]:
   value 43
</pre>
<p> The value argument in the <code>store</code> command must be a string, which is enclosed in either single quotes (&#8216;) or double quotes (&quot;). </p>
<p> A <code>profile</code> can be specified for each instance domain which includes all, some or no instances: </p>
<pre><code>
dbpmda&gt; help profile
profile indom# [ all | none ]
profile indom# [ add | delete ] number
For the instance domain specified, the profile may be changed to
include 'all' instances, no instances, add an instance or delete 
an instance.
dbpmda&gt; profile 253.0 none
dbpmda&gt; getdesc on
dbpmda&gt; fetch 253.0.1
PMID(s): 253.0.1
pmResult dump from 0x100078e0 timestamp: 0.000000 11:00:00.000 numpmid: 1
  253.0.1 (simple.color): No values returned!
dbpmda&gt; profile 253.0 add 2
dbpmda&gt; fetch 253.0.1
PMID(s): 253.0.1
pmResult dump from 0x100078e0 timestamp: 0.000000 11:00:00.000 numpmid: 1
  253.0.1 (simple.color): numval: 1 valfmt: 0 vlist[]:
   value 202
dbpmda&gt; profile 253.0 add 0
dbpmda&gt; fetch 253.0.1
PMID(s): 253.0.1
pmResult dump from 0x100078e0 timestamp: 0.000000 11:00:00.000 numpmid: 1
  253.0.1 (simple.color): numval: 2 valfmt: 0 vlist[]:
    inst [0 or ???] value 2
    inst [2 or ???] value 203
dbpmda&gt; status
PMDA       = pmda_simple.so
Connection = dso
pmDebug    = 32768 ( libpmda )
Timer      = off
Dump Instance Profile state=INCLUDE, 1 profiles
        Profile [0] indom=1061158913 [253.0] state=EXCLUDE 2 instances
                Instances: [2] [0]
dbpmda&gt; quit
</code></pre>
<p> The <code>watch</code> command (usage: <code>watch</code> <i>filename</i> ) opens an xterm window which tails the specified log file. This window must be closed by the user when no longer required. </p>
<p> The <code>wait</code> command is equivalent to <code>sleep (1)</code> and takes a single integer argument. </p>
<p> The introduction of dynamic subtrees in the PMNS and PMDA_INTERFACE_4 in <i>libpcp_pmda</i> has led to additional commands being supported in <code>dbpmda</code> to exercise the associated dynamic PMNS services. The examples below are based on the <i>sample</i> PMDA. </p>
<pre>
$ dbpmda
dbpmda&gt; open pipe /var/lib/pcp/pmdas/sample/pmdasample -d 29
Start pmdasample PMDA: /var/lib/pcp/pmdas/sample/pmdasample -d 29
dbpmda&gt; children sample.secret
Metric: sample.secret
   non-leaf foo
       leaf bar
dbpmda&gt; traverse sample.secret.foo
Metric: sample.secret.foo
   sample.secret.foo.bar.max.redirect
   sample.secret.foo.one
   sample.secret.foo.two
   sample.secret.foo.bar.three
   sample.secret.foo.bar.four
   sample.secret.foo.bar.grunt.five
   sample.secret.foo.bar.grunt.snort.six
   sample.secret.foo.bar.grunt.snort.huff.puff.seven
dbpmda&gt; pmid sample.secret.foo.bar.four
Metric: sample.secret.foo.bar.four
   29.0.1004
dbpmda&gt; name 29.0.1006
PMID: 29.0.1006
   sample.secret.foo.bar.grunt.snort.six
</pre>
<p> The <code>children</code> command returns the next name component for all the direct descendants of a node within a dynamic subtree of the PMNS. The related <code>traverse</code> command returns the full metric names for all leaf nodes in the PMNS below the specified non-leaf node in a dynamic subtree of the PMNS. </p>
<p> The <code>name</code> and <code>pmid</code> commands exercise the translation of metric names to PMIDs (and vice versa) for metrics within a dynamic subtree of the PMNS. </p>
<p> If the commands <code>children</code>, <code>traverse</code>, <code>pmid</code> or <code>name</code> are used with a PMDA that is <code>not</code> using PMDA_INTERFACE_4 or with performance metric names that are not part of a dynamic subtree of the PMNS, then the PMDA would be expected to return errors (PM_ERR_NAME or PM_ERR_PMID) to reflect the fact that the operation is in error (outside a dynamic subtree of the PMNS it is <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) and not the PMDA that is responsible for implementing these functions). </p>
<p> Client authentication mechanisms have been incorporated into the PMCS, providing per-user (and per-connection) information that is available to PMDAs. A PMDA using PMDA_INTERFACE_6 or later in <i>libpcp_pmda</i> is able to make use of the &quot;attribute&quot; method to gain visibility into these authenticated connections, with access to information including user and group identifiers, user name, and so on. The need to exercise and debug this interface has led to a new <code>dbpmda</code> command. The following example is based on the <i>sample</i> PMDA. </p>
<pre>
$ dbpmda
dbpmda&gt; open pipe pmdasample -D AUTH -l logfile
Start pmdasample PMDA: pmdasample -D AUTH -l logfile
dbpmda&gt; attr &quot;username&quot; &quot;tanya&quot;
Attribute: username=tanya
Success
dbpmda&gt; attr 11 &quot;0&quot;
Attribute: userid=0
Success
dbpmda&gt; 
</pre>
<p> The <code>attr</code> command passes connection attributes (PCP_ATTR keys) and their values into a PMDA in much the same way that PMCD would for a client connection. <code>dbpmda</code> always passes a client context identifier of zero, and while no validity checking on values is performed only recognised attributes can be set. </p>
<p> In the example above the <i>AUTH</i> debug flag is set for the PMDA, which uses this in its attribute callback and records each attribute and value pair sent to it in its <i>logfile</i>. </p>
<p> Note that authentication checks have already been performed by PMCD by the time a PMDA is presented with these attributes, so no further verification is necessary by the PMDA.</p>
<h2>CAVEATS</h2>
<p> A value cannot be stored into metrics of type <code>PM_TYPE_AGGREGATE</code> or <code>PM_TYPE_EVENT</code>. </p>
<p> <code>dbpmda</code> uses <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2) and <code><a href="/docs/linux/man/2-exec/">exec</a></code>(2) to attach to daemon PMDAs. <code>dbpmda</code> makes no attempt to detect the termination of the daemon PMDA process, so it is possible for a PMDA to exit unexpectedly without any notification. However, any further communication attempts with the PMDA will result in errors which will indicate that the PMDA is no longer responding.</p>
<h2>FILES</h2>
<dl>
<dt><i>./.dbpmdarc</i></p>
<dd> List of commands to do on startup.</dl>
<h2>PCP ENVIRONMENT</h2>
<p> Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by PCP. On each installation, the file <i>/etc/pcp.conf</i> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gdb/">gdb</a></code>(1), <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1), <code><a href="/docs/linux/man/1-pmdbg/">pmdbg</a></code>(1), <code><a href="/docs/linux/man/2-exec/">exec</a></code>(2), <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2), <code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3), <code><a href="/docs/linux/man/3-pmda/">PMDA</a></code>(3), <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5) and <code><a href="/docs/linux/man/5-pcp-env/">pcp.env</a></code>(5). </p>
<h2>Index</h2>
