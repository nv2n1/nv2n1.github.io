---
title: "xmprinttofile(3)"
name: "xmprinttofile"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmprinttofile/"
description: "XmPrintToFile — Retrieves and saves data that would normally be printed by the X Print Server."
---

<p><code>XmPrintToFile</code> &#8212; Retrieves and saves data that would normally be printed by the X Print Server.</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Print.h&gt;
<code>XtEnumXmPrintToFile</code>(
<code>Display*dpy</code>,
<code>Stringfilename</code>,
<code>XPFinishProcfinish_proc</code>,
<code>XtPointerclient_data</code>);</pre>
<h2>Description</h2>
<p><code>XmPrintToFile</code> hides the details of X display connection and <code>XpGetDocumentData</code> to the Motif application programmer. </p>
<p> This function is a convenience routine that hides the details of the X and Xp internals to the application programmer by calling the <code>XpGetDocumentData</code> function with appropriate save and finish callbacks. </p>
<p> This is used in the context of X Printing when the user has specified the &quot;print-to-file&quot; option from a regular Print Setup Dialog box. </p>
<p> <code>XmPrintToFile</code> first tries to open the given filename for writing and returns <code>False</code> if it can&#8217;t. Else, it uses <code>XpGetDocumentData</code>, giving it a save proc that writes the data received in the file and a finish proc that closes the file or removes it on an unsuccessful termination. It calls <code>finish_proc</code> at that point, passing it the argument received from the Xp layer (<code>status == XPGetDocFinished</code> means the file is valid and was closed, otherwise the file was removed). </p>
<p> <code>XmPrintToFile</code> is non-blocking; if it returns successfully, it just means the file was opened successfully, not that all the data was received.</p>
<dl COMPACT>
<dt><i>dpy</i></p>
<dd>Print display connection.</p>
<dt><i>filename</i></p>
<dd>Name of the file to put the print data in.</p>
<dt><i>finish_proc</i></p>
<dd>Called when all the data has been received.</p>
<dt><i>client_data</i></p>
<dd>Passed with the <i>finish_proc</i>.</dl>
<h2>Return Value</h2>
<p>Returns <code>False</code> if the filename could not be created or opened for writing, <code>True</code> otherwise.</p>
<h2>Errors/Warnings</h2>
<p>Not applicable</p>
<h2>Examples</h2>
<p>A typical OK callback from a <code>DtPrintSetupBox</code>: </p>
<pre><tt>PrintOKCallback(widget...)
/*-------------*/
{ int save_data = XPSpool;
 pshell = XmPrintSetup (widget, pbs-&gt;print_screen,
 &quot;Print&quot;, NULL, 0);
 XtAddCallback(pshell, XmNstartJobCallback, startJobCB, data);
 if (pbs-&gt;destination == DtPRINT_TO_FILE)
 save_data = XPGetData;
 /* start job must precede XpGetDocumentData in XmPrintToFile */
 XpStartJob(XtDisplay(pshell), save_data);
 XFlush(XtDisplay(pshell)); /* maintain the sequence
 between startjob and getdocument */
 /* setup print to file */
 if (pbs-&gt;destination == DtPRINT_TO_FILE)
 XmPrintToFile(XtDisplay(pshell),
 pbs-&gt;dest_info, FinishPrintToFile, NULL);
 }
}
static void
startJobCB(Widget, XtPointer call_data, XtPointer client_data)
{
 print(p); /* rendering happens here */
 XpEndJob(XtDisplay(p-&gt;print_shell));
 /* clean up */
 XtDestroyWidget(p-&gt;print_shell);
 XtCloseDisplay(XtDisplay(p-&gt;print_shell));
}</tt></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xmprintsetup/">XmPrintSetup</a></code>(3), <code><a href="/docs/linux/man/3-xmprintshell/">XmPrintShell</a></code>(3), <code><a href="/docs/linux/man/3-xmredisplaywidget/">XmRedisplayWidget</a></code>(3), <code><a href="/docs/linux/man/3-xmprintpopuppdm/">XmPrintPopupPDM</a></code>(3)</p>
