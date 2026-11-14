---
title: "rrddump(1)"
name: "rrddump"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rrddump/"
description: "rrddump – dump the contents of an RRD to XML format"
---

<h2 class="name">NAME</h2>
<p> rrddump &#8211; dump the contents of an RRD to XML format </p>
<h2>SYNOPSIS</h2>
<p> <code>rrdtool</code> <code>dump</code> <i>filename.rrd</i> [<i>filename.xml</i>] [<code>&#8211;header</code>|<code>-h</code>&nbsp;<wbr>{none,xsd,dtd}] [<code>&#8211;no-header</code>] [<code>&#8211;daemon</code>&nbsp;<wbr><i>address</i>] &gt;&nbsp;<wbr><i>filename.xml</i></p>
<h2>DESCRIPTION</h2>
<p> The <code>dump</code> function writes the contents of an <font SIZE="-1"><code>RRD</code></font> in human readable (?) <font SIZE="-1">XML</font> format to a file or to stdout. This format can be read by rrdrestore. Together they allow you to transfer your files from one computer architecture to another as well to manipulate the contents of an <font SIZE="-1"><code>RRD</code></font> file in a somewhat more convenient manner.</p>
<dl>
<dt><i>filename.rrd</i></p>
<dd> The name of the <font SIZE="-1"><code>RRD</code></font> you want to dump.</p>
<dt><i>filename.xml</i></p>
<dd> The (optional) filename that you want to write the <font SIZE="-1">XML</font> output to. If not specified, the <font SIZE="-1">XML</font> will be printed to stdout.</p>
<dt><code>&#8211;header</code>|<code>-h</code> {none,xsd,dtd}</p>
<dd> By default RRDtool will add a dtd header to the xml file. Here you can customize this to and xsd header or no header at all.</p>
<dt><code>&#8211;no-header</code></p>
<dd> A shortcut for &#8211;header=none. </p>
<p> If you want to restore the dump with RRDtool 1.2 you should use the &#8211;no-header option since 1.2 can not deal with xml headers.</p>
<dt><code>&#8211;daemon</code> <i>address</i></p>
<dd> Address of the rrdcached daemon. If specified, a <tt>&quot;flush&quot;</tt> command is sent to the server before reading the <font SIZE="-1">RRD</font> files. This allows <code>rrdtool</code> to return fresh data even if the daemon is configured to cache values for a long time. For a list of accepted formats, see the <code>-l</code> option in the rrdcached manual. </p>
<pre>
 rrdtool dump --daemon unix:/var/run/rrdcached.sock /var/lib/rrd/foo.rrd
</pre>
</dl>
<h2>EXAMPLES</h2>
<p> To transfer an <font SIZE="-1">RRD</font> between architectures, follow these steps:</p>
<dl>
<dt>1.</p>
<dd> On the same system where the <font SIZE="-1">RRD</font> was created, use <code>rrdtool</code> <code>dump</code> to export the data to <font SIZE="-1">XML</font> format.</p>
<dt>2.</p>
<dd> Transfer the <font SIZE="-1">XML</font> dump to the target system.</p>
<dt>3.</p>
<dd> Run <code>rrdtool</code> <code>restore</code> to create a new <font SIZE="-1">RRD</font> from the <font SIZE="-1">XML</font> dump. See <code>rrdrestore</code> for details.</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<p> The following environment variables may be used to change the behavior of <tt>&quot;rrdtool dump&quot;</tt>:</p>
<dl>
<dt><font SIZE="-1"><code>RRDCACHED_ADDRESS</code></font></p>
<dd> If this environment variable is set it will have the same effect as specifying the <tt>&quot;--daemon&quot;</tt> option on the command line. If both are present, the command line argument takes precedence.</dl>
<h2>AUTHOR</h2>
<p> Tobias Oetiker &lt;tobi [at] oetiker.ch&gt; </p>
<h2>Index</h2>
