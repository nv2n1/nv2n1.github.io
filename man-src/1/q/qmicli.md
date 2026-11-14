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
<dd> lt-qmicli [OPTION&#8230;] &#8211; Control QMI devices</dl>
<h3>Help Options:</h3>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Show help options</p>
<dt><code>&#8211;help-all</code></p>
<dd> Show all help options</p>
<dt><code>&#8211;help-dms</code></p>
<dd> Show Device Management Service options</p>
<dt><code>&#8211;help-nas</code></p>
<dd> Show Network Access Service options</p>
<dt><code>&#8211;help-wds</code></p>
<dd> Show Wireless Data Service options</p>
<dt><code>&#8211;help-pbm</code></p>
<dd> Show Phonebook Management options</p>
<dt><code>&#8211;help-uim</code></p>
<dd> Show User Identity Module options</p>
<dt><code>&#8211;help-wms</code></p>
<dd> Show Wireless Messaging Service options</p>
<dt><code>&#8211;help-wda</code></p>
<dd> Show Wireless Data Administrative options</p>
<dt><code>&#8211;help-voice</code></p>
<dd> Show Voice Service options</dl>
<p> DMS options</p>
<dl>
<dt><code>&#8211;dms-get-ids</code></p>
<dd> Get IDs</p>
<dt><code>&#8211;dms-get-capabilities</code></p>
<dd> Get capabilities</p>
<dt><code>&#8211;dms-get-manufacturer</code></p>
<dd> Get manufacturer</p>
<dt><code>&#8211;dms-get-model</code></p>
<dd> Get model</p>
<dt><code>&#8211;dms-get-revision</code></p>
<dd> Get revision</p>
<dt><code>&#8211;dms-get-msisdn</code></p>
<dd> Get MSISDN</p>
<dt><code>&#8211;dms-get-power-state</code></p>
<dd> Get power state</p>
<dt><code>&#8211;dms-uim-set-pin-protection</code>=<i>,[/</i>(PIN|PIN2),(disable|enable),(current PIN)]</p>
<dd> Set PIN protection in the UIM</p>
<dt><code>&#8211;dms-uim-verify-pin</code>=<i>,[/</i>(PIN|PIN2),(current PIN)]</p>
<dd> Verify PIN</p>
<dt><code>&#8211;dms-uim-unblock-pin</code>=<i>,[/</i>(PIN|PIN2),(PUK),(new PIN)]</p>
<dd> Unblock PIN</p>
<dt><code>&#8211;dms-uim-change-pin</code>=<i>,[/</i>(PIN|PIN2),(old PIN),(new PIN)]</p>
<dd> Change PIN</p>
<dt><code>&#8211;dms-uim-get-pin-status</code></p>
<dd> Get PIN status</p>
<dt><code>&#8211;dms-uim-get-iccid</code></p>
<dd> Get ICCID</p>
<dt><code>&#8211;dms-uim-get-imsi</code></p>
<dd> Get IMSI</p>
<dt><code>&#8211;dms-uim-get-state</code></p>
<dd> Get UIM State</p>
<dt><code>&#8211;dms-uim-get-ck-status</code>=<i>,[/</i>(pn|pu|pp|pc|pf)]</p>
<dd> Get CK Status</p>
<dt><code>&#8211;dms-uim-set-ck-protection</code>=<i>,[/</i>(pn|pu|pp|pc|pf),(disable),(key)]</p>
<dd> Disable CK protection</p>
<dt><code>&#8211;dms-uim-unblock-ck</code>=<i>,[/</i>(pn|pu|pp|pc|pf),(key)]</p>
<dd> Unblock CK</p>
<dt><code>&#8211;dms-get-hardware-revision</code></p>
<dd> Get the HW revision</p>
<dt><code>&#8211;dms-get-operating-mode</code></p>
<dd> Get the device operating mode</p>
<dt><code>&#8211;dms-set-operating-mode</code>=<i>,[/</i>(Operating mode)]</p>
<dd> Set the device operating mode</p>
<dt><code>&#8211;dms-get-time</code></p>
<dd> Get the device time</p>
<dt><code>&#8211;dms-get-prl-version</code></p>
<dd> Get the PRL version</p>
<dt><code>&#8211;dms-get-activation-state</code></p>
<dd> Get the state of the service activation</p>
<dt><code>&#8211;dms-activate-automatic</code>=<i>,[Activation/</i> Code]</p>
<dd> Request automatic service activation</p>
<dt><code>&#8211;dms-activate-manual</code>=<i>,[SPC/</i>,SID,MDN,MIN]</p>
<dd> Request manual service activation</p>
<dt><code>&#8211;dms-get-user-lock-state</code></p>
<dd> Get the state of the user lock</p>
<dt><code>&#8211;dms-set-user-lock-state</code>=<i>,[/</i>(disable|enable),(current lock code)]</p>
<dd> Set the state of the user lock</p>
<dt><code>&#8211;dms-set-user-lock-code</code>=<i>,[/</i>(old lock code),(new lock code)]</p>
<dd> Change the user lock code</p>
<dt><code>&#8211;dms-read-user-data</code></p>
<dd> Read user data</p>
<dt><code>&#8211;dms-write-user-data</code>=<i>,[/</i>(User data)]</p>
<dd> Write user data</p>
<dt><code>&#8211;dms-read-eri-file</code></p>
<dd> Read ERI file</p>
<dt><code>&#8211;dms-restore-factory-defaults</code>=<i>,[/</i>(Service Programming Code)]</p>
<dd> Restore factory defaults</p>
<dt><code>&#8211;dms-validate-service-programming-code</code>=<i>,[/</i>(Service Programming Code)]</p>
<dd> Validate the Service Programming Code</p>
<dt><code>&#8211;dms-get-band-capabilities</code></p>
<dd> Get band capabilities</p>
<dt><code>&#8211;dms-get-factory-sku</code></p>
<dd> Get factory stock keeping unit</p>
<dt><code>&#8211;dms-list-stored-images</code></p>
<dd> List stored images</p>
<dt><code>&#8211;dms-select-stored-image</code>=<i>,[modem/</i>#,pri#] where # is the index</p>
<dd> Select stored image</p>
<dt><code>&#8211;dms-delete-stored-image</code>=<i>,[modem/</i>#|pri#] where # is the index</p>
<dd> Delete stored image</p>
<dt><code>&#8211;dms-set-fcc-authentication</code></p>
<dd> Set FCC authentication</p>
<dt><code>&#8211;dms-get-supported-messages</code></p>
<dd> Get supported messages</p>
<dt><code>&#8211;dms-reset</code></p>
<dd> Reset the service state</p>
<dt><code>&#8211;dms-noop</code></p>
<dd> Just allocate or release a DMS client. Use with `&#8211;client-no-release-cid&#8217; and/or `&#8211;client-cid&#8217;</dl>
<p> NAS options</p>
<dl>
<dt><code>&#8211;nas-get-signal-strength</code></p>
<dd> Get signal strength</p>
<dt><code>&#8211;nas-get-signal-info</code></p>
<dd> Get signal info</p>
<dt><code>&#8211;nas-get-tx-rx-info</code>=<i>,[/</i>(Radio Interface)]</p>
<dd> Get TX/RX info</p>
<dt><code>&#8211;nas-get-home-network</code></p>
<dd> Get home network</p>
<dt><code>&#8211;nas-get-serving-system</code></p>
<dd> Get serving system</p>
<dt><code>&#8211;nas-get-system-info</code></p>
<dd> Get system info</p>
<dt><code>&#8211;nas-get-technology-preference</code></p>
<dd> Get technology preference</p>
<dt><code>&#8211;nas-get-system-selection-preference</code></p>
<dd> Get system selection preference</p>
<dt><code>&#8211;nas-set-system-selection-preference</code>=<i>,[cdma-1x/</i>|cdma-1xevdo|gsm|umts|lte|td-scdma]</p>
<dd> Set system selection preference</p>
<dt><code>&#8211;nas-network-scan</code></p>
<dd> Scan networks</p>
<dt><code>&#8211;nas-get-cell-location-info</code></p>
<dd> Get Cell Location Info</p>
<dt><code>&#8211;nas-force-network-search</code></p>
<dd> Force network search</p>
<dt><code>&#8211;nas-get-lte-cphy-ca-info</code></p>
<dd> Get LTE Cphy CA Info</p>
<dt><code>&#8211;nas-get-supported-messages</code></p>
<dd> Get supported messages</p>
<dt><code>&#8211;nas-reset</code></p>
<dd> Reset the service state</p>
<dt><code>&#8211;nas-noop</code></p>
<dd> Just allocate or release a NAS client. Use with `&#8211;client-no-release-cid&#8217; and/or `&#8211;client-cid&#8217;</dl>
<p> WDS options</p>
<dl>
<dt><code>&#8211;wds-start-network</code>=<i>,[/</i>&quot;key=value,&#8230;&quot;]</p>
<dd> Start network (allowed keys: apn, 3gpp-profile, 3gpp2-profile, auth (PAP|CHAP|BOTH), username, password, autoconnect=yes)</p>
<dt><code>&#8211;wds-follow-network</code></p>
<dd> Follow the network status until disconnected. Use with `&#8211;wds-start-network&#8217;</p>
<dt><code>&#8211;wds-stop-network</code>=<i>,[Packet/</i> data handle] OR [disable-autoconnect]</p>
<dd> Stop network</p>
<dt><code>&#8211;wds-get-current-settings</code></p>
<dd> Get current settings</p>
<dt><code>&#8211;wds-get-packet-service-status</code></p>
<dd> Get packet service status</p>
<dt><code>&#8211;wds-get-packet-statistics</code></p>
<dd> Get packet statistics</p>
<dt><code>&#8211;wds-get-data-bearer-technology</code></p>
<dd> Get data bearer technology</p>
<dt><code>&#8211;wds-get-current-data-bearer-technology</code></p>
<dd> Get current data bearer technology</p>
<dt><code>&#8211;wds-get-profile-list</code>=<i>,[3gpp/</i>|3gpp2]</p>
<dd> Get profile list</p>
<dt><code>&#8211;wds-get-default-settings</code>=<i>,[3gpp/</i>|3gpp2]</p>
<dd> Get default settings</p>
<dt><code>&#8211;wds-get-autoconnect-settings</code></p>
<dd> Get autoconnect settings</p>
<dt><code>&#8211;wds-set-autoconnect-settings</code>=<i>,[/</i>(enabled|disabled|paused)[,(roaming-allowed|home-only)]]</p>
<dd> Set autoconnect settings (roaming settings optional)</p>
<dt><code>&#8211;wds-get-supported-messages</code></p>
<dd> Get supported messages</p>
<dt><code>&#8211;wds-reset</code></p>
<dd> Reset the service state</p>
<dt><code>&#8211;wds-noop</code></p>
<dd> Just allocate or release a WDS client. Use with `&#8211;client-no-release-cid&#8217; and/or `&#8211;client-cid&#8217;</dl>
<p> PBM options</p>
<dl>
<dt><code>&#8211;pbm-get-all-capabilities</code></p>
<dd> Get all phonebook capabilities</p>
<dt><code>&#8211;pbm-noop</code></p>
<dd> Just allocate or release a PBM client. Use with `&#8211;client-no-release-cid&#8217; and/or `&#8211;client-cid&#8217;</dl>
<p> UIM options</p>
<dl>
<dt><code>&#8211;uim-set-pin-protection</code>=<i>,[/</i>(PIN1|PIN2|UPIN),(disable|enable),(current PIN)]</p>
<dd> Set PIN protection</p>
<dt><code>&#8211;uim-verify-pin</code>=<i>,[/</i>(PIN1|PIN2|UPIN),(current PIN)]</p>
<dd> Verify PIN</p>
<dt><code>&#8211;uim-unblock-pin</code>=<i>,[/</i>(PIN1|PIN2|UPIN),(PUK),(new PIN)]</p>
<dd> Unblock PIN</p>
<dt><code>&#8211;uim-change-pin</code>=<i>,[/</i>(PIN1|PIN2|UPIN),(old PIN),(new PIN)]</p>
<dd> Change PIN</p>
<dt><code>&#8211;uim-read-transparent</code>=<i>,[0xNNNN/</i>,0xNNNN,&#8230;]</p>
<dd> Read a transparent file given the file path</p>
<dt><code>&#8211;uim-get-file-attributes</code>=<i>,[0xNNNN/</i>,0xNNNN,&#8230;]</p>
<dd> Get the attributes of a given file</p>
<dt><code>&#8211;uim-get-card-status</code></p>
<dd> Get card status</p>
<dt><code>&#8211;uim-get-supported-messages</code></p>
<dd> Get supported messages</p>
<dt><code>&#8211;uim-reset</code></p>
<dd> Reset the service state</p>
<dt><code>&#8211;uim-noop</code></p>
<dd> Just allocate or release a UIM client. Use with `&#8211;client-no-release-cid&#8217; and/or `&#8211;client-cid&#8217;</dl>
<p> WMS options</p>
<dl>
<dt><code>&#8211;wms-get-supported-messages</code></p>
<dd> Get supported messages</p>
<dt><code>&#8211;wms-reset</code></p>
<dd> Reset the service state</p>
<dt><code>&#8211;wms-noop</code></p>
<dd> Just allocate or release a WMS client. Use with `&#8211;client-no-release-cid&#8217; and/or `&#8211;client-cid&#8217;</dl>
<p> WDA options</p>
<dl>
<dt><code>&#8211;wda-set-data-format</code>=<i>,[raw-ip/</i>|802-3]</p>
<dd> Set data format</p>
<dt><code>&#8211;wda-get-data-format</code></p>
<dd> Get data format</p>
<dt><code>&#8211;wda-get-supported-messages</code></p>
<dd> Get supported messages</p>
<dt><code>&#8211;wda-noop</code></p>
<dd> Just allocate or release a WDA client. Use with `&#8211;client-no-release-cid&#8217; and/or `&#8211;client-cid&#8217;</dl>
<p> VOICE options</p>
<dl>
<dt><code>&#8211;voice-get-config</code></p>
<dd> Get Voice service configuration</p>
<dt><code>&#8211;voice-get-supported-messages</code></p>
<dd> Get supported messages</p>
<dt><code>&#8211;voice-noop</code></p>
<dd> Just allocate or release a VOICE client. Use with `&#8211;client-no-release-cid&#8217; and/or `&#8211;client-cid&#8217;</dl>
<h3>Application Options:</h3>
<dl>
<dt><code>-d</code>, <code>&#8211;device</code>=<i>,[PATH]/</i></p>
<dd> Specify device path</p>
<dt><code>-w</code>, <code>&#8211;get-wwan-iface</code></p>
<dd> Get the WWAN iface name associated with this control port</p>
<dt><code>-e</code>, <code>&#8211;get-expected-data-format</code></p>
<dd> Get the expected data format in the WWAN iface</p>
<dt><code>-E</code>, <code>&#8211;set-expected-data-format</code>=<i>,[802-3/</i>|raw-ip]</p>
<dd> Set the expected data format in the WWAN iface</p>
<dt><code>&#8211;get-service-version-info</code></p>
<dd> Get service version info</p>
<dt><code>&#8211;device-set-instance-id</code>=<i>,[Instance/</i> ID]</p>
<dd> Set instance ID</p>
<dt><code>&#8211;device-open-version-info</code></p>
<dd> Run version info check when opening device</p>
<dt><code>&#8211;device-open-sync</code></p>
<dd> Run sync operation when opening device</p>
<dt><code>-p</code>, <code>&#8211;device-open-proxy</code></p>
<dd> Request to use the &#8216;qmi-proxy&#8217; proxy</p>
<dt><code>&#8211;device-open-mbim</code></p>
<dd> Open an MBIM device with EXT_QMUX support</p>
<dt><code>&#8211;device-open-net</code>=<i>,[net-802-3/</i>|net-raw-ip|net-qos-header|net-no-qos-header]</p>
<dd> Open device with specific link protocol and QoS flags</p>
<dt><code>&#8211;client-cid</code>=<i>,[CID]/</i></p>
<dd> Use the given CID, don&#8217;t allocate a new one</p>
<dt><code>&#8211;client-no-release-cid</code></p>
<dd> Do not release the CID when exiting</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> Run action with verbose logs, including the debug ones</p>
<dt><code>&#8211;silent</code></p>
<dd> Run action with no logs; not even the error/warning ones</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> Print version</dl>
<p> qmicli 1.15.0 Copyright &#169; 2015 Aleksander Morgado License GPLv2+: GNU GPL version 2 or later &lt;<a rel="nofollow" href="http://gnu.org/licenses/gpl-2.0.html">http://gnu.org/licenses/gpl-2.0.html</a>&gt; This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>qmicli</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>qmicli</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
<dd> <code>info qmicli</code></dl>
<p> should give you access to the complete manual. </p>
<h2>Index</h2>
