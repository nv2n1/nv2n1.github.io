---
title: "opa_osd_perf(1)"
name: "opa_osd_perf"
section: "1"
letter: "o"
url: "/docs/linux/man/1-opa_osd_perf/"
---

<h2>NAME</h2>

 opa_osd_perf 

 

 

 Tests the performance of the distributed SA shared memory database.

<h2>Syntax</h2>

 opa_osd_perf [ <i>opts</i>] <i>guidtable</i>

<h2>Options</h2>

 

<dl>
<dt>
&nbsp;<wbr><i>opts</i>&nbsp;<wbr>
<dd> Options. Values include: 

<dl>
<dt>
<dd>
<dl>
<dt>
<dd> 

 -q <i>queries</i> Runs at least <i>queries</i> queries. 

</dl>
</dl>
 

<dl>
<dt>
<dd>
<dl>
<dt>
<dd> 

 -p <i>pkey</i> Specifies to include <i>pkey</i> in the searches. Can be specified up to 8 times.</dl>
</dl>
 

<dl>
<dt>
<dd>
<dl>
<dt>
<dd> 

 -S <i>sid</i> Specifies to include SID in the searches. Can be specified up to 8 times. Note that providing both SIDs and pkeys may cause problems.</dl>
</dl>
 

<dt>
&nbsp;<wbr><i>guidtable</i>&nbsp;<wbr>
<dd> Text file that lists the destination GUIDs and LIDs. For example, from a build_table.pl file. 

</dl>

<h2>Example</h2>

 opa_osd_perf -q 100000 -p 0x8001 guidtable 

<h2>Index</h2>


