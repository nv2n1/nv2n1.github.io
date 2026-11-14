---
title: "opaextractperf(8)"
name: "opaextractperf"
section: "8"
letter: "o"
url: "/docs/linux/man/8-opaextractperf/"
---

opaextractperf 

 

 

 Provides a report of all performance counters in a CVS format suitable for importing into a spreadsheet or parsed by other scripts for further analysis. It generates a detailed opareport component summary report and pipes the result to opaxmlextract, extracting element values for NodeDesc, SystemImageGUID, PortNum, and all the performance counters. Extraction is performed only from the Systems portion of the report, which does not contain Neighbor information (the Neighbor and SMs portions are suppressed).

<h2>Syntax</h2>

opaextractperf [ <i>opareport options</i>]

<h2>Options</h2>

<dl><dt>--help
<dd>Produces full help text. 

<dt>
&nbsp;<wbr><i>opareport options</i>&nbsp;<wbr>
<dd>&nbsp;<wbr><i>Options</i>&nbsp;<wbr>are passed to opareport. See <i>opareport</i> for the full set of options.</dl>
 

 The portion of the script that calls opareport and opaxmlextract follows: 

 

 
 opareport -o comps -s -x -d 10 $@ | opaxmlextract -d ; 
 -e NodeDesc -e SystemImageGUID -e PortNum -e XmitDataMB 
 -e XmitData -e XmitPkts -e RcvDataMB -e RcvData -e RcvPkts 
 -e SymbolErrors -e LinkErrorRecovery -e LinkDowned -e PortRcvErrors 
 -e PortRcvRemotePhysicalErrors -e PortRcvSwitchRelayErrors 
 -e PortXmitDiscards -e PortXmitConstraintErrors 
 -e PortRcvConstraintErrors -e LocalLinkIntegrityErrors 
 -e ExcessiveBufferOverrunErrors -e VL15Dropped -s Neighbor -s SMs

<h2>Example</h2>

opaextractperf 
 opaextractperf -h 1 -p 2 
