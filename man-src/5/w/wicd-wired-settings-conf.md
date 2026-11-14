---
title: "wicd-wired-settings-conf(5)"
name: "wicd-wired-settings-conf"
section: "5"
letter: "w"
url: "/docs/linux/man/5-wicd-wired-settings-conf/"
description: "wicd-wired-settings.conf – controls Wicd’s wired network settings"
---

<p>wicd-wired-settings.conf &#8211; controls Wicd&#8217;s wired network settings</p>
<h2>Description</h2>
<p>This file contains configuration information for wired interfaces in Wicd.<br />
 This file is located at /etc/wicd/wired-settings.conf </p>
<h2>Settings</h2>
<dl>
<dt><code>default = </code><i>&lt;0|1&gt;</i></p>
<dd>This option decides whether to use this profile as the default. 0 = do not use this profile as default.<br />
 1 = use this profile as default.</p>
<dt><code>beforescript = </code><i>&lt;None|arbitrary_script&gt;</i></p>
<dd>This defines a script to run before Wicd brings up the connection. The script should be a Bourne-compatible script and should be executable.<br />
 IMPORTANT &#8211; scripts should ONLY be writable by root and located in a directory that is only writable by root.</p>
<dt><code>afterscript = </code><i>&lt;None|arbitrary_script&gt;</i></p>
<dd>This defines a script to run after Wicd brings up the connection. The script should be a Bourne-compatible script and should be executable.<br />
 IMPORTANT &#8211; scripts should ONLY be writable by root and located in a directory that is only writable by root.</p>
<dt><code>predisconnectscript = </code><i>&lt;None|arbitrary_script&gt;</i></p>
<dd>This defines a script to run before Wicd disconnects the interface. The script should be a Bourne-compatible script and should be executable.</p>
<dt><code>postdisconnectscript = </code><i>&lt;None|arbitrary_script&gt;</i></p>
<dd>This defines a script to run after Wicd disconnects the interface. The script should be a Bourne-compatible script and should be executable.<br />
 IMPORTANT &#8211; scripts should ONLY be writable by root and located in a directory that is only writable by root.</p>
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
<dd>True = use the global DNS servers provided in <a href="/docs/linux/man/5-wicd-manager-settings-conf/">wicd-manager-settings.conf</a>(5). This option is only appropriate if &quot;use_static_dns = True&quot;</p>
<dt><code>dns1 = </code><i>&lt;None|ip_address&gt;</i></p>
<dd>Static DNS address if &quot;use_static_dns = True&quot; and &quot;use_global_dns = False&quot;</p>
<dt><code>dns2 = </code><i>&lt;None|ip_address&gt;</i></p>
<dd>Static DNS address if &quot;use_static_dns = True&quot; and &quot;use_global_dns = False&quot;</p>
<dt><code>dns3 = </code><i>&lt;None|ip_address&gt;</i></p>
<dd>Static DNS address if &quot;use_static_dns = True&quot; and &quot;use_global_dns = False&quot; </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-wicd/">wicd</a></code>(8), <code><a href="/docs/linux/man/8-wicd-curses/">wicd-curses</a></code>(8), <code><a href="/docs/linux/man/5-wicd-manager-settings-conf/">wicd-manager-settings.conf</a></code>(5), <code><a href="/docs/linux/man/5-wicd-wireless-settings-conf/">wicd-wireless-settings.conf</a></code>(5). </p>
