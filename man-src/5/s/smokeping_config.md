---
title: "smokeping_config(5)"
name: "smokeping_config"
section: "5"
letter: "s"
url: "/docs/linux/man/5-smokeping_config/"
description: "smokeping_config – Reference for the SmokePing Config File"
---

<p>smokeping_config &#8211; Reference for the SmokePing Config File</p>
<h2>Overview</h2>
<p>SmokePing takes its configuration from a single central configuration file. Its location must be hardcoded in the smokeping script and smokeping.cgi. </p>
<p> The contents of this manual is generated directly from the configuration file parser. </p>
<p> The Parser for the Configuration file is written using David Schweikers Config::Grammar module. Read all about it in Config::Grammar. </p>
<p> The Configuration file has a tree-like structure with section headings at various levels. It also contains variable assignments and tables. </p>
<p> Warning: this manual is rather long. See smokeping_examples for simple configuration examples.</p>
<h2>Reference</h2>
<h3>GENERAL SYNTAX</h3>
<p>The text below describes the general syntax of the SmokePing configuration file. It was copied from the Config::Grammar documentation. </p>
<p> &#8216;#&#8217; denotes a comment up to the end-of-line, empty lines are allowed and space at the beginning and end of lines is trimmed. </p>
<p> &#8216;\&#8217; at the end of the line marks a continued line on the next line. A single space will be inserted between the concatenated lines. </p>
<p> &#8216;@include filename&#8217; is used to include another file. </p>
<p> &#8216;@define a some value&#8217; will replace all occurences of &#8216;a&#8217; in the following text with &#8216;some value&#8217;. </p>
<p> Fields in tables that contain white space can be enclosed in either <tt>&quot;'&quot;</tt> or <tt>&quot;&quot;&quot;</tt>. Whitespace can also be escaped with <tt>&quot;\&quot;</tt>. Quotes inside quotes are allowed but must be escaped with a backslash as well.</p>
<h3>SPECIFIC SYNTAX</h3>
<p>The text below describes the specific syntax of the SmokePing configuration file.</p>
<h3>*** General *** <i>(mandatory section)</i></h3>
<p>General configuration values valid for the whole SmokePing setup. </p>
<p> The following variables can be set in this section:</p>
<dl>
<dt><code>owner</code> <i>(mandatory setting)</i></dt>
<dd>Name of the person responsible for this smokeping installation.</dd>
<dt><code>imgcache</code> <i>(mandatory setting)</i></dt>
<dd>A directory which is visible on your webserver where SmokePing can cache graphs.</dd>
<dt><code>imgurl</code> <i>(mandatory setting)</i></dt>
<dd>Either an absolute URL to the <code>imgcache</code> directory or one relative to the directory where you keep the SmokePing cgi.</dd>
<dt><code>datadir</code> <i>(mandatory setting)</i></dt>
<dd>The directory where SmokePing can keep its rrd files.</dd>
<dt><code>dyndir</code></dt>
<dd>The base directory where SmokePing keeps the files related to the DYNAMIC function. This directory must be writeable by the WWW server. It is also used for temporary storage of slave polling results by the master in the master/slave mode. </dd>
<p> If this variable is not specified, the value of <tt>&quot;datadir&quot;</tt> will be used instead.</p>
<dt><code>pagedir</code></dt>
<dd>Directory to store static representations of pages.</dd>
<dt><code>piddir</code> <i>(mandatory setting)</i></dt>
<dd>The directory where SmokePing keeps its pid when daemonised.</dd>
<dt><code>sendmail</code></dt>
<dd>Path to your sendmail binary. It will be used for sending mails in connection with the support of DYNAMIC addresses.</dd>
<dt><code>offset</code></dt>
<dd>If you run many instances of smokeping you may want to prevent them from hitting your network all at the same time. Using the offset parameter you can change the point in time when the probes are run. Offset is specified in % of total interval, or alternatively as &#8216;random&#8217;. I recommend to use &#8216;random&#8217;. Note that this does NOT influence the rrds itself, it is just a matter of when data acqusition is initiated. The default offset is &#8216;random&#8217;.</dd>
<dt><code>smokemail</code> <i>(mandatory setting)</i></dt>
<dd>Path to the mail template for DYNAMIC hosts. This mail template must contain keywords of the form <code>&lt;##</code><i>keyword</i><code>##&gt;</code>. There is a sample template included with SmokePing.</dd>
<dt><code>cgiurl</code> <i>(mandatory setting)</i></dt>
<dd>Complete URL path of the SmokePing.cgi</dd>
<dt><code>mailhost</code></dt>
<dd>Instead of using sendmail, you can specify the name of an smtp server and use perl&#8217;s Net::SMTP module to send mail (for alerts and DYNAMIC client script). Several comma separated mailhosts can be specified. SmokePing will try one after the other if one does not answer for 5 seconds.</dd>
<dt><code>snpphost</code></dt>
<dd>If you have a SNPP (Simple Network Pager Protocol) server at hand, you can have alerts sent there too. Use the syntax <code>snpp:someaddress</code> to use a snpp address in any place where you can use a mail address otherwhise.</dd>
<dt><code>contact</code> <i>(mandatory setting)</i></dt>
<dd>Mail address of the person responsible for this smokeping installation.</dd>
<dt><code>display_name</code></dt>
<dd>What should the master host be called when working in master/slave mode. This is used in the overview graph for example.</dd>
<dt><code>syslogfacility</code></dt>
<dd>The syslog facility to use, eg. local0&#8230;local7. Note: syslog logging is only used if you specify this.</dd>
<dt><code>syslogpriority</code></dt>
<dd>The syslog priority to use, eg. debug, notice or info. Default is info.</dd>
<dt><code>concurrentprobes</code></dt>
<dd>If you use multiple probes or multiple instances of the same probe and you want them to run concurrently in separate processes, set this to &#8216;yes&#8217;. This gives you the possibility to specify probe-specific step and offset parameters (see the &#8216;Probes&#8217; section) for each probe and makes the probes unable to block each other in cases of service outages. The default is &#8216;yes&#8217;, but if you for some reason want the old behaviour you can set this to &#8216;no&#8217;.</dd>
<dt><code>changeprocessnames</code></dt>
<dd>When using &#8216;concurrentprobes&#8217; (see above), this controls whether the probe subprocesses should change their argv string to indicate their probe in the process name. If set to &#8216;yes&#8217; (the default), the probe name will be appended to the process name as &#8216;[probe]&#8217;, eg. &#8216;/usr/bin/smokeping [FPing]&#8217;. If you don&#8217;t like this behaviour, set this variable to &#8216;no&#8217;. If &#8216;concurrentprobes&#8217; is not set to &#8216;yes&#8217;, this variable has no effect. </dd>
<p> Default value: changeprocessnames = yes</p>
<dt><code>tmail</code></dt>
<dd>Path to your tSmoke HTML mail template file. See the tSmoke documentation for details.</dd>
<dt><code>changecgiprogramname</code></dt>
<dd>Usually the Smokeping CGI tries to log any possible errors with an extended program name that includes the IP address of the remote client for easier debugging. If this variable is set to &#8216;no&#8217;, the program name will not be modified. The only reason you would want this is if you have a very old version of the CGI::Carp module. See the installation document for details. </dd>
<p> Default value: changecgiprogramname = yes</p>
<dt><code>linkstyle</code></dt>
<dd>How the CGI self-referring links are created. The possible values are</dd>
<dl>
<dd>
</dd><dl>
<dt>absolute</dt>
<dd>Full hostname and path derived from the &#8216;cgiurl&#8217; variable </dd>
<p> &lt;a href=&#8220;<a rel="nofollow" href="http://hostname/path/smokeping.cgi?foo=bar''">http://hostname/path/smokeping.cgi?foo=bar&#8221;</a>&gt;</p>
<dt>relative</dt>
<dd>Only the parameter part is specified </dd>
<p> &lt;a href=&#8220;?foo=bar&#8221;&gt;</p>
<dt>original</dt>
<dd>The way the links were generated before Smokeping version 2.0.4: no hostname, only the path </dd>
<p> &lt;a href=&#8220;/path/smokeping.cgi?foo=bar&#8221;&gt;</dl>
</dl>
<dl>
<dd>The default is &#8220;relative&#8221;, which hopefully works for everybody. </dd>
<p> Default value: linkstyle = relative</dl>
<dt><code>precreateperms</code></dt>
<dd>If this variable is set, the Smokeping daemon will create its directory hierarchy under &#8216;dyndir&#8217; (the CGI-writable tree) at startup with the specified directory permission bits. The value is interpreted as an octal value, eg. 775 for rwxrwxr-x etc. </dd>
<p> If unset, the directories will be created dynamically with umask 022. </p>
<p> Example: precreateperms = 2755</dl>
<h3>*** Database *** <i>(mandatory section)</i></h3>
<p>Describes the properties of the round robin database for storing the SmokePing data. Note that it is not possible to edit existing RRDs by changing the entries in the cfg file. </p>
<p> The following variables can be set in this section:</p>
<dl>
<dt><code>step</code> <i>(mandatory setting)</i></dt>
<dd>Duration of the base operation interval of SmokePing in seconds. SmokePing will venture out every <code>step</code> seconds to ping your target hosts. If &#8216;concurrent_probes&#8217; is set to &#8216;yes&#8217; (see above), this variable can be overridden by each probe. Note that the step in the RRD files is fixed when they are originally generated, and if you change the step parameter afterwards, you&#8217;ll have to delete the old RRD files or somehow convert them.</dd>
<dt><code>pings</code> <i>(mandatory setting)</i></dt>
<dd>How many pings should be sent to each target. Suggested: 20 pings. Minimum value: 3 pings. This can be overridden by each probe. Some probes (those derived from basefork.pm, ie. most except the FPing variants) will even let this be overridden target-specifically. Note that the number of pings in the RRD files is fixed when they are originally generated, and if you change this parameter afterwards, you&#8217;ll have to delete the old RRD files or somehow convert them.</dd></dl>
<p> This section also contains a table describing the setup of the SmokePing database. Below are reasonable defaults. Only change them if you know rrdtool and its workings. Each row in the table describes one RRA. </p>
<pre> # cons xff steps rows
 AVERAGE 0.5 1 1008
 AVERAGE 0.5 12 4320
 MIN 0.5 12 4320
 MAX 0.5 12 4320
 AVERAGE 0.5 144 720
 MAX 0.5 144 720
 MIN 0.5 144 720</pre>
