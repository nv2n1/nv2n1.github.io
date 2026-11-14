---
title: "xmclipboard(3)"
name: "xmclipboard"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xmclipboard/"
description: "XmClipboard – Motif-compatible clipboard widget"
---

<p>XmClipboard &#8211; Motif-compatible clipboard widget</p>
<h2>Synopsis</h2>
<p><code>#include &lt;<a href="file:/usr/include/Xm/CutPaste.h">Xm/CutPaste.h</a>&gt;</code></p>
<h2>Description</h2>
<p>The clipboard is represented by a number of convenience functions which allow a widget or an application to exchange information with other widgets or applications. </p>
<p> The APIs described in this document are to be used by application writers, but the LessTif widgets use them internally as well when the user performs an action commanding the widget to interact with the clipboard. </p>
<p> Examples of the use of these functions can be found in the implementation of the <code><a href="/docs/linux/man/3-xmtextfield/">XmTextField</a></code>(3) widget, in <i>lib/Xm/TextF.c</i> under the root of the LessTif source directory. Specifically, the functions XmTextFieldCopy and XmTextFieldPaste have been implemented using the functions described below.</p>
<h2>Convenience Functions</h2>
<p>The functions are listed alphabetically below. Do note however that XmClipboardStartCopy is to be called before any of the other functions described in this document. </p>
<p> <code>int XmClipboardBeginCopy(Display *display, Window window, XmString clip_label, Widget widget, VoidProc callback, long *item_id)</code> </p>
<p> This appears to be the same as XmClipboardStartCopy. This function should be called first, then XmClipboardCopy may be called, potentially multiple times; the sequence must be ended with a call of XmClipboardEndCopy. </p>
<p> <code>int XmClipboardCancelCopy(Display *display, Window window, long item_id)</code> </p>
<p> Just what the name says : cancel a pending copy operation. </p>
<p> <code>int XmClipboardCopy(Display *display, Window window, long item_id, char *format_name, XtPointer buffer, unsigned long length, long private_id, long *data_id)</code> </p>
<p> This function allows you to try to copy the buffer that needs to be transferred to the clipboard. Item_id should be the same as in the call to XmClipboardBeginCopy. Private_id is a number that you can pass. </p>
<p> <code>int XmClipboardCopyByName(Display *display, Window window, long data_id, XtPointer buffer, unsigned long length, long private_id)</code> </p>
<p> <code>int XmClipboardEndCopy(Display *display, Window window, long item_id)</code> </p>
<p> See description of XmClipboardBeginCopy and XmClipboardCopy. </p>
<p> <code>int XmClipboardEndRetrieve(Display *display, Window window)</code> </p>
<p> Ends a cycle of retrieval calls, started with a call to XmClipboardBeginRetrieve, and with calls of XmClipboardRetrieve in the middle. </p>
<p> <code>int XmClipboardInquireCount(Display *display, Window window, int *count, unsigned long *max_length)</code> </p>
<p> <code>int XmClipboardInquireFormat(Display *display, Window window, int index, XtPointer format_name_buf, unsigned long buffer_len, unsigned long *copied_len)</code> </p>
<p> <code>int XmClipboardInquireLength(Display *display, Window window, char *format_name, unsigned long *length)</code> </p>
<p> You can call this function just beforeXmClipboardRetrieve to figure out how much data is waiting. This way you can allocate storage dynamically. An example of the use of this function is in the LessTif sources in the file lib/Xm/TextF.c, in function XmTextFieldPaste. </p>
<p> <code>int XmClipboardInquirePendingItems(Display *display, Window window, char *format_name, XmClipboardPendingList *item_list, unsigned long *count)</code> </p>
<p> <code>int XmClipboardLock(Display *display, Window window)</code> </p>
<p> <code>int XmClipboardRegisterFormat(Display *display, char *format_name, int format_length)</code> </p>
<p> <code>int XmClipboardRetrieve(Display *display, Window window, char *format_name, XtPointer buffer, unsigned long length, unsigned long *num_bytes, long *private_id)</code> </p>
<p> Copy a chunk of the clipboard&#8217;s data into application memory. Length indicates the buffer&#8217;s size. Private_id returns private data associated with the data item (this is just a number). </p>
<p> This function can return <code>ClipboardLocked</code>. </p>
<p> <code>int XmClipboardStartCopy(Display *display, Window window, XmString clip_label, Time timestamp, Widget widget, XmCutPasteProc callback, long *item_id)</code> </p>
<p> This function creates temporary storage that will receive clipboard data. It must be called before any other XmClipboard operation. Window identifies the widget&#8217;s window; it should be passed to all clipboard routines in the same application. Clip_label identifies the data item by name. Widget is the widget ID receiving callbacks mentioned in callback. Item_id returns a number to be used by the other clipboard copy functions to refer to this particular object. </p>
<p> This function can return <code>ClipboardLocked</code>. </p>
<p> <code>int XmClipboardStartRetrieve(Display *display, Window window, Time timestamp)</code> </p>
<p> This function indicates the start of incremental retrieval of data from the clipboard. Increments can be copied now with XmClipboardRetrieve, while XmClipboardEndRetrieve should be called to finish copying the contents of the clipboard. These functions should be called with identical format_name arguments. </p>
<p> This function can return <code>ClipboardLocked</code>. </p>
<p> <code>int XmClipboardUndoCopy(Display *display, Window window)</code> </p>
<p> <code>int XmClipboardUnlock(Display *display, Window window, Boolean remove_all_locks)</code> </p>
<p> <code>int XmClipboardWithdrawFormat(Display *display, Window window, int data_id)</code></p>
<h2>Callbacks</h2>
<p>The callback functions triggered by XmClipboardStartCopy should have the following signature : </p>
<p> <code>void CallbackFunction(Widget w, int *data_id, int *private, int *reason)</code> </p>
<p> The data_id points to the data passed by name. The private pointer points to data passed from XmClipboardCopy. The reason field can either return XmCR_CLIPBOARD_DATA_DELETE or XmCR_CLIPBOARD_DATA_REQUEST.</p>
<h2>Return Values</h2>
<p>All of the functions described in this page can return the following codes : </p>
<p> <code>ClipboardSuccess</code> the call ended successfully </p>
<p> <code>ClipboardFail</code> failure for various reasons &#8211; see the explanation with the function </p>
<p> <code>ClipboardLocked</code> some other application has locked the clipboard already </p>
<p> <code>ClipboardNoData</code> it&#8217;s empty or the format wasn&#8217;t found </p>
<p> <code>ClipboardTruncate</code> the data was truncated because the buffer was too small </p>
<p> <code>ClipboardBadFormat</code> the format name was NULL or the format didn&#8217;t have length 8, 16, or 32</p>
<h2>See Also</h2>
