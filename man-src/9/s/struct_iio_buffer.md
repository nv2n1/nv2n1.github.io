---
title: "struct_iio_buffer(9)"
name: "struct_iio_buffer"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_iio_buffer/"
description: "struct_iio_buffer – general buffer structure"
---

<p>struct_iio_buffer &#8211; general buffer structure</p>
<h2>Synopsis</h2>
<pre><code>struct iio_buffer {
    int length;
    int bytes_per_datum;
    struct attribute_group *scan_el_attrs;
    long *scan_mask;
    bool scan_timestamp;
    const struct iio_buffer_access_funcs *access;
    struct list_head scan_el_dev_attr_list;
    struct attribute_group buffer_group;
    struct attribute_group scan_el_group;
    wait_queue_head_t pollq;
    bool stufftoread;
    const struct attribute **attrs;
    struct list_head demux_list;
    void *demux_bounce;
    struct list_head buffer_list;
    struct kref ref;
    unsigned int watermark;
};</code></pre>
<h2>Members</h2>
<p>length</p>
<dl>
<dd>[DEVICE] number of datums in buffer</dl>
<p> bytes_per_datum</p>
<dl>
<dd>[DEVICE] size of individual datum including timestamp</dl>
<p> scan_el_attrs</p>
<dl>
<dd>[DRIVER] control of scan elements if that scan mode control method is used</dl>
<p> scan_mask</p>
<dl>
<dd>[INTERN] bitmask used in masking scan mode elements</dl>
<p> scan_timestamp</p>
<dl>
<dd>[INTERN] does the scan mode include a timestamp</dl>
<p> access</p>
<dl>
<dd>[DRIVER] buffer access functions associated with the implementation.</dl>
<p> scan_el_dev_attr_list</p>
<dl>
<dd>[INTERN] list of scan element related attributes.</dl>
<p> buffer_group</p>
<dl>
<dd>[INTERN] attributes of the buffer group</dl>
<p> scan_el_group</p>
<dl>
<dd>[DRIVER] attribute group for those attributes not created from the iio_chan_info array.</dl>
<p> pollq</p>
<dl>
<dd>[INTERN] wait queue to allow for polling on the buffer.</dl>
<p> stufftoread</p>
<dl>
<dd>[INTERN] flag to indicate new data.</dl>
<p> attrs</p>
<dl>
<dd>[INTERN] standard attributes of the buffer</dl>
<p> demux_list</p>
<dl>
<dd>[INTERN] list of operations required to demux the scan.</dl>
<p> demux_bounce</p>
<dl>
<dd>[INTERN] buffer for doing gather from incoming scan.</dl>
<p> buffer_list</p>
<dl>
<dd>[INTERN] entry in the devices list of current buffers.</dl>
<p> ref</p>
<dl>
<dd>[INTERN] reference count of the buffer.</dl>
<p> watermark</p>
<dl>
<dd>[INTERN] number of datums to wait for poll/read.</dl>
<h2>Author</h2>
<p><code>Daniel Baluta</code> &lt;daniel.baluta [at] intel.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
