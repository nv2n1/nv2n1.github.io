---
title: "snmptranslate(1)"
name: "snmptranslate"
section: "1"
letter: "s"
url: "/docs/linux/man/1-snmptranslate/"
description: "snmptranslate – translate MIB OID names between numeric and textual forms"
---

<h2>NAME</h2>
<p> snmptranslate &#8211; translate MIB OID names between numeric and textual forms</p>
<h2>SYNOPSIS</h2>
<p> <code>snmptranslate</code> [OPTIONS] OID [OID]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> <code>snmptranslate</code> is an application that translates one or more SNMP object identifier values from their symbolic (textual) forms into their numerical forms (or vice versa). </p>
<p> OID is either a numeric or textual object identifier.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-D</code><i>[TOKEN[,&#8230;]]</i></p>
<dd> Turn on debugging output for the given <i>TOKEN</i>(s). Try <i>ALL</i> for extremely verbose output.</p>
<dt><code>-h</code></p>
<dd> Display a brief usage message and then exit.</p>
<dt><code>-m</code><i> MIBLIST</i></p>
<dd> Specifies a colon separated list of MIB modules to load for this application. This overrides the environment variable MIBS.</p>
<dt>
<dd> The special keyword <i>ALL</i> is used to specify all modules in all directories when searching for MIB files. Every file whose name does not begin with &quot;.&quot; will be parsed as if it were a MIB file.</p>
<dt><code>-M</code><i> DIRLIST</i></p>
<dd> Specifies a colon separated list of directories to search for MIBs. This overrides the environment variable MIBDIRS.</p>
<dt><code>-T</code><i> TRANSOPTS</i></p>
<dd> Provides control over the translation of the OID values. The following <i>TRANSOPTS</i> are available:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>-Td</code></p>
<dd> Print full details of the specified OID.</p>
<dt><code>-Tp</code></p>
<dd> Print a graphical tree, rooted at the specified OID.</p>
<dt><code>-Ta</code></p>
<dd> Dump the loaded MIB in a trivial form.</p>
<dt><code>-Tl</code></p>
<dd> Dump a labeled form of all objects.</p>
<dt><code>-To</code></p>
<dd> Dump a numeric form of all objects.</p>
<dt><code>-Ts</code></p>
<dd> Dump a symbolic form of all objects.</p>
<dt><code>-Tt</code></p>
<dd> Dump a tree form of the loaded MIBs (mostly useful for debugging).</p>
<dt><code>-Tz</code></p>
<dd> Dump a numeric and labeled form of all objects (compatible with MIB2SCHEMA format).</dl>
</dl>
<dt><code>-V</code></p>
<dd> Display version information for the application and then exit.</p>
<dt><code>-w</code><i> WIDTH</i></p>
<dd> Specifies the width of <code>-Tp</code> and <code>-Td</code> output. The default is very large.</dl>
<p> In addition to the above options, <code>snmptranslate</code> takes the OID input (<code>-I</code>), MIB parsing (<code>-M</code>) and OID output (<code>-O</code>) options described in the <code>INPUT OPTIONS</code>, <code>MIB PARSING OPTIONS</code> and <code>OUTPUT OPTIONS</code> sections of the <i><a href="/docs/linux/man/1-snmpcmd/">snmpcmd</a>(1) </i> manual page.</p>
<h2>EXAMPLES</h2>
<dl>
<dt>&bull;</p>
<dd> snmptranslate -On -IR sysDescr<br />
 will translate &quot;sysDescr&quot; to a more qualified form:</p>
<dt>
<dd> system.sysDescr</p>
<dt>&bull;</p>
<dd> snmptranslate -Onf -IR sysDescr<br />
 will translate &quot;sysDecr&quot; to:</p>
<dt>
<dd> .iso.org.dod.internet.mgmt.mib-2.system.sysDescr</p>
<dt>&bull;</p>
<dd> snmptranslate -Td -OS system.sysDescr<br />
 will translate &quot;sysDecr&quot; into:</p>
<dt>
<dd>
<pre><code>
SNMPv2 - MIB::sysDescr sysDescr OBJECT - TYPE-- FROM SNMPv2 - MIB-- TEXTUAL CONVENTION DisplayString SYNTAX OCTET STRING(0..255) DISPLAY - HINT "255a" MAX - ACCESS read - only STATUS current DESCRIPTION "A textual description of the entity. This
    value should include the full name and version identification of the system's hardware type,
    software operating - system,
    and networking software."
        ::
        = {iso(1) org(3) dod(6) internet(1) mgmt(2) mib - 2(1)system(1) 1}
</code></pre>
<dt>&bull;</p>
<dd> snmptranslate -Tp -OS system<br />
 will print the following tree:</p>
<dt>
<dd>
+ &#8211;system(1) |<br />
    +&#8211; -R&#8211; String sysDescr(1) | Textual Convention:DisplayString<br />
                                                     |<br />
                                                Size:0..255 + &#8212; -R&#8211; ObjID sysObjectID(2) + &#8212; -R&#8211; TimeTicks sysUpTime(3) + &#8212; -RW &#8211; String sysContact(4) | Textual Convention:DisplayString<br />
                                                                                                                                                                                 |<br />
                                                Size:0..255 + &#8212; -RW &#8211; String sysName(5) | Textual Convention:DisplayString<br />
                                                                                                              |<br />
                                                Size:0..255 + &#8212; -RW &#8211; String sysLocation(6) | Textual Convention:DisplayString<br />
                                                                                                                  |<br />
                                                Size:0..255 + &#8212; -R&#8211; Integer sysServices(7) + &#8212; -R&#8211; TimeTicks sysORLastChange(8) | Textual Convention:TimeStamp<br />
                                                                                                                                                         |<br />
                                                                                                                                                         +&#8211;sysORTable(9) |<br />
                                                                                                                                                         +&#8211;sysOREntry(1) |<br />
                                                                                                                                                         +&#8211; &#8212; &#8211;Integer sysORIndex(1) + &#8212; -R&#8211; ObjID sysORID(2) + &#8212; -R&#8211; String sysORDescr(3) | Textual<br />
                                          Convention:DisplayString<br />
                                                     |<br />
                                                Size:0..255 + &#8212; -R&#8211; TimeTicks sysORUpTime(4)<br />
                                                                     Textual<br />
                                          Convention:TimeStamp
</dl>
<dl>
<dt>&bull;</p>
<dd> snmptranslate -Ta | head<br />
 will produce the following dump:</p>
<dt>
<dd>
<pre><code>
dump DEFINITIONS :: = BEGIN
    org ::
        = {iso 3} dod :: = {org 6} internet :: = {dod 1} directory :: = {internet 1} mgmt :: = {internet 2} experimental :: = {internet 3} private :: = {internet 4} security :: = {internet 5} snmpV2 :: = {internet 6}
</code></pre>
</dl>
<dl>
<dt>&bull;</p>
<dd> snmptranslate -Tl | head<br />
 will produce the following dump:</p>
<dt>
<dd>
<pre>
<a href="//www.systutorials.com/docs/linux/man/1-.iso/">.iso</a>(1)<a href="//www.systutorials.com/docs/linux/man/3-.org/">.org</a>(3)
<a href="//www.systutorials.com/docs/linux/man/1-.iso/">.iso</a>(1)<a href="//www.systutorials.com/docs/linux/man/3-.org/">.org</a>(3)<a href="//www.systutorials.com/docs/linux/man/6-.dod/">.dod</a>(6)
<a href="//www.systutorials.com/docs/linux/man/1-.iso/">.iso</a>(1)<a href="//www.systutorials.com/docs/linux/man/3-.org/">.org</a>(3)<a href="//www.systutorials.com/docs/linux/man/6-.dod/">.dod</a>(6)<a href="//www.systutorials.com/docs/linux/man/1-.internet/">.internet</a>(1)
<a href="//www.systutorials.com/docs/linux/man/1-.iso/">.iso</a>(1)<a href="//www.systutorials.com/docs/linux/man/3-.org/">.org</a>(3)<a href="//www.systutorials.com/docs/linux/man/6-.dod/">.dod</a>(6)<a href="//www.systutorials.com/docs/linux/man/1-.internet/">.internet</a>(1)<a href="//www.systutorials.com/docs/linux/man/1-.directory/">.directory</a>(1)
<a href="//www.systutorials.com/docs/linux/man/1-.iso/">.iso</a>(1)<a href="//www.systutorials.com/docs/linux/man/3-.org/">.org</a>(3)<a href="//www.systutorials.com/docs/linux/man/6-.dod/">.dod</a>(6)<a href="//www.systutorials.com/docs/linux/man/1-.internet/">.internet</a>(1)<a href="//www.systutorials.com/docs/linux/man/2-.mgmt/">.mgmt</a>(2)
<a href="//www.systutorials.com/docs/linux/man/1-.iso/">.iso</a>(1)<a href="//www.systutorials.com/docs/linux/man/3-.org/">.org</a>(3)<a href="//www.systutorials.com/docs/linux/man/6-.dod/">.dod</a>(6)<a href="//www.systutorials.com/docs/linux/man/1-.internet/">.internet</a>(1)<a href="//www.systutorials.com/docs/linux/man/2-.mgmt/">.mgmt</a>(2)<a href="//www.systutorials.com/docs/linux/man/1-.mib-2/">.mib-2</a>(1)
<a href="//www.systutorials.com/docs/linux/man/1-.iso/">.iso</a>(1)<a href="//www.systutorials.com/docs/linux/man/3-.org/">.org</a>(3)<a href="//www.systutorials.com/docs/linux/man/6-.dod/">.dod</a>(6)<a href="//www.systutorials.com/docs/linux/man/1-.internet/">.internet</a>(1)<a href="//www.systutorials.com/docs/linux/man/2-.mgmt/">.mgmt</a>(2)<a href="//www.systutorials.com/docs/linux/man/1-.mib-2/">.mib-2</a>(1)<a href="//www.systutorials.com/docs/linux/man/1-.system/">.system</a>(1)
<a href="//www.systutorials.com/docs/linux/man/1-.iso/">.iso</a>(1)<a href="//www.systutorials.com/docs/linux/man/3-.org/">.org</a>(3)<a href="//www.systutorials.com/docs/linux/man/6-.dod/">.dod</a>(6)<a href="//www.systutorials.com/docs/linux/man/1-.internet/">.internet</a>(1)<a href="//www.systutorials.com/docs/linux/man/2-.mgmt/">.mgmt</a>(2)<a href="//www.systutorials.com/docs/linux/man/1-.mib-2/">.mib-2</a>(1)<a href="//www.systutorials.com/docs/linux/man/1-.system/">.system</a>(1)<a href="//www.systutorials.com/docs/linux/man/1-.sysDescr/">.sysDescr</a>(1)
<a href="//www.systutorials.com/docs/linux/man/1-.iso/">.iso</a>(1)<a href="//www.systutorials.com/docs/linux/man/3-.org/">.org</a>(3)<a href="//www.systutorials.com/docs/linux/man/6-.dod/">.dod</a>(6)<a href="//www.systutorials.com/docs/linux/man/1-.internet/">.internet</a>(1)<a href="//www.systutorials.com/docs/linux/man/2-.mgmt/">.mgmt</a>(2)<a href="//www.systutorials.com/docs/linux/man/1-.mib-2/">.mib-2</a>(1)<a href="//www.systutorials.com/docs/linux/man/1-.system/">.system</a>(1)<a href="//www.systutorials.com/docs/linux/man/2-.sysObjectID/">.sysObjectID</a>(2)
<a href="//www.systutorials.com/docs/linux/man/1-.iso/">.iso</a>(1)<a href="//www.systutorials.com/docs/linux/man/3-.org/">.org</a>(3)<a href="//www.systutorials.com/docs/linux/man/6-.dod/">.dod</a>(6)<a href="//www.systutorials.com/docs/linux/man/1-.internet/">.internet</a>(1)<a href="//www.systutorials.com/docs/linux/man/2-.mgmt/">.mgmt</a>(2)<a href="//www.systutorials.com/docs/linux/man/1-.mib-2/">.mib-2</a>(1)<a href="//www.systutorials.com/docs/linux/man/1-.system/">.system</a>(1)<a href="//www.systutorials.com/docs/linux/man/3-.sysUpTime/">.sysUpTime</a>(3)
</pre>
</dl>
<dl>
<dt>&bull;</p>
<dd> snmptranslate -To | head<br />
 will produce the following dump</p>
<dt>
<dd>
<pre>
.1.3
.1.3.6
.1.3.6.1
.1.3.6.1.1
.1.3.6.1.2
.1.3.6.1.2.1
.1.3.6.1.2.1.1
.1.3.6.1.2.1.1.1
.1.3.6.1.2.1.1.2
.1.3.6.1.2.1.1.3
</pre>
</dl>
<dl>
<dt>&bull;</p>
<dd> snmptranslate -Ts | head<br />
 will produce the following dump</p>
<dt>
<dd>
<pre>
.iso.org
.iso.org.dod
.iso.org.dod.internet
.iso.org.dod.internet.directory
.iso.org.dod.internet.mgmt
.iso.org.dod.internet.mgmt.mib-2
.iso.org.dod.internet.mgmt.mib-2.system
.iso.org.dod.internet.mgmt.mib-2.system.sysDescr
.iso.org.dod.internet.mgmt.mib-2.system.sysObjectID
.iso.org.dod.internet.mgmt.mib-2.system.sysUpTime
</pre>
</dl>
<dl>
<dt>&bull;</p>
<dd> snmptranslate -Tt | head<br />
 will produce the following dump</p>
<dt>
<dd>
<pre>
  <a href="//www.systutorials.com/docs/linux/man/3-org/">org</a>(3) type=0
    <a href="//www.systutorials.com/docs/linux/man/6-dod/">dod</a>(6) type=0
      <a href="//www.systutorials.com/docs/linux/man/1-internet/">internet</a>(1) type=0
        <a href="//www.systutorials.com/docs/linux/man/1-directory/">directory</a>(1) type=0
        <a href="//www.systutorials.com/docs/linux/man/2-mgmt/">mgmt</a>(2) type=0
          <a href="//www.systutorials.com/docs/linux/man/1-mib-2/">mib-2</a>(1) type=0
            <a href="//www.systutorials.com/docs/linux/man/1-system/">system</a>(1) type=0
              <a href="//www.systutorials.com/docs/linux/man/1-sysDescr/">sysDescr</a>(1) type=2 tc=4 hint=255a
              <a href="//www.systutorials.com/docs/linux/man/2-sysObjectID/">sysObjectID</a>(2) type=1
              <a href="//www.systutorials.com/docs/linux/man/3-sysUpTime/">sysUpTime</a>(3) type=8
</pre>
</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-snmpcmd/">snmpcmd</a>(1), <a href="/docs/linux/man/5-variables/">variables</a>(5), RFC 2578-2580. </p>
<h2>Index</h2>
