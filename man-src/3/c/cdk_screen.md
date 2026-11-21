---
title: "cdk_screen(3)"
name: "cdk_screen"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cdk_screen/"
description: "cdk_screen – Cdk Screen and Widget Manipulation Functions"
---

<h2>NAME</h2>
<p> cdk_screen &#8211; Cdk Screen and Widget Manipulation Functions</p>
<h2>SYNOPSIS</h2>
<p> <code>cc</code> [ <i>flag</i> &#8230; ] <i>file</i> &#8230; <code>-lcdk</code> [ <i>library</i> &#8230; ] </p>
<p> #include &lt;cdk.h&gt; </p>
<pre><code>
void destroyCDKScreen(
    CDKSCREEN *screen);
void endCDK(void);
void eraseCDKScreen(
    CDKSCREEN *screen);
void initCDKColor(void);
CDKSCREEN *initCDKScreen(
    WINDOW *cursesWindow);
void lowerCDKObject(
    EObjectType widgetType,
    void *object);
void raiseCDKObject(
    EObjectType widgetType,
    void *object);
void refreshCDKScreen(
    CDKSCREEN *screen);
void registerCDKObject(
    CDKSCREEN *screen,
    EObjectType widgetType,
    void *object);
void unregisterCDKObject(
    EObjectType widgetType,
    void *object);
</code></pre>
</dl>
<h2>DESCRIPTION</h2>
<p> Cdk manages all of the widgets for you. These functions perform some of the management of the widgets in a screen.</p>
<h2>AVAILABLE FUNCTIONS</h2>
<dl>
<dt><code>destroyCDKScreen</code></dt>
<dd> frees any memory allocated by the Cdk screen pointer.</dd>
<dt><code>endCDK</code></dt>
<dd> cleans up any memory created by starting Cdk and shuts down curses.</dd>
<dt><code>eraseCDKScreen</code></dt>
<dd> erases all of the widgets which are currently associated to the given screen. This does <code>NOT</code> destroy the widgets.</dd>
<dt><code>initCDKColor</code></dt>
<dd> starts the Cdk color capabilities. It defines 64 color pairs each of which is accessible using the COLOR_PAIR macro. If you do not have color support, this function call makes no difference.</dd>
<dt><code>initCDKScreen</code></dt>
<dd> takes a <i>WINDOW *</i> (<i>cursesWindow</i>) and returns a pointer to a <i>CDKSCREEN *</i>. Since all of the widgets take a <i>CDKSCREEN</i> pointer as a first argument, this is also one of the first calls made. This also starts curses, so no curses initialization calls have to be made when using Cdk.</dd>
<dt><code>lowerCDKObject</code></dt>
<dd> has the opposite effect of the <code>raiseCDKObject</code> function call.</dd>
<dt><code>raiseCDKObject</code></dt>
<dd> raises the widget to the top of the screen. If there are any widgets which overlap the given object when a refresh is done, calling this function has the effect of raiding the object so no other widgets obstruct it. The <i>widgetType</i> parameter states what Cdk widget type this object is. The <i>object</i> parameter is a void pointer to the object.</dd>
<dt><code>refreshCDKScreen</code></dt>
<dd> redraws all of the widgets which are currently associated to the given screen.</dd>
<dt><code>registerCDKObject</code></dt>
<dd> is called automatically when a widget is created. If for some reason an object does get unregistered, by calling <code>unregisterCDKObject</code>, the widget can be registered again by calling this function. The <i>widgetType</i> parameter states what Cdk widget type this object is. The <i>object</i> parameter is a void pointer to the object.</dd>
<dt><code>unregisterCDKObject</code></dt>
<dd> removes the widget from the screen. This does <code>NOT</code> destroy the object, it removes the widget from any further refreshes by the function <code>refreshCDKScreen</code>. The <i>widgetType</i> parameter states what Cdk widget type this object is. The <i>object</i> parameter is a void pointer to the object.</dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-cdk/">cdk</a></code>(3), <code><a href="/docs/linux/man/3-cdk_binding/">cdk_binding</a></code>(3), <code><a href="/docs/linux/man/3-cdk_display/">cdk_display</a></code>(3) </p>
