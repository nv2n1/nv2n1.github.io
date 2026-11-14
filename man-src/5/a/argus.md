---
title: "argus(5)"
name: "argus"
section: "5"
letter: "a"
url: "/docs/linux/man/5-argus/"
description: "argus.conf – argus resource file."
---

<p><code>argus.conf</code> &#8211; <code>argus</code> resource file.</p>
<h2>Synopsis</h2>
<p><code>argus.conf</code></p>
<h2>Copyright</h2>
<p>Copyright (c) 2000-2004 QoSient. All rights reserved.</p>
<h2>Description</h2>
<p>Argus will open this argus.conf if its installed as /etc/argus.conf. It will also search for this file as argus.conf in directories specified in $ARGUSPATH, or $ARGUSHOME, $ARGUSHOME/lib, or $HOME, $HOME/lib, and parse it to set common configuration options. All values in this file can be overriden by command line options, or other files of this format that can be read in using the -F option. </p>
<h2>Variable Syntax</h2>
<p>Variable assignments must be of the form: </p>
<pre> VARIABLE=</pre>
<p>with no white space between the VARIABLE and the &#8216;=&#8217; sign. Quotes are optional for string arguments, but if you want to embed comments, then quotes are required.</p>
<h2>Argus_Daemon</h2>
<p>Argus is capable of running as a daemon, doing all the right things that daemons do. When this configuration is used for the system daemon process, say for /etc/argus.conf, this variable should be set to &quot;yes&quot;. </p>
<p> The default value is to not run as a daemon. </p>
<p> This example is to support the ./support/Startup/argus script which requires that this variable be set to &quot;yes&quot;. </p>
<p> Commandline equivalent -d </p>
<p> <code>ARGUS_DAEMON=</code>yes</p>
<h2>Argus_Monitor_Id</h2>
<p>Argus Monitor Data is uniquely identifiable based on the source identifier that is included in each output record. This is to allow you to work with Argus Data from multiple monitors at the same time. The ID is 32 bits long, and so legitimate values are 0 &#8211; 4294967296 but argus also supports IP addresses as values. The configuration allows for you to use host names, however, do have some understanding how `hostname` will be resolved by the nameserver before commiting to this strategy completely. </p>
<p> Commandline equivalent -e </p>
<p> <code>ARGUS_MONITOR_ID</code>=`hostname`<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></p>
<h2>Argus_Access_Port</h2>
<p>Argus monitors can provide a real-time remote access port for collecting Argus data. This is a TCP based port service and the default port number is tcp/561, the &quot;experimental monitor&quot; service. This feature is disabled by default, and can be forced off by setting it to zero (0). </p>
<p> When you do want to enable this service, 561 is a good choice, as all ra* clients are configured to try this port by default. </p>
<p> Commandline equivalent -P </p>
<p> <code>ARGUS_ACCESS_PORT=</code>561</p>
<h2>Argus_Bind_Ip</h2>
<p>When remote access is enabled (see above), you can specify that Argus should bind only to a specific IP address. This is useful, for example, in restricting access to the local host, or binding to a private interface while capturing from another. The default is to bind to any IP address. </p>
<p> Commandline equivalent -B </p>
<p> <code>ARGUS_BIND_IP=</code>&quot;127.0.0.1&quot;</p>
<h2>Argus_Interface</h2>
<p>By default, Argus will open the first appropriate interface on a system that it encounters. For systems that have only one network interface, this is a reasonable thing to do. But, when there are more than one suitable interface, you should specify which interface(s) Argus should read data from. </p>
<p> Argus can read packets from multiple interfaces at the same time, although this is limited to 2 interfaces at this time. Specify this in this file with multiple ARGUS_INTERFACE directives. </p>
<p> Commandline equivalent -i </p>
<p> <code>ARGUS_INTERFACE=</code>le0</p>
<h2>Argus_Output_File</h2>
<p>Argus can write its output to one or a number of files, default limit is 5 concurrent files, each with their own independant filters. </p>
<p> The format is: </p>
<pre> ARGUS_OUTPUT_FILE=/full/path/file/name
 ARGUS_OUTPUT_FILE=/full/path/file/name &quot;filter&quot;</pre>
