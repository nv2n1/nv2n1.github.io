---
title: "ext2sim(1)"
name: "ext2sim"
section: "1"
letter: "e"
url: "/docs/linux/man/1-ext2sim/"
description: "ext2sim – convert hierarchical"
---

<h2 class="name">NAME</h2>
<p> ext2sim &#8211; convert hierarchical <i></p>
<p><a href="/docs/linux/man/5-ext/">ext</a></i>(5) extracted-circuit files to flat <i><a href="/docs/linux/man/5-sim/">sim</a></i>(5) files</p>
<h2>SYNOPSIS</h2>
<p> <code>ext2sim</code> [ <code>-a</code> <i>aliasfile</i> ] [ <code>-l</code> <i>labelsfile</i> ] [ <code>-o</code> <i>simfile</i> ] [ <code>-A</code> ] [ <code>-B</code> ] [ <code>-F</code> ] [ <code>-L</code> ] [ <code>-t</code> ] [ <i>extcheck-options</i> ] [ <i>-y num</i> ] [ <i>-f mit|lbl|su</i> ] [ <i>-J hier|flat</i> ] [ <i>-j device:sdRclass[/subRclass]/defaultSubstrate</i> ] <i>root</i> </p>
<h2>DESCRIPTION</h2>
<p> Ext2sim will convert an extracted circuit from the hierarchical <i><a href="/docs/linux/man/5-ext/">ext</a></i>(5) representation produced by Magic to the flat <i><a href="/docs/linux/man/5-sim/">sim</a></i>(5) representation required by many simulation tools. The root of the tree to be extracted is the file <i>root</i><code>.ext</code>; it and all the files it references are recursively flattened. The result is a single, flat representation of the circuit that is written to the file <i>root</i><code>.sim</code>, a list of node aliases written to the file <i>root</i><code>.al</code>, and a list of the locations of all nodenames in CIF format, suitable for plotting, to the file <i>root</i><code>.nodes</code>. The file <i>root</i><code>.sim</code> is suitable for use with programs such as <i><a href="/docs/linux/man/1-crystal/">crystal</a></i>(1), <i><a href="/docs/linux/man/1-esim/">esim</a></i>(1), or <i><a href="/docs/linux/man/1-sim2spice/">sim2spice</a></i>(1). </p>
<p> The following options are recognized:</p>
<dl>
<dt><code>-a&nbsp;<wbr></code><i>aliasfile</i></p>
<dd> Instead of leaving node aliases in the file <i>root</i><code>.al</code>, leave it in <i>aliasfile</i>.</p>
<dt><code>-l&nbsp;<wbr></code><i>labelfile</i></p>
<dd> Instead of leaving a CIF file with the locations of all node names in the file <i>root</i><code>.nodes</code>, leave it in <i>labelfile</i>.</p>
<dt><code>-o&nbsp;<wbr></code><i>outfile</i></p>
<dd> Instead of leaving output in the file <i>root</i><code>.sim</code>, leave it in <i>outfile</i>.</p>
<dt><code>-A</code></p>
<dd> Don&#8217;t produce the aliases file.</p>
<dt><code>-B</code></p>
<dd> Don&#8217;t output transistor or node attributes in the <code>.sim</code> file. This option will also disable the output of information such as the area and perimeter of source and drain diffusion and the fet substrate. For compatibitlity reasons the latest version of ext2sim outputs this information as node attibutes. This option is necessary when preparing input for programs that don&#8217;t know about attributes, such as <i><a href="/docs/linux/man/1-sim2spice/">sim2spice</a></i>(1) (which is actually made obsolete by <i><a href="/docs/linux/man/1-ext2spice/">ext2spice</a></i>(1), anyway), or <i><a href="/docs/linux/man/1-rsim/">rsim</a></i>(1).</p>
<dt><code>-F</code></p>
<dd> Don&#8217;t output nodes that aren&#8217;t connected to fets (floating nodes).</p>
<dt><code>-L</code></p>
<dd> Don&#8217;t produce the label file.</p>
<dt><code>-t</code><i>char</i></p>
<dd> Trim characters from node names when writing the output file. <i>Char</i> should be either &quot;#&quot; or &quot;!&quot;. The option may be used twice if both characters are desired.</p>
<dt><code>-f </code><i>MIT|LBL|SU</i></p>
<dd> Select the output format. MIT is the traditional <i><a href="/docs/linux/man/5-sim/">sim</a></i>(5) format. LBL is a variant of it understood by <i><a href="/docs/linux/man/1-gemini/">gemini</a></i>(1) which includes the substrate connection as a fourth terminal before length and width. SU is the internal Stanford format which is described also in <i><a href="/docs/linux/man/5-sim/">sim</a></i>(5) and includes areas and perimeters of fet sources, drains and substrates.</p>
<dt><code>-y </code><i>num</i></p>
<dd> Select the precision for outputing capacitors. The default is 1 which means that the capacitors will be printed to a precision of .1 fF.</p>
<dt><code>-J </code><i>hier|flat</i></p>
<dd> Select the source/drain area and perimeter extraction algorithm. If <i>hier</i> is selected then the areas and perimeters are extracted <i>only within each subcell</i>. For each fet in a subcell the area and perimeter of its source and drain within this subcell are output. If two or more fets share a source/drain node then the total area and perimeter will be output in only one of them and the other will have 0. If <i>flat</i> is selected the same rules apply only that the scope of search for area and perimeter is the whole netlist. In general <i>flat</i> (which is the default) will give accurate results (it will take into account shared sources/drains) but hier is provided for backwards compatibility with version 6.4.5. On top of this selection you can individually control how a terminal of a specific fet will be extracted if you put a source/drain attribute. <i>ext:aph</i> makes the extraction for that specific terminal hierarchical and <i>ext:apf</i> makes the extraction flat (see the magic tutorial about attaching attribute labels). Additionaly to ease extraction of bipolar transistors the gate attribute <i>ext:aps</i> forces the output of the substrate area and perimeter for a specific fet (in flat mode only).</p>
<dt><code>-j </code><i>device:sdRclass[/subRclass]/defaultSubstrate</i></p>
<dd> Gives ext2sim information about the source/drain resistance class of the fet type <i>device</i>. Makes <i>device</i> to have <i>sdRclass</i> source drain resistance class, <i>subRclass</i> substrate (well) resistance class and the node named <i>defaultSubstrate</i> as its default substrate. The defaults are nfet:0/Gnd and pfet:1/6/Vdd which correspond to the MOSIS technology file but things might vary in your site. Ask your local cad administrator. </p>
</dl>
<p> The way the extraction of node area and perimeter works in magic the total area and perimeter of the source/drain junction is summed up on a single node. That is why all the junction areas and perimeters are summed up on a single node (this should not affect simulation results however). </p>
<p> <i>Special care must be taken when the substrate of a fet is tied to a node other than the default substrate</i> (eg in a bootstraping charge pump). To get the correct substrate info in these cases the fet(s) with separate wells should be in their own separate subcell with ext:aph attributes attached to their sensitive terminals (also all the transistors which share sensistive terminals with these should be in another subcell with the same attributes). </p>
<p> In addition, all of the options of <i><a href="/docs/linux/man/1-extcheck/">extcheck</a></i>(1) are accepted. </p>
<h2>SCALING AND UNITS</h2>
<p> If all of the <code>.ext</code> files in the tree read by <i>ext2sim</i> have the same geometrical scale (specified in the <code>scale</code> line in each <code>.ext</code> file), this scale is reflected through to the output, resulting in substantially smaller <code>.sim</code> files. Otherwise, the geometrical unit in the output <code>.sim</code> file is a centimicron. </p>
<p> Resistance and capacitance are always output in ohms and femptofarads, respectively. </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-extcheck/">extcheck</a>(1), <a href="/docs/linux/man/1-ext2dlys/">ext2dlys</a>(1), <a href="/docs/linux/man/1-ext2spice/">ext2spice</a>(1), <a href="/docs/linux/man/1-magic/">magic</a>(1), <a href="/docs/linux/man/1-rsim/">rsim</a>(1), <a href="/docs/linux/man/5-ext/">ext</a>(5), <a href="/docs/linux/man/5-sim/">sim</a>(5) </p>
<h2>AUTHOR</h2>
<p> Walter Scott additions/fixes by Stefanos Sidiropoulos. </p>
<h2>BUGS</h2>
<p> Transistor gate capacitance is typically not included in node capacitances, as most analysis tools compute the gate capacitance directly from the gate area. The <code>-c</code> flag therefore provides a limit only on non-gate capacitance. The areas and perimeters of fet sources and drains work only with the simple extraction algorith and not with the extresis flow. So you have to model them as linear capacitors (create a special extraction style) if you want to extract parasitic resistances with extresis. </p>
<h2>Index</h2>
