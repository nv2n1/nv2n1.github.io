---
title: "multixterm(1)"
name: "multixterm"
section: "1"
letter: "m"
url: "/docs/linux/man/1-multixterm/"
description: "multixterm – drive multiple xterms separately or together"
---

<h2 class="name">NAME</h2>
<p> multixterm &#8211; drive multiple xterms separately or together </p>
<h2>SYNOPSIS</h2>
<p> <code>multixterm</code> [ <i>args</i> ]</p>
<h2>DESCRIPTION</h2>
<p> Multixterm creates multiple xterms that can be driven together or separately. </p>
<p> In its simplest form, multixterm is run with no arguments and commands are interactively entered in the first entry field. Press return (or click the &quot;new xterm&quot; button) to create a new xterm running that command. </p>
<p> Keystrokes in the &quot;stdin window&quot; are redirected to all xterms started by multixterm. xterms may be driven separately simply by focusing on them. </p>
<p> The stdin window must have the focus for keystrokes to be sent to the xterms. When it has the focus, the color changes to aquamarine. As characters are entered, the color changes to green for a second. This provides feedback since characters are not echoed in the stdin window. </p>
<p> Typing in the stdin window while holding down the alt or meta keys sends an escape character before the typed characters. This provides support for programs such as emacs. </p>
<h2>ARGUMENTS</h2>
<dl>
<dt>
<dd>
<dl>
<dt>-xa</p>
<dd> The optional -xa argument indicates arguments to pass to xterm. </p>
<dt>-xc</p>
<dd> The optional -xc argument indicates a command to be run in each named xterm (see -xn). With no -xc argument, the command is the current shell. </p>
<dt>-xd</p>
<dd> The optional -xd argument indicates a directory to search for files that will appear in the Files menu. By default, the directory is: ~/lib/multixterm </p>
<dt>-xf</p>
<dd> The optional -xf argument indicates a file to be read at startup. See FILES below for more info. </p>
<dt>-xn</p>
<dd> The optional -xn argument indicates a name for each xterm. This name will also be substituted for any %n in the command argument (see -xc). </p>
<dt>-xv</p>
<dd> The optional -xv flag puts multixterm into a verbose mode where it will describe some of the things it is doing internally. The verbose output is not intended to be understandable to anyone but the author. </p>
</dl>
</dl>
<p> Less common options may be changed by the startup file (see FILES below). </p>
<p> All the usual X and wish flags are supported (i.e., -display, -name). There are so many of them that to avoid colliding and make them easy to remember, all the multixterm flags begin with -x. </p>
<p> If any arguments do not match the flags above, the remainder of the command line is made available for user processing. By default, the remainder is used as a list of xterm names in the style of -xn. The default behavior may be changed using the .multixtermrc file (see DOT FILE below). </p>
<h2>EXAMPLE COMMAND LINE ARGUMENTS</h2>
<p> The following command line starts up two xterms using ssh to the hosts bud and dexter. </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>multixterm -xc &quot;ssh %n&quot; bud dexter</p>
<h2>FILES</h2>
<p> Command files may be used to drive or initialize multixterm. The File menu may be used to invoke other files. If files exist in the command file directory (see -xd above), they will appear in the File menu. Files may also be loaded by using File-&gt;Open. Any filename is acceptable but the File-&gt;Open browser defaults to files with a .mxt suffix. </p>
<p> Files are written in Tcl and may change any variables or invoke any procedures. The primary variables of interest are &#8216;xtermCmd&#8217; which identifies the command (see -xc) and &#8216;xtermNames&#8217; which is a list of names (see -xn). The procedure xtermStartAll, starts xterms for each name in the list. Other variables and procedures may be discovered by examining multixterm itself. </p>
<h2>EXAMPLE FILE</h2>
<p> The following file does the same thing as the earlier example command line: </p>
<pre>
        # start two xterms connected to bud and dexter
        set xtermCmd &quot;ssh %n&quot;
        set xtermNames {bud dexter}
        xtermStartAll
