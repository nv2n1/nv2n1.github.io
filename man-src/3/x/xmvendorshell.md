---
title: "xmvendorshell(3)"
name: "xmvendorshell"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmvendorshell/"
description: "VendorShell – Motif-compatible replacement for X Intrinsics VendorShell"
---

<p>VendorShell &#8211; Motif-compatible replacement for X Intrinsics VendorShell</p>
<h2>Synopsis</h2>
<p><code>#include &lt;<a href="file:/usr/include/Xm/Shell.h">Xm/Shell.h</a>&gt;</code> </p>
<p> <code>VendorShell</code></p>
<h2>Description</h2>
<p>VendorShell is a widget class that replaces the X Intrinsics VendorShell widget class. Yes: they have the same name. </p>
<p> The LessTif implementation of VendorShell provides an API for use by applications for interacting with the window manager.</p>
<h2>X Resources</h2>
<table>
<tr VALIGN=top>
<td>Name</td>
<td>Class</td>
<td>Type</td>
<td>Default</td>
<td>Access
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>XmNdefaultFontList</td>
<td>XmCDefaultFontList</td>
<td>FontList</td>
<td>NULL</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>XmNbuttonFontList</td>
<td>XmCButtonFontList</td>
<td>FontList</td>
<td>NULL</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>XmNlabelFontList</td>
<td>XmCLabelFontList</td>
<td>FontList</td>
<td>NULL</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>XmNtextFontList</td>
<td>XmCTextFontList</td>
<td>FontList</td>
<td>NULL</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>XmNaudibleWarning</td>
<td>XmCAudibleWarning</td>
<td>AudibleWarning</td>
<td>NULL</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>XmNshellUnitType</td>
<td>XmCShellUnitType</td>
<td>UnitType</td>
<td>NULL</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>XmNdeleteResponse</td>
<td>XmCDeleteResponse</td>
<td>DeleteResponse</td>
<td>NULL</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>XmNkeyboardFocusPolicy</td>
<td>XmCKeyboardFocusPolicy</td>
<td>KeyboardFocusPolicy</td>
<td>NULL</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>XmNmwmDecorations</td>
<td>XmCMwmDecorations</td>
<td>Int</td>
<td>-1</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>XmNmwmFunctions</td>
<td>XmCMwmFunctions</td>
<td>Int</td>
<td>-1</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>XmNmwmInputMode</td>
<td>XmCMwmInputMode</td>
<td>Int</td>
<td>-1</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>XmNmwmMenu</td>
<td>XmCMwmMenu</td>
<td>String</td>
<td>NULL</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>XmNfocusMovedCallback</td>
<td>XmCCallback</td>
<td>Callback</td>
<td>NULL</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>XmNrealizeCallback</td>
<td>XmCCallback</td>
<td>Callback</td>
<td>NULL</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>XmNinputMethod</td>
<td>XmCInputMethod</td>
<td>String</td>
<td>NULL</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>XmNpreeditType</td>
<td>XmCPreeditType</td>
<td>String</td>
<td>NULL</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>XmNlightThreshold</td>
<td>XmCLightThreshold</td>
<td>Int</td>
<td>0</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>XmNdarkThreshold</td>
<td>XmCDarkThreshold</td>
<td>Int</td>
<td>0</td>
<td>CSG
</td>
</tr>
<tr VALIGN=top>
<td>XmNforegroundThreshold</td>
<td>XmCForegroundThreshold</td>
<td>Int</td>
<td>0</td>
<td>CSG
</td>
</tr>
</table>
<p> <code>XmNdefaultFontList</code> </p>
<p> <code>XmNbuttonFontList</code> </p>
<p> <code>XmNlabelFontList</code> </p>
<p> <code>XmNtextFontList</code> </p>
<p> <code>XmNaudibleWarning</code> </p>
<p> <code>XmNshellUnitType</code> </p>
<p> <code>XmNdeleteResponse</code> </p>
<p> <code>XmNkeyboardFocusPolicy</code> </p>
<p> <code>XmNmwmDecorations</code> </p>
<p> <code>XmNmwmFunctions</code> </p>
<p> <code>XmNmwmInputMode</code> </p>
<p> <code>XmNmwmMenu</code> </p>
<p> <code>XmNfocusMovedCallback</code> </p>
<p> <code>XmNrealizeCallback</code> </p>
<p> <code>XmNinputMethod</code> </p>
<p> <code>XmNpreeditType</code> </p>
<p> <code>XmNlightThreshold</code> </p>
<p> <code>XmNdarkThreshold</code> </p>
<p> <code>XmNforegroundThreshold</code> </p>
<h2>Class Hierarchy</h2>
<p><code><a href="/docs/linux/man/3-object/">Object</a></code>(3) <code><a href="/docs/linux/man/3-xmextobject/">XmExtObject</a></code>(3) <code><a href="/docs/linux/man/3-desktop/">Desktop</a></code>(3) <code><a href="/docs/linux/man/3-shell/">Shell</a></code>(3) <code><a href="/docs/linux/man/3-vendorshell/">VendorShell</a></code>(3)</p>
<h2>Callbacks</h2>
<h2>Convenience Functions</h2>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-vendorshell/">VendorShell</a></code>(3)</p>
