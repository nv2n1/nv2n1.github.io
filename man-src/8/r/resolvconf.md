---
title: "resolvconf(8)"
name: "resolvconf"
section: "8"
letter: "r"
url: "/docs/linux/man/8-resolvconf/"
description: "resolvconf – manage nameserver information"
---

<p>resolvconf &#8211; manage nameserver information</p>
<h2>Synopsis</h2>
<p>cat <i>FILE</i> | <code>resolvconf</code> <code>-a</code> <i>IFACE.PROG</i> </p>
<p> <code>resolvconf</code> <code>-d</code> <i>IFACE.PROG</i> </p>
<p> <code>resolvconf</code> <code>-u</code> </p>
<p> <code>resolvconf</code> <code>&#8211;enable-updates</code> | <code>&#8211;disable-updates</code> | <code>&#8211;updates-are-enabled</code></p>
<h2>Description</h2>
<p>The resolvconf package comprises a simple database for run-time nameserver information and a simple framework for notifying applications of changes in that information. Resolvconf thus sets itself up as the intermediary between programs that supply nameserver information and applications that use that information. </p>
<p> Information is added to or removed from the database using the <code>resolvconf</code> program. See the <code>OPTIONS</code> section below for a discussion of the available options.</p>
<h2>Suppliers Of Nameserver Information</h2>
<p>Normally the <code>resolvconf</code> program is run only by network interface configuration programs such as <code><a href="/docs/linux/man/8-ifup/">ifup</a></code>(8), <code>ifdown</code>, <code><a href="/docs/linux/man/8-networkmanager/">NetworkManager</a></code>(8), <code><a href="/docs/linux/man/8-dhclient/">dhclient</a></code>(8), and <code><a href="/docs/linux/man/8-pppd/">pppd</a></code>(8); and by local nameservers such as <code><a href="/docs/linux/man/8-dnsmasq/">dnsmasq</a></code>(8). These programs obtain nameserver information from some source and push it to <code>resolvconf</code>.</p>
<h3>dhclient</h3>
<p>The <code>dhclient </code> program, for example, may receive nameserver addresses and domain search list information during its negotiation with the DHCP server; if so, its hook script <i>/etc/dhcp/dhclient-enter-hooks.d/resolvconf</i> pushes this information to <code>resolvconf.</code></p>
<h3>ifup</h3>
<p>The <code>ifup</code> program can be used to configure network interfaces according to settings in <i>/etc/network/interfaces</i>. To make <code>ifup</code> push nameserver information to <code>resolvconf</code> when it configures an interface the administrator must add <code>dns-</code> option lines to the relevant <code>iface</code> stanza in <i><a href="/docs/linux/man/5-interfaces/">interfaces</a></i>(5). The following option names are accepted: <code>dns-nameserver</code>, <code>dns-search</code>, and <code>dns-sortlist</code>. </p>
<p> To add a nameserver IP address, add an option line consisting of <code>dns-nameserver </code> and the address. To add multiple nameserver addresses, include multiple such <code>dns-nameserver </code> lines. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;dns-nameserver 192.168.1.254<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;dns-nameserver 8.8.8.8 </p>
<p> To add search domain names, add a line beginning with <code>dns-search</code>. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;dns-search foo.org bar.com </p>
<p> The <code>dns-nameservers </code> option is also accepted and, unlike <code>dns-nameserver</code>, can be given multiple arguments, separated by spaces. </p>
<p> The <code>dns-domain</code> option is deprecated in favor of <code>dns-search</code>. </p>
<p> The resulting stanza might look like the following example. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;iface eth0 inet static<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;address 192.168.1.3<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;netmask 255.255.255.0<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;gateway 192.168.1.1<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;dns-nameserver 192.168.1.254<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;dns-nameserver 8.8.8.8<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;dns-search foo.org bar.com </p>
<p> N.B.: On a machine where resolvconf has just been or is about to be installed and which previously relied on a static <i>/etc/resolv.conf</i> file,</p>
<dl>
<dt>&bull;</p>
<dd>the nameserver information in that static file, (which is to say the information on <code>nameserver</code>, <code>domain</code>, <code>search</code> and <code>sortlist</code> lines) should be migrated to the appropriate <code>iface</code> stanza(s) in <i>/etc/network/<a href="/docs/linux/man/5-interfaces/">interfaces</a></i>(5) as just described;</p>
<dt>&bull;</p>
<dd>options (which is to say, any <code>options</code> lines) should be migrated to <i>/etc/resolvconf/resolv.conf.d/base</i>.</dl>
<h3>Command line</h3>
<p>The administrator <i>can</i> run <code>resolvconf</code> from the command line to add or delete nameserver information, but this is not normally necessary or advisable.</p>
<h2>Consumers Of Nameserver Information</h2>
<p>Nameserver information provided to <code>resolvconf</code> is stored for use by subscribers to <code>resolvconf</code>&#8216;s notification service. Subscriber packages that need to know when nameserver information has changed should install a script in <i>/etc/resolvconf/update.d/</i> (or in <i>/etc/resolvconf/update-libc.d/</i>: see below). For example, DNS caches such as <code><a href="/docs/linux/man/8-dnsmasq/">dnsmasq</a></code>(8) and <code><a href="/docs/linux/man/8-pdnsd/">pdnsd</a></code>(8) subscribe to the notification service so that they know whither to forward queries. Client hook scripts will find the files containing nameserver information in the current directory.</p>
<h3>libc</h3>
<p>The most important software package that subscribes to the notification service is the GNU C Library <i><a href="/docs/linux/man/3-resolver/">resolver</a></i>(3). This library is used by many applications that need to resolve domain names. When nameserver information is updated, the script <i>/etc/resolvconf/update.d/libc</i> generates a new version of the resolver configuration file, <i>/run/resolvconf/resolv.conf</i>, as described below. If the new version of the file differs from the previously generated one then the hook scripts found in <i>/etc/resolvconf/update-libc.d/</i> are executed. </p>
<p> The dynamically generated resolver configuration file always starts with the contents of <i>/etc/resolvconf/resolv.conf.d/head</i> and ends with the contents of <i>/etc/resolvconf/resolv.conf.d/tail</i>. Between <i>head</i> and <i>tail</i> the <i>libc</i> script inserts dynamic nameserver information compiled from, first, information provided for configured interfaces; second, static information from <i>/etc/resolvconf/resolv.conf.d/base</i>. Specifically, it writes:</p>
<dl>
<dt> 1)</p>
<dd>up to three <code>nameserver</code> lines, ordered according to <i>/etc/resolvconf/interface-order</i>, possibly fewer if one of the addresses is a loopback address and the <code>TRUNCATE_NAMESERVER_LIST_AFTER_LOOPBACK_ADDRESS </code> environment variable is affirmatively set, as discussed in the <code>ENVIRONMENT VARIABLES</code> section;</p>
<dt> 2)</p>
<dd>up to one <code>search</code> line containing the combined domain search list from all &quot;domain&quot; and &quot;search&quot; input lines, also ordered according to <i><a href="/docs/linux/man/5-interface-order/">interface-order</a></i>(5);</p>
<dt> 3)</p>
<dd>all other non-comment input lines.</dl>
<p> To make the resolver use this dynamically generated resolver configuration file the administrator should ensure that <i>/etc/resolv.conf</i> is a symbolic link to <i>/run/resolvconf/resolv.conf</i>. This link is normally created on installation of the resolvconf package. The link is never modified by the <code>resolvconf</code> program itself. If you find that <i>/etc/resolv.conf</i> is not being updated, please check to make sure that the link is intact. </p>
<p> The GNU C Library resolver library isn&#8217;t the only resolver library available. However, any resolver library that reads <i>/etc/resolv.conf</i> (and most of them do, in order to be compatible) should work fine with resolvconf. </p>
<p> Subscriber packages that need to know only when the resolver configuration file has changed should install a script in <i>/etc/resolvconf/update-libc.d/</i> rather than in <i>/etc/resolvconf/update.d/</i>. (For example, two packages that install <i>update-libc.d/</i> hook scripts are <code>fetchmail</code> and <code>squid</code>.) This is important for synchronization purposes: scripts in <i>update-libc.d/</i> are run <i>after</i> <i>resolv.conf</i> has been updated; the same is not necessarily true of scripts in <i>update.d/</i>.</p>
<h2>Options</h2>
<dl>
<dt><code>-a</code> <i>IFACE.PROG</i></p>
<dd>Add or overwrite the record <i>IFACE.PROG</i> then run the update scripts if updating is enabled. When this option is used the information must be provided to <code>resolvconf</code> on its standard input in the format of the <i><a href="/docs/linux/man/5-resolv-conf/">resolv.conf</a></i>(5) file. Each line in the file must be terminated by a newline.</p>
<dt><code>-d</code> <i>IFACE.PROG</i></p>
<dd>Delete the record <i>IFACE.PROG</i> then run the update scripts if updating is enabled.</dl>
<p> The string <i>IFACE.PROG</i> may not contain spaces, slashes, an initial dot, an initial hyphen or an initial tilde. It is conventionally formed from <i>IFACE</i>, the name of the interface involved, a dot, and <i>IPROG</i>, the name of the interface configuration program, e.g., &quot;eth0.dhclient&quot;.</p>
<dl>
<dt><code>-u</code></p>
<dd>Just run the update scripts (if updating is enabled).</p>
<dt>With <code>-a</code>, <code>-d</code> or <code>-u</code>:</p>
<dd>if updating is not enabled, schedule a delayed update. The delayed update will be carried out when updates are enabled.</p>
<dt><code>&#8211;enable-updates</code></p>
<dd>Set the flag indicating that <code>resolvconf</code> should run update scripts when invoked in the future with <code>-a</code>, <code>-d</code> or <code>-u</code>. If a delayed update was scheduled then run update scripts.</p>
<dt><code>&#8211;disable-updates</code></p>
<dd>Clear the flag.</p>
<dt><code>&#8211;updates-are-enabled</code></p>
<dd>Return 0 if the flag is set, otherwise return 1.</dl>
<h2>Environment Variables</h2>
<p>The following variables can be set in the configuration file <i>/etc/default/resolvconf</i>. If the file does not exist you will have to create it.</p>
<dl>
<dt><code>REPORT_ABSENT_SYMLINK</code></p>
<dd>If set to &quot;yes&quot; then <code>resolvconf</code> will print a message when <i>/etc/resolv.conf</i> is not a symbolic link to the <code>resolvconf</code>-generated resolver configuration file. Set to &quot;no&quot; to prevent the printing of this message. The default is &quot;yes&quot;.</p>
<dt><code>TRUNCATE_NAMESERVER_LIST_AFTER_LOOPBACK_ADDRESS</code></p>
<dd>If set to &quot;yes&quot; then the <i>libc</i> script will include no more nameserver addresses after the first nameserver address that is a loopback address. (In IPv4 a loopback address is any one that starts with &quot;127.&quot;. In IPv6 the loopback address is &quot;::1&quot;.)</p>
<dd>The advantage of truncating the nameserver list after a loopback address is that doing so inhibits unnecessary changes to <i>resolv.conf </i> and thus reduces the number of instances in which the <i>update-libc.d/</i> scripts have to be run. When an interface is brought up or down the local caching nameserver that listens on the loopback address is still informed of the change and adapts accordingly; the clients of the resolver which use the local caching nameserver do not need to be notified of the change. A disadvantage of this mode of operation is that applications have no secondary or tertiary nameserver address to fall back on should the local caching nameserver crash. Insofar as a local nameserver crash can be regarded as an unlikely event, this is a relatively minor disadvantage. Set to &quot;no&quot; to disable truncation. The default is &quot;yes&quot;.</p>
<dd>A deprecated synonym for this variable is <code>TRUNCATE_NAMESERVER_LIST_AFTER_127</code>.</dl>
<h2>Files</h2>
<dl>
<dt><i>/etc/default/resolvconf</i></p>
<dd>See the ENVIRONMENT VARIABLES section.</p>
<dt><i>/etc/resolvconf/interface-order</i></p>
<dd>Determines the order of precedence of nameserver addresses and search domain names. See above and <code><a href="/docs/linux/man/5-interface-order/">interface-order</a></code>(5).</p>
<dt><i>/etc/resolvconf/resolv.conf.d/base</i></p>
<dd>File containing basic resolver information. The lines in this file are included in the resolver configuration file even when no interfaces are configured.</p>
<dt><i>/etc/resolvconf/resolv.conf.d/head</i></p>
<dd>File to be prepended to the dynamically generated resolver configuration file. Normally this is just a comment line.</p>
<dt><i>/etc/resolvconf/resolv.conf.d/tail</i></p>
<dd>File to be appended to the dynamically generated resolver configuration file. To append nothing, make this an empty file. This file is a good place to put a resolver <code>options</code> line if one is needed, e.g., </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;options inet6</p>
<dt><i>/etc/resolvconf/resolv.conf.d/original</i></p>
<dd>Copy of the <i>/etc/resolv.conf</i> file before the resolvconf package was installed. This file has no effect on the functioning of resolvconf; it is retained so that <i>/etc/resolv.conf</i> can be restored to its original state if the resolvconf package is removed. </p>
<p> Note also that a copy of this file is included in the database until the first reboot after installation of the resolvconf package; this ensures that nameservers reachable before installation of resolvconf are still reachable after installation of resolvconf even though at that point not all suppliers of nameserver information may have supplied their information to <code><a href="/docs/linux/man/8-resolvconf/">resolvconf</a></code>(8). </p>
<p> Note also that the administrator can choose to create a symbolic link in <i>/etc/resolvconf/resolv.conf.d/</i> from <i>tail</i> to <i>original</i> so that the contents of <i>original</i> are always added to the end of the dynamically generated file. </p>
</dl>
<h2>Bugs</h2>
<p>Currently <code>resolvconf</code> does not check the sanity of the information provided to it.</p>
<h2>Author</h2>
<p>Written by Thomas Hood &lt;jdthood [at] gmail.com&gt; with contributions by Nathan Stratton Treadway.</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2004-2013 Thomas Hood.<br />
 This is free software; see the source for copying conditions.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-interface-order/">interface-order</a></code>(5), <code><a href="/docs/linux/man/5-resolv-conf/">resolv.conf</a></code>(5), <code><a href="/docs/linux/man/3-resolver/">resolver</a></code>(3). Read the resolvconf package <i>README</i> file for more in-depth information. </p>
