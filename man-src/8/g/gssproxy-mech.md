---
title: "gssproxy-mech(8)"
name: "gssproxy-mech"
section: "8"
letter: "g"
url: "/docs/linux/man/8-gssproxy-mech/"
description: "gssproxy-mech – GssProxy GSSAPI mechanism plugin"
---

<p>gssproxy-mech &#8211; GssProxy GSSAPI mechanism plugin</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>proxymech_v1 2.16.840.1.113730.3.8.15.1 /usr/lib64/gssproxy/proxymech.so </code> [<i>options</i>]</dl>
<h2>Description</h2>
<dd>The gssproxy proxymech module is a interposer plugin that is loaded by GSSAPI. It is enabled by /etc/gss/mech configuration file. </p>
<p> The interposer plugin allows to intercept the entire GSSAPI communication and detour to the <code>gssproxy</code> daemon. When the interposer plugin is installed two other conditions need to be met in order to activate it: </p>
<p> a) interposer configuration file</p>
<dl>
<dd>The plugin needs to be manually enabled in the /etc/gss/mech file.</dl>
<p> b) gssproxy environment variable</p>
<dl>
<dd>The interposer plugin will not forward to the gssproxy daemon unless the environment variable named <i>GSS_USE_PROXY=yes</i> is set.</dl>
<p> Furthermore, the interposer plugin can be configured to behave in different ways when called from the GSSAPI. This behavior is controlled via the <i>GSSPROXY_BEHAVIOR</i> environment variable. It accepts four different values: </p>
<p> LOCAL_ONLY</p>
<dl>
<dd>All commands received with this setting will cause to immediately reenter the GSSAPI w/o any interaction with the gssproxy daemon. When the request cannot be processed it will just fail.</dl>
<p> LOCAL_FIRST</p>
<dl>
<dd>All commands received with this setting will cause to immediately reenter the GSSAPI. When the local GSSAPI cannot process the request, it will resend the request to the gssproxy daemon.</dl>
<p> REMOTE_FIRST</p>
<dl>
<dd>All commands received with this setting will be forwarded to the gssproxy daemon first. If the request cannot be handled there, the request will reenter the local GSSAPI.</dl>
<p> REMOTE_ONLY</p>
<dl>
<dd>This setting is currently not fully implemented and therefor not supported.</dl>
<p> The default setting for <i>GSSPROXY_BEHAVIOR</i> is REMOTE_FIRST. </p>
<p> Finally the interposer may need to use a special per-service socket in order to communicate with gssproxy. The path to this socket is set via the <i>GSSPROXY_SOCKET</i> environment variable.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-gssproxy-conf/">gssproxy.conf</a></code>(5) and <code><a href="/docs/linux/man/8-gssproxy/">gssproxy</a></code>(8).</p>
<h2>Authors</h2>
<p><code>GSS-Proxy &#8211; <a rel="nofollow" href="http://fedorahosted.org/gss-proxy">http://fedorahosted.org/gss-proxy</a></code></p>
