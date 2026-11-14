---
title: "terminfo(5)"
name: "terminfo"
section: "5"
letter: "t"
url: "/docs/linux/man/5-terminfo/"
description: "terminfo – terminal capability database"
---

<p>terminfo &#8211; terminal capability database</p>
<h2>Synopsis</h2>
<p>/etc/terminfo/*/*</p>
<h2>Description</h2>
<p><i>Terminfo</i> is a database describing terminals, used by screen-oriented programs such as <code><a href="/docs/linux/man/1-nvi/">nvi</a></code>(1), <code><a href="/docs/linux/man/1-lynx/">lynx</a></code>(1), <code><a href="/docs/linux/man/1-mutt/">mutt</a></code>(1), and other curses applications, using high-level calls to libraries such as <code>ncurses</code>(3NCURSES). It is also used via low-level calls by non-curses applications which may be screen-oriented (such as <code><a href="/docs/linux/man/1-clear/">clear</a></code>(1)) or non-screen (such as <code><a href="/docs/linux/man/1-tabs/">tabs</a></code>(1)). <i>Terminfo</i> describes terminals by giving a set of capabilities which they have, by specifying how to perform screen operations, and by specifying padding requirements and initialization sequences. This manual describes <code>ncurses</code> version 6.3 (patch 20211021).</p>
<h3>Terminfo Entry Syntax</h3>
<p>Entries in <i>terminfo</i> consist of a sequence of fields:<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 Each field ends with a comma &#8220;,&#8221; (embedded commas may be escaped with a backslash or written as &#8220;,&#8221;).<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 White space between fields is ignored.<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 The first field in a <i>terminfo</i> entry begins in the first column.<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 Newlines and leading whitespace (spaces or tabs) may be used for formatting entries for readability. These are removed from parsed entries.</p>
<dl>
<dd>The <code>infocmp</code> <code>-f</code> and <code>-W</code> options rely on this to format if-then-else expressions, or to enforce maximum line-width. The resulting formatted terminal description can be read by <code>tic</code>.<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 The first field for each terminal gives the names which are known for the terminal, separated by &#8220;|&#8221; characters.</p>
<dd>The first name given is the most common abbreviation for the terminal (its primary name), the last name given should be a long name fully identifying the terminal (see <code><a href="//www.systutorials.com/docs/linux/man/3X-longname/">longname</a></code>(3X)), and all others are treated as synonyms (aliases) for the primary terminal name.</p>
<dd>X/Open Curses advises that all names but the last should be in lower case and contain no blanks; the last name may well contain upper case and blanks for readability.</p>
<dd>This implementation is not so strict; it allows mixed case in the primary name and aliases. If the last name has no embedded blanks, it allows that to be both an alias and a verbose name (but will warn about this ambiguity).<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 Lines beginning with a &#8220;#&#8221; in the first column are treated as comments.</p>
<dd>While comment lines are legal at any point, the output of <code>captoinfo</code> and <code>infotocap</code> (aliases for <code>tic</code>) will move comments so they occur only between entries.</dl>
<p> Terminal names (except for the last, verbose entry) should be chosen using the following conventions. The particular piece of hardware making up the terminal should have a root name, thus &#8220;hp2621&#8221;. This name should not contain hyphens. Modes that the hardware can be in, or user preferences, should be indicated by appending a hyphen and a mode suffix. Thus, a vt100 in 132-column mode would be vt100-w. The following suffixes should be used where possible: <center></p>
<table>
<tr VALIGN=top>
<td><code>Suffix</code></td>
<td ALIGN=center>Meaning</td>
<td>Example
</td>
</tr>
<tr VALIGN=top>
<td>&#8211;<i>nn</i></td>
<td>Number of lines on the screen</td>
<td>aaa-60
</td>
</tr>
<tr VALIGN=top>
<td>&#8211;<i>n</i>p</td>
<td>Number of pages of memory</td>
<td>c100-4p
</td>
</tr>
<tr VALIGN=top>
<td>-am</td>
<td>With automargins (usually the default)</td>
<td>vt100-am
</td>
</tr>
<tr VALIGN=top>
<td>-m</td>
<td>Mono mode; suppress color </td>
<td>ansi-m
</td>
</tr>
<tr VALIGN=top>
<td>-mc</td>
<td>Magic cookie; spaces when highlighting</td>
<td>wy30-mc
</td>
</tr>
<tr VALIGN=top>
<td>-na</td>
<td>No arrow keys (leave them in local)</td>
<td>c100-na
</td>
</tr>
<tr VALIGN=top>
<td>-nam</td>
<td>Without automatic margins </td>
<td>vt100-nam
</td>
</tr>
<tr VALIGN=top>
<td>-nl</td>
<td>No status line </td>
<td>att4415-nl
</td>
</tr>
<tr VALIGN=top>
<td>-ns</td>
<td>No status line </td>
<td>hp2626-ns
</td>
</tr>
<tr VALIGN=top>
<td>-rv</td>
<td>Reverse video </td>
<td>c100-rv
</td>
</tr>
<tr VALIGN=top>
<td>-s</td>
<td>Enable status line </td>
<td>vt100-s
</td>
</tr>
<tr VALIGN=top>
<td>-vb</td>
<td>Use visible bell instead of beep</td>
<td>wy370-vb
</td>
</tr>
<tr VALIGN=top>
<td>-w</td>
<td>Wide mode (&gt; 80 columns, usually 132)</td>
<td>vt100-w
</td>
</tr>
</table>
<p></center> For more on terminal naming conventions, see the <code><a href="/docs/linux/man/7-term/">term</a></code>(7) manual page.</p>
<h3>Terminfo Capabilities Syntax</h3>
<p>The terminfo entry consists of several <i>capabilities</i>, i.e., features that the terminal has, or methods for exercising the terminal&#8217;s features. After the first field (giving the name(s) of the terminal entry), there should be one or more <i>capability</i> fields. These are boolean, numeric or string names with corresponding values:<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 Boolean capabilities are true when present, false when absent. There is no explicit value for boolean capabilities.<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 Numeric capabilities have a &#8220;#&#8221; following the name, then an unsigned decimal integer value.<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 String capabilities have a &#8220;=&#8221; following the name, then an string of characters making up the capability value.</p>
<dl>
<dd>String capabilities can be split into multiple lines, just as the fields comprising a terminal entry can be split into multiple lines. While blanks between fields are ignored, blanks embedded within a string value are retained, except for leading blanks on a line.</dl>
<p> Any capability can be <i>canceled</i>, i.e., suppressed from the terminal entry, by following its name with &#8220;@&#8221; rather than a capability value.</p>
<h3>Similar Terminals</h3>
<p>If there are two very similar terminals, one (the variant) can be defined as being just like the other (the base) with certain exceptions. In the definition of the variant, the string capability <code>use</code> can be given with the name of the base terminal:<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 The capabilities given before <code>use</code> override those in the base type named by <code>use</code>.<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 If there are multiple <code>use</code> capabilities, they are merged in reverse order. That is, the rightmost <code>use</code> reference is processed first, then the one to its left, and so forth.<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 Capabilities given explicitly in the entry override those brought in by <code>use</code> references. A capability can be canceled by placing <code>xx@</code> to the left of the use reference that imports it, where <i>xx</i> is the capability. For example, the entry</p>
<dl>
<dd>2621-nl, smkx@, rmkx@, use=2621,</dl>
<p> defines a 2621-nl that does not have the <code>smkx</code> or <code>rmkx</code> capabilities, and hence does not turn on the function key labels when in visual mode. This is useful for different modes for a terminal, or for different user preferences. An entry included via <code>use</code> can contain canceled capabilities, which have the same effect as if those cancels were inline in the using terminal entry.</p>
<h3>Predefined Capabilities</h3>
<p><font SIZE="-1"> The following is a complete table of the capabilities included in a terminfo description block and available to terminfo-using code. In each line of the table, The <code>variable</code> is the name by which the programmer (at the terminfo level) accesses the capability. The <code>capname</code> is the short name used in the text of the database, and is used by a person updating the database. Whenever possible, capnames are chosen to be the same as or similar to the ANSI X3.64-1979 standard (now superseded by ECMA-48, which uses identical or very similar names). Semantics are also intended to match those of the specification. The termcap code is the old <code>termcap</code> capability name (some capabilities are new, and have names which termcap did not originate). Capability names have no hard length limit, but an informal limit of 5 characters has been adopted to keep them short and to allow the tabs in the source file <code>Caps</code> to line up nicely. Finally, the description field attempts to convey the semantics of the capability. You may find some codes in the description field:</p>
<dl>
<dt>(P)</p>
<dd>indicates that padding may be specified</p>
<dt>#[1-9]</p>
<dd>in the description field indicates that the string is passed through <code><a href="//www.systutorials.com/docs/linux/man/3X-tparm/">tparm</a></code>(3X) with parameters as given (#<i>i</i>).</p>
<dd>If no parameters are listed in the description, passing the string through <code><a href="//www.systutorials.com/docs/linux/man/3X-tparm/">tparm</a></code>(3X) may give unexpected results, e.g., if it contains percent (%%) signs.</p>
<dt>(P*)</p>
<dd>indicates that padding may vary in proportion to the number of lines affected</p>
<dt>(#<i>i</i>)</p>
<dd>indicates the <i>i</i>th parameter.  These are the boolean capabilities: </font><center></p>
<table>
<tr VALIGN=top>
<td ALIGN=center><code>Variable</code></td>
<td>Cap-</td>
<td>TCap</td>
<td ALIGN=center>Description
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center><code>Booleans</code></td>
<td>name</td>
<td>Code</td>
<td ALIGN=center>
</td>
</tr>
<tr VALIGN=top>
<td>auto_left_margin</td>
<td>bw</td>
<td>bw</td>
<td> cub1 wraps from column 0 to last column
</td>
</tr>
<tr VALIGN=top>
<td>auto_right_margin</td>
<td>am</td>
<td>am</td>
<td> terminal has automatic margins
</td>
</tr>
<tr VALIGN=top>
<td>back_color_erase</td>
<td>bce</td>
<td>ut</td>
<td> screen erased with background color
</td>
</tr>
<tr VALIGN=top>
<td>can_change</td>
<td>ccc</td>
<td>cc</td>
<td> terminal can re-define existing colors
</td>
</tr>
<tr VALIGN=top>
<td>ceol_standout_glitch</td>
<td>xhp</td>
<td>xs</td>
<td> standout not erased by overwriting (hp)
</td>
</tr>
<tr VALIGN=top>
<td>col_addr_glitch</td>
<td>xhpa</td>
<td>YA</td>
<td> only positive motion for hpa/mhpa caps
</td>
</tr>
<tr VALIGN=top>
<td>cpi_changes_res</td>
<td>cpix</td>
<td>YF</td>
<td> changing character pitch changes resolution
</td>
</tr>
<tr VALIGN=top>
<td>cr_cancels_micro_mode</td>
<td>crxm</td>
<td>YB</td>
<td> using cr turns off micro mode
</td>
</tr>
<tr VALIGN=top>
<td>dest_tabs_magic_smso</td>
<td>xt</td>
<td>xt</td>
<td> tabs destructive, magic so char (t1061)
</td>
</tr>
<tr VALIGN=top>
<td>eat_newline_glitch</td>
<td>xenl</td>
<td>xn</td>
<td> newline ignored after 80 cols (concept)
</td>
</tr>
<tr VALIGN=top>
<td>erase_overstrike</td>
<td>eo</td>
<td>eo</td>
<td> can erase overstrikes with a blank
</td>
</tr>
<tr VALIGN=top>
<td>generic_type</td>
<td>gn</td>
<td>gn</td>
<td> generic line type
</td>
</tr>
<tr VALIGN=top>
<td>hard_copy</td>
<td>hc</td>
<td>hc</td>
<td> hardcopy terminal
</td>
</tr>
<tr VALIGN=top>
<td>hard_cursor</td>
<td>chts</td>
<td>HC</td>
<td> cursor is hard to see
</td>
</tr>
<tr VALIGN=top>
<td>has_meta_key</td>
<td>km</td>
<td>km</td>
<td> Has a meta key (i.e., sets 8th-bit)
</td>
</tr>
<tr VALIGN=top>
<td>has_print_wheel</td>
<td>daisy</td>
<td>YC</td>
<td> printer needs operator to change character set
</td>
</tr>
<tr VALIGN=top>
<td>has_status_line</td>
<td>hs</td>
<td>hs</td>
<td> has extra status line
</td>
</tr>
<tr VALIGN=top>
<td>hue_lightness_saturation</td>
<td>hls</td>
<td>hl</td>
<td> terminal uses only HLS color notation (Tektronix)
</td>
</tr>
<tr VALIGN=top>
<td>insert_null_glitch</td>
<td>in</td>
<td>in</td>
<td> insert mode distinguishes nulls
</td>
</tr>
<tr VALIGN=top>
<td>lpi_changes_res</td>
<td>lpix</td>
<td>YG</td>
<td> changing line pitch changes resolution
</td>
</tr>
<tr VALIGN=top>
<td>memory_above</td>
<td>da</td>
<td>da</td>
<td> display may be retained above the screen
</td>
</tr>
<tr VALIGN=top>
<td>memory_below</td>
<td>db</td>
<td>db</td>
<td> display may be retained below the screen
</td>
</tr>
<tr VALIGN=top>
<td>move_insert_mode</td>
<td>mir</td>
<td>mi</td>
<td> safe to move while in insert mode
</td>
</tr>
<tr VALIGN=top>
<td>move_standout_mode</td>
<td>msgr</td>
<td>ms</td>
<td> safe to move while in standout mode
</td>
</tr>
<tr VALIGN=top>
<td>needs_xon_xoff</td>
<td>nxon</td>
<td>nx</td>
<td> padding will not work, xon/xoff required
</td>
</tr>
<tr VALIGN=top>
<td>no_esc_ctlc</td>
<td>xsb</td>
<td>xb</td>
<td> beehive (f1=escape, f2=ctrl C)
</td>
</tr>
<tr VALIGN=top>
<td>no_pad_char</td>
<td>npc</td>
<td>NP</td>
<td> pad character does not exist
</td>
</tr>
<tr VALIGN=top>
<td>non_dest_scroll_region</td>
<td>ndscr</td>
<td>ND</td>
<td> scrolling region is non-destructive
</td>
</tr>
<tr VALIGN=top>
<td>non_rev_rmcup</td>
<td>nrrmc</td>
<td>NR</td>
<td> smcup does not reverse rmcup
</td>
</tr>
<tr VALIGN=top>
<td>over_strike</td>
<td>os</td>
<td>os</td>
<td> terminal can overstrike
</td>
</tr>
<tr VALIGN=top>
<td>prtr_silent</td>
<td>mc5i</td>
<td>5i</td>
<td> printer will not echo on screen
</td>
</tr>
<tr VALIGN=top>
<td>row_addr_glitch</td>
<td>xvpa</td>
<td>YD</td>
<td> only positive motion for vpa/mvpa caps
</td>
</tr>
<tr VALIGN=top>
<td>semi_auto_right_margin</td>
<td>sam</td>
<td>YE</td>
<td> printing in last column causes cr
</td>
</tr>
<tr VALIGN=top>
<td>status_line_esc_ok</td>
<td>eslok</td>
<td>es</td>
<td> escape can be used on the status line
</td>
</tr>
<tr VALIGN=top>
<td>tilde_glitch</td>
<td>hz</td>
<td>hz</td>
<td> cannot print ~&#8217;s (Hazeltine)
</td>
</tr>
<tr VALIGN=top>
<td>transparent_underline</td>
<td>ul</td>
<td>ul</td>
<td> underline character overstrikes
</td>
</tr>
<tr VALIGN=top>
<td>xon_xoff</td>
<td>xon</td>
<td>xo</td>
<td> terminal uses xon/xoff handshaking
</td>
</tr>
</table>
<p></center> <font SIZE="-1"> These are the numeric capabilities: </font><center></p>
<table>
<tr VALIGN=top>
<td ALIGN=center><code>Variable</code></td>
<td>Cap-</td>
<td>TCap</td>
<td ALIGN=center>Description
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center><code>Numeric</code></td>
<td>name</td>
<td>Code</td>
<td ALIGN=center>
</td>
</tr>
<tr VALIGN=top>
<td>columns</td>
<td>cols</td>
<td>co</td>
<td> number of columns in a line
</td>
</tr>
<tr VALIGN=top>
<td>init_tabs</td>
<td>it</td>
<td>it</td>
<td> tabs initially every # spaces
</td>
</tr>
<tr VALIGN=top>
<td>label_height</td>
<td>lh</td>
<td>lh</td>
<td> rows in each label
</td>
</tr>
<tr VALIGN=top>
<td>label_width</td>
<td>lw</td>
<td>lw</td>
<td> columns in each label
</td>
</tr>
<tr VALIGN=top>
<td>lines</td>
<td>lines</td>
<td>li</td>
<td> number of lines on screen or page
</td>
</tr>
<tr VALIGN=top>
<td>lines_of_memory</td>
<td>lm</td>
<td>lm</td>
<td> lines of memory if &gt; line. 0 means varies
</td>
</tr>
<tr VALIGN=top>
<td>magic_cookie_glitch</td>
<td>xmc</td>
<td>sg</td>
<td> number of blank characters left by smso or rmso
</td>
</tr>
<tr VALIGN=top>
<td>max_attributes</td>
<td>ma</td>
<td>ma</td>
<td> maximum combined attributes terminal can handle
</td>
</tr>
<tr VALIGN=top>
<td>max_colors</td>
<td>colors</td>
<td>Co</td>
<td> maximum number of colors on screen
</td>
</tr>
<tr VALIGN=top>
<td>max_pairs</td>
<td>pairs</td>
<td>pa</td>
<td> maximum number of color-pairs on the screen
</td>
</tr>
<tr VALIGN=top>
<td>maximum_windows</td>
<td>wnum</td>
<td>MW</td>
<td> maximum number of definable windows
</td>
</tr>
<tr VALIGN=top>
<td>no_color_video</td>
<td>ncv</td>
<td>NC</td>
<td> video attributes that cannot be used with colors
</td>
</tr>
<tr VALIGN=top>
<td>num_labels</td>
<td>nlab</td>
<td>Nl</td>
<td> number of labels on screen
</td>
</tr>
<tr VALIGN=top>
<td>padding_baud_rate</td>
<td>pb</td>
<td>pb</td>
<td> lowest baud rate where padding needed
</td>
</tr>
<tr VALIGN=top>
<td>virtual_terminal</td>
<td>vt</td>
<td>vt</td>
<td> virtual terminal number (CB/unix)
</td>
</tr>
<tr VALIGN=top>
<td>width_status_line</td>
<td>wsl</td>
<td>ws</td>
<td> number of columns in status line
</td>
</tr>
</table>
<p></center> <font SIZE="-1"> The following numeric capabilities are present in the SVr4.0 term structure, but are not yet documented in the man page. They came in with SVr4&#8217;s printer support. </font><center></p>
<table>
<tr VALIGN=top>
<td ALIGN=center><code>Variable</code></td>
<td>Cap-</td>
<td>TCap</td>
<td ALIGN=center>Description
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center><code>Numeric</code></td>
<td>name</td>
<td>Code</td>
<td ALIGN=center>
</td>
</tr>
<tr VALIGN=top>
<td>bit_image_entwining</td>
<td>bitwin</td>
<td>Yo</td>
<td> number of passes for each bit-image row
</td>
</tr>
<tr VALIGN=top>
<td>bit_image_type</td>
<td>bitype</td>
<td>Yp</td>
<td> type of bit-image device
</td>
</tr>
<tr VALIGN=top>
<td>buffer_capacity</td>
<td>bufsz</td>
<td>Ya</td>
<td> numbers of bytes buffered before printing
</td>
</tr>
<tr VALIGN=top>
<td>buttons</td>
<td>btns</td>
<td>BT</td>
<td> number of buttons on mouse
</td>
</tr>
<tr VALIGN=top>
<td>dot_horz_spacing</td>
<td>spinh</td>
<td>Yc</td>
<td> spacing of dots horizontally in dots per inch
</td>
</tr>
<tr VALIGN=top>
<td>dot_vert_spacing</td>
<td>spinv</td>
<td>Yb</td>
<td> spacing of pins vertically in pins per inch
</td>
</tr>
<tr VALIGN=top>
<td>max_micro_address</td>
<td>maddr</td>
<td>Yd</td>
<td> maximum value in micro_&#8230;_address
</td>
</tr>
<tr VALIGN=top>
<td>max_micro_jump</td>
<td>mjump</td>
<td>Ye</td>
<td> maximum value in parm_&#8230;_micro
</td>
</tr>
<tr VALIGN=top>
<td>micro_col_size</td>
<td>mcs</td>
<td>Yf</td>
<td> character step size when in micro mode
</td>
</tr>
<tr VALIGN=top>
<td>micro_line_size</td>
<td>mls</td>
<td>Yg</td>
<td> line step size when in micro mode
</td>
</tr>
<tr VALIGN=top>
<td>number_of_pins</td>
<td>npins</td>
<td>Yh</td>
<td> numbers of pins in print-head
</td>
</tr>
<tr VALIGN=top>
<td>output_res_char</td>
<td>orc</td>
<td>Yi</td>
<td> horizontal resolution in units per line
</td>
</tr>
<tr VALIGN=top>
<td>output_res_horz_inch</td>
<td>orhi</td>
<td>Yk</td>
<td> horizontal resolution in units per inch
</td>
</tr>
<tr VALIGN=top>
<td>output_res_line</td>
<td>orl</td>
<td>Yj</td>
<td> vertical resolution in units per line
</td>
</tr>
<tr VALIGN=top>
<td>output_res_vert_inch</td>
<td>orvi</td>
<td>Yl</td>
<td> vertical resolution in units per inch
</td>
</tr>
<tr VALIGN=top>
<td>print_rate</td>
<td>cps</td>
<td>Ym</td>
<td> print rate in characters per second
</td>
</tr>
<tr VALIGN=top>
<td>wide_char_size</td>
<td>widcs</td>
<td>Yn</td>
<td> character step size when in double wide mode
</td>
</tr>
</table>
<p></center> <font SIZE="-1"> These are the string capabilities: </p>
<pre><code>VariableCap - TCapDescription

                  StringnameCode

                      acs_charsacscac
                          graphics charset pairs,
    based on vt100

        back_tabcbtbt
            back
            tab(P)

bellbelbl
    audible
    signal(bell)(P)

        carriage_returncrcr
    carriage return (P *)(P *)

        change_char_pitchcpiZA
    Change number of characters per inch to #1

    change_line_pitchlpiZB
    Change number of lines per inch to #1

    change_res_horzchrZC
    Change horizontal resolution to #1

    change_res_vertcvrZD
    Change vertical resolution to #1

    change_scroll_regioncsrcs
    change region to line #1 to line #2(P)

        char_paddingrmprP
    like ip but when in insert mode

    clear_all_tabstbcct
    clear all tab stops(P)

clear_marginsmgcMC
    clear right and left soft margins

        clear_screenclearcl
            clear screen and home
            cursor(P *)

                clr_bolel1cb
    Clear to beginning of line

    clr_eolelce
    clear to end of line(P)

clr_eosedcd
    clear to end of
    screen(P *)

        column_addresshpach
    horizontal position #1,
    absolute(P)

        command_charactercmdchCC
    terminal settable cmd character in prototype !
    ?

    create_windowcwinCW
    define a window #1 from #2,
    #3 to #4, #5

    cursor_addresscupcm move to row #1 columns #2

    cursor_downcud1do down one line

    cursor_homehomeho home cursor(if no cup)

        cursor_invisiblecivisvi make cursor invisible

    cursor_leftcub1le move left one space

    cursor_mem_addressmrcupCM memory relative cursor addressing,
    move to row #1 columns #2

        cursor_normalcnormve
        make cursor appear normal(undo civis / cvvis)

            cursor_rightcuf1nd
        non
        - destructive space(move right one space)

              cursor_to_llllll
        last line,
    first column(if no cup)

        cursor_upcuu1up
    up one line

    cursor_visiblecvvisvs
    make cursor very visible

    define_chardefcZE
    Define a character #1,
    #2 dots wide, descender #3

    delete_characterdch1dc delete character(P *)

        delete_linedl1dl delete line(P *)

            dial_phonedialDI dial number #1

    dis_status_linedslds disable status line

    display_clockdclkDK display clock

    down_half_linehdhd half a line down

    ena_acsenacseA enable alternate char set

    enter_alt_charset_modesmacsas start alternate character set(P)

enter_am_modesmamSA
        turn on automatic margins

            enter_blink_modeblinkmb
                turn on blinking

                    enter_bold_modeboldmd
                        turn on
                        bold(extra bright) mode

    enter_ca_modesmcupti
    string to start programs using cup

    enter_delete_modesmdcdm
    enter delete mode

    enter_dim_modedimmh
    turn on half
    - bright mode

    enter_doublewide_modeswidmZF Enter double -
    wide mode

    enter_draft_qualitysdrfqZG
    Enter draft
    - quality mode

    enter_insert_modesmirim enter insert mode

    enter_italics_modesitmZH Enter italic mode

    enter_leftward_modeslmZI Start leftward carriage motion

    enter_micro_modesmicmZJ Start micro
    - motion mode

    enter_near_letter_qualitysnlqZK Enter NLQ mode

    enter_normal_qualitysnrmqZL Enter normal
    - quality mode

    enter_protected_modeprotmp turn on protected mode

    enter_reverse_moderevmr turn on reverse video mode

    enter_secure_modeinvismk turn on blank mode(characters invisible)

        enter_shadow_modesshmZM Enter shadow
    - print mode

          enter_standout_modesmsoso begin standout mode

          enter_subscript_modessubmZN Enter subscript mode

          enter_superscript_modessupmZO Enter superscript mode

          enter_underline_modesmulus begin underline mode

          enter_upward_modesumZP Start upward carriage motion

          enter_xon_modesmxonSX turn on xon
          / xoff handshaking

          erase_charsechec erase #1 characters(P)

              exit_alt_charset_modermacsae end alternate character set(P)

exit_am_modermamRA
turn off automatic margins


exit_attribute_modesgr0me
turn off all attributes


exit_ca_modermcupte
strings to end programs using cup


exit_delete_modermdced
end delete mode


exit_doublewide_moderwidmZQ
End double-wide mode


exit_insert_modermirei
exit insert mode


exit_italics_moderitmZR
End italic mode


exit_leftward_moderlmZS
End left-motion mode


exit_micro_modermicmZT
End micro-motion mode


exit_shadow_modershmZU
End shadow-print mode


exit_standout_modermsose
exit standout mode


exit_subscript_modersubmZV
End subscript mode


exit_superscript_modersupmZW
End superscript mode


exit_underline_modermulue
exit underline mode


exit_upward_moderumZX
End reverse character motion


exit_xon_modermxonRX
turn off xon/xoff handshaking


fixed_pausepausePA
pause for 2-3 seconds


flash_hookhookfh
flash switch hook


flash_screenflashvb
visible bell (may not move cursor)


form_feedffff
hardcopy terminal page eject (P*)


from_status_linefslfs
return from status line


goto_windowwingoWG
go to window #1


hanguphupHU
hang-up phone


init_1stringis1i1
initialization string


init_2stringis2is
initialization string


init_3stringis3i3
initialization string


init_fileifif
name of initialization file


init_progiprogiP
path name of program for initialization


initialize_colorinitcIc
initialize color #1 to (#2,#3,#4)


initialize_pairinitpIp
Initialize color pair #1 to fg=(#2,#3,#4), bg=(#5,#6,#7)


insert_characterich1ic
insert character (P)

insert_lineil1al
            insert
            line(P *)

                insert_paddingipip
        insert padding after inserted character

        key_a1ka1K1
        upper left of keypad

        key_a3ka3K3
        upper right of keypad

        key_b2kb2K2
        center of keypad

        key_backspacekbskb
        backspace key

        key_begkbeg @1 begin key

        key_btabkcbtkB
        back
        - tab key

        key_c1kc1K4 lower left of keypad

        key_c3kc3K5 lower right of keypad

        key_cancelkcan @2 cancel key

        key_catabktbcka clear
        - all - tabs key

        key_clearkclrkC clear
        - screen
    or erase key

           key_closekclo @3 close key

           key_commandkcmd @4 command key

           key_copykcpy @5 copy key

           key_createkcrt @6 create key

           key_ctabkctabkt clear
           - tab key

           key_dckdch1kD delete -
           character key

           key_dlkdl1kL delete -
           line key

           key_downkcud1kd down
           - arrow key

           key_eickrmirkM sent by rmir
    or smir in insert mode

               key_endkend @7 end key

               key_enterkent @8 enter
               / send key

               key_eolkelkE clear
           - to - end - of - line key

           key_eoskedkS clear
           - to - end - of - screen key

           key_exitkext @9 exit key

           key_f0kf0k0 F0 function key

           key_f1kf1k1 F1 function key

           key_f10kf10k;
F10 function key

                key_f11kf11F1
                    F11 function key

                        key_f12kf12F2
                            F12 function key

                                key_f13kf13F3
                                    F13 function key

                                        key_f14kf14F4
                                            F14 function key

                                                key_f15kf15F5
                                                    F15 function key

                                                        key_f16kf16F6
                                                            F16 function key

                                                                key_f17kf17F7
                                                                    F17 function key

                                                                        key_f18kf18F8
                                                                            F18 function key

                                                                                key_f19kf19F9
                                                                                    F19 function key

                                                                                        key_f2kf2k2
                                                                                            F2 function key

                                                                                                key_f20kf20FA
                                                                                                    F20 function key

                                                                                                        key_f21kf21FB
                                                                                                            F21 function key

                                                                                                                key_f22kf22FC
                                                                                                                    F22 function key

                                                                                                                        key_f23kf23FD
                                                                                                                            F23 function key

                                                                                                                                key_f24kf24FE
                                                                                                                                    F24 function key

                                                                                                                                        key_f25kf25FF
                                                                                                                                            F25 function key

                                                                                                                                                key_f26kf26FG
                                                                                                                                                    F26 function key

                                                                                                                                                        key_f27kf27FH
                                                                                                                                                            F27 function key

                                                                                                                                                                key_f28kf28FI
                                                                                                                                                                    F28 function key

                                                                                                                                                                        key_f29kf29FJ
                                                                                                                                                                            F29 function key

                                                                                                                                                                                key_f3kf3k3
                                                                                                                                                                                    F3 function key

                                                                                                                                                                                        key_f30kf30FK
                                                                                                                                                                                            F30 function key

                                                                                                                                                                                                key_f31kf31FL
                                                                                                                                                                                                    F31 function key

                                                                                                                                                                                                        key_f32kf32FM
                                                                                                                                                                                                            F32 function key

                                                                                                                                                                                                                key_f33kf33FN
                                                                                                                                                                                                                    F33 function key

                                                                                                                                                                                                                        key_f34kf34FO
                                                                                                                                                                                                                            F34 function key

                                                                                                                                                                                                                                key_f35kf35FP
                                                                                                                                                                                                                                    F35 function key

                                                                                                                                                                                                                                        key_f36kf36FQ
                                                                                                                                                                                                                                            F36 function key

                                                                                                                                                                                                                                                key_f37kf37FR
                                                                                                                                                                                                                                                    F37 function key

                                                                                                                                                                                                                                                        key_f38kf38FS
                                                                                                                                                                                                                                                            F38 function key

                                                                                                                                                                                                                                                                key_f39kf39FT
                                                                                                                                                                                                                                                                    F39 function key

                                                                                                                                                                                                                                                                        key_f4kf4k4
                                                                                                                                                                                                                                                                            F4 function key

                                                                                                                                                                                                                                                                                key_f40kf40FU
                                                                                                                                                                                                                                                                                    F40 function key

                                                                                                                                                                                                                                                                                        key_f41kf41FV
                                                                                                                                                                                                                                                                                            F41 function key

                                                                                                                                                                                                                                                                                                key_f42kf42FW
                                                                                                                                                                                                                                                                                                    F42 function key

                                                                                                                                                                                                                                                                                                        key_f43kf43FX
                                                                                                                                                                                                                                                                                                            F43 function key

                                                                                                                                                                                                                                                                                                                key_f44kf44FY
                                                                                                                                                                                                                                                                                                                    F44 function key

                                                                                                                                                                                                                                                                                                                        key_f45kf45FZ
                                                                                                                                                                                                                                                                                                                            F45 function key

                                                                                                                                                                                                                                                                                                                                key_f46kf46Fa
                                                                                                                                                                                                                                                                                                                                    F46 function key

                                                                                                                                                                                                                                                                                                                                        key_f47kf47Fb
                                                                                                                                                                                                                                                                                                                                            F47 function key

                                                                                                                                                                                                                                                                                                                                                key_f48kf48Fc
                                                                                                                                                                                                                                                                                                                                                    F48 function key

                                                                                                                                                                                                                                                                                                                                                        key_f49kf49Fd
                                                                                                                                                                                                                                                                                                                                                            F49 function key

                                                                                                                                                                                                                                                                                                                                                                key_f5kf5k5
                                                                                                                                                                                                                                                                                                                                                                    F5 function key

                                                                                                                                                                                                                                                                                                                                                                        key_f50kf50Fe
                                                                                                                                                                                                                                                                                                                                                                            F50 function key

                                                                                                                                                                                                                                                                                                                                                                                key_f51kf51Ff
                                                                                                                                                                                                                                                                                                                                                                                    F51 function key

                                                                                                                                                                                                                                                                                                                                                                                        key_f52kf52Fg
                                                                                                                                                                                                                                                                                                                                                                                            F52 function key

                                                                                                                                                                                                                                                                                                                                                                                                key_f53kf53Fh
                                                                                                                                                                                                                                                                                                                                                                                                    F53 function key

                                                                                                                                                                                                                                                                                                                                                                                                        key_f54kf54Fi
                                                                                                                                                                                                                                                                                                                                                                                                            F54 function key

                                                                                                                                                                                                                                                                                                                                                                                                                key_f55kf55Fj
                                                                                                                                                                                                                                                                                                                                                                                                                    F55 function key

                                                                                                                                                                                                                                                                                                                                                                                                                        key_f56kf56Fk
                                                                                                                                                                                                                                                                                                                                                                                                                            F56 function key

                                                                                                                                                                                                                                                                                                                                                                                                                                key_f57kf57Fl
                                                                                                                                                                                                                                                                                                                                                                                                                                    F57 function key

                                                                                                                                                                                                                                                                                                                                                                                                                                        key_f58kf58Fm
                                                                                                                                                                                                                                                                                                                                                                                                                                            F58 function key

                                                                                                                                                                                                                                                                                                                                                                                                                                                key_f59kf59Fn
                                                                                                                                                                                                                                                                                                                                                                                                                                                    F59 function key

                                                                                                                                                                                                                                                                                                                                                                                                                                                        key_f6kf6k6
                                                                                                                                                                                                                                                                                                                                                                                                                                                            F6 function key

                                                                                                                                                                                                                                                                                                                                                                                                                                                                key_f60kf60Fo
                                                                                                                                                                                                                                                                                                                                                                                                                                                                    F60 function key

                                                                                                                                                                                                                                                                                                                                                                                                                                                                        key_f61kf61Fp
                                                                                                                                                                                                                                                                                                                                                                                                                                                                            F61 function key

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                key_f62kf62Fq
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    F62 function key

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        key_f63kf63Fr
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            F63 function key

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                key_f7kf7k7
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    F7 function key

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        key_f8kf8k8
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            F8 function key

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                key_f9kf9k9
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    F9 function key

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        key_findkfnd @0 find key

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            key_helpkhlp %
            1 help key

                key_homekhomekh
                    home key

                        key_ickich1kI
                            insert -
        character key

            key_ilkil1kA
                insert -
        line key

            key_leftkcub1kl
                left -
        arrow key

            key_llkllkH
                lower -
        left key(home down)

                key_markkmrk
            % 2 mark key

            key_messagekmsg
            % 3 message key

            key_movekmov
            % 4 move key

            key_nextknxt
            % 5 next key

            key_npageknpkN next
        - page key

              key_openkopn
              % 6 open key

              key_optionskopt
              % 7 options key

              key_ppagekppkP previous
        - page key

              key_previouskprv
              % 8 previous key

              key_printkprt
              % 9 print key

              key_redokrdo
              % 0 redo key

              key_referencekref
    &amp; 1 reference key

    key_refreshkrfr
    &amp; 2 refresh key

    key_replacekrpl
    &amp; 3 replace key

    key_restartkrst
    &amp; 4 restart key

    key_resumekres
    &amp; 5 resume key

          key_rightkcuf1kr right
          - arrow key

          key_saveksav
    &amp; 6 save key

    key_sbegkBEG
    &amp; 9 shifted begin key

    key_scancelkCAN
    &amp; 0 shifted cancel key

              key_scommandkCMD
              * 1 shifted command key

              key_scopykCPY
              * 2 shifted copy key

              key_screatekCRT
              * 3 shifted create key

              key_sdckDC
              * 4 shifted delete -
          character key

              key_sdlkDL
              * 5 shifted delete -
          line key

              key_selectkslt
              * 6 select key

              key_sendkEND
              * 7 shifted end key

              key_seolkEOL
              * 8 shifted clear
          - to - end - of - line key

                                key_sexitkEXT
                                * 9 shifted exit key

                                key_sfkindkF scroll
          - forward key

                key_sfindkFND
                * 0 shifted find key

                key_shelpkHLP #1 shifted help key

                key_shomekHOM #2 shifted home key

                key_sickIC #3 shifted insert
          - character key

          key_sleftkLFT #4 shifted left
          - arrow key

                key_smessagekMSG
                % a shifted message key

                key_smovekMOV
                % b shifted move key

                key_snextkNXT
                % c shifted next key

                key_soptionskOPT
                % d shifted options key

                key_spreviouskPRV
                % e shifted previous key

                key_sprintkPRT
                % f shifted print key

                key_srkrikR scroll
          - backward key

                key_sredokRDO
                % g shifted redo key

                key_sreplacekRPL
                % h shifted replace key

                key_srightkRIT
                % i shifted right
          - arrow key

                key_srsumekRES
                % j shifted resume key

                key_ssavekSAV !1 shifted save key

                key_ssuspendkSPD !2 shifted suspend key

                key_stabkhtskT set
          - tab key

          key_sundokUND !3 shifted undo key

          key_suspendkspd
    &amp; 7 suspend key

    key_undokund
    &amp; 8 undo key

          key_upkcuu1ku up
          - arrow key

          keypad_localrmkxke leave 'keyboard_transmit' mode

          keypad_xmitsmkxks enter 'keyboard_transmit' mode

          lab_f0lf0l0 label on function key f0 if not f0

          lab_f1lf1l1 label on function key f1 if not f1

          lab_f10lf10la label on function key f10 if not f10

          lab_f2lf2l2 label on function key f2 if not f2

          lab_f3lf3l3 label on function key f3 if not f3

          lab_f4lf4l4 label on function key f4 if not f4

          lab_f5lf5l5 label on function key f5 if not f5

          lab_f6lf6l6 label on function key f6 if not f6

          lab_f7lf7l7 label on function key f7 if not f7

          lab_f8lf8l8 label on function key f8 if not f8

          lab_f9lf9l9 label on function key f9 if not f9

          label_formatflnLf label format

          label_offrmlnLF turn off soft labels

          label_onsmlnLO turn on soft labels

          meta_offrmmmo turn off meta mode

          meta_onsmmmm turn on meta mode(8th - bit on)

              micro_column_addressmhpaZY Like column_address in micro mode

          micro_downmcud1ZZ Like cursor_down in micro mode

          micro_leftmcub1Za Like cursor_left in micro mode

          micro_rightmcuf1Zb Like cursor_right in micro mode

          micro_row_addressmvpaZc Like row_address #1 in micro mode

          micro_upmcuu1Zd Like cursor_up in micro mode

          newlinenelnw newline(behave like cr followed by lf)

              order_of_pinsporderZe Match software bits to print
          - head pins

          orig_colorsococ Set all color pairs to the original ones

          orig_pairopop Set default pair to its original value

          pad_charpadpc padding char(instead of null)

              parm_dchdchDC delete #1 characters(P *)

                  parm_delete_linedlDL delete #1 lines(P *)

                      parm_down_cursorcudDO down #1 lines(P *)

                          parm_down_micromcudZf Like parm_down_cursor in micro mode

          parm_ichichIC insert #1 characters(P *)

              parm_indexindnSF scroll forward #1 lines(P)

                  parm_insert_lineilAL insert #1 lines(P *)

                      parm_left_cursorcubLE move #1 characters to the left(P)

parm_left_micromcubZg
Like parm_left_cursor in micro mode


parm_right_cursorcufRI
move #1 characters to the right (P*)


parm_right_micromcufZh
Like parm_right_cursor in micro mode


parm_rindexrinSR
scroll back #1 lines (P)


parm_up_cursorcuuUP
up #1 lines (P*)


parm_up_micromcuuZi
Like parm_up_cursor in micro mode


pkey_keypfkeypk
program function key #1 to type string #2


pkey_localpflocpl
program function key #1 to execute string #2


pkey_xmitpfxpx
program function key #1 to transmit string #2


plab_normplnpn
program label #1 to show string #2


print_screenmc0ps
print contents of screen


prtr_nonmc5ppO
turn on printer for #1 bytes


prtr_offmc4pf
turn off printer


prtr_onmc5po
turn on printer


pulsepulsePU
select pulse dialing


quick_dialqdialQD
dial number #1 without checking


remove_clockrmclkRC
remove clock


repeat_charreprp
repeat char #1 #2 times (P*)


req_for_inputrfiRF
send next input char (for ptys)


reset_1stringrs1r1
reset string


reset_2stringrs2r2
reset string


reset_3stringrs3r3
reset string


reset_filerfrf
name of reset file


restore_cursorrcrc
restore cursor to position of last save_cursor


row_addressvpacv
vertical position #1 absolute (P)


save_cursorscsc
save current cursor position (P)

scroll_forwardindsf
    scroll text
    up(P)

scroll_reverserisr
    scroll text
    down(P)

select_char_setscsZj
    Select character set,
    #1

            set_attributessgrsa
                define video attributes #1 -
            #9(PG9)

                set_backgroundsetbSb
            Set background color #1

            set_bottom_marginsmgbZk
            Set bottom margin at current line

            set_bottom_margin_parmsmgbpZl
            Set bottom margin at line #1 or
        (if smgtp is not given) #2 lines from bottom

        set_clocksclkSC
        set clock,
    #1 hrs #2 mins #3 secs

    set_color_pairscpsp
    Set current color pair to #1

    set_foregroundsetfSf
    Set foreground color #1

    set_left_marginsmglML
    set left soft margin at current column.(ML is not in BSD termcap)
        .

    set_left_margin_parmsmglpZm
    Set left(right)
margin at column #1

    set_right_marginsmgrMR
        set right soft margin at current column

            set_right_margin_parmsmgrpZn
                Set right margin at column #1

    set_tabhtsst
        set a tab in every row,
    current columns

        set_top_marginsmgtZo
            Set top margin at current line

                set_top_margin_parmsmgtpZp
                    Set
                    top(bottom) margin at row #1


set_windowwindwi
current window is lines #1-#2 cols #3-#4


start_bit_imagesbimZq
Start printing bit image graphics


start_char_set_defscsdZr
Start character set definition #1, with #2 characters in the set


stop_bit_imagerbimZs
Stop printing bit image graphics


stop_char_set_defrcsdZt
End definition of character set #1


subscript_characterssubcsZu
List of subscriptable characters


superscript_characterssupcsZv
List of superscriptable characters


tabhtta
tab to next 8-space hardware tab stop


these_cause_crdocrZw
Printing any of these characters causes CR


to_status_linetslts
move to status line, column #1


tonetoneTO
select touch tone dialing


underline_charucuc
underline char and move past it


up_half_linehuhu
half a line up


user0u0u0
User string #0


user1u1u1
User string #1


user2u2u2
User string #2


user3u3u3
User string #3


user4u4u4
User string #4


user5u5u5
User string #5


user6u6u6
User string #6


user7u7u7
User string #7


user8u8u8
User string #8


user9u9u9
User string #9


wait_tonewaitWA
wait for dial-tone


xoff_characterxoffcXF
XOFF character


xon_characterxoncXN
XON character


zero_motionzeromZx
No motion for subsequent character</code></pre>
<p> The following string capabilities are present in the SVr4.0 term structure, but were originally not documented in the man page. </font><center></p>
<table>
<tr VALIGN=top>
<td ALIGN=center><code>Variable</code></td>
<td>Cap-</td>
<td>TCap</td>
<td ALIGN=center>Description
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center><code>String</code></td>
<td>name</td>
<td>Code</td>
<td ALIGN=center>
</td>
</tr>
<tr VALIGN=top>
<td>alt_scancode_esc</td>
<td>scesa</td>
<td>S8</td>
<td> Alternate escape for scancode emulation
</td>
</tr>
<tr VALIGN=top>
<td>bit_image_carriage_return</td>
<td>bicr</td>
<td>Yv</td>
<td> Move to beginning of same row
</td>
</tr>
<tr VALIGN=top>
<td>bit_image_newline</td>
<td>binel</td>
<td>Zz</td>
<td> Move to next row of the bit image
</td>
</tr>
<tr VALIGN=top>
<td>bit_image_repeat</td>
<td>birep</td>
<td>Xy</td>
<td> Repeat bit image cell #1 #2 times
</td>
</tr>
<tr VALIGN=top>
<td>char_set_names</td>
<td>csnm</td>
<td>Zy</td>
<td> Produce #1&#8217;th item from list of character set names
</td>
</tr>
<tr VALIGN=top>
<td>code_set_init</td>
<td>csin</td>
<td>ci</td>
<td> Init sequence for multiple codesets
</td>
</tr>
<tr VALIGN=top>
<td>color_names</td>
<td>colornm</td>
<td>Yw</td>
<td> Give name for color #1
</td>
</tr>
<tr VALIGN=top>
<td>define_bit_image_region</td>
<td>defbi</td>
<td>Yx</td>
<td> Define rectangular bit image region
</td>
</tr>
<tr VALIGN=top>
<td>device_type</td>
<td>devt</td>
<td>dv</td>
<td> Indicate language/codeset support
</td>
</tr>
<tr VALIGN=top>
<td>display_pc_char</td>
<td>dispc</td>
<td>S1</td>
<td> Display PC character #1
</td>
</tr>
<tr VALIGN=top>
<td>end_bit_image_region</td>
<td>endbi</td>
<td>Yy</td>
<td> End a bit-image region
</td>
</tr>
<tr VALIGN=top>
<td>enter_pc_charset_mode</td>
<td>smpch</td>
<td>S2</td>
<td> Enter PC character display mode
</td>
</tr>
<tr VALIGN=top>
<td>enter_scancode_mode</td>
<td>smsc</td>
<td>S4</td>
<td> Enter PC scancode mode
</td>
</tr>
<tr VALIGN=top>
<td>exit_pc_charset_mode</td>
<td>rmpch</td>
<td>S3</td>
<td> Exit PC character display mode
</td>
</tr>
<tr VALIGN=top>
<td>exit_scancode_mode</td>
<td>rmsc</td>
<td>S5</td>
<td> Exit PC scancode mode
</td>
</tr>
<tr VALIGN=top>
<td>get_mouse</td>
<td>getm</td>
<td>Gm</td>
<td> Curses should get button events, parameter #1 not documented.
</td>
</tr>
<tr VALIGN=top>
<td>key_mouse</td>
<td>kmous</td>
<td>Km</td>
<td> Mouse event has occurred
</td>
</tr>
<tr VALIGN=top>
<td>mouse_info</td>
<td>minfo</td>
<td>Mi</td>
<td> Mouse status information
</td>
</tr>
<tr VALIGN=top>
<td>pc_term_options</td>
<td>pctrm</td>
<td>S6</td>
<td> PC terminal options
</td>
</tr>
<tr VALIGN=top>
<td>pkey_plab</td>
<td>pfxl</td>
<td>xl</td>
<td> Program function key #1 to type string #2 and show string #3
</td>
</tr>
<tr VALIGN=top>
<td>req_mouse_pos</td>
<td>reqmp</td>
<td>RQ</td>
<td> Request mouse position
</td>
</tr>
<tr VALIGN=top>
<td>scancode_escape</td>
<td>scesc</td>
<td>S7</td>
<td> Escape for scancode emulation
</td>
</tr>
<tr VALIGN=top>
<td>set0_des_seq</td>
<td>s0ds</td>
<td>s0</td>
<td> Shift to codeset 0 (EUC set 0, ASCII)
</td>
</tr>
<tr VALIGN=top>
<td>set1_des_seq</td>
<td>s1ds</td>
<td>s1</td>
<td> Shift to codeset 1
</td>
</tr>
<tr VALIGN=top>
<td>set2_des_seq</td>
<td>s2ds</td>
<td>s2</td>
<td> Shift to codeset 2
</td>
</tr>
<tr VALIGN=top>
<td>set3_des_seq</td>
<td>s3ds</td>
<td>s3</td>
<td> Shift to codeset 3
</td>
</tr>
<tr VALIGN=top>
<td>set_a_background</td>
<td>setab</td>
<td>AB</td>
<td> Set background color to #1, using ANSI escape
</td>
</tr>
<tr VALIGN=top>
<td>set_a_foreground</td>
<td>setaf</td>
<td>AF</td>
<td> Set foreground color to #1, using ANSI escape
</td>
</tr>
<tr VALIGN=top>
<td>set_color_band</td>
<td>setcolor</td>
<td>Yz</td>
<td> Change to ribbon color #1
</td>
</tr>
<tr VALIGN=top>
<td>set_lr_margin</td>
<td>smglr</td>
<td>ML</td>
<td> Set both left and right margins to #1, #2. (ML is not in BSD termcap).
</td>
</tr>
<tr VALIGN=top>
<td>set_page_length</td>
<td>slines</td>
<td>YZ</td>
<td> Set page length to #1 lines
</td>
</tr>
<tr VALIGN=top>
<td>set_tb_margin</td>
<td>smgtb</td>
<td>MT</td>
<td> Sets both top and bottom margins to #1, #2
</td>
</tr>
</table>
<p></center> <font SIZE="-1"> The XSI Curses standard added these hardcopy capabilities. They were used in some post-4.1 versions of System V curses, e.g., Solaris 2.5 and IRIX 6.x. Except for <code>YI</code>, the <code>ncurses</code> termcap names for them are invented. According to the XSI Curses standard, they have no termcap names. If your compiled terminfo entries use these, they may not be binary-compatible with System V terminfo entries after SVr4.1; beware! </font><center></p>
<table>
<tr VALIGN=top>
<td ALIGN=center><code>Variable</code></td>
<td>Cap-</td>
<td>TCap</td>
<td ALIGN=center>Description
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center><code>String</code></td>
<td>name</td>
<td>Code</td>
<td ALIGN=center>
</td>
</tr>
<tr VALIGN=top>
<td>enter_horizontal_hl_mode</td>
<td>ehhlm</td>
<td>Xh</td>
<td> Enter horizontal highlight mode
</td>
</tr>
<tr VALIGN=top>
<td>enter_left_hl_mode</td>
<td>elhlm</td>
<td>Xl</td>
<td> Enter left highlight mode
</td>
</tr>
<tr VALIGN=top>
<td>enter_low_hl_mode</td>
<td>elohlm</td>
<td>Xo</td>
<td> Enter low highlight mode
</td>
</tr>
<tr VALIGN=top>
<td>enter_right_hl_mode</td>
<td>erhlm</td>
<td>Xr</td>
<td> Enter right highlight mode
</td>
</tr>
<tr VALIGN=top>
<td>enter_top_hl_mode</td>
<td>ethlm</td>
<td>Xt</td>
<td> Enter top highlight mode
</td>
</tr>
<tr VALIGN=top>
<td>enter_vertical_hl_mode</td>
<td>evhlm</td>
<td>Xv</td>
<td> Enter vertical highlight mode
</td>
</tr>
<tr VALIGN=top>
<td>set_a_attributes</td>
<td>sgr1</td>
<td>sA</td>
<td> Define second set of video attributes #1-#6
</td>
</tr>
<tr VALIGN=top>
<td>set_pglen_inch</td>
<td>slength</td>
<td>YI</td>
<td> Set page length to #1 hundredth of an inch (some implementations use sL for termcap).
</td>
</tr>
</table>
<p></center> <font SIZE="-1"> </font></p>
<h3>User-Defined Capabilities</h3>
<p>The preceding section listed the <i>predefined</i> capabilities. They deal with some special features for terminals no longer (or possibly never) produced. Occasionally there are special features of newer terminals which are awkward or impossible to represent by reusing the predefined capabilities. <code>ncurses</code> addresses this limitation by allowing user-defined capabilities. The <code>tic</code> and <code>infocmp</code> programs provide the <code>-x</code> option for this purpose. When <code>-x</code> is set, <code>tic</code> treats unknown capabilities as user-defined. That is, if <code>tic</code> encounters a capability name which it does not recognize, it infers its type (boolean, number or string) from the syntax and makes an extended table entry for that capability. The <code><a href="//www.systutorials.com/docs/linux/man/3X-use_extended_names/">use_extended_names</a></code>(3X) function makes this information conditionally available to applications. The ncurses library provides the data leaving most of the behavior to applications:<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 User-defined capability strings whose name begins with &#8220;k&#8221; are treated as function keys.<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 The types (boolean, number, string) determined by <code>tic</code> can be inferred by successful calls on <code>tigetflag</code>, etc.<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 If the capability name happens to be two characters, the capability is also available through the termcap interface. While termcap is said to be extensible because it does not use a predefined set of capabilities, in practice it has been limited to the capabilities defined by terminfo implementations. As a rule, user-defined capabilities intended for use by termcap applications should be limited to booleans and numbers to avoid running past the 1023 byte limit assumed by termcap implementations and their applications. In particular, providing extended sets of function keys (past the 60 numbered keys and the handful of special named keys) is best done using the longer names available using terminfo.</p>
<h3>A Sample Entry</h3>
<p>The following entry, describing an ANSI-standard terminal, is representative of what a <code>terminfo</code> entry for a modern terminal typically looks like. </p>
<pre><FONT SIZE="-2">ansi|ansi/pc-term compatible with color,
 am, mc5i, mir, msgr,
 colors#8, cols#80, it#8, lines#24, ncv#3, pairs#64,
 acsc=+\,-.^Y0\333`a\261f\370g\361h\260
 j\331k\277l\332m\300n\305o~p\304q\304r\304s_t\303
 u\264v\301w\302x\263y\363z\362{\343|\330}\234~\376,
 bel=^G, blink=\E[5m, bold=\E[1m, cbt=\E[Z, clear=\E[H\E[J,
 cr=^M, cub=\E[%p1%dD, cub1=\E[D, cud=\E[%p1%dB, cud1=\E[B,
 cuf=\E[%p1%dC, cuf1=\E[C, cup=\E[%i%p1%d;%p2%dH,
 cuu=\E[%p1%dA, cuu1=\E[A, dch=\E[%p1%dP, dch1=\E[P,
 dl=\E[%p1%dM, dl1=\E[M, ech=\E[%p1%dX, ed=\E[J, el=\E[K,
 el1=\E[1K, home=\E[H, hpa=\E[%i%p1%dG, ht=\E[I, hts=\EH,
 ich=\E[%p1%d@, il=\E[%p1%dL, il1=\E[L, ind=^J,
 indn=\E[%p1%dS, invis=\E[8m, kbs=^H, kcbt=\E[Z, kcub1=\E[D,
 kcud1=\E[B, kcuf1=\E[C, kcuu1=\E[A, khome=\E[H, kich1=\E[L,
 mc4=\E[4i, mc5=\E[5i, nel=\E[S, op=\E[39;49m,
 rep=%p1%c\E[%p2%{1}%-%db, rev=\E[7m, rin=\E[%p1%dT,
 rmacs=\E[10m, rmpch=\E[10m, rmso=\E[m, rmul=\E[m,
 s0ds=\E(B, s1ds=\E)B, s2ds=\E*B, s3ds=\E+B,
 setab=\E[4%p1%dm, setaf=\E[3%p1%dm,
 sgr=\E[0;10%?%p1%t;7%;
 %?%p2%t;4%;
 %?%p3%t;7%;
 %?%p4%t;5%;
 %?%p6%t;1%;
 %?%p7%t;8%;
 %?%p9%t;11%;m,
 sgr0=\E[0;10m, smacs=\E[11m, smpch=\E[11m, smso=\E[7m,
 smul=\E[4m, tbc=\E[3g, u6=\E[%i%d;%dR, u7=\E[6n,
 u8=\E[?%[;0123456789]c, u9=\E[c, vpa=\E[%i%p1%dd,
</FONT></pre>
<p>Entries may continue onto multiple lines by placing white space at the beginning of each line except the first. Comments may be included on lines beginning with &#8220;#&#8221;. Capabilities in <i>terminfo</i> are of three types:<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 Boolean capabilities which indicate that the terminal has some particular feature,<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 numeric capabilities giving the size of the terminal or the size of particular delays, and<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 string capabilities, which give a sequence which can be used to perform particular terminal operations.</p>
<h3>Types of Capabilities</h3>
<p>All capabilities have names. For instance, the fact that ANSI-standard terminals have <i>automatic margins</i> (i.e., an automatic return and line-feed when the end of a line is reached) is indicated by the capability <code>am</code>. Hence the description of ansi includes <code>am</code>. Numeric capabilities are followed by the character &#8220;#&#8221; and then a positive value. Thus <code>cols</code>, which indicates the number of columns the terminal has, gives the value &#8220;80&#8221; for ansi. Values for numeric capabilities may be specified in decimal, octal or hexadecimal, using the C programming language conventions (e.g., 255, 0377 and 0xff or 0xFF). Finally, string valued capabilities, such as <code>el</code> (clear to end of line sequence) are given by the two-character code, an &#8220;=&#8221;, and then a string ending at the next following &#8220;,&#8221;. A number of escape sequences are provided in the string valued capabilities for easy encoding of characters there:<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 Both <code>\E</code> and <code></code> map to an <font SIZE="-1">ESCAPE</font> character,<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 <code>^x</code> maps to a control-x for any appropriate <i>x</i>, and<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 the sequences</p>
<dl>
<dd><code>
</code>, <code>\l</code>, <code></code>, <code>	</code>, <code></code>, <code></code>, and <code>\s</code></dl>
<dl>
<dd>produce</p>
<dl>
<dd><i>newline</i>, <i>line-feed</i>, <i>return</i>, <i>tab</i>, <i>backspace</i>, <i>form-feed</i>, and <i>space</i>,</dl>
<dd>respectively.</dl>
<p> X/Open Curses does not say what &#8220;appropriate <i>x</i>&#8221; might be. In practice, that is a printable ASCII graphic character. The special case &#8220;^?&#8221; is interpreted as DEL (127). In all other cases, the character value is AND&#8217;d with 0x1f, mapping to ASCII control codes in the range 0 through 31. Other escapes include<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 <code>\^</code> for <code>^</code>,<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 <code>\</code> for <code>\</code>,<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 <code>\</code>, for comma,<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 <code>\:</code> for <code>:</code>,<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 and <code>
