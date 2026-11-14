---
title: "snmp-ups(8)"
name: "snmp-ups"
section: "8"
letter: "s"
url: "/docs/linux/man/8-snmp-ups/"
description: "snmp-ups – Multi-MIB Driver for SNMP UPS equipment"
---

<p>snmp-ups &#8211; Multi-MIB Driver for SNMP UPS equipment</p>
<h2>Note</h2>
<p>This man page only documents the hardware-specific features of the snmp-ups driver. For information about the core driver, see <code><a href="/docs/linux/man/8-nutupsdrv/">nutupsdrv</a></code>(8).</p>
<h2>Supported Hardware</h2>
<p>The snmp-ups driver automatically detects and supports a wide range of devices by loading various MIBS: </p>
<p> <code>ietf</code></p>
<dl>
<dd>UPS that is RFC 1628 (UPS MIB) compliant, e.g. MGE UPS SYSTEMS, Liebert, perhaps others (default)</dl>
<p> <code>mge</code></p>
<dl>
<dd>MGE UPS SYSTEMS and MGE Office Protection Systems devices with SNMP cards (ref 66062, 66045, 66074 and 66244)</dl>
<p> <code>apcc</code></p>
<dl>
<dd>APC AP9605, AP9606, AP9617, and AP9618 APC network management cards, as well as any others supporting the APC POWERNET MIB</dl>
<p> <code>netvision</code></p>
<dl>
<dd>Socomec Sicon UPS with Netvision Web/SNMP management card/external box</dl>
<p> <code>pw</code></p>
<dl>
<dd>Powerware devices with ConnectUPS SNMP cards</dl>
<p> <code>aphel_genesisII</code></p>
<dl>
<dd>Eaton Powerware ePDU Monitored</dl>
<p> <code>aphel_revelation</code></p>
<dl>
<dd>Eaton Powerware ePDU Managed</dl>
<p> <code>raritan</code></p>
<dl>
<dd>Various Raritan PDUs</dl>
<p> <code>baytech</code></p>
<dl>
<dd>Various BayTech PDUs</dl>
<p> <code>cpqpower</code></p>
<dl>
<dd>HP/Compaq AF401A management card, perhaps others</dl>
<p> <code>cyberpower</code></p>
<dl>
<dd>Cyberpower RMCARD201. Should also support RMCARD100 (net version), RMCARD202 and RMCARD301</dl>
<h2>Extra Arguments</h2>
<p>This driver supports the following optional settings in the <code><a href="/docs/linux/man/5-ups-conf/">ups.conf</a></code>(5): </p>
<p> <code>mibs</code>=<i>name</i></p>
<dl>
<dd>Set MIB compliance (default=auto, allowed entries: refer to SUPPORTED HARDWARE above). With &quot;auto&quot;, the driver will try a select set of SNMP objects until it finds one that the device responds to. Note that since NUT 2.6.2, snmp-ups has a new method that uses sysObjectID (which is a pointer to the prefered MIB of the device) to detect supported devices. This renders void the use of &quot;mibs&quot; option.</dl>
<p> <code>community</code>=<i>name</i></p>
<dl>
<dd>Set community name (default = public). Note that a RW community name is required to change UPS settings (as for a powerdown).</dl>
<p> <code>snmp_version</code>=<i>version</i></p>
<dl>
<dd>Set SNMP version (default = v1, allowed: v2c, v3)</dl>
<p> <code>pollfreq</code>=<i>value</i></p>
<dl>
<dd>Set polling frequency in seconds, to reduce network flow (default=30)</dl>
<p> <code>notransferoids</code></p>
<dl>
<dd>Disable the monitoring of the low and high voltage transfer OIDs in the hardware. This will remove input.transfer.low and input.transfer.high from the list of variables. This should only be used on APCC Symmetra equipment which has strangeness in the three-phase power reporting.</dl>
<p> <code>secLevel</code>=<i>value</i></p>
<dl>
<dd>Set the securityLevel used for SNMPv3 messages (default=noAuthNoPriv, allowed: authNoPriv,authPriv)</dl>
<p> <code>secName</code>=<i>value</i></p>
<dl>
<dd>Set the securityName used for authenticated SNMPv3 messages (no default)</dl>
<p> <code>authPassword</code>=<i>value</i></p>
<dl>
<dd>Set the authentication pass phrase used for authenticated SNMPv3 messages (no default)</dl>
<p> <code>privPassword</code>=<i>value</i></p>
<dl>
<dd>Set the privacy pass phrase used for encrypted SNMPv3 messages (no default)</dl>
<p> <code>authProtocol</code>=<i>value</i></p>
<dl>
<dd>Set the authentication protocol (MD5 or SHA) used for authenticated SNMPv3 messages (default=MD5)</dl>
<p> <code>privProtocol</code>=<i>value</i></p>
<dl>
<dd>Set the privacy protocol (DES or AES) used for encrypted SNMPv3 messages (default=DES)</dl>
<h2>Requirements</h2>
<p>You will need to install the Net-SNMP package from <a rel="nofollow" href="http://www.net-snmp.org/">http://www.net-snmp.org/</a> before building this driver. </p>
<p> SNMP v3 also requires OpenSSL support from <a rel="nofollow" href="http://www.openssl.org.">http://www.openssl.org.</a></p>
<h2>Limitations</h2>
<h3>Shutdown</h3>
<p>The shutdown sequence should be tested before relying on NUT to send a shutdown command to the UPS. The problem is that the host network stack may have been torn down by the time the driver is invoked to send the shutdown command. The driver attempts to send shutdown.return, shutdown.reboot, and load.off.delay commands to the UPS in sequence, stopping after the first supported command.</p>
<h2>Installation</h2>
<p>This driver is only built if the Net-SNMP development files are present at configuration time. You can also force it to be built by using configure &#8211;with-snmp=yes before calling make.</p>
<h2>Examples</h2>
<p>The hostname of the UPS is specified with the &quot;port&quot; value in ups.conf: </p>
<pre><code>[snmpv1]
driver = snmp-ups
port = snmp-ups.example.com
community = public
snmp_version = v1
pollfreq = 15
desc = &quot;Example SNMP v1 device&quot;
[snmpv3]
driver = snmp-ups
port = 166.99.224.132
snmp_version = v3
secLevel = authPriv
secName = mysecurityname
authPassword = myauthenticationpassphrase
privPassword = myprivatepassphrase
desc = &quot;Example SNMP v3 device, with the highest security level&quot;</code></pre>
<h2>Authors</h2>
<p>Arnaud Quette, Dmitry Frolov</p>
<h2>See Also</h2>
<h3>The core driver:</h3>
<p><code><a href="/docs/linux/man/8-nutupsdrv/">nutupsdrv</a></code>(8)</p>
<h3>NUT SNMP Protocols Library</h3>
<p>Available at: <a rel="nofollow" href="http://www.networkupstools.org/protocols/snmp/">http://www.networkupstools.org/protocols/snmp/</a></p>
<h3>Internet resources:</h3>
<p>The NUT (Network UPS Tools) home page: <a rel="nofollow" href="http://www.networkupstools.org/">http://www.networkupstools.org/</a> </p>
