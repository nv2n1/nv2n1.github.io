---
title: "opapmaquery(1)"
name: "opapmaquery"
section: "1"
letter: "o"
url: "/docs/linux/man/1-opapmaquery/"
description: "opapmaquery"
---

<h2>NAME</h2>
<p> opapmaquery </p>
<p> <code>(All)</code> Performs individual PMA queries against a specific LID. It is very useful in displaying port runtime information.</p>
<h2>Syntax</h2>
<p> opapmaquery [-v] [-s <i>sl</i>] [-l <i>lid</i>] [-h <i>hfi</i>] [-p <i>port</i>] [-o <i>otype</i>]<br />
 [-m <i>port</i>] [-n <i>mask</i>] [-e <i>mask</i>] [-w <i>mask</i>] </p>
<h2>Options</h2>
<dl>
<dt>-v</dt>
<dd> Verbose output. Can be specified more than once for additional openib debugging and libibumad debugging. </dd>
<dt>-s <i>sl</i></dt>
<dd> Specifies different service level. Default is 0. </dd>
<dt>-l <i>lid</i></dt>
<dd> Destination LID. Default is local port. </dd>
<dt>-h <i>hfi</i></dt>
<dd> HFI, numbered 1..n. Using 0 specifies that the -p <i>port</i> port is a system-wide port number. Default is 0. </dd>
<dt>-p <i>port</i></dt>
<dd> Port, numbered 1..n. If -h <i>hfi</i> is 0, then <i>port</i> is a system-wide port number. Default is first active port. </dd>
<dt>-o <i>otype</i></dt>
<dd> Output type. Default is getportstatus. </dd>
<dt>
</dt><dd> Valid output types are:</dd>
<dl>
<dl>
<dt>
</dt><dd>
<p> classportinfo List of port info records. </p>
</dd></dl>
</dl>
<dl>
<dl>
<dt>
</dt><dd>
<p> getportstatus List of port status records. </p>
</dd><dt>
</dt><dd> [-m port] [-w vl mask]</dd></dl>
</dl>
<dl>
<dl>
<dt>
</dt><dd>
<p> clearportstatus Clears the port status. </p>
</dd><dt>
</dt><dd> [-n port mask] [-e counter mask] [-w vl mask]</dd></dl>
</dl>
<dl>
<dl>
<dt>
</dt><dd>
<p> getdatacounters List of data counters. </p>
</dd><dt>
</dt><dd> [-n port mask] [-w vl mask]</dd></dl>
</dl>
<dl>
<dl>
<dt>
</dt><dd>
<p> geterrorcounters List of error counters. </p>
</dd><dt>
</dt><dd> [-n port mask] [-w vl mask]</dd></dl>
</dl>
<dl>
<dl>
<dt>
</dt><dd>
<p> geterrorinfo List of error info. </p>
</dd><dt>
</dt><dd> [-n port mask]</dd></dl>
</dl>
<dl>
<dl>
<dt>
</dt><dd>
<p> clearerrorinfo Clears the error info. </p>
</dd><dt>
</dt><dd> [-n port mask] [-e counter mask]</dd></dl>
</dl>
<dt><code>-h and -p options permit a variety of selections:</code></dt>
<dd>
</dd><dt>-h 0</dt>
<dd> First active port in system (default). </dd>
<dt>-h 0 -p 0</dt>
<dd> First active port in system. </dd>
<dt>-h <i>x</i></dt>
<dd> First active port on HFI <i>x</i>. </dd>
<dt>-h <i>x</i>#8217#160;-p 0</dt>
<dd> First active port on HFI <i>x</i>. </dd>
<dt>-h 0 -p <i>y</i></dt>
<dd> Port <i>y</i>#8217#160;within system (no matter which ports are active). </dd>
<dt>-h <i>x</i>#8217#160;-p <i>y</i></dt>
<dd> HFI <i>x</i>, port <i>y</i>. </dd>
<dt><code>otype options vary by report</code></dt>
<dd>
</dd><dt>-m <i>port</i></dt>
<dd> Port in destination device to query/clear. Required when using -l option for all but -o classportinfo. </dd>
<dt>-n <i>mask</i></dt>
<dd> Port mask, in hexadecimal. Bits represent ports 63-0. For example: 0x2 for port 1, 0x6 for ports 1, 2. </dd>
<dt>-e <i>mask</i></dt>
<dd> Counter/error select mask, in hexadecimal. The following lists &quot;Mask &#8211; Bit &#8211; Location for Counters&quot;. Where applicable, location &quot;for Error Info&quot; is presented. The default is all bits set (0xffffffe0). </dd>
<dl>
<dl>
<dt>&bull;</dt>
<dd> 0x80000000 &#8211; 31 &#8211; Transmit Data For Error Info: Receive Error Info </dd>
<dt>&bull;</dt>
<dd> 0x40000000 &#8211; 30 &#8211; Receive Data For Error Info: Excessive Buffer Overrun </dd>
<dt>&bull;</dt>
<dd> 0x20000000 &#8211; 29 &#8211; Transmit Packets For Error Info: Transmit Const Error Info </dd>
<dt>&bull;</dt>
<dd> 0x10000000 &#8211; 28 &#8211; Receive Packets For Error Info: Receive Const Error Info </dd>
<dt>&bull;</dt>
<dd> 0x08000000 &#8211; 27 &#8211; Multicast Transmit Packets For Error Info: Receive Switch Relay Error Info </dd>
<dt>&bull;</dt>
<dd> 0x04000000 &#8211; 26 &#8211; Multicast Receive Packets For Error Info: Uncorrectable Error Info </dd>
<dt>&bull;</dt>
<dd> 0x02000000 &#8211; 25 &#8211; Transmit Wait For Error Info: FM Configuration Error Info </dd>
<dt>&bull;</dt>
<dd> 0x01000000 &#8211; 24 &#8211; Congestion Discards </dd>
<dt>&bull;</dt>
<dd> 0x00800000 &#8211; 23 &#8211; Receive FECN </dd>
<dt>&bull;</dt>
<dd> 0x00400000 &#8211; 22 &#8211; Receive BECN </dd>
<dt>&bull;</dt>
<dd> 0x00200000 &#8211; 21 &#8211; Transmit Time Cong. </dd>
<dt>&bull;</dt>
<dd> 0x00100000 &#8211; 20 &#8211; Transmit Time Wasted BW </dd>
<dt>&bull;</dt>
<dd> 0x00080000 &#8211; 19 &#8211; Transmit Time Wait Data </dd>
<dt>&bull;</dt>
<dd> 0x00040000 &#8211; 18 &#8211; Receive Bubble </dd>
<dt>&bull;</dt>
<dd> 0x00020000 &#8211; 17 &#8211; Mark FECN </dd>
<dt>&bull;</dt>
<dd> 0x00010000 &#8211; 16 &#8211; Receive Constraint Errors </dd>
<dt>&bull;</dt>
<dd> 0x00008000 &#8211; 15 &#8211; Receive Switch Relay </dd>
<dt>&bull;</dt>
<dd> 0x00004000 &#8211; 14 &#8211; Transmit Discards </dd>
<dt>&bull;</dt>
<dd> 0x00002000 &#8211; 13 &#8211; Transmit Constraint Errors </dd>
<dt>&bull;</dt>
<dd> 0x00001000 &#8211; 12 &#8211; Receive Remote Physical Errors </dd>
<dt>&bull;</dt>
<dd> 0x00000800 &#8211; 11 &#8211; Local Link Integrity </dd>
<dt>&bull;</dt>
<dd> 0x00000400 &#8211; 10 &#8211; Receive Errors </dd>
<dt>&bull;</dt>
<dd> 0x00000200 &#8211; 9 &#8211; Exc. Buffer Overrun </dd>
<dt>&bull;</dt>
<dd> 0x00000100 &#8211; 8 &#8211; FM Configuration Errors </dd>
<dt>&bull;</dt>
<dd> 0x00000080 &#8211; 7 &#8211; Link Error Recovery </dd>
<dt>&bull;</dt>
<dd> 0x00000040 &#8211; 6 &#8211; Link Error Downed </dd>
<dt>&bull;</dt>
<dd> 0x00000020 &#8211; 5 &#8211; Uncorrectable Errors </dd>
</dl>
</dl>
<dt>-w <i>mask</i></dt>
<dd> Virtual Lane Select Mask, in hexadecimal. Bits represent VL number 31-0. For example, 0x1 for VL 0, 0x3 for VL 0,1. Default is none. </dd>
</dl>
<h2>Examples</h2>
<p> opapmaquery -o classportinfo </p>
<p> opapmaquery -o getportstatus<br />
 # get data and error counts, local port </p>
<p> opapmaquery -o getdatacounters -n 0x2<br />
 # get data counts, local port 1 </p>
<p> opapmaquery -o geterrorcounters -n 0x2<br />
 # get error counts, local port 1 </p>
<p> opapmaquery -o clearportstatus -n 0x2<br />
 # clear all counters local port 1 </p>
<p> opapmaquery -o geterrorinfo -n 0x2<br />
 # get error info for local port 1 </p>
<p> opapmaquery -o clearerrorinfo -n 0x2<br />
 # clear all error info, local port 1 </p>
<p> <code>Additional Examples</code> </p>
<p> opapmaquery -o getdatacounters -l 6 -n 0x7e -w 0x1<br />
 # for device at LID 6, get data counters on ports 1-6, inclusive of VL 0 data </p>
<p> opapmaquery -o clearportstatus -l 6 -n 0x2 -e 0x1ffff<br />
 # for device at LID 6, on port 1, clear only error counters </p>
<p> opapmaquery -o clearerrorinfo -l 6 -n 0x2 -e 0x04000000<br />
 # for device at LID 6, on ports 1, clear uncorrectable error info </p>
<h2>Index</h2>
