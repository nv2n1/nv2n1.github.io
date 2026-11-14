---
title: "xmspinboxvalidateposition(3)"
name: "xmspinboxvalidateposition"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmspinboxvalidateposition/"
description: "XmSpinBoxValidatePosition — translate the current value of the specified XmSpinBox child into a valid position"
---

<p><code>XmSpinBoxValidatePosition</code> &#8212; translate the current value of the specified XmSpinBox child into a valid position</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/SpinBox.h&gt;
<code>int XmSpinBoxValidatePosition</code>(
<code>Widget textfield</code>,
<code>int *position</code>);</pre>
<h2>Description</h2>
<p>The <code>XmSpinBoxValidatePosition</code> function is a utility that can be used by applications wanting to implement a policy for tracking user modifications to editable <code>XmSpinBox</code> children of type <code>XmNUMERIC</code>. The specifics of when and how the user&#8217;s modifications take effect is left up to the application.</p>
<dl COMPACT>
<dt><i>text_field</i></p>
<dd>The <i>text_field</i> argument specifies the widget ID of the child of the <code>XmSpinBox</code> that is being modified. The requirement on <i>text_field</i> is that it holds the <code>accessTextual</code> trait (already a requirement for children of <code>XmSpinBox</code>). This way, <code>XmSpinBox</code> can extract the string out of the <i>text_field</i> widget (even if it is not an <code>XmTextField</code>).</p>
<dt><i>position</i></p>
<dd>The location pointed to by the position argument is assigned the result of the translation done by <code>XmSpinBoxValidatePosition</code>. <code>XmSpinBoxValidatePosition</code> first checks to make sure this is an <code>XmNUMERIC</code> <code>XmSpinBox</code> child. If it is not, <code>XSmpinBoxValidatePosition</code> sets position to the current position and returns <code>XmCURRENT_VALUE</code>.</dl>
<p> <code>XmSpinBoxValidatePosition</code> attempts to translate the input string to a floating point number. If this translation fails, <code>XmSpinBoxValidatePosition</code> sets position to the current position and returns <code>XmCURRENT_VALUE</code>. </p>
<p> <code>XmSpinBoxValidatePosition</code> converts the floating point number to an integer using the <code>XmNdecimalPoints</code> resource. Extra decimal places are truncated. The resulting integer is range checked to make sure it falls within the valid range defined by <code>XmNminimumValue</code> and <code>XmNmaximumValue</code> inclusive. If the input falls outside this range, <code>XmSpinBoxValidatePosition</code> sets position to the nearest limit and returns either <code>XmMINIMUM_VALUE</code> or <code>XmMAXIMUM_VALUE</code>. </p>
<p> Finally, <code>XmSpinBoxValidatePosition</code> checks the integer to make sure it belongs to the series defined by <code>XmNminimumValue &#8230; XmNminimumValue + ((n &#8211; 1) * XmNincrementValue)</code>. If the integer does not belong to this series, <code>XmSpinBoxValidatePosition</code> sets position to the nearest element which is less than or equal to the integer and returns <code>XmINCREMENT_VALUE</code>. </p>
<p> Otherwise, <code>XmSpinBoxValidatePosition</code> assigns the integer to position and returns <code>XmVALID_VALUE</code>.</p>
<h2>Return Value</h2>
<p>The <code>XmSpinBoxValidatePosition</code> function returns the status of the validation. The set of possible values returned is as follows:</p>
<dl COMPACT>
<dt><code>XmCURRENT_VALUE</code></p>
<dd>Cannot convert, returning current position_value.</p>
<dt><code>XmMINIMUM_VALUE</code></p>
<dd>Less than min.</p>
<dt><code>XmMAXIMUM_VALUE</code></p>
<dd>More than max.</p>
<dt><code>XmINCREMENT_VALUE</code></p>
<dd>Not on increment.</p>
<dt><code>XmVALID_VALUE</code></p>
<dd>Okay.</dl>
<h2>Examples</h2>
<p>This first example demonstrates how the <code>XmSpinBoxValidatePosition</code> function could be used from inside an <code>XmNmodifyVerifyCallback</code> callback installed on the <code>XmSpinBox</code> or the <code>XmSimpleSpinBox</code>: </p>
<pre><tt>/*
 * Install a callback on a spin box arrow press.
 */
 XtAddCallback(sb, XmNmodifyVerifyCallback, ModifyVerifyCB, NULL);
 XtAddCallback(simple_sb, XmNmodifyVerifyCallback, ModifyVerifyCB, NULL);</tt></pre>
<p>with the callback doing: </p>
<pre><tt>void ModifyVerifyCB(widget, call_data, client_data) {
 XmSpinBoxCallbackStruct *cbs = (XmSpinBoxCallbackStruct*) call_data;
 int position;
 Widget textual = NULL;
 if (XtIsSubclass(w, xmSimpleSpinBoxWidgetClass))
 {
 Arg args[1];
 XtSetArg(args[0], XmNtextField, &amp;textual);
 XtGetValues(w, args, 1);
 }
 else if (XtIsSubclass(w, xmSpinBoxWidgetClass))
 textual = cbs-&gt;widget;
 else
 textual = (Widget) NULL;
 ...
 if (XmSpinBoxValidatePosition(textual, &amp;position) == XmCURRENT_VALUE)
 XBell(XtDisplay(w), 0);
 else
 cbs-&gt;position = position;
}</tt></pre>
<p>This second example demonstrates how the <code>XmSpinBoxValidatePosition</code> function could be used from inside an <code>XmNactivateCallback</code> callback installed on the <code>TextField</code> child of the <code>XmSpinBox</code>: </p>
<pre><tt>/*
 * Install a callback on a spin box arrow press.
 */
XtAddCallback(tf, XmNactivateCallback, ModifyVerifyChildCB, NULL);</tt></pre>
<p>with the callback doing: </p>
<pre><tt>void ModifyVerifyChildCB(widget, call_data, client_data) {
 int position;
 Widget textual = widget;
 Arg args[1];
 if (XmSpinBoxValidatePosition (textual, &amp;position) == XmCURRENT_VALUE)
 XBell(XtDisplay(widget), 0);
 /* Set the position constraint resource of the textfield */
 XtSetArg(args[0], XmNposition, position);
 XtSetValues(textual, args, 1);
}</tt></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xmspinbox/">XmSpinBox</a></code>(3), <code><a href="/docs/linux/man/3-xmcreatespinbox/">XmCreateSpinBox</a></code>(3)</p>
