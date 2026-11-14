---
title: "xmprintpopuppdm(3)"
name: "xmprintpopuppdm"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmprintpopuppdm/"
description: "XmPrintPopupPDM — Send a notification for the PDM to be popped up"
---

<p><code>XmPrintPopupPDM</code> &#8212; Send a notification for the PDM to be popped up</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/Print.h&gt;
<code>XtEnum XmPrintPopupPDM</code>(
<code>Widgetprint_shell</code>,
<code>Widgetvideo_transient_for</code>);</pre>
<h2>Description</h2>
<p>A convenience function that sends a notification to start a Print Dialog Manager on behalf of the application, <code>XmPrintPopupPDM</code> hides the details of the X selection mechanism used to notify the PDM that a new dialog must be popped up for this application. </p>
<p> <code>XmPrintPopupPDM</code> sends a selection request to either the print display of the print shell, or the video display of the transient_for video widget (depending on the environment variable <code>XPDMDISPLAY</code>, which can only takes the value &quot;print&quot; or &quot;video&quot;), asking for the PDM windows to be popped up on behalf of the app. </p>
<p> Return right away with status of <code>XmPDM_NOTIFY_FAIL</code> (e.g. if the function couldn&#8217;t malloc memory for the selection value, or if <code>XPDMDISPLAY</code> is not &quot;print&quot; or &quot;video&quot;) or with <code>XmPDM_NOTIFY_SUCCESS</code> , which only means a &quot;message&quot; was sent out to the PDM specified by <code>XPDMSELECTION</code> , not that it&#8217;s already up on the screen yet. </p>
<p> In order to know if the PDM is up, or not running, the application must register a <code>XmNpdmNotificationCallback</code> with the Print Shell. </p>
<p> <code>XmPrintPopupPDM</code> puts up an <code>InputOnly</code> window on top of the dialog, so that the end user doesn&#8217;t use the print setup dialog while the PDM is trying to come up. This window is automatically removed when the shell is about to call the callback for the first time.</p>
<dl COMPACT>
<dt><i>print_shell</i></p>
<dd>The Print Shell used for this print job and context.</p>
<dt><i>video_transient_for</i></p>
<dd>The video widget dealing with application print setup.</dl>
<h2>Return Value</h2>
<p>Returns <code>XmPDM_NOTIFY_SUCCESS</code> if the function was able to send the notification out to the PDM process, <code>XmPDM_NOTIFY_FAIL</code> otherwise.</p>
<h2>Errors/Warnings</h2>
<p>Not applicable.</p>
<h2>Examples</h2>
<p>Example of callback from a Print set up dialog box &quot;Setup&#8230;&quot; button: </p>
<pre><tt>PrintSetupCallback(print_dialog...)
/*-------------*/
{
 if (XmPrintPopupPDM (pshell, XtParent(print_dialog)) !=
 XmPDM_NOTIFY_SUCCESS) {
 /* some error dialog */
 }
}</tt></pre>
<p>Example of <code>XmNpdmNotificationCallback</code> from a Print Shell: </p>
<pre><tt>pdmNotifyCB(print_shell...)
{
 XmPrintShellCallBackStruct * pr_cb = ...
 switch (pr_cb-&gt;reason) {
 case XmCR_PDM_NONE:
 /* no PDM available */
 PostErrorDialog(...);
 break;
 case XmCR_PDM_VXAUTH:
 /* PDM is not authorized ... */
 PostErrorDialog(...);
 break;
 case XmCR_PDM_UP: the PDM is up and running
 /* everything is fine */
 break;
 default: /* other cases */
 }
}</tt></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xmprintsetup/">XmPrintSetup</a></code>(3), <code><a href="/docs/linux/man/3-xmprintshell/">XmPrintShell</a></code>(3), <code><a href="/docs/linux/man/3-xmredisplaywidget/">XmRedisplayWidget</a></code>(3), <code><a href="/docs/linux/man/3-xmprinttofile/">XmPrintToFile</a></code>(3)</p>
