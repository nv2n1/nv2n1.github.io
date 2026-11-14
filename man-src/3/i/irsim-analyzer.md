---
title: "irsim-analyzer(3)"
name: "irsim-analyzer"
section: "3"
letter: "i"
url: "/docs/linux/man/3-irsim-analyzer/"
description: "irsim-analyzer"
---

<h2>NAME</h2>
<p> irsim-analyzer</p>
<h2>SYNOPSIS</h2>
<p> <code>analyzer </code><i>node&#8230;</i></p>
<h2>DESCRIPTION</h2>
<p> The analyzer provides a graphical interface to irsim; displaying the state of the nodes (or vectors) <i>node&#8230;</i> </p>
<p> Every invocation of the <code>analyzer</code> command adds a new set of signals to the display list. </p>
<p> The view is split into 3 regions: a trace window, a text window, and a banner. The banner displays the name of the simulation (from the sim file), and the <i>pull-down</i> menu headers. The text window is a 1-line window used to request and display certain information. </p>
<p> The trace window displays the following information:</p>
<dl>
<dt><code>left side: </code></p>
<dd> names of the signals (nodes/vectors) displayed.</p>
<dt><code>top side: </code></p>
<dd> On the left and right sides, the time corresponding to the left and right edges of the trace window. In the center, the time of the current <i>cursor</i> position.</p>
<dt><code>right side: </code></p>
<dd> Values of the signals under the cursor. </p>
</dl>
<h2>MENU FUNCTIONS</h2>
<dl>
<dt><code>zoom:</code></p>
<dd>
<p> <code>in </code> Zooms in by a factor of 2 (magnify). </p>
<p> <code>out </code> Zooms out by a factor of 2 (reduce).</p>
<dt><code>base:</code></p>
<dd> Changes the numerical base used to display the value of the selected vector (see below how to select a trace) to one of the following: </p>
<p> <code>bin </code> (base 2) </p>
<p> <code>oct </code> (base 8) </p>
<p> <code>hex </code> (base 16)</dl>
<p> <code>window:1</code></p>
<dl>
<dt>
<dd>
<dl>
<dt><code>delta T</code></p>
<dd> Allows to determine the difference (in time) between any two edges. First click the mouse (any button) to the right of the first edge, then to the left of the second edge. The time of the two edges as well as their difference will be shown in the text window. As long as the button remains depressed, a line is shown between the two edges. Times are all shown in ns.</p>
<dt><code>move to </code></p>
<dd> Moves the left edge of the trace window to the specified time. The time is requested in the text window.</p>
<dt><code>set width </code></p>
<dd> Sets the number of ns. that will be displayed. The time is requested in the text window.</p>
<dt><code>name length </code></p>
<dd> Since the most important differentiating information in a long signal name is usually at the end, the analyzer will display the last 15 characters of a signal name. This option allows changing the maximum number of characters that will be displayed, which must be in the range [8-256].</p>
<dt><code>scroll </code></p>
<dd> Usually the analyzer displays simulation activity by scrolling the traces to the left, so the last changes are shown. The <i>scroll</i> feature enables/disables this scrolling, effectively freezing the traces. When scrolling is enabled, a check mark is shown on this menu entry.</dl>
</dl>
<dl>
<dt><code>print:</code></p>
<dd> These options control the generation of a PostScript file suitable for obtaining a hardcopy of the trace window.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>file</code></p>
<dd> Requests the filename to hold the PostScript output. Hitting <i>&lt;return&gt;</i> will use the default name (shown in parens). Hitting <i>&lt;ctrl-C&gt;</i> will abort generation of the file. The following menu entries control the aspect of the PostScript file; a check mark in the corresponding menu entry implies that the feature will be included in the output.</p>
<dt><code>banner</code></p>
<dd> Generate a banner, showing the simulation name and current date.</p>
<dt><code>legend</code></p>
<dd> Generate (in a separate page) a description of the signals displayed: the <i>complete</i> names of nodes (since the first characters may be stripped), and for vectors the names of the nodes of wich it is composed.</p>
<dt><code>times</code></p>
<dd> Generate a time ruler at the bottom of the traces.</p>
<dt><code>outline</code></p>
<dd> Draw an outline around the trace window.</dl>
</dl>
</dl>
<h2>MOUSE FUNCTIONS</h2>
<p> The analyzer provides various functions depending on where in the window a mouse button is depressed. All buttons have the same meaning, except inside the scrollbar. Pressing a mouse button in the following regions will provide:</p>
<dl>
<dt><code>Signal names:</code></p>
<dd> The signal name where the button was depressed will be highlighted and will be moved to the position where the button is released, scrolling the other traces if necessary. If the button is released under the same signal on which it was pressed, that signal will become <i>selected.</i> The selected signal is always underlined, and some information regarding that signal is printed in the text window. </p>
<p> If the button is released outside the traces area (above or below) the signal will be removed from the display. It can only be added again by invoking the <code>analyzer</code> command.</p>
<dt><code>Left Arrow:</code></p>
<dd> The traces are scrolled left by half a <i>page</i> (move back in time).</p>
<dt><code>Right Arrow:</code></p>
<dd> The traces are scrolled right by half a <i>page</i> (move forward in time).</p>
<dt><code>Double Left Arrow:</code></p>
<dd> Scrolls traces left by a full <i>page.</i></p>
<dt><code>Double Right Arrow:</code></p>
<dd> Scrolls traces right by a full <i>page.</i></p>
<dt><code>Scrollbar:</code></p>
<dd> The <code>left button</code> allows to <i>stretch</i> the left side of the window, thereby zooming in/out by an arbitrary amount. The right side of the window remains the same. </p>
<p> The <code>right button</code> allows to <i>stretch</i> the right side of the window, thereby zooming in/out by an arbitrary amount. The left side of the window remains the same. </p>
<p> The <code>middle button</code> moves the whole view back and forth in time. The magnification factor remains the same.</p>
<dt><code>Traces</code></p>
<dd>
<p> The <i>cursor</i> is moved to the time-step where the mouse is clicked. Some lack of accuracy in selecting the time may become apparent due to screen resolution round off. </p>
<p> Holding down the <i>shift</i> key simultaneously with the mouse button will <code>not</code> move the <i>cursor,</i> but rather show the value of the signal at the time-step where the mouse is clicked. The value is printed in the text window using the following format:</p>
<dt> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><i>name </i><code>@ </code><i> time:</i><code>value=</code><i>value</i><code>,input=</code><i>status</i></p>
<dt>
<dd>
<dd>The <i>value</i> is always shown in binary, regardless of the base selected for that signal. The <i>status</i> is a string showing which nodes where inputs at that time. Nodes that were inputs have an <code>i</code> in their respective position, otherwise an <code>-.</code></p>
<dt><code>Cursor Values:</code></p>
<dd> The selected signal value is highlighted and, when the button is released, the value of the signal is <i>expanded</i> in the text window. This is useful for displaying each of the bits that make up a vector. The information printed has the following format: </p>
<p> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> <i>name</i><code>:value=</code><i>value</i><code> input=</code><i>status</i> </p>
<p> where <i>value</i> and <i>status</i> have the same meaning as above.</p>
<dt><code>Banner:</code></p>
<dd> Clicking on the banner brings the window to the foreground.</p>
<dt><code>Box on Banner:</code></p>
<dd> Clicking in the <i>little</i> box on the left side of the banner iconizes the analyzer window. To de-iconize the window, simply click any button within the icon.</p>
<dt><code>Banner Menus:</code></p>
<dd> Pressing a mouse button in one of the banner menus (on the right side) will pull down the corresponding menu. </p>
</dl>
<h2>X DEFAULTS</h2>
<p> The analyzer application uses the appropriate resource specification at startup time to customize the appearance of its window. The format for a resource specification in the .Xdefaults file is:</p>
<dl>
<dt>
<dd>
&nbsp;<wbr>&nbsp;<wbr>[name.]resource:&nbsp;<wbr>&nbsp;<wbr>value</dl>
<p> For the analyzer, the available names are <code>irsim</code> and <code>analyzer.</code> The available resources are: </p>
<dl>
<dt><code>background</code></p>
<dd> Specifies the traces window background color. The default is black.</p>
<dt><code>foreground</code></p>
<dd> Specifies the text color, or the background of everything else besides the traces window. The default is white.</p>
<dt><code>geometry</code></p>
<dd> Specifies the default geometry (window size and screen location) of the graphic window. The default Xgeometry is &quot;=1000&#215;300+0+0&quot;.</p>
<dt><code>reverseVideo</code></p>
<dd> Specifies whether the foreground and background colors are to be reversed (on monochrome displays only). The default is off.</p>
<dt><code>font</code></p>
<dd> Specifies the fixed-width font displayed. The default is 6&#215;13.</p>
<dt><code>borderWidth</code></p>
<dd> Specifies the width of the border (in pixels). The default is 2.</p>
<dt><code>borderColor</code></p>
<dd> Specifies the border color when the window is selected. The default is black.</p>
<dt><code>highlight</code></p>
<dd> Specifies the color used for highlighting. The default is red (color displays only).</p>
<dt><code>traceColor</code></p>
<dd> Specifies the color in which the traces are drawn. The default is white.</p>
<dt><code>bannerBg</code></p>
<dd> Specifies the background color for the banner. The default is white.</p>
<dt><code>bannerFg</code></p>
<dd> Specifies the foreground (text) color for the banner. The default is black. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-irsim/">irsim</a>(1) </p>
<h2>Index</h2>
