---
title: "hivexget(1)"
name: "hivexget"
section: "1"
letter: "h"
url: "/docs/linux/man/1-hivexget/"
---

<h2 class="name">NAME</h2>
 

 hivexget - Get subkey from a Windows Registry binary &quot;hive&quot; file 

<h2>SYNOPSIS</h2>

 <pre>
 hivexget hivefile '\Path\To\SubKey'
 hivexget hivefile '\Path\To\SubKey' name
</pre>

<h2>NOTE</h2>

 This is a low-level tool. For a more convenient way to navigate the Windows Registry in Windows virtual machines, see <i><a HREF="/docs/linux/man/1-virt-win-reg/">virt-win-reg</a></i>(1). For proper regedit formatting, use <i><a HREF="/docs/linux/man/1-hivexregedit/">hivexregedit</a></i>(1).

<h2>DESCRIPTION</h2>

 This program navigates through a Windows Registry binary ``hive'' file and extracts <i>either</i> all the (key, value) data pairs stored in that subkey <i>or</i> just the single named data item. 

 In the first form: 

 <pre>
 hivexget hivefile '\Path\To\SubKey'
</pre> 

 <tt>&quot;hivefile&quot;</tt> is some Windows Registry binary hive, and <tt>&quot;\Path\To\Subkey&quot;</tt> is a path within that hive. <i></i><font SIZE="-1"><i>NB</i></font><i></i> the path is relative to the top of this hive, and is <i>not</i> the full path as you would use in Windows (eg. <tt>&quot;HKEY_LOCAL_MACHINE\SYSTEM&quot;</tt> is not a valid path). 

 If the subkey exists, then the output lists all data pairs under this subkey, in a format similar to <tt>&quot;regedit&quot;</tt> in Windows. 

 In the second form: 

 <pre>
 hivexget hivefile '\Path\To\SubKey' name
</pre> 

 <tt>&quot;hivefile&quot;</tt> and path are as above. <tt>&quot;name&quot;</tt> is the name of the value of interest (use <tt>&quot;@&quot;</tt> for the default value). 

 The corresponding data item is printed ``raw'' (ie. no processing or escaping) except:
<dl>
<dt>1.
<dd> If it's a string we will convert it from Windows <font SIZE="-1">UTF-16</font> to <font SIZE="-1">UTF-8,</font> if this conversion is possible. The string is printed with a single trailing newline.
<dt>2.
<dd> If it's a multiple-string value, each string is printed on a separate line.
<dt>3.
<dd> If it's a numeric value, it is printed as a decimal number.</dl>

<h2>SEE ALSO</h2>

 <i><a HREF="/docs/linux/man/3-hivex/">hivex</a></i>(3), <i><a HREF="/docs/linux/man/1-hivexml/">hivexml</a></i>(1), <i><a HREF="/docs/linux/man/1-hivexsh/">hivexsh</a></i>(1), <i><a HREF="/docs/linux/man/1-hivexregedit/">hivexregedit</a></i>(1), <i><a HREF="/docs/linux/man/1-virt-win-reg/">virt-win-reg</a></i>(1), <i><a HREF="/docs/linux/man/3-guestfs/">guestfs</a></i>(3), &lt;<a rel="nofollow" HREF="http://libguestfs.org/">http://libguestfs.org/</a>&gt;, <i><a HREF="/docs/linux/man/1-virt-cat/">virt-cat</a></i>(1), <i><a HREF="/docs/linux/man/1-virt-edit/">virt-edit</a></i>(1).

<h2>AUTHORS</h2>

 Richard W.M. Jones (<tt>&quot;rjones at redhat dot com&quot;</tt>)

<h2>COPYRIGHT</h2>

 Copyright (C) 2009 Red Hat Inc. 

 This program is free software; you can redistribute it and/or modify it under the terms of the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. 

 This program is distributed in the hope that it will be useful, but <font SIZE="-1">WITHOUT ANY WARRANTY</font>; without even the implied warranty of <font SIZE="-1">MERCHANTABILITY</font> or <font SIZE="-1">FITNESS FOR A PARTICULAR PURPOSE. </font> See the <font SIZE="-1">GNU</font> General Public License for more details. 

 You should have received a copy of the <font SIZE="-1">GNU</font> General Public License along with this program; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, <font SIZE="-1">MA 02110-1301 USA.</font> 

<h2>Index</h2>


