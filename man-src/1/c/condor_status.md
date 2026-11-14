---
title: "condor_status(1)"
name: "condor_status"
section: "1"
letter: "c"
url: "/docs/linux/man/1-condor_status/"
description: "condor_status Display status of the HTCondor pool"
---

<h2>Name</h2>
<p> <i>condor_status</i> Display status of the HTCondor pool </p>
<h2>Synopsis</h2>
<p> <i>condor_status</i> [ <code>-debug</code> ] [ <i>help options</i> ] [ <i>query options</i> ] [ <i>display options</i> ] [ <i>custom options</i> ] [ <i>name &#8230; </i> ] </p>
<h2>Description</h2>
<p> <i>condor_status</i> is a versatile tool that may be used to monitor and query the HTCondor pool. The <i>condor_status</i> tool can be used to query resource information, submitter information, checkpoint server information, and daemon master information. The specific query sent and the resulting information display is controlled by the query options supplied. Queries and display formats can also be customized. </p>
<p> The options that may be supplied to <i>condor_status</i> belong to five groups:</p>
<dl>
<dt>
<dd> * <code>Help options</code> provide information about the <i>condor_status</i> tool.</p>
<dt>
<dd> * <code>Query options</code> control the content and presentation of status information.</p>
<dt>
<dd> * <code>Display options</code> control the display of the queried information.</p>
<dt>
<dd> * <code>Custom options</code> allow the user to customize query and display information.</p>
<dt>
<dd> * <code>Host options</code> specify specific machines to be queried</dl>
<p> At any time, only one <i>help option</i> , one <i>query option</i> and one <i>display option</i> may be specified. Any number of <i>custom options</i> and <i>host options</i> may be specified. </p>
<h2>Options</h2>
<p> <code>-debug</code></p>
<dl>
<dt>
<dd> Causes debugging information to be sent to stderr , based on the value of the configuration variable TOOL_DEBUG</p>
<dt>
<dd></dl>
<p> <code>-help</code></p>
<dl>
<dt>
<dd> (Help option) Display usage information.</p>
<dt>
<dd></dl>
<p> <code>-diagnose</code></p>
<dl>
<dt>
<dd> (Help option) Print out ClassAd query without performing the query.</p>
<dt>
<dd></dl>
<p> <code>-absent</code></p>
<dl>
<dt>
<dd> (Query option) Query for and display only absent resources.</p>
<dt>
<dd></dl>
<p> <code>-ads </code> <i>filename</i></p>
<dl>
<dt>
<dd> (Query option) Read the set of ClassAds in the file specified by <i>filename</i> , instead of querying the <i>condor_collector</i> .</p>
<dt>
<dd></dl>
<p> <code>-any</code></p>
<dl>
<dt>
<dd> (Query option) Query all ClassAds and display their type, target type, and name.</p>
<dt>
<dd></dl>
<p> <code>-avail</code></p>
<dl>
<dt>
<dd> (Query option) Query <i>condor_startd</i> ClassAds and identify resources which are available.</p>
<dt>
<dd></dl>
<p> <code>-ckptsrvr</code></p>
<dl>
<dt>
<dd> (Query option) Query <i>condor_ckpt_server</i> ClassAds and display checkpoint server attributes.</p>
<dt>
<dd></dl>
<p> <code>-claimed</code></p>
<dl>
<dt>
<dd> (Query option) Query <i>condor_startd</i> ClassAds and print information about claimed resources.</p>
<dt>
<dd></dl>
<p> <code>-cod</code></p>
<dl>
<dt>
<dd> (Query option) Display only machine ClassAds that have COD claims. Information displayed includes the claim ID, the owner of the claim, and the state of the COD claim.</p>
<dt>
<dd></dl>
<p> <code>-collector</code></p>
<dl>
<dt>
<dd> (Query option) Query <i>condor_collector</i> ClassAds and display attributes.</p>
<dt>
<dd></dl>
<p> <code>-defrag</code></p>
<dl>
<dt>
<dd> (Query option) Query <i>condor_defrag</i> ClassAds.</p>
<dt>
<dd></dl>
<p> <code>-direct </code> <i>hostname</i></p>
<dl>
<dt>
<dd> (Query option) Go directly to the given host name to get the ClassAds to display. By default, returns the <i>condor_startd</i> ClassAd. If <code>-schedd</code> is also given, return the <i>condor_schedd</i> ClassAd on that host.</p>
<dt>
<dd></dl>
<p> <code>-java</code></p>
<dl>
<dt>
<dd> (Query option) Display only Java-capable resources.</p>
<dt>
<dd></dl>
<p> <code>-license</code></p>
<dl>
<dt>
<dd> (Query option) Display license attributes.</p>
<dt>
<dd></dl>
<p> <code>-master</code></p>
<dl>
<dt>
<dd> (Query option) Query <i>condor_master</i> ClassAds and display daemon master attributes.</p>
<dt>
<dd></dl>
<p> <code>-negotiator</code></p>
<dl>
<dt>
<dd> (Query option) Query <i>condor_negotiator</i> ClassAds and display attributes.</p>
<dt>
<dd></dl>
<p> <code>-pool </code> <i>centralmanagerhostname[:portnumber]</i></p>
<dl>
<dt>
<dd> (Query option) Query the specified central manager using an optional port number. <i>condor_status</i> queries the machine specified by the configuration variable COLLECTOR_HOST by default.</p>
<dt>
<dd></dl>
<p> <code>-run</code></p>
<dl>
<dt>
<dd> (Query option) Display information about machines currently running jobs.</p>
<dt>
<dd></dl>
<p> <code>-schedd</code></p>
<dl>
<dt>
<dd> (Query option) Query <i>condor_schedd</i> ClassAds and display attributes.</p>
<dt>
<dd></dl>
<p> <code>-server</code></p>
<dl>
<dt>
<dd> (Query option) Query <i>condor_startd</i> ClassAds and display resource attributes.</p>
<dt>
<dd></dl>
<p> <code>-startd</code></p>
<dl>
<dt>
<dd> (Query option) Query <i>condor_startd</i> ClassAds.</p>
<dt>
<dd></dl>
<p> <code>-state</code></p>
<dl>
<dt>
<dd> (Query option) Query <i>condor_startd</i> ClassAds and display resource state information.</p>
<dt>
<dd></dl>
<p> <code>-statistics </code> <i>WhichStatistics</i></p>
<dl>
<dt>
<dd> (Query option) Can only be used if the <code>-direct</code> option has been specified. Identifies which Statistics attributes to include in the ClassAd. <i>WhichStatistics</i> is specified using the same syntax as defined for STATISTICS_TO_PUBLISH . A definition is in the HTCondor Administrator&#8217;s manual section on configuration.</p>
<dt>
<dd></dl>
<p> <code>-storage</code></p>
<dl>
<dt>
<dd> (Query option) Display attributes of machines with network storage resources.</p>
<dt>
<dd></dl>
<p> <code>-submitters</code></p>
<dl>
<dt>
<dd> (Query option) Query ClassAds sent by submitters and display important submitter attributes.</p>
<dt>
<dd></dl>
<p> <code>-subsystem </code> <i>type</i></p>
<dl>
<dt>
<dd> (Query option) If <i>type</i> is one of <i>collector</i> , <i>negotiator</i> , <i>master</i> , <i>schedd</i> , <i>startd</i> , or <i>quill</i> , then behavior is the same as the query option without the <code>-subsystem</code> option. For example, <code>-subsystem </code> <i>collector</i> is the same as <code>-collector</code> . A value of <i>type</i> of <i>CkptServer</i> , <i>Machine</i> , <i>DaemonMaster</i> , or <i>Scheduler</i> targets that type of ClassAd.</p>
<dt>
<dd></dl>
<p> <code>-vm</code></p>
<dl>
<dt>
<dd> (Query option) Query <i>condor_startd</i> ClassAds, and display only VM-enabled machines. Information displayed includes the machine name, the virtual machine software version, the state of machine, the virtual machine memory, and the type of networking.</p>
<dt>
<dd></dl>
<p> <code>-offline</code></p>
<dl>
<dt>
<dd> (Query option) Query <i>condor_startd</i> ClassAds, and display, for each machine with at least one offline universe, which universes are offline for it.</p>
<dt>
<dd></dl>
<p> <code>-attributes </code> <i>Attr1[,Attr2 &#8230; ]</i></p>
<dl>
<dt>
<dd> (Display option) Explicitly list the attributes in a comma separated list which should be displayed when using the <code>-xml</code> or <code>-long</code> options. Limiting the number of attributes increases the efficiency of the query.</p>
<dt>
<dd></dl>
<p> <code>-expert</code></p>
<dl>
<dt>
<dd> (Display option) Display shortened error messages.</p>
<dt>
<dd></dl>
<p> <code>-long</code></p>
<dl>
<dt>
<dd> (Display option) Display entire ClassAds (same as <code>-verbose</code> ).</p>
<dt>
<dd></dl>
<p> <code>-sort </code> <i>expr</i></p>
<dl>
<dt>
<dd> (Display option) Change the display order to be based on ascending values of an evaluated expression given by <i>expr</i> . Evaluated expressions of a string type are in a case insensitive alphabetical order. If multiple <code>-sort</code> arguments appear on the command line, the primary sort will be on the leftmost one within the command line, and it is numbered 0. A secondary sort will be based on the second expression, and it is numbered 1. For informational or debugging purposes, the ClassAd output to be displayed will appear as if the ClassAd had two additional attributes. CondorStatusSortKeyExpr&lt;N&gt; is the expression, where &lt;N&gt; is replaced by the number of the sort. CondorStatusSortKey&lt;N&gt; gives the result of evaluating the sort expression that is numbered &lt;N&gt; .</p>
<dt>
<dd></dl>
<p> <code>-total</code></p>
<dl>
<dt>
<dd> (Display option) Display totals only.</p>
<dt>
<dd></dl>
<p> <code>-verbose</code></p>
<dl>
<dt>
<dd> (Display option) Display entire ClassAds. Implies that totals will not be displayed.</p>
<dt>
<dd></dl>
<p> <code>-xml</code></p>
<dl>
<dt>
<dd> (Display option) Display entire ClassAds, in XML format. The XML format is fully defined in the reference manual, obtained from the ClassAds web page, with a link at <a rel="nofollow" href="http://research.cs.wisc.edu/htcondor/research.html.">http://research.cs.wisc.edu/htcondor/research.html.</a></p>
<dt>
<dd></dl>
<p> <code>-constraint </code> <i>const</i></p>
<dl>
<dt>
<dd> (Custom option) Add constraint expression.</p>
<dt>
<dd></dl>
<p> <code>-format </code> <i>fmt attr</i></p>
<dl>
<dt>
<dd> (Custom option) Display attribute or expression <i>attr</i> in format <i>fmt</i> . To display the attribute or expression the format must contain a single <a href="/docs/linux/man/3-printf/">printf</a>(3) -style conversion specifier. Attributes must be from the resource ClassAd. Expressions are ClassAd expressions and may refer to attributes in the resource ClassAd. If the attribute is not present in a given ClassAd and cannot be parsed as an expression, then the format option will be silently skipped. %r prints the unevaluated, or raw values. The conversion specifier must match the type of the attribute or expression. %s is suitable for strings such as Name , %d for integers such as LastHeardFrom , and %f for floating point numbers such as LoadAvg . %v identifies the type of the attribute, and then prints the value in an appropriate format. %V identifies the type of the attribute, and then prints the value in an appropriate format as it would appear in the <code>-long</code> format. As an example, strings used with %V will have quote marks. An incorrect format will result in undefined behavior. Do not use more than one conversion specifier in a given format. More than one conversion specifier will result in undefined behavior. To output multiple attributes repeat the <code>-format</code> option once for each desired attribute. Like <a href="/docs/linux/man/3-printf/">printf</a>(3) -style formats, one may include other text that will be reproduced directly. A format without any conversion specifiers may be specified, but an attribute is still required. Include n to specify a line break.</p>
<dt>
<dd></dl>
<p> <code>-autoformat[:rtn,lVh] </code> <i>attr1 [attr2 &#8230;]</i></p>
<dl>
<dt>
<dd> (Custom option) Display machine ClassAd attribute values formatted in a default way according to their attribute types. This option takes an arbitrary number of attribute names as arguments, and prints out their values. It is like the <code>-format</code> option, but no format strings are required. It is assumed that no attribute names begin with a dash character, so that the next word that begins with dash is the start of the next option. The <code>autoformat</code> option may be followed by a colon character and formatting qualifiers:</p>
<dt>
<dd> <code>r</code> print unevaluated, or raw values,</p>
<dt>
<dd> <code>t</code> add a tab character before each field instead of the default space character,</p>
<dt>
<dd> <code>n</code> add a newline character after each field,</p>
<dt>
<dd> <code>,</code> add a comma character after each field,</p>
<dt>
<dd> <code>l</code> label each field,</p>
<dt>
<dd> <code>V</code> use %V rather than %v for formatting,</p>
<dt>
<dd> <code>h</code> print headings before the first line of output.</p>
<dt>
<dd> The newline and comma characters may <i>not</i> be used together.</p>
<dt>
<dd></dl>
<p> <code>-target </code> <i>filename</i></p>
<dl>
<dt>
<dd> (Custom option) Where evaluation requires a target ClassAd to evaluate against, file <i>filename</i> contains the target ClassAd.</p>
<dt>
<dd></dl>
<h2>General Remarks</h2>
<dl>
<dt>
<dd> * The default output from <i>condor_status</i> is formatted to be human readable, not script readable. In an effort to make the output fit within 80 characters, values in some fields might be truncated. Furthermore, the HTCondor Project can (and does) change the formatting of this default output as we see fit. Therefore, any script that is attempting to parse data from <i>condor_status</i> is strongly encouraged to use the <code>-format</code> option (described above).</p>
<dt>
<dd>
<dt>
<dd> * The information obtained from <i>condor_startd</i> and <i>condor_schedd</i> daemons may sometimes appear to be inconsistent. This is normal since <i>condor_startd</i> and <i>condor_schedd</i> daemons update the HTCondor manager at different rates, and since there is a delay as information propagates through the network and the system.</p>
<dt>
<dd>
<dt>
<dd> * Note that the ActivityTime in the Idle state is <i>not</i> the amount of time that the machine has been idle. See the section on <i>condor_startd</i> states in the <i>Administrator&#8217;s Manual</i> for more information.</p>
<dt>
<dd>
<dt>
<dd> * When using <i>condor_status</i> on a pool with SMP machines, you can either provide the host name, in which case you will get back information about all slots that are represented on that host, or you can list specific slots by name. See the examples below for details.</p>
<dt>
<dd>
<dt>
<dd> * If you specify host names, without domains, HTCondor will automatically try to resolve those host names into fully qualified host names for you. This also works when specifying specific nodes of an SMP machine. In this case, everything after the &#8220;@&#8221; sign is treated as a host name and that is what is resolved.</p>
<dt>
<dd>
<dt>
<dd> * You can use the <code>-direct</code> option in conjunction with almost any other set of options. However, at this time, the only daemon that will allow direct queries for its ad(s) is the <i>condor_startd</i> . So, the only options currently not supported with <code>-direct</code> are <code>-schedd</code> and <code>-master</code> . Most other options use startd ads for their information, so they work seamlessly with <code>-direct</code> . The only other restriction on <code>-direct</code> is that you may only use 1 <code>-direct</code> option at a time. If you want to query information directly from multiple hosts, you must run <i>condor_status</i> multiple times.</p>
<dt>
<dd>
<dt>
<dd> * Unless you use the local host name with <code>-direct</code> , <i>condor_status</i> will still have to contact a collector to find the address where the specified daemon is listening. So, using a <code>-pool</code> option in conjunction with <code>-direct</code> just tells <i>condor_status</i> which collector to query to find the address of the daemon you want. The information actually displayed will still be retrieved directly from the daemon you specified as the argument to <code>-direct</code> .</p>
<dt>
<dd></dl>
<h2>Examples</h2>
<p> <i>Example 1</i> To view information from all nodes of an SMP machine, use only the host name. For example, if you had a 4-CPU machine, named vulture.cs.wisc.edu , you might see </p>
<p> % condor_status vulture </p>
<p> Name OpSys Arch State Activity LoadAv Mem ActvtyTime </p>
<p> slot1 [at] vulture.cs.w LINUX INTEL Claimed Busy 1.050 512 0+01:47:42<br />
 slot2 [at] vulture.cs.w LINUX INTEL Claimed Busy 1.000 512 0+01:48:19<br />
 slot3 [at] vulture.cs.w LINUX INTEL Unclaimed Idle 0.070 512 1+11:05:32<br />
 slot4 [at] vulture.cs.w LINUX INTEL Unclaimed Idle 0.000 512 1+11:05:34 </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Total Owner Claimed Unclaimed Matched Preempting Backfill </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>INTEL/LINUX&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>4&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>2&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>2&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0 </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Total&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>4&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>2&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>2&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0 </p>
<p> <i>Example 2</i> To view information from a specific nodes of an SMP machine, specify the node directly. You do this by providing the name of the slot. This has the form slot#@hostname . For example: </p>
<p> % condor_status slot3 [at] vulture </p>
<p> Name OpSys Arch State Activity LoadAv Mem ActvtyTime </p>
<p> slot3 [at] vulture.cs.w LINUX INTEL Unclaimed Idle 0.070 512 1+11:10:32 </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Total Owner Claimed Unclaimed Matched Preempting Backfill </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>INTEL/LINUX&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0 </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Total&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0 </p>
<p> <i>Constraint option examples</i> </p>
<p> The Unix command to use the constraint option to see all machines with the OpSys of &quot;LINUX&quot; : </p>
<p> % condor_status -constraint OpSys==\&quot;LINUX\&quot; </p>
<p> Note that quotation marks must be escaped with the backslash characters for most shells. </p>
<p> The Windows command to do the same thing: </p>
<p> &gt;condor_status -constraint &quot; OpSys==&quot;&quot;LINUX&quot;&quot; &quot; </p>
<p> Note that quotation marks are used to delimit the single argument which is the expression, and the quotation marks that identify the string must be escaped by using a set of two double quote marks without any intervening spaces. </p>
<p> To see all machines that are currently in the Idle state, the Unix command is </p>
<p> % condor_status -constraint State==\&quot;Idle\&quot; </p>
<p> To see all machines that are bench marked to have a MIPS rating of more than 750, the Unix command is </p>
<p> % condor_status -constraint &#8216;Mips&gt;750&#8217; </p>
<p> <i>-cod option example</i> </p>
<p> The <code>-cod</code> option displays the status of COD claims within a given HTCondor pool. </p>
<p> Name ID ClaimState TimeInState RemoteUser JobId Keyword<br />
 astro.cs.wi COD1 Idle 0+00:00:04 wright<br />
 chopin.cs.w COD1 Running 0+00:02:05 wright 3.0 fractgen<br />
 chopin.cs.w COD2 Suspended 0+00:10:21 wright 4.0 fractgen </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Total&nbsp;<wbr>&nbsp;<wbr>Idle&nbsp;<wbr>&nbsp;<wbr>Running&nbsp;<wbr>&nbsp;<wbr>Suspended&nbsp;<wbr>&nbsp;<wbr>Vacating&nbsp;<wbr>&nbsp;<wbr>Killing </p>
<p>&nbsp;<wbr>INTEL/LINUX&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>3&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0 </p>
<p>&nbsp;<wbr>Total&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>3&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0 </p>
<p> <i>-format option example</i> To display the name and memory attributes of each job ClassAd in a format that is easily parsable by other tools: </p>
<p> % condor_status -format &quot;%s &quot; Name -format &quot;%d
&quot; Memory </p>
<p> To do the same with the <code>autoformat</code> option, run </p>
<p> % condor_status -autoformat Name Memory </p>
<h2>Exit Status</h2>
<p> <i>condor_status</i> will exit with a status value of 0 (zero) upon success, and it will exit with the value 1 (one) upon failure. </p>
<h2>Author</h2>
<p> Center for High Throughput Computing, University of Wisconsin-Madison</p>
<h2>Copyright</h2>
<p> Copyright (C) 1990-2015 Center for High Throughput Computing, Computer Sciences Department, University of Wisconsin-Madison, Madison, WI. All Rights Reserved. Licensed under the Apache License, Version 2.0. </p>
<h2>Index</h2>
