---
title: "cdk_traverse(3)"
name: "cdk_traverse"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cdk_traverse/"
description: "cdk_traverse – functions to support keyboard traversal"
---

<h2>NAME</h2>
<p> cdk_traverse &#8211; functions to support keyboard traversal</p>
<h2>SYNOPSIS</h2>
<p> <code>cc</code> [ <i>flag</i> &#8230; ] <i>file</i> &#8230; <code>-lcdk</code> [ <i>library</i> &#8230; ] </p>
<pre><code>
#include &lt;cdk.h&gt;
CDKOBJS *getCDKFocusCurrent(CDKSCREEN *screen);
CDKOBJS *setCDKFocusCurrent(CDKSCREEN *screen, CDKOBJS *obj);
CDKOBJS *setCDKFocusFirst(CDKSCREEN *screen);
CDKOBJS *setCDKFocusLast(CDKSCREEN *screen);
CDKOBJS *setCDKFocusNext(CDKSCREEN *screen);
CDKOBJS *setCDKFocusPrevious(CDKSCREEN *screen);
int traverseCDKScreen(CDKSCREEN *screen);
void exitOKCDKScreen(CDKSCREEN *screen);
void exitCancelCDKScreen(CDKSCREEN *screen);
void resetCDKScreen(CDKSCREEN *screen);
void exitOKCDKScreenOf(CDKOBJS *obj);
void exitCancelCDKScreenOf(CDKOBJS *obj);
void resetCDKScreenOf(CDKOBJS *obj);

void traverseCDKOnce(
    CDKSCREEN *screen,
    CDKOBJS *curobj,
    int keyCode,
    boolean functionKey,
    CHECK_KEYCODE funcMenuKey);
</code></pre>
</dl>
<h2>DESCRIPTION</h2>
<p> The functions above handle the traversal of a screen populated with various widgets. Once the screen has been created and populated with widgets, a single call to <code>traverseCDKScreen()</code> will allow the user to move between widgets and enter data (or otherwise manipulate widgets). Other functions are provided for use as callbacks by the widgets on the screen. Finally, there are several functions which allow the caller to manipulate the state of the traversal, i.e., the object which has focus. </p>
<p> In order for widgets to be used on a screen which is to be handled by <code>traverseCDKScreen()</code>, it must have the following methods available: </p>
<pre>
   injectCharObj
   inputWindowObj
   focusObj
   unfocusObj
   saveDataObj
   refreshDataObj
</pre>
<p> In addition, the following object properties must be properly handled: </p>
<pre>
   acceptsFocus
   hasFocus
   inputWindow
   dataPtr
   dataType  
</pre>
<p> At the time of this writing, not all widgets have been modified to work with the screen-traversal facility.</p>
<h2>AVAILABLE FUNCTIONS</h2>
<p> <code>int traverseCDKScreen (CDKSCREEN *</code><i>screen</i>);</p>
<dl>
<dt>
<dd> This function contains the main screen traversal engine. It does the following:</p>
<dl>
<dt>
&nbsp;<wbr>1.</p>
<dd> Calls the refreshData method on each of the widgets to tell them to update their appearance to match the data which are referenced by their respective data pointers.</p>
<dt>
&nbsp;<wbr>2.</p>
<dd> Calls the focusObject method on the first widget.</p>
<dt>
&nbsp;<wbr>3.</p>
<dd> Repeats the following until one of the exit functions listed above has been called:</p>
<dl>
<dt>
<dd>
<dl>
<dt>*</p>
<dd> Read a keystroke from the keyboard.</p>
<dt>*</p>
<dd> If the keystroke is ESCAPE and a menu widget is present, activate the menu and traverse it until the user selects an entry or hits TAB.</p>
<dt>*</p>
<dd> If the keystroke is TAB/BACKTAB then call the unfocusObject method on the current widget, and move focus to the next/previous widget (not counting menu widgets). Call the focusObject method on the newly current widget.</p>
<dt>*</p>
<dd> If the keystroke is the EXIT-SAVE keystroke, then call the saveData method on each widget and return 1.</p>
<dt>*</p>
<dd> If the keystroke is the EXIT-CANCEL keystroke, return 0 without saving changes made by the user.</p>
<dt>*</p>
<dd> If the keystroke is the RESET-DATA keystroke, then call the refreshData method on each of the widgets to reset their appearance to match the data values that were present upon entry.</p>
<dt>*</p>
<dd> Otherwise, pass the keystroke to the current widget.</dl>
</dl>
</dl>
</dl>
<dl>
<dt><code>CDKOBJS *getCDKFocusCurrent (CDKSCREEN *</code><i>screen</i>);</p>
<dd> Return a pointer to the object which currently has focus in the given screen.</p>
<dt><code>CDKOBJS *setCDKFocusCurrent (CDKSCREEN *</code><i>screen</i>, CDKOBJS *<i>obj</i>);</p>
<dd> Set the focus to the given object, if the screen contains that object. If the screen does not contain the object, return null. Otherwise, return the object.</p>
<dt><code>CDKOBJS *setCDKFocusFirst (CDKSCREEN *</code><i>screen</i>);</p>
<dd> Set focus on the first object in the given screen.</p>
<dt><code>CDKOBJS *setCDKFocusLast (CDKSCREEN *</code><i>screen</i>);</p>
<dd> Set focus on the last object in the given screen.</p>
<dt><code>CDKOBJS *setCDKFocusNext (CDKSCREEN *</code><i>screen</i>);</p>
<dd> Set focus on the next object in the given screen.</p>
<dt><code>CDKOBJS *setCDKFocusPrevious (CDKSCREEN *</code><i>screen</i>);</p>
<dd> Set focus on the previous object in the given screen.</p>
<dt><code>exitOKCDKScreen</code></p>
<dd>
<dl>
<dt>
<dd> Causes the traversal engine to exit after calling the saveData method for each of the widgets.</dl>
<dt><code>exitOKCDKScreenOf</code></p>
<dd>
<dl>
<dt>
<dd> Calls <code>exitOKCDKScreen()</code> on the screen associated with widget <i>obj</i>. This function was designed to be used as a callback routine for a button widget used as an OK button on a data-entry screen.</dl>
<dt><code>exitCancelCDKScreen </code></p>
<dd>
<dl>
<dt>
<dd> Causes the traversal engine to exit without saving user modified data.</dl>
<dt><code>exitCancelCDKScreenOf</code></p>
<dd>
<dl>
<dt>
<dd> Calls <code>exitCancelCDKScreen()</code> on the screen associated with widget <i>obj</i>. This function was designed to be used as a callback routine for a button widget used as a Cancel button on a data-entry screen.</dl>
<dt><code>resetCDKScreen</code></p>
<dd>
<dl>
<dt>
<dd>
<p> Causes the traversal engine to call the refreshData method for each widget. This will cause any unsaved changes to be discarded and the widget states will be restored to their initial values.</dl>
<dt><code>resetCDKScreenOf</code></p>
<dd>
<dl>
<dt>
<dd> Calls <code>resetCDKScreen()</code> on the screen associated with widget <i>obj</i>. This function was designed to be used as a callback routine for a button widget used as a Reset button on a data-entry screen.</dl>
<dt><code>traverseCDKOnce</code></p>
<dd>
<dl>
<dt>
<dd> This is a utility function, one of the pieces from which you can construct a customized version of <code>traverseCDKScreen</code>.</dl>
</dl>
<h2>BUGS</h2>
<p> Not all widgets have had the extra methods added so that they work with the screen traversal engine.</p>
<h2>AUTHOR</h2>
<p> Grant Edwards, Aspen Research Corporation<br />
 Thomas Dickey and contributors.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-cdk/">cdk</a></code>(3), <code><a href="/docs/linux/man/3-cdk_binding/">cdk_binding</a></code>(3), <code><a href="/docs/linux/man/3-cdk_display/">cdk_display</a></code>(3), <code><a href="/docs/linux/man/3-cdk_screen/">cdk_screen</a></code>(3) </p>
<h2>Index</h2>
