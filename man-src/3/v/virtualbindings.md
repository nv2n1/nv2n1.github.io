---
title: "virtualbindings(3)"
name: "virtualbindings"
section: "3"
letter: "v"
url: "/docs/linux/man/3-virtualbindings/"
description: "VirtualBindings — Bindings for virtual mouse and key events"
---

<p><code>VirtualBindings</code> &#8212; Bindings for virtual mouse and key events</p>
<h2>Description</h2>
<p>The Motif reference pages describe key translations in terms of <i>virtual bindings</i>, based on those described in the <i>Motif Style Guide</i>.</p>
<h3>Bindings for osf Keysyms</h3>
<p>Keysym strings that begin with <code>&lt;osf&gt;</code> are not part of the X server&#8217;s keyboard mapping. Instead, these keysyms are produced on the client side at run time. They are interpreted by the routine <code>XmTranslateKey</code>, and are used by the translation manager when the server delivers an actual key event. For each application, a mapping is maintained between <code>&lt;osf&gt;</code> keysyms and keysyms that correspond to actual keys. This mapping is based on information obtained at application startup from one of the following sources, listed in order of precedence:</p>
<dl COMPACT>
<dt> &bull;</p>
<dd>The <code>XmNdefaultVirtualBindings</code> resource from Display.</p>
<dt> &bull;</p>
<dd>A property on the root window, which can be set by <code>mwm</code> on startup, or by the <code>xmbind</code> client, or on prior startup of a Motif application.</p>
<dt> &bull;</p>
<dd>The file <code>.motifbind</code> in the user&#8217;s home directory.</p>
<dt> &bull;</p>
<dd>A set of bindings based on the vendor string and optionally the vendor release of the X server. Motif searches for these bindings in the following steps:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt> 0.</p>
<dd>If the file <code>xmbind.alias</code> exists in the user&#8217;s home directory, Motif searches this file for a pathname associated with the vendor string or with the vendor string and vendor release. If it finds such a pathname and if that file exists, Motif loads the bindings contained in that file.</p>
<dt> 1.</p>
<dd>If it has found no bindings, Motif next looks for the file <code>xmbind.alias</code> in the directory specified by the environment variable <code>XMBINDDIR</code>, if <code>XMBINDDIR</code> is set, or in the directory <code>/usr/share/X11/bindings</code> if <code>XMBINDDIR</code> is not set. If this file exists Motif searches it for a pathname associated with the vendor string or with the vendor string and vendor release. If it finds such a pathname and if that file exists, Motif loads the bindings contained in that file.</p>
<dt> 2.</p>
<dd>If it still has found no bindings, Motif loads a set of hard-coded fallback bindings.</dl>
</dl>
</dl>
<p> The <code>xmbind.alias</code> file contains zero or more lines of the following form: </p>
<pre><tt>&quot;</tt><i>vendor_string</i>[ <i>vendor_release</i>]&quot; <i>bindings_file</i></pre>
<p>where <i>vendor_string</i> is the X server vendor name as returned by the X client <code>xdpyinfo</code> or the Xlib function <code>XServerVendor</code>, and must appear in double quotes. If <i>vendor_release</i> is included, it is the X server vendor release number as returned by the X client <code>xdpyinfo</code> or the Xlib function <code>XVendorRelease</code>, and must also be contained within the double quotes separated by one space from <i>vendor_string</i>. The <i>vendor_release</i> argument is provided to allow support of changes in keyboard hardware from a vendor, assuming that the vendor increments the release number to flag such changes. Alternatively, the vendor may simply use a unique vendor string for each different keyboard. </p>
<p> The <i>bindings_file</i> argument is the pathname of the file containing the bindings themselves. It can be a relative or absolute pathname. If it it is a relative pathname, it is relative to the location of the <code>xmbind.alias</code> file. </p>
<p> Comment lines in the <code>xmbind.alias</code> file begin with ! (exclamation point). </p>
<p> The bindings found in either the <code>.motifbind</code> file or the vendor mapping are placed in a property on the root window. This property is used to determine the bindings for subsequent Motif applications. </p>
<p> On startup <code>mwm</code> attempts to load the file <code>.motifbind</code> in the user&#8217;s home directory. If this is unsuccessful, it loads the vendor bindings as described previously. It places the bindings it loads in a property on the root window for use by subsequent Motif applications. </p>
<p> The <code>xmbind</code> function loads bindings from a file if that file is specified on the command line. If no file is specified on the command line, it attempts to load the file <code>.motifbind</code> in the user&#8217;s home directory. If this fails, it loads the vendor bindings as described previously. It places the bindings it loads in a property on the root window for use by subsequent Motif applications. </p>
<p> The format of the specification for mapping <code>&lt;osf&gt;</code> keysyms to actual keysyms is similar to that of a specification for an event translation. (See below) The syntax is specified (and below) here in EBNF notation using the following conventions: </p>
<pre><tt>[</tt><i>a</i>] Means either nothing or <i>a</i>
{<i>a</i>} Means zero or more occurrences of <i>a</i>
(<i>a</i>|<i>b</i>) Means either <i>a</i> or <i>b</i>.</pre>
<p>Terminals are enclosed in double quotation marks. </p>
<p> The syntax of an <code>&lt;osf&gt;</code> keysym binding specification is as follows: </p>
<pre><tt>binding_spec = {line &quot;
&quot;} [line]
line = virtual_keysym &quot;:&quot; list_of_key_event
list_of_key_event= key_event { &quot;,&quot; key_event}
key_event = {modifier_name} &quot;&lt;Key&gt;&quot; actual_keysym
virtual_keysym = keysym
actual_keysym = keysym
keysym = A valid X11 keysym name that is
 mapped by </tt><code>XStringToKeysym</code></pre>
