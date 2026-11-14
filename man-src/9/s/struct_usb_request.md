---
title: "struct_usb_request(9)"
name: "struct_usb_request"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_usb_request/"
description: "struct_usb_request – describes one i/o request"
---

<p>struct_usb_request &#8211; describes one i/o request</p>
<h2>Synopsis</h2>
<pre><code>struct usb_request {
    void *buf;
    unsigned length;
    dma_addr_t dma;
    struct scatterlist *sg;
    unsigned num_sgs;
    unsigned num_mapped_sgs;
    unsigned stream_id : 16;
    unsigned no_interrupt : 1;
    unsigned zero : 1;
    unsigned short_not_ok : 1;
    void (*complete)(struct usb_ep *ep, struct usb_request *req);
    void *context;
    struct list_head list;
    int status;
    unsigned actual;
};</code></pre>
<h2>Members</h2>
<p>buf</p>
<dl>
<dd>Buffer used for data. Always provide this; some controllers only use PIO, or don&#8217;t use DMA for some endpoints.</dl>
<p> length</p>
<dl>
<dd>Length of that data</dl>
<p> dma</p>
<dl>
<dd>DMA address corresponding to &#8216;buf&#8217;. If you don&#8217;t set this field, and the usb controller needs one, it is responsible for mapping and unmapping the buffer.</dl>
<p> sg</p>
<dl>
<dd>a scatterlist for SG-capable controllers.</dl>
<p> num_sgs</p>
<dl>
<dd>number of SG entries</dl>
<p> num_mapped_sgs</p>
<dl>
<dd>number of SG entries mapped to DMA (internal)</dl>
<p> stream_id</p>
<dl>
<dd>The stream id, when USB3.0 bulk streams are being used</dl>
<p> no_interrupt</p>
<dl>
<dd>If true, hints that no completion irq is needed. Helpful sometimes with deep request queues that are handled directly by DMA controllers.</dl>
<p> zero</p>
<dl>
<dd>If true, when writing data, makes the last packet be &#8220;short&#8221; by adding a zero length packet as needed;</dl>
<p> short_not_ok</p>
<dl>
<dd>When reading data, makes short packets be treated as errors (queue stops advancing till cleanup).</dl>
<p> complete</p>
<dl>
<dd>Function called when request completes, so this request and its buffer may be re-used. The function will always be called with interrupts disabled, and it must not sleep. Reads terminate with a short packet, or when the buffer fills, whichever comes first. When writes terminate, some data bytes will usually still be in flight (often in a hardware fifo). Errors (for reads or writes) stop the queue from advancing until the completion function returns, so that any transfers invalidated by the error may first be dequeued.</dl>
<p> context</p>
<dl>
<dd>For use by the completion callback</dl>
<p> list</p>
<dl>
<dd>For use by the gadget driver.</dl>
<p> status</p>
<dl>
<dd>Reports completion code, zero or a negative errno. Normally, faults block the transfer queue from advancing until the completion callback returns. Code &#8220;-ESHUTDOWN&#8221; indicates completion caused by device disconnect, or when the driver disabled the endpoint.</dl>
<p> actual</p>
<dl>
<dd>Reports bytes transferred to/from the buffer. For reads (OUT transfers) this may be less than the requested length. If the short_not_ok flag is set, short reads are treated as errors even when status otherwise indicates successful completion. Note that for writes (IN transfers) some data bytes may still reside in a device-side FIFO when the request is reported as complete.</dl>
<h2>Description</h2>
<p>These are allocated/freed through the endpoint they&#8217;re used with. The hardware&#8217;s driver can add extra per-request data to the memory it returns, which often avoids separate memory allocations (potential failures), later when the request is queued. </p>
<p> Request flags affect request handling, such as whether a zero length packet is written (the &#8220;zero&#8221; flag), whether a short read should be treated as an error (blocking request queue advance, the &#8220;short_not_ok&#8221; flag), or hinting that an interrupt is not required (the &#8220;no_interrupt&#8221; flag, for use with deep request queues). </p>
<p> Bulk endpoints can use any size buffers, and can also be used for interrupt transfers. interrupt-only endpoints can be much less functional.</p>
<h2>Note</h2>
<p>this is analogous to &#8216;struct urb&#8217; on the host side, except that it&#8217;s thinner and promotes more pre-allocation.</p>
<h2>Author</h2>
<p><code>David Brownell</code> &lt;dbrownell [at] users.sourceforge.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
