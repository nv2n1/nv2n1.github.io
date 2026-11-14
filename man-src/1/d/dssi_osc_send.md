---
title: "dssi_osc_send(1)"
name: "dssi_osc_send"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dssi_osc_send/"
description: "dssi_osc_send – send OSC messages to DSSI applications."
---

<h2 class="name">NAME</h2>
<p> dssi_osc_send &#8211; send OSC messages to DSSI applications. </p>
<h2>SYNOPSIS</h2>
<p> <code>dssi_osc_send</code> <i>&lt;option&gt; &lt;OSC URL&gt; &lt;values&gt;</i></p>
<h2>DESCRIPTION</h2>
<p> <code>dssi_osc_send</code> sends DSSI OSC methods to DSSI applications. <code>dssi_osc_send</code> is typically used to control DSSI hosts (possibly for scripted operation), or to test DSSI user interfaces.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c</code></p>
<dd> Send a `control&#8217; message. Requires two values to be supplied in the &lt;values&gt; section: control port and value. For example, to set control port 1 to 0.1:<br />
&nbsp;<wbr>&nbsp;<wbr>dssi_osc_send -c&nbsp;<wbr>&lt;OSC URL&gt;&nbsp;<wbr>1 0.1</p>
<dt><code>-p</code></p>
<dd> Send a `program&#8217; message. Requires two values to be supplied in the &lt;values&gt; section: bank and program number. For example, to select bank 0 program number 7:<br />
&nbsp;<wbr>&nbsp;<wbr>dssi_osc_send -p&nbsp;<wbr>&lt;OSC URL&gt;&nbsp;<wbr>0 7</p>
<dt><code>-m</code></p>
<dd> Send `midi&#8217; message. Requires four numbers to be supplied in the &lt;values&gt; section. For example, to send a note on, middle C, velocity 64:<br />
&nbsp;<wbr>&nbsp;<wbr>dssi_osc_send -m&nbsp;<wbr>&lt;OSC URL&gt;&nbsp;<wbr>0 144 60 64</p>
<dt><code>-C</code></p>
<dd> Send a `configure&#8217; message. The &lt;values&gt; are the key and value pair. For example, to send key `load&#8217; and value `/tmp/patches.pat&#8217;:<br />
&nbsp;<wbr>&nbsp;<wbr>dssi_osc_send -C&nbsp;<wbr>&lt;OSC URL&gt;&nbsp;<wbr>load&nbsp;<wbr>/tmp/patches.pat</p>
<dt><code>-s</code></p>
<dd> Send a `show&#8217; message.<br />
&nbsp;<wbr>&nbsp;<wbr>dssi_osc_send -s&nbsp;<wbr>&lt;OSC URL&gt;</p>
<dt><code>-h</code></p>
<dd> Send a `hide&#8217; message.<br />
&nbsp;<wbr>&nbsp;<wbr>dssi_osc_send -h&nbsp;<wbr>&lt;OSC URL&gt;</p>
<dt><code>-q</code></p>
<dd> Send a `quit&#8217; message.<br />
&nbsp;<wbr>&nbsp;<wbr>dssi_osc_send -q&nbsp;<wbr>&lt;OSC URL&gt;</p>
<dt><code>-e</code></p>
<dd> Send a `exiting&#8217; message.<br />
&nbsp;<wbr>&nbsp;<wbr>dssi_osc_send -e&nbsp;<wbr>&lt;OSC URL&gt;</p>
<dt><code>&lt;OSC URL&gt;</code></p>
<dd> The URL to connect to. For example:<br />
&nbsp;<wbr>&nbsp;<wbr>osc.<a href="udp://localhost:19383/dssi/test.1">udp://localhost:19383/dssi/test.1</a><br />
&nbsp;<wbr>&nbsp;<wbr>osc.<a href="udp://my.host.org:10886/dssi/xsynth-dssi/Xsynth/chan00">udp://my.host.org:10886/dssi/xsynth-dssi/Xsynth/chan00</a></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-dssi_osc_update/">dssi_osc_update</a></code>(1). </p>
<h2>AUTHOR</h2>
<p> This manual page was originally created by Mark Hymers from the help text of the application, for the Debian project (but may be freely used by others). </p>
<h2>Index</h2>
