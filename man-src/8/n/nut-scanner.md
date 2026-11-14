---
title: "nut-scanner(8)"
name: "nut-scanner"
section: "8"
letter: "n"
url: "/docs/linux/man/8-nut-scanner/"
description: "nut-scanner – scan communication buses for NUT devices"
---

<p>nut-scanner &#8211; scan communication buses for NUT devices</p>
<h2>Synopsis</h2>
<p><code>nut-scanner</code> -h </p>
<p> <code>nut-scanner</code> [<i>OPTIONS</i>]</p>
<h2>Description</h2>
<p><code>nut-scanner</code> scans available communication buses and displays any NUT-compatible devices it has found.</p>
<h2>Installation</h2>
<p><code>nut-scanner</code> is only built if libltdl (part of libtool development suite) is available. Available options (USB, SNMP, IPMI, &#8230;) will vary according to the available compile time and runtime dependencies. For example, if Net-SNMP is installed, thus providing libsnmp (.so or .dll) and headers, both during compilation and runtime, then SNMP discovery will be available.</p>
<h2>Options</h2>
<p><code>-h</code></p>
<dl>
<dd>Display the help text.</dl>
<h2>Display Options</h2>
<p><code>-N</code> | <code>&#8211;disp_nut_conf</code></p>
<dl>
<dd>Display result in the <i>ups.conf</i> format.</dl>
<p> <code>-P</code> | <code>&#8211;disp_parsable</code></p>
<dl>
<dd>Display result in a parsable format.</dl>
<h2>Bus Options</h2>
<p><code>-C</code> | <code>&#8211;complete_scan</code></p>
<dl>
<dd>Scan all available communication buses (default behavior)</dl>
<p> <code>-U</code> | <code>&#8211;usb_scan</code></p>
<dl>
<dd>List all NUT-compatible USB devices currently plugged in.</dl>
<p> <code>-S</code> | <code>&#8211;snmp_scan</code></p>
<dl>
<dd>Scan SNMP devices. Requires at least a <i>start IP</i>, and optionally, an <i>end IP</i>. See specific SNMP OPTIONS for community and security settings.</dl>
<p> <code>-M</code> | <code>&#8211;xml_scan</code></p>
<dl>
<dd>Scan XML/HTTP devices. Broadcast a network message on the current network interfaces to retrieve XML/HTTP capable devices. No IP required.</dl>
<p> <code>-O</code> | <code>&#8211;oldnut_scan</code></p>
<dl>
<dd>Scan NUT devices (i.e. upsd daemon) on IP ranging from <i>start IP</i> to <i>end IP</i>.</dl>
<p> <code>-A</code> | <code>&#8211;avahi_scan</code></p>
<dl>
<dd>Scan NUT servers using Avahi request on the current network interfaces. No IP required.</dl>
<p> <code>-I</code> | <code>&#8211;ipmi_scan</code></p>
<dl>
<dd>Scan NUT compatible power supplies available via IPMI on the current host, or over the network.</dl>
<p> <code>-E</code> | <code>&#8211;eaton_serial</code> <i>serial ports</i></p>
<dl>
<dd>Scan Eaton devices (XCP and SHUT) available via serial bus on the current host. This option must be requested explicitely, even for a complete scan. <i>serial ports</i> can be expressed in various forms: </p>
<dl>
<dd>&bull; </p>
<p> <i>auto</i> to scan all serial ports.</dl>
<dl>
<dd>&bull; a single charcater indicating a port number (<i>0</i> (zero) for /dev/ttyS0 and /dev/ttyUSB0 on Linux, <i>1</i> for COM1 on Windows, <i>a</i> for /dev/ttya on Solaris&#8230;)</dl>
<dl>
<dd>&bull; a range of N characters, hyphen separated, describing the range of ports using <i>X-Y</i>, where X and Y are characters refering to the port number.</dl>
<dl>
<dd>&bull; a single port name.</dl>
<dl>
<dd>&bull; a list of ports name, coma separated, like <i>/dev/ttyS1,/dev/ttyS4</i>.</dl>
</dl>
<h2>Network Options</h2>
<p><code>-t</code> | <code>&#8211;timeout</code> <i>timeout</i></p>
<dl>
<dd>Set the network timeout in seconds. Default timeout is 5 seconds.</dl>
<p> <code>-s</code> | <code>&#8211;start_ip</code> <i>start IP</i></p>
<dl>
<dd>Set the first IP (IPv4 or IPv6) when a range of IP is required (SNMP, old_nut).</dl>
<p> <code>-e</code> | <code>&#8211;end_ip</code> <i>end IP</i></p>
<dl>
<dd>Set the last IP (IPv4 or IPv6) when a range of IP is required (SNMP, old_nut). If this parameter is omitted, only the <i>start IP</i> is scanned. If <i>end IP</i> is less than <i>start IP</i>, both parameters are internally permuted.</dl>
<p> <code>-m</code> | <code>&#8211;mask_cidr</code> <i>IP address/mask</i></p>
<dl>
<dd>Set a range of IP using CIDR notation.</dl>
<h2>Nut Device Option</h2>
<p><code>-p</code> | <code>&#8211;port</code> <i>port number</i></p>
<dl>
<dd>Set the port number of scanned NUT devices (default 3493).</dl>
<h2>Snmp V1 Option</h2>
<p><code>-c</code> | <code>&#8211;community</code> <i>community</i></p>
<dl>
<dd>Set SNMP v1 community name (default = public).</dl>
<h2>Snmp V3 Options</h2>
<p><code>-l</code> | <code>&#8211;secLevel</code> <i>security level</i></p>
<dl>
<dd>Set the <i>security level</i> used for SNMPv3 messages. Allowed values are: noAuthNoPriv, authNoPriv and authPriv.</dl>
<p> <code>-u</code> | <code>&#8211;secName</code> <i>security name</i></p>
<dl>
<dd>Set the <i>security name</i> used for authenticated SNMPv3 messages. This parameter is mandatory if you set <i>security level</i>.</dl>
<p> <code>-w</code> | <code>&#8211;authProtocol</code> <i>authentication protocol</i></p>
<dl>
<dd>Set the <i>authentication protocol</i> used for authenticated SNMPv3 messages. Allowed values are MD5 or SHA. Default value is MD5.</dl>
<p> <code>-W</code> | <code>&#8211;authPassword</code> <i>authentication pass phrase</i></p>
<dl>
<dd>Set the <i>authentication pass phrase</i> used for authenticated SNMPv3 messages. This parameter is mandatory if you set <i>security level</i> to authNoPriv or authPriv.</dl>
<p> <code>-x</code> | <code>&#8211;privProtocol</code> <i>privacy protocol</i></p>
<dl>
<dd>Set the <i>privacy protocol</i> used for encrypted SNMPv3 messages. Allowed values are DES or AES. Default value is DES.</dl>
<p> <code>-X</code> | <code>&#8211;privPassword</code> <i>privacy pass phrase</i></p>
<dl>
<dd>Set the <i>privacy pass phrase</i> used for encrypted SNMPv3 messages. This parameter is mandatory if you set <i>security level</i> to authPriv.</dl>
<h2>Ipmi Options</h2>
<p><code>-b</code> | <code>&#8211;username</code> <i>username</i></p>
<dl>
<dd>Set the username used for authenticating IPMI over LAN connections (mandatory for IPMI over LAN. No default).</dl>
<p> <code>-B</code> | <code>&#8211;password</code> <i>password</i></p>
<dl>
<dd>Specify the password to use when authenticationg with the remote host (mandatory for IPMI over LAN. No default).</dl>
<p> <code>-d</code> | <code>&#8211;authType</code> <i>authentication type</i></p>
<dl>
<dd>Specify the IPMI 1.5 authentication type to use (NONE, STRAIGHT_PASSWORD_KEY, MD2, and MD5) with the remote host (default=MD5). This forces connection through the <i>lan</i> IPMI interface , thus in IPMI 1.5 mode.</dl>
<p> <code>-D</code> | <code>&#8211;cipher_suite_id</code> <i>cipher suite identifier</i></p>
<dl>
<dd>Specify the IPMI 2.0 cipher suite ID to use. The Cipher Suite ID identifies a set of authentication, integrity, and confidentiality algorithms to use for IPMI 2.0 communication. The authentication algorithm identifies the algorithm to use for session setup, the integrity algorithm identifies the algorithm to use for session packet signatures, and the confidentiality algorithm identifies the algorithm to use for payload encryption (default=3). </p>
<p> The following cipher suite ids are currently supported (Authentication; Integrity; Confidentiality): </p>
<dl>
<dd>&bull; </p>
<p> <code>0</code>: None; None; None</dl>
<dl>
<dd>&bull; </p>
<p> <code>1</code>: HMAC-SHA1; None; None</dl>
<dl>
<dd>&bull; </p>
<p> <code>2</code>: HMAC-SHA1; HMAC-SHA1-96; None</dl>
<dl>
<dd>&bull; </p>
<p> <code>3</code>: HMAC-SHA1; HMAC-SHA1-96; AES-CBC-128</dl>
<dl>
<dd>&bull; </p>
<p> <code>6</code>: HMAC-MD5; None; None</dl>
<dl>
<dd>&bull; </p>
<p> <code>7</code>: HMAC-MD5; HMAC-MD5-128; None</dl>
<dl>
<dd>&bull; </p>
<p> <code>8</code>: HMAC-MD5; HMAC-MD5-128; AES-CBC-128</dl>
<dl>
<dd>&bull; </p>
<p> <code>11</code>: HMAC-MD5; MD5-128; None</dl>
<dl>
<dd>&bull; </p>
<p> <code>12</code>: HMAC-MD5; MD5-128; AES-CBC-128</dl>
<dl>
<dd>&bull; </p>
<p> <code>15</code>: HMAC-SHA256; None; None</dl>
<dl>
<dd>&bull; </p>
<p> <code>16</code>: HMAC-SHA256; HMAC_SHA256_128; None</dl>
<dl>
<dd>&bull; </p>
<p> <code>17</code>: HMAC-SHA256; HMAC_SHA256_128; AES-CBC-128</dl>
</dl>
<h2>Miscellaneous Options</h2>
<p><code>-V</code> | <code>&#8211;version</code></p>
<dl>
<dd>Display NUT version.</dl>
<p> <code>-a</code> | <code>&#8211;available</code></p>
<dl>
<dd>Display available bus that can be scanned , depending on how the binary has been compiled. (OLDNUT, USB, SNMP, XML, AVAHI, IPMI).</dl>
<p> <code>-q</code> | <code>&#8211;quiet</code></p>
<dl>
<dd>Display only scan result. No information on currently scanned bus is displayed.</dl>
<h2>Examples</h2>
<p>To scan USB devices only: </p>
<p> <code>nut-scanner -U</code> </p>
<p> To scan SNMP v1 device with public community on address range 192.168.0.0 to 192.168.0.255: </p>
<p> <code>nut-scanner -S -s 192.168.0.0 -e 192.168.0.255</code> </p>
<p> The same using CIDR notation: </p>
<p> <code>nut-scanner -S -m 192.168.0.0/24</code> </p>
<p> To scan NUT servers with a timeout of 10 seconds on IP range 192.168.0.0 to 192.168.0.128 using CIDR notation: </p>
<p> <code>nut-scanner -O -t 10 -m 192.168.0.0/25</code> </p>
<p> To scan for power supplies, through IPMI (1.5 mode) over the network, on address range 192.168.0.0 to 192.168.0.255: </p>
<p> <code>nut-scanner -I -m 192.168.0.0/24 -b username -B password</code> </p>
<p> To scan for Eaton serial devices on ports 0 and 1 (/dev/ttyS0, /dev/ttyUSB0, /dev/ttyS1 and /dev/ttyUSB1 on Linux): </p>
<p> <code>nut-scanner &#8211;eaton_serial 0-1</code> </p>
<p> To scan for Eaton serial devices on ports 1 and 2 (COM1 and COM2 on Windows): </p>
<p> <code>nut-scanner &#8211;eaton_serial 1-2</code></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-ups-conf/">ups.conf</a></code>(5)</p>
<h2>Internet Resources</h2>
<p>The NUT (Network UPS Tools) home page: <a rel="nofollow" href="http://www.networkupstools.org/">http://www.networkupstools.org/</a></p>
