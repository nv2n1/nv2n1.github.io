---
title: "ecore_imf_context_module_group(3)"
name: "ecore_imf_context_module_group"
section: "3"
letter: "e"
url: "/docs/linux/man/3-ecore_imf_context_module_group/"
description: "Ecore Input Method Context Module Functions – Functions that should be used by Ecore Input Method Context modules."
---

<p>Ecore Input Method Context Module Functions &#8211; Functions that should be used by Ecore Input Method Context modules. </p>
<h3>Functions</h3>
<p>EAPI Ecore_IMF_Context * <code>ecore_imf_context_new</code> (const Ecore_IMF_Context_Class *ctxc)<br />
 <i>Creates a new Input Method Context with klass specified by </i>ctxc.<br />
 EAPI void <code>ecore_imf_context_data_set</code> (Ecore_IMF_Context *ctx, void *data)<br />
 <i>Set the Input Method Context specific data. </i><br />
 EAPI void * <code>ecore_imf_context_data_get</code> (Ecore_IMF_Context *ctx)<br />
 <i>Get the Input Method Context specific data. </i><br />
 EAPI int <code>ecore_imf_context_surrounding_get</code> (Ecore_IMF_Context *ctx, char **text, int *cursor_pos)<br />
 <i>Retrieve context around insertion point. </i><br />
 EAPI void <code>ecore_imf_context_preedit_start_event_add</code> (Ecore_IMF_Context *ctx)<br />
 <i>Adds ECORE_IMF_EVENT_PREEDIT_START to the event queue. </i><br />
 EAPI void <code>ecore_imf_context_preedit_end_event_add</code> (Ecore_IMF_Context *ctx)<br />
 <i>Adds ECORE_IMF_EVENT_PREEDIT_END to the event queue. </i><br />
 EAPI void <code>ecore_imf_context_preedit_changed_event_add</code> (Ecore_IMF_Context *ctx)<br />
 <i>Adds ECORE_IMF_EVENT_PREEDIT_CHANGED to the event queue. </i><br />
 EAPI void <code>ecore_imf_context_commit_event_add</code> (Ecore_IMF_Context *ctx, const char *str)<br />
 <i>Adds ECORE_IMF_EVENT_COMMIT to the event queue. </i><br />
 EAPI void <code>ecore_imf_context_delete_surrounding_event_add</code> (Ecore_IMF_Context *ctx, int offset, int n_chars)<br />
 <i>Adds ECORE_IMF_EVENT_DELETE_SURROUNDING to the event queue. </i></p>
<h2>Detailed Description</h2>
<p>Functions that should be used by Ecore Input Method Context modules.</p>
<h2>Function Documentation</h2>
<h3>EAPI void ecore_imf_context_commit_event_add (Ecore_IMF_Context * ctx, const char * str)</h3>
<p>Adds ECORE_IMF_EVENT_COMMIT to the event queue. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ctx</i> An Ecore_IMF_Context.<br />
 <i>str</i> The committed string.</dl>
<p> References ecore_event_add().</p>
<h3>EAPI void* ecore_imf_context_data_get (Ecore_IMF_Context * ctx)</h3>
<p>Get the Input Method Context specific data. </p>
<p> See <code>ecore_imf_context_data_set</code> for more details. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ctx</i> An Ecore_IMF_Context.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The Input Method Context specific data.</dl>
<h3>EAPI void ecore_imf_context_data_set (Ecore_IMF_Context * ctx, void * data)</h3>
<p>Set the Input Method Context specific data. </p>
<p> Note that this method should be used by modules to set the Input Method Context specific data and it&#8217;s not meant to be used by applications to store application specific data. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ctx</i> An Ecore_IMF_Context.<br />
 <i>data</i> The Input Method Context specific data.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>A new Ecore_IMF_Context; on failure it returns NULL.</dl>
<h3>EAPI void ecore_imf_context_delete_surrounding_event_add (Ecore_IMF_Context * ctx, int offset, int n_chars)</h3>
<p>Adds ECORE_IMF_EVENT_DELETE_SURROUNDING to the event queue. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ctx</i> An Ecore_IMF_Context.<br />
 <i>offset</i> The start offset of surrounding to be deleted.<br />
 <i>n_chars</i> The number of characters to be deleted.</dl>
<p> References ecore_event_add().</p>
<h3>EAPI Ecore_IMF_Context* ecore_imf_context_new (const Ecore_IMF_Context_Class * ctxc)</h3>
<p>Creates a new Input Method Context with klass specified by ctxc. </p>
<p> This method should be used by modules implementing the Input Method Context interface. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ctxc</i> An Ecore_IMF_Context_Class.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>A new Ecore_IMF_Context; on failure it returns NULL.</dl>
<h3>EAPI void ecore_imf_context_preedit_changed_event_add (Ecore_IMF_Context * ctx)</h3>
<p>Adds ECORE_IMF_EVENT_PREEDIT_CHANGED to the event queue. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ctx</i> An Ecore_IMF_Context.</dl>
<p> References ecore_event_add().</p>
<h3>EAPI void ecore_imf_context_preedit_end_event_add (Ecore_IMF_Context * ctx)</h3>
<p>Adds ECORE_IMF_EVENT_PREEDIT_END to the event queue. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ctx</i> An Ecore_IMF_Context.</dl>
<p> References ecore_event_add().</p>
<h3>EAPI void ecore_imf_context_preedit_start_event_add (Ecore_IMF_Context * ctx)</h3>
<p>Adds ECORE_IMF_EVENT_PREEDIT_START to the event queue. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ctx</i> An Ecore_IMF_Context.</dl>
<p> References ecore_event_add().</p>
<h3>EAPI int ecore_imf_context_surrounding_get (Ecore_IMF_Context * ctx, char ** text, int * cursor_pos)</h3>
<p>Retrieve context around insertion point. </p>
<p> This function is implemented by calling the Ecore_IMF_Context::retrieve_surrounding_func ( set using <code>ecore_imf_context_retrieve_surrounding_callback_set</code>). </p>
<p> There is no obligation for a widget to respond to the retrieve_surrounding_func, so input methods must be prepared to function without context. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ctx</i> An Ecore_IMF_Context.<br />
 <i>text</i> Location to store a UTF-8 encoded string of text holding context around the insertion point. If the function returns 1, then you must free the result stored in this location with free().<br />
 <i>cursor_pos</i> Location to store the position in characters of the insertion cursor within .</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>1 if surrounding text was provided; otherwise 0.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Ecore from the source code.</p>
