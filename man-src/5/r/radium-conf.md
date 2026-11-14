---
title: "radium-conf(5)"
name: "radium-conf"
section: "5"
letter: "r"
url: "/docs/linux/man/5-radium-conf/"
description: "radium.conf – radium resource file."
---

<p><code>radium.conf</code> &#8211; <code>radium</code> resource file.</p>
<h2>Synopsis</h2>
<p><code>radium.conf</code></p>
<h2>Description</h2>
<p>Radium will open this radium.conf if its installed as /etc/radium.conf. It will also search for this file as radium.conf in directories specified in $RADIUMPATH, or $RADIUMHOME, $RADIUMHOME/lib, or $HOME, $HOME/lib, and parse it to set common configuration options. All values in this file can be overriden by command line options, or other files of this format that can be read in using the -F option. </p>
<h2>Variable Syntax</h2>
<p>Variable assignments must be of the form: </p>
<pre> VARIABLE=</pre>
<p>with no white space between the VARIABLE and the &#8216;=&#8217; sign. Quotes are optional for string arguments, but if you want to embed comments, then quotes are required.</p>
<h2>Radium_Daemon</h2>
<p>Radium is capable of running as a daemon, doing all the right things that daemons do. When this configuration is used for the system daemon process, say for /etc/radium.conf, this variable should be set to &quot;yes&quot;. </p>
<p> The default value is to not run as a daemon. </p>
<p> This example is to support the ./support/Startup/radium script which requires that this variable be set to &quot;yes&quot;. </p>
<p> Commandline equivalent -d </p>
<p> <code>RADIUM_DAEMON=</code>no</p>
<h2>Radium_Monitor_Id</h2>
<p>Radium Monitor Data is uniquely identifiable based on the source identifier that is included in each output record. This is to allow you to work with Argus Data from multiple monitors at the same time. The ID is 32 bits long, and supports a number of formats as legitimate values. Radium supports unsigned ints, IPv4 addresses and 4 bytes strings, as values. </p>
<p> The formats are discerned from the values provided. Double-quoted values are treated as strings, and are truncated to 4 characters. Non-quoted values are tested for whether they are hostnames, and if not, then they are tested wheter they are numbers. </p>
<p> The configuration allows for you to use host names, however, do have some understanding how `hostname` will be resolved by the nameserver before commiting to this strategy completely. </p>
<p> For convenience, argus supports the notion of &quot;`hostname`&quot; for assigning the probe&#8217;s id. This is to support management of large deployments, so you can have one argus.conf file that works for a lot of probes. </p>
<p> For security, argus does not rely on system programs, like hostname.1. It implements the logic of hostname itself, so don&#8217;t try to run arbitrary programs using this method, because it won&#8217;t work. </p>
<p> Commandline equivalent -e </p>
<p> <code>RADIUM_MONITOR_ID</code>=`hostname` // IPv4 address returned <code>RADIUM_MONITOR_ID</code>=10.2.45.3 // IPv4 address <code>RADIUM_MONITOR_ID</code>=2435 // Number <code>RADIUM_MONITOR_ID</code>=&quot;en0&quot; // String</p>
<h2>Radium_Argus_Server</h2>
<p>Radium can attach to any number of remote argus servers, and collect argus data in real time. The syntax for this variable is a hostname or a dot notation IP address, followed by an optional port value, separated by a &#8216;:&#8217;. If the port is not specified, the default value of 561 is used. </p>
<p> Commandline equivalent -S &lt;host[:port]&gt; </p>
<p> <code>RADIUM_ARGUS_SERVER</code>=localhost:561</p>
<h2>Radium_Cisconetflow_Port</h2>
<p>Radium can read Cicso Netflow records directly from Cisco routers. Specifying this value will alert Radium to open a UDP based socket listening for data from this name or address. </p>
<p> Commandline equivalent -C </p>
<p> <code>RADIUM_CISCONETFLOW_PORT</code>=9996</p>
<h2>Radium_User_Auth, Radium_Auth_Pass</h2>
<p>When argus is compiled with SASL support, ra* clients may be required to authenticate to the argus server before the argus will accept the connection. This variable will allow one to set the user and authorization id&#8217;s, if needed. Although not recommended you can provide a password through the RADIUM_AUTH_PASS variable. The format for this variable is: </p>
<p> Commandline equivalent -U </p>
<p> <code>RADIUM_USER_AUTH</code>=user_id/authorization_id <code>RADIUM_AUTH_PASS</code>=the_password</p>
<h2>Radium_Access_Port</h2>
<p>Radium monitors can provide a real-time remote access port for collecting Radium data. This is a TCP based port service and the default port number is tcp/561, the &quot;experimental monitor&quot; service. This feature is disabled by default, and can be forced off by setting it to zero (0). </p>
<p> When you do want to enable this service, 561 is a good choice, as all ra* clients are configured to try this port by default. </p>
<p> Commandline equivalent -P </p>
<p> <code>RADIUM_ACCESS_PORT=</code>561</p>
<h2>Radium_Bind_Ip</h2>
<p>When remote access is enabled (see above), you can specify that Radium should bind only to a specific IP address. This is useful, for example, in restricting access to the local host, or binding to a private interface while capturing from another. The default is to bind to any IP address. </p>
<p> Commandline equivalent -B </p>
<p> <code>RADIUM_BIND_IP=</code>&quot;127.0.0.1&quot;</p>
<h2>Radium_Output_File</h2>
<p>Radium can write its output to one or a number of files, default limit is 5 concurrent files, each with their own independant filters. </p>
<p> The format is: </p>
<pre> RADIUM_OUTPUT_FILE=/full/path/file/name
 RADIUM_OUTPUT_FILE=/full/path/file/name &quot;filter&quot;</pre>
