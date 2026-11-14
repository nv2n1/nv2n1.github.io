---
title: "udevadm(8)"
name: "udevadm"
section: "8"
letter: "u"
url: "/docs/linux/man/8-udevadm/"
description: "udevadm – udev management tool"
---

<p>udevadm &#8211; udev management tool</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>udevadm</code> [<code>&#8211;debug</code>] [<code>&#8211;version</code>] [<code>&#8211;help</code>]</p>
<dt> <code>udevadm info </code><code>[options]</code><code>[devpath]</code></p>
<dt> <code>udevadm trigger </code><code>[options]</code><code>[devpath]</code></p>
<dt> <code>udevadm settle </code><code>[options]</code></p>
<dt> <code>udevadm control </code><i>option</i></p>
<dt> <code>udevadm monitor </code><code>[options]</code></p>
<dt> <code>udevadm test </code><code>[options]</code><i>devpath</i></p>
<dt> <code>udevadm test-builtin </code><code>[options]</code><i>command</i><i>devpath</i></dl>
<h2>Description</h2>
<p><code>udevadm</code></p>
<dd>expects a command and command specific options. It controls the runtime behavior of <code>systemd-udevd</code>, requests kernel events, manages the event queue, and provides simple debugging mechanisms.</p>
<h2>Options</h2>
<p><code>-d</code>, <code>&#8211;debug</code></p>
<dl>
<dd>Print debug messages to standard error. This option is implied in <code>udevadm test</code> and <code>udevadm test-builtin</code> commands.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dd>Print a short help text and exit.</dl>
<h3>udevadm info [<i>options</i>] [<i>devpath</i>|<i>file</i>|<i>unit</i>&#8230;]</h3>
<p>Query the udev database for device information. </p>
<p> Positional arguments should be used to specify one or more devices. Each one may be a device name (in which case it must start with /dev/), a sys path (in which case it must start with /sys/), or a systemd device unit name (in which case it must end with &quot;.device&quot;, see <code><a href="/docs/linux/man/5-systemd-device/">systemd.device</a></code>(5)). </p>
<p> <code>-q</code>, <code>&#8211;query=</code><i>TYPE</i></p>
<dl>
<dd>Query the database for the specified type of device data. Valid <i>TYPE</i>s are: <code>name</code>, <code>symlink</code>, <code>path</code>, <code>property</code>, <code>all</code>.</dl>
<p> <code>-p</code>, <code>&#8211;path=</code><i>DEVPATH</i></p>
<dl>
<dd>The /sys/ path of the device to query, e.g. [/sys/]/class/block/sda. This option is an alternative to the positional argument with a /sys/ prefix. <code>udevadm info &#8211;path=/class/block/sda</code> is equivalent to <code>udevadm info /sys/class/block/sda</code>.</dl>
<p> <code>-n</code>, <code>&#8211;name=</code><i>FILE</i></p>
<dl>
<dd>The name of the device node or a symlink to query, e.g. [/dev/]/sda. This option is an alternative to the positional argument with a /dev/ prefix. <code>udevadm info &#8211;name=sda</code> is equivalent to <code>udevadm info /dev/sda</code>.</dl>
<p> <code>-r</code>, <code>&#8211;root</code></p>
<dl>
<dd>Print absolute paths in <code>name</code> or <code>symlink</code> query.</dl>
<p> <code>-a</code>, <code>&#8211;attribute-walk</code></p>
<dl>
<dd>Print all sysfs properties of the specified device that can be used in udev rules to match the specified device. It prints all devices along the chain, up to the root of sysfs that can be used in udev rules.</dl>
<p> <code>-x</code>, <code>&#8211;export</code></p>
<dl>
<dd>Print output as key/value pairs. Values are enclosed in single quotes. This takes effects only when <code>&#8211;query=property</code> or <code>&#8211;device-id-of-file=</code><i>FILE</i> is specified.</dl>
<p> <code>-P</code>, <code>&#8211;export-prefix=</code><i>NAME</i></p>
<dl>
<dd>Add a prefix to the key name of exported values. This implies <code>&#8211;export</code>.</dl>
<p> <code>-d</code>, <code>&#8211;device-id-of-file=</code><i>FILE</i></p>
<dl>
<dd>Print major/minor numbers of the underlying device, where the file lives on. If this is specified, all positional arguments are ignored.</dl>
<p> <code>-e</code>, <code>&#8211;export-db</code></p>
<dl>
<dd>Export the content of the udev database.</dl>
<p> <code>-c</code>, <code>&#8211;cleanup-db</code></p>
<dl>
<dd>Cleanup the udev database.</dl>
<p> <code>-w</code><code>[SECONDS]</code>, <code>&#8211;wait-for-initialization</code><code>[=SECONDS]</code></p>
<dl>
<dd>Wait for device to be initialized. If argument <i>SECONDS</i> is not specified, the default is to wait forever.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dd>Print a short help text and exit.</dl>
<p> The generated output shows the current device database entry in a terse format. Each line shown is prefixed with one of the following characters: </p>
<p> <code>Table 1. udevadm info output prefixes</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Prefix </code></td>
<td><code> Meaning </code>
</td>
</tr>
<tr VALIGN=top>
<td> &quot;P:&quot; </td>
<td> Device path in /sys/
</td>
</tr>
<tr VALIGN=top>
<td> &quot;N:&quot; </td>
<td> Kernel device node name
</td>
</tr>
<tr VALIGN=top>
<td> &quot;L:&quot; </td>
<td> Device node symlink priority
</td>
</tr>
<tr VALIGN=top>
<td> &quot;S:&quot; </td>
<td> Device node symlink
</td>
</tr>
<tr VALIGN=top>
<td> &quot;E:&quot; </td>
<td> Device property
</td>
</tr>
</table>
<h3>udevadm trigger [<i>options</i>] [<i>devpath</i>|<i>file</i>|<i>unit</i>]</h3>
<p>Request device events from the kernel. Primarily used to replay events at system coldplug time. </p>
<p> Takes device specifications as positional arguments. See the description of <code>info</code> above. </p>
<p> <code>-v</code>, <code>&#8211;verbose</code></p>
<dl>
<dd>Print the list of devices which will be triggered.</dl>
<p> <code>-n</code>, <code>&#8211;dry-run</code></p>
<dl>
<dd>Do not actually trigger the event.</dl>
<p> <code>-q</code>, <code>&#8211;quiet</code></p>
<dl>
<dd>Suppress error logging in triggering events.</dl>
<p> <code>-t</code>, <code>&#8211;type=</code><i>TYPE</i></p>
<dl>
<dd>Trigger a specific type of devices. Valid types are: <code>devices</code>, <code>subsystems</code>. The default value is <code>devices</code>.</dl>
<p> <code>-c</code>, <code>&#8211;action=</code><i>ACTION</i></p>
<dl>
<dd>Type of event to be triggered. Possible actions are &quot;add&quot;, &quot;remove&quot;, &quot;change&quot;, &quot;move&quot;, &quot;online&quot;, &quot;offline&quot;, &quot;bind&quot;, and &quot;unbind&quot;. Also, the special value &quot;help&quot; can be used to list the possible actions. The default value is &quot;change&quot;.</dl>
<p> <code>-s</code>, <code>&#8211;subsystem-match=</code><i>SUBSYSTEM</i></p>
<dl>
<dd>Trigger events for devices which belong to a matching subsystem. This option supports shell style pattern matching. When this option is specified more than once, then each matching result is ORed, that is, all the devices in each subsystem are triggered.</dl>
<p> <code>-S</code>, <code>&#8211;subsystem-nomatch=</code><i>SUBSYSTEM</i></p>
<dl>
<dd>Do not trigger events for devices which belong to a matching subsystem. This option supports shell style pattern matching. When this option is specified more than once, then each matching result is ANDed, that is, devices which do not match all specified subsystems are triggered.</dl>
<p> <code>-a</code>, <code>&#8211;attr-match=</code><i>ATTRIBUTE</i><code>=</code><i>VALUE</i></p>
<dl>
<dd>Trigger events for devices with a matching sysfs attribute. If a value is specified along with the attribute name, the content of the attribute is matched against the given value using shell style pattern matching. If no value is specified, the existence of the sysfs attribute is checked. When this option is specified multiple times, then each matching result is ANDed, that is, only devices which have all specified attributes are triggered.</dl>
<p> <code>-A</code>, <code>&#8211;attr-nomatch=</code><i>ATTRIBUTE</i><code>=</code><i>VALUE</i></p>
<dl>
<dd>Do not trigger events for devices with a matching sysfs attribute. If a value is specified along with the attribute name, the content of the attribute is matched against the given value using shell style pattern matching. If no value is specified, the existence of the sysfs attribute is checked. When this option is specified multiple times, then each matching result is ANDed, that is, only devices which have none of the specified attributes are triggered.</dl>
<p> <code>-p</code>, <code>&#8211;property-match=</code><i>PROPERTY</i><code>=</code><i>VALUE</i></p>
<dl>
<dd>Trigger events for devices with a matching property value. This option supports shell style pattern matching. When this option is specified more than once, then each matching result is ORed, that is, devices which have one of the specified properties are triggered.</dl>
<p> <code>-g</code>, <code>&#8211;tag-match=</code><i>TAG</i></p>
<dl>
<dd>Trigger events for devices with a matching tag. When this option is specified multiple times, then each matching result is ANDed, that is, devices which have all specified tags are triggered.</dl>
<p> <code>-y</code>, <code>&#8211;sysname-match=</code><i>NAME</i></p>
<dl>
<dd>Trigger events for devices for which the last component (i.e. the filename) of the /sys/ path matches the specified <i>PATH</i>. This option supports shell style pattern matching. When this option is specified more than once, then each matching result is ORed, that is, all devices which have any of the specified <i>NAME</i> are triggered.</dl>
<p> <code>&#8211;name-match=</code><i>NAME</i></p>
<dl>
<dd>Trigger events for devices with a matching device path. When this option is specified more than once, then each matching result is ORed, that is, all specified devices are triggered.</dl>
<p> <code>-b</code>, <code>&#8211;parent-match=</code><i>SYSPATH</i></p>
<dl>
<dd>Trigger events for all children of a given device. When this option is specified more than once, then each matching result is ORed, that is, all children of each specified device are triggered.</dl>
<p> <code>-w</code>, <code>&#8211;settle</code></p>
<dl>
<dd>Apart from triggering events, also waits for those events to finish. Note that this is different from calling <code>udevadm settle</code>. <code>udevadm settle</code> waits for all events to finish. This option only waits for events triggered by the same command to finish.</dl>
<p> <code>&#8211;uuid</code></p>
<dl>
<dd>Trigger the synthetic device events, and associate a randomized UUID with each. These UUIDs are printed to standard output, one line for each event. These UUIDs are included in the uevent environment block (in the &quot;SYNTH_UUID=&quot; property) and may be used to track delivery of the generated events.</dl>
<p> <code>&#8211;wait-daemon[=</code><i>SECONDS</i><code>]</code></p>
<dl>
<dd>Before triggering uevents, wait for systemd-udevd daemon to be initialized. Optionally takes timeout value. Default timeout is 5 seconds. This is equivalent to invoke invoking <code>udevadm control &#8211;ping</code> before <code>udevadm trigger</code>.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dd>Print a short help text and exit.</dl>
<p> In addition, optional positional arguments can be used to specify device names or sys paths. They must start with /dev/ or /sys/ respectively.</p>
<h3>udevadm settle [<i>options</i>]</h3>
<p>Watches the udev event queue, and exits if all current events are handled. </p>
<p> <code>-t</code>, <code>&#8211;timeout=</code><i>SECONDS</i></p>
<dl>
<dd>Maximum number of seconds to wait for the event queue to become empty. The default value is 120 seconds. A value of 0 will check if the queue is empty and always return immediately. A non-zero value will return an exit code of 0 if queue became empty before timeout was reached, non-zero otherwise.</dl>
<p> <code>-E</code>, <code>&#8211;exit-if-exists=</code><i>FILE</i></p>
<dl>
<dd>Stop waiting if file exists.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dd>Print a short help text and exit.</dl>
<p> See <code><a href="/docs/linux/man/8-systemd-udev-settle-service/">systemd-udev-settle.service</a></code>(8) for more information.</p>
<h3>udevadm control <i>option</i></h3>
<p>Modify the internal state of the running udev daemon. </p>
<p> <code>-e</code>, <code>&#8211;exit</code></p>
<dl>
<dd>Signal and wait for systemd-udevd to exit. No option except for <code>&#8211;timeout</code> can be specified after this option. Note that systemd-udevd.service contains <code>Restart=always</code> and so as a result, this option restarts systemd-udevd. If you want to stop systemd-udevd.service, please use the following: </p>
<dl>
<dd>
<pre>systemctl stop systemd-udevd-control.socket systemd-udevd-kernel.socket systemd-udevd.service</pre>
</dl>
</dl>
<p> <code>-l</code>, <code>&#8211;log-level=</code><i>value</i></p>
<dl>
<dd>Set the internal log level of systemd-udevd. Valid values are the numerical syslog priorities or their textual representations: <code>emerg</code>, <code>alert</code>, <code>crit</code>, <code>err</code>, <code>warning</code>, <code>notice</code>, <code>info</code>, and <code>debug</code>.</dl>
<p> <code>-s</code>, <code>&#8211;stop-exec-queue</code></p>
<dl>
<dd>Signal systemd-udevd to stop executing new events. Incoming events will be queued.</dl>
<p> <code>-S</code>, <code>&#8211;start-exec-queue</code></p>
<dl>
<dd>Signal systemd-udevd to enable the execution of events.</dl>
<p> <code>-R</code>, <code>&#8211;reload</code></p>
<dl>
<dd>Signal systemd-udevd to reload the rules files and other databases like the kernel module index. Reloading rules and databases does not apply any changes to already existing devices; the new configuration will only be applied to new events.</dl>
<p> <code>-p</code>, <code>&#8211;property=</code><i>KEY</i><code>=</code><i>value</i></p>
<dl>
<dd>Set a global property for all events.</dl>
<p> <code>-m</code>, <code>&#8211;children-max=</code><i>value</i></p>
<dl>
<dd>Set the maximum number of events, systemd-udevd will handle at the same time.</dl>
<p> <code>&#8211;ping</code></p>
<dl>
<dd>Send a ping message to systemd-udevd and wait for the reply. This may be useful to check that systemd-udevd daemon is running.</dl>
<p> <code>-t</code>, <code>&#8211;timeout=</code><i>seconds</i></p>
<dl>
<dd>The maximum number of seconds to wait for a reply from systemd-udevd.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dd>Print a short help text and exit.</dl>
<h3>udevadm monitor [<i>options</i>]</h3>
<p>Listens to the kernel uevents and events sent out by a udev rule and prints the devpath of the event to the console. It can be used to analyze the event timing, by comparing the timestamps of the kernel uevent and the udev event. </p>
<p> <code>-k</code>, <code>&#8211;kernel</code></p>
<dl>
<dd>Print the kernel uevents.</dl>
<p> <code>-u</code>, <code>&#8211;udev</code></p>
<dl>
<dd>Print the udev event after the rule processing.</dl>
<p> <code>-p</code>, <code>&#8211;property</code></p>
<dl>
<dd>Also print the properties of the event.</dl>
<p> <code>-s</code>, <code>&#8211;subsystem-match=</code><i>string[/string]</i></p>
<dl>
<dd>Filter kernel uevents and udev events by subsystem[/devtype]. Only events with a matching subsystem value will pass. When this option is specified more than once, then each matching result is ORed, that is, all devices in the specified subsystems are monitored.</dl>
<p> <code>-t</code>, <code>&#8211;tag-match=</code><i>string</i></p>
<dl>
<dd>Filter udev events by tag. Only udev events with a given tag attached will pass. When this option is specified more than once, then each matching result is ORed, that is, devices which have one of the specified tags are monitored.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dd>Print a short help text and exit.</dl>
<h3>udevadm test [<i>options</i>] [<i>devpath</i>]</h3>
<p>Simulate a udev event run for the given device, and print debug output. </p>
<p> <code>-a</code>, <code>&#8211;action=</code><i>ACTION</i></p>
<dl>
<dd>Type of event to be simulated. Possible actions are &quot;add&quot;, &quot;remove&quot;, &quot;change&quot;, &quot;move&quot;, &quot;online&quot;, &quot;offline&quot;, &quot;bind&quot;, and &quot;unbind&quot;. Also, the special value &quot;help&quot; can be used to list the possible actions. The default value is &quot;add&quot;.</dl>
<p> <code>-N</code>, <code>&#8211;resolve-names=</code><code>early</code><code>|</code><code>late</code><code>|</code><code>never</code></p>
<dl>
<dd>Specify when udevadm should resolve names of users and groups. When set to <code>early</code> (the default), names will be resolved when the rules are parsed. When set to <code>late</code>, names will be resolved for every event. When set to <code>never</code>, names will never be resolved and all devices will be owned by root.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dd>Print a short help text and exit.</dl>
<h3>udevadm test-builtin [<i>options</i>] [<i>command</i>] [<i>devpath</i>]</h3>
<p>Run a built-in command <i>COMMAND</i> for device <i>DEVPATH</i>, and print debug output. </p>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dd>Print a short help text and exit.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-udev/">udev</a></code>(7), <code><a href="/docs/linux/man/8-systemd-udevd-service/">systemd-udevd.service</a></code>(8) </p>
