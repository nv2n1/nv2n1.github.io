---
title: "opatmmtool(1)"
name: "opatmmtool"
section: "1"
letter: "o"
url: "/docs/linux/man/1-opatmmtool/"
description: "opatmmtool"
---

<h2>NAME</h2>
<p> opatmmtool </p>
<p> <code>(Host)</code> Manages and updates the firmware on the Thermal Management Microchip (TMM).</p>
<h2>Syntax</h2>
<p> opatmmtool [-v] [-h <i>hfi</i>] [-f <i>file</i>] <i>operation</i></p>
<h2>Options</h2>
<dl>
<dt>&#8211;h</dt>
<dd> Produces full help text. </dd>
<dt>-v</dt>
<dd> Produces verbose output. </dd>
<dt>-h <i>hfi</i></dt>
<dd> HFI, numbered 1..n. Default = 1. </dd>
<dt>-f <i>file</i></dt>
<dd> File parameter for <i>fileversion</i>, <i>update</i>, and <i>dumpotp</i> operations. </dd>
<dt>
&nbsp;<wbr><i>operation</i>&nbsp;<wbr></dt>
<dd> Includes one of the following: </dd>
<dl>
<dl>
<dt>
</dt><dd>
<p> reboot Reboots the TMM.</dd></dl>
</dl>
<dl>
<dl>
<dt>
</dt><dd>
<p> fwversion Reports the current firmware version.</dd></dl>
</dl>
<dl>
<dl>
<dt>
</dt><dd>
<p> fileversion Reports the file version. Requires -f <i>fw_file</i> option.</dd></dl>
</dl>
<dl>
<dl>
<dt>
</dt><dd>
<p> update Performs a firmware update. Requires -f <i>fw_file</i> option.</dd></dl>
</dl>
<dl>
<dl>
<dt>
</dt><dd>
<p> dumpotp Dumps the one-time programmable (OTP) region. Requires -f <i>output_file</i> option.</dd></dl>
</dl>
<dl>
<dl>
<dt>
</dt><dd>
<p> lockotp Locks the one-time programmable (OTP) region.</dd></dl>
</dl>
<dl>
<dl>
<dt>
</dt><dd>
<p> status Displays the current GPIO pin status.</dd></dl>
</dl>
</dl>
<h2>Examples</h2>
<p> opatmmtool -h 1 fwversion<br />
 opatmmtool -v -f main.signed.bin update<br />
 opatmmtool reboot </p>
<h2>Index</h2>
</p>