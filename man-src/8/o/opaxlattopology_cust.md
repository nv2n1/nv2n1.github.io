---
title: "opaxlattopology_cust(8)"
name: "opaxlattopology_cust"
section: "8"
letter: "o"
url: "/docs/linux/man/8-opaxlattopology_cust/"
description: "opaxlattopology_cust"
---

<p>opaxlattopology_cust </p>
<p> Customizable script for documenting cluster topology. Provides an alternative to the standard script (see <i>opaxlattopology</i> ). Edit the sample topology_cust.xlsx to represent each external link in a cluster, then modify opaxlattopology_cust to translate the alternate CSV form to the standard CSV form used by opaxlattopology.</p>
<h2>Syntax</h2>
<p>opaxlattopology_cust -t <i>topology_prime</i>[-s <i>topology_second</i>] -T <i>topology_out</i><br />
 [-v <i>level</i>] [-i <i>level</i>] [-c <i>char</i>] [-K] [-?]</p>
<h2>Options</h2>
<dl>
<dt>-t <i>topology_prime</i></p>
<dd>Primary topology CSV input file. Specifies the primary CSV input file and must be present. </p>
<dt>-s <i>topology_second</i></p>
<dd>Secondary topology CSV input file. Specifies a secondary CSV input file. Appended to the primary for processing. </p>
<dt>-T <i>topology_out</i></p>
<dd>Topology CSV output file. Specifies the CSV output file name and must be specified. </p>
<dt>-v <i>level</i></p>
<dd>Verbose level. Range = 0 &#8211; 8, default = 2. </p>
<dl>
<dd>
<dl>
<dd>0 No output. </p>
</dl>
</dl>
<dl>
<dd>
<dl>
<dd>1 Progress output. </p>
</dl>
</dl>
<dl>
<dd>
<dl>
<dd>2 Reserved. </p>
</dl>
</dl>
<dl>
<dd>
<dl>
<dd>4 Time stamps. </p>
</dl>
</dl>
<dl>
<dd>
<dl>
<dd>8 Reserved. </p>
</dl>
</dl>
<dt>-i <i>level</i></p>
<dd>Screen output indent level. Range = 0 &#8211; 15, default = 0. </p>
<dt>-c <i>char</i></p>
<dd>Concatenation character, used for Cable Label values. A space is used by default, but another character, such as underscore, can be specified. </p>
<dt>-K</p>
<dd>Does not clean temporary files. Prevents temporary files from being removed. Temporary files contain CSV data used during processing. Temporary files are not needed after the standard-format CSV file is created, but they can be retained for subsequent inspection or processing. </p>
<dt>-?</p>
<dd>Prints this output. </p>
</dl>
<h2>Description</h2>
<p>Each link contains source, destination, and cable fields with one link per row of the spreadsheet. Link fields must not contain commas. Source and Destination fields are each a concatenation of name and port information in the following forms. Names not of the form ib or C are assumed to be host names. The following lists the <code>Node Type</code> : <code>Source/Destination</code> :</p>
<dl>
<dt>Host :</p>
<dd>host <i>N</i> where N is a host number.</p>
<dt>Edge Switch :</p>
<dd>ib <i>N</i> p <i>N</i> where N is a switch/port number.</p>
<dt>Core Leaf :</p>
<dd>C <i>n</i> L <i>nnn</i> p <i>N</i> where N/n is a host/switch/port number.</dl>
<p> Cable values, CableLength, and CableDetails are optional and have no special syntax. If present, they are placed in the standard-format CSV file exactly as they appear. CableLabel is created automatically by opaxlattopology_cust as the concatenation of Source and Destination (see -c option). Rack Group and Rack are not supported in topology_cust.xlsx. Therefore, opaxlattopology_cust leaves these fields empty in the standard-format CSV file. </p>
