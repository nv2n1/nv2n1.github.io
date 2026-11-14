---
title: "idle_group(3)"
name: "idle_group"
section: "3"
letter: "i"
url: "/docs/linux/man/3-idle_group/"
description: "Idle Handlers – Callbacks that are called when the program enters or exits an idle state."
---

<p>Idle Handlers &#8211; Callbacks that are called when the program enters or exits an idle state. </p>
<h3>Functions</h3>
<p>EAPI <code>Ecore_Idle_Enterer</code> * <code>ecore_idle_enterer_add</code> (int(*func)(void *data), const void *data)<br />
 <i>Add an idle enterer handler. </i><br />
 EAPI <code>Ecore_Idle_Enterer</code> * <code>ecore_idle_enterer_before_add</code> (int(*func)(void *data), const void *data)<br />
 <i>Add an idle enterer handler at the start of the list so it gets called earlier than others. </i><br />
 EAPI void * <code>ecore_idle_enterer_del</code> (<code>Ecore_Idle_Enterer</code> *idle_enterer)<br />
 <i>Delete an idle enterer callback. </i><br />
 EAPI <code>Ecore_Idle_Exiter</code> * <code>ecore_idle_exiter_add</code> (int(*func)(void *data), const void *data)<br />
 <i>Add an idle exiter handler. </i><br />
 EAPI void * <code>ecore_idle_exiter_del</code> (<code>Ecore_Idle_Exiter</code> *idle_exiter)<br />
 <i>Delete an idle exiter handler from the list to be run on exiting idle state. </i><br />
 EAPI <code>Ecore_Idler</code> * <code>ecore_idler_add</code> (int(*func)(void *data), const void *data)<br />
 <i>Add an idler handler. </i><br />
 EAPI void * <code>ecore_idler_del</code> (<code>Ecore_Idler</code> *idler)<br />
 <i>Delete an idler callback from the list to be executed. </i></p>
<h2>Detailed Description</h2>
<p>Callbacks that are called when the program enters or exits an idle state. </p>
<p> The ecore main loop enters an idle state when it is waiting for timers to time out, data to come in on a file descriptor or any other event to occur. You can set callbacks to be called when the main loop enters an idle state, during an idle state or just after the program wakes up. </p>
<p> Enterer callbacks are good for updating your program&#8217;s state, if it has a state engine. Once all of the enterer handlers are called, the program will enter a &#8216;sleeping&#8217; state. </p>
<p> Idler callbacks are called when the main loop has called all enterer handlers. They are useful for interfaces that require polling and timers would be too slow to use. </p>
<p> If no idler callbacks are specified, then the process literally goes to sleep. Otherwise, the idler callbacks are called continuously while the loop is &#8216;idle&#8217;, using as much CPU as is available to the process. </p>
<p> Exiter callbacks are called when the main loop wakes up from an idle state.</p>
<h2>Function Documentation</h2>
<h3>EAPI <code>Ecore_Idle_Enterer</code>* ecore_idle_enterer_add (int(*)(void *data) func, const void * data)</h3>
<p>Add an idle enterer handler. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>func</i> The function to call when entering an idle state.<br />
 <i>data</i> The data to be passed to the func call</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>A handle to the idle enterer callback if successful. Otherwise, NULL is returned.</dl>
<h3>EAPI <code>Ecore_Idle_Enterer</code>* ecore_idle_enterer_before_add (int(*)(void *data) func, const void * data)</h3>
<p>Add an idle enterer handler at the start of the list so it gets called earlier than others. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>func</i> The function to call when entering an idle state.<br />
 <i>data</i> The data to be passed to the func call</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>A handle to the idle enterer callback if successful. Otherwise, NULL is returned.</dl>
<h3>EAPI void* ecore_idle_enterer_del (<code>Ecore_Idle_Enterer</code> * idle_enterer)</h3>
<p>Delete an idle enterer callback. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>idle_enterer</i> The idle enterer to delete</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The data pointer passed to the idler enterer callback on success. NULL otherwise.</dl>
<h3>EAPI <code>Ecore_Idle_Exiter</code>* ecore_idle_exiter_add (int(*)(void *data) func, const void * data)</h3>
<p>Add an idle exiter handler. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>func</i> The function to call when exiting an idle state.<br />
 <i>data</i> The data to be passed to the func call</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>A handle to the idle exiter callback on success. NULL otherwise.</dl>
<h3>EAPI void* ecore_idle_exiter_del (<code>Ecore_Idle_Exiter</code> * idle_exiter)</h3>
<p>Delete an idle exiter handler from the list to be run on exiting idle state. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>idle_exiter</i> The idle exiter to delete</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The data pointer that was being being passed to the handler if successful. NULL otherwise.</dl>
<h3>EAPI <code>Ecore_Idler</code>* ecore_idler_add (int(*)(void *data) func, const void * data)</h3>
<p>Add an idler handler. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>func</i> The function to call when idling.<br />
 <i>data</i> The data to be passed to this func call.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>A idler handle if successfully added. NULL otherwise.</dl>
<p> Add an idler handle to the event loop, returning a handle on success and NULL otherwise. The function func will be called repeatedly while no other events are ready to be processed, as long as it returns 1 (or ECORE_CALLBACK_RENEW). A return of 0 (or ECORE_CALLBACK_CANCEL) deletes the idler. </p>
<p> Idlers are useful for progressively prossessing data without blocking.</p>
<h3>EAPI void* ecore_idler_del (<code>Ecore_Idler</code> * idler)</h3>
<p>Delete an idler callback from the list to be executed. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>idler</i> The handle of the idler callback to delete</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The data pointer passed to the idler callback on success. NULL otherwise.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Ecore from the source code.</p>
