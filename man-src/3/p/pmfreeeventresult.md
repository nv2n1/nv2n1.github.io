---
title: "pmfreeeventresult(3)"
name: "pmfreeeventresult"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pmfreeeventresult/"
description: "pmFreeEventResult, pmFreeHighResEventResult – release storage allocated for unpacked event records"
---

<p><code>pmFreeEventResult</code>, <code>pmFreeHighResEventResult</code> &#8211; release storage allocated for unpacked event records</p>
<h2>C Synopsis</h2>
<p><code> #include &lt;pcp/pmapi.h&gt; </p>
<p> void pmFreeEventResult(pmResult **</code><i>rset</i>);<br />
 void pmFreeHighResEventResult(pmHighResResult **<i>hrset</i>); </p>
<p> cc &#8230; -lpcp</p>
<h2>Description</h2>
<p>When processing event records, if <code><a href="/docs/linux/man/3-pmunpackeventrecords/">pmUnpackEventRecords</a></code>(3) is used to unpack event records from a metric within a <i>pmResult</i> structure with a value of type <code>PM_TYPE_EVENT</code> then the structure returned from <code><a href="/docs/linux/man/3-pmunpackeventrecords/">pmUnpackEventRecords</a></code>(3) is a NULL pointer terminated array of pointers to <i>pmResult</i> structures, one for each event record. </p>
<p> <code>pmFreeEventResult</code> is a convenience method that frees all of the <i>pmResult</i> structures and the array of pointers (<i>rset</i>). </p>
<p> Similarly, <code>pmFreeHighResEventResult</code> may be used to free the <i>pmHighResResult</i> structures and array returned from the <code>pmUnpackHighResEventRecords</code> routine when using <code>PM_TYPE_HIGHRES_EVENT</code> metrics.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3) and <code><a href="/docs/linux/man/3-pmunpackeventrecords/">pmUnpackEventRecords</a></code>(3). </p>
