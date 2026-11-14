---
title: "iio_validate_scan_mask_onehot(9)"
name: "iio_validate_scan_mask_onehot"
section: "9"
letter: "i"
url: "/docs/linux/man/9-iio_validate_scan_mask_onehot/"
description: "iio_validate_scan_mask_onehot – Validates that exactly one channel is selected"
---

<p>iio_validate_scan_mask_onehot &#8211; Validates that exactly one channel is selected</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>bool iio_validate_scan_mask_onehot(struct iio_dev&nbsp;<wbr>*&nbsp;<wbr></code><i>indio_dev</i><code>, const unsigned long&nbsp;<wbr>*&nbsp;<wbr></code><i>mask</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>indio_dev</i></p>
<dl>
<dd>
<dd>the iio device</dl>
<p> <i>mask</i></p>
<dl>
<dd>scan mask to be checked</dl>
<h2>Description</h2>
<p>Return true if exactly one bit is set in the scan mask, false otherwise. It can be used for devices where only one channel can be active for sampling at a time.</p>
<h2>Author</h2>
<p><code>Daniel Baluta</code> &lt;daniel.baluta [at] intel.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
