---
title: "systemd-timer(5)"
name: "systemd-timer"
section: "5"
letter: "s"
url: "/docs/linux/man/5-systemd-timer/"
description: "systemd.timer – Timer unit configuration"
---

<p>systemd.timer &#8211; Timer unit configuration</p>
<h2>Synopsis</h2>
<p><i>timer</i>.timer</p>
<h2>Description</h2>
<p>A unit configuration file whose name ends in &quot;.timer&quot; encodes information about a timer controlled and supervised by systemd, for timer-based activation. </p>
<p> This man page lists the configuration options specific to this unit type. See <code><a href="/docs/linux/man/5-systemd-unit/">systemd.unit</a></code>(5) for the common options of all unit configuration files. The common configuration items are configured in the generic [Unit] and [Install] sections. The timer specific configuration options are configured in the [Timer] section. </p>
<p> For each timer file, a matching unit file must exist, describing the unit to activate when the timer elapses. By default, a service by the same name as the timer (except for the suffix) is activated. Example: a timer file foo.timer activates a matching service foo.service. The unit to activate may be controlled by <i>Unit=</i> (see below). </p>
<p> Note that in case the unit to activate is already active at the time the timer elapses it is not restarted, but simply left running. There is no concept of spawning new service instances in this case. Due to this, services with <i>RemainAfterExit=</i> set (which stay around continuously even after the service&#8217;s main process exited) are usually not suitable for activation via repetitive timers, as they will only be activated once, and then stay around forever.</p>
<h2>Automatic Dependencies</h2>
<h3>Implicit Dependencies</h3>
<p>The following dependencies are implicitly added: </p>
<dl>
<dd>&bull; Timer units automatically gain a <i>Before=</i> dependency on the service they are supposed to activate.</dl>
<h3>Default Dependencies</h3>
<p>The following dependencies are added unless <i>DefaultDependencies=no</i> is set: </p>
<dl>
<dd>&bull; Timer units will automatically have dependencies of type <i>Requires=</i> and <i>After=</i> on sysinit.target, a dependency of type <i>Before=</i> on timers.target, as well as <i>Conflicts=</i> and <i>Before=</i> on shutdown.target to ensure that they are stopped cleanly prior to system shutdown. Only timer units involved with early boot or late system shutdown should disable the <i>DefaultDependencies=</i> option.</dl>
<dl>
<dd>&bull; Timer units with at least one <i>OnCalendar=</i> directive acquire a pair of additional <i>After=</i> dependencies on time-set.target and time-sync.target, in order to avoid being started before the system clock has been correctly set. See <code><a href="/docs/linux/man/7-systemd-special/">systemd.special</a></code>(7) for details on these two targets.</dl>
<h2>Options</h2>
<p>Timer files must include a [Timer] section, which carries information about the timer it defines. The options specific to the [Timer] section of timer units are the following: </p>
<p> <i>OnActiveSec=</i>, <i>OnBootSec=</i>, <i>OnStartupSec=</i>, <i>OnUnitActiveSec=</i>, <i>OnUnitInactiveSec=</i></p>
<dl>
<dd>Defines monotonic timers relative to different starting points: </p>
<p> <code>Table 1. Settings and their starting points</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Setting </code></td>
<td><code> Meaning </code>
</td>
</tr>
<tr VALIGN=top>
<td> <i>OnActiveSec=</i> </td>
<td> Defines a timer relative to the moment the timer unit itself is activated.
</td>
</tr>
<tr VALIGN=top>
<td> <i>OnBootSec=</i> </td>
<td> Defines a timer relative to when the machine was booted up. In containers, for the system manager instance, this is mapped to <i>OnStartupSec=</i>, making both equivalent.
</td>
</tr>
<tr VALIGN=top>
<td> <i>OnStartupSec=</i> </td>
<td> Defines a timer relative to when the service manager was first started. For system timer units this is very similar to <i>OnBootSec=</i> as the system service manager is generally started very early at boot. It&#8217;s primarily useful when configured in units running in the per-user service manager, as the user service manager is generally started on first login only, not already during boot.
</td>
</tr>
<tr VALIGN=top>
<td> <i>OnUnitActiveSec=</i> </td>
<td> Defines a timer relative to when the unit the timer unit is activating was last activated.
</td>
</tr>
<tr VALIGN=top>
<td> <i>OnUnitInactiveSec=</i> </td>
<td> Defines a timer relative to when the unit the timer unit is activating was last deactivated.
</td>
</tr>
</table>
<p> Multiple directives may be combined of the same and of different types, in which case the timer unit will trigger whenever any of the specified timer expressions elapse. For example, by combining <i>OnBootSec=</i> and <i>OnUnitActiveSec=</i>, it is possible to define a timer that elapses in regular intervals and activates a specific service each time. Moreover, both monotonic time expressions and <i>OnCalendar=</i> calendar expressions may be combined in the same timer unit. </p>
<p> The arguments to the directives are time spans configured in seconds. Example: &quot;OnBootSec=50&quot; means 50s after boot-up. The argument may also include time units. Example: &quot;OnBootSec=5h 30min&quot; means 5 hours and 30 minutes after boot-up. For details about the syntax of time spans, see <code><a href="/docs/linux/man/7-systemd-time/">systemd.time</a></code>(7). </p>
<p> If a timer configured with <i>OnBootSec=</i> or <i>OnStartupSec=</i> is already in the past when the timer unit is activated, it will immediately elapse and the configured unit is started. This is not the case for timers defined in the other directives. </p>
<p> These are monotonic timers, independent of wall-clock time and timezones. If the computer is temporarily suspended, the monotonic clock generally pauses, too. Note that if <i>WakeSystem=</i> is used, a different monotonic clock is selected that continues to advance while the system is suspended and thus can be used as the trigger to resume the system. </p>
<p> If the empty string is assigned to any of these options, the list of timers is reset (both monotonic timers and <i>OnCalendar=</i> timers, see below), and all prior assignments will have no effect. </p>
<p> Note that timers do not necessarily expire at the precise time configured with these settings, as they are subject to the <i>AccuracySec=</i> setting below.</dl>
<p> <i>OnCalendar=</i></p>
<dl>
<dd>Defines realtime (i.e. wallclock) timers with calendar event expressions. See <code><a href="/docs/linux/man/7-systemd-time/">systemd.time</a></code>(7) for more information on the syntax of calendar event expressions. Otherwise, the semantics are similar to <i>OnActiveSec=</i> and related settings. </p>
<p> Note that timers do not necessarily expire at the precise time configured with this setting, as it is subject to the <i>AccuracySec=</i> setting below. </p>
<p> May be specified more than once, in which case the timer unit will trigger whenever any of the specified expressions elapse. Moreover calendar timers and monotonic timers (see above) may be combined within the same timer unit. </p>
<p> If the empty string is assigned to any of these options, the list of timers is reset (both <i>OnCalendar=</i> timers and monotonic timers, see above), and all prior assignments will have no effect.</dl>
<p> <i>AccuracySec=</i></p>
<dl>
<dd>Specify the accuracy the timer shall elapse with. Defaults to 1min. The timer is scheduled to elapse within a time window starting with the time specified in <i>OnCalendar=</i>, <i>OnActiveSec=</i>, <i>OnBootSec=</i>, <i>OnStartupSec=</i>, <i>OnUnitActiveSec=</i> or <i>OnUnitInactiveSec=</i> and ending the time configured with <i>AccuracySec=</i> later. Within this time window, the expiry time will be placed at a host-specific, randomized, but stable position that is synchronized between all local timer units. This is done in order to optimize power consumption to suppress unnecessary CPU wake-ups. To get best accuracy, set this option to 1us. Note that the timer is still subject to the timer slack configured via <code><a href="/docs/linux/man/5-systemd-system-conf/">systemd-system.conf</a></code>(5)&#8217;s <i>TimerSlackNSec=</i> setting. See <code><a href="/docs/linux/man/2-prctl/">prctl</a></code>(2) for details. To optimize power consumption, make sure to set this value as high as possible and as low as necessary. </p>
<p> Note that this setting is primarily a power saving option that allows coalescing CPU wake-ups. It should not be confused with <i>RandomizedDelaySec=</i> (see below) which adds a random value to the time the timer shall elapse next and whose purpose is the opposite: to stretch elapsing of timer events over a longer period to reduce workload spikes. For further details and explanations and how both settings play together, see below.</dl>
<p> <i>RandomizedDelaySec=</i></p>
<dl>
<dd>Delay the timer by a randomly selected, evenly distributed amount of time between 0 and the specified time value. Defaults to 0, indicating that no randomized delay shall be applied. Each timer unit will determine this delay randomly before each iteration, and the delay will simply be added on top of the next determined elapsing time, unless modified with <i>FixedRandomDelay=</i>, see below. </p>
<p> This setting is useful to stretch dispatching of similarly configured timer events over a certain time interval, to prevent them from firing all at the same time, possibly resulting in resource congestion. </p>
<p> Note the relation to <i>AccuracySec=</i> above: the latter allows the service manager to coalesce timer events within a specified time range in order to minimize wakeups, while this setting does the opposite: it stretches timer events over an interval, to make it unlikely that they fire simultaneously. If <i>RandomizedDelaySec=</i> and <i>AccuracySec=</i> are used in conjunction, first the randomized delay is added, and then the result is possibly further shifted to coalesce it with other timer events happening on the system. As mentioned above <i>AccuracySec=</i> defaults to 1 minute and <i>RandomizedDelaySec=</i> to 0, thus encouraging coalescing of timer events. In order to optimally stretch timer events over a certain range of time, set <i>AccuracySec=1us</i> and <i>RandomizedDelaySec=</i> to some higher value.</dl>
<p> <i>FixedRandomDelay=</i></p>
<dl>
<dd>Takes a boolean argument. When enabled, the randomized offset specified by <i>RandomizedDelaySec=</i> is reused for all firings of the same timer. For a given timer unit, the offset depends on the machine ID, user identifier and timer name, which means that it is stable between restarts of the manager. This effectively creates a fixed offset for an individual timer, reducing the jitter in firings of this timer, while still avoiding firing at the same time as other similarly configured timers. </p>
<p> This setting has no effect if <i>RandomizedDelaySec=</i> is set to 0. Defaults to <code>false</code>.</dl>
<p> <i>OnClockChange=</i>, <i>OnTimezoneChange=</i></p>
<dl>
<dd>These options take boolean arguments. When true, the service unit will be triggered when the system clock (<code>CLOCK_REALTIME</code>) jumps relative to the monotonic clock (<code>CLOCK_MONOTONIC</code>), or when the local system timezone is modified. These options can be used alone or in combination with other timer expressions (see above) within the same timer unit. These options default to <code>false</code>.</dl>
<p> <i>Unit=</i></p>
<dl>
<dd>The unit to activate when this timer elapses. The argument is a unit name, whose suffix is not &quot;.timer&quot;. If not specified, this value defaults to a service that has the same name as the timer unit, except for the suffix. (See above.) It is recommended that the unit name that is activated and the unit name of the timer unit are named identically, except for the suffix.</dl>
<p> <i>Persistent=</i></p>
<dl>
<dd>Takes a boolean argument. If true, the time when the service unit was last triggered is stored on disk. When the timer is activated, the service unit is triggered immediately if it would have been triggered at least once during the time when the timer was inactive. Such triggering is nonetheless subject to the delay imposed by <i>RandomizedDelaySec=</i>. This is useful to catch up on missed runs of the service when the system was powered down. Note that this setting only has an effect on timers configured with <i>OnCalendar=</i>. Defaults to <code>false</code>. </p>
<p> Use <code>systemctl clean &#8211;what=state &#8230;</code> on the timer unit to remove the timestamp file maintained by this option from disk. In particular, use this command before uninstalling a timer unit. See <code><a href="/docs/linux/man/1-systemctl/">systemctl</a></code>(1) for details.</dl>
<p> <i>WakeSystem=</i></p>
<dl>
<dd>Takes a boolean argument. If true, an elapsing timer will cause the system to resume from suspend, should it be suspended and if the system supports this. Note that this option will only make sure the system resumes on the appropriate times, it will not take care of suspending it again after any work that is to be done is finished. Defaults to <code>false</code>. </p>
<p> Note that this functionality requires privileges and is thus generally only available in the system service manager. </p>
<p> Note that behaviour of monotonic clock timers (as configured with <i>OnActiveSec=</i>, <i>OnBootSec=</i>, <i>OnStartupSec=</i>, <i>OnUnitActiveSec=</i>, <i>OnUnitInactiveSec=</i>, see above) is altered depending on this option. If false, a monotonic clock is used that is paused during system suspend (<code>CLOCK_MONOTONIC</code>), if true a different monotonic clock is used that continues advancing during system suspend (<code>CLOCK_BOOTTIME</code>), see <code><a href="/docs/linux/man/2-clock_getres/">clock_getres</a></code>(2) for details.</dl>
<p> <i>RemainAfterElapse=</i></p>
<dl>
<dd>Takes a boolean argument. If true, a timer will stay loaded, and its state remains queryable even after it elapsed and the associated unit (as configured with <i>Unit=</i>, see above) deactivated again. If false, an elapsed timer unit that cannot elapse anymore is unloaded once its associated unit deactivated again. Turning this off is particularly useful for transient timer units. Note that this setting has an effect when repeatedly starting a timer unit: if <i>RemainAfterElapse=</i> is on, starting the timer a second time has no effect. However, if <i>RemainAfterElapse=</i> is off and the timer unit was already unloaded, it can be started again, and thus the service can be triggered multiple times. Defaults to <code>true</code>.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/1-systemctl/">systemctl</a></code>(1), <code><a href="/docs/linux/man/5-systemd-unit/">systemd.unit</a></code>(5), <code><a href="/docs/linux/man/5-systemd-service/">systemd.service</a></code>(5), <code><a href="/docs/linux/man/7-systemd-time/">systemd.time</a></code>(7), <code><a href="/docs/linux/man/7-systemd-directives/">systemd.directives</a></code>(7), <code><a href="/docs/linux/man/5-systemd-system-conf/">systemd-system.conf</a></code>(5), <code><a href="/docs/linux/man/2-prctl/">prctl</a></code>(2) </p>
