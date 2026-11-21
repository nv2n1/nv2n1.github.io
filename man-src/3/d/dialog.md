---

title: "dialog(3)"
name: "dialog"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dialog/"
description: "dialog – widgets and utilities for the dialog program"
---

<p> dialog &#8211; widgets and utilities for the dialog program</p>
<h2>SYNOPSIS</h2>
<p> <code>cc [ flag &#8230; ] file &#8230; -ldialog [ library &#8230; ]</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>or<br />
 <code>cc `dialog-config &#8211;cflags` file &#8230; `dialog-config &#8211;libs` ]</code> </p>
<p> <code>#include &lt;dialog.h&gt;</code> </p>
<p> <code>Dialog</code> is a program that will let you to present a variety of questions or display messages using dialog boxes from a shell script. It is built from the <code>dialog</code> library, which consists of several widgets as well as utility functions that are used by the widgets or the main program.</p>
<h2>DESCRIPTION</h2>
<p> This manpage documents the features from <i>&lt;dialog.h&gt;</i> which are likely to be important to developers using the widgets directly. Some hints are also given for developing new widgets.</p>
<h2>DEFINITIONS</h2>
<p> Exit codes (passed back to the main program for its use) are defined with a &quot;<i>DLG_EXIT_</i> prefix. The defined constants can be mapped using environment variables as described in <code><a href="/docs/linux/man/1-dialog/">dialog</a></code>(1), e.g., <i>DLG_EXIT_OK</i> corresponds to <i>$DIALOG_OK</i>. </p>
<p> Useful character constants which correspond to user input are named with the &quot;<i>CHR_</i>&quot; prefix, e.g., <i>CHR_BACKSPACE</i>. </p>
<p> Colors and video attributes are categorized and associated with settings in the configuration file (see the discussion of <i>$DIALOGRC</i> in <code><a href="/docs/linux/man/1-dialog/">dialog</a></code>(1)). The <i>DIALOG_ATR(n)</i> macro is used for defining the references to the combined color and attribute table <code>dlg_color_table[]</code>. </p>
<p> The <code>dialog</code> application passes its command-line parameters to the widget functions. Some of those parameters are single values, but some of the widgets accept data as an array of values. Those include checklist/radiobox, menubox and formbox. When the <code>&#8211;item-help</code> option is given, an extra column of data is expected. The USE_ITEM_HELP(), CHECKBOX_TAGS, MENUBOX_TAGS and FORMBOX_TAGS macros are used to hide this difference from the calling application. </p>
<p> Most of the other definitions found in <i>&lt;dialog.h&gt;</i> are used for convenience in building the library or main program. These include definitions based on the generated <i>&lt;dlg_config.h&gt;</i> header. </p>
<h2>DATA STRUCTURES</h2>
<p> All of the global data for the <code>dialog</code> library is stored in a few structures: <i>DIALOG_STATE</i>, <i>DIALOG_VARS</i> and <i>DIALOG_COLORS</i>. The corresponding <code>dialog_state</code>, <code>dialog_vars</code> and <code>dlg_color_table</code> global variables should be initialized to zeros, and then populated with the data to use. A few of these must be nonzero for the corresponding widgets to function. As as the case with function names, variables beginning with &quot;<i>dialog_</i>&quot; are designed for use by the calling application while variables beginning with &quot;<i>dlg_</i>&quot; are intended for lower levels, e.g., by the <code>dialog</code> library.</p>
<dl>
<dt><i>DIALOG_STATE.all_subwindows</dt>
<dd> This is a linked list of all subwindows created by the library. The </i><code>dlg_del_window</code> function uses this to free storage for subwindows when deleting a window.</dd>
<dt><i>DIALOG_STATE.all_windows</dt>
<dd> This is a linked list of all windows created by the library. The </i><code>dlg_del_window</code> function uses this to locate windows which may be redrawn after deleting a window.</dd>
<dt><i>DIALOG_STATE.aspect_ratio</dt>
<dd> This corresponds to the command-line option &quot;</i><code>&#8211;aspect-ratio</code>&quot;. The value gives the application some control over the box dimensions when using auto sizing (specifying 0 for height and width). It represents width / height. The default is 9, which means 9 characters wide to every 1 line high.</dd>
<dt><i>DIALOG_STATE.getc_callbacks</dt>
<dd> This is setup in ui_getc.c</i> to record windows which must be polled for input, e.g,. to handle the background tailbox widget. One window is designated as the foreground or control window.</dd>
<dt><i>DIALOG_STATE.getc_redirect</dt>
<dd> If the control window for DIALOG_STATE.getc_callbacks</i> is closed, the list is transferred to this variable. Closing all windows causes the application to exit.</dd>
<dt><i>DIALOG_STATE.no_mouse</dt>
<dd> This corresponds to the command-line option &quot;</i><code>&#8211;no-mouse</code>&quot;. If true, <code>dialog</code> will not initialize (and enable) the mouse in <i>init_dialog</i>.</dd>
<dt><i>DIALOG_STATE.output</dt>
<dd> This is set in the </i><code>dialog</code> application to the stream on which the application and library functions may write text results. Normally that is the standard error, since the curses library prefers to write its data to the standard output. Some scripts, trading portability for convenience, prefer to write results to the standard output, e.g., by using the &quot;<code>&#8211;stdout</code>&quot; option.</dd>
<dt><i>DIALOG_STATE.output_count</dt>
<dd> This is incremented by </i><code>dlg_does_output</code>, which is called by each widget that writes text to the output. The <code>dialog</code> application uses that to decide if it should also write a separator, i.e., <i>DIALOG_STATE.separate_str</i>, between calls to each widget.</dd>
<dt><i>DIALOG_STATE.pipe_input</dt>
<dd> This is set in init_dialog</i> to a stream which can be used by the <code>gauge</code> widget, which must be the application&#8217;s standard input. The <code>dialog</code> application calls <i>init_dialog</i> normally with <i>input</i> set to the standard input, but optionally based on the &quot;<code>&#8211;input-fd</code>&quot; option. Since the application cannot read from a pipe (standard input) and at the same time read the curses input from the standard input, it must allow for reopening the latter from either a specific file descriptor, or directly from the terminal. The adjusted pipe stream value is stored in this variable.</dd>
<dt><i>DIALOG_STATE.screen_initialized</dt>
<dd> This is set in init_dialog</i> and reset in <i>end_dialog</i>. It is used to check if curses has been initialized, and if the <i>endwin</i> function must be called on exit.</dd>
<dt><i>DIALOG_STATE.screen_output</dt>
<dd> This is set in init_dialog</i> to the output stream used by the curses library. Normally that is the standard output, unless that happens to not be a terminal (and if <i>init_dialog</i> can successfully open the terminal directly).</dd>
<dt><i>DIALOG_STATE.separate_str</dt>
<dd> This corresponds to the command-line option &quot;</i><code>&#8211;separate-widget</code>&quot;. The given string specifies a string that will separate the output on <code>dialog</code>&#8216;s output from each widget. This is used to simplify parsing the result of a dialog with several widgets. If this option is not given, the default separator string is a tab character.</dd>
<dt><i>DIALOG_STATE.tab_len</dt>
<dd> This corresponds to the command-line option &quot;</i><code>&#8211;tab-len</code> <i>number</i>&quot;. Specify the number of spaces that a tab character occupies if the &quot;<code>&#8211;tab-correct</code>&quot; option is given. The default is 8.</dd>
<dt><i>DIALOG_STATE.trace_output</dt>
<dd> This corresponds to the command-line option &quot;</i><code>&#8211;trace</code> <i>file</i>&quot;. It is the file pointer to which trace messages are written.</dd>
<dt><i>DIALOG_STATE.use_colors</dt>
<dd> This is set in init_dialog</i> if the curses implementation supports color.</dd>
<dt><i>DIALOG_STATE.use_scrollbar</dt>
<dd> This corresponds to the command-line option &quot;</i><code>&#8211;scrollbar</code>&quot;. If true, draw a scrollbar to make windows holding scrolled data more readable.</dd>
<dt><i>DIALOG_STATE.use_shadow</dt>
<dd> This corresponds to the command-line option &quot;</i><code>&#8211;no-shadow</code>&quot;. This is set in <i>init_dialog</i> if the curses implementation supports color. If true, suppress shadows that would be drawn to the right and bottom of each dialog box.</dd>
<dt><i>DIALOG_STATE.visit_items</dt>
<dd> This corresponds to the command-line option &quot;</i><code>&#8211;visit-items</code>&quot;.</dd></dl>
<p> The <code>dialog</code> application resets the <code>dialog_vars</code> data before accepting options to invoke each widget. Most of the <i>DIALOG_VARS</i> members are set directly from <code>dialog</code>&#8216;s command-line options:</p>
<dl>
<dt><i>DIALOG_VARS.ascii_lines</dt>
<dd> This corresponds to the command-line option &quot;</i><code>&#8211;ascii-lines</code>. It causes line-drawing to be done with ASCII characters, e.g., &quot;+&quot; and &quot;-&quot;. See <i>DIALOG_VARS.no_lines</i>.</dd>
<dt><i>DIALOG_VARS.backtitle</dt>
<dd> This corresponds to the command-line option &quot;</i><code>&#8211;backtitle</code> <i>backtitle</i>&quot;. It specifies a <i>backtitle</i> string to be displayed on the backdrop, at the top of the screen.</dd>
<dt><i>DIALOG_VARS.beep_after_signal</dt>
<dd> This corresponds to the command-line option &quot;</i><code>&#8211;beep-after</code>&quot;. If true, beep after a user has completed a widget by pressing one of the buttons.</dd>
<dt><i>DIALOG_VARS.beep_signal</dt>
<dd> This corresponds to the command-line option &quot;</i><code>&#8211;beep</code>&quot;. It is obsolete.</dd>
<dt><i>DIALOG_VARS.begin_set</dt>
<dd> This is true if the command-line option &quot;</i><code>&#8211;begin y x</code>&quot; was used. It specifies the position of the upper left corner of a dialog box on the screen.</dd>
<dt><i>DIALOG_VARS.begin_x</dt>
<dd> This corresponds to the x</i> value from the command-line option &quot;<code>&#8211;begin</code> <i>y x</i>&quot; (second value).</dd>
<dt><i>DIALOG_VARS.begin_y</dt>
<dd> This corresponds to the y</i> value from the command-line option &quot;<code>&#8211;begin</code> <i>y x</i>&quot; (first value).</dd>
<dt><i>DIALOG_VARS.cancel_label</dt>
<dd> This corresponds to the command-line option &quot;</i><code>&#8211;cancel-label</code> <i>string</i>&quot;. The given <i>string</i> overrides the label used for &quot;Cancel&quot; buttons.</dd>
<dt><i>DIALOG_VARS.cant_kill</dt>
<dd> This corresponds to the command-line option &quot;</i><code>&#8211;no-kill</code>&quot;. If true, this tells <code>dialog</code> to put the <code>tailboxbg</code> box in the background, printing its process id to <code>dialog</code>&#8216;s output. SIGHUP is disabled for the background process.</dd>
<dt><i>DIALOG_VARS.colors</dt>
<dd> This corresponds to the command-line option &quot;</i><code>&#8211;colors</code>&quot;. If true, interpret embedded &quot;\Z&quot; sequences in the dialog text by the following character, which tells <code>dialog</code> to set colors or video attributes: 0 through 7 are the ANSI codes used in curses: black, red, green, yellow, blue, magenta, cyan and white respectively. Bold is set by &#8216;b&#8217;, reset by &#8216;B&#8217;. Reverse is set by &#8216;r&#8217;, reset by &#8216;R&#8217;. Underline is set by &#8216;u&#8217;, reset by &#8216;U&#8217;. The settings are cumulative, e.g., &quot;\Zb\Z1&quot; makes the following text bright red. Restore normal settings with &quot;\Zn&quot;.</dd>
<dt><i>DIALOG_VARS.column_separator</dt>
<dd> This corresponds to the command-line option &quot;</i><code>&#8211;column-separator</code>&quot;. <code>Dialog</code> splits data for radio/checkboxes and menus on the occurrences of the given string, and aligns the split data into columns.</dd>
<dt><i>DIALOG_VARS.cr_wrap</dt>
<dd> This corresponds to the command-line option &quot;</i><code>&#8211;cr-wrap</code>&quot;. If true, interpret embedded newlines in the dialog text as a newline on the screen. Otherwise, <code>dialog</code> will only wrap lines where needed to fit inside the text box. Even though you can control line breaks with this, <code>dialog</code> will still wrap any lines that are too long for the width of the box. Without cr-wrap, the layout of your text may be formatted to look nice in the source code of your script without affecting the way it will look in the dialog.</dd>
<dt><i>DIALOG_VARS.date_format</dt>
<dd> This corresponds to the command-line option &quot;</i><code>&#8211;date-format</code> <i>string</i>&quot;. If the host provides <code>strftime</code>, and the value is nonnull, the calendar widget uses this to format its output.</dd>
<dt><i>DIALOG_VARS.default_button</dt>
<dd> This is set by the command-line option &quot;</i><code>&#8211;default-button</code>. It is used by <code>dlg_default_button</code>.</dd>
<dt><i>DIALOG_VARS.default_item</dt>
<dd> This corresponds to the command-line option &quot;</i><code>&#8211;default-item</code> <i>string</i>&quot;. The given string is used as the default item in a checklist, form or menu box. Normally the first item in the box is the default.</dd>
<dt><i>DIALOG_VARS.defaultno</dt>
<dd> This corresponds to the command-line option &quot;</i><code>&#8211;defaultno</code>&quot;. If true, make the default value of the <code>yes/no</code> box a <code>No</code>. Likewise, make the default button of widgets that provide &quot;OK&quot; and &quot;Cancel&quot; a <code>Cancel</code>. If <code>&#8211;nocancel</code> was given that option overrides this, making the default button always &quot;Yes&quot; (internally the same as &quot;OK&quot;).</dd>
<dt><i>DIALOG_VARS.dlg_clear_screen</dt>
<dd> This corresponds to the command-line option &quot;</i><code>&#8211;clear</code>&quot;. This option is implemented in the main program, not the library. If true, the screen will be cleared on exit. This may be used alone, without other options.</dd>
<dt><i>DIALOG_VARS.exit_label</dt>
<dd> This corresponds to the command-line option &quot;</i><code>&#8211;exit-label string</code>&quot;. The given string overrides the label used for &quot;EXIT&quot; buttons.</dd>
<dt><i>DIALOG_VARS.extra_button</dt>
<dd> This corresponds to the command-line option &quot;</i><code>&#8211;extra-button</code>&quot;. If true, some widgets show an extra button, between &quot;OK&quot; and &quot;Cancel&quot; buttons.</dd>
<dt><i>DIALOG_VARS.extra_label</dt>
<dd> This corresponds to the command-line option &quot;</i><code>&#8211;extra-label</code> <i>string</i>&quot;. The given string overrides the label used for &quot;Extra&quot; buttons. Note: for inputmenu widgets, this defaults to &quot;Rename&quot;.</dd>
<dt><i>DIALOG_VARS.formitem_type</dt>
<dd> This is set by the command-line option &quot;</i><code>&#8211;passwordform</code>&quot; to tell the form widget that its text fields should be treated like password widgets.</dd>
<dt><i>DIALOG_VARS.help_button</dt>
<dd> This corresponds to the command-line option &quot;</i><code>&#8211;help-button</code>&quot;. If true, some widgets show a help-button after &quot;OK&quot; and &quot;Cancel&quot; buttons, i.e., in checklist, radiolist and menu boxes. If <code>&#8211;item-help</code> is also given, on exit the return status will be the same as for the &quot;OK&quot; button, and the item-help text will be written to <code>dialog</code>&#8216;s output after the token &quot;HELP&quot;. Otherwise, the return status will indicate that the Help button was pressed, and no message printed.</dd>
<dt><i>DIALOG_VARS.help_file</dt>
<dd> This corresponds to the command-line option &quot;</i><code>&#8211;hfile</code> <i>string</i>&quot;. The given filename is passed to <code>dialog_helpfile</code> when the user presses F1.</dd>
<dt><i>DIALOG_VARS.help_label</dt>
<dd> This corresponds to the command-line option &quot;</i><code>&#8211;help-label</code> <i>string</i>&quot;. The given string overrides the label used for &quot;Help&quot; buttons.</dd>
<dt><i>DIALOG_VARS.help_line</dt>
<dd> This corresponds to the command-line option &quot;</i><code>&#8211;hline</code> <i>string</i>&quot;. The given string is displayed in the bottom of dialog windows, like a subtitle.</dd>
<dt><i>DIALOG_VARS.help_status</dt>
<dd> This corresponds to the command-line option &quot;</i><code>&#8211;help-status</code>&quot;. If true, and the the help-button is selected, writes the checklist or radiolist information after the item-help &quot;HELP&quot; information. This can be used to reconstruct the state of a checklist after processing the help request.</dd>
<dt><i>DIALOG_VARS.input_length</dt>
<dd> This is nonzero if DIALOG_VARS.input_result</i> is allocated, versus being a pointer to the user&#8217;s local variables.</dd>
<dt><i>DIALOG_VARS.input_menu</dt>
<dd> This flag is set to denote whether the menubox widget implements a menu versus a inputmenu widget.</dd>
<dt>DIALOG_VARS.input_result</dt>
<dd> This may be either a user-supplied buffer, or a buffer dynamically allocated by the library, depending on DIALOG_VARS.input_length</i>:</dd>
<dl>
<dl>
<dt>&bull;</dt>
<dd> If <i>DIALOG_VARS.input_length</i> is zero, this is a pointer to user buffer (on the stack, or static). The buffer size is assumed to be <code>MAX_LEN</code>, which is defined in <i>&lt;dialog.h&gt;</i>.</dd>
<dt>&bull;</dt>
<dd> When <i>DIALOG_VARS.input_length</i> is nonzero, this is a dynamically-allocated buffer used by the widgets to return printable results to the calling application.</dd></dl>
</dl>
<dt>
</dt><dd> Certain widgets copy a result to this buffer. If the pointer is NULL, or if the length is insufficient for the result, then the <code>dialog</code> library allocates a buffer which is large enough, and sets <i>DIALOG_VARS.input_length</i>. Callers should check for this case if they have supplied their own buffer.</dd>
<dt><i>DIALOG_VARS.insecure</dt>
<dd> This corresponds to the command-line option &quot;</i><code>&#8211;insecure</code>&quot;. If true, make the password widget friendlier but less secure, by echoing asterisks for each character.</dd>
<dt><i>DIALOG_VARS.in_helpfile</dt>
<dd> This variable is used to prevent </i><code>dialog_helpfile</code> from showing anything, e.g., if F1 were pressed within a help-file display.</dd>
<dt><i>DIALOG_VARS.item_help</dt>
<dd> This corresponds to the command-line option &quot;</i><code>&#8211;item-help</code>&quot;. If true, interpret the tags data for checklist, radiolist and menu boxes adding a column whose text is displayed in the bottom line of the screen, for the currently selected item.</dd>
<dt><i>DIALOG_VARS.keep_tite</dt>
<dd> This is set by the command-line option &quot;</i><code>&#8211;keep-tite</code>&quot; to tell <code>dialog</code> to not attempt to cancel the terminal initialization (termcap <i>ti</i>/<i>te</i>) sequences which correspond to xterm&#8217;s alternate-screen switching. Normally <code>dialog</code> does this to avoid flickering when run several times in a script.</dd>
<dt><i>DIALOG_VARS.keep_window</dt>
<dd> This corresponds to the command-line option &quot;</i><code>&#8211;keep-window</code>&quot;. If true, do not remove/repaint the window on exit. This is useful for keeping the window contents visible when several widgets are run in the same process. Note that curses will clear the screen when starting a new process.</dd>
<dt><i>DIALOG_VARS.last_key</dt>
<dd> This corresponds to the command-line option &quot;</i><code>&#8211;last-key</code>&quot;.</dd>
<dt><i>DIALOG_VARS.max_input</dt>
<dd> This corresponds to the command-line option &quot;</i><code>&#8211;max-input</code> <i>size</i>&quot;. Limit input strings to the given size. If not specified, the limit is 2048.</dd>
<dt><i>DIALOG_VARS.no_items</dt>
<dd> This corresponds to the command-line option &quot;</i><code>&#8211;no-items</code>&quot;. Some widgets (checklist, inputmenu, radiolist, menu) display a list with two columns (a &quot;tag&quot; and &quot;item&quot;, i.e., &quot;description&quot;). This tells <code>dialog</code> to read shorter rows from data, omitting the &quot;list&quot;.</dd>
<dt><i>DIALOG_VARS.no_label</dt>
<dd> This corresponds to the command-line option &quot;</i><code>&#8211;no-label</code> <i>string</i>&quot;. The given string overrides the label used for &quot;No&quot; buttons.</dd>
<dt><i>DIALOG_VARS.no_lines</dt>
<dd> This corresponds to the command-line option &quot;</i><code>&#8211;no-lines</code>. It suppresses line-drawing. See <i>DIALOG_VARS.ascii_lines</i>.</dd>
<dt><i>DIALOG_VARS.no_nl_expand</dt>
<dd> This corresponds to the command-line option &quot;</i><code>&#8211;no-nl-expand</code>&quot;. If false, <code>dlg_trim_string</code> converts literal &quot;
&quot; substrings in a message into newlines.</dd>
<dt><i>DIALOG_VARS.no_tags</dt>
<dd> This corresponds to the command-line option &quot;</i><code>&#8211;no-tags</code>&quot;. Some widgets (checklist, inputmenu, radiolist, menu) display a list with two columns (a &quot;tag&quot; and &quot;item&quot;, also known as &quot;description&quot;). The tag is useful for scripting, but may not help the user. The <code>&#8211;no-tags</code> option (from Xdialog) may be used to suppress the column of tags from the display.</dd>
<dt>
</dt><dd> Normally <code>dialog</code> allows you to quickly move to entries on the displayed list, by matching a single character to the first character of the tag. When the <code>&#8211;no-tags</code> option is given, <code>dialog</code> matches against the first character of the description. In either case, the matchable character is highlighted.</dd>
<dt>
</dt><dd> Here is a table showing how the no_tags and no_items values interact: </dd>
<table>
<tr VALIGN=top>
<td>Widget</td>
<td>Fields Shown</td>
<td>Fields Read</td>
<td>.no_items</td>
<td>.no_tags
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>buildlist</td>
<td>item</td>
<td>tag,item</td>
<td ALIGN=center>0</td>
<td ALIGN=center>1
</td>
</tr>
<tr VALIGN=top>
<td>buildlist</td>
<td>tag</td>
<td>tag</td>
<td ALIGN=center>1</td>
<td ALIGN=center>0*
</td>
</tr>
<tr VALIGN=top>
<td>buildlist</td>
<td>tag</td>
<td>tag</td>
<td ALIGN=center>1</td>
<td ALIGN=center>1
</td>
</tr>
<tr VALIGN=top>
<td>checklist</td>
<td>tag,item</td>
<td>tag,item</td>
<td ALIGN=center>0</td>
<td ALIGN=center>0
</td>
</tr>
<tr VALIGN=top>
<td>checklist</td>
<td>item</td>
<td>tag,item</td>
<td ALIGN=center>0</td>
<td ALIGN=center>1
</td>
</tr>
<tr VALIGN=top>
<td>checklist</td>
<td>tag</td>
<td>tag</td>
<td ALIGN=center>1</td>
<td ALIGN=center>0
</td>
</tr>
<tr VALIGN=top>
<td>checklist</td>
<td>tag</td>
<td>tag</td>
<td ALIGN=center>1</td>
<td ALIGN=center>1
</td>
</tr>
<tr VALIGN=top>
<td>inputmenu</td>
<td>tag,item</td>
<td>tag,item</td>
<td ALIGN=center>0</td>
<td ALIGN=center>0
</td>
</tr>
<tr VALIGN=top>
<td>inputmenu</td>
<td>item</td>
<td>tag,item</td>
<td ALIGN=center>0</td>
<td ALIGN=center>1
</td>
</tr>
<tr VALIGN=top>
<td>inputmenu</td>
<td>tag</td>
<td>tag</td>
<td ALIGN=center>1</td>
<td ALIGN=center>0
</td>
</tr>
<tr VALIGN=top>
<td>inputmenu</td>
<td>tag</td>
<td>tag</td>
<td ALIGN=center>1</td>
<td ALIGN=center>1
</td>
</tr>
<tr VALIGN=top>
<td>menu</td>
<td>tag,item</td>
<td>tag,item</td>
<td ALIGN=center>0</td>
<td ALIGN=center>0
</td>
</tr>
<tr VALIGN=top>
<td>menu</td>
<td>item</td>
<td>tag,item</td>
<td ALIGN=center>0</td>
<td ALIGN=center>1
</td>
</tr>
<tr VALIGN=top>
<td>menu</td>
<td>tag</td>
<td>tag</td>
<td ALIGN=center>1</td>
<td ALIGN=center>0
</td>
</tr>
<tr VALIGN=top>
<td>menu</td>
<td>tag</td>
<td>tag</td>
<td ALIGN=center>1</td>
<td ALIGN=center>1
</td>
</tr>
<tr VALIGN=top>
<td>radiolist</td>
<td>tag,item</td>
<td>tag,item</td>
<td ALIGN=center>0</td>
<td ALIGN=center>0
</td>
</tr>
<tr VALIGN=top>
<td>radiolist</td>
<td>item</td>
<td>tag,item</td>
<td ALIGN=center>0</td>
<td ALIGN=center>1
</td>
</tr>
<tr VALIGN=top>
<td>radiolist</td>
<td>tag</td>
<td>tag</td>
<td ALIGN=center>1</td>
<td ALIGN=center>0
</td>
</tr>
<tr VALIGN=top>
<td>radiolist</td>
<td>tag</td>
<td>tag</td>
<td ALIGN=center>1</td>
<td ALIGN=center>1
</td>
</tr>
<tr VALIGN=top>
<td>treeview</td>
<td>item</td>
<td>tag,item</td>
<td ALIGN=center>0</td>
<td ALIGN=center>0*
</td>
</tr>
<tr VALIGN=top>
<td>treeview</td>
<td>item</td>
<td>tag,item</td>
<td ALIGN=center>0</td>
<td ALIGN=center>1
</td>
</tr>
<tr VALIGN=top>
<td>treeview</td>
<td>tag</td>
<td>tag</td>
<td ALIGN=center>1</td>
<td ALIGN=center>0*
</td>
</tr>
<tr VALIGN=top>
<td>treeview</td>
<td>tag</td>
<td>tag</td>
<td ALIGN=center>1</td>
<td ALIGN=center>1
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
</td>
</tr>
</table>
<dl>
<dl>
<dt>*</dt>
<dd> Xdialog does not display the tag column for the analogous buildlist and treeview widgets. <code>Dialog</code> does the same on the command-line. However the library interface defaults to displaying the tag column. Your application can enable or disable the tag column as needed for each widget.</dd></dl>
</dl>
<dt><i>DIALOG_VARS.nocancel</dt>
<dd> This corresponds to the command-line option &quot;</i><code>&#8211;no-cancel</code>&quot;. If true, suppress the &quot;Cancel&quot; button in checklist, inputbox and menu box modes. A script can still test if the user pressed the ESC key to cancel to quit.</dd>
<dt><i>DIALOG_VARS.nocollapse</dt>
<dd> This corresponds to the command-line option &quot;</i><code>&#8211;no-collapse</code>&quot;. Normally <code>dialog</code> converts tabs to spaces and reduces multiple spaces to a single space for text which is displayed in a message boxes, etc. It true, that feature is disabled. Note that <code>dialog</code> will still wrap text, subject to the <code>&#8211;cr-wrap</code> option.</dd>
<dt><i>DIALOG_VARS.nook</dt>
<dd> This corresponds to the command-line option &quot;</i><code>&#8211;nook</code>. <code>Dialog</code> will suppress the &quot;ok&quot; (or &quot;yes&quot;) button from the widget.</dd>
<dt><i>DIALOG_VARS.ok_label</dt>
<dd> This corresponds to the command-line option &quot;</i><code>&#8211;ok-label</code> <i>string</i>&quot;. The given string overrides the label used for &quot;OK&quot; buttons.</dd>
<dt><i>DIALOG_VARS.print_siz</dt>
<dd> This corresponds to the command-line option &quot;</i><code>&#8211;print-size</code>&quot;. If true, each widget prints its size to <code>dialog</code>&#8216;s output when it is invoked.</dd>
<dt><i>DIALOG_VARS.quoted</dt>
<dd> This corresponds to the command-line option &quot;</i><code>&#8211;quoted</code>.</dd>
<dt><i>DIALOG_VARS.separate_output</dt>
<dd> This corresponds to the command-line option &quot;</i><code>&#8211;separate-output</code>&quot;. If true, checklist widgets output result one line at a time, with no quoting. This facilitates parsing by another program.</dd>
<dt><i>DIALOG_VARS.single_quoted</dt>
<dd> This corresponds to the command-line option &quot;</i><code>&#8211;single-quoted</code>&quot;. If true, Use single-quoting as needed (and no quotes if unneeded) for the output of checklist&#8217;s as well as the item-help text. If this option is not set, <code>dialog</code> uses double quotes around each item. The latter requires occasional use of backslashes to make the output useful in shell scripts.</dd>
<dt><i>DIALOG_VARS.size_err</dt>
<dd> This corresponds to the command-line option &quot;</i><code>&#8211;size-err</code>&quot;. If true, check the resulting size of a dialog box before trying to use it, printing the resulting size if it is larger than the screen. (This option is obsolete, since all new-window calls are checked).</dd>
<dt><i>DIALOG_VARS.sleep_secs</dt>
<dd> This corresponds to the command-line option &quot;</i><code>&#8211;sleep</code> <i>secs</i>&quot;. This option is implemented in the main program, not the library. If nonzero, this is the number of seconds after to delay after processing a dialog box.</dd>
<dt><i>DIALOG_VARS.tab_correct</dt>
<dd> This corresponds to the command-line option &quot;</i><code>&#8211;tab-correct</code>&quot;. If true, convert each tab character of the text to one or more spaces. Otherwise, tabs are rendered according to the curses library&#8217;s interpretation.</dd>
<dt><i>DIALOG_VARS.time_format</dt>
<dd> This corresponds to the command-line option &quot;</i><code>&#8211;time-format</code> <i>string</i>&quot;. If the host provides <code>strftime</code>, and the value is nonnull, the timebox widget uses this to format its output.</dd>
<dt><i>DIALOG_VARS.timeout_secs</dt>
<dd> This corresponds to the command-line option &quot;</i><code>&#8211;timeout</code> <i>secs</i>&quot;. If nonzero, timeout input requests (exit with error code) if no user response within the given number of seconds.</dd>
<dt><i>DIALOG_VARS.title</dt>
<dd> This corresponds to the command-line option &quot;</i><code>&#8211;title</code> <i>title</i>&quot;. Specifies a <i>title</i> string to be displayed at the top of the dialog box.</dd>
<dt><i>DIALOG_VARS.trim_whitespace</dt>
<dd> This corresponds to the command-line option &quot;</i><code>&#8211;trim</code>&quot;. If true, eliminate leading blanks, trim literal newlines and repeated blanks from message text.</dd>
<dt><i>DIALOG_VARS.visit_items</dt>
<dd> This corresponds to the command-line option &quot;</i><code>&#8211;visit-items</code>&quot;. Modify the tab-traversal of the list-oriented widgets (buildlist, checklist, radiobox, menubox, inputmenu, and treeview) to include the list of items as one of the states. This is useful as a visual aid, i.e., the cursor position helps some users.</dd>
<dt><i>DIALOG_VARS.yes_label</dt>
<dd> This corresponds to the command-line option &quot;</i><code>&#8211;yes-label</code> <i>string</i>&quot;. The given string overrides the label used for &quot;Yes&quot; buttons.</dd></dl>
<h2>WIDGETS</h2>
<p> Functions that implement major functionality for the command-line <code>dialog</code> program, e.g., widgets, have names beginning &quot;<i>dialog_</i>&quot;. </p>
<p> All dialog boxes have at least three parameters:</p>
<dl>
<dt><i>title</i></dt>
<dd> the caption for the box, shown on its top border.</dd>
<dt><i>height</i></dt>
<dd> the height of the dialog box.</dd>
<dt><i>width</i></dt>
<dd> the width of the dialog box.</dd></dl>
<p> Other parameters depend on the box type.</p>
<dl>
<dt><code>dialog_buildlist</dt>
<dd> implements the &quot;&#8211;buildlist</code>&quot; option.</dd>
<dl>
<dl>
<dt><code>const char * </code><i>title</i></dt>
<dd> is the title on the top of the widget.</dd>
<dt><code>const char * </code><i>cprompt</i></dt>
<dd> is the prompt text shown within the widget.</dd>
<dt><code>int </code><i>height</i></dt>
<dd> is the desired height of the box. If zero, the height is adjusted to use the available screen size.</dd>
<dt><code>int </code><i>width</i></dt>
<dd> is the desired width of the box. If zero, the height is adjusted to use the available screen size.</dd>
<dt><code>int </code><i>list_height</i></dt>
<dd> is the minimum height to reserve for displaying the list. If zero, it is computed based on the given <i>height</i> and <i>width</i>.</dd>
<dt><code>int </code><i>item_no</i></dt>
<dd> is the number of rows in <i>items</i>.</dd>
<dt><code>char ** </code><i>items</i></dt>
<dd> is an array of strings which is viewed either as a list of rows</dd>
<dl>
<dt>
</dt><dd> <i>tag item status </i></dd></dl>
<dt>
</dt><dd> or</dd>
<dl>
<dt>
</dt><dd> <i>tag item status help</i></dd></dl>
<dt>
</dt><dd> depending on whether <code>dialog_vars.item_help</code> is set.</dd>
<dt><code>int </code><i>order_mode</i></dt>
<dd> is reserved for future enhancements</dd></dl>
</dl>
<dt><code>dialog_calendar</dt>
<dd> implements the &quot;&#8211;calendar</code>&quot; option.</dd>
<dl>
<dl>
<dt><code>const char * </code><i>title</i></dt>
<dd> is the title on the top of the widget.</dd>
<dt><code>const char * </code><i>subtitle</i></dt>
<dd> is the prompt text shown within the widget.</dd>
<dt><code>int </code><i>height</i></dt>
<dd> is the height excluding the fixed-height calendar grid.</dd>
<dt><code>int </code><i>width</i></dt>
<dd> is the overall width of the box, which is adjusted up to the calendar grid&#8217;s minimum width if needed.</dd>
<dt><code>int </code><i>day</i></dt>
<dd> is the initial day of the week shown, counting zero as Sunday. If the value is negative, the current day of the week is used.</dd>
<dt><code>int </code><i>month</i></dt>
<dd> is the initial month of the year shown, counting one as January. If the value is negative, the current month of the year is used.</dd>
<dt><code>int </code><i>year</i></dt>
<dd> is the initial year shown. If the value is negative, the current year is used.</dd></dl>
</dl>
<dt><code>dialog_checklist</dt>
<dd> implements the &quot;&#8211;checklist</code>&quot; and &quot;<code>&#8211;radiolist</code>&quot; options depending on the <i>flag</i> parameter.</dd>
<dl>
<dl>
<dt><code>const char * </code><i>title</i></dt>
<dd> is the title on the top of the widget.</dd>
<dt><code>const char * </code><i>cprompt</i></dt>
<dd> is the prompt text shown within the widget.</dd>
<dt><code>int </code><i>height</i></dt>
<dd> is the desired height of the box. If zero, the height is adjusted to use the available screen size.</dd>
<dt><code>int </code><i>width</i></dt>
<dd> is the desired width of the box. If zero, the height is adjusted to use the available screen size.</dd>
<dt><code>int </code><i>list_height</i></dt>
<dd> is the minimum height to reserve for displaying the list. If zero, it is computed based on the given <i>height</i> and <i>width</i>.</dd>
<dt><code>int </code><i>item_no</i></dt>
<dd> is the number of rows in <i>items</i>.</dd>
<dt><code>int </code><i>items</i></dt>
<dd> is an array of strings which is viewed either as a list of rows</dd>
<dl>
<dt>
</dt><dd> <i>tag item status </i></dd></dl>
<dt>
</dt><dd> or</dd>
<dl>
<dt>
</dt><dd> <i>tag item status help</i></dd></dl>
<dt>
</dt><dd> depending on whether <code>dialog_vars.item_help</code> is set.</dd>
<dt>flag</dt>
<dd> is either <i>FLAG_CHECK</i>, for checklists, or <i>FLAG_RADIO</i> for radiolists.</dd></dl>
</dl>
<dt><code>dialog_dselect</dt>
<dd> implements the &quot;&#8211;dselect</code>&quot; option.</dd>
<dl>
<dl>
<dt><code>const char * </code><i>title</i></dt>
<dd> is the title on the top of the widget.</dd>
<dt><code>const char * </code><i>path</i></dt>
<dd> is the preselected value to show in the input-box, which is used also to set the directory- and file-windows.</dd>
<dt><code>int </code><i>height</i></dt>
<dd> is the height excluding the minimum needed to show the dialog box framework. If zero, the height is based on the screen size.</dd>
<dt><code>int </code><i>width</i></dt>
<dd> is the desired width of the box. If zero, the height is based on the screen size.</dd></dl>
</dl>
<dt><code>dialog_editbox</dt>
<dd> implements the &quot;&#8211;editbox</code>&quot; option.</dd>
<dl>
<dl>
<dt><code>const char * </code><i>title</i></dt>
<dd> is the title on the top of the widget.</dd>
<dt><code>const char * </code><i>file</i></dt>
<dd> is the name of the file from which to read.</dd>
<dt><code>int </code><i>height</i></dt>
<dd> is the desired height of the box. If zero, the height is adjusted to use the available screen size.</dd>
<dt><code>int </code><i>width</i></dt>
<dd> is the desired width of the box. If zero, the height is adjusted to use the available screen size.</dd></dl>
</dl>
<dt><code>dialog_form</dt>
<dd> implements the &quot;&#8211;form</code>&quot; option.</dd>
<dl>
<dl>
<dt><code>const char * </code><i>title</i></dt>
<dd> is the title on the top of the widget.</dd>
<dt><code>const char * </code><i>cprompt</i></dt>
<dd> is the prompt text shown within the widget.</dd>
<dt><code>int </code><i>height</i></dt>
<dd> is the desired height of the box. If zero, the height is adjusted to use the available screen size.</dd>
<dt><code>int </code><i>width</i></dt>
<dd> is the desired width of the box. If zero, the height is adjusted to use the available screen size.</dd>
<dt><code>int </code><i>form_height</i></dt>
<dd> is the minimum height to reserve for displaying the list. If zero, it is computed based on the given <i>height</i> and <i>width</i>.</dd>
<dt><code>int </code><i>item_no</i></dt>
<dd> is the number of rows in <i>items</i>.</dd>
<dt><code>int </code><i>items</i></dt>
<dd> is an array of strings which is viewed either as a list of rows</dd>
<dl>
<dt>
</dt><dd> <i>Name NameY NameX Text TextY TextX FLen ILen</i></dd></dl>
<dt>
</dt><dd> or</dd>
<dl>
<dt>
</dt><dd> <i>Name NameY NameX Text TextY TextX FLen ILen Help</i></dd></dl>
<dt>
</dt><dd> depending on whether <code>dialog_vars.item_help</code> is set.</dd></dl>
</dl>
<dt><code>dialog_fselect</dt>
<dd> implements the &quot;&#8211;fselect</code>&quot; option.</dd>
<dl>
<dl>
<dt><code>const char * </code><i>title</i></dt>
<dd> is the title on the top of the widget.</dd>
<dt><code>const char * </code><i>path</i></dt>
<dd> is the preselected value to show in the input-box, which is used also to set the directory- and file-windows.</dd>
<dt><code>int </code><i>height</i></dt>
<dd> is the height excluding the minimum needed to show the dialog box framework. If zero, the height is based on the screen size.</dd>
<dt><code>int </code><i>width</i></dt>
<dd> is the desired width of the box. If zero, the height is based on the screen size.</dd></dl>
</dl>
<dt><code>dialog_gauge</dt>
<dd> implements the &quot;&#8211;gauge</code>&quot; option. Alternatively, a simpler or customized gauge widget can be setup using <code>dlg_allocate_gauge</code>, <code>dlg_update_gauge</code> and <code>dlg_free_gauge</code>.</dd>
<dl>
<dl>
<dt><code>const char * </code><i>title</i></dt>
<dd> is the title on the top of the widget.</dd>
<dt><code>const char * </code><i>cprompt</i></dt>
<dd> is the prompt text shown within the widget.</dd>
<dt><code>int </code><i>height</i></dt>
<dd> is the desired height of the box. If zero, the height is based on the screen size.</dd>
<dt><code>int </code><i>width</i></dt>
<dd> is the desired width of the box. If zero, the height is based on the screen size.</dd>
<dt><code>int </code><i>percent</i></dt>
<dd> is the percentage to show in the progress bar.</dd></dl>
</dl>
<dt><code>dialog_inputbox</dt>
<dd> implements the &quot;&#8211;inputbox</code>&quot; or &quot;<code>&#8211;password</code>&quot; option, depending on the value of <i>password</i>.</dd>
<dl>
<dl>
<dt><code>const char * </code><i>title</i></dt>
<dd> is the title on the top of the widget.</dd>
<dt><code>const char * </code><i>cprompt</i></dt>
<dd> is the prompt text shown within the widget.</dd>
<dt><code>int </code><i>height</i></dt>
<dd> is the desired height of the box. If zero, the height is based on the screen size.</dd>
<dt><code>int </code><i>width</i></dt>
<dd> is the desired width of the box. If zero, the height is based on the screen size.</dd>
<dt><code>const char * </code><i>init</i></dt>
<dd> is the initial value of the input box, whose length is taken into account when auto-sizing the width of the dialog box.</dd>
<dt><code>int </code><i>password</i></dt>
<dd> if true, causes typed input to be echoed as asterisks.</dd></dl>
</dl>
<dt><code>dialog_helpfile</dt>
<dd> implements the &quot;&#8211;hfile</code>&quot; option.</dd>
<dl>
<dl>
<dt><code>const char * </code><i>title</i></dt>
<dd> is the title on the top of the widget.</dd>
<dt><code>const char * </code><i>file</i></dt>
<dd> is the name of a file containing the text to display. This function is internally bound to F1 (function key &quot;1&quot;), passing <code>dialog_vars.help_file</code> as a parameter. The <code>dialog</code> program sets that variable when the <code>&#8211;hfile</code> option is given.</dd>
<dt><code>int </code><i>height</i></dt>
<dd> is the desired height of the box. If zero, the height is based on the screen size.</dd>
<dt><code>int </code><i>width</i></dt>
<dd> is the desired width of the box. If zero, the height is based on the screen size.</dd></dl>
</dl>
<dt><code>dialog_menu</dt>
<dd> implements the &quot;&#8211;menu</code>&quot; or &quot;<code>&#8211;inputmenu</code>&quot; option depending on whether <code>dialog_vars.input_menu</code> is set.</dd>
<dl>
<dl>
<dt><code>const char * </code><i>title</i></dt>
<dd> is the title on the top of the widget.</dd>
<dt><code>const char * </code><i>cprompt</i></dt>
<dd> is the prompt text shown within the widget.</dd>
<dt><code>int </code><i>height</i></dt>
<dd> is the desired height of the box. If zero, the height is based on the screen size.</dd>
<dt><code>int </code><i>width</i></dt>
<dd> is the desired width of the box. If zero, the height is based on the screen size.</dd>
<dt><code>int </code><i>menu_height</i></dt>
<dd> is the minimum height to reserve for displaying the list. If zero, it is computed based on the given <i>height</i> and <i>width</i>.</dd>
<dt><code>int </code><i>item_no</i></dt>
<dd> is the number of rows in <i>items</i>.</dd>
<dt><code>int </code><i>items</i></dt>
<dd> is an array of strings which is viewed either as a list of rows</dd>
<dl>
<dt>
</dt><dd> <i>tag item</i></dd></dl>
<dt>
</dt><dd> or</dd>
<dl>
<dt>
</dt><dd> <i>tag item help</i></dd></dl>
<dt>
</dt><dd> depending on whether <code>dialog_vars.item_help</code> is set.</dd></dl>
</dl>
<dt><code>dialog_mixedform</dt>
<dd> implements the &quot;&#8211;mixedform</code>&quot; option.</dd>
<dl>
<dl>
<dt><code>const char * </code><i>title</i></dt>
<dd> is the title on the top of the widget.</dd>
<dt><code>const char * </code><i>cprompt</i></dt>
<dd> is the prompt text shown within the widget.</dd>
<dt><code>int </code><i>height</i></dt>
<dd> is the desired height of the box. If zero, the height is adjusted to use the available screen size.</dd>
<dt><code>int </code><i>width</i></dt>
<dd> is the desired width of the box. If zero, the height is adjusted to use the available screen size.</dd>
<dt><code>int </code><i>form_height</i></dt>
<dd> is the minimum height to reserve for displaying the list. If zero, it is computed based on the given <i>height</i> and <i>width</i>.</dd>
<dt><code>int </code><i>item_no</i></dt>
<dd> is the number of rows in <i>items</i>.</dd>
<dt><code>int </code><i>items</i></dt>
<dd> is an array of strings which is viewed either as a list of rows</dd>
<dl>
<dt>
</dt><dd> <i>Name NameY NameX Text TextY TextX FLen ILen Ityp</i></dd></dl>
<dt>
</dt><dd> or</dd>
<dl>
<dt>
</dt><dd> <i>Name NameY NameX Text TextY TextX FLen ILen Ityp Help</i></dd></dl>
<dt>
</dt><dd> depending on whether <code>dialog_vars.item_help</code> is set.</dd></dl>
</dl>
<dt><code>dialog_mixedgauge</dt>
<dd> implements the &quot;&#8211;mixedgauge</code>&quot; option</dd>
<dl>
<dl>
<dt><code>const char * </code><i>title</i></dt>
<dd> is the title on the top of the widget.</dd>
<dt><code>const char * </code><i>cprompt</i></dt>
<dd> is the caption text shown within the widget.</dd>
<dt><code>int </code><i>height</i></dt>
<dd> is the desired height of the box. If zero, the height is based on the screen size.</dd>
<dt><code>int </code><i>width</i></dt>
<dd> is the desired width of the box. If zero, the height is based on the screen size.</dd>
<dt><code>int </code><i>percent</i></dt>
<dd> is the percentage to show in the progress bar.</dd>
<dt><code>int </code><i>item_no</i></dt>
<dd> is the number of rows in <i>items</i>.</dd>
<dt><code>int </code><i>items</i></dt>
<dd> is an array of strings which is viewed as a list of <i>tag</i> and <i>item</i> values. The <i>tag</i> values are listed, one per row, in the list at the top of the widget.</dd>
<dt>
</dt><dd> The <i>item</i> values are decoded: digits 0-9 are the following strings</dd>
<dl>
<dl>
<dt>0</dt>
<dd> Succeeded</dd>
<dt>1</dt>
<dd> Failed</dd>
<dt>2</dt>
<dd> Passed</dd>
<dt>3</dt>
<dd> Completed</dd>
<dt>4</dt>
<dd> Checked</dd>
<dt>5</dt>
<dd> Done</dd>
<dt>6</dt>
<dd> Skipped</dd>
<dt>7</dt>
<dd> In Progress</dd>
<dt>8</dt>
<dd> (blank)</dd>
<dt>9</dt>
<dd> N/A</dd></dl>
</dl>
<dt>
</dt><dd> A string with a leading &quot;-&quot; character is centered, marked with &quot;%&quot;. For example, &quot;-75&quot; is displayed as &quot;75%&quot;. Other strings are displayed as is.</dd></dl>
</dl>
<dt><code>dialog_msgbox</dt>
<dd> implements the &quot;&#8211;msgbox</code>&quot; or &quot;<code>&#8211;infobox</code>&quot; option depending on whether <i>pauseopt</i> is set.</dd>
<dl>
<dl>
<dt><code>const char * </code><i>title</i></dt>
<dd> is the title on the top of the widget.</dd>
<dt><code>const char * </code><i>cprompt</i></dt>
<dd> is the prompt text shown within the widget.</dd>
<dt><code>int </code><i>height</i></dt>
<dd> is the desired height of the box. If zero, the height is based on the screen size.</dd>
<dt><code>int </code><i>width</i></dt>
<dd> is the desired width of the box. If zero, the height is based on the screen size.</dd>
<dt><code>int </code><i>pauseopt</i></dt>
<dd> if true, an &quot;OK&quot; button will be shown, and the dialog will wait for it to complete. With an &quot;OK&quot; button, it is denoted a &quot;msgbox&quot;, without an &quot;OK&quot; button, it is denoted an &quot;infobox&quot;.</dd></dl>
</dl>
<dt><code>dialog_pause</dt>
<dd> implements the &quot;&#8211;pause</code>&quot; option.</dd>
<dl>
<dl>
<dt><code>const char * </code><i>title</i></dt>
<dd> is the title on the top of the widget.</dd>
<dt><code>int </code><i>height</i></dt>
<dd> is the desired height of the box. If zero, the height is based on the screen size.</dd>
<dt><code>int </code><i>width</i></dt>
<dd> is the desired width of the box. If zero, the height is based on the screen size.</dd>
<dt><code>int </code><i>seconds</i></dt>
<dd> is the timeout to use for the progress bar.</dd></dl>
</dl>
<dt><code>dialog_prgbox</dt>
<dd> implements the &quot;&#8211;prgbox</code>&quot; option.</dd>
<dl>
<dl>
<dt><code>const char * </code><i>title</i></dt>
<dd> is the title on the top of the widget.</dd>
<dt><code>const char * </code><i>cprompt</i></dt>
<dd> is the prompt text shown within the widget. If empty or null, no prompt is shown.</dd>
<dt><code>const char * </code><i>command</i></dt>
<dd> is the name of the command to execute.</dd>
<dt><code>int </code><i>height</i></dt>
<dd> is the desired height of the box. If zero, the height is based on the screen size.</dd>
<dt><code>int </code><i>width</i></dt>
<dd> is the desired width of the box. If zero, the height is based on the screen size.</dd>
<dt><code>int </code><i>pauseopt</i></dt>
<dd> if true, an &quot;OK&quot; button will be shown, and the dialog will wait for it to complete.</dd></dl>
</dl>
<dt><code>dialog_progressbox</dt>
<dd> implements the &quot;&#8211;progressbox</code>&quot; option.</dd>
<dl>
<dl>
<dt><code>const char * </code><i>title</i></dt>
<dd> is the title on the top of the widget.</dd>
<dt><code>const char * </code><i>cprompt</i></dt>
<dd> is the prompt text shown within the widget. If empty or null, no prompt is shown.</dd>
<dt><code>int </code><i>height</i></dt>
<dd> is the desired height of the box. If zero, the height is based on the screen size.</dd>
<dt><code>int </code><i>width</i></dt>
<dd> is the desired width of the box. If zero, the height is based on the screen size.</dd></dl>
</dl>
<dt><code>dialog_rangebox</dt>
<dd> implements the &quot;&#8211;rangebox</code>&quot; option.</dd>
<dl>
<dl>
<dt><code>const char * </code><i>title</i></dt>
<dd> is the title on the top of the widget.</dd>
<dt><code>const char * </code><i>cprompt</i></dt>
<dd> is the prompt text shown within the widget. If empty or null, no prompt is shown.</dd>
<dt><code>int </code><i>height</i></dt>
<dd> is the desired height of the widget. If zero, the height is based on the screen size.</dd>
<dt><code>int </code><i>width</i></dt>
<dd> is the desired width of the widget. If zero, the height is based on the screen size.</dd>
<dt><code>int </code><i>min_value</i></dt>
<dd> is the minimum value to allow.</dd>
<dt><code>int </code><i>max_value</i></dt>
<dd> is the maximum value to allow.</dd>
<dt><code>int </code><i>default_value</i></dt>
<dd> is the default value, if no change is made.</dd></dl>
</dl>
<dt><code>dialog_tailbox</dt>
<dd> implements the &quot;&#8211;tailbox</code>&quot; or &quot;<code>&#8211;tailboxbg</code>&quot; option depending on whether <i>bg_task</i> is set.</dd>
<dl>
<dl>
<dt><code>const char * </code><i>title</i></dt>
<dd> is the title on the top of the widget.</dd>
<dt><code>const char * </code><i>file</i></dt>
<dd> is the name of the file to display in the dialog.</dd>
<dt><code>int </code><i>height</i></dt>
<dd> is the desired height of the box. If zero, the height is based on the screen size.</dd>
<dt><code>int </code><i>width</i></dt>
<dd> is the desired width of the box. If zero, the height is based on the screen size.</dd>
<dt><code>int </code><i>bg_task</i></dt>
<dd> if true, the window is added to the callback list in <code>dialog_state</code>, and the application will poll for the window to be updated. Otherwise an &quot;OK&quot; button is added to the window, and it will be closed when the button is activated.</dd></dl>
</dl>
<dt><code>dialog_textbox</dt>
<dd> implements the &quot;&#8211;textbox</code>&quot; option.</dd>
<dl>
<dl>
<dt><code>const char * </code><i>title</i></dt>
<dd> is the title on the top of the widget.</dd>
<dt><code>const char * </code><i>file</i></dt>
<dd> is the name of the file to display in the dialog.</dd>
<dt><code>int </code><i>height</i></dt>
<dd> is the desired height of the box. If zero, the height is based on the screen size.</dd>
<dt><code>int </code><i>width</i></dt>
<dd> is the desired width of the box. If zero, the height is based on the screen size.</dd></dl>
</dl>
<dt><code>dialog_timebox</dt>
<dd> implements the &quot;&#8211;timebox</code>&quot; option.</dd>
<dl>
<dl>
<dt><code>const char * </code><i>title</i></dt>
<dd> is the title on the top of the widget.</dd>
<dt><code>const char * </code><i>subtitle</i></dt>
<dd> is the prompt text shown within the widget.</dd>
<dt><code>int </code><i>height</i></dt>
<dd> is the desired height of the box. If zero, the height is based on the screen size.</dd>
<dt><code>int </code><i>width</i></dt>
<dd> is the desired width of the box. If zero, the height is based on the screen size.</dd>
<dt><code>int </code><i>hour</i></dt>
<dd> is the initial hour shown. If the value is negative, the current hour is used. Returns DLG_EXIT_ERROR if the value specified is greater than or equal to 24.</dd>
<dt><code>int </code><i>minute</i></dt>
<dd> is the initial minute shown. If the value is negative, the current minute is used. Returns DLG_EXIT_ERROR if the value specified is greater than or equal to 60.</dd>
<dt><code>int </code><i>second</i></dt>
<dd> is the initial second shown. If the value is negative, the current second is used. Returns DLG_EXIT_ERROR if the value specified is greater than or equal to 60.</dd></dl>
</dl>
<dt><code>dialog_treeview</dt>
<dd> implements the &quot;&#8211;treeview</code>&quot; option.</dd>
<dl>
<dl>
<dt><code>const char * </code><i>title</i></dt>
<dd> is the title on the top of the widget.</dd>
<dt><code>const char * </code><i>cprompt</i></dt>
<dd> is the prompt text shown within the widget.</dd>
<dt><code>int </code><i>height</i></dt>
<dd> is the desired height of the box. If zero, the height is based on the screen size.</dd>
<dt><code>int </code><i>width</i></dt>
<dd> is the desired width of the box. If zero, the height is based on the screen size.</dd>
<dt><code>int </code><i>list_height</i></dt>
<dd> is the minimum height to reserve for displaying the list. If zero, it is computed based on the given <i>height</i> and <i>width</i>.</dd>
<dt><code>int </code><i>item_no</i></dt>
<dd> is the number of rows in <i>items</i>.</dd>
<dt><code>char ** </code><i>items</i></dt>
<dd> is the list of items, contain tag, name, and optionally help strings (if <code>dialog_vars.item_help</code> is set). The initial selection state for each item is also in this list.</dd>
<dt><code>int </code><i>flag</i></dt>
<dd>
</dd><dt>flag</dt>
<dd> is either <i>FLAG_CHECK</i>, for checklists (multiple selections), or <i>FLAG_RADIO</i> for radiolists (a single selection).</dd></dl>
</dl>
<dt><code>dialog_yesno</dt>
<dd> implements the &quot;&#8211;yesno</code>&quot; option.</dd>
<dl>
<dl>
<dt><code>const char * </code><i>title</i></dt>
<dd> is the title on the top of the widget.</dd>
<dt><code>const char * </code><i>cprompt</i></dt>
<dd> is the prompt text shown within the widget.</dd>
<dt><code>int </code><i>height</i></dt>
<dd> is the desired height of the box. If zero, the height is based on the screen size.</dd>
<dt><code>int </code><i>width</i></dt>
<dd> is the desired width of the box. If zero, the height is based on the screen size.</dd></dl>
</dl>
</dl>
<h2>UTILITY FUNCTIONS</h2>
<p> Most functions that implement lower-level functionality for the command-line <code>dialog</code> program or widgets, have names beginning &quot;<i>dlg_</i>&quot;. Bowing to longstanding usage, the functions that initialize the display and end it are named <i>init_dialog</i> and <i>end_dialog</i>. </p>
<p> The only non-widget function whose name begins with &quot;<i>dialog_</i>&quot; is <code>dialog_version</code>, which returns the version number of the library as a string. </p>
<p> Here is a brief summary of the utility functions and their parameters:</p>
<dl>
<dt><code>dlg_add_callback</code></dt>
<dd> Add a callback, used to allow polling input from multiple tailbox widgets.</dd>
<dl>
<dl>
<dt><code>DIALOG_CALLBACK *</code><i>p</i></dt>
<dd> contains the callback information.</dd></dl>
</dl>
<dt><code>dlg_add_callback_ref</code></dt>
<dd> Like <code>dlg_add_callback</code>, but passes a reference to the <code>DIALOG_CALLBACK</code> as well as a pointer to a cleanup function which will be called when the associated input ends.</dd>
<dl>
<dl>
<dt><code>DIALOG_CALLBACK **</code><i>p</i></dt>
<dd> points to the callback information. This is a reference to the pointer so that the caller&#8217;s pointer can be zeroed when input ends.</dd>
<dt><code>DIALOG_FREEBACK </code><i>func</i></dt>
<dd> function to call when input ends, e.g., to free caller&#8217;s additional data.</dd></dl>
</dl>
<dt><code>dlg_add_last_key</code></dt>
<dd> Report the last key entered by the user. This implements the <code>&#8211;last-key</code> command-line option, using <code>dialog_vars.last_key</code>.</dd>
<dl>
<dl>
<dt><code>int </code><i>mode</i></dt>
<dd> controls the way the last key report is separated from other results:</dd>
<dl>
<dl>
<dt>-2</dt>
<dd> (no separator)</dd>
<dt>-1</dt>
<dd> (separator after the key name)</dd>
<dt>0</dt>
<dd> (separator is optionally before the key name)</dd>
<dt>1</dt>
<dd> (same as -1)</dd></dl>
</dl>
</dl>
</dl>
<dt><code>dlg_add_quoted</code></dt>
<dd> Add a quoted string to the result buffer (see <code>dlg_add_result</code>). If no quotes are necessary, none are used. If <code>dialog_vars.single_quoted</code> is set, single-quotes are used. Otherwise, double-quotes are used.</dd>
<dl>
<dl>
<dt><code>char * </code><i>string</i></dt>
<dd> is the string to add.</dd></dl>
</dl>
<dt><code>dlg_add_result</code></dt>
<dd> Add a string to the result buffer <code>dialog_vars.input_result</code>.</dd>
<dl>
<dl>
<dt><code>char * </code><i>string</i></dt>
<dd> is the string to add.</dd></dl>
</dl>
<dt><code>dlg_add_separator</code></dt>
<dd> Add an output-separator to the result buffer <code>dialog_vars.input_result</code>. If <code>dialog_vars.output_separator</code> is set, use that. Otherwise, if <code>dialog_vars.separate_output</code> is set, use newline. If neither is set, use a space.</dd>
<dt><code>dlg_add_string</code></dt>
<dd> Add a quoted or unquoted string to the result buffer (see <code>dlg_add_quoted</code>) and <code>dlg_add_result</code>), according to whether <code>dialog_vars.quoted</code> is true.</dd>
<dl>
<dl>
<dt><code>char * </code><i>string</i></dt>
<dd> is the string to add.</dd></dl>
</dl>
<dt><code>dlg_align_columns</code></dt>
<dd> Copy and reformat an array of pointers to strings, aligning according to the column separator <code>dialog_vars.column_separator</code>. If no column separator is set, the array will be unmodified; otherwise it is copied and reformatted.</dd>
<dt>
</dt><dd> Caveat: This function is only implemented for 8-bit characters.</dd>
<dl>
<dl>
<dt><code>char **</code><i>target</i></dt>
<dd> This is the array to reformat. It points to the first string to modify.</dd>
<dt><code>int </code><i>per_row</i></dt>
<dd> This is the size of the struct for each row of the array.</dd>
<dt><code>int </code><i>num_rows</i></dt>
<dd> This is the number of rows in the array.</dd></dl>
</dl>
<dt><code>dlg_allocate_gauge</code></dt>
<dd> Allocates a gauge widget. Use <code>dlg_update_gauge</code> to display the result.</dd>
<dl>
<dl>
<dt><code>const char * </code><i>title</i></dt>
<dd> is the title string to display at the top of the widget.</dd>
<dt><code>const char * </code><i>cprompt</i></dt>
<dd> is the prompt text shown within the widget.</dd>
<dt><code>int </code><i>height</i></dt>
<dd> is the desired height of the box. If zero, the height is adjusted to use the available screen size.</dd>
<dt><code>int </code><i>width</i></dt>
<dd> is the desired width of the box. If zero, the height is adjusted to use the available screen size.</dd>
<dt><code>int </code><i>percent</i></dt>
<dd> is the percentage to show in the progress bar.</dd></dl>
</dl>
<dt><code>dlg_asciibox</code></dt>
<dd> returns its parameter transformed to the corresponding &quot;+&quot; or &quot;-&quot;, etc. for the line-drawing characters used in <code>dialog</code>. If the parameter is not a line-drawing or other special character such as ACS_DARROW, it returns 0.</dd>
<dl>
<dl>
<dt><code>chtype </code><i>ch</i></dt>
<dd> is the parameter, usually one of the <code>ACS_</code><i>xxx</i> constants.</dd></dl>
</dl>
<dt><code>dlg_attr_clear</code></dt>
<dd> Set window to the given attribute.</dd>
<dl>
<dl>
<dt><code>WINDOW * </code><i>win</i></dt>
<dd> is the window to update.</dd>
<dt><code>int </code><i>height</i></dt>
<dd> is the number of rows to update.</dd>
<dt><code>int </code><i>width</i></dt>
<dd> is the number of columns to update.</dd>
<dt><code>chtype </code><i>attr</i></dt>
<dd> is the attribute, e.g., <code>A_BOLD</code>.</dd></dl>
</dl>
<dt><code>dlg_auto_size</code></dt>
<dd> Automatically size the window used for a widget. If the given height or width are zero, justify the <i>prompt</i> text and return the actual limits.</dd>
<dl>
<dl>
<dt><code>const char * </code><i>title</i></dt>
<dd> is the title string to display at the top of the widget.</dd>
<dt><code>const char * </code><i>prompt</i></dt>
<dd> is the message text which will be displayed in the widget, used here to determine how large the widget should be.</dd>
<dt><code>int * </code><i>height</i></dt>
<dd> is the nominal height.</dd>
<dt><code>int * </code><i>width</i></dt>
<dd> is the nominal width.</dd>
<dt><code>int </code><i>boxlines</i></dt>
<dd> is the number of lines to reserve in the vertical direction.</dd>
<dt><code>int </code><i>mincols</i></dt>
<dd> is the minimum number of columns to use.</dd></dl>
</dl>
<dt><code>dlg_auto_sizefile</code></dt>
<dd> Like <code>dlg_auto_size</code>, but use a file contents to decide how large the widget should be.</dd>
<dl>
<dl>
<dt><code>const char * </code><i>title</i></dt>
<dd> is the title string to display at the top of the widget.</dd>
<dt><code>const char * </code><i>file</i></dt>
<dd> is the name of the file.</dd>
<dt><code>int * </code><i>height</i></dt>
<dd> is the nominal height. If it is -1, use the screen&#8217;s height (after subtracting <code>dialog_vars.begin_y</code> if <code>dialog_vars.begin_set</code> is true).</dd>
<dt><code>int * </code><i>width</i></dt>
<dd> is the nominal width. If it is -1, use the screen&#8217;s width (after subtracting <code>dialog_vars.begin_x</code> if <code>dialog_vars.begin_set</code> is true).</dd>
<dt><code>int </code><i>boxlines</i></dt>
<dd> is the number of lines to reserve on the screen for drawing boxes.</dd>
<dt><code>int </code><i>mincols</i></dt>
<dd> is the number of columns to reserve on the screen for drawing boxes.</dd></dl>
</dl>
<dt><code>dlg_beeping</code></dt>
<dd> If <code>dialog_vars.beep_signal</code> is nonzero, this calls <code>beep</code> once and sets <code>dialog_vars.beep_signal</code> to zero.</dd>
<dt><code>dlg_boxchar</code></dt>
<dd> returns its <code>chtype</code> parameter transformed as follows:</dd>
<dl>
<dl>
<dt>&bull;</dt>
<dd> if neither <code>dialog_vars.ascii_lines</code> nor <code>dialog_vars.no_lines</code> is set.</dd>
<dt>&bull;</dt>
<dd> if <code>dialog_vars.ascii_lines</code> is set, returns the corresponding &quot;+&quot; or &quot;-&quot;, etc. for the line-drawing characters used in <code>dialog</code>.</dd>
<dt>&bull;</dt>
<dd> otherwise, if <code>dialog_vars.no_lines</code> is set, returns a space for the line-drawing characters.</dd>
<dt>&bull;</dt>
<dd> if the parameter is not a line-drawing or other special character such as ACS_DARROW, it returns the parameter unchanged.</dd></dl>
</dl>
<dt><code>dlg_box_x_ordinate</code></dt>
<dd> returns a suitable x-ordinate (column) for a new widget. If <code>dialog_vars.begin_set</code> is 1, use <code>dialog_vars.begin_x</code>; otherwise center the widget on the screen (using the <i>width</i> parameter).</dd>
<dl>
<dl>
<dt><code>int </code><i>width</i></dt>
<dd> is the width of the widget.</dd></dl>
</dl>
<dt><code>dlg_box_y_ordinate</code></dt>
<dd> returns a suitable y-ordinate (row) for a new widget. If <code>dialog_vars.begin_set</code> is 1, use <code>dialog_vars.begin_y</code>; otherwise center the widget on the screen (using the <i>height</i> parameter).</dd>
<dl>
<dl>
<dt><code>int </code><i>height</i></dt>
<dd> is the height of the widget.</dd></dl>
</dl>
<dt><code>dlg_buildlist</code></dt>
<dd> This is an alternate interface to the <code>buildlist</code> widget which allows the application to read the list item states back directly without putting them in the output buffer.</dd>
<dl>
<dl>
<dt><code>const char * </code><i>title</i></dt>
<dd> is the title string to display at the top of the widget.</dd>
<dt><code>const char * </code><i>cprompt</i></dt>
<dd> is the prompt text shown within the widget.</dd>
<dt><code>int </code><i>height</i></dt>
<dd> is the desired height of the box. If zero, the height is adjusted to use the available screen size.</dd>
<dt><code>int </code><i>width</i></dt>
<dd> is the desired width of the box. If zero, the height is adjusted to use the available screen size.</dd>
<dt><code>int </code><i>list_height</i></dt>
<dd> is the minimum height to reserve for displaying the list. If zero, it is computed based on the given <i>height</i> and <i>width</i>.</dd>
<dt><code>int </code><i>item_no</i></dt>
<dd> is the number of rows in <i>items</i>.</dd>
<dt><code>DIALOG_LISTITEM * </code><i>items</i></dt>
<dd> is the list of items, contain tag, name, and optionally help strings (if <code>dialog_vars.item_help</code> is set). The initial selection state for each item is also in this list.</dd>
<dt><code>const char * </code><i>states</i></dt>
<dd> This is a list of characters to display for the given states. Normally a buildlist provides true (1) and false (0) values, which the widget displays as &quot;*&quot; and space, respectively. An application may set this parameter to an arbitrary null-terminated string. The widget determines the number of states from the length of this string, and will cycle through the corresponding display characters as the user presses the space-bar.</dd>
<dt><code>int </code><i>order_mode</i></dt>
<dd> is reserved for future enhancements</dd>
<dt><code>int * </code><i>current_item</i></dt>
<dd> The widget sets the referenced location to the index of the current display item (cursor) when it returns.</dd></dl>
</dl>
<dt><code>dlg_button_count</code></dt>
<dd> Count the buttons in the list.</dd>
<dl>
<dl>
<dt><code>const char ** </code><i>labels</i></dt>
<dd> is a list of (pointers to) button labels terminated by a null pointer.</dd></dl>
</dl>
<dt><code>dlg_button_layout</code></dt>
<dd> Make sure there is enough space for the buttons by computing the width required for their labels, adding margins and limiting based on the screen size.</dd>
<dl>
<dl>
<dt><code>const char ** </code><i>labels</i></dt>
<dd> is a list of (pointers to) button labels terminated by a null pointer.</dd>
<dt><code>int * </code><i>limit</i></dt>
<dd> the function sets the referenced <i>limit</i> to the width required for the buttons (limited by the screen size) if that is wider than the passed-in limit.</dd></dl>
</dl>
<dt><code>dlg_button_sizes</code></dt>
<dd> Compute the size of the button array in columns.</dd>
<dl>
<dl>
<dt><code>const char ** </code><i>labels</i></dt>
<dd> is a list of (pointers to) button labels terminated by a null pointer.</dd>
<dt><code>int </code><i>vertical</i></dt>
<dd> is true if the buttons are arranged in a column rather than a row.</dd>
<dt><code>int * </code><i>longest</i></dt>
<dd> Return the total number of columns in the referenced location.</dd>
<dt><code>int * </code><i>length</i></dt>
<dd> Return the longest button&#8217;s columns in the referenced location.</dd></dl>
</dl>
<dt><code>dlg_button_x_step</code></dt>
<dd> Compute the step-size needed between elements of the button array.</dd>
<dl>
<dl>
<dt><code>const char ** </code><i>labels</i></dt>
<dd> is a list of (pointers to) button labels terminated by a null pointer.</dd>
<dt><code>int </code><i>limit</i></dt>
<dd> is the maximum number of columns to allow for the buttons.</dd>
<dt><code>int * </code><i>gap</i></dt>
<dd> store the nominal gap between buttons in the referenced location. This is constrained to be at least one.</dd>
<dt><code>int * </code><i>margin</i></dt>
<dd> store the left+right total margins (for the list of buttons) in the referenced location.</dd>
<dt><code>int * </code><i>step</i></dt>
<dd> store the step-size in the referenced location.</dd></dl>
</dl>
<dt><code>dlg_button_to_char</code></dt>
<dd> Find the first uppercase character in the label, which we may use for an abbreviation. If the label is empty, return -1. If no uppercase character is found, return 0. Otherwise return the uppercase character.</dd>
<dt>
</dt><dd> Normally <code>dlg_draw_buttons</code> and <code>dlg_char_to_button</code> use the first uppercase character. However, they keep track of all of the labels and if the first has already been used in another label, they will continue looking for another uppercase character. This function does not have enough information to make that check.</dd>
<dl>
<dl>
<dt><code>const char * </code><i>label</i></dt>
<dd> is the label to test.</dd></dl>
</dl>
<dt><code>dlg_calc_list_width</code></dt>
<dd> Calculate the minimum width for the list, assuming none of the items are truncated.</dd>
<dl>
<dl>
<dt><code>int </code><i>item_no</i></dt>
<dd> is the number of <i>items</i>.</dd>
<dt><code>DIALOG_LISTITEM * </code><i>items</i></dt>
<dd> contains a <i>name</i> and <i>text</i> field, e.g., for checklists or radiobox lists. The function returns the sum of the widest columns needed for of each of these fields.</dd>
<dt>
</dt><dd> If <code>dialog_vars.no_items</code> is set, the <i>text</i> fields in the list are ignored.</dd></dl>
</dl>
<dt><code>dlg_calc_listh</code></dt>
<dd> Calculate new height and list_height values.</dd>
<dl>
<dl>
<dt><code>int * </code><i>height</i></dt>
<dd> on input, is the height without adding the list-height. On return, this contains the total list-height and is the actual widget&#8217;s height.</dd>
<dt><code>int * </code><i>list_height</i></dt>
<dd> on input, is the requested list-height. On return, this contains the number of rows available for displaying the list after taking into account the screen size and the <code>dialog_vars.begin_set</code> and <code>dialog_vars.begin_y</code> variables.</dd>
<dt><code>int </code><i>item_no</i></dt>
<dd> is the number of <i>items</i> in the list.</dd></dl>
</dl>
<dt><code>dlg_calc_listw</code></dt>
<dd> This function is obsolete, provided for library-compatibility. It is replaced by <code>dlg_calc_list_width</code>.</dd>
<dl>
<dl>
<dt><code>int </code><i>item_no</i></dt>
<dd> is the number of <i>items</i>.</dd>
<dt><code>char ** </code><i>items</i></dt>
<dd> is a list of character pointers.</dd>
<dt><code>int </code><i>group</i></dt>
<dd> is the number of items in each group, e.g., the second array index.</dd></dl>
</dl>
<dt><code>dlg_char_to_button</code></dt>
<dd> Given a list of button labels, and a character which may be the abbreviation for one, find it, if it exists. An abbreviation will be the first character which happens to be capitalized in the label. If the character is found, return its index within the list of <i>labels</i>. Otherwise, return <code>DLG_EXIT_UNKNOWN</code>.</dd>
<dl>
<dl>
<dt><code>int </code><i>ch</i></dt>
<dd> is the character to find.</dd>
<dt><code>const char ** </code><i>labels</i></dt>
<dd> is a list of (pointers to) button labels terminated by a null pointer.</dd></dl>
</dl>
<dt><code>dlg_checklist</code></dt>
<dd> This entrypoint provides the <code>&#8211;checklist</code> or &#8211;radiolist functionality without the limitations of <code>dialog</code>&#8216;s command-line syntax (compare to <code>dialog_checklist</code>).</dd>
<dl>
<dl>
<dt><code>const char * </code><i>title</i></dt>
<dd> is the title string to display at the top of the widget.</dd>
<dt><code>const char * </code><i>cprompt</i></dt>
<dd> is the prompt text shown within the widget.</dd>
<dt><code>int </code><i>height</i></dt>
<dd> is the desired height of the box. If zero, the height is adjusted to use the available screen size.</dd>
<dt><code>int </code><i>width</i></dt>
<dd> is the desired width of the box. If zero, the height is adjusted to use the available screen size.</dd>
<dt><code>int </code><i>list_height</i></dt>
<dd> is the minimum height to reserve for displaying the list. If zero, it is computed based on the given <i>height</i> and <i>width</i>.</dd>
<dt><code>int </code><i>item_no</i></dt>
<dd> is the number of <i>items</i>.</dd>
<dt><code>DIALOG_LISTITEM * </code><i>items</i></dt>
<dd> This is a list of the items to display in the checklist.</dd>
<dt><code>const char * </code><i>states</i></dt>
<dd> This is a list of characters to display for the given states. Normally a checklist provides true (1) and false (0) values, which the widget displays as &quot;*&quot; and space, respectively. An application may set this parameter to an arbitrary null-terminated string. The widget determines the number of states from the length of this string, and will cycle through the corresponding display characters as the user presses the space-bar.</dd>
<dt><code>int </code><i>flag</i></dt>
<dd> This is should be one of <code>FLAG_CHECK</code> or FLAG_RADIO, depending on whether the widget should act as a checklist or radiobox.</dd>
<dt><code>int * </code><i>current_item</i></dt>
<dd> The widget sets the referenced location to the index of the current display item (cursor) when it returns.</dd></dl>
</dl>
<dt><code>dlg_check_scrolled</code></dt>
<dd> given a function key (or other key that was mapped to a function key), check if it is one of the up/down scrolling functions: </dd>
<dl>
<dt>
</dt><dd> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>DLGK_PAGE_FIRST,</dd>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>DLGK_PAGE_LAST,</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>DLGK_GRID_UP,</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>DLGK_GRID_DOWN,</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>DLGK_PAGE_PREV or</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>DLGK_PAGE_NEXT.
</dl>
<dt>
</dt><dd> Some widgets use these key bindings for scrolling the prompt-text up and down, to allow for display in very small windows.</dd>
<dt>
</dt><dd> The function returns 0 (zero) if it finds one of these keys, and -1 if not.</dd>
<dl>
<dl>
<dt><code>int </code><i>key</i></dt>
<dd> is the function-key to check</dd>
<dt><code>int </code><i>last</i></dt>
<dd> is the number of lines which would be used to display the scrolled prompt in an arbitrarily tall window. It is used here to check limits for the <i>offset</i> value.</dd>
<dt><code>int </code><i>page</i></dt>
<dd> this is the available height for writing scrolled text, which is smaller than the window if it contains buttons.</dd>
<dt><code>bool * </code><i>show</i></dt>
<dd> on return, holds TRUE if <code>dlg_print_scrolled</code> should be used to redisplay the prompt text.</dd>
<dt><code>int * </code><i>offset</i></dt>
<dd> on entry, holds the starting line number (counting from zero) last used for <code>dlg_print_scrolled</code>. On return, holds the updated starting line number.</dd></dl>
</dl>
<dt><code>dlg_clear</code></dt>
<dd> Set window to the default <code>dialog</code> screen attribute. This is set in the rc-file with <code>screen_color</code>.</dd>
<dt><code>dlg_clr_result</code></dt>
<dd> Free storage used for the result buffer (<code>dialog_vars.input_result</code>). The corresponding pointer is set to NULL.</dd>
<dt><code>dlg_color_count</code></dt>
<dd> Return the number of colors that can be configured in <code>dialog</code>.</dd>
<dt><code>dlg_color_setup</code></dt>
<dd> Initialize the color pairs used in <code>dialog</code>.</dd>
<dt><code>dlg_count_argv</code></dt>
<dd> Count the entries in an argument vector.</dd>
<dl>
<dl>
<dt><code>argv</code></dt>
<dd> Points to the argument vector.</dd></dl>
</dl>
<dt><code>dlg_count_columns</code></dt>
<dd> Returns the number of columns used for a string. This is not necessarily the number of bytes in a string.</dd>
<dl>
<dl>
<dt><code>const char * </code><i>string</i></dt>
<dd> is the string to measure.</dd></dl>
</dl>
<dt><code>dlg_count_real_columns</code></dt>
<dd> Returns the number of columns used for a string, accounting for &quot;\Z&quot; sequences which can be used for coloring the text if <code>dialog_vars.colors</code> is set. This is not necessarily the number of bytes in a string.</dd>
<dl>
<dl>
<dt><code>const char * </code><i>string</i></dt>
<dd> is the string to measure.</dd></dl>
</dl>
<dt><code>dlg_count_wchars</code></dt>
<dd> Returns the number of wide-characters in the string.</dd>
<dl>
<dl>
<dt><code>const char * </code><i>string</i></dt>
<dd> is the string to measure.</dd></dl>
</dl>
<dt><code>dlg_create_rc</code></dt>
<dd> Create a configuration file, i.e., write internal tables to a file which can be read back by <code>dialog</code> as an rc-file.</dd>
<dl>
<dl>
<dt><code>const char * </code><i>filename</i></dt>
<dd> is the name of the file to write to.</dd></dl>
</dl>
<dt><code>dlg_ctl_size</code></dt>
<dd> If <code>dialog_vars.size_err</code> is true, check if the given window size is too large to fit on the screen. If so, exit with an error reporting the size of the window.</dd>
<dl>
<dl>
<dt><code>int </code><i>height</i></dt>
<dd> is the window&#8217;s height</dd>
<dt><code>int </code><i>width</i></dt>
<dd> is the window&#8217;s width</dd></dl>
</dl>
<dt><code>dlg_default_button</code></dt>
<dd> If <code>dialog_vars.default_button</code> is positive, return the button-index for that button code, using <code>dlg_ok_buttoncode</code> to test indices starting with zero. Otherwise (or if no match was found for the button code), return zero.</dd>
<dt><code>dlg_default_formitem</code></dt>
<dd> If <code>dialog_vars.default_item</code> is not null, find that name by matching the <i>name</i> field in the list of form <i>items</i>. If found, return the index of that item in the list. Otherwise, return zero.</dd>
<dl>
<dl>
<dt><code>DIALOG_FORMITEM * </code><i>items</i></dt>
<dd> is the list of items to search. It is terminated by an entry with a null <i>name</i> field.</dd></dl>
</dl>
<dt><code>dlg_default_item</code></dt>
<dd> This function is obsolete, provided for library-compatibility. It is replaced by <code>dlg_default_formitem</code> and <code>dlg_default_listitem</code>.</dd>
<dl>
<dl>
<dt><code>char ** </code><i>items</i></dt>
<dd> is the list of items to search.</dd>
<dt><code>int </code><i>llen</i></dt>
<dd> is the number of items in each group, e.g., the second array index.</dd></dl>
</dl>
<dt><code>dlg_defaultno_button</code></dt>
<dd> If <code>dialog_vars.defaultno</code> is true, and <code>dialog_vars.nocancel</code> is not, find the button-index for the &quot;Cancel&quot; button. Otherwise, return the index for &quot;OK&quot; (always zero).</dd>
<dt><code>dlg_del_window</code></dt>
<dd> Remove a window, repainting everything else.</dd>
<dl>
<dl>
<dt><code>WINDOW * </code><i>win</i></dt>
<dd> is the window to remove.</dd></dl>
</dl>
<dt><code>dlg_does_output</code></dt>
<dd> This is called each time a widget is invoked which may do output. It increments <code>dialog_state.output_count</code>, so the output function in <code>dialog</code> can test this and add a separator.</dd>
<dt><code>dlg_draw_arrows</code></dt>
<dd> Draw up/down arrows on a window, e.g., for scrollable lists. It calls <code>dlg_draw_arrows2</code> using the <i>menubox_color</i> and <i>menubox_border_color</i> attributes.</dd>
<dl>
<dl>
<dt><code>WINDOW * </code><i>dialog</i></dt>
<dd> is the window on which to draw an arrow.</dd>
<dt><code>int </code><i>top_arrow</i></dt>
<dd> is true if an up-arrow should be drawn at the top of the window.</dd>
<dt><code>int </code><i>bottom_arrow</i></dt>
<dd> is true if an down-arrow should be drawn at the bottom of the window.</dd>
<dt><code>int </code><i>x</i></dt>
<dd> is the zero-based column within the window on which to draw arrows.</dd>
<dt><code>int </code><i>top</i></dt>
<dd> is the zero-based row within the window on which to draw up-arrows as well as a horizontal line to show the window&#8217;s top.</dd>
<dt><code>int </code><i>bottom</i></dt>
<dd> is the zero-based row within the window on which to draw down-arrows as well as a horizontal line to show the window&#8217;s bottom.</dd></dl>
</dl>
<dt><code>dlg_draw_arrows2</code></dt>
<dd> Draw up/down arrows on a window, e.g., for scrollable lists.</dd>
<dl>
<dl>
<dt><code>WINDOW * </code><i>dialog</i></dt>
<dd> is the window on which to draw an arrow.</dd>
<dt><code>int </code><i>top_arrow</i></dt>
<dd> is true if an up-arrow should be drawn at the top of the window.</dd>
<dt><code>int </code><i>bottom_arrow</i></dt>
<dd> is true if an down-arrow should be drawn at the bottom of the window.</dd>
<dt><code>int </code><i>x</i></dt>
<dd> is the zero-based column within the window on which to draw arrows.</dd>
<dt><code>int </code><i>top</i></dt>
<dd> is the zero-based row within the window on which to draw up-arrows as well as a horizontal line to show the window&#8217;s top.</dd>
<dt><code>int </code><i>bottom</i></dt>
<dd> is the zero-based row within the window on which to draw down-arrows as well as a horizontal line to show the window&#8217;s bottom.</dd>
<dt><code>chtype </code><i>attr</i></dt>
<dd> is the window&#8217;s background attribute.</dd>
<dt><code>chtype </code><i>borderattr</i></dt>
<dd> is the window&#8217;s border attribute.</dd></dl>
</dl>
<dt><code>dlg_draw_bottom_box</code></dt>
<dd> Draw a partial box at the bottom of a window, e.g., to surround a row of buttons. It is designed to merge with an existing box around the whole window (see <code>dlg_draw_box</code>), so it uses tee-elements rather than corner-elements on the top corners of this box.</dd>
<dl>
<dl>
<dt><code>WINDOW * </code><i>win</i></dt>
<dd> is the window to update.</dd></dl>
</dl>
<dt><code>dlg_draw_bottom_box2</code></dt>
<dd> Draw a partial box at the bottom of a window, e.g., to surround a row of buttons. It is designed to merge with an existing box around the whole window (see <code>dlg_draw_box2</code>), so it uses tee-elements rather than corner-elements on the top corners of this box.</dd>
<dl>
<dl>
<dt><code>WINDOW * </code><i>win</i></dt>
<dd> is the window to update. <code>chtype </code><i>on_left</i> is used to color the upper/left edges of the box, i.e., the tee-element and horizontal line <code>chtype </code><i>on_right</i> is used to color the right edge of the box, i.e., the tee-element <code>chtype </code><i>on_inside</i> is used to fill-color the inside of the box</dd></dl>
</dl>
<dt><code>dlg_draw_box</code></dt>
<dd> Draw a rectangular box with line drawing characters.</dd>
<dl>
<dl>
<dt><code>WINDOW * </code><i>win</i></dt>
<dd> is the window to update.</dd>
<dt><code>int </code><i>y</i></dt>
<dd> is the top row of the box.</dd>
<dt><code>int </code><i>x</i></dt>
<dd> is the left column of the box.</dd>
<dt><code>int </code><i>height</i></dt>
<dd> is the height of the box.</dd>
<dt><code>int </code><i>width</i></dt>
<dd> is the width of the box.</dd>
<dt><code>chtype </code><i>boxchar</i></dt>
<dd> is used to color the right/lower edges. It also is fill-color used for the box contents.</dd>
<dt><code>chtype </code><i>borderchar</i></dt>
<dd> is used to color the upper/left edges.</dd></dl>
</dl>
<dt><code>dlg_draw_box2</code></dt>
<dd> Draw a rectangular box with line drawing characters.</dd>
<dl>
<dl>
<dt><code>WINDOW * </code><i>win</i></dt>
<dd> is the window to update.</dd>
<dt><code>int </code><i>y</i></dt>
<dd> is the top row of the box.</dd>
<dt><code>int </code><i>x</i></dt>
<dd> is the left column of the box.</dd>
<dt><code>int </code><i>height</i></dt>
<dd> is the height of the box.</dd>
<dt><code>int </code><i>width</i></dt>
<dd> is the width of the box.</dd>
<dt><code>chtype </code><i>boxchar</i></dt>
<dd> is used to fill-color for the box contents.</dd>
<dt><code>chtype </code><i>borderchar</i></dt>
<dd> is used to color the upper/left edges.</dd>
<dt><code>chtype </code><i>borderchar2</i></dt>
<dd> is used to color the right/lower edges.</dd></dl>
</dl>
<dt><code>dlg_draw_buttons</code></dt>
<dd> Print a list of buttons at the given position.</dd>
<dl>
<dl>
<dt><code>WINDOW * </code><i>win</i></dt>
<dd> is the window to update.</dd>
<dt><code>int </code><i>y</i></dt>
<dd> is the starting row.</dd>
<dt><code>int </code><i>x</i></dt>
<dd> is the starting column.</dd>
<dt><code>const char ** </code><i>labels</i></dt>
<dd> is a list of (pointers to) button labels terminated by a null pointer.</dd>
<dt><code>int </code><i>selected</i></dt>
<dd> is the index within the list of the selected button.</dd>
<dt><code>int </code><i>vertical</i></dt>
<dd> is true if the buttons are arranged in a column rather than a row.</dd>
<dt><code>int </code><i>limit</i></dt>
<dd> is the number of columns (or rows if <i>vertical</i>) allowed for the display.</dd></dl>
</dl>
<dt><code>dlg_draw_helpline</code></dt>
<dd> draw the text in <code>dialog_vars.help_line</code> at the bottom of the given window.</dd>
<dl>
<dl>
<dt><code>WINDOW * </code><i>dialog</i></dt>
<dd> is the window to modify.</dd>
<dt><code>bool </code><i>decorations</i></dt>
<dd> if true, allow room for the scrolling arrows.</dd></dl>
</dl>
<dt><code>dlg_draw_scrollbar</code></dt>
<dd> If <code>dialog_state.use_scrollbar</code> is set, draw a scrollbar on the right margin of windows holding scrollable data. Also (whether or not the scrollbar is drawn), annotate the bottom margin of the window with the percentage of data by the bottom of that window, and call <code>dlg_draw_arrows2</code> to put markers on the window showing when more data is available.</dd>
<dl>
<dl>
<dt><code>WINDOW * </code><i>win</i></dt>
<dd> is the window in which the data is scrolled. Because <i>left</i>, <i>right</i>, <i>top</i>, <i>bottom</i> are passed as parameters, this window can contain additional data.</dd>
<dt><code>long </code><i>first_data</i></dt>
<dd> is the zero-based index to the first row of data in the current window.</dd>
<dt><code>long </code><i>this_data</i></dt>
<dd> is the zero-based index to the current row of data.</dd>
<dt><code>long </code><i>next_data</i></dt>
<dd> is the zero-based index to the next data after the current row.</dd>
<dt><code>long </code><i>total_data</i></dt>
<dd> is the total number of rows of data.</dd>
<dt><code>int </code><i>left</i></dt>
<dd> is the zero-based left margin/column of the window. The up/down arrows are draw inset by 5 columns from this point.</dd>
<dt><code>int </code><i>right</i></dt>
<dd> is the zero-based right margin/column of the window. The scrollbar is drawn flush against this column.</dd>
<dt><code>int </code><i>top</i></dt>
<dd> is the zero-based row within the window on which to draw up-arrows as well as a horizontal line to show the window&#8217;s top.</dd>
<dt><code>int </code><i>bottom</i></dt>
<dd> is the zero-based row within the window on which to draw down-arrows as well as a horizontal line to show the window&#8217;s bottom.</dd>
<dt><code>chtype </code><i>attr</i></dt>
<dd> is the window&#8217;s background attribute.</dd>
<dt><code>chtype </code><i>borderattr</i></dt>
<dd> is the window&#8217;s border attribute.</dd></dl>
</dl>
<dt><code>dlg_draw_shadow</code></dt>
<dd> Draw shadows along the right and bottom edge of a window to give it a 3-dimensional look. (The height, etc., may not be the same as the window&#8217;s actual values).</dd>
<dl>
<dl>
<dt><code>WINDOW * </code><i>win</i></dt>
<dd> is the window to update.</dd>
<dt><code>int </code><i>height</i></dt>
<dd> is the height of the window.</dd>
<dt><code>int </code><i>width</i></dt>
<dd> is the width of the window.</dd>
<dt><code>int </code><i>y</i></dt>
<dd> is the top row of the window.</dd>
<dt><code>int </code><i>x</i></dt>
<dd> is the left column of the window.</dd></dl>
</dl>
<dt><code>dlg_draw_title</code></dt>
<dd> Draw a title centered at the top of the window.</dd>
<dl>
<dl>
<dt><code>WINDOW * </code><i>win</i></dt>
<dd> is the window to update.</dd>
<dt><code>const char * </code><i>title</i></dt>
<dd> is the title string to display at the top of the widget.</dd></dl>
</dl>
<dt><code>dlg_dummy_menutext</code></dt>
<dd> This is a utility function which supports the <code>&#8211;inputmenu</code> option of the <code>dialog</code> program. If <code>dialog_vars.input_menu</code> is set, <code>dialog_menu</code> passes this pointer to <code>dlg_menu</code> as the <i>rename_menutext</i> parameter. Otherwise, it passes <code>dlg_dummy_menutext</code>.</dd>
<dt>
</dt><dd> The function should only return <code>DLG_EXIT_ERROR</code>.</dd>
<dl>
<dl>
<dt><code>DIALOG_LISTITEM * </code><i>items</i></dt>
<dd> is the list of menu items</dd>
<dt><code>int </code><i>current</i></dt>
<dd> is the index of the currently-selected item</dd>
<dt><code>char * </code><i>newtext</i></dt>
<dd> is the updated text for the menu item</dd></dl>
</dl>
<dt><code>dlg_dump_keys</code></dt>
<dd> Write all user-defined key-bindings to the given stream, e.g., as part of <code>dlg_create_rc</code>.</dd>
<dl>
<dl>
<dt><code>FILE * </code><i>fp</i></dt>
<dd> is the stream on which to write the bindings.</dd></dl>
</dl>
<dt><code>dlg_dump_window_keys</code></dt>
<dd> Write all user-defined key-bindings to the given stream, e.g., as part of <code>dlg_create_rc</code>.</dd>
<dl>
<dl>
<dt><code>FILE * </code><i>fp</i></dt>
<dd> is the stream on which to write the bindings.</dd>
<dt><code>WINDOW * </code><i>win</i></dt>
<dd> is the window for which bindings should be dumped. If it is null, then only built-in bindings are dumped.</dd></dl>
</dl>
<dt><code>dlg_eat_argv</code></dt>
<dd> Remove one or more items from an argument vector.</dd>
<dl>
<dl>
<dt><code>int *argcp</code></dt>
<dd> in/out parameter giving the length of the argument vector. <code>char ***argvp</code> in/out parameter pointing to the argument vector. <code>int start</code> starting index. <code>int count</code> number of arguments to remove.</dd></dl>
</dl>
<dt><code>dlg_edit_offset</code></dt>
<dd> Given the character-offset in the string, returns the display-offset where <code>dialog</code> should position the cursor. In this context, &quot;characters&quot; may be multicolumn, since the string can be a multibyte character string.</dd>
<dl>
<dl>
<dt><code>char * </code><i>string</i></dt>
<dd> is the string to analyze</dd>
<dt><code>int </code><i>offset</i></dt>
<dd> is the character-offset</dd>
<dt><code>int </code><i>x_last</i></dt>
<dd> is a limit on the column positions that can be used, e.g., the window&#8217;s size.</dd></dl>
</dl>
<dt><code>dlg_edit_string</code></dt>
<dd> Updates the string and character-offset, given various editing characters or literal characters which are inserted at the character-offset. Returns true if an editing change was made (and the display should be updated), and false if the key was something like KEY_ENTER, which is a non-editing action outside this function.</dd>
<dl>
<dl>
<dt><code>char * </code><i>string</i></dt>
<dd> is the (multibyte) string to update</dd>
<dt><code>int * </code><i>offset</i></dt>
<dd> is the character-offset</dd>
<dt><code>int </code><i>key</i></dt>
<dd> is the editing key</dd>
<dt><code>int </code><i>fkey</i></dt>
<dd> is true if the editing key is a function-key</dd>
<dt><code>bool </code><i>force</i></dt>
<dd> is used in a special loop case by calling code to force the return value of this function when a function-key code 0 is passed in.</dd></dl>
</dl>
<dt><code>dlg_exit</code></dt>
<dd> Given an internal exit code, check if the corresponding environment variable is set. If so, remap the exit code to match the environment variable. Finally call <code>exit</code> with the resulting exit code.</dd>
<dl>
<dl>
<dt><code>int </code><i>code</i></dt>
<dd> is the internal exit code, e.g., <code>DLG_EXIT_OK</code>, which may be remapped.</dd></dl>
</dl>
<dt>
</dt><dd> The <code>dialog</code> program uses this function to allow shell scripts to remap the exit codes so they can distinguish ESC from ERROR.</dd>
<dt><code>dlg_exit_buttoncode</code></dt>
<dd> Map the given button index for <code>dlg_exit_label</code> into <code>dialog</code>&#8216;s exit-code.</dd>
<dl>
<dl>
<dt><code>int </code><i>button</i></dt>
<dd> is the button index</dd></dl>
</dl>
<dt><code>dlg_exit_label</code></dt>
<dd> Return a list of button labels. If dialog_var.extra_button is true, return the result of <code>dlg_ok_labels</code>. Otherwise, return a list with the &quot;Exit&quot; label and (if <code>dialog_vars.help_button</code> is set) the &quot;Help&quot; button as well.</dd>
<dt><code>dlg_exiterr</code></dt>
<dd> Quit program killing all <code>tailboxbg</code> widgets.</dd>
<dl>
<dl>
<dt><code>const char * </code><i>fmt</i></dt>
<dd> is the format of the <code>printf</code>-like message to write.</dd>
<dt><code>&#8230;</code></dt>
<dd>
 are the variables to apply to the <i>fmt</i> format.</dd></dl>
</dl>
<dt><code>dlg_find_index</code></dt>
<dd> Given the character-offset to find in the list, return the corresponding array index.</dd>
<dl>
<dl>
<dt><code>const int *</code><i>list</i></dt>
<dd> contains a list of character-offsets, i.e., indices into a string that denote the beginning of multibyte characters.</dd>
<dt><code>int </code><i>limit</i></dt>
<dd> is the last index into <code>list</code> to search.</dd>
<dt><code>int </code><i>to_find</i></dt>
<dd> is the character-offset to find.</dd></dl>
</dl>
<dt><code>dlg_flush_getc</code></dt>
<dd> Cancel the local data saved by <code>dlg_last_getc</code>.</dd>
<dt>dlg_editbox</dt>
<dd> This entrypoint provides the <code>&#8211;editbox</code> functionality without the limitations of <code>dialog</code>&#8216;s command-line syntax (compare to <code>dialog_editbox</code>).</dd>
<dl>
<dl>
<dt><code>const char * </code><i>title</i></dt>
<dd> is the title string to display at the top of the widget.</dd>
<dt><code>char *** </code><i>list</i></dt>
<dd> is a pointer to an array of <code>char&nbsp;<wbr>*</code> pointers. The array is allocated by the caller, and so are the strings to which it points. The <code>dlg_editbox</code> function may reallocate the array and the strings.</dd>
<dt><code>int * </code><i>rows</i></dt>
<dd> points to the nominal length of <i>list</i>. The referenced value is updated if<i>list</i> is reallocated.</dd>
<dt><code>int </code><i>height</i></dt>
<dd> is the desired height of the box. If zero, the height is adjusted to use the available screen size.</dd>
<dt><code>int </code><i>width</i></dt>
<dd> is the desired width of the box. If zero, the height is adjusted to use the available screen size.</dd></dl>
</dl>
<dt><code>dlg_form</code></dt>
<dd> This entrypoint provides the <code>&#8211;form</code> functionality without the limitations of <code>dialog</code>&#8216;s command-line syntax (compare to <code>dialog_form</code>).</dd>
<dl>
<dl>
<dt><code>const char * </code><i>title</i></dt>
<dd> is the title string to display at the top of the widget.</dd>
<dt><code>const char * </code><i>cprompt</i></dt>
<dd> is the prompt text shown within the widget.</dd>
<dt><code>int </code><i>height</i></dt>
<dd> is the desired height of the box. If zero, the height is adjusted to use the available screen size.</dd>
<dt><code>int </code><i>width</i></dt>
<dd> is the desired width of the box. If zero, the height is adjusted to use the available screen size.</dd>
<dt><code>int </code><i>form_height</i></dt>
<dd> is the minimum height to reserve for displaying the list. If zero, it is computed based on the given <i>height</i> and <i>width</i>.</dd>
<dt><code>int </code><i>item_no</i></dt>
<dd> is the number of <i>items</i>.</dd>
<dt><code>DIALOG_FORMITEM * </code><i>items</i></dt>
<dd> This is a list of the items to display in the form.</dd>
<dt><code>int * </code><i>current_item</i></dt>
<dd> The widget sets the referenced location to the index of the current display item (cursor) when it returns.</dd></dl>
</dl>
<dt><code>dlg_free_columns</code></dt>
<dd> Free data allocated by <code>dlg_align_columns</code>.</dd>
<dl>
<dl>
<dt><code>char **</code><i>target</i></dt>
<dd> This is the array which was reformatted. It points to the first string to free.</dd>
<dt><code>int </code><i>per_row</i></dt>
<dd> This is the size of the struct for each row of the array.</dd>
<dt><code>int </code><i>num_rows</i></dt>
<dd> This is the number of rows in the array.</dd></dl>
</dl>
<dt><code>dlg_free_formitems</code></dt>
<dd> Free memory owned by a list of DIALOG_FORMITEM&#8217;s.</dd>
<dl>
<dl>
<dt><code>DIALOG_FORMITEM * </code><i>items</i></dt>
<dd> is the list to free.</dd></dl>
</dl>
<dt><code>dlg_free_gauge</code></dt>
<dd> Remove the gauge widget from the screen and free its associated memory.</dd>
<dl>
<dl>
<dt><code>void *</code><i>objptr</i></dt>
<dd> points to the gauge widget.</dd></dl>
</dl>
<dt><code>dlg_getc</code></dt>
<dd> Read a character from the given window. Handle repainting here (to simplify things in the calling application). Also, if input-callback(s) are set up, poll the corresponding files and handle the updates, e.g., for displaying a tailbox. Returns the key-code.</dd>
<dl>
<dl>
<dt><code>WINDOW * </code><i>win</i></dt>
<dd> is the window within which to read.</dd>
<dt><code>int * </code><i>fkey</i></dt>
<dd> as a side-effect, set this to true if the key-code is really a function-key.</dd></dl>
</dl>
<dt><code>dlg_get_attrs</code></dt>
<dd> extract the video attributes from the given window.</dd>
<dl>
<dl>
<dt><code>WINDOW * </code><i>win</i></dt>
<dd> is the window from which to get attributes.</dd></dl>
</dl>
<dt><code>dlg_getc_callbacks</code></dt>
<dd> passes the given key-code <i>ch</i> to the current window that has established a callback. If the callback returns zero, remove it and try the next window. If no more callbacks remain, return. If any callbacks were found, return true, otherwise false.</dd>
<dl>
<dl>
<dt><code>int </code><i>ch</i></dt>
<dd> is the key-code</dd>
<dt><code>int </code><i>fkey</i></dt>
<dd> is true if the key is a function-key</dd>
<dt><code>int * </code><i>result</i></dt>
<dd> is used to pass an exit-code to the caller, which should pass that via <code>dlg_exit</code>.</dd></dl>
</dl>
<dt><code>dlg_index_columns</code></dt>
<dd> Build a list of the display-columns for the given multibyte string&#8217;s characters.</dd>
<dl>
<dl>
<dt><code>const char * </code><i>string</i></dt>
<dd> is the string to analyze</dd></dl>
</dl>
<dt><code>dlg_index_wchars</code></dt>
<dd> Build an index of the wide-characters in the string, so the caller can easily tell which byte-offset begins a given wide-character.</dd>
<dl>
<dl>
<dt><code>const char * </code><i>string</i></dt>
<dd> is the string to analyze</dd></dl>
</dl>
<dt><code>dlg_item_help</code></dt>
<dd> Draw the string for the <code>dialog_vars.item_help</code> feature.</dd>
<dl>
<dl>
<dt><code>const char * </code><i>txt</i></dt>
<dd> is the help-message</dd></dl>
</dl>
<dt><code>dlg_killall_bg</code></dt>
<dd> If <code>dialog</code> has callbacks active, purge the list of all that are not marked to keep in the background. If any remain, run those in a background process.</dd>
<dl>
<dl>
<dt><code>int * </code><i>retval</i></dt>
<dd> stores the exit-code to pass back to the caller.</dd></dl>
</dl>
<dt><code>dlg_last_getc</code></dt>
<dd> returns the most recent character that was read via <code>dlg_getc</code>.</dd>
<dt><code>dlg_limit_columns</code></dt>
<dd> Given a column limit, count the number of wide characters that can fit into that limit. The offset is used to skip over a leading character that was already written.</dd>
<dl>
<dl>
<dt><code>const char * </code><i>string</i></dt>
<dd> is the string to analyze</dd>
<dt><code>int </code><i>limit</i></dt>
<dd> is the column limit</dd>
<dt><code>int </code><i>offset</i></dt>
<dd> is the starting offset from which analysis should continue</dd></dl>
</dl>
<dt><code>dlg_lookup_key</code></dt>
<dd> Check for a key-binding. If there is no binding associated with the widget, it simply returns the given curses-key. Otherwise, it returns the result of the binding</dd>
<dl>
<dl>
<dt><code>WINDOW * </code><i>win</i></dt>
<dd> is the window on which the binding is checked</dd>
<dt><code>int </code><i>curses_key</i></dt>
<dd> is the curses key-code</dd>
<dt><code>int * </code><i>dialog_key</i></dt>
<dd> is the corresponding <code>dialog</code> internal code (see <code>DLG_KEYS_ENUM</code> in dlg_key.h).</dd></dl>
</dl>
<dt><code>dlg_max_input</code></dt>
<dd> Limit the parameter according to <code>dialog_vars.max_input</code></dd>
<dl>
<dl>
<dt><code>int </code><i>max_len</i></dt>
<dd> is the value to limit</dd></dl>
</dl>
<dt><code>dlg_match_char</code></dt>
<dd> Match a given character against the beginning of the string, ignoring case of the given character. The matching string must begin with an uppercase character.</dd>
<dl>
<dl>
<dt><code>int </code><i>ch</i></dt>
<dd> is the character to check</dd>
<dt><code>const char * </code><i>string</i></dt>
<dd> is the string to search</dd></dl>
</dl>
<dt><code>dlg_menu</code></dt>
<dd> This entrypoint provides the <code>&#8211;menu</code> functionality without the limitations of <code>dialog</code>&#8216;s command-line syntax (compare to <code>dialog_menu</code>).</dd>
<dl>
<dl>
<dt><code>const char * </code><i>title</i></dt>
<dd> is the title string to display at the top of the widget.</dd>
<dt><code>const char * </code><i>cprompt</i></dt>
<dd> is the prompt text shown within the widget.</dd>
<dt><code>int </code><i>height</i></dt>
<dd> is the desired height of the box. If zero, the height is adjusted to use the available screen size.</dd>
<dt><code>int </code><i>width</i></dt>
<dd> is the desired width of the box. If zero, the height is adjusted to use the available screen size.</dd>
<dt><code>int </code><i>menu_height</i></dt>
<dd> is the minimum height to reserve for displaying the list. If zero, it is computed based on the given <i>height</i> and <i>width</i>.</dd>
<dt><code>int </code><i>item_no</i></dt>
<dd> is the number of <i>items</i>.</dd>
<dt><code>DIALOG_LISTITEM * </code><i>items</i></dt>
<dd> This is a list of the items to display in the form.</dd>
<dt><code>int * </code><i>current_item</i></dt>
<dd> The widget sets the referenced location to the index of the current display item (cursor) when it returns.</dd>
<dt><code>DIALOG_INPUTMENU </code><i>rename_menutext</i></dt>
<dd> If this is not <code>dlg_dummy_menutext</code>, the widget acts like an <i>inputmenu</i> widget, providing an extra &quot;Rename&quot; button, which activates an edit feature on the selected menu item.</dd></dl>
</dl>
<dt><code>dlg_move_window</code></dt>
<dd> Moves/resizes the given window to the given position and size.</dd>
<dl>
<dl>
<dt><code>WINDOW *</code><i>win</i></dt>
<dd> is the window to move/resize.</dd>
<dt><code>WINDOW *</code><i>height</i></dt>
<dd> is the height of the resized window.</dd>
<dt><code>WINDOW *</code><i>width</i></dt>
<dd> is the width of the resized window.</dd>
<dt><code>WINDOW *</code><i>y</i></dt>
<dd> y-ordinate to use for the repositioned window.</dd>
<dt><code>WINDOW *</code><i>x</i></dt>
<dd> x-ordinate to use for the repositioned window.</dd></dl>
</dl>
<dt><code>dlg_mouse_bigregion</code></dt>
<dd> Retrieve the big-region under the pointer.</dd>
<dl>
<dl>
<dt><code>int </code><i>y</i></dt>
<dd> is the row on which the mouse click occurred</dd>
<dt><code>int </code><i>x</i></dt>
<dd> is the column on which the mouse click occurred</dd></dl>
</dl>
<dt><code>dlg_mouse_free_regions</code></dt>
<dd> Free the memory associated with mouse regions.</dd>
<dt><code>dlg_mouse_mkbigregion</code></dt>
<dd> Creates a region on which the mouse-clicks will return a specifed code.</dd>
<dl>
<dl>
<dt><code>int </code><i>y</i></dt>
<dd> is the top-row of the region.</dd>
<dt><code>int </code><i>x</i></dt>
<dd> is the left-column of the region.</dd>
<dt><code>int </code><i>height</i></dt>
<dd> is the height of the region.</dd>
<dt><code>int </code><i>width</i></dt>
<dd> is the width of the region.</dd>
<dt><code>int </code><i>code</i></dt>
<dd> is a code used to make the region unique within a widget</dd>
<dt><code>int </code><i>step_x</i></dt>
<dd> is used in modes 2 (columns) and 3 (cells) to determine the width of a column/cell.</dd>
<dt><code>int </code><i>step_y</i></dt>
<dd> is currently unused</dd>
<dt><code>int </code><i>mode</i></dt>
<dd> is used to determine how the mouse position is translated into a code (like a function-key):</dd>
<dl>
<dl>
<dt>1</dt>
<dd> index by lines</dd>
<dt>2</dt>
<dd> index by columns</dd>
<dt>3</dt>
<dd> index by cells</dd></dl>
</dl>
</dl>
</dl>
<dt><code>dlg_mouse_mkregion</code></dt>
<dd>
</dd><dl>
<dl>
<dt><code>int </code><i>y</i></dt>
<dd> is the top-row of the region.</dd>
<dt><code>int </code><i>x</i></dt>
<dd> is the left-column of the region.</dd>
<dt><code>int </code><i>height</i></dt>
<dd> is the height of the region.</dd>
<dt><code>int </code><i>width</i></dt>
<dd> is the width of the region.</dd>
<dt><code>int </code><i>code</i></dt>
<dd> is a code used to make the region unique within a widget</dd></dl>
</dl>
<dt><code>dlg_mouse_region</code></dt>
<dd> Retrieve the frame under the mouse pointer</dd>
<dl>
<dl>
<dt><code>int </code><i>y</i></dt>
<dd> is the row of the mouse-click</dd>
<dt><code>int </code><i>x</i></dt>
<dd> is the column of the mouse-click</dd></dl>
</dl>
<dt><code>dlg_mouse_setbase</code></dt>
<dd> Sets a base for subsequent calls to <code>dlg_mouse_mkregion</code>, so they can make regions relative to the start of a given window.</dd>
<dl>
<dl>
<dt><code>int </code><i>x</i></dt>
<dd> is the left-column for the base</dd>
<dt><code>int </code><i>y</i></dt>
<dd> is the top-row for the base</dd></dl>
</dl>
<dt><code>dlg_mouse_setcode</code></dt>
<dd> Sets a value used internally by <code>dlg_mouse_mkregion</code> which is added to the <i>code</i> parameter. By providing different values, e.g., multiples of <code>KEY_MAX</code>, it is possible to support multiple &quot;big&quot; regions in a widget. The <i>buildlist</i> widget uses this feature to recognize mouse-clicks in the left/right panes.</dd>
<dl>
<dl>
<dt><code>int </code><i>code</i></dt>
<dd> is the value to add to <code>dlg_mouse_mkregion</code>&#8216;s <i>code</i> parameter.</dd></dl>
</dl>
<dt><code>dlg_mouse_wgetch</code></dt>
<dd> is a wrapper for <code>dlg_getc</code> which additionally maps mouse-clicks (if the curses library supports those) into extended function-keys which encode the position according to the <i>mode</i> in <code>dlg_mouse_mkbigregion</code>. Returns the corresponding key-code.</dd>
<dl>
<dl>
<dt><code>WINDOW * </code><i>win</i></dt>
<dd> is the window on which to perform the input</dd>
<dt><code>int * </code><i>fkey</i></dt>
<dd> the referenced location is set to true if the key-code is an actual or extended (mouse) function-key.</dd></dl>
</dl>
<dt><code>dlg_mouse_wgetch_nowait</code></dt>
<dd> This is a non-blocking variant of <code>dlg_mouse_wgetch</code>.</dd>
<dl>
<dl>
<dt><code>WINDOW * </code><i>win</i></dt>
<dd> is the window on which to perform the input</dd>
<dt><code>int * </code><i>fkey</i></dt>
<dd> the referenced location is set to true if the key-code is an actual or extended (mouse) function-key.</dd></dl>
</dl>
<dt><code>dlg_need_separator</code></dt>
<dd> Check if an output-separator is needed. If <code>dialog_vars.output_separator</code> is set, return true. Otherwise, if <code>dialog_vars.input_result</code> is nonempty, return true. If neither, return false.</dd>
<dt><code>dlg_new_modal_window</code></dt>
<dd> Create a modal window, optionally with a shadow. The shadow is created if <code>dialog_state.use_shadow</code> is true.</dd>
<dl>
<dl>
<dt><code>WINDOW * </code><i>parent</i></dt>
<dd> is the parent window (usually the top-level window of a widget)</dd>
<dt><code>int </code><i>height</i></dt>
<dd> is the window&#8217;s height</dd>
<dt><code>int </code><i>width</i></dt>
<dd> is the window&#8217;s width</dd>
<dt><code>int </code><i>y</i></dt>
<dd> is the window&#8217;s top-row</dd>
<dt><code>int </code><i>x</i></dt>
<dd> is the window&#8217;s left-column</dd></dl>
</dl>
<dt><code>dlg_new_window</code></dt>
<dd> Create a window, optionally with a shadow. The shadow is created if <code>dialog_state.use_shadow</code> is true.</dd>
<dl>
<dl>
<dt><code>int </code><i>height</i></dt>
<dd> is the window&#8217;s height</dd>
<dt><code>int </code><i>width</i></dt>
<dd> is the window&#8217;s width</dd>
<dt><code>int </code><i>y</i></dt>
<dd> is the window&#8217;s top-row</dd>
<dt><code>int </code><i>x</i></dt>
<dd> is the window&#8217;s left-column</dd></dl>
</dl>
<dt><code>dlg_next_button</code></dt>
<dd> Return the next index in the list of labels.</dd>
<dl>
<dl>
<dt><code>const char ** </code><i>labels</i></dt>
<dd> is a list of (pointers to) button labels terminated by a null pointer.</dd>
<dt><code>int </code><i>button</i></dt>
<dd> is the current button-index.</dd></dl>
</dl>
<dt><code>dlg_next_ok_buttonindex</code></dt>
<dd> Assuming that the caller is using <code>dlg_ok_labels</code> to list buttons, find the next index in the list of buttons.</dd>
<dl>
<dl>
<dt><code>int </code><i>current</i></dt>
<dd> is the current index in the list of buttons</dd>
<dt><code>int </code><i>extra</i></dt>
<dd> if negative, provides a way to enumerate extra active areas on the widget.</dd></dl>
</dl>
<dt><code>dlg_ok_buttoncode</code></dt>
<dd> Map the given button index for <code>dlg_ok_labels</code> into <code>dialog</code>&#8216;s exit-code.</dd>
<dl>
<dl>
<dt><code>int </code><i>button</i></dt>
<dd> is the button-index (which is not necessarily the same as the index in the list of labels).</dd></dl>
</dl>
<dt><code>dlg_ok_label</code></dt>
<dd> Returns a list with the &quot;Ok&quot; label, and if <code>dialog_vars.help_button</code> is true, the &quot;Help&quot; label as well.</dd>
<dt><code>dlg_ok_labels</code></dt>
<dd> Return a list of button labels for the OK/Cancel group of widgets.</dd>
<dt><code>dlg_ordinate</code></dt>
<dd> Decode the string as an integer, decrement if greater than zero to make a curses-ordinate from a dialog-ordinate.</dd>
<dt><code>dlg_parse_bindkey</code></dt>
<dd> Parse the parameters of the &quot;bindkeys&quot; configuration-file entry. This expects widget name which may be &quot;*&quot;, followed by curses key definition and then <code>dialog</code> key definition.</dd>
<dl>
<dl>
<dt><code>char * </code><i>params</i></dt>
<dd> is the parameter string to parse.</dd></dl>
</dl>
<dt><code>dlg_parse_rc</code></dt>
<dd> Parse the configuration file and set up variables.</dd>
<dt><code>dlg_prev_button</code></dt>
<dd> Return the previous index in the list of labels.</dd>
<dl>
<dl>
<dt><code>const char ** </code><i>labels</i></dt>
<dd> is a list of (pointers to) button labels terminated by a null pointer.</dd>
<dt><code>int </code><i>button</i></dt>
<dd> is the current button index</dd></dl>
</dl>
<dt><code>dlg_print_listitem</code></dt>
<dd> This is a helper function used for the various &quot;list&quot; widgets, e.g., checklist, menu, buildlist, treeview. Each list-widget has &quot;tag&quot; and &quot;description&quot; values for each item which can be displayed. If <code>dialog_vars.no_tags</code> is true, the &quot;tag&quot; value is not shown. The first character of the first value shown (tag or description) is highlighted to indicate that the widget will match it for quick navigation.</dd>
<dl>
<dl>
<dt><code>WINDOW *</code><i>win</i></dt>
<dd> the window in which to display the text</dd>
<dt><code>const char *</code><i>text</i></dt>
<dd> the value to display</dd>
<dt><code>int </code><i>climit</i></dt>
<dd> the number of columns available for printing the text</dd>
<dt><code>bool </code><i>first</i></dt>
<dd> true if this is the first call (for &quot;tag&quot; and &quot;description&quot;), and the first character of the value should be highlighted.</dd>
<dt><code>int </code><i>selected</i></dt>
<dd> nonzero if the text should be displayed using the &quot;selected&quot; colors</dd></dl>
</dl>
<dt><code>dlg_print_scrolled</code></dt>
<dd> This is a wrapper for <code>dlg_print_autowrap</code> which allows the user to scroll too-long prompt text up/down.</dd>
<dt>
</dt><dd> See <code>dlg_check_scrolled</code> for a function which updates the <i>offset</i> variable used as a parameter here. It complements this function; you need both. If <i>pauseopt</i> is set, this function returns an updated <i>last</i> parameter, needed for <code>dlg_check_scrolled</code> calls.</dd>
<dl>
<dl>
<dt><code>WINDOW * </code><i>win</i></dt>
<dd> is the window to update.</dd>
<dt><code>const char * </code><i>prompt</i></dt>
<dd> is the string to print</dd>
<dt><code>int </code><i>offset</i></dt>
<dd> is the starting line-number to write wrapped text.</dd>
<dt><code>int </code><i>height</i></dt>
<dd> is the available height for writing the wrapped text</dd>
<dt><code>int </code><i>width</i></dt>
<dd> is the width that the wrapping should occur in</dd>
<dt><code>int </code><i>pauseopt</i></dt>
<dd> is true if the extra functionality for scrolling should be enabled. If false, this calls <code>dlg_print_autowrap</code> without doing any scrolling.</dd></dl>
</dl>
<dt><code>dlg_print_line</code></dt>
<dd> Print one line of the prompt in the window within the limits of the specified right margin. The line will end on a word boundary and a pointer to the start of the next line is returned, or a NULL pointer if the end of *prompt is reached.</dd>
<dl>
<dl>
<dt><code>WINDOW *</code><i>win</i></dt>
<dd> is the window to update.</dd>
<dt><code>chtype *</code><i>attr</i></dt>
<dd> holds the starting attributes, and is updated to reflect the final attributes applied to the string.</dd>
<dt><code>const char *</code><i>prompt</i></dt>
<dd> is the string to print</dd>
<dt><code>int </code><i>lm</i></dt>
<dd> is the left margin.</dd>
<dt><code>int </code><i>rm</i></dt>
<dd> is the right margin</dd>
<dt><code>int *</code><i>x</i></dt>
<dd> returns the ending x-ordinate.</dd></dl>
</dl>
<dt><code>dlg_prev_ok_buttonindex</code></dt>
<dd> Find the previous button index in the list from <code>dlg_ok_labels</code>.</dd>
<dl>
<dl>
<dt><code>int </code><i>current</i></dt>
<dd> is the current index</dd>
<dt><code>int </code><i>extra</i></dt>
<dd> if negative provides a way to enumerate extra active areas on the widget.</dd></dl>
</dl>
<dt><code>dlg_print_autowrap</code></dt>
<dd> Print a string of text in a window, automatically wrap around to the next line if the string is too long to fit on one line. Note that the string may contain embedded newlines. The text is written starting at the top of the window.</dd>
<dl>
<dl>
<dt><code>WINDOW * </code><i>win</i></dt>
<dd> is the window to update.</dd>
<dt><code>const char * </code><i>prompt</i></dt>
<dd> is the string to print</dd>
<dt><code>int </code><i>height</i></dt>
<dd> is the nominal height the wrapped string is limited to</dd>
<dt><code>int </code><i>width</i></dt>
<dd> is the width that the wrapping should occur in</dd></dl>
</dl>
<dt><code>dlg_print_size</code></dt>
<dd> If <code>dialog_vars.print_siz</code> is true, print the given height/width (from a widget) to <code>dialog_state.output</code>, e.g., <code>Size: height, width</code>.</dd>
<dl>
<dl>
<dt><code>int </code><i>height</i></dt>
<dd> is the window&#8217;s height</dd>
<dt><code>int </code><i>width</i></dt>
<dd> is the window&#8217;s width</dd></dl>
</dl>
<dt><code>dlg_print_text</code></dt>
<dd> Print up to <i>cols</i> columns from <code>text</code>, optionally rendering <code>dialog</code>&#8216;s escape sequences for attributes and color.</dd>
<dl>
<dl>
<dt><code>WINDOW * </code><i>win</i></dt>
<dd> is the window to update.</dd>
<dt><code>const char * </code><i>txt</i></dt>
<dd> is the string to print</dd>
<dt><code>int </code><i>col</i></dt>
<dd> is the column limit</dd>
<dt><code>chtype * </code><i>attr</i></dt>
<dd> holds the starting attributes, and is updated to reflect the final attributes applied to the string.</dd></dl>
</dl>
<p> <code>dlg_progressbox</code> implements the &quot;<code>&#8211;prgbox</code>&quot; and &quot;<code>&#8211;progressbox</code>&quot; options.</p>
<dl>
<dl>
<dt><code>const char * </code><i>title</i></dt>
<dd> is the title on the top of the widget.</dd>
<dt><code>const char * </code><i>cprompt</i></dt>
<dd> is the prompt text shown within the widget. If empty or null, no prompt is shown.</dd>
<dt><code>int </code><i>height</i></dt>
<dd> is the desired height of the box. If zero, the height is based on the screen size.</dd>
<dt><code>int </code><i>width</i></dt>
<dd> is the desired width of the box. If zero, the height is based on the screen size.</dd>
<dt><code>int </code><i>pauseopt</i></dt>
<dd> if true, an &quot;OK&quot; button will be shown, and the dialog will wait for it to complete. With an &quot;OK&quot; button, it is denoted a &quot;programbox&quot;, without an &quot;OK&quot; button, it is denoted a &quot;progressbox&quot;.</dd>
<dt><code>FILE * </code><i>fp</i></dt>
<dd> is the file pointer, which may be a pipe or a regular file.</dd></dl>
</dl>
<dt><code>dlg_put_backtitle</code></dt>
<dd> Display the background title if <code>dialog_vars.backtitle</code> is non-null. The background title is shown at the top of the screen.</dd>
<dt><code>dlg_register_buttons</code></dt>
<dd> The widget developer should call this function after <code>dlg_register_window</code>, for the list of button labels associated with the widget. One may bind a key to a button, e.g., &quot;OK&quot; for <code>DLGK_OK</code>,</dd>
<dl>
<dl>
<dt><code>WINDOW * </code><i>win</i></dt>
<dd> is the window with which to associate the buttons</dd>
<dt><code>const char * </code><i>name</i></dt>
<dd> is the widget&#8217;s binding name (usually the name of the widget).</dd>
<dt><code>const char ** </code><i>buttons</i></dt>
<dd> is the list of buttons</dd></dl>
</dl>
<dt><code>dlg_register_window</code></dt>
<dd> For a given named widget&#8217;s window, associate a binding table.</dd>
<dl>
<dl>
<dt><code>WINDOW * </code><i>win</i></dt>
<dd> is the window with which to associate the buttons</dd>
<dt><code>const char * </code><i>name</i></dt>
<dd> is the widget&#8217;s binding name (usually the name of the widget).</dd>
<dt><code>DLG_KEYS_BINDING * </code><i>binding</i></dt>
<dd> is the binding table</dd></dl>
</dl>
<dt><code>dlg_remove_callback</code></dt>
<dd> Remove a callback.</dd>
<dl>
<dl>
<dt><code>DIALOG_CALLBACK * </code><i>p</i></dt>
<dd> contains the callback information.</dd></dl>
</dl>
<dt><code>dlg_renamed_menutext</code></dt>
<dd> This is a utility function which supports the <code>&#8211;inputmenu</code> option of the <code>dialog</code> program. If <code>dialog_vars.input_menu</code> is set, <code>dialog_menu</code> passes this pointer to <code>dlg_menu</code> as the <i>rename_menutext</i> parameter. Otherwise, it passes <code>dlg_dummy_menutext</code>.</dd>
<dt>
</dt><dd> The function should add &quot;RENAMED&quot; to <code>dialog_vars.input_result</code> , followed by the menu item&#8217;s name and the <i>newtext</i> value (with a space separating the three items), and return <code>DLG_EXIT_EXTRA</code>.</dd>
<dl>
<dl>
<dt><code>DIALOG_LISTITEM * </code><i>items</i></dt>
<dd> is the list of menu items</dd>
<dt><code>int </code><i>current</i></dt>
<dd> is the index of the currently-selected item</dd>
<dt><code>char * </code><i>newtext</i></dt>
<dd> is the updated text for the menu item</dd></dl>
</dl>
<dt><code>dlg_restore_vars</code></dt>
<dd> Restore <code>dialog</code>&#8216;s variables from the given variable (see <code>dialog_save_vars</code>).</dd>
<dl>
<dl>
<dt><code>DIALOG_VARS * </code><i>save</i></dt>
<dd> is the variable from which to restore.</dd></dl>
</dl>
<dt>
</dt><dd> The <i>DIALOG_VARS.input_length</i> and <i>DIALOG_VARS.input_result</i> members are treated specially, since these are used by a widget to pass data to the caller. They are not modified by this function.</dd>
<dt><code>dlg_result_key</code></dt>
<dd> Test a <code>dialog</code> internal keycode to see if it corresponds to one of the push buttons on the widget such as &quot;OK&quot;. This is only useful if there are user-defined key bindings, since there are no built-in bindings that map directly to <code>DLGK_OK</code>, etc. Return true if a mapping was done.</dd>
<dl>
<dl>
<dt><code>int </code><i>dialog_key</i></dt>
<dd> is the <code>dialog</code> key to test</dd>
<dt><code>int </code><i>fkey</i></dt>
<dd> is true if this is a function key</dd>
<dt><code>int * </code><i>resultp</i></dt>
<dd> store the result of the mapping in the referenced location.</dd></dl>
</dl>
<dt><code>dlg_save_vars</code></dt>
<dd> Save <code>dialog</code>&#8216;s variables into the given variable (see <code>dlg_restore_vars</code>).</dd>
<dl>
<dl>
<dt><code>DIALOG_VARS * </code><i>save</i></dt>
<dd> is the variable into which to save.</dd></dl>
</dl>
<dt><code>dlg_set_focus</code></dt>
<dd> Set focus on the given window, making it display above other windows on the screen.</dd>
<dl>
<dl>
<dt><code>WINDOW * </code><i>parent</i></dt>
<dd> is the parent window (usually the top-level window of a widget)</dd>
<dt><code>WINDOW * </code><i>win</i></dt>
<dd> is the window on which to place focus (usually a subwindow of a widget)</dd></dl>
</dl>
<dt><code>dlg_set_result</code></dt>
<dd> Setup a fixed-buffer for the result in <code>dialog_vars.input_result</code></dd>
<dl>
<dl>
<dt><code>const char * </code><i>string</i></dt>
<dd> is the new contents for the result</dd></dl>
</dl>
<dt><code>dlg_show_string</code></dt>
<dd> Displays the string, shifted as necessary, to fit within the box and show the current character-offset.</dd>
<dl>
<dl>
<dt><code>WINDOW * </code><i>win</i></dt>
<dd> is the window within which to display</dd>
<dt><code>const char * </code><i>string</i></dt>
<dd> is the string to display</dd>
<dt><code>int </code><i>offset</i></dt>
<dd> is the starting (character, not bytes) offset</dd>
<dt><code>chtype </code><i>attr</i></dt>
<dd> is the window attribute to use for the string</dd>
<dt><code>int </code><i>y_base</i></dt>
<dd> beginning row on screen</dd>
<dt><code>int </code><i>x_base</i></dt>
<dd> beginning column on screen</dd>
<dt><code>int </code><i>x_last</i></dt>
<dd> number of columns on screen</dd>
<dt><code>bool </code><i>hidden</i></dt>
<dd> if true, do not echo input</dd>
<dt><code>bool </code><i>force</i></dt>
<dd> if true, force repaint</dd></dl>
</dl>
<dt><code>dlg_strclone</code></dt>
<dd> duplicate the string, like <code>strdup</code>.</dd>
<dl>
<dl>
<dt><code>const char * </code><i>cprompt</i></dt>
<dd> is the string to duplicate</dd></dl>
</dl>
<dt><code>dlg_strcmp</code></dt>
<dd> compare two strings, ignoring case.</dd>
<dl>
<dl>
<dt><code>const char * </code><i>a</i></dt>
<dd> is one string</dd>
<dt><code>const char * </code><i>b</i></dt>
<dd> is the other string</dd></dl>
</dl>
<dt><code>dlg_string_to_argv</code></dt>
<dd> Convert a string to an argument vector returning an index (which must be freed by the caller). The string is modified (replacing gaps between tokens with nulls).</dd>
<dl>
<dl>
<dt><code>char *</code><i>blob</i></dt>
<dd> is the string to convert.</dd></dl>
</dl>
<dt><code>dlg_sub_window</code></dt>
<dd> create a subwindow, e.g., for an input area of a widget</dd>
<dl>
<dl>
<dt><code>WINDOW * </code><i>win</i></dt>
<dd> is the parent window</dd>
<dt><code>int </code><i>height</i></dt>
<dd> is the subwindow&#8217;s height</dd>
<dt><code>int </code><i>width</i></dt>
<dd> is the subwindow&#8217;s width</dd>
<dt><code>int </code><i>y</i></dt>
<dd> is the subwindow&#8217;s top-row</dd>
<dt><code>int </code><i>x</i></dt>
<dd> is the subwindow&#8217;s left-column</dd></dl>
</dl>
<dt><code>dlg_tab_correct_str</code></dt>
<dd> If the <code>dialog_vars.tab_correct</code> is true, convert tabs to single spaces. Return the converted result. The caller is responsible for freeing the string.</dd>
<dl>
<dl>
<dt><code>char * </code><i>prompt</i></dt>
<dd> is the string to convert</dd></dl>
</dl>
<dt><code>dlg_trace</code></dt>
<dd> If the parameter is non-null, opens a trace file with that name and stores the file pointer in <code>dialog_state.trace</code>.</dd>
<dt><code>dlg_trace_chr</code></dt>
<dd> If <code>dialog_state.trace</code> is set, translate the parameters into a printable representation, log it on a &quot;chr&quot; line.</dd>
<dl>
<dl>
<dt><code>int ch</code></dt>
<dd> is the nominal keycode value.</dd>
<dt><code>int fkey</code></dt>
<dd> is nonzero if the value is really a function key. Some of these may be values declared in the DLG_KEYS_ENUM.</dd></dl>
</dl>
<dt><code>dlg_trace_msg</code></dt>
<dd> Write a formatted message to the trace file.</dd>
<dl>
<dl>
<dt><code>const char * </code><i>fmt</i></dt>
<dd> is the format of the <code>printf</code>-like message to write.</dd>
<dt><code>&#8230;</code></dt>
<dd>
 are the variables to apply to the <i>fmt</i> format.</dd></dl>
</dl>
<dt>
</dt><dd> Use the DLG_TRACE macro for portability, in case the trace feature is not compiled into the library. It uses an extra level of parentheses to work with a variable number of parameters, e.g.,</dd>
<dl>
<dt>
</dt><dd>
<pre>
DLG_TRACE((&quot;this is dialog version %s
&quot;, dialog_version()));
</pre>
</dd></dl>
<dt><code>dlg_trace_win</code></dt>
<dd> If <code>dialog_state.trace</code> is set, log a printable picture of the given window.</dd>
<dt><code>dlg_treeview</code></dt>
<dd> This is an alternate interface to &#8216;treeview&#8217; which allows the application to read the list item states back directly without putting them in the output buffer.</dd>
<dl>
<dl>
<dt><code>const char * </code><i>title</i></dt>
<dd> is the title on the top of the widget.</dd>
<dt><code>const char * </code><i>cprompt</i></dt>
<dd> is the prompt text shown within the widget.</dd>
<dt><code>int </code><i>height</i></dt>
<dd> is the desired height of the box. If zero, the height is based on the screen size.</dd>
<dt><code>int </code><i>width</i></dt>
<dd> is the desired width of the box. If zero, the height is based on the screen size.</dd>
<dt><code>int </code><i>list_height</i></dt>
<dd> is the minimum height to reserve for displaying the list. If zero, it is computed based on the given <i>height</i> and <i>width</i>.</dd>
<dt><code>int </code><i>item_no</i></dt>
<dd> is the number of rows in <i>items</i>.</dd>
<dt><code>DIALOG_LISTITEM * </code><i>items</i></dt>
<dd> is the list of items, contain tag, name, and optionally help strings (if <code>dialog_vars.item_help</code> is set). The initial selection state for each item is also in this list.</dd>
<dt><code>const char * </code><i>states</i></dt>
<dd> This is a list of characters to display for the given states. Normally a buildlist provides true (1) and false (0) values, which the widget displays as &quot;*&quot; and space, respectively. An application may set this parameter to an arbitrary null-terminated string. The widget determines the number of states from the length of this string, and will cycle through the corresponding display characters as the user presses the space-bar.</dd>
<dt><code>int * </code><i>depths</i></dt>
<dd> This is a list of depths of each item in the tree. It is a separate parameter from <i>items</i> to allow reuse of the existing functions.</dd>
<dt><code>int </code><i>flag</i></dt>
<dd> is either <i>FLAG_CHECK</i>, for checklists (multiple selections), or <i>FLAG_RADIO</i> for radiolists (a single selection).</dd>
<dt><code>int * </code><i>current_item</i></dt>
<dd> The widget sets the referenced location to the index of the current display item (cursor) when it returns.</dd></dl>
</dl>
<dt><code>dlg_trim_string</code></dt>
<dd> The <code>dialog</code> program uses this in each widget to adjust the message string, which may contain the newline character (referred to as &#8216;
&#8217;) and/or the special substring &quot;
&quot; (which can be translated into a newline character).</dd>
<dt>
</dt><dd> There are several optional features:</dd>
<dl>
<dl>
<dt>&bull;</dt>
<dd> Unless <code>dialog_vars.no_nl_expand</code> is set,</dd>
<dl>
<dl>
<dt>&bull;</dt>
<dd> If it has &quot;
&quot; substrings, the function preserves extra spaces. For instance, spaces following a newline (substring or character) are preserved to use as an indentation.</dd>
<dt>&bull;</dt>
<dd> The function changes embedded &quot;
&quot; substrings to &#8216;
&#8217; characters.</dd></dl>
</dl>
<dt>&bull;</dt>
<dd> If <code>dialog_vars.no_nl_expand</code> is not set, or if there are no &quot;
&quot; substrings, this function strips all extra spaces to simplify justification.</dd>
<dt>&bull;</dt>
<dd> If <code>dialog_vars.cr_wrap</code> is set, the function preserves &#8216;
&#8217; newline characters. Otherwise, each &#8216;
&#8217; newline character is converted to a space.</dd>
<dt>&bull;</dt>
<dd> Unless <code>dialog_vars.nocollapse</code> is set, each tab character is converted to a space, and sequences of blanks (space or tab) are reduced to a single space.</dd></dl>
</dl>
<dl>
<dl>
<dt><code>char * </code><i>src</i></dt>
<dd> is the string to trim</dd></dl>
</dl>
<dt><code>dlg_unregister_window</code></dt>
<dd> Remove the bindings for a given window.</dd>
<dl>
<dl>
<dt><code>WINDOW * </code><i>win</i></dt>
<dd> is the window from which to remove bindings</dd></dl>
</dl>
<dt><code>dlg_update_gauge</code></dt>
<dd> Update a gauge widget to show a different percentage value.</dd>
<dl>
<dl>
<dt><code>void *</code><i>objptr</i></dt>
<dd> points to the gauge object to update.</dd>
<dt><code>int </code><i>percent</i></dt>
<dd> is the new percentage value to display.</dd></dl>
</dl>
<dt><code>dlg_yes_buttoncode</code></dt>
<dd> Map the given button index for <code>dlg_yes_labels</code> into <code>dialog</code>&#8216;s exit-code.</dd>
<dl>
<dl>
<dt><code>int </code><i>button</i></dt>
<dd> is the button index</dd></dl>
</dl>
<dt><code>dlg_yes_labels</code></dt>
<dd> Return a list of buttons for Yes/No labels.</dd></dl>
<h2>SEE ALSO</h2>
<p> <code>dialog</code> (1).</p>
<h2>AUTHOR</h2>
<p> Thomas E. Dickey </p>
