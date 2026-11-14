---
title: "dialog(1)"
name: "dialog"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dialog/"
description: "dialog – display dialog boxes from shell scripts"
---

<h2>NAME</h2>
<p> dialog &#8211; display dialog boxes from shell scripts</p>
<h2>SYNOPSIS</h2>
<p> <code>dialog &#8211;clear</code><br />
 <code>dialog &#8211;create-rc </code><i>file</i><br />
 <code>dialog &#8211;print-maxsize</code><br />
 <code>dialog</code> <i>common-options</i> <i>box-options</i></p>
<h2>DESCRIPTION</h2>
<p> <code>Dialog</code> is a program that will let you to present a variety of questions or display messages using dialog boxes from a shell script. These types of dialog boxes are implemented (though not all are necessarily compiled into <code>dialog</code>):</p>
<dl>
<dt>
<dd>
<p> <code>buildlist</code>, <code>calendar</code>, <code>checklist</code>, <code>dselect</code>, <code>editbox</code>, <code>form</code>, <code>fselect</code>, <code>gauge</code>, <code>infobox</code>, <code>inputbox</code>, <code>inputmenu</code>, <code>menu</code>, <code>mixedform</code>, <code>mixedgauge</code>, <code>msgbox</code> (message), <code>passwordbox</code>, <code>passwordform</code>, <code>pause</code>, <code>prgbox</code>, <code>programbox</code>, <code>progressbox</code>, <code>radiolist</code>, <code>rangebox</code>, <code>tailbox</code>, <code>tailboxbg</code>, <code>textbox</code>, <code>timebox</code>, <code>treeview</code>, and <code>yesno</code> (yes/no).</dl>
<p> You can put more than one dialog box into a script:</p>
<dl>
<dt>&bull;</p>
<dd> Use the &quot;<code>&#8211;and-widget</code>&quot; token to force <code>dialog</code> to proceed to the next dialog unless you have pressed ESC to cancel, or</p>
<dt>&bull;</p>
<dd> Simply add the tokens for the next dialog box, making a chain. Dialog stops chaining when the return code from a dialog is nonzero, e.g., Cancel or No (see DIAGNOSTICS).</dl>
<p> Some widgets, e.g., checklist, will write text to <code>dialog</code>&#8216;s output. Normally that is the standard error, but there are options for changing this: &quot;<code>&#8211;output-fd</code>&quot;, &quot;<code>&#8211;stderr</code>&quot; and &quot;<code>&#8211;stdout</code>&quot;. No text is written if the Cancel button (or ESC) is pressed; <code>dialog</code> exits immediately in that case.</p>
<h2>OPTIONS</h2>
<p> All options begin with &quot;<code>&#8212;</code>&quot; (two ASCII hyphens, for the benefit of those using systems with deranged locale support). </p>
<p> A &quot;<code>&#8212;</code>&quot; by itself is used as an escape, i.e., the next token on the command-line is not treated as an option.</p>
<dl>
<dt>
<dd> <code>dialog &#8211;title &#8212; &#8211;Not an option</code></dl>
<p> The &quot;<code>&#8211;args</code>&quot; option tells <code>dialog</code> to list the command-line parameters to the standard error. This is useful when debugging complex scripts using the &quot;<code>&#8212;</code>&quot; and &quot;<code>&#8211;file</code>&quot;, since the command-line may be rewritten as these are expanded. </p>
<p> The &quot;<code>&#8211;file</code>&quot; option tells <code>dialog</code> to read parameters from the file named as its value.</p>
<dl>
<dt>
<dd> <code>dialog &#8211;file </code><i>parameterfile</i></dl>
<p> Blanks not within double-quotes are discarded (use backslashes to quote single characters). The result is inserted into the command-line, replacing &quot;<code>&#8211;file</code>&quot; and its option value. Interpretation of the command-line resumes from that point. If <i>parameterfile</i> begins with &quot;&amp;&quot;, <code>dialog</code> interprets the following text as a file descriptor number rather than a filename.</p>
<h3><code>Common Options</code></h3>
<dl>
<dt><code>&#8211;ascii-lines</p>
<dd> Rather than draw graphics lines around boxes, draw ASCII &quot;+&quot; and &quot;-&quot; in the same place. See also &quot;&#8211;no-lines</code>&quot;.</p>
<dt><code>&#8211;aspect </code><i>ratio</p>
<dd> This gives you some control over the box dimensions when using auto sizing (specifying 0 for height and width). It represents width / height. The default is 9, which means 9 characters wide to every 1 line high.</p>
<dt></i><code>&#8211;backtitle </code><i>backtitle</p>
<dd> Specifies a backtitle</i> string to be displayed on the backdrop, at the top of the screen.</p>
<dt><code>&#8211;begin </code><i>y x</p>
<dd> Specify the position of the upper left corner of a dialog box on the screen.</p>
<dt></i><code>&#8211;cancel-label </code><i>string</p>
<dd> Override the label used for &quot;Cancel&quot; buttons.</p>
<dt></i><code>&#8211;clear</p>
<dd> Clears the widget screen, keeping only the screen_color background. Use this when you combine widgets with &quot;&#8211;and-widget</code>&quot; to erase the contents of a previous widget on the screen, so it won&#8217;t be seen under the contents of a following widget. Understand this as the complement of &quot;<code>&#8211;keep-window</code>&quot;. To compare the effects, use these:</p>
<dt>
<dd> All three widgets visible, staircase effect, ordered 1,2,3:</p>
<dl>
<dt>
<dd>
<pre><code>
dialog-- begin 2 2 --yesno "" 0 0 --and-widget-- begin 4 4 --yesno "" 0 0 --and-widget-- begin 6 6 --yesno "" 0 0
</code></pre>
</dl>
<dt>
<dd> Only the last widget is left visible:</p>
<dl>
<dt>
<dd>
<p>dialog&#8211; clear&#8211; begin 2 2 &#8211;yesno &#8220;&#8221; 0 0 &#8211;and-widget&#8211; clear&#8211; begin 4 4 &#8211;yesno &#8220;&#8221; 0 0 &#8211;and-widget&#8211; begin 6 6 &#8211;yesno &#8220;&#8221; 0 0
</dl>
<dt>
<dd> All three widgets visible, staircase effect, ordered 3,2,1:</p>
<dl>
<dt>
<dd>
<p>dialog&#8211; keep &#8211; window&#8211; begin 2 2 &#8211;yesno &#8220;&#8221; 0 0 &#8211;and-widget&#8211; keep &#8211; window&#8211; begin 4 4 &#8211;yesno &#8220;&#8221; 0 0 &#8211;and-widget&#8211; begin 6 6 &#8211;yesno &#8220;&#8221; 0 0
</dl>
<dt>
<dd> First and third widget visible, staircase effect, ordered 3,1:</p>
<dl>
<dt>
<dd>
<pre><code>
dialog-- keep - window-- begin 2 2 --yesno "" 0 0 --and-widget-- clear-- begin 4 4 --yesno "" 0 0 --and-widget-- begin 6 6 --yesno "" 0 0
</code></pre>
</dl>
<dt>
<dd> Note, if you want to restore original console colors and send your cursor home after the dialog program has exited, use the <code>clear</code>&nbsp;<wbr>(1) command.</p>
<dt><code>&#8211;colors</p>
<dd> Interpret embedded &quot;\Z&quot; sequences in the dialog text by the following character, which tells dialog</code> to set colors or video attributes: 0 through 7 are the ANSI used in curses: black, red, green, yellow, blue, magenta, cyan and white respectively. Bold is set by &#8216;b&#8217;, reset by &#8216;B&#8217;. Reverse is set by &#8216;r&#8217;, reset by &#8216;R&#8217;. Underline is set by &#8216;u&#8217;, reset by &#8216;U&#8217;. The settings are cumulative, e.g., &quot;\Zb\Z1&quot; makes the following text bold (perhaps bright) red. Restore normal settings with &quot;\Zn&quot;.</p>
<dt><code>&#8211;column-separator </code><i>string</p>
<dd> Tell </i><code>dialog</code> to split data for radio/checkboxes and menus on the occurrences of the given string, and to align the split data into columns.</p>
<dt><code>&#8211;cr-wrap</p>
<dd> Interpret embedded newlines in the dialog text as a newline on the screen. Otherwise, dialog</code> will only wrap lines where needed to fit inside the text box.</p>
<dt>
<dd> Even though you can control line breaks with this, <code>Dialog</code> will still wrap any lines that are too long for the width of the box. Without cr-wrap, the layout of your text may be formatted to look nice in the source code of your script without affecting the way it will look in the dialog.</p>
<dt>
<dd> See also the &quot;<code>&#8211;no-collapse</code>&quot; and &quot;<code>&#8211;trim</code>&quot; options.</p>
<dt><code>&#8211;create-rc </code><i>file</p>
<dd> When </i><code>dialog</code> supports run-time configuration, this can be used to dump a sample configuration file to the file specified by <i>file</i>.</p>
<dt><code>&#8211;date-format </code><i>format</p>
<dd> If the host provides </i><code>strftime</code>, this option allows you to specify the format of the date printed for the <code>&#8211;calendar</code> widget. The time of day (hour, minute, second) are the current local time.</p>
<dt><code>&#8211;defaultno</p>
<dd> Make the default value of the yes/no</code> box a <code>No</code>. Likewise, make the default button of widgets that provide &quot;OK&quot; and &quot;Cancel&quot; a <code>Cancel</code>. If &quot;<code>&#8211;nocancel</code>&quot; or &quot;<code>&#8211;visit-items</code>&quot; are given those options overrides this, making the default button always &quot;Yes&quot; (internally the same as &quot;OK&quot;).</p>
<dt><code>&#8211;default-button </code><i>string</p>
<dd> Set the default (preselected) button in a widget. By preselecting a button, a script makes it possible for the user to simply press Enter</i> to proceed through a dialog with minimum interaction.</p>
<dt>
<dd> The option&#8217;s value is the name of the button: <i>ok</i>, <i>yes</i>, <i>cancel</i>, <i>no</i>, <i>help</i>&nbsp;<wbr>or <i>extra</i>.</p>
<dt>
<dd> Normally the first button in each widget is the default. The first button shown is determined by the widget together with the &quot;<code>&#8211;nook</code>&quot; and &quot;<code>&#8211;nocancel</code> options. If this option is not given, there is no default button assigned.</p>
<dt><code>&#8211;default-item </code><i>string</p>
<dd> Set the default item in a checklist, form or menu box. Normally the first item in the box is the default.</p>
<dt></i><code>&#8211;exit-label </code><i>string</p>
<dd> Override the label used for &quot;EXIT&quot; buttons.</p>
<dt></i><code>&#8211;extra-button</p>
<dd> Show an extra button, between &quot;OK&quot; and &quot;Cancel&quot; buttons.</p>
<dt>&#8211;extra-label </code><i>string</p>
<dd> Override the label used for &quot;Extra&quot; buttons. Note: for inputmenu widgets, this defaults to &quot;Rename&quot;.</p>
<dt></i><code>&#8211;help</p>
<dd> Prints the help message to the standard output and exits. The help message is also printed if no options are given, or if an unrecognized option is given.</p>
<dt>&#8211;help-button</p>
<dd> Show a help-button after &quot;OK&quot; and &quot;Cancel&quot; buttons, i.e., in checklist, radiolist and menu boxes. If &quot;&#8211;item-help</code>&quot; is also given, on exit the return status will be the same as for the &quot;OK&quot; button, and the item-help text will be written to <code>dialog</code>&#8216;s output after the token &quot;HELP&quot;. Otherwise, the return status will indicate that the Help button was pressed, and no message printed.</p>
<dt><code>&#8211;help-label </code><i>string</p>
<dd> Override the label used for &quot;Help&quot; buttons.</p>
<dt></i><code>&#8211;help-status</p>
<dd> If the help-button is selected, writes the checklist, radiolist or form information after the item-help &quot;HELP&quot; information. This can be used to reconstruct the state of a checklist after processing the help request.</p>
<dt>&#8211;hfile </code><i>filename</p>
<dd> Display the given file using a textbox when the user presses F1.</p>
<dt></i><code>&#8211;hline </code><i>string</p>
<dd> Display the given string centered at the bottom of the widget.</p>
<dt></i><code>&#8211;ignore</p>
<dd> Ignore options that dialog</code> does not recognize. Some well-known ones such as &quot;<code>&#8211;icon</code>&quot; are ignored anyway, but this is a better choice for compatibility with other implementations.</p>
<dt><code>&#8211;input-fd </code><i>fd</p>
<dd> Read keyboard input from the given file descriptor. Most </i><code>dialog</code> scripts read from the standard input, but the gauge widget reads a pipe (which is always standard input). Some configurations do not work properly when <code>dialog</code> tries to reopen the terminal. Use this option (with appropriate juggling of file-descriptors) if your script must work in that type of environment.</p>
<dt><code>&#8211;insecure</p>
<dd> Makes the password widget friendlier but less secure, by echoing asterisks for each character.</p>
<dt>&#8211;item-help</p>
<dd> Interpret the tags data for checklist, radiolist and menu boxes adding a column which is displayed in the bottom line of the screen, for the currently selected item.</p>
<dt>&#8211;keep-tite</p>
<dd> When built with ncurses</code>, <code>dialog</code> normally checks to see if it is running in an <code>xterm</code>, and in that case tries to suppress the initialization strings that would make it switch to the alternate screen. Switching between the normal and alternate screens is visually distracting in a script which runs <code>dialog</code> several times. Use this option to allow <code>dialog</code> to use those initialization strings.</p>
<dt><code>&#8211;keep-window</p>
<dd> Normally when dialog</code> performs several <code>tailboxbg</code> widgets connected by &quot;<code>&#8211;and-widget</code>&quot;, it clears the old widget from the screen by painting over it. Use this option to suppress that repainting.</p>
<dt>
<dd> At exit, <code>dialog</code> repaints all of the widgets which have been marked with &quot;<code>&#8211;keep-window</code>&quot;, even if they are not <code>tailboxbg</code> widgets. That causes them to be repainted in reverse order. See the discussion of the &quot;<code>&#8211;clear</code>&quot; option for examples.</p>
<dt><code>&#8211;last-key</p>
<dd> At exit, report the last key which the user entered. This is the curses key code rather than a symbol or literal character. It can be used by scripts to distinguish between two keys which are bound to the same action.</p>
<dt>&#8211;max-input </code><i>size</p>
<dd> Limit input strings to the given size. If not specified, the limit is 2048.</p>
<dt></i><code>&#8211;no-cancel</p>
<dd>
<dt>&#8211;nocancel</p>
<dd> Suppress the &quot;Cancel&quot; button in checklist, inputbox and menu box modes. A script can still test if the user pressed the ESC key to cancel to quit.</p>
<dt>&#8211;no-collapse</p>
<dd> Normally dialog</code> converts tabs to spaces and reduces multiple spaces to a single space for text which is displayed in a message boxes, etc. Use this option to disable that feature. Note that <code>dialog</code> will still wrap text, subject to the &quot;<code>&#8211;cr-wrap</code>&quot; and &quot;<code>&#8211;trim</code>&quot; options.</p>
<dt><code>&#8211;no-items</p>
<dd> Some widgets (checklist, inputmenu, radiolist, menu) display a list with two columns (a &quot;tag&quot; and &quot;item&quot;, i.e., &quot;description&quot;). This option tells dialog</code> to read shorter rows, omitting the &quot;item&quot; part of the list. This is occasionally useful, e.g., if the tags provide enough information.</p>
<dt>
<dd> See also <code>&#8211;no-tags</code>. If both options are given, this one is ignored.</p>
<dt><code>&#8211;no-kill</p>
<dd> Tells dialog</code> to put the <code>tailboxbg</code> box in the background, printing its process id to <code>dialog</code>&#8216;s output. SIGHUP is disabled for the background process.</p>
<dt><code>&#8211;no-label </code><i>string</p>
<dd> Override the label used for &quot;No&quot; buttons.</p>
<dt></i><code>&#8211;no-lines</p>
<dd> Rather than draw lines around boxes, draw spaces in the same place. See also &quot;&#8211;ascii-lines</code>&quot;.</p>
<dt><code>&#8211;no-mouse</p>
<dd> Do not enable the mouse.</p>
<dt>&#8211;no-nl-expand</p>
<dd> Do not convert &quot;
&quot; substrings of the message/prompt text into literal newlines.</p>
<dt>&#8211;no-ok</p>
<dd>
<dt>&#8211;nook</p>
<dd> Suppress the &quot;OK&quot; button in checklist, inputbox and menu box modes. A script can still test if the user pressed the &quot;Enter&quot; key to accept the data.</p>
<dt>&#8211;no-shadow</p>
<dd> Suppress shadows that would be drawn to the right and bottom of each dialog box.</p>
<dt>&#8211;no-tags</p>
<dd> Some widgets (checklist, inputmenu, radiolist, menu) display a list with two columns (a &quot;tag&quot; and &quot;description&quot;). The tag is useful for scripting, but may not help the user. The &#8211;no-tags</code> option (from Xdialog) may be used to suppress the column of tags from the display. Unlike the <code>&#8211;no-items</code> option, this does not affect the data which is read from the script.</p>
<dt>
<dd> Xdialog does not display the tag column for the analogous buildlist and treeview widgets; <code>dialog</code> does the same.</p>
<dt>
<dd> Normally <code>dialog</code> allows you to quickly move to entries on the displayed list, by matching a single character to the first character of the tag. When the <code>&#8211;no-tags</code> option is given, <code>dialog</code> matches against the first character of the description. In either case, the matchable character is highlighted.</p>
<dt><code>&#8211;ok-label </code><i>string</p>
<dd> Override the label used for &quot;OK&quot; buttons.</p>
<dt></i><code>&#8211;output-fd </code><i>fd</p>
<dd> Direct output to the given file descriptor. Most </i><code>dialog</code> scripts write to the standard error, but error messages may also be written there, depending on your script.</p>
<dt><code>&#8211;separator </code><i>string</p>
<dd>
<dt></i><code>&#8211;output-separator</code><i>string</p>
<dd> Specify a string that will separate the output on </i><code>dialog</code>&#8216;s output from checklists, rather than a newline (for &#8211;separate-output) or a space. This applies to other widgets such as forms and editboxes which normally use a newline.</p>
<dt><code>&#8211;print-maxsize</p>
<dd> Print the maximum size of dialog boxes, i.e., the screen size, to dialog</code>&#8216;s output. This may be used alone, without other options.</p>
<dt><code>&#8211;print-size</p>
<dd> Prints the size of each dialog box to dialog</code>&#8216;s output.</p>
<dt><code>&#8211;print-version</p>
<dd> Prints dialog</code>&#8216;s version to <code>dialog</code>&#8216;s output. This may be used alone, without other options. It does not cause <code>dialog</code> to exit by itself.</p>
<dt><code>&#8211;quoted</p>
<dd> Normally dialog</code> quotes the strings returned by checklist&#8217;s as well as the item-help text. Use this option to quote all string results.</p>
<dt><code>&#8211;scrollbar</p>
<dd> For widgets holding a scrollable set of data, draw a scrollbar on its right-margin. This does not respond to the mouse.</p>
<dt>&#8211;separate-output</p>
<dd> For checklist widgets, output result one line at a time, with no quoting. This facilitates parsing by another program.</p>
<dt>&#8211;separate-widget </code><i>string</p>
<dd> Specify a string that will separate the output on </i><code>dialog</code>&#8216;s output from each widget. This is used to simplify parsing the result of a dialog with several widgets. If this option is not given, the default separator string is a tab character.</p>
<dt><code>&#8211;shadow</p>
<dd> Draw a shadow to the right and bottom of each dialog box.</p>
<dt>&#8211;single-quoted</p>
<dd> Use single-quoting as needed (and no quotes if unneeded) for the output of checklist&#8217;s as well as the item-help text. If this option is not set, dialog</code> uses double quotes around each item. In either case, <code>dialog</code> adds backslashes to make the output useful in shell scripts.</p>
<dt><code>&#8211;size-err</p>
<dd> Check the resulting size of a dialog box before trying to use it, printing the resulting size if it is larger than the screen. (This option is obsolete, since all new-window calls are checked).</p>
<dt>&#8211;sleep </code><i>secs</p>
<dd> Sleep (delay) for the given number of seconds after processing a dialog box.</p>
<dt></i><code>&#8211;stderr</p>
<dd> Direct output to the standard error. This is the default, since curses normally writes screen updates to the standard output.</p>
<dt>&#8211;stdout</p>
<dd> Direct output to the standard output. This option is provided for compatibility with Xdialog, however using it in portable scripts is not recommended, since curses normally writes its screen updates to the standard output. If you use this option, dialog</code> attempts to reopen the terminal so it can write to the display. Depending on the platform and your environment, that may fail.</p>
<dt><code>&#8211;tab-correct</p>
<dd> Convert each tab character to one or more spaces (for the textbox</code> widget; otherwise to a single space). Otherwise, tabs are rendered according to the curses library&#8217;s interpretation.</p>
<dt><code>&#8211;tab-len </code><i>n</p>
<dd> Specify the number of spaces that a tab character occupies if the &quot;</i><code>&#8211;tab-correct</code>&quot; option is given. The default is 8. This option is only effective for the <code>textbox</code> widget.</p>
<dt><code>&#8211;time-format </code><i>format</p>
<dd> If the host provides </i><code>strftime</code>, this option allows you to specify the format of the time printed for the <code>&#8211;timebox</code> widget. The day, month, year values in this case are for the current local time.</p>
<dt><code>&#8211;timeout </code><i>secs</p>
<dd> Timeout (exit with error code) if no user response within the given number of seconds. A timeout of zero seconds is ignored.</p>
<dt>
<dd> This option is ignored by the &quot;</i><code>&#8211;pause</code>&quot; widget. It is also overridden if the background &quot;<code>&#8211;tailboxbg</code>&quot; option is used to setup multiple concurrent widgets.</p>
<dt><code>&#8211;title </code><i>title</p>
<dd> Specifies a title</i> string to be displayed at the top of the dialog box.</p>
<dt><code>&#8211;trace </code><i>filename</p>
<dd> logs the command-line parameters, keystrokes and other information to the given file. If </i><code>dialog</code> reads a configure file, it is logged as well. Piped input to the <i>gauge</i> widget is logged. Use control/T to log a picture of the current dialog window.</dl>
<p> The <code>dialog</code> program handles some command-line parameters specially, and removes them from the parameter list as they are processed. For example, if the first option is <code>&#8211;trace</code>, then that is processed (and removed) before <code>dialog</code> initializes the display.</p>
<dl>
<dt><code>&#8211;trim</p>
<dd> eliminate leading blanks, trim literal newlines and repeated blanks from message text.</p>
<dt>
<dd> See also the &quot;&#8211;cr-wrap</code>&quot; and &quot;<code>&#8211;no-collapse</code>&quot; options.</p>
<dt><code>&#8211;version</p>
<dd> Prints dialog</code>&#8216;s version to the standard output, and exits. See also &quot;<code>&#8211;print-version</code>&quot;.</p>
<dt><code>&#8211;visit-items</p>
<dd> Modify the tab-traversal of checklist, radiolist, menubox and inputmenu to include the list of items as one of the states. This is useful as a visual aid, i.e., the cursor position helps some users.</p>
<dt>
<dd> When this option is given, the cursor is initially placed on the list. Abbreviations (the first letter of the tag) apply to the list items. If you tab to the button row, abbreviations apply to the buttons.</p>
<dt>&#8211;yes-label </code><i>string</p>
<dd> Override the label used for &quot;Yes&quot; buttons.</dl>
<p> </i></p>
<h3>Box Options</h3>
<p> All dialog boxes have at least three parameters:</p>
<dl>
<dt><i>text</i></p>
<dd> the caption or contents of the box.</p>
<dt><i>height</i></p>
<dd> the height of the dialog box.</p>
<dt><i>width</i></p>
<dd> the width of the dialog box.</dl>
<p> Other parameters depend on the box type.</p>
<dl>
<dt><code>&#8211;buildlist </code><i>text height width </i>[ <i>tag item status </i>] <i>&#8230;</p>
<dd> A </i><code>buildlist</code> dialog displays two lists, side-by-side. The list on the left shows unselected items. The list on the right shows selected items. As items are selected or unselected, they move between the lists.</p>
<dt>
<dd> Use a carriage return or the &quot;OK&quot; button to accept the current value in the selected-window and exit. The results are written using the order displayed in the selected-window.</p>
<dt>
<dd> The initial on/off state of each entry is specified by <i>status</i>.</p>
<dt>
<dd> The dialog behaves like a <code>menu</code>, using the <code>&#8211;visit-items</code> to control whether the cursor is allowed to visit the lists directly.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> If <code>&#8211;visit-items</code> is not given, tab-traversal uses two states (OK/Cancel).</p>
<dt>&bull;</p>
<dd> If <code>&#8211;visit-items</code> is given, tab-traversal uses four states (Left/Right/OK/Cancel).</dl>
</dl>
<dt>
<dd> Whether or not <code>&#8211;visit&#8211;items</code> is given, it is possible to move the highlight between the two lists using the default &quot;^&quot; (left-column) and &quot;$&quot; (right-column) keys.</p>
<dt>
<dd> On exit, a list of the <i>tag</i> strings of those entries that are turned on will be printed on <code>dialog</code>&#8216;s output.</p>
<dt>
<dd> If the &quot;<code>&#8211;separate-output</code>&quot; option is not given, the strings will be quoted as needed to make it simple for scripts to separate them. By default, this uses double-quotes. See the &quot;<code>&#8211;single-quoted</code>&quot; option, which modifies the quoting behavior.</p>
<dt><code>&#8211;calendar </code><i>text height width day month year</p>
<dd> A </i><code>calendar</code> box displays month, day and year in separately adjustable windows. If the values for day, month or year are missing or negative, the current date&#8217;s corresponding values are used. You can increment or decrement any of those using the left-, up-, right- and down-arrows. Use vi-style h, j, k and l for moving around the array of days in a month. Use tab or backtab to move between windows. If the year is given as zero, the current date is used as an initial value.</p>
<dt>
<dd> On exit, the date is printed in the form day/month/year. The format can be overridden using the <code>&#8211;date-format</code> option.</p>
<dt><code>&#8211;checklist </code><i>text height width list-height </i>[ <i>tag item status </i>] <i>&#8230;</p>
<dd> A </i><code>checklist</code> box is similar to a <code>menu</code> box; there are multiple entries presented in the form of a menu. Another difference is that you can indicate which entry is currently selected, by setting its <i>status</i> to <i>on</i>. Instead of choosing one entry among the entries, each entry can be turned on or off by the user. The initial on/off state of each entry is specified by <i>status</i>.</p>
<dt>
<dd> On exit, a list of the <i>tag</i> strings of those entries that are turned on will be printed on <code>dialog</code>&#8216;s output.</p>
<dt>
<dd> If the &quot;<code>&#8211;separate-output</code>&quot; option is not given, the strings will be quoted as needed to make it simple for scripts to separate them. By default, this uses double-quotes. See the &quot;<code>&#8211;single-quoted</code>&quot; option, which modifies the quoting behavior.</p>
<dt><code>&#8211;dselect </code><i>filepath height width</i></p>
<dd> The directory-selection dialog displays a text-entry window in which you can type a directory, and above that a windows with directory names.</p>
<dt>
<dd> Here <code>filepath</code> can be a filepath in which case the directory window will display the contents of the path and the text-entry window will contain the preselected directory.</p>
<dt>
<dd> Use tab or arrow keys to move between the windows. Within the directory window, use the up/down arrow keys to scroll the current selection. Use the space-bar to copy the current selection into the text-entry window.</p>
<dt>
<dd> Typing any printable characters switches focus to the text-entry window, entering that character as well as scrolling the directory window to the closest match.</p>
<dt>
<dd> Use a carriage return or the &quot;OK&quot; button to accept the current value in the text-entry window and exit.</p>
<dt>
<dd> On exit, the contents of the text-entry window are written to <code>dialog</code>&#8216;s output.</p>
<dt><code>&#8211;editbox </code><i>filepath height width</i></p>
<dd> The edit-box dialog displays a copy of the file. You may edit it using the <i>backspace</i>, <i>delete</i> and cursor keys to correct typing errors. It also recognizes pageup/pagedown. Unlike the <code>&#8211;inputbox</code>, you must tab to the &quot;OK&quot; or &quot;Cancel&quot; buttons to close the dialog. Pressing the &quot;Enter&quot; key within the box will split the corresponding line.</p>
<dt>
<dd> On exit, the contents of the edit window are written to <code>dialog</code>&#8216;s output. </p>
<pre>
<dt><code>--form </code><i>text height width formheight </i>[ <i>label y x item y x flen ilen </i>] <i>...<dd></i></pre>
<p> The <code>form</code> dialog displays a form consisting of labels and fields, which are positioned on a scrollable window by coordinates given in the script. The field length <i>flen</i> and input-length <i>ilen</i> tell how long the field can be. The former defines the length shown for a selected field, while the latter defines the permissible length of the data entered in the field.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> If <i>flen</i> is zero, the corresponding field cannot be altered. and the contents of the field determine the displayed-length.</p>
<dt>&bull;</p>
<dd> If <i>flen</i> is negative, the corresponding field cannot be altered, and the negated value of <i>flen</i> is used as the displayed-length.</p>
<dt>&bull;</p>
<dd> If <i>ilen</i> is zero, it is set to <i>flen</i>.</dl>
</dl>
<dt>
<dd> Use up/down arrows (or control/N, control/P) to move between fields. Use tab to move between windows.</p>
<dt>
<dd> On exit, the contents of the form-fields are written to <code>dialog</code>&#8216;s output, each field separated by a newline. The text used to fill non-editable fields (<i>flen</i> is zero or negative) is not written out.</p>
<dt><code>&#8211;fselect </code><i>filepath height width</i></p>
<dd> The <code>fselect</code> (file-selection) dialog displays a text-entry window in which you can type a filename (or directory), and above that two windows with directory names and filenames.</p>
<dt>
<dd> Here <code>filepath</code> can be a filepath in which case the file and directory windows will display the contents of the path and the text-entry window will contain the preselected filename.</p>
<dt>
<dd> Use tab or arrow keys to move between the windows. Within the directory or filename windows, use the up/down arrow keys to scroll the current selection. Use the space-bar to copy the current selection into the text-entry window.</p>
<dt>
<dd> Typing any printable characters switches focus to the text-entry window, entering that character as well as scrolling the directory and filename windows to the closest match.</p>
<dt>
<dd> Typing the space character forces <code>dialog</code> to complete the current name (up to the point where there may be a match against more than one entry).</p>
<dt>
<dd> Use a carriage return or the &quot;OK&quot; button to accept the current value in the text-entry window and exit.</p>
<dt>
<dd> On exit, the contents of the text-entry window are written to <code>dialog</code>&#8216;s output.</p>
<dt><code>&#8211;gauge </code><i>text height width [percent]</i></p>
<dd> A <code>gauge</code> box displays a meter along the bottom of the box. The meter indicates the percentage. New percentages are read from standard input, one integer per line. The meter is updated to reflect each new percentage. If the standard input reads the string &quot;XXX&quot;, then the first line following is taken as an integer percentage, then subsequent lines up to another &quot;XXX&quot; are used for a new prompt. The gauge exits when EOF is reached on the standard input.</p>
<dt>
<dd> The <i>percent</i> value denotes the initial percentage shown in the meter. If not specified, it is zero.</p>
<dt>
<dd> On exit, no text is written to <code>dialog</code>&#8216;s output. The widget accepts no input, so the exit status is always OK.</p>
<dt><code>&#8211;infobox </code><i>text height width</p>
<dd> An </i><code>info</code> box is basically a <code>message</code> box. However, in this case, <code>dialog</code> will exit immediately after displaying the message to the user. The screen is not cleared when <code>dialog</code> exits, so that the message will remain on the screen until the calling shell script clears it later. This is useful when you want to inform the user that some operations are carrying on that may require some time to finish.</p>
<dt>
<dd> On exit, no text is written to <code>dialog</code>&#8216;s output. Only an &quot;OK&quot; button is provided for input, but an ESC exit status may be returned.</p>
<dt><code>&#8211;inputbox </code><i>text height width [init]</p>
<dd> An </i><code>input</code> box is useful when you want to ask questions that require the user to input a string as the answer. If init is supplied it is used to initialize the input string. When entering the string, the <i>backspace</i>, <i>delete</i> and cursor keys can be used to correct typing errors. If the input string is longer than can fit in the dialog box, the input field will be scrolled.</p>
<dt>
<dd> On exit, the input string will be printed on <code>dialog</code>&#8216;s output.</p>
<dt><code>&#8211;inputmenu </code><i>text height width menu-height </i>[ <i>tag item </i>] <i>&#8230;</p>
<dd> An </i><code>inputmenu</code> box is very similar to an ordinary <code>menu</code> box. There are only a few differences between them:</p>
<dl>
<dt>
<dd>
<dl>
<dt>1.</p>
<dd> The entries are not automatically centered but left adjusted.</p>
<dt>2.</p>
<dd> An extra button (called <i>Rename</i>) is implied to rename the current item when it is pressed.</p>
<dt>3.</p>
<dd> It is possible to rename the current entry by pressing the <i>Rename</i> button. Then <code>dialog</code> will write the following on <code>dialog</code>&#8216;s output.</p>
<dt>
<dd> RENAMED &lt;tag&gt; &lt;item&gt;</dl>
</dl>
<dt><code>&#8211;menu </code><i>text height width menu-height </i>[ <i>tag item </i>] <i>&#8230;</p>
<dd> As its name suggests, a </i><code>menu</code> box is a dialog box that can be used to present a list of choices in the form of a menu for the user to choose. Choices are displayed in the order given. Each menu entry consists of a <i>tag</i> string and an <i>item</i> string. The <i>tag</i> gives the entry a name to distinguish it from the other entries in the menu. The <i>item</i> is a short description of the option that the entry represents. The user can move between the menu entries by pressing the cursor keys, the first letter of the <i>tag</i> as a hot-key, or the number keys <i>1-9</i>. There are <i>menu-height</i> entries displayed in the menu at one time, but the menu will be scrolled if there are more entries than that.</p>
<dt>
<dd> On exit the <i>tag</i> of the chosen menu entry will be printed on <code>dialog</code>&#8216;s output. If the &quot;<code>&#8211;help-button</code>&quot; option is given, the corresponding help text will be printed if the user selects the help button. </p>
<pre>
<dt><code>--mixedform </code><i>text height width formheight </i>[ <i>label y x item y x flen ilen itype </i>] <i>...<dd></i></pre>
<p> The <code>mixedform</code> dialog displays a form consisting of labels and fields, much like the <code>&#8211;form</code> dialog. It differs by adding a field-type parameter to each field&#8217;s description. Each bit in the type denotes an attribute of the field:</p>
<dl>
<dt>
<dd>
<dl>
<dt>1</p>
<dd> hidden, e.g., a password field.</p>
<dt>2</p>
<dd> readonly, e.g., a label.</dl>
</dl>
<dt><code>&#8211;mixedgauge </code><i>text height width percent </i>[ <i>tag1 item1 </i>] <i>&#8230;</p>
<dd> A </i><code>mixedgauge</code> box displays a meter along the bottom of the box. The meter indicates the percentage.</p>
<dt>
<dd> It also displays a list of the <i>tag</i>&#8211; and <i>item</i>-values at the top of the box. See <a href="/docs/linux/man/3-dialog/">dialog</a>(3) for the tag values.</p>
<dt>
<dd> The <i>text</i> is shown as a caption between the list and meter. The <i>percent</i> value denotes the initial percentage shown in the meter.</p>
<dt>
<dd> No provision is made for reading data from the standard input as <code>&#8211;gauge</code> does.</p>
<dt>
<dd> On exit, no text is written to <code>dialog</code>&#8216;s output. The widget accepts no input, so the exit status is always OK.</p>
<dt><code>&#8211;msgbox </code><i>text height width</p>
<dd> A </i><code>message</code> box is very similar to a <code>yes/no</code> box. The only difference between a <code>message</code> box and a <code>yes/no</code> box is that a <code>message</code> box has only a single <code>OK</code> button. You can use this dialog box to display any message you like. After reading the message, the user can press the <i>ENTER</i> key so that <code>dialog</code> will exit and the calling shell script can continue its operation.</p>
<dt>
<dd> If the message is too large for the space, <code>dialog</code> may allow you to scroll it, provided that the underlying curses implementation is capable enough. In this case, a percentage is shown in the base of the widget.</p>
<dt>
<dd> On exit, no text is written to <code>dialog</code>&#8216;s output. Only an &quot;OK&quot; button is provided for input, but an ESC exit status may be returned.</p>
<dt><code>&#8211;pause </code><i>text height width seconds</i></p>
<dd> A <code>pause</code> box displays a meter along the bottom of the box. The meter indicates how many seconds remain until the end of the pause. The pause exits when timeout is reached or the user presses the OK button (status OK) or the user presses the CANCEL button or Esc key.</p>
<dt><code>&#8211;passwordbox </code><i>text height width [init]</p>
<dd> A </i><code>password</code> box is similar to an input box, except that the text the user enters is not displayed. This is useful when prompting for passwords or other sensitive information. Be aware that if anything is passed in &quot;init&quot;, it will be visible in the system&#8217;s process table to casual snoopers. Also, it is very confusing to the user to provide them with a default password they cannot see. For these reasons, using &quot;init&quot; is highly discouraged. See &quot;<code>&#8211;insecure</code>&quot; if you do not care about your password.</p>
<dt>
<dd> On exit, the input string will be printed on <code>dialog</code>&#8216;s output. </p>
<pre>
<dt><code>--passwordform </code><i>text height width formheight </i>[ <i>label y x item y x flen ilen </i>] <i>...<dd></i></pre>
<p> This is identical to <code>&#8211;form</code> except that all text fields are treated as <code>password</code> widgets rather than <code>inputbox</code> widgets.</p>
<dt><code>&#8211;prgbox </code><i>text command height width</p>
<dd>
<dt></i><code>&#8211;prgbox </code><i>command height width</p>
<dd> A </i><code>prgbox</code> is very similar to a <code>programbox</code>.</p>
<dt>
<dd> This dialog box is used to display the output of a command that is specified as an argument to <code>prgbox</code>.</p>
<dt>
<dd> After the command completes, the user can press the <i>ENTER</i> key so that <code>dialog</code> will exit and the calling shell script can continue its operation.</p>
<dt>
<dd> If three parameters are given, it displays the text under the title, delineated from the scrolling file&#8217;s contents. If only two parameters are given, this text is omitted.</p>
<dt><code>&#8211;programbox </code><i>text height width</p>
<dd>
<dt></i><code>&#8211;programbox </code><i>height width</p>
<dd> A </i><code>programbox</code> is very similar to a <code>progressbox</code>. The only difference between a <code>program</code> box and a <code>progress</code> box is that a <code>program</code> box displays an <code>OK</code> button (but only after the command completes).</p>
<dt>
<dd> This dialog box is used to display the piped output of a command. After the command completes, the user can press the <i>ENTER</i> key so that <code>dialog</code> will exit and the calling shell script can continue its operation.</p>
<dt>
<dd> If three parameters are given, it displays the text under the title, delineated from the scrolling file&#8217;s contents. If only two parameters are given, this text is omitted.</p>
<dt><code>&#8211;progressbox </code><i>text height width</p>
<dd>
<dt></i><code>&#8211;progressbox </code><i>height width</p>
<dd> A </i><code>progressbox</code> is similar to an <code>tailbox</code>, except that</p>
<dl>
<dt>
<dd>
<dl>
<dt>a) rather than displaying the contents of a file,</p>
<dd> it displays the piped output of a command and</p>
<dt>b) it will exit when it reaches the end of the file</p>
<dd> (there is no &quot;OK&quot; button).</dl>
</dl>
<dt>
<dd> If three parameters are given, it displays the text under the title, delineated from the scrolling file&#8217;s contents. If only two parameters are given, this text is omitted.</p>
<dt><code>&#8211;radiolist </code><i>text height width list-height </i> [ <i>tag item status </i>] <i>&#8230;</p>
<dd> A </i><code>radiolist</code> box is similar to a <code>menu</code> box. The only difference is that you can indicate which entry is currently selected, by setting its <i>status</i> to <i>on</i>.</p>
<dt>
<dd> On exit, the tag of the selected item is written to <code>dialog</code>&#8216;s output.</p>
<dt><code>&#8211;tailbox </code><i>file height width</p>
<dd> Display text from a file in a dialog box, as in a &quot;tail -f&quot; command. Scroll left/right using vi-style &#8216;h&#8217; and &#8216;l&#8217;, or arrow-keys. A &#8216;0&#8217; resets the scrolling.</p>
<dt>
<dd> On exit, no text is written to </i><code>dialog</code>&#8216;s output. Only an &quot;OK&quot; button is provided for input, but an ESC exit status may be returned. </p>
<pre>
<dt><code>--rangebox </code><i>text height width list-height min-value max-value default-value<dd></i></pre>
<p> Allow the user to select from a range of values, e.g., using a slider. The dialog shows the current value as a bar (like the gauge dialog). Tabs or arrow keys move the cursor between the buttons and the value. When the cursor is on the value, you can edit it by:</p>
<dl>
<dt>
<dd>
<dl>
<dt>left/right cursor movement to select a digit to modify</p>
<dd>
<dt>+/-</p>
<dd> characters to increment/decrement the digit by one</p>
<dt>0 through 9</p>
<dd> to set the digit to the given value</dl>
</dl>
<dt>
<dd> Some keys are also recognized in all cursor positions:</p>
<dl>
<dt>
<dd>
<dl>
<dt>home/end</p>
<dd> set the value to its maximum or minimum</p>
<dt>pageup/pagedown</p>
<dd> increment the value so that the slider moves by one column</dl>
</dl>
<dt><code>&#8211;tailboxbg </code><i>file height width</p>
<dd> Display text from a file in a dialog box as a background task, as in a &quot;tail -f &amp;&quot; command. Scroll left/right using vi-style &#8216;h&#8217; and &#8216;l&#8217;, or arrow-keys. A &#8216;0&#8217; resets the scrolling.</p>
<dt>
<dd> Dialog treats the background task specially if there are other widgets (</i><code>&#8211;and-widget</code>) on the screen concurrently. Until those widgets are closed (e.g., an &quot;OK&quot;), <code>dialog</code> will perform all of the tailboxbg widgets in the same process, polling for updates. You may use a tab to traverse between the widgets on the screen, and close them individually, e.g., by pressing <i>ENTER</i>. Once the non-tailboxbg widgets are closed, <code>dialog</code> forks a copy of itself into the background, and prints its process id if the &quot;<code>&#8211;no-kill</code>&quot; option is given.</p>
<dt>
<dd> On exit, no text is written to <code>dialog</code>&#8216;s output. Only an &quot;EXIT&quot; button is provided for input, but an ESC exit status may be returned.</p>
<dt>
<dd> NOTE: Older versions of <code>dialog</code> forked immediately and attempted to update the screen individually. Besides being bad for performance, it was unworkable. Some older scripts may not work properly with the polled scheme.</p>
<dt><code>&#8211;textbox </code><i>file height width</p>
<dd> A </i><code>text</code> box lets you display the contents of a text file in a dialog box. It is like a simple text file viewer. The user can move through the file by using the cursor, page-up, page-down and <i>HOME/END</i> keys available on most keyboards. If the lines are too long to be displayed in the box, the <i>LEFT/RIGHT</i> keys can be used to scroll the text region horizontally. You may also use vi-style keys h, j, k, l in place of the cursor keys, and B or N in place of the page-up and page-down keys. Scroll up/down using vi-style &#8216;k&#8217; and &#8216;j&#8217;, or arrow-keys. Scroll left/right using vi-style &#8216;h&#8217; and &#8216;l&#8217;, or arrow-keys. A &#8216;0&#8217; resets the left/right scrolling. For more convenience, vi-style forward and backward searching functions are also provided.</p>
<dt>
<dd> On exit, no text is written to <code>dialog</code>&#8216;s output. Only an &quot;EXIT&quot; button is provided for input, but an ESC exit status may be returned.</p>
<dt><code>&#8211;timebox </code><i>text height [width hour minute second]</p>
<dd> A dialog is displayed which allows you to select hour, minute and second. If the values for hour, minute or second are missing or negative, the current date&#8217;s corresponding values are used. You can increment or decrement any of those using the left-, up-, right- and down-arrows. Use tab or backtab to move between windows.</p>
<dt>
<dd> On exit, the result is printed in the form hour:minute:second. The format can be overridden using the </i><code>&#8211;time-format</code> option.</p>
<dt><code>&#8211;treeview </code><i>text height width list-height </i>[ <i>tag item status depth </i>] <i>&#8230;</p>
<dd> Display data organized as a tree. Each group of data contains a tag, the text to display for the item, its status (&quot;on&quot; or &quot;off&quot;) and the depth of the item in the tree.</p>
<dt>
<dd> Only one item can be selected (like the </i><code>radiolist</code>). The tag is not displayed.</p>
<dt>
<dd> On exit, the tag of the selected item is written to <code>dialog</code>&#8216;s output.</p>
<dt><code>&#8211;yesno </code><i>text height width</p>
<dd> A </i><code>yes/no</code> dialog box of size <i>height</i> rows by <i>width</i> columns will be displayed. The string specified by <i>text</i> is displayed inside the dialog box. If this string is too long to fit in one line, it will be automatically divided into multiple lines at appropriate places. The <i>text</i> string can also contain the sub-string <i>&quot;
&quot;</i> or newline characters <i>`
&#8217;</i> to control line breaking explicitly. This dialog box is useful for asking questions that require the user to answer either yes or no. The dialog box has a <code>Yes</code> button and a <code>No</code> button, in which the user can switch between by pressing the <i>TAB</i> key.</p>
<dt>
<dd> On exit, no text is written to <code>dialog</code>&#8216;s output. In addition to the &quot;Yes&quot; and &quot;No&quot; exit codes (see DIAGNOSTICS) an ESC exit status may be returned.</p>
<dt>
<dd> The codes used for &quot;Yes&quot; and &quot;No&quot; match those used for &quot;OK&quot; and &quot;Cancel&quot;, internally no distinction is made.</dl>
<h3>Obsolete Options</h3>
<dl>
<dt><code>&#8211;beep</p>
<dd> This was used to tell the original cdialog that it should make a beep when the separate processes of the tailboxbg widget would repaint the screen.</p>
<dt>&#8211;beep-after</p>
<dd> Beep after a user has completed a widget by pressing one of the buttons.</dl>
<p> </code></p>
<h2>RUN-TIME CONFIGURATION</h2>
<dl>
<dt>1.</p>
<dd> Create a sample configuration file by typing:</dl>
<p> &quot;dialog &#8211;create-rc &lt;file&gt;&quot;</p>
<dl>
<dt>2.</p>
<dd> At start, <code>dialog</code> determines the settings to use as follows:</p>
<dl>
<dt>
<dd>
<dl>
<dt>a)</p>
<dd> if environment variable <code>DIALOGRC</code> is set, its value determines the name of the configuration file.</p>
<dt>b)</p>
<dd> if the file in (a) is not found, use the file <i>$HOME/.dialogrc</i> as the configuration file.</p>
<dt>c)</p>
<dd> if the file in (b) is not found, try using the GLOBALRC file determined at compile-time, i.e., <i>/etc/dialogrc</i>.</p>
<dt>d)</p>
<dd> if the file in (c) is not found, use compiled in defaults.</dl>
</dl>
<dt>3.</p>
<dd> Edit the sample configuration file and copy it to some place that <code>dialog</code> can find, as stated in step 2 above.</dl>
<h2>KEY BINDINGS</h2>
<p> You can override or add to key bindings in <code>dialog</code> by adding to the configuration file. <code>Dialog</code>&#8216;s <code>bindkey</code> command maps single keys to its internal coding.</p>
<dl>
<dt>
<dd>
<pre>
bindkey <i>widget</i> <i>curses_key</i> <i>dialog_key</i>
</pre>
</dl>
<p> The <i>widget</i> name can be &quot;*&quot; (all widgets), or specific widgets such as <code>textbox</code>. Specific widget bindings override the &quot;*&quot; bindings. User-defined bindings override the built-in bindings. </p>
<p> The <i>curses_key</i> can be any of the names derived from <code>curses.h</code>, e.g., &quot;HELP&quot; from &quot;KEY_HELP&quot;. <code>Dialog</code> also recognizes ANSI control characters such as &quot;^A&quot;, &quot;^?&quot;, as well as C1-controls such as &quot;~A&quot; and &quot;~?&quot;. Finally, it allows any single character to be escaped with a backslash. </p>
<p> <code>Dialog</code>&#8216;s internal keycode names correspond to the <code>DLG_KEYS_ENUM</code> type in <code>dlg_keys.h</code>, e.g., &quot;HELP&quot; from &quot;DLGK_HELP&quot;.</p>
<h3>Widget Names</h3>
<p> Some widgets (such as the formbox) have an area where fields can be edited. Those are managed in a subwindow of the widget, and may have separate keybindings from the main widget because the subwindows are registered using a different name. <center></p>
<table>
<tr VALIGN=top>
<td><i>Widget</i></td>
<td><i>Window name</i></td>
<td><i>Subwindow Name</i>
</td>
</tr>
<tr VALIGN=top>
<td>calendar</td>
<td>calendar</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>checklist</td>
<td>checklist</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>editbox</td>
<td>editbox</td>
<td>editbox2
</td>
</tr>
<tr VALIGN=top>
<td>form</td>
<td>formbox</td>
<td>formfield
</td>
</tr>
<tr VALIGN=top>
<td>fselect</td>
<td>fselect</td>
<td>fselect2
</td>
</tr>
<tr VALIGN=top>
<td>inputbox</td>
<td>inputbox</td>
<td>inputbox2
</td>
</tr>
<tr VALIGN=top>
<td>menu</td>
<td>menubox</td>
<td>menu
</td>
</tr>
<tr VALIGN=top>
<td>msgbox</td>
<td>msgbox</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>pause</td>
<td>pause</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>progressbox</td>
<td>progressbox</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>radiolist</td>
<td>radiolist</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>tailbox</td>
<td>tailbox</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>textbox</td>
<td>textbox</td>
<td>searchbox
</td>
</tr>
<tr VALIGN=top>
<td>timebox</td>
<td>timebox</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>yesno</td>
<td>yesno</td>
<td>
</td>
</tr>
</table>
<p></center> </p>
<p> Some widgets are actually other widgets, using internal settings to modify the behavior. Those use the same widget name as the actual widget: <center></p>
<table>
<tr VALIGN=top>
<td><i>Widget</i></td>
<td><i>Actual Widget</i>
</td>
</tr>
<tr VALIGN=top>
<td>dselect</td>
<td>fselect
</td>
</tr>
<tr VALIGN=top>
<td>infobox</td>
<td>msgbox
</td>
</tr>
<tr VALIGN=top>
<td>inputmenu</td>
<td>menu
</td>
</tr>
<tr VALIGN=top>
<td>mixedform</td>
<td>form
</td>
</tr>
<tr VALIGN=top>
<td>passwordbox</td>
<td>inputbox
</td>
</tr>
<tr VALIGN=top>
<td>passwordform</td>
<td>form
</td>
</tr>
<tr VALIGN=top>
<td>prgbox</td>
<td>progressbox
</td>
</tr>
<tr VALIGN=top>
<td>programbox</td>
<td>progressbox
</td>
</tr>
<tr VALIGN=top>
<td>tailboxbg</td>
<td>tailbox
</td>
</tr>
</table>
<p></center></p>
<h3>Built-in Bindings</h3>
<p> This manual page does not list the key bindings for each widget, because that detailed information can be obtained by running <code>dialog</code>. If you have set the <code>&#8211;trace</code> option, <code>dialog</code> writes the key-binding information for each widget as it is registered.</p>
<h3>Example</h3>
<p> Normally <code>dialog</code> uses different keys for navigating between the buttons and editing part of a dialog versus navigating within the editing part. That is, tab (and back-tab) traverse buttons (or between buttons and the editing part), while arrow keys traverse fields within the editing part. Tabs are also recognized as a special case for traversing between widgets, e.g., when using multiple tailboxbg widgets. </p>
<p> Some users may wish to use the same key for traversing within the editing part as for traversing between buttons. The form widget is written to support this sort of redefinition of the keys, by adding a special group in &lt;code&gt;dlgk_keys.h&lt;/code&gt; for &quot;form&quot; (left/right/next/prev). Here is an example binding demonstrating how to do this:</p>
<dl>
<dt>
<dd>
<pre>
bindkey formfield TAB  form_NEXT
bindkey formbox   TAB  form_NEXT
bindkey formfield BTAB form_prev
bindkey formbox   BTAB form_prev
</pre>
</dl>
<p> That type of redefinition would not be useful in other widgets, e.g., calendar, due to the potentially large number of fields to traverse.</p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>DIALOGOPTS</code></p>
<dd> Define this variable to apply any of the common options to each widget. Most of the common options are reset before processing each widget. If you set the options in this environment variable, they are applied to <code>dialog</code>&#8216;s state after the reset. As in the &quot;<code>&#8211;file</code>&quot; option, double-quotes and backslashes are interpreted.</p>
<dt>
<dd> The &quot;<code>&#8211;file</code>&quot; option is not considered a common option (so you cannot embed it within this environment variable).</p>
<dt><code>DIALOGRC</code></p>
<dd> Define this variable if you want to specify the name of the configuration file to use.</p>
<dt><code>DIALOG_CANCEL</code></p>
<dd>
<dt><code>DIALOG_ERROR</code></p>
<dd>
<dt><code>DIALOG_ESC</code></p>
<dd>
<dt><code>DIALOG_EXTRA</code></p>
<dd>
<dt><code>DIALOG_HELP</code></p>
<dd>
<dt><code>DIALOG_ITEM_HELP</code></p>
<dd>
<dt><code>DIALOG_OK</code></p>
<dd> Define any of these variables to change the exit code on Cancel (1), error (-1), ESC (255), Extra (3), Help (2), Help with <code>&#8211;item-help</code> (2), or OK (0). Normally shell scripts cannot distinguish between -1 and 255.</p>
<dt><code>DIALOG_TTY</code></p>
<dd> Set this variable to &quot;1&quot; to provide compatibility with older versions of <code>dialog</code> which assumed that if the script redirects the standard output, that the &quot;<code>&#8211;stdout</code>&quot; option was given.</dl>
<h2>FILES</h2>
<dl>
<dt><i>$HOME/.dialogrc</i></p>
<dd> default configuration file</dl>
<h2>EXAMPLES</h2>
<p> The <code>dialog</code> sources contain several samples of how to use the different box options and how they look. Just take a look into the directory <code>samples/</code> of the source.</p>
<h2>DIAGNOSTICS</h2>
<p> Exit status is subject to being overridden by environment variables. The default values and corresponding environment variables that can override them are:</p>
<dl>
<dt>0</p>
<dd> if <code>dialog</code> is exited by pressing the <code>Yes</code> or <code>OK</code> button (DIALOG_OK).</p>
<dt>1</p>
<dd> if the <code>No</code> or <code>Cancel</code> button is pressed (DIALOG_CANCEL).</p>
<dt>2</p>
<dd> if the <code>Help</code> button is pressed (DIALOG_HELP).</p>
<dt>3</p>
<dd> if the <code>Extra</code> button is pressed (DIALOG_EXTRA).</p>
<dt>4</p>
<dd> if the <code>Help</code> button is pressed (DIALOG_HELP), or the <code>&#8211;item-help</code> option is set when the <code>Help</code> button is pressed (DIALOG_ITEM_HELP),</p>
<dt>-1</p>
<dd> if errors occur inside <code>dialog</code> (DIALOG_ERROR) or <code>dialog</code> is exited by pressing the <i>ESC</i> key (DIALOG_ESC).</dl>
<h2>PORTABILITY</h2>
<p> <code>Dialog</code> works with X/Open curses. However, some implementations have deficiencies:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> HPUX curses (and perhaps others) do not open the terminal properly for the <i>newterm</i> function. This interferes with <code>dialog</code>&#8216;s <code>&#8211;input-fd</code> option, by preventing cursor-keys and similar escape sequences from being recognized.</p>
<dt>&bull;</p>
<dd> NetBSD 5.1 curses has incomplete support for wide-characters. <code>dialog</code> will build, but not all examples display properly.</dl>
</dl>
<h2>COMPATIBILITY</h2>
<p> You may want to write scripts which run with other <code>dialog</code> &quot;clones&quot;.</p>
<h3>ORIGINAL DIALOG</h3>
<p> First, there is the &quot;original&quot; <code>dialog</code> program to consider (versions 0.3 to 0.9). It had some misspelled (or inconsistent) options. The <code>dialog</code> program maps those deprecated options to the preferred ones. They include:</p>
<dl>
<dt>
<dd>
<table>
<tr VALIGN=top>
<td><i>Option</i></td>
<td><i>Treatment</i>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>&#8211;guage</code></td>
<td>mapped to <code>&#8211;gauge</code>
</td>
</tr>
</table>
</dl>
<h3>XDIALOG</h3>
<p> Technically, &quot;<code>Xdialog</code>&quot;, this is an X application. With some care, it is possible to write useful scripts that work with both <code>Xdialog</code> and <code>dialog</code>. </p>
<p> The <code>dialog</code> program ignores these options which are recognized by <code>Xdialog</code>:</p>
<dl>
<dt>
<dd>
<table>
<tr VALIGN=top>
<td><i>Option</i></td>
<td><i>Treatment</i>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>&#8211;auto-placement</code></td>
<td>ignored
</td>
</tr>
<tr VALIGN=top>
<td><code>&#8211;fixed-font</code></td>
<td>ignored
</td>
</tr>
<tr VALIGN=top>
<td><code>&#8211;icon</code></td>
<td>ignored
</td>
</tr>
<tr VALIGN=top>
<td><code>&#8211;keep-colors</code></td>
<td>ignored
</td>
</tr>
<tr VALIGN=top>
<td><code>&#8211;no-close</code></td>
<td>ignored
</td>
</tr>
<tr VALIGN=top>
<td><code>&#8211;no-cr-wrap</code></td>
<td>ignored
</td>
</tr>
<tr VALIGN=top>
<td><code>&#8211;screen-center</code></td>
<td>ignored
</td>
</tr>
<tr VALIGN=top>
<td><code>&#8211;separator</code></td>
<td>mapped to <code>&#8211;separate-output</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>&#8211;smooth</code></td>
<td>ignored
</td>
</tr>
<tr VALIGN=top>
<td><code>&#8211;under-mouse</code></td>
<td>ignored
</td>
</tr>
<tr VALIGN=top>
<td><code>&#8211;wmclass</code></td>
<td>ignored
</td>
</tr>
</table>
</dl>
<p> <code>Xdialog</code>&#8216;s manpage has a section discussing its compatibility with <code>dialog</code>. There are some differences not shown in the manpage. For example, the html documentation states</p>
<dl>
<dt>
<dd>
<p> Note: former Xdialog releases used the &quot; (line feed) as a results separator for the checklist widget; this has been changed to &quot;/&quot; in Xdialog v1.5.0 so to make it compatible with (c)dialog. In your old scripts using the Xdialog checklist, you will then have to add the &#8211;separate-output option before the &#8211;checklist one.</dl>
<p> <code>Dialog</code> has not used a different separator; the difference was likely due to confusion regarding some script.</p>
<h3>WHIPTAIL</h3>
<p> Then there is <code>whiptail</code>. For practical purposes, it is maintained by Debian (very little work is done by its upstream developers). Its documentation (README.whiptail) claims</p>
<dl>
<dt>
<dd>
<pre>
<a href="//www.systutorials.com/docs/linux/man/1-whiptail/">whiptail</a>(1) is a lightweight replacement for <a href="//www.systutorials.com/docs/linux/man/1-dialog/">dialog</a>(1),
to provide dialog boxes for shell scripts.
It is built on the
newt windowing library rather than the ncurses library, allowing
it to be smaller in embedded enviroments such as installers,
rescue disks, etc.
whiptail is designed to be drop-in compatible with dialog, but
has less features: some dialog boxes are not implemented, such
as tailbox, timebox, calendarbox, etc.
</pre>
</dl>
<p> Comparing actual sizes (Debian testing, 2007/1/10): The total of sizes for <code>whiptail</code>, the newt, popt and slang libraries is 757kb. The comparable number for <code>dialog</code> (counting ncurses) is 520kb. Disregard the first paragraph. </p>
<p> The second paragraph is misleading, since <code>whiptail</code> also does not work for common options of <code>dialog</code>, such as the gauge box. <code>whiptail</code> is less compatible with <code>dialog</code> than the original mid-1990s dialog 0.4 program. </p>
<p> <code>whiptail</code>&#8216;s manpage borrows features from <code>dialog</code>, e.g., but oddly cites only <code>dialog</code> versions up to 0.4 (1994) as a source. That is, its manpage refers to features which were borrowed from more recent versions of <code>dialog</code>, e.g.,</p>
<dl>
<dt>&bull;</p>
<dd> <code>&#8211;gauge</code> (from 0.5)</p>
<dt>&bull;</p>
<dd> <code>&#8211;passwordbox</code> (from Debian changes in 1999),</p>
<dt>&bull;</p>
<dd> <code>&#8211;default-item</code> (from <code>dialog</code> 2000/02/22),</p>
<dt>&bull;</p>
<dd> <code>&#8211;output-fd</code> (from <code>dialog</code> 2002/08/14).</dl>
<p> Somewhat humorously, one may note that the <code>popt</code> feature (undocumented in its manpage) of using a &quot;&#8211;&quot; as an escape was documented in <code>dialog</code>&#8216;s manpage about a year before it was mentioned in <code>whiptail</code>&#8216;s manpage. <code>whiptail</code>&#8216;s manpage incorrectly attributes that to <code>getopt</code> (and is inaccurate anyway). </p>
<p> Debian uses <code>whiptail</code> for the official <code>dialog</code> variation. </p>
<p> The <code>dialog</code> program ignores or maps these options which are recognized by <code>whiptail</code>:</p>
<dl>
<dt>
<dd>
<table>
<tr VALIGN=top>
<td><i>Option</i></td>
<td><i>Treatment</i>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>&#8211;fb</code></td>
<td>ignored
</td>
</tr>
<tr VALIGN=top>
<td><code>&#8211;fullbutton</code></td>
<td>ignored
</td>
</tr>
<tr VALIGN=top>
<td><code>&#8211;no-button</code></td>
<td>mapped to <code>&#8211;no-label</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>&#8211;nocancel</code></td>
<td>mapped to <code>&#8211;no-cancel</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>&#8211;noitem</code></td>
<td>mapped to <code>&#8211;no-items</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>&#8211;notags</code></td>
<td>mapped to <code>&#8211;no-tags</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>&#8211;ok-button</code></td>
<td>mapped to <code>&#8211;ok-label</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>&#8211;scrolltext</code></td>
<td>mapped to <code>&#8211;scrollbar</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>&#8211;topleft</code></td>
<td>mapped to <code>&#8211;begin 0 0</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>&#8211;yes-button</code></td>
<td>mapped to <code>&#8211;yes-label</code>
</td>
</tr>
</table>
</dl>
<p> There are visual differences which are not addressed by command-line options:</p>
<dl>
<dt>&bull;</p>
<dd> <code>dialog</code> centers lists within the window. <code>whiptail</code> typically puts lists against the left margin.</p>
<dt>&bull;</p>
<dd> <code>whiptail</code> uses angle brackets (&quot;&lt;&quot; and &quot;&gt;&quot;) for marking buttons. <code>dialog</code> uses square brackets.</p>
<dt>&bull;</p>
<dd> <code>whiptail</code> marks the limits of subtitles with vertical bars. <code>dialog</code> does not mark the limits.</p>
<dt>&bull;</p>
<dd> <code>whiptail</code> attempts to mark the top/bottom cells of a scrollbar with up/down arrows. When it cannot do this, it fills those cells with the background color of the scrollbar and confusing the user. <code>dialog</code> uses the entire scrollbar space, thereby getting better resolution.</dl>
<h2>BUGS</h2>
<p> Perhaps.</p>
<h2>AUTHOR</h2>
<p> Thomas E. Dickey (updates for 0.9b and beyond)</p>
<h2>CONTRIBUTORS</h2>
<p> Kiran Cherupally &#8211; the mixed form and mixed gauge widgets. </p>
<p> Tobias C. Rittweiler </p>
<p> Valery Reznic &#8211; the form and progressbox widgets. </p>
<p> Yura Kalinichenko adapted the gauge widget as &quot;pause&quot;. </p>
<p> This is a rewrite (except as needed to provide compatibility) of the earlier version of <code>dialog 0.9a</code>, which lists as authors:</p>
<dl>
<dt>&bull;</p>
<dd> Savio Lam &#8211; version 0.3, &quot;dialog&quot;</p>
<dt>&bull;</p>
<dd> Stuart Herbert &#8211; patch for version 0.4</p>
<dt>&bull;</p>
<dd> Marc Ewing &#8211; the gauge widget.</p>
<dt>&bull;</p>
<dd> Pasquale De Marco &quot;Pako&quot; &#8211; version 0.9a, &quot;cdialog&quot; </p>
</dl>
<h2>Index</h2>
<dt><a href="#lbAI">RUN-TIME CONFIGURATION</a></p>
<dd>
<dt><a href="#lbAJ">KEY BINDINGS</a></p>
<dd>
<dt><a href="#lbAN">ENVIRONMENT</a></p>
<dd>
<dt><a href="#lbAO">FILES</a></p>
<dd>
<dt><a href="#lbAP">EXAMPLES</a></p>
<dd>
<dt><a href="#lbAQ">DIAGNOSTICS</a></p>
<dd>
<dt><a href="#lbAR">PORTABILITY</a></p>
<dd>
<dt><a href="#lbAS">COMPATIBILITY</a></p>
<dd>
<dt><a href="#lbAW">BUGS</a></p>
<dd>
<dt><a href="#lbAX">AUTHOR</a></p>
<dd>
<dt><a href="#lbAY">CONTRIBUTORS</a></p>
<dd></dl>
