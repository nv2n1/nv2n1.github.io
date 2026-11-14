---
title: "ecore_x_window_shape(3)"
name: "ecore_x_window_shape"
section: "3"
letter: "e"
url: "/docs/linux/man/3-ecore_x_window_shape/"
description: "X Window Shape Functions – These functions use the shape extension of the X server to change shape of given windows."
---

<p>X Window Shape Functions &#8211; These functions use the shape extension of the X server to change shape of given windows. </p>
<h3>Functions</h3>
<p>EAPI void <code>ecore_x_window_shape_mask_set</code> (Ecore_X_Window win, Ecore_X_Pixmap mask)<br />
 <i>Sets the shape of the given window to that given by the pixmap </i>mask.<br />
 EAPI void <code>ecore_x_window_shape_input_mask_set</code> (Ecore_X_Window win, Ecore_X_Pixmap mask)<br />
 <i>Sets the input shape of the given window to that given by the pixmap </i>mask.</p>
<h2>Detailed Description</h2>
<p>These functions use the shape extension of the X server to change shape of given windows.</p>
<h2>Function Documentation</h2>
<h3>EAPI void ecore_x_window_shape_input_mask_set (Ecore_X_Window win, Ecore_X_Pixmap mask)</h3>
<p>Sets the input shape of the given window to that given by the pixmap mask. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>win</i> The given window.<br />
 <i>mask</i> A 2-bit depth pixmap that provides the new input shape of the window.</dl>
<h3>EAPI void ecore_x_window_shape_mask_set (Ecore_X_Window win, Ecore_X_Pixmap mask)</h3>
<p>Sets the shape of the given window to that given by the pixmap mask. </p>
<p> Sets the shape of the given window to the given pixmap. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>win</i> The given window.<br />
 <i>mask</i> A 2-bit depth pixmap that provides the new shape of the window.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Ecore from the source code.</p>
