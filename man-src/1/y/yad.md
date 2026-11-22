---

title: "yad(1)"
name: "yad"
section: "1"
letter: "y"
url: "/docs/linux/man/1-yad/"
description: "yad – display GTK+ dialogs in shell scripts"
---

<p> yad &#8211; display GTK+ dialogs in shell scripts </p>
<h2>SYNOPSIS</h2>
<p> <code>yad</code> [<i>OPTIONS</i>] </p>
<h2>DESCRIPTION</h2>
<p> <code>YAD</code> is a program that will display GTK+ dialogs, and return (either in the return code or on standard output) the users input. This allows you to present information, and ask for information from the user, from all manner of shell scripts. </p>
<p> <code>YAD</code> is the fork of <code>Zenity</code> program. </p>
<h2>OPTIONS</h2>
<p> This program follows the usual GNU command line syntax, with long options starting with two dashes (`-&#8216;). </p>
<h3>Dialog options</h3>
<dl>
<dt><code>&#8211;calendar</code></dt>
<dd> Display calendar dialog.</dd>
<dt><code>&#8211;color</code></dt>
<dd> Display color selection dialog.</dd>
<dt><code>&#8211;dnd</code></dt>
<dd> Display drag-and-drop box.</dd>
<dt><code>&#8211;entry</code></dt>
<dd> Display text entry dialog.</dd>
<dt><code>&#8211;icons</code></dt>
<dd> Display box with shortcut icons.</dd>
<dt><code>&#8211;file</code></dt>
<dd> Display file selection dialog.</dd>
<dt><code>&#8211;font</code></dt>
<dd> Display font selection dialog.</dd>
<dt><code>&#8211;form</code></dt>
<dd> Display form dialog</dd>
<dt><code>&#8211;html</code></dt>
<dd> Display HTML dialog</dd>
<dt><code>&#8211;list</code></dt>
<dd> Display list dialog</dd>
<dt><code>&#8211;multi-progress</code></dt>
<dd> Display multi progress bars dialog.</dd>
<dt><code>&#8211;notebook</code></dt>
<dd> Display notebook dialog.</dd>
<dt><code>&#8211;notification</code></dt>
<dd> Display notification icon.</dd>
<dt><code>&#8211;print</code></dt>
<dd> Display print dialog.</dd>
<dt><code>&#8211;progress</code></dt>
<dd> Display progress indication dialog.</dd>
<dt><code>&#8211;text-info</code></dt>
<dd> Display text information dialog.</dd>
<dt><code>&#8211;scale</code></dt>
<dd> Display scale dialog. </dd>
</dl>
<h3>General options</h3>
<dl>
<dt><code>&#8211;title=</code><i>TITLE</i></dt>
<dd> Set the dialog title.</dd>
<dt><code>&#8211;window-icon=</code><i>ICON</i></dt>
<dd> Set the window icon.</dd>
<dt><code>&#8211;width=</code><i>WIDTH</i></dt>
<dd> Set the dialog window width.</dd>
<dt><code>&#8211;height=</code><i>HEIGHT</i></dt>
<dd> Set the dialog window height.</dd>
<dt><code>&#8211;posx=</code><i>NUMBER</i></dt>
<dd> Set the X position of dialog window. <i>NUMBER</i> can be negative.</dd>
<dt><code>&#8211;posy=</code><i>NUMBER</i></dt>
<dd> Set the Y position of dialog window. <i>NUMBER</i> can be negative.</dd>
<dt><code>&#8211;geometry=</code><i>WIDTHxHEIGHT+X+Y</i></dt>
<dd> Use standard X Window geometry notation for placing dialog. When this option is used, <i>width</i>, <i>height</i>, <i>posx</i>, <i>posy</i>, <i>mouse</i> and <i>center</i> options are ignored. This option is obsolete for gtk3 builds.</dd>
<dt><code>&#8211;timeout=</code><i>TIMEOUT</i></dt>
<dd> Set the dialog timeout in seconds.</dd>
<dt><code>&#8211;timeout-indicator=</code><i>POSITION</i></dt>
<dd> Show timeout indicator in given position. Positions are <i>top</i>, <i>bottom</i>, <i>left</i> or <i>right</i>. Style of indicator may be set through the gtkrc file. See <i><a rel="nofollow" href="http://code.google.com/p/yad/wiki/TimeoutIndicator">http://code.google.com/p/yad/wiki/TimeoutIndicator</a></i> for details.</dd>
<dt><code>&#8211;parent-win=</code><i>XID</i></dt>
<dd> Specify a parent window for the dialog. This makes <i>YAD</i> possible to use as embedded GUI tool.</dd>
<dt><code>&#8211;kill-parent</code><i>[=SIGNAL]</i></dt>
<dd> Send SIGNAL to parent process. Default value of SIGNAL is a SIGTERM. SIGNAL may be specified by it&#8217;s number or symbolic name with or without SIG prefix. See <a href="/docs/linux/man/7-signal/">signal</a>(7) for details about signals.</dd>
<dt><code>&#8211;plug=</code><i>KEY</i></dt>
<dd> Run dialog in plug mode for swallow as a notebook tab. See <i>NOTEBOOK</i> section for more.</dd>
<dt><code>&#8211;tabnum=</code><i>NUMBER</i></dt>
<dd> Set the tab number for plugged dialog. See <i>NOTEBOOK</i> section for more.</dd>
<dt><code>&#8211;text=</code><i>STRING</i></dt>
<dd> Set the dialog text.</dd>
<dt><code>&#8211;text-align=</code><i>TYPE</i></dt>
<dd> Set type of dialog text justification. <i>TYPE</i> may be <i>left</i>, <i>right</i>, <i>center</i> or <i>fill</i>.</dd>
<dt><code>&#8211;image=</code><i>IMAGE</i></dt>
<dd> Set the dialog image which appears on the left side of dialog. <i>IMAGE</i> might be file name or icon name from current icon theme.</dd>
<dt><code>&#8211;image-on-top</code></dt>
<dd> Show image above main widget instead of left. This option is always on for print dialog.</dd>
<dt><code>&#8211;icon-theme=</code><i>THEME</i></dt>
<dd> Use specified GTK icon theme instead of default.</dd>
<dt><code>&#8211;expander=</code><i>TEXT</i></dt>
<dd> Hide main widget with expander. <i>TEXT</i> is an optional argument with expander&#8217;s label.</dd>
<dt><code>&#8211;button=</code><i>BUTTON:ID</i></dt>
<dd> Add the dialog button. May be used multiply times. <i>ID</i> is an exit code or a command. <i>BUTTON</i> may be gtk stock item name for predefined buttons (like gtk-close or gtk-ok) or text in a form <i>LABEL[!ICON[!TOOLTIP]]</i> where `!&#8217; is an item separator. Full list of stock items may be found in gtk-demo program, in snippet called <i>&quot;Stock Items and Icon Browser&quot;</i>. If no buttons specified <i>OK</i> and <i>Cancel</i> buttons used. See <code>EXIT STATUS</code> section for more. If <i>ID</i> have a non-numeric value it treats like a command and click on such button doesn&#8217;t close the dialog.</dd>
<dt><code>&#8211;no-buttons</code></dt>
<dd> Don&#8217;t show buttons.</dd>
<dt><code>&#8211;buttons-layout=</code><i>TYPE</i></dt>
<dd> Set buttons layout type. Possible types are: <i>spread</i>, <i>edge</i>, <i>start</i>, <i>end</i> or <i>center</i>. Default is <i>end</i>.</dd>
<dt><code>&#8211;no-markup</code></dt>
<dd> Don&#8217;t use pango markup in dialog&#8217;s text.</dd>
<dt><code>&#8211;no-escape</code></dt>
<dd> Don&#8217;t close dialog if <i>Escape</i> was pressed.</dd>
<dt><code>&#8211;always-print-result</code></dt>
<dd> Print result for aby of the return codes. This options doesn&#8217;t work if timeout was reached or <i>Escape</i> was pressed.</dd>
<dt><code>&#8211;dialog-sep</code></dt>
<dd> Show separator between dialog and buttons. Works only with gtk+-2.0.</dd>
<dt><code>&#8211;borders=</code><i>NUM</i></dt>
<dd> Set dialog window borders.</dd>
<dt><code>&#8211;sticky</code></dt>
<dd> Make window visible on all desktops.</dd>
<dt><code>&#8211;fixed</code></dt>
<dd> Make window fixed width and height.</dd>
<dt><code>&#8211;center</code></dt>
<dd> Place window on center of screen.</dd>
<dt><code>&#8211;mouse</code></dt>
<dd> Place window under mouse position.</dd>
<dt><code>&#8211;on-top</code></dt>
<dd> Place window over other windows.</dd>
<dt><code>&#8211;undecorated</code></dt>
<dd> Make window undecorated (remove title and window borders).</dd>
<dt><code>&#8211;skip-taskbar</code></dt>
<dd> Don&#8217;t show window in taskbar and pager.</dd>
<dt><code>&#8211;maximized</code></dt>
<dd> Run dialog window maximized.</dd>
<dt><code>&#8211;fullscreen</code></dt>
<dd> Run dialog in fullscreen mode. This option may not work on all window managers.</dd>
<dt><code>&#8211;splash</code></dt>
<dd> Open window with &quot;splashscreen&quot; window hints. For details see description of <i>_NET_WM_WINDOW_TYPE_SPLASH</i> in EWMH specification. The behavior of dialog with this option is HIGHLY DEPENDS on settings of your window manager.</dd>
<dt><code>&#8211;no-focus</code></dt>
<dd> Dialog window never take focus.</dd>
<dt><code>&#8211;close-on-unfocus</code></dt>
<dd> Close the dialog window when it loose the focus.</dd>
<dt><code>&#8211;selectable-labels</code></dt>
<dd> If set, user can select dialog&#8217;s text and copy it to clipboard. This option also affects on label fields in form dialog.</dd>
<dt><code>&#8211;image-path=</code><i>PATH</i></dt>
<dd> Add specified path to the standard list of directories for looking for icons. This option can be used multiply times.</dd>
<dt><code>&#8211;rest=</code><i>FILENAME</i></dt>
<dd> Read extra arguments from given file instead of command line. Each line of a file treats as a single argument.</dd>
<dt><code>&#8211;response=</code><i>NUMBER</i></dt>
<dd> Set default response value for Ctrl+Enter action.</dd>
<dt><code>&#8211;gtkrc=</code><i>FILENAME</i></dt>
<dd> Read and parse additional GTK+ settings from given file. This option doesn&#8217;t work with GTK+-3.x builds.</dd>
<dt><code>&#8211;hscroll-policy=</code><i>TYPE</i></dt>
<dd> Set the policy type for horizontal scrollbars. <i>TYPE</i> can be one of the <i>auto</i>, <i>always</i> or <i>never</i>. Default is <i>auto</i>.</dd>
<dt><code>&#8211;vscroll-policy=</code><i>TYPE</i></dt>
<dd> Set the policy type for vertical scrollbars. <i>TYPE</i> can be one of the <i>auto</i>, <i>always</i> or <i>never</i>. Default is <i>auto</i>.</dd>
<dt><code>&#8211;enable-spell</code></dt>
<dd> Enable spell checking in textview widgets</dd>
<dt><code>&#8211;spell-lang=</code><i>LANGUAGE</i></dt>
<dd> Set spell checking language to <i>LANGUAGE</i>. By default language guesses from current locale. </dd>
</dl>
<h3>Calendar options</h3>
<dl>
<dt><code>&#8211;day=</code><i>NUMBER</i></dt>
<dd> Set the calendar day.</dd>
<dt><code>&#8211;month=</code><i>NUMBER</i></dt>
<dd> Set the calendar month.</dd>
<dt><code>&#8211;year=</code><i>NUMBER</i></dt>
<dd> Set the calendar year.</dd>
<dt><code>&#8211;date-format=</code><i>PATTERN</i></dt>
<dd> Set the format for the returned date. By default is `%x&#8217;. See <i><a href="/docs/linux/man/3-strftime/">strftime</a>(3)</i> for more details.</dd>
<dt><code>&#8211;show-weeks</code></dt>
<dd> Show the week numbers at the left side of calendar.</dd>
<dt><code>&#8211;details=</code><i>FILENAME</i></dt>
<dd> Read days description from <i>FILENAME</i>.</dd></dl>
<p> File with days details must be in following format:</p>
<dl>
<dt>
</dt><dd> &lt;date&gt; &lt;description&gt;</dd></dl>
<p> <i>date</i> field is date in format, specified with <i>&#8211;date-format</i> option. <i>description</i> is a string with date details, which may include Pango markup. </p>
<h3>Color selection options</h3>
<dl>
<dt><code>&#8211;init-color=</code><i>COLOR</i></dt>
<dd> Set initial color value.</dd>
<dt><code>&#8211;gtk-palette</code></dt>
<dd> Show system palette inside color dialog.</dd>
<dt><code>&#8211;extra</code></dt>
<dd> Show extra information about color in returned string.</dd>
<dt><code>&#8211;alpha</code></dt>
<dd> Add opacity to output color string.</dd>
<dt><code>&#8211;palette</code><i>[=FILENAME]</i></dt>
<dd> Show palette and set predefined colors from given filename. By default used <i>/etc/X11/rgb.txt</i>.</dd>
<dt><code>&#8211;expand-palette</code></dt>
<dd> Expander for list of user-defined colors will be initially opened.</dd>
<dt><code>&#8211;mode=</code><i>MODE</i></dt>
<dd> Set output color mode. Possible values are <i>hex</i> or <i>rgb</i>. Default is <i>hex</i>. HEX mode looks like <i>#rrggbbaa</i>, RGB mode &#8211; <i>rgba(r, g, b, a)</i>. In RGBA mode opacity have values from 0.0 to 1.0. </dd>
</dl>
<h3>Drag-and-Drop box options</h3>
<dl>
<dt><code>&#8211;tooltip</code></dt>
<dd> Use dialog text as a tooltip for Drag-and-Drop box.</dd>
<dt><code>&#8211;command=</code><i>CMD</i></dt>
<dd> Run command when data received. Data strings pass to command as an argument. By default data just prints to stdout. </dd>
</dl>
<h3>Text entry options</h3>
<dl>
<dt><code>&#8211;entry-label=</code><i>STRING</i></dt>
<dd> Set the entry label text.</dd>
<dt><code>&#8211;entry-text=</code><i>STRING</i></dt>
<dd> Set the initial entry text or default item in combo-box.</dd>
<dt><code>&#8211;hide-text</code></dt>
<dd> Hide the entry text.</dd>
<dt><code>&#8211;completion</code></dt>
<dd> Use completion instead of combo-box.</dd>
<dt><code>&#8211;complete=</code><i>TYPE</i></dt>
<dd> Use specific type for extended completion. <i>TYPE</i> can be <i>any</i> for match any of typed words, <i>all</i> for match all of typed words or <i>regex</i> when typed text treats as regular expression.</dd>
<dt><code>&#8211;editable</code></dt>
<dd> Allow make changes to text in combo-box.</dd>
<dt><code>&#8211;numeric</code></dt>
<dd> Use spin button instead of text entry. Additional parameters in command line treats as minimum and maximum values, step value and precisions (in that order). All this values are optional. Default range is from 0 to 65535 with step 1.</dd>
<dt><code>&#8211;float-precision=</code><i>NUMBER</i></dt>
<dd> Set precision of floating point numbers. By default precision is three digits after point.</dd>
<dt><code>&#8211;licon=</code><i>IMAGE</i></dt>
<dd> Set an icon on a left side of entry.</dd>
<dt><code>&#8211;licon-action=</code><i>CMD</i></dt>
<dd> Specify a command which will be run when the left icon clicked. Output of command will be set as entry text.</dd>
<dt><code>&#8211;ricon=</code><i>IMAGE</i></dt>
<dd> Set an icon on a right side of entry.</dd>
<dt><code>&#8211;ricon-action=</code><i>CMD</i></dt>
<dd> Specify a command which will be run when the right icon clicked. Output of command will be set as entry text.</dd>
<dt><code>&#8211;num-output</code></dt>
<dd> Output index of active element instead of text for combo-box entry.</dd></dl>
<p> Any extra data specified in command line adds as an items of combo-box entry, except of numeric mode. </p>
<p> If icon specified and icon action is not given, click on icon just clear the entry. Numeric fields will ignore the icons. </p>
<h3>Iconbox options</h3>
<dl>
<dt><code>&#8211;read-dir=</code><i>PATH</i></dt>
<dd> Read .desktop files from specified directory.</dd>
<dt><code>&#8211;monitor</code></dt>
<dd> Watch for changes in directory and automatically update content of iconbox.</dd>
<dt><code>&#8211;generic</code></dt>
<dd> Use field GenericName instead of Name for shortcut label.</dd>
<dt><code>&#8211;sort-by-name</code></dt>
<dd> Use field Name instead of filename for sorting items.</dd>
<dt><code>&#8211;descend</code></dt>
<dd> Sort items in descending order. If data reads from stdin this option is useless without <i>&#8211;sort-by-name</i>.</dd>
<dt><code>&#8211;listen</code></dt>
<dd> Read data from stdin. Data must be in order &#8211; <i>Name</i>, <i>Tooltip</i>, <i>Icon</i>, <i>Command</i>, <i>InTerm</i> separated by newline. <i>InTerm</i> is a case insensitive boolean constant (<i>TRUE</i> or <i>FALSE</i>).</dd>
<dt><code>&#8211;item-width</code></dt>
<dd> Set items width.</dd>
<dt><code>&#8211;compact</code></dt>
<dd> Use compact mode. Icon and name of each item is placed in a single row.</dd>
<dt><code>&#8211;single-click</code></dt>
<dd> Activate items by single mouse click. This option may not works properly in case of compact mode.</dd>
<dt><code>&#8211;term</code></dt>
<dd> Pattern for terminal. By default use `xterm -e %s&#8217; where %s replaced by the command.</dd></dl>
<p> If both directory and stdin specified, content of iconbox will be read from directory. </p>
<h3>File selection options</h3>
<dl>
<dt><code>&#8211;filename=</code><i>FILENAME</i></dt>
<dd> Set the filename.</dd>
<dt><code>&#8211;multiple</code></dt>
<dd> Allow selection of multiple filenames in file selection dialog.</dd>
<dt><code>&#8211;directory</code></dt>
<dd> Activate directory-only selection.</dd>
<dt><code>&#8211;save</code></dt>
<dd> Activate save mode.</dd>
<dt><code>&#8211;separator=</code><i>STRING</i></dt>
<dd> Specify separator character when returning multiple filenames.</dd>
<dt><code>&#8211;confirm-overwrite</code><i>[=TEXT]</i></dt>
<dd> Confirm file selection if filename already exists. Optional argument is a text for confirmation dialog.</dd>
<dt><code>&#8211;quoted-output</code></dt>
<dd> Output values will be shell-style quoted. </dd>
</dl>
<h3>Font selection options</h3>
<dl>
<dt><code>&#8211;fontname=</code><i>FONTNAME</i></dt>
<dd> Set the initial font. <i>FONTNAME</i> is a string with font representation in the form <i>&quot;[FAMILY-LIST] [STYLE-OPTIONS] [SIZE]&quot;</i>.</dd>
<dt><code>&#8211;preview</code></dt>
<dd> Set the preview text.</dd>
<dt><code>&#8211;separate-output</code></dt>
<dd> Separate output of selected font description.</dd>
<dt><code>&#8211;separator=</code><i>STRING</i></dt>
<dd> Set output separator character. Default is `|&#8217;.</dd>
<dt><code>&#8211;quoted-output</code></dt>
<dd> Output data will be in shell-style quotes. </dd>
</dl>
<h3>Form options</h3>
<dl>
<dt><code>&#8211;field=</code><i>LABEL[:TYPE]</i></dt>
<dd> Add field to form. Type may be <i>H</i>, <i>RO</i>, <i>NUM</i>, <i>CHK</i>, <i>CB</i>, <i>CBE</i>, <i>CE</i>, <i>FL</i>, <i>SFL</i>, <i>DIR</i>, <i>CDIR</i>, <i>FN</i>, <i>MFL</i>, <i>MDIR</i>, <i>DT</i>, <i>SCL</i>, <i>CLR</i>, <i>BTN</i>, <i>FBTN</i>, <i>LBL</i> or <i>TXT</i>.<br/>
 <code>H</code> &#8211; hidden field type. All characters are displayed as the invisible char.<br/>
 <code>RO</code> &#8211; field is in read-only mode.<br/>
 <code>NUM</code> &#8211; field is a numeric. Initial value format for this field is <i>VALUE[!RANGE[!STEP![PREC]]]</i>, where <i>RANGE</i> must be in form <i>MIN..MAX</i>. `!&#8217; is a default item separator. <i>PREC</i> is a precision for decimals.<br/>
 <code>CHK</code> &#8211; checkbox field. Initial value is a case insensitive boolean constant (<i>TRUE</i> or <i>FALSE</i>).<br/>
 <code>CB</code> &#8211; combo-box field. Initial value is a list <i>VAL1!VAL2!&#8230;</i>. The separator is the same as in <i>NUM</i> field. Value started with `^&#8217; threats as default for combo-box.<br/>
 <code>CBE</code> &#8211; editable combo-box field. Initial value same as for combo-box.<br/>
 <code>CE</code> &#8211; entry with completion. Initial value same as for combo-box.<br/>
 <code>FL</code> &#8211; file selection button.<br/>
 <code>SFL</code> &#8211; field for create file.<br/>
 <code>DIR</code> &#8211; directory selection button.<br/>
 <code>CDIR</code> &#8211; field for create folder.<br/>
 <code>FN</code> &#8211; font selection button. Initial value same as in font dialog.<br/>
 <code>MFL</code> &#8211; select multiple files. Value of this field is a list of files separated by <i>item-separator</i>.<br/>
 <code>MDIR</code> &#8211; select multiple folders. Value of this field is a list of folders separated by <i>item-separator</i>.<br/>
 <code>DT</code> &#8211; date field.<br/>
 <code>SCL</code> &#8211; scale field. Value of this field in a range 0..100.<br/>
 <code>CLR</code> &#8211; color selection button. Output values for this field generates in the same manner as for color dialog.<br/>
 <code>BTN</code> &#8211; button field. Label may be in form text in a form <i>LABEL[!ICON[!TOOLTIP]]</i> where `!&#8217; is an item separator. <i>LABEL</i> is a text of button label or gtk stock id. <i>ICON</i> is a buttons icon (stock id or file name). <i>TOOLTIP</i> is an optional text for popup help string. Initial value is a command which is running when button is clicked. A special sympols <i>%N</i> in command are replaced by value of field <i>N</i>. If command starts with <i>@</i>, the output of command will be parsed and lines started with number and colon will be treats as a new field values. A quoting style for value when <i>sh -c</i> is used &#8211; a single quotes around command and double quotes around -c argument<br/>
 <code>FBTN</code> &#8211; same as button field, but with full relief of a button.<br/>
 <code>LBL</code> &#8211; text label. If field name is empty, horizontal separator line will be shown.<br/>
 <code>TXT</code> &#8211; multiline text entry. This field is always occupy all of form width. </dd>
<p> Without type field will be a simple text entry.</p>
<dt><code>&#8211;align=</code><i>TYPE</i></dt>
<dd> Set alignment of field labels. Possible types are <i>left</i>, <i>center</i> or <i>right</i>. Default is left.</dd>
<dt><code>&#8211;columns=</code><i>NUMBER</i></dt>
<dd> Set number of columns in form. Fields will be placed from top to bottom.</dd>
<dt><code>&#8211;separator=</code><i>STRING</i></dt>
<dd> Set output separator character. Default is `|&#8217;.</dd>
<dt><code>&#8211;focus-field=</code><i>NUMBER</i></dt>
<dd> Set focused field.</dd>
<dt><code>&#8211;cycle-read</code></dt>
<dd> Cycled reading of stdin data. Sending FormFeed character clears the form. This symbol may be sent as <i>echo -e &#8216;&#8217;</i>.</dd>
<dt><code>&#8211;item-separator=</code><i>STRING</i></dt>
<dd> Set separator character for combo-box or scale values. Default is `!&#8217;.</dd>
<dt><code>&#8211;date-format=</code><i>PATTERN</i></dt>
<dd> Set the format for the date fields (same as in calendar dialog).</dd>
<dt><code>&#8211;float-precision=</code><i>NUMBER</i></dt>
<dd> Set precision of floating point numbers. By default precision is three digits after point.</dd>
<dt><code>&#8211;complete=</code><i>TYPE</i></dt>
<dd> Use specific type for extended completion. <i>TYPE</i> can be <i>any</i> for match any of typed words, <i>all</i> for match all of typed words or <i>regex</i> when typed text treats as regular expression.</dd>
<dt><code>&#8211;scroll</code></dt>
<dd> Make form scrollable.</dd>
<dt><code>&#8211;quoted-output</code></dt>
<dd> Output values will be in shell-style quotes.</dd>
<dt><code>&#8211;output-by-row</code></dt>
<dd> Output field values row by row if several columns is specified.</dd>
<dt><code>&#8211;num-output</code></dt>
<dd> Output index of active element instead of text for combo-box fields.</dd></dl>
<p> Additional data in command line interprets as a default values for form fields. A special value <i>@disabled@</i> makes corresponding field inactive. If no extra arguments specified in a command line, data will be readed from stdin, one value per line. Cycled reading means that for <i>N</i> fields <i>N+1</i> value will replace the first field. Empty values are skipped when reading from stdin. </p>
<h3>HTML options</h3>
<dl>
<dt><code>&#8211;uri=</code><i>URI</i></dt>
<dd> Open specified location. <i>URI</i> can be a filename or internet address. If <i>URI</i> is not an existing file and protocol is not specified a prefix <i>http://</i> will be added to <i>URI</i>.</dd>
<dt><code>&#8211;browser</code></dt>
<dd> Turn on browser mode. In this mode all clicked links will be opened in html widget and command <i>Open</i> will be added to context menu.</dd>
<dt><code>&#8211;print-uri</code></dt>
<dd> Print clicked links to standard output. By default clicked links opens with <i>xdg-open</i>.</dd>
<dt><code>&#8211;mime=</code><i>MIME</i></dt>
<dd> Set mime type of data passed to standard input to <i>MIME</i>. Default is <i>text/html</i>.</dd>
<dt><code>&#8211;encodintg=</code><i>ENCODING</i></dt>
<dd> Set encoding of data passed to standard input to <i>ENCODING</i>. Default is <i>UTF-8</i>. </dd>
</dl>
<h3>List options</h3>
<dl>
<dt><code>&#8211;column=</code><i>STRING[:TYPE]</i></dt>
<dd> Set the column header. Types are <i>TEXT</i>, <i>NUM</i>, <i>SZ</i>, <i>FLT</i>, <i>CHK</i>, <i>RD</i>, <i>BAR</i>, <i>IMG</i>, <i>HD</i> or <i>TIP</i>. <i>TEXT</i> type is default. Use <i>NUM</i> for integers and <i>FLT</i> for double values. <i>TIP</i> is used for define tooltip column. <i>SZ</i> size column type. Works exactly like <i>NUM</i> column but shows human readable sizes instead of numbers. <i>CHK</i> (checkboxes) and <i>RD</i> (radio toggle) are a boolean columns. <i>BAR</i> is a progress bar column. Value must be between <i>0</i> and <i>100</i>. If value is outside is range it will be croped to neares legal value. <i>HD</i> type means a hidden column. Such columns are not displayes in the list, only in output. <i>IMG</i> may be path to image or icon name from currnet GTK+ icon theme. Size of icons may be set in gtk config file at GTK_ICON_SIZE_MENU position of gtk-icon-sizes. Image field prints as empty value. </dd>
<p> Special column names <i>@fore@</i>, <i>@back@</i> and <i>@font@</i> sets corresponding rows attributes. Values of those columns don&#8217;t show in results.</p>
<dt><code>&#8211;checklist</code></dt>
<dd> Use check boxes for first column.</dd>
<dt><code>&#8211;radiolist</code></dt>
<dd> Use radio toggle for first column.</dd>
<dt><code>&#8211;separator=</code><i>STRING</i></dt>
<dd> Set output separator characters.</dd>
<dt><code>&#8211;multiple</code></dt>
<dd> Allow multiple rows to be selected.</dd>
<dt><code>&#8211;editable</code></dt>
<dd> Allow changes to text.</dd>
<dt><code>&#8211;editable-cols=</code><i>LIST</i></dt>
<dd> Set the list of editable columns. <i>LIST</i> must be a string of numbers separated by comma.</dd>
<dt><code>&#8211;no-headers</code></dt>
<dd> Do not show column headers.</dd>
<dt><code>&#8211;no-click</code></dt>
<dd> Disable sorting of column content by clicking on its header.</dd>
<dt><code>&#8211;no-rules-hint</code></dt>
<dd> Don&#8217;t draw even and odd rows by a different colors. This option depends on your current gtk theme and may not work.</dd>
<dt><code>&#8211;grid-lines=</code><i>TYPE</i></dt>
<dd> Draw grid lines of type <i>TYPE</i> in list dialog. <i>TYPE</i> can be one of the <i>hor[izontal]</i>, <i>vert[ical]</i> of <i>both</i>.</dd>
<dt><code>&#8211;no-selection</code></dt>
<dd> Disable selection in list.</dd>
<dt><code>&#8211;print-all</code></dt>
<dd> Print all data from the list.</dd>
<dt><code>&#8211;print-column=</code><i>NUMBER</i></dt>
<dd> Specify what column will be printed to standard output. <i>0</i> may be used to print all columns (this is default).</dd>
<dt><code>&#8211;hide-column=</code><i>NUMBER</i></dt>
<dd> Hide a specific column.</dd>
<dt><code>&#8211;expand-column=</code><i>NUMBER</i></dt>
<dd> Set the column expandable by default. <i>0</i> sets all columns expandable.</dd>
<dt><code>&#8211;search-column=</code><i>NUMBER</i></dt>
<dd> Set the quick search column. <i>0</i> mean to disable searching. By default search mades on first column.</dd>
<dt><code>&#8211;tooltip-column=</code><i>NUMBER</i></dt>
<dd> Set the column with popup tooltips.</dd>
<dt><code>&#8211;sep-column=</code><i>NUMBER</i></dt>
<dd> Set the row separator column. If the cell value from this column equal to specified row separator value such row will be draw as separator. Separator value must be set.</dd>
<dt><code>&#8211;sep-value=</code><i>TEXT</i></dt>
<dd> Set the <i>TEXT</i> as a row separator value. This feature highly depends on your current GTK+ theme and may not work properly.</dd>
<dt><code>&#8211;limit=</code><i>NUMBER</i></dt>
<dd> Set the number of rows in list dialog. Will be shown only the last <i>NUMBER</i> rows. This option will take effect only when data reading from stdin.</dd>
<dt><code>&#8211;wrap-width=</code><i>NUMBER</i></dt>
<dd> Set the width of column before wrapping to <i>NUMBER</i>.</dd>
<dt><code>&#8211;wrap-cols=</code><i>LIST</i></dt>
<dd> Set the list of wrapped columns. <i>LIST</i> must be a string of numbers separated by comma.</dd>
<dt><code>&#8211;ellipsize=</code><i>TYPE</i></dt>
<dd> Set ellipsize mode for text columns. <i>TYPE</i> may be <i>NONE</i>, <i>START</i>, <i>MIDDLE</i> or <i>END</i>.</dd>
<dt><code>&#8211;ellipsize-cols=</code><i>LIST</i></dt>
<dd> Set the list of ellipsized columns. <i>LIST</i> must be a string of numbers separated by comma.</dd>
<dt><code>&#8211;dclick-action=</code><i>CMD</i></dt>
<dd> Set the <i>CMD</i> as a double-click command. When user double-clicked on row, <i>CMD</i> will be launched with values of all columns as an arguments. By default double-click selects row and act as <i>OK</i> button for simple lists, set the checkbox if <i>&#8211;checklist</i> specified and do nothing when list run with <i>&#8211;multiple</i> option. When double-click specified <i>Enter</i> acts as a double-click and <i>Ctrl+Enter</i> acts as an <i>OK</i> button. <i>CMD</i> may contain a special character `%s&#8217; for setting a position for arguments. By default arguments will be concatenated to the end of <i>CMD</i>. If <i>CMD</i> starts with <i>@</i>, its output will replace values of current row. This option doesn&#8217;t work with <i>&#8211;editable</i>.</dd>
<dt><code>&#8211;select-action=</code><i>CMD</i></dt>
<dd> Set the <i>CMD</i> as a action when selection is changed. <i>CMD</i> will be launched with values of all columns as an arguments. <i>CMD</i> may contain a special character `%s&#8217; for setting a position for arguments. By default arguments will be concatenated to the end of <i>CMD</i>. This option doesn&#8217;t work with <i>&#8211;multiple</i>.</dd>
<dt><code>&#8211;add-action=</code><i>CMD</i></dt>
<dd> Set the <i>CMD</i> as a action when new row is added from a context menu. Command launched without any additional arguments. Output of this command sets the new row values.</dd>
<dt><code>&#8211;regex-search</code></dt>
<dd> Use regular expressions in search for text fields.</dd>
<dt><code>&#8211;listen</code></dt>
<dd> Listen data from stdin even if command-line values was specified.</dd>
<dt><code>&#8211;quoted-output</code></dt>
<dd> Output values will be shell-style quoted.</dd>
<dt><code>&#8211;float-precision=</code><i>NUMBER</i></dt>
<dd> Set precision of floating point numbers. By default precision is three digits after point.</dd>
<dt>Sending FormFeed character to list clears it. This symbol may be sent as <i>echo -e &#8216;&#8217;</i>.</dt>
<dd>
</dd></dl>
<h3>Multi progress bars dialog options</h3>
<dl>
<dt><code>&#8211;bar=</code><i>LABEL[:TYPE]</i></dt>
<dd> Add progress bar. <i>LABEL</i> is a text label for progress bar. <i>TYPE</i> is a progress bar type. Types are: <i>NORM</i> for normal progress bar, <i>RTL</i> for inverted progress bar and <i>PULSE</i> for pulsate progress bar.</dd>
<dt><code>&#8211;vertical</code></dt>
<dd> Set vertical orientation of progress bars.</dd>
<dt><code>&#8211;align=</code><i>TYPE</i></dt>
<dd> Set alignment of bar labels. Possible types are <i>left</i>, <i>center</i> or <i>right</i>. Default is left.</dd>
<dt><code>&#8211;auto-close</code></dt>
<dd> Close dialog when 100% has been reached for all of non-pulsating progress bars.</dd>
<dt><code>&#8211;watch-bar</code><i>NUMBER</i></dt>
<dd> Watch for 100% of bar <i>NUMBER</i> for close dialog.</dd>
<dt><code>&#8211;auto-kill</code></dt>
<dd> Kill parent process if cancel button is pressed.</dd></dl>
<p> Initial values for bars set as an extra arguments. Each lines with progress data passed to stdin must be started from <i>N:</i> where <i>N</i> is a number of progress bar. </p>
<h3>Notebook options</h3>
<dl>
<dt><code>&#8211;key=</code><i>KEY</i></dt>
<dd> Set the key of the children.</dd>
<dt><code>&#8211;tab=</code><i>TEXT</i></dt>
<dd> Add tab with specified label to notebook. <i>TEXT</i> may be in a form <i>LABEL[!ICON[!TOOLTIP]]</i> where `!&#8217; is an item separator.</dd>
<dt><code>&#8211;tab-pos=</code><i>TYPE</i></dt>
<dd> Set the tabs position. Value may be <i>top</i>, <i>bottom</i>, <i>left</i>, or <i>right</i>. Default is <i>top</i>.</dd>
<dt><code>&#8211;tab-borders=</code><i>NUMBER</i></dt>
<dd> Set the borders width around widget in tabs.</dd></dl>
<p> See <code>NOTEBOOK and PANED</code> section for more about notebook dialog. </p>
<h3>Notification options</h3>
<dl>
<dt><code>&#8211;command=</code><i>CMD</i></dt>
<dd> Set the command running when clicked on the icon. Default action is <i>quit</i> if <i>&#8211;listen</i> not specified.</dd>
<dt><code>&#8211;listen</code></dt>
<dd> Listen for commands on stdin. See <code>NOTIFICATION</code> section.</dd>
<dt><code>&#8211;separator=</code><i>STRING</i></dt>
<dd> Set separator character for menu values. Default is <i>|</i>.</dd>
<dt><code>&#8211;item-separator=</code><i>STRING</i></dt>
<dd> Set separator character for menu items. Default is <i>!</i>.</dd>
<dt><code>&#8211;menu=</code><i>STRING</i></dt>
<dd> Set initial menu for right-click.</dd>
<dt><code>&#8211;no-middle</code></dt>
<dd> Disable exit on middle click.</dd>
<dt><code>&#8211;hidden</code></dt>
<dd> Doesn&#8217;t show icon at startup.</dd></dl>
<p> See <code>NOTIFICATION</code> section for more about separators. </p>
<h3>Paned options</h3>
<dl>
<dt><code>&#8211;key=</code><i>KEY</i></dt>
<dd> Set the key of the children.</dd>
<dt><code>&#8211;orient=</code><i>TYPE</i></dt>
<dd> Set orientation of panes inside dialog. <i>TYPE</i> may be in <i>hor[izontal]</i> or <i>vert[ical]</i>.</dd>
<dt><code>&#8211;splitter=</code><i>POS</i></dt>
<dd> Set the initial splitter position.</dd></dl>
<p> See <code>NOTEBOOK and PANED</code> section for more about paned dialog. </p>
<h3>Picture options</h3>
<dl>
<dt><code>&#8211;size=</code><i>VALUE</i></dt>
<dd> Set initial size of picture. Available values are <i>fit</i> for fitting image in window or <i>orig</i> for show picture in original size.</dd>
<dt><code>&#8211;inc=</code>NUMBER</dt>
<dd> Set increment value for scaling image.</dd>
<dt><code>&#8211;filename=</code><i>FILENAME</i></dt>
<dd> Set picture filename.</dd></dl>
<p> Some actions on a picture like scaling or rotating available from popup menu. Those actions can be made only on static images. </p>
<h3>Print options</h3>
<dl>
<dt><code>&#8211;type=</code><i>TYPE</i></dt>
<dd> Set source file type. <i>TYPE</i> may be a <i>TEXT</i> for text files, <i>IMAGE</i> for image files or <i>RAW</i> for files in postscript or pdf formats.</dd>
<dt><code>&#8211;filename=</code><i>FILENAME</i></dt>
<dd> Set name or path to the source file.</dd>
<dt><code>&#8211;headers</code></dt>
<dd> Add headers to the top of page with filename and page number. This option doesn&#8217;t work for <i>RAW</i> type.</dd>
<dt><code>&#8211;add-preview</code></dt>
<dd> Add <i>Preview</i> button to the print dialog. This option doesn&#8217;t work for <i>RAW</i> type.</dd>
<dt><code>&#8211;fontname=</code><i>FONTNAME</i></dt>
<dd> Set the font for printing text. <i>FONTNAME</i> is a string with font representation in the form <i>&quot;[FAMILY-LIST] [STYLE-OPTIONS] [SIZE]&quot;</i>. This option works only for <i>TEXT</i> type. </dd>
</dl>
<h3>Progress options</h3>
<p> When the &#8211;progress option is used, yad reads lines of progress data from stdin. When the lines begin with <i>#</i> the text after <i>#</i> is displayed in the progress bar label. Numeric values treats like a persents for progress bar.</p>
<dl>
<dt><code>&#8211;progress-text=</code><i>TEXT</i></dt>
<dd> Set text in progress bar to <i>TEXT</i>.</dd>
<dt><code>&#8211;percentage=</code><i>NUMBER</i></dt>
<dd> Set initial percentage.</dd>
<dt><code>&#8211;rtl</code></dt>
<dd> Set Right-To-Left progress bar direction.</dd>
<dt><code>&#8211;auto-close</code></dt>
<dd> Close dialog when 100% has been reached.</dd>
<dt><code>&#8211;auto-kill</code></dt>
<dd> Kill parent process if cancel button is pressed.</dd>
<dt><code>&#8211;pulsate</code></dt>
<dd> Pulsate progress bar.</dd>
<dt><code>&#8211;enable-log</code><i>[=TEXT]</i></dt>
<dd> Show log window. This window gathers all of lines from stdin, started from <i>#</i> instead of setting appropriate progress labels. Optional argument <i>TEXT</i> is a text label for window expander.</dd>
<dt><code>&#8211;log-on-top</code></dt>
<dd> Place log window above progress bar.</dd>
<dt><code>&#8211;log-expanded</code></dt>
<dd> Start with expanded log window.</dd>
<dt><code>&#8211;log-height</code></dt>
<dd> Set the height of log window. </dd>
</dl>
<h3>Multiprogress options</h3>
<dl>
<dt><code>&#8211;bar=</code><i>LABEL[:TYPE]</i></dt>
<dd> Add the progress bar with type <i>TYPE</i>. <i>TYPE</i> can be one of the <i>norm</i> for average progress bar, <i>rtl</i> for progress bar with inverted direction, <i>pulse</i> for pulsating progress bar (m,oves on receiving data) or <i>perm</i> for permanent pulsatin progress bar. <i>prem</i> progress bar understant two commands &#8211; <i>start</i> for start movement and <i>stop</i> for stop it.</dd>
<dt><code>&#8211;watch-bar=</code><i>NUMBER</i></dt>
<dd> Watch for specific bar for auto closing.</dd>
<dt><code>&#8211;align=</code><i>TYPE</i></dt>
<dd> Set alignment of bar labels. <i>TYPE</i> can be <i>left</i>, <i>center</i> or <i>right</i>.</dd>
<dt><code>&#8211;auto-close</code></dt>
<dd> Dismiss the dialog when 100% of all bars (or only watching bar) has been reached.</dd>
<dt><code>&#8211;auto-kill</code></dt>
<dd> Kill parent process if cancel button was pressed. </dd>
</dl>
<h3>Text info options</h3>
<dl>
<dt><code>&#8211;filename=</code><i>FILENAME</i></dt>
<dd> Open specified file.</dd>
<dt><code>&#8211;editable</code></dt>
<dd> Allow changes to text.</dd>
<dt><code>&#8211;fore=</code><i>COLOR</i></dt>
<dd> Set foreground color of text.</dd>
<dt><code>&#8211;back=</code><i>COLOR</i></dt>
<dd> Set background color of text.</dd>
<dt><code>&#8211;fontname=</code><i>FONTNAME</i></dt>
<dd> Set text font. <i>FONTNAME</i> must be in a Pango font description format. By default <i>Monospace</i> is used.</dd>
<dt><code>&#8211;wrap</code></dt>
<dd> Enable text wrapping.</dd>
<dt><code>&#8211;justify=</code><i>TYPE</i></dt>
<dd> Set justification. <i>TYPE</i> may be <i>left</i>, <i>right</i>, <i>center</i> or <i>fill</i>. Default is <i>left</i>.</dd>
<dt><code>&#8211;margins=</code><i>NUMBER</i></dt>
<dd> Set text margins to <i>NUMBER</i>.</dd>
<dt><code>&#8211;tail</code></dt>
<dd> Autoscroll to end when new text appears. Works only when text is read from stdin.</dd>
<dt><code>&#8211;show-cursor</code></dt>
<dd> Show cursor in read-only mode.</dd>
<dt><code>&#8211;show-uri</code></dt>
<dd> Make links in text clickable. Links opens with <i>xdg-open</i> command.</dd>
<dt><code>&#8211;uri-color</code></dt>
<dd> Set color for links. Default is <i>blue</i>.</dd>
<dt><code>&#8211;lang=LANGUAGE</code></dt>
<dd> Highlight syntax for specified <i>LANGUAGE</i>. This option works only if yad builds with gtksourceview.</dd>
<dt><code>&#8211;listen</code></dt>
<dd> Listen data from stdin even if filename was specified. </dd>
<p> Sending FormFeed character to text dialog clears it. This symbol may be sent as <i>echo -e &#8216;&#8217;</i>. Pressing <i>Ctrl+S</i> popups the search entry in text dialog. </p>
</dl>
<h3>Scale options</h3>
<dl>
<dt><code>&#8211;value=</code><i>VALUE</i></dt>
<dd> Set initial value.</dd>
<dt><code>&#8211;min-value=</code><i>VALUE</i></dt>
<dd> Set minimum value.</dd>
<dt><code>&#8211;max-value=</code><i>VALUE</i></dt>
<dd> Set maximum value.</dd>
<dt><code>&#8211;step=</code><i>VALUE</i></dt>
<dd> Set step size.</dd>
<dt><code>&#8211;page=</code><i>VALUE</i></dt>
<dd> Set paging size. By default page value is STEP*10.</dd>
<dt><code>&#8211;print-partial</code></dt>
<dd> Print partial values.</dd>
<dt><code>&#8211;hide-value</code></dt>
<dd> Hide value.</dd>
<dt><code>&#8211;vertical</code></dt>
<dd> Show vertical scale.</dd>
<dt><code>&#8211;invert</code></dt>
<dd> Invert scale direction.</dd>
<dt><code>&#8211;inc-buttons</code></dt>
<dd> Show buttons on edges of a scale for increasing or decreasing scale value.</dd>
<dt><code>&#8211;mark=</code><i>[NAME]:VALUE</i></dt>
<dd> Add a mark to scale. May be used multiply times. <i>NAME</i> is an optional arguments for set label to mark. </dd>
</dl>
<h3>File filters options</h3>
<dl>
<dt><code>&#8211;file-filter=</code><i>NAME | PATTERN1 PATTERN2 &#8230;</i></dt>
<dd> Add a filename filter. <i>NAME</i> is a displayed filter name, <i>PATTERN</i> is a shell-style filename pattern (for example *.txt). This option may be used multiply times.</dd>
<dt><code>&#8211;mime-filter=</code><i>NAME | MIME1 MIME2 &#8230;</i></dt>
<dd> Add a mime-type filter. <i>NAME</i> is a displayed filter name, <i>PATTERN</i> is a name of mime type (for example text/plain). This option may be used multiply times.</dd>
<dt><code>&#8211;image-filter=</code><i>[NAME]</i></dt>
<dd> Add filter for images supported by gdk-pixbuf library. <i>NAME</i> in as optional name for this filter.</dd>
<dt><code>&#8211;add-preview</code></dt>
<dd> Add preview widget. Preview images loads from large or normal thumbnails according to XDG Thumbnails specification v0.8.0 (<a rel="nofollow" href="http://standards.freedesktop.org/thumbnail-spec/latest/)">http://standards.freedesktop.org/thumbnail-spec/latest/)</a> or creates by yad for image files and saves as large thumbnails. </dd>
<p> This options applies to all of yad&#8217;s file chooser dialogs. </p>
</dl>
<h3>Miscellaneous options</h3>
<dl>
<dt><code>-?, &#8211;help</code></dt>
<dd> Show summary of options.</dd>
<dt><code>&#8211;about</code></dt>
<dd> Display an about dialog.</dd>
<dt><code>&#8211;version</code></dt>
<dd> Show version of program. </dd>
</dl>
<p> Also the standard GTK+ options are accepted. </p>
<h2>NOTEBOOK and PANED</h2>
<p> Notebook is a complex dialog which swallow other dialogs in his tabs. Dialogs identifies by unique key (integer) and must be runs in a special plug mode (&#8211;plug option). Following example runs notebook dialog with two tabs, first has a simple text and second is an entry dialog. </p>
<pre><code>
#!/ bin / sh
yad-- plug = 12345 --tabnum = 1 --text = "first tab with text" &amp; &gt; res1 &amp;
                                                                       yad-- plug = 12345 --tabnum = 2 --text = "second tab" --entry &amp; &gt; res2 &amp;
                                                                                                                                             yad-- notebook-- key = 12345 --tab = "Tab 1" --tab = "Tab 2"
</code></pre>
<p> NOTE: The order of output results for tabs is undefined! </p>
<p> Paned works in a same manner as a notebook with one restriction &#8211; only first and secong plug dialogs will be swallowed to panes. </p>
<h2>NOTIFICATION</h2>
<p> Allows commands to be sent to yad in the form <code>command:args</code>. Possible commands are <i>icon</i>, <i>tooltip</i>, <i>visible</i>, <i>action</i>, <i>menu</i> and <i>quit</i>.</p>
<dl>
<dt><code>icon:ICONNAME</code></dt>
<dd> Set notification icon to ICONNAME.</dd>
<dt><code>tooltip:STRING</code></dt>
<dd> Set notification tooltip.</dd>
<dt><code>visible:[true|false|blink]</code></dt>
<dd> Set notification icon to visible, invisible or blinking states.</dd>
<dt><code>action:COMMAND</code></dt>
<dd> Specify the command running when click on the icon. Special string <i>&quot;quit&quot;</i> exit the program.</dd>
<dt><code>menu:STRING</code></dt>
<dd> Set popup menu for notification icon. STRING must be in form <i>name1[!action1[!icon1]]|name2[!action2[!icon2]]&#8230;</i>. Empty name add separator to menu. Separator character for values (e.g. `|&#8217;) sets with &#8211;separator argument. Separator character for menu items (e.g. `!&#8217;) sets with &#8211;item-separator argument.</dd>
<dt><code>quit</code></dt>
<dd> Exit the program. Middle click on icon also send <i>quit</i> command. </dd>
</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt><code>YAD_OPTIONS</code></dt>
<dd> This variable can holds some default options for yad. All options in this variable may be redefined from command line.</dd>
<dt><code>YAD_PID</code></dt>
<dd> This variable sets to the value of current dialog&#8217;s pid and accessible in all dialog children.</dd>
<dt><code>YAD_XID</code></dt>
<dd> This variable sets to the value of current dialog&#8217;s X Window ID and accessible in all dialog children. This variable is not set in print and notification dialogs, and in a dialogs which acts as a notebook children. </dd>
</dl>
<h2>USER DEFINED SIGNALS</h2>
<dl>
<dt><code>SIGUSR1</code></dt>
<dd> Close dialog with 0 exit code.</dd>
<dt><code>SIGUSR2</code></dt>
<dd> Close dialog with 1 exit code. </dd>
</dl>
<h2>EXIT STATUS</h2>
<dl>
<dt><code>0</code></dt>
<dd> The user has pressed <i>OK</i> button</dd>
<dt><code>1</code></dt>
<dd> The user has pressed <i>Cancel</i> button</dd>
<dt><code>70</code></dt>
<dd> The dialog has been closed because the timeout has been reached.</dd>
<dt><code>252</code></dt>
<dd> The dialog has been closed by pressing <i>Esc</i> or used the window functions to close the dialog</dd>
<dt>Exit codes for user-specified buttons must be specified in command line. Even exit code mean to print result, odd just return exit code.</dt>
<dd>
</dd></dl>
<h2>WIDGETS NAMES</h2>
<dl>
<dt>The look and feel of yad&#8217;s dialogs can be customized through gtkrc file. Here is the names of yad&#8217;s widgets:</dt>
<dd>
<table>
<tr VALIGN=top>
<td>Widget name</td>
<td>Widget type</td>
<td>Description
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>yad-dialog-window</td>
<td>GtkDialog</td>
<td>Dialog window
</td>
</tr>
<tr VALIGN=top>
<td>yad-dialog-image</td>
<td>GtkImage</td>
<td>Dialog image
</td>
</tr>
<tr VALIGN=top>
<td>yad-dialog-label</td>
<td>GtkLabel</td>
<td>Dialog text
</td>
</tr>
<tr VALIGN=top>
<td>yad-calendar-widget</td>
<td>GtkCalendar</td>
<td>Calendar widget
</td>
</tr>
<tr VALIGN=top>
<td>yad-color-widget</td>
<td>GtkColorChooser</td>
<td>Color selection widget
</td>
</tr>
<tr VALIGN=top>
<td>yad-color-palette</td>
<td>GtkTreeView</td>
<td>Predefined colors list
</td>
</tr>
<tr VALIGN=top>
<td>yad-entry-label</td>
<td>GtkLabel</td>
<td>Entry label
</td>
</tr>
<tr VALIGN=top>
<td>yad-entry-widget</td>
<td>GtkEntry</td>
<td>Entry widget
</td>
</tr>
<tr VALIGN=top>
<td>yad-entry-spin</td>
<td>GtkSpinButton</td>
<td>Entry widget for numeric values
</td>
</tr>
<tr VALIGN=top>
<td>yad-entry-combo</td>
<td>GtkComboBox</td>
<td>Entry widget with combo
</td>
</tr>
<tr VALIGN=top>
<td>yad-entry-edit-combo</td>
<td>GtkComboBoxEntry</td>
<td>Entry widget with editable combo
</td>
</tr>
<tr VALIGN=top>
<td>yad-file-widget</td>
<td>GtkFileChooser</td>
<td>File selection widget
</td>
</tr>
<tr VALIGN=top>
<td>yad-font-widget</td>
<td>GtkFontChooser</td>
<td>Font selection widget
</td>
</tr>
<tr VALIGN=top>
<td>yad-form-flabel</td>
<td>GtkLabel</td>
<td>Field label in form
</td>
</tr>
<tr VALIGN=top>
<td>yad-form-button</td>
<td>GtkButton</td>
<td>Button field in form
</td>
</tr>
<tr VALIGN=top>
<td>yad-form-entry</td>
<td>GtkEntrfy</td>
<td>Entry field in form
</td>
</tr>
<tr VALIGN=top>
<td>yad-form-spin</td>
<td>GtkSpinButton</td>
<td>Numeric entry field in form
</td>
</tr>
<tr VALIGN=top>
<td>yad-form-check</td>
<td>GtkCheckButton</td>
<td>Checkbox field in form
</td>
</tr>
<tr VALIGN=top>
<td>yad-form-combo</td>
<td>GtkComboBox</td>
<td>Combo field in form
</td>
</tr>
<tr VALIGN=top>
<td>yad-form-edit-combo</td>
<td>GtkComboBoxEntry</td>
<td>Editable combo field in form
</td>
</tr>
<tr VALIGN=top>
<td>yad-form-file</td>
<td>GtkFileChooserButton</td>
<td>File or directory field in form
</td>
</tr>
<tr VALIGN=top>
<td>yad-form-font</td>
<td>GtkFontChooserButton</td>
<td>Font field in form
</td>
</tr>
<tr VALIGN=top>
<td>yad-form-color</td>
<td>GtkColorChooserButton</td>
<td>Color field in form
</td>
</tr>
<tr VALIGN=top>
<td>yad-form-label</td>
<td>GtkLabel</td>
<td>Label field in form
</td>
</tr>
<tr VALIGN=top>
<td>yad-form-scale</td>
<td>GtkScale</td>
<td>Scale widget in form
</td>
</tr>
<tr VALIGN=top>
<td>yad-form-separator</td>
<td>GtkSeparator</td>
<td>Separator in form
</td>
</tr>
<tr VALIGN=top>
<td>yad-form-text</td>
<td>GtkTextView</td>
<td>Multiline text field in form
</td>
</tr>
<tr VALIGN=top>
<td>yad-icons-full</td>
<td>GtkIconView</td>
<td>Icons widget for normal mode
</td>
</tr>
<tr VALIGN=top>
<td>yad-icons-compact</td>
<td>GtkTreeView</td>
<td>Icons widget for compact mode
</td>
</tr>
<tr VALIGN=top>
<td>yad-list-widget</td>
<td>GtkTreeView</td>
<td>List widget
</td>
</tr>
<tr VALIGN=top>
<td>yad-notebook-widget</td>
<td>GtkNotebook</td>
<td>Notebook widget
</td>
</tr>
<tr VALIGN=top>
<td>yad-paned-widget</td>
<td>GtkPaned</td>
<td>Horizontal or vertical pane widget
</td>
</tr>
<tr VALIGN=top>
<td>yad-progress-widget</td>
<td>GtkProgressBar</td>
<td>Progressbar widget
</td>
</tr>
<tr VALIGN=top>
<td>yad-scale-widget</td>
<td>GtkScale</td>
<td>Scale widget
</td>
</tr>
<tr VALIGN=top>
<td>yad-text-widget</td>
<td>GtkTextView</td>
<td>Text info widget
</td>
</tr>
<tr VALIGN=top>
<td>yad-timeout-indicator</td>
<td>GtkProgreeBar</td>
<td>Timeout indicator
</td>
</tr>
</table>
</dd></dl>
<h2>FILES</h2>
<dl>
<dt><code>yad.conf</code></dt>
<dd> YAD default settings. <i>yad.conf</i> placed in <i>$XDG_CONFIG_HOME</i> or <i>$HOME/.config</i> directory. This file contain comments on every defaults and will be automatically recreated on yad&#8217;d start if it doesn&#8217;t exists. </dd>
</dl>
<h2>EXAMPLES</h2>
<p> Display a file selector with the title <i>Select a file to remove</i>. The file selected is returned on standard output.</p>
<dl>
<dt>
</dt><dd> yad &#8211;title=&quot;Select a file to remove&quot; &#8211;file-selection</dd></dl>
<p> Display a text entry dialog with the title <i>Select Host</i> and the text <i>Select the host you would like to flood-ping</i>. The entered text is returned on standard output.</p>
<dl>
<dt>
</dt><dd> yad &#8211;title &quot;Select Host&quot; &#8211;entry &#8211;text &quot;Select the host you would like to flood-ping&quot;</dd></dl>
<p> Display a dialog, asking <i>Microsoft Windows has been found! Would you like to remove it?</i>. The return code will be 0 (true in shell) if <i>YES</i> is selected, and 1 (false) if <i>NO</i> is selected.</p>
<dl>
<dt>
</dt><dd> yad &#8211;image &quot;dialog-question&quot; &#8211;title &quot;Alert&quot; &#8211;button=gtk-yes:0 &#8211;button=gtk-no:1 &#8211;text &quot;Microsoft Windows has been found! Would you like to remove it?&quot;</dd></dl>
<p> Show the search results in a list dialog with the title <i>Search Results</i> and the text <i>Finding all header files&#8230;</i>.</p>
<dl>
<dt>
</dt><dd> find . -name &#8216;*.h&#8217; | yad &#8211;list &#8211;title &quot;Search Results&quot; &#8211;text &quot;Finding all header files..&quot; &#8211;column &quot;Files&quot;</dd></dl>
<p> Show an icon in the notification area</p>
<dl>
<dt>
</dt><dd> yad &#8211;notification &#8211;image=update.png &#8211;text &quot;System update necessary!&quot; &#8211;command &quot;xterm -e apt-get upgrade&quot;</dd></dl>
<p> Display a weekly shopping list in a check list dialog with <i>Apples</i> and <i>Oranges</i> pre selected</p>
<dl>
<dt>
</dt><dd> yad &#8211;list &#8211;checklist &#8211;column &quot;Buy&quot; &#8211;column &quot;Item&quot; TRUE Apples TRUE Oranges FALSE Pears FALSE Toothpaste</dd></dl>
<p> Display a progress dialog while searching for all the postscript files in your home directory</p>
<dl>
<dt>
</dt><dd> find $HOME -name &#8216;*.ps&#8217; | yad &#8211;progress &#8211;pulsate</dd></dl>
<p> Display a box with all of the installed desktop applications</p>
<dl>
<dt>
</dt><dd> yad &#8211;icons &#8211;read-dir=/usr/share/applications </dd>
</dl>
<h2>DEVELOPMENT</h2>
<p> There are some developers features providing with YAD.</p>
<dl>
<dt><i>YAD icon browser</i> is a graphical tool for discover icons in current or user-specified GTK+ icon theme. Launch it as</dt>
<dd>
</dd><dt>
</dt><dd> yad-icon-browser [theme]</dd></dl>
<p> When using autoconf you may use special m4 macro <i>AM_PATH_YAD</i> for looking for yad and check it version. Usage of this macro is</p>
<dl>
<dt>
</dt><dd> AM_PATH_YAD([MINIMUM-VERSION],\ [ACTION-IF-FOUND],\ [ACTION-IF-NOT-FOUND])</dd></dl>
<h2>AUTHORS</h2>
<p> <code>Yad</code> was written by Victor Ananjevsky &lt;ananasik [at] gmail.com&gt;. Yad icon created by Bogdan Lisovich. </p>
<h2>SEE ALSO</h2>
<p> <code>gdialog</code>(1), <code><a href="/docs/linux/man/1-dialog/">dialog</a></code>(1), <code><a href="/docs/linux/man/1-zenity/">zenity</a></code>(1) </p>
