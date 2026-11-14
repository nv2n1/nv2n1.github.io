---
title: "vpsetvoxelfield(3)"
name: "vpsetvoxelfield"
section: "3"
letter: "v"
url: "/docs/linux/man/3-vpsetvoxelfield/"
description: "vpSetVoxelField, vpFieldOffset – define the size and location of a voxel field"
---

<p>vpSetVoxelField, vpFieldOffset &#8211; define the size and location of a voxel field</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;volpack.h&gt;
</code></pre>
<p> vpResult</p>
<dl>
<dt> <code>vpSetVoxelField(</code><i>vpc, field_num, field_size, field_offset,</p>
<dd>field_max</i><code>)</code></p>
<dd>vpContext *<i>vpc;</i></p>
<dd>int <i>field_num;</i></p>
<dd>int <i>field_size;</i></p>
<dd>int <i>field_offset;</i></p>
<dd>int <i>field_max;</i> </p>
<pre><code>
int

vpFieldOffset(voxel_ptr, field_name)

vpContext *vpc;

LITERAL field_name;</code></pre>
<h2>Arguments</h2>
<dl>
<dt><i>vpc</i></p>
<dd>VolPack context from <code>vpCreateContext.</code></p>
<dt><i>field_num</i></p>
<dd>Field number for the field to define (first field is 0).</p>
<dt><i>field_size</i></p>
<dd>Size of the field in bytes.</p>
<dt><i>field_offset</i></p>
<dd>Number of bytes from the beginning of the voxel to the beginning of the field.</p>
<dt><i>field_max</i></p>
<dd>Maximum possible value of the field.</p>
<dt><i>voxel_ptr</i></p>
<dd>Pointer to a C structure defining the fields in the voxel.</p>
<dt><i>field_name</i></p>
<dd>Literal name of the voxel field in the C structure.</dl>
<h2>Description</h2>
<p><code>vpSetVoxelField</code> is used to define the size and location of each field in a voxel. Once you have chosen the sizes and order for the voxel fields, call <code>vpSetVoxelSize</code> once and then call <code>vpSetVoxelField</code> once for each field. Each field has a unique field number (the <i>field_num</i> argument); the first field is 0, the next is 1, and so on, up to one less than the total number of fields defined with <i>VpSetVoxelSize</i>. The <i>field_max</i> argument is used to determine the required size for lookup tables indexed by the value in a particular field; the maximum field value may be any number from 0 to the maximum unsigned integer representable by the field size. </p>
<p> If you have declared the layout of a voxel using a C structure then you can use the <i>sizeof</i> operator and the <code>vpFieldOffset</code> macro to compute the field sizes and offsets. <code>vpFieldOffset</code> returns the number of bytes from the beginning of a C structure to the beginning of a particular field in the structure. For example, the following code shows how to declare the size and offset for one voxel field:</p>
<dl>
<dd>
<pre>struct voxel {
 char field0;
 char field1;
 short field2;
} *dummy_voxel;
#define SIZE_0 sizeof(char)
#define OFFSET_0 vpFieldOffset(dummy_voxel, field0)
#define MAX_0 127
vpSetVoxelField(vpc, 0, SIZE_0, OFFSET_0, MAX_0);
</dl>
The size of each field must be 1, 2 or 4 bytes.
You must also obey any byte-alignment restrictions required by your
hardware. On many machines, two-byte fields must begin on a two-byte
boundary and four-byte fields must begin on a four-byte boundary.
The total size of a voxel may also need to be padded so that voxels
packed one after the other still obey the alignment restrictions.
If you declare your voxel as a C structure and use the <i>sizeof</i>
operator and the <code>vpFieldOffset</code> macro then you should always get
correct results. However, if you do not consider alignment
restrictions when choosing the voxel field ordering the compiler may
have to insert padding for you, resulting in wasted memory.
Some of the VolPack routines require you to declare fields of a
particular size in order to store their results. The functions to
precompute surface normals and gradient magnitudes (see
<a href="//www.systutorials.com/docs/linux/man/3-vpVolumeNormals/">vpVolumeNormals</a>(3), <a href="//www.systutorials.com/docs/linux/man/3-vpScanlineNormals/">vpScanlineNormals</a>(3), <a href="//www.systutorials.com/docs/linux/man/3-vpClassifyVolume/">vpClassifyVolume</a>(3),
<a href="//www.systutorials.com/docs/linux/man/3-vpClassifyScalars/">vpClassifyScalars</a>(3) and <a href="//www.systutorials.com/docs/linux/man/3-vpClassifyScanline/">vpClassifyScanline</a>(3)) can optionally store a
one-byte scalar value, a one-byte
gradient magnitude, and a two-byte surface normal value in each voxel.
The following constants defined in volpack.h give the corresponding
maximum field values: VP_SCALAR_MAX, VP_GRAD_MAX, and VP_NORM_MAX.
If you choose not to use these functions then there is no need to
declare these fields.
It is usually not necessary to declare a field for the voxel opacity
if the opacity can be computed from the other voxel fields. See
<a href="//www.systutorials.com/docs/linux/man/3-vpSetClassifierTable/">vpSetClassifierTable</a>(3) for further discussion.
If the call to <code>vpSetVoxelSize</code> succeeds, any existing precomputed
volume data structures in the context are destroyed.</pre>
<h2>State Variables</h2>
<p>The current voxel field parameters can be retrieved with the following state variable codes (see <a href="/docs/linux/man/3-vpgeti/">vpGeti</a>(3)): VP_FIELD_SIZES, VP_FIELD_OFFSETS, VP_FIELD_MAXES.</p>
<h2>Errors</h2>
<p>The normal return value is VP_OK. The following error return value is possible:</p>
<dl>
<dt>VPERROR_BAD_VALUE</p>
<dd>The field number, size or offset is out of range.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-volpack/">VolPack</a>(3), <a href="/docs/linux/man/3-vpcreatecontext/">vpCreateContext</a>(3), <a href="/docs/linux/man/3-vpsetvoxelsize/">vpSetVoxelSize</a>(3) </p>
