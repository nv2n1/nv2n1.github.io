---
title: "wflinfo(1)"
name: "wflinfo"
section: "1"
letter: "w"
url: "/docs/linux/man/1-wflinfo/"
description: "wflinfo – a utility for printing OpenGL or OpenGL ES driver information"
---

<h2 class="name">NAME</h2>
<p> wflinfo &#8211; a utility for printing OpenGL or OpenGL ES driver information </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>wflinfo</code> <code>&#8211;platform=</code><i>platform</i> <code>&#8211;api=</code><i>api</i> [<i>OPTIONS</i>]</dl>
<h2>DESCRIPTION</h2>
<dd>wflinfo is utility which creates an OpenGL or OpenGL ES context using the waffle library and prints information about the context.</p>
<h2>REQUIRED PARAMETERS</h2>
<p> <code>-p</code> <i>platform</i><br />
 <code>&#8211;platform=</code><i>platform</i></p>
<dl>
<dt>
<dd> Where <i>platform</i> is android, cgl, gbm, glx, wayland, wgl, or x11_egl</dl>
<p> <code>-a</code> <i>api</i><br />
 <code>&#8211;api=</code><i>api</i></p>
<dl>
<dt>
<dd> Where <i>api</i> is gl, gles1, gles2, or gles3</dl>
<h2>OPTIONS</h2>
<p> <code>-V</code> <i>MAJOR.MINOR</i><br />
 <code>&#8211;version=</code><i>MAJOR.MINOR</i></p>
<dl>
<dt>
<dd> For example &#8211;api=gl &#8211;version=3.2 would request OpenGL 3.2</dl>
<p> <code>&#8211;profile=</code><i>profile</i></p>
<dl>
<dt>
<dd> Where <i>profile</i> is core, compat or none</dl>
<p> <code>-v</code><br />
 <code>&#8211;verbose</code></p>
<dl>
<dt>
<dd> Print more information</dl>
<p> <code>&#8211;forward-compatible</code></p>
<dl>
<dt>
<dd> Request a forward compatible context be created</dl>
<p> <code>&#8211;debug-context</code></p>
<dl>
<dt>
<dd> Request a debug context be created</dl>
<p> <code>-h</code><br />
 <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Print wflinfo usage information</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>
<dd> wflinfo &#8211;platform=glx &#8211;api=gl</dl>
<dl>
<dt>
<dd> wflinfo &#8211;platform=x11_egl &#8211;api=gl &#8211;version=3.2 &#8211;profile=core</dl>
<dl>
<dt>
<dd> wflinfo &#8211;platform=wayland &#8211;api=gles3</dl>
<dl>
<dt>
<dd> wflinfo &#8211;platform=gbm &#8211;api=gl &#8211;version=3.2 &#8211;verbose</dl>
<dl>
<dt>
<dd> wflinfo -p gbm -a gl -V 3.2 -v</dl>
<h2>ISSUES</h2>
<p> Please report bugs or and feature requests to m[blue]<code><a rel="nofollow" href="https://github.com/waffle-gl/waffle/issues">https://github.com/waffle-gl/waffle/issues</a></code>m[].</p>
<h2>SEE ALSO</h2>
<dl>
<dt>
<dd> <code><a href="/docs/linux/man/7-waffle/">waffle</a></code>(7)</dl>
<h2>AUTHORS</h2>
<p> <code>Chad Versace</code> &lt;chad.versace [at] linux.intel.com&gt;</p>
<dl>
<dt>
<dd> Maintainer</dl>
<p> <code>Jordan Justen</code> &lt;jordan.l.justen [at] intel.com&gt;</p>
<dl>
<dt>
<dd> Contributor</dl>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2013 Intel </p>
<p> This manual page is licensed under the Creative Commons Attribution-ShareAlike 3.0 United States License (CC BY-SA 3.0). To view a copy of this license, visit m[blue]<code><a rel="nofollow" href="http://creativecommons.org.license/by-sa/3.0/us">http://creativecommons.org.license/by-sa/3.0/us</a></code>m[]. </p>
<h2>Index</h2>
