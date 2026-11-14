---
title: "spu_run(2)"
name: "spu_run"
section: "2"
letter: "s"
url: "/docs/linux/man/2-spu_run/"
description: "spu_run – execute an SPU context"
---

<h2 class="name">NAME</h2>
<p> spu_run &#8211; execute an SPU context </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;sys/spu.h&gt;
int spu_run(int fd, unsigned int *npc, unsigned int *event);
</code></pre>
<p> <i>Note</i>: There is no glibc wrapper for this system call; see NOTES.</p>
<h2>DESCRIPTION</h2>
<p> The <code>spu_run</code>() system call is used on PowerPC machines that implement the Cell Broadband Engine Architecture in order to access Synergistic Processor Units (SPUs). The <i>fd</i> argument is a file descriptor returned by <code><a href="/docs/linux/man/2-spu_create/">spu_create</a></code>(2) that refers to a specific SPU context. When the context gets scheduled to a physical SPU, it starts execution at the instruction pointer passed in <i>npc</i>. </p>
<p> Execution of SPU code happens synchronously, meaning that <code>spu_run</code>() blocks while the SPU is still running. If there is a need to execute SPU code in parallel with other code on either the main CPU or other SPUs, a new thread of execution must be created first (e.g., using <code><a href="/docs/linux/man/3-pthread_create/">pthread_create</a></code>(3)). </p>
<p> When <code>spu_run</code>() returns, the current value of the SPU program counter is written to <i>npc</i>, so successive calls to <code>spu_run</code>() can use the same <i>npc</i> pointer. </p>
<p> The <i>event</i> argument provides a buffer for an extended status code. If the SPU context was created with the <code>SPU_CREATE_EVENTS_ENABLED</code> flag, then this buffer is populated by the Linux kernel before <code>spu_run</code>() returns. </p>
<p> The status code may be one (or more) of the following constants:</p>
<dl>
<dt><code>SPE_EVENT_DMA_ALIGNMENT</code></p>
<dd> A DMA alignment error occurred.</p>
<dt><code>SPE_EVENT_INVALID_DMA</code></p>
<dd> An invalid MFC DMA command was attempted.</p>
<dt><code>SPE_EVENT_SPE_DATA_STORAGE</code></p>
<dd> A DMA storage error occurred.</p>
<dt><code>SPE_EVENT_SPE_ERROR</code></p>
<dd> An illegal instruction was executed.</dl>
<p> NULL is a valid value for the <i>event</i> argument. In this case, the events will not be reported to the calling process.</p>
<h2>RETURN VALUE</h2>
<p> On success, <code>spu_run</code>() returns the value of the <i>spu_status</i> register. On error, it returns -1 and sets <i>errno</i> to one of the error codes listed below. </p>
<p> The <i>spu_status</i> register value is a bit mask of status codes and optionally a 14-bit code returned from the <code>stop-and-signal</code> instruction on the SPU. The bit masks for the status codes are:</p>
<dl>
<dt><code>0x02</code></p>
<dd> SPU was stopped by a <code>stop-and-signal</code> instruction.</p>
<dt><code>0x04</code></p>
<dd> SPU was stopped by a <code>halt</code> instruction.</p>
<dt><code>0x08</code></p>
<dd> SPU is waiting for a channel.</p>
<dt><code>0x10</code></p>
<dd> SPU is in single-step mode.</p>
<dt><code>0x20</code></p>
<dd> SPU has tried to execute an invalid instruction.</p>
<dt><code>0x40</code></p>
<dd> SPU has tried to access an invalid channel.</p>
<dt><code>0x3fff0000</code></p>
<dd> The bits masked with this value contain the code returned from a <code>stop-and-signal</code> instruction. These bits are valid only if the 0x02 bit is set.</dl>
<p> If <code>spu_run</code>() has not returned an error, one or more bits among the lower eight ones are always set.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EBADF</code></p>
<dd> <i>fd</i> is not a valid file descriptor.</p>
<dt><code>EFAULT</code></p>
<dd> <i>npc</i> is not a valid pointer, or <i>event</i> is non-NULL and an invalid pointer.</p>
<dt><code>EINTR</code></p>
<dd> A signal occurred while <code>spu_run</code>() was in progress; see <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7). The <i>npc</i> value has been updated to the new program counter value if necessary.</p>
<dt><code>EINVAL</code></p>
<dd> <i>fd</i> is not a valid file descriptor returned from <code><a href="/docs/linux/man/2-spu_create/">spu_create</a></code>(2).</p>
<dt><code>ENOMEM</code></p>
<dd> There was not enough memory available to handle a page fault resulting from a Memory Flow Controller (MFC) direct memory access.</p>
<dt><code>ENOSYS</code></p>
<dd> The functionality is not provided by the current system, because either the hardware does not provide SPUs or the spufs module is not loaded.</dl>
<h2>VERSIONS</h2>
<p> The <code>spu_run</code>() system call was added to Linux in kernel 2.6.16.</p>
<h2>CONFORMING TO</h2>
<p> This call is Linux-specific and implemented only by the PowerPC architecture. Programs using this system call are not portable.</p>
<h2>NOTES</h2>
<p> Glibc does not provide a wrapper for this system call; call it using <code><a href="/docs/linux/man/2-syscall/">syscall</a></code>(2). Note however, that <code>spu_run</code>() is meant to be used from libraries that implement a more abstract interface to SPUs, not to be used from regular applications. See for the recommended libraries.</p>
<h2>EXAMPLES</h2>
<p> The following is an example of running a simple, one-instruction SPU program with the <code>spu_run</code>() system call. </p>
<p> #include &lt;stdlib.h&gt; #include &lt;stdint.h&gt; #include &lt;unistd.h&gt; #include &lt;stdio.h&gt; #include &lt;sys/types.h&gt; #include &lt;fcntl.h&gt; </p>
<p> #define handle_error(msg) \<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;do&nbsp;{&nbsp;perror(msg);&nbsp;exit(EXIT_FAILURE);&nbsp;}&nbsp;while&nbsp;(0) </p>
<p> int main(void) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int context, fd, spu_status;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t instruction, npc; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;context&nbsp;=&nbsp;spu_create(&quot;/spu/example-context&quot;, 0, 0755);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(context&nbsp;==&nbsp;-1)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;handle_error(&quot;spu_create&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;write a&nbsp;&#8216;stop 0x1234&#8217;&nbsp;instruction to the SPU&#8217;s<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*&nbsp;local store memory<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;instruction&nbsp;=&nbsp;0x00001234; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fd&nbsp;=&nbsp;open(&quot;/spu/example-context/mem&quot;, O_RDWR);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(fd&nbsp;==&nbsp;-1)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;handle_error(&quot;open&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;write(fd,&nbsp;&amp;instruction, sizeof(instruction)); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;set npc to the starting instruction address of the<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*&nbsp;SPU program. Since we wrote the instruction at the<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*&nbsp;start of the mem file, the entry point will be 0x0<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;npc&nbsp;=&nbsp;0; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;spu_status&nbsp;=&nbsp;spu_run(context,&nbsp;&amp;npc, NULL);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(spu_status&nbsp;==&nbsp;-1)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;handle_error(&quot;open&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;we should see a status code of 0x1234002:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*&nbsp;<wbr>&nbsp;<wbr>&nbsp;0x00000002&nbsp;(spu was stopped due to stop-and-signal)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*&nbsp;| 0x12340000&nbsp;(the stop-and-signal code)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;SPU Status:&nbsp;%#08x
&quot;, spu_status); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS); }</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-close/">close</a></code>(2), <code><a href="/docs/linux/man/2-spu_create/">spu_create</a></code>(2), <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7), <code><a href="/docs/linux/man/7-spufs/">spufs</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
