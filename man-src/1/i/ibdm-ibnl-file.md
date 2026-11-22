---

title: "ibdm-ibnl-file(1)"
name: "ibdm-ibnl-file"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ibdm-ibnl-file/"
description: "ibnl – a generic IB netlist format"
---

<p> <code>ibnl</code> &#8211; a generic IB netlist format</p>
<h2>DESCRIPTION</h2>
<p> IBDM topology file <code>ibdm-topo-file</code> provide means to describe the IB fabric using a set of predefined systems. A system definition is provided in a single file in IBNL format that describes the internal InfiniBand connectivity of the system in terms of boards and devices. When IBDM starts it parses all the available system definition files before it handles the topology file. The files are located in the following directory relative to the installation prefix: &lt;prefix&gt;/lib/ibdm1.0/ibnl. </p>
<p> This man page describes the IBNL file format used to define an arbitrary IB system internal IB connectivity. It outlines the main concepts used by the file, provides details for how to write such a file and provides a formal definition of the file syntax in BNF like format (YACC/Bison readable).</p>
<h2>1. Main Concepts</h2>
<p> The described file format for defining generic system IB connectivity uses the following terminology:</p>
<dl>
<dt>NODE</dt>
<dd> The instantiation of an IB device may it be a switch or a channel adapter</dd>
<dt>SUB-SYSTEM</dt>
<dd> The instantiation of a board or module in a system</dd>
<dt>SYSTEM</dt>
<dd> A definition of a board or a module</dd>
<dt>TOPSYSTEM</dt>
<dd> The top most system defined in the given file</dd>
<dt>SUB-SYSTEM MODIFIER</dt>
<dd> Many systems allow multiple variations of their subsystem such as a 12X version of a leaf board in a MTS9600. The modifier is a suffix to the board name. The IBNL format supports assigning multiple names to the same board.</dd></dl>
<h2>2. File Format</h2>
<p> The exact file format is provided in section 4. This section only provides extra information regarding the specific semantics of various sections. </p>
<p> The IBNL file is line sensitive as it requires different sections to start on a new line. The file is broken into several SYSTEM (optional) and one TOPSYSTEM sections. Each has one or more names. </p>
<p> Connections are defined inside the SYSTEM/TOPSYSTEM section only and thus might be of two types:</p>
<dl>
<dt>1. Between any node or sub-system to other node or sub-system</dt>
<dd>
</dd><dt>2. From any node or sub-system to a connector of the system.</dt>
<dd></dd></dl>
<p> NOTE-1: The top system can define ports that might be redundant and not connected to any lower level board connector. In these cases the ports are simply omitted from the resulting system. This feature enables defining the front panel ports of a 12X/4X such that if a 12X leaf is selected only the 12X front panel ports are used. </p>
<p> NOTE-2: Port width and speed provided at the lowest level have precedence over definitions provided at upper levels of the hierarchy.</p>
<h2>3. Guidelines for writing a System IBNL File</h2>
<p> The following procedure should be followed in order to provide a new system IBNL:</p>
<dl>
<dt>a)</dt>
<dd> Name the file after the system name: &lt;any sys name (no spaces)&gt;.ibnl</dd>
<dt>b)</dt>
<dd> Define a SYSTEM section for each board included in the system</dd>
<dt>c)</dt>
<dd> The port names of the boards are just strings, we use the simple format of Pn where N is just a serial number but you can pick any name you want. Just make sure it is unique.</dd>
<dt>d)</dt>
<dd> When different flavors of the boards exists like when you have a 4x and 12x option for a board name the optional boards with a modifier postfix. An example for such system that supports a LEAF board of 12x and 4x types would be to define two SYSTEMS:</dd>
<dl>
<dl>
<dt>
</dt><dd> SYSTEM LEAF,LEAF:4x,LEAF:4X </dd>
<p> &#8230; </p>
<p> SYSTEM LEAF:12x,LEAF:12X </p>
<p> &#8230; </p>
<p> NOTE-3: The instantiations of the LEAF boards in another board or the top system need not specify the postfix and are being decided upon only when the topology file is being parsed. The &#8220;SYSTEM LEAF&#8221; with no postfix will be used by default. To continue the example here is how the LEAFs are instantiated in the top system: </p>
<dl>
<dt>
</dt><dd> TOPSYSTEM MyIbSystem </dd>
<p> LEAF leaf1 </p>
<p> &#8230; </p>
<p> LEAF leaf2 </p>
<p> &#8230;</dl>
</dl>
<dl>
<dt>
</dt><dd>
<p> The actual 4x or 12x version of the LEAF board can then be specified in the topology file CFG section to select the right combination of optional boards in the system. An example will be: </p>
</dd><dl>
<dt>
</dt><dd> MyIbSystem N001 CFG: leaf2=12x </dd>
<p> In this case leaf1 will be 4x as no special modifier is defined for it (and LEAF is by default a 4x leaf). Leaf2 will be 12x as defined in the CFG section.</dl>
<dl>
<dt>e)</dt>
<dd> Special considerations should be made to design the top system section when several optional board types exist. Top system section might include multiple definitions for front panel plugs like P1-4x and P1-12x (yes these are just names that should follow the writing on the front or back panels). As the different flavors of the boards are not required to define the same names for their ports including a 12x port might leave some of the top level connections dangling (not connected) and thus the front panel ports of the other flavor will be removed from the final system definition. As an example let us consider a simple board LEAF with 3 4x port flavor and one 12x port flavors. We recommend connecting it in the top level using the following scheme:</dd>
<dl>
<dl>
<dt>
</dt><dd> SYSTEM LEAF:4x </dd>
<p> NODE U1 </p>
<p> 1 -4x-&gt; 4XP1 </p>
<p> 2 -4x-&gt; 4XP2 </p>
<p> 3 -4x-&gt; 4XP3 </p>
<p> &#8230; </p>
<p> SYSTEM LEAF:12x </p>
<p> NODE U1 </p>
<p> 1 -12x-&gt; 12XP1 </p>
<p> &#8230; </p>
<p> TOPSYSTEM myIbSystem </p>
<p> SUBSYSTEM LEAF leaf1 </p>
<p> 4XP1 -&gt; L1/P1 </p>
<p> 4XP2 -&gt; L1/P2 </p>
<p> 4XP3 -&gt; L1/P3 </p>
<p> 12XP1 -&gt; L1/P1-12x</dl>
</dl>
<dl>
<dl>
<dt>f)</dt>
<dd> Place the file in the &lt;prefix&gt;/lib/IBDM/ibdm1.0/ibnl directory</dd>
<dt>g)</dt>
<dd> Check the new file syntax by placing it in the ibnl directory as described above, creating a simple topology (<code>ibdm-topo-file</code> file with one such system and running <code>ibdmtr</code> utility to parse it tracing a simple path through it.</dd></dl>
</dl>
</dl>
</dl>
</dl>
</dl>
<h2>4. Formal definition in YACC Syntax:</h2>
<p> INT ::= ([1-9][0-9]*|0) ; </p>
<p> WIDTH ::= (4x|8x|12x) ; </p>
<p> SPEED ::= (2.5G|5G|10G) ; </p>
<p> NODETYPE ::= (SW|CA|HCA) ; </p>
<p> NAME ::= ([\[\]\\*/A-Za-z0-9_.:%@~]+) ; </p>
<p> NL: LINE | NL LINE; </p>
<p> ONL: | NL; </p>
<p> ibnl: ONL systems topsystem; </p>
<p> systems: | systems system ; </p>
<p> sub_inst_attributes: | sub_inst_attributes sub_inst_attribute NL; </p>
<p> sub_inst_attribute: NAME &#8216;=&#8217; NAME &#8216;=&#8217; NAME | NAME &#8216;=&#8217; NAME &#8216;=&#8217; INT | NAME &#8216;=&#8217; NAME ; </p>
<p> topsystem: TOPSYSTEM system_names NL sub_inst_attributes insts ; </p>
<p> system: SYSTEM system_names NL insts ; </p>
<p> system_names: system_name | system_names &#8216;,&#8217; system_name ; </p>
<p> system_name: NAME ; </p>
<p> insts: | insts node | insts subsystem ; </p>
<p> node: node_header NL node_connections ; </p>
<p> node_header: NODE NODETYPE INT NAME NAME ; </p>
<p> node_connections: | node_connections node_connection NL ; </p>
<p> node_connection: node_to_node_link | node_to_port_link ; </p>
<p> node_to_node_link: INT &#8216;-&#8216; WIDTH &#8216;-&#8216; SPEED &#8216;-&#8216; &#8216;&gt;&#8217; NAME | INT &#8216;-&#8216; WIDTH &#8216;-&#8216; &#8216;&gt;&#8217; NAME INT | INT &#8216;-&#8216; SPEED &#8216;-&#8216; &#8216;&gt;&#8217; NAME INT | INT &#8216;-&#8216; &#8216;&gt;&#8217; NAME INT ; </p>
<p> node_to_port_link: INT &#8216;-&#8216; WIDTH &#8216;-&#8216; SPEED &#8216;-&#8216; &#8216;&gt;&#8217; NAME | INT &#8216;-&#8216; WIDTH &#8216;-&#8216; &#8216;&gt;&#8217; NAME | INT &#8216;-&#8216; SPEED &#8216;-&#8216; &#8216;&gt;&#8217; NAME | INT &#8216;-&#8216; &#8216;&gt;&#8217; NAME ; </p>
<p> subsystem: subsystem_header NL subsystem_connections ; </p>
<p> subsystem_header: SUBSYSTEM NAME NAME ; </p>
<p> subsystem_connections: | subsystem_connections subsystem_connection NL ; </p>
<p> subsystem_connection: subsystem_to_subsystem_link | subsystem_to_port_link ; </p>
<p> subsystem_to_subsystem_link: NAME &#8216;-&#8216; WIDTH &#8216;-&#8216; SPEED &#8216;-&#8216; &#8216;&gt;&#8217; NAME NAME | NAME &#8216;-&#8216; WIDTH &#8216;-&#8216; &#8216;&gt;&#8217; NAME NAME | NAME &#8216;-&#8216; SPEED &#8216;-&#8216; &#8216;&gt;&#8217; NAME NAME | NAME &#8216;-&#8216; &#8216;&gt;&#8217; NAME NAME ; </p>
<p> subsystem_to_port_link: NAME &#8216;-&#8216; WIDTH &#8216;-&#8216; SPEED &#8216;-&#8216; &#8216;&gt;&#8217; NAME | NAME &#8216;-&#8216; WIDTH &#8216;-&#8216; &#8216;&gt;&#8217; NAME | NAME &#8216;-&#8216; SPEED &#8216;-&#8216; &#8216;&gt;&#8217; NAME | NAME &#8216;-&#8216; &#8216;&gt;&#8217; NAME ;</p>
<h2>AUTHOR</h2>
<p> Eitan Zahavi, Mellanox Technologies LTD, eitan [at] mellanox.co.il </p>