<dl>
<dt>column 0</dt>
<dd>Consolidation method.</dd>
<dt>column 1</dt>
<dd>What part of the consolidated intervals must be known to warrant a known entry.</dd>
<dt>column 2</dt>
<dd>How many <code>steps</code> to consolidate into for each RRA entry.</dd>
<dt>column 3</dt>
<dd>How many <code>rows</code> this RRA should have.</dd></dl>
<h3>*** Presentation *** <i>(mandatory section)</i></h3>
<p>Defines how the SmokePing data should be presented. </p>
<p> The following variables can be set in this section:</p>
<dl>
<dt><code>template</code> <i>(mandatory setting)</i></dt>
<dd>The webpage template must contain keywords of the form <code>&lt;##</code><i>keyword</i><code>##&gt;</code>. There is a sample template included with SmokePing; use it as the basis for your experiments. Default template contains a pointer to the SmokePing counter and homepage. I would be glad if you would not remove this as it gives me an indication as to how widely used the tool is.</dd>
<dt><code>charset</code></dt>
<dd>By default, SmokePing assumes the &#8216;iso-8859-15&#8217; character set. If you use something else, this is the place to speak up.</dd></dl>
<p> The following sections are valid on level 1:</p>
<dl>
<dt><code>+overview</code> <i>(mandatory section)</i></dt>
<dd>The Overview section defines how the Overview graphs should look. </dd>
<p> The following variables can be set in this section:</p>
<dl>
<dd>
</dd><dl>
<dt><code>width</code> <i>(mandatory setting)</i></dt>
<dd>Width of the Overview Graphs.</dd>
<dt><code>height</code> <i>(mandatory setting)</i></dt>
<dd>Height of the Overview Graphs.</dd>
<dt><code>range</code></dt>
<dd>How much time should be depicted in the Overview graph. Time must be specified as a number followed by a letter which specifies the unit of time. Known units are: <code>s</code>econds, <code>m</code>inutes, <code>h</code>ours, <code>d</code>days, <code>w</code>eeks, <code>y</code>ears.</dd>
<dt><code>max_rtt</code></dt>
<dd>Any roundtrip time larger than this value will cropped in the overview graph</dd>
<dt><code>median_color</code></dt>
<dd>By default the median line is drawn in red. Override it here with a hex color in the format <i>rrggbb</i>. Note that if you work with slaves, the slaves medians will be drawn in the slave color in the overview graph.</dd>
<dt><code>strftime</code></dt>
<dd>Use posix strftime to format the timestamp in the left hand lower corner of the overview graph</dd></dl>
</dl>
<dl>
<dd></dd></dl>
<dt><code>+detail</code> <i>(mandatory section)</i></dt>
<dd>The following variables can be set in this section:</dd>
<dl>
<dd>
</dd><dl>
<dt><code>width</code> <i>(mandatory setting)</i></dt>
<dd>How many pixels wide should detail graphs be</dd>
<dt><code>height</code> <i>(mandatory setting)</i></dt>
<dd>How many pixels high should detail graphs be</dd>
<dt><code>loss_background</code></dt>
<dd>Should the graphs be shown with a background showing loss data for emphasis (yes/no)? </dd>
<p> If this option is enabled, uptime data is no longer displayed in the graph background.</p>
<dt><code>logarithmic</code></dt>
<dd>should the graphs be shown in a logarithmic scale (yes/no)</dd>
<dt><code>unison_tolerance</code></dt>
<dd>if a graph is more than this factor of the median &#8216;max&#8217; it drops out of the unison scaling algorithm. A factor of two would mean that any graph with a max either less than half or more than twice the median &#8216;max&#8217; will be dropped from unison scaling</dd>
<dt><code>max_rtt</code></dt>
<dd>Any roundtrip time larger than this value will cropped in the detail graph</dd>
<dt><code>strftime</code></dt>
<dd>Use posix strftime to format the timestamp in the left hand lower corner of the detail graph</dd>
<dt><code>nodata_color</code></dt>
<dd>Paint the graph background in a special color when there is no data for this period because smokeping has not been running (#rrggbb)</dd></dl>
</dl>
<dl>
<dd>The detailed display can contain several graphs of different resolution. In this table you can specify the resolution of each graph. </dd>
<p> Example: </p>
<pre> &quot;Last 3 Hours&quot; 3h
 &quot;Last 30 Hours&quot; 30h
 &quot;Last 10 Days&quot; 10d
 &quot;Last 400 Days&quot; 400d</pre>
<dl>
<dt>column 0</dt>
<dd>Description of the particular resolution.</dd>
<dt>column 1</dt>
<dd>How much time should be depicted. The format is the same as for the <code>age</code> parameter of the Overview section.</dd></dl>
</dl>
<dl>
<dd>The following sections are valid on level 2:</dd>
<dl>
<dt><code>++loss_colors</code></dt>
<dd>In the Detail view, the color of the median line depends the amount of lost packets. SmokePing comes with a reasonable default setting, but you may choose to disagree. The table below lets you specify your own coloring. </dd>
<p> Example: </p>
<pre> Loss Color Legend
 1 00ff00 &quot;&lt;1&quot;
 3 0000ff &quot;&lt;3&quot;
 1000 ff0000 &quot;&gt;=3&quot;</pre>
<dl>
<dd>
</dd><dl>
<dt>column 0</dt>
<dd>Activate when the number of losst pings is larger or equal to this number</dd>
<dt>column 1</dt>
<dd>Color for this range.</dd>
<dt>column 2</dt>
<dd>Description for this range.</dd></dl>
</dl>
<dl>
<dd></dd></dl>
<dt><code>++uptime_colors</code></dt>
<dd>When monitoring a host with DYNAMIC addressing, SmokePing will keep track of how long the machine is able to keep the same IP address. This time is plotted as a color in the graphs background. SmokePing comes with a reasonable default setting, but you may choose to disagree. The table below lets you specify your own coloring </dd>
<p> Example: </p>
<pre> # Uptime Color Legend
 3600 00ff00 &quot;&lt;1h&quot;
 86400 0000ff &quot;&lt;1d&quot;
 604800 ff0000 &quot;&lt;1w&quot;
 1000000000000 ffff00 &quot;&gt;1w&quot;</pre>
<p>Uptime is in days!</p>
<dl>
<dd>
</dd><dl>
<dt>column 0</dt>
<dd>Activate when uptime in days is larger of equal to this number</dd>
<dt>column 1</dt>
<dd>Color for this uptime range.</dd>
<dt>column 2</dt>
<dd>Description for this range.</dd></dl>
</dl>
<dl>
<dd></dd></dl>
</dl>
</dl>
<dl>
<dd></dd></dl>
<dt><code>+charts</code></dt>
<dd>The SmokePing Charts feature allow you to have Top X lists created according to various criteria. </dd>
<p> Each type of Chart must live in its own subsection. </p>
<pre> + charts
 menu = Charts
 title = The most interesting destinations
 ++ median
 sorter = Median(entries=&gt;10)
 title = Sorted by Median Roundtrip Time
 menu = Top Median RTT
 format = Median RTT %e s</pre>
<p>The following variables can be set in this section:</p>
<dl>
<dd>
</dd><dl>
<dt><code>menu</code> <i>(mandatory setting)</i></dt>
<dd>Menu entry for the Charts Section.</dd>
<dt><code>title</code> <i>(mandatory setting)</i></dt>
<dd>Page title for the Charts Section.</dd></dl>
</dl>
<dl>
<dd>The following sections are valid on level 2:</dd>
<dl>
<dt><code>++/[-_0-9a-zA-Z]+/</code></dt>
<dd>The following variables can be set in this section:</dd>
<dl>
<dd>
</dd><dl>
<dt><code>menu</code> <i>(mandatory setting)</i></dt>
<dd>Menu entry</dd>
<dt><code>title</code> <i>(mandatory setting)</i></dt>
<dd>Page title</dd>
<dt><code>sorter</code> <i>(mandatory setting)</i></dt>
<dd>sorter for this charts sections</dd>
<dt><code>format</code></dt>
<dd>sprintf format string to format curent value</dd></dl>
</dl>
<dl>
<dd></dd></dl>
</dl>
</dl>
<dl>
<dd></dd></dl>
<dt><code>+multihost</code></dt>
<dd>Settings for the multihost graphs. At the moment this is only used for the color setting. Check the documentation on the host property of the target section for more. </dd>
<p> The following variables can be set in this section:</p>
<dl>
<dd>
</dd><dl>
<dt><code>colors</code></dt>
<dd>Space separated list of colors for multihost graphs </dd>
<p> Example: colors = ff0000 00ff00 0000ff</dl>
</dl>
<dl>
<dd></dd></dl>
<dt><code>+hierarchies</code></dt>
<dd>Provide an alternative presentation hierarchy for your smokeping data. After setting up a hierarchy in this section. You can use it in each tagets parent property. A drop-down menu in the smokeping website lets the user switch presentation hierarchy. </dd>
<p> The following sections are valid on level 2:</p>
<dl>
<dd>
</dd><dl>
<dt><code>++/[-_0-9a-zA-Z]+/</code></dt>
<dd>Identifier of the hierarchie. Use this as prefix in the targets parent property </dd>
<p> The following variables can be set in this section:</p>
<dl>
<dd>
</dd><dl>
<dt><code>title</code> <i>(mandatory setting)</i></dt>
<dd>Title for this hierarchy</dd></dl>
</dl>
<dl>
<dd></dd></dl>
</dl>
</dl>
<dl>
<dd></dd></dl>
</dl>
<h3>*** Probes *** <i>(mandatory section)</i></h3>
<p>The Probes Section configures Probe modules. Probe modules integrate an external ping command into SmokePing. Check the documentation of each module for more information about it. </p>
<p> The following sections are valid on level 1:</p>
<dl>
<dt><code>+/[-_0-9a-zA-Z]+/</code></dt>
<dd>Each module can take specific configuration information from this area. The jumble of letters above is a regular expression defining legal module names. </dd>
<p> See the documentation of each module for details about its variables. </p>
<p> The grammar of this section is <i>dynamically</i> modified based on its name. </p>
<p> The following sections are valid on level 2:</p>
<dl>
<dd>
</dd><dl>
<dt><code>++/[-_0-9a-zA-Z]+/</code></dt>
<dd>You can define multiple instances of the same probe with subsections. These instances can have different values for their variables, so you can eg. have one instance of the FPing probe with packet size 1000 and step 300 and another instance with packet size 64 and step 30. The name of the subsection determines what the probe will be called, so you can write descriptive names for the probes. </dd>
<p> If there are any subsections defined, the main section for this probe will just provide default parameter values for the probe instances, ie. it will not become a probe instance itself. </p>
<p> The example above would be written like this: </p>
<pre> *** Probes ***
 + FPing
 # this value is common for the two subprobes
 binary = /usr/bin/fping 
 ++ FPingLarge
 packetsize = 1000
 step = 300
 ++ FPingSmall
 packetsize = 64
 step = 30</pre>
</dl>
</dl>
<dl>
<dd>Dynamical grammar changes for example instances of this section:</dd>
<dl>
<dt><code>AnotherDNS</code>: (See the separate module documentation for details about each variable.)</dt>
<dd>The following new variables are valid:</dd>
<dl>
<dd>
</dd><dl>
<dt><code>forks</code></dt>
<dd>see above </dd>
<p> Default value: forks = 5</p>
<dt><code>offset</code></dt>
<dd>see above</dd>
<dt><code>step</code></dt>
<dd>see above</dd>
<dt><code>ipversion</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>lookup</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>mininterval</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.) </dd>
<p> Default value: mininterval = 0.5</p>
<dt><code>pings</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>port</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.) </dd>
<p> Default value: port = 53</p>
<dt><code>protocol</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.) </dd>
<p> Default value: protocol = udp</p>
<dt><code>recordtype</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.) </dd>
<p> Default value: recordtype = A</p>
<dt><code>require_answers</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>require_noerror</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>timeout</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.) </dd>
<p> Default value: timeout = 5</dl>
</dl>
<dl>
<dd>Syntax changes for subsection <code>/[-_0-9a-zA-Z]+/</code> </dd>
<dl>
<dd>The following new variables are valid:</dd>
<dl>
<dt><code>forks</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here. </p>
<p> Default value: forks = 5</p>
<dt><code>offset</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>step</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>ipversion</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>lookup</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>mininterval</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here. </dd>
<p> Default value: mininterval = 0.5</p>
<dt><code>pings</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>port</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here. </dd>
<p> Default value: port = 53</p>
<dt><code>protocol</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here. </dd>
<p> Default value: protocol = udp</p>
<dt><code>recordtype</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here. </dd>
<p> Default value: recordtype = A</p>
<dt><code>require_answers</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>require_noerror</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>timeout</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here. </dd>
<p> Default value: timeout = 5</dl>
</dl>
<dl>
<dd></dd></dl>
</dl>
<dl>
<dd>(End of dynamical grammar changes for example instance <tt>&quot;AnotherDNS&quot;</tt>.)</dd></dl>
<dt><code>AnotherSSH</code>: (See the separate module documentation for details about each variable.)</dt>
<dd>The following new variables are valid:</dd>
<dl>
<dd>
</dd><dl>
<dt><code>forks</code></dt>
<dd>see above </dd>
<p> Default value: forks = 5</p>
<dt><code>offset</code></dt>
<dd>see above</dd>
<dt><code>step</code></dt>
<dd>see above</dd>
<dt><code>greeting</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.) </dd>
<p> Default value: greeting = SSH-Latency-Measurement-Sorry-for-this-logmessage</p>
<dt><code>interval</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.) </dd>
<p> Default value: interval = established</p>
<dt><code>mininterval</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.) </dd>
<p> Default value: mininterval = 0.5</p>
<dt><code>pings</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>port</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.) </dd>
<p> Default value: port = 22</p>
<dt><code>timeout</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.) </dd>
<p> Default value: timeout = 5</dl>
</dl>
<dl>
<dd>Syntax changes for subsection <code>/[-_0-9a-zA-Z]+/</code> </dd>
<dl>
<dd>The following new variables are valid:</dd>
<dl>
<dt><code>forks</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here. </p>
<p> Default value: forks = 5</p>
<dt><code>offset</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>step</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>greeting</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here. </dd>
<p> Default value: greeting = SSH-Latency-Measurement-Sorry-for-this-logmessage</p>
<dt><code>interval</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here. </dd>
<p> Default value: interval = established</p>
<dt><code>mininterval</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here. </dd>
<p> Default value: mininterval = 0.5</p>
<dt><code>pings</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>port</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here. </dd>
<p> Default value: port = 22</p>
<dt><code>timeout</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here. </dd>
<p> Default value: timeout = 5</dl>
</dl>
<dl>
<dd></dd></dl>
</dl>
<dl>
<dd>(End of dynamical grammar changes for example instance <tt>&quot;AnotherSSH&quot;</tt>.)</dd></dl>
<dt><code>CiscoRTTMonDNS</code>: (See the separate module documentation for details about each variable.)</dt>
<dd>The following new variables are valid:</dd>
<dl>
<dd>
</dd><dl>
<dt><code>forks</code></dt>
<dd>see above </dd>
<p> Default value: forks = 5</p>
<dt><code>offset</code></dt>
<dd>see above</dd>
<dt><code>step</code></dt>
<dd>see above</dd>
<dt><code>ioshost</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.) </dd>
<p> This variable <i>dynamically</i> modifies the grammar based on its value.</p>
<dt><code>iosint</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>name</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.) </dd>
<p> This variable <i>dynamically</i> modifies the grammar based on its value.</p>
<dt><code>pings</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>timeout</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.) </dd>
<p> Default value: timeout = 15</dl>
</dl>
<dl>
<dd>Syntax changes for subsection <code>/[-_0-9a-zA-Z]+/</code> </dd>
<dl>
<dd>The following new variables are valid:</dd>
<dl>
<dt><code>forks</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here. </p>
<p> Default value: forks = 5</p>
<dt><code>offset</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>step</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>ioshost</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>iosint</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>name</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>pings</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>timeout</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here. </dd>
<p> Default value: timeout = 15</dl>
</dl>
<dl>
<dd></dd></dl>
</dl>
<dl>
<dd>(End of dynamical grammar changes for example instance <tt>&quot;CiscoRTTMonDNS&quot;</tt>.)</dd></dl>
<dt><code>CiscoRTTMonEchoICMP</code>: (See the separate module documentation for details about each variable.)</dt>
<dd>The following new variables are valid:</dd>
<dl>
<dd>
</dd><dl>
<dt><code>forks</code></dt>
<dd>see above </dd>
<p> Default value: forks = 5</p>
<dt><code>offset</code></dt>
<dd>see above</dd>
<dt><code>step</code></dt>
<dd>see above</dd>
<dt><code>ioshost</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.) </dd>
<p> This variable <i>dynamically</i> modifies the grammar based on its value.</p>
<dt><code>iosint</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>packetsize</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.) </dd>
<p> Default value: packetsize = 56</p>
<dt><code>pings</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>timeout</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.) </dd>
<p> Default value: timeout = 15</p>
<dt><code>tos</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>vrf</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd></dl>
</dl>
<dl>
<dd>Syntax changes for subsection <code>/[-_0-9a-zA-Z]+/</code> </dd>
<dl>
<dd>The following new variables are valid:</dd>
<dl>
<dt><code>forks</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here. </p>
<p> Default value: forks = 5</p>
<dt><code>offset</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>step</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>ioshost</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>iosint</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>packetsize</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here. </dd>
<p> Default value: packetsize = 56</p>
<dt><code>pings</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>timeout</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here. </dd>
<p> Default value: timeout = 15</p>
<dt><code>tos</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>vrf</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd></dl>
</dl>
<dl>
<dd></dd></dl>
</dl>
<dl>
<dd>(End of dynamical grammar changes for example instance <tt>&quot;CiscoRTTMonEchoICMP&quot;</tt>.)</dd></dl>
<dt><code>CiscoRTTMonTcpConnect</code>: (See the separate module documentation for details about each variable.)</dt>
<dd>The following new variables are valid:</dd>
<dl>
<dd>
</dd><dl>
<dt><code>forks</code></dt>
<dd>see above </dd>
<p> Default value: forks = 5</p>
<dt><code>offset</code></dt>
<dd>see above</dd>
<dt><code>step</code></dt>
<dd>see above</dd>
<dt><code>ioshost</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.) </dd>
<p> This variable <i>dynamically</i> modifies the grammar based on its value.</p>
<dt><code>iosint</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>pings</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>port</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.) </dd>
<p> Default value: port = 80</p>
<dt><code>timeout</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.) </dd>
<p> Default value: timeout = 15</p>
<dt><code>tos</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd></dl>
</dl>
<dl>
<dd>Syntax changes for subsection <code>/[-_0-9a-zA-Z]+/</code> </dd>
<dl>
<dd>The following new variables are valid:</dd>
<dl>
<dt><code>forks</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here. </p>
<p> Default value: forks = 5</p>
<dt><code>offset</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>step</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>ioshost</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>iosint</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>pings</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>port</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here. </dd>
<p> Default value: port = 80</p>
<dt><code>timeout</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here. </dd>
<p> Default value: timeout = 15</p>
<dt><code>tos</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd></dl>
</dl>
<dl>
<dd></dd></dl>
</dl>
<dl>
<dd>(End of dynamical grammar changes for example instance <tt>&quot;CiscoRTTMonTcpConnect&quot;</tt>.)</dd></dl>
<dt><code>Curl</code>: (See the separate module documentation for details about each variable.)</dt>
<dd>The following new variables are valid:</dd>
<dl>
<dd>
</dd><dl>
<dt><code>binary</code></dt>
<dd>see above </dd>
<p> Default value: binary = /usr/bin/curl</p>
<dt><code>forks</code></dt>
<dd>see above </dd>
<p> Default value: forks = 5</p>
<dt><code>offset</code></dt>
<dd>see above</dd>
<dt><code>step</code></dt>
<dd>see above</dd>
<dt><code>agent</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>expect</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>extraargs</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>extrare</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.) </dd>
<p> Default value: extrare = / /</p>
<dt><code>follow_redirects</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.) </dd>
<p> Default value: follow_redirects = no</p>
<dt><code>include_redirects</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.) </dd>
<p> Default value: include_redirects = no</p>
<dt><code>insecure_ssl</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>interface</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>pings</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>ssl2</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>timeout</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.) </dd>
<p> Default value: timeout = 10</p>
<dt><code>urlformat</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.) </dd>
<p> This variable <i>dynamically</i> modifies the grammar based on its value.</dl>
</dl>
<dl>
<dd>Syntax changes for subsection <code>/[-_0-9a-zA-Z]+/</code> </dd>
<dl>
<dd>The following new variables are valid:</dd>
<dl>
<dt><code>binary</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here. </p>
<p> Default value: binary = /usr/bin/curl</p>
<dt><code>forks</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here. </p>
<p> Default value: forks = 5</p>
<dt><code>offset</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>step</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>agent</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>expect</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>extraargs</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>extrare</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here. </dd>
<p> Default value: extrare = / /</p>
<dt><code>follow_redirects</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here. </dd>
<p> Default value: follow_redirects = no</p>
<dt><code>include_redirects</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here. </dd>
<p> Default value: include_redirects = no</p>
<dt><code>insecure_ssl</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>interface</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>pings</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>ssl2</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>timeout</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here. </dd>
<p> Default value: timeout = 10</p>
<dt><code>urlformat</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd></dl>
</dl>
<dl>
<dd></dd></dl>
</dl>
<dl>
<dd>(End of dynamical grammar changes for example instance <tt>&quot;Curl&quot;</tt>.)</dd></dl>
<dt><code>DNS</code>: (See the separate module documentation for details about each variable.)</dt>
<dd>The following new variables are valid:</dd>
<dl>
<dd>
</dd><dl>
<dt><code>binary</code> <i>(mandatory setting)</i></dt>
<dd>see above</dd>
<dt><code>forks</code></dt>
<dd>see above </dd>
<p> Default value: forks = 5</p>
<dt><code>offset</code></dt>
<dd>see above</dd>
<dt><code>step</code></dt>
<dd>see above</dd>
<dt><code>timeout</code></dt>
<dd>see above </dd>
<p> Default value: timeout = 5</p>
<dt><code>lookup</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>pings</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>server</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd></dl>
</dl>
<dl>
<dd>Syntax changes for subsection <code>/[-_0-9a-zA-Z]+/</code> </dd>
<dl>
<dd>The following new variables are valid:</dd>
<dl>
<dt><code>binary</code> <i>(mandatory setting)</i></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>forks</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here. </p>
<p> Default value: forks = 5</p>
<dt><code>offset</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>step</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>timeout</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here. </p>
<p> Default value: timeout = 5</p>
<dt><code>lookup</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>pings</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>server</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd></dl>
</dl>
<dl>
<dd></dd></dl>
</dl>
<dl>
<dd>(End of dynamical grammar changes for example instance <tt>&quot;DNS&quot;</tt>.)</dd></dl>
<dt><code>DismanPing</code>: (See the separate module documentation for details about each variable.)</dt>
<dd>The following new variables are valid:</dd>
<dl>
<dd>
</dd><dl>
<dt><code>offset</code></dt>
<dd>see above</dd>
<dt><code>pings</code></dt>
<dd>see above </dd>
<p> Default value: pings = 15</p>
<dt><code>step</code></dt>
<dd>see above</dd>
<dt><code>ownerindex</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>packetsize</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.) </dd>
<p> Default value: packetsize = 56</p>
<dt><code>pinghost</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.) </dd>
<p> This variable <i>dynamically</i> modifies the grammar based on its value.</p>
<dt><code>pingsrc</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd></dl>
</dl>
<dl>
<dd>Syntax changes for subsection <code>/[-_0-9a-zA-Z]+/</code> </dd>
<dl>
<dd>The following new variables are valid:</dd>
<dl>
<dt><code>offset</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>pings</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here. </p>
<p> Default value: pings = 15</p>
<dt><code>step</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>ownerindex</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>packetsize</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here. </dd>
<p> Default value: packetsize = 56</p>
<dt><code>pinghost</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>pingsrc</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd></dl>
</dl>
<dl>
<dd></dd></dl>
</dl>
<dl>
<dd>(End of dynamical grammar changes for example instance <tt>&quot;DismanPing&quot;</tt>.)</dd></dl>
<dt><code>EchoPing</code>: (See the separate module documentation for details about each variable.)</dt>
<dd>The following new variables are valid:</dd>
<dl>
<dd>
</dd><dl>
<dt><code>binary</code></dt>
<dd>see above </dd>
<p> Default value: binary = /usr/bin/echoping</p>
<dt><code>forks</code></dt>
<dd>see above </dd>
<p> Default value: forks = 5</p>
<dt><code>offset</code></dt>
<dd>see above</dd>
<dt><code>step</code></dt>
<dd>see above</dd>
<dt><code>extraopts</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>fill</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>ipversion</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>pings</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>priority</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>size</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>timeout</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.) </dd>
<p> Default value: timeout = 5</p>
<dt><code>tos</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>udp</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>waittime</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd></dl>
</dl>
<dl>
<dd>Syntax changes for subsection <code>/[-_0-9a-zA-Z]+/</code> </dd>
<dl>
<dd>The following new variables are valid:</dd>
<dl>
<dt><code>binary</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here. </p>
<p> Default value: binary = /usr/bin/echoping</p>
<dt><code>forks</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here. </p>
<p> Default value: forks = 5</p>
<dt><code>offset</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>step</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>extraopts</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>fill</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>ipversion</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>pings</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>priority</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>size</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>timeout</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here. </dd>
<p> Default value: timeout = 5</p>
<dt><code>tos</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>udp</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>waittime</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd></dl>
</dl>
<dl>
<dd></dd></dl>
</dl>
<dl>
<dd>(End of dynamical grammar changes for example instance <tt>&quot;EchoPing&quot;</tt>.)</dd></dl>
<dt><code>EchoPingChargen</code>: (See the separate module documentation for details about each variable.)</dt>
<dd>The following new variables are valid:</dd>
<dl>
<dd>
</dd><dl>
<dt><code>binary</code></dt>
<dd>see above </dd>
<p> Default value: binary = /usr/bin/echoping</p>
<dt><code>forks</code></dt>
<dd>see above </dd>
<p> Default value: forks = 5</p>
<dt><code>offset</code></dt>
<dd>see above</dd>
<dt><code>step</code></dt>
<dd>see above</dd>
<dt><code>extraopts</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>fill</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>ipversion</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>pings</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>priority</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>size</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>timeout</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.) </dd>
<p> Default value: timeout = 5</p>
<dt><code>tos</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>waittime</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd></dl>
</dl>
<dl>
<dd>Syntax changes for subsection <code>/[-_0-9a-zA-Z]+/</code> </dd>
<dl>
<dd>The following new variables are valid:</dd>
<dl>
<dt><code>binary</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here. </p>
<p> Default value: binary = /usr/bin/echoping</p>
<dt><code>forks</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here. </p>
<p> Default value: forks = 5</p>
<dt><code>offset</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>step</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>extraopts</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>fill</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>ipversion</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>pings</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>priority</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>size</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>timeout</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here. </dd>
<p> Default value: timeout = 5</p>
<dt><code>tos</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>waittime</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd></dl>
</dl>
<dl>
<dd></dd></dl>
</dl>
<dl>
<dd>(End of dynamical grammar changes for example instance <tt>&quot;EchoPingChargen&quot;</tt>.)</dd></dl>
<dt><code>EchoPingDNS</code>: (See the separate module documentation for details about each variable.)</dt>
<dd>The following new variables are valid:</dd>
<dl>
<dd>
</dd><dl>
<dt><code>binary</code></dt>
<dd>see above </dd>
<p> Default value: binary = /usr/bin/echoping</p>
<dt><code>forks</code></dt>
<dd>see above </dd>
<p> Default value: forks = 5</p>
<dt><code>offset</code></dt>
<dd>see above</dd>
<dt><code>step</code></dt>
<dd>see above</dd>
<dt><code>dns_request</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.) </dd>
<p> This variable <i>dynamically</i> modifies the grammar based on its value.</p>
<dt><code>dns_tcp</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>dns_type</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.) </dd>
<p> Default value: dns_type = A</p>
<dt><code>extraopts</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>ipversion</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>pings</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>plugin</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.) </dd>
<p> Default value: plugin = dns</p>
<dt><code>pluginargs</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>priority</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>timeout</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.) </dd>
<p> Default value: timeout = 5</p>
<dt><code>tos</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>waittime</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd></dl>
</dl>
<dl>
<dd>Syntax changes for subsection <code>/[-_0-9a-zA-Z]+/</code> </dd>
<dl>
<dd>The following new variables are valid:</dd>
<dl>
<dt><code>binary</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here. </p>
<p> Default value: binary = /usr/bin/echoping</p>
<dt><code>forks</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here. </p>
<p> Default value: forks = 5</p>
<dt><code>offset</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>step</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>dns_request</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>dns_tcp</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>dns_type</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here. </dd>
<p> Default value: dns_type = A</p>
<dt><code>extraopts</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>ipversion</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>pings</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>plugin</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here. </dd>
<p> Default value: plugin = dns</p>
<dt><code>pluginargs</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>priority</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>timeout</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here. </dd>
<p> Default value: timeout = 5</p>
<dt><code>tos</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>waittime</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd></dl>
</dl>
<dl>
<dd></dd></dl>
</dl>
<dl>
<dd>(End of dynamical grammar changes for example instance <tt>&quot;EchoPingDNS&quot;</tt>.)</dd></dl>
<dt><code>EchoPingDiscard</code>: (See the separate module documentation for details about each variable.)</dt>
<dd>The following new variables are valid:</dd>
<dl>
<dd>
</dd><dl>
<dt><code>binary</code></dt>
<dd>see above </dd>
<p> Default value: binary = /usr/bin/echoping</p>
<dt><code>forks</code></dt>
<dd>see above </dd>
<p> Default value: forks = 5</p>
<dt><code>offset</code></dt>
<dd>see above</dd>
<dt><code>step</code></dt>
<dd>see above</dd>
<dt><code>extraopts</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>fill</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>ipversion</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>pings</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>priority</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>size</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>timeout</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.) </dd>
<p> Default value: timeout = 5</p>
<dt><code>tos</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>udp</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>waittime</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd></dl>
</dl>
<dl>
<dd>Syntax changes for subsection <code>/[-_0-9a-zA-Z]+/</code> </dd>
<dl>
<dd>The following new variables are valid:</dd>
<dl>
<dt><code>binary</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here. </p>
<p> Default value: binary = /usr/bin/echoping</p>
<dt><code>forks</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here. </p>
<p> Default value: forks = 5</p>
<dt><code>offset</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>step</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>extraopts</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>fill</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>ipversion</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>pings</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>priority</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>size</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>timeout</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here. </dd>
<p> Default value: timeout = 5</p>
<dt><code>tos</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>udp</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>waittime</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd></dl>
</dl>
<dl>
<dd></dd></dl>
</dl>
<dl>
<dd>(End of dynamical grammar changes for example instance <tt>&quot;EchoPingDiscard&quot;</tt>.)</dd></dl>
<dt><code>EchoPingHttp</code>: (See the separate module documentation for details about each variable.)</dt>
<dd>The following new variables are valid:</dd>
<dl>
<dd>
</dd><dl>
<dt><code>binary</code></dt>
<dd>see above </dd>
<p> Default value: binary = /usr/bin/echoping</p>
<dt><code>forks</code></dt>
<dd>see above </dd>
<p> Default value: forks = 5</p>
<dt><code>offset</code></dt>
<dd>see above</dd>
<dt><code>step</code></dt>
<dd>see above</dd>
<dt><code>accept_redirects</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>extraopts</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>ignore_cache</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>ipversion</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>pings</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>port</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>priority</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>revalidate_data</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>timeout</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.) </dd>
<p> Default value: timeout = 10</p>
<dt><code>tos</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>url</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.) </dd>
<p> Default value: url = /</p>
<dt><code>waittime</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd></dl>
</dl>
<dl>
<dd>Syntax changes for subsection <code>/[-_0-9a-zA-Z]+/</code> </dd>
<dl>
<dd>The following new variables are valid:</dd>
<dl>
<dt><code>binary</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here. </p>
<p> Default value: binary = /usr/bin/echoping</p>
<dt><code>forks</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here. </p>
<p> Default value: forks = 5</p>
<dt><code>offset</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>step</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>accept_redirects</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>extraopts</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>ignore_cache</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>ipversion</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>pings</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>port</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>priority</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>revalidate_data</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>timeout</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here. </dd>
<p> Default value: timeout = 10</p>
<dt><code>tos</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>url</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here. </dd>
<p> Default value: url = /</p>
<dt><code>waittime</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd></dl>
</dl>
<dl>
<dd></dd></dl>
</dl>
<dl>
<dd>(End of dynamical grammar changes for example instance <tt>&quot;EchoPingHttp&quot;</tt>.)</dd></dl>
<dt><code>EchoPingHttps</code>: (See the separate module documentation for details about each variable.)</dt>
<dd>The following new variables are valid:</dd>
<dl>
<dd>
</dd><dl>
<dt><code>binary</code></dt>
<dd>see above </dd>
<p> Default value: binary = /usr/bin/echoping</p>
<dt><code>forks</code></dt>
<dd>see above </dd>
<p> Default value: forks = 5</p>
<dt><code>offset</code></dt>
<dd>see above</dd>
<dt><code>step</code></dt>
<dd>see above</dd>
<dt><code>accept_redirects</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>extraopts</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>ignore_cache</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>ipversion</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>pings</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>port</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>priority</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>prot</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.) </dd>
<p> Default value: prot = 443</p>
<dt><code>revalidate_data</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>timeout</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.) </dd>
<p> Default value: timeout = 10</p>
<dt><code>tos</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>url</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.) </dd>
<p> Default value: url = /</p>
<dt><code>waittime</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd></dl>
</dl>
<dl>
<dd>Syntax changes for subsection <code>/[-_0-9a-zA-Z]+/</code> </dd>
<dl>
<dd>The following new variables are valid:</dd>
<dl>
<dt><code>binary</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here. </p>
<p> Default value: binary = /usr/bin/echoping</p>
<dt><code>forks</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here. </p>
<p> Default value: forks = 5</p>
<dt><code>offset</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>step</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>accept_redirects</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>extraopts</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>ignore_cache</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>ipversion</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>pings</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>port</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>priority</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>prot</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here. </dd>
<p> Default value: prot = 443</p>
<dt><code>revalidate_data</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>timeout</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here. </dd>
<p> Default value: timeout = 10</p>
<dt><code>tos</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>url</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here. </dd>
<p> Default value: url = /</p>
<dt><code>waittime</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd></dl>
</dl>
<dl>
<dd></dd></dl>
</dl>
<dl>
<dd>(End of dynamical grammar changes for example instance <tt>&quot;EchoPingHttps&quot;</tt>.)</dd></dl>
<dt><code>EchoPingIcp</code>: (See the separate module documentation for details about each variable.)</dt>
<dd>The following new variables are valid:</dd>
<dl>
<dd>
</dd><dl>
<dt><code>binary</code></dt>
<dd>see above </dd>
<p> Default value: binary = /usr/bin/echoping</p>
<dt><code>forks</code></dt>
<dd>see above </dd>
<p> Default value: forks = 5</p>
<dt><code>offset</code></dt>
<dd>see above</dd>
<dt><code>step</code></dt>
<dd>see above</dd>
<dt><code>extraopts</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>ipversion</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>pings</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>priority</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>timeout</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.) </dd>
<p> Default value: timeout = 5</p>
<dt><code>tos</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>url</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.) </dd>
<p> This variable <i>dynamically</i> modifies the grammar based on its value.</p>
<dt><code>waittime</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd></dl>
</dl>
<dl>
<dd>Syntax changes for subsection <code>/[-_0-9a-zA-Z]+/</code> </dd>
<dl>
<dd>The following new variables are valid:</dd>
<dl>
<dt><code>binary</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here. </p>
<p> Default value: binary = /usr/bin/echoping</p>
<dt><code>forks</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here. </p>
<p> Default value: forks = 5</p>
<dt><code>offset</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>step</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>extraopts</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>ipversion</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>pings</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>priority</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>timeout</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here. </dd>
<p> Default value: timeout = 5</p>
<dt><code>tos</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>url</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>waittime</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd></dl>
</dl>
<dl>
<dd></dd></dl>
</dl>
<dl>
<dd>(End of dynamical grammar changes for example instance <tt>&quot;EchoPingIcp&quot;</tt>.)</dd></dl>
<dt><code>EchoPingLDAP</code>: (See the separate module documentation for details about each variable.)</dt>
<dd>The following new variables are valid:</dd>
<dl>
<dd>
</dd><dl>
<dt><code>binary</code></dt>
<dd>see above </dd>
<p> Default value: binary = /usr/bin/echoping</p>
<dt><code>forks</code></dt>
<dd>see above </dd>
<p> Default value: forks = 5</p>
<dt><code>offset</code></dt>
<dd>see above</dd>
<dt><code>step</code></dt>
<dd>see above</dd>
<dt><code>extraopts</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>ipversion</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>ldap_base</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>ldap_request</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>ldap_scope</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>pings</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>plugin</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.) </dd>
<p> Default value: plugin = ldap</p>
<dt><code>pluginargs</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>priority</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>timeout</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.) </dd>
<p> Default value: timeout = 5</p>
<dt><code>tos</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>waittime</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd></dl>
</dl>
<dl>
<dd>Syntax changes for subsection <code>/[-_0-9a-zA-Z]+/</code> </dd>
<dl>
<dd>The following new variables are valid:</dd>
<dl>
<dt><code>binary</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here. </p>
<p> Default value: binary = /usr/bin/echoping</p>
<dt><code>forks</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here. </p>
<p> Default value: forks = 5</p>
<dt><code>offset</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>step</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>extraopts</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>ipversion</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>ldap_base</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>ldap_request</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>ldap_scope</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>pings</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>plugin</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here. </dd>
<p> Default value: plugin = ldap</p>
<dt><code>pluginargs</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>priority</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>timeout</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here. </dd>
<p> Default value: timeout = 5</p>
<dt><code>tos</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>waittime</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd></dl>
</dl>
<dl>
<dd></dd></dl>
</dl>
<dl>
<dd>(End of dynamical grammar changes for example instance <tt>&quot;EchoPingLDAP&quot;</tt>.)</dd></dl>
<dt><code>EchoPingPlugin</code>: (See the separate module documentation for details about each variable.)</dt>
<dd>The following new variables are valid:</dd>
<dl>
<dd>
</dd><dl>
<dt><code>binary</code></dt>
<dd>see above </dd>
<p> Default value: binary = /usr/bin/echoping</p>
<dt><code>forks</code></dt>
<dd>see above </dd>
<p> Default value: forks = 5</p>
<dt><code>offset</code></dt>
<dd>see above</dd>
<dt><code>step</code></dt>
<dd>see above</dd>
<dt><code>extraopts</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>ipversion</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>pings</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>plugin</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.) </dd>
<p> This variable <i>dynamically</i> modifies the grammar based on its value.</p>
<dt><code>pluginargs</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>priority</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>timeout</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.) </dd>
<p> Default value: timeout = 5</p>
<dt><code>tos</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>waittime</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd></dl>
</dl>
<dl>
<dd>Syntax changes for subsection <code>/[-_0-9a-zA-Z]+/</code> </dd>
<dl>
<dd>The following new variables are valid:</dd>
<dl>
<dt><code>binary</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here. </p>
<p> Default value: binary = /usr/bin/echoping</p>
<dt><code>forks</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here. </p>
<p> Default value: forks = 5</p>
<dt><code>offset</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>step</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>extraopts</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>ipversion</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>pings</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>plugin</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>pluginargs</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>priority</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>timeout</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here. </dd>
<p> Default value: timeout = 5</p>
<dt><code>tos</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>waittime</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd></dl>
</dl>
<dl>
<dd></dd></dl>
</dl>
<dl>
<dd>(End of dynamical grammar changes for example instance <tt>&quot;EchoPingPlugin&quot;</tt>.)</dd></dl>
<dt><code>EchoPingSmtp</code>: (See the separate module documentation for details about each variable.)</dt>
<dd>The following new variables are valid:</dd>
<dl>
<dd>
</dd><dl>
<dt><code>binary</code></dt>
<dd>see above </dd>
<p> Default value: binary = /usr/bin/echoping</p>
<dt><code>forks</code></dt>
<dd>see above </dd>
<p> Default value: forks = 5</p>
<dt><code>offset</code></dt>
<dd>see above</dd>
<dt><code>step</code></dt>
<dd>see above</dd>
<dt><code>extraopts</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>ipversion</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>pings</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>priority</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>timeout</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.) </dd>
<p> Default value: timeout = 5</p>
<dt><code>tos</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>waittime</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd></dl>
</dl>
<dl>
<dd>Syntax changes for subsection <code>/[-_0-9a-zA-Z]+/</code> </dd>
<dl>
<dd>The following new variables are valid:</dd>
<dl>
<dt><code>binary</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here. </p>
<p> Default value: binary = /usr/bin/echoping</p>
<dt><code>forks</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here. </p>
<p> Default value: forks = 5</p>
<dt><code>offset</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>step</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>extraopts</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>ipversion</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>pings</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>priority</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>timeout</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here. </dd>
<p> Default value: timeout = 5</p>
<dt><code>tos</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>waittime</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd></dl>
</dl>
<dl>
<dd></dd></dl>
</dl>
<dl>
<dd>(End of dynamical grammar changes for example instance <tt>&quot;EchoPingSmtp&quot;</tt>.)</dd></dl>
<dt><code>EchoPingWhois</code>: (See the separate module documentation for details about each variable.)</dt>
<dd>The following new variables are valid:</dd>
<dl>
<dd>
</dd><dl>
<dt><code>binary</code></dt>
<dd>see above </dd>
<p> Default value: binary = /usr/bin/echoping</p>
<dt><code>forks</code></dt>
<dd>see above </dd>
<p> Default value: forks = 5</p>
<dt><code>offset</code></dt>
<dd>see above</dd>
<dt><code>step</code></dt>
<dd>see above</dd>
<dt><code>extraopts</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>ipversion</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>pings</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>plugin</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.) </dd>
<p> Default value: plugin = whois</p>
<dt><code>pluginargs</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>priority</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>timeout</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.) </dd>
<p> Default value: timeout = 5</p>
<dt><code>tos</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>waittime</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>whois_request</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.) </dd>
<p> This variable <i>dynamically</i> modifies the grammar based on its value.</dl>
</dl>
<dl>
<dd>Syntax changes for subsection <code>/[-_0-9a-zA-Z]+/</code> </dd>
<dl>
<dd>The following new variables are valid:</dd>
<dl>
<dt><code>binary</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here. </p>
<p> Default value: binary = /usr/bin/echoping</p>
<dt><code>forks</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here. </p>
<p> Default value: forks = 5</p>
<dt><code>offset</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>step</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>extraopts</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>ipversion</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>pings</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>plugin</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here. </dd>
<p> Default value: plugin = whois</p>
<dt><code>pluginargs</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>priority</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>timeout</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here. </dd>
<p> Default value: timeout = 5</p>
<dt><code>tos</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>waittime</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>whois_request</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd></dl>
</dl>
<dl>
<dd></dd></dl>
</dl>
<dl>
<dd>(End of dynamical grammar changes for example instance <tt>&quot;EchoPingWhois&quot;</tt>.)</dd></dl>
<dt><code>FPing</code>: (See the separate module documentation for details about each variable.)</dt>
<dd>The following new variables are valid:</dd>
<dl>
<dd>
</dd><dl>
<dt><code>binary</code> <i>(mandatory setting)</i></dt>
<dd>see above</dd>
<dt><code>blazemode</code></dt>
<dd>see above</dd>
<dt><code>hostinterval</code></dt>
<dd>see above</dd>
<dt><code>mininterval</code></dt>
<dd>see above </dd>
<p> Default value: mininterval = 0.01</p>
<dt><code>offset</code></dt>
<dd>see above</dd>
<dt><code>packetsize</code></dt>
<dd>see above</dd>
<dt><code>pings</code></dt>
<dd>see above</dd>
<dt><code>sourceaddress</code></dt>
<dd>see above</dd>
<dt><code>step</code></dt>
<dd>see above</dd>
<dt><code>timeout</code></dt>
<dd>see above</dd>
<dt><code>tos</code></dt>
<dd>see above</dd>
<dt><code>usestdout</code></dt>
<dd>see above</dd></dl>
</dl>
<dl>
<dd>Syntax changes for subsection <code>/[-_0-9a-zA-Z]+/</code> </dd>
<dl>
<dd>The following new variables are valid:</dd>
<dl>
<dt><code>binary</code> <i>(mandatory setting)</i></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>blazemode</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>hostinterval</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>mininterval</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here. </p>
<p> Default value: mininterval = 0.01</p>
<dt><code>offset</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>packetsize</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>pings</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>sourceaddress</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>step</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>timeout</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>tos</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>usestdout</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dl>
</dl>
<dl>
<dd></dd></dl>
</dl>
<dl>
<dd>(End of dynamical grammar changes for example instance <tt>&quot;FPing&quot;</tt>.)</dd></dl>
<dt><code>FPing6</code>: (See the separate module documentation for details about each variable.)</dt>
<dd>The following new variables are valid:</dd>
<dl>
<dd>
</dd><dl>
<dt><code>binary</code> <i>(mandatory setting)</i></dt>
<dd>see above</dd>
<dt><code>blazemode</code></dt>
<dd>see above</dd>
<dt><code>hostinterval</code></dt>
<dd>see above</dd>
<dt><code>mininterval</code></dt>
<dd>see above </dd>
<p> Default value: mininterval = 0.01</p>
<dt><code>offset</code></dt>
<dd>see above</dd>
<dt><code>packetsize</code></dt>
<dd>see above</dd>
<dt><code>pings</code></dt>
<dd>see above</dd>
<dt><code>sourceaddress</code></dt>
<dd>see above</dd>
<dt><code>step</code></dt>
<dd>see above</dd>
<dt><code>timeout</code></dt>
<dd>see above</dd>
<dt><code>tos</code></dt>
<dd>see above</dd>
<dt><code>usestdout</code></dt>
<dd>see above</dd></dl>
</dl>
<dl>
<dd>Syntax changes for subsection <code>/[-_0-9a-zA-Z]+/</code> </dd>
<dl>
<dd>The following new variables are valid:</dd>
<dl>
<dt><code>binary</code> <i>(mandatory setting)</i></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>blazemode</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>hostinterval</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>mininterval</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here. </p>
<p> Default value: mininterval = 0.01</p>
<dt><code>offset</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>packetsize</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>pings</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>sourceaddress</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>step</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>timeout</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>tos</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>usestdout</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dl>
</dl>
<dl>
<dd></dd></dl>
</dl>
<dl>
<dd>(End of dynamical grammar changes for example instance <tt>&quot;FPing6&quot;</tt>.)</dd></dl>
<dt><code>FTPtransfer</code>: (See the separate module documentation for details about each variable.)</dt>
<dd>The following new variables are valid:</dd>
<dl>
<dd>
</dd><dl>
<dt><code>destfile</code></dt>
<dd>see above</dd>
<dt><code>forks</code></dt>
<dd>see above </dd>
<p> Default value: forks = 5</p>
<dt><code>min_interval</code></dt>
<dd>see above </dd>
<p> Default value: min_interval = 1</p>
<dt><code>mode</code> <i>(mandatory setting)</i></dt>
<dd>see above</dd>
<dt><code>offset</code></dt>
<dd>see above</dd>
<dt><code>passwordfile</code></dt>
<dd>see above</dd>
<dt><code>srcfile</code> <i>(mandatory setting)</i></dt>
<dd>see above</dd>
<dt><code>step</code></dt>
<dd>see above</dd>
<dt><code>localaddr</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>passive</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>password</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>pings</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>port</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>timeout</code> <i>(mandatory setting)</i></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>username</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd></dl>
</dl>
<dl>
<dd>Syntax changes for subsection <code>/[-_0-9a-zA-Z]+/</code> </dd>
<dl>
<dd>The following new variables are valid:</dd>
<dl>
<dt><code>destfile</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>forks</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here. </p>
<p> Default value: forks = 5</p>
<dt><code>min_interval</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here. </p>
<p> Default value: min_interval = 1</p>
<dt><code>mode</code> <i>(mandatory setting)</i></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>offset</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>passwordfile</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>srcfile</code> <i>(mandatory setting)</i></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>step</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>localaddr</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>passive</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>password</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>pings</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>port</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>timeout</code> <i>(mandatory setting)</i></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>username</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd></dl>
</dl>
<dl>
<dd></dd></dl>
</dl>
<dl>
<dd>(End of dynamical grammar changes for example instance <tt>&quot;FTPtransfer&quot;</tt>.)</dd></dl>
<dt><code>IOSPing</code>: (See the separate module documentation for details about each variable.)</dt>
<dd>The following new variables are valid:</dd>
<dl>
<dd>
</dd><dl>
<dt><code>binary</code> <i>(mandatory setting)</i></dt>
<dd>see above</dd>
<dt><code>forks</code></dt>
<dd>see above </dd>
<p> Default value: forks = 5</p>
<dt><code>offset</code></dt>
<dd>see above</dd>
<dt><code>packetsize</code></dt>
<dd>see above </dd>
<p> Default value: packetsize = 56</p>
<dt><code>step</code></dt>
<dd>see above</dd>
<dt><code>timeout</code></dt>
<dd>see above </dd>
<p> Default value: timeout = 5</p>
<dt><code>ioshost</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.) </dd>
<p> This variable <i>dynamically</i> modifies the grammar based on its value.</p>
<dt><code>iosint</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>iosuser</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>pings</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd></dl>
</dl>
<dl>
<dd>Syntax changes for subsection <code>/[-_0-9a-zA-Z]+/</code> </dd>
<dl>
<dd>The following new variables are valid:</dd>
<dl>
<dt><code>binary</code> <i>(mandatory setting)</i></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>forks</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here. </p>
<p> Default value: forks = 5</p>
<dt><code>offset</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>packetsize</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here. </p>
<p> Default value: packetsize = 56</p>
<dt><code>step</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>timeout</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here. </p>
<p> Default value: timeout = 5</p>
<dt><code>ioshost</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>iosint</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>iosuser</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>pings</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd></dl>
</dl>
<dl>
<dd></dd></dl>
</dl>
<dl>
<dd>(End of dynamical grammar changes for example instance <tt>&quot;IOSPing&quot;</tt>.)</dd></dl>
<dt><code>LDAP</code>: (See the separate module documentation for details about each variable.)</dt>
<dd>The following new variables are valid:</dd>
<dl>
<dd>
</dd><dl>
<dt><code>forks</code></dt>
<dd>see above </dd>
<p> Default value: forks = 5</p>
<dt><code>offset</code></dt>
<dd>see above</dd>
<dt><code>passwordfile</code></dt>
<dd>see above</dd>
<dt><code>step</code></dt>
<dd>see above</dd>
<dt><code>attrs</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>base</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>binddn</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>filter</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.) </dd>
<p> This variable <i>dynamically</i> modifies the grammar based on its value.</p>
<dt><code>mininterval</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.) </dd>
<p> Default value: mininterval = 1</p>
<dt><code>password</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>pings</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>port</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>scope</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.) </dd>
<p> Default value: scope = sub</p>
<dt><code>start_tls</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>timeout</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.) </dd>
<p> Default value: timeout = 5</p>
<dt><code>version</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd></dl>
</dl>
<dl>
<dd>Syntax changes for subsection <code>/[-_0-9a-zA-Z]+/</code> </dd>
<dl>
<dd>The following new variables are valid:</dd>
<dl>
<dt><code>forks</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here. </p>
<p> Default value: forks = 5</p>
<dt><code>offset</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>passwordfile</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>step</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>attrs</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>base</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>binddn</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>filter</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>mininterval</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here. </dd>
<p> Default value: mininterval = 1</p>
<dt><code>password</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>pings</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>port</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>scope</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here. </dd>
<p> Default value: scope = sub</p>
<dt><code>start_tls</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>timeout</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here. </dd>
<p> Default value: timeout = 5</p>
<dt><code>version</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd></dl>
</dl>
<dl>
<dd></dd></dl>
</dl>
<dl>
<dd>(End of dynamical grammar changes for example instance <tt>&quot;LDAP&quot;</tt>.)</dd></dl>
<dt><code>NFSping</code>: (See the separate module documentation for details about each variable.)</dt>
<dd>The following new variables are valid:</dd>
<dl>
<dd>
</dd><dl>
<dt><code>binary</code> <i>(mandatory setting)</i></dt>
<dd>see above</dd>
<dt><code>blazemode</code></dt>
<dd>see above</dd>
<dt><code>hostinterval</code></dt>
<dd>see above</dd>
<dt><code>mininterval</code></dt>
<dd>see above </dd>
<p> Default value: mininterval = 0.01</p>
<dt><code>offset</code></dt>
<dd>see above</dd>
<dt><code>pings</code></dt>
<dd>see above</dd>
<dt><code>step</code></dt>
<dd>see above</dd>
<dt><code>timeout</code></dt>
<dd>see above</dd></dl>
</dl>
<dl>
<dd>Syntax changes for subsection <code>/[-_0-9a-zA-Z]+/</code> </dd>
<dl>
<dd>The following new variables are valid:</dd>
<dl>
<dt><code>binary</code> <i>(mandatory setting)</i></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>blazemode</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>hostinterval</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>mininterval</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here. </p>
<p> Default value: mininterval = 0.01</p>
<dt><code>offset</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>pings</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>step</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>timeout</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dl>
</dl>
<dl>
<dd></dd></dl>
</dl>
<dl>
<dd>(End of dynamical grammar changes for example instance <tt>&quot;NFSping&quot;</tt>.)</dd></dl>
<dt><code>OpenSSHEOSPing</code>: (See the separate module documentation for details about each variable.)</dt>
<dd>The following new variables are valid:</dd>
<dl>
<dd>
</dd><dl>
<dt><code>forks</code></dt>
<dd>see above </dd>
<p> Default value: forks = 5</p>
<dt><code>offset</code></dt>
<dd>see above</dd>
<dt><code>packetsize</code></dt>
<dd>see above </dd>
<p> Default value: packetsize = 100</p>
<dt><code>step</code></dt>
<dd>see above</dd>
<dt><code>timeout</code></dt>
<dd>see above </dd>
<p> Default value: timeout = 5</p>
<dt><code>eospass</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.) </dd>
<p> This variable <i>dynamically</i> modifies the grammar based on its value.</p>
<dt><code>eosuser</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.) </dd>
<p> This variable <i>dynamically</i> modifies the grammar based on its value.</p>
<dt><code>pings</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>psource</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>source</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.) </dd>
<p> This variable <i>dynamically</i> modifies the grammar based on its value.</p>
<dt><code>unpriv</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd></dl>
</dl>
<dl>
<dd>Syntax changes for subsection <code>/[-_0-9a-zA-Z]+/</code> </dd>
<dl>
<dd>The following new variables are valid:</dd>
<dl>
<dt><code>forks</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here. </p>
<p> Default value: forks = 5</p>
<dt><code>offset</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>packetsize</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here. </p>
<p> Default value: packetsize = 100</p>
<dt><code>step</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>timeout</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here. </p>
<p> Default value: timeout = 5</p>
<dt><code>eospass</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>eosuser</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>pings</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>psource</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>source</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>unpriv</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd></dl>
</dl>
<dl>
<dd></dd></dl>
</dl>
<dl>
<dd>(End of dynamical grammar changes for example instance <tt>&quot;OpenSSHEOSPing&quot;</tt>.)</dd></dl>
<dt><code>OpenSSHJunOSPing</code>: (See the separate module documentation for details about each variable.)</dt>
<dd>The following new variables are valid:</dd>
<dl>
<dd>
</dd><dl>
<dt><code>forks</code></dt>
<dd>see above </dd>
<p> Default value: forks = 5</p>
<dt><code>offset</code></dt>
<dd>see above</dd>
<dt><code>packetsize</code></dt>
<dd>see above </dd>
<p> Default value: packetsize = 100</p>
<dt><code>step</code></dt>
<dd>see above</dd>
<dt><code>timeout</code></dt>
<dd>see above </dd>
<p> Default value: timeout = 5</p>
<dt><code>junospass</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.) </dd>
<p> This variable <i>dynamically</i> modifies the grammar based on its value.</p>
<dt><code>junosuser</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.) </dd>
<p> This variable <i>dynamically</i> modifies the grammar based on its value.</p>
<dt><code>pings</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>psource</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>source</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.) </dd>
<p> This variable <i>dynamically</i> modifies the grammar based on its value.</dl>
</dl>
<dl>
<dd>Syntax changes for subsection <code>/[-_0-9a-zA-Z]+/</code> </dd>
<dl>
<dd>The following new variables are valid:</dd>
<dl>
<dt><code>forks</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here. </p>
<p> Default value: forks = 5</p>
<dt><code>offset</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>packetsize</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here. </p>
<p> Default value: packetsize = 100</p>
<dt><code>step</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>timeout</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here. </p>
<p> Default value: timeout = 5</p>
<dt><code>junospass</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>junosuser</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>pings</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>psource</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>source</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd></dl>
</dl>
<dl>
<dd></dd></dl>
</dl>
<dl>
<dd>(End of dynamical grammar changes for example instance <tt>&quot;OpenSSHJunOSPing&quot;</tt>.)</dd></dl>
<dt><code>Qstat</code>: (See the separate module documentation for details about each variable.)</dt>
<dd>The following new variables are valid:</dd>
<dl>
<dd>
</dd><dl>
<dt><code>binary</code> <i>(mandatory setting)</i></dt>
<dd>see above</dd>
<dt><code>forks</code></dt>
<dd>see above </dd>
<p> Default value: forks = 5</p>
<dt><code>game</code></dt>
<dd>see above </dd>
<p> Default value: game = q3s</p>
<dt><code>mininterval</code></dt>
<dd>see above </dd>
<p> Default value: mininterval = 0.5</p>
<dt><code>offset</code></dt>
<dd>see above</dd>
<dt><code>port</code></dt>
<dd>see above</dd>
<dt><code>sourceaddress</code></dt>
<dd>see above</dd>
<dt><code>sourceport</code></dt>
<dd>see above</dd>
<dt><code>step</code></dt>
<dd>see above</dd>
<dt><code>timeout</code></dt>
<dd>see above </dd>
<p> Default value: timeout = 5</p>
<dt><code>pings</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd></dl>
</dl>
<dl>
<dd>Syntax changes for subsection <code>/[-_0-9a-zA-Z]+/</code> </dd>
<dl>
<dd>The following new variables are valid:</dd>
<dl>
<dt><code>binary</code> <i>(mandatory setting)</i></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>forks</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here. </p>
<p> Default value: forks = 5</p>
<dt><code>game</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here. </p>
<p> Default value: game = q3s</p>
<dt><code>mininterval</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here. </p>
<p> Default value: mininterval = 0.5</p>
<dt><code>offset</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>port</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>sourceaddress</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>sourceport</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>step</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>timeout</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here. </p>
<p> Default value: timeout = 5</p>
<dt><code>pings</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd></dl>
</dl>
<dl>
<dd></dd></dl>
</dl>
<dl>
<dd>(End of dynamical grammar changes for example instance <tt>&quot;Qstat&quot;</tt>.)</dd></dl>
<dt><code>Radius</code>: (See the separate module documentation for details about each variable.)</dt>
<dd>The following new variables are valid:</dd>
<dl>
<dd>
</dd><dl>
<dt><code>forks</code></dt>
<dd>see above </dd>
<p> Default value: forks = 5</p>
<dt><code>offset</code></dt>
<dd>see above</dd>
<dt><code>passwordfile</code></dt>
<dd>see above</dd>
<dt><code>secretfile</code></dt>
<dd>see above</dd>
<dt><code>step</code></dt>
<dd>see above</dd>
<dt><code>allowreject</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>mininterval</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.) </dd>
<p> Default value: mininterval = 1</p>
<dt><code>nas_ip_address</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>password</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>pings</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>port</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>secret</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>timeout</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.) </dd>
<p> Default value: timeout = 5</p>
<dt><code>username</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.) </dd>
<p> This variable <i>dynamically</i> modifies the grammar based on its value.</dl>
</dl>
<dl>
<dd>Syntax changes for subsection <code>/[-_0-9a-zA-Z]+/</code> </dd>
<dl>
<dd>The following new variables are valid:</dd>
<dl>
<dt><code>forks</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here. </p>
<p> Default value: forks = 5</p>
<dt><code>offset</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>passwordfile</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>secretfile</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>step</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>allowreject</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>mininterval</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here. </dd>
<p> Default value: mininterval = 1</p>
<dt><code>nas_ip_address</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>password</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>pings</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>port</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>secret</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>timeout</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here. </dd>
<p> Default value: timeout = 5</p>
<dt><code>username</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd></dl>
</dl>
<dl>
<dd></dd></dl>
</dl>
<dl>
<dd>(End of dynamical grammar changes for example instance <tt>&quot;Radius&quot;</tt>.)</dd></dl>
<dt><code>RemoteFPing</code>: (See the separate module documentation for details about each variable.)</dt>
<dd>The following new variables are valid:</dd>
<dl>
<dd>
</dd><dl>
<dt><code>binary</code> <i>(mandatory setting)</i></dt>
<dd>see above</dd>
<dt><code>blazemode</code></dt>
<dd>see above</dd>
<dt><code>hostinterval</code></dt>
<dd>see above</dd>
<dt><code>mininterval</code></dt>
<dd>see above </dd>
<p> Default value: mininterval = 0.01</p>
<dt><code>offset</code></dt>
<dd>see above</dd>
<dt><code>packetsize</code></dt>
<dd>see above</dd>
<dt><code>pings</code></dt>
<dd>see above</dd>
<dt><code>rbinary</code> <i>(mandatory setting)</i></dt>
<dd>see above</dd>
<dt><code>rhost</code> <i>(mandatory setting)</i></dt>
<dd>see above</dd>
<dt><code>ruser</code></dt>
<dd>see above</dd>
<dt><code>sourceaddress</code></dt>
<dd>see above</dd>
<dt><code>step</code></dt>
<dd>see above</dd>
<dt><code>timeout</code></dt>
<dd>see above</dd>
<dt><code>tos</code></dt>
<dd>see above</dd>
<dt><code>usestdout</code></dt>
<dd>see above</dd></dl>
</dl>
<dl>
<dd>Syntax changes for subsection <code>/[-_0-9a-zA-Z]+/</code> </dd>
<dl>
<dd>The following new variables are valid:</dd>
<dl>
<dt><code>binary</code> <i>(mandatory setting)</i></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>blazemode</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>hostinterval</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>mininterval</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here. </p>
<p> Default value: mininterval = 0.01</p>
<dt><code>offset</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>packetsize</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>pings</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>rbinary</code> <i>(mandatory setting)</i></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>rhost</code> <i>(mandatory setting)</i></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>ruser</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>sourceaddress</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>step</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>timeout</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>tos</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>usestdout</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dl>
</dl>
<dl>
<dd></dd></dl>
</dl>
<dl>
<dd>(End of dynamical grammar changes for example instance <tt>&quot;RemoteFPing&quot;</tt>.)</dd></dl>
<dt><code>SSH</code>: (See the separate module documentation for details about each variable.)</dt>
<dd>The following new variables are valid:</dd>
<dl>
<dd>
</dd><dl>
<dt><code>binary</code> <i>(mandatory setting)</i></dt>
<dd>see above</dd>
<dt><code>forks</code></dt>
<dd>see above </dd>
<p> Default value: forks = 5</p>
<dt><code>offset</code></dt>
<dd>see above</dd>
<dt><code>step</code></dt>
<dd>see above</dd>
<dt><code>timeout</code></dt>
<dd>see above </dd>
<p> Default value: timeout = 5</p>
<dt><code>keytype</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.) </dd>
<p> Default value: keytype = rsa</p>
<dt><code>pings</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>port</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.) </dd>
<p> Default value: port = 22</dl>
</dl>
<dl>
<dd>Syntax changes for subsection <code>/[-_0-9a-zA-Z]+/</code> </dd>
<dl>
<dd>The following new variables are valid:</dd>
<dl>
<dt><code>binary</code> <i>(mandatory setting)</i></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>forks</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here. </p>
<p> Default value: forks = 5</p>
<dt><code>offset</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>step</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>timeout</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here. </p>
<p> Default value: timeout = 5</p>
<dt><code>keytype</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here. </dd>
<p> Default value: keytype = rsa</p>
<dt><code>pings</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>port</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here. </dd>
<p> Default value: port = 22</dl>
</dl>
<dl>
<dd></dd></dl>
</dl>
<dl>
<dd>(End of dynamical grammar changes for example instance <tt>&quot;SSH&quot;</tt>.)</dd></dl>
<dt><code>SendEmail</code>: (See the separate module documentation for details about each variable.)</dt>
<dd>The following new variables are valid:</dd>
<dl>
<dd>
</dd><dl>
<dt><code>bodysize</code></dt>
<dd>see above</dd>
<dt><code>forks</code></dt>
<dd>see above </dd>
<p> Default value: forks = 5</p>
<dt><code>from</code> <i>(mandatory setting)</i></dt>
<dd>see above</dd>
<dt><code>offset</code></dt>
<dd>see above</dd>
<dt><code>step</code></dt>
<dd>see above</dd>
<dt><code>subject</code></dt>
<dd>see above </dd>
<p> Default value: subject = Test</p>
<dt><code>timeout</code></dt>
<dd>see above </dd>
<p> Default value: timeout = 5</p>
<dt><code>to</code> <i>(mandatory setting)</i></dt>
<dd>see above</dd>
<dt><code>pings</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>port</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.) </dd>
<p> Default value: port = 25</dl>
</dl>
<dl>
<dd>Syntax changes for subsection <code>/[-_0-9a-zA-Z]+/</code> </dd>
<dl>
<dd>The following new variables are valid:</dd>
<dl>
<dt><code>bodysize</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>forks</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here. </p>
<p> Default value: forks = 5</p>
<dt><code>from</code> <i>(mandatory setting)</i></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>offset</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>step</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>subject</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here. </p>
<p> Default value: subject = Test</p>
<dt><code>timeout</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here. </p>
<p> Default value: timeout = 5</p>
<dt><code>to</code> <i>(mandatory setting)</i></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>pings</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>port</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here. </dd>
<p> Default value: port = 25</dl>
</dl>
<dl>
<dd></dd></dl>
</dl>
<dl>
<dd>(End of dynamical grammar changes for example instance <tt>&quot;SendEmail&quot;</tt>.)</dd></dl>
<dt><code>SipSak</code>: (See the separate module documentation for details about each variable.)</dt>
<dd>The following new variables are valid:</dd>
<dl>
<dd>
</dd><dl>
<dt><code>binary</code></dt>
<dd>see above </dd>
<p> Default value: binary = /usr/bin/sipsak</p>
<dt><code>forks</code></dt>
<dd>see above </dd>
<p> Default value: forks = 5</p>
<dt><code>offset</code></dt>
<dd>see above</dd>
<dt><code>step</code></dt>
<dd>see above</dd>
<dt><code>timeout</code></dt>
<dd>see above </dd>
<p> Default value: timeout = 5</p>
<dt><code>keep_second</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>params</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>pings</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>port</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>user</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd></dl>
</dl>
<dl>
<dd>Syntax changes for subsection <code>/[-_0-9a-zA-Z]+/</code> </dd>
<dl>
<dd>The following new variables are valid:</dd>
<dl>
<dt><code>binary</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here. </p>
<p> Default value: binary = /usr/bin/sipsak</p>
<dt><code>forks</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here. </p>
<p> Default value: forks = 5</p>
<dt><code>offset</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>step</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>timeout</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here. </p>
<p> Default value: timeout = 5</p>
<dt><code>keep_second</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>params</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>pings</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>port</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>user</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd></dl>
</dl>
<dl>
<dd></dd></dl>
</dl>
<dl>
<dd>(End of dynamical grammar changes for example instance <tt>&quot;SipSak&quot;</tt>.)</dd></dl>
<dt><code>TCPPing</code>: (See the separate module documentation for details about each variable.)</dt>
<dd>The following new variables are valid:</dd>
<dl>
<dd>
</dd><dl>
<dt><code>binary</code> <i>(mandatory setting)</i></dt>
<dd>see above</dd>
<dt><code>forks</code></dt>
<dd>see above </dd>
<p> Default value: forks = 5</p>
<dt><code>offset</code></dt>
<dd>see above</dd>
<dt><code>step</code></dt>
<dd>see above</dd>
<dt><code>tcptraceroute</code></dt>
<dd>see above</dd>
<dt><code>timeout</code></dt>
<dd>see above </dd>
<p> Default value: timeout = 5</p>
<dt><code>pings</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>port</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd></dl>
</dl>
<dl>
<dd>Syntax changes for subsection <code>/[-_0-9a-zA-Z]+/</code> </dd>
<dl>
<dd>The following new variables are valid:</dd>
<dl>
<dt><code>binary</code> <i>(mandatory setting)</i></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>forks</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here. </p>
<p> Default value: forks = 5</p>
<dt><code>offset</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>step</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>tcptraceroute</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>timeout</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here. </p>
<p> Default value: timeout = 5</p>
<dt><code>pings</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>port</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd></dl>
</dl>
<dl>
<dd></dd></dl>
</dl>
<dl>
<dd>(End of dynamical grammar changes for example instance <tt>&quot;TCPPing&quot;</tt>.)</dd></dl>
<dt><code>TacacsPlus</code>: (See the separate module documentation for details about each variable.)</dt>
<dd>The following new variables are valid:</dd>
<dl>
<dd>
</dd><dl>
<dt><code>forks</code></dt>
<dd>see above </dd>
<p> Default value: forks = 5</p>
<dt><code>offset</code></dt>
<dd>see above</dd>
<dt><code>passwordfile</code></dt>
<dd>see above</dd>
<dt><code>secretfile</code></dt>
<dd>see above</dd>
<dt><code>step</code></dt>
<dd>see above</dd>
<dt><code>authtype</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.) </dd>
<p> Default value: authtype = ASCII</p>
<dt><code>mininterval</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.) </dd>
<p> Default value: mininterval = 1</p>
<dt><code>password</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>pings</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>port</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.) </dd>
<p> Default value: port = 49</p>
<dt><code>secret</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>timeout</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.) </dd>
<p> Default value: timeout = 5</p>
<dt><code>username</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.) </dd>
<p> This variable <i>dynamically</i> modifies the grammar based on its value.</dl>
</dl>
<dl>
<dd>Syntax changes for subsection <code>/[-_0-9a-zA-Z]+/</code> </dd>
<dl>
<dd>The following new variables are valid:</dd>
<dl>
<dt><code>forks</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here. </p>
<p> Default value: forks = 5</p>
<dt><code>offset</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>passwordfile</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>secretfile</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>step</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>authtype</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here. </dd>
<p> Default value: authtype = ASCII</p>
<dt><code>mininterval</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here. </dd>
<p> Default value: mininterval = 1</p>
<dt><code>password</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>pings</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>port</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here. </dd>
<p> Default value: port = 49</p>
<dt><code>secret</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>timeout</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here. </dd>
<p> Default value: timeout = 5</p>
<dt><code>username</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd></dl>
</dl>
<dl>
<dd></dd></dl>
</dl>
<dl>
<dd>(End of dynamical grammar changes for example instance <tt>&quot;TacacsPlus&quot;</tt>.)</dd></dl>
<dt><code>TelnetIOSPing</code>: (See the separate module documentation for details about each variable.)</dt>
<dd>The following new variables are valid:</dd>
<dl>
<dd>
</dd><dl>
<dt><code>forks</code></dt>
<dd>see above </dd>
<p> Default value: forks = 5</p>
<dt><code>offset</code></dt>
<dd>see above</dd>
<dt><code>packetsize</code></dt>
<dd>see above </dd>
<p> Default value: packetsize = 56</p>
<dt><code>step</code></dt>
<dd>see above</dd>
<dt><code>timeout</code></dt>
<dd>see above </dd>
<p> Default value: timeout = 5</p>
<dt><code>iospass</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.) </dd>
<p> This variable <i>dynamically</i> modifies the grammar based on its value.</p>
<dt><code>iosuser</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.) </dd>
<p> This variable <i>dynamically</i> modifies the grammar based on its value.</p>
<dt><code>pings</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>psource</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>source</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.) </dd>
<p> This variable <i>dynamically</i> modifies the grammar based on its value.</dl>
</dl>
<dl>
<dd>Syntax changes for subsection <code>/[-_0-9a-zA-Z]+/</code> </dd>
<dl>
<dd>The following new variables are valid:</dd>
<dl>
<dt><code>forks</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here. </p>
<p> Default value: forks = 5</p>
<dt><code>offset</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>packetsize</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here. </p>
<p> Default value: packetsize = 56</p>
<dt><code>step</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>timeout</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here. </p>
<p> Default value: timeout = 5</p>
<dt><code>iospass</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>iosuser</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>pings</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>psource</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>source</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd></dl>
</dl>
<dl>
<dd></dd></dl>
</dl>
<dl>
<dd>(End of dynamical grammar changes for example instance <tt>&quot;TelnetIOSPing&quot;</tt>.)</dd></dl>
<dt><code>TelnetJunOSPing</code>: (See the separate module documentation for details about each variable.)</dt>
<dd>The following new variables are valid:</dd>
<dl>
<dd>
</dd><dl>
<dt><code>forks</code></dt>
<dd>see above </dd>
<p> Default value: forks = 5</p>
<dt><code>offset</code></dt>
<dd>see above</dd>
<dt><code>packetsize</code></dt>
<dd>see above </dd>
<p> Default value: packetsize = 100</p>
<dt><code>step</code></dt>
<dd>see above</dd>
<dt><code>timeout</code></dt>
<dd>see above </dd>
<p> Default value: timeout = 5</p>
<dt><code>junospass</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.) </dd>
<p> This variable <i>dynamically</i> modifies the grammar based on its value.</p>
<dt><code>junosuser</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.) </dd>
<p> This variable <i>dynamically</i> modifies the grammar based on its value.</p>
<dt><code>pings</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>psource</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>source</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.) </dd>
<p> This variable <i>dynamically</i> modifies the grammar based on its value.</dl>
</dl>
<dl>
<dd>Syntax changes for subsection <code>/[-_0-9a-zA-Z]+/</code> </dd>
<dl>
<dd>The following new variables are valid:</dd>
<dl>
<dt><code>forks</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here. </p>
<p> Default value: forks = 5</p>
<dt><code>offset</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>packetsize</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here. </p>
<p> Default value: packetsize = 100</p>
<dt><code>step</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>timeout</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here. </p>
<p> Default value: timeout = 5</p>
<dt><code>junospass</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>junosuser</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>pings</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>psource</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>source</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd></dl>
</dl>
<dl>
<dd></dd></dl>
</dl>
<dl>
<dd>(End of dynamical grammar changes for example instance <tt>&quot;TelnetJunOSPing&quot;</tt>.)</dd></dl>
<dt><code>WebProxyFilter</code>: (See the separate module documentation for details about each variable.)</dt>
<dd>The following new variables are valid:</dd>
<dl>
<dd>
</dd><dl>
<dt><code>forks</code></dt>
<dd>see above </dd>
<p> Default value: forks = 5</p>
<dt><code>maxsize</code></dt>
<dd>see above </dd>
<p> Default value: maxsize = 2000</p>
<dt><code>min_interval</code></dt>
<dd>see above </dd>
<p> Default value: min_interval = 1</p>
<dt><code>offset</code></dt>
<dd>see above</dd>
<dt><code>step</code></dt>
<dd>see above</dd>
<dt><code>useragent</code></dt>
<dd>see above </dd>
<p> Default value: useragent = SmokePing/2.x (WebProxyFilter Probe)</p>
<dt><code>deny_re</code> <i>(mandatory setting)</i></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>more_hosts</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>pings</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.)</dd>
<dt><code>timeout</code></dt>
<dd>(This variable can be overridden target-specifically in the Targets section.) </dd>
<p> Default value: timeout = 2</dl>
</dl>
<dl>
<dd>Syntax changes for subsection <code>/[-_0-9a-zA-Z]+/</code> </dd>
<dl>
<dd>The following new variables are valid:</dd>
<dl>
<dt><code>forks</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here. </p>
<p> Default value: forks = 5</p>
<dt><code>maxsize</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here. </p>
<p> Default value: maxsize = 2000</p>
<dt><code>min_interval</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here. </p>
<p> Default value: min_interval = 1</p>
<dt><code>offset</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>step</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>useragent</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here. </p>
<p> Default value: useragent = SmokePing/2.x (WebProxyFilter Probe)</p>
<dt><code>deny_re</code> <i>(mandatory setting)</i></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>more_hosts</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>pings</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>timeout</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here. </dd>
<p> Default value: timeout = 2</dl>
</dl>
<dl>
<dd></dd></dl>
</dl>
<dl>
<dd>(End of dynamical grammar changes for example instance <tt>&quot;WebProxyFilter&quot;</tt>.)</dd></dl>
</dl>
</dl>
<dl>
<dd>(End of dynamical grammar changes for example instances of section <tt>&quot;/[-_0-9a-zA-Z]+/&quot;</tt>.)</dd></dl>
</dl>
<h3>*** Targets *** <i>(mandatory section)</i></h3>
<p>The Target Section defines the actual work of SmokePing. It contains a hierarchical list of hosts which mark the endpoints of the network connections the system should monitor. Each section can contain one host as well as other sections. By adding slaves you can measure the connection to an endpoint from multiple locations. </p>
<p> The following variables can be set in this section:</p>
<dl>
<dt><code>probe</code> <i>(mandatory setting)</i></dt>
<dd>The name of the probe module to be used for this host. The value of this variable gets propagated </dd>
<p> This variable <i>dynamically</i> modifies the grammar based on its value.</p>
<dt><code>menu</code> <i>(mandatory setting)</i></dt>
<dd>Menu entry for this section. If not set this will be set to the hostname.</dd>
<dt><code>title</code> <i>(mandatory setting)</i></dt>
<dd>Title of the page when it is displayed. This will be set to the hostname if left empty.</dd>
<dt><code>remark</code></dt>
<dd>An optional remark on the current section. It gets displayed on the webpage.</dd>
<dt><code>alerts</code></dt>
<dd>A comma separated list of alerts to check for this target. The alerts have to be setup in the Alerts section. Alerts are inherited by child nodes. Use an empty alerts definition to remove inherited alerts from the current target and its children.</dd>
<dt><code>slaves</code></dt>
<dd>List of slave servers. It gets inherited by all targets.</dd>
<dt><code>menuextra</code></dt>
<dd>HTML String to be added to the end of each menu entry. The <tt>&quot;{HOST}&quot;</tt> entry will be replaced by the host property of the relevant section. The <tt>&quot;{CLASS}&quot;</tt> entry will be replaced by the same class as the other tags in the manu line.</dd>
<dt><code>parents</code></dt>
<dd></dd></dl>
<p> The following sections are valid on level 1:</p>
<dl>
<dt><code>+/[-_0-9a-zA-Z]+/</code></dt>
<dd>Each target section can contain information about a host to monitor as well as further target sections. Most variables have already been described above. The expression above defines legal names for target sections. </dd>
<p> This section is <i>recursive</i>: it can contain subsection(s) with the same syntax. </p>
<p> The following variables can be set in this section:</p>
<dl>
<dd>
</dd><dl>
<dt><code>probe</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here. </dd>
<p> This variable <i>dynamically</i> modifies the grammar based on its value.</p>
<dt><code>menu</code></dt>
<dd>
</dd><dt><code>title</code></dt>
<dd>
</dd><dt><code>alerts</code></dt>
<dd>Comma separated list of alert names </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>note</code></dt>
<dd>Some information about this entry which does NOT get displayed on the web.</dd>
<dt><code>email</code></dt>
<dd>This is the contact address for the owner of the current host. In connection with the <code>DYNAMIC</code> hosts, the address will be used for sending the belowmentioned script.</dd>
<dt><code>host</code></dt>
<dd>There are three types of &#8220;hosts&#8221; in smokeping.</dd>
<dl>
<dd>
</dd><dl>
<dt>1.</dt>
<dd>The &#8216;hostname&#8217; is a name of a host you want to target from smokeping</dd>
<dt>2.</dt>
<dd>The string <code>DYNAMIC</code>. Is for machines that have a dynamic IP address. These boxes are required to regularly contact the SmokePing server to confirm their IP address.<br/>
&nbsp;<wbr>When starting SmokePing with the commandline argument <code>&#8211;email</code> it will add a secret password to each of the <code>DYNAMIC</code> host lines and send a script to the owner of each host. This script must be started periodically (cron) on the host in question to let smokeping know where the host is curently located. If the target machine supports SNMP SmokePing will also query the hosts sysContact, sysName and sysLocation properties to make sure it is still the same host.</dd>
<dt>3.</dt>
<dd>A space separated list of &#8216;target-path&#8217; entries (multihost target). All targets mentioned in this list will be displayed in one graph. Note that the graph will look different from the normal smokeping graphs. The syntax for multihost targets is as follows: </dd>
<pre> host = /world/town/host1 /world/town2/host33 /world/town2/host1~slave</pre>
</dl>
</dl>
<dl>
<dd></dd></dl>
<dt><code>remark</code></dt>
<dd>
</dd><dt><code>rawlog</code></dt>
<dd>Log the raw data, gathered for this target, in tab separated format, to a file with the same basename as the corresponding RRD file. Use posix strftime to format the timestamp to be put into the file name. The filename is built like this: </dd>
<pre> basename.strftime.csv</pre>
<p>Example: </p>
<pre> rawlog=%Y-%m-%d</pre>
<p>this would create a new logfile every day with a name like this: </p>
<pre> targethost.2004-05-03.csv</pre>
<dt><code>alertee</code></dt>
<dd>If you want to have alerts for this target and all targets below it go to a particular address on top of the address already specified in the alert, you can add it here. This can be a comma separated list of items. </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>slaves</code></dt>
<dd>The slave names must match the slaves you have setup in the slaves section. </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>menuextra</code></dt>
<dd>HTML String to be added to the end of each menu entry. The following tags will be replaced: </dd>
<pre> {HOST} -&gt; #$hostname
 {HOSTNAME} -&gt; $hostname
 {CLASS} -&gt; same class as the other tags in the menu line
 {HASH} -&gt; #</pre>
