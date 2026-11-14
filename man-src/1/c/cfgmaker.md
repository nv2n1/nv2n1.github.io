---
title: "cfgmaker(1)"
name: "cfgmaker"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cfgmaker/"
description: "cfgmaker – Creates mrtg.cfg files (for mrtg-2.17.4)"
---

<h2 class="name">NAME</h2>
<p> cfgmaker &#8211; Creates mrtg.cfg files (for mrtg-2.17.4) </p>
<h2>SYNOPSIS</h2>
<p> cfgmaker [options] [community@]router [[options] [community@]router &#8230;]</p>
<h2>OPTIONS</h2>
<pre><code>
 --ifref=nr    interface references by Interface Number (default)
 --ifref=ip                     ... by Ip Address
 --ifref=eth                        ... by Ethernet Number
 --ifref=descr                      ... by Interface Description
 --ifref=name                       ... by Interface Name
 --ifref=type                       ... by Interface Type
                You may also use multiple options separated by commas,
               in which case the first available one is used:
               e.g.  --ifref=ip,name,nr
 --ifdesc=nr       interface description uses Interface Number (default)
 --ifdesc=ip                        ... uses Ip Address
 --ifdesc=eth                       ... uses Ethernet Number
 --ifdesc=descr                     ... uses Interface Description
 --ifdesc=name                      ... uses Interface Name
 --ifdesc=catname                   ... uses CatOS Interface Name
 --ifdesc=ppname                    ... uses Passport Port Name
 --ifdesc=alias                     ... uses Interface Alias
 --ifdesc=type                      ... uses Interface Type
                You may also use multiple options separated by commas,
               in which case the first available one is used:
               e.g.  --ifdesc=catname,ppname,descr,alias,ip,name,nr
 --if-filter=f     Test every interface against filter f to decide wether
                   or not to include that interface into the collection.
                   Currently f is being evaluated as a Perl expression
                   and it's truth value is used to reject or accept the
                   interface.
                   (Experimental, under development, might change)
 --if-template=templatefile
                   Replace the normal target entries for the interfaces
                   with an entry as specified by the contents in the file
                   templatefile.  The file is supposed to contain Perl
                   code to be executed to generate the lines for the
                   target in the configuration file.
                   (Experimental, under development, might change)
 --host-template=templatefile
                   In addition to creating targets for a host's interfaces
                   do also create targets for the host itself as specified
                   by the contents in the file templatefile.  The file is
                   supposed to contain Perl code to be executed to generate
                   the lines for the host related targets (such as CPU,
                   ping response time measurements etc.) in the config-
                   uration file.
                   (Experimental, under development, might change)
 --global "x: a"   add global config entries
 --no-down         do not look at admin or opr status of interfaces
 --show-op-down    show interfaces which are operatively down
 --zero-speed=spd  use this speed in bits-per-second as the interface
                   speed for all interfaces that return a speed of 0
                   via ifSpeed/ifHighSpeed.  100Mbps = 100000000
 --subdirs=format  give each router its own subdirectory, naming each per
                   "format", in which HOSTNAME and SNMPNAME will be
                   replaced by the values of those items -- for instance,
                   --subdirs=HOSTNAME or --subdirs="HOSTNAME (SNMPNAME)"
 --noreversedns    do not reverse lookup ip numbers
 --community=cmty  Set the default community string to "cmty" instead of
                   "public".
 --enable-ipv6     Enable IPv6 support, if the required libraries are
                   present. Numeric IPv6 addresses must be enclosed
                   in square brackets, e.g. public@[2001:760:4::1]:161
 --use-16bit       Use 16bit SNMP request IDs to query all routers.
 --snmp-options=:[&lt;port&gt;][:[&lt;tmout&gt;][:[&lt;retr&gt;][:[&lt;backoff&gt;][:&lt;ver&gt;]]]]
                   Specify default SNMP options to be appended to all
                   routers following.  Individual fields can be empty.
                   Routers following might override some or all of the
           options given to --snmp-options.
 --dns-domain=domain
           Specifies a domain to append to the name of all
           routers following.
 --nointerfaces    Don't do generate any configuration lines for interfaces,
                   skip the step of gathering interface information and
                   don't run any interface template code.
 --interfaces      Generate configuration lines for interfaces (this is the
                   default).  The main purpose of this option is to negate
                   an --nointerfaces appearing earlier on the command line.
 --help            brief help message
 --man             full documentation
 --version         print the version of cfgmaker
 --output=file     output filename default is STDOUT
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>Cfgmaker</code> creates <font SIZE="-1">MRTG</font> configuration files based on information pulled from a router or another <font SIZE="-1">SNMP</font> manageable device. </p>
<p> [<i>community</i><code>@</code>]<i>router</i> </p>
<p> <i>Community</i> is the community name of the device you want to create a configuration for. If not specified, it defaults to &#8216;<code>public</code>&#8216;; you might want to try this first if you do not know the community name of a device. If you are using the wrong community name you will get no response from the device. </p>
<p> <i>Router</i> is the <font SIZE="-1">DNS</font> name or the <font SIZE="-1">IP</font> number of an SNMP-managable device. Following the name you can specify 6 further options separated by colons. The full syntax looks like this: </p>
<p> <code>router</code>[:[<code>prt</code>][:[<code>tmout</code>][:[<code>retr</code>][:[<code>backoff</code>][:<code>vers</code>]]]]] </p>
<p> Of special interest may be the last parameter, <code>vers</code>. If you set this to &#8216;2&#8217; then your device will be queried with <font SIZE="-1">SNMP</font> version 2 requests. This allows you to poll the 64 bit traffic counters in the device and will thus work much better with fast interfaces (no more counter overrun). Note that the order in which the routers are specified on the command line do matter as the same order is used when the configuration file is generated. The first specified router has it&#8217;s configuration lines genrated first, followed by the lines belonging to the next router and so on. </p>
<p> Note that the first line of the generated cfg file will contain all the commandline options you used for generating it. This is to allow for the easy &#8216;regeneration&#8217; in case you want to add newhosts or make some other global change.</p>
<h3>Configuration</h3>
<p> Except for the <code>&#8211;output</code> and <code>&#8211;global</code> options, all options affect only the routers following them on the command line. If an option specified earlier on the command line reappears later on the command line with another value, the new value overrides the old value as far as remaining routers are concerned. This way options might be tailored for groups of routers or for individual routers. </p>
<p> See <code>&#8211;output</code> and <code>&#8211;global</code> for how their behaviour is affected by where or how many times they appear on the command line. </p>
<p> See the <code>Examples</code> below on how to set an option differently for multiple routers.</p>
<dl>
<dt><code>&#8211;help</code></p>
<dd> Print a brief help message and exit.</p>
<dt><code>&#8211;man</code></p>
<dd> Prints the manual page and exits.</p>
<dt><code>&#8211;version</code></p>
<dd> Print the version of cfgmaker. This should match the version of <font SIZE="-1">MRTG</font> for which config files are being created.</p>
<dt><code>&#8211;ifref</code> <code>nr</code>|<code>ip</code>|<code>eth</code>|<code>descr</code>|<code>name</code></p>
<dd> Select the interface identification method. Default is <code>nr</code> which identifies the router interfaces by their number. Unfortunately the interface numbering scheme in an <font SIZE="-1">SNMP</font> tree can change. Some routers change their numbering when new interfaces are added, others change thier numbering every full moon just for fun. </p>
<p> To work around this sad problem <font SIZE="-1">MRTG</font> can identify interfaces by 4 other properties. None of these works for all interfaces, but you should be able to find one which does fine for you. Note that especially ethernet addrsses can be problematic as some routers have the same ethernet address on most of their interface cards. </p>
<p> Select <code>ip</code> to identify the interface by its <font SIZE="-1">IP</font> number. Use <code>eth</code> to use the ethernet address for identification. Use <code>descr</code> to use the Interface description. Or use <code>name</code> to use the Interface name. </p>
<p> You can specify multiple properties if you wish, separated by commas. In this case, cfgmaker will use the first item in the list which can provide unique identification. This allows you to specify, for example, to use <font SIZE="-1">IP</font> address and to use ifName if this is not defined:<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;ifref ip,name </p>
<p> If your chosen method does not allow unique interface identification on the device you are querying, <code>cfgmaker</code> will tell you about it.</p>
<dt><code>&#8211;ifdesc</code> <code>nr</code>|<code>ip</code>|<code>eth</code>|<code>descr</code>|<code>name</code>|<code>type</code>|<code>alias</code></p>
<dd> Select what to use as the description of the interface. The description appears in the <tt>&quot;Title[]&quot;</tt> property for the target as well as the text header in the <font SIZE="-1">HTML</font> code defined in the target&#8217;s <tt>&quot;PageTop[]&quot;</tt>. Default is to use <code>nr</code> which is just the interface number which isn&#8217;t always useful to the viewer of the graphs. </p>
<p> There are 6 other properties which could be used. Use <code>ip</code> if you want to use the interface&#8217;s IP-address. Use <code>eth</code> if you want to use the interface&#8217;s ethernet address. If you want a better description, you can use either <code>descr</code>, <code>name</code> or <code>alias</code>. Exactly what each of these do varies between different equipment so you might need to experiment. For instance, for a serial interface on a Cisco router running <font SIZE="-1">IOS</font> using <code>name</code> might result in <tt>&quot;S0&quot;</tt> being the interface description , <code>descr</code> might result in <tt>&quot;Serial0&quot;</tt> and <code>alias</code> might result in <tt>&quot;Link to HQ&quot;</tt> (provided that is what is used as the interface&#8217;s <tt>&quot;description&quot;</tt> in the router&#8217;s configuration). </p>
<p> Finally, if you want to describe the interface by it&#8217;s Btype (i.e <tt>&quot;ethernetCSMA&quot;</tt>, <tt>&quot;propPointtoPoint&quot;</tt> etc) you can use <code>type</code>. </p>
<p> You can specify multiple properties if you wish, separated by commas. In this case, cfgmaker will use the first item in the list which is available for this interface. This allows you to specify, for example, to use any of the different aliases in order of preference.</p>
<dt><code>&#8211;if-filter</code> &#8216;<code>filter-expression</code>&#8216;</p>
<dd> First of all, this is under some development and is experimental. </p>
<p> Use this if you want to have better control over what interfaces gets included into the configuration. The <code>filter-expression</code> is evaluated as a piece of Perl code and is expected to return a truth value. If true, include the interface and if false, exclude the interface. </p>
<p> For a further discussion on how these filters work, see the section &#8220;Details on Filters&#8221; below.</p>
<dt><code>&#8211;if-template</code> <code>template-file</code></p>
<dd> First of all, this is under some development and is experimental. </p>
<p> Use this if you want to control what the line for each target should look like in the configuration file. The contents of the file <code>template-file</code> will be evaluated as a Perl program which generates the lines using certain variables for input and output. </p>
<p> For a further discussion on how these templates work, see the section &#8220;Details on Temaplates&#8221; below.</p>
<dt><code>&#8211;host-template</code> <code>template-file</code></p>
<dd> First of all, this is under some development and is experimental. </p>
<p> Use this if you want to have some extra targets related to the host itself such as <font SIZE="-1">CPU</font> utilization, ping response time to the host, number of busy modems etc. The contents of the file <code>template-file</code> will be evaluated once per host as a Perl program which generates the lines using certain variables for input and output. </p>
<p> For a further discussion on how these templates work, see the section &#8220;Details on Templates&#8221; below.</p>
<dt><code>&#8211;community</code> <code>community-string</code></p>
<dd> Use this to set the community for the routers following on the command line to <code>community-string</code>. Individual routers might overrride this community string by using the syntax <code>community</code><code>@</code><code>router</code>.</p>
<dt><code>&#8211;enable-ipv6</code></p>
<dd> This option enables IPv6 support. It requires the appropriate perl modules; if they are not found then IPv6 is disabled (see the ipv6 documentation). </p>
<p> cfgmaker will use IPv6 or IPv4 depending on the target. If the target is a numeric address, the protocol depends on the type of address. If the target is a hostname, cfgmaker will try to resolve the name first to an IPv6 address then to an IPv4 address. </p>
<p> IPv6 numeric addresses must be specified between square braces. </p>
<p> For example: </p>
<pre>
 cfgmaker --enable-ipv6 [2001:760:4::1]:165:::2
</pre>
<p> If the target has both an IPv6 address and an IPv4 address with the same hostname, cfgmaker first queries the target using IPv6 and falls back to IPv4 if it fails. This is useful for targets which don&#8217;t support <font SIZE="-1">SNMP</font> over IPv6.</p>
<dt><code>&#8211;use-16bit</code></p>
<dd> This option forces the use of 16bit <font SIZE="-1">SNMP</font> request IDs. Some broken <font SIZE="-1">SNMP</font> agents do not accept 32bit request IDs. Try to avoid this option as much as possible, complain to your agent vendor instead.</p>
<dt><code>&#8211;snmp-options</code> :[<code>port</code>][:[<code>timeout</code>][:[<code>retries</code>][:[<code>backoff</code>][:<code>version</code>]]]]</p>
<dd> Use this to set the default <font SIZE="-1">SNMP</font> options for all routers following on the command line. Individual values might be omitted as well as trailing colons. Note that routers might override individual (or all) values specified by <code>&#8211;snmp-options</code> by using the syntax </p>
<p> <code>router</code>[:[<code>port</code>][:[<code>timeout</code>][:[<code>retries</code>][:[<code>backoff</code>][:<code>version</code>]]]]]</p>
<dt><code>&#8211;global</code> <code>&quot;</code><i>bla: abc</i><code>&quot;</code></p>
<dd> Use this to add global options to the generated config file. You can call <code>&#8211;global</code> several times to add multiple options. The line will appear in the configuration just before the config for the next router appearing on the command line. </p>
<pre>
 --global &quot;workdir: /home/mrtg&quot;
</pre>
<p> If you want some default Options you might want to put </p>
<pre>
 --global &quot;options[_]: growright,bits&quot;
</pre>
<p> Specifying <code>&#8211;global</code> after the last router on the command line will create a line in the configuration file which will appear after all the routers.</p>
<dt><code>&#8211;noreversedns</code></p>
<dd> Do not try to reverse lookup <font SIZE="-1">IP</font> numbers &#8230; a must for <font SIZE="-1">DNS</font> free environments.</p>
<dt><code>&#8211;no-down</code></p>
<dd> Normally cfgmaker will not include interfaces which are marked anything but administratively and operationally <font SIZE="-1">UP</font>. With this switch you get them all.</p>
<dt><code>&#8211;show-op-down</code></p>
<dd> Include interfaces which are operatively down.</p>
<dt><code>&#8211;zero-speed</code> <i>speed</i></p>
<dd> Assign this speed in bits-per-second to all interfaces which return 0 for ifSpeed and ifHighSpeed. Some switches, notably Foundry equipment, return a speed of zero for some interfaces. For example, to have all interfaces reporting zero set to 100Mbps, use &#8211;zero-speed=100000000.</p>
<dt><code>&#8211;subdirs</code> <i>format</i></p>
<dd> Give each router its own subdirectory for the <font SIZE="-1">HTML</font> and graphics (or .rrd) files. The directory name is the given <i>format</i> string with a couple of pattern replacements. The string &#8220;<font SIZE="-1">HOSTNAME</font>&#8221; will be replaced by the hostname of the router (however you specified it on the <code>cfgmaker</code> commandline &#8212; it may be an actual hostname or just an <font SIZE="-1">IP</font> address), and &#8220;<font SIZE="-1">SNMPNAME</font>&#8221; will be replaced with the device&#8217;s idea of its own name (the same name that appears on the right side of the &#8220;Title&#8221; lines). For instance, a call like: </p>
<pre>
 cfgmaker --subdirs=HOSTNAME__SNMPNAME public [at] 10.10.0.18
</pre>
<p> would result in the generation of lines looking something like: </p>
<pre>
 Directory[10.10.0.18_1]: 10.10.0.18__fp2200-bothrip-1.3
</pre>
<dt><code>&#8211;output</code> <i>file</i></p>
<dd> Write the output from <code>cfgmaker</code> into the file <i>file</i>. The default is to use <tt>&quot;STDOUT&quot;</tt>. <code>&#8211;output</code> is expected to appear only once on the command line. If used multiple times, the file specified by the last <code>&#8211;output</code> will be used.</p>
<dt><code>&#8211;nointerfaces</code></p>
<dd> Don&#8217;t generate configuration lines for interfaces. </p>
<p> This makes cfgmaker skip all steps related to interfaces which means it will not do any polling of the router to retrieve interface information which speeds up the execution of cfgmaker and it will neither run any interface templates.</p>
<dt><code>&#8211;interfaces</code></p>
<dd> This makes cfgmaker generate configuration lines for interfaces (the default behaviour). </p>
<p> The main usage of this option is to negate an &#8211;nointerfaces appearing earlier on the command line.</dl>
<h3><font SIZE="-1">SNMP</font> V3 Options</h3>
<p> <code>Cfgmaker</code> supports <font SIZE="-1">SNMP</font> V3 using the <code>Net:SNMP</code> perl module. There are optional parameters affecting <font SIZE="-1">SNMP</font> operation.</p>
<dl>
<dt>&#8211;enablesnmpv3 {yes|no}</p>
<dd> The <code>&#8211;enablesnmpv3</code> option is an optional flag to check for the presence of the <code>Net::SNMP</code> libraries. <code>Cfgmaker</code> will try to determine whether this flag is required and will set the values automatically.</dl>
<p> <i>SNMPv3 Arguments</i> </p>
<p> A <font SIZE="-1">SNMP</font> context is a collection of management information accessible by a <font SIZE="-1">SNMP</font> entity. An item of management information may exist in more than one context and a <font SIZE="-1">SNMP</font> entity potentially has access to many contexts. The combination of a contextEngineID and a contextName unambiguously identifies a context within an administrative domain. In a SNMPv3 message, the contextEngineID and contextName are included as part of the scopedPDU. All methods that generate a <font SIZE="-1">SNMP</font> message optionally take a <code>&#8211;contextengineid</code> and <code>&#8211;contextname</code> argument to configure these fields.</p>
<dl>
<dt>Context Engine <font SIZE="-1">ID</font></p>
<dd> The <code>&#8211;contextengineid</code> argument expects a hexadecimal string representing the desired contextEngineID. The string must be 10 to 64 characters (5 to 32 octets) long and can be prefixed with an optional &#8220;0x&#8221;. Once the <code>&#8211;contextengineid</code> is specified it stays with the object until it is changed again or reset to default by passing in the undefined value. By default, the contextEngineID is set to match the authoritativeEngineID of the authoritative <font SIZE="-1">SNMP</font> engine.</p>
<dt>Context Name</p>
<dd> The contextName is passed as a string which must be 0 to 32 octets in length using the <code>&#8211;contextname</code> argument. The contextName stays with the object until it is changed. The contextName defaults to an empty string which represents the &#8220;default&#8221; context.</dl>
<p> <i>User-based Security Model Arguments</i> </p>
<p> The User-based Security Model (<font SIZE="-1">USM</font>) used by SNMPv3 requires that a securityName be specified using the <code>&#8211;username</code> argument. The creation of a Net::SNMP object with the version set to SNMPv3 will fail if the <code>&#8211;username</code> argument is not present. The <code>&#8211;username</code> argument expects a string 1 to 32 octets in length. </p>
<p> Different levels of security are allowed by the User-based Security Model which address authentication and privacy concerns. A SNMPv3 target will derive the security level (securityLevel) based on which of the following arguments are specified. </p>
<p> By default a securityLevel of &#8216;noAuthNoPriv&#8217; is assumed. If the <code>&#8211;authkey</code> or <code>&#8211;authpassword</code> arguments are specified, the securityLevel becomes &#8216;authNoPriv&#8217;. The <code>&#8211;authpassword</code> argument expects a string which is at least 1 octet in length. Optionally, the <code>&#8211;authkey</code> argument can be used so that a plain text password does not have to be specified in a script. The <code>&#8211;authkey</code> argument expects a hexadecimal string produced by localizing the password with the authoritativeEngineID for the specific destination device. The <tt>&quot;snmpkey&quot;</tt> utility included with the Net::SNMP distribution can be used to create the hexadecimal string (see snmpkey). </p>
<p> Two different hash algorithms are defined by SNMPv3 which can be used by the Security Model for authentication. These algorithms are <font SIZE="-1">HMAC-MD5-96</font> &#8220;<font SIZE="-1">MD5</font>&#8221; (<font SIZE="-1">RFC</font> 1321) and <font SIZE="-1">HMAC-SHA-96</font> &#8220;<font SIZE="-1">SHA-1</font>&#8221; (<font SIZE="-1">NIST</font> <font SIZE="-1">FIPS</font> <font SIZE="-1">PUB</font> 180-1). The default algorithm used by the module is <font SIZE="-1">HMAC-MD5-96</font>. This behavior can be changed by using the <code>&#8211;authprotocol</code> argument. This argument expects either the string &#8216;md5&#8217; or &#8216;sha&#8217; to be passed to modify the hash algorithm. </p>
<p> By specifying the arguments <code>&#8211;privkey</code> or <code>&#8211;privpassword</code> the securityLevel associated with the object becomes &#8216;authPriv&#8217;. According to SNMPv3, privacy requires the use of authentication. Therefore, if either of these two arguments are present and the <code>&#8211;authkey</code> or <code>&#8211;authpassword</code> arguments are missing, the creation of the object fails. The <code>&#8211;privkey</code> and <code>&#8211;privpassword</code> arguments expect the same input as the <code>&#8211;authkey</code> and <code>&#8211;authpassword</code> arguments respectively. </p>
<p> The User-based Security Model described in <font SIZE="-1">RFC</font> 3414 defines a single encryption protocol to be used for privacy. This protocol, CBC-DES &#8220;<font SIZE="-1">DES</font>&#8221; (<font SIZE="-1">NIST</font> <font SIZE="-1">FIPS</font> <font SIZE="-1">PUB</font> 46-1), is used by default or if the string &#8216;des&#8217; is passed to the <code>&#8211;privprotocol</code> argument. By working with the Extended Security Options Consortium <a rel="nofollow" href="http://www.snmp.com/eso/,">http://www.snmp.com/eso/,</a> the module also supports additional protocols which have been defined in draft specifications. The draft <a rel="nofollow" href="http://www.snmp.com/eso/draft-reeder-snmpv3-usm-3desede-00.txt">http://www.snmp.com/eso/draft-reeder-snmpv3-usm-3desede-00.txt</a> defines the support of <font SIZE="-1">CBC-3DES-EDE</font> &#8220;Triple-DES&#8221; (<font SIZE="-1">NIST</font> <font SIZE="-1">FIPS</font> 46-3) in the User-based Security Model. This protocol can be selected using the <code>&#8211;privprotocol</code> argument with the string &#8216;3desede&#8217;. The draft <a rel="nofollow" href="http://www.snmp.com/eso/draft-blumenthal-aes-usm-04.txt">http://www.snmp.com/eso/draft-blumenthal-aes-usm-04.txt</a> describes the use of <font SIZE="-1">CFB128-AES-128/192/256</font> &#8220;<font SIZE="-1">AES</font>&#8221; (<font SIZE="-1">NIST</font> <font SIZE="-1">FIPS</font> <font SIZE="-1">PUB</font> 197) in the <font SIZE="-1">USM</font>. The three <font SIZE="-1">AES</font> encryption protocols, differentiated by their key sizes, can be selected by passing &#8216;aescfb128&#8217;, &#8216;aescfb192&#8217;, or &#8216;aescfb256&#8217; to the <code>-privprotocol</code> argument.</p>
<h3>Details on Filters</h3>
<p> The purpose of the filters is to decide which interfaces to accept and which interfaces to reject. This decision is done for each interface by evaluating the filter expression as a piece of Perl code and investigating the result of the evaluation. If true, accept the interface otherwise reject it. </p>
<p> When working with filters, remember that Perl has it&#8217;s own idea of what truth and false is. The empty string &quot;&#8220; and the string &#8221;0&quot; are false, all other strings are true. This further imples that any integer value of 0 is false as well as any undef value. It also implies that all references are considered true. </p>
<p> As the filter is evaluated as a Perl expression, several useful constructs in Perl are worth mentioning: </p>
<p> Expressions might be grouped by using parentheses &#8220;()&#8221;. Expressions might be combined using boolean operators such as the following:</p>
<dl>
<dt>&quot;<code>and</code>&quot; (equivalent with &quot;<code>&amp;&amp;</code>&quot;)</p>
<dd> Boolean &#8220;and&#8221; of the two expressions, is only true if both expressions are true. Example: <i>expression1</i> <code>and</code> <i>expression2</i></p>
<dt>&quot;<code>or</code>&quot; (equivalent with &quot;<code>||</code>&quot;)</p>
<dd> Boolean &#8220;or&#8221; of the two expressions, is true if either or both expressions are true. Example: <i>expression1</i> <code>or</code> <i>expression2</i></p>
<dt>&quot;<code>not</code>&quot; (equivalent with &quot;<code>!</code>&quot;)</p>
<dd> Boolean negation of a single expression. Example: <code>not</code> <i>expression</i> . Yet another example: <code>!</code><i>expression</i></dl>
<p> (For more details on this I recommend a book on Perl) </p>
<p> <i>Predefined Filter Variables</i> </p>
<p> To facilitate, there are a number of predefined values available to use in the filter. Note that these variables are also available when templates interfaces are evaluated (but not host templates). </p>
<p> Caveat: All these variables&#8217; names begin with a dollar sign ($), which is a syntactic requirement for scalar variables in Perl. The danger here is that the dollar sign in many shells is an active character (often used for shell variables exactly as in Perl variables) so it is important to ensure that the Perl expression isn&#8217;t evaluated by the command line shell as shell code before being passed to cfgmaker as command line arguments. In shells like Bourne shell, ksh shell or bash shell, placing the entire expression within single qoutes will avoid such accidental evaluation: </p>
<pre>
 '--if-filter=($default_iftype &amp;&amp; $if_admin)'
</pre>
<dl>
<dt><code>$if_type</code></p>
<dd> This is an integer specifying the interface type as per the <font SIZE="-1">SNMP</font> standards and as reported by the polled device. A complete list of interface types would be impractical for this document , but there are a number predefined varables below. Normally, cfgmaker puts in the target&#8217;s PageTop this iftype value within paranthesis after the name of the interface type. (e.g &#8220;propPointToPointSerial (22)&#8221;). </p>
<p> Here&#8217;s a list of some of the most common interface types by number: </p>
<pre>
   6 ethernetCsmacd
   7 iso88023Csmacd
   9 iso88025TokenRing
  15 fddi
  19 E1
  20 basicISDN
  21 primaryISDN
  22 propPointToPointSerial
  23 ppp
  24 softwareLoopback
  30 ds3
  32 frame-relay
  33 rs232
  37 atm
  39 sonet
  44 frameRelayService
  46 hssi
  49 aal5
  53 propVirtual
  62 Fast Ethernet (100BaseT)
  63 ISDN &amp; X.25
  69 Full Duplex Fast Ethernet (100BaseFX)
  94 Asymetric Digital Subscriber Loop (ADSL)
 117 Gigabit Ethernet
 134 ATM Sub Interface
</pre>
<dt><code>$default</code></p>
<dd> True if and only if cfgmaker normally should accepted the interface based on the interfaces administrative and operational state (taking the flags <code>&#8211;no-down</code> and <code>&#8211;show-op-down</code> into account) and it&#8217;s type (and a few other things).</p>
<dt><code>$default_ifstate</code></p>
<dd> True if and only if cfgmaker would have accepted the interface based on it&#8217;s operational and administrative states (also taking into account the presence of the flags <code>&#8211;no-down</code> and <code>&#8211;show-op-down</code>).</p>
<dt><code>$default_iftype</code></p>
<dd> True if and only if cfgmaker would have accepted the interface based on it&#8217;s type (and a few type specific details in addition).</p>
<dt><code>$if_admin</code></p>
<dd> True if and only if the interface is in an adminstrative up state.</p>
<dt><code>$if_oper</code></p>
<dd> True if and only if the interface is in an operational up state.</dl>
<p> A number of variables are also predefined to easily decide if an interface belong to a certain cathegory or not. Below is all those variables listed together with which if_type numbers each variable will be true for. Note that some variables refer to other variables as well.</p>
<dl>
<dt><code>$if_is_ethernet</code></p>
<dd> True for ethernet interfaces (nr 6, 7, 26, 62, 69 and 117).</p>
<dt><code>$if_is_isdn</code></p>
<dd> True for various <font SIZE="-1">ISDN</font> interface types (nr 20, 21, 63, 75, 76 and 77)</p>
<dt><code>$if_is_dialup</code></p>
<dd> True for dial-up interfaces such as <font SIZE="-1">PPP</font> as well as <font SIZE="-1">ISDN</font>. (nr 23, 81, 82 and 108 in addition to the numbers of $if_is_isdn).</p>
<dt><code>$if_is_atm</code></p>
<dd> True for miscellaneous <font SIZE="-1">ATM</font> related interface types (nr 37, 49, 107, 105, 106, 114 and 134).</p>
<dt><code>$if_is_wan</code></p>
<dd> True for <font SIZE="-1">WAN</font> interfaces point to point, Frame Relay and High Speed Serial ( 22,32,44,46)</p>
<dt><code>$if_is_lan</code></p>
<dd> True for <font SIZE="-1">LAN</font> interfaces (8, 9, 11, 15, 26, 55, 59, 60 and 115 in addition to the numbers of $if_is_ethernet).</p>
<dt><code>$if_is_dsl</code></p>
<dd> True for <font SIZE="-1">ADSL</font>, <font SIZE="-1">RDSL</font>, <font SIZE="-1">HDSL</font> and <font SIZE="-1">SDSL</font> (nr 94, 95, 96, 97)</p>
<dt><code>$if_is_loopback</code></p>
<dd> True for software loopback interfaces (nr 24)</p>
<dt><code>$if_is_ciscovlan</code></p>
<dd> True for Cisco <font SIZE="-1">VLAN</font> interfaces (interfaces with the word Vlan or <font SIZE="-1">VLAN</font> in their ifdescs)</p>
<dt><code>$if_vlan_id</code></p>
<dd> Returns the vlan id associated with a specific port on Cisco Catalyst switches under both Catalyst <font SIZE="-1">OS</font> and <font SIZE="-1">IOS</font>, and 3Com switches. If it is not a vlan interface, will return undef.</p>
<dt><code>$if_cisco_trunk</code></p>
<dd> Returns the trunking state of a specific port on Cisco Catalyst switches under both Catalyst <font SIZE="-1">OS</font> and <font SIZE="-1">IOS</font>. Returns &#8220;1&#8221; if the interface is a trunk, undef otherwise.</p>
<dt><code>$if_MTU</code></p>
<dd> Returns the Maximum Transfer Unit associated with a specific port.</dl>
<p> Besides that, you can also use the variables defined for templates below. Further, all the variables available in cfgmaker is at the scripts disposal even if the use of such features is discouraged. More &#8220;shortcuts&#8221; in the form of variables and functions will be made available in the future instead. </p>
<p> <i>Examples on Filters</i> </p>
<p> The following filter will not affect which interfaces get&#8217;s included or excluded, it will make cfgmaker behave as normally. </p>
<pre>
 '--if-filter=$default'
</pre>
<p> The following filter will make cfgmaker exclude <font SIZE="-1">PPP</font> (23) interfaces: </p>
<p>&#8216;&#8211;if-filter=$default &amp;&amp; $if_type!=23&#8217;</p>
<p> The following filter will make cfgmaker behave as usual except that it will consider the operational state of an interface irrelevant but still reject all interfaces which are administratively down. </p>
<pre>
 '--if-filter=$if_admin &amp;&amp; $default_iftype'
</pre>
<h3>Details on Templates</h3>
<p> The contents of the template files are evaluated as a Perl program. A number or Perl variables are available for the program to read and others are used to be written to. </p>
<p> As quite a few of the predefined variables has values which are are supposed to be used in <font SIZE="-1">HTML</font> code some of them have an &#8220;HTML-escaped&#8221; variant, e.g <tt>$html_syslocation</tt> is the <font SIZE="-1">HTML</font> escaped variant of <tt>$syslocation</tt>. The <font SIZE="-1">HTML</font> escaping means that the chars &#8220;&lt;&#8221;, &#8220;&gt;&#8221; and &#8220;&amp;&#8221; are replaced by &#8220;&amp;lt;&#8221;, &#8220;&amp;gt;&#8221; and &#8220;&amp;amp;&#8221; and that newlines embedded in the string are prepended with &#8220;&lt;<font SIZE="-1">BR</font>&gt;&#8221; and appended with a space character (if a newline is last in the string it is not touched). </p>
<p> <i>Writable Template Variables</i> </p>
<p> These are the variables available to store the configuration lines in. Some of them are initialized prior to the evaluation of the template but such content normally is comments for inclusion in the final configuration file so those variables might be reset to the empty string in the template code to eliminate the comments. The other way around is also possible, the contents of these variables might be extended with further information for various reasons such as debugging etc. </p>
<p> Once the template has been evaluated, the following happens: if the template is a interface template and the actual interface for some reason is rejected and thus needs to be commented out, all the lines in the variable $target_lines are turned into comments by adding a hash mark (&#8220;#&#8221;) at their beginning. Then all the variables $head_lines, $problem_lines , $target_lines and $separator_lines are concatenated together to form the lines to add to the configuration file.</p>
<dl>
<dt><code>$target_lines</code></p>
<dd> This variable is the placeholder for the configuration lines created by the template. $target_lines is predefined to be empty when the template code is evaluated.</p>
<dt><code>$head_lines</code></p>
<dd> This variable is intended to be the placeholder for the comment line appearing just before the target in the configuration file. It is initialized with that comment line before the evaluation of the template code and if the template doesn&#8217;t modify $head_lines during evaluation, the comment will look like usual in the config file.</p>
<dt><code>$problem_lines</code></p>
<dd> This variable is intended to be the placholder for the comment lines describing any problems which might have been encountered when trying to add the target into the configuration. For host templates it&#8217;s normally not used and for those it&#8217;s predefined as the empty string. For interface templates $problem_lines is predefined with the error description comments which cfgmaker normally would use for rejected interfaces or as the empty string for accepted interfaces. </p>
<p> It is possible to test against $problem_lines to find out if an interface will be included or rejected but this is not recommended. Test against $if_ok instead.</p>
<dt><code>$separator_lines</code></p>
<dd> This variable is the placeholder for the string to use as the separator between the code for individual targets. The contents of this variable is put after each target (so the lines will appear after the end of the last target in the config as well).</dl>
<p> <i>Predefined Template Variables</i> </p>
<p> All the variables below are available for interface templates to use. For host templates, only those listed under &#8220;Host and System Variables&#8221; are available. </p>
<p> For interface templates the variables listed under &#8220;Predefined Filter Variables&#8221; are also available. </p>
<p> <i>Host and System Variables</i></p>
<dl>
<dt><code>$router_name</code></p>
<dd> This is the fully qualified name for the router. It is affected by the following items on the command line: the router name itself and <code>&#8211;dns-domain</code>.</p>
<dt><code>$router_connect</code></p>
<dd> This is the reference string for the router being polled. It is on the form community [at] router possibly followed by some snmp options. It is affected by the following items on the command line: the router name itself, <code>&#8211;community</code>, <code>&#8211;snmp-options</code> and <code>&#8211;dns-domain</code>. (There&#8217;s no <font SIZE="-1">HTML</font> escaped variant available)</p>
<dt><code>$directory_name</code></p>
<dd> This variable should contain the directory name as cfgmaker normally would use as the value for the &#8220;Directory[]&#8221; directive. The value is determined by the <code>&#8211;subdirs</code> command line option. If <code>&#8211;subdirs</code> isn&#8217;t specified $directory_name will be the empty string. (There&#8217;s no <font SIZE="-1">HTML</font> escaped variant available)</p>
<dt><code>$syscontact</code></p>
<dd> This variable is the router&#8217;s <font SIZE="-1">SNMP</font> sysContact value. (<font SIZE="-1">HTML</font> escaped variant: $html_syscontact)</p>
<dt><code>$sysname</code></p>
<dd> This variable is the router&#8217;s <font SIZE="-1">SNMP</font> sysName value. (No <font SIZE="-1">HTML</font> escaped variant available)</p>
<dt><code>$syslocation</code></p>
<dd> This variable is the router&#8217;s <font SIZE="-1">SNMP</font> sysLocation value. (<font SIZE="-1">HTML</font> escaped variant: $html_syslocation)</p>
<dt><code>$sysdescr</code></p>
<dd> This variable is the router&#8217;s <font SIZE="-1">SNMP</font> sysDescr value. It is normally not used by cfgmaker but might be useful in a template. (<font SIZE="-1">HTML</font> escaped variant: $html_sysdescr)</dl>
<p> <i>Interface Target Related Variables</i></p>
<dl>
<dt><code>$target_name</code></p>
<dd> This is what cfgmaker normally would use as the the name of the target. The target name is what is found within the square brackets, &#8220;[]&#8221;, for target directives. (There&#8217;s no <font SIZE="-1">HTML</font> escaped variant available)</p>
<dt><code>$if_ref</code></p>
<dd> This the reference string for the interface. It is expected to be used in the &#8220;Target[xyz]&#8221; directive to distinguish what interface to use. The value of this variable is affected by the <code>&#8211;ifref</code> command line option. It is normally used together with $router_connect. (There&#8217;s no <font SIZE="-1">HTML</font> escaped variant available)</p>
<dt><code>$if_ok</code></p>
<dd> This variable is true if the interface is going to be included into the configuration file, otherwise false. Don&#8217;t test against other variables such as $problem_lines to find out if an interface will be rejected or not, use this $if_ok instead.</p>
<dt><code>$default_target_lines</code></p>
<dd> This variable contains all the target lines which cfgmaker by default outputs for this interface. It&#8217;s useful if you want to have the &#8220;standard target&#8221; but want to add some extra lines to it by using a template.</dl>
<p> By default cfgmaker uses the following directives for each target it generates: Target[], SetEnv[], MaxBytes[], Title[], PageTop[] and if there is any directory specified also the Directory[] directive. </p>
<p> To facilitate the creation of templates which generates target configs which are similar to the default one, each of the above mentioned directive lines have a corresponding variable containing the line as cfgmaker would have output it by default. </p>
<p> Note that none of these have a <font SIZE="-1">HTML</font> escaped variant, text in them is <font SIZE="-1">HTML</font> escaped where needed. Also note that they do not have any newline at the end.</p>
<dl>
<dt><code>$default_target_directive</code></p>
<dd> This variable contains the default string for the Target[] directive line.</p>
<dt><code>$default_setenv_directive</code></p>
<dd> This variable contains the default string for the SetEnv[] directive line.</p>
<dt><code>$default_directory_directive</code></p>
<dd> This variable contains the default string for the Directory[] directive line which means it is an empty string (with no newline) if there&#8217;s no directory.</p>
<dt><code>$default_maxbytes_directive</code></p>
<dd> This variable contains the default string for the MaxBytes[] directive line.</p>
<dt><code>$default_title_directive</code></p>
<dd> This variable contains the default string for the Title[] directive line.</p>
<dt><code>$default_pagetop_directive</code></p>
<dd> This variable contains the default string for the PageTop[] directive lines.</dl>
<p> <i>Interface Network Configuration Variables</i></p>
<dl>
<dt><code>$if_ip</code></p>
<dd> This variable should contain the IP-address of the interface, if any has been assigned to it. (There&#8217;s no <font SIZE="-1">HTML</font> escaped variant available)</p>
<dt><code>$ifindex</code></p>
<dd> This variable is the <font SIZE="-1">SNMP</font> ifIndex for the interface which per definition always is an integer. (There&#8217;s no <font SIZE="-1">HTML</font> escaped variant available)</p>
<dt><code>$if_index</code></p>
<dd> Equivalent with $ifindex.</p>
<dt><code>$if_eth</code></p>
<dd> Contains the ethernet address of the interface, if any. (There&#8217;s no <font SIZE="-1">HTML</font> escaped variant available)</p>
<dt><code>$if_speed</code></p>
<dd> This variable is the speed in bytes/second (with prefixes). (There&#8217;s no <font SIZE="-1">HTML</font> escaped variant available)</p>
<dt><code>$if_speed_str</code></p>
<dd> This variable is a cooked speed description which is either in bits or bytes depending on wether or not the bits option is active and also with the proper prefix for the speed (k, M, G etc). (No <font SIZE="-1">HTML</font> escaped variant available)</p>
<dt><code>$if_type_desc</code></p>
<dd> This variable is a textual description of the interface type. (<font SIZE="-1">HTML</font> escaped variant: $html_if_type_desc)</p>
<dt><code>$if_type_num</code></p>
<dd> This variable the integer value corresponding to the interface type (for a listing for the value for the more common interface types, see the section <font SIZE="-1">DETAILS</font> <font SIZE="-1">ON</font> <font SIZE="-1">FILTERS</font> above). (No <font SIZE="-1">HTML</font> escaped variant available)</p>
<dt><code>$if_dns_name</code></p>
<dd> This is the <font SIZE="-1">DNS</font> name for the interface. (No <font SIZE="-1">HTML</font> escaped variant available)</dl>
<p> <i>Interface Name, Description and Alias Variables</i> </p>
<p> It might seem confusing with both <i>Name</i>, <i>Description</i> and <i>Alias</i> in this context and to some extent it is. <i>Name</i> and <i>Description</i> are usually supported on most equipment but how they are used varies, both between manufacturers as well as between different cathegories of equipment from the same manufacturer. The <i>Alias</i> is at least supported by Cisco <font SIZE="-1">IOS</font>, and that variable contains whatever is used in the <font SIZE="-1">IOS</font> statement called &#8220;description&#8221; for the interface (not to be confused with the <font SIZE="-1">SNMP</font> variables for <i>Description</i>). </p>
<p> For better control from the command line consider $if_title_desc which contents are controlled by the <code>&#8211;if-descr</code> command line option.</p>
<dl>
<dt><code>$if_snmp_descr</code></p>
<dd> This variable should contain the &#8220;raw&#8221; description of the interface as determined by the <font SIZE="-1">SNMP</font> polling of the router. (<font SIZE="-1">HTML</font> escaped variant: $html_if_snmp_descr)</p>
<dt><code>$if_snmp_name</code></p>
<dd> The &#8220;raw&#8221; name for the interface as provided by <font SIZE="-1">SNMP</font> polling. (<font SIZE="-1">HTML</font> escaped variant: $html_if_snmp_name)</p>
<dt><code>$if_snmp_alias</code></p>
<dd> The &#8220;raw&#8221; ifAlias for the interface as provided by <font SIZE="-1">SNMP</font> polling. (<font SIZE="-1">HTML</font> escaped variant: $html_if_snmp_alias)</p>
<dt><code>$if_cisco_descr</code></p>
<dd> The &#8220;raw&#8221; CiscolocIfDescr for the interface as provided by <font SIZE="-1">SNMP</font> polling. (<font SIZE="-1">HTML</font> escaped variant: $html_if_cisco_descr)</p>
<dt><code>$if_description</code></p>
<dd> This is the &#8220;cooked&#8221; description string for the interface, taking into account the <font SIZE="-1">SNMP</font> values found for the interface&#8217;s RDescr, ifAlias and CiscolocIfDescr. (<font SIZE="-1">HTML</font> escaped variant: $html_if_description)</p>
<dt><code>$if_title</code></p>
<dd> The full string cfgmaker by default would have used for the Title[] directive in the configuration as well as the content of the topmost H1 tag in the PageTop[]. Is composed by the contents of $desc_prefix, $if_title_desc and $sysname. </p>
<p> As $if_title depends on $if_title_desc, it is possible to indirectly control $if_title by using the command line option <code>&#8211;if-descr</code>. </p>
<p> (<font SIZE="-1">HTML</font> escaped variant: $html_if_title)</p>
<dt><code>$if_port_name</code></p>
<dd> If the host is a Cisco Catalyst <font SIZE="-1">LAN</font> switch, this variable is the name of that port. (No <font SIZE="-1">HTML</font> escaped variant available)</p>
<dt><code>$if_pp_port_name</code></p>
<dd> If the host is a Nortel Passport <font SIZE="-1">LAN</font> switch, this variable is the name of that port. (No <font SIZE="-1">HTML</font> escaped variant available)</p>
<dt><code>$desc_prefix</code></p>
<dd> This variable is a prefix of the description of what the target is to use in the &#8220;Title[]&#8221; directive and in the H1 section of the &#8220;PageTop[]&#8221;. Default is &#8220;Traffic analysis for &#8221;. (<font SIZE="-1">HTML</font> escaped variant: $html_desc_prefix)</p>
<dt><code>$if_title_desc</code></p>
<dd> This is the description of the interface normally used by cfgmaker as part of the variable $if_title. The latter is used as the full string in the &#8220;Title[]&#8221; directove and the H1 section in the PageTop[]. </p>
<p> $if_title_desc is controlled by the command line option <code>&#8211;if-descr</code> which indirectly controls the contents of $if_title </p>
<p> (<font SIZE="-1">HTML</font> escaped variant: $html_if_title_desc)</dl>
<p> <i>Help Functions for Templates</i> </p>
<p> The following functions exists to facilitate the writing of host and interface templates.</p>
<dl>
<dt><code>html_escape(</code>string<code>)</code></p>
<dd> html_escape() takes a string as an argument and returns a new string where the following substitutions has been done: the chars &#8220;&lt;&#8221;, &#8220;&gt;&#8221; and &#8220;&amp;&#8221; are replaced by &#8220;&amp;lt;&#8221;, &#8220;&amp;gt;&#8221; and &#8220;&amp;amp;&#8221; and that newlines embedded in the string are prepended with &#8220;&lt;<font SIZE="-1">BR</font>&gt;&#8221; and appended with a space character (newlines at the end of the string are not touched).</p>
<dt><code>oid_pick($router_connect,$v3opt,&quot;oid1&quot;,&quot;oid2&quot;&#8230;)</code></p>
<dd> This function will try to poll each of the oids specified until it is successful or has run out of oids. It will return the name of the first oid that worked or undef if it is not successful</dl>
<p> <i>Example Template Files</i> </p>
<p> Template Example 1: Eliminating Rejected Targets From Appearing </p>
<p> This template file generates exactly the same configuration code per interface as cfgmaker does by default, with the exception that it eliminates all lines (comments as well as config code) for an interface if the interface happens to be rejected. </p>
<p>if (not $problem_lines) {<br />
    $target_lines.= &lt;&lt; ECHO;<br />
    Target[$target_name] : $if_ref : $router_connect<br />
                                         SetEnv[$target_name] : MRTG_INT_IP = &#8220;$if_ip&#8221; MRTG_INT_DESCR = &#8220;$if_snmp_descr&#8221; ECHO if ($directory_name)<br />
    {<br />
        $target_lines.= &#8220;Directory[$target_name]: $directory_name
&#8221;;<br />
    }<br />
    $target_lines.= &lt;&lt; ECHO;<br />
    MaxBytes[$target_name] : $if_speed<br />
                                 Title[$target_name] : $html_desc_prefix$html_if_title_desc&#8211; $sysname<br />
                                                           PageTop[$target_name] : &lt;h1&gt;<br />
                                                                                       $html_desc_prefix$html_if_title_desc&#8211; $sysname&lt;/ h1&gt;<br />
                                                                                   &lt;div id = &#8220;sysdetails&#8221;&gt;<br />
                                                                                   &lt;table&gt;<br />
                                                                                   &lt;tr&gt;<br />
                                                                                   &lt;td&gt;<br />
                                                                                       System : &lt;/ td&gt;<br />
                                                                                                &lt;td&gt;<br />
                                                                                                    $sysname in $html_syslocation&lt;/ td&gt;<br />
                                                                                                &lt;/ tr&gt;<br />
                                                                                                &lt;tr&gt;<br />
                                                                                                &lt;td&gt;<br />
                                                                                                    Maintainer : &lt;/ td&gt;<br />
                                                                                                                 &lt;td&gt;<br />
                                                                                                                     $html_syscontact&lt;/ td&gt;<br />
                                                                                                                 &lt;/ tr&gt;<br />
                                                                                                                 &lt;tr&gt;<br />
                                                                                                                 &lt;td&gt;<br />
                                                                                                                     Description : &lt;/ td&gt;<br />
                                                                                                                                   &lt;td&gt;<br />
                                                                                                                                       $html_if_description&lt;/ td&gt;<br />
                                                                                                                                   &lt;/ tr&gt;<br />
                                                                                                                                   &lt;tr&gt;<br />
                                                                                                                                   &lt;td&gt;<br />
                                                                                                                                       ifType : &lt;/ td&gt;<br />
                                                                                                                                                &lt;td&gt;<br />
                                                                                                                                                    $html_if_type_desc($if_type_num)&lt;/ td&gt;<br />
                                                                                                                                                &lt;/ tr&gt;<br />
                                                                                                                                                &lt;tr&gt;<br />
                                                                                                                                                &lt;td&gt;<br />
                                                                                                                                                    ifName : &lt;/ td&gt;<br />
                                                                                                                                                             &lt;td&gt;<br />
                                                                                                                                                                 $html_if_snmp_name&lt;/ td&gt;<br />
                                                                                                                                                             &lt;/ tr&gt;<br />
                                                                                                                                                                 ECHO<br />
                                                                                                                                                                     $target_lines.=<br />
        &lt;&lt; ECHO if defined $if_port_name;<br />
    &lt;tr&gt;<br />
        &lt;td&gt; Port Name : &lt;/ td&gt;<br />
                         &lt;td&gt;<br />
                             $if_port_name&lt;/ td&gt;<br />
                         &lt;/ tr&gt;<br />
                             ECHO<br />
                                 $target_lines.=<br />
        &lt;&lt; ECHO if defined $if_pp_port_name;<br />
    &lt;tr&gt;<br />
        &lt;td&gt; Port Name : &lt;/ td&gt;<br />
                         &lt;td&gt;<br />
                             $if_pp_port_name&lt;/ td&gt;<br />
                         &lt;/ tr&gt;<br />
                             ECHO<br />
                                 $target_lines.=<br />
        &lt;&lt; ECHO;<br />
    &lt;tr&gt;<br />
        &lt;td&gt; Max Speed : &lt;/ td&gt;<br />
                         &lt;td&gt;<br />
                             $if_speed_str&lt;/ td&gt;<br />
                         &lt;/ tr&gt;<br />
                             ECHO<br />
                                 $target_lines.=<br />
        &lt;&lt; ECHO if $if_ip;<br />
    &lt;tr&gt;<br />
        &lt;td&gt; Ip : &lt;/ td&gt;<br />
                  &lt;td&gt;<br />
                      $if_ip($if_dns_name)&lt;/ td&gt;<br />
                  &lt;/ tr&gt;<br />
                      ECHO<br />
                          $target_lines.=<br />
        &lt;&lt; ECHO;<br />
    &lt;/ table&gt;<br />
        &lt;/ div&gt;<br />
            ECHO<br />
} else {<br />
    $head_lines = &#8220;&#8221;;<br />
    $problem_lines = &#8220;&#8221;;<br />
    $target_lines = &#8220;&#8221;;<br />
    $separator_lines = &#8220;&#8221;;<br />
}</p>
<p> <i>Template Example 2: Simplier Version of Example 1</i> </p>
<p> Example 1 was partly intended to demonstrate how to customize the generation of interface targets but also to provide a hint of how the variables are used in the &#8220;default&#8221; template which one could consider that cfgmaker normally uses. </p>
<p> If you&#8217;re only intrested in the easiest way of entirely eliminating those reject interfaces, the template below would do the job as well by using $default_target_lines. </p>
<p>if ($if_ok) {<br />
    $target_lines = $default_target_lines;<br />
} else {<br />
    $head_lines = &#8220;&#8221;;<br />
    $problem_lines = &#8220;&#8221;;<br />
    $target_lines = &#8220;&#8221;;<br />
    $separator_lines = &#8220;&#8221;;<br />
}</p>
<p> <i>Template Example 3: Creating </i><font SIZE="-1"><i>CPU</i></font><i> Targets for Hosts</i> </p>
<p> Below is an example of a host template. </p>
<p>$head_lines.= &lt;&lt; ECHO;<br />
#&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;<br />
ECHO<br />
    my $target_name = $router_name.&#8221;.cpu&#8221;;<br />
$target_lines.= &lt;&lt; ECHO;<br />
YLegend[$target_name] : Percentage CPU load<br />
                            ShortLegend[$target_name] : %<br />
                                                        Legend1[$target_name] : CPU load in %<br />
                                                                                Legend2[$target_name] : Legend3[$target_name] : Max Observed CPU load<br />
                                                                                                                                    Legend4[$target_name] : LegendI[$target_name] : &amp;nbsp;<br />
CPU Load : LegendO[$target_name] : WithPeak[$target_name] : ywm<br />
                                                                MaxBytes[$target_name] : 100 Options[$target_name] : growright,<br />
                                                                                                                     gauge,<br />
                                                                                                                     nopercent<br />
                                                                                                                             Title[$target_name] : $router_name CPU load<br />
                                                                                                                                                       Target[$target_name] : 1.3.6.1.4.1.9.2.1.58.0 &amp;<br />
                                                                                                                                                   1.3.6.1.4.1.9.2.1.58.0 : $router_connect<br />
                                                                                                                                                                                PageTop[$target_name] : &lt;h1&gt;<br />
                                                                                                                                                                                                            $router_name CPU load&lt;/ h1&gt;<br />
                                                                                                                                                                                                        &lt;div&gt;<br />
                                                                                                                                                                                                        &lt;table&gt;<br />
                                                                                                                                                                                                        &lt;tr&gt;<br />
                                                                                                                                                                                                        &lt;td&gt;<br />
                                                                                                                                                                                                            System : &lt;/ td&gt;<br />
                                                                                                                                                                                                                     &lt;td&gt;<br />
                                                                                                                                                                                                                         $router_name in $html_syslocation&lt;/ td&gt;<br />
                                                                                                                                                                                                                     &lt;/ tr&gt;<br />
                                                                                                                                                                                                                     &lt;tr&gt;<br />
                                                                                                                                                                                                                     &lt;td&gt;<br />
                                                                                                                                                                                                                         Maintainer : &lt;/ td&gt;<br />
                                                                                                                                                                                                                                      &lt;td&gt;<br />
                                                                                                                                                                                                                                          $html_syscontact&lt;/ td&gt;<br />
                                                                                                                                                                                                                                      &lt;/ tr&gt;<br />
                                                                                                                                                                                                                                      &lt;tr&gt;<br />
                                                                                                                                                                                                                                      &lt;td&gt;<br />
                                                                                                                                                                                                                                          Description : &lt;/ td&gt;<br />
                                                                                                                                                                                                                                                        &lt;td&gt;<br />
                                                                                                                                                                                                                                                            $html_sysdescr&lt;/ td&gt;<br />
                                                                                                                                                                                                                                                        &lt;/ tr&gt;<br />
                                                                                                                                                                                                                                                        &lt;tr&gt;<br />
                                                                                                                                                                                                                                                        &lt;td&gt;<br />
                                                                                                                                                                                                                                                            Resource : &lt;/ td&gt;<br />
                                                                                                                                                                                                                                                                       &lt;td&gt;<br />
                                                                                                                                                                                                                                                                           CPU.&lt;/ td&gt;<br />
                                                                                                                                                                                                                                                                       &lt;/ tr&gt;<br />
                                                                                                                                                                                                                                                                       &lt;/ table&gt;<br />
                                                                                                                                                                                                                                                                       &lt;/ div&gt;<br />
                                                                                                                                                                                                                                                                           ECHO</p>
<h2>EXAMPLES</h2>
<p> The first example creates a config file for <i>router.place.xyz</i>: the router has the community name <i>public</i>. Interfaces get identified by their <font SIZE="-1">IP</font> number. Two global options get added to the config file. The config file gets redirected to <i>mrtg.conf</i>. The &#8216;\&#8217; signs at the end of the line mean that this command should be written on a single line. </p>
<p>cfgmaker&#8211; global &#8220;WorkDir: /home/tobi&#8221; &#8211;global &#8220;Options[_]: growright,bits&#8221; &#8211;ifref = ip public[at] router.place.xyz &gt; mrtg.cfg</p>
<p> Note: if cfgmaker is not in your path, but you are in the directory where cfgmaker is stored, you can start it with ./cfgmaker </p>
<p> The next example creates a config file for four devices: <i>router1.place.xyz</i>, <i>router2.place.xyz</i>, <i>switch1.place.xyz</i> and <i>switch2.place.xyz</i> all with the community <i>public</i>. </p>
<p> The two routers will have <code>&#8211;ifref</code> set to <code>descr</code> whilst the two switches will use <code>&#8211;ifref</code> set to <code>name</code>. Further the routers will use <code>&#8211;ifdesc</code> set to <code>alias</code> and <i>switch1.place.xyz</i> will use <code>&#8211;ifdesc</code> set to <code>descr</code> whilst <i>switch2.place.xyz</i> use <code>name</code> instead. </p>
<p> Finally, there will be two Options lines inserted in the configuration: One will be in the beginning, whilst the other will be inserted after the lines related to the two routers but before those lines related to the switches. </p>
<p>cfgmaker&#8211; global &#8220;WorkDir: /home/tobi&#8221; &#8211;global &#8220;Options[_]: growright,bits&#8221; &#8211;ifref = descr&#8211; ifdesc = alias public[at] router1.place.xyz public[at] router2.place.xyz&#8211; global &#8220;Options[_]: growright&#8221; &#8211;ifref = name&#8211; ifdesc = descr public[at] switch1.place.xyz&#8211; ifdesc = name public[at] switch2.place.xyz &gt; mrtg.cfg</p>
<p> The next example demonstrates how to use the <code>&#8211;community</code>, <code>&#8211;snmp-options</code> and <code>&#8211;dns-domain</code> to make the command line simpler. All the equipment will use the community <i>hidden</i>, except for the ppp-server which use community <i>access</i>. All equipment uses these <font SIZE="-1">SNMP</font> options: <code>1s timeout</code>, <code>1 retry</code> and <font SIZE="-1"><code>SNMP</code></font><code> version 2</code> (<code>backoff</code> and <code>port</code> is unspecified which means they use the default values). The exception again is the ppp-server which uses <font SIZE="-1"><code>SNMP</code></font><code> version 1</code>. Finally, all the equipment is part of the domain <i>place.xyz</i>, except for the ppp-server which is part of the domain <i>remote.place.xyz</i>. Note that the latter is achieved simply by specifying the name of the ppp-server to be <i>ppp-server.</i>remote<i></i> . </p>
<pre><code>
cfgmaker-- global "WorkDir: /home/tobi" --global "Options[_]: growright,bits" --dns - domain = place.xyz-- community = hidden-- snmp - options = ::1 : 1 ::2 router1
                                                                                                                                                         router2
                                                                                                                                                             router3
                                                                                                                                                                 router4
                                                                                                                                                                     router5
                                                                                                                                                                         switch1
                                                                                                                                                                             switch2
                                                                                                                                                                                 switch3
                                                                                                                                                                                     switch4
                                                                                                                                                                                         switch5
                                                                                                                                                                                             switch6
                                                                                                                                                                                                 switch7
                                                                                                                                                                                                     access[at] ppp -
                                                                                                                                                     server.remote:: :: : 1 &gt;
                                                                                                                                                 mrtg.cfg
</code></pre>
<h2>SEE ALSO</h2>
<p> mrtg-reference</p>
<h2>AUTHOR</h2>
<p> Tobias Oetiker &lt;tobi [at] oetiker.ch&gt; and Jakob Ilves &lt;jakob.ilves [at] oracle.com&gt;</p>
<h2>LICENSE</h2>
<p> <font SIZE="-1">GNU</font> General Public License</p>
<h2>COPYRIGHT</h2>
<p> Cfgmaker is Copyright 2000 by Tobias Oetiker &lt;tobi [at] oetiker.ch&gt; </p>
<h2>Index</h2>
<dt><a href="#lbAJ">EXAMPLES</a></p>
<dd>
<dt><a href="#lbAK">SEE ALSO</a></p>
<dd>
<dt><a href="#lbAL">AUTHOR</a></p>
<dd>
<dt><a href="#lbAM">LICENSE</a></p>
<dd>
<dt><a href="#lbAN">COPYRIGHT</a></p>
<dd></dl>
