---
title: "ipmimonitoring(8)"
name: "ipmimonitoring"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ipmimonitoring/"
description: "ipmi-sensors – display IPMI sensor information"
---

<p>ipmi-sensors &#8211; display IPMI sensor information</p>
<h2>Synopsis</h2>
<p><code>ipmi-sensors</code> [<i>OPTION</i>&#8230;]</p>
<h2>Description</h2>
<p><code>Ipmi-sensors</code> displays current readings of sensors and sensor data repository (SDR) information. The default display outputs each sensor&#8217;s record id, sensor name, sensor type name, sensor reading (if appropriate), and the current sensor event. More verbose information can be found using the verbose options specified below. <code>Ipmi-sensors</code> does not inform the user if a problem exists with a particular sensor because sensor readings and events are not analyzed by default. Users may wish to use the <code>&#8211;output-sensor-state</code> option to output the analyzed sensor state. Some sensors may have a sensor reading or sensor event of &quot;N/A&quot; if the information is unavailable. This is typical of a sensor that is not enabled or not owned by a BMC. Please see <code>&#8211;bridge-sensors</code> option below to deal with sensors not owned by a BMC. Sensors may output a sensor event of &quot;Unknown&quot; if the sensor reading cannot be read. This is typical of a sensor that is busy or a reading that cannot be calculated. If sensors report &quot;Unrecognized State&quot;, it is indicative of an unkown sensor type, typically an OEM sensor. If the sensor OEM interpretation is available, the <code>&#8211;interpret-oem-data</code> may be able to report the appropriate sensor state. Sensors need not always report a sensor event. When a sensor event is not present, &quot;OK&quot; is typically reported. </p>
<p> Listed below are general IPMI options, tool specific options, trouble shooting information, workaround information, examples, and known issues. For a general introduction to FreeIPMI please see <code><a href="/docs/linux/man/7-freeipmi/">freeipmi</a>(7).</code> To perform IPMI sensor configuration, please see <code><a href="/docs/linux/man/8-ipmi-sensors-config/">ipmi-sensors-config</a>(8).</code> To perform some advanced SDR management, please see <code><a href="/docs/linux/man/8-bmc-device/">bmc-device</a>(8).</code></p>
<h2>General Options</h2>
<p>The following options are general options for configuring IPMI communication and executing general tool commands.</p>
<dl>
<dt><code>-D</code> <i>IPMIDRIVER</i>, <code>&#8211;driver-type</code>=<i>IPMIDRIVER</i></p>
<dd>Specify the driver type to use instead of doing an auto selection. The currently available outofband drivers are LAN and LAN_2_0, which perform IPMI 1.5 and IPMI 2.0 respectively. The currently available inband drivers are KCS, SSIF, OPENIPMI, and SUNBMC.</p>
<dt><code>&#8211;disable-auto-probe</code></p>
<dd>Do not probe in-band IPMI devices for default settings.</p>
<dt><code>&#8211;driver-address</code>=<i>DRIVER-ADDRESS</i></p>
<dd>Specify the in-band driver address to be used instead of the probed value. <i>DRIVER-ADDRESS</i> should be prefixed with &quot;0x&quot; for a hex value and &#8216;0&#8217; for an octal value.</p>
<dt><code>&#8211;driver-device</code>=<i>DEVICE</i></p>
<dd>Specify the in-band driver device path to be used instead of the probed path.</p>
<dt><code>&#8211;register-spacing</code>=<i>REGISTER-SPACING</i></p>
<dd>Specify the in-band driver register spacing instead of the probed value. Argument is in bytes (i.e. 32bit register spacing = 4)</p>
<dt><code>&#8211;target-channel-number</code>=<i>CHANNEL-NUMBERFR</p>
<dd>Specify the in-band driver target channel number to send IPMI requests to.</p>
<dt></i><code>&#8211;target-slave-address</code>=<i>SLAVE-ADDRESSFR</p>
<dd>Specify the in-band driver target slave number to send IPMI requests to.</p>
<dt></i><code>-h</code> <i>IPMIHOST1,IPMIHOST2,&#8230;</i>, <code>&#8211;hostname</code>=<i>IPMIHOST1[:PORT],IPMIHOST2[:PORT],&#8230;</i></p>
<dd>Specify the remote host(s) to communicate with. Multiple hostnames may be separated by comma or may be specified in a range format; see HOSTRANGED SUPPORT below. An optional port can be specified with each host, which may be useful in port forwarding or similar situations.</p>
<dt><code>-u</code> <i>USERNAME</i>, <code>&#8211;username</code>=<i>USERNAME</i></p>
<dd>Specify the username to use when authenticating with the remote host. If not specified, a null (i.e. anonymous) username is assumed. The user must have atleast OPERATOR privileges in order for this tool to operate fully.</p>
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
<dd>Specify the packet retransmission timeout in milliseconds. Defaults to 1000 milliseconds (1 second) if not specified. The retransmission timeout cannot be larger than the session timeout.</p>
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
<h2>Ipmi-Sensors Options</h2>
<p>The following options are specific to <code>Ipmi-sensors.</code></p>
<dl>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>Output verbose sensor output. This option will output additional information about sensors such as thresholds, ranges, numbers, and event/reading type codes.</p>
<dt><code>-vv</code></p>
<dd>Output very verbose sensor output. This option will output more additional information than the verbose option such as information about events, other sensor types, and oem sensors.</p>
<dt><code>-i</code>, <code>&#8211;sdr-info</code></p>
<dd>Show sensor data repository (SDR) information</p>
<dt><code>-q</code>, <code>&#8211;quiet-readings</code></p>
<dd>Do not output sensor reading values by default. This option is particularly useful if you want to use hostranged output across a cluster and want to consolidate the output.</p>
<dt><code>-r</code> <i>RECORD-IDS-LIST</i>, <code>&#8211;record-ids</code>=<i>RECORD-IDS-LIST</i></p>
<dd>Specify sensors to show by record id. Multiple record ids can be separated by commas or spaces. If both <code>&#8211;record-ids</code> and <code>&#8211;sensor-types</code> are specified, <code>&#8211;record-ids</code> takes precedence. A special command line record id of &quot;all&quot;, will indicate all record ids should be shown (may be useful for overriding configured defaults).</p>
<dt><code>-R</code> <i>RECORD-IDS-LIST</i>, <code>&#8211;exclude-record-ids</code>=<i>RECORD-IDS-LIST</i></p>
<dd>Specify sensors to not show by record id. Multiple record ids can be separated by commas or spaces. A special command line record id of &quot;none&quot;, will indicate no record ids should be excluded (may be useful for overriding configured defaults).</p>
<dt><code>-t</code> <i>SENSOR-TYPE-LIST</i>, <code>&#8211;sensor-types</code>=<i>SENSOR-TYPE-LIST</i></p>
<dd>Specify sensor types to show outputs for. Multiple types can be separated by commas or spaces. If both <code>&#8211;record-ids</code> and <code>&#8211;sensor-types</code> are specified, <code>&#8211;record-ids</code> takes precedence. A special command line type of &quot;all&quot;, will indicate all types should be shown (may be useful for overriding configured defaults). Users may specify sensor types by string (see <code>&#8211;list-sensor-types</code> below) or by number (decimal or hex).</p>
<dt><code>-T</code> <i>SENSOR-TYPE-LIST</i>, <code>&#8211;exclude-sensor-types</code>=<i>SENSOR-TYPE-LIST</i></p>
<dd>Specify sensor types to not show outputs for. Multiple types can be eparated by commas or spaces. A special command line type of &quot;none&quot;, will indicate no types should be excluded (may be useful for overriding configured defaults). Users may specify sensor types by string (see <code>&#8211;list-sensor-types</code> below) or by number (decimal or hex).</p>
<dt><code>-L</code>, <code>&#8211;list-sensor-types</code></p>
<dd>List sensor types.</p>
<dt><code>-b</code>, <code>&#8211;bridge-sensors</code></p>
<dd>By default, sensors readings are not attempted for sensors on non-BMC owners. By setting this option, sensor requests can be bridged to non-BMC owners to obtain sensor readings. Bridging may not work on some interfaces/driver types.</p>
<dt><code>&#8211;shared-sensors</code></p>
<dd>Some sensors share the same sensor data record (SDR). This is typically utilized for system event log (SEL) entries and not for sensor readings. However, there may be some motherboards in which this format is utilized for multiple active sensors, or the user simply has interest in seeing the permutation of entries shared by a SDR entry. By setting this option, each sensor number shared by a record will be iterated over and output.</p>
<dt><code>&#8211;interpret-oem-data</code></p>
<dd>Attempt to interpret OEM data, such as event data, sensor readings, or general extra info, etc. If an OEM interpretation is not available, the default output will be generated. Correctness of OEM interpretations cannot be guaranteed due to potential changes OEM vendors may make in products, firmware, etc. See OEM INTERPRETATION below for confirmed supported motherboard interpretations.</p>
<dt><code>&#8211;ignore-not-available-sensors</code></p>
<dd>Ignore not-available (i.e. N/A) sensors in output.</p>
<dt><code>&#8211;ignore-unrecognized-events</code></p>
<dd>Ignore unrecognized sensor events. This will suppress output of unrecognized events, typically shown as &#8216;Unrecognized Event = XXXXh&#8217; in output. In addition, unrecognized events will be ignored when calculating sensor state with <i>&#8211;output-sensor-state</i> below.</p>
<dt><code>&#8211;output-event-bitmask</code></p>
<dd>Output event bitmask value instead of the string representation.</p>
<dt><code>&#8211;output-sensor-state</code></p>
<dd>Output sensor state in output. This will add an additional output reporting if a sensor is in a NOMINAL, WARNING, or CRITICAL state. The sensor state is an interpreted value based on the current sensor event. The sensor state interpretations are determined by the configuration file /etc/freeipmi//freeipmi_interpret_sensor.conf. See <code><a href="/docs/linux/man/5-freeipmi_interpret_sensor-conf/">freeipmi_interpret_sensor.conf</a>(5)</code> for more information. This option gives identical output to the sensor state previously output by <code><a href="/docs/linux/man/8-ipmimonitoring/">ipmimonitoring</a>(8).</code></p>
<dt><code>&#8211;sensor-state-config-file</code>=<i>FILE</i></p>
<dd>Specify an alternate sensor state configuration file. Option ignored if <code>&#8211;output-sensor-state</code> not specified.</p>
<dt><code>&#8211;entity-sensor-names</code></p>
<dd>Output sensor names prefixed with their entity id and instance number when appropriate. This may be necessary on some motherboards to help identify what sensors are referencing. For example, a motherboard may have multiple sensors named &#8216;TEMP&#8217;. The entity id and instance number may help clarify which sensor refers to &quot;Processor 1&quot; vs. &quot;Processor 2&quot;.</p>
<dt><code>&#8211;output-sensor-thresholds</code></p>
<dd>Output sensor thresholds in output. This will add columns to the default output for lower non-recoverable, lower critical, lower non-critical, upper non-critical, upper critical, and upper non-recoverable thresholds.</p>
<dt><code>&#8211;no-sensor-type-output</code></p>
<dd>Do not show sensor type output for each entry. On many systems, the sensor type is redundant to the name of the sensor. This can especially be true if <code>&#8211;entity-sensor-names</code> is specified. If the sensor name is sufficient, or if the sensor type is of no interest to the user, this option can be specified to condense output.</p>
<dt><code>&#8211;comma-separated-output</p>
<dd>Output fields in comma separated format.</p>
<dt>&#8211;no-header-output</p>
<dd>Do not output column headers. May be useful in scripting.</p>
<dt>&#8211;non-abbreviated-units</code></p>
<dd>Output non-abbreviated units (e.g. &#8216;Amps&#8217; instead of &#8216;A&#8217;). May aid in disambiguation of units (e.g. &#8216;C&#8217; for Celsius or Coulombs).</p>
<dt><code>&#8211;legacy-output</code></p>
<dd>Output in legacy format. Newer options may not be applicable to legacy output.</p>
<dt><code>&#8211;ipmimonitoring-legacy-output</code></p>
<dd>Output legacy format of legacy <code>ipmimonitoring</code> tool. Newer options may not be applicable to legacy output.</dl>
<h2>Sdr Cache Options</h2>
<p>This tool requires access to the sensor data repository (SDR) cache for general operation. By default, SDR data will be downloaded and cached on the local machine. The following options apply to the SDR cache.</p>
<dl>
<dt><code>-f</code>, <code>&#8211;flush-cache</code></p>
<dd>Flush a cached version of the sensor data repository (SDR) cache. The SDR is typically cached for faster subsequent access. However, it may need to be flushed and re-generated if the SDR has been updated on a system.</p>
<dt><code>-Q</code>, <code>&#8211;quiet-cache</code></p>
<dd>Do not output information about cache creation/deletion. May be useful in scripting.</p>
<dt><code>&#8211;sdr-cache-recreate</code></p>
<dd>If the SDR cache is out of date or invalid, automatically recreate the sensor data repository (SDR) cache. This option may be useful for scripting purposes.</p>
<dt><code>&#8211;sdr-cache-file</code>=<i>FILE</i></p>
<dd>Specify a specific sensor data repository (SDR) cache file to be stored or read from. If this option is used when multiple hosts are specified, the same SDR cache file will be used for all hosts.</p>
<dt><code>&#8211;sdr-cache-directory</code>=<i>DIRECTORY</i></p>
<dd>Specify an alternate directory for sensor data repository (SDR) caches to be stored or read from. Defaults to the home directory if not specified.</dl>
<h2>Hostranged Options</h2>
<p>The following options manipulate hostranged output. See HOSTRANGED SUPPORT below for additional information on hostranges.</p>
<dl>
<dt><code>-B</code>, <code>&#8211;buffer-output</code></p>
<dd>Buffer hostranged output. For each node, buffer standard output until the node has completed its IPMI operation. When specifying this option, data may appear to output slower to the user since the the entire IPMI operation must complete before any data can be output. See HOSTRANGED SUPPORT below for additional information.</p>
<dt><code>-C</code>, <code>&#8211;consolidate-output</code></p>
<dd>Consolidate hostranged output. The complete standard output from every node specified will be consolidated so that nodes with identical output are not output twice. A header will list those nodes with the consolidated output. When this option is specified, no output can be seen until the IPMI operations to all nodes has completed. If the user breaks out of the program early, all currently consolidated output will be dumped. See HOSTRANGED SUPPORT below for additional information.</p>
<dt><code>-F</code> <i>NUM</i>, <code>&#8211;fanout</code>=<i>NUM</i></p>
<dd>Specify multiple host fanout. A &quot;sliding window&quot; (or fanout) algorithm is used for parallel IPMI communication so that slower nodes or timed out nodes will not impede parallel communication. The maximum number of threads available at the same time is limited by the fanout. The default is 64.</p>
<dt><code>-E</code>, <code>&#8211;eliminate</code></p>
<dd>Eliminate hosts determined as undetected by <code>ipmidetect.</code> This attempts to remove the common issue of hostranged execution timing out due to several nodes being removed from service in a large cluster. The <code>ipmidetectd</code> daemon must be running on the node executing the command.</p>
<dt><code>&#8211;always-prefix</code></p>
<dd>Always prefix output, even if only one host is specified or communicating in-band. This option is primarily useful for scripting purposes. Option will be ignored if specified with the <code>-C</code> option.</dl>
<h2>Hostranged Support</h2>
<p>Multiple hosts can be input either as an explicit comma separated lists of hosts or a range of hostnames in the general form: prefix[n-m,l-k,&#8230;], where n &lt; m and l &lt; k, etc. The later form should not be confused with regular expression character classes (also denoted by []). For example, foo[19] does not represent foo1 or foo9, but rather represents a degenerate range: foo19. </p>
<p> This range syntax is meant only as a convenience on clusters with a prefixNN naming convention and specification of ranges should not be considered necessary &#8212; the list foo1,foo9 could be specified as such, or by the range foo[1,9]. </p>
<p> Some examples of range usage follow: </p>
<pre> foo[01-05] instead of foo01,foo02,foo03,foo04,foo05
 foo[7,9-10] instead of foo7,foo9,foo10
 foo[0-3] instead of foo0,foo1,foo2,foo3</pre>
<p>As a reminder to the reader, some shells will interpret brackets ([ and ]) for pattern matching. Depending on your shell, it may be necessary to enclose ranged lists within quotes. </p>
<p> When multiple hosts are specified by the user, a thread will be executed for each host in parallel up to the configured fanout (which can be adjusted via the <code>-F</code> option). This will allow communication to large numbers of nodes far more quickly than if done in serial. </p>
<p> By default, standard output from each node specified will be output with the hostname prepended to each line. Although this output is readable in many situations, it may be difficult to read in other situations. For example, output from multiple nodes may be mixed together. The <code>-B</code> and <code>-C</code> options can be used to change this default. </p>
<p> In-band IPMI Communication will be used when the host &quot;localhost&quot; is specified. This allows the user to add the localhost into the hostranged output.</p>
<h2>General Troubleshooting</h2>
<p>Most often, IPMI problems are due to configuration problems. </p>
<p> IPMI over LAN problems involve a misconfiguration of the remote machine&#8217;s BMC. Double check to make sure the following are configured properly in the remote machine&#8217;s BMC: IP address, MAC address, subnet mask, username, user enablement, user privilege, password, LAN privilege, LAN enablement, and allowed authentication type(s). For IPMI 2.0 connections, double check to make sure the cipher suite privilege(s) and K_g key are configured properly. The <code><a href="/docs/linux/man/8-bmc-config/">bmc-config</a>(8)</code> tool can be used to check and/or change these configuration settings. </p>
<p> Inband IPMI problems are typically caused by improperly configured drivers or non-standard BMCs. </p>
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
<p> &quot;device not found&quot; &#8211; The specified device could not be found. Please check configuration or inputs and try again. </p>
<p> &quot;driver timeout&quot; &#8211; Communication with the driver or device has timed out. Please try again. </p>
<p> &quot;message timeout&quot; &#8211; Communication with the driver or device has timed out. Please try again. </p>
<p> &quot;BMC busy&quot; &#8211; The BMC is currently busy. It may be processing information or have too many simultaneous sessions to manage. Please wait and try again. </p>
<p> &quot;could not find inband device&quot; &#8211; An inband device could not be found. Please check configuration or specify specific device or driver on the command line. </p>
<p> &quot;driver timeout&quot; &#8211; The inband driver has timed out communicating to the local BMC or service processor. The BMC or service processor may be busy or (worst case) possibly non-functioning. </p>
<p> &quot;internal IPMI error&quot; &#8211; An IPMI error has occurred that FreeIPMI does not know how to handle. Please e-mail &lt;freeipmi-users [at] gnu.org&gt; to report the issue. </p>
<p> &quot;sensor config file parse error&quot; &#8211; A parse error was found in the sensor interpretation configuration file. Please see <code><a href="/docs/linux/man/5-freeipmi_interpret_sensor-conf/">freeipmi_interpret_sensor.conf</a>(5).</code></p>
<h2>Workarounds</h2>
<p>With so many different vendors implementing their own IPMI solutions, different vendors may implement their IPMI protocols incorrectly. The following describes a number of workarounds currently available to handle discovered compliance issues. When possible, workarounds have been implemented so they will be transparent to the user. However, some will require the user to specify a workaround be used via the -W option. </p>
<p> The hardware listed below may only indicate the hardware that a problem was discovered on. Newer versions of hardware may fix the problems indicated below. Similar machines from vendors may or may not exhibit the same problems. Different vendors may license their firmware from the same IPMI firmware developer, so it may be worthwhile to try workarounds listed below even if your motherboard is not listed. </p>
<p> If you believe your hardware has an additional compliance issue that needs a workaround to be implemented, please contact the FreeIPMI maintainers on &lt;freeipmi-users [at] gnu.org&gt; or &lt;freeipmi-devel [at] gnu.org&gt;. </p>
<p> <i>assumeio</i> &#8211; This workaround flag will assume inband interfaces communicate with system I/O rather than being memory-mapped. This will work around systems that report invalid base addresses. Those hitting this issue may see &quot;device not supported&quot; or &quot;could not find inband device&quot; errors. Issue observed on HP ProLiant DL145 G1. </p>
<p> <i>spinpoll</i> &#8211; This workaround flag will inform some inband drivers (most notably the KCS driver) to spin while polling rather than putting the process to sleep. This may significantly improve the wall clock running time of tools because an operating system scheduler&#8217;s granularity may be much larger than the time it takes to perform a single IPMI message transaction. However, by spinning, your system may be performing less useful work by not contexting out the tool for a more useful task. </p>
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
<p> <i>assumemaxsdrrecordcount</i> &#8211; This workaround will inform SDR reading to stop reading after a known maximum numer of SDR records have been read. This will work around systems that have mis-implemented SDR reading functions that. Those hitting this issue may see &quot;SDR record count invalid&quot; errors. Issue observed on unspecified Inspur motherboard. </p>
<p> <i>discretereading</i> &#8211; This workaround option will allow analog sensor readings (i.e. rpm, degrees, etc.) to be read even if the event/reading type code for the sensor is for a discrete sensor (i.e. assert vs. deassert). This option works around poorly defined (and arguably illegal) SDR records that expect analog sensor readings to be read alongside discrete sensors. This option is confirmed to work around issues on HP Proliant DL380 G7 and HP ProLiant ML310 G5 motherboards. </p>
<p> <i>ignorescanningdisabled</i> &#8211; This workaround option will allow sensor readings to be read even if the sensor scanning bit indicates a sensor is disabled. This option works around motherboards that incorrectly indicate sensors as disabled. This may problem may exist on your motherboard if sensors are listed as &quot;N/A&quot; even if they should be available. This option is confirmed to work around issues on Dell Poweredge 2900, Dell Poweredge 2950, Dell Poweredge R410, Dell Poweredge R610, and HP Integrity rx3600 motherboards. </p>
<p> <i>assumebmcowner</i> &#8211; This workaround option will allow sensor readings to be read if the sensor owner is the BMC, but the reported sensor owner is not the BMC. Typically, sensors owned by a non-BMC sensor owner must be bridged (e.g. with the <code>&#8211;bridge-sensors</code> option), however if the non-BMC sensor owner is invalid, bridging fails. This option works around motherboards that incorrectly report an non-BMC sensor owner by always assuming the sensor owner is the BMC. This problem may exist on your motherboard if sensors are listed as &quot;N/A&quot; even if they should be available. This option is confirmed to work around issues on Fujitsu RX300 and Fujitsu RX300S2 motherboards. </p>
<p> <i>ignoreauthcode</i> &#8211; This workaround option will allow sensor readings to be read if the remote machine is invalidly calculating authentication codes (i.e. authentication hashes) when communicating over LAN. This problem may exist on your system if the error &quot;session timeout&quot; errors or there is an appearance of a hang. Users are cautioned on the use of this option, as it removes an authentication check verifying the validity of a packet. However, in most organizations, this is unlikely to be a security issue. The ignoring of authentication packets is only limited to the period in which sensor readings are done, and not for any portion of the session authentication or session teardown. This option is confirmed to work on Inventec 5441/Dell Xanadu II and Inventec 5442/Dell Xanadu III. (Note: On the above systems, this issue has only been observed when the <code>&#8211;bridge-sensors</code> is used.) </p>
<p> No IPMI 1.5 Support &#8211; Some motherboards that support IPMI 2.0 have been found to not support IPMI 1.5. Those hitting this issue may see &quot;ipmi 2.0 unavailable&quot; or &quot;connection timeout&quot; errors. This issue can be worked around by using IPMI 2.0 instead of IPMI 1.5 by specifying <code>&#8211;driver-type</code>=<i>LAN_2_0</i>. Issue observed on HP Proliant DL 145.</p>
<h2>Oem Interpretation</h2>
<p>The following motherboards are confirmed to have atleast some support by the <code>&#8211;interpret-oem-data</code> option. While highly probable the OEM data interpretations would work across other motherboards by the same manufacturer, there are no guarantees. Some of the motherboards below may be rebranded by vendors/distributors. </p>
<p> Dell Poweredge R210, Dell Poweredge R610, Dell Poweredge R710, Dell Poweredge R720, Fujitsu iRMC S1 and iRMC S2 systems, HP Proliant DL160 G8, Intel S5500WB/Penguin Computing Relion 700, Intel S2600JF/Appro 512X, Intel S5000PAL, Supermicro X7DBR-3, Supermicro X7DB8, Supermicro X8DTN, Supermicro X7SBI-LN4, Supermicro X8DTH, Supermicro X8DTG, Supermicro X8DTU, Supermicro X8DT3-LN4F, Supermicro X8DTU-6+, Supermicro X8DTL, Supermicro X8DTL-3F, Supermicro X8SIL-F, Supermicro X9SCL, Supermicro X9SCM, Supermicro X8DTN+-F, Supermicro X8SIE, Supermicro X9SCA-F-O, Supermicro H8DGU-F, Supermicro X9DRi-F, Supermicro X9DRI-LN4F+, Supermicro X9SPU-F-O, Supermicro X9SCM-iiF, Wistron/Dell Poweredge C6220.</p>
<h2>Examples</h2>
<p><code># ipmi-sensors</code> Show all sensors and readings on the local machine. <code># ipmi-sensors &#8211;verbose</code> Show verbose sensors and readings on the local machine. <code># ipmi-sensors &#8211;record-ids=7,11,102</code> Show sensor record ids 7, 11, and 102 on the local machine. <code># ipmi-sensors &#8211;sensor-types=fan</code> Show all sensors of type fan on the local machine. <code># ipmi-sensors -h ahost -u myusername -p mypassword</code> Show all sensors on a remote machine using IPMI over LAN. <code># ipmi-sensors -h mycluster[0-127] -u myusername -p mypassword</code> Show all sensors across a cluster using IPMI over LAN. </p>
<h2>Diagnostics</h2>
<p>Upon successful execution, exit status is 0. On error, exit status is 1. </p>
<p> If multiple hosts are specified for communication, the exit status is 0 if and only if all targets successfully execute. Otherwise the exit status is 1.</p>
<h2>Known Issues</h2>
<p>On older operating systems, if you input your username, password, and other potentially security relevant information on the command line, this information may be discovered by other users when using tools like the <code><a href="/docs/linux/man/1-ps/">ps</a>(1)</code> command or looking in the /proc file system. It is generally more secure to input password information with options like the -P or -K options. Configuring security relevant information in the FreeIPMI configuration file would also be an appropriate way to hide this information. </p>
<p> In order to prevent brute force attacks, some BMCs will temporarily &quot;lock up&quot; after a number of remote authentication errors. You may need to wait awhile in order to this temporary &quot;lock up&quot; to pass before you may authenticate again. </p>
<p> Some sensors may be output as not available (i.e. N/A) because the owner of the sensor is not the BMC. To attempt to bridge sensors and access sensors not on the BMC, users may wish to try the <code>-b</code> or <code>&#8211;bridge-sensors</code> options.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;freeipmi-users [at] gnu.org&gt; or &lt;freeipmi-devel [at] gnu.org&gt;.</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2003-2012 FreeIPMI Core Team. </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 3 of the License, or (at your option) any later version.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/7-freeipmi/">freeipmi</a>(7), <a href="/docs/linux/man/8-bmc-config/">bmc-config</a>(8), <a href="/docs/linux/man/8-bmc-device/">bmc-device</a>(8), <a href="/docs/linux/man/8-ipmi-sensors-config/">ipmi-sensors-config</a>(8), <a href="/docs/linux/man/5-freeipmi_interpret_sensor-conf/">freeipmi_interpret_sensor.conf</a>(5) <a rel="nofollow" href="http://www.gnu.org/software/freeipmi/">http://www.gnu.org/software/freeipmi/</a> </p>
