---
title: "ufw-framework(8)"
name: "ufw-framework"
section: "8"
letter: "u"
url: "/docs/linux/man/8-ufw-framework/"
description: "ufw-framework – using the ufw framework"
---

<p>ufw-framework &#8211; using the ufw framework</p>
<h2>Description</h2>
<p><code>ufw</code> provides both a command line interface and a framework for managing a netfilter firewall. While the <code>ufw</code> command provides an easy to use interface for managing a firewall, the <code>ufw</code> framework provides the administrator methods to customize default behavior and add rules not supported by the command line tool. In this way, <code>ufw</code> can take full advantage of Linux netfilter&#8217;s power and flexibility. </p>
<h2>Overview</h2>
<p>The framework provides boot time initialization, rules files for adding custom rules, a method for loading netfilter modules, configuration of kernel parameters and configuration of IPv6. The framework consists of the following files:</p>
<dl>
<dt>/lib/ufw/ufw-init</p>
<dd>initialization script</p>
<dt>/etc/ufw/before.init</p>
<dd>initialization customization script run before ufw is initialized</p>
<dt>/etc/ufw/after.init</p>
<dd>initialization customization script run after ufw is initialized</p>
<dt>/etc/ufw/before[6].rules</p>
<dd>rules file containing rules evaluated before UI added rules</p>
<dt>/etc/ufw/user[6].rules</p>
<dd>rules file containing UI added rules (managed with the <code>ufw</code> command)</p>
<dt>/etc/ufw/after[6].rules</p>
<dd>rules file containing rules evaluated after UI added rules</p>
<dt>/etc/default/ufw</p>
<dd>high level configuration</p>
<dt>/etc/ufw/sysctl.conf</p>
<dd>kernel network tunables</p>
<dt>/etc/ufw/ufw.conf</p>
<dd>additional high level configuration </p>
</dl>
<h2>Boot Initialization</h2>
<p><code>ufw</code> is started on boot with /lib/ufw/ufw-init. This script is a standard SysV style initscript used by the <code>ufw</code> command and should not be modified. The /etc/before.init and /etc/after.init scripts may be used to perform any additional firewall configuration that is not yet supported in ufw itself and if they exist and are executable, ufw-init will execute these scripts. ufw-init will exit with error if either of these scripts exit with error. ufw-init supports the following arguments:</p>
<dl>
<dt>start:</p>
<dd>loads the firewall</p>
<dt>stop:</p>
<dd>unloads the firewall</p>
<dt>restart:</p>
<dd>reloads the firewall</p>
<dt>force-reload:</p>
<dd>same as restart</p>
<dt>status:</p>
<dd>basic status of the firewall</p>
<dt>force-stop:</p>
<dd>same as stop, except does not check if the firewall is already loaded</p>
<dt>flush-all:</p>
<dd>flushes the built-in chains, deletes all non-built-in chains and resets the policy to ACCEPT</dl>
<p> ufw-init will call before.init and after.init with start, stop, status and flush-all, but typically, if used, these scripts need only implement start and stop. </p>
<p> <code>ufw</code> uses many user-defined chains in addition to the built-in iptables chains. If MANAGE_BUILTINS in /etc/default/ufw is set to &#8216;yes&#8217;, on stop and reload the built-in chains are flushed. If it is set to &#8216;no&#8217;, on stop and reload the <code>ufw</code> secondary chains are removed and the <code>ufw</code> primary chains are flushed. In addition to flushing the <code>ufw</code> specific chains, it keeps the primary chains in the same order with respect to any other user-defined chains that may have been added. This allows for <code>ufw</code> to interoperate with other software that may manage their own firewall rules. </p>
<p> To ensure your firewall is loading on boot, you must integrate this script into the boot process. Consult your distribution&#8217;s documentation for the proper way to modify your boot process if <code>ufw</code> is not already integrated.</p>
<h2>Rules Files</h2>
<p><code>ufw</code> is in part a front-end for <code>iptables-restore</code>, with its rules saved in /etc/ufw/before.rules, /etc/ufw/after.rules and /etc/ufw/user.rules. Administrators can customize <code>before.rules</code> and <code>after.rules</code> as desired using the standard <code>iptables-restore</code> syntax. Rules are evaluated as follows: <code>before.rules</code> first, <code>user.rules</code> next, and <code>after.rules</code> last. IPv6 rules are evaluated in the same way, with the rules files named <code>before6.rules</code>, <code>user6.rules</code> and <code>after6.rules</code>. Please note that <code>ufw status</code> only shows rules added with <code>ufw</code> and not the rules found in the /etc/ufw rules files. </p>
<p> <code>Important</code>: <code>ufw</code> only uses the *filter table by default. You may add any other tables such as *nat, *raw and *mangle as desired. For each table a corresponding COMMIT statement is required. </p>
<p> After modifying any of these files, you must reload <code>ufw</code> for the rules to take effect. See the EXAMPLES section for common uses of these rules files.</p>
<h2>Modules</h2>
<p>Netfilter has many different connection tracking modules. These modules are aware of the underlying protocol and allow the administrator to simplify his or her rule sets. You can adjust which netfilter modules to load by adjusting IPT_MODULES in /etc/default/ufw. Some popular modules to load are: </p>
<p>&nbsp;<wbr>&nbsp;nf_conntrack_ftp<br />
&nbsp;<wbr>&nbsp;nf_nat_ftp<br />
&nbsp;<wbr>&nbsp;nf_conntrack_irc<br />
&nbsp;<wbr>&nbsp;nf_nat_irc<br />
&nbsp;<wbr>&nbsp;nf_conntrack_netbios_ns<br />
&nbsp;<wbr>&nbsp;nf_conntrack_pptp<br />
&nbsp;<wbr>&nbsp;nf_conntrack_tftp<br />
&nbsp;<wbr>&nbsp;nf_nat_tftp<br />
&nbsp;<wbr>&nbsp;nf_conntrack_sane </p>
<p> Unconditional loading of connection tracking modules (nf_conntrack_*) in this manner is deprecated. <code>ufw</code> continues to support the functionality but new configuration should only contain the specific modules required for the site. For more information, see CONNECTION HELPERS.</p>
<h2>Kernel Parameters</h2>
<p><code>ufw</code> will read in /etc/ufw/sysctl.conf on boot when enabled. Please note that /etc/ufw/sysctl.conf overrides values in the system systcl.conf (usually /etc/sysctl.conf). Administrators can change the file used by modifying /etc/default/ufw.</p>
<h2>Ipv6</h2>
<p>IPv6 is enabled by default. When disabled, all incoming, outgoing and forwarded packets are dropped, with the exception of traffic on the loopback interface. To adjust this behavior, set IPV6 to &#8216;yes&#8217; in /etc/default/ufw. See the <code>ufw</code> manual page for details.</p>
<h2>Examples</h2>
<p>As mentioned, <code>ufw</code> loads its rules files into the kernel by using the <code>iptables-restore</code> and <code>ip6tables-restore</code> commands. Users wanting to add rules to the <code>ufw</code> rules files manually must be familiar with these as well as the <code>iptables</code> and <code>ip6tables</code> commands. Below are some common examples of using the <code>ufw</code> rules files. All examples assume IPv4 only and that DEFAULT_FORWARD_POLICY in /etc/default/ufw is set to DROP.</p>
<h3>IP Masquerading</h3>
<p>To allow IP masquerading for computers from the 10.0.0.0/8 network on eth1 to share the single IP address on eth0:</p>
<dl>
<dt>Edit /etc/ufw/sysctl.conf to have:</p>
<dd>&nbsp;net.ipv4.ip_forward=1</p>
<dt>Add to the end of /etc/ufw/before.rules, after the *filter section:</p>
<dd>&nbsp;*nat<br />
&nbsp;:POSTROUTING ACCEPT&nbsp;[0:0]<br />
&nbsp;-A POSTROUTING -s 10.0.0.0/8 -o eth0 -j MASQUERADE<br />
&nbsp;COMMIT</p>
<dt>If your firewall is using IPv6 tunnels or 6to4 and is also doing NAT, then you should not usually masquerade protocol &#8217;41&#8217; (ipv6) packets. For example, instead of the above, /etc/ufw/before.rules can be adjusted to have:</p>
<dd>&nbsp;*nat<br />
&nbsp;:POSTROUTING ACCEPT&nbsp;[0:0]<br />
&nbsp;-A POSTROUTING -s 10.0.0.0/8&nbsp;!&nbsp;&#8211;protocol 41 -o eth0 -j MASQUERADE<br />
&nbsp;COMMIT</p>
<dt>Add the <code>ufw route</code> to allow the traffic:</p>
<dd>&nbsp;ufw route allow in on eth1 out on eth0 from 10.0.0.0/8</dl>
<h3>Port Redirections</h3>
<p>To forward tcp port 80 on eth0 to go to the webserver at 10.0.0.2:</p>
<dl>
<dt>Edit /etc/ufw/sysctl.conf to have:</p>
<dd>&nbsp;net.ipv4.ip_forward=1</p>
<dt>Add to the end of /etc/ufw/before.rules, after the *filter section:</p>
<dd>&nbsp;*nat<br />
&nbsp;:PREROUTING ACCEPT&nbsp;[0:0]<br />
&nbsp;-A PREROUTING -p tcp -i eth0 &#8211;dport 80 -j DNAT&nbsp;\<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8211;to-destination 10.0.0.2:80<br />
&nbsp;COMMIT</p>
<dt>Add the <code>ufw route</code> rule to allow the traffic:</p>
<dd>&nbsp;ufw route allow in on eth0 to 10.0.0.2 port 80 proto tcp</dl>
<h3>Egress filtering</h3>
<p>To block RFC1918 addresses going out of eth0:</p>
<dl>
<dt>Add the <code>ufw route</code> rules to reject the traffic:</p>
<dd>&nbsp;ufw route reject out on eth0 to 10.0.0.0/8<br />
&nbsp;ufw route reject out on eth0 to 172.16.0.0/12<br />
&nbsp;ufw route reject out on eth0 to 192.168.0.0/16</dl>
<h3>Full example</h3>
<p>This example combines the other examples and demonstrates a simple routing firewall. <code>Warning</code>: this setup is only an example to demonstrate the functionality of the <code>ufw</code> framework in a concise and simple manner and should not be used in production without understanding what each part does and does not do. Your firewall will undoubtedly want to be less open. This router/firewall has two interfaces: eth0 (Internet facing) and eth1 (internal LAN). Internal clients have addresses on the 10.0.0.0/8 network and should be able to connect to anywhere on the Internet. Connections to port 80 from the Internet should be forwarded to 10.0.0.2. Access to ssh port 22 from the administrative workstation (10.0.0.100) to this machine should be allowed. Also make sure no internal traffic goes to the Internet.</p>
<dl>
<dt>Edit /etc/ufw/sysctl.conf to have:</p>
<dd>&nbsp;<wbr>&nbsp;net.ipv4.ip_forward=1</p>
<dt>Add to the end of /etc/ufw/before.rules, after the *filter section:</p>
<dd>&nbsp;*nat<br />
&nbsp;:PREROUTING ACCEPT&nbsp;[0:0]<br />
&nbsp;:POSTROUTING ACCEPT&nbsp;[0:0]<br />
&nbsp;-A PREROUTING -p tcp -i eth0 &#8211;dport 80 -j DNAT&nbsp;\<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8211;to-destination 10.0.0.2:80<br />
&nbsp;-A POSTROUTING -s 10.0.0.0/8 -o eth0 -j MASQUERADE<br />
&nbsp;COMMIT</p>
<dt>Add the necessary <code>ufw</code> rules:</p>
<dd>&nbsp;ufw route reject out on eth0 to 10.0.0.0/8<br />
&nbsp;ufw route reject out on eth0 to 172.16.0.0/12<br />
&nbsp;ufw route reject out on eth0 to 192.168.0.0/16<br />
&nbsp;ufw route allow in on eth1 out on eth0 from 10.0.0.0/8<br />
&nbsp;ufw route allow in on eth0 to 10.0.0.2 port 80 proto tcp<br />
&nbsp;ufw allow in on eth1 from 10.0.0.100 to any port 22 proto tcp </p>
<h2>Connection Helpers</h2>
<p>Various protocols require the use of netfilter connection tracking helpers to group related packets into RELATED flows to make rulesets clearer and more precise. For example, with a couple of kernel modules and a couple of rules, a ruleset could simply allow a connection to FTP port 21, then the kernel would examine the traffic and mark the other FTP data packets as RELATED to the initial connection. </p>
<p> When the helpers were first introduced, one could only configure the modules as part of module load (eg, if your FTP server listened on a different port than 21, you&#8217;d have to load the nf_conntrack_ftp module specifying the correct port). Over time it was understood that unconditionally using connection helpers could lead to abuse, in part because some protocols allow user specified data that would allow traversing the firewall in undesired ways. As of kernel 4.7, automatic conntrack helper assignment (ie, handling packets for a given port and all IP addresses) is disabled (the old behavior can be restored by setting net/netfilter/nf_conntrack_helper=1 in /etc/ufw/sysctl.conf). Firewalls should now instead use the CT target to associate traffic with a particular helper and then set RELATED rules to use the helper. This allows sites to tailor the use of helpers and help avoid abuse. </p>
<p> In general, to use helpers securely, the following needs to happen:</p>
<dl>
<dt>1.</p>
<dd>net/netfilter/nf_conntrack_helper should be set to 0 (default)</p>
<dt>2.</p>
<dd>create a rule for the start of a connection (eg for FTP, port 21)</p>
<dt>3.</p>
<dd>create a helper rule to associate the helper with this connection</p>
<dt>4.</p>
<dd>create a helper rule to associate a RELATED flow with this connection</p>
<dt>5.</p>
<dd>if needed, add the corresponding nf_conntrack_* module to IPT_MODULES</p>
<dt>6.</p>
<dd>optionally add the corresponding nf_nat_* module to IPT_MODULES</dl>
<p> In general it is desirable to make connection helper rules as specific as possible and ensure anti-spoofing is correctly setup for your site to avoid security issues in your ruleset. For more information, see ANTI-SPOOFING, above, and &lt;<a rel="nofollow" href="https://home.regit.org/netfilter-en/secure-use-of-helpers/">https://home.regit.org/netfilter-en/secure-use-of-helpers/</a>&gt;. </p>
<p> Currently helper rules must be managed in via the RULES FILES. A future version of <code>ufw</code> will introduce syntax for working with helper rules.</p>
<h2>Notes</h2>
<p>When using ufw with libvirt and bridging, packets may be blocked. The libvirt team recommends that the following sysctl&#8217;s be set to disable netfilter on the bridge: </p>
<pre><code>net.bridge.bridge-nf-call-ip6tables = 0

net.bridge.bridge-nf-call-iptables = 0

net.bridge.bridge-nf-call-arptables = 0</code></pre>
<p> Note that the bridge module must be loaded in to the kernel before these values are set. One way to ensure this works properly with ufw is to add &#8216;bridge&#8217; to IPT_MODULES in /etc/default/ufw, and then add the above rules to /etc/ufw/sysctl.conf. Alternatively to disabling netfilter on the bridge, you can configure iptables to allow all traffic to be forwarded across the bridge. Eg, add to /etc/ufw/before.rules within the *filter section:<br />
&nbsp;<wbr>&nbsp;-I FORWARD -m physdev &#8211;physdev-is-bridged -j ACCEPT </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-ufw/">ufw</a></code>(8), <code><a href="/docs/linux/man/8-iptables/">iptables</a></code>(8), <code><a href="/docs/linux/man/8-ip6tables/">ip6tables</a></code>(8), <code><a href="/docs/linux/man/8-iptables-restore/">iptables-restore</a></code>(8), <code><a href="/docs/linux/man/8-ip6tables-restore/">ip6tables-restore</a></code>(8), <code><a href="/docs/linux/man/8-sysctl/">sysctl</a></code>(8), <code><a href="/docs/linux/man/5-sysctl-conf/">sysctl.conf</a></code>(5) </p>
<h2>Author</h2>
<p>ufw is Copyright 2008-2021, Canonical Ltd.</p>
