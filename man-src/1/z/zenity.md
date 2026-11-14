---
title: "zenity(1)"
name: "zenity"
section: "1"
letter: "z"
url: "/docs/linux/man/1-zenity/"
description: "zenity – display GTK+ dialogs"
---

<h2 class="name">NAME</h2>
<p> zenity &#8211; display GTK+ dialogs </p>
<h2>SYNOPSIS</h2>
<p> <code>zenity</code> [<i>options</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>zenity</code> is a program that will display GTK+ dialogs, and return (either in the return code, or on standard output) the users input. This allows you to present information, and ask for information from the user, from all manner of shell scripts. </p>
<p> For example, <code>zenity &#8211;question</code> will return either 0, 1 or 5, depending on whether the user pressed <i>OK</i>, <i>Cancel</i> or timeout has been reached. <code>zenity &#8211;entry</code> will output on standard output what the user typed into the text entry field. </p>
<p> Comprehensive documentation is available in the GNOME Help Browser.</p>
<h2>OPTIONS</h2>
<p> This program follows the usual GNU command line syntax, with long options starting with two dashes (`-&#8216;). </p>
<p> Dialog options </p>
<dl>
<dt><code>&#8211;calendar</code></p>
<dd> Display calendar dialog</p>
<dt><code>&#8211;entry</code></p>
<dd> Display text entry dialog</p>
<dt><code>&#8211;error</code></p>
<dd> Display error dialog</p>
<dt><code>&#8211;file-selection</code></p>
<dd> Display file selection dialog</p>
<dt><code>&#8211;info</code></p>
<dd> Display info dialog</p>
<dt><code>&#8211;list</code></p>
<dd> Display list dialog</p>
<dt><code>&#8211;notification</code></p>
<dd> Display notification</p>
<dt><code>&#8211;progress</code></p>
<dd> Display progress indication dialog</p>
<dt><code>&#8211;question</code></p>
<dd> Display question dialog</p>
<dt><code>&#8211;text-info</code></p>
<dd> Display text information dialog</p>
<dt><code>&#8211;warning</code></p>
<dd> Display warning dialog</p>
<dt><code>&#8211;scale</code></p>
<dd> Display scale dialog</p>
<dt><code>&#8211;color-selection</code></p>
<dd> Display color selection dialog</p>
<dt><code>&#8211;password</code></p>
<dd> Display password dialog</p>
<dt><code>&#8211;forms</code></p>
<dd> Display forms dialog </p>
</dl>
<p> General options </p>
<dl>
<dt><code>&#8211;title=TITLE</code></p>
<dd> Set the dialog title</p>
<dt><code>&#8211;window-icon=ICONPATH</code></p>
<dd> Set the window icon with the path to an image. Alternatively, one of the four stock icons can be used: &#8216;error&#8217;, &#8216;info&#8217;, &#8216;question&#8217; or &#8216;warning&#8217;</p>
<dt><code>&#8211;icon-name=ICONNAME</code></p>
<dd> The name of the icon to display on the dialog to override the default stock icons</p>
<dt><code>&#8211;width=WIDTH</code></p>
<dd> Set the dialog width</p>
<dt><code>&#8211;height=HEIGHT</code></p>
<dd> Set the dialog height</p>
<dt><code>&#8211;timeout=TIMEOUT</code></p>
<dd> Set the dialog timeout in seconds</dl>
<p> Calendar options </p>
<dl>
<dt><code>&#8211;text=STRING</code></p>
<dd> Set the dialog text</p>
<dt><code>&#8211;day=INT</code></p>
<dd> Set the calendar day</p>
<dt><code>&#8211;month=INT</code></p>
<dd> Set the calendar month</p>
<dt><code>&#8211;year=INT</code></p>
<dd> Set the calendar year</p>
<dt><code>&#8211;date-format=PATTERN</code></p>
<dd> Set the format for the returned date. The default depends on the user locale or be set with the strftime style. For example %A %d/%m/%y </p>
</dl>
<p> Text entry options </p>
<dl>
<dt><code>&#8211;text=STRING</code></p>
<dd> Set the dialog text</p>
<dt><code>&#8211;entry-text=STRING</code></p>
<dd> Set the entry text</p>
<dt><code>&#8211;hide-text</code></p>
<dd> Hide the entry text </p>
</dl>
<p> Error options</p>
<dl>
<dt><code>&#8211;text=STRING</code></p>
<dd> Set the dialog text</p>
<dt><code>&#8211;no-wrap</code></p>
<dd> Do not enable text wrapping</p>
<dt><code>&#8211;no-markup</code></p>
<dd> Do not enable pango markup </p>
</dl>
<p> File selection options</p>
<dl>
<dt><code>&#8211;filename=FILENAME</code></p>
<dd> Set the file or directory to be selected by default</p>
<dt><code>&#8211;multiple</code></p>
<dd> Allow selection of multiple filenames in file selection dialog</p>
<dt><code>&#8211;directory</code></p>
<dd> Activate directory-only selection</p>
<dt><code>&#8211;save</code></p>
<dd> Activate save mode</p>
<dt><code>&#8211;separator=SEPARATOR</code></p>
<dd> Specify separator character when returning multiple filenames</p>
<dt><code>&#8211;confirm-overwrite</code></p>
<dd> Confirm file selection if filename already exists</p>
<dt><code>&#8211;file-filter=NAME | PATTERN1 PATTERN2</code></p>
<dd> Sets a filename filter </p>
</dl>
<p> Info options</p>
<dl>
<dt><code>&#8211;text=STRING</code></p>
<dd> Set the dialog text</p>
<dt><code>&#8211;no-wrap</code></p>
<dd> Do not enable text wrapping</p>
<dt><code>&#8211;no-markup</code></p>
<dd> Do not enable pango markup </p>
</dl>
<p> List options </p>
<dl>
<dt><code>&#8211;text=STRING</code></p>
<dd> Set the dialog text</p>
<dt><code>&#8211;column=STRING</code></p>
<dd> Set the column header</p>
<dt><code>&#8211;checklist</code></p>
<dd> Use check boxes for first column</p>
<dt><code>&#8211;radiolist</code></p>
<dd> Use radio buttons for first column</p>
<dt><code>&#8211;separator=STRING</code></p>
<dd> Set output separator character</p>
<dt><code>&#8211;multiple</code></p>
<dd> Allow multiple rows to be selected</p>
<dt><code>&#8211;editable</code></p>
<dd> Allow changes to text</p>
<dt><code>&#8211;print-column=NUMBER</code></p>
<dd> Specify what column to print to standard output. The default is to return the first column. &#8216;ALL&#8217; may be used to print all columns.</p>
<dt><code>&#8211;hide-column=NUMBER</code></p>
<dd> Hide a specific column</p>
<dt><code>&#8211;hide-header</code></p>
<dd> Hides the column headers </p>
</dl>
<p> Notification options </p>
<dl>
<dt><code>&#8211;text=STRING</code></p>
<dd> Set the notification text</p>
<dt><code>&#8211;listen</code></p>
<dd> Listen for commands on stdin. Commands include &#8216;message&#8217;, &#8216;tooltip&#8217;, &#8216;icon&#8217;, and &#8216;visible&#8217; separated by a colon. For example, &#8216;message: Hello world&#8217;, &#8216;visible: false&#8217;, or &#8216;icon: /path/to/icon&#8217;. The icon command also accepts the four stock icon: &#8216;error&#8217;, &#8216;info&#8217;, &#8216;question&#8217;, and &#8216;warning&#8217; </p>
</dl>
<p> Progress options </p>
<dl>
<dt><code>&#8211;text=STRING</code></p>
<dd> Set the dialog text</p>
<dt><code>&#8211;percentage=INT</code></p>
<dd> Set initial percentage</p>
<dt><code>&#8211;auto-close</code></p>
<dd> Close dialog when 100% has been reached</p>
<dt><code>&#8211;auto-kill</code></p>
<dd> Kill parent process if cancel button is pressed</p>
<dt><code>&#8211;pulsate</code></p>
<dd> Pulsate progress bar</p>
<dt><code>&#8211;no-cancel</code></p>
<dd> Hides the cancel button </p>
</dl>
<p> Question options </p>
<dl>
<dt><code>&#8211;text=STRING</code></p>
<dd> Set the dialog text</p>
<dt><code>&#8211;no-wrap</code></p>
<dd> Do not enable text wrapping</p>
<dt><code>&#8211;no-markup</code></p>
<dd> Do not enable pango markup</p>
<dt><code>&#8211;ok-label</code></p>
<dd> Set the text of the OK button</p>
<dt><code>&#8211;cancel-label</code></p>
<dd> Set the text of the cancel button </p>
</dl>
<p> Text options </p>
<dl>
<dt><code>&#8211;filename=FILENAME</code></p>
<dd> Open file</p>
<dt><code>&#8211;editable</code></p>
<dd> Allow changes to text</p>
<dt><code>&#8211;checkbox=TEXT</code></p>
<dd> Enable a checkbox for use like a &#8216;I read and accept the terms.&#8217;</p>
<dt><code>&#8211;ok-label</code></p>
<dd> Set the text of the OK button</p>
<dt><code>&#8211;cancel-label</code></p>
<dd> Set the text of the cancel button </p>
</dl>
<p> Warning options </p>
<dl>
<dt><code>&#8211;text=STRING</code></p>
<dd> Set the dialog text</p>
<dt><code>&#8211;no-wrap</code></p>
<dd> Do not enable text wrapping</p>
<dt><code>&#8211;no-markup</code></p>
<dd> Do not enable pango markup </p>
</dl>
<p> Scale options </p>
<dl>
<dt><code>&#8211;text=STRING</code></p>
<dd> Set the dialog text</p>
<dt><code>&#8211;value=VALUE</code></p>
<dd> Set initial value</p>
<dt><code>&#8211;min-value=VALUE</code></p>
<dd> Set minimum value</p>
<dt><code>&#8211;max-value=VALUE</code></p>
<dd> Set maximum value</p>
<dt><code>&#8211;step=VALUE</code></p>
<dd> Set step size</p>
<dt><code>&#8211;print-partial</code></p>
<dd> Print partial values</p>
<dt><code>&#8211;hide-value</code></p>
<dd> Hide value </p>
</dl>
<p> Color selection options </p>
<dl>
<dt><code>&#8211;color=VALUE</code></p>
<dd> Set the initial color</p>
<dt><code>&#8211;show-palette</code></p>
<dd> Show the palette </p>
</dl>
<p> Password dialog options </p>
<dl>
<dt><code>&#8211;username</code></p>
<dd> Display the username field </p>
</dl>
<p> Forms dialog options </p>
<dl>
<dt><code>&#8211;add-entry=FIELDNAME</code></p>
<dd> Add a new Entry in forms dialog</p>
<dt><code>&#8211;add-password=FIELDNAME</code></p>
<dd> Add a new Password Entry in forms dialog</p>
<dt><code>&#8211;add-calendar=FIELDNAME</code></p>
<dd> Add a new Calendar in forms dialog</p>
<dt><code>&#8211;text=STRING</code></p>
<dd> Set the dialog text</p>
<dt><code>&#8211;separator=STRING</code></p>
<dd> Set output separator character</p>
<dt><code>&#8211;forms-date-format=PATTERN</code></p>
<dd> Set the format for the returned date. The default depends on the user locale or be set with the strftime style. For example %A %d/%m/%y </p>
</dl>
<p> Miscellaneous options </p>
<dl>
<dt><code>-?, &#8211;help</code></p>
<dd> Show summary of options.</p>
<dt><code>&#8211;about</code></p>
<dd> Display an about dialog.</p>
<dt><code>&#8211;version</code></p>
<dd> Show version of program. </p>
</dl>
<p> Also the standard GTK+ options are accepted. For more information about the GTK+ options, execute following command.</p>
<dl>
<dt>
<dd> zenity &#8211;help-gtk </p>
</dl>
<h2>ENVIRONMENT</h2>
<p> Normally, zenity detects the terminal window from which it was launched and keeps itself above that window. This behavior can be disabled by unsetting the WINDOWID environment variable. </p>
<h2>EXAMPLES</h2>
<p> Display a file selector with the title <i>Select a file to remove</i>. The file selected is returned on standard output.</p>
<dl>
<dt>
<dd> zenity &#8211;title=&quot;Select a file to remove&quot; &#8211;file-selection</dl>
<p> Display a text entry dialog with the title <i>Select Host</i> and the text <i>Select the host you would like to flood-ping</i>. The entered text is returned on standard output.</p>
<dl>
<dt>
<dd> zenity &#8211;title &quot;Select Host&quot; &#8211;entry &#8211;text &quot;Select the host you would like to flood-ping&quot;</dl>
<p> Display a dialog, asking <i>Microsoft Windows has been found! Would you like to remove it?</i>. The return code will be 0 (true in shell) if <i>OK</i> is selected, and 1 (false) if <i>Cancel</i> is selected.</p>
<dl>
<dt>
<dd> zenity &#8211;question &#8211;title &quot;Alert&quot; &#8211;text &quot;Microsoft Windows has been found! Would you like to remove it?&quot;</dl>
<p> Show the search results in a list dialog with the title <i>Search Results</i> and the text <i>Finding all header files&#8230;</i>.</p>
<dl>
<dt>
<dd> find . -name &#8216;*.h&#8217; | zenity &#8211;list &#8211;title &quot;Search Results&quot; &#8211;text &quot;Finding all header files..&quot; &#8211;column &quot;Files&quot;</dl>
<p> Show a notification in the message tray</p>
<dl>
<dt>
<dd> zenity &#8211;notification &#8211;window-icon=update.png &#8211;text &quot;System update necessary!&quot;</dl>
<p> Display a weekly shopping list in a check list dialog with <i>Apples</i> and <i>Oranges</i> pre selected</p>
<dl>
<dt>
<dd> zenity &#8211;list &#8211;checklist &#8211;column &quot;Buy&quot; &#8211;column &quot;Item&quot; TRUE Apples TRUE Oranges FALSE Pears FALSE Toothpaste</dl>
<p> Display a progress dialog while searching for all the postscript files in your home directory </p>
<p> find $HOME -name &#8216;*.ps&#8217; | zenity &#8211;progress &#8211;pulsate</p>
<h2>AUTHOR</h2>
<p> <code>Zenity</code> was written by Glynn Foster &lt;glynn.foster [at] sun.com&gt;. </p>
<p> This manual page was written by Ross Burton &lt;ross [at] burtonini.com&gt;. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-dialog/">dialog</a></code>(1) </p>
<h2>Index</h2>
