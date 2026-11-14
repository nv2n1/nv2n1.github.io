---
title: "xmredisplaywidget(3)"
name: "xmredisplaywidget"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmredisplaywidget/"
description: "XmRedisplayWidget — Synchronously activates the expose method of a widget to draw its content"
---

<p><code>XmRedisplayWidget</code> &#8212; Synchronously activates the <code>expose</code> method of a widget to draw its content</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Xm.h&gt;
<code>voidXmRedisplayWidget</code>(
<code>Widgetwidget</code>);</pre>
<h2>Description</h2>
<p>This function is a convenience routine that hides the details of the Xt internals to the application programmer by calling the <code>expose</code> method of the given widget with a well formed <code>Expose</code> event and <code>Region</code> corresponding to the total area of the widget. If the widget doesn&#8217;t have an <code>Expose</code> method, the function does nothing. </p>
<p> This is primarily used in the context of X Printing if the programming model chosen by the application is <i>synchronous</i>; that is, it doesn&#8217;t rely of X Print events for the driving of page layout but wants to completely control the sequence of rendering requests. </p>
<p> <code>XmRedisplayWidget</code> doesn&#8217;t clear the widget window prior to calling the <code>expose</code> method, since this is handled by calls to <code>XpStartPage</code> .</p>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>The widget to redisplay.</dl>
<h2>Return Value</h2>
<p>None.</p>
<h2>Errors/Warnings</h2>
<p>Not applicable</p>
<h2>Examples</h2>
<p>In the following, a simple application wants to print the content of a multi-page text widget (similar to <code>dtpad</code>). </p>
<pre><tt>PrintOKCallback(print_dialog...)
/*-------------*/
{
 pshell = XmPrintSetup (print_dialog, pbs-&gt;print_screen,
 &quot;Print&quot;, NULL, 0);
 XpStartJob(XtDisplay(pshell), XPSpool);
 /**** here I realize the shell, get its size, create my widget
 hierarchy: a bulletin board, and then a text widget,
 that I stuff with the video text widget buffer */
 /* get the total number of pages to print */
 XtVaGetValues(ptext, XmNrows, &amp;prows,
 XmNtotalLines, n_lines, NULL);
 n_pages = n_lines / prows;
 /***** now print the pages in a loop */
 for (cur_page=0; cur_page != n_pages; cur_page++) {
 XpStartPage(XtDisplay(pshell), XtWindow(pshell), False);
 XmRedisplayWidget(ptext); /* do the drawing */
 XpEndPage(XtDisplay(pshell));
 XmTextScroll(ptext, prows); /* get ready for next page */
 }
 /***** I'm done */
 XpEndJob(XtDisplay(pshell));
}</tt></pre>
<p>Of course, one could change the above code to include it in a <code>fork()</code> branch so that the main program is not blocked while printing is going on. Another way to achieve a &quot;print-in-the-background&quot; effect is to use an Xt workproc. Using the same sample application, that gives us: </p>
<pre><tt>Boolean
PrintOnePageWP(XtPointer npages) /* workproc */
/*-------------*/
{
 static int cur_page = 0;
 cur_page++;
 XpStartPage(XtDisplay(pshell), XtWindow(pshell), False);
 XmRedisplayWidget(ptext); /* do the drawing */
 XpEndPage(XtDisplay(pshell));
 XmTextScroll(ptext, prows); /* get ready for next page */
 if (cur_page == n_pages) { /***** I'm done */
 XpEndJob(XtDisplay(pshell));
 XtDestroyWidget(pshell);
 XtCloseDisplay(XtDisplay(pshell));
 }
 return (cur_page == n_pages);
}
PrintOKCallback(...)
/*-------------*/
{
 pshell = XmPrintSetup (widget, pbs-&gt;print_screen,
 &quot;Print&quot;, NULL, 0);
 XpStartJob(XtDisplay(pshell), XPSpool);
 /**** here I get the size of the shell, create my widget
 hierarchy: a bulletin board, and then a text widget,
 that I stuff with the video text widget buffer */
 /* get the total number of pages to print */
 /* ... same code as above example */
 /***** print the pages in the background */
 XtAppAddWorkProc(app_context, PrintOnePageWP, n_pages);
}</tt></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xmprintsetup/">XmPrintSetup</a></code>(3), <code><a href="/docs/linux/man/3-xmprintshell/">XmPrintShell</a></code>(3)</p>
