---
title: "snmptrapd-conf(5)"
name: "snmptrapd-conf"
section: "5"
letter: "s"
url: "/docs/linux/man/5-snmptrapd-conf/"
description: "snmptrapd.conf – configuration file for the Net-SNMP notification receiver"
---

<p>snmptrapd.conf &#8211; configuration file for the Net-SNMP notification receiver</p>
<h2>Description</h2>
<p>The Net-SNMP notification receiver (trap daemon) uses one or more configuration files to control its operation and how incoming traps (and INFORM requests) should be processed. This file (<code>snmptrapd.conf</code>) can be located in one of several locations, as described in the <i><a href="/docs/linux/man/5-snmp_config/">snmp_config</a>(5)</i> manual page.</p>
<h2>Important</h2>
<p>Previously, <code>snmptrapd</code> would accept all incoming notifications, and log them automatically (even if no explicit configuration was provided). Starting with release 5.3, access control checks will be applied to incoming notifications. If <code>snmptrapd</code> is run without a suitable configuration file (or equivalent access control settings), then such traps <code>WILL NOT</code> be processed. See the section <code>ACCESS CONTROL</code> for more details. </p>
<p> As with the agent configuration, the <i>snmptrapd.conf</i> directives can be divided into four distinct groups.</p>
<h2>Trapd Behaviour</h2>
<dl>
<dt>snmpTrapdAddr [&lt;transport-specifier&gt;:]&lt;transport-address&gt;[,&#8230;]</p>
<dd>defines a list of listening addresses, on which to receive incoming SNMP notifications. See the section <code>LISTENING ADDRESSES</code> in the <i><a href="/docs/linux/man/8-snmpd/">snmpd</a>(8)</i> manual page for more information about the format of listening addresses.</p>
<dd>The default behaviour is to listen on UDP port 162 on all IPv4 interfaces.</p>
<dt>doNotRetainNotificationLogs yes</p>
<dd>disables support for the NOTIFICATION-LOG-MIB. Normally the snmptrapd program keeps a record of the traps received, which can be retrieved by querying the nlmLogTable and nlmLogvariableTable tables. This directive can be used to suppress this behaviour.</p>
<dd>See the <i><a href="/docs/linux/man/8-snmptrapd/">snmptrapd</a>(8) </i> manual page and the NOTIFICATION-LOG-MIB for details.</p>
<dt>doNotLogTraps yes</p>
<dd>disables the logging of notifications altogether. This is useful if the <code>snmptrapd</code> application should only run traphandle hooks and should not log traps to any location.</p>
<dt>doNotFork yes</p>
<dd>do not fork from the calling shell.</p>
<dt>pidFile PATH</p>
<dd>defines a file in which to store the process ID of the notification receiver. By default, this ID is not saved.</dl>
<h2>Access Control</h2>
<p>Starting with release 5.3, it is necessary to explicitly specify who is authorised to send traps and informs to the notification receiver (and what types of processing these are allowed to trigger). This uses an extension of the VACM model, used in the main SNMP agent. </p>
<p> There are currently three types of processing that can be specified:</p>
<dl>
<dd>
<dl>
<dt>log</p>
<dd>log the details of the notification &#8211; either in a specified file, to standard output (or stderr), or via <i>syslog</i> (or similar).</p>
<dt>execute</p>
<dd>pass the details of the trap to a specified handler program, including embedded perl.</p>
<dt>net</p>
<dd>forward the trap to another notification receiver.</dl>
</dl>
<p> In the following directives, <i>TYPES</i> will be a (comma-separated) list of one or more of these tokens. Most commonly, this will typically be <i>log,execute,net</i> to cover any style of processing for a particular category of notification. But it is perfectly possible (even desirable) to limit certain notification sources to selected processing only.</p>
<dl>
<dt>authCommunity TYPES COMMUNITY [SOURCE [OID | -v VIEW ]]</p>
<dd>authorises traps (and SNMPv2c INFORM requests) with the specified community to trigger the types of processing listed. By default, this will allow any notification using this community to be processed. The SOURCE field can be used to specify that the configuration should only apply to notifications received from particular sources &#8211; see <i><a href="/docs/linux/man/5-snmpd-conf/">snmpd.conf</a>(5)</i> for more details.</p>
<dt>authUser TYPES [-s MODEL] USER [LEVEL [OID | -v VIEW ]]</p>
<dd>authorises SNMPv3 notifications with the specified user to trigger the types of processing listed. By default, this will accept authenticated requests. (<i>authNoPriv</i> or <i>authPriv</i>). The LEVEL field can be used to allow unauthenticated notifications (<i>noauth</i>), or to require encryption (<i>priv</i>), just as for the SNMP agent.</p>
<dd>With both of these directives, the OID (or <i>-v VIEW</i>) field can be used to retrict this configuration to the processing of particular notifications.</p>
<dl>
<dd>
<dl>
<dt>Note:</p>
<dd>Unlike the VACM processing described in RFC 3415, this view is <code>only</code> matched against the snmpTrapOID value of the incoming notification. It is not applied to the payload varbinds held within that notification.</dl>
</dl>
<dt>authGroup TYPES [-s MODEL] GROUP [LEVEL [OID | -v VIEW ]]</p>
<dd>
<dt>authAccess TYPES [-s MODEL] GROUP VIEW [LEVEL [CONTEXT]]</p>
<dd>
<dt>setAccess GROUP CONTEXT MODEL LEVEL PREFIX VIEW TYPES</p>
<dd>authorise notifications in the specified GROUP (configured using the <i>group</i> directive) to trigger the types of processing listed. See <i><a href="/docs/linux/man/5-snmpd-conf/">snmpd.conf</a>(5)</i> for more details.</p>
<dt>createUser [-e ENGINEID] username (MD5|SHA) authpassphrase [DES|AES]</p>
<dd>See the <i><a href="/docs/linux/man/5-snmpd-conf/">snmpd.conf</a>(5)</i> manual page for a description of how to create SNMPv3 users. This is roughly the same, but the file name changes to snmptrapd.conf from snmpd.conf.</p>
<dt>disableAuthorization yes</p>
<dd>will disable the above access control checks, and revert to the previous behaviour of accepting all incoming notifications.</p>
<dd></dl>
<h2>Logging</h2>
<dl>
<dt>format1 FORMAT</p>
<dd>
<dt>format2 FORMAT</p>
<dd>specify the format used to display SNMPv1 TRAPs and SNMPv2 notifications respectively. Note that SNMPv2c and SNMPv3 both use the same SNMPv2 PDU format.</p>
<dd>See <i><a href="/docs/linux/man/8-snmptrapd/">snmptrapd</a>(8)</i> for the layout characters available.</p>
<dt>ignoreAuthFailure yes</p>
<dd>instructs the receiver to ignore <i>authenticationFailure</i> traps.</p>
<dl>
<dd>
<dl>
<dt>Note:</p>
<dd>This currently only affects the logging of such notifications. <i>authenticationFailure</i> traps will still be passed to trap handler scripts, and forwarded to other notification receivers. This behaviour should not be relied on, as it is likely to change in future versions.</dl>
</dl>
<dt>logOption string</p>
<dd>specifies where notifications should be logged &#8211; to standard output, standard error, a specified file or via <i>syslog</i>. See the section LOGGING OPTIONS in the <i><a href="/docs/linux/man/1-snmpcmd/">snmpcmd</a>(1)</i> manual page for details.</p>
<dt>outputOption string</p>
<dd>specifies various characteristics of how OIDs and other values should be displayed. See the section OUTPUT OPTIONS in the <i><a href="/docs/linux/man/1-snmpcmd/">snmpcmd</a>(1)</i> manual page for details.</dl>
<h2>MySQL Logging</h2>
<p>There are two configuration variables that work together to control when queued traps are logged to the MySQL database. A non-zero value must be specified for sqlSaveInterval to enable MySQL logging.</p>
<dl>
<dt>sqlMaxQueue max</p>
<dd>specifies the maximum number of traps to queue before a forced flush to the MySQL database.</p>
<dt>sqlSaveInterval seconds</p>
<dd>specified the number of seconds between periodic queue flushes. A value of 0 for will disable MySQL logging.</dl>
<h2>Notification Processing</h2>
<p>As well as logging incoming notifications, they can also be forwarded on to another notification receiver, or passed to an external program for specialised processing.</p>
<dl>
<dt>traphandle OID|default PROGRAM [ARGS &#8230;]</p>
<dd>invokes the specified program (with the given arguments) whenever a notification is received that matches the OID token. For SNMPv2c and SNMPv3 notifications, this token will be compared against the snmpTrapOID value taken from the notification. For SNMPv1 traps, the generic and specific trap values and the enterprise OID will be converted into the equivalent OID (following RFC 2576).</p>
<dd>Typically, the OID token will be the name (or numeric OID) of a NOTIFICATION-TYPE object, and the specified program will be invoked for notifications that match this OID exactly. However this token also supports a simple form of wildcard suffixing. By appending the character &#8216;*&#8217; to the OID token, the corresponding program will be invoked for any notification based within subtree rooted at the specified OID. For example, an OID token of .1.3.6.1.4.1* would match any enterprise specific notification (including the specified OID itself). An OID token of .1.3.6.1.4.1.* would would work in much the same way, but would not match this exact OID &#8211; just notifications that lay strictly below this root. Note that this syntax does not support full regular expressions or wildcards &#8211; an OID token of the form oid.*.subids is <code>not</code> valid.</p>
<dd>If the OID field is the token <i>default</i> then the program will be invoked for any notification not matching another (OID specific) <i>traphandle</i> entry.</dl>
<p> Details of the notification are fed to the program via its standard input. Note that this will always use the SNMPv2-style notification format, with SNMPv1 traps being converted as per RFC 2576, before being passed to the program. The input format is as follows, one entry per line:</p>
<dl>
<dd>
<dl>
<dt>HOSTNAME</p>
<dd>The name of the host that sent the notification, as determined by <i><a href="/docs/linux/man/3-gethostbyaddr/">gethostbyaddr</a>(3)</i>. </p>
<dt>IPADDRESS</p>
<dd>The IP address of the host that sent the notification.</p>
<dt>VARBINDS</p>
<dd>A list of variable bindings describing the contents of the notification, one per line. The first token on each line (up until a space) is the OID of the varind, and the remainder of the line is its value. The format of both of these are controlled by the <i>outputOption</i> directive (or similar configuration).</p>
<dd>The first OID should always be SNMPv2-MIB::sysUpTime.0, and the second should be SNMPv2-MIB::snmpTrapOID.0. The remaining lines will contain the payload varbind list. For SNMPv1 traps, the final OID will be SNMPv2-MIB::snmpTrapEnterprise.0. </p>
<dt>Example:</p>
<dd>A <code>traptoemail</code> script has been included in the Net-SNMP package that can be used within a <i>traphandle</i> directive: </p>
<dl>
<dd>traphandle default /usr/bin/perl /usr/bin/traptoemail -s mysmtp.somewhere.com -f admin [at] somewhere.com me [at] somewhere.com</dl>
</dl>
</dl>
<dl>
<dt>forward OID|default DESTINATION</p>
<dd>forwards notifications that match the specified OID to another receiver listening on DESTINATION. The interpretation of OID (and <i>default</i>) is the same as for the <i>traphandle</i> directive).</p>
<dd>See the section <code>LISTENING ADDRESSES</code> in the <i><a href="/docs/linux/man/8-snmpd/">snmpd</a>(8)</i> manual page for more information about the format of listening addresses.</dl>
<h2>Notes</h2>
<dl>
<dt>o</p>
<dd>The daemon blocks while executing the <i>traphandle</i> commands. (This should be fixed in the future with an appropriate signal catch and wait() combination).</p>
<dt>o</p>
<dd>All directives listed with a value of &quot;yes&quot; actually accept a range of boolean values. These will accept any of <i>1</i>, <i>yes</i> or <i>true</i> to enable the corresponding behaviour, or any of <i>0</i>, <i>no</i> or <i>false</i> to disable it. The default in each case is for the feature to be turned off, so these directives are typically only used to enable the appropriate behaviour.</dl>
<h2>Files</h2>
<p>/etc/snmp/snmptrapd.conf</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/5-snmp_config/">snmp_config</a>(5), <a href="/docs/linux/man/8-snmptrapd/">snmptrapd</a>(8), <a href="/docs/linux/man/8-syslog/">syslog</a>(8), <a href="/docs/linux/man/5-variables/">variables</a>(5), <a href="/docs/linux/man/5-snmpd-conf/">snmpd.conf</a>(5), <a href="/docs/linux/man/3-netsnmp_config_api/">netsnmp_config_api</a>(3). </p>
