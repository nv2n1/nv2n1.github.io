---
title: "xentrace(8)"
name: "xentrace"
section: "8"
letter: "x"
url: "/docs/linux/man/8-xentrace/"
description: "xentrace – capture Xen trace buffer data"
---

<p>xentrace &#8211; capture Xen trace buffer data</p>
<h2>Synopsis</h2>
<p><code>xentrace</code> [ <i>OPTIONS</i> ] [ <i>FILE</i> ]</p>
<h2>Description</h2>
<p><code>xentrace</code> is used to capture trace buffer data from Xen. The data is output in the following binary format (host endian):<br />
&nbsp;<wbr>CPU(uint)&nbsp;<wbr>TSC(u64)&nbsp;<wbr>EVENT(u32)&nbsp;<wbr>D1 D2 D3 D4 D5&nbsp;<wbr>(all u32) Where CPU is the processor number, TSC is the record&#8217;s timestamp (the value of the CPU cycle counter), EVENT is the event ID and D1&#8230;D5 are the trace data. Data is dumped onto the standard output (which must not be a TTY) or a <i>FILE</i> specified on the command line. The output should be parsed using the tool xentrace_format, which can produce human-readable output in ASCII format.</p>
<h3>Options</h3>
<dl>
<dt><code>-t, &#8211;log-thresh=l</code></p>
<dd>set the threshold number, l, of new records required to trigger a write of all new records to the output</p>
<dt><code>-s, &#8211;poll-sleep=p</code></p>
<dd>set the time, p, (in milliseconds) to sleep between polling the buffers for new data.</p>
<dt><code>-c, &#8211;cpu-mask=c</code></p>
<dd>set cpu-mask</p>
<dt><code>-e, &#8211;evt-mask=e</code></p>
<dd>set evt-mask</p>
<dt><code>-?, &#8211;help</code></p>
<dd>Give this help list</p>
<dt><code>&#8211;usage</code></p>
<dd>Give a short usage message</p>
<dt><code>-V, &#8211;version</code></p>
<dd>Print program version</dl>
<h3>Event Classes (Masks)</h3>
<p>The following event classes (masks) can be used to filter the events being gathered by xentrace:<br />
&nbsp;<wbr>&nbsp;<wbr><i>ID</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><i>Description</i><br />
&nbsp;<wbr>&nbsp;<wbr>0x0001f000&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>TRC_GEN<br />
&nbsp;<wbr>&nbsp;<wbr>0x0002f000&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>TRC_SCHED<br />
&nbsp;<wbr>&nbsp;<wbr>0x0004f000&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>TRC_DOM0OP<br />
&nbsp;<wbr>&nbsp;<wbr>0x0008f000&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>TRC_HVM<br />
&nbsp;<wbr>&nbsp;<wbr>0x0010f000&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>TRC_MEM<br />
&nbsp;<wbr>&nbsp;<wbr>0xfffff000&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>TRC_ALL</p>
<h3>Event Subclasses (More Masks)</h3>
<p>The following event subclasses (masks) can also be used to filter the events being gathered by xentrace:<br />
&nbsp;<wbr>&nbsp;<wbr><i>ID</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><i>Description</i><br />
&nbsp;<wbr>&nbsp;<wbr>0x00081000&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>TRC_HVM_ENTRYEXIT<br />
&nbsp;<wbr>&nbsp;<wbr>0x00082000&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>TRC_HVM_HANDLER</p>
<h3>Events</h3>
<p><code>xentrace</code> collects the following events from the trace buffer:<br />
&nbsp;<wbr>&nbsp;<wbr><i>ID</i>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><i>Description</i><br />
&nbsp;<wbr>&nbsp;<wbr>0x0001f001&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>TRC_LOST_RECORDS<br />
&nbsp;<wbr>&nbsp;<wbr>0x0002f001&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>TRC_SCHED_DOM_ADD<br />
&nbsp;<wbr>&nbsp;<wbr>0x0002f002&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>TRC_SCHED_DOM_REM<br />
&nbsp;<wbr>&nbsp;<wbr>0x0002f003&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>TRC_SCHED_SLEEP<br />
&nbsp;<wbr>&nbsp;<wbr>0x0002f004&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>TRC_SCHED_WAKE<br />
&nbsp;<wbr>&nbsp;<wbr>0x0002f005&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>TRC_SCHED_YIELD<br />
&nbsp;<wbr>&nbsp;<wbr>0x0002f006&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>TRC_SCHED_BLOCK<br />
&nbsp;<wbr>&nbsp;<wbr>0x0002f007&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>TRC_SCHED_SHUTDOWN<br />
&nbsp;<wbr>&nbsp;<wbr>0x0002f008&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>TRC_SCHED_CTL<br />
&nbsp;<wbr>&nbsp;<wbr>0x0002f009&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>TRC_SCHED_ADJDOM<br />
&nbsp;<wbr>&nbsp;<wbr>0x0002f010&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>TRC_SCHED_SWITCH<br />
&nbsp;<wbr>&nbsp;<wbr>0x0002f011&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>TRC_SCHED_S_TIMER_FN<br />
&nbsp;<wbr>&nbsp;<wbr>0x0002f012&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>TRC_SCHED_T_TIMER_FN<br />
&nbsp;<wbr>&nbsp;<wbr>0x0002f013&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>TRC_SCHED_DOM_TIMER_FN<br />
&nbsp;<wbr>&nbsp;<wbr>0x0002f014&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>TRC_SCHED_SWITCH_INFPREV<br />
&nbsp;<wbr>&nbsp;<wbr>0x0002f015&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>TRC_SCHED_SWITCH_INFNEXT<br />
&nbsp;<wbr>&nbsp;<wbr>0x00081001&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>TRC_HVM_VMENTRY<br />
&nbsp;<wbr>&nbsp;<wbr>0x00081002&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>TRC_HVM_VMEXIT<br />
&nbsp;<wbr>&nbsp;<wbr>0x00082001&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>TRC_HVM_PF_XEN<br />
&nbsp;<wbr>&nbsp;<wbr>0x00082002&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>TRC_HVM_PF_INJECT<br />
&nbsp;<wbr>&nbsp;<wbr>0x00082003&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>TRC_HVM_INJ_EXC<br />
&nbsp;<wbr>&nbsp;<wbr>0x00082004&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>TRC_HVM_INJ_VIRQ<br />
&nbsp;<wbr>&nbsp;<wbr>0x00082005&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>TRC_HVM_REINJ_VIRQ<br />
&nbsp;<wbr>&nbsp;<wbr>0x00082006&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>TRC_HVM_IO_READ<br />
&nbsp;<wbr>&nbsp;<wbr>0x00082007&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>TRC_HVM_IO_WRITE<br />
&nbsp;<wbr>&nbsp;<wbr>0x00082008&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>TRC_HVM_CR_READ<br />
&nbsp;<wbr>&nbsp;<wbr>0x00082009&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>TRC_HVM_CR_WRITE<br />
&nbsp;<wbr>&nbsp;<wbr>0x0008200A&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>TRC_HVM_DR_READ<br />
&nbsp;<wbr>&nbsp;<wbr>0x0008200B&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>TRC_HVM_DR_WRITE<br />
&nbsp;<wbr>&nbsp;<wbr>0x0008200C&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>TRC_HVM_MSR_READ<br />
&nbsp;<wbr>&nbsp;<wbr>0x0008200D&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>TRC_HVM_MSR_WRITE<br />
&nbsp;<wbr>&nbsp;<wbr>0x0008200E&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>TRC_HVM_CPUID<br />
&nbsp;<wbr>&nbsp;<wbr>0x0008200F&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>TRC_HVM_INTR<br />
&nbsp;<wbr>&nbsp;<wbr>0x00082010&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>TRC_HVM_NMI&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>0x00082011&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>TRC_HVM_SMI&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>0x00082012&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>TRC_HVM_VMMCALL<br />
&nbsp;<wbr>&nbsp;<wbr>0x00082013&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>TRC_HVM_HLT<br />
&nbsp;<wbr>&nbsp;<wbr>0x00082014&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>TRC_HVM_INVLPG<br />
&nbsp;<wbr>&nbsp;<wbr>0x0010f001&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>TRC_MEM_PAGE_GRANT_MAP<br />
&nbsp;<wbr>&nbsp;<wbr>0x0010f002&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>TRC_MEM_PAGE_GRANT_UNMAP<br />
&nbsp;<wbr>&nbsp;<wbr>0x0010f003&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>TRC_MEM_PAGE_GRANT_TRANSFER </p>
<h2>Author</h2>
<p>Mark A. Williamson &lt;mark.a.williamson [at] intel.com&gt;</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-xentrace_format/">xentrace_format</a>(1) </p>
