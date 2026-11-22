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
<p>opaxlattopology_cust -t <i>topology_prime</i>[-s <i>topology_second</i>] -T <i>topology_out</i><br/>
 [-v <i>level</i>] [-i <i>level</i>] [-c <i>char</i>] [-K] [-?]</p>
<h2>Options</h2>
<dl>
<dt>-t <i>topology_prime</i></dt>
<dd>Primary topology CSV input file. Specifies the primary CSV input file and must be present. </dd>
<dt>-s <i>topology_second</i></dt>
<dd>Secondary topology CSV input file. Specifies a secondary CSV input file. Appended to the primary for processing. </dd>
<dt>-T <i>topology_out</i></dt>
<dd>Topology CSV output file. Specifies the CSV output file name and must be specified. </dd>
<dt>-v <i>level</i></dt>
<dd>Verbose level. Range = 0 &#8211; 8, default = 2. </dd>
<dl>
<dd>
</dd><dl>
<dd>0 No output. </dd>
</dl>
</dl>
<dl>
<dd>
</dd><dl>
<dd>1 Progress output. </dd>
</dl>
</dl>
<dl>
<dd>
</dd><dl>
<dd>2 Reserved. </dd>
</dl>
</dl>
<dl>
<dd>
</dd><dl>
<dd>4 Time stamps. </dd>
</dl>
</dl>
<dl>
<dd>
</dd><dl>
<dd>8 Reserved. </dd>
</dl>
</dl>
<dt>-i <i>level</i></dt>
<dd>Screen output indent level. Range = 0 &#8211; 15, default = 0. </dd>
<dt>-c <i>char</i></dt>
<dd>Concatenation character, used for Cable Label values. A space is used by default, but another character, such as underscore, can be specified. </dd>
<dt>-K</dt>
<dd>Does not clean temporary files. Prevents temporary files from being removed. Temporary files contain CSV data used during processing. Temporary files are not needed after the standard-format CSV file is created, but they can be retained for subsequent inspection or processing. </dd>
<dt>-?</dt>
<dd>Prints this output. </dd>
</dl>
<h2>Description</h2>
<p>Each link contains source, destination, and cable fields with one link per row of the spreadsheet. Link fields must not contain commas. Source and Destination fields are each a concatenation of name and port information in the following forms. Names not of the form ib or C are assumed to be host names. The following lists the <code>Node Type</code> : <code>Source/Destination</code> :</p>
<dl>
<dt>Host :</dt>
<dd>host <i>N</i> where N is a host number.</dd>
<dt>Edge Switch :</dt>
<dd>ib <i>N</i> p <i>N</i> where N is a switch/port number.</dd>
<dt>Core Leaf :</dt>
<dd>C <i>n</i> L <i>nnn</i> p <i>N</i> where N/n is a host/switch/port number.</dd></dl>
<p> Cable values, CableLength, and CableDetails are optional and have no special syntax. If present, they are placed in the standard-format CSV file exactly as they appear. CableLabel is created automatically by opaxlattopology_cust as the concatenation of Source and Destination (see -c option). Rack Group and Rack are not supported in topology_cust.xlsx. Therefore, opaxlattopology_cust leaves these fields empty in the standard-format CSV file. </p>
