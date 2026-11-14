---
title: "cdk_display(3)"
name: "cdk_display"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cdk_display/"
description: "cdk_display – Curses Development Kit Display Capabilities."
---

<h2>NAME</h2>
<p> cdk_display &#8211; <code>Curses Development Kit</code> Display Capabilities.</p>
<h2>SYNOPSIS</h2>
<p> Cdk has a number of pre-defined display types. The following are outlined in this manual page: </p>
<dl>
<dt>&bull; How To Use Colors</p>
<dd>
<dt>&bull; How To Use Different Character Attributes</p>
<dd>
<dt>&bull; How To Justify Strings</p>
<dd>
<dt>&bull; How To Use Special Drawing Characters</p>
<dd>
<dt>&bull; Edit/Display Type Codes (EDisplayType)</p>
<dd></dl>
<h2>DESCRIPTION</h2>
<p> Cdk has special formatting commands which can be included in any string which add highlights, justification, or even colors to a basic string. These attributes, once set, remain in effect until changed explicitly, or until the end of the string. </p>
<p> This manual page outlines and demonstrates how they work.</p>
<h3>How To Use Colors</h3>
<p> Cdk has the capability to display colors in almost every string type displayed in a Cdk widget. To turn on colors, the function <code>initCDKColor</code> has to be called. When this function is called 64 color pairs are created. Normally the color pairs are accessed via the COLOR_PAIR macro. You can still do this, but creating a string with multiple colors gets terribly difficult. That is why the color commands were created. </p>
<p> The color settings are stored directly in the string. When the widget is created or activated, the string is converted to take advantage of any color commands in the string. To turn on a color pair insert &lt;/XX&gt; into the string; where <i>XX</i> is a numeric value from 0 to 64. Color pair 0 is the standard default color pair for the screen. To turn off a color pair use the format command &lt;!XX&gt; where <i>XX</i> is a numeric value from 0 to 64. </p>
<p> The following example demonstrates the use of the color commands. </p>
<pre><code>

-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

#include &lt;cdk/cdk.h&gt;
                                                         void
                                                         main()
{
    CDKSCREEN *cdkscreen;
    CDKLABEL *demo;
    WINDOW *screen;
    char *mesg[4];
    /* Initialize the Cdk screen.        */
    screen = initscr();
    cdkscreen = initCDKScreen(screen);
    /* Start CDK Colors */
    initCDKColor();
    /* Set the labels up.                */
    mesg[0] = "&lt;/31&gt;This line should have a yellow foreground and a cyan background.&lt;!31&gt;";
    mesg[1] = "&lt;/05&gt;This line should have a white  foreground and a blue background.&lt;!05&gt;";
    mesg[2] = "&lt;/26&gt;This line should have a yellow foreground and a red  background.&lt;!26&gt;";
    mesg[3] = "&lt;C&gt;This line should be set to whatever the screen default is.";
    /* Declare the labels.       */
    demo = newCDKLabel(cdkscreen, CENTER, CENTER, mesg, 4, TRUE, TRUE);
    /* Draw the label            */
    drawCDKLabel(demo, TRUE);
    waitCDKLabel(demo, ' ');
    /* Clean up                  */
    destroyCDKLabel(demo);
    destroyCDKScreen(cdkscreen);
    endCDK();
    exit(0);
}
</code></pre>
<p> <center> <i>&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;-</i><br />
 </center> </p>
