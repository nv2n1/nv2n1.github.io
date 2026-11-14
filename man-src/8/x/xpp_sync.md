---
title: "xpp_sync(8)"
name: "xpp_sync"
section: "8"
letter: "x"
url: "/docs/linux/man/8-xpp_sync/"
---

xpp_sync - Handle sync selection of Xorcom Astribanks.

<h2>Synopsis</h2>

xpp_sync [auto|dahdi|nn]

<h2>Description</h2>

On a normal operation one Astribank device provides timing for all the other Astribank devices. 

 When run without parameters, xpp_sync will display a list of Astribanks (xbuses) that are connected and registered as Dahdi spans. The current xpp sync master will be marked. 

 If you this an Astribank is connected and yet it does not appear on the output of xpp_sync, it may be unregistered. Try running dahdi_registration .

<h2>Parameters</h2>

<dl><dt>auto
<dd>Automatically selects the best Astribank for syncing.
<dt>dahdi
<dd>Gets synchronization from the Dahdi sync master.
<dt>nn
<dd>Sets <font SIZE="-1">XBUS-</font><i>nn</i> as sync source.</dl>
 

 (Parameter name is case-insensitive)

<h2>Example output:</h2>

<pre> Setting SYNC
 Current sync: 01
 Best Available Syncers:
 + XBUS-01 (usb-0000:00:10.4-3) [usb:12345678] [ PRI_TE PRI_NT PRI_TE PRI_NT ]
 XBUS-00 (usb-0000:00:10.4-2) [usb:QA-01] [ FXS FXO ]
 ==================================================
 WARNING: FXO which is not the syncer cause bad PCM
 Affected Astribanks are:
 --------------------------------------------------
 XBUS-00
 ==================================================</pre>In this example we see that the recommended xpp sync master is <font SIZE="-1">XBUS-02</font> - it is the first on the list. It is also the actual syncer, as we can see from the '+' beside it. 

 xpp_sync is normally called from the dahdi init.d script. The parameter it is called with defaults to <i>auto</i>, but it is possible to override that parameter (e.g: set it to <i>dahdi</i>) through the value of <font SIZE="-1">XPP_SYNC</font> in /etc/dahdi/init.conf .

<h2>Files</h2>

<dl><dt>/proc/xpp/sync
<dd>xpp_sync is essentially a nicer interface to /proc/xpp/sync . That file shows the current xpp sync master (and in what format you need to write to it to set the master). 

</dl>