<p>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>parents</code></dt>
<dd>After setting up a hierarchy in the Presentation section of the configuration file you can use this property to assign an entry to alternate hierarchies. The format for parent entries is. </dd>
<pre> hierarchyA:/Node1/Node2 hierarchyB:/Node3</pre>
<p>The entries from all parent properties together will build a new tree for each hierarchy. With this method it is possible to make a single target show up multiple times in a tree. If you think this is a good thing, go ahead, nothing is stopping you. Since you do not only define the parent but the full path of the parent node, circular dependencies are not possible.</p>
<dt><code>hide</code></dt>
<dd>Set the hide property to &#8216;yes&#8217; to hide this host from the navigation menu and from search results. Note that if you set the hide property on a non leaf entry all subordinate entries will also disapear in the menu structure. If you know a direct link to a page it is still accessible. Pages which are hidden from the menu due to a parent being hidden will still show up in search results and in alternate hierarchies where they are below a non hidden parent. </dd>
<p> Default value: hide = no</p>
<dt><code>nomasterpoll</code></dt>
<dd>Use this in a master/slave setup where the master must not poll a particular target. The master will now skip this entry in its polling cycle. Note that if you set the hide property on a non leaf entry all subordinate entries will also disapear in the menu structure. You can still access them via direct link or via an alternate hierarchy. </dd>
<p> If you have no master/slave setup this will have a similar effect to the hide property, except that the menu entry will still show up, but will not contain any graphs. </p>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here. </p>
<p> Default value: nomasterpoll = no</dl>
</dl>
<dl>
<dd>The following sections are valid on level 2:</dd>
<dl>
<dt><code>++/[-_0-9a-zA-Z]+/</code></dt>
<dd>This section is <i>recursive</i>: it can contain subsection(s) with the same syntax.</dd></dl>
</dl>
<dl>
<dd></dd></dl>
</dl>
<p> Dynamical grammar changes for example values of variable <tt>&quot;probe&quot;</tt>:</p>
<dl>
<dt><code>AnotherDNS</code>: (See the separate module documentation for details about each variable.)</dt>
<dd>The following new variables are valid:</dd>
<dl>
<dd>
</dd><dl>
<dt><code>ipversion</code></dt>
<dd>see above</dd>
<dt><code>lookup</code></dt>
<dd>see above</dd>
<dt><code>mininterval</code></dt>
<dd>see above</dd>
<dt><code>pings</code></dt>
<dd>see above</dd>
<dt><code>port</code></dt>
<dd>see above</dd>
<dt><code>protocol</code></dt>
<dd>see above</dd>
<dt><code>recordtype</code></dt>
<dd>see above</dd>
<dt><code>require_answers</code></dt>
<dd>see above</dd>
<dt><code>require_noerror</code></dt>
<dd>see above</dd>
<dt><code>timeout</code></dt>
<dd>see above</dd></dl>
</dl>
<dl>
<dd>Syntax changes for subsection <code>/[-_0-9a-zA-Z]+/</code> </dd>
<dl>
<dd>The following new variables are valid:</dd>
<dl>
<dt><code>ipversion</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>lookup</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>mininterval</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>pings</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>port</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>protocol</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>recordtype</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>require_answers</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>require_noerror</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>timeout</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dl>
</dl>
<dl>
<dd></dd></dl>
</dl>
<dl>
<dd>(End of dynamical grammar changes for variable <tt>&quot;probe&quot;</tt> example value <tt>&quot;AnotherDNS&quot;</tt>.)</dd></dl>
<dt><code>AnotherSSH</code>: (See the separate module documentation for details about each variable.)</dt>
<dd>The following new variables are valid:</dd>
<dl>
<dd>
</dd><dl>
<dt><code>greeting</code></dt>
<dd>see above</dd>
<dt><code>interval</code></dt>
<dd>see above</dd>
<dt><code>mininterval</code></dt>
<dd>see above</dd>
<dt><code>pings</code></dt>
<dd>see above</dd>
<dt><code>port</code></dt>
<dd>see above</dd>
<dt><code>timeout</code></dt>
<dd>see above</dd></dl>
</dl>
<dl>
<dd>Syntax changes for subsection <code>/[-_0-9a-zA-Z]+/</code> </dd>
<dl>
<dd>The following new variables are valid:</dd>
<dl>
<dt><code>greeting</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>interval</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>mininterval</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>pings</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>port</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>timeout</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dl>
</dl>
<dl>
<dd></dd></dl>
</dl>
<dl>
<dd>(End of dynamical grammar changes for variable <tt>&quot;probe&quot;</tt> example value <tt>&quot;AnotherSSH&quot;</tt>.)</dd></dl>
<dt><code>CiscoRTTMonDNS</code>: (See the separate module documentation for details about each variable.)</dt>
<dd>The following new variables are valid:</dd>
<dl>
<dd>
</dd><dl>
<dt><code>ioshost</code></dt>
<dd>see above</dd>
<dt><code>iosint</code></dt>
<dd>see above</dd>
<dt><code>name</code></dt>
<dd>see above</dd>
<dt><code>pings</code></dt>
<dd>see above</dd>
<dt><code>timeout</code></dt>
<dd>see above</dd></dl>
</dl>
<dl>
<dd>Syntax changes for subsection <code>/[-_0-9a-zA-Z]+/</code> </dd>
<dl>
<dd>The following new variables are valid:</dd>
<dl>
<dt><code>ioshost</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>iosint</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>name</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>pings</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>timeout</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dl>
</dl>
<dl>
<dd></dd></dl>
</dl>
<dl>
<dd>(End of dynamical grammar changes for variable <tt>&quot;probe&quot;</tt> example value <tt>&quot;CiscoRTTMonDNS&quot;</tt>.)</dd></dl>
<dt><code>CiscoRTTMonEchoICMP</code>: (See the separate module documentation for details about each variable.)</dt>
<dd>The following new variables are valid:</dd>
<dl>
<dd>
</dd><dl>
<dt><code>ioshost</code></dt>
<dd>see above</dd>
<dt><code>iosint</code></dt>
<dd>see above</dd>
<dt><code>packetsize</code></dt>
<dd>see above</dd>
<dt><code>pings</code></dt>
<dd>see above</dd>
<dt><code>timeout</code></dt>
<dd>see above</dd>
<dt><code>tos</code></dt>
<dd>see above</dd>
<dt><code>vrf</code></dt>
<dd>see above</dd></dl>
</dl>
<dl>
<dd>Syntax changes for subsection <code>/[-_0-9a-zA-Z]+/</code> </dd>
<dl>
<dd>The following new variables are valid:</dd>
<dl>
<dt><code>ioshost</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>iosint</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>packetsize</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>pings</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>timeout</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>tos</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>vrf</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dl>
</dl>
<dl>
<dd></dd></dl>
</dl>
<dl>
<dd>(End of dynamical grammar changes for variable <tt>&quot;probe&quot;</tt> example value <tt>&quot;CiscoRTTMonEchoICMP&quot;</tt>.)</dd></dl>
<dt><code>CiscoRTTMonTcpConnect</code>: (See the separate module documentation for details about each variable.)</dt>
<dd>The following new variables are valid:</dd>
<dl>
<dd>
</dd><dl>
<dt><code>ioshost</code></dt>
<dd>see above</dd>
<dt><code>iosint</code></dt>
<dd>see above</dd>
<dt><code>pings</code></dt>
<dd>see above</dd>
<dt><code>port</code></dt>
<dd>see above</dd>
<dt><code>timeout</code></dt>
<dd>see above</dd>
<dt><code>tos</code></dt>
<dd>see above</dd></dl>
</dl>
<dl>
<dd>Syntax changes for subsection <code>/[-_0-9a-zA-Z]+/</code> </dd>
<dl>
<dd>The following new variables are valid:</dd>
<dl>
<dt><code>ioshost</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>iosint</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>pings</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>port</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>timeout</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>tos</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dl>
</dl>
<dl>
<dd></dd></dl>
</dl>
<dl>
<dd>(End of dynamical grammar changes for variable <tt>&quot;probe&quot;</tt> example value <tt>&quot;CiscoRTTMonTcpConnect&quot;</tt>.)</dd></dl>
<dt><code>Curl</code>: (See the separate module documentation for details about each variable.)</dt>
<dd>The following new variables are valid:</dd>
<dl>
<dd>
</dd><dl>
<dt><code>agent</code></dt>
<dd>see above</dd>
<dt><code>expect</code></dt>
<dd>see above</dd>
<dt><code>extraargs</code></dt>
<dd>see above</dd>
<dt><code>extrare</code></dt>
<dd>see above</dd>
<dt><code>follow_redirects</code></dt>
<dd>see above</dd>
<dt><code>include_redirects</code></dt>
<dd>see above</dd>
<dt><code>insecure_ssl</code></dt>
<dd>see above</dd>
<dt><code>interface</code></dt>
<dd>see above</dd>
<dt><code>pings</code></dt>
<dd>see above</dd>
<dt><code>ssl2</code></dt>
<dd>see above</dd>
<dt><code>timeout</code></dt>
<dd>see above</dd>
<dt><code>urlformat</code></dt>
<dd>see above</dd></dl>
</dl>
<dl>
<dd>Syntax changes for subsection <code>/[-_0-9a-zA-Z]+/</code> </dd>
<dl>
<dd>The following new variables are valid:</dd>
<dl>
<dt><code>agent</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>expect</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>extraargs</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>extrare</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>follow_redirects</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>include_redirects</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>insecure_ssl</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>interface</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>pings</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>ssl2</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>timeout</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>urlformat</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dl>
</dl>
<dl>
<dd></dd></dl>
</dl>
<dl>
<dd>(End of dynamical grammar changes for variable <tt>&quot;probe&quot;</tt> example value <tt>&quot;Curl&quot;</tt>.)</dd></dl>
<dt><code>DNS</code>: (See the separate module documentation for details about each variable.)</dt>
<dd>The following new variables are valid:</dd>
<dl>
<dd>
</dd><dl>
<dt><code>lookup</code></dt>
<dd>see above</dd>
<dt><code>pings</code></dt>
<dd>see above</dd>
<dt><code>server</code></dt>
<dd>see above</dd></dl>
</dl>
<dl>
<dd>Syntax changes for subsection <code>/[-_0-9a-zA-Z]+/</code> </dd>
<dl>
<dd>The following new variables are valid:</dd>
<dl>
<dt><code>lookup</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>pings</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>server</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dl>
</dl>
<dl>
<dd></dd></dl>
</dl>
<dl>
<dd>(End of dynamical grammar changes for variable <tt>&quot;probe&quot;</tt> example value <tt>&quot;DNS&quot;</tt>.)</dd></dl>
<dt><code>DismanPing</code>: (See the separate module documentation for details about each variable.)</dt>
<dd>The following new variables are valid:</dd>
<dl>
<dd>
</dd><dl>
<dt><code>ownerindex</code></dt>
<dd>see above</dd>
<dt><code>packetsize</code></dt>
<dd>see above</dd>
<dt><code>pinghost</code></dt>
<dd>see above</dd>
<dt><code>pingsrc</code></dt>
<dd>see above</dd></dl>
</dl>
<dl>
<dd>Syntax changes for subsection <code>/[-_0-9a-zA-Z]+/</code> </dd>
<dl>
<dd>The following new variables are valid:</dd>
<dl>
<dt><code>ownerindex</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>packetsize</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>pinghost</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>pingsrc</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dl>
</dl>
<dl>
<dd></dd></dl>
</dl>
<dl>
<dd>(End of dynamical grammar changes for variable <tt>&quot;probe&quot;</tt> example value <tt>&quot;DismanPing&quot;</tt>.)</dd></dl>
<dt><code>EchoPing</code>: (See the separate module documentation for details about each variable.)</dt>
<dd>The following new variables are valid:</dd>
<dl>
<dd>
</dd><dl>
<dt><code>extraopts</code></dt>
<dd>see above</dd>
<dt><code>fill</code></dt>
<dd>see above</dd>
<dt><code>ipversion</code></dt>
<dd>see above</dd>
<dt><code>pings</code></dt>
<dd>see above</dd>
<dt><code>priority</code></dt>
<dd>see above</dd>
<dt><code>size</code></dt>
<dd>see above</dd>
<dt><code>timeout</code></dt>
<dd>see above</dd>
<dt><code>tos</code></dt>
<dd>see above</dd>
<dt><code>udp</code></dt>
<dd>see above</dd>
<dt><code>waittime</code></dt>
<dd>see above</dd></dl>
</dl>
<dl>
<dd>Syntax changes for subsection <code>/[-_0-9a-zA-Z]+/</code> </dd>
<dl>
<dd>The following new variables are valid:</dd>
<dl>
<dt><code>extraopts</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>fill</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>ipversion</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>pings</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>priority</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>size</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>timeout</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>tos</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>udp</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>waittime</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dl>
</dl>
<dl>
<dd></dd></dl>
</dl>
<dl>
<dd>(End of dynamical grammar changes for variable <tt>&quot;probe&quot;</tt> example value <tt>&quot;EchoPing&quot;</tt>.)</dd></dl>
<dt><code>EchoPingChargen</code>: (See the separate module documentation for details about each variable.)</dt>
<dd>The following new variables are valid:</dd>
<dl>
<dd>
</dd><dl>
<dt><code>extraopts</code></dt>
<dd>see above</dd>
<dt><code>fill</code></dt>
<dd>see above</dd>
<dt><code>ipversion</code></dt>
<dd>see above</dd>
<dt><code>pings</code></dt>
<dd>see above</dd>
<dt><code>priority</code></dt>
<dd>see above</dd>
<dt><code>size</code></dt>
<dd>see above</dd>
<dt><code>timeout</code></dt>
<dd>see above</dd>
<dt><code>tos</code></dt>
<dd>see above</dd>
<dt><code>waittime</code></dt>
<dd>see above</dd></dl>
</dl>
<dl>
<dd>Syntax changes for subsection <code>/[-_0-9a-zA-Z]+/</code> </dd>
<dl>
<dd>The following new variables are valid:</dd>
<dl>
<dt><code>extraopts</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>fill</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>ipversion</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>pings</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>priority</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>size</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>timeout</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>tos</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>waittime</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dl>
</dl>
<dl>
<dd></dd></dl>
</dl>
<dl>
<dd>(End of dynamical grammar changes for variable <tt>&quot;probe&quot;</tt> example value <tt>&quot;EchoPingChargen&quot;</tt>.)</dd></dl>
<dt><code>EchoPingDNS</code>: (See the separate module documentation for details about each variable.)</dt>
<dd>The following new variables are valid:</dd>
<dl>
<dd>
</dd><dl>
<dt><code>dns_request</code></dt>
<dd>see above</dd>
<dt><code>dns_tcp</code></dt>
<dd>see above</dd>
<dt><code>dns_type</code></dt>
<dd>see above</dd>
<dt><code>extraopts</code></dt>
<dd>see above</dd>
<dt><code>ipversion</code></dt>
<dd>see above</dd>
<dt><code>pings</code></dt>
<dd>see above</dd>
<dt><code>plugin</code></dt>
<dd>see above</dd>
<dt><code>pluginargs</code></dt>
<dd>see above</dd>
<dt><code>priority</code></dt>
<dd>see above</dd>
<dt><code>timeout</code></dt>
<dd>see above</dd>
<dt><code>tos</code></dt>
<dd>see above</dd>
<dt><code>waittime</code></dt>
<dd>see above</dd></dl>
</dl>
<dl>
<dd>Syntax changes for subsection <code>/[-_0-9a-zA-Z]+/</code> </dd>
<dl>
<dd>The following new variables are valid:</dd>
<dl>
<dt><code>dns_request</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>dns_tcp</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>dns_type</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>extraopts</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>ipversion</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>pings</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>plugin</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>pluginargs</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>priority</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>timeout</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>tos</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>waittime</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dl>
</dl>
<dl>
<dd></dd></dl>
</dl>
<dl>
<dd>(End of dynamical grammar changes for variable <tt>&quot;probe&quot;</tt> example value <tt>&quot;EchoPingDNS&quot;</tt>.)</dd></dl>
<dt><code>EchoPingDiscard</code>: (See the separate module documentation for details about each variable.)</dt>
<dd>The following new variables are valid:</dd>
<dl>
<dd>
</dd><dl>
<dt><code>extraopts</code></dt>
<dd>see above</dd>
<dt><code>fill</code></dt>
<dd>see above</dd>
<dt><code>ipversion</code></dt>
<dd>see above</dd>
<dt><code>pings</code></dt>
<dd>see above</dd>
<dt><code>priority</code></dt>
<dd>see above</dd>
<dt><code>size</code></dt>
<dd>see above</dd>
<dt><code>timeout</code></dt>
<dd>see above</dd>
<dt><code>tos</code></dt>
<dd>see above</dd>
<dt><code>udp</code></dt>
<dd>see above</dd>
<dt><code>waittime</code></dt>
<dd>see above</dd></dl>
</dl>
<dl>
<dd>Syntax changes for subsection <code>/[-_0-9a-zA-Z]+/</code> </dd>
<dl>
<dd>The following new variables are valid:</dd>
<dl>
<dt><code>extraopts</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>fill</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>ipversion</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>pings</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>priority</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>size</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>timeout</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>tos</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>udp</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>waittime</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dl>
</dl>
<dl>
<dd></dd></dl>
</dl>
<dl>
<dd>(End of dynamical grammar changes for variable <tt>&quot;probe&quot;</tt> example value <tt>&quot;EchoPingDiscard&quot;</tt>.)</dd></dl>
<dt><code>EchoPingHttp</code>: (See the separate module documentation for details about each variable.)</dt>
<dd>The following new variables are valid:</dd>
<dl>
<dd>
</dd><dl>
<dt><code>accept_redirects</code></dt>
<dd>see above</dd>
<dt><code>extraopts</code></dt>
<dd>see above</dd>
<dt><code>ignore_cache</code></dt>
<dd>see above</dd>
<dt><code>ipversion</code></dt>
<dd>see above</dd>
<dt><code>pings</code></dt>
<dd>see above</dd>
<dt><code>port</code></dt>
<dd>see above</dd>
<dt><code>priority</code></dt>
<dd>see above</dd>
<dt><code>revalidate_data</code></dt>
<dd>see above</dd>
<dt><code>timeout</code></dt>
<dd>see above</dd>
<dt><code>tos</code></dt>
<dd>see above</dd>
<dt><code>url</code></dt>
<dd>see above</dd>
<dt><code>waittime</code></dt>
<dd>see above</dd></dl>
</dl>
<dl>
<dd>Syntax changes for subsection <code>/[-_0-9a-zA-Z]+/</code> </dd>
<dl>
<dd>The following new variables are valid:</dd>
<dl>
<dt><code>accept_redirects</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>extraopts</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>ignore_cache</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>ipversion</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>pings</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>port</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>priority</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>revalidate_data</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>timeout</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>tos</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>url</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>waittime</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dl>
</dl>
<dl>
<dd></dd></dl>
</dl>
<dl>
<dd>(End of dynamical grammar changes for variable <tt>&quot;probe&quot;</tt> example value <tt>&quot;EchoPingHttp&quot;</tt>.)</dd></dl>
<dt><code>EchoPingHttps</code>: (See the separate module documentation for details about each variable.)</dt>
<dd>The following new variables are valid:</dd>
<dl>
<dd>
</dd><dl>
<dt><code>accept_redirects</code></dt>
<dd>see above</dd>
<dt><code>extraopts</code></dt>
<dd>see above</dd>
<dt><code>ignore_cache</code></dt>
<dd>see above</dd>
<dt><code>ipversion</code></dt>
<dd>see above</dd>
<dt><code>pings</code></dt>
<dd>see above</dd>
<dt><code>port</code></dt>
<dd>see above</dd>
<dt><code>priority</code></dt>
<dd>see above</dd>
<dt><code>prot</code></dt>
<dd>see above</dd>
<dt><code>revalidate_data</code></dt>
<dd>see above</dd>
<dt><code>timeout</code></dt>
<dd>see above</dd>
<dt><code>tos</code></dt>
<dd>see above</dd>
<dt><code>url</code></dt>
<dd>see above</dd>
<dt><code>waittime</code></dt>
<dd>see above</dd></dl>
</dl>
<dl>
<dd>Syntax changes for subsection <code>/[-_0-9a-zA-Z]+/</code> </dd>
<dl>
<dd>The following new variables are valid:</dd>
<dl>
<dt><code>accept_redirects</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>extraopts</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>ignore_cache</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>ipversion</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>pings</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>port</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>priority</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>prot</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>revalidate_data</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>timeout</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>tos</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>url</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>waittime</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dl>
</dl>
<dl>
<dd></dd></dl>
</dl>
<dl>
<dd>(End of dynamical grammar changes for variable <tt>&quot;probe&quot;</tt> example value <tt>&quot;EchoPingHttps&quot;</tt>.)</dd></dl>
<dt><code>EchoPingIcp</code>: (See the separate module documentation for details about each variable.)</dt>
<dd>The following new variables are valid:</dd>
<dl>
<dd>
</dd><dl>
<dt><code>extraopts</code></dt>
<dd>see above</dd>
<dt><code>ipversion</code></dt>
<dd>see above</dd>
<dt><code>pings</code></dt>
<dd>see above</dd>
<dt><code>priority</code></dt>
<dd>see above</dd>
<dt><code>timeout</code></dt>
<dd>see above</dd>
<dt><code>tos</code></dt>
<dd>see above</dd>
<dt><code>url</code></dt>
<dd>see above</dd>
<dt><code>waittime</code></dt>
<dd>see above</dd></dl>
</dl>
<dl>
<dd>Syntax changes for subsection <code>/[-_0-9a-zA-Z]+/</code> </dd>
<dl>
<dd>The following new variables are valid:</dd>
<dl>
<dt><code>extraopts</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>ipversion</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>pings</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>priority</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>timeout</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>tos</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>url</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>waittime</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dl>
</dl>
<dl>
<dd></dd></dl>
</dl>
<dl>
<dd>(End of dynamical grammar changes for variable <tt>&quot;probe&quot;</tt> example value <tt>&quot;EchoPingIcp&quot;</tt>.)</dd></dl>
<dt><code>EchoPingLDAP</code>: (See the separate module documentation for details about each variable.)</dt>
<dd>The following new variables are valid:</dd>
<dl>
<dd>
</dd><dl>
<dt><code>extraopts</code></dt>
<dd>see above</dd>
<dt><code>ipversion</code></dt>
<dd>see above</dd>
<dt><code>ldap_base</code></dt>
<dd>see above</dd>
<dt><code>ldap_request</code></dt>
<dd>see above</dd>
<dt><code>ldap_scope</code></dt>
<dd>see above</dd>
<dt><code>pings</code></dt>
<dd>see above</dd>
<dt><code>plugin</code></dt>
<dd>see above</dd>
<dt><code>pluginargs</code></dt>
<dd>see above</dd>
<dt><code>priority</code></dt>
<dd>see above</dd>
<dt><code>timeout</code></dt>
<dd>see above</dd>
<dt><code>tos</code></dt>
<dd>see above</dd>
<dt><code>waittime</code></dt>
<dd>see above</dd></dl>
</dl>
<dl>
<dd>Syntax changes for subsection <code>/[-_0-9a-zA-Z]+/</code> </dd>
<dl>
<dd>The following new variables are valid:</dd>
<dl>
<dt><code>extraopts</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>ipversion</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>ldap_base</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>ldap_request</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>ldap_scope</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>pings</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>plugin</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>pluginargs</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>priority</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>timeout</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>tos</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>waittime</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dl>
</dl>
<dl>
<dd></dd></dl>
</dl>
<dl>
<dd>(End of dynamical grammar changes for variable <tt>&quot;probe&quot;</tt> example value <tt>&quot;EchoPingLDAP&quot;</tt>.)</dd></dl>
<dt><code>EchoPingPlugin</code>: (See the separate module documentation for details about each variable.)</dt>
<dd>The following new variables are valid:</dd>
<dl>
<dd>
</dd><dl>
<dt><code>extraopts</code></dt>
<dd>see above</dd>
<dt><code>ipversion</code></dt>
<dd>see above</dd>
<dt><code>pings</code></dt>
<dd>see above</dd>
<dt><code>plugin</code></dt>
<dd>see above</dd>
<dt><code>pluginargs</code></dt>
<dd>see above</dd>
<dt><code>priority</code></dt>
<dd>see above</dd>
<dt><code>timeout</code></dt>
<dd>see above</dd>
<dt><code>tos</code></dt>
<dd>see above</dd>
<dt><code>waittime</code></dt>
<dd>see above</dd></dl>
</dl>
<dl>
<dd>Syntax changes for subsection <code>/[-_0-9a-zA-Z]+/</code> </dd>
<dl>
<dd>The following new variables are valid:</dd>
<dl>
<dt><code>extraopts</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>ipversion</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>pings</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>plugin</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>pluginargs</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>priority</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>timeout</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>tos</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>waittime</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dl>
</dl>
<dl>
<dd></dd></dl>
</dl>
<dl>
<dd>(End of dynamical grammar changes for variable <tt>&quot;probe&quot;</tt> example value <tt>&quot;EchoPingPlugin&quot;</tt>.)</dd></dl>
<dt><code>EchoPingSmtp</code>: (See the separate module documentation for details about each variable.)</dt>
<dd>The following new variables are valid:</dd>
<dl>
<dd>
</dd><dl>
<dt><code>extraopts</code></dt>
<dd>see above</dd>
<dt><code>ipversion</code></dt>
<dd>see above</dd>
<dt><code>pings</code></dt>
<dd>see above</dd>
<dt><code>priority</code></dt>
<dd>see above</dd>
<dt><code>timeout</code></dt>
<dd>see above</dd>
<dt><code>tos</code></dt>
<dd>see above</dd>
<dt><code>waittime</code></dt>
<dd>see above</dd></dl>
</dl>
<dl>
<dd>Syntax changes for subsection <code>/[-_0-9a-zA-Z]+/</code> </dd>
<dl>
<dd>The following new variables are valid:</dd>
<dl>
<dt><code>extraopts</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>ipversion</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>pings</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>priority</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>timeout</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>tos</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>waittime</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dl>
</dl>
<dl>
<dd></dd></dl>
</dl>
<dl>
<dd>(End of dynamical grammar changes for variable <tt>&quot;probe&quot;</tt> example value <tt>&quot;EchoPingSmtp&quot;</tt>.)</dd></dl>
<dt><code>EchoPingWhois</code>: (See the separate module documentation for details about each variable.)</dt>
<dd>The following new variables are valid:</dd>
<dl>
<dd>
</dd><dl>
<dt><code>extraopts</code></dt>
<dd>see above</dd>
<dt><code>ipversion</code></dt>
<dd>see above</dd>
<dt><code>pings</code></dt>
<dd>see above</dd>
<dt><code>plugin</code></dt>
<dd>see above</dd>
<dt><code>pluginargs</code></dt>
<dd>see above</dd>
<dt><code>priority</code></dt>
<dd>see above</dd>
<dt><code>timeout</code></dt>
<dd>see above</dd>
<dt><code>tos</code></dt>
<dd>see above</dd>
<dt><code>waittime</code></dt>
<dd>see above</dd>
<dt><code>whois_request</code></dt>
<dd>see above</dd></dl>
</dl>
<dl>
<dd>Syntax changes for subsection <code>/[-_0-9a-zA-Z]+/</code> </dd>
<dl>
<dd>The following new variables are valid:</dd>
<dl>
<dt><code>extraopts</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>ipversion</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>pings</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>plugin</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>pluginargs</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>priority</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>timeout</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>tos</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>waittime</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>whois_request</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dl>
</dl>
<dl>
<dd></dd></dl>
</dl>
<dl>
<dd>(End of dynamical grammar changes for variable <tt>&quot;probe&quot;</tt> example value <tt>&quot;EchoPingWhois&quot;</tt>.)</dd></dl>
<dt><code>FPing</code>: (See the separate module documentation for details about each variable.)</dt>
<dd>No changes that can be automatically described. </dd>
<p> (End of dynamical grammar changes for variable <tt>&quot;probe&quot;</tt> example value <tt>&quot;FPing&quot;</tt>.)</p>
<dt><code>FPing6</code>: (See the separate module documentation for details about each variable.)</dt>
<dd>No changes that can be automatically described. </dd>
<p> (End of dynamical grammar changes for variable <tt>&quot;probe&quot;</tt> example value <tt>&quot;FPing6&quot;</tt>.)</p>
<dt><code>FTPtransfer</code>: (See the separate module documentation for details about each variable.)</dt>
<dd>The following new variables are valid:</dd>
<dl>
<dd>
</dd><dl>
<dt><code>localaddr</code></dt>
<dd>see above</dd>
<dt><code>passive</code></dt>
<dd>see above</dd>
<dt><code>password</code></dt>
<dd>see above</dd>
<dt><code>pings</code></dt>
<dd>see above</dd>
<dt><code>port</code></dt>
<dd>see above</dd>
<dt><code>timeout</code></dt>
<dd>see above</dd>
<dt><code>username</code></dt>
<dd>see above</dd></dl>
</dl>
<dl>
<dd>Syntax changes for subsection <code>/[-_0-9a-zA-Z]+/</code> </dd>
<dl>
<dd>The following new variables are valid:</dd>
<dl>
<dt><code>localaddr</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>passive</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>password</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>pings</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>port</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>timeout</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>username</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dl>
</dl>
<dl>
<dd></dd></dl>
</dl>
<dl>
<dd>(End of dynamical grammar changes for variable <tt>&quot;probe&quot;</tt> example value <tt>&quot;FTPtransfer&quot;</tt>.)</dd></dl>
<dt><code>IOSPing</code>: (See the separate module documentation for details about each variable.)</dt>
<dd>The following new variables are valid:</dd>
<dl>
<dd>
</dd><dl>
<dt><code>ioshost</code></dt>
<dd>see above</dd>
<dt><code>iosint</code></dt>
<dd>see above</dd>
<dt><code>iosuser</code></dt>
<dd>see above</dd>
<dt><code>pings</code></dt>
<dd>see above</dd></dl>
</dl>
<dl>
<dd>Syntax changes for subsection <code>/[-_0-9a-zA-Z]+/</code> </dd>
<dl>
<dd>The following new variables are valid:</dd>
<dl>
<dt><code>ioshost</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>iosint</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>iosuser</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>pings</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dl>
</dl>
<dl>
<dd></dd></dl>
</dl>
<dl>
<dd>(End of dynamical grammar changes for variable <tt>&quot;probe&quot;</tt> example value <tt>&quot;IOSPing&quot;</tt>.)</dd></dl>
<dt><code>LDAP</code>: (See the separate module documentation for details about each variable.)</dt>
<dd>The following new variables are valid:</dd>
<dl>
<dd>
</dd><dl>
<dt><code>attrs</code></dt>
<dd>see above</dd>
<dt><code>base</code></dt>
<dd>see above</dd>
<dt><code>binddn</code></dt>
<dd>see above</dd>
<dt><code>filter</code></dt>
<dd>see above</dd>
<dt><code>mininterval</code></dt>
<dd>see above</dd>
<dt><code>password</code></dt>
<dd>see above</dd>
<dt><code>pings</code></dt>
<dd>see above</dd>
<dt><code>port</code></dt>
<dd>see above</dd>
<dt><code>scope</code></dt>
<dd>see above</dd>
<dt><code>start_tls</code></dt>
<dd>see above</dd>
<dt><code>timeout</code></dt>
<dd>see above</dd>
<dt><code>version</code></dt>
<dd>see above</dd></dl>
</dl>
<dl>
<dd>Syntax changes for subsection <code>/[-_0-9a-zA-Z]+/</code> </dd>
<dl>
<dd>The following new variables are valid:</dd>
<dl>
<dt><code>attrs</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>base</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>binddn</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>filter</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>mininterval</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>password</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>pings</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>port</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>scope</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>start_tls</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>timeout</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>version</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dl>
</dl>
<dl>
<dd></dd></dl>
</dl>
<dl>
<dd>(End of dynamical grammar changes for variable <tt>&quot;probe&quot;</tt> example value <tt>&quot;LDAP&quot;</tt>.)</dd></dl>
<dt><code>NFSping</code>: (See the separate module documentation for details about each variable.)</dt>
<dd>No changes that can be automatically described. </dd>
<p> (End of dynamical grammar changes for variable <tt>&quot;probe&quot;</tt> example value <tt>&quot;NFSping&quot;</tt>.)</p>
<dt><code>OpenSSHEOSPing</code>: (See the separate module documentation for details about each variable.)</dt>
<dd>The following new variables are valid:</dd>
<dl>
<dd>
</dd><dl>
<dt><code>eospass</code></dt>
<dd>see above</dd>
<dt><code>eosuser</code></dt>
<dd>see above</dd>
<dt><code>pings</code></dt>
<dd>see above</dd>
<dt><code>psource</code></dt>
<dd>see above</dd>
<dt><code>source</code></dt>
<dd>see above</dd>
<dt><code>unpriv</code></dt>
<dd>see above</dd></dl>
</dl>
<dl>
<dd>Syntax changes for subsection <code>/[-_0-9a-zA-Z]+/</code> </dd>
<dl>
<dd>The following new variables are valid:</dd>
<dl>
<dt><code>eospass</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>eosuser</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>pings</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>psource</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>source</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>unpriv</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dl>
</dl>
<dl>
<dd></dd></dl>
</dl>
<dl>
<dd>(End of dynamical grammar changes for variable <tt>&quot;probe&quot;</tt> example value <tt>&quot;OpenSSHEOSPing&quot;</tt>.)</dd></dl>
<dt><code>OpenSSHJunOSPing</code>: (See the separate module documentation for details about each variable.)</dt>
<dd>The following new variables are valid:</dd>
<dl>
<dd>
</dd><dl>
<dt><code>junospass</code></dt>
<dd>see above</dd>
<dt><code>junosuser</code></dt>
<dd>see above</dd>
<dt><code>pings</code></dt>
<dd>see above</dd>
<dt><code>psource</code></dt>
<dd>see above</dd>
<dt><code>source</code></dt>
<dd>see above</dd></dl>
</dl>
<dl>
<dd>Syntax changes for subsection <code>/[-_0-9a-zA-Z]+/</code> </dd>
<dl>
<dd>The following new variables are valid:</dd>
<dl>
<dt><code>junospass</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>junosuser</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>pings</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>psource</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>source</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dl>
</dl>
<dl>
<dd></dd></dl>
</dl>
<dl>
<dd>(End of dynamical grammar changes for variable <tt>&quot;probe&quot;</tt> example value <tt>&quot;OpenSSHJunOSPing&quot;</tt>.)</dd></dl>
<dt><code>Qstat</code>: (See the separate module documentation for details about each variable.)</dt>
<dd>The following new variables are valid:</dd>
<dl>
<dd>
</dd><dl>
<dt><code>pings</code></dt>
<dd>see above</dd></dl>
</dl>
<dl>
<dd>Syntax changes for subsection <code>/[-_0-9a-zA-Z]+/</code> </dd>
<dl>
<dd>The following new variables are valid:</dd>
<dl>
<dt><code>pings</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dl>
</dl>
<dl>
<dd></dd></dl>
</dl>
<dl>
<dd>(End of dynamical grammar changes for variable <tt>&quot;probe&quot;</tt> example value <tt>&quot;Qstat&quot;</tt>.)</dd></dl>
<dt><code>Radius</code>: (See the separate module documentation for details about each variable.)</dt>
<dd>The following new variables are valid:</dd>
<dl>
<dd>
</dd><dl>
<dt><code>allowreject</code></dt>
<dd>see above</dd>
<dt><code>mininterval</code></dt>
<dd>see above</dd>
<dt><code>nas_ip_address</code></dt>
<dd>see above</dd>
<dt><code>password</code></dt>
<dd>see above</dd>
<dt><code>pings</code></dt>
<dd>see above</dd>
<dt><code>port</code></dt>
<dd>see above</dd>
<dt><code>secret</code></dt>
<dd>see above</dd>
<dt><code>timeout</code></dt>
<dd>see above</dd>
<dt><code>username</code></dt>
<dd>see above</dd></dl>
</dl>
<dl>
<dd>Syntax changes for subsection <code>/[-_0-9a-zA-Z]+/</code> </dd>
<dl>
<dd>The following new variables are valid:</dd>
<dl>
<dt><code>allowreject</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>mininterval</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>nas_ip_address</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>password</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>pings</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>port</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>secret</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>timeout</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>username</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dl>
</dl>
<dl>
<dd></dd></dl>
</dl>
<dl>
<dd>(End of dynamical grammar changes for variable <tt>&quot;probe&quot;</tt> example value <tt>&quot;Radius&quot;</tt>.)</dd></dl>
<dt><code>RemoteFPing</code>: (See the separate module documentation for details about each variable.)</dt>
<dd>No changes that can be automatically described. </dd>
<p> (End of dynamical grammar changes for variable <tt>&quot;probe&quot;</tt> example value <tt>&quot;RemoteFPing&quot;</tt>.)</p>
<dt><code>SSH</code>: (See the separate module documentation for details about each variable.)</dt>
<dd>The following new variables are valid:</dd>
<dl>
<dd>
</dd><dl>
<dt><code>keytype</code></dt>
<dd>see above</dd>
<dt><code>pings</code></dt>
<dd>see above</dd>
<dt><code>port</code></dt>
<dd>see above</dd></dl>
</dl>
<dl>
<dd>Syntax changes for subsection <code>/[-_0-9a-zA-Z]+/</code> </dd>
<dl>
<dd>The following new variables are valid:</dd>
<dl>
<dt><code>keytype</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>pings</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>port</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dl>
</dl>
<dl>
<dd></dd></dl>
</dl>
<dl>
<dd>(End of dynamical grammar changes for variable <tt>&quot;probe&quot;</tt> example value <tt>&quot;SSH&quot;</tt>.)</dd></dl>
<dt><code>SendEmail</code>: (See the separate module documentation for details about each variable.)</dt>
<dd>The following new variables are valid:</dd>
<dl>
<dd>
</dd><dl>
<dt><code>pings</code></dt>
<dd>see above</dd>
<dt><code>port</code></dt>
<dd>see above</dd></dl>
</dl>
<dl>
<dd>Syntax changes for subsection <code>/[-_0-9a-zA-Z]+/</code> </dd>
<dl>
<dd>The following new variables are valid:</dd>
<dl>
<dt><code>pings</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>port</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dl>
</dl>
<dl>
<dd></dd></dl>
</dl>
<dl>
<dd>(End of dynamical grammar changes for variable <tt>&quot;probe&quot;</tt> example value <tt>&quot;SendEmail&quot;</tt>.)</dd></dl>
<dt><code>SipSak</code>: (See the separate module documentation for details about each variable.)</dt>
<dd>The following new variables are valid:</dd>
<dl>
<dd>
</dd><dl>
<dt><code>keep_second</code></dt>
<dd>see above</dd>
<dt><code>params</code></dt>
<dd>see above</dd>
<dt><code>pings</code></dt>
<dd>see above</dd>
<dt><code>port</code></dt>
<dd>see above</dd>
<dt><code>user</code></dt>
<dd>see above</dd></dl>
</dl>
<dl>
<dd>Syntax changes for subsection <code>/[-_0-9a-zA-Z]+/</code> </dd>
<dl>
<dd>The following new variables are valid:</dd>
<dl>
<dt><code>keep_second</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>params</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>pings</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>port</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>user</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dl>
</dl>
<dl>
<dd></dd></dl>
</dl>
<dl>
<dd>(End of dynamical grammar changes for variable <tt>&quot;probe&quot;</tt> example value <tt>&quot;SipSak&quot;</tt>.)</dd></dl>
<dt><code>TCPPing</code>: (See the separate module documentation for details about each variable.)</dt>
<dd>The following new variables are valid:</dd>
<dl>
<dd>
</dd><dl>
<dt><code>pings</code></dt>
<dd>see above</dd>
<dt><code>port</code></dt>
<dd>see above</dd></dl>
</dl>
<dl>
<dd>Syntax changes for subsection <code>/[-_0-9a-zA-Z]+/</code> </dd>
<dl>
<dd>The following new variables are valid:</dd>
<dl>
<dt><code>pings</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>port</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dl>
</dl>
<dl>
<dd></dd></dl>
</dl>
<dl>
<dd>(End of dynamical grammar changes for variable <tt>&quot;probe&quot;</tt> example value <tt>&quot;TCPPing&quot;</tt>.)</dd></dl>
<dt><code>TacacsPlus</code>: (See the separate module documentation for details about each variable.)</dt>
<dd>The following new variables are valid:</dd>
<dl>
<dd>
</dd><dl>
<dt><code>authtype</code></dt>
<dd>see above</dd>
<dt><code>mininterval</code></dt>
<dd>see above</dd>
<dt><code>password</code></dt>
<dd>see above</dd>
<dt><code>pings</code></dt>
<dd>see above</dd>
<dt><code>port</code></dt>
<dd>see above</dd>
<dt><code>secret</code></dt>
<dd>see above</dd>
<dt><code>timeout</code></dt>
<dd>see above</dd>
<dt><code>username</code></dt>
<dd>see above</dd></dl>
</dl>
<dl>
<dd>Syntax changes for subsection <code>/[-_0-9a-zA-Z]+/</code> </dd>
<dl>
<dd>The following new variables are valid:</dd>
<dl>
<dt><code>authtype</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>mininterval</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>password</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>pings</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>port</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>secret</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>timeout</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>username</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dl>
</dl>
<dl>
<dd></dd></dl>
</dl>
<dl>
<dd>(End of dynamical grammar changes for variable <tt>&quot;probe&quot;</tt> example value <tt>&quot;TacacsPlus&quot;</tt>.)</dd></dl>
<dt><code>TelnetIOSPing</code>: (See the separate module documentation for details about each variable.)</dt>
<dd>The following new variables are valid:</dd>
<dl>
<dd>
</dd><dl>
<dt><code>iospass</code></dt>
<dd>see above</dd>
<dt><code>iosuser</code></dt>
<dd>see above</dd>
<dt><code>pings</code></dt>
<dd>see above</dd>
<dt><code>psource</code></dt>
<dd>see above</dd>
<dt><code>source</code></dt>
<dd>see above</dd></dl>
</dl>
<dl>
<dd>Syntax changes for subsection <code>/[-_0-9a-zA-Z]+/</code> </dd>
<dl>
<dd>The following new variables are valid:</dd>
<dl>
<dt><code>iospass</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>iosuser</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>pings</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>psource</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>source</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dl>
</dl>
<dl>
<dd></dd></dl>
</dl>
<dl>
<dd>(End of dynamical grammar changes for variable <tt>&quot;probe&quot;</tt> example value <tt>&quot;TelnetIOSPing&quot;</tt>.)</dd></dl>
<dt><code>TelnetJunOSPing</code>: (See the separate module documentation for details about each variable.)</dt>
<dd>The following new variables are valid:</dd>
<dl>
<dd>
</dd><dl>
<dt><code>junospass</code></dt>
<dd>see above</dd>
<dt><code>junosuser</code></dt>
<dd>see above</dd>
<dt><code>pings</code></dt>
<dd>see above</dd>
<dt><code>psource</code></dt>
<dd>see above</dd>
<dt><code>source</code></dt>
<dd>see above</dd></dl>
</dl>
<dl>
<dd>Syntax changes for subsection <code>/[-_0-9a-zA-Z]+/</code> </dd>
<dl>
<dd>The following new variables are valid:</dd>
<dl>
<dt><code>junospass</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>junosuser</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>pings</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>psource</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>source</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dl>
</dl>
<dl>
<dd></dd></dl>
</dl>
<dl>
<dd>(End of dynamical grammar changes for variable <tt>&quot;probe&quot;</tt> example value <tt>&quot;TelnetJunOSPing&quot;</tt>.)</dd></dl>
<dt><code>WebProxyFilter</code>: (See the separate module documentation for details about each variable.)</dt>
<dd>The following new variables are valid:</dd>
<dl>
<dd>
</dd><dl>
<dt><code>deny_re</code></dt>
<dd>see above</dd>
<dt><code>more_hosts</code></dt>
<dd>see above</dd>
<dt><code>pings</code></dt>
<dd>see above</dd>
<dt><code>timeout</code></dt>
<dd>see above</dd></dl>
</dl>
<dl>
<dd>Syntax changes for subsection <code>/[-_0-9a-zA-Z]+/</code> </dd>
<dl>
<dd>The following new variables are valid:</dd>
<dl>
<dt><code>deny_re</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>more_hosts</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>pings</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</p>
<dt><code>timeout</code></dt>
<dd>see above </dd>
<p> This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dl>
</dl>
<dl>
<dd></dd></dl>
</dl>
<dl>
<dd>(End of dynamical grammar changes for variable <tt>&quot;probe&quot;</tt> example value <tt>&quot;WebProxyFilter&quot;</tt>.)</dd></dl>
</dl>
<p> (End of dynamical grammar changes for example values of variable <tt>&quot;probe&quot;</tt>.)</p>
<h3>*** Alerts ***</h3>
<p>The Alert section lets you setup loss and RTT pattern detectors. After each round of polling, SmokePing will examine its data and determine which detectors match. Detectors are enabled per target and get inherited by the targets children. </p>
<p> Detectors are not just simple thresholds which go off at first sight of a problem. They are configurable to detect special loss or RTT patterns. They let you look at a number of past readings to make a more educated decision on what kind of alert should be sent, or if an alert should be sent at all. </p>
<p> The patterns are numbers prefixed with an operator indicating the type of comparison required for a match. </p>
<p> The following RTT pattern detects if a target&#8217;s RTT goes from constantly below 10ms to constantly 100ms and more: </p>
<pre> old ------------------------------&gt; new
 &lt;10,&lt;10,&lt;10,&lt;10,&lt;10,&gt;10,&gt;100,&gt;100,&gt;100</pre>
