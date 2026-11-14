---
title: "mbimcli(1)"
name: "mbimcli"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mbimcli/"
description: "mbimcli – Control MBIM devices"
---

<h2>NAME</h2>
<p> mbimcli &#8211; Control MBIM devices</p>
<h2>DESCRIPTION</h2>
<h3>Usage:</h3>
<dl>
<dt>
<dd> lt-mbimcli [OPTION&#8230;] &#8211; Control MBIM devices</dl>
<h3>Help Options:</h3>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Show help options</p>
<dt><code>&#8211;help-all</code></p>
<dd> Show all help options</p>
<dt><code>&#8211;help-basic-connect</code></p>
<dd> Show Basic Connect Service options</p>
<dt><code>&#8211;help-phonebook</code></p>
<dd> Show Phonebook Service options</p>
<dt><code>&#8211;help-dss</code></p>
<dd> Show Device Service Stream options</p>
<dt><code>&#8211;help-ms-firmware-id</code></p>
<dd> Show Microsoft Firmware ID Service options</p>
<dt><code>&#8211;help-ms-host-shutdown</code></p>
<dd> Show Microsoft Host Shutdown Service options</dl>
<p> Basic Connect options</p>
<dl>
<dt><code>&#8211;query-device-caps</code></p>
<dd> Query device capabilities</p>
<dt><code>&#8211;query-subscriber-ready-status</code></p>
<dd> Query subscriber ready status</p>
<dt><code>&#8211;query-radio-state</code></p>
<dd> Query radio state</p>
<dt><code>&#8211;set-radio-state</code>=<i>,[/</i>(on|off)]</p>
<dd> Set radio state</p>
<dt><code>&#8211;query-device-services</code></p>
<dd> Query device services</p>
<dt><code>&#8211;query-pin-state</code></p>
<dd> Query PIN state</p>
<dt><code>&#8211;enter-pin</code>=<i>,[/</i>(current PIN)]</p>
<dd> Enter PIN</p>
<dt><code>&#8211;change-pin</code>=<i>,[/</i>(current PIN),(new PIN)]</p>
<dd> Change PIN</p>
<dt><code>&#8211;enable-pin</code>=<i>,[/</i>(current PIN)]</p>
<dd> Enable PIN</p>
<dt><code>&#8211;disable-pin</code>=<i>,[/</i>(current PIN)]</p>
<dd> Disable PIN</p>
<dt><code>&#8211;enter-puk</code>=<i>,[/</i>(PUK),(new PIN)]</p>
<dd> Enter PUK</p>
<dt><code>&#8211;query-home-provider</code></p>
<dd> Query home provider</p>
<dt><code>&#8211;query-preferred-providers</code></p>
<dd> Query preferred providers</p>
<dt><code>&#8211;query-visible-providers</code></p>
<dd> Query visible providers</p>
<dt><code>&#8211;query-registration-state</code></p>
<dd> Query registration state</p>
<dt><code>&#8211;register-automatic</code></p>
<dd> Launch automatic registration</p>
<dt><code>&#8211;query-signal-state</code></p>
<dd> Query signal state</p>
<dt><code>&#8211;query-packet-service-state</code></p>
<dd> Query packet service state</p>
<dt><code>&#8211;attach-packet-service</code></p>
<dd> Attach to the packet service</p>
<dt><code>&#8211;detach-packet-service</code></p>
<dd> Detach from the packet service</p>
<dt><code>&#8211;query-connection-state</code>=<i>,[SessionID]/</i></p>
<dd> Query connection state (SessionID is optional, defaults to 0)</p>
<dt><code>&#8211;connect</code>=<i>,[/</i>&quot;key=value,&#8230;&quot;]</p>
<dd> Connect (allowed keys: session-id, apn, auth (PAP|CHAP|MSCHAPV2), username, password)</p>
<dt><code>&#8211;query-ip-configuration</code>=<i>,[SessionID]/</i></p>
<dd> Query IP configuration (SessionID is optional, defaults to 0)</p>
<dt><code>&#8211;disconnect</code>=<i>,[SessionID]/</i></p>
<dd> Disconnect (SessionID is optional, defaults to 0)</p>
<dt><code>&#8211;query-packet-statistics</code></p>
<dd> Query packet statistics</dl>
<p> Phonebook options</p>
<dl>
<dt><code>&#8211;phonebook-query-configuration</code></p>
<dd> Query the phonebook configuration</p>
<dt><code>&#8211;phonebook-read</code>=<i>,[/</i>(Phonebook index)]</p>
<dd> Read phonebook entry with given index</p>
<dt><code>&#8211;phonebook-read-all</code></p>
<dd> Read all phonebook entries</p>
<dt><code>&#8211;phonebook-write</code>=<i>,[/</i>(Name),(Number)[,(Index)]]</p>
<dd> Add new phonebook entry or update an existing one</p>
<dt><code>&#8211;phonebook-delete</code>=<i>,[/</i>(Phonebook index)]</p>
<dd> Delete phonebook entry with given index</p>
<dt><code>&#8211;phonebook-delete-all</code></p>
<dd> Delete all phonebook entries</dl>
<p> Device Service Stream options</p>
<dl>
<dt><code>&#8211;dss-connect</code>=<i>,[/</i>(UUID),(Session ID)]</p>
<dd> Connect DSS session</p>
<dt><code>&#8211;dss-disconnect</code>=<i>,[/</i>(UUID),(Session ID)]</p>
<dd> Disconnect DSS session</dl>
<p> Microsoft Firmware ID options</p>
<dl>
<dt><code>&#8211;ms-query-firmware-id</code></p>
<dd> Query firmware ID</dl>
<p> Microsoft Host Shutdown options</p>
<dl>
<dt><code>&#8211;ms-notify-host-shutdown</code></p>
<dd> Notify that host is shutting down</dl>
<h3>Application Options:</h3>
<dl>
<dt><code>-d</code>, <code>&#8211;device</code>=<i>,[PATH]/</i></p>
<dd> Specify device path</p>
<dt><code>-p</code>, <code>&#8211;device-open-proxy</code></p>
<dd> Request to use the &#8216;mbim-proxy&#8217; proxy</p>
<dt><code>&#8211;no-open</code>=<i>,[Transaction/</i> ID]</p>
<dd> Do not explicitly open the MBIM device before running the command</p>
<dt><code>&#8211;no-close</code></p>
<dd> Do not close the MBIM device after running the command</p>
<dt><code>&#8211;noop</code></p>
<dd> Don&#8217;t run any command</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> Run action with verbose logs, including the debug ones</p>
<dt><code>&#8211;silent</code></p>
<dd> Run action with no logs; not even the error/warning ones</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> Print version</dl>
<p> mbimcli 1.14.0 Copyright (2013-2014) Aleksander Morgado License GPLv2+: GNU GPL version 2 or later &lt;<a rel="nofollow" href="http://gnu.org/licenses/gpl-2.0.html">http://gnu.org/licenses/gpl-2.0.html</a>&gt; This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>mbimcli</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>mbimcli</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
<dd> <code>info mbimcli</code></dl>
<p> should give you access to the complete manual. </p>
<h2>Index</h2>
