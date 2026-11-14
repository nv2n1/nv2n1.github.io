---
title: "wicd-wireless-settings-conf(5)"
name: "wicd-wireless-settings-conf"
section: "5"
letter: "w"
url: "/docs/linux/man/5-wicd-wireless-settings-conf/"
description: "wicd-wired-settings.conf – controls Wicd’s wireless network settings"
---

<p>wicd-wired-settings.conf &#8211; controls Wicd&#8217;s wireless network settings</p>
<h2>Description</h2>
<p>This file contains configuration information for wireless interfaces in Wicd.<br />
 This file is located at /etc/wicd/wireless-settings.conf </p>
<h2>Settings</h2>
<dl>
<dt><code>bssid = </code><i>&lt;BSSID_of_network&gt;</i></p>
<dd>This value can be found using <a href="/docs/linux/man/8-iwconfig/">iwconfig</a>(8).</p>
<dt><code>essid = </code><i>&lt;ESSID_of_network&gt;</i></p>
<dd>This value can be found using <a href="/docs/linux/man/8-iwconfig/">iwconfig</a>(8).</p>
<dt><code>hidden = </code><i>&lt;True|False&gt;</i></p>
<dd>This option notes whether the network&#8217;s ESSID is broadcast or not.</p>
<dt><code>channel = </code><i>&lt;integer_value&gt;</i></p>
<dd>Valid channels are dependent upon country.<br />
 This value can be found using <a href="/docs/linux/man/8-iwconfig/">iwconfig</a>(8).</p>
<dt><code>mode = </code><i>&lt;Master|Ad-hoc&gt;</i></p>
<dd>This value can be found using <a href="/docs/linux/man/8-iwconfig/">iwconfig</a>(8).</p>
<dt><code>enctype = </code><i>&lt;encryption_template&gt;</i></p>
<dd>This can take the value of any encryption template shown in /etc/wicd/encryption/templates/.</p>
<dt><code>encryption_method = WEP|WPA|WPA2&gt;</code></p>
<dd>This value can be found using <a href="/docs/linux/man/8-iwconfig/">iwconfig</a>(8).</p>
<dt><code>key = </code><i>&lt;plain_text_key&gt;</i></p>
<dd>Be sure this file is readable only by root.</p>
<dt><code>automatic = </code><i>&lt;True|False&gt;</i></p>
<dd>This option determines whether Wicd should automatically connect to this network.</p>
<dt><code>ip = </code><i>&lt;None|ip_address&gt;</i></p>
<dd>Use this option if you have a static ip address for your system.</p>
<dt><code>netmask = </code><i>&lt;None|network</i><code>mask&gt;</code></p>
<dd>This setting is only appropriate if a static ip address is configured above.</p>
<dt><code>broadcast = </code><i>&lt;None|broadcast_address&gt;</i></p>
<dd>This setting is only appropriate if a static ip address is configured above.</p>
<dt><code>gateway = </code><i>&lt;None|gateway_address&gt;</i></p>
<dd>This setting is only appropriate if a static ip address is configured above.</p>
<dt><code>use_static_dns = </code><i>&lt;True|False&gt;</i></p>
<dd>True = use static DNS servers instead of accepting what the dhcp server supplies.</p>
<dt><code>use_global_dns = </code><i>&lt;True|False&gt;</i></p>
<dd>True = use the global DNS servers provided in <a href="/docs/linux/man/5-wicd-manager-settings-conf/">wicd-manager-settings.conf</a>(5).<br />
 This option is only appropriate if &quot;use_static_dns = True&quot;</p>
<dt><code>dns1 = </code><i>&lt;None|ip_address&gt;</i></p>
<dd>Static DNS address if &quot;use_static_dns = True&quot; and &quot;use_global_dns = False&quot;</p>
<dt><code>dns2 = </code><i>&lt;None|ip_address&gt;</i></p>
<dd>Static DNS address if &quot;use_static_dns = True&quot; and &quot;use_global_dns = False&quot;</p>
<dt><code>dns3 = </code><i>&lt;None|ip_address&gt;</i></p>
<dd>Static DNS address if &quot;use_static_dns = True&quot; and &quot;use_global_dns = False&quot;</p>
<dt><code>use_settings_globally = </code><i>&lt;0|1&gt;</i></p>
<dd>Wicd keeps track of whether to autoconnect to networks based on bssid. This ensures that you don&#8217;t accidentally connect to another network that is not yours but happens to have the same essid &#8211; for example, there are a lot of commercial routers in use with &quot;linksys&quot; as the essid.<br />
 0 = Do not use settings globally<br />
 1 = Use settings globally</p>
<dt><code>beforescript = </code><i>&lt;None|arbitrary_script&gt;</i></p>
<dd>This defines a script to run before Wicd brings up the connection.<br />
 IMPORTANT &#8211; scripts should ONLY be writable by root and should be located in a directory that is writable by only root.</p>
<dt><code>afterscript = </code><i>&lt;None|arbitrary_script&gt;</i></p>
<dd>This defines a script to run after Wicd brings up the connection.<br />
 IMPORTANT &#8211; scripts should ONLY be writable by root and located in a directory that is writable by only root.</p>
<dt><code>predisconnectscript = </code><i>&lt;None|arbitrary_script&gt;</i></p>
<dd>This defines a script to run before Wicd disconnects the interface.</p>
<dt><code>postdisconnectscript = </code><i>&lt;None|arbitrary_script&gt;</i></p>
<dd>This defines a script to run after Wicd disconnects the interface.<br />
 IMPORTANT &#8211; scripts should ONLY be writable by root and located in a directory that is writable by only root. </p>
</dl>
<h2>Other</h2>
<p>The &quot;use_settings_globally&quot; option determines how an individual network&#8217;s configuration stanza starts. If the option is &quot;0&quot; (do not use settings globally), then the stanza&#8217;s top line will be the bssid of the access point (in this format):<br />
 [00:15:3E:87:D3:68]<br />
 If the &quot;option is set to &quot;1&quot; (use settings globally), then the first line of the stanza will be in this format:<br />
 [essid:UA Public Wireless Network]</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-wicd/">wicd</a></code>(8), <code><a href="/docs/linux/man/8-wicd-curses/">wicd-curses</a></code>(8), <code><a href="/docs/linux/man/5-wicd-manager-settings-conf/">wicd-manager-settings.conf</a></code>(5), <code><a href="/docs/linux/man/5-wicd-wired-settings-conf/">wicd-wired-settings.conf</a></code>(5). </p>
