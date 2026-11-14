---
title: "boxes(1)"
name: "boxes"
section: "1"
letter: "b"
url: "/docs/linux/man/1-boxes/"
description: "boxes – text mode box and comment drawing filter"
---

<h2 class="name">NAME</h2>
<p> boxes &#8211; text mode box and comment drawing filter </p>
<h2>SYNOPSIS</h2>
<p> <code>boxes</code> [-hlmrv] [-a format] [-d design] [-f file] [-i indent] [-k bool] [-p pad] [-s size] [-t tabopts] [infile [outfile]]</p>
<h2>DESCRIPTION</h2>
<p> <i>Boxes</i> is a text filter which can draw any kind of box around its input text. Box design choices range from simple boxes to complex ASCII art. A box can also be removed and repaired, even if it has been badly damaged by editing of the text inside. Since boxes may be open on any side, <i>boxes</i> can also be used to create regional comments in any programming language. New box designs of all sorts can easily be added and shared by appending to a free format configuration file.<br />
 <i>boxes</i> was originally intended to be used with the <i><a href="/docs/linux/man/1-vim/">vim</a>(1)</i> text editor, but it can be tied to any text editor which supports filters, as well as called from the command line as a standalone tool.</p>
<h2>OPTIONS</h2>
<p> Options offered by <i>boxes</i> are the following:</p>
<dl>
<dt><code>-a </code><i>string</i></p>
<dd> Alignment/positioning of text inside box. This option takes a format string argument which is read from left to right. The format string may not contain whitespace and must consist of one or more of the following components: </p>
<p> <code>h</code>x &#8211; horizontal alignment of the input text block inside a potentially larger box. Possible values for <i>x</i> are <code>l</code> (ell, for left alignment), <code>c</code> (center), or <code>r</code> (right). This does not affect the justification of text lines within the input text block (use the <code>j</code> argument instead).<br />
 <code>v</code>x &#8211; vertical alignment of the input text block inside a potentially larger box. Possible values for <i>x</i> are <code>t</code> (for top alignment), <code>c</code> (center), or <code>b</code> (bottom).<br />
 <code>j</code>x &#8211; justification of lines within the input text block. Possible values for <i>x</i> are <code>l</code> (ell, for left justification), <code>c</code> (center), or <code>r</code> (right). This does not affect the alignment of the input text block itself within the box. Use the <code>h</code> and <code>v</code> arguments for input text block positioning. </p>
<p> Short hand notations (can be combined with the above arguments):<br />
 <code>l</code> (ell) &#8211; short for <code>h</code>l<code>v</code>c<code>j</code>l<br />
 <code>c</code> &#8211; short for <code>h</code>c<code>v</code>c<code>j</code>c<br />
 <code>r</code> &#8211; short for <code>h</code>r<code>v</code>c<code>j</code>r </p>
<p> The factory default setting for <code>-a</code> is <code>h</code>l<code>v</code>t.</p>
<dt><code>-c </code><i>string</i></p>
<dd> Command line design definition for simple cases. The argument of this option is the definition for the &quot;west&quot; (W) shape. The defined shape must consist of exactly one line, i.e. no multi-line shapes are allowed. The <code>-c</code> option is intended as a shortcut for those cases where simple regional comments are to be created, which only need a certain character or sequence of characters to be placed in front of every line. In such cases, it is much more convenient to simply specify <code>-c</code> than to do a complete design definition in one&#8217;s config file, where the only shape defined is the west shape.<br />
 This option implies a <code>-d</code> and does not access the config file. <code>-c</code> may of course be used in conjunction with any of the other options. By default, <code>-c</code> is not specified.</p>
<dt><code>-d </code><i>string</i></p>
<dd> Design selection. The one argument of this option is the name of the design to use.</p>
<dt><code>-f </code><i>string</i></p>
<dd> Use alternate config file. The one argument of this option is the name of a valid <i>boxes</i> config file, containing new and exciting designs!</p>
<dt><code>-h</code></p>
<dd> Print usage information.</p>
<dt><code>-i </code><i>string</i></p>
<dd> Indentation mode. Possible arguments are &quot;text&quot; (indent text inside of box), &quot;box&quot; (indent box, not text inside of box), or &quot;none&quot; (throw away indentation). Arguments may be abbreviated. The default is to indent the box, but not the text.</p>
<dt><code>-k </code><i>bool</i></p>
<dd> Kill leading/trailing blank lines on removal. The value of <i>bool</i> can be specified as on, yes, true, 1, or t, all meaning yes, or off, no, false, 0, or f, which mean no. This is case-insensitive. This option only takes effect in connection with <code>-r</code>. If set to yes, leading and trailing blank lines will be removed from the output. If set to no, the entire content of the former box is returned. The default is no, if both the top and the bottom part of the box are open, as is the case with most regional comments. If the box&#8217;s design defines a top part or a bottom part, the default is yes.</p>
<dt><code>-l</code></p>
<dd> (ell) List designs. Produces a listing of all available box designs in the config file, along with a sample box and information about it&#8217;s creator. Also checks syntax of the entire config file. If used in connection with <code>-d</code>, displays detailed information about the specified design.</p>
<dt><code>-m</code></p>
<dd> Mend box. This removes a (potentially broken) box as with <code>-r</code>, and redraws it afterwards. The mended box is drawn according to the options given. This may be important to know when it comes to restoring padding, identation, etc. for the mended box. Implies <code>-k</code> false.</p>
<dt><code>-p </code><i>string</i></p>
<dd> Padding. Specify padding in spaces around the input text block for all sides of the box. The argument string may not contain whitespace and must consist of a combination of the following characters, each followed by a number indicating the padding in spaces:<br />
 <code>a</code> &#8211; (all) give padding for all sides at once<br />
 <code>h</code> &#8211; (horiz) give padding for both horizontal sides<br />
 <code>v</code> &#8211; (vertical) give padding for both vertical sides<br />
 <code>b</code> &#8211; (bottom) give padding for bottom (south) side<br />
 <code>l</code> &#8211; (left) give padding for left (west) side<br />
 <code>t</code> &#8211; (top) give padding for top (north) side<br />
 <code>r</code> &#8211; (right) give padding for right (east) side<br />
 Example: <code>-p a</code>4<code>t</code>2 would define the padding to be 4 characters on all sides, except for the top of the box, where the input text block will be only 2 lines away from the box.<br />
 By default, unless specified otherwise in the config file, no padding is used.</p>
