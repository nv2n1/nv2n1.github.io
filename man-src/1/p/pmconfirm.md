---
title: "pmconfirm(1)"
name: "pmconfirm"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmconfirm/"
description: "pmconfirm, pmmessage, pmquery – general purpose dialog box"
---

<h2>NAME</h2>
<p> <code>pmconfirm</code>, <code>pmmessage</code>, <code>pmquery</code> &#8211; general purpose dialog box</p>
<h2>SYNOPSIS</h2>
<p> <code>pmconfirm</code> [<code>-c</code>] [<code>-b</code> <i>button-name</i>] [<code>-B</code> <i>default-button-name</i>] [<code>-t</code> <i>string</i>] [<code>-file</code> <i>filename</i>] [<code>-icon</code> <i>icontype</i>] [<code>-font</code> <i>font</i>] [<code>-header</code> <i>titlebar-string</i>] [<code>-useslider</code>] [<code>-noslider</code>] [<code>-noframe</code>] [<code>-exclusive</code>] </p>
<p> <code>pmmessage</code> [<code>-buttons</code> <i>label1</i>[:<i>value1</i>][,<i>label2</i>[:<i>value2</i>][,&#8230;]]] [<code>-center</code>] [<code>-nearmouse</code>] [<code>-default</code> <i>button</i>] [<code>-file</code> <i>filename</i>] [<code>-print</code>] [<code>-timeout</code> <i>sec</i>] <i>message&#8230;</i> </p>
<p> <code>pmquery [-input</code>] [<code>all above options&#8230;</code>] [<i>message&#8230;</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>pmquery</code> provides a command-line-option compatible implementation of the <code>xconfirm</code> and <code>xmessage</code> tools, using a look-and-feel that is consistent with <code>pmchart</code>. Several extensions to the functionality of the original tools have been made, in order to improve their specific utility for <code>pmchart</code>, but wherever possible the original semantics remain. </p>
<p> <code>pmconfirm</code> displays a line of text for each <code>-t</code> argument specified (or a file when the <code>-file</code> argument is used), and a button for each <code>-b</code> argument specified. When one of the buttons is pressed, the label of that button is written to <code>pmquery&#8217;s</code> standard output. This provides a means of communication/feedback from within shell scripts and a means to display useful information to a user from an application. </p>
<p> <code>pmmessage</code> displays a window containing a message from the command line, a file, or standard input. It additionally allows buttons to be associated with an exit status, and only optionally will write the label of the button to standard output. </p>
<p> <code>pmquery</code> extends the above tools to additionally support limited user input, as free form text. In this <code>-input</code> mode, any text entered will be output when the default button is pressed. A default text can be entered using the same mechanisms as the other tools. </p>
<p> Command line options are available to specify font style, frame style, modality and one of several different icons to be presented for tailored visual feedback to the user.</p>
<dl>
<dt><code>-c </code>or <code>-center</code></p>
<dd> Center the window on the display.</p>
<dt><code>-nearmouse</code></p>
<dd> Pop up the window near the mouse cursor.</p>
<dt><code>-b </code><i>button-name</i></p>
<dd> Displays a button with the label <i>button-name</i>. If <i>button-name</i> is the empty string, the button in that position is not displayed. If no <code>-b</code> arguments are present, the default is a button with the label Continue. The exit status associated with <i>button-name</i> is zero.</p>
<dt><code>-B </code><i>button-name</i></p>
<dd> Displays a button with the label <i>button-name</i> and specifies it as the button to be activated when enter is pressed. The exit status associated with <i>button-name</i> is zero.</p>
<dt><code>-buttons </code><i>button,button,&#8230;</i></p>
<dd> This option will create one button for each comma-separated <i>button</i> argument. Each <i>button</i> consists of a label optionally followed by a colon and an exit value. The exit value will be returned if that button is selected. The default exit value is 100 plus the button number. Buttons are numbered from the left starting with one.</p>
<dt><code>-default </code><i>label</i></p>
<dd> Defines the button with a matching <i>label</i> to be the default. If not specified there is no default. The corresponding resource is <code>defaultButton</code>. Pressing Return anywhere in the <i>xmessage</i> window will activate the default button. The default button has a wider border than the others.</p>
<dt><code>-t </code><i>message</i></p>
<dd> Displays message. Any number of strings can be listed on the command line (each must be preceded with the <code>-t</code> option).</p>
<dt><code>-file </code><i>filename</i></p>
<dd> Displays the file <i>filename.</i> All <code>-t</code> options will be ignored. A <i>filename</i> of `<i>&#8211;</i>&#8216; reads from standard input.</p>
<dt><code>-icon </code><i>icontype</i></p>
<dd> Displays the icon <i>icontype</i> where icontype is one of: <i>info</i>, <i>error</i>, <i>question</i>, <i>warning</i>, <i>critical</i>. <i>action</i> is also accepted as a synonym for <i>error</i> for backward compatibility. <code>pmquery</code> introduces the additional <i>archive</i> and <i>host</i> icon types as well as the original <code>xconfirm</code> types listed earlier.</p>
<dt><code>-font </code><i>fontname</i></p>
<dd> Use fontname as the font. This option is only available when using the X Window System.</p>
<dt><code>-header </code><i>string</i></p>
<dd> Use string as the window title.</p>
<dt><code>-print</code></p>
<dd> This causes the program to write the label of the button pressed to standard output. It is the default behaviour for <code>pmconfirm</code> and <code>pmquery</code>.</p>
<dt><code>-noprint</code></p>
<dd> This causes the program to not write the label of the button pressed to standard output. It is the default behaviour for <code>pmmessage</code>.</p>
<dt><code>-geometry </code><i>geometry-string</i></p>
<dd> This provides xconfirm with an X-compatible geometry string specification. This option is only available when using the X Window System.</p>
<dt><code>-useslider</code></p>
<dd> When displaying a file, always use a slider instead of determining automatically whether a slider is necessary.</p>
<dt><code>-noslider</code></p>
<dd> Do not create a slider, and clip text to the window size, instead of determining automatically whether a slider is necessary..</p>
<dt><code>-noframe</code></p>
<dd> Do not display a frame around the contents.</p>
<dt><code>-exclusive</code></p>
<dd> Grab the keyboard/pointer and do not allow further input until a button is pressed.</p>
<dt><code>-timeout </code><i>secs</i></p>
<dd> Exit with status 0 after <i>secs</i> seconds if the user has not clicked on a button yet. The corresponding resource is <code>timeout</code>.</dl>
<h2>EXAMPLES</h2>
<p> The following shell script will display a window with an information icon, asking the user a yes or no question with &quot;Yes&quot; as the default. </p>
<pre><code>
#!/ bin / sh
 case `pmquery -t "Really power down?" -b No -B Yes -icon question
 in
   Yes) shutdown;;
   No) ;;
 esac
</code></pre>
<p> A second example, which prompts for a hostname then starts a terminal with an ssh session connected to the requested host. </p>
<pre>
 #! /bin/sh
 host=`pmquery -input -icon host -b Cancel -B OK \
               -header &quot;Remote Terminal - Secure Shell&quot;
 [ &quot;$host&quot; = &quot;Cancel&quot; -o -z &quot;$host&quot; ] &amp;&amp; exit
 gnome-terminal -e &quot;ssh $host&quot;
</pre>
<h2>ENVIRONMENT</h2>
<p> <code>pmquery</code> is an excellent choice of utility for the &quot;PCP_XCONFIRM_PROG&quot; Performance Co-Pilot configuration parameter (refer to <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5) for details). </p>
<p> Note that PCP_XCONFIRM_PROG will be automatically set to <code>pmquery</code> inside tools like <code>pmchart</code>, unless PCP_XCONFIRM_PROG is already set in the environment.</p>
<h2>EXIT STATUS</h2>
<p> If it detects an error, <code>pmquery</code> always returns 1, so this value should not be associated with a button. Unless <i>-button</i> option has not been used, the return code will be zero on success.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pmchart/">pmchart</a></code>(1), <code><a href="/docs/linux/man/1-xconfirm/">xconfirm</a></code>(1), <code><a href="/docs/linux/man/1-xmessage/">xmessage</a></code>(1), <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5). </p>
<h2>Index</h2>
