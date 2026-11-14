---
title: "term(7)"
name: "term"
section: "7"
letter: "t"
url: "/docs/linux/man/7-term/"
description: "term – conventions for naming terminal types"
---

<p>term &#8211; conventions for naming terminal types</p>
<h2>Description</h2>
<p>The environment variable <code>TERM</code> should normally contain the type name of the terminal, console or display-device type you are using. This information is critical for all screen-oriented programs, including your editor and mailer. </p>
<p> A default <code>TERM</code> value will be set on a per-line basis by either <code>/etc/inittab</code> (e.g., System-V-like UNIXes) or <code>/etc/ttys</code> (BSD UNIXes). This will nearly always suffice for workstation and microcomputer consoles. </p>
<p> If you use a dialup line, the type of device attached to it may vary. Older UNIX systems pre-set a very dumb terminal type like &#8220;dumb&#8221; or &#8220;dialup&#8221; on dialup lines. Newer ones may pre-set &#8220;vt100&#8221;, reflecting the prevalence of DEC VT100-compatible terminals and personal-computer emulators. </p>
<p> Modern telnets pass your <code>TERM</code> environment variable from the local side to the remote one. There can be problems if the remote terminfo or termcap entry for your type is not compatible with yours, but this situation is rare and can almost always be avoided by explicitly exporting &#8220;vt100&#8221; (assuming you are in fact using a VT100-superset console, terminal, or terminal emulator). </p>
<p> In any case, you are free to override the system <code>TERM</code> setting to your taste in your shell profile. The <code><a href="/docs/linux/man/1-tset/">tset</a></code>(1) utility may be of assistance; you can give it a set of rules for deducing or requesting a terminal type based on the tty device and baud rate. </p>
<p> Setting your own <code>TERM</code> value may also be useful if you have created a custom entry incorporating options (such as visual bell or reverse-video) which you wish to override the system default type for your line. </p>
<p> Terminal type descriptions are stored as files of capability data underneath /etc/terminfo. To browse a list of all terminal names recognized by the system, do </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>toe | more</p>
<p> from your shell. These capability files are in a binary format optimized for retrieval speed (unlike the old text-based <code>termcap</code> format they replace); to examine an entry, you must use the <code><a href="/docs/linux/man/1-infocmp/">infocmp</a></code>(1) command. Invoke it as follows: </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>infocmp <i>entry_name</i></p>
<p> where <i>entry_name</i> is the name of the type you wish to examine (and the name of its capability file the subdirectory of /etc/terminfo named for its first letter). This command dumps a capability file in the text format described by <code><a href="/docs/linux/man/5-terminfo/">terminfo</a></code>(5). </p>
<p> The first line of a <code><a href="/docs/linux/man/5-terminfo/">terminfo</a></code>(5) description gives the names by which terminfo knows a terminal, separated by &#8220;|&#8221; (pipe-bar) characters with the last name field terminated by a comma. The first name field is the type&#8217;s <i>primary name</i>, and is the one to use when setting <code>TERM</code>. The last name field (if distinct from the first) is actually a description of the terminal type (it may contain blanks; the others must be single words). Name fields between the first and last (if present) are aliases for the terminal, usually historical names retained for compatibility. </p>
<p> There are some conventions for how to choose terminal primary names that help keep them informative and unique. Here is a step-by-step guide to naming terminals that also explains how to parse them: </p>
<p> First, choose a root name. The root will consist of a lower-case letter followed by up to seven lower-case letters or digits. You need to avoid using punctuation characters in root names, because they are used and interpreted as filenames and shell meta-characters (such as !, $, *, ?, etc.) embedded in them may cause odd and unhelpful behavior. The slash (/), or any other character that may be interpreted by anyone&#8217;s file system (\, $, [, ]), is especially dangerous (terminfo is platform-independent, and choosing names with special characters could someday make life difficult for users of a future port). The dot (.) character is relatively safe as long as there is at most one per root name; some historical terminfo names use it. </p>
<p> The root name for a terminal or workstation console type should almost always begin with a vendor prefix (such as <code>hp</code> for Hewlett-Packard, <code>wy</code> for Wyse, or <code>att</code> for AT&amp;T terminals), or a common name of the terminal line (<code>vt</code> for the VT series of terminals from DEC, or <code>sun</code> for Sun Microsystems workstation consoles, or <code>regent</code> for the ADDS Regent series. You can list the terminfo tree to see what prefixes are already in common use. The root name prefix should be followed when appropriate by a model number; thus <code>vt100</code>, <code>hp2621</code>, <code>wy50</code>. </p>
<p> The root name for a PC-Unix console type should be the OS name, i.e., <code>linux</code>, <code>bsdos</code>, <code>freebsd</code>, <code>netbsd</code>. It should <i>not</i> be <code>console</code> or any other generic that might cause confusion in a multi-platform environment! If a model number follows, it should indicate either the OS release level or the console driver release level. </p>
<p> The root name for a terminal emulator (assuming it does not fit one of the standard ANSI or vt100 types) should be the program name or a readily recognizable abbreviation of it (i.e., <code>versaterm</code>, <code>ctrm</code>). </p>
<p> Following the root name, you may add any reasonable number of hyphen-separated feature suffixes.</p>
<dl>
<dt>2p</p>
<dd>Has two pages of memory. Likewise 4p, 8p, etc.</p>
<dt>mc</p>
<dd>Magic-cookie. Some terminals (notably older Wyses) can only support one attribute without magic-cookie lossage. Their base entry is usually paired with another that has this suffix and uses magic cookies to support multiple attributes.</p>
<dt>-am</p>
<dd>Enable auto-margin (right-margin wraparound).</p>
<dt>-m</p>
<dd>Mono mode &#8211; suppress color support.</p>
<dt>-na</p>
<dd>No arrow keys &#8211; termcap ignores arrow keys which are actually there on the terminal, so the user can use the arrow keys locally.</p>
<dt>-nam</p>
<dd>No auto-margin &#8211; suppress am capability.</p>
<dt>-nl</p>
<dd>No labels &#8211; suppress soft labels.</p>
<dt>-nsl</p>
<dd>No status line &#8211; suppress status line.</p>
<dt>-pp</p>
<dd>Has a printer port which is used.</p>
<dt>-rv</p>
<dd>Terminal in reverse video mode (black on white).</p>
<dt>-s</p>
<dd>Enable status line.</p>
<dt>-vb</p>
<dd>Use visible bell (flash) rather than beep.</p>
<dt>-w</p>
<dd>Wide; terminal is in 132-column mode.</dl>
<p> Conventionally, if your terminal type is a variant intended to specify a line height, that suffix should go first. So, for a hypothetical FuBarCo model 2317 terminal in 30-line mode with reverse video, best form would be <code>fubar-30-rv</code> (rather than, say, &#8220;fubar-rv-30&#8221;). </p>
<p> Terminal types that are written not as standalone entries, but rather as components to be plugged into other entries via <code>use</code> capabilities, are distinguished by using embedded plus signs rather than dashes. </p>
<p> Commands which use a terminal type to control display often accept a -T option that accepts a terminal name argument. Such programs should fall back on the <code>TERM</code> environment variable when no -T option is specified.</p>
<h2>Portability</h2>
<p>For maximum compatibility with older System V UNIXes, names and aliases should be unique within the first 14 characters.</p>
<h2>Files</h2>
<dl>
<dt>/etc/terminfo/?/*</p>
<dd>compiled terminal capability database</p>
<dt>/etc/inittab</p>
<dd>tty line initialization (AT&amp;T-like UNIXes)</p>
<dt>/etc/ttys</p>
<dd>tty line initialization (BSD-like UNIXes)</dl>
<h2>See Also</h2>
<p><code>ncurses</code>(3NCURSES), <code><a href="/docs/linux/man/5-terminfo/">terminfo</a></code>(5), <code><a href="/docs/linux/man/5-term/">term</a></code>(5). </p>
