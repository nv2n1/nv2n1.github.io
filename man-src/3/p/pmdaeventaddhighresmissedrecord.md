---
title: "pmdaeventaddhighresmissedrecord(3)"
name: "pmdaeventaddhighresmissedrecord"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pmdaeventaddhighresmissedrecord/"
description: "pmdaEventNewArray, pmdaEventResetArray, pmdaEventReleaseArray, pmdaEventAddRecord, pmdaEventAddMissedRecord, pmdaEventAddParam, pmdaEventGetAddr, pmdaEventNewHighResArray, pmdaEventResetHighResArra..."
---

<p><code>pmdaEventNewArray</code>, <code>pmdaEventResetArray</code>, <code>pmdaEventReleaseArray</code>, <code>pmdaEventAddRecord</code>, <code>pmdaEventAddMissedRecord</code>, <code>pmdaEventAddParam</code>, <code>pmdaEventGetAddr</code>, <code>pmdaEventNewHighResArray</code>, <code>pmdaEventResetHighResArray</code>, <code>pmdaEventReleaseHighResArray</code>, <code>pmdaEventAddHighResRecord</code>, <code>pmdaEventAddHighResMissedRecord</code>, <code>pmdaEventHighResAddParam</code>, <code>pmdaEventHighResGetAddr</code> &#8211; utilities for PMDAs to build packed arrays of event records</p>
<h2>C Synopsis</h2>
<pre>#include &lt;pcp/pmapi.h&gt;
#include &lt;pcp/impl.h&gt;
#include &lt;pcp/pmda.h&gt;</pre>
<p>int pmdaEventNewArray(void); </p>
<p> int pmdaEventResetArray(int <i>idx</i>); </p>
<p> int pmdaEventReleaseArray(int <i>idx</i>); </p>
<p> int pmdaEventAddRecord(int <i>idx</i>, struct timeval *<i>tp</i>, int&nbsp;<wbr><i>flags</i>); </p>
<p> int pmdaEventAddMissedRecord(int <i>idx</i>, struct timeval *<i>tp</i>, int&nbsp;<wbr><i>nmissed</i>); </p>
<p> int pmdaEventAddParam(int <i>idx</i>, pmID <i>pmid</i>, int <i>type</i>, pmAtomValue&nbsp;<wbr>*<i>avp</i>); </p>
<p> pmEventArray *pmdaEventGetAddr(int <i>idx</i>); </p>
<p> int pmdaEventNewHighResArray(void); </p>
<p> int pmdaEventResetHighResArray(int <i>idx</i>); </p>
<p> int pmdaEventReleaseHighResArray(int <i>idx</i>); </p>
<p> int pmdaEventAddHighResRecord(int <i>idx</i>, struct timespec *<i>ts</i>, int&nbsp;<wbr><i>flags</i>); </p>
<p> int pmdaEventAddHighResMissedRecord(int <i>idx</i>, struct timespec *<i>ts</i>, int&nbsp;<wbr><i>nmissed</i>); </p>
<p> int pmdaEventHighResAddParam(int <i>idx</i>, pmID <i>pmid</i>, int <i>type</i>, pmAtomValue&nbsp;<wbr>*<i>avp</i>); </p>
<p> pmHighResEventArray *pmdaEventHighResGetAddr(int <i>idx</i>); </p>
<p> cc &#8230; -lpcp</p>
<h2>Description</h2>
<p>A Performance Metrics Domain Agent (PMDA) that wishes to export event records (or trace records) is encouraged to use a metric of either type <code>PM_TYPE_EVENT</code> or <code>PM_TYPE_HIGHRES_EVENT</code> to encode a group of event records into a single packed array. </p>
<p> The only difference between the two metric types is the resolution of the timestamp associated with each &#8211; in high resolution form it is nanosecond scale (see <code><a href="/docs/linux/man/2-clock_gettime/">clock_gettime</a></code>(2)), otherwise it is microseconds (see <code><a href="/docs/linux/man/2-gettimeofday/">gettimeofday</a></code>(2)). For simplicity, we will only refer to the lower resolution API and data structures hereafter &#8211; however, the higher resolution variants are all named similarly and are used in the same way. </p>
<p> The packed array of event records format is defined in <i>&lt;pcp/pmapi.h&gt;</i> and consists of a <code>pmEventArray</code> structure containing a variable number of <code>pmEventRecord</code> structures, each of which contains a variable number of <code>pmEventParameter</code> structures, which in turn may contain a variable length value for each parameter of each event record. </p>
<p> The higher resolution equivalents are defined in the same location, and the structures are named the same. Note that the <code>pmEventParameter</code> structure has no timestamp associated with it, hence it this does not have a high resolution counterpart. </p>
<p> The routines described here are designed to assist the PMDA developer in building a packed array of event records, and managing all of the memory allocations required to hold each instance of an array of event records in a contiguous buffer. Normal use would be as part of PMDA&#8217;s <code>pmdaFetchCallBack</code> method. </p>
<p> <code>pmdaEventNewArray</code> is used to create a new event array. The return value is a small integer that is used as the <i>idx</i> parameter to the other routines to identify a specific event array. If needed, a PMDA can create and use multiple event arrays. </p>
<p> To start a new cycle and refill an event array from the beginning, call <code>pmdaEventResetArray</code>. </p>
<p> If the PMDA has finished with an event array, <code>pmdaEventReleaseArray</code> may be used to release the underlying storage and &#8220;close&#8221; the event array so that subsequent attempts to use <i>idx</i> will return <code>PM_ERR_NOCONTEXT</code>. </p>
<p> To start a new event record, use <code>pmdaEventAddRecord</code>. The timestamp for the event record is given via <i>tp</i> and the <i>flags</i> parameter may be used to set the control field that determines the type of the event record &#8211; <i>flags</i> may be the bit-wise &#8220;or&#8221; of one or more of the <code>PM_EVENT_FLAG_*</code> values defined in <i>&lt;pcp/pmapi.h&gt;</i> (but note that <code>PM_EVENT_FLAG_MISSED</code> should not be used in this context). </p>
<p> If event records have been missed, either because the PMDA cannot keep up or because the PMAPI client cannot keep up, then <code>pmdaEventAddMissedRecord</code> may be used. <i>idx</i> and <i>tp</i> have the same meaning as for <code>pmdaEventAddRecord</code> and <i>nmissed</i> is the number of event records that have been missed at this point in the time-series of event records. <code>pmdaEventAddMissedRecord</code> may be called multiple times for a single batch of event records if there are more than one &#8220;missed event record&#8221; episode. </p>
<p> Once an event record has been started by calling <code>pmdaEventAddRecord</code>, one or more event parameters may be added using <code>pmdaEventAddParam</code>. The <i>pmid</i> and <i>type</i> parameters decribe the PMID of the parameter and the data type (one of the <code>PM_TYPE_*</code> values from <i>&lt;pcp/pmapi.h&gt;</i>) of the value that is passed via <i>avp</i>. <i>type</i> should one where the size of the value is implied by the <i>type</i> or by the length of a string value (for <code>PM_TYPE_STRING</code>) or encoded within <i>avp-&gt;vbp</i> (for <code>PM_TYPE_AGGREGATE</code>). </p>
<p> Once the packed array has been constructed, <code>pmdaEventGetAddr</code> should be used to initialize the <code>ea_type</code> and <code>ea_len</code> fields at the start of the <code>pmEventArray</code> and return the base address of the event array that is assigned to the <code>vp</code> field of the <code>pmAtomValue</code> structure that the <code>pmdaFetchCallBack</code> method should return.</p>
<h2>Example</h2>
<p>The following skeletal code shows how these routines might be used. </p>
<pre><code>int sts;
int myarray;
int first = 1;
pmEventArray eap;

