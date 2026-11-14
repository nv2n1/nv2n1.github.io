---
title: "eurephia-variables(7)"
name: "eurephia-variables"
section: "7"
letter: "e"
url: "/docs/linux/man/7-eurephia-variables/"
description: "Overview over all eurephia configuration variables. These variables are stored in the database and can be modified by the eurephiadm config command."
---

<p>Overview over all eurephia configuration variables. These variables are stored in the database and can be modified by the <code>eurephiadm config</code> command.</p>
<h2>Password Hash</h2>
<p>These variables are related to the password hash configuration. All of them must be set, but they can be changed over time without affecting the functionality of the already stored passwords.</p>
<dl>
<dt>These parameters are the first to be set when <code>eurephia_init</code> is run. The minimum and maximum hash rounds are bechmarked for you with this tool to find more suitable numbers for the hardware eurephia will be running on.</p>
<dd>
<dt><code>passwordhash_salt_length</code></p>
<dd>Sets number of bytes to use for the password hash salt.</p>
<dt><code>passwordhash_rounds_min</code></p>
<dd>Sets the minimum number of hashing rounds to perform when calculating new password hashes.</p>
<dt><code>passwordhash_rounds_max</code></p>
<dd>Sets the maximum number of hashing rounds to perform when calculating new password hashes</dl>
<h2>Attempts Settings</h2>
<p>eurephia can blacklist user names, certificates and IP addresses based on number of failed attempts. The following parameters defines the limits of how many attempts you are willing to allow before blacklisting them.</p>
<dl>
<dt><code>allow_cert_attempts</code></p>
<dd>Defines the number of attempts of failed login attempts you allow before you will blacklist the OpenVPN clients cerrtificate. This number should normally be higher than <code>allow_username_attempts</code>. Default is 5.</p>
<dt><code>allow_username_attempts</code></p>
<dd>Defines the number of failed ttempts for a user name can be tried before you will blacklist the user name from further attempts. Default is 3.</p>
<dt><code>allow_ipaddr_attempts</code></p>
<dd>Defines the number of failed attempts for an IP address to be used before you will blacklist the IP address from further attempts. This one should be the least strictest limit. You also need to consider if your clients will log in via a proxy or NATed network and how many of your clients will do so. If you experience many users failing to log on and more of them are behind the same proxy or NAT gateway, this may blacklist the IP address quicker than intended. But if among many failing attempts a valid authentication happens, the attempts counter will be reset again, so this limit do not need to be too forgiving. Default is 10.</dl>
<h2>Firewall Integration</h2>
<p>If you are running the OpenVPN server with eurephia on a Linux server, it is possible to let eurephia interact with the firewall as well. These settings will enable the firewall integration and tell eurephia how to interact with the firewall. These parameters are very <code>iptables</code> oriented. The <code>iptables</code> firewall module must be enabled at compile time and be installed to work.</p>
<dl>
<dt><code>firewall_interface</code></p>
<dd>This is the variable which enables firewall integration. This variable must point at the firewall driver, which is a shared object file which eurephia will load dynamically. These drivers are prefixed <code>efw</code> and will be found in the same <code>lib</code> or <code>lib64</code> directory as the <code>eurephia-auth</code> and <code>edb-sqlite</code> modules. The variable must contain the full path to the driver module.</p>
<dt><code>firewall_command</code></p>
<dd>This defines the binary the firewall module will execute to help update the firewall. For <code>iptables</code> this defaults to <code>/sbin/iptables</code>.</p>
<dt><code>firewall_destination</code></p>
<dd>Defines which predefined firewall rule to use when updating the firewall. The default value is <code>vpn_users</code>.</p>
<dt><code>firewall_blacklist_destination</code></p>
<dd>This activates firewall based IP address blacklisting in addition to the internal blacklist in eurephia. This variable defines which firewall rule to use when wanting to blacklist an IP address.</p>
<dt><code>firewall_blacklist_send_to</code></p>
<dd>This is an optional parameter. Normally when eurephia blacklists an IP address it will default to drop the network packets from that client. You can use this variable to send it to a different firewall target. This is useful if you to, for example, log the incident to the system log before dropping the packets.</dl>
<h2>Eurephia Utilities</h2>
<p>These settings are used by the eurephia administration utility, <code>eurephiadm</code>.</p>
<dl>
<dt><code>eurephiadmin_autologout</code></p>
<dd>This defines how long a eurephia administration utility may have an open session before it is considered inactive. When exceeding this limit, the administrator user will be out automatically. The unit for this setting is minutes and the default value is 10.</p>
<dt><code>eurephiadm_xslt_path</code></p>
<dd>The <code>eurephiadm</code> utility uses XSLT templates for generating the output to the screen. This variable gives you the possibility to have your own set of templates in a different directory instead of using the system wide XSLT templates installed by default. This variable is not set by default.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-eurephiadm-config/">eurephiadm-config</a></code>(7), <code><a href="/docs/linux/man/7-eurephia_init/">eurephia_init</a></code>(7),<br />
 Administrators Tutorial and Manual</p>
<h2>Author</h2>
<p>Copyright (C) 2008-2010 David Sommerseth &lt;dazo [at] users.sourceforge.net&gt;</p>
