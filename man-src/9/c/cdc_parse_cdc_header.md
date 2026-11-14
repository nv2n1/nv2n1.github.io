---
title: "cdc_parse_cdc_header(9)"
name: "cdc_parse_cdc_header"
section: "9"
letter: "c"
url: "/docs/linux/man/9-cdc_parse_cdc_header/"
---

cdc_parse_cdc_header - parse the extra headers present in CDC devices

<h2>Synopsis</h2>

<pre><code>int cdc_parse_cdc_header(struct usb_cdc_parsed_header *hdr, struct usb_interface *intf, u8 *buffer, int buflen);</code></pre>

<h2>Arguments</h2>

<i>hdr</i>
<dl><dd><dd>the place to put the results of the parsing</dl>
 

 <i>intf</i>
<dl><dd>the interface for which parsing is requested</dl>
 

 <i>buffer</i>
<dl><dd>pointer to the extra headers to be parsed</dl>
 

 <i>buflen</i>
<dl><dd>length of the extra headers</dl>

<h2>Description</h2>

This evaluates the extra headers present in CDC devices which bind the interfaces for data and control and provide details about the capabilities of the device.

<h2>Return</h2>

number of descriptors parsed or -EINVAL if the header is contradictory beyond salvage

<h2>Copyright</h2>


