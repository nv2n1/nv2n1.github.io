---
title: "ipmi-power(8)"
name: "ipmi-power"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ipmi-power/"
description: "ipmipower – IPMI power control utility"
---

<p>ipmipower &#8211; IPMI power control utility</p>
<h2>Synopsis</h2>
<p><code>ipmipower</code> [<i>OPTION</i>&#8230;]</p>
<h2>Description</h2>
<p><code>ipmipower</code> allows users to remotely power on, off, cycle, hard reset, get a power status query, perform a pulse diagnostic interrupt, or initiate a soft-shutdown of the OS via ACPI through the IPMI over LAN protocol. </p>
<p> When a power command (<code>&#8211;on</code>, <code>&#8211;off</code>, <code>&#8211;cycle</code>, <code>&#8211;reset</code>, <code>&#8211;stat</code>, <code>&#8211;pulse</code>, or <code>&#8211;soft</code>) is specified on the command line, <code>ipmipower</code> will attempt to run the power command on all hostnames listed on the command line then exit. </p>
<p> If no power commands are specified on the command line, <code>ipmipower</code> will run in interactive mode. Interactive mode gives the user a command line interface to enter various commands. Details of the interactive command line interface can be found below under INTERACTIVE COMMANDS. </p>
<p> Listed below are general IPMI options, tool specific options, trouble shooting information, workaround information, examples, and known issues. For a general introduction to FreeIPMI please see <code><a href="/docs/linux/man/7-freeipmi/">freeipmi</a>(7).</code></p>
<h2>General Options</h2>
<p>The following options are general options for configuring IPMI communication and executing general tool commands.</p>
<dl>
<dt><code>-D</code> <i>IPMIDRIVER</i>, <code>&#8211;driver-type</code>=<i>IPMIDRIVER</i></p>
<dd>Specify the driver type to use instead of doing an auto selection. The currently available outofband drivers are LAN and LAN_2_0, which perform IPMI 1.5 and IPMI 2.0 respectively.</p>
<dt><code>-h</code> <i>IPMIHOST1,IPMIHOST2,&#8230;</i>, <code>&#8211;hostname</code>=<i>IPMIHOST1[:PORT],IPMIHOST2[:PORT],&#8230;</i></p>
<dd>Specify the remote host(s) to communicate with. Multiple hostnames may be separated by comma or may be specified in a range format; see HOSTRANGED SUPPORT below. An optional port can be specified with each host, which may be useful in port forwarding or similar situations.</p>
<dt><code>-u</code> <i>USERNAME</i>, <code>&#8211;username</code>=<i>USERNAME</i></p>
<dd>Specify the username to use when authenticating with the remote host. If not specified, a null (i.e. anonymous) username is assumed. The user must have atleast OPERATOR privileges to run the &#8211;on, &#8211;off, &#8211;reset, &#8211;cycle, &#8211;pulse, or &#8211;soft power control commands. The user must have atleast USER privileges to determine the power status of the machine through &#8211;stat.</p>
<dt><code>-p</code> <i>PASSWORD</i>, <code>&#8211;password</code>=<i>PASSWORD</i></p>
<dd>Specify the password to use when authenticationg with the remote host. If not specified, a null password is assumed. Maximum password length is 16 for IPMI 1.5 and 20 for IPMI 2.0.</p>
<dt><code>-P</code>, <code>&#8211;password-prompt</code></p>
<dd>Prompt for password to avoid possibility of listing it in process lists.</p>
<dt><code>-k</code> <i>K_G</i>, <code>&#8211;k-g</code>=<i>K_G</i></p>
<dd>Specify the K_g BMC key to use when authenticating with the remote host for IPMI 2.0. If not specified, a null key is assumed. To input the key in hexadecimal form, prefix the string with &#8216;0x&#8217;. E.g., the key &#8216;abc&#8217; can be entered with the either the string &#8216;abc&#8217; or the string &#8216;0x616263&#8217;</p>
<dt><code>-K</code>, <code>&#8211;k-g-prompt</code></p>
<dd>Prompt for k-g to avoid possibility of listing it in process lists.</p>
<dt><code>&#8211;session-timeout</code>=<i>MILLISECONDS</i></p>
<dd>Specify the session timeout in milliseconds. Defaults to 20000 milliseconds (20 seconds) if not specified.</p>
<dt><code>&#8211;retransmission-timeout</code>=<i>MILLISECONDS</i></p>
<dd>Specify the packet retransmission timeout in milliseconds. Defaults to 400 milliseconds (0.4 seconds) if not specified.</p>
<dt><code>-a</code> <i>AUTHENTICATION-TYPE</i>, <code>&#8211;authentication-type</code>=<i>AUTHENTICATION-TYPE</i></p>
<dd>Specify the IPMI 1.5 authentication type to use. The currently available authentication types are NONE, STRAIGHT_PASSWORD_KEY, MD2, and MD5. Defaults to MD5 if not specified.</p>
<dt><code>-I</code> <i>CIPHER-SUITE-ID</i>, <code>&#8211;cipher-suite-id</code>=<i>CIPHER-SUITE-ID</i></p>
<dd>Specify the IPMI 2.0 cipher suite ID to use. The Cipher Suite ID identifies a set of authentication, integrity, and confidentiality algorithms to use for IPMI 2.0 communication. The authentication algorithm identifies the algorithm to use for session setup, the integrity algorithm identifies the algorithm to use for session packet signatures, and the confidentiality algorithm identifies the algorithm to use for payload encryption. Defaults to cipher suite ID 3 if not specified. The following cipher suite ids are currently supported: </p>
<p> 0 &#8211; Authentication Algorithm = None; Integrity Algorithm = None; Confidentiality Algorithm = None </p>
<p> 1 &#8211; Authentication Algorithm = HMAC-SHA1; Integrity Algorithm = None; Confidentiality Algorithm = None </p>
<p> 2 &#8211; Authentication Algorithm = HMAC-SHA1; Integrity Algorithm = HMAC-SHA1-96; Confidentiality Algorithm = None </p>
<p> 3 &#8211; Authentication Algorithm = HMAC-SHA1; Integrity Algorithm = HMAC-SHA1-96; Confidentiality Algorithm = AES-CBC-128 </p>
<p> 6 &#8211; Authentication Algorithm = HMAC-MD5; Integrity Algorithm = None; Confidentiality Algorithm = None </p>
<p> 7 &#8211; Authentication Algorithm = HMAC-MD5; Integrity Algorithm = HMAC-MD5-128; Confidentiality Algorithm = None </p>
<p> 8 &#8211; Authentication Algorithm = HMAC-MD5; Integrity Algorithm = HMAC-MD5-128; Confidentiality Algorithm = AES-CBC-128 </p>
<p> 11 &#8211; Authentication Algorithm = HMAC-MD5; Integrity Algorithm = MD5-128; Confidentiality Algorithm = None </p>
<p> 12 &#8211; Authentication Algorithm = HMAC-MD5; Integrity Algorithm = MD5-128; Confidentiality Algorithm = AES-CBC-128 </p>
<p> 15 &#8211; Authentication Algorithm = HMAC-SHA256; Integrity Algorithm = None; Confidentiality Algorithm = None </p>
<p> 16 &#8211; Authentication Algorithm = HMAC-SHA256; Integrity Algorithm = HMAC_SHA256_128; Confidentiality Algorithm = None </p>
<p> 17 &#8211; Authentication Algorithm = HMAC-SHA256; Integrity Algorithm = HMAC_SHA256_128; Confidentiality Algorithm = AES-CBC-128</p>
<dt><code>-l</code> <i>PRIVILEGE-LEVEL</i>, <code>&#8211;privilege-level</code>=<i>PRIVILEGE-LEVEL</i></p>
<dd>Specify the privilege level to be used. The currently available privilege levels are USER, OPERATOR, and ADMIN. Defaults to OPERATOR if not specified.</p>
<dt><code>&#8211;config-file</code>=<i>FILE</i></p>
<dd>Specify an alternate configuration file.</p>
<dt><code>-W</code> <i>WORKAROUNDS</i>, <code>&#8211;workaround-flags</code>=<i>WORKAROUNDS</i></p>
<dd>Specify workarounds to vendor compliance issues. Multiple workarounds can be specified separated by commas. A special command line flag of &quot;none&quot;, will indicate no workarounds (may be useful for overriding configured defaults). See WORKAROUNDS below for a list of available workarounds.</p>
<dt><code>&#8211;debug</code></p>
<dd>Turn on debugging.</p>
<dt><code>-?</code>, <code>&#8211;help</code></p>
<dd>Output a help list and exit.</p>
<dt><code>&#8211;usage</code></p>
<dd>Output a usage message and exit.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>Output the program version and exit.</dl>
<h2>Ipmipower Options</h2>
<p>The following options are specific to <code>ipmipower.</code></p>
<dl>
<dt><code>-n</code>, <code>&#8211;on</code></p>
<dd>Power on the target hosts.</p>
<dt><code>-f</code>, <code>&#8211;off</code></p>
<dd>Power off the target hosts.</p>
<dt><code>-c</code>, <code>&#8211;cycle</code></p>
<dd>Power cycle the target hosts.</p>
<dt><code>-r</code>, <code>&#8211;reset</code></p>
<dd>Reset the target hosts.</p>
<dt><code>-s</code>, <code>&#8211;stat</code></p>
<dd>Get power status of the target hosts.</p>
<dt><code>&#8211;pulse</code></p>
<dd>Send power diagnostic interrupt to target hosts.</p>
<dt><code>&#8211;soft</code></p>
<dd>Initiate a soft-shutdown of the OS via ACPI.</p>
<dt><code>&#8211;on-if-off</code></p>
<dd>The IPMI specification does not require the power cycle or hard reset commands to turn on a machine that is currently powered off. This option will force <code>ipmipower</code> to issue a power on command instead of a power cycle or hard reset command if the remote machine&#8217;s power is currently off.</p>
<dt><code>&#8211;wait-until-on</code></p>
<dd>The IPMI specification allows power on commands to return prior to the power on actually taking place. This option will force <code>ipmipower</code> to regularly query the remote BMC and return only after the machine has powered on.</p>
<dt><code>&#8211;wait-until-off</code></p>
<dd>The IPMI specification allows power off commands to return prior the power off actually taking place. This option will force <code>ipmipower</code> to regularly query the remote BMC and return only after the machine has powered off.</p>
<dt><code>&#8211;oem-power-type</code>=<i>OEM-POWER-TYPE</i></p>
<dd>This option informs <code>ipmipower</code> to initiate power control operations via an IPMI OEM specific power control extension. The currently available POWERTYPEs are <i>NONE</i> and <i>C410X</i>. Please see OEM POWER EXTENSIONS below for additional information.</dl>
<h2>Ipmipower Advanced Network Options</h2>
<p>The following options are used to change the networking behavior of <code>ipmipower.</code></p>
<dl>
<dt><code>&#8211;retransmission-wait-timeout</code>=<i>MILLISECONDS</i></p>
<dd>Specify the retransmission wait timeout length in milliseconds. The retransmission wait timeout is similar to the retransmission timeout above, but is used specifically for power completion verification with the <code>&#8211;wait-until-on</code> and <code>&#8211;wait-until-off</code> options. Defaults to 500 milliseconds (0.5 seconds).</p>
<dt><code>&#8211;retransmission-backoff-count</code>=<i>COUNT</i></p>
<dd>Specify the retransmission backoff count for retransmissions. After ever COUNT retransmissions, the retransmission timeout length will be increased by another factor. Defaults to 8.</p>
<dt><code>&#8211;ping-interval</code>=<i>MILLISECONDS</i></p>
<dd>Specify the ping interval length in milliseconds. When running in interactive mode, RMCP (Remote Management Control Protocol) discovery messages will be sent to all configured remote hosts every MILLISECONDS to confirm their support of IPMI. Power commands cannot be sent to a host until it is discovered (or re-discovered if previously lost). Defaults to 5000 milliseconds (5 seconds). Ping discovery messages can be disabled by setting this valu to 0. RMCP ping discovery messages are automatically disabled in non-interactive mode.</p>
<dt><code>&#8211;ping-timeout</code>=<i>MILLISECONDS</i></p>
<dd>Specify the ping timeout length in milliseconds. When running in interactive mode, RMCP (Remote Management Control Protocol) messages discovery will be sent to all configured remote hosts to confirm their support of IPMI. A remote host is considered undiscovered if the host does not respond in MILLISECONDS time. Defaults to 30000 milliseconds (30 seconds). The ping timeout cannot be larger than the ping interval.</p>
<dt><code>&#8211;ping-packet-count</code>=<i>COUNT</i></p>
<dd>Specify the ping packet count size. Defaults to 10. See the <code>&#8211;ping-percent-fR option below for more information on this option.</p>
<dt>&#8211;ping-percent</code>=<i>PERCENT</i></p>
<dd>Specify the ping percent value. Defaults to 50. Since IPMI is based on UDP, it is difficult for <code>ipmipower</code> to distinguish between a missing machine and a bad (or heavily loaded) network connection in interactive mode. when running in interactive mode. For example, suppose a link consistently drops 80% of the packets to a particular machine. The power control operation may have difficulty completing, although a recent pong response from RMCP makes <code>ipmipower</code> believe the machine is up and functioning properly. The ping packet acount and percent options are used to alleviate this problem. <code>Ipmipower</code> will monitor RMCP ping packets in packet count chunks. If <code>ipmipower</code> does not receive a response to greater than ping percent of those packets, <code>ipmipower</code> will assume the link to this node is bad and will not send power control operations to that node until the connection is determined to be reliable. This heuristic can be disabled by setting either the ping packet count or ping percent to 0. This feature is not used if ping interval is set to 0.</p>
<dt><code>&#8211;ping-consec-count</code>=<i>COUNT</i></p>
<dd>Specify the ping consecutive count. This is another heuristic used to determine if a node should be considered discovered, undiscovered, or with a bad connection. If a valid RMCP pong response was received for the last COUNT ping packets, a node will be considered discovered, regardless of other heuristics listed above. Defaults to 5. This heuristic can be disabled by setting this value to 0. This feature is not used if other ping features described above are disabled.</dl>
<h2>Hostranged Options</h2>
<p>The following options manipulate hostranged output. See HOSTRANGED SUPPORT below for additional information on hostranges.</p>
<dl>
<dt><code>-B</code>, <code>&#8211;buffer-output</code></p>
<dd>Buffer hostranged output. For each node, buffer standard output until the node has completed its IPMI operation. When specifying this option, data may appear to output slower to the user since the the entire IPMI operation must complete before any data can be output. See HOSTRANGED SUPPORT below for additional information.</p>
<dt><code>-C</code>, <code>&#8211;consolidate-output</code></p>
<dd>Consolidate hostranged output. The complete standard output from every node specified will be consolidated so that nodes with identical output are not output twice. A header will list those nodes with the consolidated output. When this option is specified, no output can be seen until the IPMI operations to all nodes has completed. If the user breaks out of the program early, all currently consolidated output will be dumped. See HOSTRANGED SUPPORT below for additional information.</p>
<dt><code>-F</code> <i>NUM</i>, <code>&#8211;fanout</code>=<i>NUM</i></p>
<dd>Specify multiple host fanout. Indicates the maximum number of power control operations that can be executed in parallel.</p>
<dt><code>-E</code>, <code>&#8211;eliminate</code></p>
<dd>Eliminate hosts determined as undetected by <code>ipmidetect.</code> This attempts to remove the common issue of hostranged execution timing out due to several nodes being removed from service in a large cluster. The <code>ipmidetectd</code> daemon must be running on the node executing the command.</p>
<dt><code>&#8211;always-prefix</code></p>
<dd>Always prefix output, even if only one host is specified or communicating in-band. This option is primarily useful for scripting purposes. Option will be ignored if specified with the <code>-C</code> option.</dl>
<h2>Interactive Commands</h2>
<p><code>ipmipower</code> provides the following interactive commands at the ipmipower&gt; prompt. Before any power commands (on, off, cycle, reset, stat, pulse, or soft) can be used, hostnames must be configured into <code>ipmipower,</code> either through the command prompt or the hostname command below. The parameters and options to the commands below mirror their appropriate command line options.</p>
<dl>
<dt><code>hostname</code> <i>[IPMIHOST(s)]</i></p>
<dd>Specify a new set of hosts. No input to unconfigure all hosts.</p>
<dt><code>username</code> <i>[USERNAME]</i></p>
<dd>Specify a new username. No input for null username.</p>
<dt><code>password</code> <i>[PASSWORD]</i></p>
<dd>Specify a new password. No input for null password.</p>
<dt><code>k_g</code> <i>[K_G]</i></p>
<dd>Specify a new K_g BMC Key. No input for null key. Prefix with &#8216;0x&#8217; to enter a key in hexadecimal</p>
<dt><code>ipmi-version</code> <i>IPMIVERSION</i></p>
<dd>Specify the ipmi version to use.</p>
<dt><code>session-timeout</code> <i>MILLISECONDS</i></p>
<dd>Specify a new session timeout length.</p>
<dt><code>retransmission-timeout</code> <i>MILLISECONDS</i></p>
<dd>Specify a new retransmiision timeout length.</p>
<dt><code>authentication-type</code> <i>AUTHENTICATION-TYPE</i></p>
<dd>Specify the authentication type to use.</p>
<dt><code>cipher-suite-id</code> <i>CIPHER-SUITE-ID</i></p>
<dd>Specify the cipher suite id to use.</p>
<dt><code>privilege-level</code> <i>PRIVILEGE-LEVEL</i></p>
<dd>Specify the privilege level to use.</p>
<dt><code>workaround-flags</code> <i>WORKAROUNDS</i></p>
<dd>Specify workaround flags.</p>
<dt><code>debug</code> <i>[on|off]</i></p>
<dd>Toggle debug output.</p>
<dt><code>on</code> <i>[IPMIHOST(s)]</i></p>
<dd>Turn on all configured hosts or specified hosts.</p>
<dt><code>off</code> <i>[IPMIHOST(s)]</i></p>
<dd>Turn off all configured hosts or specified hosts.</p>
<dt><code>cycle</code> <i>[IPMIHOST(s)]</i></p>
<dd>Power cycle all configured hosts or specified hosts.</p>
<dt><code>reset</code> <i>[IPMIHOST(s)]</i></p>
<dd>Reset all configured hosts or specified hosts.</p>
<dt><code>stat</code> <i>[IPMIHOST(s)]</i></p>
<dd>Query power status for all configured hosts or specified hosts.</p>
<dt><code>pulse</code> <i>[IPMIHOST(s)]</i></p>
<dd>Pulse diagnostic interrupt all configured hosts or specified hosts.</p>
<dt><code>soft</code> <i>[IPMIHOST(s)]</i></p>
<dd>Initiate a soft-shutdown for all configured hosts or specified hosts.</p>
<dt><code>identify-on</code> <i>[IPMIHOST(s)]</i></p>
<dd>Turn on physical system identification.</p>
<dt><code>identify-off</code> <i>[IPMIHOST(s)]</i></p>
<dd>Turn off physical system identification.</p>
<dt><code>identify-status</code> <i>[IPMIHOST(s)]</i></p>
<dd>Query physical system identification status.</p>
<dt><code>on-if-off</code> <i>[on|off]</i></p>
<dd>Toggle on-if-off functionality.</p>
<dt><code>wait-until-on</code> <i>[on|off]</i></p>
<dd>Toggle wait-until-on functionality.</p>
<dt><code>wait-until-off</code> <i>[on|off]</i></p>
<dd>Toggle wait-until-off functionality.</p>
<dt><code>retransmission-wait-timeout</code> <i>MILLISECONDS</i></p>
<dd>Specify a new retransmission wait timeout length.</p>
<dt><code>retransmission-backoff-count</code> <i>COUNT</i></p>
<dd>Specify a new retransmission backoff count.</p>
<dt><code>ping-interval</code> <i>MILLISECONDS</i></p>
<dd>Specify a new ping interval length.</p>
<dt><code>ping-timeout</code> <i>MILLISECONDS</i></p>
<dd>Specify a new ping timeout length.</p>
<dt><code>ping-packet-count</code> <i>COUNT</i></p>
<dd>Specify a new ping packet count.</p>
<dt><code>ping-percent</code> <i>PERCENT</i></p>
<dd>Specify a new ping percent.</p>
<dt><code>ping-consec-count</code> <i>COUNT</i></p>
<dd>Specify a new ping consec count.</p>
<dt><code>buffer-output</code> <i>[on|off]</i></p>
<dd>Toggle buffer-output functionality.</p>
<dt><code>consolidate-output</code> <i>[on|off]</i></p>
<dd>Toggle consolidate-output functionality.</p>
<dt><code>fanout</code> <i>COUNT</i></p>
<dd>Specify a fanout.</p>
<dt><code>always-prefix</code> <i>[on|off]</i></p>
<dd>Toggle always-prefix functionality.</p>
<dt><code>help</code></p>
<dd>Output help menu.</p>
<dt><code>version</code></p>
<dd>Output version.</p>
<dt><code>config</code></p>
<dd>Output the current configuration.</p>
<dt><code>quit</code></p>
<dd>Quit program. <code>ipmipower.</code></dl>
<h2>Oem Power Extensions</h2>
<p>Some motherboards include IPMI OEM extensions for alternate power control mechanisms. For example, these power control mechanisms may allow you to power control a sub-device within the system rather than the entire system itself. </p>
<p> By specifying an OEM power type via <code>&#8211;oem-power-type</code> on the command line or <code><a href="/docs/linux/man/5-freeipmi-conf/">freeipmi.conf</a>(5),</code> you can instruct <code>ipmipower</code> to execute alternate power control implementations over the standard ones. Depending on the OEM extension, some power control commands may no longer be available. For example, an OEM extension may allow <code>on</code> but not <code>cycle</code>. Specific <code>ipmipower</code> options may not longer function either. </p>
<p> Some OEM extensions may require additional arguments for their power control action, such as a sub-device identifier. Additional arguments can be provided by appending a plus sign (&#8216;+&#8217;) and the extra information to the end of the hostname. This can be done on the command line or in interactive mode. For example, the hostname <i>mynode+18</i> would indicate the power control operation should be sent to the host <i>mynode</i>, and <i>18</i> is the identifier of a possible sub-device to be power controlled. The <i>&#8211;consolidate-output</i> option is commonly disabled when using an OEM power control that requires extra arguments. </p>
<p> Because OEM power control may involve subtypes, it is possible a user may wish to power control multiple sub-devices on the same host. For example, you might specify the hosts <i>mynode+1,mynode+2</i>, indicating to power control subdevice 1 and 2 on <i>mynode</i>. Because many BMCs cannot handle multiple IPMI sessions, power control operations to the same host will be serialized internally by <code>ipmipower.</code> </p>
<p> The following are the current OEM power types available, along with information on the systems they work with and the power control operations available.</p>
<dl>
<dt><code>C410X</code></p>
<dd>This OEM power type supports the power control of PCIe slots on Dell Poweredge C410x systems. It supports <code>on</code>, <code>off</code>, and <code>stat</code>. The PCIe slot number ranges from 1-16 and must always be specified when attempting to power control with this extension. For example, the hostname <i>mynode+2</i> would inform <code>ipmipower</code> to operate on slot number <i>2</i> on <i>mynode</i>. The C410x appears to have difficulty handling new slot power control requests until prior ones have completed. Users may wish to strongly consider using the <code>&#8211;wait-until-on</code> and <code>&#8211;wait-until-off</code> options if multiple slots will be power controlled in short succession.</p>
<dt><code>NONE</code></p>
<dd>This informs <code>ipmipower</code> that no OEM power type extension is to be used and standard IPMI power control is used. This is the default.</dl>
<h2>Hostranged Support</h2>
<p>Multiple hosts can be input either as an explicit comma separated lists of hosts or a range of hostnames in the general form: prefix[n-m,l-k,&#8230;], where n &lt; m and l &lt; k, etc. The later form should not be confused with regular expression character classes (also denoted by []). For example, foo[19] does not represent foo1 or foo9, but rather represents a degenerate range: foo19. </p>
<p> This range syntax is meant only as a convenience on clusters with a prefixNN naming convention and specification of ranges should not be considered necessary &#8212; the list foo1,foo9 could be specified as such, or by the range foo[1,9]. </p>
<p> Some examples of range usage follow: </p>
<pre> foo[01-05] instead of foo01,foo02,foo03,foo04,foo05
 foo[7,9-10] instead of foo7,foo9,foo10
 foo[0-3] instead of foo0,foo1,foo2,foo3</pre>
<p>As a reminder to the reader, some shells will interpret brackets ([ and ]) for pattern matching. Depending on your shell, it may be necessary to enclose ranged lists within quotes. </p>
<p> When multiple hosts are specified by the user, a socket will be created for each host and polled on, effectively allowing communication to all hosts in parallel. This will allow communication to large numbers of nodes far more quickly than if done in serial. The <code>-F</code> option can configure the number of nodes that can be communicated with in parallel at the same time. </p>
<p> By default, standard output from each node specified will be output with the hostname prepended to each line. Although this output is readable in many situations, it may be difficult to read in other situations. For example, output from multiple nodes may be mixed together. The <code>-B</code> and <code>-C</code> options can be used to change this default.</p>
<h2>Examples</h2>
<p>Determine the power status of foo[0-2] with null username and password<br />
&nbsp;<wbr>&nbsp;<wbr>ipmipower -h foo[0-2]&nbsp;<wbr>&#8211;stat </p>
<p> Determine the power status of foo[0-2] with non-null username and password<br />
&nbsp;<wbr>&nbsp;<wbr>ipmipower -h foo[0-2]&nbsp;<wbr>-u foo -p bar &#8211;stat </p>
<p> Hard reset nodes foo[0-2] with non-null username and password<br />
&nbsp;<wbr>&nbsp;<wbr>ipmipower -h foo[0-2]&nbsp;<wbr>-u foo -p bar &#8211;reset</p>
<h2>General Troubleshooting</h2>
<p>Most often, IPMI problems are due to configuration problems. </p>
<p> IPMI over LAN problems involve a misconfiguration of the remote machine&#8217;s BMC. Double check to make sure the following are configured properly in the remote machine&#8217;s BMC: IP address, MAC address, subnet mask, username, user enablement, user privilege, password, LAN privilege, LAN enablement, and allowed authentication type(s). For IPMI 2.0 connections, double check to make sure the cipher suite privilege(s) and K_g key are configured properly. The <code><a href="/docs/linux/man/8-bmc-config/">bmc-config</a>(8)</code> tool can be used to check and/or change these configuration settings. </p>
<p> In addition to the troubleshooting tips below, please see WORKAROUNDS below to also if there are any vendor specific bugs that have been discovered and worked around. </p>
<p> Listed below are many of the common issues for error messages. For additional support, please e-mail the &lt;freeipmi-users [at] gnu.org&gt; mailing list. </p>
<p> &quot;username invalid&quot; &#8211; The username entered (or a NULL username if none was entered) is not available on the remote machine. It may also be possible the remote BMC&#8217;s username configuration is incorrect. </p>
<p> &quot;password invalid&quot; &#8211; The password entered (or a NULL password if none was entered) is not correct. It may also be possible the password for the user is not correctly configured on the remote BMC. </p>
<p> &quot;password verification timeout&quot; &#8211; Password verification has timed out. A &quot;password invalid&quot; error (described above) or a generic &quot;session timeout&quot; (described below) occurred. During this point in the protocol it cannot be differentiated which occurred. </p>
<p> &quot;k_g invalid&quot; &#8211; The K_g key entered (or a NULL K_g key if none was entered) is not correct. It may also be possible the K_g key is not correctly configured on the remote BMC. </p>
<p> &quot;privilege level insufficient&quot; &#8211; An IPMI command requires a higher user privilege than the one authenticated with. Please try to authenticate with a higher privilege. This may require authenticating to a different user which has a higher maximum privilege. </p>
<p> &quot;privilege level cannot be obtained for this user&quot; &#8211; The privilege level you are attempting to authenticate with is higher than the maximum allowed for this user. Please try again with a lower privilege. It may also be possible the maximum privilege level allowed for a user is not configured properly on the remote BMC. </p>
<p> &quot;authentication type unavailable for attempted privilege level&quot; &#8211; The authentication type you wish to authenticate with is not available for this privilege level. Please try again with an alternate authentication type or alternate privilege level. It may also be possible the available authentication types you can authenticate with are not correctly configured on the remote BMC. </p>
<p> &quot;cipher suite id unavailable&quot; &#8211; The cipher suite id you wish to authenticate with is not available on the remote BMC. Please try again with an alternate cipher suite id. It may also be possible the available cipher suite ids are not correctly configured on the remote BMC. </p>
<p> &quot;ipmi 2.0 unavailable&quot; &#8211; IPMI 2.0 was not discovered on the remote machine. Please try to use IPMI 1.5 instead. </p>
<p> &quot;connection timeout&quot; &#8211; Initial IPMI communication failed. A number of potential errors are possible, including an invalid hostname specified, an IPMI IP address cannot be resolved, IPMI is not enabled on the remote server, the network connection is bad, etc. Please verify configuration and connectivity. </p>
<p> &quot;session timeout&quot; &#8211; The IPMI session has timed out. Please reconnect. If this error occurs often, you may wish to increase the retransmission timeout. Some remote BMCs are considerably slower than others. </p>
<p> &quot;internal IPMI error&quot; &#8211; An IPMI error has occurred that FreeIPMI does not know how to handle. Please e-mail &lt;freeipmi-users [at] gnu.org&gt; to report the issue.</p>
<h2>Ipmipower Troubleshooting</h2>
<p>When powering on a powered off machine, the client must have a means by which to resolve the MAC address of the remote machine&#8217;s ethernet card. While most modern IPMI solutions support the ability to ARP and resolve addresses when the machine is powered off, some older machines do not. This is typically solved in one of two ways: </p>
<p> 1) Enable gratuitous ARPs on the remote machine. The remote machine will send out a gratuitous ARP, which advertises the ethernet IP and MAC address so that other machines on the network this information their local ARP cache. For large clusters, this method is not recommended since gratuitous ARPs can flood the network with unnecessary traffic. </p>
<p> 2) Permanently store the remote machine&#8217;s MAC address in the local ARP cache. This is the more common approach on large clusters. </p>
<p> Other methods are listed in the IPMI specification.</p>
<h2>Workarounds</h2>
<p>With so many different vendors implementing their own IPMI solutions, different vendors may implement their IPMI protocols incorrectly. The following describes a number of workarounds currently available to handle discovered compliance issues. When possible, workarounds have been implemented so they will be transparent to the user. However, some will require the user to specify a workaround be used via the -W option. </p>
<p> The hardware listed below may only indicate the hardware that a problem was discovered on. Newer versions of hardware may fix the problems indicated below. Similar machines from vendors may or may not exhibit the same problems. Different vendors may license their firmware from the same IPMI firmware developer, so it may be worthwhile to try workarounds listed below even if your motherboard is not listed. </p>
<p> If you believe your hardware has an additional compliance issue that needs a workaround to be implemented, please contact the FreeIPMI maintainers on &lt;freeipmi-users [at] gnu.org&gt; or &lt;freeipmi-devel [at] gnu.org&gt;. </p>
<p> <i>authcap</i> &#8211; This workaround flag will skip early checks for username capabilities, authentication capabilities, and K_g support and allow IPMI authentication to succeed. It works around multiple issues in which the remote system does not properly report username capabilities, authentication capabilities, or K_g status. Those hitting this issue may see &quot;username invalid&quot;, &quot;authentication type unavailable for attempted privilege level&quot;, or &quot;k_g invalid&quot; errors. Issue observed on Asus P5M2/P5MT-R/RS162-E4/RX4, Intel SR1520ML/X38ML, and Sun Fire 2200/4150/4450 with ELOM. </p>
<p> <i>nochecksumcheck</i> &#8211; This workaround flag will tell FreeIPMI to not check the checksums returned from IPMI command responses. It works around systems that return invalid checksums due to implementation errors, but the packet is otherwise valid. Users are cautioned on the use of this option, as it removes validation of packet integrity in a number of circumstances. However, it is unlikely to be an issue in most situations. Those hitting this issue may see &quot;connection timeout&quot;, &quot;session timeout&quot;, or &quot;password verification timeout&quot; errors. On IPMI 1.5 connections, the &quot;noauthcodecheck&quot; workaround may also needed too. Issue observed on Supermicro X9SCM-iiF, Supermicro X9DRi-F, and Supermicro X9DRFR. </p>
<p> <i>idzero</i> &#8211; This workaround flag will allow empty session IDs to be accepted by the client. It works around IPMI sessions that report empty session IDs to the client. Those hitting this issue may see &quot;session timeout&quot; errors. Issue observed on Tyan S2882 with M3289 BMC. </p>
<p> <i>unexpectedauth</i> &#8211; This workaround flag will allow unexpected non-null authcodes to be checked as though they were expected. It works around an issue when packets contain non-null authentication data when they should be null due to disabled per-message authentication. Those hitting this issue may see &quot;session timeout&quot; errors. Issue observed on Dell PowerEdge 2850,SC1425. Confirmed fixed on newer firmware. </p>
<p> <i>forcepermsg</i> &#8211; This workaround flag will force per-message authentication to be used no matter what is advertised by the remote system. It works around an issue when per-message authentication is advertised as disabled on the remote system, but it is actually required for the protocol. Those hitting this issue may see &quot;session timeout&quot; errors. Issue observed on IBM eServer 325. </p>
<p> <i>endianseq</i> &#8211; This workaround flag will flip the endian of the session sequence numbers to allow the session to continue properly. It works around IPMI 1.5 session sequence numbers that are the wrong endian. Those hitting this issue may see &quot;session timeout&quot; errors. Issue observed on some Sun ILOM 1.0/2.0 (depends on service processor endian). </p>
<p> <i>noauthcodecheck</i> &#8211; This workaround flag will tell FreeIPMI to not check the authentication codes returned from IPMI 1.5 command responses. It works around systems that return invalid authentication codes due to hashing or implementation errors. Users are cautioned on the use of this option, as it removes an authentication check verifying the validity of a packet. However, in most organizations, this is unlikely to be a security issue. Those hitting this issue may see &quot;connection timeout&quot;, &quot;session timeout&quot;, or &quot;password verification timeout&quot; errors. Issue observed on Xyratex FB-H8-SRAY. </p>
<p> <i>intel20</i> &#8211; This workaround flag will work around several Intel IPMI 2.0 authentication issues. The issues covered include padding of usernames, and password truncation if the authentication algorithm is HMAC-MD5-128. Those hitting this issue may see &quot;username invalid&quot;, &quot;password invalid&quot;, or &quot;k_g invalid&quot; errors. Issue observed on Intel SE7520AF2 with Intel Server Management Module (Professional Edition). </p>
<p> <i>supermicro20</i> &#8211; This workaround flag will work around several Supermicro IPMI 2.0 authentication issues on motherboards w/ Peppercon IPMI firmware. The issues covered include handling invalid length authentication codes. Those hitting this issue may see &quot;password invalid&quot; errors. Issue observed on Supermicro H8QME with SIMSO daughter card. Confirmed fixed on newerver firmware. </p>
<p> <i>sun20</i> &#8211; This workaround flag will work work around several Sun IPMI 2.0 authentication issues. The issues covered include invalid lengthed hash keys, improperly hashed keys, and invalid cipher suite records. Those hitting this issue may see &quot;password invalid&quot; or &quot;bmc error&quot; errors. Issue observed on Sun Fire 4100/4200/4500 with ILOM. This workaround automatically includes the &quot;opensesspriv&quot; workaround. </p>
<p> <i>opensesspriv</i> &#8211; This workaround flag will slightly alter FreeIPMI&#8217;s IPMI 2.0 connection protocol to workaround an invalid hashing algorithm used by the remote system. The privilege level sent during the Open Session stage of an IPMI 2.0 connection is used for hashing keys instead of the privilege level sent during the RAKP1 connection stage. Those hitting this issue may see &quot;password invalid&quot;, &quot;k_g invalid&quot;, or &quot;bad rmcpplus status code&quot; errors. Issue observed on Sun Fire 4100/4200/4500 with ILOM, Inventec 5441/Dell Xanadu II, Supermicro X8DTH, Supermicro X8DTG, Intel S5500WBV/Penguin Relion 700, Intel S2600JF/Appro 512X, and Quanta QSSC-S4R/Appro GB812X-CN. This workaround is automatically triggered with the &quot;sun20&quot; workaround. </p>
<p> <i>integritycheckvalue</i> &#8211; This workaround flag will work around an invalid integrity check value during an IPMI 2.0 session establishment when using Cipher Suite ID 0. The integrity check value should be 0 length, however the remote motherboard responds with a non-empty field. Those hitting this issue may see &quot;k_g invalid&quot; errors. Issue observed on Supermicro X8DTG, Supermicro X8DTU, and Intel S5500WBV/Penguin Relion 700, and Intel S2600JF/Appro 512X. </p>
<p> No IPMI 1.5 Support &#8211; Some motherboards that support IPMI 2.0 have been found to not support IPMI 1.5. Those hitting this issue may see &quot;ipmi 2.0 unavailable&quot; or &quot;connection timeout&quot; errors. This issue can be worked around by using IPMI 2.0 instead of IPMI 1.5 by specifying <code>&#8211;driver-type</code>=<i>LAN_2_0</i>. Issue observed on HP Proliant DL 145.</p>
<h2>Diagnostics</h2>
<p>Upon successful execution, exit status is 0. On error, exit status is 1. </p>
<p> If multiple hosts are specified for communication, the exit status is 0 if and only if all targets successfully execute. Otherwise the exit status is 1. </p>
<p> When operating in interactive mode, the exit value will be based on the last power operation executed.</p>
<h2>Known Issues</h2>
<p>On older operating systems, if you input your username, password, and other potentially security relevant information on the command line, this information may be discovered by other users when using tools like the <code><a href="/docs/linux/man/1-ps/">ps</a>(1)</code> command or looking in the /proc file system. It is generally more secure to input password information with options like the -P or -K options. Configuring security relevant information in the FreeIPMI configuration file would also be an appropriate way to hide this information. </p>
<p> In order to prevent brute force attacks, some BMCs will temporarily &quot;lock up&quot; after a number of remote authentication errors. You may need to wait awhile in order to this temporary &quot;lock up&quot; to pass before you may authenticate again. </p>
<p> IPMI specifications do not require BMCs to perform a power control operation before returning a completion code to the caller. Therefore, it is possible for <code>ipmipower</code> to return power status queries opposite of what you are expecting. For example, if a &quot;power off&quot; operation is performed, a BMC may return a successful completion code to <code>ipmipower</code> before the &quot;power off&quot; operation is actually performed. Subsequent power status queries may return &quot;on&quot; for several seconds, until the BMC actually performs the &quot;power off&quot; operation.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;freeipmi-users [at] gnu.org&gt; or &lt;freeipmi-devel [at] gnu.org&gt;.</p>
<h2>Copyright</h2>
<p>Copyright (C) 2007-2012 Lawrence Livermore National Security, LLC.<br />
 Copyright (C) 2003-2007 The Regents of the University of California. </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 3 of the License, or (at your option) any later version.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/5-freeipmi-conf/">freeipmi.conf</a>(5), <a href="/docs/linux/man/7-freeipmi/">freeipmi</a>(7), <a href="/docs/linux/man/8-bmc-config/">bmc-config</a>(8), <a href="/docs/linux/man/8-ipmi-oem/">ipmi-oem</a>(8) <a rel="nofollow" href="http://www.gnu.org/software/freeipmi/">http://www.gnu.org/software/freeipmi/</a> </p>
