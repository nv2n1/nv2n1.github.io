---
title: "opaportconfig(1)"
name: "opaportconfig"
section: "1"
letter: "o"
url: "/docs/linux/man/1-opaportconfig/"
description: "opaportconfig"
---

<h2>NAME</h2>
<p> opaportconfig </p>
<p> <code>(Host or Switch)</code> Controls the configuration and state of a specified Intel(R) Omni-Path Host Fabric Interface (HFI) port on the local host or a remote switch.</p>
<h2>Syntax</h2>
<p> opaportconfig [-l <i>lid</i>[-m <i>dest_port</i>]] [-h <i>hfi</i>] [-p <i>port</i>] [-r <i>secs</i>] [-z]<br />
 [-S <i>state</i>] [-P <i>physstate</i>] [-s <i>speed</i>] [-w <i>width</i>] [-c <i>LTPCRC</i>] [-K <i>mkey</i>]<br />
 [-v] [-x] [-L <i>lid</i>] [#8217lt; <i>sub command</i>&gt;]</p>
<h2>Options</h2>
<dl>
<dt>-l <i>lid</i></p>
<dd> Destination LID. Default is local port. </p>
<dt>-m <i>dest_port</i></p>
<dd> Destination port. Default is port with given LID. Used to access switch ports. </p>
<dt>-h <i>hfi</i></p>
<dd> HFI to send through/to. Default is first HFI. </p>
<dt>-p <i>port</i></p>
<dd> Port to send through/to. Default is first port. </p>
<dt>-K <i>mkey</i></p>
<dd> SM management key to access remote ports. </p>
<dt>
&nbsp;<wbr><i>sub command</i>&nbsp;<wbr></p>
<dd> One of the following choices: </p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<p> enable Enables port. </p>
</dl>
</dl>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<p> disable Disables port. </p>
</dl>
</dl>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<p> bounce Bounces port. </p>
<dt>
<dd>
</dl>
<p> <code>NOTE:</code> Bouncing remote ports may cause timeouts. </p>
</dl>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<p> ledon Turns port LED on. </p>
</dl>
</dl>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<p> ledoff Turns port LED off. </p>
</dl>
</dl>
</dl>
<h2>Configuration Options</h2>
<dl>
<dt>-r <i>secs</i></p>
<dd> Repeats to keep the port down for the specified amount of seconds. </p>
<dt>-S <i>state</i></p>
<dd> New state. Default is 0. </p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<p> 0 No-op. </p>
</dl>
</dl>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<p> 1 Down. </p>
</dl>
</dl>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<p> 2 Initiate. </p>
</dl>
</dl>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<p> 3 Armed. </p>
</dl>
</dl>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<p> 4 Active. </p>
</dl>
</dl>
<dt>-P <i>physstate</i></p>
<dd> New physical state. Default is 0. </p>
<dt>
<dd>
</dl>
<p> <code>NOTE:</code> All transitions are valid. </p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<p> 0 No-op. </p>
</dl>
</dl>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<p> 2 Polling. </p>
</dl>
</dl>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<p> 3 Disabled. </p>
</dl>
</dl>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<p> 11 Phy-Test. Current physstate must be disabled. </p>
</dl>
</dl>
<dl>
<dt>-s <i>speed</i></p>
<dd> New link speeds enabled. Default is 0. To enable multiple speeds, use the sum of the desired speeds. </p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<p> 0 No-op. </p>
</dl>
</dl>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<p> 2 0x0002 &#8211; 25 Gb/s. </p>
</dl>
</dl>
<dt>-w <i>width</i></p>
<dd> New link widths enabled. Default is 0. To enable multiple widths, use sum of desired widths. </p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<p> 0 No-op. </p>
</dl>
</dl>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<p> 1 0x01 &#8211; 1x. </p>
</dl>
</dl>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<p> 2 0x02 &#8211; 2x. </p>
</dl>
</dl>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<p> 4 0x04 &#8211; 3x. </p>
</dl>
</dl>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<p> 8 0x08 &#8211; 4x. </p>
</dl>
</dl>
<dt>-c <i>LTPCRC</i></p>
<dd> New LTP CRCs enabled. Default is 0. To enable multiple LTP CRCs, use sum of desired LTP CRCs. </p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<p> 0 No-op. </p>
</dl>
</dl>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<p> 1 0x1 &#8211; 14-bit LTP CRC mode. </p>
</dl>
</dl>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<p> 2 0x2 &#8211; 16-bit LTP CRC mode. </p>
</dl>
</dl>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<p> 4 0x4 &#8211; 48-bit LTP CRC mode.</dl>
</dl>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<p> 8 0x8 &#8211; 12/16 bits per lane LTP CRC mode. </p>
</dl>
</dl>
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
<dd> Verbose output. Additional invocations turn on debugging, openib debugging, and libibumad debugging. </p>
<dt>-z</p>
<dd> Does not get port info first, clears most port attributes. </p>
<dt>-L <i>lid</i></p>
<dd> Sets PortInfo.LID = lid. </p>
</dl>
<h2>Examples</h2>
<p> opaportconfig -w 1<br />
 opaportconfig -p 1 -h 2 -w 3</p>
<h2>Description</h2>
<p> Port configuration is transient in nature. If the given host is rebooted or its Intel(R) Omni-Path Fabric Stack is restarted, the port reverts to its default configuration and state. Typically, the default state is to have the port enabled with all speeds and widths supported by the given HFI port. </p>
<p> To access switch ports using this command, the -l and -m options must be given. The -l option specifies the lid of switch port 0 (the logical management port for the switch) and -m specifies the actual switch port to access. If SMA mkeys are used, the -K option is also needed. However, the Intel(R) Omni-Path Fabric Suite Fabric Manager does not use SMA mkeys by default, therefore this option may not be required. </p>
<p> <code>NOTE:</code> The /etc/init.d/opaportconfig script is provided as an example of changing port speed every time the server boots. This script can be edited, then scheduled, using chkconfig to control link settings on any set of HFI ports. </p>
<p> <code>CAUTION:</code> When using this command to disable or reconfigure switch ports, if the final port in the path between the Fabric Management Node and the switch is disabled or fails to come online, then opaenableports is not able to reenable it. In this case, the switch CLI and/or a switch reboot may be needed to correct the situation. </p>
<h2>Index</h2>
