---
title: "sfcbinst2mof(1)"
name: "sfcbinst2mof"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sfcbinst2mof/"
description: "sfcbinst2mof – Dump static instances to mof"
---

<h2>NAME</h2>
<p> sfcbinst2mof &#8211; Dump static instances to mof</p>
<h2>SYNOPSIS</h2>
<p> <code>sfcbinst2mof &lt;options&gt; [-n namespace] [-c classname]</code></p>
<h2>OPTIONS</h2>
<p> Allowed options are:</p>
<dl>
<dt><code>-h</code></p>
<dd> display this message</p>
<dt><code>-v</code></p>
<dd> verbose: print some extra processing information to stdout</p>
<dt><code>-V</code></p>
<dd> print version information</p>
<dt><code>-n</code> &lt;namespace&gt;</p>
<dd> [REQUIRED]</p>
<dt><code>-c</code> &lt;classname&gt;</p>
<dd> [REQUIRED] &#8211; actual class name instrumented &#8211; not a parent class</p>
<dt> <code>-g</code> &lt;sfcb cfg file&gt; (default=/etc/sfcb/sfcb.cfg)</p>
<dt><code>-o</code> &lt;output file&gt;</p>
<dd>
<dd>full path to output file. Path must exist, with write rights. (default = stdout)</p>
<dt><code>-t</code></p>
<dd> truncate output file before writing to it (default = append)</p>
<dt><code>-m</code></p>
<dd> output instances that were created in MOF, in addition to instances created interactively</p>
<dt><code>-M</code></p>
<dd> output ONLY instances that were created in MOF (don&#8217;t include instances created interactively)</p>
<dt> <code>-r</code> &lt;repository dir&gt; use alternate repository (override sfcb cfg file). (default = /var/lib/sfcb/registration/repository) </p>
</dl>
<h2>Index</h2>
