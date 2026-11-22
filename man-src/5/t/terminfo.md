---

title: "terminfo(5)"
name: "terminfo"
section: "5"
letter: "t"
url: "/docs/linux/man/5-terminfo/"
description: "terminfo – terminal capability database"
---

<p>terminfo &#8211; terminal capability database </p>

<p> /etc/terminfo/*/*  </p>
<h2>DESCRIPTION</h2>
<p> <i>Terminfo</i> is a database describing terminals, used by screen-oriented programs such as <code>nvi</code>(1), <code><a href="/docs/linux/man/1-lynx/">lynx</a></code>(1), <code><a href="/docs/linux/man/1-mutt/">mutt</a></code>(1), and other curses applications, using high-level calls to libraries such as <code>ncurses</code>(3NCURSES). It is also used via low-level calls by non-curses applications which may be screen-oriented (such as <code><a href="/docs/linux/man/1-clear/">clear</a></code>(1)) or non-screen (such as <code><a href="/docs/linux/man/1-tabs/">tabs</a></code>(1)). </p>
<p> <i>Terminfo</i> describes terminals by giving a set of capabilities which they have, by specifying how to perform screen operations, and by specifying padding requirements and initialization sequences. </p>
<p>This manual describes <code>ncurses</code> version 6.3 (patch 20211021).  </p>
<h3>Terminfo Entry Syntax</h3>
<p>Entries in <i>terminfo</i> consist of a sequence of fields: <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 Each field ends with a comma ``,&#8216;&#8216; (embedded commas may be escaped with a backslash or written as ``\054&#8217;&#8216;). <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 White space between fields is ignored. <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 The first field in a <i>terminfo</i> entry begins in the first column. <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 Newlines and leading whitespace (spaces or tabs) may be used for formatting entries for readability. These are removed from parsed entries. </p>
<dl>
<dd> <p> The <code>infocmp</code> <code>-f</code> and <code>-W</code> options rely on this to format if-then-else expressions, or to enforce maximum line-width. The resulting formatted terminal description can be read by <code>tic</code>. <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 The first field for each terminal gives the names which are known for the terminal, separated by ``|&#8216;&#8216; characters. </p>
 </dd>
<dd> <p> The first name given is the most common abbreviation for the terminal (its primary name), the last name given should be a long name fully identifying the terminal (see <code>longname</code>(3X)), and all others are treated as synonyms (aliases) for the primary terminal name. </p>
 </dd>
<dd> <p> X/Open Curses advises that all names but the last should be in lower case and contain no blanks; the last name may well contain upper case and blanks for readability. </p>
 </dd>
<dd> <p> This implementation is not so strict; it allows mixed case in the primary name and aliases. If the last name has no embedded blanks, it allows that to be both an alias and a verbose name (but will warn about this ambiguity). <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 Lines beginning with a ``#&#8216;&#8216; in the first column are treated as comments. </p>
 </dd>
<dd> <p> While comment lines are legal at any point, the output of <code>captoinfo</code> and <code>infotocap</code> (aliases for <code>tic</code>) will move comments so they occur only between entries. </p>
 </dd></dl>
<p>Terminal names (except for the last, verbose entry) should be chosen using the following conventions. The particular piece of hardware making up the terminal should have a root name, thus ``hp2621&#8217;&#8216;. This name should not contain hyphens. Modes that the hardware can be in, or user preferences, should be indicated by appending a hyphen and a mode suffix. Thus, a vt100 in 132-column mode would be vt100-w. The following suffixes should be used where possible: </p>
<p> <center> </p>
<table>
<tr VALIGN=top>
<td><code>Suffix</code></td>
<td>Meaning</td>
<td>Example
</td>
</tr>
<tr VALIGN=top>
<td>-<i>nn</i></td>
<td>Number of lines on the screen</td>
<td>aaa-60
</td>
</tr>
<tr VALIGN=top>
<td>-<i>n</i>p</td>
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
<p> </center> </p>
<p>For more on terminal naming conventions, see the <code><a href="/docs/linux/man/7-term/">term</a></code>(7) manual page.  </p>
<h3>Terminfo Capabilities Syntax</h3>
<p>The terminfo entry consists of several <i>capabilities</i>, i.e., features that the terminal has, or methods for exercising the terminal&#8217;s features. </p>
<p>After the first field (giving the name(s) of the terminal entry), there should be one or more <i>capability</i> fields. These are boolean, numeric or string names with corresponding values: <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 Boolean capabilities are true when present, false when absent. There is no explicit value for boolean capabilities. <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 Numeric capabilities have a ``#&#8216;&#8216; following the name, then an unsigned decimal integer value. <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 String capabilities have a ``=&#8216;&#8216; following the name, then an string of characters making up the capability value. </p>
<dl>
<dd> <p> String capabilities can be split into multiple lines, just as the fields comprising a terminal entry can be split into multiple lines. While blanks between fields are ignored, blanks embedded within a string value are retained, except for leading blanks on a line. </p>
 </dd></dl>
<p>Any capability can be <i>canceled</i>, i.e., suppressed from the terminal entry, by following its name with ``@&#8216;&#8216; rather than a capability value.  </p>
<h3>Similar Terminals</h3>
<p>If there are two very similar terminals, one (the variant) can be defined as being just like the other (the base) with certain exceptions. In the definition of the variant, the string capability <code>use</code> can be given with the name of the base terminal: <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 The capabilities given before <code>use</code> override those in the base type named by <code>use</code>. <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 If there are multiple <code>use</code> capabilities, they are merged in reverse order. That is, the rightmost <code>use</code> reference is processed first, then the one to its left, and so forth. <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 Capabilities given explicitly in the entry override those brought in by <code>use</code> references. </p>
<p>A capability can be canceled by placing <code>xx@</code> to the left of the use reference that imports it, where <i>xx</i> is the capability. For example, the entry </p>
<dl>
<dd> <p>2621-nl, smkx@, rmkx@, use=2621, </p>
 </dd></dl>
<p>defines a 2621-nl that does not have the <code>smkx</code> or <code>rmkx</code> capabilities, and hence does not turn on the function key labels when in visual mode. This is useful for different modes for a terminal, or for different user preferences. </p>
<p>An entry included via <code>use</code> can contain canceled capabilities, which have the same effect as if those cancels were inline in the using terminal entry.  </p>
<h3>Predefined Capabilities</h3>
<p>  The following is a complete table of the capabilities included in a terminfo description block and available to terminfo-using code. In each line of the table, </p>
<p>The <code>variable</code> is the name by which the programmer (at the terminfo level) accesses the capability. </p>
<p>The <code>capname</code> is the short name used in the text of the database, and is used by a person updating the database. Whenever possible, capnames are chosen to be the same as or similar to the ANSI X3.64-1979 standard (now superseded by ECMA-48, which uses identical or very similar names). Semantics are also intended to match those of the specification. </p>
<p>The termcap code is the old <code>termcap</code> capability name (some capabilities are new, and have names which termcap did not originate). </p>
<p>Capability names have no hard length limit, but an informal limit of 5 characters has been adopted to keep them short and to allow the tabs in the source file <code>Caps</code> to line up nicely. </p>
<p>Finally, the description field attempts to convey the semantics of the capability. You may find some codes in the description field: </p>
<dl>
<dt>(P)</dt>
<dd> <p> indicates that padding may be specified </p>
 </dd>
<dt>#[1-9]</dt>
<dd> <p> in the description field indicates that the string is passed through <code>tparm</code>(3X) with parameters as given (#<i>i</i>). </p>
 </dd>
<dd> <p> If no parameters are listed in the description, passing the string through <code>tparm</code>(3X) may give unexpected results, e.g., if it contains percent (%%) signs. </p>
 </dd>
<dt>(P*)</dt>
<dd> <p> indicates that padding may vary in proportion to the number of lines affected </p>
 </dd>
<dt>(#<i>i</i>)</dt>
<dd> <p> indicates the <i>i</i>th parameter. </p>
 </dd></dl>
<p>These are the boolean capabilities: </p>
<p> <center> </p>
<table>
<tr VALIGN=top>
<td><code>Variable</code></td>
<td>Cap-</td>
<td>TCap</td>
<td>Description
</td>
</tr>
<tr VALIGN=top>
<td><code>Booleans</code></td>
<td>name</td>
<td>Code</td>
<td>
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
<td> cannot print ~&#8216;s (Hazeltine) 
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
<p> </center>  </p>
<p>These are the numeric capabilities: </p>
<p> <center> </p>
<table>
<tr VALIGN=top>
<td><code>Variable</code></td>
<td>Cap-</td>
<td>TCap</td>
<td>Description
</td>
</tr>
<tr VALIGN=top>
<td><code>Numeric</code></td>
<td>name</td>
<td>Code</td>
<td>
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
<p> </center>  </p>
<p>The following numeric capabilities are present in the SVr4.0 term structure, but are not yet documented in the man page. They came in with SVr4&#8217;s printer support. </p>
<p> <center> </p>
<table>
<tr VALIGN=top>
<td><code>Variable</code></td>
<td>Cap-</td>
<td>TCap</td>
<td>Description
</td>
</tr>
<tr VALIGN=top>
<td><code>Numeric</code></td>
<td>name</td>
<td>Code</td>
<td>
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
<td> maximum value in micro_..._address 
</td>
</tr>
<tr VALIGN=top>
<td>max_micro_jump</td>
<td>mjump</td>
<td>Ye</td>
<td> maximum value in parm_..._micro 
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
<p> </center>  </p>
<p>These are the string capabilities: </p>
<p> <center> </p>
<table>
<tr VALIGN=top>
<td><code>Variable</code></td>
<td>Cap-</td>
<td>TCap</td>
<td>Description
</td>
</tr>
<tr VALIGN=top>
<td><code>String</code></td>
<td>name</td>
<td>Code</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>acs_chars</td>
<td>acsc</td>
<td>ac</td>
<td> graphics charset pairs, based on vt100 
</td>
</tr>
<tr VALIGN=top>
<td>back_tab</td>
<td>cbt</td>
<td>bt</td>
<td> back tab (P) 
</td>
</tr>
<tr VALIGN=top>
<td>bell</td>
<td>bel</td>
<td>bl</td>
<td> audible signal (bell) (P) 
</td>
</tr>
<tr VALIGN=top>
<td>carriage_return</td>
<td>cr</td>
<td>cr</td>
<td> carriage return (P*) (P*) 
</td>
</tr>
<tr VALIGN=top>
<td>change_char_pitch</td>
<td>cpi</td>
<td>ZA</td>
<td> Change number of characters per inch to #1 
</td>
</tr>
<tr VALIGN=top>
<td>change_line_pitch</td>
<td>lpi</td>
<td>ZB</td>
<td> Change number of lines per inch to #1 
</td>
</tr>
<tr VALIGN=top>
<td>change_res_horz</td>
<td>chr</td>
<td>ZC</td>
<td> Change horizontal resolution to #1 
</td>
</tr>
<tr VALIGN=top>
<td>change_res_vert</td>
<td>cvr</td>
<td>ZD</td>
<td> Change vertical resolution to #1 
</td>
</tr>
<tr VALIGN=top>
<td>change_scroll_region</td>
<td>csr</td>
<td>cs</td>
<td> change region to line #1 to line #2 (P) 
</td>
</tr>
<tr VALIGN=top>
<td>char_padding</td>
<td>rmp</td>
<td>rP</td>
<td> like ip but when in insert mode 
</td>
</tr>
<tr VALIGN=top>
<td>clear_all_tabs</td>
<td>tbc</td>
<td>ct</td>
<td> clear all tab stops (P) 
</td>
</tr>
<tr VALIGN=top>
<td>clear_margins</td>
<td>mgc</td>
<td>MC</td>
<td> clear right and left soft margins 
</td>
</tr>
<tr VALIGN=top>
<td>clear_screen</td>
<td>clear</td>
<td>cl</td>
<td> clear screen and home cursor (P*) 
</td>
</tr>
<tr VALIGN=top>
<td>clr_bol</td>
<td>el1</td>
<td>cb</td>
<td> Clear to beginning of line 
</td>
</tr>
<tr VALIGN=top>
<td>clr_eol</td>
<td>el</td>
<td>ce</td>
<td> clear to end of line (P) 
</td>
</tr>
<tr VALIGN=top>
<td>clr_eos</td>
<td>ed</td>
<td>cd</td>
<td> clear to end of screen (P*) 
</td>
</tr>
<tr VALIGN=top>
<td>column_address</td>
<td>hpa</td>
<td>ch</td>
<td> horizontal position #1, absolute (P) 
</td>
</tr>
<tr VALIGN=top>
<td>command_character</td>
<td>cmdch</td>
<td>CC</td>
<td> terminal settable cmd character in prototype !? 
</td>
</tr>
<tr VALIGN=top>
<td>create_window</td>
<td>cwin</td>
<td>CW</td>
<td> define a window #1 from #2,#3 to #4,#5 
</td>
</tr>
<tr VALIGN=top>
<td>cursor_address</td>
<td>cup</td>
<td>cm</td>
<td> move to row #1 columns #2 
</td>
</tr>
<tr VALIGN=top>
<td>cursor_down</td>
<td>cud1</td>
<td>do</td>
<td> down one line 
</td>
</tr>
<tr VALIGN=top>
<td>cursor_home</td>
<td>home</td>
<td>ho</td>
<td> home cursor (if no cup) 
</td>
</tr>
<tr VALIGN=top>
<td>cursor_invisible</td>
<td>civis</td>
<td>vi</td>
<td> make cursor invisible 
</td>
</tr>
<tr VALIGN=top>
<td>cursor_left</td>
<td>cub1</td>
<td>le</td>
<td> move left one space 
</td>
</tr>
<tr VALIGN=top>
<td>cursor_mem_address</td>
<td>mrcup</td>
<td>CM</td>
<td> memory relative cursor addressing, move to row #1 columns #2 
</td>
</tr>
<tr VALIGN=top>
<td>cursor_normal</td>
<td>cnorm</td>
<td>ve</td>
<td> make cursor appear normal (undo civis/cvvis) 
</td>
</tr>
<tr VALIGN=top>
<td>cursor_right</td>
<td>cuf1</td>
<td>nd</td>
<td> non-destructive space (move right one space) 
</td>
</tr>
<tr VALIGN=top>
<td>cursor_to_ll</td>
<td>ll</td>
<td>ll</td>
<td> last line, first column (if no cup) 
</td>
</tr>
<tr VALIGN=top>
<td>cursor_up</td>
<td>cuu1</td>
<td>up</td>
<td> up one line 
</td>
</tr>
<tr VALIGN=top>
<td>cursor_visible</td>
<td>cvvis</td>
<td>vs</td>
<td> make cursor very visible 
</td>
</tr>
<tr VALIGN=top>
<td>define_char</td>
<td>defc</td>
<td>ZE</td>
<td> Define a character #1, #2 dots wide, descender #3 
</td>
</tr>
<tr VALIGN=top>
<td>delete_character</td>
<td>dch1</td>
<td>dc</td>
<td> delete character (P*) 
</td>
</tr>
<tr VALIGN=top>
<td>delete_line</td>
<td>dl1</td>
<td>dl</td>
<td> delete line (P*) 
</td>
</tr>
<tr VALIGN=top>
<td>dial_phone</td>
<td>dial</td>
<td>DI</td>
<td> dial number #1 
</td>
</tr>
<tr VALIGN=top>
<td>dis_status_line</td>
<td>dsl</td>
<td>ds</td>
<td> disable status line 
</td>
</tr>
<tr VALIGN=top>
<td>display_clock</td>
<td>dclk</td>
<td>DK</td>
<td> display clock 
</td>
</tr>
<tr VALIGN=top>
<td>down_half_line</td>
<td>hd</td>
<td>hd</td>
<td> half a line down 
</td>
</tr>
<tr VALIGN=top>
<td>ena_acs</td>
<td>enacs</td>
<td>eA</td>
<td> enable alternate char set 
</td>
</tr>
<tr VALIGN=top>
<td>enter_alt_charset_mode</td>
<td>smacs</td>
<td>as</td>
<td> start alternate character set (P) 
</td>
</tr>
<tr VALIGN=top>
<td>enter_am_mode</td>
<td>smam</td>
<td>SA</td>
<td> turn on automatic margins 
</td>
</tr>
<tr VALIGN=top>
<td>enter_blink_mode</td>
<td>blink</td>
<td>mb</td>
<td> turn on blinking 
</td>
</tr>
<tr VALIGN=top>
<td>enter_bold_mode</td>
<td>bold</td>
<td>md</td>
<td> turn on bold (extra bright) mode 
</td>
</tr>
<tr VALIGN=top>
<td>enter_ca_mode</td>
<td>smcup</td>
<td>ti</td>
<td> string to start programs using cup 
</td>
</tr>
<tr VALIGN=top>
<td>enter_delete_mode</td>
<td>smdc</td>
<td>dm</td>
<td> enter delete mode 
</td>
</tr>
<tr VALIGN=top>
<td>enter_dim_mode</td>
<td>dim</td>
<td>mh</td>
<td> turn on half-bright mode 
</td>
</tr>
<tr VALIGN=top>
<td>enter_doublewide_mode</td>
<td>swidm</td>
<td>ZF</td>
<td> Enter double-wide mode 
</td>
</tr>
<tr VALIGN=top>
<td>enter_draft_quality</td>
<td>sdrfq</td>
<td>ZG</td>
<td> Enter draft-quality mode 
</td>
</tr>
<tr VALIGN=top>
<td>enter_insert_mode</td>
<td>smir</td>
<td>im</td>
<td> enter insert mode 
</td>
</tr>
<tr VALIGN=top>
<td>enter_italics_mode</td>
<td>sitm</td>
<td>ZH</td>
<td> Enter italic mode 
</td>
</tr>
<tr VALIGN=top>
<td>enter_leftward_mode</td>
<td>slm</td>
<td>ZI</td>
<td> Start leftward carriage motion 
</td>
</tr>
<tr VALIGN=top>
<td>enter_micro_mode</td>
<td>smicm</td>
<td>ZJ</td>
<td> Start micro-motion mode 
</td>
</tr>
<tr VALIGN=top>
<td>enter_near_letter_quality</td>
<td>snlq</td>
<td>ZK</td>
<td> Enter NLQ mode 
</td>
</tr>
<tr VALIGN=top>
<td>enter_normal_quality</td>
<td>snrmq</td>
<td>ZL</td>
<td> Enter normal-quality mode 
</td>
</tr>
<tr VALIGN=top>
<td>enter_protected_mode</td>
<td>prot</td>
<td>mp</td>
<td> turn on protected mode 
</td>
</tr>
<tr VALIGN=top>
<td>enter_reverse_mode</td>
<td>rev</td>
<td>mr</td>
<td> turn on reverse video mode 
</td>
</tr>
<tr VALIGN=top>
<td>enter_secure_mode</td>
<td>invis</td>
<td>mk</td>
<td> turn on blank mode (characters invisible) 
</td>
</tr>
<tr VALIGN=top>
<td>enter_shadow_mode</td>
<td>sshm</td>
<td>ZM</td>
<td> Enter shadow-print mode 
</td>
</tr>
<tr VALIGN=top>
<td>enter_standout_mode</td>
<td>smso</td>
<td>so</td>
<td> begin standout mode 
</td>
</tr>
<tr VALIGN=top>
<td>enter_subscript_mode</td>
<td>ssubm</td>
<td>ZN</td>
<td> Enter subscript mode 
</td>
</tr>
<tr VALIGN=top>
<td>enter_superscript_mode</td>
<td>ssupm</td>
<td>ZO</td>
<td> Enter superscript mode 
</td>
</tr>
<tr VALIGN=top>
<td>enter_underline_mode</td>
<td>smul</td>
<td>us</td>
<td> begin underline mode 
</td>
</tr>
<tr VALIGN=top>
<td>enter_upward_mode</td>
<td>sum</td>
<td>ZP</td>
<td> Start upward carriage motion 
</td>
</tr>
<tr VALIGN=top>
<td>enter_xon_mode</td>
<td>smxon</td>
<td>SX</td>
<td> turn on xon/xoff handshaking 
</td>
</tr>
<tr VALIGN=top>
<td>erase_chars</td>
<td>ech</td>
<td>ec</td>
<td> erase #1 characters (P) 
</td>
</tr>
<tr VALIGN=top>
<td>exit_alt_charset_mode</td>
<td>rmacs</td>
<td>ae</td>
<td> end alternate character set (P) 
</td>
</tr>
<tr VALIGN=top>
<td>exit_am_mode</td>
<td>rmam</td>
<td>RA</td>
<td> turn off automatic margins 
</td>
</tr>
<tr VALIGN=top>
<td>exit_attribute_mode</td>
<td>sgr0</td>
<td>me</td>
<td> turn off all attributes 
</td>
</tr>
<tr VALIGN=top>
<td>exit_ca_mode</td>
<td>rmcup</td>
<td>te</td>
<td> strings to end programs using cup 
</td>
</tr>
<tr VALIGN=top>
<td>exit_delete_mode</td>
<td>rmdc</td>
<td>ed</td>
<td> end delete mode 
</td>
</tr>
<tr VALIGN=top>
<td>exit_doublewide_mode</td>
<td>rwidm</td>
<td>ZQ</td>
<td> End double-wide mode 
</td>
</tr>
<tr VALIGN=top>
<td>exit_insert_mode</td>
<td>rmir</td>
<td>ei</td>
<td> exit insert mode 
</td>
</tr>
<tr VALIGN=top>
<td>exit_italics_mode</td>
<td>ritm</td>
<td>ZR</td>
<td> End italic mode 
</td>
</tr>
<tr VALIGN=top>
<td>exit_leftward_mode</td>
<td>rlm</td>
<td>ZS</td>
<td> End left-motion mode 
</td>
</tr>
<tr VALIGN=top>
<td>exit_micro_mode</td>
<td>rmicm</td>
<td>ZT</td>
<td> End micro-motion mode 
</td>
</tr>
<tr VALIGN=top>
<td>exit_shadow_mode</td>
<td>rshm</td>
<td>ZU</td>
<td> End shadow-print mode 
</td>
</tr>
<tr VALIGN=top>
<td>exit_standout_mode</td>
<td>rmso</td>
<td>se</td>
<td> exit standout mode 
</td>
</tr>
<tr VALIGN=top>
<td>exit_subscript_mode</td>
<td>rsubm</td>
<td>ZV</td>
<td> End subscript mode 
</td>
</tr>
<tr VALIGN=top>
<td>exit_superscript_mode</td>
<td>rsupm</td>
<td>ZW</td>
<td> End superscript mode 
</td>
</tr>
<tr VALIGN=top>
<td>exit_underline_mode</td>
<td>rmul</td>
<td>ue</td>
<td> exit underline mode 
</td>
</tr>
<tr VALIGN=top>
<td>exit_upward_mode</td>
<td>rum</td>
<td>ZX</td>
<td> End reverse character motion 
</td>
</tr>
<tr VALIGN=top>
<td>exit_xon_mode</td>
<td>rmxon</td>
<td>RX</td>
<td> turn off xon/xoff handshaking 
</td>
</tr>
<tr VALIGN=top>
<td>fixed_pause</td>
<td>pause</td>
<td>PA</td>
<td> pause for 2-3 seconds 
</td>
</tr>
<tr VALIGN=top>
<td>flash_hook</td>
<td>hook</td>
<td>fh</td>
<td> flash switch hook 
</td>
</tr>
<tr VALIGN=top>
<td>flash_screen</td>
<td>flash</td>
<td>vb</td>
<td> visible bell (may not move cursor) 
</td>
</tr>
<tr VALIGN=top>
<td>form_feed</td>
<td>ff</td>
<td>ff</td>
<td> hardcopy terminal page eject (P*) 
</td>
</tr>
<tr VALIGN=top>
<td>from_status_line</td>
<td>fsl</td>
<td>fs</td>
<td> return from status line 
</td>
</tr>
<tr VALIGN=top>
<td>goto_window</td>
<td>wingo</td>
<td>WG</td>
<td> go to window #1 
</td>
</tr>
<tr VALIGN=top>
<td>hangup</td>
<td>hup</td>
<td>HU</td>
<td> hang-up phone 
</td>
</tr>
<tr VALIGN=top>
<td>init_1string</td>
<td>is1</td>
<td>i1</td>
<td> initialization string 
</td>
</tr>
<tr VALIGN=top>
<td>init_2string</td>
<td>is2</td>
<td>is</td>
<td> initialization string 
</td>
</tr>
<tr VALIGN=top>
<td>init_3string</td>
<td>is3</td>
<td>i3</td>
<td> initialization string 
</td>
</tr>
<tr VALIGN=top>
<td>init_file</td>
<td>if</td>
<td>if</td>
<td> name of initialization file 
</td>
</tr>
<tr VALIGN=top>
<td>init_prog</td>
<td>iprog</td>
<td>iP</td>
<td> path name of program for initialization 
</td>
</tr>
<tr VALIGN=top>
<td>initialize_color</td>
<td>initc</td>
<td>Ic</td>
<td> initialize color #1 to (#2,#3,#4) 
</td>
</tr>
<tr VALIGN=top>
<td>initialize_pair</td>
<td>initp</td>
<td>Ip</td>
<td> Initialize color pair #1 to fg=(#2,#3,#4), bg=(#5,#6,#7) 
</td>
</tr>
<tr VALIGN=top>
<td>insert_character</td>
<td>ich1</td>
<td>ic</td>
<td> insert character (P) 
</td>
</tr>
<tr VALIGN=top>
<td>insert_line</td>
<td>il1</td>
<td>al</td>
<td> insert line (P*) 
</td>
</tr>
<tr VALIGN=top>
<td>insert_padding</td>
<td>ip</td>
<td>ip</td>
<td> insert padding after inserted character 
</td>
</tr>
<tr VALIGN=top>
<td>key_a1</td>
<td>ka1</td>
<td>K1</td>
<td> upper left of keypad 
</td>
</tr>
<tr VALIGN=top>
<td>key_a3</td>
<td>ka3</td>
<td>K3</td>
<td> upper right of keypad 
</td>
</tr>
<tr VALIGN=top>
<td>key_b2</td>
<td>kb2</td>
<td>K2</td>
<td> center of keypad 
</td>
</tr>
<tr VALIGN=top>
<td>key_backspace</td>
<td>kbs</td>
<td>kb</td>
<td> backspace key 
</td>
</tr>
<tr VALIGN=top>
<td>key_beg</td>
<td>kbeg</td>
<td>@1</td>
<td> begin key 
</td>
</tr>
<tr VALIGN=top>
<td>key_btab</td>
<td>kcbt</td>
<td>kB</td>
<td> back-tab key 
</td>
</tr>
<tr VALIGN=top>
<td>key_c1</td>
<td>kc1</td>
<td>K4</td>
<td> lower left of keypad 
</td>
</tr>
<tr VALIGN=top>
<td>key_c3</td>
<td>kc3</td>
<td>K5</td>
<td> lower right of keypad 
</td>
</tr>
<tr VALIGN=top>
<td>key_cancel</td>
<td>kcan</td>
<td>@2</td>
<td> cancel key 
</td>
</tr>
<tr VALIGN=top>
<td>key_catab</td>
<td>ktbc</td>
<td>ka</td>
<td> clear-all-tabs key 
</td>
</tr>
<tr VALIGN=top>
<td>key_clear</td>
<td>kclr</td>
<td>kC</td>
<td> clear-screen or erase key 
</td>
</tr>
<tr VALIGN=top>
<td>key_close</td>
<td>kclo</td>
<td>@3</td>
<td> close key 
</td>
</tr>
<tr VALIGN=top>
<td>key_command</td>
<td>kcmd</td>
<td>@4</td>
<td> command key 
</td>
</tr>
<tr VALIGN=top>
<td>key_copy</td>
<td>kcpy</td>
<td>@5</td>
<td> copy key 
</td>
</tr>
<tr VALIGN=top>
<td>key_create</td>
<td>kcrt</td>
<td>@6</td>
<td> create key 
</td>
</tr>
<tr VALIGN=top>
<td>key_ctab</td>
<td>kctab</td>
<td>kt</td>
<td> clear-tab key 
</td>
</tr>
<tr VALIGN=top>
<td>key_dc</td>
<td>kdch1</td>
<td>kD</td>
<td> delete-character key 
</td>
</tr>
<tr VALIGN=top>
<td>key_dl</td>
<td>kdl1</td>
<td>kL</td>
<td> delete-line key 
</td>
</tr>
<tr VALIGN=top>
<td>key_down</td>
<td>kcud1</td>
<td>kd</td>
<td> down-arrow key 
</td>
</tr>
<tr VALIGN=top>
<td>key_eic</td>
<td>krmir</td>
<td>kM</td>
<td> sent by rmir or smir in insert mode 
</td>
</tr>
<tr VALIGN=top>
<td>key_end</td>
<td>kend</td>
<td>@7</td>
<td> end key 
</td>
</tr>
<tr VALIGN=top>
<td>key_enter</td>
<td>kent</td>
<td>@8</td>
<td> enter/send key 
</td>
</tr>
<tr VALIGN=top>
<td>key_eol</td>
<td>kel</td>
<td>kE</td>
<td> clear-to-end-of-line key 
</td>
</tr>
<tr VALIGN=top>
<td>key_eos</td>
<td>ked</td>
<td>kS</td>
<td> clear-to-end-of-screen key 
</td>
</tr>
<tr VALIGN=top>
<td>key_exit</td>
<td>kext</td>
<td>@9</td>
<td> exit key 
</td>
</tr>
<tr VALIGN=top>
<td>key_f0</td>
<td>kf0</td>
<td>k0</td>
<td> F0 function key 
</td>
</tr>
<tr VALIGN=top>
<td>key_f1</td>
<td>kf1</td>
<td>k1</td>
<td> F1 function key 
</td>
</tr>
<tr VALIGN=top>
<td>key_f10</td>
<td>kf10</td>
<td>k;</td>
<td> F10 function key 
</td>
</tr>
<tr VALIGN=top>
<td>key_f11</td>
<td>kf11</td>
<td>F1</td>
<td> F11 function key 
</td>
</tr>
<tr VALIGN=top>
<td>key_f12</td>
<td>kf12</td>
<td>F2</td>
<td> F12 function key 
</td>
</tr>
<tr VALIGN=top>
<td>key_f13</td>
<td>kf13</td>
<td>F3</td>
<td> F13 function key 
</td>
</tr>
<tr VALIGN=top>
<td>key_f14</td>
<td>kf14</td>
<td>F4</td>
<td> F14 function key 
</td>
</tr>
<tr VALIGN=top>
<td>key_f15</td>
<td>kf15</td>
<td>F5</td>
<td> F15 function key 
</td>
</tr>
<tr VALIGN=top>
<td>key_f16</td>
<td>kf16</td>
<td>F6</td>
<td> F16 function key 
</td>
</tr>
<tr VALIGN=top>
<td>key_f17</td>
<td>kf17</td>
<td>F7</td>
<td> F17 function key 
</td>
</tr>
<tr VALIGN=top>
<td>key_f18</td>
<td>kf18</td>
<td>F8</td>
<td> F18 function key 
</td>
</tr>
<tr VALIGN=top>
<td>key_f19</td>
<td>kf19</td>
<td>F9</td>
<td> F19 function key 
</td>
</tr>
<tr VALIGN=top>
<td>key_f2</td>
<td>kf2</td>
<td>k2</td>
<td> F2 function key 
</td>
</tr>
<tr VALIGN=top>
<td>key_f20</td>
<td>kf20</td>
<td>FA</td>
<td> F20 function key 
</td>
</tr>
<tr VALIGN=top>
<td>key_f21</td>
<td>kf21</td>
<td>FB</td>
<td> F21 function key 
</td>
</tr>
<tr VALIGN=top>
<td>key_f22</td>
<td>kf22</td>
<td>FC</td>
<td> F22 function key 
</td>
</tr>
<tr VALIGN=top>
<td>key_f23</td>
<td>kf23</td>
<td>FD</td>
<td> F23 function key 
</td>
</tr>
<tr VALIGN=top>
<td>key_f24</td>
<td>kf24</td>
<td>FE</td>
<td> F24 function key 
</td>
</tr>
<tr VALIGN=top>
<td>key_f25</td>
<td>kf25</td>
<td>FF</td>
<td> F25 function key 
</td>
</tr>
<tr VALIGN=top>
<td>key_f26</td>
<td>kf26</td>
<td>FG</td>
<td> F26 function key 
</td>
</tr>
<tr VALIGN=top>
<td>key_f27</td>
<td>kf27</td>
<td>FH</td>
<td> F27 function key 
</td>
</tr>
<tr VALIGN=top>
<td>key_f28</td>
<td>kf28</td>
<td>FI</td>
<td> F28 function key 
</td>
</tr>
<tr VALIGN=top>
<td>key_f29</td>
<td>kf29</td>
<td>FJ</td>
<td> F29 function key 
</td>
</tr>
<tr VALIGN=top>
<td>key_f3</td>
<td>kf3</td>
<td>k3</td>
<td> F3 function key 
</td>
</tr>
<tr VALIGN=top>
<td>key_f30</td>
<td>kf30</td>
<td>FK</td>
<td> F30 function key 
</td>
</tr>
<tr VALIGN=top>
<td>key_f31</td>
<td>kf31</td>
<td>FL</td>
<td> F31 function key 
</td>
</tr>
<tr VALIGN=top>
<td>key_f32</td>
<td>kf32</td>
<td>FM</td>
<td> F32 function key 
</td>
</tr>
<tr VALIGN=top>
<td>key_f33</td>
<td>kf33</td>
<td>FN</td>
<td> F33 function key 
</td>
</tr>
<tr VALIGN=top>
<td>key_f34</td>
<td>kf34</td>
<td>FO</td>
<td> F34 function key 
</td>
</tr>
<tr VALIGN=top>
<td>key_f35</td>
<td>kf35</td>
<td>FP</td>
<td> F35 function key 
</td>
</tr>
<tr VALIGN=top>
<td>key_f36</td>
<td>kf36</td>
<td>FQ</td>
<td> F36 function key 
</td>
</tr>
<tr VALIGN=top>
<td>key_f37</td>
<td>kf37</td>
<td>FR</td>
<td> F37 function key 
</td>
</tr>
<tr VALIGN=top>
<td>key_f38</td>
<td>kf38</td>
<td>FS</td>
<td> F38 function key 
</td>
</tr>
<tr VALIGN=top>
<td>key_f39</td>
<td>kf39</td>
<td>FT</td>
<td> F39 function key 
</td>
</tr>
<tr VALIGN=top>
<td>key_f4</td>
<td>kf4</td>
<td>k4</td>
<td> F4 function key 
</td>
</tr>
<tr VALIGN=top>
<td>key_f40</td>
<td>kf40</td>
<td>FU</td>
<td> F40 function key 
</td>
</tr>
<tr VALIGN=top>
<td>key_f41</td>
<td>kf41</td>
<td>FV</td>
<td> F41 function key 
</td>
</tr>
<tr VALIGN=top>
<td>key_f42</td>
<td>kf42</td>
<td>FW</td>
<td> F42 function key 
</td>
</tr>
<tr VALIGN=top>
<td>key_f43</td>
<td>kf43</td>
<td>FX</td>
<td> F43 function key 
</td>
</tr>
<tr VALIGN=top>
<td>key_f44</td>
<td>kf44</td>
<td>FY</td>
<td> F44 function key 
</td>
</tr>
<tr VALIGN=top>
<td>key_f45</td>
<td>kf45</td>
<td>FZ</td>
<td> F45 function key 
</td>
</tr>
<tr VALIGN=top>
<td>key_f46</td>
<td>kf46</td>
<td>Fa</td>
<td> F46 function key 
</td>
</tr>
<tr VALIGN=top>
<td>key_f47</td>
<td>kf47</td>
<td>Fb</td>
<td> F47 function key 
</td>
</tr>
<tr VALIGN=top>
<td>key_f48</td>
<td>kf48</td>
<td>Fc</td>
<td> F48 function key 
</td>
</tr>
<tr VALIGN=top>
<td>key_f49</td>
<td>kf49</td>
<td>Fd</td>
<td> F49 function key 
</td>
</tr>
<tr VALIGN=top>
<td>key_f5</td>
<td>kf5</td>
<td>k5</td>
<td> F5 function key 
</td>
</tr>
<tr VALIGN=top>
<td>key_f50</td>
<td>kf50</td>
<td>Fe</td>
<td> F50 function key 
</td>
</tr>
<tr VALIGN=top>
<td>key_f51</td>
<td>kf51</td>
<td>Ff</td>
<td> F51 function key 
</td>
</tr>
<tr VALIGN=top>
<td>key_f52</td>
<td>kf52</td>
<td>Fg</td>
<td> F52 function key 
</td>
</tr>
<tr VALIGN=top>
<td>key_f53</td>
<td>kf53</td>
<td>Fh</td>
<td> F53 function key 
</td>
</tr>
<tr VALIGN=top>
<td>key_f54</td>
<td>kf54</td>
<td>Fi</td>
<td> F54 function key 
</td>
</tr>
<tr VALIGN=top>
<td>key_f55</td>
<td>kf55</td>
<td>Fj</td>
<td> F55 function key 
</td>
</tr>
<tr VALIGN=top>
<td>key_f56</td>
<td>kf56</td>
<td>Fk</td>
<td> F56 function key 
</td>
</tr>
<tr VALIGN=top>
<td>key_f57</td>
<td>kf57</td>
<td>Fl</td>
<td> F57 function key 
</td>
</tr>
<tr VALIGN=top>
<td>key_f58</td>
<td>kf58</td>
<td>Fm</td>
<td> F58 function key 
</td>
</tr>
<tr VALIGN=top>
<td>key_f59</td>
<td>kf59</td>
<td>Fn</td>
<td> F59 function key 
</td>
</tr>
<tr VALIGN=top>
<td>key_f6</td>
<td>kf6</td>
<td>k6</td>
<td> F6 function key 
</td>
</tr>
<tr VALIGN=top>
<td>key_f60</td>
<td>kf60</td>
<td>Fo</td>
<td> F60 function key 
</td>
</tr>
<tr VALIGN=top>
<td>key_f61</td>
<td>kf61</td>
<td>Fp</td>
<td> F61 function key 
</td>
</tr>
<tr VALIGN=top>
<td>key_f62</td>
<td>kf62</td>
<td>Fq</td>
<td> F62 function key 
</td>
</tr>
<tr VALIGN=top>
<td>key_f63</td>
<td>kf63</td>
<td>Fr</td>
<td> F63 function key 
</td>
</tr>
<tr VALIGN=top>
<td>key_f7</td>
<td>kf7</td>
<td>k7</td>
<td> F7 function key 
</td>
</tr>
<tr VALIGN=top>
<td>key_f8</td>
<td>kf8</td>
<td>k8</td>
<td> F8 function key 
</td>
</tr>
<tr VALIGN=top>
<td>key_f9</td>
<td>kf9</td>
<td>k9</td>
<td> F9 function key 
</td>
</tr>
<tr VALIGN=top>
<td>key_find</td>
<td>kfnd</td>
<td>@0</td>
<td> find key 
</td>
</tr>
<tr VALIGN=top>
<td>key_help</td>
<td>khlp</td>
<td>%1</td>
<td> help key 
</td>
</tr>
<tr VALIGN=top>
<td>key_home</td>
<td>khome</td>
<td>kh</td>
<td> home key 
</td>
</tr>
<tr VALIGN=top>
<td>key_ic</td>
<td>kich1</td>
<td>kI</td>
<td> insert-character key 
</td>
</tr>
<tr VALIGN=top>
<td>key_il</td>
<td>kil1</td>
<td>kA</td>
<td> insert-line key 
</td>
</tr>
<tr VALIGN=top>
<td>key_left</td>
<td>kcub1</td>
<td>kl</td>
<td> left-arrow key 
</td>
</tr>
<tr VALIGN=top>
<td>key_ll</td>
<td>kll</td>
<td>kH</td>
<td> lower-left key (home down) 
</td>
</tr>
<tr VALIGN=top>
<td>key_mark</td>
<td>kmrk</td>
<td>%2</td>
<td> mark key 
</td>
</tr>
<tr VALIGN=top>
<td>key_message</td>
<td>kmsg</td>
<td>%3</td>
<td> message key 
</td>
</tr>
<tr VALIGN=top>
<td>key_move</td>
<td>kmov</td>
<td>%4</td>
<td> move key 
</td>
</tr>
<tr VALIGN=top>
<td>key_next</td>
<td>knxt</td>
<td>%5</td>
<td> next key 
</td>
</tr>
<tr VALIGN=top>
<td>key_npage</td>
<td>knp</td>
<td>kN</td>
<td> next-page key 
</td>
</tr>
<tr VALIGN=top>
<td>key_open</td>
<td>kopn</td>
<td>%6</td>
<td> open key 
</td>
</tr>
<tr VALIGN=top>
<td>key_options</td>
<td>kopt</td>
<td>%7</td>
<td> options key 
</td>
</tr>
<tr VALIGN=top>
<td>key_ppage</td>
<td>kpp</td>
<td>kP</td>
<td> previous-page key 
</td>
</tr>
<tr VALIGN=top>
<td>key_previous</td>
<td>kprv</td>
<td>%8</td>
<td> previous key 
</td>
</tr>
<tr VALIGN=top>
<td>key_print</td>
<td>kprt</td>
<td>%9</td>
<td> print key 
</td>
</tr>
<tr VALIGN=top>
<td>key_redo</td>
<td>krdo</td>
<td>%0</td>
<td> redo key 
</td>
</tr>
<tr VALIGN=top>
<td>key_reference</td>
<td>kref</td>
<td>&amp;1</td>
<td> reference key 
</td>
</tr>
<tr VALIGN=top>
<td>key_refresh</td>
<td>krfr</td>
<td>&amp;2</td>
<td> refresh key 
</td>
</tr>
<tr VALIGN=top>
<td>key_replace</td>
<td>krpl</td>
<td>&amp;3</td>
<td> replace key 
</td>
</tr>
<tr VALIGN=top>
<td>key_restart</td>
<td>krst</td>
<td>&amp;4</td>
<td> restart key 
</td>
</tr>
<tr VALIGN=top>
<td>key_resume</td>
<td>kres</td>
<td>&amp;5</td>
<td> resume key 
</td>
</tr>
<tr VALIGN=top>
<td>key_right</td>
<td>kcuf1</td>
<td>kr</td>
<td> right-arrow key 
</td>
</tr>
<tr VALIGN=top>
<td>key_save</td>
<td>ksav</td>
<td>&amp;6</td>
<td> save key 
</td>
</tr>
<tr VALIGN=top>
<td>key_sbeg</td>
<td>kBEG</td>
<td>&amp;9</td>
<td> shifted begin key 
</td>
</tr>
<tr VALIGN=top>
<td>key_scancel</td>
<td>kCAN</td>
<td>&amp;0</td>
<td> shifted cancel key 
</td>
</tr>
<tr VALIGN=top>
<td>key_scommand</td>
<td>kCMD</td>
<td>*1</td>
<td> shifted command key 
</td>
</tr>
<tr VALIGN=top>
<td>key_scopy</td>
<td>kCPY</td>
<td>*2</td>
<td> shifted copy key 
</td>
</tr>
<tr VALIGN=top>
<td>key_screate</td>
<td>kCRT</td>
<td>*3</td>
<td> shifted create key 
</td>
</tr>
<tr VALIGN=top>
<td>key_sdc</td>
<td>kDC</td>
<td>*4</td>
<td> shifted delete-character key 
</td>
</tr>
<tr VALIGN=top>
<td>key_sdl</td>
<td>kDL</td>
<td>*5</td>
<td> shifted delete-line key 
</td>
</tr>
<tr VALIGN=top>
<td>key_select</td>
<td>kslt</td>
<td>*6</td>
<td> select key 
</td>
</tr>
<tr VALIGN=top>
<td>key_send</td>
<td>kEND</td>
<td>*7</td>
<td> shifted end key 
</td>
</tr>
<tr VALIGN=top>
<td>key_seol</td>
<td>kEOL</td>
<td>*8</td>
<td> shifted clear-to-end-of-line key 
</td>
</tr>
<tr VALIGN=top>
<td>key_sexit</td>
<td>kEXT</td>
<td>*9</td>
<td> shifted exit key 
</td>
</tr>
<tr VALIGN=top>
<td>key_sf</td>
<td>kind</td>
<td>kF</td>
<td> scroll-forward key 
</td>
</tr>
<tr VALIGN=top>
<td>key_sfind</td>
<td>kFND</td>
<td>*0</td>
<td> shifted find key 
</td>
</tr>
<tr VALIGN=top>
<td>key_shelp</td>
<td>kHLP</td>
<td>#1</td>
<td> shifted help key 
</td>
</tr>
<tr VALIGN=top>
<td>key_shome</td>
<td>kHOM</td>
<td>#2</td>
<td> shifted home key 
</td>
</tr>
<tr VALIGN=top>
<td>key_sic</td>
<td>kIC</td>
<td>#3</td>
<td> shifted insert-character key 
</td>
</tr>
<tr VALIGN=top>
<td>key_sleft</td>
<td>kLFT</td>
<td>#4</td>
<td> shifted left-arrow key 
</td>
</tr>
<tr VALIGN=top>
<td>key_smessage</td>
<td>kMSG</td>
<td>%a</td>
<td> shifted message key 
</td>
</tr>
<tr VALIGN=top>
<td>key_smove</td>
<td>kMOV</td>
<td>%b</td>
<td> shifted move key 
</td>
</tr>
<tr VALIGN=top>
<td>key_snext</td>
<td>kNXT</td>
<td>%c</td>
<td> shifted next key 
</td>
</tr>
<tr VALIGN=top>
<td>key_soptions</td>
<td>kOPT</td>
<td>%d</td>
<td> shifted options key 
</td>
</tr>
<tr VALIGN=top>
<td>key_sprevious</td>
<td>kPRV</td>
<td>%e</td>
<td> shifted previous key 
</td>
</tr>
<tr VALIGN=top>
<td>key_sprint</td>
<td>kPRT</td>
<td>%f</td>
<td> shifted print key 
</td>
</tr>
<tr VALIGN=top>
<td>key_sr</td>
<td>kri</td>
<td>kR</td>
<td> scroll-backward key 
</td>
</tr>
<tr VALIGN=top>
<td>key_sredo</td>
<td>kRDO</td>
<td>%g</td>
<td> shifted redo key 
</td>
</tr>
<tr VALIGN=top>
<td>key_sreplace</td>
<td>kRPL</td>
<td>%h</td>
<td> shifted replace key 
</td>
</tr>
<tr VALIGN=top>
<td>key_sright</td>
<td>kRIT</td>
<td>%i</td>
<td> shifted right-arrow key 
</td>
</tr>
<tr VALIGN=top>
<td>key_srsume</td>
<td>kRES</td>
<td>%j</td>
<td> shifted resume key 
</td>
</tr>
<tr VALIGN=top>
<td>key_ssave</td>
<td>kSAV</td>
<td>!1</td>
<td> shifted save key 
</td>
</tr>
<tr VALIGN=top>
<td>key_ssuspend</td>
<td>kSPD</td>
<td>!2</td>
<td> shifted suspend key 
</td>
</tr>
<tr VALIGN=top>
<td>key_stab</td>
<td>khts</td>
<td>kT</td>
<td> set-tab key 
</td>
</tr>
<tr VALIGN=top>
<td>key_sundo</td>
<td>kUND</td>
<td>!3</td>
<td> shifted undo key 
</td>
</tr>
<tr VALIGN=top>
<td>key_suspend</td>
<td>kspd</td>
<td>&amp;7</td>
<td> suspend key 
</td>
</tr>
<tr VALIGN=top>
<td>key_undo</td>
<td>kund</td>
<td>&amp;8</td>
<td> undo key 
</td>
</tr>
<tr VALIGN=top>
<td>key_up</td>
<td>kcuu1</td>
<td>ku</td>
<td> up-arrow key 
</td>
</tr>
<tr VALIGN=top>
<td>keypad_local</td>
<td>rmkx</td>
<td>ke</td>
<td> leave &#8216;keyboard_transmit&#8217; mode 
</td>
</tr>
<tr VALIGN=top>
<td>keypad_xmit</td>
<td>smkx</td>
<td>ks</td>
<td> enter &#8216;keyboard_transmit&#8217; mode 
</td>
</tr>
<tr VALIGN=top>
<td>lab_f0</td>
<td>lf0</td>
<td>l0</td>
<td> label on function key f0 if not f0 
</td>
</tr>
<tr VALIGN=top>
<td>lab_f1</td>
<td>lf1</td>
<td>l1</td>
<td> label on function key f1 if not f1 
</td>
</tr>
<tr VALIGN=top>
<td>lab_f10</td>
<td>lf10</td>
<td>la</td>
<td> label on function key f10 if not f10 
</td>
</tr>
<tr VALIGN=top>
<td>lab_f2</td>
<td>lf2</td>
<td>l2</td>
<td> label on function key f2 if not f2 
</td>
</tr>
<tr VALIGN=top>
<td>lab_f3</td>
<td>lf3</td>
<td>l3</td>
<td> label on function key f3 if not f3 
</td>
</tr>
<tr VALIGN=top>
<td>lab_f4</td>
<td>lf4</td>
<td>l4</td>
<td> label on function key f4 if not f4 
</td>
</tr>
<tr VALIGN=top>
<td>lab_f5</td>
<td>lf5</td>
<td>l5</td>
<td> label on function key f5 if not f5 
</td>
</tr>
<tr VALIGN=top>
<td>lab_f6</td>
<td>lf6</td>
<td>l6</td>
<td> label on function key f6 if not f6 
</td>
</tr>
<tr VALIGN=top>
<td>lab_f7</td>
<td>lf7</td>
<td>l7</td>
<td> label on function key f7 if not f7 
</td>
</tr>
<tr VALIGN=top>
<td>lab_f8</td>
<td>lf8</td>
<td>l8</td>
<td> label on function key f8 if not f8 
</td>
</tr>
<tr VALIGN=top>
<td>lab_f9</td>
<td>lf9</td>
<td>l9</td>
<td> label on function key f9 if not f9 
</td>
</tr>
<tr VALIGN=top>
<td>label_format</td>
<td>fln</td>
<td>Lf</td>
<td> label format 
</td>
</tr>
<tr VALIGN=top>
<td>label_off</td>
<td>rmln</td>
<td>LF</td>
<td> turn off soft labels 
</td>
</tr>
<tr VALIGN=top>
<td>label_on</td>
<td>smln</td>
<td>LO</td>
<td> turn on soft labels 
</td>
</tr>
<tr VALIGN=top>
<td>meta_off</td>
<td>rmm</td>
<td>mo</td>
<td> turn off meta mode 
</td>
</tr>
<tr VALIGN=top>
<td>meta_on</td>
<td>smm</td>
<td>mm</td>
<td> turn on meta mode (8th-bit on) 
</td>
</tr>
<tr VALIGN=top>
<td>micro_column_address</td>
<td>mhpa</td>
<td>ZY</td>
<td> Like column_address in micro mode 
</td>
</tr>
<tr VALIGN=top>
<td>micro_down</td>
<td>mcud1</td>
<td>ZZ</td>
<td> Like cursor_down in micro mode 
</td>
</tr>
<tr VALIGN=top>
<td>micro_left</td>
<td>mcub1</td>
<td>Za</td>
<td> Like cursor_left in micro mode 
</td>
</tr>
<tr VALIGN=top>
<td>micro_right</td>
<td>mcuf1</td>
<td>Zb</td>
<td> Like cursor_right in micro mode 
</td>
</tr>
<tr VALIGN=top>
<td>micro_row_address</td>
<td>mvpa</td>
<td>Zc</td>
<td> Like row_address #1 in micro mode 
</td>
</tr>
<tr VALIGN=top>
<td>micro_up</td>
<td>mcuu1</td>
<td>Zd</td>
<td> Like cursor_up in micro mode 
</td>
</tr>
<tr VALIGN=top>
<td>newline</td>
<td>nel</td>
<td>nw</td>
<td> newline (behave like cr followed by lf) 
</td>
</tr>
<tr VALIGN=top>
<td>order_of_pins</td>
<td>porder</td>
<td>Ze</td>
<td> Match software bits to print-head pins 
</td>
</tr>
<tr VALIGN=top>
<td>orig_colors</td>
<td>oc</td>
<td>oc</td>
<td> Set all color pairs to the original ones 
</td>
</tr>
<tr VALIGN=top>
<td>orig_pair</td>
<td>op</td>
<td>op</td>
<td> Set default pair to its original value 
</td>
</tr>
<tr VALIGN=top>
<td>pad_char</td>
<td>pad</td>
<td>pc</td>
<td> padding char (instead of null) 
</td>
</tr>
<tr VALIGN=top>
<td>parm_dch</td>
<td>dch</td>
<td>DC</td>
<td> delete #1 characters (P*) 
</td>
</tr>
<tr VALIGN=top>
<td>parm_delete_line</td>
<td>dl</td>
<td>DL</td>
<td> delete #1 lines (P*) 
</td>
</tr>
<tr VALIGN=top>
<td>parm_down_cursor</td>
<td>cud</td>
<td>DO</td>
<td> down #1 lines (P*) 
</td>
</tr>
<tr VALIGN=top>
<td>parm_down_micro</td>
<td>mcud</td>
<td>Zf</td>
<td> Like parm_down_cursor in micro mode 
</td>
</tr>
<tr VALIGN=top>
<td>parm_ich</td>
<td>ich</td>
<td>IC</td>
<td> insert #1 characters (P*) 
</td>
</tr>
<tr VALIGN=top>
<td>parm_index</td>
<td>indn</td>
<td>SF</td>
<td> scroll forward #1 lines (P) 
</td>
</tr>
<tr VALIGN=top>
<td>parm_insert_line</td>
<td>il</td>
<td>AL</td>
<td> insert #1 lines (P*) 
</td>
</tr>
<tr VALIGN=top>
<td>parm_left_cursor</td>
<td>cub</td>
<td>LE</td>
<td> move #1 characters to the left (P) 
</td>
</tr>
<tr VALIGN=top>
<td>parm_left_micro</td>
<td>mcub</td>
<td>Zg</td>
<td> Like parm_left_cursor in micro mode 
</td>
</tr>
<tr VALIGN=top>
<td>parm_right_cursor</td>
<td>cuf</td>
<td>RI</td>
<td> move #1 characters to the right (P*) 
</td>
</tr>
<tr VALIGN=top>
<td>parm_right_micro</td>
<td>mcuf</td>
<td>Zh</td>
<td> Like parm_right_cursor in micro mode 
</td>
</tr>
<tr VALIGN=top>
<td>parm_rindex</td>
<td>rin</td>
<td>SR</td>
<td> scroll back #1 lines (P) 
</td>
</tr>
<tr VALIGN=top>
<td>parm_up_cursor</td>
<td>cuu</td>
<td>UP</td>
<td> up #1 lines (P*) 
</td>
</tr>
<tr VALIGN=top>
<td>parm_up_micro</td>
<td>mcuu</td>
<td>Zi</td>
<td> Like parm_up_cursor in micro mode 
</td>
</tr>
<tr VALIGN=top>
<td>pkey_key</td>
<td>pfkey</td>
<td>pk</td>
<td> program function key #1 to type string #2 
</td>
</tr>
<tr VALIGN=top>
<td>pkey_local</td>
<td>pfloc</td>
<td>pl</td>
<td> program function key #1 to execute string #2 
</td>
</tr>
<tr VALIGN=top>
<td>pkey_xmit</td>
<td>pfx</td>
<td>px</td>
<td> program function key #1 to transmit string #2 
</td>
</tr>
<tr VALIGN=top>
<td>plab_norm</td>
<td>pln</td>
<td>pn</td>
<td> program label #1 to show string #2 
</td>
</tr>
<tr VALIGN=top>
<td>print_screen</td>
<td>mc0</td>
<td>ps</td>
<td> print contents of screen 
</td>
</tr>
<tr VALIGN=top>
<td>prtr_non</td>
<td>mc5p</td>
<td>pO</td>
<td> turn on printer for #1 bytes 
</td>
</tr>
<tr VALIGN=top>
<td>prtr_off</td>
<td>mc4</td>
<td>pf</td>
<td> turn off printer 
</td>
</tr>
<tr VALIGN=top>
<td>prtr_on</td>
<td>mc5</td>
<td>po</td>
<td> turn on printer 
</td>
</tr>
<tr VALIGN=top>
<td>pulse</td>
<td>pulse</td>
<td>PU</td>
<td> select pulse dialing 
</td>
</tr>
<tr VALIGN=top>
<td>quick_dial</td>
<td>qdial</td>
<td>QD</td>
<td> dial number #1 without checking 
</td>
</tr>
<tr VALIGN=top>
<td>remove_clock</td>
<td>rmclk</td>
<td>RC</td>
<td> remove clock 
</td>
</tr>
<tr VALIGN=top>
<td>repeat_char</td>
<td>rep</td>
<td>rp</td>
<td> repeat char #1 #2 times (P*) 
</td>
</tr>
<tr VALIGN=top>
<td>req_for_input</td>
<td>rfi</td>
<td>RF</td>
<td> send next input char (for ptys) 
</td>
</tr>
<tr VALIGN=top>
<td>reset_1string</td>
<td>rs1</td>
<td>r1</td>
<td> reset string 
</td>
</tr>
<tr VALIGN=top>
<td>reset_2string</td>
<td>rs2</td>
<td>r2</td>
<td> reset string 
</td>
</tr>
<tr VALIGN=top>
<td>reset_3string</td>
<td>rs3</td>
<td>r3</td>
<td> reset string 
</td>
</tr>
<tr VALIGN=top>
<td>reset_file</td>
<td>rf</td>
<td>rf</td>
<td> name of reset file 
</td>
</tr>
<tr VALIGN=top>
<td>restore_cursor</td>
<td>rc</td>
<td>rc</td>
<td> restore cursor to position of last save_cursor 
</td>
</tr>
<tr VALIGN=top>
<td>row_address</td>
<td>vpa</td>
<td>cv</td>
<td> vertical position #1 absolute (P) 
</td>
</tr>
<tr VALIGN=top>
<td>save_cursor</td>
<td>sc</td>
<td>sc</td>
<td> save current cursor position (P) 
</td>
</tr>
<tr VALIGN=top>
<td>scroll_forward</td>
<td>ind</td>
<td>sf</td>
<td> scroll text up (P) 
</td>
</tr>
<tr VALIGN=top>
<td>scroll_reverse</td>
<td>ri</td>
<td>sr</td>
<td> scroll text down (P) 
</td>
</tr>
<tr VALIGN=top>
<td>select_char_set</td>
<td>scs</td>
<td>Zj</td>
<td> Select character set, #1 
</td>
</tr>
<tr VALIGN=top>
<td>set_attributes</td>
<td>sgr</td>
<td>sa</td>
<td> define video attributes #1-#9 (PG9) 
</td>
</tr>
<tr VALIGN=top>
<td>set_background</td>
<td>setb</td>
<td>Sb</td>
<td> Set background color #1 
</td>
</tr>
<tr VALIGN=top>
<td>set_bottom_margin</td>
<td>smgb</td>
<td>Zk</td>
<td> Set bottom margin at current line 
</td>
</tr>
<tr VALIGN=top>
<td>set_bottom_margin_parm</td>
<td>smgbp</td>
<td>Zl</td>
<td> Set bottom margin at line #1 or (if smgtp is not given) #2 lines from bottom 
</td>
</tr>
<tr VALIGN=top>
<td>set_clock</td>
<td>sclk</td>
<td>SC</td>
<td> set clock, #1 hrs #2 mins #3 secs 
</td>
</tr>
<tr VALIGN=top>
<td>set_color_pair</td>
<td>scp</td>
<td>sp</td>
<td> Set current color pair to #1 
</td>
</tr>
<tr VALIGN=top>
<td>set_foreground</td>
<td>setf</td>
<td>Sf</td>
<td> Set foreground color #1 
</td>
</tr>
<tr VALIGN=top>
<td>set_left_margin</td>
<td>smgl</td>
<td>ML</td>
<td> set left soft margin at current column.<code>&nbsp;</code> (ML is not in BSD termcap). 
</td>
</tr>
<tr VALIGN=top>
<td>set_left_margin_parm</td>
<td>smglp</td>
<td>Zm</td>
<td> Set left (right) margin at column #1 
</td>
</tr>
<tr VALIGN=top>
<td>set_right_margin</td>
<td>smgr</td>
<td>MR</td>
<td> set right soft margin at current column 
</td>
</tr>
<tr VALIGN=top>
<td>set_right_margin_parm</td>
<td>smgrp</td>
<td>Zn</td>
<td> Set right margin at column #1 
</td>
</tr>
<tr VALIGN=top>
<td>set_tab</td>
<td>hts</td>
<td>st</td>
<td> set a tab in every row, current columns 
</td>
</tr>
<tr VALIGN=top>
<td>set_top_margin</td>
<td>smgt</td>
<td>Zo</td>
<td> Set top margin at current line 
</td>
</tr>
<tr VALIGN=top>
<td>set_top_margin_parm</td>
<td>smgtp</td>
<td>Zp</td>
<td> Set top (bottom) margin at row #1 
</td>
</tr>
<tr VALIGN=top>
<td>set_window</td>
<td>wind</td>
<td>wi</td>
<td> current window is lines #1-#2 cols #3-#4 
</td>
</tr>
<tr VALIGN=top>
<td>start_bit_image</td>
<td>sbim</td>
<td>Zq</td>
<td> Start printing bit image graphics 
</td>
</tr>
<tr VALIGN=top>
<td>start_char_set_def</td>
<td>scsd</td>
<td>Zr</td>
<td> Start character set definition #1, with #2 characters in the set 
</td>
</tr>
<tr VALIGN=top>
<td>stop_bit_image</td>
<td>rbim</td>
<td>Zs</td>
<td> Stop printing bit image graphics 
</td>
</tr>
<tr VALIGN=top>
<td>stop_char_set_def</td>
<td>rcsd</td>
<td>Zt</td>
<td> End definition of character set #1 
</td>
</tr>
<tr VALIGN=top>
<td>subscript_characters</td>
<td>subcs</td>
<td>Zu</td>
<td> List of subscriptable characters 
</td>
</tr>
<tr VALIGN=top>
<td>superscript_characters</td>
<td>supcs</td>
<td>Zv</td>
<td> List of superscriptable characters 
</td>
</tr>
<tr VALIGN=top>
<td>tab</td>
<td>ht</td>
<td>ta</td>
<td> tab to next 8-space hardware tab stop 
</td>
</tr>
<tr VALIGN=top>
<td>these_cause_cr</td>
<td>docr</td>
<td>Zw</td>
<td> Printing any of these characters causes CR 
</td>
</tr>
<tr VALIGN=top>
<td>to_status_line</td>
<td>tsl</td>
<td>ts</td>
<td> move to status line, column #1 
</td>
</tr>
<tr VALIGN=top>
<td>tone</td>
<td>tone</td>
<td>TO</td>
<td> select touch tone dialing 
</td>
</tr>
<tr VALIGN=top>
<td>underline_char</td>
<td>uc</td>
<td>uc</td>
<td> underline char and move past it 
</td>
</tr>
<tr VALIGN=top>
<td>up_half_line</td>
<td>hu</td>
<td>hu</td>
<td> half a line up 
</td>
</tr>
<tr VALIGN=top>
<td>user0</td>
<td>u0</td>
<td>u0</td>
<td> User string #0 
</td>
</tr>
<tr VALIGN=top>
<td>user1</td>
<td>u1</td>
<td>u1</td>
<td> User string #1 
</td>
</tr>
<tr VALIGN=top>
<td>user2</td>
<td>u2</td>
<td>u2</td>
<td> User string #2 
</td>
</tr>
<tr VALIGN=top>
<td>user3</td>
<td>u3</td>
<td>u3</td>
<td> User string #3 
</td>
</tr>
<tr VALIGN=top>
<td>user4</td>
<td>u4</td>
<td>u4</td>
<td> User string #4 
</td>
</tr>
<tr VALIGN=top>
<td>user5</td>
<td>u5</td>
<td>u5</td>
<td> User string #5 
</td>
</tr>
<tr VALIGN=top>
<td>user6</td>
<td>u6</td>
<td>u6</td>
<td> User string #6 
</td>
</tr>
<tr VALIGN=top>
<td>user7</td>
<td>u7</td>
<td>u7</td>
<td> User string #7 
</td>
</tr>
<tr VALIGN=top>
<td>user8</td>
<td>u8</td>
<td>u8</td>
<td> User string #8 
</td>
</tr>
<tr VALIGN=top>
<td>user9</td>
<td>u9</td>
<td>u9</td>
<td> User string #9 
</td>
</tr>
<tr VALIGN=top>
<td>wait_tone</td>
<td>wait</td>
<td>WA</td>
<td> wait for dial-tone 
</td>
</tr>
<tr VALIGN=top>
<td>xoff_character</td>
<td>xoffc</td>
<td>XF</td>
<td> XOFF character 
</td>
</tr>
<tr VALIGN=top>
<td>xon_character</td>
<td>xonc</td>
<td>XN</td>
<td> XON character 
</td>
</tr>
<tr VALIGN=top>
<td>zero_motion</td>
<td>zerom</td>
<td>Zx</td>
<td> No motion for subsequent character 
</td>
</tr>
</table>
<p> </center>  </p>
<p>The following string capabilities are present in the SVr4.0 term structure, but were originally not documented in the man page. </p>
<p> <center> </p>
<table>
<tr VALIGN=top>
<td><code>Variable</code></td>
<td>Cap-</td>
<td>TCap</td>
<td>Description
</td>
</tr>
<tr VALIGN=top>
<td><code>String</code></td>
<td>name</td>
<td>Code</td>
<td>
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
<p> </center>  </p>
<p>The XSI Curses standard added these hardcopy capabilities. They were used in some post-4.1 versions of System V curses, e.g., Solaris 2.5 and IRIX 6.x. Except for <code>YI</code>, the <code>ncurses</code> termcap names for them are invented. According to the XSI Curses standard, they have no termcap names. If your compiled terminfo entries use these, they may not be binary-compatible with System V terminfo entries after SVr4.1; beware! </p>
<p> <center> </p>
<table>
<tr VALIGN=top>
<td><code>Variable</code></td>
<td>Cap-</td>
<td>TCap</td>
<td>Description
</td>
</tr>
<tr VALIGN=top>
<td><code>String</code></td>
<td>name</td>
<td>Code</td>
<td>
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
<p> </center>    </p>
<h3>User-Defined Capabilities</h3>
<p> The preceding section listed the <i>predefined</i> capabilities. They deal with some special features for terminals no longer (or possibly never) produced. Occasionally there are special features of newer terminals which are awkward or impossible to represent by reusing the predefined capabilities. </p>
<p> <code>ncurses</code> addresses this limitation by allowing user-defined capabilities. The <code>tic</code> and <code>infocmp</code> programs provide the <code>-x</code> option for this purpose. When <code>-x</code> is set, <code>tic</code> treats unknown capabilities as user-defined. That is, if <code>tic</code> encounters a capability name which it does not recognize, it infers its type (boolean, number or string) from the syntax and makes an extended table entry for that capability. The <code>use_extended_names</code>(3X) function makes this information conditionally available to applications. The ncurses library provides the data leaving most of the behavior to applications: <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 User-defined capability strings whose name begins with ``k&#8217;&#8216; are treated as function keys. <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 The types (boolean, number, string) determined by <code>tic</code> can be inferred by successful calls on <code>tigetflag</code>, etc. <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 If the capability name happens to be two characters, the capability is also available through the termcap interface. </p>
<p>While termcap is said to be extensible because it does not use a predefined set of capabilities, in practice it has been limited to the capabilities defined by terminfo implementations. As a rule, user-defined capabilities intended for use by termcap applications should be limited to booleans and numbers to avoid running past the 1023 byte limit assumed by termcap implementations and their applications. In particular, providing extended sets of function keys (past the 60 numbered keys and the handful of special named keys) is best done using the longer names available using terminfo.  </p>
<h3>A Sample Entry</h3>
<p> The following entry, describing an ANSI-standard terminal, is representative of what a <code>terminfo</code> entry for a modern terminal typically looks like. </p>
<pre><code>
ansi|ansi/pc-term compatible with color,
        am, mc5i, mir, msgr,
        colors#8, cols#80, it#8, lines#24, ncv#3, pairs#64,
        acsc=+\020\,\021-\030.^Y0\333`\004a\261f\370g\361h\260
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
        mc4=\E[4i, mc5=\E[5i, nel=\r\E[S, op=\E[39;49m,
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
</code></pre>
<p>Entries may continue onto multiple lines by placing white space at the beginning of each line except the first. Comments may be included on lines beginning with ``#&#8216;&#8216;. Capabilities in <i>terminfo</i> are of three types: <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 Boolean capabilities which indicate that the terminal has some particular feature, <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 numeric capabilities giving the size of the terminal or the size of particular delays, and <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 string capabilities, which give a sequence which can be used to perform particular terminal operations. </p>
<h3>Types of Capabilities</h3>
<p>All capabilities have names. For instance, the fact that ANSI-standard terminals have <i>automatic margins</i> (i.e., an automatic return and line-feed when the end of a line is reached) is indicated by the capability <code>am</code>. Hence the description of ansi includes <code>am</code>. Numeric capabilities are followed by the character ``#&#8216;&#8216; and then a positive value. Thus <code>cols</code>, which indicates the number of columns the terminal has, gives the value ``80&#8217;&#8216; for ansi. Values for numeric capabilities may be specified in decimal, octal or hexadecimal, using the C programming language conventions (e.g., 255, 0377 and 0xff or 0xFF). </p>
<p>Finally, string valued capabilities, such as <code>el</code> (clear to end of line sequence) are given by the two-character code, an ``=&#8216;&#8216;, and then a string ending at the next following ``,&#8216;&#8216;. </p>
<p>A number of escape sequences are provided in the string valued capabilities for easy encoding of characters there: <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 Both <code>\E</code> and <code>\e</code> map to an ESCAPE character, <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 <code>^x</code> maps to a control-x for any appropriate <i>x</i>, and <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 the sequences </p>
<dl>
<dd> <p> <code>\n</code>, <code>\l</code>, <code>\r</code>, <code>\t</code>, <code>\b</code>, <code>\f</code>, and <code>\s</code> </p>
 </dd></dl>
<dl>
<dd> <p> produce </p>
 </dd>
<dl>
<dd> <p> <i>newline</i>, <i>line-feed</i>, <i>return</i>, <i>tab</i>, <i>backspace</i>, <i>form-feed</i>, and <i>space</i>, </p>
 </dd></dl>
<dd> <p> respectively. </p>
 </dd></dl>
<p>X/Open Curses does not say what ``appropriate <i>x</i>&#8216;&#8216; might be. In practice, that is a printable ASCII graphic character. The special case ``^?&#8216;&#8216; is interpreted as DEL (127). In all other cases, the character value is AND&#8217;d with 0x1f, mapping to ASCII control codes in the range 0 through 31. </p>
<p>Other escapes include <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 <code>\^</code> for <code>^</code>, <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 <code>\\</code> for <code>\</code>, <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 <code>\</code>, for comma, <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 <code>\:</code> for <code>:</code>, <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 and <code>\0</code> for null. </p>
<dl>
<dd> <p> <code>\0</code> will produce \200, which does not terminate a string but behaves as a null character on most terminals, providing CS7 is specified. See <code><a href="/docs/linux/man/1-stty/">stty</a></code>(1). </p>
 </dd>
<dd> <p> The reason for this quirk is to maintain binary compatibility of the compiled terminfo files with other implementations, e.g., the SVr4 systems, which document this. Compiled terminfo files use null-terminated strings, with no lengths. Modifying this would require a new binary format, which would not work with other implementations. </p>
 </dd></dl>
<p>Finally, characters may be given as three octal digits after a <code>\</code>. </p>
<p>A delay in milliseconds may appear anywhere in a string capability, enclosed in $&lt;..&gt; brackets, as in <code>el</code>=\EK$&lt;5&gt;, and padding characters are supplied by <code>tputs</code>(3X) to provide this delay. <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 The delay must be a number with at most one decimal place of precision; it may be followed by suffixes ``*&#8216;&#8216; or ``/&#8216;&#8216; or both. <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 A ``*&#8216;&#8216; indicates that the padding required is proportional to the number of lines affected by the operation, and the amount given is the per-affected-unit padding required. (In the case of insert character, the factor is still the number of <i>lines</i> affected.) </p>
<dl>
<dd> <p> Normally, padding is advisory if the device has the <code>xon</code> capability; it is used for cost computation but does not trigger delays. <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 A ``/&#8216;&#8216; suffix indicates that the padding is mandatory and forces a delay of the given number of milliseconds even on devices for which <code>xon</code> is present to indicate flow control. </p>
 </dd></dl>
<p>Sometimes individual capabilities must be commented out. To do this, put a period before the capability name. For example, see the second <code>ind</code> in the example above. <br/>
 </p>
<h3>Fetching Compiled Descriptions</h3>
<p>The <code>ncurses</code> library searches for terminal descriptions in several places. It uses only the first description found. The library has a compiled-in list of places to search which can be overridden by environment variables. Before starting to search, <code>ncurses</code> eliminates duplicates in its search list. <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 If the environment variable TERMINFO is set, it is interpreted as the pathname of a directory containing the compiled description you are working on. Only that directory is searched. <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 If TERMINFO is not set, <code>ncurses</code> will instead look in the directory <code>$HOME/.terminfo</code> for a compiled description. <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 Next, if the environment variable TERMINFO_DIRS is set, <code>ncurses</code> will interpret the contents of that variable as a list of colon-separated directories (or database files) to be searched. </p>
<dl>
<dd> <p> An empty directory name (i.e., if the variable begins or ends with a colon, or contains adjacent colons) is interpreted as the system location <i>/etc/terminfo</i>. <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 Finally, <code>ncurses</code> searches these compiled-in locations: </p>
 </dd>
<dl>
<dd> <p> <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 a list of directories (no default value), and <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 the system terminfo directory, <i>/etc/terminfo</i> (the compiled-in default). </p>
 </dd></dl>
</dl>
<h3>Preparing Descriptions</h3>
<p>We now outline how to prepare descriptions of terminals. The most effective way to prepare a terminal description is by imitating the description of a similar terminal in <i>terminfo</i> and to build up a description gradually, using partial descriptions with <i>vi</i> or some other screen-oriented program to check that they are correct. Be aware that a very unusual terminal may expose deficiencies in the ability of the <i>terminfo</i> file to describe it or bugs in the screen-handling code of the test program. </p>
<p>To get the padding for insert line right (if the terminal manufacturer did not document it) a severe test is to edit a large file at 9600 baud, delete 16 or so lines from the middle of the screen, then hit the ``u&#8217;&#8216; key several times quickly. If the terminal messes up, more padding is usually needed. A similar test can be used for insert character. </p>
<h3>Basic Capabilities</h3>
<p>The number of columns on each line for the terminal is given by the <code>cols</code> numeric capability. If the terminal is a CRT, then the number of lines on the screen is given by the <code>lines</code> capability. If the terminal wraps around to the beginning of the next line when it reaches the right margin, then it should have the <code>am</code> capability. If the terminal can clear its screen, leaving the cursor in the home position, then this is given by the <code>clear</code> string capability. If the terminal overstrikes (rather than clearing a position when a character is struck over) then it should have the <code>os</code> capability. If the terminal is a printing terminal, with no soft copy unit, give it both <code>hc</code> and <code>os</code>. (<code>os</code> applies to storage scope terminals, such as TEKTRONIX 4010 series, as well as hard copy and APL terminals.) If there is a code to move the cursor to the left edge of the current row, give this as <code>cr</code>. (Normally this will be carriage return, control/M.) If there is a code to produce an audible signal (bell, beep, etc) give this as <code>bel</code>. </p>
<p>If there is a code to move the cursor one position to the left (such as backspace) that capability should be given as <code>cub1</code>. Similarly, codes to move to the right, up, and down should be given as <code>cuf1</code>, <code>cuu1</code>, and <code>cud1</code>. These local cursor motions should not alter the text they pass over, for example, you would not normally use ``<code>cuf1</code>=&nbsp;&#8216;&#8216; because the space would erase the character moved over. </p>
<p>A very important point here is that the local cursor motions encoded in <i>terminfo</i> are undefined at the left and top edges of a CRT terminal. Programs should never attempt to backspace around the left edge, unless <code>bw</code> is given, and never attempt to go up locally off the top. In order to scroll text up, a program will go to the bottom left corner of the screen and send the <code>ind</code> (index) string. </p>
<p>To scroll text down, a program goes to the top left corner of the screen and sends the <code>ri</code> (reverse index) string. The strings <code>ind</code> and <code>ri</code> are undefined when not on their respective corners of the screen. </p>
<p>Parameterized versions of the scrolling sequences are <code>indn</code> and <code>rin</code> which have the same semantics as <code>ind</code> and <code>ri</code> except that they take one parameter, and scroll that many lines. They are also undefined except at the appropriate edge of the screen. </p>
<p>The <code>am</code> capability tells whether the cursor sticks at the right edge of the screen when text is output, but this does not necessarily apply to a <code>cuf1</code> from the last column. The only local motion which is defined from the left edge is if <code>bw</code> is given, then a <code>cub1</code> from the left edge will move to the right edge of the previous row. If <code>bw</code> is not given, the effect is undefined. This is useful for drawing a box around the edge of the screen, for example. If the terminal has switch selectable automatic margins, the <i>terminfo</i> file usually assumes that this is on; i.e., <code>am</code>. If the terminal has a command which moves to the first column of the next line, that command can be given as <code>nel</code> (newline). It does not matter if the command clears the remainder of the current line, so if the terminal has no <code>cr</code> and <code>lf</code> it may still be possible to craft a working <code>nel</code> out of one or both of them. </p>
<p>These capabilities suffice to describe hard-copy and ``glass-tty&#8217;&#8216; terminals. Thus the model 33 teletype is described as </p>
<pre><code>
33|tty33|tty|model 33 teletype,
        bel=^G, cols#72, cr=^M, cud1=^J, hc, ind=^J, os,
</code></pre>
<p>while the Lear Siegler ADM-3 is described as </p>
<pre><code>
adm3|3|lsi adm3,
        am, bel=^G, clear=^Z, cols#80, cr=^M, cub1=^H, cud1=^J,
        ind=^J, lines#24,
</code></pre>
<h3>Parameterized Strings</h3>
<p>Cursor addressing and other strings requiring parameters in the terminal are described by a parameterized string capability, with <i>printf</i>-like escapes such as <i>%x</i> in it. For example, to address the cursor, the <code>cup</code> capability is given, using two parameters: the row and column to address to. (Rows and columns are numbered from zero and refer to the physical screen visible to the user, not to any unseen memory.) If the terminal has memory relative cursor addressing, that can be indicated by <code>mrcup</code>. </p>
<p>The parameter mechanism uses a stack and special <code>%</code> codes to manipulate it. Typically a sequence will push one of the parameters onto the stack and then print it in some format. Print (e.g., ``%d&#8217;&#8216;) is a special case. Other operations, including ``%t&#8217;&#8216; pop their operand from the stack. It is noted that more complex operations are often necessary, e.g., in the <code>sgr</code> string. </p>
<p>The <code>%</code> encodings have the following meanings: </p>
<dl>
<dt><code>%%</code></dt>
<dd> <p> outputs ``%&#8216;&#8216; </p>
 </dd>
<dt><code>%</code><i>[[</i>:<i>]flags][width[.precision]][</i><code>doxXs</code><i>]</i></dt>
<dd> <p> as in <code><a href="/docs/linux/man/3-printf/">printf</a></code>(3), flags are <i>[-+#]</i> and <i>space</i>. Use a ``:&#8216;&#8216; to allow the next character to be a ``-&#8216;&#8216; flag, avoiding interpreting ``%-&#8216;&#8216; as an operator. </p>
 </dd>
<dt><code>%c</code></dt>
<dd> <p> print <i>pop()</i> like %c in <code>printf</code> </p>
 </dd>
<dt><code>%s</code></dt>
<dd> <p> print <i>pop()</i> like %s in <code>printf</code> </p>
 </dd>
<dt><code>%p</code><i>[1-9]</i></dt>
<dd> <p> push <i>i</i>&#8216;th parameter </p>
 </dd>
<dt><code>%P</code><i>[a-z]</i></dt>
<dd> <p> set dynamic variable <i>[a-z]</i> to <i>pop()</i> </p>
 </dd>
<dt><code>%g</code><i>[a-z]/</i></dt>
<dd> <p> get dynamic variable <i>[a-z]</i> and push it </p>
 </dd>
<dt><code>%P</code><i>[A-Z]</i></dt>
<dd> <p> set static variable <i>[a-z]</i> to <i>pop()</i> </p>
 </dd>
<dt><code>%g</code><i>[A-Z]</i></dt>
<dd> <p> get static variable <i>[a-z]</i> and push it </p>
 </dd>
<dd> <p> The terms ``static&#8217;&#8216; and ``dynamic&#8217;&#8216; are misleading. Historically, these are simply two different sets of variables, whose values are not reset between calls to <code>tparm</code>(3X). However, that fact is not documented in other implementations. Relying on it will adversely impact portability to other implementations: </p>
 </dd>
<dl>
<dd> <p> <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 SVr2 curses supported <i>dynamic</i> variables. Those are set only by a <code>%P</code> operator. A <code>%g</code> for a given variable without first setting it with <code>%P</code> will give unpredictable results, because dynamic variables are an uninitialized local array on the stack in the <code>tparm</code> function. <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 SVr3.2 curses supported <i>static</i> variables. Those are an array in the <code>TERMINAL</code> structure (declared in <code>term.h</code>), and are zeroed automatically when the <code>setupterm</code> function allocates the data. <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 SVr4 curses made no further improvements to the <i>dynamic/static</i> variable feature. <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 Solaris XPG4 curses does not distinguish between <i>dynamic</i> and <i>static</i> variables. They are the same. Like SVr4 curses, XPG4 curses does not initialize these explicitly. <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 Before version 6.3, ncurses stores both <i>dynamic</i> and <i>static</i> variables in persistent storage, initialized to zeros. <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 Beginning with version 6.3, ncurses stores <i>static</i> and <i>dynamic</i> variables in the same manner as SVr4. Unlike other implementations, ncurses zeros dynamic variables before the first <code>%g</code> or <code>%P</code> operator. </p>
 </dd></dl>
<dt><code>%&#8216;</code><i>c</i><code>&#8216;</code></dt>
<dd> <p> char constant <i>c</i> </p>
 </dd>
<dt><code>%{</code><i>nn</i><code>}</code></dt>
<dd> <p> integer constant <i>nn</i> </p>
 </dd>
<dt><code>%l</code></dt>
<dd> <p> push strlen(pop) </p>
 </dd>
<dt><code>%+</code>, <code>%-</code>, <code>%*</code>, <code>%/</code>, <code>%m</code></dt>
<dd> <p> arithmetic (%m is <i>mod</i>): <i>push(pop() op pop())</i> </p>
 </dd>
<dt><code>%&amp;</code>, <code>%|</code>, <code>%^</code></dt>
<dd> <p> bit operations (AND, OR and exclusive-OR): <i>push(pop() op pop())</i> </p>
 </dd>
<dt><code>%=</code>, <code>%&gt;</code>, <code>%&lt;</code></dt>
<dd> <p> logical operations: <i>push(pop() op pop())</i> </p>
 </dd>
<dt><code>%A</code>, <code>%O</code></dt>
<dd> <p> logical AND and OR operations (for conditionals) </p>
 </dd>
<dt><code>%!</code>, <code>%~</code></dt>
<dd> <p> unary operations (logical and bit complement): <i>push(op pop())</i> </p>
 </dd>
<dt><code>%i</code></dt>
<dd> <p> add 1 to first two parameters (for ANSI terminals) </p>
 </dd>
<dt><code>%?</code><i>expr</i><code>%t</code><i>thenpart</i><code>%e</code><i>elsepart</i><code>%;</code></dt>
<dd> <p> This forms an if-then-else. The <code>%e</code> <i>elsepart</i> is optional. Usually the <code>%?</code> <i>expr</i> part pushes a value onto the stack, and <code>%t</code> pops it from the stack, testing if it is nonzero (true). If it is zero (false), control passes to the <code>%e</code> (else) part. </p>
 </dd>
<dd> <p> It is possible to form else-if&#8217;s a la Algol 68: </p>
 </dd>
<dl>
<dd> <p> <code>%?</code> c1 <code>%t</code> b1 <code>%e</code> c2 <code>%t</code> b2 <code>%e</code> c3 <code>%t</code> b3 <code>%e</code> c4 <code>%t</code> b4 <code>%e</code> <code>%;</code> </p>
 </dd></dl>
<dd> <p> where ci are conditions, bi are bodies. </p>
 </dd>
<dd> <p> Use the <code>-f</code> option of <code>tic</code> or <code>infocmp</code> to see the structure of if-then-else&#8217;s. Some strings, e.g., <code>sgr</code> can be very complicated when written on one line. The <code>-f</code> option splits the string into lines with the parts indented. </p>
 </dd></dl>
<p>Binary operations are in postfix form with the operands in the usual order. That is, to get x-5 one would use ``%gx%{5}%-&#8216;&#8216;. <code>%P</code> and <code>%g</code> variables are persistent across escape-string evaluations. </p>
<p>Consider the HP2645, which, to get to row 3 and column 12, needs to be sent \E&amp;a12c03Y padded for 6 milliseconds. Note that the order of the rows and columns is inverted here, and that the row and column are printed as two digits. Thus its <code>cup</code> capability is ``cup=6\E&amp;%p2%2dc%p1%2dY&#8217;&#8216;. </p>
<p>The Microterm ACT-IV needs the current row and column sent preceded by a <code>^T</code>, with the row and column simply encoded in binary, ``cup=^T%p1%c%p2%c&#8217;&#8216;. Terminals which use ``%c&#8217;&#8216; need to be able to backspace the cursor (<code>cub1</code>), and to move the cursor up one line on the screen (<code>cuu1</code>). This is necessary because it is not always safe to transmit <code>\n</code> <code>^D</code> and <code>\r</code>, as the system may change or discard them. (The library routines dealing with terminfo set tty modes so that tabs are never expanded, so \t is safe to send. This turns out to be essential for the Ann Arbor 4080.) </p>
<p>A final example is the LSI ADM-3a, which uses row and column offset by a blank character, thus ``cup=\E=%p1%&#8216; &#8216;%+%c%p2%&#8216; &#8216;%+%c&#8217;&#8216;. After sending ``\E=&#8216;&#8216;, this pushes the first parameter, pushes the ASCII value for a space (32), adds them (pushing the sum on the stack in place of the two previous values) and outputs that value as a character. Then the same is done for the second parameter. More complex arithmetic is possible using the stack. </p>
<h3>Cursor Motions</h3>
<p>If the terminal has a fast way to home the cursor (to very upper left corner of screen) then this can be given as <code>home</code>; similarly a fast way of getting to the lower left-hand corner can be given as <code>ll</code>; this may involve going up with <code>cuu1</code> from the home position, but a program should never do this itself (unless <code>ll</code> does) because it can make no assumption about the effect of moving up from the home position. Note that the home position is the same as addressing to (0,0): to the top left corner of the screen, not of memory. (Thus, the \EH sequence on HP terminals cannot be used for <code>home</code>.) </p>
<p>If the terminal has row or column absolute cursor addressing, these can be given as single parameter capabilities <code>hpa</code> (horizontal position absolute) and <code>vpa</code> (vertical position absolute). Sometimes these are shorter than the more general two parameter sequence (as with the hp2645) and can be used in preference to <code>cup</code>. If there are parameterized local motions (e.g., move <i>n</i> spaces to the right) these can be given as <code>cud</code>, <code>cub</code>, <code>cuf</code>, and <code>cuu</code> with a single parameter indicating how many spaces to move. These are primarily useful if the terminal does not have <code>cup</code>, such as the TEKTRONIX 4025. </p>
<p>If the terminal needs to be in a special mode when running a program that uses these capabilities, the codes to enter and exit this mode can be given as <code>smcup</code> and <code>rmcup</code>. This arises, for example, from terminals like the Concept with more than one page of memory. If the terminal has only memory relative cursor addressing and not screen relative cursor addressing, a one screen-sized window must be fixed into the terminal for cursor addressing to work properly. This is also used for the TEKTRONIX 4025, where <code>smcup</code> sets the command character to be the one used by terminfo. If the <code>smcup</code> sequence will not restore the screen after an <code>rmcup</code> sequence is output (to the state prior to outputting <code>rmcup</code>), specify <code>nrrmc</code>. </p>
<h3>Margins</h3>
<p> SVr4 (and X/Open Curses) list several string capabilities for setting margins. Two were intended for use with terminals, and another six were intended for use with printers. <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 The two terminal capabilities assume that the terminal may have the capability of setting the left and/or right margin at the current cursor column position. <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 The printer capabilities assume that the printer may have two types of capability: </p>
<dl>
<dd> <p> <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 the ability to set a top and/or bottom margin using the current line position, and <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 parameterized capabilities for setting the top, bottom, left, right margins given the number of rows or columns. </p>
 </dd></dl>
<p>In practice, the categorization into ``terminal&#8217;&#8216; and ``printer&#8217;&#8216; is not suitable: <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 The AT&amp;T SVr4 terminal database uses <code>smgl</code> four times, for AT&amp;T hardware. </p>
<dl>
<dd> <p> Three of the four are printers. They lack the ability to set left/right margins by specifying the column. <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 Other (non-AT&amp;T) terminals may support margins but using different assumptions from AT&amp;T. </p>
 </dd>
<dd> <p> For instance, the DEC VT420 supports left/right margins, but only using a column parameter. As an added complication, the VT420 uses two settings to fully enable left/right margins (left/right margin mode, and origin mode). The former enables the margins, which causes printed text to wrap within margins, but the latter is needed to prevent cursor-addressing outside those margins. <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 Both DEC VT420 left/right margins are set with a single control sequence. If either is omitted, the corresponding margin is set to the left or right edge of the display (rather than leaving the margin unmodified). </p>
 </dd></dl>
<p>These are the margin-related capabilities: <center> </p>
<table>
<tr VALIGN=top>
<td><code>Name</code></td>
<td>Description
</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td>smgr</td>
<td>Set right margin at current column
</td>
</tr>
<tr VALIGN=top>
<td>smgb</td>
<td>Set bottom margin at current line
</td>
</tr>
<tr VALIGN=top>
<td>smgt</td>
<td>Set top margin at current line
</td>
</tr>
<tr VALIGN=top>
<td>smgbp</td>
<td>Set bottom margin at line <i>N</i>
</td>
</tr>
<tr VALIGN=top>
<td>smglp</td>
<td>Set left margin at column <i>N</i>
</td>
</tr>
<tr VALIGN=top>
<td>smgrp</td>
<td>Set right margin at column <i>N</i>
</td>
</tr>
<tr VALIGN=top>
<td>smgtp</td>
<td>Set top margin at line <i>N</i>
</td>
</tr>
<tr VALIGN=top>
<td>smglr</td>
<td>Set both left and right margins to <i>L</i> and <i>R</i>
</td>
</tr>
<tr VALIGN=top>
<td>smgtb</td>
<td>Set both top and bottom margins to <i>T</i> and <i>B</i>
</td>
</tr>
</table>
<p> </center> </p>
<p>When writing an application that uses these string capabilities, the pairs should be first checked to see if each capability in the pair is set or only one is set: <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 If both <code>smglp</code> and <code>smgrp</code> are set, each is used with a single argument, <i>N</i>, that gives the column number of the left and right margin, respectively. <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 If both <code>smgtp</code> and <code>smgbp</code> are set, each is used to set the top and bottom margin, respectively: </p>
<dl>
<dd> <p> <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 <code>smgtp</code> is used with a single argument, <i>N</i>, the line number of the top margin. <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 <code>smgbp</code> is used with two arguments, <i>N</i> and <i>M</i>, that give the line number of the bottom margin, the first counting from the top of the page and the second counting from the bottom. This accommodates the two styles of specifying the bottom margin in different manufacturers&#8217; printers. </p>
 </dd></dl>
<dl>
<dd> <p> When designing a terminfo entry for a printer that has a settable bottom margin, only the first or second argument should be used, depending on the printer. When developing an application that uses <code>smgbp</code> to set the bottom margin, both arguments must be given. </p>
 </dd></dl>
<p>Conversely, when only one capability in the pair is set: <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 If only one of <code>smglp</code> and <code>smgrp</code> is set, then it is used with two arguments, the column number of the left and right margins, in that order. <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 Likewise, if only one of <code>smgtp</code> and <code>smgbp</code> is set, then it is used with two arguments that give the top and bottom margins, in that order, counting from the top of the page. </p>
<dl>
<dd> <p> When designing a terminfo entry for a printer that requires setting both left and right or top and bottom margins simultaneously, only one capability in the pairs <code>smglp</code> and <code>smgrp</code> or <code>smgtp</code> and <code>smgbp</code> should be defined, leaving the other unset. </p>
 </dd></dl>
<p>Except for very old terminal descriptions, e.g., those developed for SVr4, the scheme just described should be considered obsolete. An improved set of capabilities was added late in the SVr4 releases (<code>smglr</code> and <code>smgtb</code>), which explicitly use two parameters for setting the left/right or top/bottom margins. </p>
<p>When setting margins, the line- and column-values are zero-based. </p>
<p>The <code>mgc</code> string capability should be defined. Applications such as <code><a href="/docs/linux/man/1-tabs/">tabs</a></code>(1) rely upon this to reset all margins.  </p>
<h3>Area Clears</h3>
<p>If the terminal can clear from the current position to the end of the line, leaving the cursor where it is, this should be given as <code>el</code>. If the terminal can clear from the beginning of the line to the current position inclusive, leaving the cursor where it is, this should be given as <code>el1</code>. If the terminal can clear from the current position to the end of the display, then this should be given as <code>ed</code>. <code>Ed</code> is only defined from the first column of a line. (Thus, it can be simulated by a request to delete a large number of lines, if a true <code>ed</code> is not available.) </p>
<h3>Insert/delete line and vertical motions</h3>
<p>If the terminal can open a new blank line before the line where the cursor is, this should be given as <code>il1</code>; this is done only from the first position of a line. The cursor must then appear on the newly blank line. If the terminal can delete the line which the cursor is on, then this should be given as <code>dl1</code>; this is done only from the first position on the line to be deleted. Versions of <code>il1</code> and <code>dl1</code> which take a single parameter and insert or delete that many lines can be given as <code>il</code> and <code>dl</code>. </p>
<p>If the terminal has a settable scrolling region (like the vt100) the command to set this can be described with the <code>csr</code> capability, which takes two parameters: the top and bottom lines of the scrolling region. The cursor position is, alas, undefined after using this command. </p>
<p>It is possible to get the effect of insert or delete line using <code>csr</code> on a properly chosen region; the <code>sc</code> and <code>rc</code> (save and restore cursor) commands may be useful for ensuring that your synthesized insert/delete string does not move the cursor. (Note that the <code>ncurses</code>(3NCURSES) library does this synthesis automatically, so you need not compose insert/delete strings for an entry with <code>csr</code>). </p>
<p>Yet another way to construct insert and delete might be to use a combination of index with the memory-lock feature found on some terminals (like the HP-700/90 series, which however also has insert/delete). </p>
<p>Inserting lines at the top or bottom of the screen can also be done using <code>ri</code> or <code>ind</code> on many terminals without a true insert/delete line, and is often faster even on terminals with those features. </p>
<p>The boolean <code>non_dest_scroll_region</code> should be set if each scrolling window is effectively a view port on a screen-sized canvas. To test for this capability, create a scrolling region in the middle of the screen, write something to the bottom line, move the cursor to the top of the region, and do <code>ri</code> followed by <code>dl1</code> or <code>ind</code>. If the data scrolled off the bottom of the region by the <code>ri</code> re-appears, then scrolling is non-destructive. System V and XSI Curses expect that <code>ind</code>, <code>ri</code>, <code>indn</code>, and <code>rin</code> will simulate destructive scrolling; their documentation cautions you not to define <code>csr</code> unless this is true. This <code>curses</code> implementation is more liberal and will do explicit erases after scrolling if <code>ndsrc</code> is defined. </p>
<p>If the terminal has the ability to define a window as part of memory, which all commands affect, it should be given as the parameterized string <code>wind</code>. The four parameters are the starting and ending lines in memory and the starting and ending columns in memory, in that order. </p>
<p>If the terminal can retain display memory above, then the <code>da</code> capability should be given; if display memory can be retained below, then <code>db</code> should be given. These indicate that deleting a line or scrolling may bring non-blank lines up from below or that scrolling back with <code>ri</code> may bring down non-blank lines. </p>
<h3>Insert/Delete Character</h3>
<p>There are two basic kinds of intelligent terminals with respect to insert/delete character which can be described using <i>terminfo.</i> The most common insert/delete character operations affect only the characters on the current line and shift characters off the end of the line rigidly. Other terminals, such as the Concept 100 and the Perkin Elmer Owl, make a distinction between typed and untyped blanks on the screen, shifting upon an insert or delete only to an untyped blank on the screen which is either eliminated, or expanded to two untyped blanks. </p>
<p>You can determine the kind of terminal you have by clearing the screen and then typing text separated by cursor motions. Type ``abc&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;def&#8217;&#8216; using local cursor motions (not spaces) between the ``abc&#8217;&#8216; and the ``def&#8217;&#8216;. Then position the cursor before the ``abc&#8217;&#8216; and put the terminal in insert mode. If typing characters causes the rest of the line to shift rigidly and characters to fall off the end, then your terminal does not distinguish between blanks and untyped positions. If the ``abc&#8217;&#8216; shifts over to the ``def&#8217;&#8216; which then move together around the end of the current line and onto the next as you insert, you have the second type of terminal, and should give the capability <code>in</code>, which stands for ``insert null&#8217;&#8216;. </p>
<p>While these are two logically separate attributes (one line versus multi-line insert mode, and special treatment of untyped spaces) we have seen no terminals whose insert mode cannot be described with the single attribute. </p>
<p>Terminfo can describe both terminals which have an insert mode, and terminals which send a simple sequence to open a blank position on the current line. Give as <code>smir</code> the sequence to get into insert mode. Give as <code>rmir</code> the sequence to leave insert mode. Now give as <code>ich1</code> any sequence needed to be sent just before sending the character to be inserted. Most terminals with a true insert mode will not give <code>ich1</code>; terminals which send a sequence to open a screen position should give it here. </p>
<p>If your terminal has both, insert mode is usually preferable to <code>ich1</code>. Technically, you should not give both unless the terminal actually requires both to be used in combination. Accordingly, some non-curses applications get confused if both are present; the symptom is doubled characters in an update using insert. This requirement is now rare; most <code>ich</code> sequences do not require previous smir, and most smir insert modes do not require <code>ich1</code> before each character. Therefore, the new <code>curses</code> actually assumes this is the case and uses either <code>rmir</code>/<code>smir</code> or <code>ich</code>/<code>ich1</code> as appropriate (but not both). If you have to write an entry to be used under new curses for a terminal old enough to need both, include the <code>rmir</code>/<code>smir</code> sequences in <code>ich1</code>. </p>
<p>If post insert padding is needed, give this as a number of milliseconds in <code>ip</code> (a string option). Any other sequence which may need to be sent after an insert of a single character may also be given in <code>ip</code>. If your terminal needs both to be placed into an ``insert mode&#8217;&#8216; and a special code to precede each inserted character, then both <code>smir</code>/<code>rmir</code> and <code>ich1</code> can be given, and both will be used. The <code>ich</code> capability, with one parameter, <i>n</i>, will repeat the effects of <code>ich1</code> <i>n</i> times. </p>
<p>If padding is necessary between characters typed while not in insert mode, give this as a number of milliseconds padding in <code>rmp</code>. </p>
<p>It is occasionally necessary to move around while in insert mode to delete characters on the same line (e.g., if there is a tab after the insertion position). If your terminal allows motion while in insert mode you can give the capability <code>mir</code> to speed up inserting in this case. Omitting <code>mir</code> will affect only speed. Some terminals (notably Datamedia&#8217;s) must not have <code>mir</code> because of the way their insert mode works. </p>
<p>Finally, you can specify <code>dch1</code> to delete a single character, <code>dch</code> with one parameter, <i>n</i>, to delete <i>n characters,</i> and delete mode by giving <code>smdc</code> and <code>rmdc</code> to enter and exit delete mode (any mode the terminal needs to be placed in for <code>dch1</code> to work). </p>
<p>A command to erase <i>n</i> characters (equivalent to outputting <i>n</i> blanks without moving the cursor) can be given as <code>ech</code> with one parameter. </p>
<h3>Highlighting, Underlining, and Visible Bells</h3>
<p>If your terminal has one or more kinds of display attributes, these can be represented in a number of different ways. You should choose one display form as <i>standout mode</i>, representing a good, high contrast, easy-on-the-eyes, format for highlighting error messages and other attention getters. (If you have a choice, reverse video plus half-bright is good, or reverse video alone.) The sequences to enter and exit standout mode are given as <code>smso</code> and <code>rmso</code>, respectively. If the code to change into or out of standout mode leaves one or even two blank spaces on the screen, as the TVI 912 and Teleray 1061 do, then <code>xmc</code> should be given to tell how many spaces are left. </p>
<p>Codes to begin underlining and end underlining can be given as <code>smul</code> and <code>rmul</code> respectively. If the terminal has a code to underline the current character and move the cursor one space to the right, such as the Microterm Mime, this can be given as <code>uc</code>. </p>
<p>Other capabilities to enter various highlighting modes include <code>blink</code> (blinking) <code>bold</code> (bold or extra bright) <code>dim</code> (dim or half-bright) <code>invis</code> (blanking or invisible text) <code>prot</code> (protected) <code>rev</code> (reverse video) <code>sgr0</code> (turn off <i>all</i> attribute modes) <code>smacs</code> (enter alternate character set mode) and <code>rmacs</code> (exit alternate character set mode). Turning on any of these modes singly may or may not turn off other modes. </p>
<p>If there is a sequence to set arbitrary combinations of modes, this should be given as <code>sgr</code> (set attributes), taking 9 parameters. Each parameter is either 0 or nonzero, as the corresponding attribute is on or off. The 9 parameters are, in order: standout, underline, reverse, blink, dim, bold, blank, protect, alternate character set. Not all modes need be supported by <code>sgr</code>, only those for which corresponding separate attribute commands exist. </p>
<p>For example, the DEC vt220 supports most of the modes: </p>
<p> <center> </p>
<table>
<tr VALIGN=top>
<td><code>tparm parameter</code></td>
<td>attribute</td>
<td>escape sequence
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>none</td>
<td>none</td>
<td>\E[0m
</td>
</tr>
<tr VALIGN=top>
<td>p1</td>
<td>standout</td>
<td>\E[0;1;7m
</td>
</tr>
<tr VALIGN=top>
<td>p2</td>
<td>underline</td>
<td>\E[0;4m
</td>
</tr>
<tr VALIGN=top>
<td>p3</td>
<td>reverse</td>
<td>\E[0;7m
</td>
</tr>
<tr VALIGN=top>
<td>p4</td>
<td>blink</td>
<td>\E[0;5m
</td>
</tr>
<tr VALIGN=top>
<td>p5</td>
<td>dim</td>
<td>not available
</td>
</tr>
<tr VALIGN=top>
<td>p6</td>
<td>bold</td>
<td>\E[0;1m
</td>
</tr>
<tr VALIGN=top>
<td>p7</td>
<td>invis</td>
<td>\E[0;8m
</td>
</tr>
<tr VALIGN=top>
<td>p8</td>
<td>protect</td>
<td>not used
</td>
</tr>
<tr VALIGN=top>
<td>p9</td>
<td>altcharset</td>
<td>^O (off) ^N (on)
</td>
</tr>
</table>
<p> </center> </p>
<p>We begin each escape sequence by turning off any existing modes, since there is no quick way to determine whether they are active. Standout is set up to be the combination of reverse and bold. The vt220 terminal has a protect mode, though it is not commonly used in sgr because it protects characters on the screen from the host&#8217;s erasures. The altcharset mode also is different in that it is either ^O or ^N, depending on whether it is off or on. If all modes are turned on, the resulting sequence is \E[0;1;4;5;7;8m^N. </p>
<p>Some sequences are common to different modes. For example, ;7 is output when either p1 or p3 is true, that is, if either standout or reverse modes are turned on. </p>
<p>Writing out the above sequences, along with their dependencies yields </p>
<p> <center> </p>
<table>
<tr VALIGN=top>
<td><code>sequence</code></td>
<td>when to output</td>
<td>terminfo translation
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>\E[0</td>
<td>always</td>
<td>\E[0
</td>
</tr>
<tr VALIGN=top>
<td>;1</td>
<td>if p1 or p6</td>
<td>%?%p1%p6%|%t;1%;
</td>
</tr>
<tr VALIGN=top>
<td>;4</td>
<td>if p2</td>
<td>%?%p2%|%t;4%;
</td>
</tr>
<tr VALIGN=top>
<td>;5</td>
<td>if p4</td>
<td>%?%p4%|%t;5%;
</td>
</tr>
<tr VALIGN=top>
<td>;7</td>
<td>if p1 or p3</td>
<td>%?%p1%p3%|%t;7%;
</td>
</tr>
<tr VALIGN=top>
<td>;8</td>
<td>if p7</td>
<td>%?%p7%|%t;8%;
</td>
</tr>
<tr VALIGN=top>
<td>m</td>
<td>always</td>
<td>m
</td>
</tr>
<tr VALIGN=top>
<td>^N or ^O</td>
<td>if p9 ^N, else ^O</td>
<td>%?%p9%t^N%e^O%;
</td>
</tr>
</table>
<p> </center> </p>
<p>Putting this all together into the sgr sequence gives: </p>
<pre><code>    sgr=\E[0%?%p1%p6%|%t;1%;%?%p2%t;4%;%?%p4%t;5%;
        %?%p1%p3%|%t;7%;%?%p7%t;8%;m%?%p9%t\016%e\017%;,
</code></pre>
<p>Remember that if you specify sgr, you must also specify sgr0. Also, some implementations rely on sgr being given if sgr0 is, Not all terminfo entries necessarily have an sgr string, however. Many terminfo entries are derived from termcap entries which have no sgr string. The only drawback to adding an sgr string is that termcap also assumes that sgr0 does not exit alternate character set mode. </p>
<p>Terminals with the ``magic cookie&#8217;&#8216; glitch (<code>xmc</code>) deposit special ``cookies&#8217;&#8216; when they receive mode-setting sequences, which affect the display algorithm rather than having extra bits for each character. Some terminals, such as the HP 2621, automatically leave standout mode when they move to a new line or the cursor is addressed. Programs using standout mode should exit standout mode before moving the cursor or sending a newline, unless the <code>msgr</code> capability, asserting that it is safe to move in standout mode, is present. </p>
<p>If the terminal has a way of flashing the screen to indicate an error quietly (a bell replacement) then this can be given as <code>flash</code>; it must not move the cursor. </p>
<p>If the cursor needs to be made more visible than normal when it is not on the bottom line (to make, for example, a non-blinking underline into an easier to find block or blinking underline) give this sequence as <code>cvvis</code>. If there is a way to make the cursor completely invisible, give that as <code>civis</code>. The capability <code>cnorm</code> should be given which undoes the effects of both of these modes. </p>
<p>If your terminal correctly generates underlined characters (with no special codes needed) even though it does not overstrike, then you should give the capability <code>ul</code>. If a character overstriking another leaves both characters on the screen, specify the capability <code>os</code>. If overstrikes are erasable with a blank, then this should be indicated by giving <code>eo</code>. </p>
<h3>Keypad and Function Keys</h3>
<p>If the terminal has a keypad that transmits codes when the keys are pressed, this information can be given. Note that it is not possible to handle terminals where the keypad only works in local (this applies, for example, to the unshifted HP 2621 keys). If the keypad can be set to transmit or not transmit, give these codes as <code>smkx</code> and <code>rmkx</code>. Otherwise the keypad is assumed to always transmit. </p>
<p>The codes sent by the left arrow, right arrow, up arrow, down arrow, and home keys can be given as <code>kcub1, kcuf1, kcuu1, kcud1, </code>and <code> khome</code> respectively. If there are function keys such as f0, f1, ..., f10, the codes they send can be given as <code>kf0, kf1, ..., kf10</code>. If these keys have labels other than the default f0 through f10, the labels can be given as <code>lf0, lf1, ..., lf10</code>. </p>
<p>The codes transmitted by certain other special keys can be given: <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 <code>kll</code> (home down), <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 <code>kbs</code> (backspace), <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 <code>ktbc</code> (clear all tabs), <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 <code>kctab</code> (clear the tab stop in this column), <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 <code>kclr</code> (clear screen or erase key), <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 <code>kdch1</code> (delete character), <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 <code>kdl1</code> (delete line), <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 <code>krmir</code> (exit insert mode), <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 <code>kel</code> (clear to end of line), <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 <code>ked</code> (clear to end of screen), <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 <code>kich1</code> (insert character or enter insert mode), <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 <code>kil1</code> (insert line), <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 <code>knp</code> (next page), <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 <code>kpp</code> (previous page), <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 <code>kind</code> (scroll forward/down), <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 <code>kri</code> (scroll backward/up), <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 <code>khts</code> (set a tab stop in this column). </p>
<p>In addition, if the keypad has a 3 by 3 array of keys including the four arrow keys, the other five keys can be given as <code>ka1</code>, <code>ka3</code>, <code>kb2</code>, <code>kc1</code>, and <code>kc3</code>. These keys are useful when the effects of a 3 by 3 directional pad are needed. </p>
<p>Strings to program function keys can be given as <code>pfkey</code>, <code>pfloc</code>, and <code>pfx</code>. A string to program screen labels should be specified as <code>pln</code>. Each of these strings takes two parameters: the function key number to program (from 0 to 10) and the string to program it with. Function key numbers out of this range may program undefined keys in a terminal dependent manner. The difference between the capabilities is that <code>pfkey</code> causes pressing the given key to be the same as the user typing the given string; <code>pfloc</code> causes the string to be executed by the terminal in local; and <code>pfx</code> causes the string to be transmitted to the computer. </p>
<p>The capabilities <code>nlab</code>, <code>lw</code> and <code>lh</code> define the number of programmable screen labels and their width and height. If there are commands to turn the labels on and off, give them in <code>smln</code> and <code>rmln</code>. <code>smln</code> is normally output after one or more pln sequences to make sure that the change becomes visible. </p>
<h3>Tabs and Initialization</h3>
<p>A few capabilities are used only for tabs: <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 If the terminal has hardware tabs, the command to advance to the next tab stop can be given as <code>ht</code> (usually control/I). <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 A ``back-tab&#8217;&#8216; command which moves leftward to the preceding tab stop can be given as <code>cbt</code>. </p>
<dl>
<dd> <p> By convention, if the teletype modes indicate that tabs are being expanded by the computer rather than being sent to the terminal, programs should not use <code>ht</code> or <code>cbt</code> even if they are present, since the user may not have the tab stops properly set. <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 If the terminal has hardware tabs which are initially set every <i>n</i> spaces when the terminal is powered up, the numeric parameter <code>it</code> is given, showing the number of spaces the tabs are set to. </p>
 </dd>
<dd> <p> The <code>it</code> capability is normally used by the <code>tset</code> command to determine whether to set the mode for hardware tab expansion, and whether to set the tab stops. If the terminal has tab stops that can be saved in non-volatile memory, the terminfo description can assume that they are properly set. </p>
 </dd></dl>
<p>Other capabilities include <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 <code>is1</code>, <code>is2</code>, and <code>is3</code>, initialization strings for the terminal, <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 <code>iprog</code>, the path name of a program to be run to initialize the terminal, <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 and <code>if</code>, the name of a file containing long initialization strings. </p>
<p>These strings are expected to set the terminal into modes consistent with the rest of the terminfo description. They are normally sent to the terminal, by the <i>init</i> option of the <code>tput</code> program, each time the user logs in. They will be printed in the following order: </p>
<dl>
<dd>  </dd>
<dl>
<dt>run the program</dt>
<dd> <p> <code>iprog</code> </p>
 </dd>
<dt>output</dt>
<dd> <p> <br/>
 <code>is1</code> and <br/>
 <code>is2</code> </p>
 </dd>
<dt>set the margins using</dt>
<dd> <p> <code>mgc</code> or <br/>
 <code>smglp</code> and <code>smgrp</code> or <br/>
 <code>smgl</code> and <code>smgr</code> </p>
 </dd>
<dt>set tabs using</dt>
<dd> <p> <code>tbc</code> and <code>hts</code> </p>
 </dd>
<dt>print the file</dt>
<dd> <p> <code>if</code> </p>
 </dd>
<dt>and finally output</dt>
<dd> <p> <code>is3</code>. </p>
 </dd></dl>
</dl>
<p>Most initialization is done with <code>is2</code>. Special terminal modes can be set up without duplicating strings by putting the common sequences in <code>is2</code> and special cases in <code>is1</code> and <code>is3</code>. </p>
<p>A set of sequences that does a harder reset from a totally unknown state can be given as <code>rs1</code>, <code>rs2</code>, <code>rf</code> and <code>rs3</code>, analogous to <code>is1 ,</code> <code>is2 ,</code> <code>if</code> and <code>is3</code> respectively. These strings are output by <i>reset</i> option of <code>tput</code>, or by the <code>reset</code> program (an alias of <code>tset</code>), which is used when the terminal gets into a wedged state. Commands are normally placed in <code>rs1</code>, <code>rs2</code> <code>rs3</code> and <code>rf</code> only if they produce annoying effects on the screen and are not necessary when logging in. For example, the command to set the vt100 into 80-column mode would normally be part of <code>is2</code>, but it causes an annoying glitch of the screen and is not normally needed since the terminal is usually already in 80-column mode. </p>
<p>The <code>reset</code> program writes strings including <code>iprog</code>, etc., in the same order as the <i>init</i> program, using <code>rs1</code>, etc., instead of <code>is1</code>, etc. If any of <code>rs1</code>, <code>rs2</code>, <code>rs3</code>, or <code>rf</code> reset capability strings are missing, the <code>reset</code> program falls back upon the corresponding initialization capability string. </p>
<p>If there are commands to set and clear tab stops, they can be given as <code>tbc</code> (clear all tab stops) and <code>hts</code> (set a tab stop in the current column of every row). If a more complex sequence is needed to set the tabs than can be described by this, the sequence can be placed in <code>is2</code> or <code>if</code>. </p>
<p>The <code>tput reset</code> command uses the same capability strings as the <code>reset</code> command, although the two programs (<code>tput</code> and <code>reset</code>) provide different command-line options. </p>
<p>In practice, these terminfo capabilities are not often used in initialization of tabs (though they are required for the <code>tabs</code> program): <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 Almost all hardware terminals (at least those which supported tabs) initialized those to every <i>eight</i> columns: </p>
<dl>
<dd> <p> The only exception was the AT&amp;T 2300 series, which set tabs to every <i>five</i> columns. <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 In particular, developers of the hardware terminals which are commonly used as models for modern terminal emulators provided documentation demonstrating that <i>eight</i> columns were the standard. <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 Because of this, the terminal initialization programs <code>tput</code> and <code>tset</code> use the <code>tbc</code> (<code>clear_all_tabs</code>) and <code>hts</code> (<code>set_tab</code>) capabilities directly only when the <code>it</code> (<code>init_tabs</code>) capability is set to a value other than <i>eight</i>. </p>
 </dd></dl>
<h3>Delays and Padding</h3>
<p>Many older and slower terminals do not support either XON/XOFF or DTR handshaking, including hard copy terminals and some very archaic CRTs (including, for example, DEC VT100s). These may require padding characters after certain cursor motions and screen changes. </p>
<p>If the terminal uses xon/xoff handshaking for flow control (that is, it automatically emits ^S back to the host when its input buffers are close to full), set <code>xon</code>. This capability suppresses the emission of padding. You can also set it for memory-mapped console devices effectively that do not have a speed limit. Padding information should still be included so that routines can make better decisions about relative costs, but actual pad characters will not be transmitted. </p>
<p>If <code>pb</code> (padding baud rate) is given, padding is suppressed at baud rates below the value of <code>pb</code>. If the entry has no padding baud rate, then whether padding is emitted or not is completely controlled by <code>xon</code>. </p>
<p>If the terminal requires other than a null (zero) character as a pad, then this can be given as <code>pad</code>. Only the first character of the <code>pad</code> string is used. </p>
<h3>Status Lines</h3>
<p> Some terminals have an extra ``status line&#8217;&#8216; which is not normally used by software (and thus not counted in the terminal&#8217;s <code>lines</code> capability). </p>
<p>The simplest case is a status line which is cursor-addressable but not part of the main scrolling region on the screen; the Heathkit H19 has a status line of this kind, as would a 24-line VT100 with a 23-line scrolling region set up on initialization. This situation is indicated by the <code>hs</code> capability. </p>
<p>Some terminals with status lines need special sequences to access the status line. These may be expressed as a string with single parameter <code>tsl</code> which takes the cursor to a given zero-origin column on the status line. The capability <code>fsl</code> must return to the main-screen cursor positions before the last <code>tsl</code>. You may need to embed the string values of <code>sc</code> (save cursor) and <code>rc</code> (restore cursor) in <code>tsl</code> and <code>fsl</code> to accomplish this. </p>
<p>The status line is normally assumed to be the same width as the width of the terminal. If this is untrue, you can specify it with the numeric capability <code>wsl</code>. </p>
<p>A command to erase or blank the status line may be specified as <code>dsl</code>. </p>
<p>The boolean capability <code>eslok</code> specifies that escape sequences, tabs, etc., work ordinarily in the status line. </p>
<p>The <code>ncurses</code> implementation does not yet use any of these capabilities. They are documented here in case they ever become important. </p>
<h3>Line Graphics</h3>
<p>Many terminals have alternate character sets useful for forms-drawing. Terminfo and <code>curses</code> have built-in support for most of the drawing characters supported by the VT100, with some characters from the AT&amp;T 4410v1 added. This alternate character set may be specified by the <code>acsc</code> capability. </p>
<p> <center> </p>
<table>
<tr VALIGN=top>
<td><code>Glyph</code></td>
<td>ACS</td>
<td>Ascii</td>
<td>acsc</td>
<td>acsc
</td>
</tr>
<tr VALIGN=top>
<td><code>Name</code></td>
<td>Name</td>
<td>Default</td>
<td>Char</td>
<td>Value
</td>
</tr>
<tr VALIGN=top>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
<td><hr />
</td>
</tr>
<tr VALIGN=top>
<td>arrow pointing left</td>
<td>ACS_LARROW</td>
<td>&lt;</td>
<td>,</td>
<td>0x2c
</td>
</tr>
<tr VALIGN=top>
<td>arrow pointing up</td>
<td>ACS_UARROW</td>
<td>^</td>
<td>-</td>
<td>0x2d
</td>
</tr>
<tr VALIGN=top>
<td>arrow pointing down</td>
<td>ACS_DARROW</td>
<td>v</td>
<td>.</td>
<td>0x2e
</td>
</tr>
<tr VALIGN=top>
<td>solid square block</td>
<td>ACS_BLOCK</td>
<td>#</td>
<td>0</td>
<td>0x30
</td>
</tr>
<tr VALIGN=top>
<td>diamond </td>
<td>ACS_DIAMOND</td>
<td>+</td>
<td>`</td>
<td>0x60
</td>
</tr>
<tr VALIGN=top>
<td>checker board (stipple)</td>
<td>ACS_CKBOARD</td>
<td>:</td>
<td>a</td>
<td>0x61
</td>
</tr>
<tr VALIGN=top>
<td>degree symbol </td>
<td>ACS_DEGREE</td>
<td>\</td>
<td>f</td>
<td>0x66
</td>
</tr>
<tr VALIGN=top>
<td>plus/minus </td>
<td>ACS_PLMINUS</td>
<td>#</td>
<td>g</td>
<td>0x67
</td>
</tr>
<tr VALIGN=top>
<td>board of squares</td>
<td>ACS_BOARD</td>
<td>#</td>
<td>h</td>
<td>0x68
</td>
</tr>
<tr VALIGN=top>
<td>lantern symbol </td>
<td>ACS_LANTERN</td>
<td>#</td>
<td>i</td>
<td>0x69
</td>
</tr>
<tr VALIGN=top>
<td>lower right corner</td>
<td>ACS_LRCORNER</td>
<td>+</td>
<td>j</td>
<td>0x6a
</td>
</tr>
<tr VALIGN=top>
<td>upper right corner</td>
<td>ACS_URCORNER</td>
<td>+</td>
<td>k</td>
<td>0x6b
</td>
</tr>
<tr VALIGN=top>
<td>upper left corner</td>
<td>ACS_ULCORNER</td>
<td>+</td>
<td>l</td>
<td>0x6c
</td>
</tr>
<tr VALIGN=top>
<td>lower left corner</td>
<td>ACS_LLCORNER</td>
<td>+</td>
<td>m</td>
<td>0x6d
</td>
</tr>
<tr VALIGN=top>
<td>large plus or crossover</td>
<td>ACS_PLUS</td>
<td>+</td>
<td>n</td>
<td>0x6e
</td>
</tr>
<tr VALIGN=top>
<td>scan line 1 </td>
<td>ACS_S1 </td>
<td>~</td>
<td>o</td>
<td>0x6f
</td>
</tr>
<tr VALIGN=top>
<td>scan line 3 </td>
<td>ACS_S3 </td>
<td>-</td>
<td>p</td>
<td>0x70
</td>
</tr>
<tr VALIGN=top>
<td>horizontal line </td>
<td>ACS_HLINE</td>
<td>-</td>
<td>q</td>
<td>0x71
</td>
</tr>
<tr VALIGN=top>
<td>scan line 7 </td>
<td>ACS_S7 </td>
<td>-</td>
<td>r</td>
<td>0x72
</td>
</tr>
<tr VALIGN=top>
<td>scan line 9 </td>
<td>ACS_S9 </td>
<td>_</td>
<td>s</td>
<td>0x73
</td>
</tr>
<tr VALIGN=top>
<td>tee pointing right</td>
<td>ACS_LTEE</td>
<td>+</td>
<td>t</td>
<td>0x74
</td>
</tr>
<tr VALIGN=top>
<td>tee pointing left</td>
<td>ACS_RTEE</td>
<td>+</td>
<td>u</td>
<td>0x75
</td>
</tr>
<tr VALIGN=top>
<td>tee pointing up </td>
<td>ACS_BTEE</td>
<td>+</td>
<td>v</td>
<td>0x76
</td>
</tr>
<tr VALIGN=top>
<td>tee pointing down</td>
<td>ACS_TTEE</td>
<td>+</td>
<td>w</td>
<td>0x77
</td>
</tr>
<tr VALIGN=top>
<td>vertical line </td>
<td>ACS_VLINE</td>
<td>|</td>
<td>x</td>
<td>0x78
</td>
</tr>
<tr VALIGN=top>
<td>less-than-or-equal-to</td>
<td>ACS_LEQUAL</td>
<td>&lt;</td>
<td>y</td>
<td>0x79
</td>
</tr>
<tr VALIGN=top>
<td>greater-than-or-equal-to</td>
<td>ACS_GEQUAL</td>
<td>&gt;</td>
<td>z</td>
<td>0x7a
</td>
</tr>
<tr VALIGN=top>
<td>greek pi </td>
<td>ACS_PI</td>
<td>*</td>
<td>{</td>
<td>0x7b
</td>
</tr>
<tr VALIGN=top>
<td>not-equal </td>
<td>ACS_NEQUAL</td>
<td>!</td>
<td>|</td>
<td>0x7c
</td>
</tr>
<tr VALIGN=top>
<td>UK pound sign </td>
<td>ACS_STERLING</td>
<td>f</td>
<td>}</td>
<td>0x7d
</td>
</tr>
<tr VALIGN=top>
<td>bullet </td>
<td>ACS_BULLET</td>
<td>o</td>
<td>~</td>
<td>0x7e
</td>
</tr>
</table>
<p> </center> </p>
<p>A few notes apply to the table itself: <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 X/Open Curses incorrectly states that the mapping for <i>lantern</i> is uppercase ``I&#8217;&#8216; although Unix implementations use the lowercase ``i&#8217;&#8216; mapping. <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 The DEC VT100 implemented graphics using the alternate character set feature, temporarily switching <i>modes</i> and sending characters in the range 0x60 (96) to 0x7e (126) (the <code>acsc Value</code> column in the table). <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 The AT&amp;T terminal added graphics characters outside that range. </p>
<dl>
<dd> <p> Some of the characters within the range do not match the VT100; presumably they were used in the AT&amp;T terminal: <i>board of squares</i> replaces the VT100 <i>newline</i> symbol, while <i>lantern symbol</i> replaces the VT100 <i>vertical tab</i> symbol. The other VT100 symbols for control characters (<i>horizontal tab</i>, <i>carriage return</i> and <i>line-feed</i>) are not (re)used in curses. </p>
 </dd></dl>
<p>The best way to define a new device&#8217;s graphics set is to add a column to a copy of this table for your terminal, giving the character which (when emitted between <code>smacs</code>/<code>rmacs</code> switches) will be rendered as the corresponding graphic. Then read off the VT100/your terminal character pairs right to left in sequence; these become the ACSC string. </p>
<h3>Color Handling</h3>
<p>The curses library functions <code>init_pair</code> and <code>init_color</code> manipulate the <i>color pairs</i> and <i>color values</i> discussed in this section (see <code>curs_color</code>(3X) for details on these and related functions). </p>
<p>Most color terminals are either ``Tektronix-like&#8217;&#8216; or ``HP-like&#8217;&#8216;: <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 Tektronix-like terminals have a predefined set of <i>N</i> colors (where <i>N</i> is usually 8), and can set character-cell foreground and background characters independently, mixing them into <i>N</i>&nbsp;*&nbsp;<i>N</i> color-pairs. <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 On HP-like terminals, the user must set each color pair up separately (foreground and background are not independently settable). Up to <i>M</i> color-pairs may be set up from 2*<i>M</i> different colors. ANSI-compatible terminals are Tektronix-like. </p>
<p>Some basic color capabilities are independent of the color method. The numeric capabilities <code>colors</code> and <code>pairs</code> specify the maximum numbers of colors and color-pairs that can be displayed simultaneously. The <code>op</code> (original pair) string resets foreground and background colors to their default values for the terminal. The <code>oc</code> string resets all colors or color-pairs to their default values for the terminal. Some terminals (including many PC terminal emulators) erase screen areas with the current background color rather than the power-up default background; these should have the boolean capability <code>bce</code>. </p>
<p>While the curses library works with <i>color pairs</i> (reflecting the inability of some devices to set foreground and background colors independently), there are separate capabilities for setting these features: <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 To change the current foreground or background color on a Tektronix-type terminal, use <code>setaf</code> (set ANSI foreground) and <code>setab</code> (set ANSI background) or <code>setf</code> (set foreground) and <code>setb</code> (set background). These take one parameter, the color number. The SVr4 documentation describes only <code>setaf</code>/<code>setab</code>; the XPG4 draft says that &quot;If the terminal supports ANSI escape sequences to set background and foreground, they should be coded as <code>setaf</code> and <code>setab</code>, respectively. <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 If the terminal supports other escape sequences to set background and foreground, they should be coded as <code>setf</code> and <code>setb</code>, respectively. The <code>vidputs</code> and the <code>refresh</code>(3X) functions use the <code>setaf</code> and <code>setab</code> capabilities if they are defined. </p>
<p>The <code>setaf</code>/<code>setab</code> and <code>setf</code>/<code>setb</code> capabilities take a single numeric argument each. Argument values 0-7 of <code>setaf</code>/<code>setab</code> are portably defined as follows (the middle column is the symbolic #define available in the header for the <code>curses</code> or <code>ncurses</code> libraries). The terminal hardware is free to map these as it likes, but the RGB values indicate normal locations in color space. </p>
<p> <center> </p>
<table>
<tr VALIGN=top>
<td><code>Color</code></td>
<td>#define </td>
<td>Value</td>
<td>RGB
</td>
</tr>
<tr VALIGN=top>
<td>black</td>
<td><code>COLOR_BLACK</code></td>
<td>0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td>0, 0, 0
</td>
</tr>
<tr VALIGN=top>
<td>red</td>
<td><code>COLOR_RED&nbsp;</code></td>
<td>1&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td>max,0,0
</td>
</tr>
<tr VALIGN=top>
<td>green</td>
<td><code>COLOR_GREEN</code></td>
<td>2&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td>0,max,0
</td>
</tr>
<tr VALIGN=top>
<td>yellow</td>
<td><code>COLOR_YELLOW</code></td>
<td>3&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td>max,max,0
</td>
</tr>
<tr VALIGN=top>
<td>blue</td>
<td><code>COLOR_BLUE</code></td>
<td>4&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td>0,0,max
</td>
</tr>
<tr VALIGN=top>
<td>magenta</td>
<td><code>COLOR_MAGENTA</code></td>
<td>5&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td>max,0,max
</td>
</tr>
<tr VALIGN=top>
<td>cyan</td>
<td><code>COLOR_CYAN</code></td>
<td>6&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td>0,max,max
</td>
</tr>
<tr VALIGN=top>
<td>white</td>
<td><code>COLOR_WHITE</code></td>
<td>7&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td>max,max,max
</td>
</tr>
</table>
<p> </center> </p>
<p>The argument values of <code>setf</code>/<code>setb</code> historically correspond to a different mapping, i.e., <center> </p>
<table>
<tr VALIGN=top>
<td><code>Color</code></td>
<td>#define </td>
<td>Value</td>
<td>RGB
</td>
</tr>
<tr VALIGN=top>
<td>black</td>
<td><code>COLOR_BLACK</code></td>
<td>0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td>0, 0, 0
</td>
</tr>
<tr VALIGN=top>
<td>blue</td>
<td><code>COLOR_BLUE</code></td>
<td>1&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td>0,0,max
</td>
</tr>
<tr VALIGN=top>
<td>green</td>
<td><code>COLOR_GREEN</code></td>
<td>2&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td>0,max,0
</td>
</tr>
<tr VALIGN=top>
<td>cyan</td>
<td><code>COLOR_CYAN</code></td>
<td>3&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td>0,max,max
</td>
</tr>
<tr VALIGN=top>
<td>red</td>
<td><code>COLOR_RED&nbsp;</code></td>
<td>4&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td>max,0,0
</td>
</tr>
<tr VALIGN=top>
<td>magenta</td>
<td><code>COLOR_MAGENTA</code></td>
<td>5&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td>max,0,max
</td>
</tr>
<tr VALIGN=top>
<td>yellow</td>
<td><code>COLOR_YELLOW</code></td>
<td>6&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td>max,max,0
</td>
</tr>
<tr VALIGN=top>
<td>white</td>
<td><code>COLOR_WHITE</code></td>
<td>7&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</td>
<td>max,max,max
</td>
</tr>
</table>
<p> </center> </p>
<p>It is important to not confuse the two sets of color capabilities; otherwise red/blue will be interchanged on the display. </p>
<p>On an HP-like terminal, use <code>scp</code> with a color-pair number parameter to set which color pair is current. </p>
<p>Some terminals allow the <i>color values</i> to be modified: <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 On a Tektronix-like terminal, the capability <code>ccc</code> may be present to indicate that colors can be modified. If so, the <code>initc</code> capability will take a color number (0 to <code>colors</code> - 1)and three more parameters which describe the color. These three parameters default to being interpreted as RGB (Red, Green, Blue) values. If the boolean capability <code>hls</code> is present, they are instead as HLS (Hue, Lightness, Saturation) indices. The ranges are terminal-dependent. <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 On an HP-like terminal, <code>initp</code> may give a capability for changing a color-pair value. It will take seven parameters; a color-pair number (0 to <code>max_pairs</code> - 1), and two triples describing first background and then foreground colors. These parameters must be (Red, Green, Blue) or (Hue, Lightness, Saturation) depending on <code>hls</code>. </p>
<p>On some color terminals, colors collide with highlights. You can register these collisions with the <code>ncv</code> capability. This is a bit-mask of attributes not to be used when colors are enabled. The correspondence with the attributes understood by <code>curses</code> is as follows: </p>
<p> <center> </p>
<table>
<tr VALIGN=top>
<td><code>Attribute</code></td>
<td>Bit</td>
<td>Decimal</td>
<td>Set by
</td>
</tr>
<tr VALIGN=top>
<td>A_STANDOUT</td>
<td>0</td>
<td>1</td>
<td>sgr
</td>
</tr>
<tr VALIGN=top>
<td>A_UNDERLINE</td>
<td>1</td>
<td>2</td>
<td>sgr
</td>
</tr>
<tr VALIGN=top>
<td>A_REVERSE</td>
<td>2</td>
<td>4</td>
<td>sgr
</td>
</tr>
<tr VALIGN=top>
<td>A_BLINK </td>
<td>3</td>
<td>8</td>
<td>sgr
</td>
</tr>
<tr VALIGN=top>
<td>A_DIM </td>
<td>4</td>
<td>16</td>
<td>sgr
</td>
</tr>
<tr VALIGN=top>
<td>A_BOLD </td>
<td>5</td>
<td>32</td>
<td>sgr
</td>
</tr>
<tr VALIGN=top>
<td>A_INVIS </td>
<td>6</td>
<td>64</td>
<td>sgr
</td>
</tr>
<tr VALIGN=top>
<td>A_PROTECT</td>
<td>7</td>
<td>128</td>
<td>sgr
</td>
</tr>
<tr VALIGN=top>
<td>A_ALTCHARSET</td>
<td>8</td>
<td>256</td>
<td>sgr
</td>
</tr>
<tr VALIGN=top>
<td>A_HORIZONTAL</td>
<td>9</td>
<td>512</td>
<td>sgr1
</td>
</tr>
<tr VALIGN=top>
<td>A_LEFT</td>
<td>10</td>
<td>1024</td>
<td>sgr1
</td>
</tr>
<tr VALIGN=top>
<td>A_LOW</td>
<td>11</td>
<td>2048</td>
<td>sgr1
</td>
</tr>
<tr VALIGN=top>
<td>A_RIGHT</td>
<td>12</td>
<td>4096</td>
<td>sgr1
</td>
</tr>
<tr VALIGN=top>
<td>A_TOP</td>
<td>13</td>
<td>8192</td>
<td>sgr1
</td>
</tr>
<tr VALIGN=top>
<td>A_VERTICAL</td>
<td>14</td>
<td>16384</td>
<td>sgr1
</td>
</tr>
<tr VALIGN=top>
<td>A_ITALIC</td>
<td>15</td>
<td>32768</td>
<td>sitm
</td>
</tr>
</table>
<p> </center> </p>
<p>For example, on many IBM PC consoles, the underline attribute collides with the foreground color blue and is not available in color mode. These should have an <code>ncv</code> capability of 2. </p>
<p>SVr4 curses does nothing with <code>ncv</code>, ncurses recognizes it and optimizes the output in favor of colors. </p>
<h3>Miscellaneous</h3>
<p> If the terminal requires other than a null (zero) character as a pad, then this can be given as pad. Only the first character of the pad string is used. If the terminal does not have a pad character, specify npc. Note that ncurses implements the termcap-compatible <code>PC</code> variable; though the application may set this value to something other than a null, ncurses will test <code>npc</code> first and use napms if the terminal has no pad character. </p>
<p>If the terminal can move up or down half a line, this can be indicated with <code>hu</code> (half-line up) and <code>hd</code> (half-line down). This is primarily useful for superscripts and subscripts on hard-copy terminals. If a hard-copy terminal can eject to the next page (form feed), give this as <code>ff</code> (usually control/L). </p>
<p>If there is a command to repeat a given character a given number of times (to save time transmitting a large number of identical characters) this can be indicated with the parameterized string <code>rep</code>. The first parameter is the character to be repeated and the second is the number of times to repeat it. Thus, tparm(repeat_char, &#8216;x&#8217;, 10) is the same as ``xxxxxxxxxx&#8217;&#8216;. </p>
<p>If the terminal has a settable command character, such as the TEKTRONIX 4025, this can be indicated with <code>cmdch</code>. A prototype command character is chosen which is used in all capabilities. This character is given in the <code>cmdch</code> capability to identify it. The following convention is supported on some UNIX systems: The environment is to be searched for a <code>CC</code> variable, and if found, all occurrences of the prototype character are replaced with the character in the environment variable. </p>
<p>Terminal descriptions that do not represent a specific kind of known terminal, such as <i>switch</i>, <i>dialup</i>, <i>patch</i>, and <i>network</i>, should include the <code>gn</code> (generic) capability so that programs can complain that they do not know how to talk to the terminal. (This capability does not apply to <i>virtual</i> terminal descriptions for which the escape sequences are known.) </p>
<p>If the terminal has a ``meta key&#8217;&#8216; which acts as a shift key, setting the 8th bit of any character transmitted, this fact can be indicated with <code>km</code>. Otherwise, software will assume that the 8th bit is parity and it will usually be cleared. If strings exist to turn this ``meta mode&#8217;&#8216; on and off, they can be given as <code>smm</code> and <code>rmm</code>. </p>
<p>If the terminal has more lines of memory than will fit on the screen at once, the number of lines of memory can be indicated with <code>lm</code>. A value of <code>lm</code>#0 indicates that the number of lines is not fixed, but that there is still more memory than fits on the screen. </p>
<p>If the terminal is one of those supported by the UNIX virtual terminal protocol, the terminal number can be given as <code>vt</code>. </p>
<p>Media copy strings which control an auxiliary printer connected to the terminal can be given as <code>mc0</code>: print the contents of the screen, <code>mc4</code>: turn off the printer, and <code>mc5</code>: turn on the printer. When the printer is on, all text sent to the terminal will be sent to the printer. It is undefined whether the text is also displayed on the terminal screen when the printer is on. A variation <code>mc5p</code> takes one parameter, and leaves the printer on for as many characters as the value of the parameter, then turns the printer off. The parameter should not exceed 255. All text, including <code>mc4</code>, is transparently passed to the printer while an <code>mc5p</code> is in effect. </p>
<h3>Glitches and Braindamage</h3>
<p>Hazeltine terminals, which do not allow ``~&#8216;&#8216; characters to be displayed should indicate <code>hz</code>. </p>
<p>Terminals which ignore a line-feed immediately after an <code>am</code> wrap, such as the Concept and vt100, should indicate <code>xenl</code>. </p>
<p>If <code>el</code> is required to get rid of standout (instead of merely writing normal text on top of it), <code>xhp</code> should be given. </p>
<p>Teleray terminals, where tabs turn all characters moved over to blanks, should indicate <code>xt</code> (destructive tabs). Note: the variable indicating this is now ``dest_tabs_magic_smso&#8217;&#8216;; in older versions, it was teleray_glitch. This glitch is also taken to mean that it is not possible to position the cursor on top of a ``magic cookie&#8217;&#8216;, that to erase standout mode it is instead necessary to use delete and insert line. The ncurses implementation ignores this glitch. </p>
<p>The Beehive Superbee, which is unable to correctly transmit the escape or control/C characters, has <code>xsb</code>, indicating that the f1 key is used for escape and f2 for control/C. (Only certain Superbees have this problem, depending on the ROM.) Note that in older terminfo versions, this capability was called ``beehive_glitch&#8217;&#8216;; it is now ``no_esc_ctl_c&#8217;&#8216;. </p>
<p>Other specific terminal problems may be corrected by adding more capabilities of the form <code>x</code><i>x</i>. </p>
<h3>Pitfalls of Long Entries</h3>
<p>Long terminfo entries are unlikely to be a problem; to date, no entry has even approached terminfo&#8217;s 4096-byte string-table maximum. Unfortunately, the termcap translations are much more strictly limited (to 1023 bytes), thus termcap translations of long terminfo entries can cause problems. </p>
<p>The man pages for 4.3BSD and older versions of <code>tgetent</code> instruct the user to allocate a 1024-byte buffer for the termcap entry. The entry gets null-terminated by the termcap library, so that makes the maximum safe length for a termcap entry 1k-1 (1023) bytes. Depending on what the application and the termcap library being used does, and where in the termcap file the terminal type that <code>tgetent</code> is searching for is, several bad things can happen. </p>
<p>Some termcap libraries print a warning message or exit if they find an entry that&#8217;s longer than 1023 bytes; others do not; others truncate the entries to 1023 bytes. Some application programs allocate more than the recommended 1K for the termcap entry; others do not. </p>
<p>Each termcap entry has two important sizes associated with it: before ``tc&#8217;&#8216; expansion, and after ``tc&#8217;&#8216; expansion. ``tc&#8217;&#8216; is the capability that tacks on another termcap entry to the end of the current one, to add on its capabilities. If a termcap entry does not use the ``tc&#8217;&#8216; capability, then of course the two lengths are the same. </p>
<p>The ``before tc expansion&#8217;&#8216; length is the most important one, because it affects more than just users of that particular terminal. This is the length of the entry as it exists in /etc/termcap, minus the backslash-newline pairs, which <code>tgetent</code> strips out while reading it. Some termcap libraries strip off the final newline, too (GNU termcap does not). Now suppose: <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 a termcap entry before expansion is more than 1023 bytes long, <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 and the application has only allocated a 1k buffer, <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 and the termcap library (like the one in BSD/OS 1.1 and GNU) reads the whole entry into the buffer, no matter what its length, to see if it is the entry it wants, <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 and <code>tgetent</code> is searching for a terminal type that either is the long entry, appears in the termcap file after the long entry, or does not appear in the file at all (so that <code>tgetent</code> has to search the whole termcap file). </p>
<p>Then <code>tgetent</code> will overwrite memory, perhaps its stack, and probably core dump the program. Programs like telnet are particularly vulnerable; modern telnets pass along values like the terminal type automatically. The results are almost as undesirable with a termcap library, like SunOS 4.1.3 and Ultrix 4.4, that prints warning messages when it reads an overly long termcap entry. If a termcap library truncates long entries, like OSF/1 3.0, it is immune to dying here but will return incorrect data for the terminal. </p>
<p>The ``after tc expansion&#8217;&#8216; length will have a similar effect to the above, but only for people who actually set TERM to that terminal type, since <code>tgetent</code> only does ``tc&#8217;&#8216; expansion once it is found the terminal type it was looking for, not while searching. </p>
<p>In summary, a termcap entry that is longer than 1023 bytes can cause, on various combinations of termcap libraries and applications, a core dump, warnings, or incorrect operation. If it is too long even before ``tc&#8217;&#8216; expansion, it will have this effect even for users of some other terminal types and users whose TERM variable does not have a termcap entry. </p>
<p>When in -C (translate to termcap) mode, the <code>ncurses</code> implementation of <code><a href="/docs/linux/man/1-tic/">tic</a></code>(1) issues warning messages when the pre-tc length of a termcap translation is too long. The -c (check) option also checks resolved (after tc expansion) lengths.  </p>
<h3>Binary Compatibility</h3>
<p> It is not wise to count on portability of binary terminfo entries between commercial UNIX versions. The problem is that there are at least two versions of terminfo (under HP-UX and AIX) which diverged from System V terminfo after SVr1, and have added extension capabilities to the string table that (in the binary format) collide with System V and XSI Curses extensions.  </p>
<h2>EXTENSIONS</h2>
<p>Searching for terminal descriptions in <code>$HOME/.terminfo</code> and TERMINFO_DIRS is not supported by older implementations. </p>
<p>Some SVr4 <code>curses</code> implementations, and all previous to SVr4, do not interpret the %A and %O operators in parameter strings. </p>
<p>SVr4/XPG4 do not specify whether <code>msgr</code> licenses movement while in an alternate-character-set mode (such modes may, among other things, map CR and NL to characters that do not trigger local motions). The <code>ncurses</code> implementation ignores <code>msgr</code> in <code>ALTCHARSET</code> mode. This raises the possibility that an XPG4 implementation making the opposite interpretation may need terminfo entries made for <code>ncurses</code> to have <code>msgr</code> turned off. </p>
<p>The <code>ncurses</code> library handles insert-character and insert-character modes in a slightly non-standard way to get better update efficiency. See the <code>Insert/Delete Character</code> subsection above. </p>
<p>The parameter substitutions for <code>set_clock</code> and <code>display_clock</code> are not documented in SVr4 or the XSI Curses standard. They are deduced from the documentation for the AT&amp;T 505 terminal. </p>
<p>Be careful assigning the <code>kmous</code> capability. The <code>ncurses</code> library wants to interpret it as <code>KEY_MOUSE</code>, for use by terminals and emulators like xterm that can return mouse-tracking information in the keyboard-input stream. </p>
<p>X/Open Curses does not mention italics. Portable applications must assume that numeric capabilities are signed 16-bit values. This includes the <i>no_color_video</i> (ncv) capability. The 32768 mask value used for italics with ncv can be confused with an absent or cancelled ncv. If italics should work with colors, then the ncv value must be specified, even if it is zero. </p>
<p>Different commercial ports of terminfo and curses support different subsets of the XSI Curses standard and (in some cases) different extension sets. Here is a summary, accurate as of October 1995: <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 <code>SVR4, Solaris, ncurses</code> -- These support all SVr4 capabilities. <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 <code>SGI</code> -- Supports the SVr4 set, adds one undocumented extended string capability (<code>set_pglen</code>). <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 <code>SVr1, Ultrix</code> -- These support a restricted subset of terminfo capabilities. The booleans end with <code>xon_xoff</code>; the numerics with <code>width_status_line</code>; and the strings with <code>prtr_non</code>. <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 <code>HP/UX</code> -- Supports the SVr1 subset, plus the SVr[234] numerics <code>num_labels</code>, <code>label_height</code>, <code>label_width</code>, plus function keys 11 through 63, plus <code>plab_norm</code>, <code>label_on</code>, and <code>label_off</code>, plus some incompatible extensions in the string table. <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 <code>AIX</code> -- Supports the SVr1 subset, plus function keys 11 through 63, plus a number of incompatible string table extensions. <br/>
&nbsp;.IP&nbsp;&bull;&nbsp;4 <code>OSF</code> -- Supports both the SVr4 set and the AIX extensions.  </p>
<h2>FILES</h2>
<dl>
<dt>/etc/terminfo/?/*</dt>
<dd> <p> files containing terminal descriptions </p>
 </dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-infocmp/">infocmp</a></code>(1), <code><a href="/docs/linux/man/1-tabs/">tabs</a></code>(1), <code><a href="/docs/linux/man/1-tic/">tic</a></code>(1), <code>ncurses</code>(3NCURSES), <code>color</code>(3NCURSES), <code>curses_variables</code>(3NCURSES), <code><a href="/docs/linux/man/3-printf/">printf</a></code>(3), <code>terminfo_variables</code>(3NCURSES). <code><a href="/docs/linux/man/5-term/">term</a></code>(5). <code><a href="/docs/linux/man/5-user_caps/">user_caps</a></code>(5).  </p>
<h2>AUTHORS</h2>
<p> Zeyd M. Ben-Halim, Eric S. Raymond, Thomas E. Dickey. Based on pcurses by Pavel Curtis. </p>
