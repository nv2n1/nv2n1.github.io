---
title: "opaportinfo(1)"
name: "opaportinfo"
section: "1"
letter: "o"
url: "/docs/linux/man/1-opaportinfo/"
description: "opaportinfo"
---

<h2>NAME</h2>
<p> opaportinfo </p>
<p> <code>(Host or Switch)</code> Displays configuration and state of a specified Intel(R) Omni-Path Host Fabric Interface (HFI) port on the local host or a remote switch.</p>
<h2>Syntax</h2>
<p> opaportinfo [-l <i>lid</i>[-m <i>dest_port</i>]] [-h <i>hfi</i>] [-p <i>port</i>] [-K <i>mkey</i>] [-v]</p>
<h2>Options</h2>
<dl>
<dt>-l <i>lid</i></p>
<dd> Destination LID. Default is local port. </p>
<dt>-m <i>dest_port</i></p>
<dd> Destination port. Default is port with given LID. Useful to access switch ports. </p>
<dt>-h <i>hfi</i></p>
<dd> HFI to send through/to. Default is first HFI. </p>
<dt>-p <i>port</i></p>
<dd> Port to send through/to. Default is first port. </p>
<dt>-K <i>mkey</i></p>
<dd> SM management key to access remote ports. </p>
</dl>
<h2>-h and -p options permit a variety of selections:</h2>
<dl>
<dt>-h 0</p>
<dd> First port in system (default). </p>
<dt>-h <i>x</i></p>
<dd> First port on HFI <i>x</i>. </p>
<dt>-h 0 -p <i>y</i></p>
<dd> Port <i>y</i> within system. </p>
<dt>-h <i>x</i>#8217#160;-p <i>y</i></p>
<dd> HFI <i>x</i>, port <i>y</i>. </p>
</dl>
<h2>Debug Options</h2>
<dl>
<dt>-v</p>
<dd> Verbose output. Additional invocations (#8217#8211;v -v &#8230;) turn on debugging, openib debugging, and libibumad debugging. </p>
</dl>
<h2>Examples</h2>
<p> opaportinfo -p 1<br />
 opaportinfo -p 2 -h 2 -l 5 -m 18</p>
<h2>Description</h2>
<p> To access switch ports using this command, the -l and -m options must be given. The -l option specifies the LID of switch port 0 (the logical management port for the switch) and -m specifies the actual switch port to access. If SMA mkeys are used, the -K option is also needed. However, the Intel(R) Omni-Path Fabric Suite Fabric Manager does not use SMA mkeys by default, therefore this option may not be required. </p>
<h2>Index</h2>
