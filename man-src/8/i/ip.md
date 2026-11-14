---
title: "ip(8)"
name: "ip"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ip/"
description: "ip – show / manipulate routing, network devices, interfaces and tunnels"
---

<p>ip &#8211; show / manipulate routing, network devices, interfaces and tunnels</p>
<h2>Synopsis</h2>
<pre><code>ip

[ OPTIONS ] OBJECT { COMMAND |

    help }
</code></pre>
<p> <code>ip</code> [ <code>-force</code> ] <code>-batch </code><i>filename</i> </p>
<pre><code>OBJECT := {

    link | address | addrlabel | route | rule | neigh | ntable | tunnel | tuntap | maddress | mroute | mrule | monitor | xfrm | netns }

OPTIONS := {

    -V[ersion] |
    -h[uman-readable] |
    -s[tatistics] |
    -d[etails] |
    -r[esolve] |
    -iec |
    -f[amily] {
        inet | inet6 | link } |

    -4 |
    -6 |
    -B |
    -0 |
    -l[oops] { maximum-addr-flush-attempts } |
    -o[neline] |
    -rc[vbuf] [size] |
    -t[imestamp] |
    -ts[hort] |
    -n[etns] name |
    -N[umeric] |
    -a[ll] |
    -c[olor] |
    -br[ief] |
    -j[son] |
    -p[retty] }
