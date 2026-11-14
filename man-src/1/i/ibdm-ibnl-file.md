---
title: "ibdm-ibnl-file(1)"
name: "ibdm-ibnl-file"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ibdm-ibnl-file/"
description: "ibnl – a generic IB netlist format"
---

<h2>NAME</h2>
<p> <code>ibnl</code> &#8211; a generic IB netlist format</p>
<h2>DESCRIPTION</h2>
<p> <font SIZE="-1">IBDM</font> topology file <code>ibdm-topo-file</code> provide means to describe the <font SIZE="-1">IB</font> fabric using a set of predefined systems. A system definition is provided in a single file in <font SIZE="-1">IBNL</font> format that describes the internal InfiniBand connectivity of the system in terms of boards and devices. When <font SIZE="-1">IBDM</font> starts it parses all the available system definition files before it handles the topology file. The files are located in the following directory relative to the installation prefix: &lt;prefix&gt;/lib/ibdm1.0/ibnl. </p>
<p> This man page describes the <font SIZE="-1">IBNL</font> file format used to define an arbitrary <font SIZE="-1">IB</font> system internal <font SIZE="-1">IB</font> connectivity. It outlines the main concepts used by the file, provides details for how to write such a file and provides a formal definition of the file syntax in <font SIZE="-1">BNF</font> like format (YACC/Bison readable).</p>
<h2>1. Main Concepts</h2>
<p> The described file format for defining generic system <font SIZE="-1">IB</font> connectivity uses the following terminology:</p>
<dl>
<dt><font SIZE="-1">NODE</font></p>
<dd> The instantiation of an <font SIZE="-1">IB</font> device may it be a switch or a channel adapter</p>
<dt>SUB-SYSTEM</p>
<dd> The instantiation of a board or module in a system</p>
<dt><font SIZE="-1">SYSTEM</font></p>
<dd> A definition of a board or a module</p>
<dt><font SIZE="-1">TOPSYSTEM</font></p>
<dd> The top most system defined in the given file</p>
<dt>SUB-SYSTEM <font SIZE="-1">MODIFIER</font></p>
<dd> Many systems allow multiple variations of their subsystem such as a 12X version of a leaf board in a <font SIZE="-1">MTS9600</font>. The modifier is a suffix to the board name. The <font SIZE="-1">IBNL</font> format supports assigning multiple names to the same board.</dl>
<h2>2. File Format</h2>
<p> The exact file format is provided in section 4. This section only provides extra information regarding the specific semantics of various sections. </p>
<p> The <font SIZE="-1">IBNL</font> file is line sensitive as it requires different sections to start on a new line. The file is broken into several <font SIZE="-1">SYSTEM</font> (optional) and one <font SIZE="-1">TOPSYSTEM</font> sections. Each has one or more names. </p>
<p> Connections are defined inside the <font SIZE="-1">SYSTEM/TOPSYSTEM</font> section only and thus might be of two types:</p>
<dl>
<dt>1. Between any node or sub-system to other node or sub-system</p>
<dd>
<dt>2. From any node or sub-system to a connector of the system.</p>
<dd></dl>
<p> <font SIZE="-1">NOTE-1:</font> The top system can define ports that might be redundant and not connected to any lower level board connector. In these cases the ports are simply omitted from the resulting system. This feature enables defining the front panel ports of a 12X/4X such that if a 12X leaf is selected only the 12X front panel ports are used. </p>
<p> <font SIZE="-1">NOTE-2:</font> Port width and speed provided at the lowest level have precedence over definitions provided at upper levels of the hierarchy.</p>
<h2>3. Guidelines for writing a System IBNL File</h2>
<p> The following procedure should be followed in order to provide a new system <font SIZE="-1">IBNL:</font></p>
<dl>
<dt>a)</p>
<dd> Name the file after the system name: &lt;any sys name (no spaces)&gt;.ibnl</p>
<dt>b)</p>
<dd> Define a <font SIZE="-1">SYSTEM</font> section for each board included in the system</p>
<dt>c)</p>
<dd> The port names of the boards are just strings, we use the simple format of Pn where N is just a serial number but you can pick any name you want. Just make sure it is unique.</p>
<dt>d)</p>
<dd> When different flavors of the boards exists like when you have a 4x and 12x option for a board name the optional boards with a modifier postfix. An example for such system that supports a <font SIZE="-1">LEAF</font> board of 12x and 4x types would be to define two <font SIZE="-1">SYSTEMS:</font></p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> <font SIZE="-1">SYSTEM</font> <font SIZE="-1">LEAF</font>,LEAF:4x,LEAF:4X </p>
<p> &#8230; </p>
<p> <font SIZE="-1">SYSTEM</font> LEAF:12x,LEAF:12X </p>
<p> &#8230; </p>
<p> <font SIZE="-1">NOTE-3:</font> The instantiations of the <font SIZE="-1">LEAF</font> boards in another board or the top system need not specify the postfix and are being decided upon only when the topology file is being parsed. The &#8220;<font SIZE="-1">SYSTEM</font> <font SIZE="-1">LEAF</font>&#8221; with no postfix will be used by default. To continue the example here is how the LEAFs are instantiated in the top system: </p>
<dl>
<dt>
<dd> <font SIZE="-1">TOPSYSTEM</font> MyIbSystem </p>
<p> <font SIZE="-1">LEAF</font> leaf1 </p>
<p> &#8230; </p>
<p> <font SIZE="-1">LEAF</font> leaf2 </p>
<p> &#8230;</dl>
</dl>
<dl>
<dt>
<dd>
<p> The actual 4x or 12x version of the <font SIZE="-1">LEAF</font> board can then be specified in the topology file <font SIZE="-1">CFG</font> section to select the right combination of optional boards in the system. An example will be: </p>
<dl>
<dt>
<dd> MyIbSystem N001 <font SIZE="-1">CFG:</font> leaf2=12x </p>
<p> In this case leaf1 will be 4x as no special modifier is defined for it (and <font SIZE="-1">LEAF</font> is by default a 4x leaf). Leaf2 will be 12x as defined in the <font SIZE="-1">CFG</font> section.</dl>
<dl>
<dt>e)</p>
<dd> Special considerations should be made to design the top system section when several optional board types exist. Top system section might include multiple definitions for front panel plugs like P1-4x and P1-12x (yes these are just names that should follow the writing on the front or back panels). As the different flavors of the boards are not required to define the same names for their ports including a 12x port might leave some of the top level connections dangling (not connected) and thus the front panel ports of the other flavor will be removed from the final system definition. As an example let us consider a simple board <font SIZE="-1">LEAF</font> with 3 4x port flavor and one 12x port flavors. We recommend connecting it in the top level using the following scheme:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> <font SIZE="-1">SYSTEM</font> LEAF:4x </p>
<p> <font SIZE="-1">NODE</font> U1 </p>
<p> 1 -4x-&gt; 4XP1 </p>
<p> 2 -4x-&gt; 4XP2 </p>
<p> 3 -4x-&gt; 4XP3 </p>
<p> &#8230; </p>
<p> <font SIZE="-1">SYSTEM</font> LEAF:12x </p>
<p> <font SIZE="-1">NODE</font> U1 </p>
<p> 1 -12x-&gt; 12XP1 </p>
<p> &#8230; </p>
<p> <font SIZE="-1">TOPSYSTEM</font> myIbSystem </p>
<p> <font SIZE="-1">SUBSYSTEM</font> <font SIZE="-1">LEAF</font> leaf1 </p>
<p> 4XP1 -&gt; L1/P1 </p>
<p> 4XP2 -&gt; L1/P2 </p>
<p> 4XP3 -&gt; L1/P3 </p>
<p> 12XP1 -&gt; L1/P1-12x</dl>
</dl>
<dl>
<dt>
<dd>
<dl>
<dt>f)</p>
<dd> Place the file in the &lt;prefix&gt;/lib/IBDM/ibdm1.0/ibnl directory</p>
<dt>g)</p>
<dd> Check the new file syntax by placing it in the ibnl directory as described above, creating a simple topology (<code>ibdm-topo-file</code> file with one such system and running <code>ibdmtr</code> utility to parse it tracing a simple path through it.</dl>
</dl>
</dl>
</dl>
</dl>
</dl>
<h2>4. Formal definition in YACC Syntax:</h2>
<p> <font SIZE="-1">INT</font> ::= ([1-9][0-9]*|0) ; </p>
<p> <font SIZE="-1">WIDTH</font> ::= (4x|8x|12x) ; </p>
<p> <font SIZE="-1">SPEED</font> ::= (2.5G|5G|10G) ; </p>
<p> <font SIZE="-1">NODETYPE</font> ::= (SW|CA|HCA) ; </p>
<p> <font SIZE="-1">NAME</font> ::= ([\[\]\\*/A-Za-z0-9_.:%@~]+) ; </p>
<p> <font SIZE="-1">NL:</font> <font SIZE="-1">LINE</font> | <font SIZE="-1">NL</font> <font SIZE="-1">LINE</font>; </p>
<p> <font SIZE="-1">ONL:</font> | <font SIZE="-1">NL</font>; </p>
<p> ibnl: <font SIZE="-1">ONL</font> systems topsystem; </p>
<p> systems: | systems system ; </p>
<p> sub_inst_attributes: | sub_inst_attributes sub_inst_attribute <font SIZE="-1">NL</font>; </p>
<p> sub_inst_attribute: <font SIZE="-1">NAME</font> &#8216;=&#8217; <font SIZE="-1">NAME</font> &#8216;=&#8217; <font SIZE="-1">NAME</font> | <font SIZE="-1">NAME</font> &#8216;=&#8217; <font SIZE="-1">NAME</font> &#8216;=&#8217; <font SIZE="-1">INT</font> | <font SIZE="-1">NAME</font> &#8216;=&#8217; <font SIZE="-1">NAME</font> ; </p>
<p> topsystem: <font SIZE="-1">TOPSYSTEM</font> system_names <font SIZE="-1">NL</font> sub_inst_attributes insts ; </p>
<p> system: <font SIZE="-1">SYSTEM</font> system_names <font SIZE="-1">NL</font> insts ; </p>
<p> system_names: system_name | system_names &#8216;,&#8217; system_name ; </p>
<p> system_name: <font SIZE="-1">NAME</font> ; </p>
<p> insts: | insts node | insts subsystem ; </p>
<p> node: node_header <font SIZE="-1">NL</font> node_connections ; </p>
<p> node_header: <font SIZE="-1">NODE</font> <font SIZE="-1">NODETYPE</font> <font SIZE="-1">INT</font> <font SIZE="-1">NAME</font> <font SIZE="-1">NAME</font> ; </p>
<p> node_connections: | node_connections node_connection <font SIZE="-1">NL</font> ; </p>
<p> node_connection: node_to_node_link | node_to_port_link ; </p>
<p> node_to_node_link: <font SIZE="-1">INT</font> &#8216;-&#8216; <font SIZE="-1">WIDTH</font> &#8216;-&#8216; <font SIZE="-1">SPEED</font> &#8216;-&#8216; &#8216;&gt;&#8217; <font SIZE="-1">NAME</font> | <font SIZE="-1">INT</font> &#8216;-&#8216; <font SIZE="-1">WIDTH</font> &#8216;-&#8216; &#8216;&gt;&#8217; <font SIZE="-1">NAME</font> <font SIZE="-1">INT</font> | <font SIZE="-1">INT</font> &#8216;-&#8216; <font SIZE="-1">SPEED</font> &#8216;-&#8216; &#8216;&gt;&#8217; <font SIZE="-1">NAME</font> <font SIZE="-1">INT</font> | <font SIZE="-1">INT</font> &#8216;-&#8216; &#8216;&gt;&#8217; <font SIZE="-1">NAME</font> <font SIZE="-1">INT</font> ; </p>
<p> node_to_port_link: <font SIZE="-1">INT</font> &#8216;-&#8216; <font SIZE="-1">WIDTH</font> &#8216;-&#8216; <font SIZE="-1">SPEED</font> &#8216;-&#8216; &#8216;&gt;&#8217; <font SIZE="-1">NAME</font> | <font SIZE="-1">INT</font> &#8216;-&#8216; <font SIZE="-1">WIDTH</font> &#8216;-&#8216; &#8216;&gt;&#8217; <font SIZE="-1">NAME</font> | <font SIZE="-1">INT</font> &#8216;-&#8216; <font SIZE="-1">SPEED</font> &#8216;-&#8216; &#8216;&gt;&#8217; <font SIZE="-1">NAME</font> | <font SIZE="-1">INT</font> &#8216;-&#8216; &#8216;&gt;&#8217; <font SIZE="-1">NAME</font> ; </p>
<p> subsystem: subsystem_header <font SIZE="-1">NL</font> subsystem_connections ; </p>
<p> subsystem_header: <font SIZE="-1">SUBSYSTEM</font> <font SIZE="-1">NAME</font> <font SIZE="-1">NAME</font> ; </p>
<p> subsystem_connections: | subsystem_connections subsystem_connection <font SIZE="-1">NL</font> ; </p>
<p> subsystem_connection: subsystem_to_subsystem_link | subsystem_to_port_link ; </p>
<p> subsystem_to_subsystem_link: <font SIZE="-1">NAME</font> &#8216;-&#8216; <font SIZE="-1">WIDTH</font> &#8216;-&#8216; <font SIZE="-1">SPEED</font> &#8216;-&#8216; &#8216;&gt;&#8217; <font SIZE="-1">NAME</font> <font SIZE="-1">NAME</font> | <font SIZE="-1">NAME</font> &#8216;-&#8216; <font SIZE="-1">WIDTH</font> &#8216;-&#8216; &#8216;&gt;&#8217; <font SIZE="-1">NAME</font> <font SIZE="-1">NAME</font> | <font SIZE="-1">NAME</font> &#8216;-&#8216; <font SIZE="-1">SPEED</font> &#8216;-&#8216; &#8216;&gt;&#8217; <font SIZE="-1">NAME</font> <font SIZE="-1">NAME</font> | <font SIZE="-1">NAME</font> &#8216;-&#8216; &#8216;&gt;&#8217; <font SIZE="-1">NAME</font> <font SIZE="-1">NAME</font> ; </p>
<p> subsystem_to_port_link: <font SIZE="-1">NAME</font> &#8216;-&#8216; <font SIZE="-1">WIDTH</font> &#8216;-&#8216; <font SIZE="-1">SPEED</font> &#8216;-&#8216; &#8216;&gt;&#8217; <font SIZE="-1">NAME</font> | <font SIZE="-1">NAME</font> &#8216;-&#8216; <font SIZE="-1">WIDTH</font> &#8216;-&#8216; &#8216;&gt;&#8217; <font SIZE="-1">NAME</font> | <font SIZE="-1">NAME</font> &#8216;-&#8216; <font SIZE="-1">SPEED</font> &#8216;-&#8216; &#8216;&gt;&#8217; <font SIZE="-1">NAME</font> | <font SIZE="-1">NAME</font> &#8216;-&#8216; &#8216;&gt;&#8217; <font SIZE="-1">NAME</font> ;</p>
<h2>AUTHOR</h2>
<p> Eitan Zahavi, Mellanox Technologies <font SIZE="-1">LTD</font>, eitan [at] mellanox.co.il </p>
<h2>Index</h2>
