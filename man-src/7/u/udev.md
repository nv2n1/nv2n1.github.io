---
title: "udev(7)"
name: "udev"
section: "7"
letter: "u"
url: "/docs/linux/man/7-udev/"
description: "udev – Dynamic device management"
---

<p>udev &#8211; Dynamic device management</p>
<h2>Description</h2>
<p>udev supplies the system software with device events, manages permissions of device nodes and may create additional symlinks in the /dev/ directory, or renames network interfaces. The kernel usually just assigns unpredictable device names based on the order of discovery. Meaningful symlinks or network device names provide a way to reliably identify devices based on their properties or current configuration. </p>
<p> The udev daemon, <code><a href="/docs/linux/man/8-systemd-udevd-service/">systemd-udevd.service</a></code>(8), receives device uevents directly from the kernel whenever a device is added or removed from the system, or it changes its state. When udev receives a device event, it matches its configured set of rules against various device attributes to identify the device. Rules that match may provide additional device information to be stored in the udev database or to be used to create meaningful symlink names. </p>
<p> All device information udev processes is stored in the udev database and sent out to possible event subscribers. Access to all stored data and the event sources is provided by the library libudev.</p>
<h2>Rules Files</h2>
<p>The udev rules are read from the files located in the system rules directories /lib/udev/rules.d and /usr/local/lib/udev/rules.d, the volatile runtime directory /run/udev/rules.d and the local administration directory /etc/udev/rules.d. All rules files are collectively sorted and processed in lexical order, regardless of the directories in which they live. However, files with identical filenames replace each other. Files in /etc/ have the highest priority, files in /run/ take precedence over files with the same name under /usr/. This can be used to override a system-supplied rules file with a local file if needed; a symlink in /etc/ with the same name as a rules file in /lib/, pointing to /dev/null, disables the rules file entirely. Rule files must have the extension .rules; other extensions are ignored. </p>
<p> Every line in the rules file contains at least one key-value pair. Except for empty lines or lines beginning with &quot;#&quot;, which are ignored. There are two kinds of keys: match and assignment. If all match keys match against their values, the rule gets applied and the assignment keys get the specified values assigned. </p>
<p> A matching rule may rename a network interface, add symlinks pointing to the device node, or run a specified program as part of the event handling. </p>
<p> A rule consists of a comma-separated list of one or more key-operator-value expressions. Each expression has a distinct effect, depending on the key and operator used.</p>
<h3>Operators</h3>
<p>&quot;==&quot;</p>
<dl>
<dd>Compare for equality. (The specified key has the specified value.)</dl>
<p> &quot;!=&quot;</p>
<dl>
<dd>Compare for inequality. (The specified key doesn&#8217;t have the specified value, or the specified key is not present at all.)</dl>
<p> &quot;=&quot;</p>
<dl>
<dd>Assign a value to a key. Keys that represent a list are reset and only this single value is assigned.</dl>
<p> &quot;+=&quot;</p>
<dl>
<dd>Add the value to a key that holds a list of entries.</dl>
<p> &quot;-=&quot;</p>
<dl>
<dd>Remove the value from a key that holds a list of entries.</dl>
<p> &quot;:=&quot;</p>
<dl>
<dd>Assign a value to a key finally; disallow any later changes.</dl>
<h3>Values</h3>
<p>Values are written as double quoted strings, such as (&quot;string&quot;). To include a quotation mark (&quot;) in the value, precede it by a backslash (\&quot;). Any other occurrences of a backslash followed by a character are not unescaped. That is, &quot;	
&quot; is treated as four characters: backslash, lowercase t, backslash, lowercase n. </p>
<p> The string can be prefixed with a lowercase e (e&quot;string
&quot;) to mark the string as m[blue]<code>C-style escaped</code>m[]<font SIZE="-2">[1]</font>. For example, e&quot;string
&quot; is parsed as 7 characters: 6 lowercase letters and a newline. This can be useful for writing special characters when a kernel driver requires them. </p>
<p> Please note that <code>NUL</code> is not allowed in either string variant.</p>
<h3>Keys</h3>
<p>The following key names can be used to match against device properties. Some of the keys also match against properties of the parent devices in sysfs, not only the device that has generated the event. If multiple keys that match a parent device are specified in a single rule, all these keys must match at one and the same parent device. </p>
<p> <i>ACTION</i></p>
<dl>
<dd>Match the name of the event action.</dl>
<p> <i>DEVPATH</i></p>
<dl>
<dd>Match the devpath of the event device.</dl>
<p> <i>KERNEL</i></p>
<dl>
<dd>Match the name of the event device.</dl>
<p> <i>KERNELS</i></p>
<dl>
<dd>Search the devpath upwards for a matching device name.</dl>
<p> <i>NAME</i></p>
<dl>
<dd>Match the name of a network interface. It can be used once the NAME key has been set in one of the preceding rules.</dl>
<p> <i>SYMLINK</i></p>
<dl>
<dd>Match the name of a symlink targeting the node. It can be used once a SYMLINK key has been set in one of the preceding rules. There may be multiple symlinks; only one needs to match.</dl>
<p> <i>SUBSYSTEM</i></p>
<dl>
<dd>Match the subsystem of the event device.</dl>
<p> <i>SUBSYSTEMS</i></p>
<dl>
<dd>Search the devpath upwards for a matching device subsystem name.</dl>
<p> <i>DRIVER</i></p>
<dl>
<dd>Match the driver name of the event device. Only set this key for devices which are bound to a driver at the time the event is generated.</dl>
<p> <i>DRIVERS</i></p>
<dl>
<dd>Search the devpath upwards for a matching device driver name.</dl>
<p> <i>ATTR{</i><i>filename</i><i>}</i></p>
<dl>
<dd>Match sysfs attribute value of the event device. </p>
<p> Trailing whitespace in the attribute values is ignored unless the specified match value itself contains trailing whitespace.</dl>
<p> <i>ATTRS{</i><i>filename</i><i>}</i></p>
<dl>
<dd>Search the devpath upwards for a device with matching sysfs attribute values. If multiple <i>ATTRS</i> matches are specified, all of them must match on the same device. </p>
<p> Trailing whitespace in the attribute values is ignored unless the specified match value itself contains trailing whitespace.</dl>
<p> <i>SYSCTL{</i><i>kernel parameter</i><i>}</i></p>
<dl>
<dd>Match a kernel parameter value.</dl>
<p> <i>ENV{</i><i>key</i><i>}</i></p>
<dl>
<dd>Match against a device property value.</dl>
<p> <i>CONST{</i><i>key</i><i>}</i></p>
<dl>
<dd>Match against a system-wide constant. Supported keys are: </p>
<p> &quot;arch&quot;</p>
<dl>
<dd>System&#8217;s architecture. See <code>ConditionArchitecture=</code> in <code><a href="/docs/linux/man/5-systemd-unit/">systemd.unit</a></code>(5) for possible values.</dl>
<p> &quot;virt&quot;</p>
<dl>
<dd>System&#8217;s virtualization environment. See <code><a href="/docs/linux/man/1-systemd-detect-virt/">systemd-detect-virt</a></code>(1) for possible values.</dl>
<p> Unknown keys will never match.</dl>
<p> <i>TAG</i></p>
<dl>
<dd>Match against a device tag.</dl>
<p> <i>TAGS</i></p>
<dl>
<dd>Search the devpath upwards for a device with matching tag.</dl>
<p> <i>TEST{</i><i>octal mode mask</i><i>}</i></p>
<dl>
<dd>Test the existence of a file. An octal mode mask can be specified if needed.</dl>
<p> <i>PROGRAM</i></p>
<dl>
<dd>Execute a program to determine whether there is a match; the key is true if the program returns successfully. The device properties are made available to the executed program in the environment. The program&#8217;s standard output is available in the <i>RESULT</i> key. </p>
<p> This can only be used for very short-running foreground tasks. For details, see <i>RUN</i>. </p>
<p> Note that multiple <i>PROGRAM</i> keys may be specified in one rule, and &quot;=&quot;, &quot;:=&quot;, and &quot;+=&quot; have the same effect as &quot;==&quot;.</dl>
<p> <i>RESULT</i></p>
<dl>
<dd>Match the returned string of the last <i>PROGRAM</i> call. This key can be used in the same or in any later rule after a <i>PROGRAM</i> call.</dl>
<p> Most of the fields support shell glob pattern matching and alternate patterns. The following special characters are supported: </p>
<p> &quot;*&quot;</p>
<dl>
<dd>Matches zero or more characters.</dl>
<p> &quot;?&quot;</p>
<dl>
<dd>Matches any single character.</dl>
<p> &quot;[]&quot;</p>
<dl>
<dd>Matches any single character specified within the brackets. For example, the pattern string &quot;tty[SR]&quot; would match either &quot;ttyS&quot; or &quot;ttyR&quot;. Ranges are also supported via the &quot;-&quot; character. For example, to match on the range of all digits, the pattern &quot;[0-9]&quot; could be used. If the first character following the &quot;[&quot; is a &quot;!&quot;, any characters not enclosed are matched.</dl>
<p> &quot;|&quot;</p>
<dl>
<dd>Separates alternative patterns. For example, the pattern string &quot;abc|x*&quot; would match either &quot;abc&quot; or &quot;x*&quot;.</dl>
<p> The following keys can get values assigned: </p>
<p> <i>NAME</i></p>
<dl>
<dd>The name to use for a network interface. See <code><a href="/docs/linux/man/5-systemd-link/">systemd.link</a></code>(5) for a higher-level mechanism for setting the interface name. The name of a device node cannot be changed by udev, only additional symlinks can be created.</dl>
<p> <i>SYMLINK</i></p>
<dl>
<dd>The name of a symlink targeting the node. Every matching rule adds this value to the list of symlinks to be created. </p>
<p> The set of characters to name a symlink is limited. Allowed characters are &quot;0-9A-Za-z#+-.:=@_/&quot;, valid UTF-8 character sequences, and &quot;
