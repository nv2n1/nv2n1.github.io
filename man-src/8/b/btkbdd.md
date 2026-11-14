---
title: "btkbdd(8)"
name: "btkbdd"
section: "8"
letter: "b"
url: "/docs/linux/man/8-btkbdd/"
description: "btkbdd – Bluetooth Keyboard Daemon"
---

<p>btkbdd &#8211; Bluetooth Keyboard Daemon</p>
<h2>Synopsis</h2>
<p><code>btkbdd</code> [-s <i>addr</i>] [-t <i>addr</i>] [-c <i>file</i>] [-d] <i>device</i></p>
<h2>Description</h2>
<p>This tool starts a Bluetooth <font SIZE="-1">HID</font> Keyboard service, serving keystrokes obtained via Linux Input subsystem&#8217;s event device (<i>evdev</i>). In practical terms, it turns your Linux box with a physical keyboard into a Bluetooth keyboard, which can be used by various Bluetooth <font SIZE="-1">HID</font> capable devices, including desktop or tablet computers, smart phones, game consoles and so on. </p>
<p> It implements most of the important <font SIZE="-1">HID</font> protocol features, including robust connection restores (<i>virtual cabling</i>) and report protocol (as required by Apple&#8217;s Darwin-based devices). It is possible and encouraged to use the tool from udev, starting it when event devices appear after a keyboard is plugged in.</p>
<h2>Options</h2>
<dl>
<dt><code>-s</code> <i>addr</i></p>
<dd>Accept connections on given Bluetooth address. Useful when your computer has multiple Bluetooth Host Controller Interfaces (<i></i><font SIZE="-1"><i>HCI</i></font><i></i>). </p>
<p> Class of this device is changed into keyboard while the program is running and restored upon termination. </p>
<p> Defaults to accepting connections on any interface, while changing the class only of the first interface <i>hci0</i>, which is a sane default for computers with a single <font SIZE="-1">HCI.</font></p>
<dt><code>-t</code> <i>addr</i></p>
<dd>Attempt connecting to given address upon key press, if no connection has been estabilished yet. This can be used to effectively &#8220;hardwire&#8221; the keyboard to a given host. </p>
<p> Once an incoming connection is estabilished and terminated, btkbdd always tries to restore it upon a key press event.</p>
<dt><code>-c</code> <i>file</i></p>
<dd>Save the last connected remote address into given file upon termination and restore it on startup. </p>
<p> Use this option if you want to remember last connected device between btkbdd runs.</p>
<dt><code>-d</code></p>
<dd>Become a daemon. Give up controlling terminal, open file descriptors and double-fork to escape parent process control. </p>
<p> While breaking process hierarchy has certain disadvantages and is deprecated with modern service control daemons such as <i><a href="/docs/linux/man/8-systemd/">systemd</a></i>(8)), it is necessary to do so with <i><a href="/docs/linux/man/8-udevd/">udevd</a></i>(8), otherwise btkbdd would block the whole worker process.</p>
<dt><i>device</i></p>
<dd>Linux input subsystem event device to use as source for key presses.</dl>
<h2>Examples</h2>
<p>Use with <i><a href="/docs/linux/man/7-udev/">udev</a></i>(7) and <i><a href="/docs/linux/man/1-systemd/">systemd</a></i>(1) is recommended. Look into <i>90-btkbdd.rules</i> and <i>btkbdd [at] .service</i> files distributed with btkbdd for examples.</p>
<dl>
<dt><code>btkbdd /dev/input/event8</code></p>
<dd>Most basic usage &#8212; just open a keyboard device and listen for incoming connections. When in doubt about which physical device corresponds to an event device node, use <tt>&quot;udevadm info --attribute-walk --name=</tt>file<tt>&quot;</tt> to identify the device and its connection details.</p>
<dt><code>btkbdd /dev/input/event8 -s </code><font SIZE="-1"><code>EC:55:F9:EF:12:34</code></font><code> -c /var/lib/btkbdd/keyboard.cable</code></p>
<dd>Only accept connections on given <font SIZE="-1">HCI</font> and remember the connected device. You can discover your <font SIZE="-1">HCI</font> device addresses with <tt>&quot;hcitool dev&quot;</tt> command.</p>
<dt><code>btkbdd /dev/input/event8 -t </code><font SIZE="-1"><code>EC:55:F9:EF:56:78</code></font></p>
<dd>Initiate a connection to given Bluetooth host. You can discover available devices with <tt>&quot;hcitool scan&quot;</tt>.</dl>
<h2>Bugs</h2>
<p>Bluez <i><a href="/docs/linux/man/8-bluetoothd/">bluetoothd</a></i>(8) daemon is likely to listen for <font SIZE="-1">HID</font> events. For btkbdd to accept connection you need to disable the Bluez input plugin by setting <tt>&quot;DisablePlugins = input&quot;</tt> in <i>/etc/bluetooth/main.conf</i>. </p>
<p> Nothing but errors is logged and when in daemon mode even the error output is lost. Attach <i><a href="/docs/linux/man/1-strace/">strace</a></i>(1) or launch btkbdd manually to troubleshoot errors. </p>
<p> Only a common 101-key keyboard is supported. </p>
<p> To estabilish pairing with iPad, iPod Touch or iPhone, connection must be initiated and authenticated via <i><a href="/docs/linux/man/1-bluetooth-applet/">bluetooth-applet</a></i>(1) before starting btkbdd. Otherwise the device will initiate a PIN-based authentication that is not supported. Once trust is estabilished, connections will work without a need for any other hassle.</p>
<h2>Authors</h2>
<dl>
<dt>&bull;</p>
<dd>Lubomir Rintel &lt;lkundrak [at] v3.sk&gt;</p>
<dt>&bull;</p>
<dd>Collin R. Mulliner &lt;collin [at] betaversion.net&gt; </p>
<p> &lt;<a rel="nofollow" href="http://www.mulliner.org/bluetooth/">http://www.mulliner.org/bluetooth/</a>&gt; </p>
<p> Parts of code were taken from were taken from <i>xkbd-bthid</i> project.</dl>
<p> btkbdd can be redistributed under the same terms and conditions as <i>xkbd-bthid</i> itself: <font SIZE="-1">GNU</font> General Public License (any version at your option). </p>
<p> The source code repository can be obtained from &lt;<a rel="nofollow" href="https://github.com/lkundrak/virtkbd">https://github.com/lkundrak/virtkbd</a>&gt;. Bug fixes and feature ehancements licensed under same conditions as btkbdd are welcome via <font SIZE="-1">GIT</font> pull requests.</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/7-udev/">udev</a></i>(7), <i><a href="/docs/linux/man/1-systemd/">systemd</a></i>(1), <i><a href="/docs/linux/man/5-systemd-service/">systemd.service</a></i>(5), <i><a href="/docs/linux/man/5-systemd-unit/">systemd.unit</a></i>(5), <i><a href="/docs/linux/man/8-bluetoothd/">bluetoothd</a></i>(8), <i><a href="/docs/linux/man/1-hcitool/">hcitool</a></i>(1), <i></i><font SIZE="-1"><i>USB</i></font><i> Device Class Definition for Human Interface Devices (</i><font SIZE="-1"><i>HID</i></font><i>)</i>, <i>Bluetooth </i><font SIZE="-1"><i>HID</i></font><i> Profile</i>. </p>
