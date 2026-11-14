---
title: "papi_decode(1)"
name: "papi_decode"
section: "1"
letter: "p"
url: "/docs/linux/man/1-papi_decode/"
---

<h2 class="name">NAME</h2>
 

 papi_decode - papi_decode utility. 

 file decode.c 

<h2 class="name">NAME</h2>
 

 

 papi_decode - provides availability and detail information for PAPI preset events. 

<h2>Synopsis</h2>

 

 papi_decode [-ah]

<h2>Description</h2>

 

 papi_decode is a PAPI utility program that converts the PAPI presets for the existing library into a comma separated value format that can then be viewed or modified in spreadsheet applications or text editors, and can be supplied to PAPI_encode_events (3) as a way of adding or modifying event definitions for specialized applications. The format for the csv output consists of a line of field names, followed by a blank line, followed by one line of comma separated values for each event contained in the preset table. A portion of this output (for Pentium 4) is shown below: 

 <pre>
*       name,derived,postfix,short_descr,long_descr,note,[native,...]
*       PAPI_L1_ICM,NOT_DERIVED,,&quot;L1I cache misses&quot;,&quot;Level 1 instruction cache misses&quot;,,BPU_fetch_request_TCMISS
*       PAPI_L2_TCM,NOT_DERIVED,,&quot;L2 cache misses&quot;,&quot;Level 2 cache misses&quot;,,BSQ_cache_reference_RD_2ndL_MISS_WR_2ndL_MISS
*       PAPI_TLB_DM,NOT_DERIVED,,&quot;Data TLB misses&quot;,&quot;Data translation lookaside buffer misses&quot;,,page_walk_type_DTMISS
* 
</pre> 

<h2>Options</h2>

 

<dl>
<dt>&bull;
<dd> -a Convert only the available PAPI preset events.
<dt>&bull;
<dd> -h Display help information about this utility.</dl>
 

<h2>Bugs</h2>

 

 There are no known bugs in this utility. If you find a bug, it should be reported to the PAPI Mailing List at ptools-perfapi [at] ptools.org. 

<h2>Index</h2>


