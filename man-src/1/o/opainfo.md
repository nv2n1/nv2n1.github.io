---
title: "opainfo(1)"
name: "opainfo"
section: "1"
letter: "o"
url: "/docs/linux/man/1-opainfo/"
description: "opainfo"
---

<h2>NAME</h2>
<p> opainfo </p>
<p> Provides summary information for local HFI port(s).</p>
<h2>Syntax</h2>
<p> opainfo [-h <i>hfi</i>] [-p <i>port</i>] [-o <i>type</i>] [-g] [-d <i>detail</i>] [-v [-v]&#8230;] </p>
<h2>Options</h2>
<dl>
<dt>&#8211;help</p>
<dd> Produces full help text. </p>
<dt>-h <i>hfi</i></p>
<dd> HFI, numbered 1..n. Default = 0 which specifies the first HFI that has the first active port. </p>
<dt>-p <i>port</i></p>
<dd> Port, numbered 1..n. Using 0 specifies the first active port across all HFIs/ports. Default = 1 which indicates all ports. If selected, the tool returns information on all available ports if p is not defined. </p>
<dt>-o <i>type</i></p>
<dd> Output type specified and can appear more than once. </p>
<dt>
<dd>
</dl>
<p> <code>NOTE:</code> Behavior without -o gives a brief summary of portinfo, counters and cableinfo. </p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<p> info Outputs detailed portinfo.</dl>
</dl>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<p> stats Outputs detailed port counters.</dl>
</dl>
<dl>
<dt>-g</p>
<dd> Output is displayed in line-by-line format. Default = summary format. </p>
<dt>-d <i>detail</i></p>
<dd> Output detail level. Range = 0 &#8211; 4. CableInfo only. Default = 0. </p>
<dt>
<dd>
</dl>
<p> <code>NOTE:</code> -d option is ignored when used with -o type. </p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<p> 0 Minimal crucial information (for example, cable length, vendor) </p>
</dl>
</dl>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<p> 1 Brief summary </p>
</dl>
</dl>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<p> 2 Extended brief summary </p>
</dl>
</dl>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<p> 3 Verbose output </p>
</dl>
</dl>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<p> 4 Verbose and debug output. Lists all settings both statically and dynamically configured in the cable. </p>
</dl>
</dl>
<dl>
<dt><code>-h and -p options permit a variety of selections:</code></p>
<dd>
<dt>-h 0</p>
<dd> All ports on all HFIs (default). </p>
<dt>-h 0 -p 0</p>
<dd> First active port in system. </p>
<dt>-h <i>x</i></p>
<dd> All active ports on HFI <i>x</i>. </p>
<dt>-h <i>x</i>#8217#160;-p 0</p>
<dd> First active port on HFI <i>x</i>. </p>
<dt>-h 0 -p <i>y</i></p>
<dd> Port <i>y</i>#8217#160;within system (no matter which ports are active). </p>
<dt>-h <i>x</i>#8217#160;-p <i>y</i></p>
<dd> HFI <i>x</i>, port <i>y</i> </p>
<dt><code>Debug Options</code></p>
<dd>
<dt>-v</p>
<dd> Verbose output. Additional invocations (#8217#8211;v -v &#8230;) turn on debugging, openib debugging, and libibumad debugging. </p>
</dl>
<h2>Examples</h2>
<p> opainfo<br />
 hfi1_0:1 PortGID:0xfe80000000000000:001175010165b19c<br />
 PortState: Active<br />
 LinkSpeed Act: 25Gb En: 25Gb<br />
 LinkWidth Act: 4 En: 4<br />
 LinkWidthDnGrd ActTx: 4 Rx: 4 En: 3,4<br />
 LCRC Act: 14-bit En: 14-bit,16-bit,48-bit Mgmt: True<br />
 LID: 0x00000001-0x00000001 SM LID: 0x00000002 SL: 0<br />
 QSFP: PassiveCu, 1m FCI Electronics P/N 10131941-2010LF Rev 5<br />
 Xmit Data: 22581581 MB Pkts: 5100825193<br />
 Recv Data: 18725619 MB Pkts: 4024569756<br />
 Link Quality: 5 (Excellent) </p>
<h2>Index</h2>
