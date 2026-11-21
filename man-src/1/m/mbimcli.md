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
</dt><dd> lt-mbimcli [OPTION&#8230;] &#8211; Control MBIM devices</dd></dl>
<h3>Help Options:</h3>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> Show help options</dd>
<dt><code>&#8211;help-all</code></dt>
<dd> Show all help options</dd>
<dt><code>&#8211;help-basic-connect</code></dt>
<dd> Show Basic Connect Service options</dd>
<dt><code>&#8211;help-phonebook</code></dt>
<dd> Show Phonebook Service options</dd>
<dt><code>&#8211;help-dss</code></dt>
<dd> Show Device Service Stream options</dd>
<dt><code>&#8211;help-ms-firmware-id</code></dt>
<dd> Show Microsoft Firmware ID Service options</dd>
<dt><code>&#8211;help-ms-host-shutdown</code></dt>
<dd> Show Microsoft Host Shutdown Service options</dd></dl>
<p> Basic Connect options</p>
<dl>
<dt><code>&#8211;query-device-caps</code></dt>
<dd> Query device capabilities</dd>
<dt><code>&#8211;query-subscriber-ready-status</code></dt>
<dd> Query subscriber ready status</dd>
<dt><code>&#8211;query-radio-state</code></dt>
<dd> Query radio state</dd>
<dt><code>&#8211;set-radio-state</code>=<i>,[/</i>(on|off)]</dt>
<dd> Set radio state</dd>
<dt><code>&#8211;query-device-services</code></dt>
<dd> Query device services</dd>
<dt><code>&#8211;query-pin-state</code></dt>
<dd> Query PIN state</dd>
<dt><code>&#8211;enter-pin</code>=<i>,[/</i>(current PIN)]</dt>
<dd> Enter PIN</dd>
<dt><code>&#8211;change-pin</code>=<i>,[/</i>(current PIN),(new PIN)]</dt>
<dd> Change PIN</dd>
<dt><code>&#8211;enable-pin</code>=<i>,[/</i>(current PIN)]</dt>
<dd> Enable PIN</dd>
<dt><code>&#8211;disable-pin</code>=<i>,[/</i>(current PIN)]</dt>
<dd> Disable PIN</dd>
<dt><code>&#8211;enter-puk</code>=<i>,[/</i>(PUK),(new PIN)]</dt>
<dd> Enter PUK</dd>
<dt><code>&#8211;query-home-provider</code></dt>
<dd> Query home provider</dd>
<dt><code>&#8211;query-preferred-providers</code></dt>
<dd> Query preferred providers</dd>
<dt><code>&#8211;query-visible-providers</code></dt>
<dd> Query visible providers</dd>
<dt><code>&#8211;query-registration-state</code></dt>
<dd> Query registration state</dd>
<dt><code>&#8211;register-automatic</code></dt>
<dd> Launch automatic registration</dd>
<dt><code>&#8211;query-signal-state</code></dt>
<dd> Query signal state</dd>
<dt><code>&#8211;query-packet-service-state</code></dt>
<dd> Query packet service state</dd>
<dt><code>&#8211;attach-packet-service</code></dt>
<dd> Attach to the packet service</dd>
<dt><code>&#8211;detach-packet-service</code></dt>
<dd> Detach from the packet service</dd>
<dt><code>&#8211;query-connection-state</code>=<i>,[SessionID]/</i></dt>
<dd> Query connection state (SessionID is optional, defaults to 0)</dd>
<dt><code>&#8211;connect</code>=<i>,[/</i>&quot;key=value,&#8230;&quot;]</dt>
<dd> Connect (allowed keys: session-id, apn, auth (PAP|CHAP|MSCHAPV2), username, password)</dd>
<dt><code>&#8211;query-ip-configuration</code>=<i>,[SessionID]/</i></dt>
<dd> Query IP configuration (SessionID is optional, defaults to 0)</dd>
<dt><code>&#8211;disconnect</code>=<i>,[SessionID]/</i></dt>
<dd> Disconnect (SessionID is optional, defaults to 0)</dd>
<dt><code>&#8211;query-packet-statistics</code></dt>
<dd> Query packet statistics</dd></dl>
<p> Phonebook options</p>
<dl>
<dt><code>&#8211;phonebook-query-configuration</code></dt>
<dd> Query the phonebook configuration</dd>
<dt><code>&#8211;phonebook-read</code>=<i>,[/</i>(Phonebook index)]</dt>
<dd> Read phonebook entry with given index</dd>
<dt><code>&#8211;phonebook-read-all</code></dt>
<dd> Read all phonebook entries</dd>
<dt><code>&#8211;phonebook-write</code>=<i>,[/</i>(Name),(Number)[,(Index)]]</dt>
<dd> Add new phonebook entry or update an existing one</dd>
<dt><code>&#8211;phonebook-delete</code>=<i>,[/</i>(Phonebook index)]</dt>
<dd> Delete phonebook entry with given index</dd>
<dt><code>&#8211;phonebook-delete-all</code></dt>
<dd> Delete all phonebook entries</dd></dl>
<p> Device Service Stream options</p>
<dl>
<dt><code>&#8211;dss-connect</code>=<i>,[/</i>(UUID),(Session ID)]</dt>
<dd> Connect DSS session</dd>
<dt><code>&#8211;dss-disconnect</code>=<i>,[/</i>(UUID),(Session ID)]</dt>
<dd> Disconnect DSS session</dd></dl>
<p> Microsoft Firmware ID options</p>
<dl>
<dt><code>&#8211;ms-query-firmware-id</code></dt>
<dd> Query firmware ID</dd></dl>
<p> Microsoft Host Shutdown options</p>
<dl>
<dt><code>&#8211;ms-notify-host-shutdown</code></dt>
<dd> Notify that host is shutting down</dd></dl>
<h3>Application Options:</h3>
<dl>
<dt><code>-d</code>, <code>&#8211;device</code>=<i>,[PATH]/</i></dt>
<dd> Specify device path</dd>
<dt><code>-p</code>, <code>&#8211;device-open-proxy</code></dt>
<dd> Request to use the &#8216;mbim-proxy&#8217; proxy</dd>
<dt><code>&#8211;no-open</code>=<i>,[Transaction/</i> ID]</dt>
<dd> Do not explicitly open the MBIM device before running the command</dd>
<dt><code>&#8211;no-close</code></dt>
<dd> Do not close the MBIM device after running the command</dd>
<dt><code>&#8211;noop</code></dt>
<dd> Don&#8217;t run any command</dd>
<dt><code>-v</code>, <code>&#8211;verbose</code></dt>
<dd> Run action with verbose logs, including the debug ones</dd>
<dt><code>&#8211;silent</code></dt>
<dd> Run action with no logs; not even the error/warning ones</dd>
<dt><code>-V</code>, <code>&#8211;version</code></dt>
<dd> Print version</dd></dl>
<p> mbimcli 1.14.0 Copyright (2013-2014) Aleksander Morgado License GPLv2+: GNU GPL version 2 or later &lt;<a rel="nofollow" href="http://gnu.org/licenses/gpl-2.0.html">http://gnu.org/licenses/gpl-2.0.html</a>&gt; This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>mbimcli</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>mbimcli</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
</dt><dd> <code>info mbimcli</code></dd></dl>
<p> should give you access to the complete manual. </p>
