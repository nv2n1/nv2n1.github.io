---
title: "xvattr(1)"
name: "xvattr"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xvattr/"
description: "xvattr – Query/Set X11 XVideo Setting(s)"
---

<h2 class="name">NAME</h2>
<p> xvattr &#8211; Query/Set X11 XVideo Setting(s) </p>
<h2>SYNOPSIS</h2>
<p> <code>xvattr</code> [<i>options</i>&#8230;] </p>
<p> This program is used for getting and setting X11 Xv attributes such as <font SIZE="-1">XV_BRIGHTNESS, XV_CONTRAST, XV_SATURATION, XV_HUE, XV_COLORKEY, &#8230;</font> </p>
<p> For this program to work, you must have a version of X11 with the XVideo extension and a graphics card that has Xv graphics acceleration. </p>
<p> Note: On some cards <font SIZE="-1">XV_BRIGHTNESS</font> and <font SIZE="-1">XV_CONTRAST</font> are not listed among the available attributes, but they can still be set/changed.</p>
<h3><font SIZE="-1">OPTIONS</font></h3>
<p> With no options, all parameters are displayed. </p>
<p> Long options are handled by <font SIZE="-1">GNU</font> getopts and follow those rules. In particular, options that are specified with a double dash (&#8211;) rather than a single dash (-), can be abbreviated as long as they are unique. Long parameters that need a value specified may have the parameter and the value separated with blank space or an optional equals sign (and no intervening space). </p>
<p> For example the following are all equivalent: </p>
<p> xvattr -a <font SIZE="-1">XV_BRIGHTNESS</font> xvattr &#8211;attribute <font SIZE="-1">XV_BRIGHTNESS</font> xvattr &#8211;att <font SIZE="-1">XV_BRIGHTNESS</font> xvattr &#8211;att=XV_BRIGHTNESS </p>
<p> Example: </p>
<pre>
  &gt; xvattr
  Adaptor: 0
  Name: Matrox G-Series Backend Scaler
   Port: 46
    Name: XV_COLORKEY
     Flags: XvGettable XvSettable 
     Min value: 0
     Max value: 16777215
     Current value: 66046
</pre>
<dl>
<dt>{-a | &#8211;attribute} <i>attribute name</i></p>
<dd> Show value of attribute <i>attribute name</i> </p>
<p> Example: </p>
<pre>
  &gt; xvattr -a XV_BRIGHTNESS
  XV_BRIGHTNESS = 24
</pre>
<dt>{-a | &#8211;attribute} <i>attribute name</i> [-v | &#8211;value] <i>value</i></p>
<dd> Set attribute <i>attribute name</i> to value <i>value</i>. </p>
<p> Example: </p>
<pre>
  &gt; xvattr -a XV_COLORKEY -v 10
  XV_COLORKEY set to 10
</pre>
<dt>{-p | &#8211;port} <i>port number</i></p>
<dd> Get the attribute on the specified port. If -p is not set, the first available port is used. </p>
<p> Example: </p>
<pre>
  &gt; xvattr -p 66
  Found Xv 2.2
  Adaptor: 0
  Name: SIS Video Overlay
   Port: 66
    Name: XV_COLORKEY
     Flags: XvGettable XvSettable 
     Min value: 0
     Max value: 16777215
     Current value: 66046
    Name: XV_BRIGHTNESS
     Flags: XvGettable XvSettable 
     Min value: -128
     Max value: 127
     Current value: 0
    Name: XV_CONTRAST
     Flags: XvGettable XvSettable 
     Min value: 0
     Max value: 255
     Current value: 128
</pre>
</dl>
<h2>AUTHOR</h2>
<p> Bjo.rn Englund. Send bug reports to <tt>&quot;d4bjorn [at] dtek.chalmers.se&quot;</tt> <tt>&quot;rocky [at] panix.com&quot;</tt> turned the <font SIZE="-1">README</font> into this document.</p>
<h2>SEE ALSO</h2>
<p> See also xvinfo and XvQueryAdaptors, XvSetPortAttribute, and XvGetPortAttribute.</p>
<h2>COPYRIGHT</h2>
<pre><code>
Copyright(C) 2001 - 2002 Bjo.rn Englund
                    This program is free software;
you can redistribute it and / or modify
                                     it under the terms of the GNU General Public License as published by
                                         the Free Software Foundation;
either version 2 of the License, or
                                     (at your option) any later version.This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License for more details.
  You should have received a copy of the GNU General Public License
  along with this program;
if
not, write to the Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111 - 1307 USA
</code></pre>
<h2>Index</h2>
<dt><a href="#lbAE">AUTHOR</a></p>
<dd>
<dt><a href="#lbAF">SEE ALSO</a></p>
<dd>
<dt><a href="#lbAG">COPYRIGHT</a></p>
<dd></dl>
