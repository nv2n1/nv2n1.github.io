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
<dt><code>destroyCDKScreen</code></p>
<dd> frees any memory allocated by the Cdk screen pointer.</p>
<dt><code>endCDK</code></p>
<dd> cleans up any memory created by starting Cdk and shuts down curses.</p>
<dt><code>eraseCDKScreen</code></p>
<dd> erases all of the widgets which are currently associated to the given screen. This does <code>NOT</code> destroy the widgets.</p>
<dt><code>initCDKColor</code></p>
<dd> starts the Cdk color capabilities. It defines 64 color pairs each of which is accessible using the COLOR_PAIR macro. If you do not have color support, this function call makes no difference.</p>
<dt><code>initCDKScreen</code></p>
<dd> takes a <i>WINDOW *</i> (<i>cursesWindow</i>) and returns a pointer to a <i>CDKSCREEN *</i>. Since all of the widgets take a <i>CDKSCREEN</i> pointer as a first argument, this is also one of the first calls made. This also starts curses, so no curses initialization calls have to be made when using Cdk.</p>
<dt><code>lowerCDKObject</code></p>
<dd> has the opposite effect of the <code>raiseCDKObject</code> function call.</p>
<dt><code>raiseCDKObject</code></p>
<dd> raises the widget to the top of the screen. If there are any widgets which overlap the given object when a refresh is done, calling this function has the effect of raiding the object so no other widgets obstruct it. The <i>widgetType</i> parameter states what Cdk widget type this object is. The <i>object</i> parameter is a void pointer to the object.</p>
<dt><code>refreshCDKScreen</code></p>
<dd> redraws all of the widgets which are currently associated to the given screen.</p>
<dt><code>registerCDKObject</code></p>
<dd> is called automatically when a widget is created. If for some reason an object does get unregistered, by calling <code>unregisterCDKObject</code>, the widget can be registered again by calling this function. The <i>widgetType</i> parameter states what Cdk widget type this object is. The <i>object</i> parameter is a void pointer to the object.</p>
<dt><code>unregisterCDKObject</code></p>
<dd> removes the widget from the screen. This does <code>NOT</code> destroy the object, it removes the widget from any further refreshes by the function <code>refreshCDKScreen</code>. The <i>widgetType</i> parameter states what Cdk widget type this object is. The <i>object</i> parameter is a void pointer to the object.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-cdk/">cdk</a></code>(3), <code><a href="/docs/linux/man/3-cdk_binding/">cdk_binding</a></code>(3), <code><a href="/docs/linux/man/3-cdk_display/">cdk_display</a></code>(3) </p>
<h2>Index</h2>
