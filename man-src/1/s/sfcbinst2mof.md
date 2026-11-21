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
<p> <code>sfcbinst2mof &lt;options&gt; [-n namespace] [-c classname]</code></p>
<h2>OPTIONS</h2>
<p> Allowed options are:</p>
<dl>
<dt><code>-h</code></dt>
<dd> display this message</dd>
<dt><code>-v</code></dt>
<dd> verbose: print some extra processing information to stdout</dd>
<dt><code>-V</code></dt>
<dd> print version information</dd>
<dt><code>-n</code> &lt;namespace&gt;</dt>
<dd> [REQUIRED]</dd>
<dt><code>-c</code> &lt;classname&gt;</dt>
<dd> [REQUIRED] &#8211; actual class name instrumented &#8211; not a parent class</dd>
<dt> <code>-g</code> &lt;sfcb cfg file&gt; (default=/etc/sfcb/sfcb.cfg)</dt>
<dt><code>-o</code> &lt;output file&gt;</dt>
<dd>
</dd><dd>full path to output file. Path must exist, with write rights. (default = stdout)</dd>
<dt><code>-t</code></dt>
<dd> truncate output file before writing to it (default = append)</dd>
<dt><code>-m</code></dt>
<dd> output instances that were created in MOF, in addition to instances created interactively</dd>
<dt><code>-M</code></dt>
<dd> output ONLY instances that were created in MOF (don&#8217;t include instances created interactively)</dd>
<dt> <code>-r</code> &lt;repository dir&gt; use alternate repository (override sfcb cfg file). (default = /var/lib/sfcb/registration/repository) </dt>
</dl>
