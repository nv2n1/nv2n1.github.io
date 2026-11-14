---
title: "yapet(1)"
name: "yapet"
section: "1"
letter: "y"
url: "/docs/linux/man/1-yapet/"
description: "yapet – text based password manager"
---

<h2 class="name">NAME</h2>
<p> yapet &#8211; text based password manager </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>yapet</code> [[<code>-c</code>] | [<code>-h</code>] | [<code>-V</code>]] [[<code>-i</code>] | [<code>-r</code>&nbsp;<wbr>{<i>rcfile</i>}]] [[<code>-s</code>] | [<code>-S</code>]] [<code>-t</code>&nbsp;<wbr>{<i>sec</i>}] [<i>filename</i>]</dl>
<h2>DESCRIPTION</h2>
<p> <code>yapet</code></p>
<dd>provides a text user interface for storing passwords and associated information (referred to as password records) in files encrypted on disk. A password record is comprised of a record name, host name, user name, password, and comment. A master password is required to encrypt/decrypt the password records in a given file. <code>yapet</code> does not impose a limit of password records per file. </p>
<p> Files created by <code>yapet</code> always have the suffix .pet. Also, if a file is loaded using the command line, <code>yapet</code> appends the suffix .pet to the filename unless the filename includes this suffix already. By default, <code>yapet</code> refuses to load files not having a file mode of 0600. This behavior can be changed by providing the <code>-s</code> option when starting <code>yapet</code> or using a configuration file (see <code><a href="/docs/linux/man/5-yapet_config/">yapet_config</a></code>(5), and the section called &#8220;OPTIONS&#8221;). </p>
<p> After loading a file, the record name of each password record is displayed in a list. Existing password records can be opened by selecting them and pressing Enter. By default, existing password records are opened in read-only mode to avoid accidental changes. Pressing Ctrl+r toggles between read-only and edit mode. </p>
<p> On terminals supporting colors, the password is hidden if the password record dialog is in read-only mode. The password can be made visible, by either going to edit mode (Ctrl+r), or by pressing Ctrl+t. </p>
<p> <code>yapet</code> relies on OpenSSL for encryption and decryption of password records. The cipher for encryption and decryption is Blowfish with a 448 bits key. </p>
<p> Other features of <code>yapet</code> are: </p>
<dl>
<dt>
<dd> &bull; Screen lock after a certain amount of inactivity when password file is loaded (see also <code><a href="/docs/linux/man/5-yapet_config/">yapet_config</a></code>(5) and the section called &#8220;OPTIONS&#8221;).</dl>
<dl>
<dt>
<dd> &bull; Password records opened in read-only mode (default) hide the password. Toggling into edit mode reveals the password (see the section called &#8220;Password Record Dialog Keys&#8221;).</dl>
<dl>
<dt>
<dd> &bull; Import of CSV files (see <code>csv2yapet</code>).</dl>
<dl>
<dt>
<dd> &bull; Export of YAPET files to CSV files (see <code>yapet2csv</code>).</dl>
<dl>
<dt>
<dd> &bull; Integrated password generator.</dl>
<h3>Main Window Function Keys</h3>
<p> Following function keys are recognized in the main window: </p>
<p> h</p>
<dl>
<dt>
<dd> Show an overview of the function keys.</dl>
<p> Enter</p>
<dl>
<dt>
<dd> Open the currently selected password record.</dl>
<p> s</p>
<dl>
<dt>
<dd> Save changes to currently loaded file.</dl>
<p> r</p>
<dl>
<dt>
<dd> Open a file.</dl>
<p> e</p>
<dl>
<dt>
<dd> Create a new, empty file.</dl>
<p> l</p>
<dl>
<dt>
<dd> Lock the screen immediately. Takes only effect if a file is loaded.</dl>
<p> a</p>
<dl>
<dt>
<dd> Add a new password record.</dl>
<p> d</p>
<dl>
<dt>
<dd> Delete the currently selected password record.</dl>
<p> o</p>
<dl>
<dt>
<dd> Change the sort order of the password record list.</dl>
<p> /</p>
<dl>
<dt>
<dd> Search for a password record. The search is only performed on the Name of the password record. Other password record fields won&#8217;t be searched.</dl>
<p> n</p>
<dl>
<dt>
<dd> Search for the next occurrence of a previous search initiated by /.</dl>
<p> c</p>
<dl>
<dt>
<dd> Change the master password of the currently loaded YAPET file.</dl>
<p> i</p>
<dl>
<dt>
<dd> Show various information about YAPET and the loaded file, if any.</dl>
<p> Ctrl+l (^L)</p>
<dl>
<dt>
<dd> Redraw the entire screen.</dl>
<p> g</p>
<dl>
<dt>
<dd> Open the password generator.</dl>
<p> q</p>
<dl>
<dt>
<dd> Quit YAPET.</dl>
<h3>Cursor Movement Keys</h3>
<p> Cursor movement, whether in clear text or password fields, is accomplished by using the following keys: </p>
<p> Left, Ctrl+b</p>
<dl>
<dt>
<dd> Moves the cursor one character to the left.</dl>
<p> Right, Ctrl+f</p>
<dl>
<dt>
<dd> Moves the cursor one character to the right.</dl>
<p> Home, Ctrl+a</p>
<dl>
<dt>
<dd> Moves the cursor to the beginning of the input field.</dl>
<p> End, Ctrl+e</p>
<dl>
<dt>
<dd> Moves the cursor to the end of the input field.</dl>
<p> Backspace</p>
<dl>
<dt>
<dd> Delete the character left of the cursor.</dl>
<p> Delete, Ctrl+d</p>
<dl>
<dt>
<dd> Delete the character under the cursor.</dl>
<p> Ctrl+k</p>
<dl>
<dt>
<dd> Delete all characters under and right of the cursor.</dl>
<p> Ctrl+u</p>
<dl>
<dt>
<dd> Delete all characters left of the cursor.</dl>
<p> Enter, Tab</p>
<dl>
<dt>
<dd> Focus the next widget.</dl>
<p> Shift+Tab</p>
<dl>
<dt>
<dd> Focus the previous widget.</dl>
<h3>Password Record Dialog Keys</h3>
<p> Following function keys are recognized in the password record dialog, besides cursor movement keys (see the section called &#8220;Cursor Movement Keys&#8221;): </p>
<p> Ctrl+r</p>
<dl>
<dt>
<dd> Toggle the password record dialog between read-only and edit mode. In read-only mode, <code>yapet</code> hides the password (only supported on color terminals).</dl>
<p> Ctrl+t</p>
<dl>
<dt>
<dd> Toggle between hiding and showing the password, without setting the password record dialog to edit mode (only supported on color terminals). Has no effect if the password record dialog is in edit mode.</dl>
<h2>OPTIONS</h2>
<p> The following options are supported: </p>
<p> <code>-c</code></p>
<dl>
<dt>
<dd> Show copyright information.</dl>
<p> <code>-h</code></p>
<dl>
<dt>
<dd> Print help text.</dl>
<p> <code>-i</code></p>
<dl>
<dt>
<dd> Do not read the configuration file.</dl>
<p> <code>-r</code> <i>rcfile</i></p>
<dl>
<dt>
<dd> Read the configuration file specified by <i>rcfile</i>. If this option is not given, the default configuration file read is <code>$HOME</code>/.yapet unless <code>-i</code> is specified.</dl>
<p> <code>-s</code></p>
<dl>
<dt>
<dd> Disable the check for the owner and file mode when loading files. Without this option, <code>yapet</code> checks password files for having the same owner as the user running <code>yapet</code> and verifies that the file mode is strictly 0600. If one of these conditions are not met, <code>yapet</code> refuses to load the file. Providing this options disables those checks and <code>yapet</code> will load files with owners other than the process owner of <code>yapet</code> and file modes different from 0600. </p>
<p> New files saved while this option is active will have the file mode set according to <code><a href="/docs/linux/man/2-umask/">umask</a></code>(2).</dl>
<p> <code>-S</code></p>
<dl>
<dt>
<dd> Enable the check for the owner and file mode when loading files. This option makes <code>yapet</code> to load password files having the owner set to the process owner of <code>yapet</code> and the file mode strictly set to 0600 only. If one of these conditions are not met, <code>yapet</code> refuses to load the file. </p>
<p> New files saved while this option is active will have the file mode set to 0600. </p>
<p> This is the default mode.</dl>
<p> <code>-t</code> <i>sec</i></p>
<dl>
<dt>
<dd> Set the timeout until the screen is locked to <i>sec</i> seconds. The minimum time allowed is 10 seconds. If a smaller value is provided, the timeout will be set to 10 seconds. </p>
<p> Default: 10 min.</dl>
<p> <code>-V</code></p>
<dl>
<dt>
<dd> Show version of <code>yapet</code>.</dl>
<p> <i>filename</i></p>
<dl>
<dt>
<dd> The file to open upon invocation of <code>yapet</code>. If the file does not exist, <code>yapet</code> asks whether it should be created. </p>
<p> Files created by <code>yapet</code> always have the suffix .pet.</dl>
<h2>FILES</h2>
<p> <code>$HOME</code>/.yapet</p>
<dl>
<dt>
<dd> The per-user configuration file. If existing, options are read from this file but can be overridden by the command line options. </p>
<p> Processing of this file can be disabled by invoking <code>yapet</code> with the <code>-i</code> option. </p>
<p> Refer to the <code><a href="/docs/linux/man/5-yapet_config/">yapet_config</a></code>(5) for an explanation of the per-user configuration file.</dl>
<h2>ENVIRONMENT</h2>
<p> <code>LC_MESSAGES</code></p>
<dl>
<dt>
<dd> Displaying messages in the specified language. Currently only German is supported besides English.</dl>
<h2>FORMAT OF YAPET FILES</h2>
<p> Please refer to the DESIGN file in the source code distribution or point your browser to m[blue]<code><a rel="nofollow" href="http://www.guengel.ch/myapps/yapet/">http://www.guengel.ch/myapps/yapet/</a></code>m[].</p>
<h2>BUGS</h2>
<p> Please report bugs to m[blue]<code><a rel="nofollow" href="http://bugs.guengel.ch/">http://bugs.guengel.ch/</a></code>m[].</p>
<h2>AUTHOR</h2>
<p> Rafael Ostertag rafi [at] guengel.ch</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-yapet_config/">yapet_config</a></code>(5), <code><a href="/docs/linux/man/5-yapet_colors/">yapet_colors</a></code>(5), <code><a href="/docs/linux/man/1-csv2yapet/">csv2yapet</a></code>(1), <code><a href="/docs/linux/man/1-yapet2csv/">yapet2csv</a></code>(1)</p>
<h2>AVAILABILITY</h2>
<p> The latest version of <code>yapet</code> can be found under m[blue]<code><a rel="nofollow" href="http://www.guengel.ch/myapps/yapet/">http://www.guengel.ch/myapps/yapet/</a></code>m[].</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2008, 2009, 2010, 2011, 2013, 2014 Rafael Ostertag &lt;rafi [at] guengel.ch&gt; </p>
<h2>Index</h2>
