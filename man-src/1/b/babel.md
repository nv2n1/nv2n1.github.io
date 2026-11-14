---
title: "babel(1)"
name: "babel"
section: "1"
letter: "b"
url: "/docs/linux/man/1-babel/"
description: "babel , obabel – a converter for chemistry and molecular modeling data files"
---

<h2>NAME</h2>
<p> <code>babel , obabel</code> &#8211; a converter for chemistry and molecular modeling data files</p>
<h2>SYNOPSIS</h2>
<p> [-<code>H </code><i>help-options</i> ]<br />
 [<i>OPTIONS</i> ] [-<code>i </code><i>input-type</i> ] <i>infile</i> [-<code>o </code><i>output-type</i> ] <i>outfile</i> </p>
<p><code>obabel</code> [-<code>H </code><i>help-options</i> ]<br />
<code>obabel</code> [<i>OPTIONS</i> ] [-<code>i </code><i>input-type | &#8211;</i><code>: Qo </code><i>SMILES-string Qc </i><i>infile</i> ] [-<code>o </code><i>output-type</i> ] &#8211;<code>O </code><i>outfile</i></p>
<h2>DESCRIPTION</h2>
<p> is a cross-platform program designed to interconvert between many file formats used in molecular modeling and computational chemistry and related areas. </p>
<p> <code>obabel</code> and are slightly different. The first is closer to the normal Unix convention for commandline programs and more flexible when the user needs to specify parameter values on options. With <code>babel</code> this only works when the option is the last on the line; with <code>obabel</code> no such restriction applies. It further has a shortcut for entering SMILES strings, which can be used in place of an input file. </p>
<p> Open Babel is also a complete programmers toolkit for developing chemistry software. For more information, se the Open Babel web pages &lt;<code><a rel="nofollow" href="http://openbabel.org/">http://openbabel.org/</a></code>&gt;.</p>
<h2>OPTIONS</h2>
<p> If only input and output files are given, Open Babel will guess the file type from the filename extension.</p>
<dl>
<dt><code>-: Qo </code><i>SMILES-string Qc </i>Enter SMILES string and use it in place of an input file. The SMILES string</p>
<dd> should be enclosed in quotation marks. More than one can be used, and a molecule title can be included if enclosed in quotes.</p>
<dt><code>-a </code><i>options</i></p>
<dd> Format-specific input options. See &#8211;<code>H </code><i>format-ID </i> for options allowed by a particular format</p>
<dt><code>&#8211;addtotitle</code></p>
<dd> Append text to the current molecule title</p>
<dt><code>&#8211;addformula</code></p>
<dd> Append the molecular formula after the current molecule title</p>
<dt><code>-b</code></p>
<dd> Convert dative bonds: e.g., [N+]([O-])=O to N(=O)=O</p>
<dt><code>-c</code></p>
<dd> Center atomic coordinates at (0,0,0)</p>
<dt><code>-C</code></p>
<dd> Combine molecules in first file with others having the same name</p>
<dt><code>-e</code></p>
<dd> Continue after errors</p>
<dt><code>-d</code></p>
<dd> Delete Hydrogens</p>
<dt><code>&#8212;errorlevel </code><i>2</i></p>
<dd> Filter the level of errors and warnings displayed: </p>
<p>&nbsp;<wbr>1&nbsp;<wbr>=&nbsp;<wbr>critical errors only<br />
&nbsp;<wbr>2&nbsp;<wbr>=&nbsp;<wbr>include warnings too&nbsp;<wbr>(default)<br />
&nbsp;<wbr>3&nbsp;<wbr>=&nbsp;<wbr>include informational messages too<br />
&nbsp;<wbr>4&nbsp;<wbr>=&nbsp;<wbr>include&nbsp;<wbr>&quot;audit log&quot;&nbsp;<wbr>messages of changes to data<br />
&nbsp;<wbr>5&nbsp;<wbr>=&nbsp;<wbr>include debugging messages too</p>
<dt><code>-f </code><i>file &#8230;</i></p>
<dd> For multiple entry input, start import with molecule # as the first entry</p>
<dt><code>-F</code></p>
<dd> Output the available fingerprint types</p>
<dt><code>-h</code></p>
<dd> Add hydrogens</p>
<dt><code>-H</code></p>
<dd> Output usage information</p>
<dt><code>-H </code><i>format-ID</i></p>
<dd> Output formatting information and options for format specified</p>
<dt><code>-Hall</code></p>
<dd> Output formatting information and options for all formats</p>
<dt><code>-i&lt;format-ID&gt;</code></p>
<dd> Specifies input format, see below for the available formats</p>
<dt><code>-j</code></p>
<dd>
<dt><code>&#8211;join</code></p>
<dd> Join all input molecules into a single output molecule entry</p>
<dt><code>-k</code></p>
<dd> Translate computational chemistry modeling keywords (e.g., GAMESS and Gaussian)</p>
<dt><code>-m</code></p>
<dd> Produce multiple output files, to allow:</p>
<dl>
<dt><code>Splitting one input file &#8211; put each molecule into consecutively</code></p>
<dd> numbered output files</p>
<dt><code>Batch conversion &#8211; convert each of multiple input files into a</code></p>
<dd> specified output format</dl>
<dt><code>-l </code><i>file &#8230;</i></p>
<dd> For multiple entry input, stop import with molecule # as the last entry</p>
<dt><code>-o </code><i>format-ID</i></p>
<dd> Specifies output format, see below for the available formats</p>
<dt><code>-O </code><i>outfile</i></p>
<dd> Specify the output file. This option applies to <code>obabel</code> only.</p>
<dt><code>-p</code></p>
<dd> Add Hydrogens appropriate for pH (use transforms in phmodel.txt)</p>
<dt><code>&#8211;property </code></p>
<dd> Add or replace a property (e.g., in an MDL SD file)</p>
<dt><code>-s </code><i>SMARTS</i></p>
<dd> Convert only molecules matching the SMARTS pattern specified</p>
<dt><code>&#8211;separate</code></p>
<dd> Separate disconnected fragments into individual molecular records</p>
<dt><code>-t</code></p>
<dd> All input files describe a single molecule</p>
<dt><code>&#8211;title </code><i>title</i></p>
<dd> Add or replace molecular title</p>
<dt><code>-x </code><i>options</i></p>
<dd> Format-specific output options. See &#8211;<code>H </code><i>format-ID</i> for options allowed by a particular format</p>
<dt><code>-v </code><i>SMARTS</i></p>
<dd> Convert only molecules <code>NOT</code> matching SMARTS pattern specified</p>
<dt><code>-V</code></p>
<dd> Output version number and exit</p>
<dt><code>-z</code></p>
<dd> Compress the output with gzip</dl>
<h2>FILE FORMATS</h2>
<p> The following formats are currently supported by Open Babel:</p>
<dl>
<dt><code>acr &#8212; Carine ASCI Crystal</code></p>
<dd>
<dt><code>alc &#8212; Alchemy format</code></p>
<dd>
<dt><code>arc &#8212; Accelrys/MSI Biosym/Insight II CAR format [Read-only]</code></p>
<dd>
<dt><code>bgf &#8212; MSI BGF format</code></p>
<dd>
<dt><code>box &#8212; Dock 3.5 Box format</code></p>
<dd>
<dt><code>bs &#8212; Ball and Stick format</code></p>
<dd>
<dt><code>c3d1 &#8212; Chem3D Cartesian 1 format</code></p>
<dd>
<dt><code>c3d2 &#8212; Chem3D Cartesian 2 format</code></p>
<dd>
<dt><code>caccrt &#8212; Cacao Cartesian format</code></p>
<dd>
<dt><code>cache &#8212; CAChe MolStruct format [Write-only]</code></p>
<dd>
<dt><code>cacint &#8212; Cacao Internal format [Write-only]</code></p>
<dd>
<dt><code>can &#8212; Canonical SMILES format</code></p>
<dd>
<dt><code>car &#8212; Accelrys/MSI Biosym/Insight II CAR format [Read-only]</code></p>
<dd>
<dt><code>ccc &#8212; CCC format [Read-only]</code></p>
<dd>
<dt><code>cdx &#8212; ChemDraw binary format [Read-only]</code></p>
<dd>
<dt><code>cdxml &#8212; ChemDraw CDXML format</code></p>
<dd>
<dt><code>cht &#8212; Chemtool format [Write-only]</code></p>
<dd>
<dt><code>cif &#8212; Crystallographic Information File</code></p>
<dd>
<dt><code>cml &#8212; Chemical Markup Language</code></p>
<dd>
<dt><code>cmlr &#8212; CML Reaction format</code></p>
<dd>
<dt><code>com &#8212; Gaussian 98/03 Cartesian Input [Write-only]</code></p>
<dd>
<dt><code>copy &#8212; Copies raw text [Write-only]</code></p>
<dd>
<dt><code>crk2d &#8212; Chemical Resource Kit 2D diagram format</code></p>
<dd>
<dt><code>crk3d &#8212; Chemical Resource Kit 3D format</code></p>
<dd>
<dt><code>csr &#8212; Accelrys/MSI Quanta CSR format [Write-only]</code></p>
<dd>
<dt><code>cssr &#8212; CSD CSSR format [Write-only]</code></p>
<dd>
<dt><code>ct &#8212; ChemDraw Connection Table format </code></p>
<dd>
<dt><code>dmol &#8212; DMol3 coordinates format</code></p>
<dd>
<dt><code>ent &#8212; Protein Data Bank format</code></p>
<dd>
<dt><code>fa &#8212; FASTA format [Write-only]</code></p>
<dd>
<dt><code>fasta &#8212; FASTA format [Write-only]</code></p>
<dd>
<dt><code>fch &#8212; Gaussian formatted checkpoint file format [Read-only]</code></p>
<dd>
<dt><code>fchk &#8212; Gaussian formatted checkpoint file format [Read-only]</code></p>
<dd>
<dt><code>fck &#8212; Gaussian formatted checkpoint file format [Read-only]</code></p>
<dd>
<dt><code>feat &#8212; Feature format</code></p>
<dd>
<dt><code>fh &#8212; Fenske-Hall Z-Matrix format [Write-only]</code></p>
<dd>
<dt><code>fix &#8212; SMILES FIX format [Write-only]</code></p>
<dd>
<dt><code>fpt &#8212; Fingerprint format [Write-only]</code></p>
<dd>
<dt><code>fract &#8212; Free Form Fractional format</code></p>
<dd>
<dt><code>fs &#8212; Open Babel FastSearching database</code></p>
<dd>
<dt><code>fsa &#8212; FASTA format [Write-only]</code></p>
<dd>
<dt><code>g03 &#8212; Gaussian 98/03 Output [Read-only]</code></p>
<dd>
<dt><code>g98 &#8212; Gaussian 98/03 Output [Read-only]</code></p>
<dd>
<dt><code>gam &#8212; GAMESS Output [Read-only]</code></p>
<dd>
<dt><code>gamin &#8212; GAMESS Input [Write-only]</code></p>
<dd>
<dt><code>gamout &#8212; GAMESS Output [Read-only]</code></p>
<dd>
<dt><code>gau &#8212; Gaussian 98/03 Cartesian Input [Write-only]</code></p>
<dd>
<dt><code>gjc &#8212; Gaussian 98/03 Cartesian Input [Write-only]</code></p>
<dd>
<dt><code>gjf &#8212; Gaussian 98/03 Cartesian Input [Write-only]</code></p>
<dd>
<dt><code>gpr &#8212; Ghemical format</code></p>
<dd>
<dt><code>gr96 &#8212; GROMOS96 format [Write-only]</code></p>
<dd>
<dt><code>hin &#8212; HyperChem HIN format</code></p>
<dd>
<dt><code>inchi &#8212; IUPAC InChI [Write-only]</code></p>
<dd>
<dt><code>inp &#8212; GAMESS Input [Write-only]</code></p>
<dd>
<dt><code>ins &#8212; ShelX format [Read-only]</code></p>
<dd>
<dt><code>jin &#8212; Jaguar input format [Write-only]</code></p>
<dd>
<dt><code>jout &#8212; Jaguar output format [Read-only]</code></p>
<dd>
<dt><code>mdl &#8212; MDL MOL format</code></p>
<dd>
<dt><code>mmd &#8212; MacroModel format</code></p>
<dd>
<dt><code>mmod &#8212; MacroModel format</code></p>
<dd>
<dt><code>mol &#8212; MDL MOL format</code></p>
<dd>
<dt><code>mol2 &#8212; Sybyl Mol2 format</code></p>
<dd>
<dt><code>molreport &#8212; Open Babel molecule report [Write-only]</code></p>
<dd>
<dt><code>moo &#8212; MOPAC Output format [Read-only]</code></p>
<dd>
<dt><code>mop &#8212; MOPAC Cartesian format</code></p>
<dd>
<dt><code>mopcrt &#8212; MOPAC Cartesian format</code></p>
<dd>
<dt><code>mopin &#8212; MOPAC Internal</code></p>
<dd>
<dt><code>mopout &#8212; MOPAC Output format [Read-only]</code></p>
<dd>
<dt><code>mpc &#8212; MOPAC Cartesian format</code></p>
<dd>
<dt><code>mpd &#8212; Sybyl descriptor format [Write-only]</code></p>
<dd>
<dt><code>mpqc &#8212; MPQC output format [Read-only]</code></p>
<dd>
<dt><code>mpqcin &#8212; MPQC simplified input format [Write-only]</code></p>
<dd>
<dt><code>nw &#8212; NWChem input format [Write-only]</code></p>
<dd>
<dt><code>nwo &#8212; NWChem output format [Read-only]</code></p>
<dd>
<dt><code>pc &#8212; PubChem format [Read-only]</code></p>
<dd>
<dt><code>pcm &#8212; PCModel format</code></p>
<dd>
<dt><code>pdb &#8212; Protein Data Bank format</code></p>
<dd>
<dt><code>pov &#8212; POV-Ray input format [Write-only]</code></p>
<dd>
<dt><code>pqs &#8212; Parallel Quantum Solutions format</code></p>
<dd>
<dt><code>prep &#8212; Amber Prep format [Read-only]</code></p>
<dd>
<dt><code>qcin &#8212; Q-Chem input format [Write-only]</code></p>
<dd>
<dt><code>qcout &#8212; Q-Chem output format [Read-only]</code></p>
<dd>
<dt><code>report &#8212; Open Babel report format [Write-only]</code></p>
<dd>
<dt><code>res &#8212; ShelX format [Read-only]</code></p>
<dd>
<dt><code>rxn &#8212; MDL RXN format</code></p>
<dd>
<dt><code>sd &#8212; MDL MOL format</code></p>
<dd>
<dt><code>sdf &#8212; MDL MOL format</code></p>
<dd>
<dt><code>smi &#8212; SMILES format</code></p>
<dd>
<dt><code>sy2 &#8212; Sybyl Mol2 format</code></p>
<dd>
<dt><code>tdd &#8212; Thermo format</code></p>
<dd>
<dt><code>test &#8212; Test format [Write-only]</code></p>
<dd>
<dt><code>therm &#8212; Thermo format</code></p>
<dd>
<dt><code>tmol &#8212; TurboMole Coordinate format</code></p>
<dd>
<dt><code>txyz &#8212; Tinker MM2 format [Write-only]</code></p>
<dd>
<dt><code>unixyz &#8212; UniChem XYZ format</code></p>
<dd>
<dt><code>vmol &#8212; ViewMol format</code></p>
<dd>
<dt><code>xed &#8212; XED format [Write-only]</code></p>
<dd>
<dt><code>xml &#8212; General XML format [Read-only]</code></p>
<dd>
<dt><code>xyz &#8212; XYZ cartesian coordinates format</code></p>
<dd>
<dt><code>yob &#8212; YASARA.org YOB format</code></p>
<dd>
<dt><code>zin &#8212; ZINDO input format [Write-only]</code></p>
<dd></dl>
<h2>FORMAT OPTIONS</h2>
<p> Individual file formats may have additional formatting options. </p>
<p> Input format options are preceded by &#8216;a&#8217;, e.g. -as </p>
<p> Output format options are preceded by &#8216;x&#8217;, e.g. -xn </p>
<p> For further specific information and options, use -H&lt;format-type&gt; </p>
<p>&nbsp;<wbr>e.g., -Hcml</p>
<h2>EXAMPLES</h2>
<p> Standard conversion: </p>
<blockquote><p><tt>&quot;babel -ixyz ethanol.xyz -opdb ethanol.pdb&quot;</tt></p></blockquote>
<p> Conversion from a SMI file in STDIN to a Mol2 file written to STDOUT: </p>
<blockquote><p><tt>&quot;babel -ismi -omol2&quot;</tt></p></blockquote>
<p> Split a multi-molecule file into new1.smi, new2.smi, etc.: </p>
<blockquote><p><tt>&quot;babel infile.mol new.smi -m&quot;</tt></p></blockquote>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-obenergy/">obenergy</a>(1), <a href="/docs/linux/man/1-obfit/">obfit</a>(1), <a href="/docs/linux/man/1-obgrep/">obgrep</a>(1), <a href="/docs/linux/man/1-obminimize/">obminimize</a>(1), <a href="/docs/linux/man/1-obprop/">obprop</a>(1), <a href="/docs/linux/man/1-obrotate/">obrotate</a>(1), <a href="/docs/linux/man/1-obrotamer/">obrotamer</a>(1). The web pages for Open Babel can be found at: &lt;<code><a rel="nofollow" href="http://openbabel.org/">http://openbabel.org/</a></code>&gt;</p>
<h2>AUTHORS</h2>
<p> An -nosplit A cast of many, including the currrent maintainers An Geoff Hutchison , An Chris Morley , An Michael Banck , and innumerable others who have contributed fixes and additions. For more contributors to Open Babel, see &lt;<code><a rel="nofollow" href="http://openbabel.org/wiki/THANKS">http://openbabel.org/wiki/THANKS</a></code>&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 1998-2001 by OpenEye Scientific Software, Inc.<br />
 Some portions Copyright (C) 2001-2007 by Geoffrey R. Hutchison </p>
<p>&nbsp;<wbr>This program is free software;&nbsp;<wbr>you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation version 2 of the License. </p>
<p>&nbsp;<wbr>This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<h2>Index</h2>
