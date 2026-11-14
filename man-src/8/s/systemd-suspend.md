---
title: "systemd-suspend(8)"
name: "systemd-suspend"
section: "8"
letter: "s"
url: "/docs/linux/man/8-systemd-suspend/"
description: "systemd-suspend.service, systemd-hibernate.service, systemd-hybrid-sleep.service, systemd-sleep – System sleep state logic"
---

<p>systemd-suspend.service, systemd-hibernate.service, systemd-hybrid-sleep.service, systemd-sleep &#8211; System sleep state logic</p>
<h2>Synopsis</h2>
<p>systemd-suspend.service </p>
<p> systemd-hibernate.service </p>
<p> systemd-hybrid-sleep.service </p>
<p> /usr/lib/systemd/system-sleep</p>
<h2>Description</h2>
<p>systemd-suspend.service is a system service that is pulled in by suspend.target and is responsible for the actual system suspend. Similarly, systemd-hibernate.service is pulled in by hibernate.target to execute the actual hibernation. Finally, systemd-hybrid-sleep.service is pulled in by hybrid-sleep.target to execute hybrid hibernation with system suspend. </p>
<p> Immediately before entering system suspend and/or hibernation systemd-suspend.service (and the other mentioned units, respectively) will run all executables in /usr/lib/systemd/system-sleep/ and pass two arguments to them. The first argument will be &quot;pre&quot;, the second either &quot;suspend&quot;, &quot;hibernate&quot;, or &quot;hybrid-sleep&quot; depending on the chosen action. Immediately after leaving system suspend and/or hibernation the same executables are run, but the first argument is now &quot;post&quot;. All executables in this directory are executed in parallel, and execution of the action is not continued until all executables have finished. </p>
<p> Note that scripts or binaries dropped in /usr/lib/systemd/system-sleep/ are intended for local use only and should be considered hacks. If applications want to be notified of system suspend/hibernation and resume, there are much nicer interfaces available. </p>
<p> Note that systemd-suspend.service, systemd-hibernate.service, and systemd-hybrid-sleep.service should never be executed directly. Instead, trigger system sleep states with a command such as &quot;systemctl suspend&quot; or similar. </p>
<p> Internally, this service will echo a string like &quot;mem&quot; into /sys/power/state, to trigger the actual system suspend. What exactly is written where can be configured in the &quot;[Sleep]&quot; section of /etc/systemd/sleep.conf. See <code><a href="/docs/linux/man/5-systemd-sleep-conf/">systemd-sleep.conf</a></code>(5).</p>
<h2>Options</h2>
<p><code>systemd-sleep</code> understands the following commands: </p>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dd>Print a short help text and exit.</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dd>Print a short version string and exit.</dl>
<p> <code>suspend</code>, <code>hibernate</code>, <code>hybrid-sleep</code></p>
<dl>
<dd>Suspend, hibernate, or put the system to hybrid sleep.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-systemd-sleep-conf/">systemd-sleep.conf</a></code>(5), <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/1-systemctl/">systemctl</a></code>(1), <code><a href="/docs/linux/man/7-systemd-special/">systemd.special</a></code>(7), <code><a href="/docs/linux/man/8-systemd-halt-service/">systemd-halt.service</a></code>(8) </p>
