---
title: "locale-conf(5)"
name: "locale-conf"
section: "5"
letter: "l"
url: "/docs/linux/man/5-locale-conf/"
description: "locale.conf – Configuration file for locale settings"
---

<p>locale.conf &#8211; Configuration file for locale settings</p>
<h2>Synopsis</h2>
<p>/etc/locale.conf</p>
<h2>Description</h2>
<p>The /etc/locale.conf file configures system-wide locale settings. It is read at early boot by <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1). </p>
<p> The basic file format of locale.conf is a newline-separated list of environment-like shell-compatible variable assignments. It is possible to source the configuration from shell scripts, however, beyond mere variable assignments, no shell features are supported, allowing applications to read the file without implementing a shell compatible execution engine. </p>
<p> Note that the kernel command line options <i>locale.LANG=</i>, <i>locale.LANGUAGE=</i>, <i>locale.LC_CTYPE=</i>, <i>locale.LC_NUMERIC=</i>, <i>locale.LC_TIME=</i>, <i>locale.LC_COLLATE=</i>, <i>locale.LC_MONETARY=</i>, <i>locale.LC_MESSAGES=</i>, <i>locale.LC_PAPER=</i>, <i>locale.LC_NAME=</i>, <i>locale.LC_ADDRESS=</i>, <i>locale.LC_TELEPHONE=</i>, <i>locale.LC_MEASUREMENT=</i>, <i>locale.LC_IDENTIFICATION=</i> may be used to override the locale settings at boot. </p>
<p> The locale settings configured in /etc/locale.conf are system-wide and are inherited by every service or user, unless overridden or unset by individual programs or individual users. </p>
<p> Depending on the operating system, other configuration files might be checked for locale configuration as well, however only as fallback. </p>
<p> /etc/locale.conf is usually created and updated using <code><a href="/docs/linux/man/8-systemd-localed-service/">systemd-localed.service</a></code>(8). <code><a href="/docs/linux/man/1-localectl/">localectl</a></code>(1) may be used to alter the settings in this file during runtime from the command line. Use <code><a href="/docs/linux/man/1-systemd-firstboot/">systemd-firstboot</a></code>(1) to initialize them on mounted (but not booted) system images.</p>
<h2>Options</h2>
<p>The following locale settings may be set using /etc/locale.conf: <i>LANG=</i>, <i>LANGUAGE=</i>, <i>LC_CTYPE=</i>, <i>LC_NUMERIC=</i>, <i>LC_TIME=</i>, <i>LC_COLLATE=</i>, <i>LC_MONETARY=</i>, <i>LC_MESSAGES=</i>, <i>LC_PAPER=</i>, <i>LC_NAME=</i>, <i>LC_ADDRESS=</i>, <i>LC_TELEPHONE=</i>, <i>LC_MEASUREMENT=</i>, <i>LC_IDENTIFICATION=</i>. Note that <i>LC_ALL</i> may not be configured in this file. For details about the meaning and semantics of these settings, refer to <code><a href="/docs/linux/man/7-locale/">locale</a></code>(7).</p>
<h2>Example</h2>
<p><code>Example 1. German locale with English messages</code> </p>
<p> /etc/locale.conf: </p>
<dl>
<dd>
<pre>LANG=de_DE.UTF-8
LC_MESSAGES=en_US.UTF-8</pre>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/7-locale/">locale</a></code>(7), <code><a href="/docs/linux/man/1-localectl/">localectl</a></code>(1), <code><a href="/docs/linux/man/8-systemd-localed-service/">systemd-localed.service</a></code>(8), <code><a href="/docs/linux/man/1-systemd-firstboot/">systemd-firstboot</a></code>(1) </p>
