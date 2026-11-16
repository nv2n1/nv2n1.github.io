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
<dt>&#8211;help</dt>
<dd> Produces full help text. </dd>
<dt>-h <i>hfi</i></dt>
<dd> HFI, numbered 1..n. Default = 0 which specifies the first HFI that has the first active port. </dd>
<dt>-p <i>port</i></dt>
<dd> Port, numbered 1..n. Using 0 specifies the first active port across all HFIs/ports. Default = 1 which indicates all ports. If selected, the tool returns information on all available ports if p is not defined. </dd>
<dt>-o <i>type</i></dt>
<dd> Output type specified and can appear more than once. </dd>
</dl>
<p> <code>NOTE:</code> Behavior without -o gives a brief summary of portinfo, counters and cableinfo. </p>
<dl>
<dl>
<dt>
</dt><dd>
<p> info Outputs detailed portinfo.</dd></dl>
</dl>
<dl>
<dl>
<dt>
</dt><dd>
<p> stats Outputs detailed port counters.</dd></dl>
</dl>
<dl>
<dt>-g</dt>
<dd> Output is displayed in line-by-line format. Default = summary format. </dd>
<dt>-d <i>detail</i></dt>
<dd> Output detail level. Range = 0 &#8211; 4. CableInfo only. Default = 0. </dd>
</dl>
<p> <code>NOTE:</code> -d option is ignored when used with -o type. </p>
<dl>
<dl>
<dt>
</dt><dd>
<p> 0 Minimal crucial information (for example, cable length, vendor) </p>
</dd></dl>
</dl>
<dl>
<dl>
<dt>
</dt><dd>
<p> 1 Brief summary </p>
</dd></dl>
</dl>
<dl>
<dl>
<dt>
</dt><dd>
<p> 2 Extended brief summary </p>
</dd></dl>
</dl>
<dl>
<dl>
<dt>
</dt><dd>
<p> 3 Verbose output </p>
</dd></dl>
</dl>
<dl>
<dl>
<dt>
</dt><dd>
<p> 4 Verbose and debug output. Lists all settings both statically and dynamically configured in the cable. </p>
</dd></dl>
</dl>
<dl>
<dt><code>-h and -p options permit a variety of selections:</code></dt>
<dd>
</dd><dt>-h 0</dt>
<dd> All ports on all HFIs (default). </dd>
<dt>-h 0 -p 0</dt>
<dd> First active port in system. </dd>
<dt>-h <i>x</i></dt>
<dd> All active ports on HFI <i>x</i>. </dd>
<dt>-h <i>x</i>#8217#160;-p 0</dt>
<dd> First active port on HFI <i>x</i>. </dd>
<dt>-h 0 -p <i>y</i></dt>
<dd> Port <i>y</i>#8217#160;within system (no matter which ports are active). </dd>
<dt>-h <i>x</i>#8217#160;-p <i>y</i></dt>
<dd> HFI <i>x</i>, port <i>y</i> </dd>
<dt><code>Debug Options</code></dt>
<dd>
</dd><dt>-v</dt>
<dd> Verbose output. Additional invocations (#8217#8211;v -v &#8230;) turn on debugging, openib debugging, and libibumad debugging. </dd>
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
