---
title: "systemd-sleep(8)"
name: "systemd-sleep"
section: "8"
letter: "s"
url: "/docs/linux/man/8-systemd-sleep/"
description: "systemd-suspend.service, systemd-hibernate.service, systemd-hybrid-sleep.service, systemd-suspend-then-hibernate.service, systemd-sleep – System sleep state logic"
---

<p>systemd-suspend.service, systemd-hibernate.service, systemd-hybrid-sleep.service, systemd-suspend-then-hibernate.service, systemd-sleep &#8211; System sleep state logic</p>
<h2>Synopsis</h2>
<p>systemd-suspend.service </p>
<p> systemd-hibernate.service </p>
<p> systemd-hybrid-sleep.service </p>
<p> systemd-suspend-then-hibernate.service </p>
<p> /lib/systemd/system-sleep</p>
<h2>Description</h2>
<p>systemd-suspend.service is a system service that is pulled in by suspend.target and is responsible for the actual system suspend. Similarly, systemd-hibernate.service is pulled in by hibernate.target to execute the actual hibernation. Finally, systemd-hybrid-sleep.service is pulled in by hybrid-sleep.target to execute hybrid hibernation with system suspend and pulled in by suspend-then-hibernate.target to execute system suspend with a timeout that will activate hibernate later. </p>
<p> Immediately before entering system suspend and/or hibernation systemd-suspend.service (and the other mentioned units, respectively) will run all executables in /lib/systemd/system-sleep/ and pass two arguments to them. The first argument will be &quot;pre&quot;, the second either &quot;suspend&quot;, &quot;hibernate&quot;, &quot;hybrid-sleep&quot;, or &quot;suspend-then-hibernate&quot; depending on the chosen action. An environment variable called &quot;SYSTEMD_SLEEP_ACTION&quot; will be set and contain the sleep action that is processing. This is primarily helpful for &quot;suspend-then-hibernate&quot; where the value of the variable will be &quot;suspend&quot;, &quot;hibernate&quot;, or &quot;suspend-after-failed-hibernate&quot; in cases where hibernation has failed. Immediately after leaving system suspend and/or hibernation the same executables are run, but the first argument is now &quot;post&quot;. All executables in this directory are executed in parallel, and execution of the action is not continued until all executables have finished. </p>
<p> Note that scripts or binaries dropped in /lib/systemd/system-sleep/ are intended for local use only and should be considered hacks. If applications want to react to system suspend/hibernation and resume, they should rather use the m[blue]<code>Inhibitor interface</code>m[]<font SIZE="-2">[1]</font>. </p>
<p> Note that systemd-suspend.service, systemd-hibernate.service, systemd-hybrid-sleep.service, and systemd-suspend-then-hibernate.service should never be executed directly. Instead, trigger system sleep with a command such as <code>systemctl suspend</code> or <code>systemctl hibernate</code>. </p>
<p> Internally, this service will echo a string like &quot;mem&quot; into /sys/power/state, to trigger the actual system suspend. What exactly is written where can be configured in the [Sleep] section of /etc/systemd/sleep.conf or a sleep.conf.d file. See <code><a href="/docs/linux/man/5-systemd-sleep-conf/">systemd-sleep.conf</a></code>(5).</p>
<h2>Options</h2>
<p><code>systemd-sleep</code> understands the following commands: </p>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dd>Print a short help text and exit.</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dd>Print a short version string and exit.</dl>
<p> <code>suspend</code>, <code>hibernate</code>, <code>suspend-then-hibernate</code>, <code>hybrid-sleep</code></p>
<dl>
<dd>Suspend, hibernate, suspend then hibernate, or put the system to hybrid sleep.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-systemd-sleep-conf/">systemd-sleep.conf</a></code>(5), <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/1-systemctl/">systemctl</a></code>(1), <code><a href="/docs/linux/man/7-systemd-special/">systemd.special</a></code>(7), <code><a href="/docs/linux/man/8-systemd-halt-service/">systemd-halt.service</a></code>(8)</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>Inhibitor interface</p>
<dl>
<dd><a rel="nofollow" href="https://www.freedesktop.org/wiki/Software/systemd/inhibit">https://www.freedesktop.org/wiki/Software/systemd/inhibit</a></dl>
