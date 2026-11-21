---

title: "matedialog(1)"
name: "matedialog"
section: "1"
letter: "m"
url: "/docs/linux/man/1-matedialog/"
description: "matedialog – display GTK+ dialogs"
---

<h2>NAME</h2>
<p> matedialog &#8211; display GTK+ dialogs</p>
<p> <code>matedialog</code> [<i>options</i>]</p>
<p> <code>matedialog</code> is a program that will display GTK+ dialogs, and return (either in the return code, or on standard output) the users input. This allows you to present information, and ask for information from the user, from all manner of shell scripts. </p>
<p> For example, <code>matedialog &#8211;question</code> will return either 0 or 1, depending on whether the user pressed <i>OK</i> or <i>Cancel</i>. <code>matedialog &#8211;entry</code> will output on standard output what the user typed into the text entry field. </p>
<p> Comprehensive documentation is available in the MATE Help Browser, under <i>MATE/Utilities</i>.</p>
<h2>OPTIONS</h2>
<p> This program follows the usual GNU command line syntax, with long options starting with two dashes (`-&#8216;). </p>
<p> Dialog options </p>
<dl>
<dt><code>&#8211;calendar</code></dt>
<dd> Display calendar dialog</dd>
<dt><code>&#8211;entry</code></dt>
<dd> Display text entry dialog</dd>
<dt><code>&#8211;error</code></dt>
<dd> Display error dialog</dd>
<dt><code>&#8211;file-selection</code></dt>
<dd> Display file selection dialog</dd>
<dt><code>&#8211;info</code></dt>
<dd> Display info dialog</dd>
<dt><code>&#8211;list</code></dt>
<dd> Display list dialog</dd>
<dt><code>&#8211;notification</code></dt>
<dd> Display notification icon</dd>
<dt><code>&#8211;progress</code></dt>
<dd> Display progress indication dialog</dd>
<dt><code>&#8211;question</code></dt>
<dd> Display question dialog</dd>
<dt><code>&#8211;text-info</code></dt>
<dd> Display text information dialog</dd>
<dt><code>&#8211;warning</code></dt>
<dd> Display warning dialog</dd>
<dt><code>&#8211;scale</code></dt>
<dd> Display scale dialog</dd>
<dt><code>&#8211;color-selection</code></dt>
<dd> Display color selection dialog </dd>
</dl>
<p> General options </p>
<dl>
<dt><code>&#8211;title=TITLE</code></dt>
<dd> Set the dialog title</dd>
<dt><code>&#8211;window-icon=ICONPATH</code></dt>
<dd> Set the window icon with the path to an image. Alternatively, one of the four stock icons can be used: &#8216;error&#8217;, &#8216;info&#8217;, &#8216;question&#8217; or &#8216;warning&#8217;</dd>
<dt><code>&#8211;width=WIDTH</code></dt>
<dd> Set the dialog width</dd>
<dt><code>&#8211;height=HEIGHT</code></dt>
<dd> Set the dialog height</dd>
<dt><code>&#8211;timeout=TIMEOUT</code></dt>
<dd> Set the dialog timeout in seconds</dd></dl>
<p> Calendar options </p>
<dl>
<dt><code>&#8211;text=STRING</code></dt>
<dd> Set the dialog text</dd>
<dt><code>&#8211;day=INT</code></dt>
<dd> Set the calendar day</dd>
<dt><code>&#8211;month=INT</code></dt>
<dd> Set the calendar month</dd>
<dt><code>&#8211;year=INT</code></dt>
<dd> Set the calendar year</dd>
<dt><code>&#8211;date-format=PATTERN</code></dt>
<dd> Set the format for the returned date. The default depends on the user locale or be set with the strftime style. For example %A %d/%m/%y </dd>
</dl>
<p> Text entry options </p>
<dl>
<dt><code>&#8211;text=STRING</code></dt>
<dd> Set the dialog text</dd>
<dt><code>&#8211;entry-text=STRING</code></dt>
<dd> Set the entry text</dd>
<dt><code>&#8211;hide-text</code></dt>
<dd> Hide the entry text </dd>
</dl>
<p> Error options</p>
<dl>
<dt><code>&#8211;text=STRING</code></dt>
<dd> Set the dialog text</dd>
<dt><code>&#8211;no-wrap</code></dt>
<dd> Do not enable text wrapping </dd>
</dl>
<p> File selection options</p>
<dl>
<dt><code>&#8211;filename=FILENAME</code></dt>
<dd> Set the file or directory to be selected by default</dd>
<dt><code>&#8211;multiple</code></dt>
<dd> Allow selection of multiple filenames in file selection dialog</dd>
<dt><code>&#8211;directory</code></dt>
<dd> Activate directory-only selection</dd>
<dt><code>&#8211;save</code></dt>
<dd> Activate save mode</dd>
<dt><code>&#8211;separator=SEPARATOR</code></dt>
<dd> Specify separator character when returning multiple filenames</dd>
<dt><code>&#8211;confirm-overwrite</code></dt>
<dd> Confirm file selection if filename already exists</dd>
<dt><code>&#8211;file-filter=NAME | PATTERN1 PATTERN2</code></dt>
<dd> Sets a filename filter </dd>
</dl>
<p> Info options</p>
<dl>
<dt><code>&#8211;text=STRING</code></dt>
<dd> Set the dialog text</dd>
<dt><code>&#8211;no-wrap</code></dt>
<dd> Do not enable text wrapping </dd>
</dl>
<p> List options </p>
<dl>
<dt><code>&#8211;text=STRING</code></dt>
<dd> Set the dialog text</dd>
<dt><code>&#8211;column=STRING</code></dt>
<dd> Set the column header</dd>
<dt><code>&#8211;checklist</code></dt>
<dd> Use check boxes for first column</dd>
<dt><code>&#8211;radiolist</code></dt>
<dd> Use radio buttons for first column</dd>
<dt><code>&#8211;separator=STRING</code></dt>
<dd> Set output separator character</dd>
<dt><code>&#8211;multiple</code></dt>
<dd> Allow multiple rows to be selected</dd>
<dt><code>&#8211;editable</code></dt>
<dd> Allow changes to text</dd>
<dt><code>&#8211;print-column=NUMBER</code></dt>
<dd> Specify what column to print to standard output. The default is to return the first column. &#8216;ALL&#8217; may be used to print all columns.</dd>
<dt><code>&#8211;hide-column=NUMBER</code></dt>
<dd> Hide a specific column</dd>
<dt><code>&#8211;hide-header</code></dt>
<dd> Hides the column headers </dd>
</dl>
<p> Notification options </p>
<dl>
<dt><code>&#8211;text=STRING</code></dt>
<dd> Set the notification text</dd>
<dt><code>&#8211;listen</code></dt>
<dd> Listen for commands on stdin. Commands include &#8216;message&#8217;, &#8216;tooltip&#8217;, &#8216;icon&#8217;, and &#8216;visible&#8217; separated by a colon. For example, &#8216;message: Hello world&#8217;, &#8216;visible: false&#8217;, or &#8216;icon: /path/to/icon&#8217;. The icon command also accepts the four stock icon: &#8216;error&#8217;, &#8216;info&#8217;, &#8216;question&#8217;, and &#8216;warning&#8217; </dd>
</dl>
<p> Progress options </p>
<dl>
<dt><code>&#8211;text=STRING</code></dt>
<dd> Set the dialog text</dd>
<dt><code>&#8211;percentage=INT</code></dt>
<dd> Set initial percentage</dd>
<dt><code>&#8211;auto-close</code></dt>
<dd> Close dialog when 100% has been reached</dd>
<dt><code>&#8211;auto-kill</code></dt>
<dd> Kill parent process if cancel button is pressed</dd>
<dt><code>&#8211;pulsate</code></dt>
<dd> Pulsate progress bar</dd>
<dt><code>&#8211;no-cancel</code></dt>
<dd> Hides the cancel button </dd>
</dl>
<p> Question options </p>
<dl>
<dt><code>&#8211;text=STRING</code></dt>
<dd> Set the dialog text</dd>
<dt><code>&#8211;no-wrap</code></dt>
<dd> Do not enable text wrapping</dd>
<dt><code>&#8211;ok-label</code></dt>
<dd> Set the text of the OK button</dd>
<dt><code>&#8211;cancel-label</code></dt>
<dd> Set the text of the cancel button </dd>
</dl>
<p> Text options </p>
<dl>
<dt><code>&#8211;filename=FILENAME</code></dt>
<dd> Open file</dd>
<dt><code>&#8211;editable</code></dt>
<dd> Allow changes to text </dd>
</dl>
<p> Warning options </p>
<dl>
<dt><code>&#8211;text=STRING</code></dt>
<dd> Set the dialog text</dd>
<dt><code>&#8211;no-wrap</code></dt>
<dd> Do not enable text wrapping </dd>
</dl>
<p> Scale options </p>
<dl>
<dt><code>&#8211;text=STRING</code></dt>
<dd> Set the dialog text</dd>
<dt><code>&#8211;value=VALUE</code></dt>
<dd> Set initial value</dd>
<dt><code>&#8211;min-value=VALUE</code></dt>
<dd> Set minimum value</dd>
<dt><code>&#8211;max-value=VALUE</code></dt>
<dd> Set maximum value</dd>
<dt><code>&#8211;step=VALUE</code></dt>
<dd> Set step size</dd>
<dt><code>&#8211;print-partial</code></dt>
<dd> Print partial values</dd>
<dt><code>&#8211;hide-value</code></dt>
<dd> Hide value </dd>
</dl>
<p> Color selection options </p>
<dl>
<dt><code>&#8211;color=VALUE</code></dt>
<dd> Set the initial color</dd>
<dt><code>&#8211;show-palette</code></dt>
<dd> Show the palette </dd>
</dl>
<p> Miscellaneous options </p>
<dl>
<dt><code>-?, &#8211;help</code></dt>
<dd> Show summary of options.</dd>
<dt><code>&#8211;about</code></dt>
<dd> Display an about dialog.</dd>
<dt><code>&#8211;version</code></dt>
<dd> Show version of program. </dd>
</dl>
<p> Also the standard GTK+ options are accepted. </p>
<h2>ENVIRONMENT</h2>
<p> Normally, matedialog detects the terminal window from which it was launched and keeps itself above that window. This behavior can be disabled by unsetting the WINDOWID environment variable. </p>
<h2>EXAMPLES</h2>
<p> Display a file selector with the title <i>Select a file to remove</i>. The file selected is returned on standard output.</p>
<dl>
<dt>
</dt><dd> matedialog &#8211;title=&quot;Select a file to remove&quot; &#8211;file-selection</dd></dl>
<p> Display a text entry dialog with the title <i>Select Host</i> and the text <i>Select the host you would like to flood-ping</i>. The entered text is returned on standard output.</p>
<dl>
<dt>
</dt><dd> matedialog &#8211;title &quot;Select Host&quot; &#8211;entry &#8211;text &quot;Select the host you would like to flood-ping&quot;</dd></dl>
<p> Display a dialog, asking <i>Microsoft Windows has been found! Would you like to remove it?</i>. The return code will be 0 (true in shell) if <i>OK</i> is selected, and 1 (false) if <i>Cancel</i> is selected.</p>
<dl>
<dt>
</dt><dd> matedialog &#8211;question &#8211;title &quot;Alert&quot; &#8211;text &quot;Microsoft Windows has been found! Would you like to remove it?&quot;</dd></dl>
<p> Show the search results in a list dialog with the title <i>Search Results</i> and the text <i>Finding all header files&#8230;</i>.</p>
<dl>
<dt>
</dt><dd> find . -name &#8216;*.h&#8217; | matedialog &#8211;list &#8211;title &quot;Search Results&quot; &#8211;text &quot;Finding all header files..&quot; &#8211;column &quot;Files&quot;</dd></dl>
<p> Show an icon in the notification area</p>
<dl>
<dt>
</dt><dd> matedialog &#8211;notification &#8211;window-icon=update.png &#8211;text &quot;System update necessary!&quot;</dd></dl>
<p> Display a weekly shopping list in a check list dialog with <i>Apples</i> and <i>Oranges</i> pre selected</p>
<dl>
<dt>
</dt><dd> matedialog &#8211;list &#8211;checklist &#8211;column &quot;Buy&quot; &#8211;column &quot;Item&quot; TRUE Apples TRUE Oranges FALSE Pears FALSE Toothpaste</dd></dl>
<p> Display a progress dialog while searching for all the postscript files in your home directory </p>
<p> find $HOME -name &#8216;*.ps&#8217; | matedialog &#8211;progress &#8211;pulsate</p>
<h2>AUTHOR</h2>
<p> <code>MateDialog</code> was written by Glynn Foster &lt;glynn.foster [at] sun.com&gt;. </p>
<p> This manual page was written by Ross Burton &lt;ross [at] burtonini.com&gt;. </p>
<h2>SEE ALSO</h2>
<p> <code>gdialog</code>(1), <code><a href="/docs/linux/man/1-dialog/">dialog</a></code>(1) </p>
