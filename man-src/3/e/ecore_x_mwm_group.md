---
title: "ecore_x_mwm_group(3)"
name: "ecore_x_mwm_group"
section: "3"
letter: "e"
url: "/docs/linux/man/3-ecore_x_mwm_group/"
description: "MWM related functions. – Functions related to MWM."
---

<p>MWM related functions. &#8211; Functions related to MWM. </p>
<h3>Functions</h3>
<p>EAPI void <code>ecore_x_mwm_hints_get_prefetch</code> (Ecore_X_Window window)<br />
 <i>Sends the GetProperty request. </i><br />
 EAPI void <code>ecore_x_mwm_hints_get_fetch</code> (void)<br />
 <i>Gets the reply of the GetProperty request sent by </i><code>ecore_x_mwm_hints_get_prefetch()</code>.<br />
 EAPI int <code>ecore_x_mwm_hints_get</code> (Ecore_X_Window window __UNUSED__, Ecore_X_MWM_Hint_Func *fhint, Ecore_X_MWM_Hint_Decor *dhint, Ecore_X_MWM_Hint_Input *ihint)<br />
 <i>To document. </i><br />
 EAPI void <code>ecore_x_mwm_borderless_set</code> (Ecore_X_Window window, int borderless)<br />
 <i>Sets the borderless flag of a window using MWM. </i></p>
<h2>Detailed Description</h2>
<p>Functions related to MWM.</p>
<h2>Function Documentation</h2>
<h3>EAPI void ecore_x_mwm_borderless_set (Ecore_X_Window window, int borderless)</h3>
<p>Sets the borderless flag of a window using MWM. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> The window.<br />
 <i>borderless</i> The borderless flag.</dl>
<h3>EAPI int ecore_x_mwm_hints_get (Ecore_X_Window window __UNUSED__, Ecore_X_MWM_Hint_Func * fhint, Ecore_X_MWM_Hint_Decor * dhint, Ecore_X_MWM_Hint_Input * ihint)</h3>
<p>To document. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> Unused.<br />
 <i>fhint</i> To document.<br />
 <i>dhint</i> To document.<br />
 <i>ihint</i> To document.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 on success, 0 otherwise.</dl>
<p> To use this function, you must call before, and in order, <code>ecore_x_mwm_hints_get_prefetch()</code>, which sends the GetProperty request, then <code>ecore_x_mwm_hints_get_fetch()</code>, which gets the reply.</p>
<h3>EAPI void ecore_x_mwm_hints_get_prefetch (Ecore_X_Window window)</h3>
<p>Sends the GetProperty request. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>window</i> Window whose MWM hints are requested.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Ecore from the source code.</p>
