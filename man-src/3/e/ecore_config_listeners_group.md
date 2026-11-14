---
title: "ecore_config_listeners_group(3)"
name: "ecore_config_listeners_group"
section: "3"
letter: "e"
url: "/docs/linux/man/3-ecore_config_listeners_group/"
description: "Ecore Config Listeners – Functions that set and unset property listener callbacks."
---

<p>Ecore Config Listeners &#8211; Functions that set and unset property listener callbacks. </p>
<h3>Functions</h3>
<p>EAPI int <code>ecore_config_listen</code> (const char *name, const char *key, <code>Ecore_Config_Listener</code> listener, int tag, void *data)<br />
 <i>Adds a callback function to the list of functions called when a property changes. </i><br />
 EAPI int <code>ecore_config_deaf</code> (const char *name, const char *key, <code>Ecore_Config_Listener</code> listener)<br />
 <i>Removes a listener callback. </i></p>
<h2>Detailed Description</h2>
<p>Functions that set and unset property listener callbacks.</p>
<h2>Function Documentation</h2>
<h3>EAPI int ecore_config_deaf (const char * name, const char * key, <code>Ecore_Config_Listener</code> listener)</h3>
<p>Removes a listener callback. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>name</i> Name of the callback to remove.<br />
 <i>key</i> The property key the callback is listening to.<br />
 <i>listener</i> The callback function to remove.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>ECORE_CONFIG_ERR_SUCC if successful in removing the callback. If no callback matches the given parameters, then ECORE_CONFIG_ERR_NOTFOUND is returned. If NULL is passed for the key pointer, ECORE_CONFIG_ERR_NODATA is returned.</dl>
<p> References ecore_config_get(), and Ecore_Config_Prop::listeners.</p>
<h3>EAPI int ecore_config_listen (const char * name, const char * key, <code>Ecore_Config_Listener</code> listener, int tag, void * data)</h3>
<p>Adds a callback function to the list of functions called when a property changes. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>name</i> Name of the callback.<br />
 <i>key</i> The key of the property to listen to.<br />
 <i>listener</i> Listener callback function.<br />
 <i>tag</i> Tag to pass to listener when it is called.<br />
 <i>data</i> Data to pass to listener when it is called.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>ECORE_CONFIG_ERR_SUCC if successful in setting up the callback.</dl>
<p> References ecore_config_get(), ECORE_CONFIG_NIL, and Ecore_Config_Prop::listeners.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Ecore from the source code.</p>