if (first) {
    first = 0;
    if ((myarray = pmdaEventNewArray()) &lt; 0) {
        // report error and fail
    }
}

pmdaEventResetArray(myarray);

// loop over all event records to be exported
...
{
    struct timeval stamp;
    int flags;

    // establish timestamp and set flags to 0 or some combination
    // of PM_EVENT_FLAG_POINT, PM_EVENT_FLAG_START, PM_EVENT_FLAG_ID,
    // etc
    if ((sts = pmdaEventAddRecord(myarray, &amp;stamp, flags)) &lt; 0) {
        // report error and fail
    }

    // loop over all parameters for this event record
    ...
    {
        pmID pmid;
        int type;
        pmAtomValue atom;

        // construct pmid, type and atom for the parameter and
        // its value
        if ((sts = pmdaEventAddParam(myarray, pmid, type, &amp;atom)) &lt; 0) {
            // report error and fail
        }
    }

    // if some event records were missed (could be at the start
    // of the exported set, or at the end, or in the middle, or
    // a combination of multiple missed record episodes)
    ...
    {
        int nmiss;
        struct timeval stamp;

        if ((sts = pmdaEventAddMissedRecord(myarray, &amp;stamp, nmiss)) &lt; 0) {
            // report error and fail
        }
    }
}

// finish up
eap = pmdaEventGetAddr(myarray);</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/2-clock_gettime/">clock_gettime</a></code>(2), <code><a href="/docs/linux/man/2-gettimeofday/">gettimeofday</a></code>(2), <code><a href="/docs/linux/man/3-pmdaeventnewqueue/">pmdaEventNewQueue</a></code>(3), <code><a href="/docs/linux/man/3-pmdaeventnewclient/">pmdaEventNewClient</a></code>(3), <code><a href="/docs/linux/man/3-pmda/">PMDA</a></code>(3) and <code><a href="/docs/linux/man/3-pmeventflagsstr/">pmEventFlagsStr</a></code>(3). </p>