<p>Loss patterns work in a similar way, except that the loss is defined as the percentage the total number of received packets is of the total number of packets sent. </p>
<pre> old ------------------------------&gt; new
 ==0%,==0%,==0%,==0%,&gt;20%,&gt;20%,&gt;=20%</pre>
<p>Apart from normal numbers, patterns can also contain the values <code>*</code> which is true for all values regardless of the operator. And <code>U</code> which is true for <code>unknown</code> data together with the <code>==</code> and <code>=!</code> operators. </p>
<p> Detectors normally act on state changes. This has the disadvantage, that they will fail to find conditions which were already present when launching smokeping. For this it is possible to write detectors that begin with the special value <code>==S</code> it is inserted whenever smokeping is started up. </p>
<p> You can write </p>
<pre> ==S,&gt;20%,&gt;20%</pre>
<p>to detect lines that have been losing more than 20% of the packets for two periods after startup. </p>
<p> If you want to make sure a value within a certain range you can use two conditions in one element </p>
<pre> &gt;45%&lt;=55%</pre>
<p>Sometimes it may be that conditions occur at irregular intervals. But still you only want to throw an alert if they occur several times within a certain amount of times. The operator <code>*X*</code> will ignore up to <i>X</i> values and still let the pattern match: </p>
<pre> &gt;10%,*10*,&gt;10%</pre>
<p>will fire if more than 10% of the packets have been lost at least twice over the last 10 samples. </p>
<p> A complete example </p>
<pre> *** Alerts ***
 to = admin [at] company.xy,peter [at] home.xy
 from = smokealert [at] company.xy
 +lossdetect
 type = loss
 # in percent
 pattern = ==0%,==0%,==0%,==0%,&gt;20%,&gt;20%,&gt;20%
 comment = suddenly there is packet loss
 +miniloss
 type = loss
 # in percent
 pattern = &gt;0%,*12*,&gt;0%,*12*,&gt;0%
 comment = detected loss 3 times over the last two hours
 +rttdetect
 type = rtt
 # in milliseconds
 pattern = &lt;10,&lt;10,&lt;10,&lt;10,&lt;10,&lt;100,&gt;100,&gt;100,&gt;100
 comment = routing messed up again ?
 +rttbadstart
 type = rtt
 # in milliseconds
 pattern = ==S,==U
 comment = offline at startup</pre>
