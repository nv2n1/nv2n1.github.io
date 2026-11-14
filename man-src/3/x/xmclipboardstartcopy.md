---
title: "xmclipboardstartcopy(3)"
name: "xmclipboardstartcopy"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmclipboardstartcopy/"
description: "XmClipboardStartCopy — A clipboard function that sets up a storage and data structure"
---

<p><code>XmClipboardStartCopy</code> &#8212; A clipboard function that sets up a storage and data structure</p>
<h2>Synopsis</h2>
<pre>#include &lt;Xm/CutPaste.h&gt;
int XmClipboardStartCopy (<i>display, window, clip_label,
 timestamp, widget, callback, item_id</i>)
 Display <i>* display</i>;
 Window <i>window</i>;
 XmString <i>clip_label</i>;
 Time <i>timestamp</i>;
 Widget <i>widget</i>;
 XmCutPasteProc <i>callback</i>;
 long <i>* item_id</i>;
(<code>void</code>)</pre>
<h2>Description</h2>
<p><code>XmClipboardStartCopy</code> sets up storage and data structures to receive clipboard data. An application calls this function during a cut or copy operation. The data item that these structures receive then becomes the next data item in the clipboard. </p>
<p> Copying a large piece of data to the clipboard can take a long time. It is possible that, once the data is copied, no application will ever request that data. The Motif Toolkit provides a mechanism so that an application does not need to actually pass data to the clipboard until the data has been requested by some application. </p>
<p> Instead, the application passes format and length information in <code>XmClipboardCopy</code> to the clipboard functions, along with a widget ID and a callback function address that is passed in <code>XmClipboardStartCopy</code>. The widget ID is necessary for communications between the clipboard functions in the application that owns the data and the clipboard functions in the application that requests the data. </p>
<p> The callback functions are responsible for copying the actual data to the clipboard through <code>XmClipboardCopyByName</code>. The callback function is also called if the data item is removed from the clipboard and the actual data is no longer needed.</p>
<dl COMPACT>
<dt><i>display</i></p>
<dd>Specifies a pointer to the <code>Display</code> structure that was returned in a previous call to <code>XOpenDisplay</code> or <code>XtDisplay</code>.</p>
<dt><i>window</i></p>
<dd>Specifies the window ID of a widget that relates the application window to the clipboard. The widget&#8217;s window ID can be obtained through <code>XtWindow</code>. The same application instance should pass the same window ID to each of the clipboard functions that it calls.</p>
<dt><i>clip_label</i></p>
<dd>Specifies the label to be associated with the data item. This argument is used to identify the data item, as in a clipboard viewer. An example of a label is the name of the application that places the data in the clipboard.</p>
<dt><i>timestamp</i></p>
<dd>Specifies the time of the event that triggered the copy. A valid timestamp must be supplied; it is not sufficient to use <code>CurrentTime</code>.</p>
<dt><i>widget</i></p>
<dd>Specifies the ID of the widget that receives messages requesting data previously passed by name. This argument must be present in order to pass data by name. Any valid widget ID in your application can be used for this purpose and all the message handling is taken care of by the cut and paste functions.</p>
<dt><i>callback</i></p>
<dd>Specifies the address of the callback function that is called when the clipboard needs data that was originally passed by name. This is also the callback to receive the <i>delete</i> message for items that were originally passed by name. This argument must be present in order to pass data by name.</p>
<dt><i>item_id</i></p>
<dd>Specifies the number assigned to this data item. The application uses this number in calls to <code>XmClipboardCopy</code>, <code>XmClipboardEndCopy</code>, and <code>XmClipboardCancelCopy</code>.</dl>
<p> For more information on passing data by name, see <code><a href="/docs/linux/man/3-xmclipboardcopy/">XmClipboardCopy</a></code>(3) and <code><a href="/docs/linux/man/3-xmclipboardcopybyname/">XmClipboardCopyByName</a></code>(3). </p>
<p> The <i>widget</i> and <i>callback</i> arguments must be present in order to pass data by name. The callback format is as follows: </p>
<pre>void (*<i>callback)</i> (<i>widget, data_id, private, reason</i>)
 Widget <i>widget</i>;
 long *<i>data_id</i>;
 long *<i>private</i>;
 int *<i>reason</i>;
(<code>void</code>)</pre>
<dl COMPACT>
<dt><i>widget</i></p>
<dd>Specifies the ID of the widget passed to this function.</p>
<dt><i>data_id</i></p>
<dd>Specifies the identifying number returned by <code>XmClipboardCopy</code>, which identifies the pass-by-name data.</p>
<dt><i>private</i></p>
<dd>Specifies the private information passed to <code>XmClipboardCopy</code>.</p>
<dt><i>reason</i></p>
<dd>Specifies the reason. <code>XmCR_CLIPBOARD_DATA_DELETE</code> or <code>XmCR_CLIPBOARD_DATA_REQUEST</code> are the possible values.</dl>
<h2>Return</h2>
<dl COMPACT>
<dt><code>XmClipboardSuccess</code></p>
<dd>The function was successful.</p>
<dt><code>XmClipboardLocked</code></p>
<dd>The function failed because the clipboard was locked by another application. The application can continue to call the function again with the same parameters until the lock goes away. This gives the application the opportunity to ask if the user wants to keep trying or to give up on the operation.</dl>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/3-xmclipboardcancelcopy/">XmClipboardCancelCopy</a></code>(3), <code><a href="/docs/linux/man/3-xmclipboardcopy/">XmClipboardCopy</a></code>(3), <code><a href="/docs/linux/man/3-xmclipboardcopybyname/">XmClipboardCopyByName</a></code>(3), <code><a href="/docs/linux/man/3-xmclipboardendcopy/">XmClipboardEndCopy</a></code>(3), <code><a href="/docs/linux/man/3-xmclipboardendretrieve/">XmClipboardEndRetrieve</a></code>(3), <code><a href="/docs/linux/man/3-xmclipboardinquirecount/">XmClipboardInquireCount</a></code>(3), <code><a href="/docs/linux/man/3-xmclipboardinquireformat/">XmClipboardInquireFormat</a></code>(3), <code><a href="/docs/linux/man/3-xmclipboardinquirelength/">XmClipboardInquireLength</a></code>(3), <code><a href="/docs/linux/man/3-xmclipboardinquirependingitems/">XmClipboardInquirePendingItems</a></code>(3), <code><a href="/docs/linux/man/3-xmclipboardlock/">XmClipboardLock</a></code>(3), <code><a href="/docs/linux/man/3-xmclipboardregisterformat/">XmClipboardRegisterFormat</a></code>(3), <code><a href="/docs/linux/man/3-xmclipboardretrieve/">XmClipboardRetrieve</a></code>(3), <code><a href="/docs/linux/man/3-xmclipboardstartretrieve/">XmClipboardStartRetrieve</a></code>(3), <code><a href="/docs/linux/man/3-xmclipboardundocopy/">XmClipboardUndoCopy</a></code>(3), <code><a href="/docs/linux/man/3-xmclipboardunlock/">XmClipboardUnlock</a></code>(3), and <code><a href="/docs/linux/man/3-xmclipboardwithdrawformat/">XmClipboardWithdrawFormat</a></code>(3).</p>
