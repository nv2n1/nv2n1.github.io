---
title: "ibstat(8)"
name: "ibstat"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ibstat/"
description: "IBSTAT –"
---

<p>IBSTAT &#8211;</p>
<h2>Query Basic Status Of Infiniband Device(S)</h2>
<h3>Synopsis</h3>
<p>ibstat [options] &lt;ca_name&gt; [portnum]</p>
<h3>Description</h3>
<p>ibstat is a binary which displays basic information obtained from the local IB driver. Output includes LID, SMLID, port state, link width active, and port physical state. </p>
<p> It is similar to the ibstatus utility but implemented as a binary rather than a script. It has options to list CAs and/or ports and displays more information than ibstatus.</p>
<h3>Options</h3>
<dl>
<dt><code>-l, &#8211;list_of_cas</code></p>
<dd>list all IB devices</p>
<dt><code>-s, &#8211;short</code></p>
<dd>short output</p>
<dt><code>-p, &#8211;port_list</code></p>
<dd>show port list</p>
<dt><code>ca_name</code></p>
<dd>InfiniBand device name</p>
<dt><code>portnum</code></p>
<dd>port number of InfiniBand device</dl>
<h3>Debugging flags</h3>
<dl>
<dt><code>-d</code></p>
<dd>raise the IB debugging level. May be used several times (-ddd or -d -d -d). </p>
<p> <code>-h, &#8211;help</code> show the usage message</p>
<dt><code>-v, &#8211;verbose</code></p>
<dd>increase the application verbosity level. May be used several times (-vv or -v -v -v) </p>
<p> <code>-V, &#8211;version</code> show the version info.</dl>
<h3>Configuration flags</h3>
<p><code>&#8211;config, -z &lt;config_file&gt;</code> Specify alternate config file. Default: /etc/infiniband-diags/ibdiag.conf</p>
<h3>Examples</h3>
<dl>
<dt><code>::</code></p>
<dd>ibstat # display status of all ports on all IB devices ibstat -l # list all IB devices ibstat -p # show port guids ibstat mthca0 2 # show status of port 2 of &#8216;mthca0&#8217;</dl>
<h3>See Also</h3>
<p>ibstatus (8)</p>
<h3>Author</h3>
<dl>
<dt><code>Hal Rosenstock</code></p>
<dd>&lt; <i>halr [at] voltaire.com</i> &gt; </p>
</dl>