<p>As with event translations, more specific event descriptions must precede less specific descriptions. For example, an event description for a key with a modifier must precede a description for the same key without the same modifier. </p>
<p> Following is an example of a specification for the <code>defaultVirtualBindings</code> resource in a resource file: </p>
<pre><tt>*defaultVirtualBindings: \
 osfBackSpace: &lt;Key&gt;BackSpace 
\
 osfInsert: &lt;Key&gt;InsertChar 
\
 osfDelete: &lt;Key&gt;DeleteChar 
\
...
 osfLeft: &lt;Key&gt;left, Ctrl&lt;Key&gt;H</tt></pre>
<p>The format of a <code>.motifbind</code> file or of a file containing vendor bindings is the same, except that the binding specification for each keysym is placed on a separate line. The previous example specification appears as follows in a <code>.motifbind</code> or vendor bindings file: </p>
<pre><tt>osfBackSpace: &lt;Key&gt;BackSpace
osfInsert: &lt;Key&gt;InsertChar
osfDelete: &lt;Key&gt;DeleteChar
...
osfLeft: &lt;Key&gt;left, Ctrl&lt;Key&gt;H</tt></pre>
<p>The following table lists the fixed fallback default bindings for <code>&lt;osf&gt;</code> keysyms. </p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td ALIGN=center COLSPAN=2> <code>Fallback Default Bindings for osf Keysyms</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>&lt;osf Keysym&gt;</code></td>
<td><code>Fallback Default Binding</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>&lt;osfActivate&gt;</code><code>:</code></td>
<td><code>&lt;Key&gt;KP_Enter</code>, <code>&lt;Key&gt;Execute</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>&lt;osfAddMode&gt;</code><code>:</code></td>
<td><code>Shift&lt;Key&gt;F8</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>&lt;osfBackSpace&gt;</code><code>:</code></td>
<td><code>&lt;Key&gt;</code><code>BackSpace</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>&lt;osfBeginLine&gt;</code><code>:</code></td>
<td><code>&lt;Key&gt;Home</code>, <code>&lt;Key&gt;Begin</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>&lt;osfCancel&gt;</code><code>:</code></td>
<td><code>&lt;Key&gt;Escape</code>, <code>&lt;Key&gt;Cancel</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>&lt;osfClear&gt;</code><code>:</code></td>
<td><code>&lt;Key&gt;</code><code>Clear</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>&lt;osfCopy&gt;</code><code>:</code></td>
<td><i>unbound</i>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>&lt;osfCut&gt;</code><code>:</code></td>
<td><i>unbound</i>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>&lt;osfDelete&gt;</code><code>:</code></td>
<td><code>&lt;Key&gt;</code><code>Delete</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>&lt;osfDeselectAll&gt;</code><code>:</code></td>
<td><i>unbound</i>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>&lt;osfDown&gt;</code><code>:</code></td>
<td><code>&lt;Key&gt;</code><code>Down</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>&lt;osfEndLine&gt;</code><code>:</code></td>
<td><code>&lt;Key&gt;</code><code>End</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>&lt;osfHelp&gt;</code><code>:</code></td>
<td><code>&lt;Key&gt;F1</code>, <code>&lt;Key&gt;Help</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>&lt;osfInsert&gt;</code><code>:</code></td>
<td><code>&lt;Key&gt;</code><code>Insert</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>&lt;osfLeft&gt;</code><code>:</code></td>
<td><code>&lt;Key&gt;</code><code>Left</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>&lt;osfLeftLine&gt;</code><code>:</code></td>
<td><i>unbound</i>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>&lt;osfMenu&gt;</code><code>:</code></td>
<td><code>Shift</code><code>&lt;Key&gt;F10</code>, <code>&lt;Key&gt;Menu</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>&lt;osfMenuBar&gt;</code><code>:</code></td>
<td><code>&lt;Key&gt;F10</code>, <code>Shift&lt;Key&gt;</code><code>Menu</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>&lt;osfNextMinor&gt;</code><code>:</code></td>
<td><i>unbound</i>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>&lt;osfPageDown&gt;</code><code>:</code></td>
<td><code>&lt;Key&gt;</code><code>Next</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>&lt;osfPageLeft&gt;</code><code>:</code></td>
<td><i>unbound</i>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>&lt;osfPageRight&gt;</code><code>:</code></td>
<td><i>unbound</i>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>&lt;osfPageUp&gt;</code><code>:</code></td>
<td><code>&lt;Key&gt;</code><code>Prior</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>&lt;osfPaste&gt;</code><code>:</code></td>
<td><i>unbound</i>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>&lt;osfPrimaryPaste&gt;</code><code>:</code></td>
<td><i>unbound</i>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>&lt;osfPriorMinor&gt;</code><code>:</code></td>
<td><i>unbound</i>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>&lt;osfReselect&gt;</code><code>:</code></td>
<td><i>unbound</i>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>&lt;osfRestore&gt;</code><code>:</code></td>
<td><i>unbound</i>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>&lt;osfRight&gt;</code><code>:</code></td>
<td><code>&lt;Key&gt;</code><code>Right</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>&lt;osfRightLine&gt;</code><code>:</code></td>
<td><i>unbound</i>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>&lt;osfSelect&gt;</code><code>:</code></td>
<td><code>&lt;Key&gt;</code><code>Select</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>&lt;osfSelectAll&gt;</code><code>:</code></td>
<td><i>unbound</i>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>&lt;osfSwitchDirection&gt;</code><code>:</code></td>
<td><code>Alt&lt;Key&gt;Return</code>, <code>Alt&lt;Key&gt;KP_Enter</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>&lt;osfUndo&gt;</code><code>:</code></td>
<td><code>&lt;Key&gt;</code><code>Undo</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td><code>&lt;osfUp&gt;</code><code>:</code></td>
<td><code>&lt;Key&gt;</code><code>Up</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
</table>
</table>
<h3>Changes in the Handling of Shifted Keys</h3>
<p>In conjunction with MIT X11R5 Patch 24, this version of Motif introduces a change in the way that keys involving the &lt;Shift&gt; modifier are processed. This change allows the numeric keypad to be used to generate numbers using the standard X mechanisms. Since the default behavior is now to honor the xmodmap keymap bindings, translations and virtual key bindings that use &lt;Shift&gt; may behave differently. A common symptom is that unshifted keypad and function keys (with or without other modifiers) produce the expected results, but shifted ones do not. </p>
<p> To obtain the old behavior you can remove the shifted interpretation from problematic keys using the <code>xmodmap</code> utility. Each entry in a <code>xmodmap</code> keymap table contains up to four keysym bindings. The second and fourth keysyms are for shifted keys. If an expression contains only two keysyms, simply remove the second keysym. If an entry contains three or more keysyms, replace the second keysym with <code>NoSymbol</code> and remove the fourth keysym.</p>
<h3>Action Translations</h3>
<p>The translation table syntax used by Motif is completely specified in the X11R5 Toolkit Intrinsics Documentation. For the complete syntax description, and for general instructions about writing or modifying a translation table, please refer to this document. A brief summary of the translation table format, however, is included below. </p>
<p> The syntax is defined as in the binding syntax specification above. Informal descriptions are contained in angle brackets (&lt;&gt;). </p>
<pre><tt>TranslationTable= [ directive ] { production }
directive = ( &quot;#replace&quot; | &quot;#override&quot; | &quot;#augment&quot;) &quot;
&quot;
production = lhs &quot;:&quot; rhs &quot;
&quot;
lhs = ( event | keyseq) {&quot;,&quot; ( event | keyseq) }
keyseq = &quot;&quot;&quot; keychar { keychar } &quot;&quot;&quot;
keychar = ( &quot;^&quot; | &quot;$&quot; | &quot;\&quot;) &lt;ISO Latin 1 character&gt;
event = [ modifier_list ] &quot;&lt;&quot; event_type &quot;&gt;&quot; [ count ] {detail}
modifier_list = ( [&quot;!&quot;][&quot;:&quot;] { modifier } | &quot;None&quot;)
modifier = [ &quot;~&quot; ] ( &quot;@&quot; &lt;keysym&gt; | &lt;name from table below&gt;)
count = &quot;(&quot; &lt;positive integer&gt; [ &quot;+&quot; ] &quot;)&quot;
rhs = { action_name &quot;(&quot; [params] &quot;)&quot; }
params = string { &quot;,&quot; string }</tt></pre>
<p>The <i>string</i> field need not be quoted unless it includes a space or tab character, or any comma, newline, or parenthesis. The entire list of string values making up the <i>params</i> field will ba passed to the named action routine. </p>
<p> The <i>details</i> field may be used to specify a keysym that will identify a particular key event. For example, <code>&lt;Key&gt;</code> is the name of a type of event, but it must be modified by the <i>details</i> field to name a specific event, such as <code>&lt;Key&gt;</code><code>A</code>. </p>
<p> <code>Modifier Names</code> The modifier list, which may be empty, consists of a list of modifier keys that must be pressed with the key sequence. The modifier keys may abbreviated with single letters, as in the following list of the familiar modifiers:</p>
<dl COMPACT>
<dt>s</p>
<dd>Shift</p>
<dt>c or&nbsp;<wbr>^</p>
<dd>Ctrl (Control)</p>
<dt>m or&nbsp;<wbr>$</p>
<dd>Meta</p>
<dt>a</p>
<dd>Alt</dl>
<p> Other modifiers are available, such as &quot;Mod5&quot; and &quot;Button2.&quot; These have no abbreviation (although the &quot;Button&quot; modifiers may be abbreviated in combination with events, as outlined below). If a modifier list has no entries, and is not &quot;None&quot;, it means the position of the modifier keys is irrelevant. If modifiers are listed, the designated keys must be in the specified position, but the unlisted modifier keys are irrelevant. If the list begins with an exclamation point (!), however, the unlisted modifiers may not be asserted. In addition, if a modifier name is preceded by a tilde (~), the corresponding key must <i>not</i> be pressed. </p>
<p> If a modifier list begins with a colon (:), X tries to use the standard modifiers (Shift and Lock), if present, to map the key event code into a recognized keysym. </p>
<p> Event Types These are a few of the recognized event types.</p>
<dl COMPACT>
<dt>Key or KeyDown</p>
<dd>A keyboard key was pressed.</p>
<dt>KeyUp</p>
<dd>A keyboard key was released.</p>
<dt>BtnDown</p>
<dd>A mouse button was pressed.</p>
<dt>BtnUp</p>
<dd>A mouse button was released.</p>
<dt>Motion</p>
<dd>The mouse pointer moved.</p>
<dt>Enter</p>
<dd>The pointer entered the widget&#8217;s window.</p>
<dt>Leave</p>
<dd>The pointer left the widget&#8217;s window.</p>
<dt>FocusIn</p>
<dd>The widget has received focus.</p>
<dt>FocusOut</p>
<dd>The widget has lost focus.</dl>
<p> There are some event abbreviations available. For example, <code>&lt;Btn1Motion&gt;</code> is actually a &quot;Motion&quot; event, modified with the &quot;Button1&quot; modifier (<code>Button1&lt;Motion&gt;</code>). Similarly, <code>&lt;Btn3Up&gt;</code> is actually a &quot;BtnUp&quot; event with the &quot;Button3&quot; modifier. These abbreviations are used extensively in the Motif translation tables.</p>
<h2>Related</h2>
<p><code><a href="/docs/linux/man/1-xmbind/">xmbind</a></code>(1)</p>
