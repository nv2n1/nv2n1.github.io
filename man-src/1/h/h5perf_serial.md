---
title: "h5perf_serial(1)"
name: "h5perf_serial"
section: "1"
letter: "h"
url: "/docs/linux/man/1-h5perf_serial/"
description: "h5perf_serial: – Measures HDF5 serial performance."
---

<h2>NAME</h2>
<p> h5perf_serial: &#8211; Measures HDF5 serial performance.</p>
<h2>DESCRIPTION</h2>
<p> h5perf_serial: Version 1.8.7 usage: h5perf_serial [OPTIONS]</p>
<dl>
<dt>
<dd> OPTIONS</p>
<dt><code>-h</code></p>
<dd> Print an usage message and exit</p>
<dt><code>-A</code> AL</p>
<dd> Which APIs to test [default: all of them]</p>
<dt><code>-c</code> SL</p>
<dd> Selects chunked storage and defines chunks dimensions and sizes [default: Off]</p>
<dt><code>-e</code> SL</p>
<dd> Dimensions and sizes of dataset [default: 100,200]</p>
<dt><code>-i</code> N</p>
<dd> Number of iterations to perform [default: 1]</p>
<dt><code>-r</code> NL</p>
<dd> Dimension access order (see below for description) [default: 1,2]</p>
<dt><code>-t</code></p>
<dd> Selects extendable dimensions for HDF5 dataset [default: Off]</p>
<dt><code>-v</code> VFD</p>
<dd> Selects file driver for HDF5 access [default: sec2]</p>
<dt><code>-w</code></p>
<dd> Perform write tests, not the read tests [default: Off]</p>
<dt><code>-x</code> SL</p>
<dd> Dimensions and sizes of the transfer buffer [default: 10,20]</p>
<dt>N</p>
<dd> &#8211; is an integer &gt; 0.</p>
<dt>S</p>
<dd> &#8211; is a size specifier, an integer &gt; 0 followed by a size indicator:</p>
<dt>
<dd> K &#8211; Kilobyte (1024) M &#8211; Megabyte (1048576) G &#8211; Gigabyte (1073741824)</p>
<dt>
<dd> Example: &#8217;37M&#8217; is 37 megabytes or 38797312 bytes</p>
<dt>
<dd> AL &#8211; is an API list. Valid values are:</p>
<dt>
<dd> hdf5 &#8211; HDF5 posix &#8211; POSIX</p>
<dt>
<dd> Example: <code>-A</code> posix,hdf5</p>
<dt>
<dd> NL &#8211; is list of integers (N) separated by commas.</p>
<dt>
<dd> Example: 1,2,3</p>
<dt>
<dd> SL &#8211; is list of size specifiers (S) separated by commas.</p>
<dt>
<dd> Example: 2K,2K,3K</p>
<dt>
<dd> The example defines an object (dataset, tranfer buffer) with three dimensions. Be aware that as the number of dimensions increases, the the total size of the object increases exponentially.</p>
<dt>VFD</p>
<dd> &#8211; is an HDF5 file driver specifier. Valid values are:</p>
<dt>
<dd> sec2, stdio, core, split, multi, family, direct</p>
<dt>
<dd> Dimension access order:</p>
<dt>
<dd> Data access starts at the cardinal origin of the dataset using the transfer buffer. The next access occurs on a dataset region next to the previous one. For a multidimensional dataset, there are several directions as to where to proceed. This can be specified in the dimension access order. For example, <code>-r</code> 1,2 states that the tool should traverse dimension 1 first, and then dimension 2.</p>
<dt>
<dd> Environment variables:</p>
<dt>HDF5_NOCLEANUP</p>
<dd> Do not remove data files if set [default remove]</p>
<dt>HDF5_PREFIX</p>
<dd> Data file prefix</dl>
<p> usage: h5perf_serial [OPTIONS]</p>
<dl>
<dt>
<dd> OPTIONS</p>
<dt><code>-h</code></p>
<dd> Print an usage message and exit</p>
<dt><code>-A</code> AL</p>
<dd> Which APIs to test [default: all of them]</p>
<dt><code>-c</code> SL</p>
<dd> Selects chunked storage and defines chunks dimensions and sizes [default: Off]</p>
<dt><code>-e</code> SL</p>
<dd> Dimensions and sizes of dataset [default: 100,200]</p>
<dt><code>-i</code> N</p>
<dd> Number of iterations to perform [default: 1]</p>
<dt><code>-r</code> NL</p>
<dd> Dimension access order (see below for description) [default: 1,2]</p>
<dt><code>-t</code></p>
<dd> Selects extendable dimensions for HDF5 dataset [default: Off]</p>
<dt><code>-v</code> VFD</p>
<dd> Selects file driver for HDF5 access [default: sec2]</p>
<dt><code>-w</code></p>
<dd> Perform write tests, not the read tests [default: Off]</p>
<dt><code>-x</code> SL</p>
<dd> Dimensions and sizes of the transfer buffer [default: 10,20]</p>
<dt>N</p>
<dd> &#8211; is an integer &gt; 0.</p>
<dt>S</p>
<dd> &#8211; is a size specifier, an integer &gt; 0 followed by a size indicator:</p>
<dt>
<dd> K &#8211; Kilobyte (1024) M &#8211; Megabyte (1048576) G &#8211; Gigabyte (1073741824)</p>
<dt>
<dd> Example: &#8217;37M&#8217; is 37 megabytes or 38797312 bytes</p>
<dt>
<dd> AL &#8211; is an API list. Valid values are:</p>
<dt>
<dd> hdf5 &#8211; HDF5 posix &#8211; POSIX</p>
<dt>
<dd> Example: <code>-A</code> posix,hdf5</p>
<dt>
<dd> NL &#8211; is list of integers (N) separated by commas.</p>
<dt>
<dd> Example: 1,2,3</p>
<dt>
<dd> SL &#8211; is list of size specifiers (S) separated by commas.</p>
<dt>
<dd> Example: 2K,2K,3K</p>
<dt>
<dd> The example defines an object (dataset, tranfer buffer) with three dimensions. Be aware that as the number of dimensions increases, the the total size of the object increases exponentially.</p>
<dt>VFD</p>
<dd> &#8211; is an HDF5 file driver specifier. Valid values are:</p>
<dt>
<dd> sec2, stdio, core, split, multi, family, direct</p>
<dt>
<dd> Dimension access order:</p>
<dt>
<dd> Data access starts at the cardinal origin of the dataset using the transfer buffer. The next access occurs on a dataset region next to the previous one. For a multidimensional dataset, there are several directions as to where to proceed. This can be specified in the dimension access order. For example, <code>-r</code> 1,2 states that the tool should traverse dimension 1 first, and then dimension 2.</p>
<dt>
<dd> Environment variables:</p>
<dt>HDF5_NOCLEANUP</p>
<dd> Do not remove data files if set [default remove]</p>
<dt>HDF5_PREFIX</p>
<dd> Data file prefix</dl>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>h5perf_serial:</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>h5perf_serial:</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
<dd> <code>info h5perf_serial:</code></dl>
<p> should give you access to the complete manual. </p>
<h2>Index</h2>
