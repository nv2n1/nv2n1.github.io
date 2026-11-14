---
title: "cdk_binding(3)"
name: "cdk_binding"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cdk_binding/"
description: "cdk_binding – Curses Development Kit Character Binding Capabilities."
---

<h2>NAME</h2>
<p> cdk_binding &#8211; <code>Curses Development Kit</code> Character Binding Capabilities. </p>
<h2>SYNOPSIS</h2>
<p> <code>cc</code> [ <i>flag</i> &#8230; ] <i>file</i> &#8230; <code>-lcdk</code> [ <i>library</i> &#8230; ] </p>
<pre><code>
#include &lt;cdk.h&gt;

void bindCDKObject(
    EObjectType cdkType,
    void *object,
    chtype key,
    BINDFN function,
    void *data);
int checkCDKObjectBind(
    EObjectType cdkType,
    void *object,
    chtype key);
void cleanCDKObjectBindings(
    EObjectType cdkType,
    void *object);
bool isCDKObjectBind(
    EObjectType cdkType,
    void *object,
    chtype key);
void unbindCDKObject(
    EObjectType cdkType,
    void *object,
    chtype key);
int getcCDKObject(
    CDKOBJS *object);
int getchCDKObject(
    CDKOBJS *object,
    boolean *functionKey);
</code></pre>
</dl>
<h2>DESCRIPTION</h2>
<p> Cdk has the ability to create user definable key bindings. This ability makes Cdk more dynamic and usable for a wide variety of tasks. The following section outlines the binding functions, their use, and their purpose.</p>
<dl>
<dt><code>bindCDKObject</code></p>
<dd> creates a key binding between a specific Cdk widget (<code>object</code>) given key (<code>key</code>). The parameter <code>cdkType</code> is of type <i>EObjectType</i> which is one of the following values.</dl>
<p> <center></p>
<table>
<tr VALIGN=top>
<td><code>EObjectType_Value</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>vALPHALIST
</td>
<td>Alphalist Widget
</td>
</tr>
<tr VALIGN=top>
<td>vBUTTON
</td>
<td>Button Widget
</td>
<td>cdk_button (3)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>
</td>
</tr>
<tr VALIGN=top>
<td>vBUTTONBOX
</td>
<td>Buttonbox Widget
</td>
<td>cdk_buttonbox (3)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>
</td>
</tr>
<tr VALIGN=top>
<td>vCALENDAR
</td>
<td>Calendar Widget
</td>
<td>cdk_calendar (3)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>
</td>
</tr>
<tr VALIGN=top>
<td>vDIALOG
</td>
<td>Dialog Widget
</td>
<td>cdk_dialog (3)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>
</td>
</tr>
<tr VALIGN=top>
<td>vDSCALE
</td>
<td>DoubleFloat Widget
</td>
<td>cdk_dscale (3)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>
</td>
</tr>
<tr VALIGN=top>
<td>vENTRY
</td>
<td>Entry Widget
</td>
<td>cdk_entry (3)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>
</td>
</tr>
<tr VALIGN=top>
<td>vFSCALE
</td>
<td>Floating Scale Widget
</td>
<td>cdk_fscale (3)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>
</td>
</tr>
<tr VALIGN=top>
<td>vFSELECT
</td>
<td>File Selector Widget
</td>
<td>cdk_fselect (3)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>
</td>
</tr>
<tr VALIGN=top>
<td>vFSLIDER
</td>
<td>Floating Slider Widget
</td>
<td>cdk_fslider (3)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>
</td>
</tr>
<tr VALIGN=top>
<td>vGRAPH
</td>
<td>Graph Widget
</td>
<td>cdk_graph (3)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>
</td>
</tr>
<tr VALIGN=top>
<td>vHISTOGRAM
</td>
<td>Histogram Widget
</td>
<td>cdk_histogram (3)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>
</td>
</tr>
<tr VALIGN=top>
<td>vITEMLIST
</td>
<td>Item List Widget
</td>
<td>cdk_itemlist (3)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>
</td>
</tr>
<tr VALIGN=top>
<td>vLABEL
</td>
<td>Label Widget
</td>
<td>cdk_label (3)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>
</td>
</tr>
<tr VALIGN=top>
<td>vMARQUEE
</td>
<td>Marquee Widget
</td>
<td>cdk_marquee (3)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>
</td>
</tr>
<tr VALIGN=top>
<td>vMATRIX
</td>
<td>Matrix Widget
</td>
<td>cdk_matrix (3)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>
</td>
</tr>
<tr VALIGN=top>
<td>vMENTRY
</td>
<td>Multiple Line Entry Widget
</td>
<td>cdk_mentry (3)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>
</td>
</tr>
<tr VALIGN=top>
<td>vMENU
</td>
<td>Menu Widget
</td>
<td>cdk_menu (3)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>
</td>
</tr>
<tr VALIGN=top>
<td>vRADIO
</td>
<td>Radio List Widget
</td>
<td>cdk_radio (3)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>
</td>
</tr>
<tr VALIGN=top>
<td>vSCALE
</td>
<td>Integer Scale Widget
</td>
<td>cdk_scale (3)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>
</td>
</tr>
<tr VALIGN=top>
<td>vSCROLL
</td>
<td>Scrolling List Widget
</td>
<td>cdk_scroll (3)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>
</td>
</tr>
<tr VALIGN=top>
<td>vSELECTION
</td>
<td>Selection List Widget
</td>
<td>cdk_selection (3)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>
</td>
</tr>
<tr VALIGN=top>
<td>vSLIDER
</td>
<td>Slider Widget
</td>
<td>cdk_slider (3)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>
</td>
</tr>
<tr VALIGN=top>
<td>vSWINDOW
</td>
<td>Scrolling Window Widget
</td>
<td>cdk_swindow (3)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>
</td>
</tr>
<tr VALIGN=top>
<td>vTEMPLATE
</td>
<td>Template Entry Widget
</td>
<td>cdk_template (3)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>
</td>
</tr>
<tr VALIGN=top>
<td>vUSCALE
</td>
<td>Unsigned Scale Widget
</td>
<td>cdk_uscale (3)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>
</td>
</tr>
<tr VALIGN=top>
<td>vUSLIDER
</td>
<td>Unsigned Slider Widget
</td>
<td>cdk_uslider (3)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>
</td>
</tr>
<tr VALIGN=top>
<td>vVIEWER
</td>
<td>Viewer Widget
</td>
<td>cdk_viewer (3)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
<hr>
</td>
</tr>
</table>
<p></center></p>
<dl>
<dt>
<dd> The parameter <code>function</code> is the callback function. The parameter <code>data</code> points to data passed to the callback function. The parameter <code>key</code> is the key hit which triggered this callback.</dl>
<dl>
<dt><code>checkCDKObjectBind</code></p>
<dd> check to see if a binding for the given <code>key</code> exists. If it does, Cdk runs the associated command and returns its value, normally TRUE. If no binding exists, return FALSE.</p>
<dt>
<dd> The widgets which accept input, e.g., via &quot;inject&quot; methods, use this to check if the injected character is bound to a function. If that returns TRUE, the widget may update its <i>exitType</i> value: if <i>earlyExit</i> value is set (not equal to vNEVER_ACTIVATED), the widget sets <i>exitType</i> to that value.</p>
<dt><code>cleanCDKObjectBindings</code></p>
<dd> removes all user defined key bindings from the given widget.</p>
<dt><code>isCDKObjectBind</code></p>
<dd> check to see if a binding for the given <code>key</code> exists. If it does return TRUE. If no binding exists, return FALSE.</p>
<dt><code>unbindCDKObject</code></p>
<dd> removes a specific binding to an object. The parameter are the same as for <code>bindCDKObject</code>.</p>
<dt><code>getcCDKObject</code></p>
<dd> reads a keycode from the given widget. This is depcrecated: use <code>getchCDKObject</code>.</p>
<dt><code>getchCDKObject</code></p>
<dd> reads a keycode from the given widget. It sets a flag to indicate if the result is a function key. If the keycode has been bound to the special function <code>getcCDKBind</code>, then it will be translated to the value which was given for the binding data. Otherwise, a few special cases are performed: <center></p>
<table BORDER>
<tr VALIGN=top>
<td><code>Key</code></td>
<td>Result
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>CTRL-A</td>
<td>KEY_HOME
</td>
</tr>
<tr VALIGN=top>
<td>CTRL-B</td>
<td>KEY_LEFT
</td>
</tr>
<tr VALIGN=top>
<td>CTRL-E</td>
<td>KEY_END
</td>
</tr>
<tr VALIGN=top>
<td>CTRL-F</td>
<td>KEY_RIGHT
</td>
</tr>
<tr VALIGN=top>
<td>CTRL-N</td>
<td>tab
</td>
</tr>
<tr VALIGN=top>
<td>CTRL-P</td>
<td>KEY_BTAB
</td>
</tr>
<tr VALIGN=top>
<td>DEL</td>
<td>KEY_DC
</td>
</tr>
<tr VALIGN=top>
<td>backspace</td>
<td>KEY_BACKSPACE
</td>
</tr>
<tr VALIGN=top>
<td>carriage return</td>
<td>KEY_ENTER
</td>
</tr>
<tr VALIGN=top>
<td>newline</td>
<td>KEY_ENTER
</td>
</tr>
</table>
<p></center></dl>
<p> All of the widgets use <code>getchCDKObject</code> internally for consistency.</p>
<h2>EXAMPLE</h2>
<p> To help demonstrate how to use the key bindings I will demonstrate a simple dialog box widget with help for each button. The following code segment creates a dialog box and a callback function named <i>dialogHelpCB</i>. </p>
<pre><code>

________________________________________

#include &lt;cdk.h&gt;
#ifdef HAVE_XCURSES
char *XCursesProgramName = "bind_ex";
#endif
static int dialogHelpCB(EObjectType cdktype GCC_UNUSED, void *object, void *clientData GCC_UNUSED, chtype key GCC_UNUSED)
{
    CDKDIALOG *dialog = (CDKDIALOG *)object;
    char *mesg[5];
    /* Check which button we are on. */
    if (dialog-&gt;currentButton == 0) {
        mesg[0] = "&lt;C&gt;&lt;/U&gt;Help for &lt;/U&gt;Who&lt;!U&gt;.";
        mesg[1] = "&lt;C&gt;When this button is picked the name of the current";
        mesg[2] = "&lt;C&gt;user is displayed on the screen in a popup window.";
        popupLabel(ScreenOf(dialog), mesg, 3);
    } else if (dialog-&gt;currentButton == 1) {
        mesg[0] = "&lt;C&gt;&lt;/U&gt;Help for &lt;/U&gt;Time&lt;!U&gt;.";
        mesg[1] = "&lt;C&gt;When this button is picked the current time is";
        mesg[2] = "&lt;C&gt;displayed on the screen in a popup window.";
        popupLabel(ScreenOf(dialog), mesg, 3);
    } else if (dialog-&gt;currentButton == 2) {
        mesg[0] = "&lt;C&gt;&lt;/U&gt;Help for &lt;/U&gt;Date&lt;!U&gt;.";
        mesg[1] = "&lt;C&gt;When this button is picked the current date is";
        mesg[2] = "&lt;C&gt;displayed on the screen in a popup window.";
        popupLabel(ScreenOf(dialog), mesg, 3);
    } else if (dialog-&gt;currentButton == 3) {
        mesg[0] = "&lt;C&gt;&lt;/U&gt;Help for &lt;/U&gt;Quit&lt;!U&gt;.";
        mesg[1] = "&lt;C&gt;When this button is picked the dialog box is exited.";
        popupLabel(ScreenOf(dialog), mesg, 2);
    }
    return (FALSE);
}
int main(void)
{
    /* Declare variables. */
    CDKSCREEN *cdkscreen;
    CDKDIALOG *question;
    WINDOW *cursesWin;
    char *buttons[40];
    char *message[40], *info[5], *loginName;
    char temp[256];
    int selection;
    time_t clck;
    struct tm *currentTime;
    /* Set up CDK. */
    cursesWin = initscr();
    cdkscreen = initCDKScreen(cursesWin);
    /* Start color. */
    initCDKColor();
    /* Set up the dialog box. */
    message[0] = "&lt;C&gt;&lt;/U&gt;Simple Command Interface";
    message[1] = "Pick the command you wish to run.";
    message[2] = "&lt;C&gt;Press &lt;/R&gt;?&lt;!R&gt; for help.";
    buttons[0] = "Who";
    buttons[1] = "Time";
    buttons[2] = "Date";
    buttons[3] = "Quit";
    /* Create the dialog box. */
    question = newCDKDialog(cdkscreen, CENTER, CENTER,
                            message, 3, buttons, 4, A_REVERSE,
                            TRUE, TRUE, FALSE);
    /* Check if we got a null value back. */
    if (question == (CDKDIALOG *)0) {
        destroyCDKScreen(cdkscreen);
        /* End curses... */
        endCDK();
        /* Spit out a message. */
        printf("Oops. Can't seem to create the dialog box. Is the window too small?
");
        exit(1);
    }
    /* Create the key binding. */
    bindCDKObject(vDIALOG, question, '?', dialogHelpCB, 0);
    /* Activate the dialog box. */
    selection = 0;
    while (selection != 3) {
        /* Get the users button selection. */
        selection = activateCDKDialog(question, (chtype *)0);
        /* Check the results. */
        if (selection == 0) {
            /* Get the users login name. */
            info[0] = "&lt;C&gt;     &lt;/U&gt;Login Name&lt;!U&gt;     ";
            loginName = getlogin();
            if (loginName == (char *)0) {
                strcpy(temp, "&lt;C&gt;&lt;/R&gt;Unknown");
            } else {
                sprintf(temp, "&lt;C&gt;&lt;%s&gt;", loginName);
            }
            info[1] = copyChar(temp);
            popupLabel(ScreenOf(question), info, 2);
            freeChar(info[1]);
        } else if (selection == 1) {
            /* Print out the time. */
            time(&amp;clck);
            currentTime = localtime(&amp;clck);
            sprintf(temp, "&lt;C&gt;%d:%d:%d", currentTime-&gt;tm_hour,
                    currentTime-&gt;tm_min,
                    currentTime-&gt;tm_sec);
            info[0] = "&lt;C&gt;   &lt;/U&gt;Current Time&lt;!U&gt;   ";
            info[1] = copyChar(temp);
            popupLabel(ScreenOf(question), info, 2);
            freeChar(info[1]);
        } else if (selection == 2) {
            /* Print out the date. */
            time(&amp;clck);
            currentTime = localtime(&amp;clck);
            sprintf(temp, "&lt;C&gt;%d/%d/%02d", currentTime-&gt;tm_mday,
                    currentTime-&gt;tm_mon,
                    currentTime-&gt;tm_year % 100);
            info[0] = "&lt;C&gt;   &lt;/U&gt;Current Date&lt;!U&gt;   ";
            info[1] = copyChar(temp);
            popupLabel(ScreenOf(question), info, 2);
            freeChar(info[1]);
        }
    }
    /* Clean up. */
    destroyCDKDialog(question);
    destroyCDKScreen(cdkscreen);
    delwin(cursesWin);
    endCDK();
    exit(0);
}
</code></pre>
<p> <center> <i>________________________________________</i><br />
 </center> </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-cdk/">cdk</a></code>(3), <code><a href="/docs/linux/man/3-cdk_display/">cdk_display</a></code>(3), <code><a href="/docs/linux/man/3-cdk_screen/">cdk_screen</a></code>(3) </p>
<h2>Index</h2>
