---
title: "xtallocategc(3)"
name: "xtallocategc"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xtallocategc/"
description: "XtAllocateGC – obtain a sharable GC with modifiable fields"
---

<p>XtAllocateGC &#8211; obtain a sharable GC with modifiable fields </p>
<h2>Syntax</h2>
<p>#include &lt;X11/Intrinsic.h&gt;</p>
<dl COMPACT>
<dd>GC XtAllocateGC(Widget <i>w</i>, Cardinal <i>depth</i>, XtGCMask <i>value_mask</i>, XGCValues *<i>values</i>, XtGCMask <i>dynamic_mask</i>, XtGCMask <i>unused_mask</i>);</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>values</i></p>
<dd>Specifies the actual values for this GC.</p>
<dt><i>value_mask</i></p>
<dd>Specifies which fields of the values are specified.</p>
<dt><i>w</i></p>
<dd>Specifies the widget.</p>
<dt><i>depth</i></p>
<dd>Specifies the depth for which the returned GC is valid, or 0.</p>
<dt><i>dynamic_mask</i></p>
<dd>Specifies the fields of the GC that will be modified by the caller.</p>
<dt><i>unused_mask</i></p>
<dd>Specifies the fields of the GC that will not be needed by the caller.</dl>
<h2>Description</h2>
<p>The <code>XtAllocateGC</code> function returns a sharable GC that may be modified by the client. The <i>screen</i> field of the specified widget or of the nearest widget ancestor of the specified object and the specified <i>depth</i> argument supply the root and drawable depths for which the GC is to be valid. If <i>depth</i> is zero the depth is taken from the <i>depth</i> field of the specified widget or of the nearest widget ancestor of the specified object. </p>
<p> The <i>value_mask</i> argument specifies the fields of the GC that will be initialized with the respective members of the <i>values</i> structure. The <i>dynamic_mask</i> argument specifies fields that the caller intends to modify during program execution. The caller must ensure that the corresponding GC field is set prior to each use of the GC. The <i>unused_mask</i> argument specifies fields of the GC that are of no interest to the caller. The caller may make no assumptions about the contents of any fields specified in <i>unused_mask</i>. The caller may assume that at all times all fields not specified in either <i>dynamic_mask</i> or <i>unused_mask</i> have their default value if not specified in <i>value_mask</i> or the value specified by <i>values</i>. If a field is specified in both <i>value_mask</i> and dynamic_mask, the effect is as if it were specified only in <i>dynamic_mask</i> and then immediately set to the value in <i>values</i>. If a field is set in <i>unused_mask</i> and also in either <i>value_mask</i> or <i>dynamic_mask</i>, the specification in <i>unused_mask</i> is ignored. </p>
<p> <code>XtAllocateGC</code> tries to minimize the number of unique GCs created by comparing the arguments with those of previous calls and returning an existing GC when there are no conflicts. <code>XtAllocateGC</code> may modify and return an existing GC if it was allocated with a nonzero <i>unused_mask</i>.</p>
<h2>See Also</h2>
<p><code>XtGetGC</code><br />
 <i>X Toolkit Intrinsics &#8211; C Language Interface</i><br />
 <i>Xlib &#8211; C Language X Interface</i></p>
