---
title: "hb_report(8)"
name: "hb_report"
section: "8"
letter: "h"
url: "/docs/linux/man/8-hb_report/"
description: "hb_report – create report for CRM based clusters (Pacemaker)"
---

<p>hb_report &#8211; create report for CRM based clusters (Pacemaker)</p>
<h2>Synopsis</h2>
<p><code>hb_report</code> -f {time|&quot;cts:&quot;testnum} [-t time] [-u user] [-l file] [-n nodes] [-E files] [-p patt] [-L patt] [-e prog] [-MSDCAv] dest</p>
<h2>Description</h2>
<p>The <a href="/docs/linux/man/1-hb_report/">hb_report</a>(1) is a utility to collect all information (logs, configuration files, system information, etc) relevant to Pacemaker (CRM) over the given period of time.</p>
<h2>Options</h2>
<p>dest</p>
<dl>
<dd>The destination directory. Must be an absolute path. The resulting tarball is placed in the parent directory and contains the last directory element of this path. Typically something like /tmp/standby-failed.</dl>
<p> <code>-f</code> { time | &quot;cts:&quot;testnum }</p>
<dl>
<dd>The start time from which to collect logs. The time is in the format as used by the Date::Parse perl module. For cts tests, specify the &quot;cts:&quot; string followed by the test number. This option is required.</dl>
<p> <code>-t</code> time</p>
<dl>
<dd>The end time to which to collect logs. Defaults to now.</dl>
<p> <code>-n</code> nodes</p>
<dl>
<dd>A list of space separated hostnames (cluster members). hb_report may try to find out the set of nodes by itself, but if it runs on the loghost which, as it is usually the case, does not belong to the cluster, that may be difficult. Also, OpenAIS doesncqt contain a list of nodes and if Pacemaker is not running, there is no way to find it out automatically. This option is cummulative (i.e. use -n &quot;a b&quot; or -n a -n b).</dl>
<p> <code>-l</code> file</p>
<dl>
<dd>Log file location. If, for whatever reason, hb_report cannot find the log files, you can specify its absolute path.</dl>
<p> <code>-E</code> files</p>
<dl>
<dd>Extra log files to collect. This option is cummulative. By default, /var/log/messages are collected along with the cluster logs.</dl>
<p> <code>-M</code></p>
<dl>
<dd>Doncqt collect extra log files, but only the file containing messages from the cluster subsystems.</dl>
<p> <code>-L</code> patt</p>
<dl>
<dd>A list of regular expressions to match in log files for analysis. This option is additive (default: &quot;CRIT: ERROR:&quot;).</dl>
<p> <code>-p</code> patt</p>
<dl>
<dd>Regular expression to match variables to be sanitized (replaced by a string of asterisks). If you doncqt want information to be exposed in your report, you can specify here a set of patterns to match variables in the CIB and pengine files. stonith_host directives in ha.cf are also sanitized. Logs are not sanitized. This option is cummulative (default: &quot;passw.*&quot;).</dl>
<p> <code>-A</code></p>
<dl>
<dd>This is an OpenAIS cluster. hb_report has some heuristics to find the cluster stack, but that is not always reliable. By default, hb_report assumes that it is run on a Heartbeat cluster.</dl>
<p> <code>-u</code> user</p>
<dl>
<dd>The ssh user. hb_report will try to login to other nodes without specifying a user, then as &quot;root&quot;, and finally as &quot;hacluster&quot;. If you have another user for administration over ssh, please use this option.</dl>
<p> <code>-S</code></p>
<dl>
<dd>Single node operation. Run hb_report only on this node and doncqt try to start slave collectors on other members of the cluster. Under normal circumstances this option is not needed. Use if <a href="/docs/linux/man/1-ssh/">ssh</a>(1) does not work to other nodes.</dl>
<p> <code>-v</code></p>
<dl>
<dd>Increase verbosity. Normally used to debug unexpected behaviour.</dl>
<p> <code>-h</code></p>
<dl>
<dd>Show usage and some examples.</dl>
<p> <code>-D</code> (obsolete)</p>
<dl>
<dd>Doncqt invoke editor to fill the description text file.</dl>
<p> <code>-e</code> prog (obsolete)</p>
<dl>
<dd>Your favourite text editor. Defaults to $EDITOR, vim, vi, emacs, or nano, whichever is found first.</dl>
<p> <code>-C</code> (obsolete)</p>
<dl>
<dd>Remove the destination directory once the report has been put in a tarball.</dl>
<h2>Examples</h2>
<p>Last night during the backup there were several warnings encountered (logserver is the log host): </p>
<dl>
<dd><font SIZE="-1"> </font></p>
<pre>logserver# hb_report -f 3:00 -t 4:00 -n &quot;node1 node2&quot; /tmp/report</pre>
<p><font SIZE="+1"></dl>
<p> collects everything from all nodes from 3am to 4am last night. The files are compressed to a tarball /tmp/report.tar.bz2. </p>
<p> Just found a problem during testing: </p>
<dl>
<dd></font> </p>
<pre># note the current time
node1# date
Fri Sep 11 18:51:40 CEST 2009
node1# /etc/init.d/heartbeat start
node1# nasty-command-that-breaks-things
node1# sleep 120 #wait for the cluster to settle
node1# hb_report -f 18:51 /tmp/hb1</pre>
<p><font SIZE="+1"></dl>
<dl>
<dd></font> </p>
<pre># if hb_report can't figure out that this is openais
node1# hb_report -f 18:51 -A /tmp/hb1</pre>
<p><font SIZE="+1"></dl>
<dl>
<dd></font> </p>
<pre># if hb_report can't figure out the cluster members
node1# hb_report -f 18:51 -n &quot;node1 node2&quot; /tmp/hb1</pre>
<p><font SIZE="+1"></dl>
<p> The files are compressed to a tarball /tmp/hb1.tar.bz2. </font></p>
<h2>Interpreting Results</h2>
<p>The compressed tar archive is the final product of hb_report. This is one example of its content, for a CTS test case on a three node OpenAIS cluster: </p>
<dl>
<dd><font SIZE="-1"> </font></p>
<pre>$ ls -RF 001-Restart</pre>
<p><font SIZE="+1"></dl>
<dl>
<dd></font> </p>
<pre>001-Restart:
analysis.txt events.txt logd.cf s390vm13/ s390vm16/
description.txt ha-log.txt openais.conf s390vm14/</pre>
<p><font SIZE="+1"></dl>
<dl>
<dd></font> </p>
<pre>001-Restart/s390vm13:
STOPPED crm_verify.txt hb_uuid.txt openais.conf@ sysinfo.txt
cib.txt dlm_dump.txt logd.cf@ pengine/ sysstats.txt
cib.xml events.txt messages permissions.txt</pre>
<p><font SIZE="+1"></dl>
<dl>
<dd></font> </p>
<pre>001-Restart/s390vm13/pengine:
pe-input-738.bz2 pe-input-740.bz2 pe-warn-450.bz2
pe-input-739.bz2 pe-warn-449.bz2 pe-warn-451.bz2</pre>
<p><font SIZE="+1"></dl>
<dl>
<dd></font> </p>
<pre>001-Restart/s390vm14:
STOPPED crm_verify.txt hb_uuid.txt openais.conf@ sysstats.txt
cib.txt dlm_dump.txt logd.cf@ permissions.txt
cib.xml events.txt messages sysinfo.txt</pre>
<p><font SIZE="+1"></dl>
<dl>
<dd></font> </p>
<pre>001-Restart/s390vm16:
STOPPED crm_verify.txt hb_uuid.txt messages sysinfo.txt
cib.txt dlm_dump.txt hostcache openais.conf@ sysstats.txt
cib.xml events.txt logd.cf@ permissions.txt</pre>
<p><font SIZE="+1"></dl>
<p> The top directory contains information which pertains to the cluster or event as a whole. Files with exactly the same content on all nodes will also be at the top, with per-node links created (as it is in this example the case with openais.conf and logd.cf). </p>
<p> The cluster log files are named ha-log.txt regardless of the actual log file name on the system. If it is found on the loghost, then it is placed in the top directory. Files named messages are excerpts of /var/log/messages from nodes. </p>
<p> Most files are copied verbatim or they contain output of a command. For instance, cib.xml is a copy of the CIB found in /var/lib/heartbeat/crm/cib.xml. crm_verify.txt is output of the <a href="/docs/linux/man/8-crm_verify/">crm_verify</a>(8) program. </p>
<p> Some files are result of a more involved processing: </p>
<p> <code>analysis.txt</code></p>
<dl>
<dd>A set of log messages matching user defined patterns (may be provided with the -L option).</dl>
<p> <code>events.txt</code></p>
<dl>
<dd>A set of log messages matching event patterns. It should provide information about major cluster motions without unnecessary details. These patterns are devised by the cluster experts. Currently, the patterns cover membership and quorum changes, resource starts and stops, fencing (stonith) actions, and cluster starts and stops. events.txt is always generated for each node. In case the central cluster log was found, also combined for all nodes.</dl>
<p> <code>permissions.txt</code></p>
<dl>
<dd>One of the more common problem causes are file and directory permissions. hb_report looks for a set of predefined directories and checks their permissions. Any issues are reported here.</dl>
<p> <code>backtraces.txt</code></p>
<dl>
<dd>gdb generated backtrace information for cores dumped within the specified period.</dl>
<p> <code>sysinfo.txt</code></p>
<dl>
<dd>Various release information about the platform, kernel, operating system, packages, and anything else deemed to be relevant. The static part of the system.</dl>
<p> <code>sysstats.txt</code></p>
<dl>
<dd>Output of various system commands such as <a href="/docs/linux/man/1-ps/">ps</a>(1), <a href="/docs/linux/man/1-uptime/">uptime</a>(1), <a href="/docs/linux/man/8-netstat/">netstat</a>(8), and <a href="/docs/linux/man/8-ifconfig/">ifconfig</a>(8). The dynamic part of the system.</dl>
<p> description.txt should contain a user supplied description of the problem, but since it is very seldom used, it will be dropped from the future releases. </font></p>
<h2>Prerequisites</h2>
<p>ssh</p>
<dl>
<dd>It is not strictly required, but you woncqt regret having a password-less ssh. It is not too difficult to setup and will save you a lot of time. If you cancqt have it, for example because your security policy does not allow such a thing, or you just prefer menial work, then you will have to resort to the semi-manual semi-automated report generation. See below for instructions. </p>
<p> If you need to supply a password for your passphrase/login, then please use the FC-uF[] option.</dl>
<p> Times</p>
<dl>
<dd>In order to find files and messages in the given period and to parse the FC-fF[] and FC-tF[] options, FChb_reportF[] uses perl and one of the FCDate::ParseF[] or FCDate::ManipF[] perl modules. Note that you need only one of these. Furthermore, on nodes which have no logs and where you doncqt run FChb_reportF[] directly, no date parsing is necessary. In other words, if you run this on a loghost then you doncqt need these perl modules on the cluster nodes. </p>
<p> On rpm based distributions, you can find FCDate::ParseF[] in FCperl-TimeDateF[] and on Debian and its derivatives in FClibtimedate-perlF[].</dl>
<p> Core dumps</p>
<dl>
<dd>To backtrace core dumps gdb is needed and the packages with the debugging info. The debug info packages may be installed at the time the report is created. Letcqs hope that you will need this really seldom.</dl>
<h2>Times</h2>
<p>Specifying times can at times be a nuisance. That is why we have chosen to use one of the perl modules&#8212;they do allow certain freedom when talking dates. You can either read the instructions at the Date::Parse examples page. or just rely on common sense and try stuff like: </p>
<dl>
<dd><font SIZE="-1"> </font></p>
<pre>3:00 (today at 3am)
15:00 (today at 3pm)
2007/9/1 2pm (September 1st at 2pm)
Tue Sep 15 20:46:27 CEST 2009 (September 15th etc)</pre>
<p><font SIZE="+1"></dl>
<p> FChb_reportF[] will (probably) complain if it cancqt figure out what do you mean. </p>
<p> Try to delimit the event as close as possible in order to reduce the size of the report, but still leaving a minute or two around for good measure. </p>
<p> FC-fF[] is not optional. And doncqt forget to quote dates when they contain spaces. </font></p>
<h2>Should I send all this to the rest of Internet?</h2>
<p>We make an effort to remove sensitive data from the configuration (CIB, ha.cf, and transition graphs). By default, parameters starting matching <i>passw.</i><i></i><i> are replaced by a string of </i><i></i>. Use the FC-pF[] option to specify additional regular expressions to match variable names which may contain information you doncqt want to leak. For example: </p>
<dl>
<dd><font SIZE="-1"> </font></p>
<pre># hb_report -f 18:00 -p &quot;user.*&quot; -p &quot;secret.*&quot; /var/tmp/report</pre>
<p><font SIZE="+1"></dl>
<p> Logs and other files are not filtered. </font></p>
<h2>Logs</h2>
<p>It may be tricky to find syslog logs. The scheme used is to log a unique message on all nodes and then look it up in the usual syslog locations. This procedure is not foolproof, in particular if the syslog files are in a non-standard directory. We look in /var/log /var/logs /var/syslog /var/adm /var/log/ha /var/log/cluster. In case we cancqt find the logs, please supply their location: </p>
<dl>
<dd><font SIZE="-1"> </font></p>
<pre># hb_report -f 5pm -l /var/log/cluster1/ha-log -S /tmp/report_node1</pre>
<p><font SIZE="+1"></dl>
<p> If you have different log locations on different nodes, well, perhaps youcqd like to make them the same and make life easier for everybody. </p>
<p> Files starting with &quot;ha-&quot; are preferred. In case syslog sends messages to more than one file, if one of them is named ha-log or ha-debug those will be favoured to syslog or messages. </p>
<p> hb_report supports also archived logs in case the period specified extends that far in the past. The archives must reside in the same directory as the current log and their names must be prefixed with the name of the current log (syslog-1.gz or messages-20090105.bz2). </p>
<p> If there is no separate log for the cluster, possibly unrelated messages from other programs are included. We doncqt filter logs, just pick a segment for the period you specified. </font></p>
<h2>Manual Report Collection</h2>
<p>So, your ssh doesncqt work. In that case, you will have to run this procedure on all nodes. Use FC-SF[] so that we doncqt bother with ssh: </p>
<dl>
<dd><font SIZE="-1"> </font></p>
<pre># hb_report -f 5:20pm -t 5:30pm -S /tmp/report_node1</pre>
<p><font SIZE="+1"></dl>
<p> If you also have a log host which is not in the cluster, then youcqll have to copy the log to one of the nodes and tell us where it is: </p>
<dl>
<dd></font> </p>
<pre># hb_report -f 5:20pm -t 5:30pm -l /var/tmp/ha-log -S /tmp/report_node1</pre>
<p><font SIZE="+1"></dl>
<p> If you reconsider and want the ssh setup, take a look at the CTS README file for instructions. </font></p>
<h2>Operation</h2>
<p>hb_report collects files and other information in a fairly straightforward way. The most complex tasks are discovering the log file locations (if syslog is used which is the most common case) and coordinating the operation on multiple nodes. </p>
<p> The instance of hb_report running on the host where it was invoked is the master instance. Instances running on other nodes are slave instances. The master instance communicates with slave instances by ssh. There are multiple ssh invocations per run, so it is essential that the ssh works without password, i.e. with the public key authentication and authorized_keys. </p>
<p> The operation consists of three phases. Each phase must finish on all nodes before the next one can commence. The first phase consists of logging unique messages through syslog on all nodes. This is the shortest of all phases. </p>
<p> The second phase is the most involved. During this phase all local information is collected, which includes: </p>
<dl>
<dd>* logs (both current and archived if the start time is far in the past)</dl>
<dl>
<dd>* various configuration files (openais, heartbeat, logd)</dl>
<dl>
<dd>* the CIB (both as xml and as represented by the crm shell)</dl>
<dl>
<dd>* pengine inputs (if this node was the DC at any point in time over the given period)</dl>
<dl>
<dd>* system information and status</dl>
<dl>
<dd>* package information and status</dl>
<dl>
<dd>* dlm lock information</dl>
<dl>
<dd>* backtraces (if there were core dumps)</dl>
<p> The third phase is collecting information from all nodes and analyzing it. The analyzis consists of the following tasks: </p>
<dl>
<dd>* identify files equal on all nodes which may then be moved to the top directory</dl>
<dl>
<dd>* save log messages matching user defined patterns (defaults to ERRORs and CRITical conditions)</dl>
<dl>
<dd>* report if there were coredumps and by whom</dl>
<dl>
<dd>* report <a href="/docs/linux/man/8-crm_verify/">crm_verify</a>(8) results</dl>
<dl>
<dd>* save log messages matching major events to events.txt</dl>
<dl>
<dd>* in case logging is configured without loghost, node logs and events files are combined using a perl utility</dl>
<h2>Bugs</h2>
<p>Finding logs may at times be extremely difficult, depending on how weird the syslog configuration. It would be nice to ask syslog-ng developers to provide a way to find out the log destination based on facility and priority. </p>
<p> hb_report can function in a satisfactory way only if ssh works to all nodes using authorized_keys (without password). </p>
<p> There are way too many options.</p>
<h2>Author</h2>
<p>Written by Dejan Muhamedagic, &lt;dejan [at] suse.de&gt;</p>
<h2>Resources</h2>
<p>Pacemaker: <a rel="nofollow" href="http://clusterlabs.org/">http://clusterlabs.org/</a> </p>
<p> Heartbeat and other Linux HA resources: <a rel="nofollow" href="http://linux-ha.org/">http://linux-ha.org/</a> </p>
<p> OpenAIS: <a rel="nofollow" href="http://www.openais.org/">http://www.openais.org/</a></p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-date--parse/">Date::Parse</a>(3)</p>
<h2>Copying</h2>
<p>Copyright (C) 2007-2009 Dejan Muhamedagic. Free use of this software is granted under the terms of the GNU General Public License (GPL).</p>
