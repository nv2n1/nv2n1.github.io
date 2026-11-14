---
title: "cdk_position(3)"
name: "cdk_position"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cdk_position/"
description: "cdk_position – curses widget positioning key-bindings"
---

<h2>NAME</h2>
<p> cdk_position &#8211; curses widget positioning key-bindings</p>
<h2>SYNOPSIS</h2>
<p> Position methods for the Cdk widgets allow the user to move the widget around the screen via the cursor/keypad keys.</p>
<h2>DESCRIPTION</h2>
<p> The following key bindings can be used to move the widget around the screen. </p>
<p> <center></p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td><code>Key</code></td>
<td>Action
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>Up Arrow</td>
<td> Moves the widget up one row.
</td>
</tr>
<tr VALIGN=top>
<td>Down Arrow</td>
<td> Moves the widget down one row.
</td>
</tr>
<tr VALIGN=top>
<td>Left Arrow</td>
<td> Moves the widget left one column
</td>
</tr>
<tr VALIGN=top>
<td>Right Arrow</td>
<td> Moves the widget right one column
</td>
</tr>
<tr VALIGN=top>
<td>1</td>
<td> Moves the widget down one row and left one column.
</td>
</tr>
<tr VALIGN=top>
<td>2</td>
<td> Moves the widget down one row.
</td>
</tr>
<tr VALIGN=top>
<td>3</td>
<td> Moves the widget down one row and right one column.
</td>
</tr>
<tr VALIGN=top>
<td>4</td>
<td> Moves the widget left one column
</td>
</tr>
<tr VALIGN=top>
<td>5</td>
<td> Centers the widget both vertically and horizontally.
</td>
</tr>
<tr VALIGN=top>
<td>6</td>
<td>Moves the widget right one column
</td>
</tr>
<tr VALIGN=top>
<td>7</td>
<td> Moves the widget up one row and left one column.
</td>
</tr>
<tr VALIGN=top>
<td>8</td>
<td> Moves the widget up one row.
</td>
</tr>
<tr VALIGN=top>
<td>9</td>
<td> Moves the widget up one row and right one column.
</td>
</tr>
<tr VALIGN=top>
<td>t</td>
<td> Moves the widget to the top of the screen.
</td>
</tr>
<tr VALIGN=top>
<td>b</td>
<td> Moves the widget to the bottom of the screen.
</td>
</tr>
<tr VALIGN=top>
<td>l</td>
<td> Moves the widget to the left of the screen.
</td>
</tr>
<tr VALIGN=top>
<td>r</td>
<td> Moves the widget to the right of the screen.
</td>
</tr>
<tr VALIGN=top>
<td>c</td>
<td> Centers the widget between the left and right of the window.
</td>
</tr>
<tr VALIGN=top>
<td>C</td>
<td> Centers the widget between the top and bottom of the window.
</td>
</tr>
<tr VALIGN=top>
<td>Escape</td>
<td>Returns the widget to its original position.
</td>
</tr>
<tr VALIGN=top>
<td>Return</td>
<td> Exits the function and leaves the widgetwhere it was.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
<hr>
</td>
</tr>
</table>
</table>
<p></center> </p>
<p> The numbers 0-9 are chosen to correspond to the numeric keypad on your terminal. Cdk does not handle the application mode keypad control sequences, since those are not defined via terminfo. To use the numeric keypad you should ensure that it is in normal (or NumLock) mode.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-cdk/">cdk</a></code>(3), <code><a href="/docs/linux/man/3-cdk_binding/">cdk_binding</a></code>(3), <code><a href="/docs/linux/man/3-cdk_display/">cdk_display</a></code>(3), <code><a href="/docs/linux/man/3-cdk_screen/">cdk_screen</a></code>(3) </p>
<h2>Index</h2>
