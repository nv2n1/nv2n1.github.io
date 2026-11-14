---
title: "org-freedesktop-timedate1(5)"
name: "org-freedesktop-timedate1"
section: "5"
letter: "o"
url: "/docs/linux/man/5-org-freedesktop-timedate1/"
description: "org.freedesktop.timedate1 – The D-Bus interface of systemd-timedated"
---

<p>org.freedesktop.timedate1 &#8211; The D-Bus interface of systemd-timedated</p>
<h2>Introduction</h2>
<p><code><a href="/docs/linux/man/8-systemd-timedated-service/">systemd-timedated.service</a></code>(8) is a system service that can be used to control the system time and related settings. This page describes the D-Bus interface.</p>
<h2>The D-Bus Api</h2>
<p>The service exposes the following interfaces on the bus: </p>
<dl>
<dd>
<pre>node /org/freedesktop/timedate1 {
 interface org.freedesktop.timedate1 {
 methods:
 SetTime(in x usec_utc,
 in b relative,
 in b interactive);
 SetTimezone(in s timezone,
 in b interactive);
 SetLocalRTC(in b local_rtc,
 in b fix_system,
 in b interactive);
 SetNTP(in b use_ntp,
 in b interactive);
 ListTimezones(out as timezones);
 properties:
 readonly s Timezone = '...';
 readonly b LocalRTC = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly b CanNTP = ...;
 readonly b NTP = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly b NTPSynchronized = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t TimeUSec = ...;
 @org.freedesktop.DBus.Property.EmitsChangedSignal(&quot;false&quot;)
 readonly t RTCTimeUSec = ...;
 };
 interface org.freedesktop.DBus.Peer { ... };
 interface org.freedesktop.DBus.Introspectable { ... };
 interface org.freedesktop.DBus.Properties { ... };
};</pre>
</dl>
<h3>Methods</h3>
<p>Use <code>SetTime()</code> to change the system clock. Pass a value of microseconds since the UNIX epoch (1 Jan 1970 UTC). If <i>relative</i> is true, the passed usec value will be added to the current system time. If it is false, the current system time will be set to the passed usec value. If the system time is set with this method, the RTC will be updated as well. </p>
<p> Use <code>SetTimezone()</code> to set the system timezone. Pass a value like &quot;Europe/Berlin&quot; to set the timezone. Valid timezones are listed in /usr/share/zoneinfo/zone.tab. If the RTC is configured to be maintained in local time, it will be updated accordingly. </p>
<p> Use <code>SetLocalRTC()</code> to control whether the RTC is in local time or UTC. It is strongly recommended to maintain the RTC in UTC. However, some OSes (Windows) maintain the RTC in local time, which might make it necessary to enable this feature. Note that this might create various problems as daylight changes could be missed. If <i>fix_system</i> is &quot;true&quot;, the time from the RTC is read again and the system clock is adjusted according to the new setting. If <i>fix_system</i> is &quot;false&quot;, the system time is written to the RTC taking the new setting into account. Use <i>fix_system=true</i> in installers and livecds where the RTC is probably more reliable than the system time. Use <i>fix_system=false</i> in configuration UIs that are run during normal operation and where the system clock is probably more reliable than the RTC. </p>
<p> Use <code>SetNTP()</code> to control whether the system clock is synchronized with the network using systemd-timesyncd. This will enable and start or disable and stop the chosen time synchronization service. </p>
<p> <code>ListTimezones()</code> returns a list of time zones known on the local system as an array of names (&quot;[&quot;Africa/Abidjan&quot;, &quot;Africa/Accra&quot;, &#8230;, &quot;UTC&quot;]&quot;).</p>
<h3>Properties</h3>
<p><i>Timezone</i> shows the currently configured time zone. <i>LocalRTC</i> shows whether the RTC is configured to use UTC (false), or the local time zone (true). <i>CanNTP</i> shows whether a service to perform time synchronization over the network is available, and <i>NTP</i> shows whether such a service is enabled. </p>
<p> <i>NTPSynchronized</i> shows whether the kernel reports the time as synchronized (c.f. <code><a href="/docs/linux/man/3-adjtimex/">adjtimex</a></code>(3)). <i>TimeUSec</i> and <i>RTCTimeUSec</i> show the current time on the system and in the RTC. The purpose of those three properties is to allow remote clients to access this information over D-Bus. Local clients can access the information directly. </p>
<p> Whenever the <i>Timezone</i> and <i>LocalRTC</i> settings are changed via the daemon, <code>PropertyChanged</code> signals are sent out to which clients can subscribe. </p>
<p> Note that this service will not inform you about system time changes. Use <code><a href="/docs/linux/man/3-timerfd/">timerfd</a></code>(3) with <code>CLOCK_REALTIME</code> and <code>TFD_TIMER_CANCEL_ON_SET</code> for that.</p>
<h3>Security</h3>
<p>The <i>interactive</i> boolean parameters can be used to control whether m[blue]<code>polkit</code>m[]<font SIZE="-2">[1]</font> should interactively ask the user for authentication credentials if required. </p>
<p> The polkit action for <code>SetTimezone()</code> is org.freedesktop.timedate1.set-timezone. For <code>SetLocalRTC()</code> it is org.freedesktop.timedate1.set-local-rtc, for <code>SetTime()</code> it is org.freedesktop.timedate1.set-time and for <code>SetNTP()</code> it is org.freedesktop.timedate1.set-ntp. <code>ListTimezones()</code> does not require any privileges.</p>
<h2>Examples</h2>
<p><code>Example 1. Introspect org.freedesktop.timedate1 on the bus</code> </p>
<dl>
<dd>
<pre>$ gdbus introspect --system \
 --dest org.freedesktop.timedate1 \
 --object-path /org/freedesktop/timedate1</pre>
</dl>
<h2>Versioning</h2>
<p>These D-Bus interfaces follow m[blue]<code>the usual interface versioning guidelines</code>m[]<font SIZE="-2">[2]</font>.</p>
<h2>See Also</h2>
<p>m[blue]<code>More information on how the system clock and RTC interact</code>m[]<font SIZE="-2">[3]</font></p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>polkit</p>
<dl>
<dd><a rel="nofollow" href="https://www.freedesktop.org/software/polkit/docs/latest/">https://www.freedesktop.org/software/polkit/docs/latest/</a></dl>
<dt> 2.</p>
<dd>the usual interface versioning guidelines</p>
<dl>
<dd><a rel="nofollow" href="http://0pointer.de/blog/projects/versioning-dbus.html">http://0pointer.de/blog/projects/versioning-dbus.html</a></dl>
<dt> 3.</p>
<dd>More information on how the system clock and RTC interact</p>
<dl>
<dd><a rel="nofollow" href="https://lists.freedesktop.org/archives/systemd-devel/2011-May/002526.html">https://lists.freedesktop.org/archives/systemd-devel/2011-May/002526.html</a></dl>
