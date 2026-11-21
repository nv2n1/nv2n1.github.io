---

title: "i3-wsbar(1)"
name: "i3-wsbar"
section: "1"
letter: "i"
url: "/docs/linux/man/1-i3-wsbar/"
description: "i3-wsbar – sample implementation of a standalone workspace bar"
---

<p> i3-wsbar -c &lt;dzen2-commandline&gt; [options]</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;command</code> &lt;command&gt;</dt>
<dd> This command (at the moment only dzen2 is supported) will be started for each output. <tt>%x</tt> will be replaced with the X coordinate of the output. </dd>
<p> Example:<br />
&nbsp;<wbr>&#8211;command&nbsp;<wbr>&#8220;dzen2 -dock -x&nbsp;<wbr><tt>%x</tt>&#8221;</p>
<dt><code>&#8211;input-on</code> &lt;list-of-RandR-outputs&gt;</dt>
<dd> Specifies on which outputs the contents of stdin should be appended to the workspace bar. </dd>
<p> Example:<br />
&nbsp;<wbr>&#8211;input-on&nbsp;<wbr>&#8220;<font SIZE="-1">LVDS1</font>&#8221;</p>
<dt><code>&#8211;output-on</code> &lt;list-of-RandR-outputs&gt;</dt>
<dd> Specifies for which outputs i3-wsbar should start <tt>&quot;command&quot;</tt>.</dd>
<dt><code>&#8211;show-all</code></dt>
<dd> If enabled, all workspaces are shown (not only those of the current output). Handy to use with <tt>&quot;--output-on&quot;</tt>. </dd>
</dl>
