---
title: "qmicli(1)"
name: "qmicli"
section: "1"
letter: "q"
url: "/docs/linux/man/1-qmicli/"
description: "qmicli – Control QMI devices"
---

<h2>NAME</h2>
<p> qmicli &#8211; Control QMI devices</p>
<h2>DESCRIPTION</h2>
<h3>Usage:</h3>
<dl>
<dt>
</dt><dd> lt-qmicli [OPTION&#8230;] &#8211; Control QMI devices</dd></dl>
<h3>Help Options:</h3>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> Show help options</dd>
<dt><code>&#8211;help-all</code></dt>
<dd> Show all help options</dd>
<dt><code>&#8211;help-dms</code></dt>
<dd> Show Device Management Service options</dd>
<dt><code>&#8211;help-nas</code></dt>
<dd> Show Network Access Service options</dd>
<dt><code>&#8211;help-wds</code></dt>
<dd> Show Wireless Data Service options</dd>
<dt><code>&#8211;help-pbm</code></dt>
<dd> Show Phonebook Management options</dd>
<dt><code>&#8211;help-uim</code></dt>
<dd> Show User Identity Module options</dd>
<dt><code>&#8211;help-wms</code></dt>
<dd> Show Wireless Messaging Service options</dd>
<dt><code>&#8211;help-wda</code></dt>
<dd> Show Wireless Data Administrative options</dd>
<dt><code>&#8211;help-voice</code></dt>
<dd> Show Voice Service options</dd></dl>
<p> DMS options</p>
<dl>
<dt><code>&#8211;dms-get-ids</code></dt>
<dd> Get IDs</dd>
<dt><code>&#8211;dms-get-capabilities</code></dt>
<dd> Get capabilities</dd>
<dt><code>&#8211;dms-get-manufacturer</code></dt>
<dd> Get manufacturer</dd>
<dt><code>&#8211;dms-get-model</code></dt>
<dd> Get model</dd>
<dt><code>&#8211;dms-get-revision</code></dt>
<dd> Get revision</dd>
<dt><code>&#8211;dms-get-msisdn</code></dt>
<dd> Get MSISDN</dd>
<dt><code>&#8211;dms-get-power-state</code></dt>
<dd> Get power state</dd>
<dt><code>&#8211;dms-uim-set-pin-protection</code>=<i>,[/</i>(PIN|PIN2),(disable|enable),(current PIN)]</dt>
<dd> Set PIN protection in the UIM</dd>
<dt><code>&#8211;dms-uim-verify-pin</code>=<i>,[/</i>(PIN|PIN2),(current PIN)]</dt>
<dd> Verify PIN</dd>
<dt><code>&#8211;dms-uim-unblock-pin</code>=<i>,[/</i>(PIN|PIN2),(PUK),(new PIN)]</dt>
<dd> Unblock PIN</dd>
<dt><code>&#8211;dms-uim-change-pin</code>=<i>,[/</i>(PIN|PIN2),(old PIN),(new PIN)]</dt>
<dd> Change PIN</dd>
<dt><code>&#8211;dms-uim-get-pin-status</code></dt>
<dd> Get PIN status</dd>
<dt><code>&#8211;dms-uim-get-iccid</code></dt>
<dd> Get ICCID</dd>
<dt><code>&#8211;dms-uim-get-imsi</code></dt>
<dd> Get IMSI</dd>
<dt><code>&#8211;dms-uim-get-state</code></dt>
<dd> Get UIM State</dd>
<dt><code>&#8211;dms-uim-get-ck-status</code>=<i>,[/</i>(pn|pu|pp|pc|pf)]</dt>
<dd> Get CK Status</dd>
<dt><code>&#8211;dms-uim-set-ck-protection</code>=<i>,[/</i>(pn|pu|pp|pc|pf),(disable),(key)]</dt>
<dd> Disable CK protection</dd>
<dt><code>&#8211;dms-uim-unblock-ck</code>=<i>,[/</i>(pn|pu|pp|pc|pf),(key)]</dt>
<dd> Unblock CK</dd>
<dt><code>&#8211;dms-get-hardware-revision</code></dt>
<dd> Get the HW revision</dd>
<dt><code>&#8211;dms-get-operating-mode</code></dt>
<dd> Get the device operating mode</dd>
<dt><code>&#8211;dms-set-operating-mode</code>=<i>,[/</i>(Operating mode)]</dt>
<dd> Set the device operating mode</dd>
<dt><code>&#8211;dms-get-time</code></dt>
<dd> Get the device time</dd>
<dt><code>&#8211;dms-get-prl-version</code></dt>
<dd> Get the PRL version</dd>
<dt><code>&#8211;dms-get-activation-state</code></dt>
<dd> Get the state of the service activation</dd>
<dt><code>&#8211;dms-activate-automatic</code>=<i>,[Activation/</i> Code]</dt>
<dd> Request automatic service activation</dd>
<dt><code>&#8211;dms-activate-manual</code>=<i>,[SPC/</i>,SID,MDN,MIN]</dt>
<dd> Request manual service activation</dd>
<dt><code>&#8211;dms-get-user-lock-state</code></dt>
<dd> Get the state of the user lock</dd>
<dt><code>&#8211;dms-set-user-lock-state</code>=<i>,[/</i>(disable|enable),(current lock code)]</dt>
<dd> Set the state of the user lock</dd>
<dt><code>&#8211;dms-set-user-lock-code</code>=<i>,[/</i>(old lock code),(new lock code)]</dt>
<dd> Change the user lock code</dd>
<dt><code>&#8211;dms-read-user-data</code></dt>
<dd> Read user data</dd>
<dt><code>&#8211;dms-write-user-data</code>=<i>,[/</i>(User data)]</dt>
<dd> Write user data</dd>
<dt><code>&#8211;dms-read-eri-file</code></dt>
<dd> Read ERI file</dd>
<dt><code>&#8211;dms-restore-factory-defaults</code>=<i>,[/</i>(Service Programming Code)]</dt>
<dd> Restore factory defaults</dd>
<dt><code>&#8211;dms-validate-service-programming-code</code>=<i>,[/</i>(Service Programming Code)]</dt>
<dd> Validate the Service Programming Code</dd>
<dt><code>&#8211;dms-get-band-capabilities</code></dt>
<dd> Get band capabilities</dd>
<dt><code>&#8211;dms-get-factory-sku</code></dt>
<dd> Get factory stock keeping unit</dd>
<dt><code>&#8211;dms-list-stored-images</code></dt>
<dd> List stored images</dd>
<dt><code>&#8211;dms-select-stored-image</code>=<i>,[modem/</i>#,pri#] where # is the index</dt>
<dd> Select stored image</dd>
<dt><code>&#8211;dms-delete-stored-image</code>=<i>,[modem/</i>#|pri#] where # is the index</dt>
<dd> Delete stored image</dd>
<dt><code>&#8211;dms-set-fcc-authentication</code></dt>
<dd> Set FCC authentication</dd>
<dt><code>&#8211;dms-get-supported-messages</code></dt>
<dd> Get supported messages</dd>
<dt><code>&#8211;dms-reset</code></dt>
<dd> Reset the service state</dd>
<dt><code>&#8211;dms-noop</code></dt>
<dd> Just allocate or release a DMS client. Use with `&#8211;client-no-release-cid&#8217; and/or `&#8211;client-cid&#8217;</dd></dl>
<p> NAS options</p>
<dl>
<dt><code>&#8211;nas-get-signal-strength</code></dt>
<dd> Get signal strength</dd>
<dt><code>&#8211;nas-get-signal-info</code></dt>
<dd> Get signal info</dd>
<dt><code>&#8211;nas-get-tx-rx-info</code>=<i>,[/</i>(Radio Interface)]</dt>
<dd> Get TX/RX info</dd>
<dt><code>&#8211;nas-get-home-network</code></dt>
<dd> Get home network</dd>
<dt><code>&#8211;nas-get-serving-system</code></dt>
<dd> Get serving system</dd>
<dt><code>&#8211;nas-get-system-info</code></dt>
<dd> Get system info</dd>
<dt><code>&#8211;nas-get-technology-preference</code></dt>
<dd> Get technology preference</dd>
<dt><code>&#8211;nas-get-system-selection-preference</code></dt>
<dd> Get system selection preference</dd>
<dt><code>&#8211;nas-set-system-selection-preference</code>=<i>,[cdma-1x/</i>|cdma-1xevdo|gsm|umts|lte|td-scdma]</dt>
<dd> Set system selection preference</dd>
<dt><code>&#8211;nas-network-scan</code></dt>
<dd> Scan networks</dd>
<dt><code>&#8211;nas-get-cell-location-info</code></dt>
<dd> Get Cell Location Info</dd>
<dt><code>&#8211;nas-force-network-search</code></dt>
<dd> Force network search</dd>
<dt><code>&#8211;nas-get-lte-cphy-ca-info</code></dt>
<dd> Get LTE Cphy CA Info</dd>
<dt><code>&#8211;nas-get-supported-messages</code></dt>
<dd> Get supported messages</dd>
<dt><code>&#8211;nas-reset</code></dt>
<dd> Reset the service state</dd>
<dt><code>&#8211;nas-noop</code></dt>
<dd> Just allocate or release a NAS client. Use with `&#8211;client-no-release-cid&#8217; and/or `&#8211;client-cid&#8217;</dd></dl>
<p> WDS options</p>
<dl>
<dt><code>&#8211;wds-start-network</code>=<i>,[/</i>&quot;key=value,&#8230;&quot;]</dt>
<dd> Start network (allowed keys: apn, 3gpp-profile, 3gpp2-profile, auth (PAP|CHAP|BOTH), username, password, autoconnect=yes)</dd>
<dt><code>&#8211;wds-follow-network</code></dt>
<dd> Follow the network status until disconnected. Use with `&#8211;wds-start-network&#8217;</dd>
<dt><code>&#8211;wds-stop-network</code>=<i>,[Packet/</i> data handle] OR [disable-autoconnect]</dt>
<dd> Stop network</dd>
<dt><code>&#8211;wds-get-current-settings</code></dt>
<dd> Get current settings</dd>
<dt><code>&#8211;wds-get-packet-service-status</code></dt>
<dd> Get packet service status</dd>
<dt><code>&#8211;wds-get-packet-statistics</code></dt>
<dd> Get packet statistics</dd>
<dt><code>&#8211;wds-get-data-bearer-technology</code></dt>
<dd> Get data bearer technology</dd>
<dt><code>&#8211;wds-get-current-data-bearer-technology</code></dt>
<dd> Get current data bearer technology</dd>
<dt><code>&#8211;wds-get-profile-list</code>=<i>,[3gpp/</i>|3gpp2]</dt>
<dd> Get profile list</dd>
<dt><code>&#8211;wds-get-default-settings</code>=<i>,[3gpp/</i>|3gpp2]</dt>
<dd> Get default settings</dd>
<dt><code>&#8211;wds-get-autoconnect-settings</code></dt>
<dd> Get autoconnect settings</dd>
<dt><code>&#8211;wds-set-autoconnect-settings</code>=<i>,[/</i>(enabled|disabled|paused)[,(roaming-allowed|home-only)]]</dt>
<dd> Set autoconnect settings (roaming settings optional)</dd>
<dt><code>&#8211;wds-get-supported-messages</code></dt>
<dd> Get supported messages</dd>
<dt><code>&#8211;wds-reset</code></dt>
<dd> Reset the service state</dd>
<dt><code>&#8211;wds-noop</code></dt>
<dd> Just allocate or release a WDS client. Use with `&#8211;client-no-release-cid&#8217; and/or `&#8211;client-cid&#8217;</dd></dl>
<p> PBM options</p>
<dl>
<dt><code>&#8211;pbm-get-all-capabilities</code></dt>
<dd> Get all phonebook capabilities</dd>
<dt><code>&#8211;pbm-noop</code></dt>
<dd> Just allocate or release a PBM client. Use with `&#8211;client-no-release-cid&#8217; and/or `&#8211;client-cid&#8217;</dd></dl>
<p> UIM options</p>
<dl>
<dt><code>&#8211;uim-set-pin-protection</code>=<i>,[/</i>(PIN1|PIN2|UPIN),(disable|enable),(current PIN)]</dt>
<dd> Set PIN protection</dd>
<dt><code>&#8211;uim-verify-pin</code>=<i>,[/</i>(PIN1|PIN2|UPIN),(current PIN)]</dt>
<dd> Verify PIN</dd>
<dt><code>&#8211;uim-unblock-pin</code>=<i>,[/</i>(PIN1|PIN2|UPIN),(PUK),(new PIN)]</dt>
<dd> Unblock PIN</dd>
<dt><code>&#8211;uim-change-pin</code>=<i>,[/</i>(PIN1|PIN2|UPIN),(old PIN),(new PIN)]</dt>
<dd> Change PIN</dd>
<dt><code>&#8211;uim-read-transparent</code>=<i>,[0xNNNN/</i>,0xNNNN,&#8230;]</dt>
<dd> Read a transparent file given the file path</dd>
<dt><code>&#8211;uim-get-file-attributes</code>=<i>,[0xNNNN/</i>,0xNNNN,&#8230;]</dt>
<dd> Get the attributes of a given file</dd>
<dt><code>&#8211;uim-get-card-status</code></dt>
<dd> Get card status</dd>
<dt><code>&#8211;uim-get-supported-messages</code></dt>
<dd> Get supported messages</dd>
<dt><code>&#8211;uim-reset</code></dt>
<dd> Reset the service state</dd>
<dt><code>&#8211;uim-noop</code></dt>
<dd> Just allocate or release a UIM client. Use with `&#8211;client-no-release-cid&#8217; and/or `&#8211;client-cid&#8217;</dd></dl>
<p> WMS options</p>
<dl>
<dt><code>&#8211;wms-get-supported-messages</code></dt>
<dd> Get supported messages</dd>
<dt><code>&#8211;wms-reset</code></dt>
<dd> Reset the service state</dd>
<dt><code>&#8211;wms-noop</code></dt>
<dd> Just allocate or release a WMS client. Use with `&#8211;client-no-release-cid&#8217; and/or `&#8211;client-cid&#8217;</dd></dl>
<p> WDA options</p>
<dl>
<dt><code>&#8211;wda-set-data-format</code>=<i>,[raw-ip/</i>|802-3]</dt>
<dd> Set data format</dd>
<dt><code>&#8211;wda-get-data-format</code></dt>
<dd> Get data format</dd>
<dt><code>&#8211;wda-get-supported-messages</code></dt>
<dd> Get supported messages</dd>
<dt><code>&#8211;wda-noop</code></dt>
<dd> Just allocate or release a WDA client. Use with `&#8211;client-no-release-cid&#8217; and/or `&#8211;client-cid&#8217;</dd></dl>
<p> VOICE options</p>
<dl>
<dt><code>&#8211;voice-get-config</code></dt>
<dd> Get Voice service configuration</dd>
<dt><code>&#8211;voice-get-supported-messages</code></dt>
<dd> Get supported messages</dd>
<dt><code>&#8211;voice-noop</code></dt>
<dd> Just allocate or release a VOICE client. Use with `&#8211;client-no-release-cid&#8217; and/or `&#8211;client-cid&#8217;</dd></dl>
<h3>Application Options:</h3>
<dl>
<dt><code>-d</code>, <code>&#8211;device</code>=<i>,[PATH]/</i></dt>
<dd> Specify device path</dd>
<dt><code>-w</code>, <code>&#8211;get-wwan-iface</code></dt>
<dd> Get the WWAN iface name associated with this control port</dd>
<dt><code>-e</code>, <code>&#8211;get-expected-data-format</code></dt>
<dd> Get the expected data format in the WWAN iface</dd>
<dt><code>-E</code>, <code>&#8211;set-expected-data-format</code>=<i>,[802-3/</i>|raw-ip]</dt>
<dd> Set the expected data format in the WWAN iface</dd>
<dt><code>&#8211;get-service-version-info</code></dt>
<dd> Get service version info</dd>
<dt><code>&#8211;device-set-instance-id</code>=<i>,[Instance/</i> ID]</dt>
<dd> Set instance ID</dd>
<dt><code>&#8211;device-open-version-info</code></dt>
<dd> Run version info check when opening device</dd>
<dt><code>&#8211;device-open-sync</code></dt>
<dd> Run sync operation when opening device</dd>
<dt><code>-p</code>, <code>&#8211;device-open-proxy</code></dt>
<dd> Request to use the &#8216;qmi-proxy&#8217; proxy</dd>
<dt><code>&#8211;device-open-mbim</code></dt>
<dd> Open an MBIM device with EXT_QMUX support</dd>
<dt><code>&#8211;device-open-net</code>=<i>,[net-802-3/</i>|net-raw-ip|net-qos-header|net-no-qos-header]</dt>
<dd> Open device with specific link protocol and QoS flags</dd>
<dt><code>&#8211;client-cid</code>=<i>,[CID]/</i></dt>
<dd> Use the given CID, don&#8217;t allocate a new one</dd>
<dt><code>&#8211;client-no-release-cid</code></dt>
<dd> Do not release the CID when exiting</dd>
<dt><code>-v</code>, <code>&#8211;verbose</code></dt>
<dd> Run action with verbose logs, including the debug ones</dd>
<dt><code>&#8211;silent</code></dt>
<dd> Run action with no logs; not even the error/warning ones</dd>
<dt><code>-V</code>, <code>&#8211;version</code></dt>
<dd> Print version</dd></dl>
<p> qmicli 1.15.0 Copyright &#169; 2015 Aleksander Morgado License GPLv2+: GNU GPL version 2 or later &lt;<a rel="nofollow" href="http://gnu.org/licenses/gpl-2.0.html">http://gnu.org/licenses/gpl-2.0.html</a>&gt; This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>qmicli</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>qmicli</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
</dt><dd> <code>info qmicli</code></dd></dl>
<p> should give you access to the complete manual. </p>
<h2>Index</h2>
