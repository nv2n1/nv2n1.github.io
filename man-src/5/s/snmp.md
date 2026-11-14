---
title: "snmp(5)"
name: "snmp"
section: "5"
letter: "s"
url: "/docs/linux/man/5-snmp/"
description: "snmp.conf – configuration files for the Net-SNMP applications"
---

<p>snmp.conf &#8211; configuration files for the Net-SNMP applications</p>
<h2>Description</h2>
<p>Applications built using the Net-SNMP libraries typically use one or more configuration files to control various aspects of their operation. These files (<code>snmp.conf</code> and <code>snmp.local.conf</code>) can be located in one of several locations, as described in the <i><a href="/docs/linux/man/5-snmp_config/">snmp_config</a>(5)</i> manual page. </p>
<p> In particular, /etc/snmp/snmp.conf is a common file, containing the settings shared by all users of the system. ~/.snmp/snmp.conf is a personal file, with the settings specific to a particular user.</p>
<h2>Host-Specific Files</h2>
<p>Host-specific files may also be loaded and will be searched for if a transport name is specified that matches a <i>PATH/hosts/HOST.conf</i> file. For example, if you wanted a particular host to use SNMPv2c by default you could create a ~/.snmp/hosts/NAME.conf file and in it put:</p>
<dl>
<dd>defVersion 2c</dl>
<p> Any connections set to connect to the hostname <i>NAME</i> will use SNMPv2c. Also see the <i>transport</i> token below for additional host-specific examples. </p>
<p> Host-specific configuration files are loaded at the time the connection is opened. Thus they&#8217;re generally loaded after all other configuration files and can be used to override settings from the generic files. </p>
<p> To avoid loading any host-specific config files set &quot;dontLoadHostConfig true&quot; in your snmp.conf file.</p>
<h2>Command-Line Options</h2>
<p>All of the tokens described in this file can be used on the command line of Net-SNMP applications as well by prefixing them with &quot;&#8211;&quot;. EG, specifying <i>&#8211;dontLoadHostConfig=true</i> on the command line will turn of loading of the host specific configuration files.</p>
<h2>Important Note</h2>
<p>Several of these directives may contain sensitive information (such as pass phrases). Configuration files that include such settings should only be readable by the user concerned. </p>
<p> As well as application-specific configuration tokens, there are several directives that relate to standard library behaviour, relevant to most Net-SNMP applications. Many of these correspond to standard command-line options, which are described in the <i><a href="/docs/linux/man/1-snmpcmd/">snmpcmd</a>(1)</i> manual page. </p>
<p> These directives can be divided into several distinct groups.</p>
<h2>Client Behaviour</h2>
<dl>
<dt>defDomain application domain</p>
<dd>The transport domain that should be used for a certain application type unless something else is specified.</p>
<dt>defTarget application domain target</p>
<dd>The target that should be used for connections to a certain application if the connection should be in a specific domain.</p>
<dt>defaultPort PORT</p>
<dd>defines the default UDP port that client SNMP applications will attempt to connect to. This can be overridden by explicitly including a port number in the <i>AGENT</i> specification. See the <i><a href="/docs/linux/man/1-snmpcmd/">snmpcmd</a>(1)</i> manual page for more details.</p>
<dd>If not specified, the default value for this token is 161.</p>
<dt>transport HOSTSPECIFIER</p>
<dd>This special token should go into a hostname-specific configuration file in a <i>hosts</i> sub-directory. For example if the file <i>hosts/foo.conf</i> exists in the search path it will be loaded if a transport name of <i>foo</i> was used. Within the foo.conf file you may put both general snmp.conf settings as well as a special <i>transport</i> string to specify the destination to connect to. For example, putting:</p>
<dl>
<dd>
<dl>
<dd>transport tcp:foo.example.com:9876</dl>
</dl>
<dd>in the <i>hosts/foo.conf</i> file will make applications referencing the <i>foo</i> hostname (e.g. <i>snmpget</i>) to actually connect via TCP to <i>foo.exmaple.com</i> on port 9876.</p>
<dt>defVersion (1|2c|3)</p>
<dd>defines the default version of SNMP to use. This can be overridden using the <code>-v</code> option.</p>
<dt>defCommunity STRING</p>
<dd>defines the default community to use for SNMPv1 and SNMPv2c requests. This can be overridden using the <code>-c</code> option.</p>
<dt>alias NAME DEFINITION</p>
<dd>Creates an aliased tied to NAME for a given transport definition. The alias can the be referred to using an alias: prefix. Eg, a line of &quot;alias here udp:127.0.0.1:6161&quot; would allow you to use a destination host of &quot;alias:here&quot; instead of &quot;udp:127.0.0.1:6161&quot;. This becomes more useful with complex transport addresses involving IPv6 addresses, etc.</p>
<dt>dumpPacket yes</p>
<dd>defines whether to display a hexadecimal dump of the raw SNMP requests sent and received by the application. This is equivalent to the <code>-d</code> option.</p>
<dt>doDebugging (1|0)</p>
<dd>turns on debugging for all applications run if set to 1.</p>
<dt>debugTokens TOKEN[,TOKEN&#8230;]</p>
<dd>defines the debugging tokens that should be turned on when <i>doDebugging</i> is set. This is equivalent to the <code>-D</code> option.</p>
<dt>16bitIDs yes</p>
<dd>restricts requestIDs, etc to 16-bit values.</p>
<dd>The SNMP specifications define these ID fields as 32-bit quantities, and the Net-SNMP library typically initialises them to random values for security. However certain (broken) agents cannot handle ID values greater than 2^16 &#8211; this option allows interoperability with such agents.</p>
<dt>clientaddr [&lt;transport-specifier&gt;:]&lt;transport-address&gt;</p>
<dd>specifies the source address to be used by command-line applications when sending SNMP requests. See <i><a href="/docs/linux/man/1-snmpcmd/">snmpcmd</a>(1)</i> for more information about the format of addresses.</p>
<dd>This value is also used by <code>snmpd</code> when generating notifications.</p>
<dt>clientRecvBuf INTEGER</p>
<dd>specifies the desired size of the buffer to be used when receiving responses to SNMP requests. If the OS hard limit is lower than the <i>clientRecvBuf</i> value, then this will be used instead. Some platforms may decide to increase the size of the buffer actually used for internal housekeeping.</p>
<dd>This directive will be ignored if the platforms does not support <i>setsockopt()</i>.</p>
<dt>clientSendBuf INTEGER</p>
<dd>is similar to <i>clientRecvBuf</i>, but applies to the size of the buffer used when sending SNMP requests.</p>
<dt>noRangeCheck yes</p>
<dd>disables the validation of varbind values against the MIB definition for the relevant OID. This is equivalent to the <code>-Ir</code> option.</p>
<dd>This directive is primarily relevant to the <code>snmpset</code> command, but will also apply to any application that calls <i>snmp_add_var()</i> with a non-NULL value.</p>
<dt>noTokenWarnings</p>
<dd>disables warnings about unknown config file tokens.</p>
<dt>reverseEncodeBER (1|yes|true|0|no|false)</p>
<dd>controls how the encoding of SNMP requests is handled.</p>
<dd>The default behaviour is to encode packets starting from the end of the PDU and working backwards. This directive can be used to disable this behaviour, and build the encoded request in the (more obvious) forward direction.</p>
<dd>It should not normally be necessary to change this setting, as the encoding is basically the same in either case &#8211; but working backwards typically produces a slightly more efficient encoding, and hence a smaller network datagram.</p>
<dt>dontLoadHostConfig (1|yes|true|0|no|false)</p>
<dd>Specifies whether or not the host-specific configuration files are loaded. Set to &quot;true&quot; to turn off the loading of the host specific configuration files.</p>
<dt>retries INTEGER</p>
<dd>Specifies the number of retries to be used in the requests.</p>
<dt>timeout INTEGER</p>
<dd>Specifies the timeout in seconds between retries.</dl>
<h2>SNMPv3 SETTINGS</h2>
<dl>
<dt>defSecurityName STRING</p>
<dd>defines the default security name to use for SNMPv3 requests. This can be overridden using the <code>-u</code> option.</p>
<dt>defSecurityLevel noAuthNoPriv|authNoPriv|authPriv</p>
<dd>defines the default security level to use for SNMPv3 requests. This can be overridden using the <code>-l</code> option.</p>
<dd>If not specified, the default value for this token is <i>noAuthNoPriv</i>.</p>
<dl>
<dd>
<dl>
<dt>Note:</p>
<dd><i>authPriv</i> is only available if the software has been compiled to use the OpenSSL libraries.</dl>
</dl>
<dt>defPassphrase STRING</p>
<dd>
<dt>defAuthPassphrase STRING</p>
<dd>
<dt>defPrivPassphrase STRING</p>
<dd>define the default authentication and privacy pass phrases to use for SNMPv3 requests. These can be overridden using the <code>-A</code> and <code>-X</code> options respectively.</p>
<dd>The <code>defPassphrase</code> value will be used for the authentication and/or privacy pass phrases if either of the other directives are not specified.</p>
<dt>defAuthType MD5|SHA</p>
<dd>
<dt>defPrivType DES|AES</p>
<dd>define the default authentication and privacy protocols to use for SNMPv3 requests. These can be overridden using the <code>-a</code> and <code>-x</code> options respectively.</p>
<dd>If not specified, SNMPv3 requests will default to MD5 authentication and DES encryption.</p>
<dl>
<dd>
<dl>
<dt>Note:</p>
<dd>If the software has not been compiled to use the OpenSSL libraries, then only MD5 authentication is supported. Neither SHA authentication nor any form of encryption will be available.</dl>
</dl>
<dt>defContext STRING</p>
<dd>defines the default context to use for SNMPv3 requests. This can be overridden using the <code>-n</code> option.</p>
<dd>If not specified, the default value for this token is the default context (i.e. the empty string &quot;&quot;).</p>
<dt>defSecurityModel STRING</p>
<dd>defines the security model to use for SNMPv3 requests. The default value is &quot;usm&quot; which is the only widely used security model for SNMPv3.</p>
<dt>defAuthMasterKey 0xHEXSTRING</p>
<dd>
<dt>defPrivMasterKey 0xHEXSTRING</p>
<dd>
<dt>defAuthLocalizedKey 0xHEXSTRING</p>
<dd>
<dt>defPrivLocalizedKey 0xHEXSTRING</p>
<dd>define the (hexadecimal) keys to be used for SNMPv3 secure communications. SNMPv3 keys are frequently derived from a passphrase, as discussed in the <i>defPassphrase</i> section above. However for improved security a truely random key can be generated and used instead (which would normally has better entropy than a password unless it is amazingly long). The directives are equivalent to the short-form command line options <code>-3m</code>, <code>-3M</code>, <code>-3k</code>, and <code>-3K</code>.</p>
<dd>Localized keys are master keys which have been converted to a unique key which is only suitable for on particular SNMP engine (agent). The length of the key needs to be appropriate for the authentication or encryption type being used (auth keys: MD5=16 bytes, SHA1=20 bytes; priv keys: DES=16 bytes (8 bytes of which is used as an IV and not a key), and AES=16 bytes).</p>
<dt>sshtosnmpsocket PATH</p>
<dd>Sets the path of the <code>sshtosnmp</code> socket created by an application (e.g. snmpd) listening for incoming ssh connections through the <code>sshtosnmp</code> unix socket.</p>
<dt>sshtosnmpsocketperms MODE [OWNER [GROUP]]</p>
<dd>Sets the mode, owner and group of the <code>sshtosnmp</code> socket created by an application (e.g. <code>snmpd</code>) listening for incoming ssh connections through the <code>sshtosnmp</code> unix socket. The socket needs to be read/write privileged for SSH users that are allowed to connect to the SNMP service (VACM access still needs to be granted as well, most likely through the TSM security model).</p>
<dt>sshusername NAME</p>
<dd>Sets the SSH user name for logging into the remote system.</p>
<dt>sshpubkey FILE</p>
<dd>Set the public key file to use when connecting to a remote system.</p>
<dt>sshprivkey FILE</p>
<dd>Set the private key file to use when connecting to a remote system.</dl>
<h2>Server Behaviour</h2>
<dl>
<dt>persistentDir DIRECTORY</p>
<dd>defines the directory where <code>snmpd</code> and <code>snmptrapd</code> store persistent configuration settings.</p>
<dd>If not specified, the persistent directory defaults to /var/lib/snmp</p>
<dt>noPersistentLoad yes</p>
<dd>
<dt>noPersistentSave yes</p>
<dd>disable the loading and saving of persistent configuration information.</p>
<dl>
<dd>
<dl>
<dt>Note:</p>
<dd>This will break SNMPv3 operations (and other behaviour that relies on changes persisting across application restart). Use With Care.</dl>
</dl>
<dt>tempFilePattern PATTERN</p>
<dd>defines a filename template for creating temporary files, for handling input to and output from external shell commands. Used by the <i>mkstemp()</i> and <i>mktemp()</i> functions.</p>
<dd>If not specified, the default pattern is &quot;/tmp/snmpdXXXXXX&quot;.</p>
<dt>serverRecvBuf INTEGER</p>
<dd>specifies the desired size of the buffer to be used when receiving incoming SNMP requests. If the OS hard limit is lower than the <i>serverRecvBuf</i> value, then this will be used instead. Some platforms may decide to increase the size of the buffer actually used for internal housekeeping.</p>
<dd>This directive will be ignored if the platforms does not support <i>setsockopt()</i>.</p>
<dt>serverSendBuf INTEGER</p>
<dd>is similar to <i>serverRecvBuf</i>, but applies to the size of the buffer used when sending SNMP responses.</dl>
<h2>Mib Handling</h2>
<dl>
<dt>mibdirs DIRLIST</p>
<dd>specifies a list of directories to search for MIB files. This operates in the same way as the <code>-M</code> option &#8211; see <i><a href="/docs/linux/man/1-snmpcmd/">snmpcmd</a>(1)</i> for details. Note that this value can be overridden by the <code>MIBDIRS</code> environment variable, and the <code>-M</code> option.</p>
<dt>mibs MIBLIST</p>
<dd>specifies a list of MIB modules (not files) that should be loaded. This operates in the same way as the <code>-m</code> option &#8211; see <i><a href="/docs/linux/man/1-snmpcmd/">snmpcmd</a>(1)</i> for details. Note that this list can be overridden by the <code>MIBS</code> environment variable, and the <code>-m</code> option.</p>
<dt>mibfile FILE</p>
<dd>specifies a (single) MIB file to load, in addition to the list read from the <i>mibs</i> token (or equivalent configuration). Note that this value can be overridden by the <code>MIBFILES</code> environment variable.</p>
<dt>showMibErrors (1|yes|true|0|no|false)</p>
<dd>whether to display MIB parsing errors.</p>
<dt>commentToEOL (1|yes|true|0|no|false)</p>
<dd>whether MIB parsing should be strict about comment termination. Many MIB writers assume that ASN.1 comments extend to the end of the text line, rather than being terminated by the next &quot;&#8211;&quot; token. This token can be used to accept such (strictly incorrect) MIBs.<br />
 Note that this directive was previous (mis-)named <i>strictCommentTerm</i>, but with the reverse behaviour from that implied by the name. This earlier token is still accepted for backwards compatibility.</p>
<dt>mibAllowUnderline (1|yes|true|0|no|false)</p>
<dd>whether to allow underline characters in MIB object names and enumeration values. This token can be used to accept such (strictly incorrect) MIBs.</p>
<dt>mibWarningLevel INTEGER</p>
<dd>the minimum warning level of the warnings printed by the MIB parser.</dl>
<h2>Output Configuration</h2>
<dl>
<dt>logTimestamp (1|yes|true|0|no|false)</p>
<dd>Whether the commands should log timestamps with their error/message logging or not. Note that output will not look as pretty with timestamps if the source code that is doing the logging does incremental logging of messages that are not line buffered before being passed to the logging routines. This option is only used when file logging is active.</p>
<dt>printNumericEnums (1|yes|true|0|no|false)</p>
<dd>Equivalent to <code>-Oe</code>.</p>
<dt>printNumericOids (1|yes|true|0|no|false)</p>
<dd>Equivalent to <code>-On</code>.</p>
<dt>dontBreakdownOids (1|yes|true|0|no|false)</p>
<dd>Equivalent to <code>-Ob</code>.</p>
<dt>escapeQuotes (1|yes|true|0|no|false)</p>
<dd>Equivalent to <code>-OE</code>.</p>
<dt>quickPrinting (1|yes|true|0|no|false)</p>
<dd>Equivalent to <code>-Oq</code>.</p>
<dt>printValueOnly (1|yes|true|0|no|false)</p>
<dd>Equivalent to <code>-Ov</code>.</p>
<dt>dontPrintUnits (1|yes|true|0|no|false)</p>
<dd>Equivalent to <code>-OU</code>.</p>
<dt>numericTimeticks (1|yes|true|0|no|false)</p>
<dd>Equivalent to <code>-Ot</code>.</p>
<dt>printHexText (1|yes|true|0|no|false)</p>
<dd>Equivalent to <code>-OT</code>.</p>
<dt>hexOutputLength integer</p>
<dd>Specifies where to break up the output of hexadecimal strings. Set to 0 to disable line breaks. Defaults to 16.</p>
<dt>suffixPrinting (0|1|2)</p>
<dd>The value 1 is equivalent to <code>-Os</code> and the value 2 is equivalent to <code>-OS</code>.</p>
<dt>oidOutputFormat (1|2|3|4|5|6)</p>
<dd>Maps -O options as follow: -Os=1, -OS=2, -Of=3, -On=4, -Ou=5. The value 6 has no matching -O option. It suppresses output.</p>
<dt>extendedIndex (1|yes|true|0|no|false)</p>
<dd>Equivalent to <code>-OX</code>.</p>
<dt>noDisplayHint (1|yes|true|0|no|false)</p>
<dd>Disables the use of DISPLAY-HINT information when parsing indices and values to set. Equivalent to <code>-Ih</code>.</dl>
<h2>Files</h2>
<dl>
<dt>System-wide configuration files:</p>
<dd>/etc/snmp/snmp.conf<br />
 /etc/snmp/snmp.local.conf</p>
<dt>User-specific configuration settings:</p>
<dd>$HOME/.snmp/snmp.conf<br />
 $HOME/.snmp/snmp.local.conf</p>
<dt>Destination host specific files:</p>
<dd>/etc/snmp/hosts/HOSTNAME.conf<br />
 $HOME/.snmp/hosts/HOSTNAME.conf </p>
</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/5-snmp_config/">snmp_config</a>(5), <a href="/docs/linux/man/3-netsnmp_config_api/">netsnmp_config_api</a>(3), <a href="/docs/linux/man/1-snmpcmd/">snmpcmd</a>(1). </p>
