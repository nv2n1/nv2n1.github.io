---
title: "snmpdelta(1)"
name: "snmpdelta"
section: "1"
letter: "s"
url: "/docs/linux/man/1-snmpdelta/"
description: "snmpdelta – Monitor delta differences in SNMP Counter values"
---

<h2>NAME</h2>
<p> snmpdelta &#8211; Monitor delta differences in SNMP Counter values</p>
<h2>SYNOPSIS</h2>
<p> <code>snmpdelta</code> [ COMMON OPTIONS ] [-Cf] [ -Ct ] [ -Cs ] [ -CS ] [ -Cm ] [ -CF configfile ] [ -Cl ] [ -Cp period ] [ -CP Peaks ] [ -Ck ] [ -CT ] AGENT OID [ OID &#8230; ]</p>
<h2>DESCRIPTION</h2>
<p> <code>snmpdelta</code> will monitor the specified integer valued OIDs, and report changes over time. </p>
<p> AGENT identifies a target SNMP agent, which is instrumented to monitor the given objects. At its simplest, the AGENT specification will consist of a hostname or an IPv4 address. In this situation, the command will attempt communication with the agent, using UDP/IPv4 to port 161 of the given target host. See <a href="/docs/linux/man/1-snmpcmd/">snmpcmd</a>(1) for a full list of the possible formats for AGENT. </p>
<p> OID is an object identifier which uniquely identifies the object type within a MIB. Multiple OIDs can be specified on a single snmpdelta command. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>COMMON OPTIONS</code></p>
<dd> Please see <i><a href="/docs/linux/man/1-snmpcmd/">snmpcmd</a>(1)</i> for a list of possible values for COMMON OPTIONS as well as their descriptions.</p>
<dt><code>-Cf</code></p>
<dd> Don&#8217;t fix errors and retry the request. Without this option, if multiple oids have been specified for a single request and if the request for one or more of the oids fails, snmpdelta will retry the request so that data for oids apart from the ones that failed will still be returned. Specifying -Cf tells <i>snmpdelta</i> not to retry a request, even if there are multiple oids specified.</p>
<dt><code>-Ct</code></p>
<dd> Flag will determine time interval from the monitored entity.</p>
<dt><code>-Cs</code></p>
<dd> Flag will display a timestamp.</p>
<dt><code>-CS</code></p>
<dd> Generates a &quot;sum count&quot; in addition to the individual instance counts. The &quot;sum count&quot; is the total of all the individual deltas for each time period.</p>
<dt><code>-Cm</code></p>
<dd> Prints the max value ever attained.</p>
<dt><code>-CF configfile</code></p>
<dd> Tells <code>snmpdelta</code> to read it&#8217;s configuration from the specified file. This options allows the input to be set up in advance rather than having to be specified on the command line.</p>
<dt><code>-Cl</code></p>
<dd> Tells <code>snmpdelta</code> to write it&#8217;s configuration to files whose names correspond to the MIB instances monitored. For example, snmpdelta -Cl localhost ifInOctets.1 will create a file &quot;localhost-ifInOctets.1&quot;.</p>
<dt><code>-Cp</code></p>
<dd> Specifies the number of seconds between polling periods. Polling constitutes sending a request to the agent. The default polling period is one second.</p>
<dt><code>-CP peaks</code></p>
<dd> Specifies the reporting period in number of polling periods. If this option is specified, snmpdelta polls the agent <i>peaks</i> number of times before reporting the results. The result reported includes the average value over the reporting period. In addition, the highest polled value within the reporting period is shown.</p>
<dt><code>-Ck</code></p>
<dd> When the polling period (-Cp) is an increment of 60 seconds and the timestamp is displayed in the output (-Cs), then the default display shows the timestamp in the format hh:mm mm/dd. This option causes the timestamp format to be hh:mm:ss mm/dd.</p>
<dt><code>-CT</code></p>
<dd> Makes <code>snmpdelta</code> print its output in tabular form.</p>
<dt><code>-Cv vars/pkt</code></p>
<dd> Specifies the maximum number of oids allowed to be packaged in a single PDU. Multiple PDUs can be created in a single request. The default value of variables per packet is 60. This option is useful if a request response results in an error becaues the packet is too big.</dl>
<p> Note that <code>snmpdelta</code> REQUIRES an argument specifying the agent to query and at least one OID argument, as described in the <i><a href="/docs/linux/man/1-snmpcmd/">snmpcmd</a>(1)</i> manual page.</p>
<h2>EXAMPLES</h2>
<pre><code>
$ snmpdelta - c public - v 1 - Cs localhost IF - MIB::ifInUcastPkts .3 IF - MIB::ifOutUcastPkts .3 [20:
                                                                                                    15:43 6 / 14] ifInUcastPkts .3 /
                                                                                1 sec : 158 [20:
                                                                                             15:43 6 / 14] ifOutUcastPkts .3 /
                                                                                1 sec : 158 [20:
                                                                                             15:44 6 / 14] ifInUcastPkts .3 /
                                                                                1 sec : 184 [20:
                                                                                             15:44 6 / 14] ifOutUcastPkts .3 /
                                                                                1 sec : 184 [20:
                                                                                             15:45 6 / 14] ifInUcastPkts .3 /
                                                                                1 sec : 184 [20:
                                                                                             15:45 6 / 14] ifOutUcastPkts .3 /
                                                                                1 sec : 184 [20:
                                                                                             15:46 6 / 14] ifInUcastPkts .3 /
                                                                                1 sec : 158 [20:
                                                                                             15:46 6 / 14] ifOutUcastPkts .3 /
                                                                                1 sec : 158 [20:
                                                                                             15:47 6 / 14] ifInUcastPkts .3 /
                                                                                1 sec : 184 [20:
                                                                                             15:47 6 / 14] ifOutUcastPkts .3 /
                                                                                1 sec : 184 [20:
                                                                                             15:48 6 / 14] ifInUcastPkts .3 /
                                                                                1 sec : 184 [20:
                                                                                             15:48 6 / 14] ifOutUcastPkts .3 /
                                                                                1 sec : 184 [20:
                                                                                             15:49 6 / 14] ifInUcastPkts .3 /
                                                                                1 sec : 158 [20:
                                                                                             15:49 6 / 14] ifOutUcastPkts .3 /
                                                                                1 sec : 158 ^
    C
            $ snmpdelta -
        c public - v 1 - Cs - CT localhost IF - MIB : ifInUcastPkts .3 IF - MIB : ifOutcastPkts .3 localhost ifInUcastPkts .3 ifOutUcastPkts .3 [20:
                                                                                                                                                 15:59 6 / 14] 184.00 184.00 [20:
                                                                                                                                                                              16:00 6 / 14] 158.00 158.00 [20:
                                                                                                                                                                                                           16:01 6 / 14] 184.00 184.00 [20:
                                                                                                                                                                                                                                        16:02 6 / 14] 184.00 184.00 [20:
                                                                                                                                                                                                                                                                     16:03 6 / 14] 158.00 158.00 [20:
                                                                                                                                                                                                                                                                                                  16:04 6 / 14] 184.00 184.00 [20:
                                                                                                                                                                                                                                                                                                                               16:05 6 / 14] 184.00 184.00 [20:
                                                                                                                                                                                                                                                                                                                                                            16:06 6 / 14] 158.00 158.00 ^
    C
</code></pre>
<p> The following example uses a number of options. Since the <i>Cl </i> option is specified, the output is sent to a file and not to the screen. </p>
<pre>
$ snmpdelta -c public -v 1 -Ct -Cs -CS -Cm -Cl -Cp 60 -CP 60
  interlink.sw.net.cmu.edu .1.3.6.1.2.1.2.2.1.16.3 .1.3.6.1.2.1.2.2.1.16.4
</pre>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-snmpcmd/">snmpcmd</a>(1), <a href="/docs/linux/man/5-variables/">variables</a>(5). </p>
<h2>Index</h2>
