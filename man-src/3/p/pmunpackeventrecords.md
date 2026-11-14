---
title: "pmunpackeventrecords(3)"
name: "pmunpackeventrecords"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pmunpackeventrecords/"
description: "pmUnpackEventRecords – unpack event records"
---

<p><code>pmUnpackEventRecords</code> &#8211; unpack event records</p>
<h2>C Synopsis</h2>
<p><code> #include &lt;pcp/pmapi.h&gt; </p>
<p> int pmUnpackEventRecords(pmValueSet *</code><i>vsp</i>, int <i>idx</i>, pmResult ***<i>rap</i>); </p>
<p> int pmUnpackHighResEventRecords(pmValueSet *<i>vsp</i>, int <i>idx</i>, pmHighResResult ***<i>hrap</i>); </p>
<p> cc &#8230; -lpcp</p>
<h2>Description</h2>
<p>Event records are encoded as a packed array of records within a <i>pmResult</i> using a container metric with a value of type <code>PM_TYPE_EVENT ,</code> and a <i>pmHighResResult</i> when using a metric of type <code>PM_TYPE_HIGHRES_EVENT</code>. </p>
<p> <code>pmUnpackEventRecords</code> and <code>pmUnpackHighResEventRecords</code> may be used to unpack event records from a metric value identified by <i>vsp</i> and <i>idx</i>. If the metric has a singular value, <i>idx</i> should be 0, else the ordinal instance value identified by <i>idx</i> will be unpacked, i.e. vsp-&gt;vlist[idx]. The unpacked records are turned into either <i>pmResult</i> or <i>pmHighResResult</i> structures, one per event record and one metric per event parameter, and <i>rap</i> is returned as a pointer to an array (NULL pointer terminated) of pointers to the result structures. </p>
<p> The only difference between the two result types is the timestamp scale; the <i>pmHighResResult</i> allows for nanosecond precision, whereas <i>pmResult</i> allows for microsecond resolution. </p>
<p> Some control information from the packed event records is unpacked into additional &#8220;anonymous&#8221; metrics as follows:</p>
<dl>
<dt>1.</p>
<dd>If the event record has a non-zero flags value, then the corresponding <i>pmResult</i>/<i>pmHighResResult</i> will have the flags value encoded with the additional metric <code>event.flags</code> that is inserted ahead of all other event parameters.</p>
<dt>2.</p>
<dd>If the event record flag is set to <code>PM_EVENT_FLAG_MISSED</code>, then the corresponding <i>pmResult</i>/<i>pmHighResResult</i> will have one metric <code>event.missed</code> with a value that equals the number of event records &#8220;missed&#8221; because either the PMDA could not keep up, or the PMAPI client did not collect the event records fast enough.</dl>
<p> <code>pmUnpackEventRecords</code> returns the number of <i>pmResult</i> structures as the return value, which is &gt;= 0 for success. Similarly, <code>pmUnpackHighResEventRecords</code> returns the number of <i>pmHighResResult</i> structures as the return value, which is &gt;= 0 for success. </p>
<p> <i>rap</i> and the associated <i>pmResult</i> structures may be freed using the convenience function <code><a href="/docs/linux/man/3-pmfreeeventresult/">pmFreeEventResult</a></code>(3). </p>
<p> Similarly, the <i>hrap</i> and the associated <i>pmHighResResult</i> structures may be freed using the convenience function <code>pmFreeHighResEventResult</code>.</p>
<h2>Return Value</h2>
<p>The following errors are possible:</p>
<dl>
<dt>PM_ERR_CONV</p>
<dd>The values associated with <i>vsp</i> are not encoded using the format PM_VAL_DPTR or PM_VAL_SPTR, or the flags at the head of the event record has an unexpected value.</p>
<dt>PM_ERR_INST</p>
<dd>The value associated with <i>vsp</i> is not singular as expected.</p>
<dt>PM_ERR_TYPE</p>
<dd><i>vsp</i> is not a value of type <code>PM_TYPE_EVENT</code>.</p>
<dt>PM_ERR_TOOSMALL</p>
<dd>The value identified by <i>vbp</i> is not legal because the value length is less than the minimum size, or the number of event records encoded in the (value header) <i>pmEventArray</i>/<i>pmEventHighResArray</i> structure is negative, or the number of missed event records in the array is negative.</p>
<dt>PM_ERR_TOOBIG</p>
<dd>Either <code>vsp</code> indicates more than one value is present (all the event records are expected to be packed in a single metric value), or when unpacking the event records, the processing continues past the end of the enclosing value. Indicates corruption of the packed event record.</p>
<dt>PM_ERR_TYPE</p>
<dd>Event parameters must have one of the arithmetic types, else <code>PM_TYPE_AGGREGATE</code>, <code>PM_TYPE_STRING</code> or <code>PM_TYPE_AGGREGATE_STATIC</code>.</p>
<dt>other values &lt; 0</p>
<dd>refer to <code><a href="/docs/linux/man/3-pmerrstr/">pmErrStr</a></code>(3).</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3) and <code><a href="/docs/linux/man/3-pmfreeeventresult/">pmFreeEventResult</a></code>(3). </p>