</code></pre>
<h2>Options</h2>
<dl>
<dt><code>-V</code>,<code> -Version</code></p>
<dd>Print the version of the <code>ip</code> utility and exit. </p>
<dt><code>-h,</code> -human,<code> -human-readable</code></p>
<dd>output statistics with human readable values followed by suffix. </p>
<dt><code>-b,</code> -batch <code>&lt;FILENAME&gt;</code></p>
<dd>Read commands from provided file or standard input and invoke them. First failure will cause termination of ip. </p>
<dt><code>-force</code></p>
<dd>Don&#8217;t terminate ip on errors in batch mode. If there were any errors during execution of the commands, the application return code will be non zero. </p>
<dt><code>-s</code>,<code> -stats</code>,<code> -statistics</code></p>
<dd>Output more information. If the option appears twice or more, the amount of information increases. As a rule, the information is statistics or some time values. </p>
<dt><code>-d</code>,<code> -details</code></p>
<dd>Output more detailed information. </p>
<dt><code>-l</code>,<code> -loops </code>&lt;COUNT&gt;</p>
<dd>Specify maximum number of loops the &#8216;ip address flush&#8217; logic will attempt before giving up. The default is 10. Zero (0) means loop until all addresses are removed. </p>
<dt><code>-f</code>,<code> -family </code>&lt;FAMILY&gt;</p>
<dd>Specifies the protocol family to use. The protocol family identifier can be one of <code>inet</code>,<code> inet6</code>,<code> bridge</code>,<code> mpls</code> or <code>link</code>. If this option is not present, the protocol family is guessed from other arguments. If the rest of the command line does not give enough information to guess the family, <code>ip</code> falls back to the default one, usually <code>inet</code> or <code>any</code>. <code>link</code> is a special family identifier meaning that no networking protocol is involved. </p>
<dt><code>-4</code></p>
<dd>shortcut for <code>-family inet</code>. </p>
<dt><code>-6</code></p>
<dd>shortcut for <code>-family inet6</code>. </p>
<dt><code>-B</code></p>
<dd>shortcut for <code>-family bridge</code>. </p>
<dt><code>-M</code></p>
<dd>shortcut for <code>-family mpls</code>. </p>
<dt><code>-0</code></p>
<dd>shortcut for <code>-family link</code>. </p>
<dt><code>-o</code>,<code> -oneline</code></p>
<dd>output each record on a single line, replacing line feeds with the <code>&#8216;\&#8217;</code> character. This is convenient when you want to count records with <code><a href="/docs/linux/man/1-wc/">wc</a></code>(1) or to <code><a href="/docs/linux/man/1-grep/">grep</a></code>(1) the output. </p>
<dt><code>-r</code>,<code> -resolve</code></p>
<dd>use the system&#8217;s name resolver to print DNS names instead of host addresses. </p>
<dt><code>-n</code>,<code> -netns </code>&lt;NETNS&gt;</p>
<dd>switches <code>ip</code> to the specified network namespace <i>NETNS</i>. Actually it just simplifies executing of: </p>
<p> <code>ip netns exec</code> <i>NETNS</i> <code>ip</code> [ <i>OPTIONS</i> ] <i>OBJECT</i> { <i>COMMAND</i> | <code>help</code> } </p>
<p> to </p>
<p> <code>ip</code> -n[etns] <i>NETNS</i> [ <i>OPTIONS</i> ] <i>OBJECT</i> { <i>COMMAND</i> | <code>help</code> } </p>
<dt><code>-N</code>,<code> -Numeric</code></p>
<dd>Print the number of protocol, scope, dsfield, etc directly instead of converting it to human readable name. </p>
<dt><code>-a</code>,<code> -all</code></p>
<dd>executes specified command over all objects, it depends if command supports this option. </p>
<dt><code>-c</code>[<code>color</code>][<code>=</code>{<code>always</code>|<code>auto</code>|<code>never</code>}</p>
<dd>Configure color output. If parameter is omitted or <code>always</code>, color output is enabled regardless of stdout state. If parameter is <code>auto</code>, stdout is checked to be a terminal before enabling color output. If parameter is <code>never</code>, color output is disabled. If specified multiple times, the last one takes precedence. This flag is ignored if <code>-json</code> is also given. </p>
<p> Used color palette can be influenced by <code>COLORFGBG</code> environment variable (see <code>ENVIRONMENT</code>). </p>
<dt><code>-t</code>,<code> -timestamp</code></p>
<dd>display current time when using monitor option. </p>
<dt><code>-ts</code>,<code> -tshort</code></p>
<dd>Like <code>-timestamp</code>, but use shorter format. </p>
<dt><code>-rc</code>,<code> -rcvbuf</code>&lt;SIZE&gt;</p>
<dd>Set the netlink socket receive buffer size, defaults to 1MB. </p>
<dt><code>-iec</code></p>
<dd>print human readable rates in IEC units (e.g. 1Ki = 1024). </p>
<dt><code>-br</code>,<code> -brief</code></p>
<dd>Print only basic information in a tabular format for better readability. This option is currently only supported by <code>ip addr show ,</code> ip link show <code>&amp;</code> ip neigh show <code>commands.</code> </p>
<dt><code>-j,</code> -json</p>
<dd>Output results in JavaScript Object Notation (JSON). </p>
<dt><code>-p,</code> -pretty</p>
<dd>The default JSON format is compact and more efficient to parse but hard for most users to read. This flag adds indentation for readability. </p>
</dl>
<h2>Ip &#8211; Command Syntax</h2>
<h3><i>OBJECT</i></h3>
<dl>
<dt><code>address</code></p>
<dd>&#8211; protocol (IP or IPv6) address on a device. </p>
<dt><code>addrlabel</code></p>
<dd>&#8211; label configuration for protocol address selection. </p>
<dt><code>ioam</code></p>
<dd>&#8211; manage IOAM namespaces and IOAM schemas. </p>
<dt><code>l2tp</code></p>
<dd>&#8211; tunnel ethernet over IP (L2TPv3). </p>
<dt><code>link</code></p>
<dd>&#8211; network device. </p>
<dt><code>maddress</code></p>
<dd>&#8211; multicast address. </p>
<dt><code>monitor</code></p>
<dd>&#8211; watch for netlink messages. </p>
<dt><code>mptcp</code></p>
<dd>&#8211; manage MPTCP path manager. </p>
<dt><code>mroute</code></p>
<dd>&#8211; multicast routing cache entry. </p>
<dt><code>mrule</code></p>
<dd>&#8211; rule in multicast routing policy database. </p>
<dt><code>neighbour</code></p>
<dd>&#8211; manage ARP or NDISC cache entries. </p>
<dt><code>netns</code></p>
<dd>&#8211; manage network namespaces. </p>
<dt><code>ntable</code></p>
<dd>&#8211; manage the neighbor cache&#8217;s operation. </p>
<dt><code>route</code></p>
<dd>&#8211; routing table entry. </p>
<dt><code>rule</code></p>
<dd>&#8211; rule in routing policy database. </p>
<dt><code>tcp_metrics/tcpmetrics</code></p>
<dd>&#8211; manage TCP Metrics </p>
<dt><code>token</code></p>
<dd>&#8211; manage tokenized interface identifiers. </p>
<dt><code>tunnel</code></p>
<dd>&#8211; tunnel over IP. </p>
<dt><code>tuntap</code></p>
<dd>&#8211; manage TUN/TAP devices. </p>
<dt><code>vrf</code></p>
<dd>&#8211; manage virtual routing and forwarding devices. </p>
<dt><code>xfrm</code></p>
<dd>&#8211; manage IPSec policies. </p>
</dl>
<p> The names of all objects may be written in full or abbreviated form, for example <code>address</code> can be abbreviated as <code>addr</code> or just <code>a.</code></p>
<h3><i>COMMAND</i></h3>
<p>Specifies the action to perform on the object. The set of possible actions depends on the object type. As a rule, it is possible to <code>add</code>,<code> delete</code> and <code>show</code> (or <code>list</code> ) objects, but some objects do not allow all of these operations or have some additional commands. The <code>help</code> command is available for all objects. It prints out a list of available commands and argument syntax conventions. </p>
<p> If no command is given, some default command is assumed. Usually it is <code>list</code> or, if the objects of this class cannot be listed, <code>help</code>.</p>
<h2>Environment</h2>
<dl>
<dt><code>COLORFGBG</code></p>
<dd>If set, it&#8217;s value is used for detection whether background is dark or light and use contrast colors for it. </p>
<p> COLORFGBG environment variable usually contains either two or three values separated by semicolons; we want the last value in either case. If this value is 0-6 or 8, chose colors suitable for dark background: </p>
<p> COLORFGBG=&quot;;0&quot; ip -c a </p>
</dl>
<h2>Exit Status</h2>
<p>Exit status is 0 if command was successful, and 1 if there is a syntax error. If an error was reported by the kernel exit status is 2.</p>
<h2>Examples</h2>
<p>ip addr</p>
<dl>
<dd>Shows addresses assigned to all network interfaces.</dl>
<p> ip neigh</p>
<dl>
<dd>Shows the current neighbour table in kernel.</dl>
<p> ip link set x up</p>
<dl>
<dd>Bring up interface x.</dl>
<p> ip link set x down</p>
<dl>
<dd>Bring down interface x.</dl>
<p> ip route</p>
<dl>
<dd>Show table routes.</dl>
<h2>History</h2>
<p><code>ip</code> was written by Alexey N. Kuznetsov and added in Linux 2.2.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-ip-address/">ip-address</a></code>(8), <code><a href="/docs/linux/man/8-ip-addrlabel/">ip-addrlabel</a></code>(8), <code><a href="/docs/linux/man/8-ip-ioam/">ip-ioam</a></code>(8), <code><a href="/docs/linux/man/8-ip-l2tp/">ip-l2tp</a></code>(8), <code><a href="/docs/linux/man/8-ip-link/">ip-link</a></code>(8), <code><a href="/docs/linux/man/8-ip-maddress/">ip-maddress</a></code>(8), <code><a href="/docs/linux/man/8-ip-monitor/">ip-monitor</a></code>(8), <code><a href="/docs/linux/man/8-ip-mptcp/">ip-mptcp</a></code>(8), <code><a href="/docs/linux/man/8-ip-mroute/">ip-mroute</a></code>(8), <code><a href="/docs/linux/man/8-ip-neighbour/">ip-neighbour</a></code>(8), <code><a href="/docs/linux/man/8-ip-netns/">ip-netns</a></code>(8), <code><a href="/docs/linux/man/8-ip-ntable/">ip-ntable</a></code>(8), <code><a href="/docs/linux/man/8-ip-route/">ip-route</a></code>(8), <code><a href="/docs/linux/man/8-ip-rule/">ip-rule</a></code>(8), <code><a href="/docs/linux/man/8-ip-tcp_metrics/">ip-tcp_metrics</a></code>(8), <code><a href="/docs/linux/man/8-ip-token/">ip-token</a></code>(8), <code><a href="/docs/linux/man/8-ip-tunnel/">ip-tunnel</a></code>(8), <code><a href="/docs/linux/man/8-ip-vrf/">ip-vrf</a></code>(8), <code><a href="/docs/linux/man/8-ip-xfrm/">ip-xfrm</a></code>(8)<br />
 IP Command reference <code>ip-cref.ps</code></p>
<h2>Reporting Bugs</h2>
<p>Report any bugs to the Network Developers mailing list <code>&lt;netdev [at] vger.kernel.org&gt;</code> where the development and maintenance is primarily done. You do not have to be subscribed to the list to send a message there.</p>
<h2>Author</h2>
<p>Original Manpage by Michail Litvak &lt;mci [at] owl.openwall.com&gt;</p>
