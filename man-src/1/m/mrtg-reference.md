---
title: "mrtg-reference(1)"
name: "mrtg-reference"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mrtg-reference/"
description: "mrtg-reference – MRTG 2.17.4 configuration reference"
---

<h2 class="name">NAME</h2>
<p> mrtg-reference &#8211; MRTG 2.17.4 configuration reference </p>
<h2>OVERVIEW</h2>
<p> The runtime behaviour of <font SIZE="-1">MRTG</font> is governed by a configuration file. Run-of-the-mill configuration files can be generated with <code>cfgmaker</code>. (Check cfgmaker). But for more elaborate configurations some hand-tuning is required. </p>
<p> This document describes all the configuration options understood by the mrtg software.</p>
<h2>SYNTAX</h2>
<p> <font SIZE="-1">MRTG</font> configuration file syntax follows some simple rules:</p>
<dl>
<dt>&bull;</p>
<dd> Keywords must start at the beginning of a line.</p>
<dt>&bull;</p>
<dd> Lines which follow a keyword line which start with a blank are appended to the keyword line</p>
<dt>&bull;</p>
<dd> Empty Lines are ignored</p>
<dt>&bull;</p>
<dd> Lines starting with a # sign are comments.</p>
<dt>&bull;</p>
<dd> You can add other files into the configuration file using </p>
<p> <code>Include:</code> <i>file</i> </p>
<p> Example: </p>
<pre>
 Include: base-options.inc
</pre>
<p> If included files are specified with relative paths, both the current working directory and the directory containing the main config file will be searched for the files. The current working directory will be searched first. </p>
<p> If the included filename contains an asterisk, then this is taken as a wildcard for zero or more characters, and all matching files are included. Thus, you can use this statement to include all files in a specified subdirectory. </p>
<p> Example: </p>
<pre>
 Include: servers/*.cfg
</pre>
<p> In this case, you should be very careful that your wildcard pattern does not find a match relative to the current working directory if you mean it to be relative to the main config file directory, since the working directory is checked for a match first (as with a normal Include directive). Therefore, use of something like &#8216;*/*&#8217; is discouraged.</dl>
<h2>GLOBAL KEYWORDS</h2>
<h3>WorkDir</h3>
<p> WorkDir specifies where the logfiles and the webpages should be created. </p>
<p> Example: </p>
<pre>
 WorkDir: /usr/tardis/pub/www/stats/mrtg
