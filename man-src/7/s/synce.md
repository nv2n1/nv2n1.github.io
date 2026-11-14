---
title: "synce(7)"
name: "synce"
section: "7"
letter: "s"
url: "/docs/linux/man/7-synce/"
---

SynCE - A project for connecting to devices running Microsoft Windows Mobile. 

<h2>Description</h2>

The SynCE project aims to provide libraries and tools to connect to and synchronise with PDA's and other devices running Microsoft Windows Mobile, or Windows CE. 

 The main components include :-

<h3>libsynce</h3>

Core library that provides various support services and functions.

<h3>librapi2</h3>

Core library implementing the RAPI protocol, equivalent to rapi.dll on a Windows OS. RAPI is used for most kinds of interaction with a WM device. 

 This library actually implements two versions of the protocol. RAPI 1 is used for devices up to and including CE 5.0, with RAPI 2 coming into use from 5.1 (WM5).

<h3>librra</h3>

Library implementing RRA (Remote Replication Agent), a protocol used for synchronisation. This protocol is used for all data synchronisation until WM5, at which point Airsync is used for the majority. RRA is still used for file synchronisation however.

<h3>dccm</h3>

The dccm daemon negotiates the initial connection with a WM device, and may provide keep-alive signals and client connections, depending on the device version and flavour of dccm. 

 There have been a number of dccm 'flavours'. The original, also known as synce-dccm, is now considered obsolete and should not be used. Vdccm is a natural progression of dccm which is not greatly used anymore. Odccm is the most common in use at the moment, and uses dbus to provide connections to both legacy and modern devices. Hal-dccm is a new option that integrates the dccm functionality into hal to provide a more platform consistent interface. 

 

 The following steps are required to get started with SynCE:

<h3>(1) Ensure the rndis kernel module or a serial connection mechanism is installed</h3>

To use advanced network features (rndis) with a WM5 or later device, which is recommended, you must use the usb-rndis-[lite|ng] driver from SynCE. For older devices or to use serial with WM5, if synce-hal is not used you will require the synce-serial package. You will of course also need a dccm daemon, synce-hal or odccm is recommended.

<h3>(2) Start the connection daemon (as root)</h3>

If using odccm, this daemon must run as the root user. With synce-hal, dccm will be started as required. Older dccm implementations must be run as your user.

<h3>(3) Run tools that access the device (as user)</h3>

See for example <a HREF="/docs/linux/man/1-pls/">pls</a>(1) and <a HREF="/docs/linux/man/1-pcp/">pcp</a>(1). 

 

 See <a rel="nofollow" HREF="http://www.synce.org/">http://www.synce.org/</a> for more information about the SynCE project.

<h2>Author</h2>

This manual page was written by David Eriksson &lt;twogood [at] users.sourceforge.net&gt;. It was later updated by Jonny Lamb &lt;jonnylamb [at] jonnylamb.com&gt; and Mark Ellis &lt;mark [at] mpellis.org.uk&gt;.

<h2>See Also</h2>

<a HREF="/docs/linux/man/1-odccm/">odccm</a>(1) 
