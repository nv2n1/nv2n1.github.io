---
title: "rpm-plugin-systemd-inhibit(8)"
name: "rpm-plugin-systemd-inhibit"
section: "8"
letter: "r"
url: "/docs/linux/man/8-rpm-plugin-systemd-inhibit/"
description: "rpm-plugin-systemd-inhibit – Plugin for the RPM Package Manager"
---

<p>rpm-plugin-systemd-inhibit &#8211; Plugin for the RPM Package Manager </p>
<h2>Description</h2>
<p>This plugin for RPM prevents the system to enter shutdown, sleep or idle mode while there is a rpm transaction running to prevent system corruption that can occur if the transaction is interrupted by a reboot. This is achieved by using the inhibit DBUS interface of systemd. The call is roughly equivalent to executing  See <code><a href="/docs/linux/man/1-systemd-inhibit/">systemd-inhibit</a>(1)</code> for the details of this mechanism. It is strongly advised to have the plugin installed on all systemd based systems. </p>
<h2>Prerequisites</h2>
<p>For the plugin to work systemd has to be used as init system and though the DBUS system bus must be available. If the plugin cannot access the interface it gives a warning but does not stop the transaction.</p>
<h2>Configuration</h2>
<p>The plugin currently does not have any configuration option other than turning it on and off. It can be disabled by commenting out the <i>%__transaction_systemd_inhibit</i> macro in main macros file (typically located at <i>/usr/lib/rpm/macros</i>) or otherwise change the value of the macro. </p>
<p> Another option is to remove the plugin from the system if it is packaged in its own sub package.</p>
