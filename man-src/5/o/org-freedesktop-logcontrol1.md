---
title: "org-freedesktop-logcontrol1(5)"
name: "org-freedesktop-logcontrol1"
section: "5"
letter: "o"
url: "/docs/linux/man/5-org-freedesktop-logcontrol1/"
description: "org.freedesktop.LogControl1 – D-Bus interface to query and set logging configuration"
---

<p>org.freedesktop.LogControl1 &#8211; D-Bus interface to query and set logging configuration</p>
<h2>Introduction</h2>
<p>org.freedesktop.LogControl1 is a generic interface that is intended to be used by any daemon which allows the log level and target to be set over D-Bus. It is implemented by various daemons that are part of the <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1) suite. </p>
<p> It is assumed that those settings are global for the whole program, so a fixed object path is used. The interface should always be available under the path /org/freedesktop/LogControl1.</p>
<h2>Description</h2>
<p>The following interface is exposed: </p>
<pre><code>node /org/freedesktop/LogControl1 {
    interface org.freedesktop.LogControl1 {
        properties:
        @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
        @org.freedesktop.systemd1.Privileged(&quot;true&quot;)
        readwrite s LogLevel = '...';
        @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
        @org.freedesktop.systemd1.Privileged(&quot;true&quot;)
        readwrite s LogTarget = '...';
        @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
        readonly s SyslogIdentifier = '...';
    };
    interface org.freedesktop.DBus.Peer { ... };
    interface org.freedesktop.DBus.Introspectable { ... };
    interface org.freedesktop.DBus.Properties { ... };
};


</code></pre>
<h3>Properties</h3>
<p><i>LogLevel</i> describes the <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3)-style log-level, and should be one of &quot;emerg&quot;, &quot;alert&quot;, &quot;crit&quot;, &quot;err&quot;, &quot;warning&quot;, &quot;notice&quot;, &quot;info&quot;, &quot;debug&quot;, in order of increasing verbosity. <i>LogTarget</i> describes the log target (mechanism). It should be one of &quot;console&quot; (log to the console or standard output), &quot;kmsg&quot; (log to the kernel ring buffer), &quot;journal&quot; (log to the journal natively, see <code><a href="/docs/linux/man/8-systemd-journald-service/">systemd-journald.service</a></code>(8)), &quot;syslog&quot; (log using the <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3) call). Those two properties are writable, so they may be set by sufficiently privileged users. <i>SyslogIdentifier</i> is a read-only property that shows the &quot;syslog identifier&quot;. It is a short string that identifies the program that is the source of log messages that is passed to the <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3) call.</p>
<h2>Tools</h2>
<p><code>journalctl</code> option <code>-p</code>/<code>&#8211;priority=</code> may be used to filter log messages by log level, option <code>-t</code>/<code>&#8211;identifier=</code> may be used to by the syslog identifier, and filters like &quot;_TRANSPORT=syslog&quot;, &quot;_TRANSPORT=journal&quot;, and &quot;_TRANSPORT=kernel&quot; may be used to filter messages by the mechanism through which they reached <code>systemd-journald</code>. </p>
<p> <code>systemctl log-level</code> and <code>systemctl log-target</code> verbs may be used to query and set the <i>LogLevel</i> and <i>LogTarget</i> properties of the service manager. <code>systemctl service-log-level</code> and <code>systemctl service-log-target</code> may similarly be used for individual services. (Services must have the <i>BusName=</i> property set and must implement the interface described here. See <code><a href="/docs/linux/man/5-systemd-service/">systemd.service</a></code>(5) for details about <i>BusName=</i>.)</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/1-journalctl/">journalctl</a></code>(1), <code><a href="/docs/linux/man/1-systemctl/">systemctl</a></code>(1), <code><a href="/docs/linux/man/5-systemd-service/">systemd.service</a></code>(5), <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3) </p>
