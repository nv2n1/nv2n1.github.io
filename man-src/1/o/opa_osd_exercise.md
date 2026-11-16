---
title: "opa_osd_exercise(1)"
name: "opa_osd_exercise"
section: "1"
letter: "o"
url: "/docs/linux/man/1-opa_osd_exercise/"
---

<h2>NAME</h2>

 opa_osd_exercise 

 

 

 Performs stress test on SM and distributed SA query system.

<h2>Syntax</h2>

 opa_osd_exercise [ <i>opts</i>] <i>guidlist</i>

<h2>Options</h2>

 

<dl>
<dt>
&nbsp;<wbr><i>opts</i>&nbsp;<wbr>
</dt><dd> Options. Values include: 
</dd><dl>
<dl>
<dt>
</dt><dd> 
 -d <i>debug level</i> Sets debugging level. 
</dd></dl>
</dl>
 

<dl>
<dl>
<dt>
</dt><dd> 
 -s <i>seconds</i> Specifies running for at least <i>seconds</i> seconds.</dd></dl>
</dl>
 

<dl>
<dl>
<dt>
</dt><dd> 
 -r <i>remote</i> Specifies the host running the fabric simulator.</dd></dl>
</dl>
 

<dl>
<dl>
<dt>
</dt><dd> 
 -x <i>count</i> Number of destinations to toggle up or down after each pass. Maximum = MAX_TOGGLES.</dd></dl>
</dl>
 

<dl>
<dl>
<dt>
</dt><dd> 
 -X <i>count</i> Specifies how often to toggle a source port up or down (in seconds).</dd></dl>
</dl>
 

<dl>
<dl>
<dt>
</dt><dd> 
 -D <i>seconds</i> Specifies how long to sleep after each pass. This value gives the Subnet Manager time to process port events.</dd></dl>
</dl>
 

<dl>
<dl>
<dt>
</dt><dd> 
 -p <i>pkey</i> Specifies to include <i>pkey</i> in the searches. Can be specified up to 8 times.</dd></dl>
</dl>
 

<dt>-S <i>sid</i>
</dt><dd> Specifies to include SID in the searches.
</dd><dt>-t <i>error threshold</i>
</dt><dd> Cancels the test if the number of path errors to a single destination exceeds <i>error threshold</i>. The count is reset to zero when a correct result is retrieved. Can be specified up to 8 times. Note that providing both SIDs and pkeys may cause problems.
</dd><dt>-e
</dt><dd> Instructs simulator to enable all ports before starting.
</dd><dt>
&nbsp;<wbr><i>guidlist</i>&nbsp;<wbr>
</dt><dd> Text file that lists the source and destination GUIDs and LIDs. For example, from a build_table.pl file. 

</dd></dl>

<h2>Example</h2>

 opa_osd_exercise -p 0x9001 guidtable 

<h2>Index</h2>


