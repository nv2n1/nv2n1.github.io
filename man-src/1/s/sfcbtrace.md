---
title: "sfcbtrace(1)"
name: "sfcbtrace"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sfcbtrace/"
description: "sfcbtrace – toggle the tracemask for SFCB trace output"
---

<h2>NAME</h2>
<p> sfcbtrace &#8211; toggle the tracemask for SFCB trace output</p>
<h2>SYNOPSIS</h2>
<p> <code>sfcbtrace</code> &lt;trace_mask&gt; &lt;shm_key&gt;</p>
<h2>OPTIONS</h2>
<dl>
<dt>trace_mask &#8211; an unsigned long or hex value for component(s) to trace (default=0)</p>
<dd>
<dt>shm_key &#8211; the shared memory ID being used by SFCB (default=deb001)</p>
<dd></dl>
<p> Traceable Components: Int Hex<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>providerMgr:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0x00001<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>providerDrv:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>2&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0x00002<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>cimxmlProc:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>4&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0x00004<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>httpDaemon:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>8&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0x00008<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>upCalls:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>16&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0x00010<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>encCalls:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>32&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0x00020<br />
&nbsp;<wbr>&nbsp;<wbr>ProviderInstMgr:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>64&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0x00040<br />
&nbsp;<wbr>providerAssocMgr:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>128&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0x00080<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>providers:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>256&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0x00100<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>indProvider:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>512&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0x00200<br />
&nbsp;<wbr>internalProvider:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1024&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0x00400<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>objectImpl:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>2048&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0x00800<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>xmlIn:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>4096&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0x01000<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>xmlOut:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>8192&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0x02000<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>sockets:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>16384&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0x04000<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>memoryMgr:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>32768&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0x08000<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>msgQueue:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>65536&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>0x10000<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>xmlParsing:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>131072&nbsp;<wbr>&nbsp;<wbr>0x20000<br />
responseTiming:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>262144&nbsp;<wbr>&nbsp;<wbr>0x40000<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>dbpdaemon:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>524288&nbsp;<wbr>&nbsp;<wbr>0x80000<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>slp:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1048576 0x100000 </p>
<h2>Index</h2>
