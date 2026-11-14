---
title: "ibdm-topo-file(1)"
name: "ibdm-topo-file"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ibdm-topo-file/"
description: "IBDM Topology File"
---

<h2>NAME</h2>
<p> <code>IBDM Topology File</code> </p>
<p> The topology file describes the IB connectivity and systems included in the network. It serves two purposes:</p>
<dl>
<dt>1. Support for arbitrary system names to be later used in every report that IBDM generates.</p>
<dd>
<dt>2. Connectivity verification: The specified network topology is verified against the discovered one. Mismatch errors resulting from missing cables and/or wrong connections are reported by IBADM.</p>
<dd></dl>
<p> The topology file is composed &quot;system&quot; sections. Each such section describes the connectivity of one system to other systems in the network. The first line of each section is a declaration of the system composed of a system-type, its system-name section, and optional configuration details. The lines to follow until the next empty line describe the connections between this system ports to the other systems. The following is a formal definition of a system section syntax. </p>
<p> An example is listed afterwards. </p>
<p> SYSTEM-TYPE SYSTEM-NAME [CFG: &lt;b1&gt;=&lt;modifier&gt;, [&lt;b2&gt;=&lt;modifier&gt;]&#8230;] </p>
<pre>
        LOCAL-PORT-PANEL-NAME -&gt; REM-SYS-TYPE REM-SYS-NAME REM-PORT-PANEL-NAME
</pre>
<pre>
        LOCAL-PORT-PANEL-NAME -&gt; REM-SYS-TYPE REM-SYS-NAME REM-PORT-PANEL-NAME
</pre>
<pre>
        LOCAL-PORT-PANEL-NAME -&gt; REM-SYS-TYPE REM-SYS-NAME REM-PORT-PANEL-NAME
</pre>
<pre>
        . . .
</pre>
<p> SYSTEM-TYPE SYSTEM-NAME [CFG: &lt;b1&gt;=&lt;modifier&gt;, [&lt;b2&gt;=&lt;modifier&gt;]&#8230;] </p>
<pre>
        LOCAL-PORT-PANEL-NAME -&gt; REM-SYS-TYPE REM-SYS-NAME REM-PORT-PANEL-NAME
</pre>
<pre>
        LOCAL-PORT-PANEL-NAME -&gt; REM-SYS-TYPE REM-SYS-NAME REM-PORT-PANEL-NAME
</pre>
<pre>
        . . .
</pre>
<p> . . . </p>
<p> Where:</p>
<dl>
<dt><code>SYSTEM-TYPE</code> and <code>REM-SYS-TYPE</code></p>
<dd> Any system that has a corresponding IBNL definition. See man <code>ibdm-ibnl-file</code></p>
<dt><code>SYSTEM-NAME</code></p>
<dd> The name of the system described in this topology file section.</p>
<dt><code>LOCAL-PORT-PANEL-NAME</code></p>
<dd> The name of the local system port. The numbers printed on the front panel are used together with Ln for Leaf no. N or Sn for Spine no. N.</p>
<dt><code>REM-SYS-NAME</code></p>
<dd> The name of the system connected to the local port.</p>
<dt><code>REM-PORT-PANEL-NAME</code></p>
<dd> A name of the remote system port. We use the numbers as printed on the front panel and Ln for Leaf number N or Sn for Spine number N.</dl>
<h2>EXAMPLE</h2>
<p> The following is a topology file for a simple cluster with one 24 port switch and two HCAs. The firts <font SIZE="-1">HCA</font> named H-1 and connect to the fabric with its two ports. The second <font SIZE="-1">HCA</font> named H-2. The switch is of type <font SIZE="-1">MTS2400</font> and is named S-1 </p>
<p> <font SIZE="-1">MTS2400</font> S-1<br />
P1 -&gt;&nbsp;<wbr><font SIZE="-1">MT23108</font>&nbsp;<wbr>H-1 P1<br />
P2 -&gt;&nbsp;<wbr><font SIZE="-1">MT23108</font>&nbsp;<wbr>H-1 P2<br />
P24 -&gt;&nbsp;<wbr><font SIZE="-1">MT23108</font>&nbsp;<wbr>H-2 P1</p>
<h2>OPTIONAL CFG SECTION</h2>
<p> This section in the system declaration line describes the special customization of each board of the system. </p>
<p> That is the <font SIZE="-1">CFG</font> string is a set of comma-separated sub-fields. Each sub-field describes some special configuration of a corresponding system board. The actual semantics of the specific board modifiers is defined by the <font SIZE="-1">IBNL</font> of the specific system.</p>
<h2>EXAMPLE</h2>
<p> The following is an example of a definition-line in a topology file of the <font SIZE="-1">MTS9600</font> switch system. This switch system can have up to eight leafs and four spines. This example of the <font SIZE="-1">MTS9600</font> lacks (R) leafs no.6,7 and 8, and lacks spines no. 3 and 4. </p>
<p> <font SIZE="-1">MTS9600</font> PartialGz1 <font SIZE="-1">CFG:</font> leaf3=R,leaf5=R,leaf7=R,spine1=R</p>
<h2>AUTHOR</h2>
<p> Eitan Zahavi, Mellanox Technologies <font SIZE="-1">LTD</font>, eitan [at] mellanox.co.il </p>
<h2>Index</h2>
