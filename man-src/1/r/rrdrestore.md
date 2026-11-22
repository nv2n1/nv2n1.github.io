---

title: "rrdrestore(1)"
name: "rrdrestore"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rrdrestore/"
description: "rrdrestore – Restore the contents of an RRD from its XML dump format"
---

<p> rrdrestore &#8211; Restore the contents of an RRD from its XML dump format </p>
<h2>SYNOPSIS</h2>
<p> <code>rrdtool</code> <code>restore</code> <i>filename.xml</i> <i>filename.rrd</i> [<code>&#8211;range-check</code>|<code>-r</code>]</p>
<h2>DESCRIPTION</h2>
<p> The <code>restore</code> function reads the XML representation of an RRD and converts it to the native <code>RRD</code> format.</p>
<dl>
<dt><i>filename.xml</i></dt>
<dd> The name of the <code>XML</code> file you want to restore.</dd>
<dt><i>filename.rrd</i></dt>
<dd> The name of the <code>RRD</code> to restore.</dd>
<dt><code>&#8211;range-check</code>|<code>-r</code></dt>
<dd> Make sure the values in the RRAs do not exceed the limits defined for the various data sources.</dd>
<dt><code>&#8211;force-overwrite</code>|<code>-f</code></dt>
<dd> Allows <code>RRDtool</code> to overwrite the destination <code>RRD</code>.</dd></dl>
<h2>AUTHOR</h2>
<p> Tobias Oetiker &lt;tobi [at] oetiker.ch&gt; </p>
