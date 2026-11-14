---
title: "mkdssp(1)"
name: "mkdssp"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mkdssp/"
description: "mkdssp – Calculate secondary structure for proteins in a PDB file"
---

<h2>NAME</h2>
<p> mkdssp &#8211; Calculate secondary structure for proteins in a PDB file</p>
<h2>SYNOPSIS</h2>
<p> <code>mkdssp</code> [OPTION] pdbfile [dsspfile]</p>
<h2>DESCRIPTION</h2>
<p> The <i>mkdssp</i> program was originally designed by Wolfgang Kabsch and Chris Sander to standardize secondary structure assignment. DSSP is a database of secondary structure assignments (and much more) for all protein entries in the Protein Data Bank (PDB) and <i>mkdssp</i> is the application that calculates the DSSP entries from PDB entries. Please note that <i>mkdssp</i> <code>does not predict</code> secondary structure.</p>
<h2>OPTIONS</h2>
<p> If you invoke <i>mkdssp</i> with only one parameter, it will be interpreted as the PDB file to process and output will be sent to stdout. If a second parameter is specified this is interpreted as the name of the DSSP file to create. Both the input and the output file names may have either .gz or .bz2 as extension resulting in the proper compression.</p>
<dl>
<dt><code>-i</code>, <code>&#8211;input</code> filename</p>
<dd> The file name of a <i>PDB</i> formatted file containing the protein structure data. This file may be a file compressed by gzip or bzip2.</p>
<dt><code>-o</code>, <code>&#8211;output</code> filename</p>
<dd> The file name of a <i>DSSP</i> file to create. If the filename ends in .gz or .bz2 a compressed file is created.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> Write out diagnositic information.</p>
<dt><code>&#8211;version</code></p>
<dd> Print the version number and exit.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Print the help message and exit. The directory containing the parser scripts for mrs.</dl>
<h2>THEORY</h2>
<p> The DSSP program works by calculating the most likely secondary structure assignment given the 3D structure of a protein. It does this by reading the position of the atoms in a protein (the ATOM records in a PDB file) followed by calculation of the H-bond energy between all atoms. The best two H-bonds for each atom are then used to determine the most likely class of secondary structure for each residue in the protein. </p>
<p> This means you do need to have a full and valid 3D structure for a protein to be able to calculate the secondary structure. There&#8217;s no magic in DSSP, so e.g. it cannot guess the secondary structure for a mutated protein for which you don&#8217;t have the 3D structure.</p>
<h2>DSSP FILE FORMAT</h2>
<p> The header part of each DSSP file is self explaining, it contains some of the information copied over from the PDB file and there are some statistics gathered while calculating the secondary structure. </p>
<p> The second half of the file contains the calculated secondary structure information per residue. What follows is a brief explanation for each column. </p>
<table>
<tr VALIGN=top>
<td><code>Column Name</code></td>
<td COLSPAN=2><code>Description</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>#</td>
<td COLSPAN=2>The residue number as counted by mkdssp
</td>
</tr>
<tr VALIGN=top>
<td>RESIDUE</td>
<td COLSPAN=2> The residue number as specified by the PDB file followed by a chain identifier.
</td>
</tr>
<tr VALIGN=top>
<td>AA</td>
<td COLSPAN=2> The one letter code for the amino acid. If this letter is lower case this means this is a cysteine that form a sulfur bridge with the other amino acid in this column with the same lower case letter.
</td>
</tr>
<tr VALIGN=top>
<td ROWSPAN=2>STRUCTURE</td>
<td COLSPAN=2> This is a complex column containing multiple sub columns. The first column contains a letter indicating the secondary structure assigned to this residue. Valid values are:
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center><code>Code</code></td>
<td><code>Description</code></td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>H</td>
<td>Alpha Helix</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>B</td>
<td>Beta Bridge</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>E</td>
<td>Strand</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>G</td>
<td>Helix-3</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>I</td>
<td>Helix-5</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>T</td>
<td>Turn</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>S</td>
<td>Bend</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2> What follows are three column indicating for each of the three helix types (3, 4 and 5) whether this residue is a candidate in forming this helix. A <code>&gt;</code> character indicates it starts a helix, a number indicates it is inside such a helix and a <code>&lt;</code> character means it ends the helix. </td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2> The next column contains a S character if this residue is a possible bend. </td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2> Then there&#8217;s a column indicating the chirality and this can either be positive or negative (i.e. the alpha torsion is either positive or negative). </td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2> The last two columns contain beta bridge labels. Lower case here means parallel bridge and thus upper case means anti parallel. </td>
</tr>
<tr VALIGN=top>
<td>BP1 and BP2</td>
<td COLSPAN=2> The first and second bridge pair candidate, this is followed by a letter indicating the sheet.
</td>
</tr>
<tr VALIGN=top>
<td>ACC</td>
<td COLSPAN=2> The accessibility of this residue, this is the surface area expressed in square Ångstrom that can be accessed by a water molecule.
</td>
</tr>
<tr VALIGN=top>
<td>N-H&#8211;&gt;O..O&#8211;&gt;H-N</td>
<td COLSPAN=2> Four columns, they give for each residue the H-bond energy with another residue where the current residue is either acceptor or donor. Each column contains two numbers, the first is an offset from the current residue to the partner residue in this H-bond (in DSSP numbering), the second number is the calculated energy for this H-bond.
</td>
</tr>
<tr VALIGN=top>
<td>TCO</td>
<td COLSPAN=2> The cosine of the angle between C=O of the current residue and C=O of previous residue. For alpha-helices, TCO is near +1, for beta-sheets TCO is near -1. Not used for structure definition.
</td>
</tr>
<tr VALIGN=top>
<td>Kappa</td>
<td COLSPAN=2> The virtual bond angle (bend angle) defined by the three C-alpha atoms of the residues current &#8211; 2, current and current + 2. Used to define bend (structure code &#8216;S&#8217;).
</td>
</tr>
<tr VALIGN=top>
<td>PHI and PSI</td>
<td COLSPAN=2> IUPAC peptide backbone torsion angles.
</td>
</tr>
<tr VALIGN=top>
<td>X-CA, Y-CA and Z-CA</td>
<td COLSPAN=2> The C-alpha coordinates
</td>
</tr>
</table>
<h2>HISTORY</h2>
<p> The original DSSP application was written by Wolfgang Kabsch and Chris Sander in Pascal. This version is a complete rewrite in C++ based on the original source code. A few bugs have been fixed since and the algorithms have been tweaked here and there.</p>
<h2>TODO</h2>
<p> The code desperately needs an update. The first thing that needs implementing is the improved recognition of pi-helices. A second improvement would be to use angle dependent H-bond energy calculation.</p>
<h2>BUGS</h2>
<p> If you find any, please let me know.</p>
<h2>AUTHOR</h2>
<p> Maarten L. Hekkelman (m.hekkelman (at) cmbi.ru.nl) </p>
<h2>Index</h2>