</pre>
<h2>OPTIONAL GLOBAL KEYWORDS</h2>
<h3>HtmlDir</h3>
<p> HtmlDir specifies the directory where the html (or shtml, but we&#8217;ll get on to those later) lives. </p>
<p> <font SIZE="-1">NOTE:</font> Workdir overrides the settings for htmldir, imagedir and logdir. </p>
<p> Example: </p>
<pre>
 Htmldir: /www/mrtg/
</pre>
<h3>ImageDir</h3>
<p> ImageDir specifies the directory where the images live. They should be under the html directory. </p>
<p> Example: </p>
<pre>
 Imagedir: /www/mrtg/images
</pre>
<h3>LogDir</h3>
<p> LogDir specifies the directory where the logs are stored. This need not be under htmldir directive. </p>
<p> Example: </p>
<pre>
 Logdir: /www/mrtg/logs
</pre>
<h3>Forks (<font SIZE="-1">UNIX</font> only)</h3>
<p> With system that supports fork (<font SIZE="-1">UNIX</font> for example), mrtg can fork itself into multiple instances while it is acquiring data via snmp. </p>
<p> For situations with high latency or a great number of devices this will speed things up considerably. It will not make things faster, though, if you query a single switch sitting next door. </p>
<p> As far as I know <font SIZE="-1">NT</font> can not fork so this option is not available on <font SIZE="-1">NT</font>. </p>
<p> Example: </p>
<pre>
 Forks: 4
</pre>
<h3>EnableIPv6</h3>
<p> When set to yes, IPv6 support is enabled if the required libraries are present (see the mrtg-ipv6 manpage). When IPv6 is enabled, mrtg can talk to routers using <font SIZE="-1">SNMP</font> over IPv6 and targets may be specified by their numeric IPv6 addresses as well as by hostname or IPv4 address. </p>
<p> If IPv6 is enabled and the target is a hostname, mrtg will try to resolve the hostname to an IPv6 address and, if this fails, to an IPv4 address. Note that mrtg will only use IPv4 if you specify an IPv4 address or a hostname with no corresponding IPv6 address; it will not fall back to IPv4 if it simply fails to communicate with the target using IPv6. This is by design. </p>
<p> Note that many routers do not currently support <font SIZE="-1">SNMP</font> over IPv6. Use the <i>IPv4Only</i> per target option for these routers. </p>
<p> IPv6 is disabled by default. </p>
<p> Example: </p>
<pre>
 EnableIPv6: Yes
</pre>
<h3>EnableSnmpV3</h3>
<p> When set to yes, uses the Net::SNMP module instead of the <font SIZE="-1">SNMP_SESSION</font> module for generating snmp queries. This allows the use of SNMPv3 if other snmpv3 parameters are set. </p>
<p> SNMPv3 is disabled by default. </p>
<p> Example: </p>
<pre>
 EnableSnmpV3: yes
</pre>
<h3>Refresh</h3>
<p> How many seconds apart should the browser (Netscape) be instructed to reload the page? If this is not defined, the default is 300 seconds (5 minutes). </p>
<p> Example: </p>
<pre>
 Refresh: 600
</pre>
<h3>Interval</h3>
<p> How often do you call mrtg? The default is 5 minutes. If you call it less often, you should specify it here. This does two things:</p>
<dl>
<dt>&bull;</p>
<dd> The generated <font SIZE="-1">HTML</font> page contains the right information about the calling interval &#8230;</p>
<dt>&bull;</p>
<dd> A <font SIZE="-1">META</font> header in the generated <font SIZE="-1">HTML</font> page will instruct caches about the time-to-live of this page &#8230;..</dl>
<p> In this example, we tell mrtg that we will be calling it every 10 minutes. If you are calling mrtg every 5 minutes, you can leave this line commented out. </p>
<p> Example: </p>
<pre>
 Interval: 10
</pre>
<p> Note that unless you are using rrdtool you can not set Interval to less than 5 minutes. If you are using rrdtool you can set interval in the format </p>
<pre>
 Interval: MM[:SS]
</pre>
<p> Down to 1 second. Note though, setting the Interval for an rrdtool/mrtg setup will influence the initial creation of the database. If you change the interval later, all existing databases will remain at the resolution they were initially created with. Also note that you must make sure that your mrtg-rrd Web-frontend can deal with this kind of Interval setting.</p>
<h3>MaxAge</h3>
<p> <font SIZE="-1">MRTG</font> relies heavily on the real time clock of your computer. If the time is set to a wrong value, especially if it is advanced far into the future, this will cause mrtg to expire lots of supposedly old data from the log files. </p>
<p> To prevent this, you can add a &#8216;reasonability&#8217; check by specifying a maximum age for log files. If a file seems to be older, mrtg will not touch it but complain instead, giving you a chance to investigate the cause. </p>
<p> Example: </p>
<pre>
 MaxAge: 7200
</pre>
<p> The example above will make mrtg refuse to update log files older than 2 hours (7200 seconds).</p>
<h3>WriteExpires</h3>
<p> With this switch mrtg will generate .meta files for <font SIZE="-1">CERN</font> and Apache servers which contain Expiration tags for the html and gif files. The *.meta files will be created in the same directory as the other files, so you will have to set &#8220;MetaDir .&#8221; and &#8220;MetaFiles on&#8221; in your apache.conf or .htaccess file for this to work </p>
<p> <font SIZE="-1">NOTE:</font> If you are running Apache-1.2 or later, you can use the mod_expire to achieve the same effect &#8230; see the file htaccess.txt </p>
<p> Example: </p>
<pre>
 WriteExpires: Yes
</pre>
<h3>NoMib2</h3>
<p> Normally we ask the <font SIZE="-1">SNMP</font> device for &#8216;sysUptime&#8217; and &#8216;sysName&#8217; properties. Some do not have these. If you want to avoid getting complaints from mrtg about these missing properties, specify the nomib2 option. </p>
<p> An example of agents which do not implement base mib2 attributes are Computer Associates &#8211; Unicenter <font SIZE="-1">TNG</font> Agents. <font SIZE="-1">CA</font> relies on using the base <font SIZE="-1">OS</font> <font SIZE="-1">SNMP</font> agent in addition to its own agents to supplement the management of a system. </p>
<p> Example: </p>
<pre>
 NoMib2: Yes
</pre>
<h3>SingleRequest</h3>
<p> Some <font SIZE="-1">SNMP</font> implementations can not deal with requests asking for multiple snmp variables in one go. Set this in your cfg file to force mrtg to only ask for one variable per request. </p>
<p> Examples </p>
<pre>
 SingleRequest: Yes
</pre>
<h3>SnmpOptions</h3>
<p> Apart from the per target timeout options, you can also configure the behaviour of the snmpget process on a more profound level. SnmpOptions accepts a hash of options. The following options are currently supported: </p>
<pre>
 timeout                   =&gt; $default_timeout,
 retries                   =&gt; $default_retries,
 backoff                   =&gt; $default_backoff,
 default_max_repetitions   =&gt; $max_repetitions,
 use_16bit_request_ids     =&gt; 1,
 lenient_source_port_matching =&gt; 0,
 lenient_source_address_matching =&gt; 1
</pre>
<p> The values behind the options indicate the current default value. Note that these settings <font SIZE="-1">OVERRIDE</font> the per target timeout settings. </p>
<p> A per-target SnmpOptions[] keyword will override the global settings. That keyword is primarily for SNMPv3. </p>
<p> The 16bit request ids are the only way to query the broken <font SIZE="-1">SNMP</font> implementation of <font SIZE="-1">SMC</font> Barricade routers. </p>
<p> Example: </p>
<pre>
 SnmpOptions: retries =&gt; 2, only_ip_address_matching =&gt; 0
</pre>
<p> Note that <font SIZE="-1">AS/400</font> snmp seems to be broken in a way which prevents mrtg from working with it unless </p>
<pre>
 SnmpOptions: lenient_source_port_matching =&gt; 1
</pre>
<p> is set.</p>
<h3>IconDir</h3>
<p> If you want to keep the mrtg icons in someplace other than the working (or imagedir) directory, use the <i>IconDir</i> variable for defining the url of the icons directory. </p>
<p> Example: </p>
<pre>
 IconDir: /mrtgicons/
</pre>
<h3>LoadMIBs</h3>
<p> Load the <font SIZE="-1">MIB</font> file(s) specified and make its OIDs available as symbolic names. For better efficiancy, a cache of MIBs is maintained in the WorkDir. </p>
<p> Example: </p>
<pre>
 LoadMIBs: /dept/net/mibs/netapp.mib,/usr/local/lib/ft100m.mib
</pre>
<h3>Language</h3>
<p> Switch output format to the selected Language (Check the <i>translate</i> directory to see which languages are supported at the moment. In this directory you can also find instructions on how to create new translations). </p>
<p> Currently the following laguages are supported: </p>
<p> big5 brazilian bulgarian catalan chinese croatian czech danish dutch eucjp french galician gb gb2312 german greek hungarian icelandic indonesia iso2022jp italian korean lithuanian malay norwegian polish portuguese romanian russian russian1251 serbian slovak slovenian spanish swedish turkish ukrainian </p>
<p> Example: </p>
<pre>
 Language: danish
</pre>
<h3>LogFormat</h3>
<p> Setting LogFormat to &#8216;rrdtool&#8217; in your mrtg.cfg file enables rrdtool mode. In rrdtool mode, mrtg relies on <code>rrdtool</code> to do its logging. See mrtg-rrd. </p>
<p> Example: </p>
<pre>
 LogFormat: rrdtool
</pre>
<h3>LibAdd</h3>
<p> If you are using rrdtool mode and your <code>rrdtool</code> Perl module (RRDs.pm) is not installed in a location where perl can find it on its own, you can use LibAdd to supply an appropriate path. </p>
<p> Example: </p>
<pre>
 LibAdd: /usr/local/rrdtool/lib/perl/
</pre>
<h3>PathAdd</h3>
<p> If the <code>rrdtool</code> executable can not be found in the normal <tt>&quot;PATH&quot;</tt>, you can use this keyword to add a suitable directory to your path. </p>
<p> Example: </p>
<pre>
 PathAdd: /usr/local/rrdtool/bin/
</pre>
<h3>RRDCached</h3>
<p> If you are running RRDTool 1.4 or later with <code>rrdcached</code>, then you can configure <font SIZE="-1">MRTG</font> to take advantage of this for updates, either by using the <font SIZE="-1">RRDCACHED_ADDRESS</font> environment variable, or by setting the RRDCached keyword in the configuration file. Note that, if both are set, the configuration file keyword will take precedence. </p>
<p> Only <font SIZE="-1">UNIX</font> domain sockets are fully supported prior to RRDTool v1.5, and you should note that using RRDCached mode will disable all Threshold checking normally done by <font SIZE="-1">MRTG</font>. Appropriate warning messages will be printed if necessary. </p>
<p> Examples: </p>
<pre>
 RRDCached: unix:/var/tmp/rrdcached.sock
 
 RRDCached: localhost:42217
</pre>
<h3>RunAsDaemon</h3>
<p> The RunAsDaemon keyword enables daemon mode operation. The purpose of daemon mode is that <font SIZE="-1">MRTG</font> is launched once and not repeatedly (as it is with cron). This behavior saves computing resourses as loading and parsing of configuration files happens only once on startup, and if the configuration file is modified. </p>
<p> Using daemon mode <font SIZE="-1">MRTG</font> itself is responible for timing the measurement intervals. Therfore its important to set the Interval keyword to an apropiate value. </p>
<p> Note that when using daemon mode <font SIZE="-1">MRTG</font> should no longer be started from cron as each new process runs forever. Instead <font SIZE="-1">MRTG</font> should be started from the command prompt or by a system startup script. </p>
<p> If you want mrtg to run under a particular user and group (it is not recomended to run <font SIZE="-1">MRTG</font> as root) then you can use the <code>&#8211;user=</code><i>user_name</i> and <code>&#8211;group=</code><i>group_name</i> options on the mrtg commandline. </p>
<pre>
 mrtg --user=mrtg_user --group=mrtg_group mrtg.cfg
</pre>
<p> Also note that in daemon mode restarting the process is required in order to activate changes in the config file. </p>
<p> Under <font SIZE="-1">UNIX</font>, the Daemon switch causes mrtg to fork into background after checking its config file. On Windows <font SIZE="-1">NT</font> the <font SIZE="-1">MRTG</font> process will detach from the console, but because the <font SIZE="-1">NT/2000</font> shell waits for its children you have to use this special start sequence when you launch the program: </p>
<pre>
 start /b perl mrtg mrtg.cfg
</pre>
<p> You may have to add path information equal to what you add when you run mrtg from the commandline. </p>
<p> Example </p>
<pre>
 RunAsDaemon: Yes
 Interval:    5
</pre>
<p> This makes <font SIZE="-1">MRTG</font> run as a daemon beginning data collection every 5 minutes </p>
<p> If you are daemontools and still want to run mrtg as a daemon you can additionally specify </p>
<pre>
 NoDetach:     Yes
</pre>
<p> this will make mrtg run but without detaching it from the terminal. </p>
<p> If the modification date on the configuration file changes during operation, then <font SIZE="-1">MRTG</font> will re-read the configuration on the next polling cycle. Note that sub-files which are included from the main configuration do not have their modification times monitored, only the top-level file is so checked.</p>
<h3>ConversionCode</h3>
<p> Some devices may produce non-numeric values that would nevertheless be useful to graph with <font SIZE="-1">MRTG</font> if those values could be converted to numbers. The ConversionCode keyword specifies the path to a file containing Perl code to perform such conversions. The code in this file must consist of one or more Perl subroutines. Each subroutine must accept a single string argument and return a single numeric value. When RRDtool is in use, a decimal value may be returned. When the name of one of these subroutines is specified in a target definition (see below), <font SIZE="-1">MRTG</font> calls it twice for that target, once to convert the the input value being monitored and a second time to convert the output value. The subroutine must return an undefined value if the conversion fails. In case of failure, a warning may be posted to the <font SIZE="-1">MRTG</font> log file using Perl&#8217;s warn function. <font SIZE="-1">MRTG</font> imports the subroutines into a separate name space (package MRTGConversion), so the user need not worry about pollution of <font SIZE="-1">MRTG</font>&#8216;s global name space. <font SIZE="-1">MRTG</font> automatically prepends this package declaration to the user-supplied code. </p>
<p> Example: Suppose a particular <font SIZE="-1">OID</font> returns a character string whose length is proportional to the value to be monitored. To convert this string to a number that can be graphed by <font SIZE="-1">MRTG</font>, create a file arbitrarily named &#8220;MyConversions.pl&#8221; containing the following code: </p>
<pre><code>
#Return the length of the string argument
sub Length2Int
{
    my $value = shift;
    return length($value);
}
</code></pre>
<p> Then include the following global keyword in the <font SIZE="-1">MRTG</font> configuration file (assuming that the conversion code file is saved in the mrtg/bin directory along with mrtg itself): </p>
<pre>
 ConversionCode: MyConversions.pl
</pre>
<p> This will cause <font SIZE="-1">MRTG</font> to include the definition of the subroutine Length2Int in its execution environment. Length2Int can then be invoked on any target by appending &#8220;|Length2Int&#8221; to the target definition as follows: </p>
<p>Target[myrouter] : 1.3.6.1.4.1.999.1 &amp; 1.3.6.1.4.1.999.1 : public[at] mydevice | Length2Int</p>
<p> See &#8220;Extended Host Name Syntax&#8221; below for complete target definition syntax information.</p>
<h2>PER TARGET CONFIGURATION</h2>
<p> Each monitoring target must be identified by a unique name. This name must be appended to each parameter belonging to the same target. The name will also be used for naming the generated webpages, logfiles and images for this target.</p>
<h3>Target</h3>
<p> With the <i>Target</i> keyword you tell mrtg what it should monitor. The <i>Target</i> keyword takes arguments in a wide range of formats:</p>
<dl>
<dt>Basic</p>
<dd> The most basic format is &#8220;port:community [at] router&#8221; This will generate a traffic graph for the interface &#8216;port&#8217; of the host &#8216;router&#8217; (dns name or <font SIZE="-1">IP</font> address) and it will use the community &#8216;community&#8217; (snmp password) for the snmp query. </p>
<p> Example: </p>
<p>Target[myrouter] : 2 : public[at] wellfleet &#8211; fddi.domain</p>
<p> If your community contains a &#8220;@&#8221; or a &#8220; &#8221; these characters must be escaped with a &#8220;\&#8221;. </p>
<pre>
 Target[bla]: 2:stu\ pi\@d@router
</pre>
<dt>SNMPv2c</p>
<dd> If you have a fast router you might want to try to poll the ifHC* counters. This feature gets activated by switching to SNMPv2c. Unfortunately not all devices support SNMPv2c yet. If it works, this will prevent your counters from wraping within the 5 minute polling interval, since we now use 64 bit instead of the normal 32 bit. </p>
<p> Example: </p>
<p>Target[myrouter] : 2 : public[at] router1:: :: : 2</p>
<dt>SNMPv3</p>
<dd> As an alternative to SNMPv2c, SNMPv3 provides access to the ifHC* counters, along with encryption. Not all devices support SNMPv3, and you will also need the perl Net::SNMP library in order to use it. It is recommended that cfgmaker be used to generate configurations involving SNMPv3, as it will check if the Net::SNMP library is loadable, and will switch to SNMPv2c if v3 is unavailable. </p>
<p> <font SIZE="-1">SNMP</font> v3 requires additional authentication parameters, passed using the SnmpOptions[] per-target keyword. </p>
<p> Example:<br />
&nbsp;<wbr>&nbsp;<wbr>Target[myrouter]: 2:router1:::::3<br />
&nbsp;<wbr>&nbsp;<wbr>SnmpOptions[myrouter]: username=&gt;&#8217;user1&#8242;</p>
<dt>noHC</p>
<dd> Not all routers that support SNMPv2 or SNMPv3 provide the ifHC* counters on every interface. The noHC[] per-target keyword signals that the low-speed counters ifInOctets and ifOutOctets should be queried instead. cfgmaker will automatically insert this tag if SNMPv2 or SNMPv3 is specified but the ifHC* counters are unavailable. </p>
<p> Example:<br />
&nbsp;<wbr>&nbsp;<wbr>Target[myrouter]:&nbsp;<wbr>#Bri0:router1:::::3<br />
&nbsp;<wbr>&nbsp;<wbr>SnmpOptions[myrouter]: username=&gt;&#8217;user1&#8242;<br />
&nbsp;<wbr>&nbsp;<wbr>noHC[myrouter]: yes</p>
<dt>Reversing</p>
<dd> Sometimes you are sitting on the wrong side of the link, and you would like to have mrtg report Incoming traffic as Outgoing and vice versa. This can be achieved by adding the &#8216;-&#8216; sign in front of the &#8220;Target&#8221; description. It flips the incoming and outgoing traffic rates. </p>
<p> Example: </p>
<p>Target[ezci] : -1 : public[at] ezci &#8211; ether.domain</p>
<dt>Explicit OIDs</p>
<dd> You can also explicitly define which <font SIZE="-1">OID</font> to query by using the following syntax &#8216;OID_1&amp;OID_2:community [at] router&#8217; The following example will retrieve error counts for input and output on interface 1. <font SIZE="-1">MRTG</font> needs to graph two variables, so you need to specify two <font SIZE="-1">OID</font>&#8216;s such as temperature and humidity or error input and error output. </p>
<p> Example: </p>
<p>Target[myrouter] : 1.3.6.1.2.1.2.2.1.14.1 &amp; 1.3.6.1.2.1.2.2.1.20.1 : public[at] myrouter</p>
<dt><font SIZE="-1">MIB</font> Variables</p>
<dd> <font SIZE="-1">MRTG</font> knows a number of symbolic <font SIZE="-1">SNMP</font> variable names. See the file mibhelp.txt for a list of known names. One example are the ifInErrors and ifOutErrors. This means you can specify the above as: </p>
<p> Example: </p>
<p>Target[myrouter] : ifInErrors .1 &amp; ifOutErrors .1 : public[at] myrouter</p>
<dt>SnmpWalk</p>
<dd> It may be that you want to monitor an snmp object that is only reachable by &#8216;walking&#8217;. You can get mrtg to walk by prepending the <font SIZE="-1">OID</font> with the string <code>WaLK</code> or if you want a particular entry from the table returned by the walk you can use <code>WaLK</code><i>x</i> where <i>x</i> is a number starting from 0 (!). </p>
<p> Example: </p>
<p>Target[myrouter] : WaLKstrangeOid .1 &amp; WaLKstrangeOid .2 : public[at] myrouter Target[myrouter] : WaLK3strangeOid .1 &amp; WaLK4strangeOid .2 : public[at] myrouter</p>
<dt>SnmpGetNext</p>
<dd> A special case of an snmp object that is only reachable by &#8216;walking&#8217; occurs when a single snmpgetnext will return the correct value, but snmpwalk fails. This may occur with snmp V2 or V3, as the snmpgetbulk method is used in these versions. You can get mrtg to use getnext instead of getbulk by prepending the <font SIZE="-1">OID</font> with the string <code>GeTNEXT</code>. </p>
<p> Example: </p>
<p>Target[myrouter] : GeTNEXTstrangeOid &amp;GeTNEXTstrangeOid : public[at] myrouter</p>
<dt>Counted <font SIZE="-1">SNMP</font> Walk</p>
<dd> In other situations, an snmpwalk is needed to count rows, but the actual data is uninteresting. For example, counting the number of mac-addresses in a <font SIZE="-1">CAM</font> table, or the number of simultaneous dialup sessions. You can get <font SIZE="-1">MRTG</font> to count the number of instances by prepending the <font SIZE="-1">OID</font> with the string <code>CnTWaLK</code>. The following will retrieve the number of simultaneous <font SIZE="-1">VOIP</font> calls on some routers: </p>
<p> Example: </p>
<p>Target[myrouter] : CnTWaLK1 .3.6.1.4.1.9.10.55.1.1.1.1.3 &amp; CnTWaLK1 .3.6.1.4.1.9.10.55.1.1.1.1.3 : public[at] myrouter</p>
<dt>Interface by <font SIZE="-1">IP</font></p>
<dd> Sometimes <font SIZE="-1">SNMP</font> interface index can change, like when new interfaces are added or removed. This can cause all Target entries in your config file to become offset, causing <font SIZE="-1">MRTG</font> to graphs wrong instances etc. <font SIZE="-1">MRTG</font> supports <font SIZE="-1">IP</font> address instead of ifindex in target definition. Then <font SIZE="-1">MRTG</font> will query snmp device and try to map <font SIZE="-1">IP</font> address to the current ifindex. You can use <font SIZE="-1">IP</font> addresses in every type of target definition by adding <font SIZE="-1">IP</font> address of the numbered interface after <font SIZE="-1">OID</font> and separation char &#8216;/&#8217;. </p>
<p> Make sure that the given <font SIZE="-1">IP</font> address is used on your same target router, especially when graphing two different OIDs and/or interface split by &#8216;&amp;&#8217; delimiter. </p>
<p> You can tell cfgmaker to generate such references with the option <code>&#8211;ifref=ip</code>. </p>
<p> Example: </p>
<p>Target[myrouter] : / 1.2.3.4 : public[at] wellfleet &#8211; fddi.domain Target[ezci] : &#8211; / 1.2.3.4 : public[at] ezci &#8211; ether.domain Target[myrouter] : ifInErrors / 1.2.3.4 &amp; ifOutErrors / 1.2.3.4 : public[at] myrouter</p>
<dt>Interface by Description</p>
<dd> If you can not use <font SIZE="-1">IP</font> addresses you might want to use the interface names. This works similar to the <font SIZE="-1">IP</font> address aproach except that the prefix to use is a \ instead of a / </p>
<p> You can tell cfgmaker to generate such references with the option <code>&#8211;ifref=descr</code>. </p>
<p> Example: </p>
<p>Target[myrouter] : \My &#8211; Interface2 : public[at] wellfleet &#8211; fddi.domain Target[ezci] : -\My &#8211; Interface2 : public[at] ezci &#8211; ether.domain Target[myrouter] : ifInErrors\My &#8211; If2 &amp;ifOutErrors\My &#8211; If3 : public[at] myrouter</p>
<p> If your description contains a &#8220;&amp;&#8221;, a &#8220;:&#8221;, a &#8220;@&#8221; or a &#8220; &#8221; you can include them but you must escape with a backlash: </p>
<p>Target[myrouter] : un\:\ ney\&amp;ddd : public[at] hello.router</p>
<dt>Interface by Name</p>
<dd> This is the only sensible way to reference the interfaces of your switches. </p>
<p> You can tell cfgmaker to generate such references with the option <code>&#8211;ifref=name</code>. </p>
<p> Example: </p>
<p>Target[myrouter] : #2 / 11 : public[at] wellfleet &#8211; fddi.domain Target[ezci] : -#2 / 11 : public[at] ezci &#8211; ether.domain Target[myrouter] : ifInErrors #3 / 7 &amp; ifOutErrors #3 / 7 : public[at] myrouter</p>
<p> If your description contains a &#8220;&amp;&#8221;, a &#8220;:&#8221;, a &#8220;@&#8221; or a &#8220; &#8221; you can include them but you must escape with a backlash: </p>
<p>Target[myrouter] : #\:\ fun : public[at] hello.router</p>
<p> Note that the # sign will be interpreted as a comment character if it is the first non white-space character on the line.</p>
<dt>Interface by Ethernet Address</p>
<dd> When the <font SIZE="-1">SNMP</font> interface index changes, you can key that interface by its &#8216;Physical Address&#8217;, sometimes called a &#8216;hard address&#8217;, which is the <font SIZE="-1">SNMP</font> variable &#8216;ifPhysAddress&#8217;. Internally, <font SIZE="-1">MRTG</font> matches the Physical Address from the *.cfg file to its current index, and then uses that index for the rest of the session. </p>
<p> You can use the Physical Address in every type of target definition by adding the Physical Address after the <font SIZE="-1">OID</font> and the separation char &#8216;!&#8217; (analogous to the <font SIZE="-1">IP</font> address option). The Physical address is specified as &#8216;-&#8216; delimited octets, such as &#8220;0a-0-f1-5-23-18&#8221; (omit the double quotes). Note that some routers use the same Hardware Ethernet Address for all of their Interfaces which prevents unique interface identification. Mrtg will notice such problems and alert you. </p>
<p> You can tell cfgmaker to generate configuration files with hardware ethernet address references by using the option <code>&#8211;ifref=eth</code>. </p>
<p> Example: </p>
<p>Target[myrouter] : !0a &#8211; 0b &#8211; 0c &#8211; 0d : public[at] wellfleet &#8211; fddi.domain Target[ezci] : -!0 &#8211; f &#8211; bb &#8211; 05 &#8211; 71 &#8211; 22 : public[at] ezci &#8211; ether.domain Target[myrouter] : 1.3.6.1.2.1.2.2.1.14 !0a &#8211; 00 &#8211; 10 &#8211; 23 &#8211; 44 &#8211; 51 &amp; *BREAK * 1.3.6.1.2.1.2.2.1.14 !0a &#8211; 00 &#8211; 10 &#8211; 23 &#8211; 44 &#8211; 51 : public[at] myrouter Target[myrouter] : ifInErrors !0a &#8211; 00 &#8211; 10 &#8211; 23 &#8211; 44 &#8211; 51 &amp; *BREAK * ifOutErrors !0a &#8211; 00 &#8211; 10 &#8211; 23 &#8211; 44 &#8211; 51 : public[at] myrouter</p>
<p> Join the lines at *BREAK* &#8230;</p>
<dt>Interface by Type</p>
<dd> It seems that there are devices that try to defy all monitoring efforts: the interesting interfaces have neither ifName nor a constant ifDescr not to mention a persistent ifIndex. The only way to get a constant mapping is by looking at the interface type, because the interface you are interested in is unique in the device you are looking at &#8230; </p>
<p> You can tell cfgmaker to generate such references with the option <code>&#8211;ifref=type</code>. </p>
<p> Example: </p>
<p>Target[myrouter] : % 13 : public[at] wellfleet &#8211; fddi.domain Target[ezci] : &#8211; % 13 : public[at] ezci &#8211; ether.domain Target[myrouter] : ifInErrors % 13 &amp; ifOutErrors % 14 : public[at] myrouter</p>
<dt>Extended positioning of ifIndex</p>
<dd> There are OIDs that contain the interface index at some inner position within the <font SIZE="-1">OID</font>. To use the above mentioned Interface by IP/Description/Name/Type methods in the target definition the keyword &#8216;IndexPOS&#8217; can be used to indicate the position of ifIndex. If &#8216;IndexPOS&#8217; is not used the ifIndex will be appended at the end of the <font SIZE="-1">OID</font>. </p>
<p> Example: </p>
<p>Target[myrouter] : OID.IndexPOS .1 / 1.2.3.4 &amp; OID.IndexPOS .1 / 1.2.3.4 : public[at] myrouter</p>
<p> Replace <font SIZE="-1">OID</font> by your numeric <font SIZE="-1">OID</font>.</p>
<dt>Extended Host Name Syntax</p>
<dd> In all places where &#8220;community [at] router&#8221; is accepted, you can add additional parameters for the <font SIZE="-1">SNMP</font> communication using colon-separated suffixes. You can also append a pipe symbol ( | ) and the name of a numeric conversion subroutine as described under the global keyword &#8220;ConversionCode&#8221; above. The full syntax is as follows: </p>
<p>community[at] router[:[port][:[timeout][:[retries][:[backoff][:[version]][| name]]]]]</p>
<p> where the meaning of each parameter is as follows:</p>
<dl>
<dt>
<dd>
<dl>
<dt>port</p>
<dd> the <font SIZE="-1">UDP</font> port under which to contact the <font SIZE="-1">SNMP</font> agent (default: 161) </p>
<p> The complete syntax of the port parameter is </p>
<p>remote_port[!local_address[!local_port]]</p>
<p> Some machines have additional security features that only allow <font SIZE="-1">SNMP</font> queries to come from certain <font SIZE="-1">IP</font> addresses. If the host doing the query has multiple interface, it may be necessary to specify the interface the query should come from. </p>
<p> The port parameter allows the specification of the port of the machine being queried. In addition, the <font SIZE="-1">IP</font> address (or hostname) and port of the machine doing the query may be specified. </p>
<p> Examples: </p>
<pre>
 somehost
 somehost:161
 somehost:161!192.168.2.4!4000 use 192.168.2.4 and port 4000 as source
 somehost:!192.168.2.4 use 192.168.2.4 as source
 somehost:!!4000 use port 4000 as source
</pre>
<dt>timeout</p>
<dd> initial timeout for <font SIZE="-1">SNMP</font> queries, in seconds (default: 2.0)</p>
<dt>retries</p>
<dd> number of times a timed-out request will be retried (default: 5)</p>
<dt>backoff</p>
<dd> factor by which the timeout is multiplied on every retry (default: 1.0).</p>
<dt>version</p>
<dd> for <font SIZE="-1">SNMP</font> version. If you have a fast router you might want to put a &#8216;2&#8217; here. For authenticated or encrypted <font SIZE="-1">SNMP</font>, you can try to put a &#8216;3&#8217; here. This will make mrtg try to poll the 64 bit counters and thus prevent excessive counter wrapping. Not all routers support this though. <font SIZE="-1">SNMP</font> v3 requires additional setup, see SnmpOptions[] for full details. </p>
<p> Example: </p>
<pre>
 3:public [at] router1:::::2
</pre>
<dt>name</p>
<dd> the name of the subroutine that <font SIZE="-1">MRTG</font> will call to convert the input and output values to integers. See the complete example under the global keyword &#8220;ConversionCode&#8221; above. </p>
<p> Example: </p>
<pre>
 1.3.6.1.4.1.999.1&amp;1.3.6.1.4.1.999.2:public [at] mydevice:161::::2|Length2Int
</pre>
<p> This would retrieve values from the <font SIZE="-1">OID</font> 1.3.6.1.4.1.999.1 for input and .2 for output on mydevice using <font SIZE="-1">UDP</font> port 161 and <font SIZE="-1">SNMP</font> version 2, and would execute the user-defined numeric conversion subroutine Length2Int to convert those values to integers.</dl>
</dl>
<dl>
<dt>
<dd>
<p> A value that equals the default value can be omitted. Trailing colons can be omitted, too. The pipe symbol followed by the name parameter, if present, must come at the end. There must be no spaces around the colons or pipe symbol. </p>
<p> Example: </p>
<p>Target[ezci] : 1 : public[at] ezci &#8211; ether.domain : 9161 ::4</p>
<p> This would refer to the input/output octet counters for the interface with <i>ifIndex 1</i> on <i>ezci-ether.domain</i>, as known by the <font SIZE="-1">SNMP</font> agent listening on <font SIZE="-1">UDP</font> port 9161. The standard initial timeout (2.0 seconds) is used, but the number of retries is set to four. The backoff value is the default.</dl>
<dt>Numeric IPv6 addresses</p>
<dd> If IPv6 is enabled you may also specify a target using its IPv6 address. To avoid ambiguity with the port number, numeric IPv6 addresses must be placed in square brackets. </p>
<p> Example: </p>
<p>Target[IPv6test] : 2 : public @[ 2001 : 760 : 4 ::] : 6161 ::4</p>
<dt>External Monitoring Scripts</p>
<dd> If you want to monitor something which does not provide data via snmp you can use some external program to do the data gathering. </p>
<p> The external command must return 4 lines of output:</p>
<dl>
<dt>
<dd>
<dl>
<dt>Line 1</p>
<dd> current state of the first variable, normally &#8216;incoming bytes count&#8217;</p>
<dt>Line 2</p>
<dd> current state of the second variable, normally &#8216;outgoing bytes count&#8217;</p>
<dt>Line 3</p>
<dd> string (in any human readable format), telling the uptime of the target.</p>
<dt>Line 4</p>
<dd> string, telling the name of the target.</dl>
</dl>
<dl>
<dt>
<dd>
<p> Depending on the type of data your script returns you might want to use the &#8216;gauge&#8217; or &#8216;absolute&#8217; arguments for the <i>Options</i> keyword. </p>
<p> Example: </p>
<pre>
 Target[myrouter]: `/usr/local/bin/df2mrtg /dev/dsk/c0t2d0s0`
</pre>
<p> Note the use of the backticks (`), not apostrophes (&#8216;) around the command. </p>
<p> If you want to use a backtick in the command name this can be done but you must escape it with a backslash &#8230; </p>
<p> If your script does not have any data to return but does not want mrtg to complain about invalid data, it can return &#8216;<font SIZE="-1">UNKNOWN</font>&#8216; instead of a number. Note though that only rrdtool is realy equipped to handle unknown data well.</dl>
<dt>Multi Target Syntax</p>
<dd> You can also combine several target definitions in a mathematical expression. Any syntactically correct expression that the Perl interpreter can evaluate to will work. An expression could be used, for example, to aggregate both B channels in an <font SIZE="-1">ISDN</font> connection or to calculate the percentage hard disk utilization of a server from the absolute used space and total capacity. </p>
<p> Examples: </p>
<p>Target[myrouter] : 2 : public[at] wellfleetA + 1 : public[at] wellfleetA<br />
                                                       Target[myrouter] : .1.3.6.1.4.1.999.1 &amp;<br />
    .1.3.6.1.4.1.999.2 : public[at] mydevice /<br />
                         .1.3.6.1.4.1.999.3 &amp;<br />
    .1.3.6.1.4.1.999.4 : public[at] mydevice * 100</p>
<p> Note that whitespace must surround each target definition in the expression. Target definitions themselves must not contain whitespace, except in interface descriptions and interface names, where each whitespace character is escaped by a backslash. </p>
<p> <font SIZE="-1">MRTG</font> automatically rounds the result of the expression to an integer unless RRDTool logging is in use and the gauge option is in effect for the target. Internally <font SIZE="-1">MRTG</font> uses Perl&#8217;s Math::BigFloat package to calculate the result of the expression with 40 digits of precision. Even in extreme cases, where, for example, you take the difference of two 64-bit integers, the result of the expression should be accurate.</p>
<dt><font SIZE="-1">SNMP</font> Request Optimization</p>
<dd> <font SIZE="-1">MRTG</font> is designed to economize on its <font SIZE="-1">SNMP</font> requests. Where a target definition appears more than once in the configuration file, <font SIZE="-1">MRTG</font> requests the data from the device only once per round of data collection and uses the collected data for each instance of a particular target. Recognition of two target definitions as being identical is based on a simple string match rather than any kind of deeper semantic analysis. </p>
<p> Example: </p>
<p>Target[Targ1] : 1 : public[at] CiscoA<br />
                        Target[Targ2] : 2 : public[at] CiscoA<br />
                                                Target[Targ3] : 1 : public[at] CiscoA +<br />
                                                                    2 : public[at] CiscoA<br />
                                                                            Target[Targ4] : 1 : public[at] CISCOA</p>
<p> This results in a total of three <font SIZE="-1">SNMP</font> requests. Data for 1:public [at] CiscoA and 2:public [at] CiscoA are requested only once each, and used for Targ1, Targ2, and Targ3. Targ4 causes another <font SIZE="-1">SNMP</font> request for 1:public [at] CISCOA, which is not recognized as being identical to 1:public [at] CiscoA.</dl>
<h3>MaxBytes</h3>
<p> The maximum value either of the two variables monitored are allowed to reach. For monitoring router traffic this is normally the bytes per second this interface port can carry. </p>
<p> If a number higher than <i>MaxBytes</i> is returned, it is ignored. Also read the section on <i>AbsMax</i> for further info. The <i>MaxBytes</i> value is also used in calculating the Y range for unscaled graphs (see the section on <i>Unscaled</i>). </p>
<p> Since most links are rated in bits per second, you need to divide their maximum bandwidth (in bits) by eight (8) in order to get bytes per second. This is very important to make your unscaled graphs display realistic information. T1 = 193000, 56K = 7000, 10 <font SIZE="-1">MB</font> Ethernet = 1250000, 100 <font SIZE="-1">MB</font> Ethernet = 12500000. The <i>MaxBytes</i> value will be used by mrtg to decide whether it got a valid response from the router. </p>
<p> If you need two different MaxBytes values for the two monitored variables, you can use MaxBytes1 and MaxBytes2 instead of MaxBytes. </p>
<p> Example: </p>
<pre>
 MaxBytes[myrouter]: 1250000
</pre>
<h3>Title</h3>
<p> Title for the <font SIZE="-1">HTML</font> page which gets generated for the graph. </p>
<p> Example: </p>
<pre>
 Title[myrouter]: Traffic Analysis for Our Nice Company
</pre>
<h2>OPTIONAL PER TARGET KEYWORDS</h2>
<h3>PageTop</h3>
<p> Things to add to the top of the generated <font SIZE="-1">HTML</font> page. Note that you can have several lines of text as long as the first column is empty. </p>
<p> Note that the continuation lines will all end up on the same line in the html page. If you want linebreaks in the generated html use the &#8216;
&#8217; sequence. </p>
<p> Example: </p>
<pre>
 PageTop[myrouter]: &lt;H1&gt;Traffic Analysis for ETZ C95.1&lt;/H1&gt;
   Our Campus Backbone runs over an FDDI line

   with a maximum transfer rate of 12.5 megabytes per
   Second.
</pre>
<h3>RouterUptime</h3>
<p> In cases where you calculate the used bandwidth from several interfaces you normally don&#8217;t get the router uptime and router name displayed on the web page. </p>
<p> If these interfaces are on the same router and the uptime and name should be displayed you have to specify its community and address again with the <i>RouterUptime</i> keyword. </p>
<p> If you want to use a special <font SIZE="-1">OID</font> for querying the router uptime, use prepend the oid. </p>
<p> Example: </p>
<p>Target[kacisco.comp.edu] : 1 : public[at] 194.64.66.250 + 2 : public[at] 194.64.66.250 RouterUptime[kacisco.comp.edu] : public[at] 194.64.66.250 RouterUptime[kacisco.comp.edu] : hrSystemUptime .0 : public[at] 194.64.66.250</p>
<h3>RouterName</h3>
<p> If the default name of the router is incorrect/uninformative, you can use RouterName to specify a different <font SIZE="-1">OID</font> on either the same or a different host. </p>
<p> A practical example: sysName on BayTech <font SIZE="-1">DS72</font> units always display &#8220;ds72&#8221;, no matter what you set the Unit <font SIZE="-1">ID</font> to be. Instead, the Unit <font SIZE="-1">ID</font> is stored at 1.3.6.1.4.1.4779.1.1.3.0, so we can have <font SIZE="-1">MRTG</font> display this instead of sysName. </p>
<p> Example: </p>
<pre>
 RouterName[kacisco.comp.edu]: 1.3.6.1.4.1.4779.1.1.3.0
</pre>
<p> A different <font SIZE="-1">OID</font> on a different host can also be specified: </p>
<p>RouterName[kacisco.comp.edu] : 1.3.6.1.4.1.4779.1.1.3.0 : public[at] 194.64.66.251</p>
<h3>MaxBytes1</h3>
<p> Same as MaxBytes, for variable 1.</p>
<h3>MaxBytes2</h3>
<p> Same as MaxBytes, for variable 2.</p>
<h3>IPv4Only</h3>
<p> Many IPv6 routers do not currently support <font SIZE="-1">SNMP</font> over IPv6 and must be monitored using IPv4. The IPv4Only option forces mrtg to use IPv4 when communicating with the target, even if IPv6 is enabled. This is useful if the target is a hostname with both IPv4 and IPv6 addresses; without the IPv4Only keyword, monitoring such a router will not work if IPv6 is enabled. </p>
<p> If set to no (the default), mrtg will use IPv6 unless the target has no IPv6 addresses, in which case it will use IPv4. If set to yes, mrtg will only use IPv4. </p>
<p> Note that if this option is set to yes and the target does not have an IPv4 address, communication with the target will fail. </p>
<p> This option has no effect if IPv6 is not enabled. </p>
<p> Example: </p>
<p>Target[v4onlyrouter_1] : 1 : public[at] v4onlyrouter<br />
                                 IPv4Only[v4onlyrouter_1] : Yes</p>
<h3>SnmpOptions (V3)</h3>
<p> SNMPv3 requires a fairly rich set of options. This per-target keyword allows access to the User Security Model of SNMPv3. Options are listed in the same syntax as a perl hash. </p>
<p> <i>Security Modes</i> </p>
<p> SNMPv3 has three security modes, defined on the device being polled. For example, on Cisco routers the security mode is defined by the snmp-server group global configuration command.</p>
<dl>
<dt>NoAuthNoPriv</p>
<dd> Neither Authentication nor Privacy is defined. Only the Username option is specified for this mode. </p>
<p> Example: </p>
<pre>
 SnmpOptions[myrouter]: username=&gt;'user1'
</pre>
<dt>AuthNoPriv</p>
<dd> Uses a Username and a password. The password can be hashed using the snmpkey application, or passed in plain text along with the ContextEngineID </p>
<p> Example: </p>
<pre>
 SnmpOptions[myrouter]: username=&gt;'user1',authpassword=&gt;'example',
   contextengineid=&gt;'80000001110000004000000'
</pre>
<dt>Priv</p>
<dd> Both Authentication and Privacy is defined. The default privacy protocol is des. </p>
<p> Example:<br />
&nbsp;<wbr>SnmpOptions[myrouter]: authkey=&gt;&#8217;0x1e93ab5a396e2af234c8920e61cfe2028072c0e2&#8242;,<br />
authprotocol=&gt;&#8217;sha&#8217;,privprotocol=&gt;&#8217;des&#8217;,username=&gt;&#8217;user1&#8242;,<br />
privkey=&gt;&#8217;0x498d74940c5872ed387201d74b9b25e2&#8242;</dl>
<p> <i>snmp options</i> </p>
<p> The following option keywords are recognized:</p>
<dl>
<dt>username</p>
<dd> The user associated with the User Security Model</p>
<dt>contextname</p>
<dd> An <font SIZE="-1">SNMP</font> agent can define multiple contexts. This keyword allows them to be polled.</p>
<dt>contextengineid</p>
<dd> A unique 24-byte string identifying the snmp-agent.</p>
<dt>authpassword</p>
<dd> The plaintext password for a user in either AuthNoPriv or Priv mode.</p>
<dt>authkey</p>
<dd> A md5 or sha hash of the plain-text password, along with the engineid. Use the snmpkey commandline program to generate this hash, or use Net::SNMP::Security::USM in a script.</p>
<dt>authprotocol {sha|md5}</p>
<dd> The hashing algorithm defined on the <font SIZE="-1">SNMP</font> client. Defaults to md5.</p>
<dt>privpassword</p>
<dd> A plaintext pre-shared key for encrypting snmp packets in Priv mode.</p>
<dt>privkey</p>
<dd> A hash of the plain-text pre-shared key, along with the engineid. Use the snmpkey commandline program to generate this hash, or use Net::SNMP::Security::USM in a script.</p>
<dt>privprotocol {des|3desede|aescfb128|aescfb192|aescfb256}</p>
<dd> Specifies the encryption method defined on the snmp agent. The default is des.</dl>
<h3>PageFoot</h3>
<p> Things to add to the bottom of the generated <font SIZE="-1">HTML</font> page. Note that you can have several lines of text as long as the first column is empty. </p>
<p> Note that the continuation lines will all end up on the same line in the html page. If you want linebreaks in the generated html use the &#8216;
&#8217; sequence. </p>
<p> The material will be added just before the &lt;/BODY&gt; tag: </p>
<p> Example: </p>
<p>PageFoot[myrouter] : Contact&lt;A href = &#8220;mailto:peter [at] x.yz&#8221;&gt; Peter&lt;/ A&gt; if you have questions regarding this page</p>
<h3>AddHead</h3>
<p> Use this tag like the <i>PageTop</i> header, but its contents will be added between &lt;/TITLE&gt; and &lt;/HEAD&gt;. </p>
<p> Example: </p>
<p>AddHead[myrouter] : &lt;link rev = &#8220;made&#8221; href = &#8220;mailto:mrtg [at] blabla.edu&#8221;&gt;</p>
<h3>BodyTag</h3>
<p> BodyTag lets you supply your very own &lt;body &#8230;&gt; tag for the generated webpages. </p>
<p> Example: </p>
<pre>
 BodyTag[myrouter]: &lt;BODY LEFTMARGIN=&quot;1&quot; TOPMARGIN=&quot;1&quot; 
                      BACKGROUND=&quot;/stats/images/bg.neo2.gif&quot;&gt;
</pre>
<h3>AbsMax</h3>
<p> If you are monitoring a link which can handle more traffic than the <i>MaxBytes</i> value. Eg, a line which uses compression or some frame relay link, you can use the <i>AbsMax</i> keyword to give the absolute maximum value ever to be reached. We need to know this in order to sort out unrealistic values returned by the routers. If you do not set <i>AbsMax</i>, rateup will ignore values higher than <i>MaxBytes</i>. </p>
<p> Example: </p>
<pre>
 AbsMax[myrouter]: 2500000
</pre>
<h3>Unscaled</h3>
<p> By default each graph is scaled vertically to make the actual data visible even when it is much lower than <i>MaxBytes</i>. With the <i>Unscaled</i> variable you can suppress this. It&#8217;s argument is a string, containing one letter for each graph you don&#8217;t want to be scaled: d=day w=week m=month y=year. There is also a special case to unset the variable completely: n=none. This could be useful in the event you need to override a global configuration. In the example scaling for the yearly and the monthly graph are suppressed. </p>
<p> Example: </p>
<pre>
 Unscaled[myrouter]: ym
</pre>
<h3>WithPeak</h3>
<p> By default the graphs only contain the average values of the monitored variables &#8211; normally the transfer rates for incoming and outgoing traffic. The following option instructs mrtg to display the peak 5 minute values in the [w]eekly, [m]onthly and [y]early graph. In the example we define the monthly and the yearly graph to contain peak as well as average values. </p>
<p> Examples: </p>
<pre>
 WithPeak[myrouter]: ym
</pre>
<h3>Suppress</h3>
<p> By default mrtg produces 4 graphs. With this option you can suppress the generation of selected graphs. The option value syntax is analogous to the above two options. In this example we suppress the yearly graph as it is quite empty in the beginning. </p>
<p> Example: </p>
<pre>
 Suppress[myrouter]: y
</pre>
<h3>Extension</h3>
<p> By default, mrtg creates .html files. Use this option to tell mrtg to use a different extension. For example you could set the extension to php3, then you will be able to enclose <font SIZE="-1">PHP</font> tags into the output (useful for getting a router name out of a database). </p>
<p> Example: </p>
<pre>
 Extension[myrouter]: phtml
</pre>
<h3>Directory</h3>
<p> By default, mrtg puts all the files that it generates for each target (the GIFs, the <font SIZE="-1">HTML</font> page, the log file, etc.) in <i>WorkDir</i>. </p>
<p> If the <i>Directory</i> option is specified, the files are instead put into a directory under <i>WorkDir</i> or Log-, Image- and HtmlDir). (For example the <i>Directory</i> option below would cause all the files for a target myrouter to be put into directory /usr/tardis/pub/www/stats/mrtg/myrouter/ .) </p>
<p> The directory must already exist; mrtg will not create it. </p>
<p> Example: </p>
<pre>
 WorkDir: /usr/tardis/pub/www/stats/mrtg
 Directory[myrouter]: myrouter
</pre>
<p> <font SIZE="-1">NOTE:</font> the Directory option must always be &#8216;relative&#8217; or bad things will happen.</p>
<h3>Clonedirectory</h3>
<p> If the <i>Directory</i> option is specified, the <i>Clonedirectory</i> option will copy all the contents of <i>Directory</i> to the <i>Clonedirectory</i>. </p>
<p> Example: </p>
<p>WorkDir : / usr / tardis / pub / www / stats / mrtg Directory[myrouter] : myrouter Clonedirectory[myrouter] : myclonedirectory</p>
<p> Optionally the target name can be changed in the cloning process. </p>
<p> Example: </p>
<p>WorkDir : / usr / tardis / pub / www / stats / mrtg Directory[myrouter] : myrouter Clonedirectory[myrouter] : myclonedirectory mynewtarget</p>
<p> <font SIZE="-1">NOTE1:</font> The clone directory must already exist; mrtg will not create it. </p>
<p> <font SIZE="-1">NOTE2:</font> The Clonedirectory option must also always be &#8216;relative&#8217; or bad things will happen. </p>
<p> <font SIZE="-1">NOTE3:</font> This requires the File::Copy module</p>
<h3>XSize and YSize</h3>
<p> By default mrtgs graphs are 100 by 400 pixels wide (plus some more for the labels. In the example we get almost square graphs &#8230; </p>
<p> Note: XSize must be between 20 and 600; YSize must be larger than 20 </p>
<p> Example: </p>
<p>XSize[myrouter] : 300 YSize[myrouter] : 300</p>
<h3>XZoom and YZoom</h3>
<p> If you want your graphs to have larger pixels, you can &#8220;Zoom&#8221; them. </p>
<p> Example: </p>
<p>XZoom[myrouter] : 2.0 YZoom[myrouter] : 2.0</p>
<h3>XScale and YScale</h3>
<p> If you want your graphs to be actually scaled use <i>XScale</i> and <i>YScale</i>. (Beware: while this works, the results look ugly (to be frank) so if someone wants to fix this: patches are welcome. </p>
<p> Example: </p>
<p>XScale[myrouter] : 1.5 YScale[myrouter] : 1.5</p>
<h3>YTics and YTicsFactor</h3>
<p> If you want to show more than 4 lines per graph, use YTics. If you want to scale the value used for the YLegend of these tics, use YTicsFactor. The default value for YTics is 4 and the default value for YTicsFactor is 1.0 . </p>
<p> Example: </p>
<p> Suppose you get values ranging from 0 to 700. You want to plot 7 lines and want to show 0, 1, 2, 3, 4, 5, 6, 7 instead of 0, 100, 200, 300, 400, 500, 600, 700. You should write then: </p>
<p>YTics[myrouter] : 7 YTicsFactor[myrouter] : 0.01</p>
<h3>Factor</h3>
<p> If you want to multiply all numbers shown below the graph with a constant factor, use this directive to define it .. </p>
<p> Example: </p>
<pre>
  Factor[as400]: 4096
</pre>
<h3>Step</h3>
<p> Change the default step from 5 * 60 seconds to something else (I have not tested this much &#8230;) </p>
<p> Example: </p>
<pre>
 Step[myrouter]: 60
</pre>
<h3>PNGTitle</h3>
<p> When using rateup for graph generation, this will print the given title in the graph it generates. </p>
<p> Example: </p>
<pre>
 PNGTitle[myrouter]: WAN Link UK-US
</pre>
<h3>Options</h3>
<p> The <i>Options</i> Keyword allows you to set some boolean switches:</p>
<dl>
<dt>growright</p>
<dd> The graph grows to the left by default. This option flips the direction of growth causing the current time to be at the right edge of the graph and the history values to the left of it.</p>
<dt>bits</p>
<dd> All the monitored variable values are multiplied by 8 (i.e. shown in bits instead of bytes) &#8230; looks much more impressive :-) It also affects the &#8216;factory default&#8217; labeling and units for the given target.</p>
<dt>perminute</p>
<dd> All the monitored variable values are multiplied by 60 (i.e. shown in units per minute instead of units per second) in case of small values more accurate graphs are displayed. It also affects the &#8216;factory default&#8217; labeling and units for the given target.</p>
<dt>perhour</p>
<dd> All the monitored variable values are multiplied by 3600 (i.e. shown in units per hour instead of units per second) in case of small values more accurate graphs are displayed. It also affects the &#8216;factory default&#8217; labeling and units for the given target.</p>
<dt>noinfo</p>
<dd> Suppress the information about uptime and device name in the generated webpage.</p>
<dt>nopercent</p>
<dd> Don&#8217;t print usage percentages.</p>
<dt>transparent</p>
<dd> Make the background of the generated gifs transparent.</p>
<dt>integer</p>
<dd> Print summary lines below graph as integers without commas.</p>
<dt>dorelpercent</p>
<dd> The relative percentage of IN-traffic to OUT-traffic is calculated and displayed in the graph as an additional line. Note: Only a fixed scale is available (from 0 to 100%). Therefore if IN-traffic is greater than OUT-traffic then 100% is displayed. If you suspect that your IN-traffic is not always less than or equal to your OUT-traffic you are urged to not use this options. Note: If you use this option in combination with the <i>Colours</i> options, a fifth colour-name colour-value pair is required there.</p>
<dt>avgpeak</p>
<dd> There are some ISPs who use the average Peak values to bill their customers. Using this option <font SIZE="-1">MRTG</font> displays these values for each graph. The value is built by averaging the max 5 minute traffic average for each &#8216;step&#8217; shown in the graph. For the Weekly graph this means that it builds the average of all 2 hour intervals 5 minute peak values. (Confused? Thought so!)</p>
<dt>gauge</p>
<dd> Treat the values gathered from target as &#8216;current status&#8217; measurements and not as ever incrementing counters. This would be useful to monitor things like disk space, processor load, temperature, and the like &#8230; </p>
<p> In the absence of &#8216;gauge&#8217; or &#8216;absolute&#8217; options, <font SIZE="-1">MRTG</font> treats variables as a counters and calculates the difference between the current and the previous value and divides that by the elapsed time between the last two readings to get the value to be plotted.</p>
<dt>absolute</p>
<dd> This is for counter type data sources which reset their value when they are read. This means that rateup does not have to build the difference between the current and the last value read from the data source. The value obtained is still divided by the elapsed time between the current and the last reading, which makes it different from the &#8216;gauge&#8217; option. Useful for external data gatherers.</p>
<dt>derive</p>
<dd> If you are using rrdtool as logger/grapher you can use a third type of data source. Derive is like counter, except that it is not required to go <font SIZE="-1">UP</font> all the time. It is useful for situations where the change of some value should be graphed.</p>
<dt>unknaszero</p>
<dd> Log unknown data as zero instead of the default behaviour of repeating the last value seen. Be careful with this, often a flat line in the graph is much more obvious than a line at 0.</p>
<dt>withzeroes</p>
<dd> Normally we ignore all values which are zero when calculating the average transfer rate on a line. If this is not desirable use this option.</p>
<dt>noborder</p>
<dd> If you are using rateup to log data, <font SIZE="-1">MRTG</font> will create the graph images. Normally these images have a shaded border around them. If you do not want the border to be drawn, enable this option. This option has no effect if you are not using rateup.</p>
<dt>noarrow</p>
<dd> As with the option above, this effects rateup graph generation only. Normally rateup will generate graphs with a small arrow showing the direction of the data. If you do not want this arrow to be drawn, enable this option. This option has no effect if you are not using rateup.</p>
<dt>noi</p>
<dd> When using rateup for graph generation, you can use this option to stop rateup drawing a graph for the &#8216;I&#8217; or first variable. This also removes entries for this variable in the <font SIZE="-1">HTML</font> page <font SIZE="-1">MRTG</font> generates, and will remove the peaks for this variable if they are enabled. This allows you to hide this data, or can be very useful if you are only graphing one line of data rather than two. This option is not destructive &#8211; any data received for the the variable continued to be logged, it just isn&#8217;t shown.</p>
<dt>noo</p>
<dd> Same as above, except relating to the &#8216;O&#8217; or second variable.</p>
<dt>nobanner</p>
<dd> When using rateup for graph generation, this option disables <font SIZE="-1">MRTG</font> adding the <font SIZE="-1">MRTG</font> banner to the <font SIZE="-1">HTML</font> pages it generates.</p>
<dt>nolegend</p>
<dd> When using rateup for graph generation, this option will stop <font SIZE="-1">MRTG</font> from creating a legend at the bottom of the <font SIZE="-1">HTML</font> pages it generates.</p>
<dt>printrouter</p>
<dd> When using rateup for graph generation, this option will print the router name in the graph it generates. This option is overridden by the value of PNGTitle if one is given</p>
<dt>pngdate</p>
<dd> When using rateup for graph generation, this option will print a timestamp in the graph it generates, including a timezone if one is specified by the &#8216;Timezone&#8217; parameter. This is aequivalent to setting TimeStrPost[x]: <font SIZE="-1">RU</font></p>
<dt>logscale</p>
<dd> The <code>logscale</code> option causes rateup to display the data with the Y axis scaled logarithmically. Doing so allows the normal traffic to occupy the majority of the vertical range, while still showing any spikes at their full height. </p>
<p> <code>logscale</code> displays all the available data and will always produce well-behaved graphs. People often consider a logarithmically scaled graph counterintuitive, however, and thus hard to interpret.</p>
<dt>expscale</p>
<dd> The <code>expscale</code> option causes rateup to display the data with the Y axis scaled exponentially. Doing so emphasizes small changes at the top of the scale; this can be useful when graphing values that fluctuate by a small amount near the top of the scale, such as line voltage. </p>
<p> <code>expscale</code> is essentially the inverse of <code>logscale</code>.</p>
<dt>secondmean</p>
<dd> The <code>secondmean</code> option sets the maximum value on the graph to the mean of the data greater than the mean of all data. This produces a graph that focuses more on the typical data, while clipping large peaks. </p>
<p> Using <code>secondmean</code> will give a more intutive linearly scaled graph, but can result in a uselessly high or low scale in some rare situations (specifically, when the data includes a large portion of values far from the actual mean) </p>
<p> If a target includes both <code>logscale</code> and <code>secondmean</code> in the options, the <code>secondmean</code> takes precedence.</dl>
<p> Example: </p>
<pre>
 Options[myrouter]: growright, bits
</pre>
<h3>kilo</h3>
<p> Use this option to change the multiplier value for building prefixes. Defaultvalue is 1000. This tag is for the special case that 1kB = 1024B, 1MB = 1024kB and so far. </p>
<p> Example: </p>
<pre>
 kilo[myrouter]: 1024
</pre>
<h3>kMG</h3>
<p> Change the default multiplier prefixes (,k,M,G,T,P). In the tag <i>ShortLegend</i> define only the basic units. Format: Comma separated list of prefixed. Two consecutive commas or a comma at start or end of the line gives no prefix on this item. If you do not want prefixes, just put two consecutive commas. If you want to skip a magnitude select &#8216;-&#8216; as value. </p>
<p> Example: velocity in nm/s (nanometers per second) displayed in nm/h. </p>
<p>ShortLegend[myrouter] : m / h<br />
                                kMG[myrouter] : n,<br />
    u, m, , k, M, G, T, P options[myrouter] : perhour</p>
<h3>Colours</h3>
<p> The <i>Colours</i> tag allows you to override the default colour scheme. Note: All 4 of the required colours must be specified here. The colour name (&#8216;Colourx&#8217; below) is the legend name displayed, while the <font SIZE="-1">RGB</font> value is the real colour used for the display, both on the graph and in the html doc. </p>
<p> Format is: Col1#RRGGBB,Col2#RRGGBB,Col3#RRGGBB,Col4#RRGGBB </p>
<p> Important: If you use the <i>dorelpercent</i> options tag a fifth colour name colour value pair is required: Col1#RRGGBB,Col2#RRGGBB,Col3#RRGGBB,Col4#RRGGBB,Col5#RRGGBB</p>
<dl>
<dt>Colour1</p>
<dd> First variable (normally Input) on default graph.</p>
<dt>Colour2</p>
<dd> Second variable (normally Output) on default graph.</p>
<dt>Colour3</p>
<dd> Max first variable (input).</p>
<dt>Colour4</p>
<dd> Max second variable (output).</p>
<dt><font SIZE="-1">RRGGBB</font></p>
<dd> 2 digit hex values for Red, Green and Blue.</dl>
<p> Example: </p>
<pre>
 Colours[myrouter]: GREEN#00eb0c,BLUE#1000ff,DARK GREEN#006600,VIOLET#ff00ff
</pre>
<h3>Background</h3>
<p> With the <i>Background</i> tag you can configure the background colour of the generated <font SIZE="-1">HTML</font> page. </p>
<p> Example: </p>
<pre>
 Background[myrouter]: #a0a0a0a
</pre>
<h3>YLegend, ShortLegend, Legend[1234]</h3>
<p> The following keywords allow you to override the text displayed for the various legends of the graph and in the <font SIZE="-1">HTML</font> document:</p>
<dl>
<dt>YLegend</p>
<dd> The Y-axis label of the graph. Note that a text which is too long to fit in the graph will be silently ignored.</p>
<dt>ShortLegend</p>
<dd> The units string (default &#8216;b/s&#8217;) used for Max, Average and Current</p>
<dt>Legend[1234IO]</p>
<dd> The strings for the colour legend.</dl>
<p> Example: </p>
<p>YLegend[myrouter] : Bits per Second<br />
                        ShortLegend[myrouter] : b /<br />
                                                s<br />
                                                    Legend1[myrouter] : Incoming Traffic in Bits per Second<br />
                                                                            Legend2[myrouter] : Outgoing Traffic in Bits per Second<br />
                                                                                                    Legend3[myrouter] : Maximal 5 Minute Incoming Traffic<br />
                                                                                                                            Legend4[myrouter] : Maximal 5 Minute Outgoing Traffic<br />
                                                                                                                                                    LegendI[myrouter] : &amp;nbsp;<br />
In : LegendO[myrouter] : &amp;nbsp;<br />
Out:</p>
<p> Note, if <i>LegendI</i> or <i>LegendO</i> are set to an empty string with </p>
<pre>
 LegendO[myrouter]:
</pre>
<p> The corresponding line below the graph will not be printed at all.</p>
<h3>Timezone</h3>
<p> If you live in an international world, you might want to generate the graphs in different timezones. This is set in the <font SIZE="-1">TZ</font> variable. Under certain operating systems like Solaris, this will provoke the localtime call to give the time in the selected timezone. </p>
<p> Example: </p>
<pre>
 Timezone[myrouter]: Japan
</pre>
<p> The Timezone is the standard timezone of your system, ie Japan, Hongkong, <font SIZE="-1">GMT</font>, <font SIZE="-1">GMT+1</font> etc etc.</p>
<h3>Weekformat</h3>
<p> By default, mrtg (actually rateup) uses the <i><a href="/docs/linux/man/3-strftime/">strftime</a></i>(3) &#8216;%V&#8217; option to format week numbers in the monthly graphs. The exact semantics of this format option vary between systems. If you find that the week numbers are wrong, and your system&#8217;s <i><a href="/docs/linux/man/3-strftime/">strftime</a></i>(3) routine supports it, you can try another format option. The <font SIZE="-1">POSIX</font> &#8216;%V&#8217; option correspond to the widely used <font SIZE="-1">ISO</font> 8601 week numbering standard. The week format character should be specified as a single letter; either W, V, or U. </p>
<p> The <font SIZE="-1">UNIX</font> version of rateup uses the libc implementation of strftime. On Windows, the native strftime implementation does not know about <tt>%V</tt>. So there we use a different implementation of strftime that does support <tt>%V</tt>. </p>
<p> Example: </p>
<pre>
 Weekformat[myrouter]: W
</pre>
<h3>RRDRowCount</h3>
<p> This affects the creation of new rrd files. By default rrds are created to hold about 1 day&#8217;s worth of high resolution data. (plus 1 week of 30 minute data, 2 months of 2 hour data and 2 years of 1 day data). With this Keyword you can change the number of base interval entries configured for new rrds as they get created. Note that you must take the interval time into account. </p>
<p> Example: </p>
<pre>
 RRDRowCount[myrouter]: 1600
</pre>
<h3>RRDRowCount30m</h3>
<p> As per RRDRowCount, but for the <font SIZE="-1">RRA</font>&#8216;s -typically- used for 30 minute data. Even so, you must still take the base interval into account. Leaving out this keyword will force the old default of 800 rows. </p>
<p> Example: </p>
<pre>
 RRDRowCount30m[myrouter]: 800
</pre>
<h3>RRDRowCount2h</h3>
<p> As per RRDRowCount, but for the <font SIZE="-1">RRA</font>&#8216;s -typically- used for 2 hour data. Even so, you must still take the base interval into account. Leaving out this keyword will force the old default of 800 rows. </p>
<p> Example: </p>
<pre>
 RRDRowCount2h[myrouter]: 400
</pre>
<h3>RRDRowCount1d</h3>
<p> As per RRDRowCount, but for the <font SIZE="-1">RRA</font>&#8216;s -typically- used for 1 day data. Even so, you must still take the base interval into account. Leaving out this keyword will force the old default of 800 rows. </p>
<p> Example: </p>
<pre>
 RRDRowCount1d[myrouter]: 200
</pre>
<h3>RRDHWRRAs</h3>
<p> Normally the RRDs created by <font SIZE="-1">MRTG</font> will just contain the information gathered directly from the respective target. With this option you can tap into rrdtools advanced aberrant behaviour detection module based on Holt-Winters forecasting. The RRDHWRRAs property specifies the Holt-Winters RRAs as described in the rrdcreate manual page. </p>
<p> Note, this setting will only affect newly created RRDs (targets). </p>
<p> Example: </p>
<pre>
 RRDHWRRAs[myrouter]: RRA:HWPREDICT:1440:0.1:0.0035:288
</pre>
<h3>TimeStrPos</h3>
<p> This defines placement of the timestamp string on the image. Possible values are <font SIZE="-1">RU</font>, <font SIZE="-1">LU</font>, <font SIZE="-1">RL</font>, <font SIZE="-1">LL</font> (which stand, respectively, for RightUpper, LeftUpper, RightLower and LeftLower corner) and <font SIZE="-1">NO</font> (for no timestamp). By default, no timestamp is placed on the image. </p>
<p> Example: </p>
<pre>
 TimeStrPos[myrouter]: RU
</pre>
<h3>TimeStrFmt</h3>
<p> Using this keyword you may specify format of the timestamp to be placed on the image (if enabled by the TimeStrPos keyword). Specified string will be used by the <i>strftime()</i> function &#8211; see <i><a href="/docs/linux/man/3-strftime/">strftime</a></i>(3) documentation for conversion specifiers available on your system. Default format: <tt>%Y</tt>-%m-%d <tt>%H:</tt>%M </p>
<p> Example: </p>
<pre>
 TimeStrFmt[myrouter]: %H:%M:%S
</pre>
<h2>THRESHOLD CHECKING</h2>
<p> Through its threshold checking functionality mrtg is able to detect threshold problems for the various targets and can call external scripts to handle those problems (e.g. send email or a page to an administrator). </p>
<p> Threshold checking is configured through the following parameters:</p>
<h3>ThreshDir (<font SIZE="-1">GLOBAL</font>)</h3>
<p> By defining ThreshDir to point to a writable directory, <font SIZE="-1">MRTG</font> will only alert you when a threshold boundary has been crossed. </p>
<p> Example: </p>
<pre>
 ThreshDir: /var/mrtg/thresh
</pre>
<h3>ThreshHyst (<font SIZE="-1">GLOBAL</font>)</h3>
<p> If a threshold is broken, and you have a threshdir defined, then mrtg will send mail once the threshold becomes &#8216;unborken&#8217; to avoid situations where broken and unbroken messages get sent in close succession, we only send an unbroken message once the curent value is 0.1 (10%) away from the threshold. using the ThreshHyst config variable you can customize this value. </p>
<p> Example for 5%: </p>
<pre>
 ThreshHyst: 0.05
</pre>
<h3>ThreshMailServer (<font SIZE="-1">GLOBAL</font>)</h3>
<p> Adderss of an <font SIZE="-1">SMTP</font> server which is going to accept mail about Thresholds being broken and unbroken.</p>
<h3>ThreshMailSender (<font SIZE="-1">GLOBAL</font>)</h3>
<p> What is the sender address of the threshold mail. </p>
<p> Example: </p>
<pre>
 ThreshMailSender: mrtg [at] example.com
</pre>
<h3>ThreshMailAddress (<font SIZE="-1">PER</font> <font SIZE="-1">TARGET</font>)</h3>
<p> Email address for Threshold related Mails. This will only work if a mailserver has been configured. </p>
<p> Example: </p>
<p>ThreshMailAddress[_] : admin[at] example.com<br />
                           ThreshMailAddress[router]:</p>
<p> This would bring threshold releaed mail to all but the target called &#8216;router&#8217;.</p>
<h3>ThreshMinI (<font SIZE="-1">PER</font> <font SIZE="-1">TARGET</font>)</h3>
<p> This is the minimum acceptable value for the Input (first) parameter. If the parameter falls below this value, the program specified in ThreshProgI will be run and a mail will be sent to the ThreshMailAddress if specified. If the value ends in &#8216;%&#8217; then the threshold is defined relative to MaxBytes.</p>
<h3>ThreshMaxI (<font SIZE="-1">PER</font> <font SIZE="-1">TARGET</font>)</h3>
<p> Works the same as TheshMinI but it acts when the value is higher than ThreshMaxI.</p>
<h3>ThreshDesc (<font SIZE="-1">PER</font> <font SIZE="-1">TARGET</font>)</h3>
<p> Its value will be assigned to the environment variable <font SIZE="-1">THRESH_DESC</font> before any of the programs mentioned below are called. The programs can use the value of this variable to produce more user-friendly output.</p>
<h3>ThreshProgI (<font SIZE="-1">PER</font> <font SIZE="-1">TARGET</font>)</h3>
<p> This defines a program to be run if ThreshMinI or ThreshMaxI is broken. <font SIZE="-1">MRTG</font> passes 3 arguments: the <tt>$router</tt> variable, the threshold value broken, and the current parameter value.</p>
<h3>ThreshProgOKI (<font SIZE="-1">PER</font> <font SIZE="-1">TARGET</font>)</h3>
<p> This defines a program to be run if the parameter is currently <font SIZE="-1">OK</font> (based on ThreshMinI and ThreshMaxI), but wasn&#8217;t <font SIZE="-1">OK</font> on the previous running &#8212; based on the files found in ThreshDir. <font SIZE="-1">MRTG</font> passes 3 arguments: the <tt>$router</tt> variable the unbroken threshold value, and the current parameter value.</p>
<h3>ThreshMinO, ThreshMaxO, ThreshProgO, and ThreshProgOKO</h3>
<p> These work the same as their *I counterparts, except on the Output (second) parameter.</p>
<h3>SetEnv</h3>
<p> When calling threshold scripts from within your cfg file you might want to pass some data on to the script. This can be done with the SetEnv configuration option which takes a series of environment variable assignments. Note that the quotes are mandatory. This does not work for external scripts. It is not possible to set environment variables per target. </p>
<p> Example: </p>
<p>SetEnv[myrouter] : EMAIL = &#8220;contact_email [at] someplace.net&#8221; HOST = &#8220;www.some_server.net&#8221;</p>
<h3><font SIZE="-1">HW</font> Failure Bassed Threshold Checking</h3>
<p> When using rrd based logging with <font SIZE="-1">HW</font> RRAs defined. You can use the confidence bounds violations stored in the <font SIZE="-1">FAILURES</font> <font SIZE="-1">RRA</font> for threshold based alerts. </p>
<p> There the all target specific threshold variables have a Hold-Winters counterpart: </p>
<pre>
 ThreshMailAddress -&gt; HWThreshMailAddress
 ThreshMinI        -&gt; HWThreshMinI
 ...
</pre>
<p> The global variables for threshold checking are shared except for the </p>
<pre>
 ThreshHyst        -&gt; HWThreshHyst
</pre>
<p> And HWThreshDesc sets the <font SIZE="-1">HWTHRESH_DESC</font> variable.</p>
<h2>PER TARGET DEFAULT VALUES</h2>
<h3>Pre- and Postfix</h3>
<p> To save yourself some typing you can define a target called &#8216;^&#8217;. The text of every Keyword you define for this target will be <font SIZE="-1">PREPENDED</font> to the corresponding Keyword of all the targets defined below this line. The same goes for a Target called &#8216;$&#8217; but its text will be <font SIZE="-1">APPENDED</font>. </p>
<p> Note that a space is inserted between the prepended text and the Keyword value, as well as between the Keyword value and the appended text. This works well for text-valued Keywords, but is not very useful for other Keywords. See the &#8220;default&#8221; target description below. </p>
<p> The example will make mrtg use a common header and a common contact person in all the pages generated from targets defined later in this file. </p>
<p> Example: </p>
<p>PageTop[^] : &lt;H1&gt; NoWhere Unis Traffic Stats&lt;/ H1&gt;&lt;HR&gt;<br />
                 PageTop[$] : Contact Peter Norton if you have any questions&lt;HR&gt;</p>
<p> To remove the prepend/append value, specify an empty value, e.g.: </p>
<p>PageTop[^] : PageTop[$]:</p>
<h3>NoSpaceChar</h3>
<p> With <font SIZE="-1">PREPEND</font> and <font SIZE="-1">APPEND</font> (see below) there is normally a space inserted between the local value and the <font SIZE="-1">PRE-</font> or <font SIZE="-1">APPEND</font> value. Sometimes this is not desirable. You can use the global option <i>NoSpaceChar</i> to define a character which can be mentioned at the end of a $ or ^ definition in order to supress the space. </p>
<p> Example: </p>
<p>NoSpaceChar : ~Target[^] : 1.3.6.1.4.1.482.50.2.4.20.0 &amp; 1.3.6.1.4.1.482.50.2.4.21.0 : get @~Target[a] : a.tolna.net<br />
                                                                                                             Target[b] : b.tolna.net<br />
                                                                                                                             Target[c] : c.tolna.net<br />
                                                                                                                                             Target[d] : d.tolna.net</p>
<h3>Default Values</h3>
<p> The target name &#8216;_&#8217; specifies a default value for that Keyword. In the absence of explicit Keyword value, the prepended and the appended keyword value, the default value will be used. </p>
<p> Example: </p>
<p>YSize[_] : 150 Options[_] : growright, bits, nopercent WithPeak[_] : ymw Suppress[_] : y MaxBytes[_] : 1250000</p>
<p> To remove the default value and return to the &#8216;factory default&#8217;, specify an empty value, e.g.: </p>
<pre>
 YLegend[_]:
</pre>
<p> There can be several instances of setting the default/prepend/append values in the configuration file. The later setting replaces the previous one for the rest of the configuration file. The default/prepend/append values used for a given keyword/target pair are the ones that were in effect at the point in the configuration file where the target was mentioned for the first time. </p>
<p> Example: </p>
<p> MaxBytes[_]: 1250000<br />
 Target[myrouter.somplace.edu.2]: 2:public [at] myrouter.somplace.edu<br />
 MaxBytes[_]: 8000<br />
 Title[myrouter.somplace.edu.2]: Traffic Analysis for myrouter.somplace.edu IF 2</p>
<p> The default <i>MaxBytes</i> for the target myrouter.someplace.edu.2 in the above example will be 1250000, which was in effect where the target name myrouter.someplace.edu.2 first appeared in the config file.</p>
<h2>COMMAND LINE OPTIONS</h2>
<dl>
<dt><code>&#8211;user</code> <i>username</i> and <code>&#8211;group</code> <i>groupname</i></p>
<dd> Run as the given user and/or group. (Unix Only)</p>
<dt><code>&#8211;lock-file</code> <i>filename</i></p>
<dd> Use an alternate lock-file (the default is to use the configuration-file appended with <tt>&quot;_l&quot;</tt>).</p>
<dt><code>&#8211;confcache-file</code> <i>filename</i></p>
<dd> Use an alternate confcache-file (the default is to use the configuration-file appended with <tt>&quot;.ok&quot;</tt>)</p>
<dt><code>&#8211;logging</code> <i>filename</i>|<code>eventlog</code></p>
<dd> If this is set to writable filename, all output from mrtg (warnings, debug messages, errors) will go to <i>filename</i>. If you are running on Win32 you can specify <code>eventlog</code> instead of a filename which will send all error to the windows event log. </p>
<p> <font SIZE="-1"><code>NOTE:</code></font> Note, there is no Message <font SIZE="-1">DLL</font> for mrtg included with mrtg. This has the side effect that the windows event logger will display a nice message with every entry in the event log, complaing about the fact that mrtg has no message dll. If you go to the mrtg contrib download area (on the website) you will find the mrtg-message-dll.zip which does contain such a thing.</p>
<dt><code>&#8211;daemon</code></p>
<dd> Put <font SIZE="-1">MRTG</font> into the background, running as a daemon. This works the same way as the config file option, but the switch is required for proper <font SIZE="-1">FHS</font> operation (because /var/run is writable only by root)</p>
<dt><code>&#8211;fhs</code></p>
<dd> Configure all mrtg paths to conform to the <font SIZE="-1">FHS</font> specification; <a rel="nofollow" href="http://www.pathname.com/fhs/">http://www.pathname.com/fhs/</a></p>
<dt><code>&#8211;check</code></p>
<dd> Only check the cfg file for errors. Do not do anything.</p>
<dt><code>&#8211;pid-file=s</code></p>
<dd> Define the name and path of the pid file for mrtg running as a daemon</p>
<dt><code>&#8211;debug=s</code></p>
<dd> Enable debug options. The argument of the debug option is a comma separated list of debug values: </p>
<pre>
 cfg  - watch the config file reading
 dir  - directory mangeling
 base - basic program flow 
 tarp - target parser
 snpo - snmp polling 
 coca - confcache operations
 fork - forking view 
 time - some timing info
 log  - logging of data via rateup or rrdtool
 eval - print eval strings before evaluting them
 prof - add hires timing info the rrd calls
</pre>
<p> Example: </p>
<pre>
 --debug=&quot;cfg,snpo&quot;
</pre>
</dl>
<h2>EXIT CODES</h2>
<p> An exit code of 0 indicates that all targets were successful. Generally speaking, most codes greater than 0 indicate that there was an unrecoverable problem. One exception to this is code 91, which indicates that at least one of the targets was successful. A partial listing of the codes follows: </p>
<pre>
  0: All targets sucessful
  2: Config error (can't read, fatal error in config, etc)
 17: Another MRTG process is processing config
 91: At least one target sucessful
 92: No targets were sucessful
</pre>
<h2>EXAMPLES</h2>
<h3>Minimal mrtg.cfg</h3>
<p> WorkDir: /usr/tardis/pub/www/stats/mrtg<br />
 Target[r1]: 2:public [at] myrouter.somplace.edu<br />
 MaxBytes[r1]: 8000<br />
 Title[r1]: Traffic Analysis ISDN<br />
 PageTop[r1]: &lt;H1&gt;Stats for our ISDN Line&lt;/H1&gt;</p>
<h3>Cfg for several Routers.</h3>
<pre><code>
 WorkDir: /usr/tardis/pub/www/stats/mrtg
 Title[^]: Traffic Analysis for
 PageTop[^]: &lt;H1&gt;Stats for
 PageTop[$]: Contact The Chief if you notice anybody&lt;HR&gt;
 MaxBytes[_]: 8000
 Options[_]: growright
 Title[isdn]: our ISDN Line
 PageTop[isdn]: our ISDN Line&lt;/H1&gt;
 Target[isdn]: 2:public [at] router.somplace.edu
 Title[backb]: our Campus Backbone
 PageTop[backb]: our Campus Backbone&lt;/H1&gt;
 Target[backb]: 1:public [at] router.somplace.edu
 MaxBytes[backb]: 1250000
#the following line removes the default prepend value
#defined above
 Title[^]:
 Title[isdn2]: Traffic for the Backup ISDN Line
 PageTop[isdn2]: our ISDN Line&lt;/H1&gt;
 Target[isdn2]: 3:public [at] router.somplace.edu
</code></pre>
<h2>AUTHOR</h2>
<p> Tobias Oetiker &lt;tobi [at] oetiker.ch&gt; and many contributors </p>
<h2>Index</h2>
<dt><a href="#lbBD">PER TARGET CONFIGURATION</a></p>
<dd>
<dt><a href="#lbBH">OPTIONAL PER TARGET KEYWORDS</a></p>
<dd>
<dt><a href="#lbCV">THRESHOLD CHECKING</a></p>
<dd>
<dt><a href="#lbDJ">PER TARGET DEFAULT VALUES</a></p>
<dd>
<dt><a href="#lbDN">COMMAND LINE OPTIONS</a></p>
<dd>
<dt><a href="#lbDO">EXIT CODES</a></p>
<dd>
<dt><a href="#lbDP">EXAMPLES</a></p>
<dd>
<dt><a href="#lbDS">AUTHOR</a></p>
<dd></dl>
