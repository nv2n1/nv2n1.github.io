---
title: "lesstif(1)"
name: "lesstif"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lesstif/"
description: "LessTif – an open-source Motif replacement"
---

<h2 class="name">NAME</h2>
<p> LessTif &#8211; an open-source Motif replacement </p>
<h2>SUMMARY</h2>
<p> <code>LessTif</code> is a free replacement for OSF/Motif&#174;. </p>
<p> As with Motif&#174;, LessTif consists of a widget set, a window manager, and a UIL implementation (libMrm and the UIL compiler). In LessTif, our main area of attention is the widget set. We also have a working window manager mwm, but UIL is not under very active development. </p>
<p> LessTif is licensed under the LGPL, the Library Gnu Public License. The license itself accompanies LessTif in the file COPYING.LIB. More information can be obtained from the Free Software Foundation. </p>
<h2>DEBUGGING</h2>
<p> For more info on Debugging check out our documentation in HTML format. </p>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt>DEBUG_SOURCES</p>
<dd> Colon-separated list of files from which debug output is generated. Special values &quot;all&quot;/&quot;none&quot; have obvious meaning. To block entries from a list, add a &quot;-&quot; prefix. You may use an asterisk &quot;*&quot; as a wildcard as well. </p>
<dt>DEBUG_FILE</p>
<dd> If this variable exists, then the file is being used for output. If &quot;%p&quot; is part of the value of DEBUG_FILE, then it is replaced by the current process id. </p>
<dt>DEBUG_PRINT_WIDGETID</p>
<dd> If this variable exists, then all widgets printed with XdbDebug() etc. will also print their widget ID. If the variable doesn&#8217;t exist, then they only print their name for identification. </p>
<dt>DEBUG_REDIRECT_XMWARNING</p>
<dd> If this variable exists any output of _XmWarning() and equivalent functions is sent to the file specified by <code>DEBUG_FILE</code> </p>
<dt>DEBUG_SIGNAL</p>
<dd> Specifies the name of the signal which should be used to switch the built-in LessTif debugging system. Valid values depend on the system on which LessTif was compiled and is running and are a subset of: </p>
<p> SIGUNUSED, SIGUSR1, SIGUSR2, SIGUSR3, SIGBREAK </p>
<dt>DEBUG_TOGGLE</p>
<dd> Specifies the initial status of the built-in LessTif debugging system. Valid values are &#8216;on&#8217; and &#8216;off&#8217; </p>
</dl>
<h2>INTERFACES</h2>
<p> The following interfaces exist to Set, Toggle and Query the current status of the debugging subsystem: </p>
<p> void <code>_LtDebugSet</code> (Boolean flag); </p>
<p> void <code>_LtDebugToggle</code> (void); </p>
<p> Boolean <code>_LtDebugQueryState</code> (void); </p>
<h2>SOURCE CODE</h2>
<p> The major part of the source code which implements the debugging system of LessTif resides in <i>/lib/Xm/DebugUtil.c</i> Using the preprocessor define <i>LESSTIF_PRODUCTION</i> the relevant code sections are en-/disabled during the build process. </p>
<p>&nbsp;<wbr></p>
<h2>SEE ALSO</h2>
<p> <code>Clients:</code></p>
<dl>
<dt>
<dd> <code><a href="/docs/linux/man/1-mwm/">mwm</a></code>(1) <code><a href="/docs/linux/man/1-uil/">uil</a></code>(1) <code><a href="/docs/linux/man/1-xmbind/">xmbind</a></code>(1)</dl>
<p> <code>Tools:</code></p>
<dl>
<dt>
<dd> <code><a href="/docs/linux/man/1-ltversion/">ltversion</a></code>(1)</dl>
<p> <code>Other Widget Sets:</code></p>
<dl>
<dt>
<dd> <code><a href="/docs/linux/man/1-xbae/">xbae</a></code>(1) <code><a href="/docs/linux/man/1-xlt/">xlt</a></code>(1)</dl>
<p> <code>Motif Widgets:</code></p>
<dl>
<dt>
<dd>
<p> <code><a href="/docs/linux/man/3-xmfileselectionbox/">XmFileSelectionBox</a></code>(3) <code><a href="/docs/linux/man/3-xmarrowbutton/">XmArrowButton</a></code>(3) <code><a href="/docs/linux/man/3-xmarrowbuttongadget/">XmArrowButtonGadget</a></code>(3) <code><a href="/docs/linux/man/3-xmbulletinboard/">XmBulletinBoard</a></code>(3) <code><a href="/docs/linux/man/3-xmcascadebutton/">XmCascadeButton</a></code>(3) <code><a href="/docs/linux/man/3-xmcascadebuttongcacheobj/">XmCascadeButtonGCacheObj</a></code>(3) <code><a href="/docs/linux/man/3-xmcascadebuttongadget/">XmCascadeButtonGadget</a></code>(3) <code><a href="/docs/linux/man/3-xmcombobox/">XmComboBox</a></code>(3) <code><a href="/docs/linux/man/3-xmcommand/">XmCommand</a></code>(3) <code><a href="/docs/linux/man/3-xmdesktop/">XmDesktop</a></code>(3) <code><a href="/docs/linux/man/3-xmdialogshell/">XmDialogShell</a></code>(3) <code><a href="/docs/linux/man/3-xmdialogshellext/">XmDialogShellExt</a></code>(3) <code><a href="/docs/linux/man/3-xmdisplay/">XmDisplay</a></code>(3) <code><a href="/docs/linux/man/3-xmdragcontext/">XmDragContext</a></code>(3) <code><a href="/docs/linux/man/3-xmdragicon/">XmDragIcon</a></code>(3) <code><a href="/docs/linux/man/3-xmdragovershell/">XmDragOverShell</a></code>(3) <code><a href="/docs/linux/man/3-xmdrawingarea/">XmDrawingArea</a></code>(3) <code><a href="/docs/linux/man/3-xmdrawnbutton/">XmDrawnButton</a></code>(3) <code><a href="/docs/linux/man/3-xmdropsitemanager/">XmDropSiteManager</a></code>(3) <code><a href="/docs/linux/man/3-xmdroptransfer/">XmDropTransfer</a></code>(3) <code><a href="/docs/linux/man/3-xmfileselectionbox/">XmFileSelectionBox</a></code>(3) <code><a href="/docs/linux/man/3-xmform/">XmForm</a></code>(3) <code><a href="/docs/linux/man/3-xmframe/">XmFrame</a></code>(3) <code><a href="/docs/linux/man/3-xmgadget/">XmGadget</a></code>(3) <code><a href="/docs/linux/man/3-xmgrabshell/">XmGrabShell</a></code>(3) <code><a href="/docs/linux/man/3-xmicongcacheobj/">XmIconGCacheObj</a></code>(3) <code><a href="/docs/linux/man/3-xmicongadget/">XmIconGadget</a></code>(3) <code><a href="/docs/linux/man/3-xmlabel/">XmLabel</a></code>(3) <code><a href="/docs/linux/man/3-xmlabelgcacheobj/">XmLabelGCacheObj</a></code>(3) <code><a href="/docs/linux/man/3-xmlabelgadget/">XmLabelGadget</a></code>(3) <code><a href="/docs/linux/man/3-xmlist/">XmList</a></code>(3) <code><a href="/docs/linux/man/3-xmmainwindow/">XmMainWindow</a></code>(3) <code><a href="/docs/linux/man/3-xmmanager/">XmManager</a></code>(3) <code><a href="/docs/linux/man/3-xmmenushell/">XmMenuShell</a></code>(3) <code><a href="/docs/linux/man/3-xmmessagebox/">XmMessageBox</a></code>(3) <code><a href="/docs/linux/man/3-xmnotebook/">XmNotebook</a></code>(3) <code><a href="/docs/linux/man/3-xmpanedwindow/">XmPanedWindow</a></code>(3) <code><a href="/docs/linux/man/3-xmprimitive/">XmPrimitive</a></code>(3) <code><a href="/docs/linux/man/3-xmprotocol/">XmProtocol</a></code>(3) <code><a href="/docs/linux/man/3-xmpushbutton/">XmPushButton</a></code>(3) <code><a href="/docs/linux/man/3-xmpushbuttongcacheobj/">XmPushButtonGCacheObj</a></code>(3) <code><a href="/docs/linux/man/3-xmpushbuttongadget/">XmPushButtonGadget</a></code>(3) <code><a href="/docs/linux/man/3-xmrowcolumn/">XmRowColumn</a></code>(3) <code><a href="/docs/linux/man/3-xmsash/">XmSash</a></code>(3) <code><a href="/docs/linux/man/3-xmscale/">XmScale</a></code>(3) <code><a href="/docs/linux/man/3-xmscreen/">XmScreen</a></code>(3) <code><a href="/docs/linux/man/3-xmscrollbar/">XmScrollBar</a></code>(3) <code><a href="/docs/linux/man/3-xmscrolledwindow/">XmScrolledWindow</a></code>(3) <code><a href="/docs/linux/man/3-xmselectionbox/">XmSelectionBox</a></code>(3) <code><a href="/docs/linux/man/3-xmseparator/">XmSeparator</a></code>(3) <code><a href="/docs/linux/man/3-xmseparatorgcacheobj/">XmSeparatorGCacheObj</a></code>(3) <code><a href="/docs/linux/man/3-xmseparatorgadget/">XmSeparatorGadget</a></code>(3) <code><a href="/docs/linux/man/3-xmspinbox/">XmSpinBox</a></code>(3) <code><a href="/docs/linux/man/3-xmtearoffbutton/">XmTearOffButton</a></code>(3) <code><a href="/docs/linux/man/3-xmtext/">XmText</a></code>(3) <code><a href="/docs/linux/man/3-xmtextfield/">XmTextField</a></code>(3) <code><a href="/docs/linux/man/3-xmtogglebutton/">XmToggleButton</a></code>(3) <code><a href="/docs/linux/man/3-xmtogglebuttongcacheobj/">XmToggleButtonGCacheObj</a></code>(3) <code><a href="/docs/linux/man/3-xmtogglebuttongadget/">XmToggleButtonGadget</a></code>(3) <code><a href="/docs/linux/man/3-xmvendorshellext/">XmVendorShellExt</a></code>(3) <code><a href="/docs/linux/man/3-xmworld/">XmWorld</a></code>(3)</dl>
<p> <code>Xt Widgets:</code></p>
<dl>
<dt>
<dd>
<p> <code><a href="/docs/linux/man/3-applicationshell/">ApplicationShell</a></code>(3) <code><a href="/docs/linux/man/3-composite/">Composite</a></code>(3) <code><a href="/docs/linux/man/3-core/">Core</a></code>(3) <code><a href="/docs/linux/man/3-object/">Object</a></code>(3) <code><a href="/docs/linux/man/3-overrideshell/">OverrideShell</a></code>(3) <code><a href="/docs/linux/man/3-shell/">Shell</a></code>(3) <code><a href="/docs/linux/man/3-toplevelshell/">TopLevelShell</a></code>(3) <code><a href="/docs/linux/man/3-transientshell/">TransientShell</a></code>(3) <code><a href="/docs/linux/man/3-wmshell/">WmShell</a></code>(3) <code><a href="/docs/linux/man/3-rect/">Rect</a></code>(3) <code><a href="/docs/linux/man/3-unnamedobj/">UnNamedObj</a></code>(3) <code><a href="/docs/linux/man/3-constraint/">Constraint</a></code>(3) <code><a href="/docs/linux/man/3-vendorshell/">VendorShell</a></code>(3)</dl>
<p> <code>File Formats:</code></p>
<dl>
<dt>
<dd>
<p> <code><a href="/docs/linux/man/5-mwmrc/">mwmrc</a></code>(5)</dl>
<p> <code>Utility Functions:</code></p>
<dl>
<dt>
<dd>
<p> <code><a href="/docs/linux/man/3-xmclipboard/">XmClipboard</a></code>(3) <code><a href="/docs/linux/man/3-lesstifinternals/">LessTifInternals</a></code>(3)</dl>
<p> <code>Internet Resources:</code></p>
<dl>
<dt>
<dd>
<p> The LessTif home page: <a rel="nofollow" href="http://www.lesstif.org">http://www.lesstif.org</a> </p>
<p> The Free Software Foundation (FSF) home page: <a rel="nofollow" href="http://www.gnu.org">http://www.gnu.org</a> </p>
<p> The OpenGroup (owners of OSF/Motif&#174; and the X Window System) home page: <a rel="nofollow" href="http://www.opengroup.org">http://www.opengroup.org</a></dl>
<h2>Index</h2>
