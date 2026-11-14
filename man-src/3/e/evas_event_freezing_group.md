---
title: "evas_event_freezing_group(3)"
name: "evas_event_freezing_group"
section: "3"
letter: "e"
url: "/docs/linux/man/3-evas_event_freezing_group/"
description: "Evas Event Freezing Functions – Functions that deal with the freezing of event processing of an evas."
---

<p>Evas Event Freezing Functions &#8211; Functions that deal with the freezing of event processing of an evas. </p>
<h3>Functions</h3>
<p>EAPI void <code>evas_event_freeze</code> (<code>Evas</code> *e)<br />
 <i>Freeze all event processing. </i><br />
 EAPI void <code>evas_event_thaw</code> (<code>Evas</code> *e)<br />
 <i>Thaw a canvas out after freezing. </i><br />
 EAPI int <code>evas_event_freeze_get</code> (const <code>Evas</code> *e)<br />
 <i>Return the freeze count of a given canvas. </i></p>
<h2>Detailed Description</h2>
<p>Functions that deal with the freezing of event processing of an evas.</p>
<h2>Function Documentation</h2>
<h3>EAPI void evas_event_freeze (<code>Evas</code> * e)</h3>
<p>Freeze all event processing. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>e</i> The canvas to freeze event processing on</dl>
<p> This function will indicate to evas that the canvas e is to have all event processing frozen until a matching <code>evas_event_thaw()</code> function is called on the same canvas. Every freeze call must be matched by a thaw call in order to completely thaw out a canvas. </p>
<p> Example: </p>
<pre> extern Evas *evas;
 extern Evas_Object *object;
 evas_event_freeze(evas);
 evas_object_move(object, 50, 100);
 evas_object_resize(object, 200, 200);
 evas_event_thaw(evas);</pre>
<p>&nbsp;<wbr></p>
<h3>EAPI int evas_event_freeze_get (const <code>Evas</code> * e)</h3>
<p>Return the freeze count of a given canvas. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>e</i> The canvas to fetch the freeze count from</dl>
<p> This returns the number of times the canvas has been told to freeze events. It is possible to call <code>evas_event_freeze()</code> multiple times, and these must be matched by <code>evas_event_thaw()</code> calls. This call allows the program to discover just how many times things have been frozen in case it may want to break out of a deep freeze state where the count is high. </p>
<p> Example: </p>
<pre> extern Evas *evas;
 while (evas_event_freeze_get(evas) &gt; 0) evas_event_thaw(evas);</pre>
<p>&nbsp;<wbr></p>
<h3>EAPI void evas_event_thaw (<code>Evas</code> * e)</h3>
<p>Thaw a canvas out after freezing. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>e</i> The canvas to thaw out</dl>
<p> This will thaw out a canvas after a matching <code>evas_event_freeze()</code> call. If this call completely thaws out a canvas, events will start being processed again after this call, but this call will not invole any &#8216;missed&#8217; events to be evaluated. </p>
<p> See <code>evas_event_freeze()</code> for an example.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Evas from the source code.</p>