<h3>How To Use Different Character Attributes</h3>
<p> Cdk also provides attribute commands which allow different character attributes to be displayed in a Cdk widget. To use a character attribute the format command is <i>&lt;/X&gt;</i> where <i>X</i> is one of several command characters. To turn a attribute off use the command <i>&lt;!X&gt;</i>. The following table outlines the command characters: </p>
<p> <center></p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td><code>Command Character</code></td>
<td>Character Attribute
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>B</td>
<td>Bold
</td>
</tr>
<tr VALIGN=top>
<td>U</td>
<td>Underline
</td>
</tr>
<tr VALIGN=top>
<td>K</td>
<td>Blink
</td>
</tr>
<tr VALIGN=top>
<td>R</td>
<td>Reverse
</td>
</tr>
<tr VALIGN=top>
<td>S</td>
<td>Standout
</td>
</tr>
<tr VALIGN=top>
<td>D</td>
<td>Dim
</td>
</tr>
<tr VALIGN=top>
<td>N</td>
<td>Normal
</td>
</tr>
</table>
</table>
<p></center> </p>
<p> The following example demonstrates the use of character display attributes. </p>
<p>&#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212;</p>
<p>#include &lt;cdk/cdk.h&gt;<br />
                                                         void<br />
                                                         main()<br />
{<br />
    CDKSCREEN *cdkscreen;<br />
    CDKLABEL *demo;<br />
    WINDOW *screen;<br />
    char *mesg[4];<br />
    /* Initialize the Cdk screen.  */<br />
    screen = initscr();<br />
    cdkscreen = initCDKScreen(screen);<br />
    /* Start CDK Colors */<br />
    initCDKColor();<br />
    /* Set the labels up.  */<br />
    mesg[0] = &#8220;&lt;/B/31&gt;Bold text            yellow foreground / blue background.&lt;!31&gt;&#8221;;<br />
    mesg[1] = &#8220;&lt;/U/05&gt;Underlined text      white  foreground / blue background.&lt;!05&gt;&#8221;;<br />
    mesg[2] = &#8220;&lt;/K/26&gt;Blinking text        yellow foreground / red  background.&lt;!26&gt;&#8221;;<br />
    mesg[3] = &#8220;&lt;C&gt;This line uses the screen default colors.&#8221;;<br />
    /* Declare the labels.  */<br />
    demo = newCDKLabel(cdkscreen, CENTER, CENTER, mesg, 4, TRUE, TRUE);<br />
    /* Draw the label */<br />
    drawCDKLabel(demo, TRUE);<br />
    waitCDKLabel(demo, &#8216; &#8216;);<br />
    /* Clean up */<br />
    destroyCDKLabel(demo);<br />
    destroyCDKScreen(cdkscreen);<br />
    endCDK();<br />
    exit(0);<br />
}</p>
<p>&#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212;</p>
<p> Note that color commands and format commands can be mixed inside the same format marker. The above example underlines the label marker, which also sets color pair number 2.</p>
<h3>How To Justify Strings</h3>
<p> Justification commands can left justify, right justify, or center a string of text. To use a justification format in a string the command &lt;X&gt; is used. The following table lists the format commands: </p>
<p> <center></p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td><code>Command</code></td>
<td>Action.
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>&lt;L&gt;</td>
<td>Left Justified. Default if not stated.
</td>
</tr>
<tr VALIGN=top>
<td>&lt;C&gt;</td>
<td>Centered text.
</td>
</tr>
<tr VALIGN=top>
<td>&lt;R&gt;</td>
<td>Right justified.
</td>
</tr>
<tr VALIGN=top>
<td>&lt;I=X&gt;</td>
<td>Indent the line X characters.
</td>
</tr>
<tr VALIGN=top>
<td>&lt;B=X&gt;</td>
<td>Bullet. X is the bullet string to use.
</td>
</tr>
<tr VALIGN=top>
<td>&lt;F=X&gt;</td>
<td> Links in a file where X is the filename. This works only with the viewer widget.
</td>
</tr>
</table>
</table>
<p></center> </p>
<p> The following example demonstrates how to use the justification commands in a Cdk widget. <center> <i>&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;-</i><br />
 </center><br />
#include &lt;cdk/cdk.h&gt;<br />
void main()<br />
{<br />
    CDKSCREEN *cdkscreen;<br />
    CDKLABEL *demo;<br />
    WINDOW *screen;<br />
    char *mesg[5];<br />
    /* Initialize the Cdk screen.  */<br />
    screen = initscr();<br />
    cdkscreen = initCDKScreen(screen);<br />
    /* Start CDK Colors */<br />
    initCDKColor();<br />
    /* Set the labels up.  */<br />
    mesg[0] = &#8220;&lt;R&gt;&lt;/B/31&gt;This line should have a yellow foreground and a blue background.&lt;!31&gt;&#8221;;<br />
    mesg[1] = &#8220;&lt;/U/05&gt;This line should have a white  foreground and a blue background.&lt;!05&gt;&#8221;;<br />
    mesg[2] = &#8220;&lt;B=+&gt;This is a bullet.&#8221;;<br />
    mesg[3] = &#8220;&lt;I=10&gt;This is indented 10 characters.&#8221;;<br />
    mesg[4] = &#8220;&lt;C&gt;This line should be set to whatever the screen default is.&#8221;;<br />
    /* Declare the labels.  */<br />
    demo = newCDKLabel(cdkscreen, CENTER, CENTER, mesg, 5, TRUE, TRUE);<br />
    /* Draw the label */<br />
    drawCDKLabel(demo, TRUE);<br />
    waitCDKLabel(demo, &#8216; &#8216;);<br />
    /* Clean up */<br />
    destroyCDKLabel(demo);<br />
    destroyCDKScreen(cdkscreen);<br />
    endCDK();<br />
    exit(0);<br />
}<br />
 <center> <i>&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;-</i><br />
 </center> </p>
<p> The bullet format command can take either a single character or a string. The bullet in the above example would look like</p>
<dl>
<dt>
<dd> <i>+</i> This is a bullet.</dl>
<p> but if we were to use the following command instead</p>
<dl>
<dt>
<dd> &lt;B=***&gt;This is a bullet.</dl>
<p> it would look like</p>
<dl>
<dt>
<dd> <i>***</i> This is a bullet.</dl>
<p> A format command must be at the beginning of the string.</p>
<h3>How To Use Special Drawing Characters</h3>
<p> Cdk has a set of special drawing characters which can be inserted into any ASCII file. In order to use a special character the format command &lt;#XXX&gt; is used. The following table lists all of the special character commands available. <center></p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td><code>Special_Character</code></td>
<td>Character
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>&lt;#UL&gt;</td>
<td>Upper Left Corner
</td>
</tr>
<tr VALIGN=top>
<td>&lt;#UR&gt;</td>
<td>Upper Right Corner
</td>
</tr>
<tr VALIGN=top>
<td>&lt;#LL&gt;</td>
<td>Lower Left Corner
</td>
</tr>
<tr VALIGN=top>
<td>&lt;#LR&gt;</td>
<td>Lower Right Corner
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>&lt;#LT&gt;</td>
<td>Left Tee
</td>
</tr>
<tr VALIGN=top>
<td>&lt;#RT&gt;</td>
<td>Right Tee
</td>
</tr>
<tr VALIGN=top>
<td>&lt;#TT&gt;</td>
<td>Top Tee
</td>
</tr>
<tr VALIGN=top>
<td>&lt;#BT&gt;</td>
<td>Bottom Tee
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>&lt;#HL&gt;</td>
<td>Horizontal Line
</td>
</tr>
<tr VALIGN=top>
<td>&lt;#VL&gt;</td>
<td>Vertical Line
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>&lt;#PL&gt;</td>
<td>Plus Sign
</td>
</tr>
<tr VALIGN=top>
<td>&lt;#PM&gt;</td>
<td>Plus or Minus Sign
</td>
</tr>
<tr VALIGN=top>
<td>&lt;#DG&gt;</td>
<td>Degree Sign
</td>
</tr>
<tr VALIGN=top>
<td>&lt;#CB&gt;</td>
<td>Checker Board
</td>
</tr>
<tr VALIGN=top>
<td>&lt;#DI&gt;</td>
<td>Diamond
</td>
</tr>
<tr VALIGN=top>
<td>&lt;#BU&gt;</td>
<td>Bullet
</td>
</tr>
<tr VALIGN=top>
<td>&lt;#S1&gt;</td>
<td>Scan line 1
</td>
</tr>
<tr VALIGN=top>
<td>&lt;#S9&gt;</td>
<td>Scan line 9
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>&lt;#LA&gt;</td>
<td>Left Arrow
</td>
</tr>
<tr VALIGN=top>
<td>&lt;#RA&gt;</td>
<td>Right Arrow
</td>
</tr>
<tr VALIGN=top>
<td>&lt;#TA&gt;</td>
<td>Top Arrow
</td>
</tr>
<tr VALIGN=top>
<td>&lt;#BA&gt;</td>
<td>Bottom Arrow
</td>
</tr>
</table>
</table>
<p></center> </p>
<p> The character formats can be repeated using an optional numeric repeat value. To repeat a character add the repeat count within parentheses to the end of the character format. The following example draws 10 horizontal-line characters: </p>
<p> &lt;#HL(10)&gt; </p>
<p> The following example draws a box within a label window: <center> <i>&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;-</i><br />
 </center> </p>
<pre><code>
#include &lt;cdk/cdk.h&gt;
void main()
{
    /* Declare variables.  */
    CDKSCREEN *cdkscreen;
    CDKLABEL *demo;
    WINDOW *cursesWin;
    char *mesg[4];
    /* Set up CDK */
    cursesWin = initscr();
    cdkscreen = initCDKScreen(cursesWin);
    /* Start CDK Colors */
    initCDKColor();
    /* Set the labels up.  */
    mesg[0] = "&lt;C&gt;&lt;#UL&gt;&lt;#HL(26)&gt;&lt;#UR&gt;";
    mesg[1] = "&lt;C&gt;&lt;#VL&gt;&lt;/R&gt;This text should be boxed.&lt;!R&gt;&lt;#VL&gt;";
    mesg[2] = "&lt;C&gt;&lt;#LL&gt;&lt;#HL(26)&gt;&lt;#LR&gt;";
    mesg[3] = "&lt;C&gt;While this is not.";
    /* Declare the labels.  */
    demo = newCDKLabel(cdkscreen, CENTER, CENTER, mesg, 4, TRUE, TRUE);
    /* Is the label NULL???  */
    if (demo == (CDKLABEL *)NULL) {
        /* Clean up the memory.  */
        destroyCDKScreen(cdkscreen);
        /* End curses...  */
        endCDK();
        /* Spit out a message.  */
        printf("Oops. Can't seem to create the label. Is the window too small?
");
        exit(1);
    }
    /* Draw the CDK screen.  */
    refreshCDKScreen(cdkscreen);
    waitCDKLabel(demo, ' ');
    /* Clean up */
    destroyCDKLabel(demo);
    destroyCDKScreen(cdkscreen);
    delwin(cursesWin);
    endCDK();
    exit(0);
}
</code></pre>
<p> <center> <i>&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;-</i><br />
 </center> </p>
<p> Notice that drawn text can also be justified. </p>
<h3>Edit/Display Type Codes (EDisplayType)</h3>
<p> <center></p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td><code>Display_Type</code></td>
<td>Result
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>vCHAR</td>
<td>Only accepts alphabetic characters.
</td>
</tr>
<tr VALIGN=top>
<td>vLCHAR</td>
<td> Only accepts alphabetic characters. Maps the character to lower case when a character has been accepted.
</td>
</tr>
<tr VALIGN=top>
<td>vUCHAR</td>
<td> Only accepts alphabetic characters. Maps the character to upper case when a character has been accepted.
</td>
</tr>
<tr VALIGN=top>
<td>vHCHAR</td>
<td> Only accepts alphabetic characters. Displays a period (<i>.</i>) when a character has been accepted.
</td>
</tr>
<tr VALIGN=top>
<td>vUHCHAR</td>
<td> Only accepts alphabetic characters. Displays a period (<i>.</i>) and maps the character to upper case when a character has been accepted.
</td>
</tr>
<tr VALIGN=top>
<td>vLHCHAR</td>
<td> Only accepts alphabetic characters. Displays a period (<i>.</i>) and maps the character to lower case when a character has been accepted.
</td>
</tr>
<tr VALIGN=top>
<td>vINT</td>
<td> Only accepts numeric characters.
</td>
</tr>
<tr VALIGN=top>
<td>vHINT</td>
<td> Only accepts numeric characters. Displays a period (<i>.</i>) when a character has been accepted.
</td>
</tr>
<tr VALIGN=top>
<td>vMIXED</td>
<td>Accepts any character types.
</td>
</tr>
<tr VALIGN=top>
<td>vLMIXED</td>
<td> Accepts any character types. Maps the character to lower case when an alphabetic character has been accepted.
</td>
</tr>
<tr VALIGN=top>
<td>vUMIXED</td>
<td> Accepts any character types. Maps the character to upper case when an alphabetic character has been accepted.
</td>
</tr>
<tr VALIGN=top>
<td>vHMIXED</td>
<td> Accepts any character types. Displays a period (<i>.</i>) when a character has been accepted.
</td>
</tr>
<tr VALIGN=top>
<td>vLHMIXED</td>
<td> Accepts any character types. Displays a period (<i>.</i>) and maps the character to lower case when a character has been accepted.
</td>
</tr>
<tr VALIGN=top>
<td>vUHMIXED</td>
<td> Accepts any character types. Displays a period (<i>.</i>) and maps the character to upper case when a character has been accepted.
</td>
</tr>
<tr VALIGN=top>
<td>vVIEWONLY</td>
<td>Uneditable field.
</td>
</tr>
</table>
</table>
<p></center></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-cdk/">cdk</a></code>(3), <code><a href="/docs/linux/man/3-cdk_binding/">cdk_binding</a></code>(3), <code><a href="/docs/linux/man/3-cdk_screen/">cdk_screen</a></code>(3) </p>
<h2>Index</h2>