<p>Most sites will have radium write to a file, for reliablity and performance. The example file name is used here as supporting programs, such as ./support/Archive/radiumarchive are configured to use this file. </p>
<p> Commandline equivalent -w </p>
<p> <code>RADIUM_OUTPUT_FILE=</code>/var/log/radium/radium.out</p>
<h2>Radium_Set_Pid</h2>
<p>When Radium is configured to run as a daemon, with the -d option, Radium can store its pid in a file, to aid in managing the running daemon. However, creating a system pid file requires priviledges that may not be appropriate for all cases. </p>
<p> When configured to generate a pid file, if Radium cannot create the pid file, it will fail to run. This variable is available to override the default, in case this gets in your way. </p>
<p> The default value is to generate a pid. </p>
<p> No Commandline equivalent </p>
<p> <code>RADIUM_SET_PID</code>=yes </p>
<p>&nbsp;<wbr></p>
<h2>Radium_Adjust_Time</h2>
<p>Radium can correct for time synchronization problems that may exist between data sources. If configured to do so, radium will adjust all the timestamps in records by the calculated drift between radium and its many data sources. Records whose timevalues have been &#8216;corrected&#8217; are marked so that subsequent readers can differentiate between true primitive time and modified time. </p>
<p> Commandline equivalent -T<br />
&nbsp;<wbr> <code>RADIUM_ADJUST_TIME=</code>no</p>
<h2>Radium_Mar_Status_Interval</h2>
<p>Radium will periodically report on a its own health, providing interface status, total packet and bytes counts, packet drop rates, and flow oriented statistics. </p>
<p> These records can be used as &quot;keep alives&quot; for periods when there is no network traffic to be monitored. </p>
<p> The default value is 300 seconds, but a value of 60 seconds is very common. </p>
<p> Commandline equivalent -M </p>
<p> <code>RADIUM_MAR_STATUS_INTERVAL</code>=60</p>
<h2>Radium_Debug_Level</h2>
<p>If compiled to support this option, Radium is capable of generating a lot of debug information. </p>
<p> The default value is zero (0). </p>
<p> Commandline equivalent -D </p>
<p> <code>RADIUM_DEBUG_LEVEL=</code>0</p>
<h2>Radium_Filter_Optimizer</h2>
<p>Radium uses the packet filter capabilities of libpcap. If there is a need to not use the libpcap filter optimizer, you can turn it off here. The default is to leave it on. </p>
<p> Commandline equivalent -O </p>
<p> <code>RADIUM_FILTER_OPTIMIZER=</code>yes</p>
<h2>Radium_Filter</h2>
<p>You can provide a filter expression here, if you like. It should be limited to 2K in length. The default is to not filter. </p>
<p> No Commandline equivalent </p>
<p> <code>RADIUM_FILTER=</code>&quot;&quot;</p>
<h2>Radium_Chroot_Dir</h2>
<p>Radium supports <a href="/docs/linux/man/2-chroot/">chroot</a>(2) in order to control the file system that radium exists in and can access. Generally used when radium is running with privleges, this limits the negative impacts that radium could inflict on its host machine. </p>
<p> This option will cause the output file names to be relative to this directory, and so consider this when trying to find your output files. </p>
<p> Commandline equivalent -C </p>
<p> <code>RADIUM_CHROOT_DIR=</code>&quot;&quot;<br />
&nbsp;<wbr><br />
&nbsp;<wbr></p>
<h2>Radium_Setuser_Id</h2>
<p>Radium can be directed to change its user id using the setuid() system call. This is can used when radium is started as root, in order to access privleged resources, but then after the resources are opened, this directive will cause radium to change its user id value to a &#8216;lesser&#8217; capable account. Recommended when radium is running as a daemon. </p>
<p> Commandline equivalent -u </p>
<p> <code>RADIUM_SETUSER_ID=</code>&quot;user&quot;<br />
&nbsp;<wbr></p>
<h2>Radium_Setgroup_Id</h2>
<p>&nbsp;<wbr> Radium can be directed to change its group id using the setgid() system call. This is can used when radium is started as root, in order to access privleged resources, but then after the resources are opened, this directive can be used to change argu&#8217;s group id value to a &#8216;lesser&#8217; capable account. Recommended when radium is running as a daemon. </p>
<p> Commandline equivalent -g </p>
<p> <code>RADIUM_SETGROUP_ID=</code>&quot;group&quot;</p>
<h2>Radium_Classifier_File</h2>
<p>Radium can be used to label records as they are distributed. This can be used to classify flow records, or simply to mark them for post processing purposes. </p>
<p> When provided with a ralabel.conf formatted file, radium will label all matching records. </p>
<p> Commandline equivalent none </p>
<p> <code>RADIUM_CLASSIFIER_FILE</code>=/usr/local/argus/ralabel.conf</p>
<h2>Radium_Correlate</h2>
<p>Radium has a correlation function, where flow data from multiple source&#8217;s can be compared and &#8216;correlateda. </p>
<p> This function is enabled with a single radium configuration keyword RADIUM_CORRELATE=&quot;yes&quot;. With this variable set, radium(). will buffer incoming data to generate delay, and will correlate data from multiple sources with an event window of about 3 seconds. Data that is matchable, which means that it has the same flow identifiers, or the same hints, will treated as if they were &quot;observed&quot; by multiple probes, and merged. </p>
<p>&nbsp;<wbr>Commandline equivalent&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>none </p>
<p> <code>RADIUM_CORRELATE=</code>&quot;no&quot;</p>
<h2>Copyright</h2>
<p>Copyright (c) 2000-2016 QoSient All rights reserved.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-radium/">radium</a></code>(8) </p>
