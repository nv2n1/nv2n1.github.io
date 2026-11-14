---
title: "check_openmanage(8)"
name: "check_openmanage"
section: "8"
letter: "c"
url: "/docs/linux/man/8-check_openmanage/"
description: "check_openmanage – Nagios plugin for checking the hardware status on Dell servers running OpenManage"
---

<p>check_openmanage &#8211; Nagios plugin for checking the hardware status on Dell servers running OpenManage</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>check_openmanage</code> [<i>option</i>&#8230;]</p>
<dt> <code>check_openmanage</code> -H&nbsp;<wbr><i>hostname</i> [<i>option</i>&#8230;]</dl>
<h2>Description</h2>
<p><code>check_openmanage</code></p>
<dd>is a plugin for Nagios which checks the hardware health of Dell servers running OpenManage Server Administrator (OMSA). The plugin checks the health of the storage subsystem, power supplies, memory modules, temperature probes etc., and gives an alert if any of the components are faulty or operate outside normal parameters. </p>
<p> <code>check_openmanage</code> is designed to be used by either locally (using NRPE or similar) or remotely (using SNMP). In either mode, the output is (nearly) the same. Note that checking the alert log is not supported in SNMP mode.</p>
<h2>General Options</h2>
<p><code>-f</code>, <code>&#8211;config </code><i>file</i></p>
<dl>
<dd>Specify a configuration file. For reference on the config file syntax and options, consult the <code><a href="/docs/linux/man/5-check_openmanage-conf/">check_openmanage.conf</a></code>(5) manual page.</dl>
<p> <code>-t</code>, <code>&#8211;timeout </code><i>seconds</i></p>
<dl>
<dd>The number of seconds after which the plugin will abort. Default timeout is 30 seconds if the option is not present.</dl>
<p> <code>-p</code>, <code>&#8211;perfdata</code> [<i>argument</i>]</p>
<dl>
<dd>Collect performance data. Performance data collected include temperatures (in Celsius) and fan speeds (in rpm). On systems that support it, power consumption is also collected (in Watts). This option takes one of two arguments, both of which are optional: </p>
<p> <i>minimal</i></p>
<dl>
<dd>If <i>minimal</i> is specified as argument, the plugin will use shorter names for the performance data labels, e.g. &#8220;t0&#8221; instead of &#8220;temp_0_system_board_ambient&#8221;. This can be used as a workaround in cases where the plugin output needs shortening, for example if the 1024 character limit of NRPE is reached.</dl>
<p> <i>multiline</i></p>
<dl>
<dd>If <i>multiline</i> is specified as argument, the plugin will output the performance data on multiple lines, for Nagios 3.x and above.</dl>
<p> The default behaviour should be sufficient for most users.</dl>
<p> <code>&#8211;legacy-perfdata</code></p>
<dl>
<dd>With version 3.7.0, performance data output changed. The new format is not compatible with the old format. Users who wish to postpone switching to the new performance data API may set this option.</dl>
<p> <code>-w</code>, <code>&#8211;warning</code> <i>string</i> | <i>file</i></p>
<dl>
<dd>Override the machine-default temperature warning thresholds. Syntax is: </p>
<dl>
<dd>
<pre><i>id1</i>=<i>max</i>[/<i>min</i>],<i>id2</i>=<i>max</i>[/<i>min</i>],...</pre>
</dl>
<p> The following example sets warning limits to max 50C for probe 0, and max 45C and min 10C for probe 1: </p>
<dl>
<dd>
<pre>check_openmanage -w 0=50,1=45/10</pre>
</dl>
<p> The minimum limit can be omitted, if desired. Most often, you are only interested in setting the maximum thresholds. </p>
<p> This parameter can be either a string with the limits, or a file containing the limits string. The option can be specified multiple times. </p>
<p> <i>NOTE</i>: This option should only be used to narrow the field of OK temperatures wrt. the OMSA defaults. To expand the field of OK temperatures, increase the OMSA thresholds. See the plugin web page for more information.</dl>
<p> <code>-c</code>, <code>&#8211;critical</code> <i>string</i> | <i>file</i></p>
<dl>
<dd>Override the machine-default temperature critical thresholds. Syntax and behaviour is the same as for warning thresholds described above.</dl>
<p> <code>-F</code>, <code>&#8211;fahrenheit</code></p>
<dl>
<dd>Set Fahrenheit as unit for all temperatures. This option will override the <code>&#8211;tempunit</code> option, if used simultaneously.</dl>
<p> <code>&#8211;tempunit</code> <i>unit</i></p>
<dl>
<dd>Set temperature unit. Legal values are: </p>
<p> <i>F</i>: Fahrenheit </p>
<p> <i>C</i>: Celsius </p>
<p> <i>K</i>: Kelvin </p>
<p> <i>R</i>: Rankine </p>
<p> Default: C</dl>
<p> <code>&#8211;omreport</code> <i>path</i></p>
<dl>
<dd>Specify full path to omreport, if it is not installed in any of the regular places. Usually this option is only needed on Windows, if omreport is not installed on the C: drive.</dl>
<p> <code>&#8211;vdisk-critical</code></p>
<dl>
<dd>Make any alerts concerning virtual disks appear as critical.</dl>
<p> <code>-d</code>, <code>&#8211;debug</code></p>
<dl>
<dd>Debug output. Will report status on everything, even if status is ok. Blacklisted or unchecked components are ignored (i.e. no output). </p>
<p> <i>NOTE</i>: This option is intended for diagnostics and debugging purposes only. Do not use this option from within Nagios, i.e. in the Nagios config.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dd>Display help message and exit.</dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dd>Print version info and exit.</dl>
<h2>Output Options</h2>
<p><code>-o</code>, <code>&#8211;ok-info</code> <i>level</i></p>
<dl>
<dd>This option lets you define how much output you want the plugin to give when everything is OK, i.e. the verbosity level. The default value is 0 (one line of output). The output levels are cumulative. </p>
<p> <i>0</i>: Only one line </p>
<p> <i>1</i>: BIOS and firmware info on a separate line </p>
<p> <i>2</i>: Storage controller and enclosure info on separate lines </p>
<p> <i>3</i>: OMSA version on separate line </p>
<p> Default: 0 </p>
<p> The reason that OMSA version is separated from the rest is that finding it requires running a really slow omreport command, when the plugin is run locally via NRPE.</dl>
<p> <code>-B</code>, <code>&#8211;show-blacklist</code></p>
<dl>
<dd>If used together with blacklisting, this option will make the plugin output all blacklistings that are being used. The output will have the correct blacklisting syntax, and will make it easy to maintain control over which blacklistings that are used for each server, as any blacklistings can be viewed from Nagios. </p>
<p> When blacklisting is not used, this option has no effect.</dl>
<p> <code>-i</code>, <code>&#8211;info</code></p>
<dl>
<dd>Prefix any alerts with the service tag.</dl>
<p> <code>-e</code>, <code>&#8211;extinfo</code></p>
<dl>
<dd>Display a short summary of system information (model and service tag) in case of an alert.</dl>
<p> <code>-I</code>, <code>&#8211;htmlinfo</code> [<i>code</i>]</p>
<dl>
<dd>Using this option will make the servicetag and model name into clickable HTML links in the output. The model name link will point to the official Dell documentation for that model, while the servicetag link will point to a website containing support info for that particular server. </p>
<p> This option takes an optional argument, which should be a country or area code or. If the country code is omitted the servicetag link will still work, but it will not be speficic for your country or area. Example for Germany: </p>
<dl>
<dd>
<pre>check_openmanage --htmlinfo de</pre>
</dl>
<p> If this option is used together with either the <code>&#8211;extinfo</code> or <code>&#8211;info</code> options, it is particularly useful. Only the most common country codes is supported at this time: </p>
<table>
<tr VALIGN=top>
<td COLSPAN=3> Europe, Middle East and Africa (EMEA)
</td>
</tr>
<tr VALIGN=top>
<td> <i>at</i>: Austria </td>
<td> <i>be</i>: Belgium </td>
<td> <i>cz</i>: Czech Republic
</td>
</tr>
<tr VALIGN=top>
<td> <i>de</i>: Germany </td>
<td> <i>dk</i>: Denmark </td>
<td> <i>es</i>: Spain
</td>
</tr>
<tr VALIGN=top>
<td> <i>fi</i>: Finland </td>
<td> <i>fr</i>: France </td>
<td> <i>gr</i>: Greece
</td>
</tr>
<tr VALIGN=top>
<td> <i>it</i>: Italy </td>
<td> <i>il</i>: Israel </td>
<td> <i>me</i>: Middle East
</td>
</tr>
<tr VALIGN=top>
<td> <i>no</i>: Norway </td>
<td> <i>nl</i>: The Netherlands </td>
<td> <i>pl</i>: Poland
</td>
</tr>
<tr VALIGN=top>
<td> <i>pt</i>: Portugal </td>
<td> <i>ru</i>: Russia </td>
<td> <i>se</i>: Sweden
</td>
</tr>
<tr VALIGN=top>
<td> <i>uk</i>: United Kingdom </td>
<td> <i>za</i>: South Africa </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3> &nbsp;<wbr>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3> America
</td>
</tr>
<tr VALIGN=top>
<td> <i>br</i>: Brazil </td>
<td> <i>ca</i>: Canada </td>
<td> <i>mx</i>: Mexico
</td>
</tr>
<tr VALIGN=top>
<td> <i>us</i>: USA </td>
<td>
</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3> &nbsp;<wbr>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3> Asia / Pacific
</td>
</tr>
<tr VALIGN=top>
<td> <i>au</i>: Australia </td>
<td> <i>cn</i>: China </td>
<td> <i>in</i>: India
</td>
</tr>
<tr VALIGN=top>
<td> <i>jp</i>: Japan </td>
<td>
</td>
<td>
</td>
</tr>
</table>
</dl>
<p> <code>&#8211;postmsg</code> <i>string</i> | <i>file</i></p>
<dl>
<dd>User specified post message. Useful for displaying arbitrary or various system information at the end of alerts. The argument is either a string with the message, or a file containing that string. You can control the format with the following interpreted sequences: </p>
<p> <i>%m</i>: System model </p>
<p> <i>%s</i>: Service tag </p>
<p> <i>%b</i>: BIOS version </p>
<p> <i>%d</i>: BIOS release date </p>
<p> <i>%o</i>: Operating system name </p>
<p> <i>%r</i>: Operating system release </p>
<p> <i>%p</i>: Number of physical drives </p>
<p> <i>%l</i>: Number of logical drives </p>
<p> <i>%n</i>: Line break. Will be a regular line break if run from a TTY, else an HTML line break. </p>
<p> <i>%%</i>: A literal &#8220;%&#8221;</dl>
<p> <code>-s</code>, <code>&#8211;state</code></p>
<dl>
<dd>Prefix each alert with its corresponding service state (i.e. warning, critical etc.). This is useful in case of several alerts from the same monitored system.</dl>
<p> <code>-S</code>, <code>&#8211;short-state</code></p>
<dl>
<dd>Same as the <code>&#8211;state</code> option above, except that the state is abbreviated to a single letter (<i>W</i>=warning, <i>C</i>=critical etc.).</dl>
<p> <code>&#8211;hide-servicetag</code></p>
<dl>
<dd>This option will replace the servicetag (serial number) in the output with &#8220;XXXXXXX&#8221;. Use this option to suppress or censor the servicetag in the plugin output.</dl>
<p> <code>&#8211;linebreak</code> <i>string</i></p>
<dl>
<dd>check_openmanage will sometimes report more than one line, e.g. if there are several alerts. If the script has a TTY, it will use regular linebreaks. If not (which is the case with NRPE) it will use HTML linebreaks. Sometimes it can be useful to control what the plugin uses as a line separator, and this option provides that control. </p>
<p> The argument is the exact string to be used as the line separator. There are two exceptions, i.e. two keywords that translates to the following: </p>
<p> <i>REG</i>: Regular linebreaks, i.e. &#8220;
&#8221;. </p>
<p> <i>HTML</i>: HTML linebreaks, i.e. &#8220;&lt;br/&gt;&#8221;. </p>
<p> This is a rather special option that is normally not needed. The default behaviour should be sufficient for most users.</dl>
<h2>Snmp Options</h2>
<p><code>-H</code>, <code>&#8211;hostname </code><i>hostname</i></p>
<dl>
<dd>The transport address of the destination SNMP device. Using this option triggers SNMP mode.</dl>
<p> <code>-P</code>, <code>&#8211;protocol</code> <i>protocol-number</i></p>
<dl>
<dd>SNMP protocol version. This option is optional and expects either of the following: </p>
<p> <i>1</i>: SNMP version 1 </p>
<p> <i>2</i>, <i>2c</i>: SNMP version 2c </p>
<p> <i>3</i>: SNMP version 3 </p>
<p> Default: 2c</dl>
<p> <code>&#8211;port</code> <i>port-number</i></p>
<dl>
<dd>SNMP port of the remote (monitored) system. Defaults to the well-known SNMP port 161.</dl>
<p> <code>-6</code>, <code>&#8211;ipv6</code></p>
<dl>
<dd>This option will cause the plugin to use IPv6. The default is IPv4 if the option is not present.</dl>
<p> <code>&#8211;tcp</code></p>
<dl>
<dd>This option will cause the plugin to use TCP as transport protocol. The default is UDP if the option is not present.</dl>
<p> <code>&#8211;snmp-timeout</code> <i>seconds</i></p>
<dl>
<dd>This option sets the timeout for the SNMP object of the Net::SNMP perl module. Legal values are between 1 and 60 seconds, and the default is 5 seconds if the option is not present. Note that there is one retry (with the same timeout) before the SNMP object times out completely. For an unresponsive SNMP server, you&#8217;ll see that the plugin times out with an SNMP error after 10 seconds if the 5 second default is used. </p>
<p> This option is usually not needed. The default timeout of 5 seconds is more than sufficient in most cases.</dl>
<p> <code>-U</code>, <code>&#8211;username</code> <i>securityname</i></p>
<dl>
<dd>[SNMPv3] The User-based Security Model (USM) used by SNMPv3 requires that a securityName be specified. This option is required when using SNMP version 3, and expects a string 1 to 32 octets in lenght.</dl>
<p> <code>&#8211;authpassword</code> <i>password</i>, <code>&#8211;authkey</code> <i>key</i></p>
<dl>
<dd>[SNMPv3] By default a securityLevel of <i>noAuthNoPriv</i> is assumed. If the <code>&#8211;authpassword</code> option is specified, the securityLevel becomes <i>authNoPriv</i>. The <code>&#8211;authpassword</code> option expects a string which is at least 1 octet in length as argument. </p>
<p> Optionally, instead of the <code>&#8211;authpassword</code> option, the <code>&#8211;authkey</code> option can be used so that a plain text password does not have to be specified in a script. The <code>&#8211;authkey</code> option expects a hexadecimal string produced by localizing the password with the authoritativeEngineID for the specific destination device. The <code>snmpkey</code> utility included with the Net::SNMP distribution can be used to create the hexadecimal string. See <code><a href="/docs/linux/man/1-snmpkey/">snmpkey</a></code>(1) for more information.</dl>
<p> <code>&#8211;authprotocol</code> <i>algorithm</i></p>
<dl>
<dd>[SNMPv3] Two different hash algorithms are defined by SNMPv3 which can be used by the Security Model for authentication. These algorithms are HMAC-MD5-96 &#8220;MD5&#8221; (RFC 1321) and HMAC-SHA-96 &#8220;SHA-1&#8221; (NIST FIPS PUB 180-1). The default algorithm used by the plugin is HMAC-MD5-96. This behavior can be changed by using this option. The option expects either the string <i>md5</i> or <i>sha</i> to be passed as argument to modify the hash algorithm.</dl>
<p> <code>&#8211;privpassword</code> <i>password</i>, <code>&#8211;privkey</code> <i>key</i></p>
<dl>
<dd>[SNMPv3] By specifying the options <code>&#8211;privkey</code> or <code>&#8211;privpassword</code>, the securityLevel associated with the object becomes <i>authPriv</i>. According to SNMPv3, privacy requires the use of authentication. Therefore, if either of these two options are present and the <code>&#8211;authkey</code> or <code>&#8211;authpassword</code> arguments are missing, the creation of the object fails. The <code>&#8211;privkey</code> and <code>&#8211;privpassword</code> options expect the same input as the <code>&#8211;authkey</code> and <code>&#8211;authpassword</code> options respectively.</dl>
<p> <code>&#8211;privprotocol</code> <i>algorithm</i></p>
<dl>
<dd>[SNMPv3] The User-based Security Model described in RFC 3414 defines a single encryption protocol to be used for privacy. This protocol, CBC-DES &#8220;DES&#8221; (NIST FIPS PUB 46-1), is used by default or if the string <i>des</i> is passed to the <code>&#8211;privprotocol</code> option. The Net::SNMP module also supports RFC 3826 which describes the use of CFB128-AES-128 &#8220;AES&#8221; (NIST FIPS PUB 197) in the USM. The AES encryption protocol can be selected by passing <i>aes</i> or <i>aes128</i> to the <code>&#8211;privprotocol</code> option. </p>
<p> One of the following arguments are required: des, aes, aes128, 3des, 3desde</dl>
<p> <code>&#8211;use-get_table</code></p>
<dl>
<dd>This option exists as a workaround when using check_openmanage with SNMPv3 on Windows with net-snmp. Using this option will make check_openmanage use the Net::SNMP function get_table() instead of get_entries() while fetching values via SNMP. The latter is faster and is the default.</dl>
<h2>Blacklisting</h2>
<p><code>-b</code>, <code>&#8211;blacklist</code> <i>string</i> | <i>file</i></p>
<dl>
<dd>Blacklist missing and/or failed components, if you do not plan to fix them. The parameter is either the blacklist string, or a file (that may or may not exist) containing the string. The blacklist string contains component names with component IDs separated by slash &#8220;/&#8221;. Blacklisted components are left unchecked. </p>
<p> <i>TIP</i>: Use the option <code>-d</code> or <code>&#8211;debug</code> to get the blacklist ID for devices. The ID is listed in a separate column in the debug output. </p>
<p> <i>NOTE</i>: If blacklisting is in effect, the global health of the system is not checked. </p>
<p> Syntax: </p>
<dl>
<dd>
<pre><i>component1</i>=<i>id1</i>[,<i>id2</i>,...]/<i>component2</i>=<i>id1</i>[,<i>id2</i>,...]/...</pre>
</dl>
<p> The ID part can also be &#8220;all&#8221;, in which all components of that type is blacklisted. </p>
<p> Example: </p>
<dl>
<dd>
<pre>check_openmanage -b ps=0/fan=3,5/pdisk=1:0:0:1/ctrl_driver=all</pre>
</dl>
<p> In the example we blacklist powersupply 0, fans 3 and 5, physical disk 1:0:0:1, and warnings about out-of-date drivers for all controllers. Legal component names include: </p>
<p> <i>ctrl</i></p>
<dl>
<dd>Storage controller. Note that if a controller is blacklisted, all components on that controller (such as physical and logical drives) are blacklisted as well.</dl>
<p> <i>ctrl_fw</i></p>
<dl>
<dd>Suppress the special warning message about old controller firmware. Use this if you can not or will not upgrade the firmware.</dl>
<p> <i>ctrl_driver</i></p>
<dl>
<dd>Suppress the special warning message about old controller driver. Particularly useful on systems where you can not upgrade the driver.</dl>
<p> <i>ctrl_stdr</i></p>
<dl>
<dd>Suppress the special warning message about old Storport driver on Windows.</dl>
<p> <i>ctrl_pdisk</i></p>
<dl>
<dd>This blacklisting keyword exists as a possible workaround for physical drives with bad firmware which makes Openmanage choke. It takes the controller number as argument. Use this option to blacklist all physical drives on a specific controller. This blacklisting keyword is only available in local mode, i.e. not with SNMP.</dl>
<p> <i>pdisk</i></p>
<dl>
<dd>Physical disk.</dl>
<p> <i>pdisk_cert</i></p>
<dl>
<dd>Suppress warning message about non-certified physical disk.</dl>
<p> <i>pdisk_foreign</i></p>
<dl>
<dd>Suppress warning message about foreign physical disk.</dl>
<p> <i>vdisk</i></p>
<dl>
<dd>Logical drive (virtual disk).</dl>
<p> <i>bat</i></p>
<dl>
<dd>Controller cache battery.</dl>
<p> <i>bat_charge</i></p>
<dl>
<dd>Ignore warnings related to the controller cache battery charging cycle, which happens approximately every 40-90 days on Dell servers. Note that using this blacklist keyword makes check_openmanage ignore non-critical cache battery errors.</dl>
<p> <i>conn</i></p>
<dl>
<dd>Connector (channel).</dl>
<p> <i>encl</i></p>
<dl>
<dd>Storage enclosure.</dl>
<p> <i>encl_fan</i></p>
<dl>
<dd>Enclosure fan.</dl>
<p> <i>encl_ps</i></p>
<dl>
<dd>Enclosure power supply.</dl>
<p> <i>encl_temp</i></p>
<dl>
<dd>Enclosure temperature probe.</dl>
<p> <i>encl_emm</i></p>
<dl>
<dd>Enclosure management module (EMM).</dl>
<p> <i>dimm</i></p>
<dl>
<dd>Memory module.</dl>
<p> <i>fan</i></p>
<dl>
<dd>Chassis fan.</dl>
<p> <i>ps</i></p>
<dl>
<dd>Power supply.</dl>
<p> <i>temp</i></p>
<dl>
<dd>Temperature sensor.</dl>
<p> <i>cpu</i></p>
<dl>
<dd>Processor (CPU).</dl>
<p> <i>volt</i></p>
<dl>
<dd>Voltage probe.</dl>
<p> <i>bp</i></p>
<dl>
<dd>System battery.</dl>
<p> <i>amp</i></p>
<dl>
<dd>Amperage probe (power consumption monitoring).</dl>
<p> <i>intr</i></p>
<dl>
<dd>Intrusion detection sensor.</dl>
<p> <i>sd</i></p>
<dl>
<dd>SD card</dl>
</dl>
<h2>Check Control</h2>
<p><code>&#8211;no-storage</code></p>
<dl>
<dd>Turn off storage checking. This is an alias for &#8220;&#8211;check storage=0&#8221;.</dl>
<p> <code>&#8211;only</code> <i>keyword</i></p>
<dl>
<dd>Makes check_openmanage check and/or report on a single class of components or warning level. This option can be specifed once and expects an argument. The different arguments and the corresponding behaviour are described below. </p>
<p> <i>critical</i></p>
<dl>
<dd>Print only critical alerts. With this option any warning alerts are suppressed.</dl>
<p> <i>warning</i></p>
<dl>
<dd>Print only warning alerts. With this option any critical alerts are suppressed.</dl>
<p> <i>chassis</i></p>
<dl>
<dd>Check all chassis components and nothing else.</dl>
<p> <i>storage</i></p>
<dl>
<dd>Only check storage</dl>
<p> <i>memory</i></p>
<dl>
<dd>Only check memory modules</dl>
<p> <i>fans</i></p>
<dl>
<dd>Only check fans</dl>
<p> <i>power</i></p>
<dl>
<dd>Only check power supplies</dl>
<p> <i>temp</i></p>
<dl>
<dd>Only check temperatures</dl>
<p> <i>cpu</i></p>
<dl>
<dd>Only check processors</dl>
<p> <i>voltage</i></p>
<dl>
<dd>Only check voltage probes</dl>
<p> <i>batteries</i></p>
<dl>
<dd>Only check batteries</dl>
<p> <i>amperage</i></p>
<dl>
<dd>Only check power usage</dl>
<p> <i>intrusion</i></p>
<dl>
<dd>Only check chassis intrusion</dl>
<p> <i>sdcard</i></p>
<dl>
<dd>Only check SD cards</dl>
<p> <i>esmhealth</i></p>
<dl>
<dd>Only check ESM log overall health, i.e. fill grade</dl>
<p> <i>servicetag</i></p>
<dl>
<dd>Only check for sane service tag</dl>
<p> <i>esmlog</i></p>
<dl>
<dd>Only check the event log (ESM) content</dl>
<p> <i>alertlog</i></p>
<dl>
<dd>Only check the alert log content</dl>
</dl>
<p> <code>&#8211;check</code> <i>string</i> | <i>file</i></p>
<dl>
<dd>This parameter allows you to adjust which components that should be checked at all. This is a rougher approach than blacklisting, which require that you specify component id or index. The parameter should be either a string containing the adjustments, or a file containing the string. No errors are raised if the file does not exist. </p>
<p> Example: </p>
<dl>
<dd>
<pre>check_openmanage --check storage=0,intrusion=1</pre>
</dl>
<p> Legal values are described below, along with the default value. </p>
<p> <i>storage</i></p>
<dl>
<dd>Check storage subsystem (controllers, disks etc.). Default: ON</dl>
<p> <i>memory</i></p>
<dl>
<dd>Check memory (dimms). Default: ON</dl>
<p> <i>fans</i></p>
<dl>
<dd>Check chassis fans. Default: ON</dl>
<p> <i>power</i></p>
<dl>
<dd>Check power supplies. Default: ON</dl>
<p> <i>temp</i></p>
<dl>
<dd>Check temperature sensors. Default: ON</dl>
<p> <i>cpu</i></p>
<dl>
<dd>Check CPUs. Default: ON</dl>
<p> <i>voltage</i></p>
<dl>
<dd>Check voltage sensors. Default: ON</dl>
<p> <i>batteries</i></p>
<dl>
<dd>Check system batteries. Default: ON</dl>
<p> <i>amperage</i></p>
<dl>
<dd>Check amperage probes. Default: ON</dl>
<p> <i>intrusion</i></p>
<dl>
<dd>Check chassis intrusion. Default: ON</dl>
<p> <i>sdcard</i></p>
<dl>
<dd>Check SD cards. Default: ON</dl>
<p> <i>esmhealth</i></p>
<dl>
<dd>Check the ESM log health, i.e. fill grade. Default: ON</dl>
<p> <i>servicetag</i></p>
<dl>
<dd>Check that the service tag (serial number) is sane and not empty. Default: ON</dl>
<p> <i>esmlog</i></p>
<dl>
<dd>Check the ESM log content. Default: OFF</dl>
<p> <i>alertlog</i></p>
<dl>
<dd>Check the alert log content. Default: OFF</dl>
</dl>
<h2>Diagnostics</h2>
<p>The option <code>-d</code> or <code>&#8211;debug</code> can be specified to display all monitored components.</p>
<h2>Exit Status</h2>
<p>If no errors are discovered, a value of 0 (OK) is returned. An exit value of 1 (WARNING) signifies one or more non-critical errors, while 2 (CRITICAL) signifies one or more critical errors. </p>
<p> The exit value 3 (UNKNOWN) is reserved for errors within the script, or errors getting values from Dell OMSA.</p>
<h2>Bugs And Limitations</h2>
<p>Storage info is not collected or checked on very old PowerEdge models and/or old OMSA versions, due to limitations in OMSA. The overall support on those models/versions by this plugin is not well tested.</p>
<h2>License And Copyright</h2>
<p>This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with this program. If not, see <a rel="nofollow" href="http://www.gnu.org/licenses/.">http://www.gnu.org/licenses/.</a></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-check_openmanage-conf/">check_openmanage.conf</a></code>(5), <code><a href="/docs/linux/man/3-net--snmp/">Net::SNMP</a></code>(3), <a rel="nofollow" href="http://folk.uio.no/trondham/software/check_openmanage.html">http://folk.uio.no/trondham/software/check_openmanage.html</a></p>
<h2>Authors</h2>
<p><code>Trond Hasle Amundsen &lt;t.h.amundsen [at] usit.uio.no&gt;</code></p>
