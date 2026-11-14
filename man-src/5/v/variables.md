---
title: "variables(5)"
name: "variables"
section: "5"
letter: "v"
url: "/docs/linux/man/5-variables/"
---

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;variables - Format of specifying variable names to SNMP tools.

<h2>Description</h2>

The syntax and semantics of management information in SNMP is given by the definitions of MIB objects, loaded from one or more MIB files (or &quot;MIB modules&quot;). These definitions are not strictly required for the SNMP protocol to operate correctly, but are typically needed by SNMP client applications to display information in a meaningful manner. The MIB file also serves as a design document when developing an SNMP agent (or sub-agent) that provides this information, and ensures that client and server share a common understanding about what management information represents. 

<h2>OIDs</h2>

MIB objects are specified using Object Identifiers (OIDs), which can take a number of forms. Note that all of the examples in this section refer to the same MIB object.

<h3>Numeric OIDs</h3>

The fundamental format of an OID is a sequence of integer values (or &quot;subidentifiers&quot;), typically written using dots to separate the individual subidentifiers.
<dl><dd>&nbsp;.1.3.6.1.2.1.1.1</dl>
 This is the format that is used within the SNMP protocol itself, in the packets that are sent over the network. 

 This form of representing an OID does not require MIB files or MIB object definitions to be available. However it does rely on the client application and/or network administrator knowing what a given numeric OID refers to. As such, it is not a particularly helpful representation to anyone just starting out with SNMP. 

 This format can be obtained by giving the command-line option -On to most Net-SNMP commands.

<h3>Full OID path</h3>

A similar (but somewhat more informative) format uses the same dotted list representation, but with the numeric subidentifiers replaced by names, taken from the relevant MIB file(s).
<dl><dd>&nbsp;.iso.org.dod.internet.mgmt.mib-2.system.sysDescr</dl>
 This uniquely identifies a particular MIB object (as with the numeric OID), but the list of names should hopefully give some indication as to what information this object represents. However it does rely on the relevant MIB files being available (as do all formats other than the purely numeric OID). Such OIDs also tend to be fairly long! 

 This format can be obtained by giving the command-line option -Of to most Net-SNMP commands. 

 A variant of this (typically used when writing OIDs in descriptive text, rather than running programs), is to combine the name and numeric subidentifier:
<dl><dd>&nbsp;<a HREF="/docs/linux/man/1--iso/">.iso</a>(1)<a HREF="/docs/linux/man/3--org/">.org</a>(3)<a HREF="/docs/linux/man/6--dod/">.dod</a>(6)<a HREF="/docs/linux/man/1--internet/">.internet</a>(1)<a HREF="/docs/linux/man/2--mgmt/">.mgmt</a>(2)<a HREF="/docs/linux/man/1--mib-2/">.mib-2</a>(1)<a HREF="/docs/linux/man/1--system/">.system</a>(1) 
&nbsp;<a HREF="/docs/linux/man/1--sysdescr/">.sysDescr</a>(1)</dl>

<h3>Module-qualified OIDs</h3>

An alternative way to (more-or-less) uniquely specify an OID, is to give the name of the MIB object, together with the MIB module where it is defined.
<dl><dd>SNMPv2-MIB::sysDescr</dl>
 MIB object names are unique within a given module, so as long as there are not two MIB modules with the same name (which is unusual, though not unheard of), this format specifies the desired object in a reasonably compact form. It also makes it relatively easy to find the definition of the MIB object. 

 This is the default format for displaying OIDs in Net-SNMP applications. It can also be specified explicitly by giving the command-line option -OS to most Net-SNMP commands.

<h3>Object name</h3>

Possibly the most common form for specifying MIB objects is using the name of the object alone - without the full path or the name of the module that defines it.
<dl><dd>sysDescr</dl>
 This is by far the shortest and most convenient way to refer to a MIB object. However the danger is that if two MIB modules each define a MIB object with the same name (which is perfectly legal in some circumstances), then it's not necessarily clear which MIB object is actually meant. For day-to-day use, particularly when using standard MIB objects, this is <i>probaby</i> safe. But it's important to be aware of the potential ambiguities. 

 This format can be obtained by giving the command-line option -Os to most Net-SNMP commands.

<h3>UCD-format</h3>

Previous versions of the code (UCD v4.x and earlier) used a simple approach to shortening the way OIDs were specified. If the full path of the OID began with .iso.org.dod.internet.mgmt.mib-2 then this prefix was removed from the OID before displaying it. All other OIDs were displayed in full. 

 Similarly, if an OID was passed to the UCD library that did not begin with a dot (and wasn't in the module::name format), then the same prefix was prepended. The example OID from the formats listed above would therefore be given or displayed as
<dl><dd>system.sysDescr</dl>
 The inconsistent handling of OIDs, depending on their location within the OID tree, proved to be more trouble than it was worth, and this format is no longer recommended. 

 The previous behaviour can be obtained by giving the command-line option -Ou (for displaying output), or -Iu (for interpreting input OIDs without a leading dot) to most Net-SNMP commands.

<h2>See Also</h2>

<a HREF="/docs/linux/man/1-snmpcmd/">snmpcmd</a>(1)

<h2>Bugs</h2>

The parser of the MIB files file is not expected to handle bizarre (although correct) interpretations of the ASN.1 notation. 
