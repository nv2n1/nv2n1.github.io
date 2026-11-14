---
title: "electric(1)"
name: "electric"
section: "1"
letter: "e"
url: "/docs/linux/man/1-electric/"
description: "electric – a VLSI design system"
---

<h2>NAME</h2>
<p> electric &#8211; a VLSI design system </p>
<h2>SYNOPSIS</h2>
<p> <code>electric</code> [<i>-m</i>] [<i>-t technology</i>] [<i>library</i>] </p>
<h2>DESCRIPTION</h2>
<p> Electric is a general purpose system for all electrical design. It currently knows about nMOS, CMOS, Bipolar, artwork, schematics, printed-circuit boards, and many other technologies. Its has a large set of tools including multiple design-rule checkers (both incremental and hierarchical), an electrical rules checker, over a dozen simulator interfaces, multiple generators (PLA and pad frame), multiple routers (stitching, maze, river), network comparison, compaction, compensation, a VHDL compiler, and a silicon compiler that places-and-routes standard cells. </p>
<p> In addition to the text terminal used to invoke the program, Electric uses a color display with a mouse as a work station. Separate windows are used for text and graphics. </p>
<p> If a <i>library</i> disk file is mentioned on the command line, that file is read as the initial design for editing. In addition, the following switches are recognized:</p>
<dl>
<dt>-t</p>
<dd> specifies an initial technology. The argument must be a technology name such as &quot;nmos&quot;, &quot;cmos&quot;, &quot;mocmos&quot; (MOSIS CMOS), &quot;mocmossub&quot; (MOSIS CMOS Submicron), &quot;bipolar&quot; (simple Bipolar), &quot;schematic&quot; (Schematic capture), or &quot;artwork&quot; (sketchpad mode).</p>
<dt>-m</p>
<dd> specifies there may be multiple monitors and that Electric should look for them. </p>
</dl>
<h2>REPRESENTATION</h2>
<p> Circuits are represented as networks that contain <i>nodes</i> and connecting <i>arcs</i>. The nodes are electrical components such as transistors, logic gates, and contacts. The arcs are simply wires that connect the nodes. In addition, each node has a set of <i>ports</i> which are the sites of arc connection. A <i>technology</i>, then, is simply a set of primitive nodes and arcs that are the building blocks of circuits designed in that environment. </p>
<p> Collections of nodes and arcs can also be aggregated into <i>facets</i> of <i>cells</i> which can be used higher in the hierarchy to act as nodes. These user-defined nodes have ports that come from internal nodes whose ports are <i>exported</i>. Facets are collected in <i>libraries</i> which contain a hierarchically consistent design. </p>
<p> Arcs have properties that help constrain the design. For example, an arc may rotate arbitrarily or be fixed in their angle. Arcs can also be stretchable or <i>rigid</i> under modification of their connecting nodes. These constraints propagate hierarchically from the bottom-up. </p>
<h2>TECHNOLOGIES</h2>
<p> A large set of technologies is provided in Electric. These can be modified with the technology editor, or completely new technologies can be created. The following paragraphs describe some of the basic technologies. </p>
<p> The nMOS technologies have arcs available in Metal, Polysilicon, and Diffusion. The primitive nodes include normal contacts, buried contacts, transistors, and &quot;pins&quot; for making arc corners. Transistors may be serpentine and the pure layer nodes may be polygonally described with the <code>node trace</code> command. The &quot;nmos&quot; technology has the standard Mead&amp;Conway design rules. </p>
<p> The CMOS technologies have arcs available in Metal, Polysilicon, and Diffusion. The Diffusion arcs may be found in a P-well implant or in a P implant. Thus, there are two types of metal-to-diffusion contacts, two types of diffusion pins, and two types of transistors: in P-well and in P implant. As with nMOS, the transistors may be serpentine and the pure layer primitives may be polygonally defined. The &quot;cmos&quot; technology has the standard design rules according to Griswold; the &quot;mocmos&quot; technology has design rules for the MOSIS CMOS process (double metal); the &quot;mocmossub&quot; technology has design rules for the MOSIS CMOS Submicron process (double poly and up to 6 metal); the &quot;rcmos&quot; technology has round geometry for the MOSIS CMOS process. </p>
<p> The &quot;schematic&quot; technology provides basic symbols for doing schematic capture. It contains the logic symbols: BUFFER, AND, OR, and XOR. Negating bubbles can be placed by negating a connecting arc. There are also more complex components such as flip-flop, off-page-connector, black-box, meter, and power source. Finally, there are the electrical components: transistor, resistor, diode, capacitor, and inductor. Two arc types exist for normal wires and variable-width busses. </p>
<p> The &quot;artwork&quot; technology is a sketchpad environment for doing general-purpose graphics. Components can be placed with arbitrary color and shape. </p>
<p> The &quot;generic&quot; technology exists for those miscellaneous purposes that do not fall into the domain of other technologies. It has the universal arc and pin which can connect to ANY other object and are therefore useful in mixed-technology designs. The invisible arc can be used for constraining two nodes without making a connection. The unrouted arc can be used for electrical connections that are to be routed later with real wires. The facet-center primitive, when placed in a facet, defines the cursor origin on instances of that facet. </p>
<h2>DESIGN-RULE CHECKING</h2>
<p> The incremental design-rule checker is normally on and watches all changes made to the circuit. It does not correct but prints error messages when design rules are violated. Hierarchy is not handled, so the contents of subfacets are not checked. </p>
<p> The hierarchical checker looks all the way down the circuit for all design-rules. Another option allows an input deck to prepared for ECAD&#8217;s Dracula design-rule checker. </p>
<h2>COMPACTION</h2>
<p> The compactor attempts to reduce the size of a facet by removing unnecessary space between elements. When invoked it will compact in the vertical and horizontal directions until it can find no way to compact the facet any further. It does not do hierarchical compaction, does not guarantee optimal compaction, nor can it handle non-manhattan geometry properly. The compactor will also spread out the facet to guarantee no design-rule violations, if the &quot;spread&quot; option is set. </p>
<h2>SIMULATION</h2>
<p> There are many simulator interfaces: ESIM (the default simulator: switch-level for nMOS without timing), RSIM (switch-level for MOS with timing), RNL (switch-level for MOS with timing and LISP front-end), MOSSIM (switch-level for MOS with timing), COSMOS (switch-level for MOS with timing), VERILOG (Cadence simulator), TEXSIM (a commercial simulator), SILOS (a commercial simulator), ABEL (PAL generator/simulator for schematic), and SPICE (circuit level). MOSSIM, COSMOS, VERILOG, TEXSIM, SILOS, and ABEL do not actually simulate: they only write an input deck of your circuit. </p>
<p> In preparation for most simulators, it is necessary to export those ports that you wish to manipulate or examine. You must also export power and ground ports. </p>
<p> In preparation for SPICE simulation, you must export power and ground signals and. explicitly connect them to source nodes. The source should then be parameterized to indicate the amount and whether it is voltage or current. For example, to make a 5 volt supply, create a source node and set the SPICE card to: &quot;DC 5&quot;. Next, all input ports must be exported and connected to the positive side of sources. Next, all values that are being plotted must be exported and have meter nodes placed on them. The node should have the top and bottom ports connected appropriately. </p>
<h2>PLA GENERATION</h2>
<p> There are two PLA generators, one specific to nMOS layout, and another specific to CMOS layout. The nMOS PLA generator reads a single personality table and generates the array and all driving circuitry including power and ground connections. The CMOS PLA generator reads two personality tables (AND and OR) and also reads a library of PLA helper components (called &quot;pla_mocmos&quot;) and generates the array. </p>
<h2>ROUTING</h2>
<p> The router is able to do river routing, maze routing, and simple facet stitching (the explicit wiring of implicitly connected nodes that abut). River routing runs a bus of wires between the two opposite sides of a routing channel. The connections on each side must be in a line so that the bus runs between two parallel sets of points. You must use the Unrouted arc from the Generic technology to indicate the ports to be connected. The river router can also connect wires to the perpendicular sides of the routing channel if one or more Unrouted wires cross these sides. </p>
<p> There are two stitching modes: auto stitching and mimic stitching. In auto stitching, all ports that physically touch will be stitched. Mimic stitching watches arcs that are created by the user and adds similar ones at other places in the facet. </p>
<h2>NETWORK COMPARISON</h2>
<p> The network maintainer tool is able to compare the networks in the two facets being displayed on the screen. Once compared, nodes in one facet can be equated with nodes in the other. If the two networks are automorphic or otherwise difficult to distinguish, equivalence information can be specified prior to comparison by selecting a component in the first facet then selecting a component in the second facet. </p>
<h2>AUTHOR</h2>
<pre>
Steven M. Rubin
   Static Free Software
   4119 Alpine Road
   Portola Valley, Ca 94028
