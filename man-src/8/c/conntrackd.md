---
title: "conntrackd(8)"
name: "conntrackd"
section: "8"
letter: "c"
url: "/docs/linux/man/8-conntrackd/"
description: "conntrackd – netfilter connection tracking user-space daemon"
---

<p>conntrackd &#8211; netfilter connection tracking user-space daemon</p>
<h2>Synopsis</h2>
<p><code>conntrackd [options]</code></p>
<h2>Description</h2>
<p><code>conntrackd</code> is the user-space daemon for the netfilter connection tracking system. This daemon synchronizes connection tracking states between several replica firewalls. Thus, <code>conntrackd </code> can be used to deploy highly available stateful firewalls. The daemon supports Primary-Backup and Multiprimary setups. The daemon can also be used as statistics collector.</p>
<h2>Options</h2>
<p>The options recognized by <code>conntrackd</code> can be divided into several different groups.</p>
<h3>Modes</h3>
<p>These options specify the particular operation mode in which conntrackd runs. Only one of them can be specified at any given time.</p>
<dl>
<dt><code>-d </code></p>
<dd>Run conntrackd in daemon mode.</dl>
<h3>Client Commands</h3>
<p><code>conntrackd </code> can be used in client mode to request several information and operations to a running daemon</p>
<dl>
<dt><code>-i [ct|expect]</code></p>
<dd>Dump the internal cache, i.e. show local states</p>
<dt><code>-e [ct|expect]</code></p>
<dd>Dump the external cache, i.e. show foreign states</p>
<dt><code>-x </code></p>
<dd>Display output in XML format. This option is only valid in combination with &quot;-i&quot; and &quot;-e&quot; parameters.</p>
<dt><code>-f </code><i>[|internal|external]</i></p>
<dd>Flush the internal and/or external cache</p>
<dt><code>-F [ct|expect]</code></p>
<dd>Flush the kernel conntrack table (if you use a Linux kernel &gt;= 2.6.29, this option will not flush your internal and external cache).</p>
<dt><code>-c </code></p>
<dd>Commit external cache to conntrack table.</p>
<dt><code>-B </code></p>
<dd>Force a bulk send to other replica firewalls. With this command, you will ask conntrackd to send the state-entries that it owns to others.</p>
<dt><code>-n </code></p>
<dd>Request resync with other node (only FT-FW and NOTRACK modes).</p>
<dt><code>-k </code></p>
<dd>Kill the daemon</p>
<dt><code>-s </code><i>[|network|cache|runtime|link|rsqueue|process|queue|ct|expect]</i></p>
<dd>Dump statistics. If no parameter is passed, it displays the general statistics. If &quot;network&quot; is passed as parameter it displays the networking statistics. If &quot;cache&quot; is passed as parameter, it shows the extended cache statistics. If &quot;runtime&quot; is passed as parameter, it shows the run-time statistics. If &quot;process&quot; is passed as parameter, it shows existing child processes (if any). If &quot;queue&quot; is passed as parameter, it shows queue statistics. If &quot;ct&quot; is passed, it displays the general statistics. If &quot;expect&quot; is passed as parameter, it shows expectation statistics.</p>
<dt><code>-R </code><i>[ct|expect]</i></p>
<dd>Force a resync against the kernel connection tracking table</p>
<dt><code>-t </code></p>
<dd>Reset the in-kernel timers (See PurgeTimeout clause)</p>
<dt><code>-v </code></p>
<dd>Display version information.</p>
<dt><code>-h </code></p>
<dd>Display help information.</p>
<dt><code>-C config file</code></p>
<dd>Configuration file path.</p>
<dt></dl>
<h2>Diagnostics</h2>
<dd>The exit code is 0 for correct function. Errors cause an exit code of 1.</p>
<h2>Examples</h2>
<p>The following example are illustrative, for a real use in a firewall fail-over, check the primary-backup.sh script that comes with the sources.</p>
<dl>
<dt><code>conntrackd -d</code></p>
<dd>Runs conntrackd in daemon and synchronization mode</p>
<dt><code>conntrackd -i</code></p>
<dd>Dumps the states held in the internal cache, i.e. those handled by this firewall</p>
<dt><code>conntrackd -e</code></p>
<dd>Dumps the states held in the external cache, i.e. those handled by other replica firewalls</p>
<dt><code>conntrackd -c</code></p>
<dd>Commits the external cache into the kernel connection tracking system. This is used to inject the state so that the connections can be recovered during the failover.</dl>
<h2>Dependencies</h2>
<p>This daemon requires a Linux kernel version &gt;= 2.6.18. TCP window tracking support requires &gt;= 2.6.22, otherwise you have to disable it. Helpers are fully supported since &gt;= 2.6.25, however, if you use any previous version, depending on the protocol helper and your setup (e.g. if you setup performs NAT sequence adjustments or not), your help connection may be successfully recovered.</p>
<dl>
<dt>There are several unsupported stateful iptables matches such as recent, connbytes and the quota matches which gather internal information to operate. Since that information does not belong to the domain of the connection tracking system, connections affected by those matches may not be fully recovered during the takeover.</p>
<dd>
<dt>The daemon requires a Linux kernel version &gt;= 2.6.26 to support kernel-space event filtering. Otherwise, all the event filtering is done in userspace with the corresponding extra overhead. If you are not using the Filter clause in the configuration file, ignore this notice.</p>
<dd></dl>
<h2>Incompatibilities</h2>
<p>During the 0.9.9 development, some important changes in the replication message format were introduced. Therefore, conntrackd &gt;= 0.9.9 will not work appropriately with conntrackd &lt;= 0.9.8. This should not be a problem if you use the same conntrackd version in all the firewall replica nodes.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-conntrack/">conntrack</a></code>(8),<code><a href="/docs/linux/man/8-iptables/">iptables</a></code>(8)<br />
 See <code><a rel="nofollow" href="http://conntrack-tools.netfilter.org">http://conntrack-tools.netfilter.org</a></code></p>
<h2>Bugs</h2>
<p>Please, report them to netfilter-devel [at] vger.kernel.org or file a bug in Netfilter&#8217;s bugzilla (<a rel="nofollow" href="https://bugzilla.netfilter.org">https://bugzilla.netfilter.org</a>).</p>
<h2>Authors</h2>
<p>Pablo Neira Ayuso wrote and maintains the conntrackd tool</p>
<dl>
<dt>Please send bug reports to &lt;netfilter-devel [at] lists.netfilter.org&gt;. Subscription is required.</p>
<dd></dl>
<p> Man page written by Pablo Neira Ayuso &lt;pablo [at] netfilter.org&gt;.</p>
