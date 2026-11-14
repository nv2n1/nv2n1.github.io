---
title: "opaxmlgenerate(8)"
name: "opaxmlgenerate"
section: "8"
letter: "o"
url: "/docs/linux/man/8-opaxmlgenerate/"
description: "opaxmlgenerate"
---

<p>opaxmlgenerate </p>
<p> <code>(Linux)</code> Takes comma-separated-values (CSV) data as input and generates sequences of XML containing user-specified element names and element values within start and end tag specifications. Use this tool to create an XML representation of fabric data from its CSV form.</p>
<h2>Syntax</h2>
<p>opaxmlgenerate [-v] [-d <i>delimiter</i>] [-i <i>number</i>] [-g <i>element</i>] [-h <i>element</i>] [-e <i>element</i>] [-X <i>input_file</i>] [-P <i>param_file</i>]</p>
<h2>Options</h2>
<dl>
<dt>-g/&#8211;generate <i>element</i></p>
<dd>Generates value for <i>element</i> using value in next field from the input file. Can be used multiple times on the command line. Values are assigned to elements in order. </p>
<dt>-h/&#8211;header <i>element</i></p>
<dd>Name of the XML element that is the enclosing header start tag. </p>
<dt>-e/&#8211;end <i>element</i></p>
<dd>Name of the XML element that is the enclosing header end tag. </p>
<dt>-d/&#8211;delimit <i>delimiter</i></p>
<dd>Specifies the delimiter character that separates values in the input file. Default is semicolon. </p>
<dt>-i/&#8211;indent <i>number</i></p>
<dd>Number of spaces to indent each level of XML output. Default is 0. </p>
<dt>-X/&#8211;infile <i>input_file</i></p>
<dd>File to read delimited input data from. One record per line with fields in each record separated by the specified delimiter. </p>
<dt>-P/&#8211;pfile <i>param_file</i></p>
<dd>Uses input command line options (parameters) from param_file. </p>
<dt>-v/&#8211;verbose</p>
<dd>Produces verbose output. Includes output progress reports during extraction. </p>
</dl>
<h2>Details</h2>
<p>opaxmlgenerate takes the CSV data from an input file. It generates fragments of XML, and in combination with a script, can be used to generate complete XML sequences. opaxmlgenerate does not use nor require a connection to an Intel(R) Omni-Path Fabric. </p>
<p> opaxmlgenerate reads CSV element values and applies element (tag) names to those values. The element names are supplied as command line options to the tool and constitute a template that is applied to the input. </p>
<p> Element names on the command line are of three (3) types, distinguished by their command line option &#8211; Generate, Header, and Header_End. The Header and Header_End types together constitute enclosing element types. Enclosing elements do not contain a value, but serve to separate and organize Generate elements. </p>
<p> Generate elements, along with a value from the CSV input file, cause XML in the form of #8217lt;element_name&gt; <i>value</i>&lt;/element_name&gt; to be generated. Generate elements are normally the majority of the XML output since they specify elements containing the input values. Header elements cause an XML header start tag of the form: &lt;element_name&gt; to be generated. Header_End elements cause an XML header end tag of the form &lt;/element_name&gt; to be generated. Output of enclosing elements is controlled entirely by the placement of those element types on the command line. opaxmlgenerate does <code>not</code> check for matching start and end tags or proper nesting of tags. </p>
<p> Options (parameters) to opaxmlgenerate can be specified on the command line, with a parameter file, or both. A parameter file is specified with -P <i>param_file</i>. When a parameter file specification is encountered on the command line, option processing on the command line is suspended, the parameter file is read and processed entirely, and then command line processing is resumed. Option syntax within a parameter file is the same as on the command line. Multiple parameter file specifications can be made, on the command line or within other parameter files. At each point that a parameter file is specified, current option processing is suspended while the parameter file is processed, then resumed. Options are processed in the order they are encountered on the command line or in parameter files. A parameter file can be up to 8192 bytes in size and may contain up to 512 parameters.</p>
<h2>Using opaxmlgenerate to Create Topology Input Files</h2>
<p>opaxmlgenerate can be used to create scripts to translate from user-specific format into the opareport topology_input file format. opaxmlgenerate itself works against a CSV style file with one line per record. Given such a file it can produce hierarchical XML output of arbitrary complexity and depth. </p>
<p> The typical flow for a script which translates from a user-specific format into opareport topology_input would be:</p>
<dl>
<dt>&bull;</p>
<dd>As needed, reorganize the data into link and node data CSV files, in a sequencing similar to that used by opareport topology_input. One link record per line in one temporary file, one node record per line in another temporary file and one SM per line in a third temporary file.</p>
<dt>&bull;</p>
<dd>The script must directly output the boilerplate for XML version, etc.</p>
<dt>&bull;</p>
<dd>opaxmlgenerate can be used to output the Link section of the topology_input, using the link record temporary file.</p>
<dt>&bull;</p>
<dd>opaxmlgenerate can be used to output the Node sections of the topology_input using the node record temporary file. If desired, there could be separate node record temporary files for HFIs, Switches, and Routers.</p>
<dt>&bull;</p>
<dd>opaxmlgenerate can be used to output the SM section of the topology_input, if desired.</p>
<dt>&bull;</p>
<dd>The script must directly output the closing XML tags to complete the topology_input file. </p>
</dl>
