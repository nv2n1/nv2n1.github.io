---
title: "fig2mpdf(1)"
name: "fig2mpdf"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fig2mpdf/"
description: "fig2mpdf – creation of multilayer pdf or eps figures from fig files using latex for typesetting"
---

<h2 class="name">NAME</h2>
<p> fig2mpdf &#8211; creation of multilayer pdf or eps figures from fig files using latex for typesetting </p>
<h2>SYNOPSIS</h2>
<p> <code>fig2mpdf</code> [<i>OPTION</i>]&#8230; <i>FILE</i></p>
<h2>DESCRIPTION</h2>
<p> This tool can create pdf or eps figures using fig files as source. For beamer presentations, for example, you can use the multilayer mode to create multiple figures that can be overlayed to get a dynamic figure. For proper appearance you can use latex to typeset some or all texts, possibly containing formulas. </p>
<p> The default interpretation of the given fig <i>FILE</i> depends on its suffix.</p>
<dl>
<dt><i>fig</i></p>
<dd> Normal conversion of a fig file. All texts are interpreted as postscript texts and all elements of the figure are included in the resulting figure.</p>
<dt><i>lfig</i></p>
<dd> LaTeX interpretation of the file. All texts of the input file that have the special bit set are typeset by pdflatex resp. latex (see: Option <code>-|+l</code>).</p>
<dt><i>mfig</i></p>
<dd> Multilayer file interpretation. Depending on the used depths of the figure it is split into multiple parts. For each part an output file is created (see: section <code>MultiLayerOutput</code>).</p>
<dt><i>mlfig</i> or <i>lmfig</i></p>
<dd> Combination of multilayer and LaTeX interpretation of the input (see: Suffix <i>lfig</i> and <i>mfig</i>).</dl>
<p> The default interpretation of the input can be changed by using the options below.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-e</code></p>
<dd> produce an eps output file. Instead of creating a pdf file (the default) an eps figure is produced.</p>
<dt><code>-|+l</code></p>
<dd> force calling (pdf)latex (-) or do not use (pdf)latex (+) for typesetting the text marked with the special flag. With this option you can change the default behavior given by the input file suffix.</p>
<dt><code>-|+m</code></p>
<dd> force set (-) or unset (+) the multilayer interpretation (see: <code>MultiLayerOutput</code> below) which was previously set by the input file suffix.</p>
<dt><code>-p</code> <i>ranges</i></p>
<dd> explicitly set the ranges of depths for splitting the input figure in multilayer mode. <i>ranges</i> is a colon separated list of ranges of the form <i>upper-lower</i> or <i>depth</i> where <i>upper</i> is the top and <i>lower</i> the bottom depth in the range. If you use the <i>depth</i> form the range consist of just that depth.</p>
<dt><code>-i</code></p>
<dd> include the the bottommost range (that is, the one with the highest depth) into all output figures. This is for compatibility to older versions of this tool.</p>
<dt><code>-I</code></p>
<dd> turn on pyramid mode. The figure of a corresponding range in multilayer mode includes all lower ranges too.</p>
<dt><code>-g</code> <i>gapwidth</i></p>
<dd> set the allowed gapwidth between two used depths to decide if these depths should be grouped together in one range. With this option you get more flexibility to insert objects with new depths. The default width is zero (no gap = consecutively numbered depths are grouped together).</p>
<dt><code>-s</code> <i>style</i></p>
<dd> replace the default style for selecting a font family in LaTeX mode. If this option is omitted the style `times&#8217; is set by default.</p>
<dt><code>-H</code> <i>header</i></p>
<dd> replace the default header sequence for creating temporary LaTeX documents in LaTeX mode. To get maximum flexibility you can set the entire document header in the file <i>header</i> (see: <code>Customized Headers</code> below).</p>
<dt><code>-G</code></p>
<dd> in multilayer mode change the default output file pattern to the PDF format which is &lt;name&gt;.page&lt;no&gt;.&lt;ext&gt;</p>
<dt><code>-v</code></p>
<dd> be verbose and print out all executed commands</p>
<dt><code>-V</code></p>
<dd> print out the version of <code>fig2mpdf</code></dl>
<h2>MultiLayerOutput</h2>
<p> In xfig you can assign an individual depth to all objects of the figure. These depths are normally used to determine the order of printing the objects. <code>fig2mpdf</code> uses these depths to group the objects into ranges in automatic mode (if the ranges option is omitted). In the list of used depths, consecutively numbered depths are grouped into one range. That is, all gaps between used depths are used to logically split the figure. With <code>-g</code> you can set the gapwidth which doesn&#8217;t split the figure (default: zero). </p>
<p> The resulting list of ranges determines the number of output files. In default mode all objects with depths assigned to one range are collected and put into the corresponding output file. The contents of the output files can be changed with the two Options <code>-i</code> and <code>-I</code>. </p>
<p> The <code>-i</code> option reduces the number of output files by one. The bottommost range, that is the range which consist of the highest depths of the figure, is included into all output files. </p>
<p> In pyramid mode, activated by the option <code>-I</code>, the output files contain additionally all lower ranges. With this mode you can get stand alone figures that don&#8217;t have to be overlayed to have meaningful content. </p>
<p> <code>Example 1</code> </p>
<p> Assume that you have a fig file <i>foo.fig</i> which contains the three ranges <i>230-233,</i> <i>455-460</i> and <i>499-500.</i> </p>
<p> With no options set you get three output files, one per range. But if you set the <code>-i</code> option you get the following two files where the bottommost range is included in both of the files: </p>
<p>&nbsp;<wbr>&nbsp;<i>foo-0.pdf</i>&nbsp;with ranges&nbsp;<i>455-460</i>&nbsp;and&nbsp;<i>499-500</i> </p>
<p>&nbsp;<wbr>&nbsp;<i>foo-1.pdf</i>&nbsp;with ranges&nbsp;<i>230-233</i>&nbsp;and&nbsp;<i>499-500</i>. </p>
<p> <code>Example 2</code> </p>
<p> The pyramid mode, activated by the option <code>-I</code>, will produce the following files from the source file of <code>Example 1</code>: </p>
<p>&nbsp;<wbr>&nbsp;<i>foo-0.pdf</i>&nbsp;with ranges&nbsp;<i>499-500</i> </p>
<p>&nbsp;<wbr>&nbsp;<i>foo-1.pdf</i>&nbsp;with ranges&nbsp;<i>455-460</i>&nbsp;and&nbsp;<i>499-500</i> </p>
<p>&nbsp;<wbr>&nbsp;<i>foo-2.pdf</i>&nbsp;with ranges&nbsp;<i>230-233</i>,&nbsp;<i>455-460</i>&nbsp;and&nbsp;<i>499-500</i>. </p>
<p> <code>Example 3</code> </p>
<p> If both options are set you will get just two files with the following contents: </p>
<p>&nbsp;<wbr>&nbsp;<i>foo-0.pdf</i>&nbsp;with ranges&nbsp;<i>455-460</i>&nbsp;and&nbsp;<i>499-500</i> </p>
<p>&nbsp;<wbr>&nbsp;<i>foo-1.pdf</i>&nbsp;with ranges&nbsp;<i>230-233</i>,&nbsp;<i>455-460</i>&nbsp;and&nbsp;<i>499-500</i>. </p>
<h2>Customized Headers</h2>
<p> For various reasons you might want to change the standard latex generation, e.g., if you want to change the default font family. The following example represents a valid header file. </p>
<p> The usage of this example file changes the font family to sans serif and adds an additional search path for includegraphics to the `figures&#8217; subdirectory. </p>
<p>&nbsp;<wbr>&nbsp;\documentclass{article} </p>
<p>&nbsp;<wbr>&nbsp;