<p>The following variables can be set in this section:</p>
<dl>
<dt><code>to</code> <i>(mandatory setting)</i></dt>
<dd>Either an email address to send alerts to, or the name of a program to execute when an alert matches. To call a program, the first character of the <code>to</code> value must be a pipe symbol &#8220;|&#8221;. The program will the be called whenever an alert matches, using the following 5 arguments (except if <code>edgetrigger</code> is &#8216;yes&#8217;; see below): <code>name-of-alert</code>, <code>target</code>, <code>loss-pattern</code>, <code>rtt-pattern</code>, <code>hostname</code>. You can also provide a comma separated list of addresses and programs.</dd>
<dt><code>from</code> <i>(mandatory setting)</i></dt>
<dd>who should alerts appear to be coming from ?</dd>
<dt><code>edgetrigger</code></dt>
<dd>The alert notifications and/or the programs executed are normally triggered every time the alert matches. If this variable is set to &#8216;yes&#8217;, they will be triggered only when the alert&#8217;s state is changed, ie. when it&#8217;s raised and when it&#8217;s cleared. Subsequent matches of the same alert will thus not trigger a notification. </dd>
<p> When this variable is set to &#8216;yes&#8217;, a notification program (see the <code>to</code> variable documentation above) will get a sixth argument, <code>raise</code>, which has the value 1 if the alert was just raised and 0 if it was cleared. </p>
<p> Default value: edgetrigger = no</p>
<dt><code>mailtemplate</code></dt>
<dd>When sending out mails for alerts, smokeping normally uses an internally generated message. With the mailtemplate you can customize the alert mails to look they way you like them. The all <code>&lt;##</code><i>keyword</i><code>##&gt;</code> type strings will get replaced in the template before it is sent out. the following keywords are supported: </dd>
<pre> &lt;##ALERT##&gt; - target name
 &lt;##WHAT##&gt; - status (is active, was raised, was celared)
 &lt;##LINE##&gt; - path in the config tree
 &lt;##URL##&gt; - webpage for graph
 &lt;##STAMP##&gt; - date and time 
 &lt;##PAT##&gt; - pattern that matched the alert
 &lt;##LOSS##&gt; - loss history
 &lt;##RTT##&gt; - rtt history
 &lt;##COMMENT##&gt; - comment</pre>