Also a cast of thousands:
   Philip Attfield (Queens University): Polygon merging, facet dates
   Ron Bolton (University of Saskatchewan): Miscellaneous help
   Mark Brinsmead (Calgary): Apollo porting
   Stefano Concina (Schlumberger): Polygon clipping
   Peter Gallant (Queen's University): ALS simulation
   T. J. Goodman (University of Canterbury) TEXSIM simulation
   D. Guptill (Technical University of Nova Scotia): X-window interface
   Robert Hon (Columbia University): CIF input
   Sundaravarathan Iyengar (Case Western Reserve University): nMOS PLA generator
   Allan Jost (Technical University of Nova Scotia): X-window interface
   Wallace Kroeker (University of Calgary): Digital filter technology, CMOS PLA generator
   Andrew Kostiuk (Queen's University): QUISC 1.0 Silicon compiler
   Glen Lawson (S-MOS Systems): GDS-II input
   David Lewis (University of Toronto): Short circuit checker
   John Mohammed (Schlumberger): Miscellaneous help
   Mark Moraes (University of Toronto): X-window interface
   Sid Penstone (Queens University): many technologies, GDS-II output, SPICE improvements, SILOS simulation, GENERIC simulation
   J. P. Polonovski (Ecole Polytechnique, France): Memory management improvement
   Kevin Ryan (Technical University of Nova Scotia): X-window interface
   Nora Ryan (Schlumberger): Technology translation, Compaction
   Brent Serbin (Queen's University): ALS Simulator
   Lyndon Swab (Queen's University): Northern Telecom CMOS technologies
   Brian W. Thomson (University of Toronto): Mimic stitcher, RSIM interface
   Burnie West (Schlumberger): Network maintainer help, bipolar technology
   Telle Whitney (Schlumberger): River router
   Rob Winstanley (University of Calgary): CIF input, RNL interface
   Russell Wright (Queen's University): Lots of help
   David J. Yurach (Queen's University): QUISC 2.0 Silicon compiler
</pre>
<h2>SEE ALSO</h2>
<p> Rubin, Steven M., &quot;A General-Purpose Framework for CAD Algorithms&quot;, <i>IEEE Communications</i>, Special Issue on Communications and VLSI, May 1991.<br />
 Rubin, Steven M., <i>Computer Aids for VLSI Design</i>, Addison-Wesley, Reading, Massachusetts, 1987.<br />
 Rubin, Steven M., &quot;An Integrated Aid for Top-Down Electrical Design&quot;, <i>Proceedings, VLSI &#8217;83</i> (Anceau and Aas, eds.), North Holland, Amsterdam, 1983.<br />
 Mead, C. and Conway, L., <i>Introduction to VLSI Systems</i>, Addison-Wesley, 1980.<br />
 Electrical User&#8217;s Guide.<br />
 Electric Internals manual. </p>
<h2>FILES</h2>
<table>
<tr VALIGN=top>
<td>~/.cadrc</td>
<td>Personal startup file
</td>
</tr>
<tr VALIGN=top>
<td>~/electric.log</td>
<td>Session logging file
</td>
</tr>
<tr VALIGN=top>
<td>*.elib</td>
<td>Binary input/output files
</td>
</tr>
<tr VALIGN=top>
<td>*.txt</td>
<td>Text input/output files
</td>
</tr>
<tr VALIGN=top>
<td>*.cif</td>
<td>CIF input/output files
</td>
</tr>
<tr VALIGN=top>
<td>*.pla</td>
<td>PLA personality input files
</td>
</tr>
<tr VALIGN=top>
<td>*.map</td>
<td>Color map files
</td>
</tr>
<tr VALIGN=top>
<td>*.mac</td>
<td>Macro files
</td>
</tr>
<tr VALIGN=top>
<td>*.sim</td>
<td>ESIM, RSIM, RNL, and COSMOS simulation output
</td>
</tr>
<tr VALIGN=top>
<td>rsim.in</td>
<td>RSIM simulation binary output
</td>
</tr>
<tr VALIGN=top>
<td>rnl.in</td>
<td>RNL simulation binary output
</td>
</tr>
<tr VALIGN=top>
<td>*.spi</td>
<td>SPICE simulation output
</td>
</tr>
<tr VALIGN=top>
<td>*.ver</td>
<td>VERILOG simulation output
</td>
</tr>
<tr VALIGN=top>
<td>*.ntk</td>
<td>MOSSIM simulation output
</td>
</tr>
<tr VALIGN=top>
<td>*.sil</td>
<td>SILOS simulation output
</td>
</tr>
<tr VALIGN=top>
<td>*.tdl</td>
<td>TEXSIM simulation output
</td>
</tr>
<tr VALIGN=top>
<td>*.pal</td>
<td>ABLE PAL simulation output
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td>
</td>
</tr>
</table>
<h2>Index</h2>
