---
title: "wicd-manager-settings-conf(5)"
name: "wicd-manager-settings-conf"
section: "5"
letter: "w"
url: "/docs/linux/man/5-wicd-manager-settings-conf/"
description: "wicd-manager-settings.conf – contains settings that control Wicd’s behavior"
---

<p>wicd-manager-settings.conf &#8211; contains settings that control Wicd&#8217;s behavior</p>
<h2>Description</h2>
<p>This file contains general configuration information for Wicd.<br />
 This file is located at /etc/wicd/manager-settings.conf </p>
<h2>Settings</h2>
<dl>
<dt><code>link_detect_tool = </code><i>&lt;0|1|2&gt;</i></p>
<dd>0 = autodetect<br />
 1 = ethtool<br />
 2 = mii-tool</p>
<dt><code>flush_tool = </code><i>&lt;0|1|2&gt;</i></p>
<dd>0 = autodetect<br />
 1 = ip<br />
 2 = route</p>
<dt><code>backend = </code><i>&lt;ioctl|external&gt;</i></p>
<dd>Default is ioctl backend.</p>
<dt><code>signal_display_type = </code><i>&lt;0|1&gt;</i></p>
<dd>0 = Show signal strength as a percentage<br />
 1 = Show signal strength in dBm</p>
<dt><code>dhcp_client = </code><i>&lt;0|1|2|3&gt;</i></p>
<dd>0 = autodetect<br />
 1 = dhclient<br />
 2 = dhcpcd<br />
 3 = pump</p>
<dt><code>sudo_app = </code><i>&lt;0|1|2|3&gt;</i></p>
<dd>0 = autodetect<br />
 1 = gksu<br />
 2 = kdesu<br />
 3 = ktsuss</p>
<dt><code>wired_interface = </code><i>&lt;interface_name|None&gt;</i></p>
<dd>
<dt><code>always_show_wired_interface = </code><i>&lt;True|False&gt;</i></p>
<dd>
<dt><code>wired_connect_mode = </code><i>&lt;1|2|3&gt;</i></p>
<dd>1 = default profile<br />
 2 = show list<br />
 3 = last used profile</p>
<dt><code>prefer_wired = </code><i>&lt;True|False&gt;</i></p>
<dd>True = Switch to wired interface if a link is detected, even if already connected to wireless<br />
 False = Do not switch to wired interface automatically</p>
<dt><code>wireless_interface = </code><i>&lt;name_of_wireless_interface|None&gt;</i></p>
<dd>
<dt><code>wpa_driver = </code><i>&lt;wext|madwifi|ndiswrapper|hostap|hermes|atmel|broadcom|ipw|ralink</i><code>legacy|none&gt;</code></p>
<dd>The default (and best supported) is wext. It should work properly in most cases. The <code>none</code> special value makes WICD pass no <i>-D</i> parameter to wpa_supplicant, which might be useful in some cases.</p>
<dt><code>auto_reconnect = </code><i>&lt;True|False&gt;</i></p>
<dd>This settings determines whether Wicd will attempt to reconnect on connection loss.</p>
<dt><code>use_global_dns = </code><i>&lt;True|False&gt;</i></p>
<dd>If set to &quot;True&quot; and values are specified in the global DNS settings below, this will cause Wicd to use these DNS settings.</p>
<dt><code>global_dns_dom = </code><i>&lt;plaintext_domain_name&gt;</i></p>
<dd>This specifies the default search domain to be used by the resolver.</p>
<dt><code>global_dns_1 = </code><i>&lt;ip_address&gt;</i></p>
<dd>
<dt><code>global_dns_2 = </code><i>&lt;ip_address&gt;</i></p>
<dd>
<dt><code>global_dns_3 = </code><i>&lt;ip_address&gt;</i></p>
<dd>
<dt><code>debug_mode = </code><i>&lt;integer_value&gt;</i></p>
<dd>0 = disabled<br />
 1 = enabled </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-wicd/">wicd</a></code>(8), <code><a href="/docs/linux/man/8-wicd-curses/">wicd-curses</a></code>(8), <code><a href="/docs/linux/man/5-wicd-wired-settings-conf/">wicd-wired-settings.conf</a></code>(5), <code><a href="/docs/linux/man/5-wicd-wireless-settings-conf/">wicd-wireless-settings.conf</a></code>(5). </p>
