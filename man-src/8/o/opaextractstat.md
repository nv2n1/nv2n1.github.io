---
title: "opaextractstat(8)"
name: "opaextractstat"
section: "8"
letter: "o"
url: "/docs/linux/man/8-opaextractstat/"
---

opaextractstat 

 

 

 Performs an error analysis of a fabric and provides augmented information from a topology_file. The report provides cable information as well as symbol error counts. 

 opaextractstat generates a detailed opareport errors report that also has a topology file (see <i>opareport</i> for more information about topology files). The report is piped to opaxmlextract which extracts values for Link, Cable and Port. (The port element names are context-sensitive.) Note that opaxmlextract generates two extraction records for each link (one for each port on the link); therefore, opaextractstat merges the two records into a single record and removes redundant link and cable information. 

 opaextractstat contains a while read loop that reads the CSV line-by-line, uses cut to remove redundant information, and outputs the data on a common line.

<h2>Syntax</h2>

opaextractstat topology_file [ <i>opareport options</i>]

<h2>Options</h2>

<dl><dt>--help
<dd>Produces full help text. 

<dt>topology_file
<dd>Specifies topology_file to use. 

<dt>
&nbsp;<wbr><i>opareport options</i>&nbsp;<wbr>
<dd>&nbsp;<wbr><i>Options</i>&nbsp;<wbr>are passed to opareport. See <i>opareport</i> for the full set of options.</dl>
 

 The portion of the script that calls opareport and opaxmlextract follows: 

 

 
 opareport -x -d 10 -s -o errors -T $@ | opaxmlextract -d ; 
 -e Rate -e MTU -e LinkDetails -e CableLength -e CableLabel 
 -e CableDetails -e Port.NodeDesc -e Port.PortNum -e SymbolErrors.Value

<h2>Examples</h2>

opaextractstat topology_file 
 opaextractstat topology_file -c my_opamon.conf 
