---
title: "v_sim(1)"
name: "v_sim"
section: "1"
letter: "v"
url: "/docs/linux/man/1-v_sim/"
description: "v_sim – a GTK program for 3D visualisation of atomic systems"
---

<h2 class="name">NAME</h2>
<p> v_sim &#8211; a GTK program for 3D visualisation of atomic systems </p>
<h2>SYNOPSIS</h2>
<p> <code>v_sim</code> <code>[-e</code> <i>file</i> <code>]</code> <code>[-r</code> <i>file</i> <code>]</code> <code>[-h</code> <code>]</code> <code>[-g</code> <i>&lt;w&gt;x&lt;h&gt;</i> <code>]</code> <code>[-s</code> <i>file</i> <code>]</code> <code>[-m</code> <i>id</i> <code>]</code> <code>[-a</code> <code>]</code> <code>[-c</code> <i>file</i> <code>]</code> <code>[-u</code> <i>l:m:n</i> <code>]</code> <code>[-d</code> <i>id</i> <code>]</code> <code>[-t</code> <i>x:y:z</i> <code>]</code> <code>[-x</code> <i>x:y:z</i> <code>]</code> <code>[-p</code> <i>file</i> <code>]</code> <code>[-f</code> <i>file</i> <code>]</code> <code>[-v</code> <i>v[:v]</i> <code>]</code> <code>[-i</code> <i>file</i> <code>]</code> <code>[-b</code> <i>id[:id]</i> <code>]</code> <code>[&#8211;log-scale</code> <i>id</i> <code>]</code> <code>[-n</code> <i>val</i> <code>]</code> <code>[&#8211;color-iso-lines</code> <i>[R:G:B] or auto</i> <code>]</code> <code>[&#8211;fit-to-box</code> <i>val</i> <code>]</code> <code>[&#8211;bg-image</code> <i>file</i> <code>]</code> <code>[-o</code> <i>id=value</i> <code>]</code> <code>[-w</code> <i>mode</i> <code>]</code> <code>[&#8211;i-set</code> <i>i</i> <code>]</code> <code>[&#8211;value-file</code> <i>file</i> <code>]</code> <code>[&#8211;map-precision</code> <i>prec</i> <code>]</code> <code>[&#8211;map-clamp</code> <i>min:max or auto</i> <code>]</code> <code>[&#8211;introspect-dump</code> <i>fileToDump</i> <code>]</code> <code>[&#8211;color-clamp</code> <i>col#min:max or auto</i> <code>]</code> <code>[&#8211;scaling-column</code> <i>id</i> <code>]</code> <code>[</code> <i>fileToRender</i> <code>]</code> </p>
<p> This manual page documents briefly the <code>v_sim</code> commands. It is a software to visualise atomic structures with OpenGl rendering.</p>
<h2>OPTIONS</h2>
<p> This program follows the usual GNU command line syntax, with long options starting with two dashes (`-&#8216;). </p>
<p> A complete list of options is included below.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</p>
<dl>
<dt><code>-e, &#8211;export file (from v3.0.0)</code></p>
<dd> make an image from the fileToRender argument. The format is specified through the extension of the argument or by the -o fileFormatId=id option (get the id of available file formats with -o list). </p>
<dt><code>-r, &#8211;resources file (from v3.4.0)</code></p>
<dd> load the given resources file on startup instead of looking for a valid resources file in the standard locations. </p>
<dt><code>-h, &#8211;help (from v3.0.0)</code></p>
<dd> show this little help. </p>
<dt><code>-g, &#8211;geometry &lt;w&gt;x&lt;h&gt; (from v3.0.0)</code></p>
<dd> specify the size of the rendering window, the size argument must have the following format: &lt;width&gt;x&lt;height&gt; with positive non null values. (Default value: 600&#215;600) </p>
<dt><code>-s, &#8211;spin-file file (from v3.1.0)</code></p>
<dd> use the given argument as a spin indicator. If this option is used, V_Sim switches automatically to spin rendering whatever method is specified in the parameter file. </p>
<dt><code>-m, &#8211;hiding-mode id (from v3.2.0)</code></p>
<dd> policy used to show or not null modulus spins possible values are positives. (Default value: 0) </p>
<dt><code>-a, &#8211;spin-and-atomic (from v3.3.0)</code></p>
<dd> always draws atomic rendering on node position in addition to spin rendering. </p>
<dt><code>-c, &#8211;colorize file (from v3.1.0)</code></p>
<dd> the argument fileToRender must be called, then the given file of the option is used to colorize the elements. </p>
<dt><code>-u, &#8211;use-column l:m:n (from v3.1.0)</code></p>
<dd> it specifies the columns to use from the data file for the three colour channels [l;m;n]. Columns are counted from 1. Use -3, -2, -1 and 0 to use the special values, constant 1, coord. x, coord. y, and coord. z, respectively. </p>
<dt><code>-d, &#8211;color-preset id (from v3.1.0)</code></p>
<dd> this option can be used with the &#8216;&#8211;colorize&#8217; one or the &#8216;&#8211;build-map&#8217; one. It chooses a preset color scheme. The id argument is an integer that corresponds to a defined color shade (ranging from 0). </p>
<dt><code>-t, &#8211;translate x:y:z (from v3.3.0)</code></p>
<dd> a file must be loaded. It applies the given translations to the loaded file. The units are those of the file. This is available for periodic file formats only. </p>
<dt><code>-x, &#8211;expand x:y:z (from v3.4.0)</code></p>
<dd> a file must be loaded. It applies the given expansion to the loaded file. The values are given in box coordinates. This is available for periodic file formats only. </p>
<dt><code>-p, &#8211;planes file (from v3.2.0)</code></p>
<dd> the argument fileToRender must be called, then the given file of the option is parsed as a list of planes and they are rendered. </p>
<dt><code>-f, &#8211;scalar-field file (from v3.3.0)</code></p>
<dd> the argument fileToRender must be called, then the given file of the option is parsed as a scalar field and loaded. </p>
<dt><code>-v, &#8211;iso-values v[:v] (from v3.3.0)</code></p>
<dd> must be used with the &#8216;&#8211;scalar-field&#8217; option, then the given surfaces are built and rendered. If a name is appended to a value using &#8216;#&#8217; as a separator, this name is used as the name for the iso-surface (i.e. 0.25#Blue). </p>
<dt><code>-i, &#8211;iso-surfaces file (from v3.2.0)</code></p>
<dd> the argument fileToRender must be given, then the given file of the option is parsed and surfaces are rendered. </p>
<dt><code>-b, &#8211;build-map id[:id] (from v3.4.0)</code></p>
<dd> the argument fileToRender must be given, as the &#8216;&#8211;planes&#8217;, &#8216;&#8211;color-preset&#8217; and &#8216;&#8211;scalar-field&#8217; options used, then the given plane &#8216;id&#8217; is replaced by a coloured map using given scalar field and shade. &#8216;id&#8217; ranges from 0. If several ids are given, several maps are built. </p>
<dt><code>&#8211;log-scale id (from v3.4.0)</code></p>
<dd> select the scaling method to use with gradients (0: linear, 1: log scaled and 2 is zero-centred log scale), default is linear scale. </p>
<dt><code>-n, &#8211;n-iso-lines val (from v3.4.0)</code></p>
<dd> when positive, val isolines are plotted on the coloured map. </p>
<dt><code>&#8211;color-iso-lines [R:G:B] or auto (from v3.5.0)</code></p>
<dd> when given, generated iso-lines are colourised [R:G:B] or auto with the values. The specific value &#8216;auto&#8217; will produced iso-lines in inversed colours. (Default value: [0:0:0]) </p>
<dt><code>&#8211;fit-to-box val (from v3.3.0)</code></p>
<dd> if val is not TRUE, the surfaces use their own bounding box. (Default value: TRUE) </p>
<dt><code>&#8211;bg-image file (from v3.4.0)</code></p>
<dd> draw the given image on the background. </p>
<dt><code>-o, &#8211;option id=value (from v3.3.0)</code></p>
<dd> this is a generic way to give extended option. to V_Sim. As much as -o can be used. Each one store a key and its value (boolean, integer or float). </p>
<dt><code>-w, &#8211;window-mode mode (from v3.5.0)</code></p>
<dd> used to choose the windowing mode. By default the command panel and the rendering window are separated. In the &#8216;oneWindow&#8217; mode they are joined. In the &#8216;renderOnly&#8217; mode, the command panel is not used. (Default value: classic) </p>
<dt><code>&#8211;i-set i (from v3.5.0)</code></p>
<dd> this flag is used to choose the id of the loaded file if the format has support for multiple ids in one file (see XYZ format or -posi.d3 ones). (Default value: 0) </p>
<dt><code>&#8211;value-file file (from v3.5.0)</code></p>
<dd> specify an XML file with some value information for V_Sim, like a list of planes, highlighted nodes&#8230; It replaces and extend the previous &#8211;planes option. </p>
<dt><code>&#8211;map-precision prec (from v3.5.0)</code></p>
<dd> Give the precision in percent to render the coloured map. (Default value: 100) </p>
<dt><code>&#8211;map-clamp min:max or auto (from v3.6.0)</code></p>
<dd> Set the minimum and maximum values for the coloured map rendering. (Default value: auto) </p>
<dt><code>&#8211;introspect-dump fileToDump (from v3.6.0)</code></p>
<dd> Dump object signals and properties for introspection. </p>
<dt><code>&#8211;color-clamp col#min:max or auto (from v3.7.0)</code></p>
<dd> Range to adjust values into for colourisation. col specifiesthe column to apply the range to. Use -2, -1 and 0 for x, yand z directions respectively. (Default value: auto) </p>
<dt><code>&#8211;scaling-column id (from v3.7.0)</code></p>
<dd> used with a data file (see -c), it specifies the column id to be used to scale the nodes. </p>
</dl>
<h2>FILES</h2>
<p> <i>/usr/share/v_sim/v_sim.res</i> specify all rendering informations from position of the camera to colour of the elements.<br />
 <i>/usr/share/v_sim/v_sim.par</i> specify all interface and non-rendering options such as the positions of the panels.<br />
 <i>~/$XDG_CONFIG_DIR/v_sim</i> a directory where overloading <code>v_sim.res</code> and <code>v_sim.par</code> can be put.</p>
<h2>AUTHOR</h2>
<p> V_Sim was written by Luc Billard, Damien Caliste, Olivier D&#8217;Astier Aurélien Lherbier, Jérémy Blanc, Simon Planès, Thomas Jourdan and Yoann Ratao. </p>
<p> This manual page was written by Damien Caliste &lt;damien.caliste [at] cea.fr&gt;.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp; </p>
<h2>Index</h2>
