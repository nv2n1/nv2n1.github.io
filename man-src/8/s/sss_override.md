---
title: "sss_override(8)"
name: "sss_override"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sss_override/"
description: "sss_override – create local overrides of user and group attributes"
---

<p>sss_override &#8211; create local overrides of user and group attributes</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>sss_override</code> <i>COMMAND</i> [<i>options</i>]</dl>
<h2>Description</h2>
<p><code>sss_override</code></p>
<dd>enables to create a client-side view and allows to change selected values of specific user and groups. This change takes effect only on local machine. </p>
<p> Overrides data are stored in the SSSD cache. If the cache is deleted, all local overrides are lost. Please note that after the first override is created using any of the following <i>user-add</i>, <i>group-add</i>, <i>user-import</i> or <i>group-import</i> command. SSSD needs to be restarted to take effect. <i>sss_override</i> prints message when a restart is required.</p>
<h2>Available Commands</h2>
<p>Argument <i>NAME</i> is the name of original object in all commands. It is not possible to override <i>uid</i> or <i>gid</i> to 0. </p>
<p> <code>user-add</code> <i>NAME</i> [<code>-n,&#8211;name</code> NAME] [<code>-u,&#8211;uid</code> UID] [<code>-g,&#8211;gid</code> GID] [<code>-h,&#8211;home</code> HOME] [<code>-s,&#8211;shell</code> SHELL] [<code>-c,&#8211;gecos</code> GECOS] [<code>-x,&#8211;certificate</code> BASE64 ENCODED CERTIFICATE]</p>
<dl>
<dd>Override attributes of an user. Please be aware that calling this command will replace any previous override for the (NAMEd) user.</dl>
<p> <code>user-del</code> <i>NAME</i></p>
<dl>
<dd>Remove user overrides. However be aware that overridden attributes might be returned from memory cache. Please see SSSD option <i>memcache_timeout</i> for more details.</dl>
<p> <code>user-find</code> [<code>-d,&#8211;domain</code> DOMAIN]</p>
<dl>
<dd>List all users with set overrides. If <i>DOMAIN</i> parameter is set, only users from the domain are listed.</dl>
<p> <code>user-show</code> <i>NAME</i></p>
<dl>
<dd>Show user overrides.</dl>
<p> <code>user-import</code> <i>FILE</i></p>
<dl>
<dd>Import user overrides from <i>FILE</i>. Data format is similar to standard passwd file. The format is: </p>
<p> original_name:name:uid:gid:gecos:home:shell:base64_encoded_certificate </p>
<p> where original_name is original name of the user whose attributes should be overridden. The rest of fields correspond to new values. You can omit a value simply by leaving corresponding field empty. </p>
<p> Examples: </p>
<p> ckent:superman:::::: </p>
<p> ckent [at] krypton.com::501:501:Superman:/home/earth:/bin/bash:</dl>
<p> <code>user-export</code> <i>FILE</i></p>
<dl>
<dd>Export all overridden attributes and store them in <i>FILE</i>. See <i>user-import</i> for data format.</dl>
<p> <code>group-add</code> <i>NAME</i> [<code>-n,&#8211;name</code> NAME] [<code>-g,&#8211;gid</code> GID]</p>
<dl>
<dd>Override attributes of a group. Please be aware that calling this command will replace any previous override for the (NAMEd) group.</dl>
<p> <code>group-del</code> <i>NAME</i></p>
<dl>
<dd>Remove group overrides. However be aware that overridden attributes might be returned from memory cache. Please see SSSD option <i>memcache_timeout</i> for more details.</dl>
<p> <code>group-find</code> [<code>-d,&#8211;domain</code> DOMAIN]</p>
<dl>
<dd>List all groups with set overrides. If <i>DOMAIN</i> parameter is set, only groups from the domain are listed.</dl>
<p> <code>group-show</code> <i>NAME</i></p>
<dl>
<dd>Show group overrides.</dl>
<p> <code>group-import</code> <i>FILE</i></p>
<dl>
<dd>Import group overrides from <i>FILE</i>. Data format is similar to standard group file. The format is: </p>
<p> original_name:name:gid </p>
<p> where original_name is original name of the group whose attributes should be overridden. The rest of fields correspond to new values. You can omit a value simply by leaving corresponding field empty. </p>
<p> Examples: </p>
<p> admins:administrators: </p>
<p> Domain Users:Users:501</dl>
<p> <code>group-export</code> <i>FILE</i></p>
<dl>
<dd>Export all overridden attributes and store them in <i>FILE</i>. See <i>group-import</i> for data format.</dl>
<h2>Common Options</h2>
<p>Those options are available with all commands. </p>
<p> <code>&#8211;debug</code> <i>LEVEL</i></p>
<dl>
<dd>SSSD supports two representations for specifying the debug level. The simplest is to specify a decimal value from 0-9, which represents enabling that level and all lower-level debug messages. The more comprehensive option is to specify a hexadecimal bitmask to enable or disable specific levels (such as if you wish to suppress a level). </p>
<p> Please note that each SSSD service logs into its own log file. Also please note that enabling &#8220;debug_level&#8221; in the &#8220;[sssd]&#8221; section only enables debugging just for the sssd process itself, not for the responder or provider processes. The &#8220;debug_level&#8221; parameter should be added to all sections that you wish to produce debug logs from. </p>
<p> In addition to changing the log level in the config file using the &#8220;debug_level&#8221; parameter, which is persistent, but requires SSSD restart, it is also possible to change the debug level on the fly using the <code><a href="/docs/linux/man/8-sss_debuglevel/">sss_debuglevel</a></code>(8) tool. </p>
<p> Currently supported debug levels: </p>
<p> <i>0</i>, <i>0x0010</i>: Fatal failures. Anything that would prevent SSSD from starting up or causes it to cease running. </p>
<p> <i>1</i>, <i>0x0020</i>: Critical failures. An error that doesn&#8217;t kill the SSSD, but one that indicates that at least one major feature is not going to work properly. </p>
<p> <i>2</i>, <i>0x0040</i>: Serious failures. An error announcing that a particular request or operation has failed. </p>
<p> <i>3</i>, <i>0x0080</i>: Minor failures. These are the errors that would percolate down to cause the operation failure of 2. </p>
<p> <i>4</i>, <i>0x0100</i>: Configuration settings. </p>
<p> <i>5</i>, <i>0x0200</i>: Function data. </p>
<p> <i>6</i>, <i>0x0400</i>: Trace messages for operation functions. </p>
<p> <i>7</i>, <i>0x1000</i>: Trace messages for internal control functions. </p>
<p> <i>8</i>, <i>0x2000</i>: Contents of function-internal variables that may be interesting. </p>
<p> <i>9</i>, <i>0x4000</i>: Extremely low-level tracing information. </p>
<p> To log required bitmask debug levels, simply add their numbers together as shown in following examples: </p>
<p> <i>Example</i>: To log fatal failures, critical failures, serious failures and function data use 0x0270. </p>
<p> <i>Example</i>: To log fatal failures, configuration settings, function data, trace messages for internal control functions use 0x1310. </p>
<p> <i>Note</i>: The bitmask format of debug levels was introduced in 1.7.0. </p>
<p> <i>Default</i>: 0</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-sssd/">sssd</a></code>(8), <code><a href="/docs/linux/man/5-sssd-conf/">sssd.conf</a></code>(5), <code><a href="/docs/linux/man/5-sssd-ldap/">sssd-ldap</a></code>(5), <code><a href="/docs/linux/man/5-sssd-krb5/">sssd-krb5</a></code>(5), <code><a href="/docs/linux/man/5-sssd-simple/">sssd-simple</a></code>(5), <code><a href="/docs/linux/man/5-sssd-ipa/">sssd-ipa</a></code>(5), <code><a href="/docs/linux/man/5-sssd-ad/">sssd-ad</a></code>(5), <code><a href="/docs/linux/man/5-sssd-sudo/">sssd-sudo</a></code>(5),<code><a href="/docs/linux/man/8-sss_cache/">sss_cache</a></code>(8), <code><a href="/docs/linux/man/8-sss_debuglevel/">sss_debuglevel</a></code>(8), <code><a href="/docs/linux/man/8-sss_groupadd/">sss_groupadd</a></code>(8), <code><a href="/docs/linux/man/8-sss_groupdel/">sss_groupdel</a></code>(8), <code><a href="/docs/linux/man/8-sss_groupshow/">sss_groupshow</a></code>(8), <code><a href="/docs/linux/man/8-sss_groupmod/">sss_groupmod</a></code>(8), <code><a href="/docs/linux/man/8-sss_useradd/">sss_useradd</a></code>(8), <code><a href="/docs/linux/man/8-sss_userdel/">sss_userdel</a></code>(8), <code><a href="/docs/linux/man/8-sss_usermod/">sss_usermod</a></code>(8), <code><a href="/docs/linux/man/8-sss_obfuscate/">sss_obfuscate</a></code>(8), <code><a href="/docs/linux/man/8-sss_seed/">sss_seed</a></code>(8), <code><a href="/docs/linux/man/8-sssd_krb5_locator_plugin/">sssd_krb5_locator_plugin</a></code>(8), <code><a href="/docs/linux/man/8-sss_ssh_authorizedkeys/">sss_ssh_authorizedkeys</a></code>(8), <code><a href="/docs/linux/man/8-sss_ssh_knownhostsproxy/">sss_ssh_knownhostsproxy</a></code>(8),<code><a href="/docs/linux/man/5-sssd-ifp/">sssd-ifp</a></code>(5),<code><a href="/docs/linux/man/8-pam_sss/">pam_sss</a></code>(8). <code><a href="/docs/linux/man/5-sss_rpcidmapd/">sss_rpcidmapd</a></code>(5)</p>
<h2>Authors</h2>
<p><code>The SSSD upstream &#8211; <a rel="nofollow" href="http://fedorahosted.org/sssd">http://fedorahosted.org/sssd</a></code></p>
