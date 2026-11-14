---
title: "whiptail(1)"
name: "whiptail"
section: "1"
letter: "w"
url: "/docs/linux/man/1-whiptail/"
description: "whiptail – display dialog boxes from shell scripts"
---

<h2 class="name">NAME</h2>
<p> whiptail &#8211; display dialog boxes from shell scripts </p>
<h2>SYNOPSIS</h2>
<p> <code>whiptail</code> [ <code>&#8211;title</code> <i>title</i> ] [ <code>&#8211;backtitle</code> <i>backtitle</i> ] [ <code>&#8211;clear</code> ] [ <code>&#8211;default-item</code> <i>string</i> ] [ <code>&#8211;defaultno</code> ] [ <code>&#8211;fb</code> ] [ <code>&#8211;nocancel</code> ] [ <code>&#8211;yes-button</code> <i>text</i> ] [ <code>&#8211;no-button</code> <i>text</i> ] [ <code>&#8211;ok-button</code> <i>text</i> ] [ <code>&#8211;cancel-button</code> <i>text</i> ] [ <code>&#8211;noitem</code> [ ] <code>&#8211;output-fd</code> <i>fd</i> ] [ <code>&#8211;separate-output</code> ] [ <code>&#8211;scrolltext</code> ] [ <code>&#8211;topleft</code> ] <code>box-options</code></p>
<h2>DESCRIPTION</h2>
<p> <code>whiptail</code> is a program that will let you present a variety of questions or display messages using dialog boxes from a shell script. Currently, these types of dialog boxes are implemented: </p>
<p> <code>yes/no</code> box,<code> menu</code> box,<code> input</code> box, <code>message</code> box,<code> text</code> box,<code> info</code> box, <code>checklist</code> box,<code> radiolist</code> box<code>, gauge</code> box, and <code>password</code> box.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;clear</code></p>
<dd> The screen will be cleared to the <code>screen attribute</code> on exit. This doesn&#8217;t work in an xterm (and descendants) if alternate screen switching is enabled, because in that case slang writes to (and clears) an alternate screen.</p>
<dt><code>&#8211;defaultno</code></p>
<dd> The dialog box will open with the cursor over the <code>No</code> button.</p>
<dt><code>&#8211;default-item</code><i> string</i></p>
<dd> Set the default item in a menu box. Normally the first item in the box is the default.</p>
<dt><code>&#8211;fb</code>, <code>&#8211;fullbuttons</code></p>
<dd> Use full buttons. (By default, <code>whiptail</code> uses compact buttons).</p>
<dt><code>&#8211;nocancel</code></p>
<dd> The dialog box won&#8217;t have a <code>Cancel</code> button.</p>
<dt><code>&#8211;yes-button</code><i> text</i></p>
<dd> Set the text of the <code>Yes</code> button.</p>
<dt><code>&#8211;no-button</code><i> text</i></p>
<dd> Set the text of the <code>No</code> button.</p>
<dt><code>&#8211;ok-button</code><i> text</i></p>
<dd> Set the text of the <code>Ok</code> button.</p>
<dt><code>&#8211;cancel-button</code><i> text</i></p>
<dd> Set the text of the <code>Cancel</code> button.</p>
<dt><code>&#8211;noitem</code></p>
<dd> The menu, checklist and radiolist widgets will display tags only, not the item strings. The menu widget still needs some items specified, but checklist and radiolist expect only tag and status.</p>
<dt><code>&#8211;notags</code></p>
<dd> Don&#8217;t display tags in the menu, checklist and radiolist widgets.</p>
<dt><code>&#8211;separate-output</code></p>
<dd> For checklist widgets, output result one line at a time, with no quoting. This facilitates parsing by another program.</p>
<dt><code>&#8211;output-fd</code><i> fd</i></p>
<dd> Direct output to the given file descriptor. Most <code>whiptail</code> scripts write to standard error, but error messages may also be written there, depending on your script.</p>
<dt><code>&#8211;title</code><i> title</i></p>
<dd> Specifies a <i>title</i> string to be displayed at the top of the dialog box.</p>
<dt><code>&#8211;backtitle</code><i> backtitle</i></p>
<dd> Specifies a <i>backtitle</i> string to be displayed on the backdrop, at the top of the screen.</p>
<dt><code>&#8211;scrolltext</code></p>
<dd> Force the display of a vertical scrollbar.</p>
<dt><code>&#8211;topleft</code></p>
<dd> Put window in top-left corner.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Print a help message and exit.</p>
<dt><code>-v</code>, <code>&#8211;version</code></p>
<dd> Print version information and exit.</p>
<dt><code>Box Options</code></p>
<dd>
<dt><code>&#8211;yesno</code><i> text height width</i></p>
<dd> A<code> yes/no</code> dialog box of size <i>height</i> rows by <i>width</i> columns will be displayed. The string specified by <i>text</i> is displayed inside the dialog box. If this string is too long to be fit in one line, it will be automatically divided into multiple lines at appropriate places. The <i>text</i> string may also contain the sub-string <i>&quot;
&quot;</i> or newline characters <i>`
&#8217;</i> to control line breaking explicitly. This dialog box is useful for asking questions that require the user to answer either yes or no. The dialog box has a<code> Yes</code> button and a <code>No</code> button, in which the user can switch between by pressing the <i>TAB</i> key.</p>
<dt><code>&#8211;msgbox</code><i> text height width</i></p>
<dd> A<code> message</code> box is very similar to a<code> yes/no</code> box. The only difference between a <code>message</code> box and a <code>yes/no</code> box is that a <code>message</code> box has only a single <code>OK</code> button. You can use this dialog box to display any message you like. After reading the message, the user can press the <i>ENTER</i> key so that <code>whiptail</code> will exit and the calling shell script can continue its operation.</p>
<dt><code>&#8211;infobox</code><i> text height width</i></p>
<dd> An<code> info</code> box is basically a<code> message</code> box. However, in this case, <code>whiptail</code> will exit immediately after displaying the message to the user. The screen is not cleared when <code>whiptail</code> exits, so that the message will remain on the screen until the calling shell script clears it later. This is useful when you want to inform the user that some operations are carrying on that may require some time to finish.</p>
<dt><code>&#8211;inputbox</code><i> text height width [init]</i></p>
<dd> An <code>input</code> box is useful when you want to ask questions that require the user to input a string as the answer. If init is supplied it is used to initialize the input string. When inputing the string, the <i>BACKSPACE</i> key can be used to correct typing errors. If the input string is longer than the width of the dialog box, the input field will be scrolled. On exit, the input string will be printed on <i>stderr</i>.</p>
<dt><code>&#8211;passwordbox</code><i> text height width [init]</i></p>
<dd> A <code>password</code> box is similar to an input box, except the text the user enters is not displayed. This is useful when prompting for passwords or other sensitive information. Be aware that if anything is passed in &quot;init&quot;, it will be visible in the system&#8217;s process table to casual snoopers. Also, it is very confusing to the user to provide them with a default password they cannot see. For these reasons, using &quot;init&quot; is highly discouraged.</p>
<dt><code>&#8211;textbox</code><i> file height width</i></p>
<dd> A<code> text</code> box lets you display the contents of a text file in a dialog box. It is like a simple text file viewer. The user can move through the file by using the <i>UP/DOWN</i>, <i>PGUP/PGDN</i> and<i> HOME/END</i> keys available on most keyboards. If the lines are too long to be displayed in the box, the <i>LEFT/RIGHT</i> keys can be used to scroll the text region horizontally. For more convenience, forward and backward searching functions are also provided.</p>
<dt><code>&#8211;menu </code><i>text height width menu-height </i>[ <i>tag item </i>] <i>&#8230;</p>
<dd> As its name suggests, a </i><code>menu</code> box is a dialog box that can be used to present a list of choices in the form of a menu for the user to choose. Each menu entry consists of a <i>tag</i> string and an <i>item</i> string. The <i>tag</i> gives the entry a name to distinguish it from the other entries in the menu. The <i>item</i> is a short description of the option that the entry represents. The user can move between the menu entries by pressing the <i>UP/DOWN</i> keys, the first letter of the <i>tag</i> as a hot-key. There are <i>menu-height</i> entries displayed in the menu at one time, but the menu will be scrolled if there are more entries than that. When <code>whiptail</code> exits, the <i>tag</i> of the chosen menu entry will be printed on <i>stderr</i>.</p>
<dt><code>&#8211;checklist </code><i>text height width list-height </i>[ <i>tag item status </i>] <i>&#8230;</p>
<dd> </i>A <code>checklist</code> box is similar to a <code>menu</code> box in that there are multiple entries presented in the form of a menu. You can select and deselect items using the SPACE key. The initial on/off state of each entry is specified by <i>status</i>. On exit, a list of the <i>tag</i> strings of those entries that are turned on will be printed on <i>stderr</i>. </p>
<dt><code>&#8211;radiolist </code><i>text height width list-height </i> [ <i>tag item status </i>] <i>&#8230;</p>
<dd> </i>A <code>radiolist</code> box is similar to a <code>menu</code> box. The only difference is that you can indicate which entry is currently selected, by setting its <i>status</i> to <i>on</i>. </p>
<dt><code>&#8211;gauge </code><i>text height width percent</i></p>
<dd> A <code>gauge</code> box displays a meter along the bottom of the box. The meter indicates a percentage. New percentages are read from standard input, one integer per line. The meter is updated to reflect each new percentage. If stdin is XXX, the first following line is a percentage and subsequent lines up to another XXX are used for a new prompt. The gauge exits when EOF is reached on stdin. </p>
</dl>
<h2>NOTES</h2>
<p> whiptail interprets arguments starting with a dash &quot;-&quot; as being arguments. To avoid this, and start some text in, for example, a menubox item, with a dash, whiptail honours the getopt convention of accepting the special argument &quot;&#8211;&quot; which means that all following arguments with dashes are to be treated verbatim and not parsed as options.</p>
<h2>DIAGNOSTICS</h2>
<p> Exit status is 0 if <code>whiptail</code> is exited by pressing the <code>Yes</code> or <code>OK</code> button, and 1 if the <code>No</code> or <code>Cancel</code> button is pressed. Otherwise, if errors occur inside <code>whiptail</code> or <code>whiptail</code> is exited by pressing the <i>ESC</i> key, the exit status is 255.</p>
<h2>AUTHOR</h2>
<p> Based on the man page for <a href="/docs/linux/man/1-dialog/">dialog</a>(1) by: </p>
<p> Savio Lam (lam836 [at] cs.cuhk.hk) &#8211; version 0.3 </p>
<p> Stuart Herbert (S.Herbert [at] sheffield.ac.uk) &#8211; patch for version 0.4 </p>
<p> Modifications for whiptail by: </p>
<p> Enrique Zanardi (ezanard [at] debian.org) </p>
<p> Alastair McKinstry (mckinstry [at] debian.org) </p>
<h2>Index</h2>
