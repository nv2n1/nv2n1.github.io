---
title: "cdk(3)"
name: "cdk"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cdk/"
description: "cdk – Curses Development Kit"
---

<h2>NAME</h2>
<p> cdk &#8211; <code>Curses Development Kit</code></p>
<h2>SYNOPSIS</h2>
<p> <code>cc</code> [ <i>flag</i> &#8230; ] <i>file</i> &#8230; <code>-lcdk</code> [ <i>library</i> &#8230; ] </p>
<p> #include &lt;cdk.h&gt; </p>
<p> Cdk provides functions to use a large number of predefined curses widgets. To use the Cdk widgets the header file <i>cdk.h</i> must be included in the source. </p>
<p> The widgets available from Cdk are listed below. </p>
<p> <center></p>
<table>
<tr VALIGN=top>
<td><code>Widget Type</code></td>
<td>Manual Page Name
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>Alphalist</td>
<td>cdk_alphalist (3)
</td>
</tr>
<tr VALIGN=top>
<td>Button</td>
<td>cdk_button (3)
</td>
</tr>
<tr VALIGN=top>
<td>Buttonbox</td>
<td>cdk_buttonbox (3)
</td>
</tr>
<tr VALIGN=top>
<td>Calendar</td>
<td>cdk_calendar (3)
</td>
</tr>
<tr VALIGN=top>
<td>Dialog</td>
<td>cdk_dialog (3)
</td>
</tr>
<tr VALIGN=top>
<td>DoubleFloat Scale</td>
<td>cdk_dscale (3)
</td>
</tr>
<tr VALIGN=top>
<td>Entry Field</td>
<td>cdk_entry (3)
</td>
</tr>
<tr VALIGN=top>
<td>File Selector</td>
<td>cdk_fselect (3)
</td>
</tr>
<tr VALIGN=top>
<td>File Viewer</td>
<td>cdk_viewer (3)
</td>
</tr>
<tr VALIGN=top>
<td>Floating Scale</td>
<td>cdk_fscale (3)
</td>
</tr>
<tr VALIGN=top>
<td>Floating Slider</td>
<td>cdk_fslider (3)
</td>
</tr>
<tr VALIGN=top>
<td>Graph</td>
<td>cdk_graph (3)
</td>
</tr>
<tr VALIGN=top>
<td>Histogram</td>
<td>cdk_histogram (3)
</td>
</tr>
<tr VALIGN=top>
<td>Integer Scale</td>
<td>cdk_scale (3)
</td>
</tr>
<tr VALIGN=top>
<td>Integer Slider</td>
<td>cdk_slider (3)
</td>
</tr>
<tr VALIGN=top>
<td>Item List</td>
<td>cdk_itemlist (3)
</td>
</tr>
<tr VALIGN=top>
<td>Label</td>
<td>cdk_label (3)
</td>
</tr>
<tr VALIGN=top>
<td>Marquee</td>
<td>cdk_marquee (3)
</td>
</tr>
<tr VALIGN=top>
<td>Matrix</td>
<td>cdk_matrix (3)
</td>
</tr>
<tr VALIGN=top>
<td>Multiple Line Entry Field</td>
<td>cdk_mentry (3)
</td>
</tr>
<tr VALIGN=top>
<td>Pulldown Menu</td>
<td>cdk_menu (3)
</td>
</tr>
<tr VALIGN=top>
<td>Radio List</td>
<td>cdk_radio (3)
</td>
</tr>
<tr VALIGN=top>
<td>Scrolling List</td>
<td>cdk_scroll (3)
</td>
</tr>
<tr VALIGN=top>
<td>Scrolling Selection List</td>
<td>cdk_selection (3)
</td>
</tr>
<tr VALIGN=top>
<td>Scrolling Window</td>
<td>cdk_swindow (3)
</td>
</tr>
<tr VALIGN=top>
<td>Template</td>
<td>cdk_template (3)
</td>
</tr>
<tr VALIGN=top>
<td>Unsigned Scale</td>
<td>cdk_uscale (3)
</td>
</tr>
<tr VALIGN=top>
<td>Unsigned Slider</td>
<td>cdk_uslider (3)
</td>
</tr>
</table>
<p></center> </p>
<p> The rest of the manual pages describe supporting functions: </p>
<p> <center></p>
<table>
<tr VALIGN=top>
<td><code>Manual Page Name</code></td>
<td>Description
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>cdk_binding (3)</td>
<td> Outlines how to create user definable key bindings.
</td>
</tr>
<tr VALIGN=top>
<td>cdk_display (3)</td>
<td> Shows how to add special display attributes, colors, and justification into a widget.
</td>
</tr>
<tr VALIGN=top>
<td>cdk_draw (3)</td>
<td> Outlines functions used for drawing text and lines.
</td>
</tr>
<tr VALIGN=top>
<td>cdk_screen (3)</td>
<td> Demonstrates the use of screens within Cdk.
</td>
</tr>
<tr VALIGN=top>
<td>cdk_misc (3)</td>
<td> Outlines miscellaneous functions provided with the Cdk library.
</td>
</tr>
<tr VALIGN=top>
<td>cdk_process (3)</td>
<td> Demonstrates the use of the pre- and post-process function class.
</td>
</tr>
</table>
<p></center></p>
<h2>DESCRIPTION</h2>
<p> Cdk is a library of functions which allow a programmer to quickly create a full screen interactive program with ease. The Cdk widgets support the following features: </p>
<dl>
<dt>&bull; Ncurses library.</p>
<dd> Instead of using the standard curses library, Cdk can take advantage of the colors that Ncurses provides. To learn how to take advantage of Cdk&#8217;s color capabilities, see <i>cdk_display (3)</i>.</dl>
<dl>
<dt>&bull; Key Bindings.</p>
<dd> Individual keys can be overridden with a callback. The callback is set up using the <code>bindCDKObject</code> function. To learn more about this see <i>cdk_binding (3)</i>.</dl>
<dl>
<dt>&bull; Pre and Post Processing.</p>
<dd> Certain widgets allow the user to trap a character before and after the character has been applied to the widget. This allows programmers to `filter&#8217; character input. To learn more about this see <i>cdk_process (3)</i>.</dl>
<dl>
<dt>&bull; Self Test Widgets.</p>
<dd> With the use of the inject function class and the activate function, programmers can have the widgets test themselves. This allows the programmer to perform automated tests on a final program.</dl>
<dl>
<dt>&bull; Special Display Formats</p>
<dd> There are special character format commands that can be inserted into any string in Cdk and the contents will get mapped to a <i>chtype</i> (see the curses manual page) with character attributes. This allows the programmer to insert format types on each character if they wish.</dl>
<dl>
<dt>&bull; The Ability To Build Predefined Screens</p>
<dd> Widgets can be associated to any given screen. If there is more than one screen defined, then Cdk has the ability to &quot;flip&quot; from one screen to another with ease. See the <i>cdk_screen</i> manual page for more details.</dl>
<h2>STANDARD WIDGET BEHAVIOR</h2>
<p> All of the widgets have a member of the structure called <i>exitType</i>. This member states how the widget exited. There are three values in which to check for, they are as follows: </p>
<p> <center></p>
<table BORDER>
<tr VALIGN=top>
<td><code>Value</code></td>
<td>Meaning
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>vNORMAL</td>
<td> This means the widget exited normally. This value is set when the widget is given the characters TAB or RETURN.
</td>
</tr>
<tr VALIGN=top>
<td>vEARLY_EXIT</td>
<td> This means the widget exited early. This value is set when characters such as TAB or RETURN are injected into the widget via the injectCDKXXX function and the character injected does not exit the widget.
</td>
</tr>
<tr VALIGN=top>
<td>vERROR</td>
<td> This value states that an error was returned by curses, e.g., if the terminal was disconnected.
</td>
</tr>
<tr VALIGN=top>
<td>vESCAPE_HIT</td>
<td> This value states the user hit ESCAPE to leave the widget.
</td>
</tr>
<tr VALIGN=top>
<td>vNEVER_ACTIVATED</td>
<td> This is the initial state of the value. This means that the widget has not been activated.
</td>
</tr>
</table>
<p></center></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-cdk_binding/">cdk_binding</a></code>(3), <code><a href="/docs/linux/man/3-cdk_display/">cdk_display</a></code>(3), <code><a href="/docs/linux/man/3-cdk_draw/">cdk_draw</a></code>(3), <code><a href="/docs/linux/man/3-cdk_misc/">cdk_misc</a></code>(3), <code><a href="/docs/linux/man/3-cdk_process/">cdk_process</a></code>(3), <code><a href="/docs/linux/man/3-cdk_screen/">cdk_screen</a></code>(3)</p>
<h2>NOTES</h2>
<p> The header file <i>&lt;cdk.h&gt;</i> automatically includes the header files <i>&lt;curses.h&gt;</i>, <i>&lt;stdlib.h&gt;</i>, <i>&lt;string.h&gt;</i>, <i>&lt;ctype.h&gt;</i>, <i>&lt;unistd.h&gt;</i>, <i>&lt;dirent.h&gt;</i>, <i>&lt;time.h&gt;</i>, <i>&lt;errno.h&gt;</i>, <i>&lt;pwd.h&gt;</i>, <i>&lt;grp.h&gt;</i>, <i>&lt;sys/stat.h&gt;</i>, and <i>&lt;sys/types.h&gt;</i>. The <i>&lt;curses.h&gt;</i> header file includes <i>&lt;stdio.h&gt;</i> and <i>&lt;unctrl.h&gt;</i>. </p>
<h2>Index</h2>