<p>Most sites will have argus write to a file, for reliablity and performance. The example file name is used here as supporting programs, such as ./support/Archive/argusarchive are configured to use this file. </p>
<p> Commandline equivalent -w </p>
<p> <code>ARGUS_OUTPUT_FILE=</code>/var/log/argus/argus.out</p>
<h2>Argus_Max_Instances</h2>
<p>There can be any number of Argus Monitors running on a single system. While this is a blessing for some, this does cause some confusion in traditonal system administration tasks, such as pid file creation and failure recover methods. If you plan on having a more than one argus daemon running on your system, say, monitoring different interfaces, then set this variable to the number of daemons you expect to support. </p>
<p> Commandline equivalent -I </p>
<p> <code>ARGUS_MAX_INSTANCES=</code>1<br />
&nbsp;<wbr><br />
&nbsp;<wbr></p>
<h2>Argus_Set_Pid</h2>
<p>When Argus is configured to run as a daemon, with the -d option, Argus can store its pid in a file, to aid in managing the running daemon. Creating a system pid file requires priviledges that may not be appropriate for all cases. To assist in managing pid file creation and support, argus </p>
<p> When configured to generate a pid file, if Argus cannot create the pid file, it will fail to run. This variable is available to override the default, in case this gets in your way. </p>
<p> The default value is to generate a pid in /var/run if it exists, and if not in $ARGUSHOME. </p>
<p> Commandline equivalent -c </p>
<p>&nbsp;<wbr> <code>ARGUS_SET_PID=</code>yes</p>
<h2>Argus_Pid_Filename</h2>
<p>Argus has a mechanism for generating pid filenames, but in some circumstances, being able to specify the pid filename is required due to permission restriction or just out of convenience. If this file exists, argus will read the pid that the file contains, and test if that process is running. If not, the old pid is replaced, and argus continues to run. </p>
<p> When this variable is set, argus assumes &quot;-I 1&quot; and &quot;-c&quot;. </p>
<p> Commandline equivalent -n &lt;pid file&gt;<br />
&nbsp;<wbr>&nbsp;<wbr> </p>
<p> <code>ARGUS_PID_FILENAME</code>=/var/run/argus.pid<br />
&nbsp;<wbr></p>
<h2>Argus_Go_Promiscuous</h2>
<p>By default, Argus will put its interface in promiscuous mode in order to monitor all the traffic that can be collected. This can put an undo load on systems. </p>
<p> If the intent is to monitor only the network activity of the specific system, say to measure the performance of an HTTP service or DNS service, you&#8217;ll want to turn promiscuous mode off. </p>
<p> The default value is go into prmiscuous mode. </p>
<p> Commandline equivalent -p </p>
<p> <code>ARGUS_GO_PROMISCUOUS=</code>yes</p>
<h2>Argus_Flow_Status_Interval</h2>
<p>Argus will periodically report on a flow&#8217;s activity every ARGUS_FLOW_STATUS_INTERVAL seconds, as long as there is new activity on the flow. This is so that you can get a view into the activity of very long lived flows. The default is 60 seconds, but this number may be too low or too high depending on your uses. </p>
<p> The default value is 60 seconds, but argus does support a minimum value of 1. This is very useful for doing measurements in a controlled experimental environment where the number of flows is &lt; 1000. </p>
<p> Commandline equivalent -S </p>
<p> <code>ARGUS_FLOW_STATUS_INTERVAL=</code>60</p>
<h2>Argus_Mar_Status_Interval</h2>
<p>Argus will periodically report on a its own health, providing interface status, total packet and bytes counts, packet drop rates, and flow oriented statistics. </p>
<p> These records can be used as &quot;keep alives&quot; for periods when there is no network traffic to be monitored. </p>
<p> The default value is 300 seconds, but a value of 60 seconds is very common. </p>
<p> Commandline equivalent -M </p>
<p> <code>ARGUS_MAR_STATUS_INTERVAL=</code>300</p>
<h2>Argus_Debug_Level</h2>
<p>If compiled to support this option, Argus is capable of generating a lot of debug information. </p>
<p> The default value is zero (0). </p>
<p> Commandline equivalent -D </p>
<p> <code>ARGUS_DEBUG_LEVEL=</code>0</p>
<h2>Argus_Generate_Response_Time_Data</h2>
<p>Argus can be configured to report on flows in a manner than provides the best information for calculating application reponse times and network round trip times. </p>
<p> The default value is to not generate this data. </p>
<p> Commandline equivalent -R </p>
<p>&nbsp;<wbr> <code>ARGUS_GENERATE_RESPONSE_TIME_DATA=</code>no</p>
<h2>Argus_Generate_Jitter_Data</h2>
<p>Argus can be configured to generate packet jitter information on a per flow basis. The default value is to not generate this data. </p>
<p> Commandline equivalent -J </p>
<p>&nbsp;<wbr> <code>ARGUS_GENERATE_JITTER_DATA=</code>no</p>
<h2>Argus_Generate_Mac_Data</h2>
<p>Argus can be configured to not provide MAC addresses in it audit data. This is available if MAC address tracking and audit is not a requirement. </p>
<p> The default value is to not generate this data. </p>
<p> Commandline equivalent -m </p>
<p>&nbsp;<wbr> <code>ARGUS_GENERATE_MAC_DATA=</code>no</p>
<h2>Argus_Capture_Data_Len</h2>
<p>Argus can be configured to capture a number of user data bytes from the packet stream. </p>
<p> The default value is to not generate this data. </p>
<p> Commandline equivalent -U </p>
<p>&nbsp;<wbr> <code>ARGUS_CAPTURE_DATA_LEN=</code>0</p>
<h2>Argus_Filter_Optimizer</h2>
<p>Argus uses the packet filter capabilities of libpcap. If there is a need to not use the libpcap filter optimizer, you can turn it off here. The default is to leave it on. </p>
<p> Commandline equivalent -O </p>
<p> <code>ARGUS_FILTER_OPTIMIZER=</code>yes</p>
<h2>Argus_Filter</h2>
<p>You can provide a filter expression here, if you like. It should be limited to 2K in length. The default is to not filter. </p>
<p> No Commandline equivalent </p>
<p> <code>ARGUS_FILTER=</code>&quot;&quot;</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-argus/">argus</a></code>(8) </p>
