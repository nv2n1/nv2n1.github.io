---

title: "intel_reg_write(1)"
name: "intel_reg_write"
section: "1"
letter: "i"
url: "/docs/linux/man/1-intel_reg_write/"
description: "intel_reg_write – Set an Intel GPU register to a value"
---

<h2>NAME</h2>
<p> intel_reg_write &#8211; Set an Intel GPU register to a value</p>
<p> <code>intel_reg_write </code><i>register</i> <i>value</i></p>
<p> <code>intel_reg_write</code> is a tool to set Intel GPU registers to values, for use in speeding up debugging. The <i>register</i> and <i>value</i> arguments are given as hexadecimal.</p>
<h2>EXAMPLES</h2>
<dl>
<dt>intel_reg_write 0x61230 0x0</dt>
<dd> Disables the first internal panel fitter. </dd>
</dl>
