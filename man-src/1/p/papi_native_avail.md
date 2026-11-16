---
title: "papi_native_avail(1)"
name: "papi_native_avail"
section: "1"
letter: "p"
url: "/docs/linux/man/1-papi_native_avail/"
---

<h2 class="name">NAME</h2>
 

 papi_native_avail - papi_native_avail utility. 

 file native_avail.c 

<h2 class="name">NAME</h2>
 

 

 papi_native_avail - provides detailed information for PAPI native events. 

<h2>Synopsis</h2>

 

<h2>Description</h2>

 

 papi_native_avail is a PAPI utility program that reports information about the native events available on the current platform. A native event is an event specific to a specific hardware platform. On many platforms, a specific native event may have a number of optional settings. In such cases, the native event and the valid settings are presented, rather than every possible combination of those settings. For each native event, a name, a description, and specific bit patterns are provided.

<h2>Options</h2>

 

<dl>
<dt>&bull;
</dt><dd> --help, -h print this help message
</dd><dt>&bull;
</dt><dd> -d display detailed information about native events
</dd><dt>&bull;
</dt><dd> -e EVENTNAME display detailed information about named native event
</dd><dt>&bull;
</dt><dd> -i EVENTSTR include only event names that contain EVENTSTR
</dd><dt>&bull;
</dt><dd> -x EVENTSTR exclude any event names that contain EVENTSTR
</dd><dt>&bull;
</dt><dd> --noumasks suppress display of Unit Mask information</dd></dl>
 

 

 Processor-specific options 

<dl>
<dt>&bull;
</dt><dd> --darr display events supporting Data Address Range Restriction
</dd><dt>&bull;
</dt><dd> --dear display Data Event Address Register events only
</dd><dt>&bull;
</dt><dd> --iarr display events supporting Instruction Address Range Restriction
</dd><dt>&bull;
</dt><dd> --iear display Instruction Event Address Register events only
</dd><dt>&bull;
</dt><dd> --opcm display events supporting OpCode Matching
</dd><dt>&bull;
</dt><dd> --nogroups suppress display of Event grouping information</dd></dl>
 

<h2>Bugs</h2>

 

 There are no known bugs in this utility. If you find a bug, it should be reported to the PAPI Mailing List at ptools-perfapi [at] ptools.org. 

<h2>Index</h2>


