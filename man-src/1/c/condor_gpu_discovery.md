---
title: "condor_gpu_discovery(1)"
name: "condor_gpu_discovery"
section: "1"
letter: "c"
url: "/docs/linux/man/1-condor_gpu_discovery/"
description: "condor_gpu_discovery Output GPU-related ClassAd attributes"
---

<h2>Name</h2>
<p> <i>condor_gpu_discovery</i> Output GPU-related ClassAd attributes </p>
<h2>Synopsis</h2>
<p> <i>condor_gpu_discovery</i> <code>-help</code> </p>
<p> <i>condor_gpu_discovery</i> [ <code>&lt;options&gt;</code> ] </p>
<h2>Description</h2>
<p> <i>condor_gpu_discovery</i> runs discovery software to determine the host&#8217;s GPU capabilities, which are output as ClassAd attributes. </p>
<p> This tool is not available for MAC OS platforms. </p>
<p> With no command line options, the single ClassAd attribute DetectedGPUs is printed. If the value is 0, no GPUs were detected. If one or more GPUS were detected, the value is a string, presented as a comma and space separated list of the GPUs discovered, where each is given a name further used as the <i>prefix string</i> in other attribute names. Where there is more than one GPU of a particular type, the <i>prefix string</i> includes an integer value numbering the device; these integer values monotonically increase from 0. For example, a discovery of two GPUs may output </p>
<p> DetectedGPUs=&quot;CUDA0, CUDA1&quot; </p>
<p> Further command line options use &quot;CUDA&quot; either with or without one of the integer values 0 or 1 as the <i>prefix string</i> in attribute names. </p>
<h2>Options</h2>
<p> <code>-help</code></p>
<dl>
<dt>
<dd> Print usage information and exit.</p>
<dt>
<dd></dl>
<p> <code>-properties</code></p>
<dl>
<dt>
<dd> In addition to the DetectedGPUs attribute, display standard CUDA attributes. Each of these attribute names will have a <i>prefix string</i> at the beginning of its name. For a host with more than one of the same GPU type, those attribute values that are the same across all of the GPUs will not have an integer value in the <i>prefix string</i> . The attributes are Capability , DeviceName , DriverVersion , ECCEnabled , GlobalMemoryMb , and RuntimeVersion . The displayed standard Open CL attributes are DeviceName , ECCEnabled , OpenCLVersion , and GlobalMemoryMb .</p>
<dt>
<dd></dl>
<p> <code>-extra</code></p>
<dl>
<dt>
<dd> Display the additional attributes of Each of these attribute names will have a <i>prefix string</i> at the beginning of its name. ClockMhz , ComputeUnits , and CoresPerCU for a CUDA device, and ClockMhz and ComputeUnits for an OCL device.</p>
<dt>
<dd></dl>
<p> <code>-dynamic</code></p>
<dl>
<dt>
<dd> Display attributes of NVIDIA devices that change values as the GPU is working. Each of these attribute names will have a <i>prefix string</i> at the beginning of its name. These are FanSpeedPct , BoardTempC , DieTempC , EccErrorsSingleBit , and EccErrorsDoubleBit .</p>
<dt>
<dd></dl>
<p> <code>-mixed</code></p>
<dl>
<dt>
<dd> When displaying attribute values, assume that the machine has a heterogeneous set of GPUs, so always include the integer value in the <i>prefix string</i> .</p>
<dt>
<dd></dl>
<p> <code>-device </code> <i>&lt;N&gt;</i></p>
<dl>
<dt>
<dd> Display properties only for GPU device <i>&lt;N&gt;</i> , where <i>&lt;N&gt;</i> is the integer value defined for the <i>prefix string</i> . Note that the attribute names in this output will <i>not</i> contain the value for <i>&lt;N&gt;</i> .</p>
<dt>
<dd></dl>
<p> <code>-tag </code> <i>string</i></p>
<dl>
<dt>
<dd> Set the resource tag portion of the intended machine ClassAd attribute Detected&lt;ResourceTag&gt; to be <i>string</i> . If this option is not specified, the resource tag is &quot;GPUs&quot; , resulting in attribute name DetectedGPUs .</p>
<dt>
<dd></dl>
<p> <code>-prefix </code> <i>str</i></p>
<dl>
<dt>
<dd> When naming attributes, use <i>str</i> as the <i>prefix string</i> . When this option is not specified, the <i>prefix string</i> is either CUDA or OCL .</p>
<dt>
<dd></dl>
<p> <code>-simulate:D,N</code></p>
<dl>
<dt>
<dd> For testing purposes, assume that N devices of type D were detected. No discovery software is invoked. If D is 0, it refers to GeForce GT 330, and a default value for N is 1. If D is 1, it refers to GeForce GTX 480, and a default value for N is 2.</p>
<dt>
<dd></dl>
<p> <code>-opencl</code></p>
<dl>
<dt>
<dd> Prefer detection via OpenCL rather than CUDA. Without this option, CUDA detection software is invoked first, and no further Open CL software is invoked if CUDA devices are detected.</p>
<dt>
<dd></dl>
<p> <code>-cuda</code></p>
<dl>
<dt>
<dd> Do only CUDA detection.</p>
<dt>
<dd></dl>
<p> <code>-nvcuda</code></p>
<dl>
<dt>
<dd> For Windows platforms only, use a CUDA driver rather than the CUDA run time.</p>
<dt>
<dd></dl>
<p> <code>-config</code></p>
<dl>
<dt>
<dd> Output in the syntax of HTCondor configuration, instead of ClassAd language. An additional attribute is produced NUM_DETECTED_GPUs which is set to the number of GPUs detected.</p>
<dt>
<dd></dl>
<p> <code>-verbose</code></p>
<dl>
<dt>
<dd> For interactive use of the tool, output extra information to show detection while in progress.</p>
<dt>
<dd></dl>
<p> <code>-diagnostic</code></p>
<dl>
<dt>
<dd> Show diagnostic information, to aid in tool development.</p>
<dt>
<dd></dl>
<h2>Exit Status</h2>
<p> <i>condor_gpu_discovery</i> will exit with a status value of 0 (zero) upon success, and it will exit with the value 1 (one) upon failure. </p>
<h2>Author</h2>
<p> Center for High Throughput Computing, University of Wisconsin-Madison</p>
<h2>Copyright</h2>
<p> Copyright (C) 1990-2015 Center for High Throughput Computing, Computer Sciences Department, University of Wisconsin-Madison, Madison, WI. All Rights Reserved. Licensed under the Apache License, Version 2.0. </p>
<h2>Index</h2>
