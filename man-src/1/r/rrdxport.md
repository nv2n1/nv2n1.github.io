---
title: "rrdxport(1)"
name: "rrdxport"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rrdxport/"
description: "rrdxport – Export data in XML format based on data from one or several RRD"
---

<h2 class="name">NAME</h2>
<p> rrdxport &#8211; Export data in XML format based on data from one or several RRD </p>
<h2>SYNOPSIS</h2>
<p> <code>rrdtool</code> <code>xport</code> [<code>-s</code>|<code>&#8211;start</code>&nbsp;<wbr><i>seconds</i>] [<code>-e</code>|<code>&#8211;end</code>&nbsp;<wbr><i>seconds</i>] [<code>-m</code>|<code>&#8211;maxrows</code>&nbsp;<wbr><i>rows</i>] [<code>&#8211;step</code>&nbsp;<wbr><i>value</i>] [<code>&#8211;json</code>] [<code>&#8211;daemon</code>&nbsp;<wbr><i>address</i>] [<font SIZE="-1"><code>DEF:</code></font><i>vname</i><code>=</code><i>rrd</i><code>:</code><i>ds-name</i><code>:</code><i></i><font SIZE="-1"><i>CF</i></font><i></i>] [<font SIZE="-1"><code>CDEF:</code></font><i>vname</i><code>=</code><i>rpn-expression</i>] [<font SIZE="-1"><code>XPORT</code></font><code>:</code><i>vname</i>[<code>:</code><i>legend</i>]]</p>
<h2>DESCRIPTION</h2>
<p> The <code>xport</code> function&#8217;s main purpose is to write an <font SIZE="-1">XML</font> formatted representation of the data stored in one or several <font SIZE="-1"><code>RRD</code></font>s. It can also extract numerical reports. </p>
<p> If no <i></i><font SIZE="-1"><i>XPORT</i></font><i></i> statements are found, there will be no output.</p>
<dl>
<dt><code>-s</code>|<code>&#8211;start</code> <i>seconds</i> (default end-1day)</p>
<dd> The time when the exported range should begin. Time in seconds since epoch (1970-01-01) is required. Negative numbers are relative to the current time. By default one day worth of data will be printed. See also AT-STYLE <font SIZE="-1">TIME</font> <font SIZE="-1">SPECIFICATION</font> section in the <i>rrdfetch</i> documentation for a detailed explanation on how to specify time.</p>
<dt><code>-e</code>|<code>&#8211;end</code> <i>seconds</i> (default now)</p>
<dd> The time when the exported range should end. Time in seconds since epoch. See also AT-STYLE <font SIZE="-1">TIME</font> <font SIZE="-1">SPECIFICATION</font> section in the <i>rrdfetch</i> documentation for a detailed explanation of ways to specify time.</p>
<dt><code>-m</code>|<code>&#8211;maxrows</code> <i>rows</i> (default 400 rows)</p>
<dd> This works like the <code>-w</code>|<code>&#8211;width</code> parameter of <i>rrdgraph</i>. In fact it is exactly the same, but the parameter was renamed to describe its purpose in this module. See <i>rrdgraph</i> documentation for details.</p>
<dt><code>&#8211;step</code> <i>value</i> (default automatic)</p>
<dd> See rrdgraph documentation.</p>
<dt><code>&#8211;daemon</code> <i>address</i></p>
<dd> Address of the rrdcached daemon. If specified, a <tt>&quot;flush&quot;</tt> command is sent to the server before reading the <font SIZE="-1">RRD</font> files. This allows <code>rrdtool</code> to return fresh data even if the daemon is configured to cache values for a long time. For a list of accepted formats, see the <code>-l</code> option in the rrdcached manual. </p>
<pre>
  rrdtool xport --daemon unix:/var/run/rrdcached.sock ...
</pre>
<dt><code>&#8211;json</code></p>
<dd> produce json formated output (instead of xml)</p>
<dt><code>&#8211;enumds</code></p>
<dd> The generated xml should contain the data values in enumerated tags. </p>
<pre>
 &lt;v0&gt;val&lt;/v0&gt;&lt;v1&gt;val&lt;/v1&gt;
</pre>
<dt><font SIZE="-1"><code>DEF:</code></font><i>vname</i><code>=</code><i>rrd</i><code>:</code><i>ds-name</i><code>:</code><i></i><font SIZE="-1"><i>CF</i></font><i></i></p>
<dd> See <i>rrdgraph</i> documentation.</p>
<dt><font SIZE="-1"><code>CDEF:</code></font><i>vname</i><code>=</code><i>rpn-expression</i></p>
<dd> See <i>rrdgraph</i> documentation.</p>
<dt><font SIZE="-1"><code>XPORT:</code></font><i>vname</i><code>:</code><code>:</code><i>legend</i></p>
<dd> At least one <i></i><font SIZE="-1"><i>XPORT</i></font><i></i> statement should be present. The values referenced by <i>vname</i> are printed. Optionally add a legend.</dl>
<h2>Output format</h2>
<p> The output is enclosed in an <code>xport</code> element and contains two blocks. The first block is enclosed by a <code>meta</code> element and contains some meta data. The second block is enclosed by a <code>data</code> element and contains the data rows. </p>
<p> Let&#8217;s assume that the <i>xport</i> command looks like this: </p>
<pre>
  rrdtool xport \
          --start now-1h --end now \
          DEF:xx=host-inout.lo.rrd:output:AVERAGE \
          DEF:yy=host-inout.lo.rrd:input:AVERAGE \
          CDEF:aa=xx,yy,+,8,* \
          XPORT:xx:&quot;out bytes&quot; \
          XPORT:aa:&quot;in and out bits&quot;
</pre>
<p> The resulting meta data section is (the values will depend on the <font SIZE="-1">RRD</font> characteristics): </p>
<pre>
  &lt;meta&gt;
    &lt;start&gt;1020611700&lt;/start&gt;
    &lt;step&gt;300&lt;/step&gt;
    &lt;end&gt;1020615600&lt;/end&gt;
    &lt;rows&gt;14&lt;/rows&gt;
    &lt;columns&gt;2&lt;/columns&gt;
    &lt;legend&gt;
      &lt;entry&gt;out bytes&lt;/entry&gt;
      &lt;entry&gt;in and out bits&lt;/entry&gt;
    &lt;/legend&gt;
  &lt;/meta&gt;
</pre>
<p> The resulting data section is: </p>
<pre>
  &lt;data&gt;
    &lt;row&gt;&lt;t&gt;1020611700&lt;/t&gt;&lt;v&gt;3.4000000000e+00&lt;/v&gt;&lt;v&gt;5.4400000000e+01&lt;/v&gt;&lt;/row&gt;
    &lt;row&gt;&lt;t&gt;1020612000&lt;/t&gt;&lt;v&gt;3.4000000000e+00&lt;/v&gt;&lt;v&gt;5.4400000000e+01&lt;/v&gt;&lt;/row&gt;
    &lt;row&gt;&lt;t&gt;1020612300&lt;/t&gt;&lt;v&gt;3.4000000000e+00&lt;/v&gt;&lt;v&gt;5.4400000000e+01&lt;/v&gt;&lt;/row&gt;
    &lt;row&gt;&lt;t&gt;1020612600&lt;/t&gt;&lt;v&gt;3.4113333333e+00&lt;/v&gt;&lt;v&gt;5.4581333333e+01&lt;/v&gt;&lt;/row&gt;
    &lt;row&gt;&lt;t&gt;1020612900&lt;/t&gt;&lt;v&gt;3.4000000000e+00&lt;/v&gt;&lt;v&gt;5.4400000000e+01&lt;/v&gt;&lt;/row&gt;
    &lt;row&gt;&lt;t&gt;1020613200&lt;/t&gt;&lt;v&gt;3.4000000000e+00&lt;/v&gt;&lt;v&gt;5.4400000000e+01&lt;/v&gt;&lt;/row&gt;
    &lt;row&gt;&lt;t&gt;1020613500&lt;/t&gt;&lt;v&gt;3.4000000000e+00&lt;/v&gt;&lt;v&gt;5.4400000000e+01&lt;/v&gt;&lt;/row&gt;
    &lt;row&gt;&lt;t&gt;1020613800&lt;/t&gt;&lt;v&gt;3.4000000000e+00&lt;/v&gt;&lt;v&gt;5.4400000000e+01&lt;/v&gt;&lt;/row&gt;
    &lt;row&gt;&lt;t&gt;1020614100&lt;/t&gt;&lt;v&gt;3.4000000000e+00&lt;/v&gt;&lt;v&gt;5.4400000000e+01&lt;/v&gt;&lt;/row&gt;
    &lt;row&gt;&lt;t&gt;1020614400&lt;/t&gt;&lt;v&gt;3.4000000000e+00&lt;/v&gt;&lt;v&gt;5.4400000000e+01&lt;/v&gt;&lt;/row&gt;
    &lt;row&gt;&lt;t&gt;1020614700&lt;/t&gt;&lt;v&gt;3.7333333333e+00&lt;/v&gt;&lt;v&gt;5.9733333333e+01&lt;/v&gt;&lt;/row&gt;
    &lt;row&gt;&lt;t&gt;1020615000&lt;/t&gt;&lt;v&gt;3.4000000000e+00&lt;/v&gt;&lt;v&gt;5.4400000000e+01&lt;/v&gt;&lt;/row&gt;
    &lt;row&gt;&lt;t&gt;1020615300&lt;/t&gt;&lt;v&gt;3.4000000000e+00&lt;/v&gt;&lt;v&gt;5.4400000000e+01&lt;/v&gt;&lt;/row&gt;
    &lt;row&gt;&lt;t&gt;1020615600&lt;/t&gt;&lt;v&gt;NaN&lt;/v&gt;&lt;v&gt;NaN&lt;/v&gt;&lt;/row&gt;
  &lt;/data&gt;
</pre>
<h2>EXAMPLE 1</h2>
<pre>
  rrdtool xport \
          DEF:out=if1-inouts.rrd:outoctets:AVERAGE \
          XPORT:out:&quot;out bytes&quot;
</pre>
<h2>EXAMPLE 2</h2>
<pre>
  rrdtool xport \
          DEF:out1=if1-inouts.rrd:outoctets:AVERAGE \
          DEF:out2=if2-inouts.rrd:outoctets:AVERAGE \
          CDEF:sum=out1,out2,+ \
          XPORT:out1:&quot;if1 out bytes&quot; \
          XPORT:out2:&quot;if2 out bytes&quot; \
          XPORT:sum:&quot;output sum&quot;
</pre>
<h2>ENVIRONMENT VARIABLES</h2>
<p> The following environment variables may be used to change the behavior of <tt>&quot;rrdtool xport&quot;</tt>:</p>
<dl>
<dt><font SIZE="-1"><code>RRDCACHED_ADDRESS</code></font></p>
<dd> If this environment variable is set it will have the same effect as specifying the <tt>&quot;--daemon&quot;</tt> option on the command line. If both are present, the command line argument takes precedence.</dl>
<h2>AUTHOR</h2>
<p> Tobias Oetiker &lt;tobi [at] oetiker.ch&gt; </p>
<h2>Index</h2>
