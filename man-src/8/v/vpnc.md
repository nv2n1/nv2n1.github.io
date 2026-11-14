---
title: "vpnc(8)"
name: "vpnc"
section: "8"
letter: "v"
url: "/docs/linux/man/8-vpnc/"
description: "vpnc – client for Cisco VPN3000 Concentrator, IOS and PIX"
---

<p>vpnc &#8211; client for Cisco VPN3000 Concentrator, IOS and PIX</p>
<h2>Synopsis</h2>
<p><code>vpnc</code> [<i>&#8211;version</i>] [<i>&#8211;print-config</i>] [<i>&#8211;help</i>] [<i>&#8211;long-help</i>] [<i>options</i>] [<i>config files</i>]</p>
<h2>Description</h2>
<p>This manual page documents briefly the <code>vpnc</code> and <code>vpnc-disconnect</code> commands. <code>vpnc</code> is a VPN client for the Cisco 3000 VPN Concentrator, creating a IPSec-like connection as a tunneling network device for the local system. It uses the TUN/TAP driver in Linux kernel 2.4 and above and device <a href="/docs/linux/man/4-tun/">tun</a>(4) on BSD. The created connection is presented as a tunneling network device to the local system. OBLIGATORY WARNING: the most used configuration (XAUTH authentication with pre-shared keys and password authentication) is insecure by design, be aware of this fact when you use vpnc to exchange sensitive data like passwords! The vpnc daemon by itself does not set any routes, but it calls <code>vpnc-script</code> to do this job. <code>vpnc-script</code> displays a connect banner. If the concentrator supplies a network list for split-tunneling these networks are added to the routing table. Otherwise the default-route will be modified to point to the tunnel. Further a host route to the concentrator is added in the later case. If the client host needs DHCP, care must be taken to add another host route to the DHCP-Server around the tunnel. The <code>vpnc-disconnect</code> command is used to terminate the connection previously created by <code>vpnc</code> and restore the previous routing configuration. </p>
<h2>Configuration</h2>
<p>The daemon reads configuration data from the following places:</p>
<dl>
<dt>&bull;</p>
<dd>command line options</p>
<dt>&bull;</p>
<dd>config file(s) specified on the command line</p>
<dt>&bull;</p>
<dd>/etc/vpnc/default.conf</p>
<dt>&bull;</p>
<dd>/etc/vpnc.conf</p>
<dt>&bull;</p>
<dd>prompting the user if not found above </p>
</dl>
<p> vpnc can parse options and <code>configuration files</code> in any order. However the first place to set an option wins. configuration filenames which do not contain a / will be searched at <code>/etc/vpnc/&lt;filename&gt;</code> and <code>/etc/vpnc/&lt;filename&gt;.conf.</code> Otherwise <code>&lt;filename&gt;</code> and <code>&lt;filename&gt;.conf</code> will be used. If no configuration file is specified on the command-line at all, both <code>/etc/vpnc/default.conf</code> and <code>/etc/vpnc.conf</code> will be loaded.</p>
<h2>Options</h2>
<p>The program options can be either given as arguments (but not all of them for security reasons) or be stored in a configuration file. </p>
<dl>
<dt><code>&#8211;gateway</code><i> &lt;ip/hostname&gt;</i></p>
<dd>IP/name of your IPSec gateway</dl>
<p> conf-variable: <code>IPSec gateway</code><i> &lt;ip/hostname&gt;</i> </p>
<dl>
<dt><code>&#8211;id</code><i> &lt;ASCII string&gt;</i></p>
<dd>your group name</dl>
<p> conf-variable: <code>IPSec ID</code><i> &lt;ASCII string&gt;</i> </p>
<dl>
<dt><code>(configfile only option)</code></p>
<dd>your group password (cleartext)</dl>
<p> conf-variable: <code>IPSec secret</code><i> &lt;ASCII string&gt;</i> </p>
<dl>
<dt><code>(configfile only option)</code></p>
<dd>your group password (obfuscated)</dl>
<p> conf-variable: <code>IPSec obfuscated secret</code><i> &lt;hex string&gt;</i> </p>
<dl>
<dt><code>&#8211;username</code><i> &lt;ASCII string&gt;</i></p>
<dd>your username</dl>
<p> conf-variable: <code>Xauth username</code><i> &lt;ASCII string&gt;</i> </p>
<dl>
<dt><code>(configfile only option)</code></p>
<dd>your password (cleartext)</dl>
<p> conf-variable: <code>Xauth password</code><i> &lt;ASCII string&gt;</i> </p>
<dl>
<dt><code>(configfile only option)</code></p>
<dd>your password (obfuscated)</dl>
<p> conf-variable: <code>Xauth obfuscated password</code><i> &lt;hex string&gt;</i> </p>
<dl>
<dt><code>&#8211;domain</code><i> &lt;ASCII string&gt;</i></p>
<dd>(NT-) Domain name for authentication</dl>
<p> conf-variable: <code>Domain</code><i> &lt;ASCII string&gt;</i> </p>
<dl>
<dt><code>&#8211;xauth-inter</code></p>
<dd>enable interactive extended authentication (for challenge response auth)</dl>
<p> conf-variable: <code>Xauth interactive</code> </p>
<dl>
<dt><code>&#8211;vendor</code><i> &lt;cisco/netscreen&gt;</i></p>
<dd>vendor of your IPSec gateway</p>
<dd>Default: cisco</dl>
<p> conf-variable: <code>Vendor</code><i> &lt;cisco/netscreen&gt;</i> </p>
<dl>
<dt><code>&#8211;natt-mode</code><i> &lt;natt/none/force-natt/cisco-udp&gt;</i></p>
<dd>Which NAT-Traversal Method to use:</p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd>natt &#8212; NAT-T as defined in RFC3947</p>
<dt>&bull;</p>
<dd>none &#8212; disable use of any NAT-T method</p>
<dt>&bull;</p>
<dd>force-natt &#8212; always use NAT-T encapsulation even without presence of a NAT device (useful if the OS captures all ESP traffic)</p>
<dt>&bull;</p>
<dd>cisco-udp &#8212; Cisco proprietary UDP encapsulation, commonly over Port 10000</dl>
</dl>
<dd>Note: cisco-tcp encapsulation is not yet supported</p>
<dd>Default: natt</dl>
<p> conf-variable: <code>NAT Traversal Mode</code><i> &lt;natt/none/force-natt/cisco-udp&gt;</i> </p>
<dl>
<dt><code>&#8211;script</code><i> &lt;command&gt;</i></p>
<dd>command is executed using system() to configure the interface, routing and so on. Device name, IP, etc. are passed using enviroment variables, see README. This script is executed right after ISAKMP is done, but before tunneling is enabled. It is called when vpnc terminates, too</p>
<dd>Default: /etc/vpnc/vpnc-script</dl>
<p> conf-variable: <code>Script</code><i> &lt;command&gt;</i> </p>
<dl>
<dt><code>&#8211;dh</code><i> &lt;dh1/dh2/dh5&gt;</i></p>
<dd>name of the IKE DH Group</p>
<dd>Default: dh2</dl>
<p> conf-variable: <code>IKE DH Group</code><i> &lt;dh1/dh2/dh5&gt;</i> </p>
<dl>
<dt><code>&#8211;pfs</code><i> &lt;nopfs/dh1/dh2/dh5/server&gt;</i></p>
<dd>Diffie-Hellman group to use for PFS</p>
<dd>Default: server</dl>
<p> conf-variable: <code>Perfect Forward Secrecy</code><i> &lt;nopfs/dh1/dh2/dh5/server&gt;</i> </p>
<dl>
<dt><code>&#8211;enable-1des</code></p>
<dd>enables weak single DES encryption</dl>
<p> conf-variable: <code>Enable Single DES</code> </p>
<dl>
<dt><code>&#8211;enable-no-encryption</code></p>
<dd>enables using no encryption for data traffic (key exchanged must be encrypted)</dl>
<p> conf-variable: <code>Enable no encryption</code> </p>
<dl>
<dt><code>&#8211;application-version</code><i> &lt;ASCII string&gt;</i></p>
<dd>Application Version to report. Note: Default string is generated at runtime.</p>
<dd>Default: Cisco Systems VPN Client 0.5.3:Linux</dl>
<p> conf-variable: <code>Application version</code><i> &lt;ASCII string&gt;</i> </p>
<dl>
<dt><code>&#8211;ifname</code><i> &lt;ASCII string&gt;</i></p>
<dd>visible name of the TUN/TAP interface</dl>
<p> conf-variable: <code>Interface name</code><i> &lt;ASCII string&gt;</i> </p>
<dl>
<dt><code>&#8211;ifmode</code><i> &lt;tun/tap&gt;</i></p>
<dd>mode of TUN/TAP interface:</p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd>tun: virtual point to point interface (default)</p>
<dt>&bull;</p>
<dd>tap: virtual ethernet interface</dl>
</dl>
<dd>Default: tun</dl>
<p> conf-variable: <code>Interface mode</code><i> &lt;tun/tap&gt;</i> </p>
<dl>
<dt><code>&#8211;debug</code><i> &lt;0/1/2/3/99&gt;</i></p>
<dd>
<dd>Show verbose debug messages</p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd>&nbsp;<wbr>0: Do not print debug information.</p>
<dt>&bull;</p>
<dd>&nbsp;<wbr>1: Print minimal debug information.</p>
<dt>&bull;</p>
<dd>&nbsp;<wbr>2: Show statemachine and packet/payload type information.</p>
<dt>&bull;</p>
<dd>&nbsp;<wbr>3: Dump everything exluding authentication data.</p>
<dt>&bull;</p>
<dd>99: Dump everything INCLUDING AUTHENTICATION data (e.g. PASSWORDS).</dl>
</dl>
</dl>
<p> conf-variable: <code>Debug</code><i> &lt;0/1/2/3/99&gt;</i> </p>
<dl>
<dt><code>&#8211;no-detach</code></p>
<dd>
<dd>Don&#8217;t detach from the console after login</dl>
<p> conf-variable: <code>No Detach</code> </p>
<dl>
<dt><code>&#8211;pid-file</code><i> &lt;filename&gt;</i></p>
<dd>store the pid of background process in &lt;filename&gt;</p>
<dd>Default: /var/run/vpnc/pid</dl>
<p> conf-variable: <code>Pidfile</code><i> &lt;filename&gt;</i> </p>
<dl>
<dt><code>&#8211;local-addr</code><i> &lt;ip/hostname&gt;</i></p>
<dd>local IP to use for ISAKMP / ESP / &#8230; (0.0.0.0 == automatically assign)</p>
<dd>Default: 0.0.0.0</dl>
<p> conf-variable: <code>Local Addr</code><i> &lt;ip/hostname&gt;</i> </p>
<dl>
<dt><code>&#8211;local-port</code><i> &lt;0-65535&gt;</i></p>
<dd>local ISAKMP port number to use (0 == use random port)</p>
<dd>Default: 500</dl>
<p> conf-variable: <code>Local Port</code><i> &lt;0-65535&gt;</i> </p>
<dl>
<dt><code>&#8211;udp-port</code><i> &lt;0-65535&gt;</i></p>
<dd>Local UDP port number to use (0 == use random port). This is only relevant if cisco-udp nat-traversal is used. This is the _local_ port, the remote udp port is discovered automatically. It is especially not the cisco-tcp port.</p>
<dd>Default: 10000</dl>
<p> conf-variable: <code>Cisco UDP Encapsulation Port</code><i> &lt;0-65535&gt;</i> </p>
<dl>
<dt><code>&#8211;dpd-idle</code><i> &lt;0,10-86400&gt;</i></p>
<dd>Send DPD packet after not receiving anything for &lt;idle&gt; seconds. Use 0 to disable DPD completely (both ways).</p>
<dd>Default: 600</dl>
<p> conf-variable: <code>DPD idle timeout (our side)</code><i> &lt;0,10-86400&gt;</i> </p>
<dl>
<dt><code>&#8211;non-inter</code></p>
<dd>Don&#8217;t ask anything, exit on missing options</dl>
<p> conf-variable: <code>Noninteractive</code> </p>
<dl>
<dt><code>&#8211;auth-mode</code><i> &lt;psk/cert/hybrid&gt;</i></p>
<dd>Authentication mode:</p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd>psk: pre-shared key (default)</p>
<dt>&bull;</p>
<dd>cert: server + client certificate (not implemented yet)</p>
<dt>&bull;</p>
<dd>hybrid: server certificate + xauth (if built with openssl support)</dl>
</dl>
<dd>Default: psk</dl>
<p> conf-variable: <code>IKE Authmode</code><i> &lt;psk/cert/hybrid&gt;</i> </p>
<dl>
<dt><code>&#8211;ca-file</code><i> &lt;filename&gt;</i></p>
<dd>
<dd>filename and path to the CA-PEM-File</dl>
<p> conf-variable: <code>CA-File</code><i> &lt;filename&gt;</i> </p>
<dl>
<dt><code>&#8211;ca-dir</code><i> &lt;directory&gt;</i></p>
<dd>path of the trusted CA-Directory</p>
<dd>Default: /etc/ssl/certs</dl>
<p> conf-variable: <code>CA-Dir</code><i> &lt;directory&gt;</i> </p>
<dl>
<dt><code>&#8211;target-network</code><i> &lt;target network/netmask&gt;</i></p>
<dd>Target network in dotted decimal or CIDR notation</p>
<dd>Default: 0.0.0.0/0.0.0.0</dl>
<p> conf-variable: <code>IPSEC target network</code><i> &lt;target network/netmask&gt;</i> </p>
<dl>
<dt> <code>&#8211;print-config</code></p>
<dd>
<dd>Prints your configuration; output can be used as vpnc.conf </p>
</dl>
<h2>Files</h2>
<p><i>/etc/vpnc.conf</i> <i>/etc/vpnc/default.conf</i></p>
<dl>
<dd>The default configuration file. You can specify the same config directives as with command line options and additionaly <code>IPSec secret</code> and <code>Xauth password</code> both supplying a cleartext password. Scrambled passwords from the Cisco configuration profiles can be used with <code>IPSec obfuscated secret</code> and <code>Xauth obfuscated password.</code> </p>
<p> See <code>EXAMPLES</code> for further details.</dl>
<p> <i>/etc/vpnc/*.conf</i></p>
<dl>
<dd>vpnc will read configuration files in this directory when the config filename (with or without .conf) is specified on the command line.</dl>
<h2>Examples</h2>
<p>This is an example vpnc.conf with pre-shared keys:</p>
<dl>
<dd>IPSec gateway vpn.example.com IPSec ID ExampleVpnPSK IKE Authmode psk IPSec secret PskS3cret! Xauth username user [at] example.com Xauth password USecr3t</dl>
<p> And another one with hybrid authentication (requires that vpnc was built with openssl support):</p>
<dl>
<dd>IPSec gateway vpn.example.com IPSec ID ExampleVpnHybrid IKE Authmode hybrid CA-Dir /etc/vpnc <code>or</code> CA-File /etc/vpnc/vpn-example-com.pem IPSec secret HybS3cret? Xauth username user [at] example.com Xauth password 123456</dl>
<p> The lines begin with a keyword (no leading spaces!). The values start exactly one space after the keywords, and run to the end of line. This lets you put any kind of weird character (except CR, LF and NUL) in your strings, but it does mean you can&#8217;t add comments after a string, or spaces before them. In case the the <code>CA-Dir</code> option is used, your certificate needs to be named something like 722d15bd.X, where X is a manually assigned number to make sure that files with colliding hashes have different names. The number can be derived from the certificate file itself: openssl x509 -subject_hash -noout -in /etc/vpnc/vpn-example-com.pem See also the <code>&#8211;print-config</code> option to generate a config file, and the example file in the package documentation directory where more advanced usage is demonstrated. Advanced features like manual setting of multiple target routes and disabling /etc/resolv.conf rewriting is documented in the README of the vpnc package. </p>
<h2>Todo</h2>
<p>Certificate support (Pre-Shared-Key + XAUTH is known to be insecure). </p>
<p> Further points can be found in the TODO file.</p>
<h2>Author</h2>
<p>This man-page has been written by Eduard Bloch &lt;blade(at)debian.org&gt; and Christian Lackas &lt;delta(at)lackas.net&gt;, based on vpnc README by Maurice Massar &lt;vpnc(at)unix-ag.uni-kl.de&gt;. Permission is granted to copy, distribute and/or modify this document under the terms of the GNU General Public License, Version 2 any later version published by the Free Software Foundation. </p>
<p> On Debian systems, the complete text of the GNU General Public License can be found in /usr/share/common-licenses/GPL.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-pcf2vpnc/">pcf2vpnc</a></code>(1), <code><a href="/docs/linux/man/1-cisco-decrypt/">cisco-decrypt</a></code>(1), <code><a href="/docs/linux/man/8-ip/">ip</a></code>(8), <code><a href="/docs/linux/man/8-ifconfig/">ifconfig</a></code>(8), <code><a href="/docs/linux/man/1-route/">route</a></code>(1), <code><a rel="nofollow" href="http://www.unix-ag.uni-kl.de/~massar/vpnc/">http://www.unix-ag.uni-kl.de/~massar/vpnc/</a></code> </p>