</dl>
<p> The following sections are valid on level 1:</p>
<dl>
<dt><code>+/[^\s,]+/</code></dt>
<dd>The following variables can be set in this section:</dd>
<dl>
<dd>
</dd><dl>
<dt><code>type</code> <i>(mandatory setting)</i></dt>
<dd>Currently the pattern types <code>rtt</code> and <code>loss</code> and <code>matcher</code> are known. </dd>
<p> Matchers are plugin modules that extend the alert conditions. Known matchers are Avgratio, CheckLatency, CheckLoss, ExpLoss, Median, Medratio. </p>
<p> See the documentation of the corresponding matcher module (eg. Smokeping::matchers::Avgratio) for instructions on configuring it.</p>
<dt><code>pattern</code> <i>(mandatory setting)</i></dt>
<dd>a comma separated list of comparison operators and numbers. rtt patterns are in milliseconds, loss patterns are in percents</dd>
<dt><code>comment</code> <i>(mandatory setting)</i></dt>
<dd>
</dd><dt><code>to</code></dt>
<dd>Similar to the &#8220;to&#8221; parameter on the top-level except that it will only be used IN ADDITION to the value of the toplevel parameter. Same rules apply.</dd>
<dt><code>edgetrigger</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here. </dd>
<p> Default value: edgetrigger = no</p>
<dt><code>mailtemplate</code></dt>
<dd>This variable <i>inherits</i> its value from the parent section if nothing is specified here.</dd>
<dt><code>priority</code></dt>
<dd>if multiple alerts &#8216;match&#8217; only the one with the highest priority (lowest number) will cause and alert to be sent. Alerts without priority will be sent in any case.</dd></dl>
</dl>
<dl>
<dd></dd></dl>
</dl>
<h3>*** Slaves ***</h3>
<p>Your smokeping can remote control other somkeping instances running in slave mode on different hosts. Use this section to tell your master smokeping about the slaves you are going to use. </p>
<p> The following variables can be set in this section:</p>
<dl>
<dt><code>secrets</code> <i>(mandatory setting)</i></dt>
<dd>The slave secrets file contines one line per slave with the name of the slave followed by a colon and the secret: </dd>
<pre> slave1:secret1
 slave2:secret2
 ...</pre>
