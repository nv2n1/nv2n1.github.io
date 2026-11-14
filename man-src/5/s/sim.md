---
title: "sim(5)"
name: "sim"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sim/"
description: "sim – format of .sim files read by esim, crystal, etc."
---

<p>sim &#8211; format of .sim files read by esim, crystal, etc.</p>
<h2>Description</h2>
<p>The simulation tools <i><a href="/docs/linux/man/1-crystal/">crystal</a></i>(1) and <i><a href="/docs/linux/man/1-esim/">esim</a></i>(1) accept a circuit description in <code>.sim</code> format. There is a single <code>.sim</code> file for the entire circuit, unlike Magic&#8217;s <i><a href="/docs/linux/man/5-ext/">ext</a></i>(5) format in which there is a <code>.ext</code> file for every cell in a hierarchical design. A <code>.sim</code> file consists of a series of lines, each of which begins with a key letter. The key letter beginning a line determines how the remainder of the line is interpreted. The following are the list of key letters understood.</p>
<dl>
<dt><code>| units: </code><i>s</i><code> tech: </code><i>tech</i> format: <i>MIT|LBL|SU</i></p>
<dd>If present, this must be the first line in the <code>.sim</code> file. It identifies the technology of this circuit as <i>tech</i> and gives a scale factor for units of linear dimension as <i>s</i>. All linear dimensions appearing in the <code>.sim</code> file are multiplied by <i>s</i> to give centimicrons. The format field signifies the sim variant. MIT and SU are compatible and understood by all tools. LBL is understood only by <a href="/docs/linux/man/1-gemini/">gemini</a>(1).</p>
<dt><i>type g s d l w x y </i><code>g=</code><i>gattrs </i><code>s=</code><i>sattrs </i><code>d=</code><i>dattrs</i></p>
<dd>Defines a transistor of type <i>type</i>. Currently, <i>type</i> may be <code>e</code> or <code>d</code> for NMOS, or <code>p</code> or <code>n</code> for CMOS. The name of the node to which the gate, source, and drain of the transistor are connected are given by <i>g</i>, <i>s</i>, and <i>d</i> respectively. The length and width of the transistor are <i>l</i> and <i>w</i>. The next two tokens, <i>x</i> and <i>y</i>, are optional. If present, they give the location of a point inside the gate region of the transistor. The last three tokens are the attribute lists for the transistor gate, source, and drain. If no attributes are present for a particular terminal, the corresponding attribute list may be absent (i.e, there may be no <code>g=</code> field at all). The attribute lists <i>gattrs</i>, etc. are comma-separated lists of labels. The label names should not include any spaces, although some tools can accept label names with spaces if they are enclosed in double quotes. <code>In version 6.4.5 and later </code> the default format produced by ext2sim is SU. In this format the attribute of the gate starting with S_ is the substrate node of the fet. The attributes of the gate, and source and substrate starting with A_, P_ are the area and perimeter (summed for that node only once) of the source and drain respectively. This addition to the format is backwards compatible.</p>
<dt><code>C </code><i>n1 n2 cap</i></p>
<dd>Defines a capacitor between nodes <i>n1</i> and <i>n2</i>. The value of the capacitor is <i>cap</i> femtofarads. <code>NOTE:</code> since many analysis tools compute transistor gate capacitance themselves from the transistor&#8217;s area and perimeter, the capacitance between a node and substrate (GND!) normally does not include the capacitance from transistor gates connected to that node. If the <code>.sim</code> file was produced by <i><a href="/docs/linux/man/1-ext2sim/">ext2sim</a></i>(1), check the technology file that was used to produce the original <code>.ext</code> files to see whether transistor gate capacitance is included or excluded; see &#8220;Magic Maintainer&#8217;s Manual #2: The Technology File&#8221; for details.</p>
<dt><code>R </code><i>node res</i></p>
<dd>Defines the lumped resistance of node <i>node</i> to be <i>res</i> ohms. This construct is only interpreted by a few programs.</p>
<dt><code>r </code><i>node1 node2 res</i></p>
<dd>Defines an explicit resistor between nodes <i>node1</i> and <i>node2</i> of resistance <i>res</i> ohms. This construct is only interpreted by a few programs.</p>
<dt><code>N </code><i>node darea dperim parea pperim marea mperim</i></p>
<dd>As an alternative to computed capacitances, some tools expect the total perimeter and area of the polysilicon, diffusion, and metal in each node to be reported in the <code>.sim</code> file. The <code>N</code> construct associates diffusion area <i>darea</i> (in square centimicrons) and diffusion perimeter <i>dperim</i> (in centimicrons) with node <i>node</i>, polysilicon area <i>parea</i> and perimeter <i>pperim</i>, and metal area <i>marea</i> and perimeter <i>mperim</i>. <i>This construct is technology dependent and obsolete.</i></p>
<dt><code>A </code><i>node attr</i></p>
<dd>Associates attribute <i>attr</i> for node <i>node</i>. The string <i>attr</i> should contain no blanks.</p>
<dt><code>= </code><i>node1 node2</i></p>
<dd>Each node in a <code>.sim</code> file is named implicitly by having it appear in a transistor definition. All node names appearing in a <code>.sim</code> file are assumed to be distinct. Some tools, such as <i><a href="/docs/linux/man/1-esim/">esim</a></i>(1), recognize aliases for node names. The <code>=</code> construct allows the name <i>node2</i> to be defined as an alias for the name <i>node1</i>. Aliases defined by means of this construct may not appear anywhere else in the <code>.sim</code> file. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-crystal/">crystal</a>(1), <a href="/docs/linux/man/1-esim/">esim</a>(1), <a href="/docs/linux/man/1-ext2sim/">ext2sim</a>(1), <a href="/docs/linux/man/1-sim2spice/">sim2spice</a>(1), <a href="/docs/linux/man/5-ext/">ext</a>(5) </p>
