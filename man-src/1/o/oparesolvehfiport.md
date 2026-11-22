---

title: "oparesolvehfiport(1)"
name: "oparesolvehfiport"
section: "1"
letter: "o"
url: "/docs/linux/man/1-oparesolvehfiport/"
description: "oparesolvehfiport"
---

<p> oparesolvehfiport </p>
<p> <code>(Host)</code> Permits the Intel(R) Omni-Path Fabric Host Software style Intel(R) Omni-Path Host Fabric Interface (HFI) number and port number arguments to be converted to a Host Software style HFI name and physical port number.</p>
<h2>Syntax</h2>
<p> oparesolvehfiport <i>hfi</i> <i>port</i></p>
<h2>Options</h2>
<dl>
<dt>&#8211;help</dt>
<dd> Produces full help text. </dd>
<dt>
&nbsp;<wbr><i>hfi</i>&nbsp;<wbr></dt>
<dd> HFI to send by. Numbered 1..n. 0 = system-wide port num. Default is first HFI. </dd>
<dt>
&nbsp;<wbr><i>port</i>&nbsp;<wbr></dt>
<dd> Port to send by. Numbered 1..n. 0 (default) is first active port. </dd>
<dt><code>-h and -p options permit a variety of selections:</code></dt>
<dd>
</dd><dt>-h 0 -p 0</dt>
<dd> First active port in system. </dd>
<dt>-h <i>x</i>#8217#160;-p 0</dt>
<dd> First active port on HFI <i>x</i>. </dd>
<dt>-h 0 -p <i>y</i></dt>
<dd> Port <i>y</i>#8217#160;within system (no matter which ports are active). </dd>
<dt>-h <i>x</i>#8217#160;-p <i>y</i></dt>
<dd> HFI <i>x</i>, port <i>y</i> </dd>
</dl>
<h2>Examples</h2>
<p> oparesolvehfiport 0 1<br/>
 Output:<br/>
 #8217#160; hfi_0:1 </p>
