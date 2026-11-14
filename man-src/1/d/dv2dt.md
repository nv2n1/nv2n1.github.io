---
title: "dv2dt(1)"
name: "dv2dt"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dv2dt/"
description: "dv2dt – convert a binary TeX DVI file to DTL text representation"
---

<h2 class="name">NAME</h2>
<p> dv2dt &#8211; convert a binary TeX DVI file to DTL text representation </p>
<h2>SYNOPSIS</h2>
<p> <code>dv2dt</code> <i>input-DVI-file</i> <i>output-DTL-file</i> </p>
<p> If the filenames are omitted, then <i>stdin</i> and <i>stdout</i> are assumed.</p>
<h2>DESCRIPTION</h2>
<p> <code>dv2dt</code> converts a binary TeX DVI file to an editable text file in DTL (<i>DVI Text Language</i>) format. The companion <code><a href="/docs/linux/man/1-dt2dv/">dt2dv</a></code>(1) utility can convert the DTL file back to a binary DVI file.</p>
<h2>DVI COMMAND DESCRIPTION</h2>
<p> TeX DVI files contain a compact binary description of typeset pages, as a stream of operation code bytes, each immediately followed by zero or more parameter bytes. The format of DVI files is fully described in Donald E. Knuth, <i>TeX: The Program</i>, Addison-Wesley (1986), ISBN 0-201-13437-3, as well as in the <code><a href="/docs/linux/man/1-dvitype/">dvitype</a></code>(1) literate program source code. </p>
<p> For convenience, we provide a summary of DVI commands here. In the following list, operation code bytes are given as unsigned decimal values, followed by their symbolic names (not present in the DVI file), and a short description. A designation like <i>b[+n]</i> means that the operation code byte is followed by a parameter <i>b</i> which uses <i>n</i> bytes, and is signed. Without the plus sign, the parameter is unsigned. Signed integer parameter values are always represented in two&#8217;s complement arithmetic, which is the system followed by most computers manufactured today, including all personal computers and workstations.</p>
<dl>
<dt>
<dd> <i>0 set_char_0</i> Set character 0 from current font.</p>
<dt><i>&#8230;</i></p>
<dd>
<dt><i>127 set_char_127</i></p>
<dd> Set character 127 from current font.</p>
<dt><i>128 set1 c[1]</i></p>
<dd> Set 1-byte unsigned character (uchar) number <i>c</i>.</p>
<dt><i>129 set2 c[2]</i></p>
<dd> Set 2-byte uchar number <i>c</i>.</p>
<dt><i>130 set3 c[3]</i></p>
<dd> Set 3-byte uchar number <i>c</i>.</p>
<dt><i>131 set4 c[+4]</i></p>
<dd> Set 4-byte signed character (schar) number <i>c</i>.</p>
<dt><i>132 set_rule a[+4] b[+4]</i></p>
<dd> Set rule, height <i>a</i>, width <i>b</i>.</p>
<dt><i>133 put1 c[1]</i></p>
<dd> Put 1-byte uchar <i>c</i>.</p>
<dt><i>134 put2 c[2]</i></p>
<dd> Put 2-byte uchar <i>c</i>.</p>
<dt><i>135 put3 c[3]</i></p>
<dd> Put 3-byte uchar <i>c</i>.</p>
<dt><i>136 put4 c[+4]</i></p>
<dd> Put 4-byte schar <i>c</i>.</p>
<dt><i>137 put_rule a[+4] b[+4]</i></p>
<dd> Put rule, height <i>a</i>, width <i>b</i>.</p>
<dt><i>138 nop</i></p>
<dd> Do nothing.</p>
<dt><i>139 bop c0[+4] &#8230; c9[+4] p[+4]</i></p>
<dd> Beginning of page. The parameters <i>c0 &#8230; c9</i> are the TeX page counters, the contents of TeX count registers <i>