<dt><code>-r</code></p>
<dd> Remove box. Removes an existing box instead of drawing it. Which design to use is detected automatically. In order to save time or in case the detection does not decide correctly, combine with <code>-d</code> to specify the design. The default is to draw a new box.</p>
<dt><code>-s </code><i>width</i><code>x</code>height</p>
<dd> Box size. This option specifies the desired box size in units of columns (for width) and lines (for height). If only a single number is given as argument, this number specifies the desired box width. A single number prefixed by &#8216;x&#8217; specifies only the box height. The actual resulting box size may vary depending on the individual shape sizes of the chosen design. Also, other command line options may influence the box size (such as <code>-p</code>).<br />
 By default, the smallest possible box is created around the text.</p>
<dt><code>-t </code><i>string</i></p>
<dd> Tab handling. This option controls how tab characters in the input text are handled. The option string must always begin with a <i>uint</i> number indicating the distance between tab stops. It is important that this value be set correctly, or tabulator characters will upset your input text. The correct tab distance value depends on the settings used for the text you are processing. A common value is 8.<br />
 Immediately following the tab distance, an optional character can be appended, telling <i>boxes</i> how to treat the leading tabs. The following options are available:<br />
 <code>e</code> &#8211; expand tabs into spaces<br />
 <code>k</code> &#8211; keep tabs as close to what they were as possible<br />
 <code>u</code> &#8211; unexpand tabs. This makes <i>boxes</i> turn as many spaces as possible into tabs. </p>
<p> In order to maintain backwards compatibility, the <code>-t</code> <i>string</i> can be just a number. In that case, <code>e</code> is assumed for tab handling, which removes all tabs and replaces them with spaces. The factory default for the <code>-t</code> option is simply 8, which is just such a case.<br />
 For example, you could specify <code>-t </code>4u in order to have your leading tabs unexpanded. In the box content, tabs are always converted into spaces. The tab distance in this example is 4.</p>
<dt><code>-v</code></p>
<dd> Print out current version number.</dl>
<h2>CONFIGURATION FILES</h2>
<p> <i>Boxes</i> will use the configuration file specified on the command line (using <code>-f</code>). If no config file is specified on the command line, <i>boxes</i> will check for the BOXES environment variable, which may contain a filename to use. If BOXES is not set, <i>boxes</i> will try to read $HOME/.boxes and use it as a config file. Failing that, <i>boxes</i> will try to read the system-wide config file (see FILES). </p>
<p> The syntax of <i>boxes</i> config files is described on the website (see below). They are quite self-explanatory, though.</p>
<h2>AVAILABILITY</h2>
<p> <i>Boxes</i> is available from its website at &lt;URL:<a rel="nofollow" href="http://boxes.thomasjensen.com/">http://boxes.thomasjensen.com/</a>&gt;. The website also features a number of examples illustrating this manual page as well as more in-depth documentation. </p>
<p> Check out <i><a href="/docs/linux/man/1-vim/">vim</a>(1)</i> at &lt;URL:<a rel="nofollow" href="http://www.vim.org/">http://www.vim.org/</a>&gt;!</p>
<h2>AUTHOR</h2>
<p> <i>Boxes</i> was made by Thomas Jensen &lt;boxes [at] thomasjensen.com&gt;.<br />
 Please see the <i>boxes</i> website for a current email address.</p>
<h2>VERSION</h2>
<p> This is <i>boxes</i> version 1.1.1.</p>
<h2>BUGS</h2>
<p> Although it is doing fine in most cases, imho the design autodetector needs some more work.<br />
 Should you notice any other unspecified behavior, please tell the author!</p>
<h2>ENVIRONMENT</h2>
<p> <i>Boxes</i> recognizes the following environment variables:</p>
<dl>
<dt>HOME</p>
<dd> The user&#8217;s home directory.</p>
<dt>BOXES</p>
<dd> Name of <i>boxes</i> configuration file, if different from ~/.boxes.</dl>
<h2>FILES</h2>
<dl>
<dt>$HOME/.boxes</p>
<dd> <i>boxes</i> configuration file</p>
<dt>/usr/share/boxes/boxes</p>
<dd> system-wide configuration file</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-tal/">tal</a>(1)</i> , <i><a href="/docs/linux/man/1-vim/">vim</a>(1)</i> </p>
<h2>Index</h2>
