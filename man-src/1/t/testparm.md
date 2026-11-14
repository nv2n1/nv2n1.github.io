---
title: "testparm(1)"
name: "testparm"
section: "1"
letter: "t"
url: "/docs/linux/man/1-testparm/"
description: "testparm – check an smb.conf configuration file for internal correctness"
---

<h2 class="name">NAME</h2>
<p> testparm &#8211; check an smb.conf configuration file for internal correctness </p>
<h2>SYNOPSIS</h2>
<dl>
<dt>
<dd>testparm [-s|&#8211;suppress-prompt] [&#8211;help] [-v|&#8211;verbose] {config filename} [hostname hostIP]</dl>
<h2>DESCRIPTION</h2>
<p> This tool is part of the <code><a href="/docs/linux/man/7-samba/">samba</a></code>(7) suite. </p>
<p> testparm is a very simple test program to check an <code><a href="/docs/linux/man/8-smbd/">smbd</a></code>(8) configuration file for internal correctness. If this program reports no problems, you can use the configuration file with confidence that smbd will successfully load the configuration file. </p>
<p> Note that this is <i>NOT</i> a guarantee that the services specified in the configuration file will be available or will operate as expected. </p>
<p> If the optional host name and host IP address are specified on the command line, this test program will run through the service entries reporting whether the specified host has access to each service. </p>
<p> If testparm finds an error in the smb.conf file it returns an exit code of 1 to the calling program, else it returns an exit code of 0. This allows shell scripts to test the output from testparm.</p>
<h2>OPTIONS</h2>
<p> -s|&#8211;suppress-prompt</p>
<dl>
<dt>
<dd> Without this option, testparm will prompt for a carriage return after printing the service names and before dumping the service definitions.</dl>
<p> -V|&#8211;version</p>
<dl>
<dt>
<dd> Prints the program version number.</dl>
<p> &#8211;option=&lt;name&gt;=&lt;value&gt;</p>
<dl>
<dt>
<dd> Set the <code><a href="/docs/linux/man/5-smb-conf/">smb.conf</a></code>(5) option &quot;&lt;name&gt;&quot; to value &quot;&lt;value&gt;&quot; from the command line. This overrides compiled-in defaults and options read from the configuration file.</dl>
<p> -?|&#8211;help</p>
<dl>
<dt>
<dd> Print a summary of command line options.</dl>
<p> &#8211;usage</p>
<dl>
<dt>
<dd> Display brief usage message.</dl>
<p> -d|&#8211;debuglevel=level</p>
<dl>
<dt>
<dd> <i>level</i> is an integer from 0 to 10. The default value if this parameter is not specified is 1. </p>
<p> The higher this value, the more detail will be logged to the log files about the activities of the server. At level 0, only critical errors and serious warnings will be logged. Level 1 is a reasonable level for day-to-day running &#8211; it generates a small amount of information about operations carried out. </p>
<p> Levels above 1 will generate considerable amounts of log data, and should only be used when investigating a problem. Levels above 3 are designed for use only by developers and generate HUGE amounts of log data, most of which is extremely cryptic. </p>
<p> Note that specifying this parameter here will override the m[blue]<code>log level</code>m[] parameter in the smb.conf file.</dl>
<p> -v|&#8211;verbose</p>
<dl>
<dt>
<dd> If this option is specified, testparm will also output all options that were not used in <code><a href="/docs/linux/man/5-smb-conf/">smb.conf</a></code>(5) and are thus set to their defaults.</dl>
<p> &#8211;parameter-name parametername</p>
<dl>
<dt>
<dd> Dumps the named parameter. If no section-name is set the view is limited by default to the global section. It is also possible to dump a parametrical option. Therefore the option has to be separated by a colon from the parametername.</dl>
<p> &#8211;section-name sectionname</p>
<dl>
<dt>
<dd> Dumps the named section.</dl>
<p> &#8211;show-all-parameters</p>
<dl>
<dt>
<dd> Show the parameters, type, possible values.</dl>
<p> -l|&#8211;skip-logic-checks</p>
<dl>
<dt>
<dd> Skip the global checks.</dl>
<p> configfilename</p>
<dl>
<dt>
<dd> This is the name of the configuration file to check. If this parameter is not present then the default <code><a href="/docs/linux/man/5-smb-conf/">smb.conf</a></code>(5) file will be checked.</dl>
<p> hostname</p>
<dl>
<dt>
<dd> If this parameter and the following are specified, then testparm will examine the <i>hosts allow</i> and <i>hosts deny</i> parameters in the <code><a href="/docs/linux/man/5-smb-conf/">smb.conf</a></code>(5) file to determine if the hostname with this IP address would be allowed access to the smbd server. If this parameter is supplied, the hostIP parameter must also be supplied.</dl>
<p> hostIP</p>
<dl>
<dt>
<dd> This is the IP address of the host specified in the previous parameter. This address must be supplied if the hostname parameter is supplied.</dl>
<h2>FILES</h2>
<p> <code><a href="/docs/linux/man/5-smb-conf/">smb.conf</a></code>(5)</p>
<dl>
<dt>
<dd> This is usually the name of the configuration file used by <code><a href="/docs/linux/man/8-smbd/">smbd</a></code>(8).</dl>
<h2>DIAGNOSTICS</h2>
<p> The program will issue a message saying whether the configuration file loaded OK or not. This message may be preceded by errors and warnings if the file did not load. If the file was loaded OK, the program then dumps all known service details to stdout.</p>
<h2>VERSION</h2>
<p> This man page is part of version 4.11.6-Ubuntu of the Samba suite.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-smb-conf/">smb.conf</a></code>(5), <code><a href="/docs/linux/man/8-smbd/">smbd</a></code>(8)</p>
<h2>AUTHOR</h2>
<p> The original Samba software and related utilities were created by Andrew Tridgell. Samba is now developed by the Samba Team as an Open Source project similar to the way the Linux kernel is developed. </p>
<h2>Index</h2>