</pre>
<h2>DOT FILE</h2>
<p> At startup, multixterm reads ~/.multixtermrc if present. This is similar to the command files (see FILES above) except that .multixtermrc may not call xtermStartAll. Instead it is called implicitly, similar to the way that it is implicit in the command line use of -xn. </p>
<p> The following example .multixtermrc file makes every xterm run ssh to the hosts named on the command line. </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>set xtermCmd &quot;ssh %n&quot;</p>
<p> Then multixterm could be called simply: </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>multixterm bud dexter</p>
<p> If any command-line argument does not match a multixterm flag, the remainder of the command line is made available to .multixtermrc in the argv variable. If argv is non-empty when .multixtermrc returns, it is assigned to xtermNames unless xtermNames is non-empty in which case, the content of argv is ignored. </p>
<p> Commands from multixterm are evaluated early in the initialization of multixterm. Anything that must be done late in the initialization (such as adding additional bindings to the user interface) may be done by putting the commands inside a procedure called &quot;initLate&quot;. </p>
<h2>MENUS</h2>
<p> Except as otherwise noted, the menus are self-explanatory. Some of the menus have dashed lines as the first entry. Clicking on the dashed lines will &quot;tear off&quot; the menus. </p>
<h2>USAGE SUGGESTION &#8211; ALIASES AND COMMAND FILES</h2>
<p> Aliases may be used to store lengthy command-line invocations. Command files can be also be used to store such invocations as well as providing a convenient way to share configurations. </p>
<p> Tcl is a general-purpose language. Thus multixterm command files can be extremely flexible, such as loading hostnames from other programs or files that may change from day-to-day. In addition, command files can be used for other purposes. For example, command files may be used to prepared common canned interaction sequences. For example, the command to send the same string to all xterms is: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;xtermSend&nbsp;&quot;a particularly long string&quot; </p>
<p> The File menu (torn-off) makes canned sequences particularly convenient. Interactions could also be bound to a mouse button, keystroke, or added to a menu via the .multixtermrc file. </p>
<p> The following .multixtermrc causes tiny xterms to tile across and down the screen. (You may have to adjust the parameters for your screen.) This can be very helpful when dealing with large numbers of xterms. </p>
<pre><code>
set yPos 0 set xPos 0 trace variable xtermArgs r traceArgs
    proc traceArgs{args}
{
    global xPos yPos
        set ::xtermArgs "-geometry 80x12+$xPos+$yPos -font 6x10" if {$xPos}
    {
        set xPos 0 incr yPos 145 if {$yPos &gt; 800}
        {
            set yPos 0
        }
    }
    else
    {
        set xPos 500
    }
}
</code></pre>
<p> The xtermArgs variable in the code above is the variable corresponding to the -xa argument. </p>
<p> xterms can be also be created directly. The following command file creates three xterms overlapped horizontally:<br />
set xPos 0 foreach name{bud dexter hotdog}<br />
{<br />
    set ::xtermArgs &#8220;-geometry 80&#215;12+$xPos+0 -font 6&#215;10&#8221; set ::xtermNames $name<br />
        xtermStartAll<br />
            incr xPos 300<br />
}</p>
<h2>USAGE SUGGESTION &#8211; SELECTING HOSTS BY NICKNAME</h2>
<p> The following .multixtermrc shows an example of changing the default handling of the arguments from hostnames to a filename containing hostnames: </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>set xtermNames [exec cat $argv]</p>
<p> The following is a variation, retrieving the host names from the yp database: </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>set xtermNames [exec ypcat $argv]</p>
<p> The following hardcodes two sets of hosts, so that you can call multixterm with either &quot;cluster1&quot; or &quot;cluster2&quot;: </p>
<pre><code>
switch
    $argv
    {
        cluster1{
            set xtermNames "bud dexter"} cluster2
        {
            set xtermNames "frank hotdog weiner"
        }
    }
</code></pre>
<h2>COMPARE/CONTRAST</h2>
<p> It is worth comparing multixterm to xkibitz. Multixterm connects a separate process to each xterm. xkibitz connects the same process to each xterm. </p>
<h2>LIMITATIONS</h2>
<p> Multixterm provides no way to remotely control scrollbars, resize, and most other window system related functions. </p>
<p> Because xterm has no mechanism for propagating size information to external processes, particularly for character graphic applications (e.g., vi, emacs), you may have to manually ensure that the spawned process behind each xterm has the correct size. For example, if you create or set the xterm to a size, you may have to send an explicit stty command with the correct size to the spawned process(es). Alternatively, you can add the correct size argument when an xterm is created (i.e., &quot;-geometry 80&#215;20&quot;). </p>
<p> Multixterm can only control new xterms that multixterm itself has started. </p>
<p> As a convenience, the File menu shows a limited number of files. To show all the files, use File-&gt;Open. </p>
<h2>FILES</h2>
<p> $DOTDIR/.multixtermrc initial command file<br />
 ~/.multixtermrc fallback command file<br />
 ~/lib/multixterm/ default command file directory </p>
<h2>BUGS</h2>
<p> If multixterm is killed using an uncatchable kill, the xterms are not killed. This appears to be a bug in xterm itself. </p>
<p> Send/expect sequences can be done in multixterm command files. However, due to the richness of the possibilities, to document it properly would take more time than the author has at present. </p>
<h2>REQUIREMENTS</h2>
<p> Requires Expect 5.36.0 or later.<br />
 Requires Tk 8.3.3 or later. </p>
<h2>VERSION</h2>
<p> This man page describes version 1.8 of multixterm. </p>
<p> The latest version of multixterm is available from <a rel="nofollow" href="http://expect.nist.gov/example/multixterm">http://expect.nist.gov/example/multixterm</a> . If your version of Expect and Tk are too old (see REQUIREMENTS above), download a new version of Expect from <a rel="nofollow" href="http://expect.nist.gov">http://expect.nist.gov</a> </p>
<h2>DATE</h2>
<p> April 30, 2002 </p>
<h2>AUTHOR</h2>
<p> Don Libes &lt;don [at] libes.com&gt; </p>
<h2>LICENSE</h2>
<p> Multixterm is in the public domain; however the author would appreciate acknowledgement if multixterm or parts of it or ideas from it are used. </p>
<h2>Index</h2>
