---
title: "xmprintshell(3)"
name: "xmprintshell"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmprintshell/"
description: "XmPrintShell — a shell widget class used for printing in Motif"
---

<p><code>XmPrintShell</code> &#8212; a shell widget class used for printing in Motif</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Print.h&gt;
<code>Boolean XmIsPrintShell</code>(
<code>Widget</code>);</pre>
<h2>Description</h2>
<p>The <code>XmPrintShell</code> provides the Motif application programmer with an Xt widget oriented API to some of the X Print resources and a callback to drive the pagination. </p>
<p> The <code>XmPrintShell</code> provides a simple callback to handle the pagination logic, and a set of resources to get and set common printer attributes. </p>
<p> If not created on an <code>XPrint</code> connection, <code>XmPrintShell</code> behaves as a regular applicationShell. </p>
<p> The <code>XmPrintShell</code> also initializes the <code>Xp</code> extension event handling mechanism, by registering an extension selector that calls <code>XpSelectInput</code> and event dispatcher for print and attributes <code>Xp</code> events, so applications can use <code>XtInsertEventTypeHandler</code> to register their own handler with the <code>Xp</code> events.</p>
<h3>Arguments</h3>
<p>No <code>XmCreate</code> function is provided, since this is a toplevel shell, most likely created thru some <code>Xt</code> shell creation routine or <code>XmPrintSetup</code>.</p>
<h3>Classes</h3>
<p><code>XmPrintShell</code> is a subclass of <code>ApplicationShell</code>; it inherits behavior, resources and traits from all its superclasses. The class pointer is <code>XmPrintShellWidgetClass</code>.</p>
<h3>New Resources</h3>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=5><code>XmPrintShell Resource Set</code>
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
<td><code>XmNstartJobCallback</code></td>
<td><code>XmCCallback</code></td>
<td><code>XtCallbackList</code></td>
<td><code>NULL</code></td>
<td><code>CSG</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>XmNendJobCallback</code></td>
<td><code>XmCCallback</code></td>
<td><code>XtCallbackList</code></td>
<td><code>NULL</code></td>
<td><code>CSG</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>XmNpageSetupCallback</code></td>
<td><code>XmCCallback</code></td>
<td><code>XtCallbackList</code></td>
<td><code>NULL</code></td>
<td><code>CSG</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>XmNminX</code></td>
<td><code>XmCMinX</code></td>
<td><code>Dimension</code></td>
<td><code>dynamic</code></td>
<td><code>G</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>XmNminY</code></td>
<td><code>XmCMinY</code></td>
<td><code>Dimension</code></td>
<td><code>dynamic</code></td>
<td><code>G</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>XmNmaxX</code></td>
<td><code>XmCMaxX</code></td>
<td><code>Dimension</code></td>
<td><code>dynamic</code></td>
<td><code>G</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>XmNmaxY</code></td>
<td><code>XmCMaxY</code></td>
<td><code>Dimension</code></td>
<td><code>dynamic</code></td>
<td><code>G</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>XmNdefaultPixmapResolution</code></td>
<td><code>XmCDefaultPixmapResolution</code></td>
<td><code>unsigned short</code></td>
<td><code>100</code></td>
<td><code>CSG</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>XmNpdmNotificationCallback</code></td>
<td><code>XmCCallback</code></td>
<td><code>XtCallbackList</code></td>
<td><code>NULL</code></td>
<td><code>CSG</code>
</td>
</tr>
</table>
<dl COMPACT>
<dt><i>XmNstartJobCallback</i></p>
<dd>Specifies the callback driving the beginning of rendering. It is safe for an application to start rendering after this callback has been activated. <code>XpStartJob</code> must be called to trigger this callback.</p>
<dt><i>XmNendJobCallback</i></p>
<dd>Specifies the callback driving the end of rendering. Notify the client that all rendering has been processed (whether on print-to-file or regular spool). <code>XpEndJob</code> is called by the print shell to trigger this callback.</p>
<dt><i>XmNpageSetupCallback</i></p>
<dd>Specifies the callback driving the page layout. It is safe for an app to start rendering from this callback even if the <code>XmNstartJobCallback</code> is not used.</p>
<dt><i>XmNminX, XmNminY, XmNmaxX, XmNmaxY</i></p>
<dd>Specify the imageable area of the page in the current print context. <code>XmPrintShell</code> also maintains a proper size at all times by updating its own widget dimension whenever an attribute, such as resolution or orientation, changes. It is sized in its <code>Initialize</code> routine so that the application can rely on a proper size before the first <code>StartPage</code> call is issued.</p>
<dt><i>XmNdefaultPixmapResolution</i></p>
<dd>Indicates the resolution in dpi (dot per inch) of the image files read and converted by Motif for the widget descendants of this shell. It is used to determine a scaling ratio to be applied to pixmap created thru regular pixmap/icon conversion of the following Widget resources:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt> &bull;</p>
<dd><code>XmLabel</code>.label*Pixmap, <code>XmIconG</code>.*IconPixmap <code>XmToggleB</code>.selectPixmap, <code>XmPushBG</code>.armPixmap, <code>XmIconG</code>.*IconMask, <code>XmMessageBox</code>.symbolPixmap, <code>XmContainer</code>.*StatePixmap, &#8230;</p>
<dt> &bull;</p>
<dd>Leaving out the pixmap resources being used for tiling (XmNhighlightPixmap, XmNtopShadowPixmap, XmNbottomShadowPixmap, XmNbackgroundPixmap, &#8230;)</dl>
</dl>
<dt><i>XmNpdmNotificationCallback</i></p>
<dd>A callback notifying the application about the status of the PDM (see XmPrintPopupPDM). A XmPrintShellCallbackStruct is used, with reason:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt> &bull;</p>
<dd><code>XmCR_PDM_NONE</code>: no PDM available on this display for the named selection (provided in detail)</p>
<dt> &bull;</p>
<dd><code>XmCR_PDM_START_VXAUTH</code> : the PDM is not authorized to connect to the video display.</p>
<dt> &bull;</p>
<dd><code>XmCR_PDM_START_PXAUTH</code> : the PDM is not authorized to connect to the print display.</p>
<dt> &bull;</p>
<dd><code>XmCR_PDM_UP</code> : the PDM is up and running</p>
<dt> &bull;</p>
<dd><code>XmCR_PDM_OK</code> : the PDM has exited with OK status</p>
<dt> &bull;</p>
<dd><code>XmCR_PDM_CANCEL</code> : the PDM has exited with CANCEL</p>
<dt> &bull;</p>
<dd><code>XmCR_PDM_START_ERROR</code> : the PDM cannot start due to some error (usually logged)</p>
<dt> &bull;</p>
<dd><code>XmCR_PDM_EXIT_ERROR</code> : the PDM has exited with an error</dl>
</dl>
</dl>
<h3>Callback Information</h3>
<p>The <code>XmNstartJobCallback</code>, <code>XmNendJobCallback,</code> <code>XmNpageSetupCallback</code> and <code>XmNpdmNotificationCallback</code> operate on a <code>XmPrintShellCallbackStruct</code>, which is defined as follow: </p>
<pre><tt>typedef struct
{
 int reason; /* XmCR_START_JOB, XmCR_END_JOB,
 XmCR_PAGE_SETUP, XmCR_PDM_* */
 XEvent *event;
 XPContext print_context;
 Boolean last_page; /* in_out */
 XtPointer detail;
} XmPrintShellCallbackStruct;</tt></pre>
<h3>Additional Behavior</h3>
<p>The <code>last_page</code> field is only meaningful when the reason is <code>XmCR_PAGE_SETUP</code>. </p>
<p> The page setup callback is called with <code>last_page</code> <code>False</code> to notify the application that it has to get its internal layout state ready for the next page. Typically, a widget based application will change the content of a <code>Label</code> showing the page number, or scroll the content of the <code>Text</code> widget. </p>
<p> When the application has processed its last page, it should set the <code>last_page</code> field in the callback struct to <code>True</code>. The callback will be called a last time after that with <code>last_page</code> <code>False</code> to notify the application that it can safely clean-up its internal state (e.g., destroy widgets). </p>
<p> No drawing should occur from within the callback function in the application, this is an Exposure event-driven programming model where widgets render themselves from their expose methods. </p>
<p> The print shell calls <code>XpStartPage</code> after the <code>pageSetupCallback</code> returns, and <code>XpEndPage</code> upon reception of <code>StartPageNotify</code>.</p>
<h2>Errors/Warnings</h2>
<p><code>XmPrintShell</code> can generate the following warnings:</p>
<dl COMPACT>
<dt> &bull;</p>
<dd><code>Not connected to a valid X Print Server: behavior undefined.</code></p>
<dt> &bull;</p>
<dd><code>Attempt to set an invalid resolution on a printer: %s</code></p>
<dt> &bull;</p>
<dd><code>Attempt to set an invalid orientation on a printer: %s</code></dl>
<h2>Return Value</h2>
<p>Not applicable</p>
<h2>Examples</h2>
<pre><tt>PrintOnePageCB(Widget pshell, XtPointer npages,
/*----------*/ XmPrintSetPageCBStruct psp)
{
 static int cur_page = 0;
 cur_page++;
 if (! psp-&gt;last_page
 &amp;&amp; curPage &gt; 1) /* no need to scroll for the first page */
 {
 XmTextScroll(ptext, prows); /* get ready for next page */
 } else { /**** I'm done */
 XtDestroyWidget(pshell);
 XtCloseDisplay(XtDisplay(pshell));
 }
 if (cur_page == (int) n_pages) psp-&gt;last_page = True;
}
PrintOKCallback(...)
/*-------------*/
{
 pshell = XmPrintSetup (widget, pbs-&gt;print_screen,
 &quot;Print&quot;, NULL, 0);
 XpStartJob(XtDisplay(pshell), XPSpool);
 /**** here I get the size of the shell, create my widget
 hierarchy: a bulleting board, and then a text widget,
 that I stuff with the video text widget buffer */
 /* get the total number of pages to print */
 /* same code as previous example to get n_pages */
 /**** set up my print callback */
 XtAddCallback(pshell, XmNpageSetUpCallback,
 PrintOnePageCB, n_pages);
}</tt></pre>
<p>Examples of <code>XmNdefaultPixmapResolution</code> usage:</p>
<dl COMPACT>
<dt> &bull;</p>
<dd>An application reuses the same image sources it uses for the video interface, in XBM, XPM, PNG ot JPEG, to layout on its printed pages. In this case, scaling is seamless.</dl>
<pre><tt> ! icon.xpm is 30x30 pixels
 app*dialog.pushb.labelPixmap:icon.xpm
 ! print is 400dpi
 app.print*form.lab.labelPixmap:icon.xpm
 ! 120x120 pixels on the paper (auto scaling)</tt></pre>
<dl COMPACT>
<dt> &bull;</p>
<dd>An application provides a new set of image files, for a given printer resolution (say 300). It doesn&#8217;t want automatic scaling by the toolkit for that resolution, it wants scaling based on these 300dpi images for higher resolution. It creates its print shell inside using the name &quot;printHiRes&quot; and adds the following in its resource file:</dl>
<pre><tt> app.printHiRes.defaultPixmapResolution:300
 ! icon300.xpm is 120x120 pixels
 app.printHiRes*form.lab.labelPixmap:icon300.xpm
 ! 120x120 pixels on the paper (no scaling)</tt></pre>
<p>This way a printer resolution of 600 will result in a scale of a 300 dpi image by 2 (dpi=600 divided by base=300), while a printer resolution of 150 (using default print shell name &quot;print&quot;) will use the 100 dpi icon scaled by 1.5 (dpi=150 divided by default base=100).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xmprintsetup/">XmPrintSetup</a></code>(3), <code><a href="/docs/linux/man/3-xmredisplaywidget/">XmRedisplayWidget</a></code>(3), <code><a href="/docs/linux/man/3-xmprinttofile/">XmPrintToFile</a></code>(3), <code><a href="/docs/linux/man/3-xmprintpopuppdm/">XmPrintPopupPDM</a></code>(3)</p>
