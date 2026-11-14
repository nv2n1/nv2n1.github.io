---
title: "struct_urb(9)"
name: "struct_urb"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_urb/"
description: "struct_urb – USB Request Block"
---

<p>struct_urb &#8211; USB Request Block</p>
<h2>Synopsis</h2>
<pre><code>struct urb {
    struct list_head urb_list;
    struct list_head anchor_list;
    struct usb_anchor *anchor;
    struct usb_device *dev;
    struct usb_host_endpoint *ep;
    unsigned int pipe;
    unsigned int stream_id;
    int status;
    unsigned int transfer_flags;
    void *transfer_buffer;
    dma_addr_t transfer_dma;
    struct scatterlist *sg;
    int num_mapped_sgs;
    int num_sgs;
    u32 transfer_buffer_length;
    u32 actual_length;
    unsigned char *setup_packet;
    dma_addr_t setup_dma;
    int start_frame;
    int number_of_packets;
    int interval;
    int error_count;
    void *context;
    usb_complete_t complete;
    struct usb_iso_packet_descriptor iso_frame_desc[0];
};</code></pre>
<h2>Members</h2>
<p>urb_list</p>
<dl>
<dd>For use by current owner of the URB.</dl>
<p> anchor_list</p>
<dl>
<dd>membership in the list of an anchor</dl>
<p> anchor</p>
<dl>
<dd>to anchor URBs to a common mooring</dl>
<p> dev</p>
<dl>
<dd>Identifies the USB device to perform the request.</dl>
<p> ep</p>
<dl>
<dd>Points to the endpoint&#8217;s data structure. Will eventually replace <i>pipe</i>.</dl>
<p> pipe</p>
<dl>
<dd>Holds endpoint number, direction, type, and more. Create these values with the eight macros available; usb_{snd,rcv}TYPEpipe(dev,endpoint), where the TYPE is &#8220;ctrl&#8221; (control), &#8220;bulk&#8221;, &#8220;int&#8221; (interrupt), or &#8220;iso&#8221; (isochronous). For example <code>usb_sndbulkpipe</code> or <code>usb_rcvintpipe</code>. Endpoint numbers range from zero to fifteen. Note that &#8220;in&#8221; endpoint two is a different endpoint (and pipe) from &#8220;out&#8221; endpoint two. The current configuration controls the existence, type, and maximum packet size of any given endpoint.</dl>
<p> stream_id</p>
<dl>
<dd>the endpoint&#8217;s stream ID for bulk streams</dl>
<p> status</p>
<dl>
<dd>This is read in non-iso completion functions to get the status of the particular request. ISO requests only use it to tell whether the URB was unlinked; detailed status for each frame is in the fields of the iso_frame-desc.</dl>
<p> transfer_flags</p>
<dl>
<dd>A variety of flags may be used to affect how URB submission, unlinking, or operation are handled. Different kinds of URB can use different flags.</dl>
<p> transfer_buffer</p>
<dl>
<dd>This identifies the buffer to (or from) which the I/O request will be performed unless URB_NO_TRANSFER_DMA_MAP is set (however, do not leave garbage in transfer_buffer even then). This buffer must be suitable for DMA; allocate it with <code>kmalloc</code> or equivalent. For transfers to &#8220;in&#8221; endpoints, contents of this buffer will be modified. This buffer is used for the data stage of control transfers.</dl>
<p> transfer_dma</p>
<dl>
<dd>When transfer_flags includes URB_NO_TRANSFER_DMA_MAP, the device driver is saying that it provided this DMA address, which the host controller driver should use in preference to the transfer_buffer.</dl>
<p> sg</p>
<dl>
<dd>scatter gather buffer list, the buffer size of each element in the list (except the last) must be divisible by the endpoint&#8217;s max packet size if no_sg_constraint isn&#8217;t set in &#8216;struct usb_bus&#8217;</dl>
<p> num_mapped_sgs</p>
<dl>
<dd>(internal) number of mapped sg entries</dl>
<p> num_sgs</p>
<dl>
<dd>number of entries in the sg list</dl>
<p> transfer_buffer_length</p>
<dl>
<dd>How big is transfer_buffer. The transfer may be broken up into chunks according to the current maximum packet size for the endpoint, which is a function of the configuration and is encoded in the pipe. When the length is zero, neither transfer_buffer nor transfer_dma is used.</dl>
<p> actual_length</p>
<dl>
<dd>This is read in non-iso completion functions, and it tells how many bytes (out of transfer_buffer_length) were transferred. It will normally be the same as requested, unless either an error was reported or a short read was performed. The URB_SHORT_NOT_OK transfer flag may be used to make such short reads be reported as errors.</dl>
<p> setup_packet</p>
<dl>
<dd>Only used for control transfers, this points to eight bytes of setup data. Control transfers always start by sending this data to the device. Then transfer_buffer is read or written, if needed.</dl>
<p> setup_dma</p>
<dl>
<dd>DMA pointer for the setup packet. The caller must not use this field; setup_packet must point to a valid buffer.</dl>
<p> start_frame</p>
<dl>
<dd>Returns the initial frame for isochronous transfers.</dl>
<p> number_of_packets</p>
<dl>
<dd>Lists the number of ISO transfer buffers.</dl>
<p> interval</p>
<dl>
<dd>Specifies the polling interval for interrupt or isochronous transfers. The units are frames (milliseconds) for full and low speed devices, and microframes (1/8 millisecond) for highspeed and SuperSpeed devices.</dl>
<p> error_count</p>
<dl>
<dd>Returns the number of ISO transfers that reported errors.</dl>
<p> context</p>
<dl>
<dd>For use in completion functions. This normally points to request-specific driver context.</dl>
<p> complete</p>
<dl>
<dd>Completion handler. This URB is passed as the parameter to the completion function. The completion function may then do what it likes with the URB, including resubmitting or freeing it.</dl>
<p> iso_frame_desc[0]</p>
<dl>
<dd>Used to provide arrays of ISO transfer buffers and to collect the transfer status for each buffer.</dl>
<h2>Description</h2>
<p>This structure identifies USB transfer requests. URBs must be allocated by calling <code>usb_alloc_urb</code> and freed with a call to <code>usb_free_urb</code>. Initialization may be done using various usb_fill_*<code>_urb</code> functions. URBs are submitted using <code>usb_submit_urb</code>, and pending requests may be canceled using <code>usb_unlink_urb</code> or <code>usb_kill_urb</code>. </p>
<p> Data Transfer Buffers: </p>
<p> Normally drivers provide I/O buffers allocated with <code>kmalloc</code> or otherwise taken from the general page pool. That is provided by transfer_buffer (control requests also use setup_packet), and host controller drivers perform a dma mapping (and unmapping) for each buffer transferred. Those mapping operations can be expensive on some platforms (perhaps using a dma bounce buffer or talking to an IOMMU), although they&#8217;re cheap on commodity x86 and ppc hardware. </p>
<p> Alternatively, drivers may pass the URB_NO_TRANSFER_DMA_MAP transfer flag, which tells the host controller driver that no such mapping is needed for the transfer_buffer since the device driver is DMA-aware. For example, a device driver might allocate a DMA buffer with <code>usb_alloc_coherent</code> or call <code>usb_buffer_map</code>. When this transfer flag is provided, host controller drivers will attempt to use the dma address found in the transfer_dma field rather than determining a dma address themselves. </p>
<p> Note that transfer_buffer must still be set if the controller does not support DMA (as indicated by bus.uses_dma) and when talking to root hub. If you have to trasfer between highmem zone and the device on such controller, create a bounce buffer or bail out with an error. If transfer_buffer cannot be set (is in highmem) and the controller is DMA capable, assign NULL to it, so that usbmon knows not to use the value. The setup_packet must always be set, so it cannot be located in highmem. </p>
<p> Initialization: </p>
<p> All URBs submitted must initialize the dev, pipe, transfer_flags (may be zero), and complete fields. All URBs must also initialize transfer_buffer and transfer_buffer_length. They may provide the URB_SHORT_NOT_OK transfer flag, indicating that short reads are to be treated as errors; that flag is invalid for write requests. </p>
<p> Bulk URBs may use the URB_ZERO_PACKET transfer flag, indicating that bulk OUT transfers should always terminate with a short packet, even if it means adding an extra zero length packet. </p>
<p> Control URBs must provide a valid pointer in the setup_packet field. Unlike the transfer_buffer, the setup_packet may not be mapped for DMA beforehand. </p>
<p> Interrupt URBs must provide an interval, saying how often (in milliseconds or, for highspeed devices, 125 microsecond units) to poll for transfers. After the URB has been submitted, the interval field reflects how the transfer was actually scheduled. The polling interval may be more frequent than requested. For example, some controllers have a maximum interval of 32 milliseconds, while others support intervals of up to 1024 milliseconds. Isochronous URBs also have transfer intervals. (Note that for isochronous endpoints, as well as high speed interrupt endpoints, the encoding of the transfer interval in the endpoint descriptor is logarithmic. Device drivers must convert that value to linear units themselves.) </p>
<p> If an isochronous endpoint queue isn&#8217;t already running, the host controller will schedule a new URB to start as soon as bandwidth utilization allows. If the queue is running then a new URB will be scheduled to start in the first transfer slot following the end of the preceding URB, if that slot has not already expired. If the slot has expired (which can happen when IRQ delivery is delayed for a long time), the scheduling behavior depends on the URB_ISO_ASAP flag. If the flag is clear then the URB will be scheduled to start in the expired slot, implying that some of its packets will not be transferred; if the flag is set then the URB will be scheduled in the first unexpired slot, breaking the queue&#8217;s synchronization. Upon URB completion, the start_frame field will be set to the (micro)frame number in which the transfer was scheduled. Ranges for frame counter values are HC-specific and can go from as low as 256 to as high as 65536 frames. </p>
<p> Isochronous URBs have a different data transfer model, in part because the quality of service is only &#8220;best effort&#8221;. Callers provide specially allocated URBs, with number_of_packets worth of iso_frame_desc structures at the end. Each such packet is an individual ISO transfer. Isochronous URBs are normally queued, submitted by drivers to arrange that transfers are at least double buffered, and then explicitly resubmitted in completion handlers, so that data (such as audio or video) streams at as constant a rate as the host controller scheduler can support. </p>
<p> Completion Callbacks: </p>
<p> The completion callback is made <code>in_interrupt</code>, and one of the first things that a completion handler should do is check the status field. The status field is provided for all URBs. It is used to report unlinked URBs, and status for all non-ISO transfers. It should not be examined before the URB is returned to the completion handler. </p>
<p> The context field is normally used to link URBs back to the relevant driver or request state. </p>
<p> When the completion callback is invoked for non-isochronous URBs, the actual_length field tells how many bytes were transferred. This field is updated even when the URB terminated with an error or was unlinked. </p>
<p> ISO transfer status is reported in the status and actual_length fields of the iso_frame_desc array, and the number of errors is reported in error_count. Completion callbacks for ISO transfers will normally (re)submit URBs to ensure a constant transfer rate. </p>
<p> Note that even fields marked &#8220;public&#8221; should not be touched by the driver when the urb is owned by the hcd, that is, since the call to <code>usb_submit_urb</code> till the entry into the completion routine.</p>
<h2>Copyright</h2>
