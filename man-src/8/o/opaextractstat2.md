---
title: "opaextractstat2(8)"
name: "opaextractstat2"
section: "8"
letter: "o"
url: "/docs/linux/man/8-opaextractstat2/"
---

opaextractstat2 

 

 

 Performs an error analysis of a fabric and provides augmented information from a topology_file including all error counters. The output is in a CSV format suitable for importing into a spreadsheet or parsed by other scripts. opaextractstat2 is a front end to the opareport and opaxmlextract tools.

<h2>Syntax</h2>

opaextractstat2 topology_file [ <i>opareport options</i>]

<h2>Options</h2>

<dl><dt>--help
<dd>Produces full help text. 

<dt>topology_file
<dd>Specifies topology_file to use. 

<dt>
&nbsp;<wbr><i>opareport options</i>&nbsp;<wbr>
<dd>&nbsp;<wbr><i>options</i>&nbsp;<wbr>are passed to opareport. See&nbsp;<wbr> <i>opareport</i> for the full set of options.</dl>
 

 The portion of the script that calls opareport and opaxmlextract follows:opareport -x -d 10 -s -o errors -T $@ | opaxmlextract -d ; 
 -e Rate -e MTU -e Internal -e LinkDetails -e CableLength -e CableLabel 
 -e CableDetails -e Port.NodeGUID -e Port.PortGUID -e Port.PortNum 
 -e Port.PortType -e Port.NodeDesc -e Port.PortDetails 
 -e PortXmitData.Value -e PortXmitPkts.Value -e PortRcvData.Value 
 -e PortRcvPkts.Value -e SymbolErrors.Value -e LinkErrorRecovery.Value 
 -e LinkDowned.Value -e PortRcvErrors.Value 
 -e PortRcvRemotePhysicalErrors.Value -e PortRcvSwitchRelayErrors.Value 
 -e PortXmitConstraintErrors.Value -e PortRcvConstraintErrors.Value 
 -e LocalLinkIntegrityErrors.Value -e ExcessiveBufferOverrunErrors.Value

<h2>Example</h2>

opaextractstat2 topology_file 
 
 opaextractstat2 topology_file -c my_opamon.conf 