<p>Note that these secrets combined with a man-in-the-middle attack effectively give shell access to the corresponding slaves (see smokeping_master_slave), so the file should be appropriately protected and the secrets should not be easily crackable.</dl>
<p> The following sections are valid on level 1:</p>
<dl>
<dt><code>+/[-_0-9a-zA-Z.]+/</code></dt>
<dd>Define some basic properties for the slave. </dd>
<p> The following variables can be set in this section:</p>
<dl>
<dd>
</dd><dl>
<dt><code>display_name</code> <i>(mandatory setting)</i></dt>
<dd>Name of the Slave host.</dd>
<dt><code>location</code></dt>
<dd>Where is the slave located.</dd>
<dt><code>color</code> <i>(mandatory setting)</i></dt>
<dd>Color for the slave in graphs where input from multiple hosts is presented.</dd></dl>
</dl>
<dl>
<dd>The following sections are valid on level 2:</dd>
<dl>
<dt><code>++override</code></dt>
<dd>If part of the configuration information must be overwritten to match the settings of the you can specify this in this section. A setting is overwritten by giveing the full path of the configuration variable. If you have this configuration in the Probes section: </dd>
<pre> *** Probes ***
 +FPing
 binary = /usr/sepp/bin/fping</pre>
<p>You can override it for a particular slave like this: </p>
<pre> ++override
 Probes.FPing.binary = /usr/bin/fping</pre>
<p>The following variables can be set in this section:</p>
<dl>
<dd>
</dd><dl>
<dt><code>/\S+/</code></dt>
<dd></dd></dl>
</dl>
<dl>
<dd></dd></dl>
</dl>
</dl>
<dl>
<dd></dd></dl>
</dl>
<h2>Copyright</h2>
<p>Copyright (c) 2001-2007 by Tobias Oetiker. All right reserved.</p>
<h2>License</h2>
<p>This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.</p>
<h2>Author</h2>
<p>Tobias Oetiker &lt;tobi [at] oetiker.ch&gt;</p>
