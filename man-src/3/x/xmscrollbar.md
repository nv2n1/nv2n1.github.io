---
title: "xmscrollbar(3)"
name: "xmscrollbar"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmscrollbar/"
description: "XmScrollBar — The ScrollBar widget class"
---

<p><code>XmScrollBar</code> &#8212; The ScrollBar widget class</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/ScrollBar.h&gt;</pre>
<h2>Description</h2>
<p>The ScrollBar widget allows the user to view data that is too large to be displayed all at once. ScrollBars are usually located inside a ScrolledWindow and adjacent to the widget that contains the data to be viewed. When the user interacts with the ScrollBar, the data within the other widget scrolls. </p>
<p> A ScrollBar consists of two arrows placed at each end of a rectangle. The rectangle is called the scroll region. A smaller rectangle, called the slider, is placed within the scroll region. The data is scrolled by clicking either arrow, selecting on the scroll region, or dragging the slider. When an arrow is selected, the slider within the scroll region is moved in the direction of the arrow by an amount supplied by the application. If the mouse button is held down, the slider continues to move at a constant rate. </p>
<p> The ratio of the slider size to the scroll region size typically corresponds to the relationship between the size of the visible data and the total size of the data. For example, if 10 percent of the data is visible, the slider typically occupies 10 percent of the scroll region. This provides the user with a visual clue to the size of the invisible data. </p>
<p> If the ScrollBar parent is an automatic ScrolledWindow, the <code>XmNtraversalOn</code> default is True. Otherwise, the default is False. </p>
<p> ScrollBar holds the <code>XmQTnavigator</code> traits.</p>
<h3>Classes</h3>
<p>ScrollBar inherits behavior, resources, and traits from the <code>Core</code> and <code>XmPrimitive</code> classes. </p>
<p> The class pointer is <code>xmScrollBarWidgetClass</code>. </p>
<p> The class name is <code>XmScrollBar</code>.</p>
<h3>New Resources</h3>
<p>The following table defines a set of widget resources used by the programmer to specify data. The programmer can also set the resource values for the inherited classes to set attributes for this widget. To reference a resource by name or by class in a <code>.Xdefaults</code> file, remove the <code>XmN</code> or <code>XmC</code> prefix and use the remaining letters. To specify one of the defined values for a resource in a <code>.Xdefaults</code> file, remove the <code>Xm</code> prefix and use the remaining letters (in either lowercase or uppercase, but include any underscores between words). The codes in the access column indicate if the given resource can be set at creation time (C), set by using <code>XtSetValues</code> (S), retrieved by using <code>XtGetValues</code> (G), or is not applicable (N/A). </p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=5><code>XmScrollBar Resource Set</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>Name</code></td>
<td><code>Class</code></td>
<td><code>Type</code></td>
<td><code>Default</code></td>
<td><code>Access</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNdecrementCallback</td>
<td>XmCCallback</td>
<td>XtCallbackList</td>
<td>NULL</td>
<td>C
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNdragCallback</td>
<td>XmCCallback</td>
<td>XtCallbackList</td>
<td>NULL</td>
<td>C
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNeditable</td>
<td>XmCEditable</td>
<td>Boolean</td>
<td>True</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNincrement</td>
<td>XmCIncrement</td>
<td>int</td>
<td>1</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNincrementCallback</td>
<td>XmCCallback</td>
<td>XtCallbackList</td>
<td>NULL</td>
<td>C
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNinitialDelay</td>
<td>XmCInitialDelay</td>
<td>int</td>
<td>250 ms</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNmaximum</td>
<td>XmCMaximum</td>
<td>int</td>
<td>100</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNminimum</td>
<td>XmCMinimum</td>
<td>int</td>
<td>0</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNorientation</td>
<td>XmCOrientation</td>
<td>unsigned char</td>
<td>XmVERTICAL</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNpageDecrementCallback</td>
<td>XmCCallback</td>
<td>XtCallbackList</td>
<td>NULL</td>
<td>C
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNpageIncrement</td>
<td>XmCPageIncrement</td>
<td>int</td>
<td>10</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNpageIncrementCallback</td>
<td>XmCCallback</td>
<td>XtCallbackList</td>
<td>NULL</td>
<td>C
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNprocessingDirection</td>
<td>XmCProcessingDirection</td>
<td>unsigned char</td>
<td>dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNrepeatDelay</td>
<td>XmCRepeatDelay</td>
<td>int</td>
<td>50 ms</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNshowArrows</td>
<td>XmCShowArrows</td>
<td>XtEnum</td>
<td>XmEACH_SIDE</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNsliderSize</td>
<td>XmCSliderSize</td>
<td>int</td>
<td>dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNsliderMark</td>
<td>XmCSliderMark</td>
<td>XtEnum</td>
<td>dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNsliderVisual</td>
<td>XmCSliderVisual</td>
<td>XtEnum</td>
<td>XmSHADOWED</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNslidingMode</td>
<td>XmCSlidingMode</td>
<td>XtEnum</td>
<td>XmSLIDER</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNsnapBackMultiple</td>
<td>XmCSnapBackMultiple</td>
<td>unsigned short</td>
<td>MaxValue</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNtoBottomCallback</td>
<td>XmCCallback</td>
<td>XtCallbackList</td>
<td>NULL</td>
<td>C
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNtoTopCallback</td>
<td>XmCCallback</td>
<td>XtCallbackList</td>
<td>NULL</td>
<td>C
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNtroughColor</td>
<td>XmCTroughColor</td>
<td>Pixel</td>
<td>dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNvalue</td>
<td>XmCValue</td>
<td>int</td>
<td>dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNvalueChangedCallback</td>
<td>XmCCallback</td>
<td>XtCallbackList</td>
<td>NULL</td>
<td>C
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
</table>
</table>
<dl COMPACT>
<dt><code>XmNdecrementCallback</code></p>
<dd>Specifies the list of callbacks that is called when the user takes an action that moves the ScrollBar by one increment and the value decreases. The reason passed to the callback is <code>XmCR_DECREMENT</code>.</p>
<dt><code>XmNdragCallback</code></p>
<dd>Specifies the list of callbacks that is called on each incremental change of position when the slider is being dragged. The reason sent by the callback is <code>XmCR_DRAG</code>.</p>
<dt><code>XmNeditable</code></p>
<dd>Specifies how ScrollBar will react to user input. This resource can be True or False values, as follows:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>True</code></p>
<dd>Allows the scrollbar to be sensitive to user input. This is the default value.</p>
<dt><code>False</code></p>
<dd>Makes the Scale scrollbar insensitive to user input. The visual is not greyed out. This value would mostly be used in <code>XmTHERMOMETER</code> mode.</dl>
</dl>
<dd>When <code>XmNeditable</code> is used on a widget it sets the dropsite to <code>XmDROP_SITE_ACTIVE</code>.</p>
<dt><code>XmNincrement</code></p>
<dd>Specifies the amount by which the value increases or decreases when the user takes an action that moves the slider by one increment. The actual change in value is the lesser of <code>XmNincrement</code> and (previous <code>XmNvalue</code>&nbsp;<wbr>&#8211; <code>XmNminimum</code>) when the slider moves to the end of the ScrollBar with the minimum value, and the lesser of <code>XmNincrement</code> and (<code>XmNmaximum</code>&#8211; <code>XmNsliderSize</code>&nbsp;<wbr>&#8211; previous <code>XmNvalue</code>) when the slider moves to the end of the ScrollBar with the maximum value. The value of this resource must be greater than 0 (zero).</p>
<dt><code>XmNincrementCallback</code></p>
<dd>Specifies the list of callbacks that is called when the user takes an action that moves the ScrollBar by one increment and the value increases. The reason passed to the callback is <code>XmCR_INCREMENT</code>.</p>
<dt><code>XmNinitialDelay</code></p>
<dd>Specifies the amount of time in milliseconds to wait before starting continuous slider movement while a button is pressed in an arrow or the scroll region. The value of this resource must be greater than 0 (zero).</p>
<dt><code>XmNmaximum</code></p>
<dd>Specifies the slider&#8217;s maximum value. <code>XmNmaximum</code> must be greater than <code>XmNminimum</code>.</p>
<dt><code>XmNminimum</code></p>
<dd>Specifies the slider&#8217;s minimum value. <code>XmNmaximum</code> must be greater than <code>XmNminimum</code>.</p>
<dt><code>XmNorientation</code></p>
<dd>Specifies whether the ScrollBar is displayed vertically or horizontally. This resource can have values of <code>XmVERTICAL</code> and <code>XmHORIZONTAL</code>.</p>
<dt><code>XmNpageDecrementCallback</code></p>
<dd>Specifies the list of callbacks that is called when the user takes an action that moves the ScrollBar by one page increment and the value decreases. The reason passed to the callback is <code>XmCR_PAGE_DECREMENT</code>.</p>
<dt><code>XmNpageIncrement</code></p>
<dd>Specifies the amount by which the value increases or decreases when the user takes an action that moves the slider by one page increment. The actual change in value is the lesser of <code>XmNpageIncrement</code> and (previous <code>XmNvalue</code>&nbsp;<wbr>&#8211; <code>XmNminimum</code>) when the slider moves to the end of the ScrollBar with the minimum value, and the lesser of <code>XmNpageIncrement</code> and (<code>XmNmaximum</code>&#8211; <code>XmNsliderSize</code>&nbsp;<wbr>&#8211; previous <code>XmNvalue</code>) when the slider moves to the end of the ScrollBar with the maximum value. The value of this resource must be greater than 0 (zero).</p>
<dt><code>XmNpageIncrementCallback</code></p>
<dd>Specifies the list of callbacks that is called when the user takes an action that moves the ScrollBar by one page increment and the value increases. The reason passed to the callback is <code>XmCR_PAGE_INCREMENT</code>.</p>
<dt><code>XmNprocessingDirection</code></p>
<dd>Specifies whether the value for <code>XmNmaximum</code> should be on the right or left side of <code>XmNminimum</code> for horizontal ScrollBars or above or below <code>XmNminimum</code> for vertical ScrollBars. This resource can have values of <code>XmMAX_ON_TOP, XmMAX_ON_BOTTOM, XmMAX_ON_LEFT</code>, and <code>XmMAX_ON_RIGHT</code>. If the ScrollBar is oriented vertically, the default value is <code>XmMAX_ON_BOTTOM</code>. If the ScrollBar is oriented horizontally, the default value depends on the <code>XmNlayoutDirection</code> resource of the widget.</p>
<dt><code>XmNrepeatDelay</code></p>
<dd>Specifies the amount of time in milliseconds to wait between subsequent slider movements after the <code>XmNinitialDelay</code> has been processed. The value of this resource must be greater than 0 (zero).</p>
<dt><code>XmNshowArrows</code></p>
<dd>Specifies whether the arrows are displayed and how they are to be displayed. This resource can take the following values:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>XmEACH_SIDE</code></p>
<dd>Indicates that one arrow is displayed on each end of the ScrollBar slider. This corresponds to a value of True in previous releases.</p>
<dt><code>XmMAX_SIDE</code></p>
<dd>Indicates that both arrows are displayed on the <code>XmNmaximum</code> side of the ScrollBar slider.</p>
<dt><code>XmMIN_SIDE</code></p>
<dd>Indicates that both arrows are displayed on the <code>XmNminimum</code> side of the ScrollBar slider.</p>
<dt><code>XmNONE</code></p>
<dd>Indicates that no arrows are displayed. This corresponds to a value of False in previous releases.</dl>
</dl>
<dd><code>XmEACH_SIDE</code> is the default value.</p>
<dt><code>XmNsliderMark</code></p>
<dd>Specifies the shape the slider is to be displayed in. This resource can take the following values:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>XmETCHED_LINE</code></p>
<dd>Specifies the slider as an etched line.</p>
<dt><code>XmNONE</code></p>
<dd>Specifies the slider as a foregrounded rectangle. This is the default for a regular slider.</p>
<dt><code>XmROUND_MARK</code></p>
<dd>Specifies the slider as a shadowed circle. This is the default when the slider is a thermometer.</p>
<dt><code>XmTHUMB_MARK</code></p>
<dd>Specifies the slider as a series of three etched lines centered in the middle of the slider.</dl>
</dl>
<dt><code>XmNslidingMode</code></p>
<dd>Specifies the mode the slider works in. There are two possible modes:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>XmSLIDER</code></p>
<dd>Allows the slider to move freely between the minimum and maximum ends of the scale. This is the default value.</p>
<dt><code>XmTHERMOMETER</code></p>
<dd>Forces the slider to be anchored to one side of the trough area.</dl>
</dl>
<dt><code>XmNsliderSize</code></p>
<dd>Specifies the length of the slider between the values of 1 and (<code>XmNmaximum</code>&nbsp;<wbr>&#8211; <code>XmNminimum</code>). The value is constrained to be within these inclusive bounds. The default value is (<code>XmNmaximum</code>&nbsp;<wbr>&#8211; <code>XmNminimum</code>) divided by 10, with a minimum of 1.</p>
<dt><code>XmNsliderVisual</code></p>
<dd>Specifies the color of the slider visual. This resource can take the following values:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt><code>XmBACKGROUND_COLOR</code></p>
<dd>Specifies that the slider visual is in the background color.</p>
<dt><code>XmFOREGROUND_COLOR</code></p>
<dd>Specifies that the slider visual is in the foreground color.</p>
<dt><code>XmSHADOWED_BACKGROUND</code></p>
<dd>Specifies that the slider visual is in the background color, with a shadow. This is the default for a regular slider.</p>
<dt><code>XmTROUGH_COLOR</code></p>
<dd>Specifies that the slider visual is in the trough color. This is the default when the slider is a thermometer.</dl>
</dl>
<dt><code>XmNsnapBackMultiple</code></p>
<dd>Specifies the distance over which the scrollbar slider snaps back to its original position when the user drags the mouse outside the ScrollBar edge. This distance is defined in terms of multiples of the width of the slider. For example, a multiple of 0 (zero) causes the slider to snap back as soon as the pointer moves out of the ScrollBar frame, a multiple of 1 causes the slider to snap back as soon as the pointer moves beyond 1 ScrollBar width of the ScrollBar edge. Whenever the slider snaps back, the ScrollBar <code>dragCallback</code> is called if there is one.</p>
<dd>The default value is large enough to prevent unwanted snapBack activity if the mouse is moved within the boundaries of any reasonable screen. To reset the default, set this resource to a large value, such as 10000.</p>
<dt><code>XmNtoBottomCallback</code></p>
<dd>Specifies the list of callbacks that is called when the user takes an action that moves the slider to the end of the ScrollBar with the maximum value. The reason passed to the callback is <code>XmCR_TO_BOTTOM</code>.</p>
<dt><code>XmNtoTopCallback</code></p>
<dd>Specifies the list of callbacks that is called when the user takes an action that moves the slider to the end of the ScrollBar with the minimum value. The reason passed to the callback is <code>XmCR_TO_TOP</code>.</p>
<dt><code>XmNtroughColor</code></p>
<dd>Specifies the color of the slider trough. This color defaults to the color used for selections.</p>
<dt><code>XmNvalue</code></p>
<dd>Specifies the slider&#8217;s position, between <code>XmNminimum</code> and (<code>XmNmaximum</code>&nbsp;<wbr>&#8211; <code>XmNsliderSize</code>). The value is constrained to be within these inclusive bounds. The initial value of this resource is the larger of 0 (zero) and <code>XmNminimum</code>.</p>
<dt><code>XmNvalueChangedCallback</code></p>
<dd>Specifies the list of callbacks that is called when the slider is released after being dragged. These callbacks are also called in place of <code>XmNincrementCallback</code>, <code>XmNdecrementCallback</code>, <code>XmNpageIncrementCallback</code>, <code>XmNpageDecrementCallback</code>, <code>XmNtoTopCallback</code>, or <code>XmNtoBottomCallback</code> when one of these callback lists would normally be called but the value of the corresponding resource is NULL. The reason passed to the callback is <code>XmCR_VALUE_CHANGED</code>.</dl>
<h3>Inherited Resources</h3>
<p>ScrollBar inherits behavior and resources from the superclasses described in the following tables. For a complete description of each resource, refer to the reference page for that superclass. </p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=5><code>XmPrimitive Resource Set</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>Name</code></td>
<td><code>Class</code></td>
<td><code>Type</code></td>
<td><code>Default</code></td>
<td><code>Access</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNbottomShadowColor</td>
<td>XmCBottomShadowColor</td>
<td>Pixel</td>
<td>dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNbottomShadowPixmap</td>
<td>XmCBottomShadowPixmap</td>
<td>Pixmap</td>
<td>XmUNSPECIFIED_PIXMAP</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNconvertCallback</td>
<td>XmCCallback</td>
<td>XtCallbackList</td>
<td>NULL</td>
<td>C
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNforeground</td>
<td>XmCForeground</td>
<td>Pixel</td>
<td>dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNhelpCallback</td>
<td>XmCCallback</td>
<td>XtCallbackList</td>
<td>NULL</td>
<td>C
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNhighlightColor</td>
<td>XmCHighlightColor</td>
<td>Pixel</td>
<td>dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNhighlightOnEnter</td>
<td>XmCHighlightOnEnter</td>
<td>Boolean</td>
<td>False</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNhighlightPixmap</td>
<td>XmCHighlightPixmap</td>
<td>Pixmap</td>
<td>dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNhighlightThickness</td>
<td>XmCHighlightThickness</td>
<td>Dimension</td>
<td>dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNlayoutDirection</td>
<td>XmCLayoutDirection</td>
<td>XmDirection</td>
<td>dynamic</td>
<td>CG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNnavigationType</td>
<td>XmCNavigationType</td>
<td>XmNavigationType</td>
<td>XmSTICKY_TAB_GROUP</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNpopupHandlerCallback</td>
<td>XmCCallback</td>
<td>XtCallbackList</td>
<td>NULL</td>
<td>C
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNshadowThickness</td>
<td>XmCShadowThickness</td>
<td>Dimension</td>
<td>2</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNtopShadowColor</td>
<td>XmCTopShadowColor</td>
<td>Pixel</td>
<td>dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNtopShadowPixmap</td>
<td>XmCTopShadowPixmap</td>
<td>Pixmap</td>
<td>dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNtraversalOn</td>
<td>XmCTraversalOn</td>
<td>Boolean</td>
<td>dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNunitType</td>
<td>XmCUnitType</td>
<td>unsigned char</td>
<td>dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNuserData</td>
<td>XmCUserData</td>
<td>XtPointer</td>
<td>NULL</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
</table>
</table>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=5><code>Core Resource Set</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>Name</code></td>
<td><code>Class</code></td>
<td><code>Type</code></td>
<td><code>Default</code></td>
<td><code>Access</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNaccelerators</td>
<td>XmCAccelerators</td>
<td>XtAccelerators</td>
<td>dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNancestorSensitive</td>
<td>XmCSensitive</td>
<td>Boolean</td>
<td>dynamic</td>
<td>G
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNbackground</td>
<td>XmCBackground</td>
<td>Pixel</td>
<td>dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNbackgroundPixmap</td>
<td>XmCPixmap</td>
<td>Pixmap</td>
<td>XmUNSPECIFIED_PIXMAP</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNborderColor</td>
<td>XmCBorderColor</td>
<td>Pixel</td>
<td>XtDefaultForeground</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNborderPixmap</td>
<td>XmCPixmap</td>
<td>Pixmap</td>
<td>XmUNSPECIFIED_PIXMAP</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNborderWidth</td>
<td>XmCBorderWidth</td>
<td>Dimension</td>
<td>0</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNcolormap</td>
<td>XmCColormap</td>
<td>Colormap</td>
<td>dynamic</td>
<td>CG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNdepth</td>
<td>XmCDepth</td>
<td>int</td>
<td>dynamic</td>
<td>CG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNdestroyCallback</td>
<td>XmCCallback</td>
<td>XtCallbackList</td>
<td>NULL</td>
<td>C
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNheight</td>
<td>XmCHeight</td>
<td>Dimension</td>
<td>dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNinitialResourcesPersistent</td>
<td>XmCInitialResourcesPersistent</td>
<td>Boolean</td>
<td>True</td>
<td>C
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNmappedWhenManaged</td>
<td>XmCMappedWhenManaged</td>
<td>Boolean</td>
<td>True</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNscreen</td>
<td>XmCScreen</td>
<td>Screen *</td>
<td>dynamic</td>
<td>CG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNsensitive</td>
<td>XmCSensitive</td>
<td>Boolean</td>
<td>True</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNtranslations</td>
<td>XmCTranslations</td>
<td>XtTranslations</td>
<td>dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNwidth</td>
<td>XmCWidth</td>
<td>Dimension</td>
<td>dynamic</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNx</td>
<td>XmCPosition</td>
<td>Position</td>
<td>0</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNy</td>
<td>XmCPosition</td>
<td>Position</td>
<td>0</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
</table>
</table>
<h3>Callback Information</h3>
<p>A pointer to the following structure is passed to each callback: </p>
<pre>typedef struct
{
 int <i>reason</i>;
 XEvent <i>* event</i>;
 int <i>value</i>;
 int <i>pixel</i>;
} XmScrollBarCallbackStruct;</pre>
<dl COMPACT>
<dt><i>reason</i></p>
<dd>Indicates why the callback was invoked.</p>
<dt><i>event</i></p>
<dd>Points to the <code>XEvent</code> that triggered the callback.</p>
<dt><i>value</i></p>
<dd>Contains the new slider location value.</p>
<dt><i>pixel</i></p>
<dd>Is used only for <code>XmNtoTopCallback</code> and <code>XmNtoBottomCallback</code>. For horizontal ScrollBars, it contains the <i>x</i> coordinate of where the mouse button selection occurred. For vertical ScrollBars, it contains the <i>y</i> coordinate.</dl>
<h3>Translations</h3>
<p><code>XmScrollBar</code> includes translations from Primitive. The <code>XmScrollBar</code> translations are described in the following list. </p>
<p> The following key names are listed in the X standard key event translation table syntax. This format is the one used by Motif to specify the widget actions corresponding to a given key. A brief overview of the format is provided under <code><a href="/docs/linux/man/3-virtualbindings/">VirtualBindings</a></code>(3). For a complete description of the format, please refer to the X Toolkit Instrinsics Documentation.</p>
<dl COMPACT>
<dt><code>&asymp;s &asymp;c &asymp;m &asymp;a</code> <code>&lt;Btn1Down&gt;</code>:</p>
<dd>Select()</p>
<dt><code>&asymp;s &asymp;c &asymp;m &asymp;a</code> <code>&lt;Btn1Up&gt;</code>:</p>
<dd>Release()</p>
<dt><code>&asymp;s &asymp;c &asymp;m &asymp;a Button1</code><code>&lt;PtrMoved&gt;</code>:</p>
<dd>Moved()</p>
<dt><code>&asymp;s &asymp;c &asymp;m &asymp;a</code> <code>&lt;Btn2Down&gt;</code>:</p>
<dd>Select()</p>
<dt><code>&asymp;s &asymp;c &asymp;m &asymp;a</code> <code>&lt;Btn2Up&gt;</code>:</p>
<dd>Release()</p>
<dt><code>&asymp;s &asymp;c &asymp;m &asymp;a Button2</code><code>&lt;PtrMoved&gt;</code>:</p>
<dd>Moved()</p>
<dt><code>&asymp;s c &asymp;m &asymp;a</code> <code>&lt;Btn1Down&gt;</code>:</p>
<dd>TopOrBottom()</p>
<dt><code>&asymp;s c &asymp;m &asymp;a</code> <code>&lt;Btn1Up&gt;</code>:</p>
<dd>Release()</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfActivate&gt;</code>:</p>
<dd>PrimitiveParentActivate()</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfCancel&gt;</code>:</p>
<dd>CancelDrag()</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfBeginLine&gt;</code>:</p>
<dd>TopOrBottom()</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfEndLine&gt;</code>:</p>
<dd>TopOrBottom()</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfPageLeft&gt;</code>:</p>
<dd>PageUpOrLeft(<code>Left</code>)</p>
<dt><code>:c</code> <code>&lt;Key&gt;</code><code>&lt;osfPageUp&gt;</code>:</p>
<dd>PageUpOrLeft(<code>Left</code>)</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfPageUp&gt;</code>:</p>
<dd>PageUpOrLeft(<code>Up</code>)</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfPageRight&gt;</code>:</p>
<dd>PageDownOrRight(<code>Right</code>)</p>
<dt><code>:c</code> <code>&lt;Key&gt;</code><code>&lt;osfPageDown&gt;</code>:</p>
<dd>PageDownOrRight(<code>Right</code>)</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfPageDown&gt;</code>:</p>
<dd>PageDownOrRight(<code>Down</code>)</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfHelp&gt;</code>:</p>
<dd>PrimitiveHelp()</p>
<dt><code>:c</code> <code>&lt;Key&gt;</code><code>&lt;osfUp&gt;</code>:</p>
<dd>PageUpOrLeft(<code>Up</code>)</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfUp&gt;</code>:</p>
<dd>IncrementUpOrLeft(<code>Up</code>)</p>
<dt><code>:c</code> <code>&lt;Key&gt;</code><code>&lt;osfDown&gt;</code>:</p>
<dd>PageDownOrRight(<code>Down</code>)</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfDown&gt;</code>:</p>
<dd>IncrementDownOrRight(<code>Down</code>)</p>
<dt><code>:c</code> <code>&lt;Key&gt;</code><code>&lt;osfLeft&gt;</code>:</p>
<dd>PageUpOrLeft(<code>Left</code>)</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfLeft&gt;</code>:</p>
<dd>IncrementUpOrLeft(<code>Left</code>)</p>
<dt><code>:c</code> <code>&lt;Key&gt;</code><code>&lt;osfRight&gt;</code>:</p>
<dd>PageDownOrRight(<code>Right</code>)</p>
<dt><code>:</code><code>&lt;Key&gt;</code><code>&lt;osfRight&gt;</code>:</p>
<dd>IncrementDownOrRight(<code>Right</code>)</p>
<dt><code>&asymp;s &asymp;m &asymp;a</code> <code>&lt;Key&gt;</code><code>Return</code>:</p>
<dd>PrimitiveParentActivate()</p>
<dt><code>s &asymp;m &asymp;a</code> <code>&lt;Key&gt;</code><code>Tab</code>:</p>
<dd>PrimitivePrevTabGroup()</p>
<dt><code>&asymp;m &asymp;a</code> <code>&lt;Key&gt;</code><code>Tab</code>:</p>
<dd>PrimitiveNextTabGroup()</dl>
<h3>Action Routines</h3>
<p>The ScrollBar action routines are</p>
<dl COMPACT>
<dt>CancelDrag():</p>
<dd>If the key press occurs during scrolling, cancels the scroll and returns the slider to its previous location in the scrollbar, otherwise, and if the parent is a manager, it passes the event to the parent.</p>
<dt>IncrementDownOrRight(<code>Down|Right</code>):</p>
<dd>With an argument of <code>Down</code>, or 0 (zero) for compatibility, moves the slider down by one increment. With an argument of <code>Right</code>, or 1 for compatibility, it moves the slider right by one increment. If <code>XmNprocessingDirection</code> is <code>XmMAX_ON_RIGHT</code> or <code>XmMAX_ON_BOTTOM</code>, movement toward the right or bottom calls the callbacks for <code>XmNincrementCallback</code>. If <code>XmNprocessingDirection</code> is <code>XmMAX_ON_LEFT</code> or <code>XmMAX_ON_TOP</code>, movement toward the right or bottom calls the callbacks for <code>XmNdecrementCallback</code>. The <code>XmNvalueChangedCallback</code> is called if the <code>XmNincrementCallback</code> or <code>XmNdecrementCallback</code> is NULL.</p>
<dt>IncrementUpOrLeft(<code>Up|Left</code>):</p>
<dd>With an argument of <code>Up</code>, or 0 (zero) for compatibility, moves the slider up by one increment. With an argument of <code>Left</code>, or 1 for compatibility, it moves the slider left by one increment. If <code>XmNprocessingDirection</code> is <code>XmMAX_ON_RIGHT</code> or <code>XmMAX_ON_BOTTOM</code>, movement to the left or top calls the callbacks for <code>XmNdecrementCallback</code>. If <code>XmNprocessingDirection</code> is <code>XmMAX_ON_LEFT</code> or <code>XmMAX_ON_TOP</code>, movement to the left or top calls the callbacks for <code>XmNincrementCallback</code>. The <code>XmNvalueChangedCallback</code> is called if the <code>XmNincrementCallback</code> or <code>XmNdecrementCallback</code> is NULL.</p>
<dt>Moved():</p>
<dd>If the button press occurs within the slider, the subsequent motion events move the slider to the position of the pointer and call the callbacks for <code>XmNdragCallback</code>.</p>
<dt>PageDownOrRight(<code>Down|Right</code>):</p>
<dd>With an argument of <code>Down</code>, or 0 (zero) for compatibility, moves the slider down by one page increment. With an argument of <code>Right</code>, or 1 for compatibility, moves the slider right by one page increment. If <code>XmNprocessingDirection</code> is <code>XmMAX_ON_RIGHT</code> or <code>XmMAX_ON_BOTTOM</code>, movement toward the right or bottom calls the callbacks for <code>XmNpageIncrementCallback</code>. If <code>XmNprocessingDirection</code> is <code>XmMAX_ON_LEFT</code> or <code>XmMAX_ON_TOP</code>, movement toward the right or bottom calls the <code>XmNpageDecrementCallback</code> callbacks. The <code>XmNvalueChangedCallback</code> is called if the <code>XmNpageIncrementCallback</code> or <code>XmNpageDecrementCallback</code> is NULL.</p>
<dt>PageUpOrLeft(<code>Up|Left</code>):</p>
<dd>With an argument of <code>Up</code>, or 0 (zero) for compatibility, moves the slider up by one page increment. With an argument of <code>Left</code>, or 1 for compatibility, it moves the slider left by one page increment. If <code>XmNprocessingDirection</code> is <code>XmMAX_ON_RIGHT</code> or <code>XmMAX_ON_BOTTOM</code>, movement to the left or top calls the callbacks for <code>XmNpageDecrementCallback</code>. If <code>XmNprocessingDirection</code> is <code>XmMAX_ON_LEFT</code> or <code>XmMAX_ON_TOP</code>, movement to the left or top calls the <code>XmNpageIncrementCallback</code> callbacks. The <code>XmNvalueChangedCallback</code> is called if the <code>XmNpageIncrementCallback</code> or <code>XmNpageDecrementCallback</code> is NULL.</p>
<dt>PrimitiveHelp():</p>
<dd>Calls the callbacks for <code>XmNhelpCallback</code> if any exist. If there are no help callbacks for this widget, this action calls the help callbacks for the nearest ancestor that has them.</p>
<dt>PrimitiveNextTabGroup():</p>
<dd>Traverses to the first item in the next tab group. If the current tab group is the last entry in the tab group list, it wraps to the beginning of the tab group list.</p>
<dt>PrimitiveParentActivate():</p>
<dd>If the parent is a manager, passes the event to the parent.</p>
<dt>PrimitivePrevTabGroup():</p>
<dd>Traverses to the first item in the previous tab group. If the beginning of the tab group list is reached, it wraps to the end of the tab group list.</p>
<dt>Release():</p>
<dd>If the button press occurs within the slider and the slider position is changed, the callbacks for <code>XmNvalueChangedCallback</code> are called.</p>
<dt>Select():</p>
<dd><code>In arrow</code>: Moves the slider by one increment in the direction of the arrow. If <code>XmNprocessingDirection</code> is <code>XmMAX_ON_RIGHT</code> or <code>XmMAX_ON_BOTTOM</code>, movement toward the right or bottom calls the callbacks for <code>XmNincrementCallback</code>, and movement to the left or top calls the callbacks for <code>XmNdecrementCallback</code>. If <code>XmNprocessingDirection</code> is <code>XmMAX_ON_LEFT</code> or <code>XmMAX_ON_TOP</code>, movement toward the right or bottom calls the callbacks for <code>XmNdecrementCallback</code>, and movement to the left or top calls the callbacks for <code>XmNincrementCallback</code>. The <code>XmNvalueChangedCallback</code> is called if the <code>XmNincrementCallback</code> or <code>XmNdecrementCallback</code> is NULL.</p>
<dd><code>In scroll region between an arrow and the slider</code>: Moves the slider by one page increment in the direction of the arrow. If <code>XmNprocessingDirection</code> is <code>XmMAX_ON_RIGHT</code> or <code>XmMAX_ON_BOTTOM</code>, movement toward the right or bottom calls the callbacks for <code>XmNpageIncrementCallback</code>, and movement to the left or top calls the callbacks for <code>XmNpageDecrementCallback</code>. If <code>XmNprocessingDirection</code> is <code>XmMAX_ON_LEFT</code> or <code>XmMAX_ON_TOP</code>, movement toward the right or bottom calls the callbacks for <code>XmNpageDecrementCallback</code>, and movement to the left or top calls the callbacks for <code>XmNpageIncrementCallback</code>. The <code>XmNvalueChangedCallback</code> is called if the <code>XmNpageIncrementCallback</code> or <code>XmNpageDecrementCallback</code> is NULL.</p>
<dd><code>In slider</code>: Activates the interactive dragging of the slider.</p>
<dd>If the button is held down in either the arrows or the scroll region longer than the <code>XmNinitialDelay</code> resource, the slider is moved again by the same increment and the same callbacks are called. After the initial delay has been used, the time delay changes to the time defined by the resource <code>XmNrepeatDelay</code>.</p>
<dt>TopOrBottom():</p>
<dd><code>&lt;Ctrl&gt;</code><code>&lt;Btn1Down&gt;</code> in an arrow or in the scroll region between an arrow and the slider moves the slider as far as possible in the direction of the arrow. If <code>XmNprocessingDirection</code> is <code>XmMAX_ON_RIGHT</code> or <code>XmMAX_ON_BOTTOM</code>, movement toward the right or bottom calls the callbacks for <code>XmNtoBottomCallback</code>, and movement to the left or top calls the callbacks for <code>XmNtoTopCallback</code>. If <code>XmNprocessingDirection</code> is <code>XmMAX_ON_LEFT</code> or <code>XmMAX_ON_TOP</code>, movement toward the right or bottom calls the callbacks for <code>XmNtoTopCallback</code>, and movement to the left or top calls the callbacks for <code>XmNtoBottomCallback</code>. The <code>XmNvalueChangedCallback</code> is called if the <code>XmNtoTopCallback</code> or <code>XmNtoBottomCallback</code> is NULL. Pressing <code>&lt;Key&gt;</code><code>&lt;osfBeginLine&gt;</code> or <code>&lt;Key&gt;</code><code>&lt;osfBeginData&gt;</code> moves the slider to the minimum value and invokes the <code>XmNtoTopCallback</code>. Pressing <code>&lt;Key&gt;</code><code>&lt;osfEndLine&gt;</code> or <code>&lt;Key&gt;</code><code>&lt;osfEndData&gt;</code> moves the slider to the maximum value and invokes the <code>XmNtoBottomCallback</code>.</dl>
<h3>Virtual Bindings</h3>
<p>The bindings for virtual keys are vendor specific. For information about bindings for virtual buttons and keys, see <code><a href="/docs/linux/man/3-virtualbindings/">VirtualBindings</a></code>(3).</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-core/">Core</a></code>(3), <code><a href="/docs/linux/man/3-xmcreatescrollbar/">XmCreateScrollBar</a></code>(3), <code><a href="/docs/linux/man/3-xmprimitive/">XmPrimitive</a></code>(3), <code><a href="/docs/linux/man/3-xmscrollbargetvalues/">XmScrollBarGetValues</a></code>(3), <code><a href="/docs/linux/man/3-xmscrollbarsetvalues/">XmScrollBarSetValues</a></code>(3), <code><a href="/docs/linux/man/3-xmvacreatescrollbar/">XmVaCreateScrollBar</a></code>(3), and <code><a href="/docs/linux/man/3-xmvacreatemanagedscrollbar/">XmVaCreateManagedScrollBar</a></code>(3).</p>
