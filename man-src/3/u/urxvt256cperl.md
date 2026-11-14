---
title: "urxvt256cperl(3)"
name: "urxvt256cperl"
section: "3"
letter: "u"
url: "/docs/linux/man/3-urxvt256cperl/"
description: "urxvtperl – rxvt-unicode’s embedded perl interpreter"
---

<p>urxvtperl &#8211; rxvt-unicode&#8217;s embedded perl interpreter</p>
<h2>Synopsis</h2>
<pre> # create a file grab_test in $HOME:
 sub on_sel_grab {
 warn &quot;you selected &quot;, $_[0]-&gt;selection;
 ()
 }
 # start a urxvt using it:
 urxvt --perl-lib $HOME -pe grab_test</pre>
<h2>Description</h2>
<p>Every time a terminal object gets created, extension scripts specified via the <tt>&quot;perl&quot;</tt> resource are loaded and associated with it. </p>
<p> Scripts are compiled in a &#8216;use strict &#8220;vars&#8221;&#8217; and &#8216;use utf8&#8217; environment, and thus must be encoded as <font SIZE="-1">UTF-8.</font> </p>
<p> Each script will only ever be loaded once, even in urxvtd, where scripts will be shared (but not enabled) for all terminals. </p>
<p> You can disable the embedded perl interpreter by setting both &#8220;perl-ext&#8221; and &#8220;perl-ext-common&#8221; resources to the empty string.</p>
<h2>Prepackaged Extensions</h2>
<p>A number of extensions are delivered with this release. You can find them in <i>&lt;libdir&gt;/urxvt/perl/</i>, and the documentation can be viewed using <i>man urxvt-&lt;</i><font SIZE="-1"><i>EXTENSIONNAME</i></font><i>&gt;</i>. </p>
<p> You can activate them like this: </p>
<pre> urxvt -pe &lt;extensionname&gt;</pre>
<p>Or by adding them to the resource for extensions loaded by default: </p>
<pre> URxvt.perl-ext-common: default,selection-autotransform</pre>
<p>Extensions may add additional resources and <tt>&quot;actions&quot;</tt>, i.e., methods which can be bound to a key and invoked by the user. An extension can define the resources it support using so called <font SIZE="-1">META</font> comments, described below. Similarly to builtin resources, extension resources can also be specified on the command line as long options (with <tt>&quot;.&quot;</tt> replaced by <tt>&quot;-&quot;</tt>), in which case the corresponding extension is loaded automatically. For this to work the extension <code>must</code> define <font SIZE="-1">META</font> comments for its resources.</p>
<h2>Api Documentation</h2>
<h3>General <font SIZE="-1">API</font> Considerations</h3>
<p>All objects (such as terminals, time watchers etc.) are typical reference-to-hash objects. The hash can be used to store anything you like. All members starting with an underscore (such as <tt>&quot;_ptr&quot;</tt> or <tt>&quot;_hook&quot;</tt>) are reserved for internal uses and <font SIZE="-1"><code>MUST NOT</code></font> be accessed or modified). </p>
<p> When objects are destroyed on the C<font SIZE="-2">++</font> side, the perl object hashes are emptied, so its best to store related objects such as time watchers and the like inside the terminal object so they get destroyed as soon as the terminal is destroyed. </p>
<p> Argument names also often indicate the type of a parameter. Here are some hints on what they mean:</p>
<dl>
<dt>$text</p>
<dd>Rxvt-unicode&#8217;s special way of encoding text, where one &#8220;unicode&#8221; character always represents one screen cell. See ROW_t for a discussion of this format.</p>
<dt>$string</p>
<dd>A perl text string, with an emphasis on <i>text</i>. It can store all unicode characters and is to be distinguished with text encoded in a specific encoding (often locale-specific) and binary data.</p>
<dt>$octets</p>
<dd>Either binary data or &#8211; more common &#8211; a text string encoded in a locale-specific way.</p>
<dt>$keysym</p>
<dd>an integer that is a valid X11 keysym code. You can convert a string into a keysym and viceversa by using <tt>&quot;XStringToKeysym&quot;</tt> and <tt>&quot;XKeysymToString&quot;</tt>.</dl>
<h3>Extension Objects</h3>
<p>Every perl extension is a perl class. A separate perl object is created for each terminal, and each terminal has its own set of extension objects, which are passed as the first parameter to hooks. So extensions can use their <tt>$self</tt> object without having to think about clashes with other extensions or other terminals, with the exception of methods and members that begin with an underscore character <tt>&quot;_&quot;</tt>: these are reserved for internal use. </p>
<p> Although it isn&#8217;t a <tt>&quot;urxvt::term&quot;</tt> object, you can call all methods of the <tt>&quot;urxvt::term&quot;</tt> class on this object. </p>
<p> Additional methods only supported for extension objects are described in the <tt>&quot;urxvt::extension&quot;</tt> section below.</p>
<h3><font SIZE="-1">META</font> comments</h3>
<p>Rxvt-unicode recognizes special meta comments in extensions that define different types of metadata. </p>
<p> Currently, it recognises only one such comment:</p>
<dl>
<dt>#:META:RESOURCE:name:type:desc</p>
<dd>The <font SIZE="-1">RESOURCE</font> comment defines a resource used by the extension, where <tt>&quot;name&quot;</tt> is the resource name, <tt>&quot;type&quot;</tt> is the resource type, <tt>&quot;boolean&quot;</tt> or <tt>&quot;string&quot;</tt>, and <tt>&quot;desc&quot;</tt> is the resource description.</dl>
<h3>Hooks</h3>
<p>The following subroutines can be declared in extension files, and will be called whenever the relevant event happens. </p>
<p> The first argument passed to them is an extension object as described in the in the <tt>&quot;Extension Objects&quot;</tt> section. </p>
<p> <code>All</code> of these hooks must return a boolean value. If any of the called hooks returns true, then the event counts as being <i>consumed</i>, and the relevant action might not be carried out by the C<font SIZE="-2">++</font> code. </p>
<p> <i>When in doubt, return a false value (preferably </i>&quot;()&quot;<i>).</i></p>
<dl>
<dt>on_init $term</p>
<dd>Called after a new terminal object has been initialized, but before windows are created or the command gets run. Most methods are unsafe to call or deliver senseless data, as terminal size and other characteristics have not yet been determined. You can safely query and change resources and options, though. For many purposes the <tt>&quot;on_start&quot;</tt> hook is a better place.</p>
<dt>on_start $term</p>
<dd>Called at the very end of initialisation of a new terminal, just before trying to map (display) the toplevel and returning to the main loop.</p>
<dt>on_destroy $term</p>
<dd>Called whenever something tries to destroy terminal, when the terminal is still fully functional (not for long, though).</p>
<dt>on_reset $term</p>
<dd>Called after the screen is &#8220;reset&#8221; for any reason, such as resizing or control sequences. Here is where you can react on changes to size-related variables.</p>
<dt>on_child_start $term, $pid</p>
<dd>Called just after the child process has been <tt>&quot;fork&quot;</tt>ed.</p>
<dt>on_child_exit $term, $status</p>
<dd>Called just after the child process has exited. <tt>$status</tt> is the status from <tt>&quot;waitpid&quot;</tt>.</p>
<dt>on_sel_make $term, $eventtime</p>
<dd>Called whenever a selection has been made by the user, but before the selection text is copied, so changes to the beginning, end or type of the selection will be honored. </p>
<p> Returning a true value aborts selection making by urxvt, in which case you have to make a selection yourself by calling <tt>&quot;$term-&gt;selection_grab&quot;</tt>.</p>
<dt>on_sel_grab $term, $eventtime</p>
<dd>Called whenever a selection has been copied, but before the selection is requested from the server. The selection text can be queried and changed by calling <tt>&quot;$term-&gt;selection&quot;</tt>. </p>
<p> Returning a true value aborts selection grabbing. It will still be highlighted.</p>
<dt>on_sel_extend $term</p>
<dd>Called whenever the user tries to extend the selection (e.g. with a double click) and is either supposed to return false (normal operation), or should extend the selection itself and return true to suppress the built-in processing. This can happen multiple times, as long as the callback returns true, it will be called on every further click by the user and is supposed to enlarge the selection more and more, if possible. </p>
<p> See the <i>selection</i> example extension.</p>
<dt>on_view_change $term, $offset</p>
<dd>Called whenever the view offset changes, i.e. the user or program scrolls. Offset <tt>0</tt> means display the normal terminal, positive values show this many lines of scrollback.</p>
<dt>on_scroll_back $term, $lines, $saved</p>
<dd>Called whenever lines scroll out of the terminal area into the scrollback buffer. <tt>$lines</tt> is the number of lines scrolled out and may be larger than the scroll back buffer or the terminal. </p>
<p> It is called before lines are scrolled out (so rows 0 .. min ($lines &#8211; 1, <tt>$nrow</tt> &#8211; 1) represent the lines to be scrolled out). <tt>$saved</tt> is the total number of lines that will be in the scrollback buffer.</p>
<dt>on_osc_seq $term, $op, $args, $resp</p>
<dd>Called on every <font SIZE="-1">OSC</font> sequence and can be used to suppress it or modify its behaviour. The default should be to return an empty list. A true value suppresses execution of the request completely. Make sure you don&#8217;t get confused by recursive invocations when you output an <font SIZE="-1">OSC</font> sequence within this callback. </p>
<p> <tt>&quot;on_osc_seq_perl&quot;</tt> should be used for new behaviour.</p>
<dt>on_osc_seq_perl $term, $args, $resp</p>
<dd>Called whenever the <font SIZE="-1"><code>ESC </code></font><code>] 777 ; string </code><font SIZE="-1"><code>ST</code></font> command sequence (<font SIZE="-1">OSC</font> = operating system command) is processed. Cursor position and other state information is up-to-date when this happens. For interoperability, the string should start with the extension name (sans -osc) and a semicolon, to distinguish it from commands for other extensions, and this might be enforced in the future. </p>
<p> For example, <tt>&quot;overlay-osc&quot;</tt> uses this: </p>
<pre> sub on_osc_seq_perl {
 my ($self, $osc, $resp) = @_;
 return unless $osc =~ s/^overlay;//;
 ... process remaining $osc string
 }</pre>
<p>Be careful not ever to trust (in a security sense) the data you receive, as its source can not easily be controlled (e-mail content, messages from other users on the same system etc.). </p>
<p> For responses, <tt>$resp</tt> contains the end-of-args separator used by the sender.</p>
<dt>on_add_lines $term, $string</p>
<dd>Called whenever text is about to be output, with the text as argument. You can filter/change and output the text yourself by returning a true value and calling <tt>&quot;$term-&gt;scr_add_lines&quot;</tt> yourself. Please note that this might be very slow, however, as your hook is called for <code>all</code> text being output.</p>
<dt>on_tt_write $term, $octets</p>
<dd>Called whenever some data is written to the tty/pty and can be used to suppress or filter tty input.</p>
<dt>on_tt_paste $term, $octets</p>
<dd>Called whenever text is about to be pasted, with the text as argument. You can filter/change and paste the text yourself by returning a true value and calling <tt>&quot;$term-&gt;tt_paste&quot;</tt> yourself. <tt>$octets</tt> is locale-encoded.</p>
<dt>on_line_update $term, $row</p>
<dd>Called whenever a line was updated or changed. Can be used to filter screen output (e.g. underline urls or other useless stuff). Only lines that are being shown will be filtered, and, due to performance reasons, not always immediately. </p>
<p> The row number is always the topmost row of the line if the line spans multiple rows. </p>
<p> Please note that, if you change the line, then the hook might get called later with the already-modified line (e.g. if unrelated parts change), so you cannot just toggle rendition bits, but only set them.</p>
<dt>on_refresh_begin $term</p>
<dd>Called just before the screen gets redrawn. Can be used for overlay or similar effects by modifying the terminal contents in refresh_begin, and restoring them in refresh_end. The built-in overlay and selection display code is run after this hook, and takes precedence.</p>
<dt>on_refresh_end $term</p>
<dd>Called just after the screen gets redrawn. See <tt>&quot;on_refresh_begin&quot;</tt>.</p>
<dt>on_action $term, $string</p>
<dd>Called whenever an action is invoked for the corresponding extension (e.g. via a <tt>&quot;extension:string&quot;</tt> builtin action bound to a key, see description of the <code>keysym</code> resource in the <i><a href="/docs/linux/man/1-urxvt/">urxvt</a></i>(1) manpage). The event is simply the action string. Note that an action event is always associated to a single extension.</p>
<dt>on_user_command $term, $string *DEPRECATED*</p>
<dd>Called whenever a user-configured event is being activated (e.g. via a <tt>&quot;perl:string&quot;</tt> action bound to a key, see description of the <code>keysym</code> resource in the <i><a href="/docs/linux/man/1-urxvt/">urxvt</a></i>(1) manpage). </p>
<p> The event is simply the action string. This interface is going away in preference to the <tt>&quot;on_action&quot;</tt> hook.</p>
<dt>on_resize_all_windows $term, $new_width, $new_height</p>
<dd>Called just after the new window size has been calculated, but before windows are actually being resized or hints are being set. If this hook returns a true value, setting of the window hints is being skipped.</p>
<dt>on_x_event $term, $event</p>
<dd>Called on every X event received on the vt window (and possibly other windows). Should only be used as a last resort. Most event structure members are not passed.</p>
<dt>on_root_event $term, $event</p>
<dd>Like <tt>&quot;on_x_event&quot;</tt>, but is called for events on the root window.</p>
<dt>on_focus_in $term</p>
<dd>Called whenever the window gets the keyboard focus, before rxvt-unicode does focus in processing.</p>
<dt>on_focus_out $term</p>
<dd>Called whenever the window loses keyboard focus, before rxvt-unicode does focus out processing.</p>
<dt>on_configure_notify $term, $event</p>
<dd>
<dt>on_property_notify $term, $event</p>
<dd>
<dt>on_key_press $term, $event, $keysym, $octets</p>
<dd>
<dt>on_key_release $term, $event, $keysym</p>
<dd>
<dt>on_button_press $term, $event</p>
<dd>
<dt>on_button_release $term, $event</p>
<dd>
<dt>on_motion_notify $term, $event</p>
<dd>
<dt>on_map_notify $term, $event</p>
<dd>
<dt>on_unmap_notify $term, $event</p>
<dd>Called whenever the corresponding X event is received for the terminal. If the hook returns true, then the event will be ignored by rxvt-unicode. </p>
<p> The event is a hash with most values as named by Xlib (see the XEvent manpage), with the additional members <tt>&quot;row&quot;</tt> and <tt>&quot;col&quot;</tt>, which are the (real, not screen-based) row and column under the mouse cursor. </p>
<p> <tt>&quot;on_key_press&quot;</tt> additionally receives the string rxvt-unicode would output, if any, in locale-specific encoding.</p>
<dt>on_client_message $term, $event</p>
<dd>
<dt>on_wm_protocols $term, $event</p>
<dd>
<dt>on_wm_delete_window $term, $event</p>
<dd>Called when various types of ClientMessage events are received (all with format=32, <font SIZE="-1">WM_PROTOCOLS</font> or <font SIZE="-1">WM_PROTOCOLS:WM_DELETE_WINDOW</font>).</p>
<dt>on_bell $term</p>
<dd>Called on receipt of a bell character.</dl>
<h3>Variables in the urxvt Package</h3>
<dl>
<dt>$urxvt::LIBDIR</p>
<dd>The rxvt-unicode library directory, where, among other things, the perl modules and scripts are stored.</p>
<dt>$urxvt::RESCLASS, $urxvt::RESCLASS</p>
<dd>The resource class and name rxvt-unicode uses to look up X resources.</p>
<dt>$urxvt::RXVTNAME</p>
<dd>The basename of the installed binaries, usually <tt>&quot;urxvt&quot;</tt>.</p>
<dt>$urxvt::TERM</p>
<dd>The current terminal. This variable stores the current <tt>&quot;urxvt::term&quot;</tt> object, whenever a callback/hook is executing.</p>
<dt>@urxvt::TERM_INIT</p>
<dd>All code references in this array will be called as methods of the next newly created <tt>&quot;urxvt::term&quot;</tt> object (during the <tt>&quot;on_init&quot;</tt> phase). The array gets cleared before the code references that were in it are being executed, so references can push themselves onto it again if they so desire. </p>
<p> This complements to the perl-eval command line option, but gets executed first.</p>
<dt>@urxvt::TERM_EXT</p>
<dd>Works similar to <tt>@TERM_INIT</tt>, but contains perl package/class names, which get registered as normal extensions after calling the hooks in <tt>@TERM_INIT</tt> but before other extensions. Gets cleared just like <tt>@TERM_INIT</tt>.</dl>
<h3>Functions in the urxvt Package</h3>
<dl>
<dt>urxvt::fatal $errormessage</p>
<dd>Fatally aborts execution with the given error message (which should include a trailing newline). Avoid at all costs! The only time this is acceptable (and useful) is in the init hook, where it prevents the terminal from starting up.</p>
<dt>urxvt::warn $string</p>
<dd>Calls <tt>&quot;rxvt_warn&quot;</tt> with the given string which should include a trailing newline. The module also overwrites the <tt>&quot;warn&quot;</tt> builtin with a function that calls this function. </p>
<p> Using this function has the advantage that its output ends up in the correct place, e.g. on stderr of the connecting urxvtc client. </p>
<p> Messages have a size limit of 1023 bytes currently.</p>
<dt>@terms = urxvt::termlist</p>
<dd>Returns all urxvt::term objects that exist in this process, regardless of whether they are started, being destroyed etc., so be careful. Only term objects that have perl extensions attached will be returned (because there is no urxvt::term object associated with others).</p>
<dt>$time = urxvt::NOW</p>
<dd>Returns the &#8220;current time&#8221; (as per the event loop).</p>
<dt>urxvt::CurrentTime</p>
<dd>
<dt>urxvt::ShiftMask, LockMask, ControlMask, Mod1Mask, Mod2Mask, Mod3Mask, Mod4Mask, Mod5Mask, Button1Mask, Button2Mask, Button3Mask, Button4Mask, Button5Mask, AnyModifier</p>
<dd>
<dt>urxvt::NoEventMask, KeyPressMask, KeyReleaseMask, ButtonPressMask, ButtonReleaseMask, EnterWindowMask, LeaveWindowMask, PointerMotionMask, PointerMotionHintMask, Button1MotionMask, Button2MotionMask, Button3MotionMask, Button4MotionMask, Button5MotionMask, ButtonMotionMask, KeymapStateMask, ExposureMask, VisibilityChangeMask, StructureNotifyMask, ResizeRedirectMask, SubstructureNotifyMask, SubstructureRedirectMask, FocusChangeMask, PropertyChangeMask, ColormapChangeMask, OwnerGrabButtonMask</p>
<dd>
<dt>urxvt::KeyPress, KeyRelease, ButtonPress, ButtonRelease, MotionNotify, EnterNotify, LeaveNotify, FocusIn, FocusOut, KeymapNotify, Expose, GraphicsExpose, NoExpose, VisibilityNotify, CreateNotify, DestroyNotify, UnmapNotify, MapNotify, MapRequest, ReparentNotify, ConfigureNotify, ConfigureRequest, GravityNotify, ResizeRequest, CirculateNotify, CirculateRequest, PropertyNotify, SelectionClear, SelectionRequest, SelectionNotify, ColormapNotify, ClientMessage, MappingNotify</p>
<dd>Various constants for use in X calls and event processing.</dl>
<h3><font SIZE="-1">RENDITION</font></h3>
<p>Rendition bitsets contain information about colour, font, font styles and similar information for each screen cell. </p>
<p> The following &#8220;macros&#8221; deal with changes in rendition sets. You should never just create a bitset, you should always modify an existing one, as they contain important information required for correct operation of rxvt-unicode.</p>
<dl>
<dt>$rend = urxvt::DEFAULT_RSTYLE</p>
<dd>Returns the default rendition, as used when the terminal is starting up or being reset. Useful as a base to start when creating renditions.</p>
<dt>$rend = urxvt::OVERLAY_RSTYLE</p>
<dd>Return the rendition mask used for overlays by default.</p>
<dt>$rendbit = urxvt::RS_Bold, urxvt::RS_Italic, urxvt::RS_Blink, urxvt::RS_RVid, urxvt::RS_Uline</p>
<dd>Return the bit that enabled bold, italic, blink, reverse-video and underline, respectively. To enable such a style, just logically <font SIZE="-1">OR</font> it into the bitset.</p>
<dt>$foreground = urxvt::GET_BASEFG $rend</p>
<dd>
<dt>$background = urxvt::GET_BASEBG $rend</p>
<dd>Return the foreground/background colour index, respectively.</p>
<dt>$rend = urxvt::SET_FGCOLOR $rend, $new_colour</p>
<dd>
<dt>$rend = urxvt::SET_BGCOLOR $rend, $new_colour</p>
<dd>
<dt>$rend = urxvt::SET_COLOR $rend, $new_fg, $new_bg</p>
<dd>Replace the foreground/background colour in the rendition mask with the specified one.</p>
<dt>$value = urxvt::GET_CUSTOM $rend</p>
<dd>Return the &#8220;custom&#8221; value: Every rendition has 5 bits for use by extensions. They can be set and changed as you like and are initially zero.</p>
<dt>$rend = urxvt::SET_CUSTOM $rend, $new_value</p>
<dd>Change the custom value.</dl>
<h3>The urxvt::term::extension class</h3>
<p>Each extension attached to a terminal object is represented by a <tt>&quot;urxvt::term::extension&quot;</tt> object. </p>
<p> You can use these objects, which are passed to all callbacks to store any state related to the terminal and extension instance. </p>
<p> The methods (And data members) documented below can be called on extension objects, in addition to call methods documented for the &lt;urxvt::term&gt; class.</p>
<dl>
<dt>$urxvt_term = $self-&gt;{term}</p>
<dd>Returns the <tt>&quot;urxvt::term&quot;</tt> object associated with this instance of the extension. This member <i>must not</i> be changed in any way.</p>
<dt>$self-&gt;enable ($hook_name =&gt; $cb[, $hook_name =&gt; $cb..])</p>
<dd>Dynamically enable the given hooks (named without the <tt>&quot;on_&quot;</tt> prefix) for this extension, replacing any hook previously installed via <tt>&quot;enable&quot;</tt> in this extension. </p>
<p> This is useful when you want to overwrite time-critical hooks only temporarily. </p>
<p> To install additional callbacks for the same hook, you can use the <tt>&quot;on&quot;</tt> method of the <tt>&quot;urxvt::term&quot;</tt> class.</p>
<dt>$self-&gt;disable ($hook_name[, $hook_name..])</p>
<dd>Dynamically disable the given hooks.</p>
<dt>$guard = $self-&gt;on ($hook_name =&gt; $cb[, $hook_name =&gt; $cb..])</p>
<dd>Similar to the <tt>&quot;enable&quot;</tt> enable, but installs additional callbacks for the given hook(s) (that is, it doesn&#8217;t replace existing callbacks), and returns a guard object. When the guard object is destroyed the callbacks are disabled again.</p>
<dt>$self-&gt;bind_action ($hotkey, $action)</p>
<dd>
<dt>$self-&gt;x_resource ($pattern)</p>
<dd>
<dt>$self-&gt;x_resource_boolean ($pattern)</p>
<dd>These methods support an additional <tt>&quot;%&quot;</tt> prefix for <tt>$action</tt> or <tt>$pattern</tt> when called on an extension object, compared to the <tt>&quot;urxvt::term&quot;</tt> methods of the same name &#8211; see the description of these methods in the <tt>&quot;urxvt::term&quot;</tt> class for details.</dl>
<h3>The urxvt::anyevent Class</h3>
<p>The sole purpose of this class is to deliver an interface to the <tt>&quot;AnyEvent&quot;</tt> module &#8211; any module using it will work inside urxvt without further programming. The only exception is that you cannot wait on condition variables, but non-blocking condvar use is ok. </p>
<p> In practical terms this means is that you cannot use blocking APIs, but the non-blocking variant should work.</p>
<h3>The urxvt::term Class</h3>
<dl>
<dt>$term = new urxvt::term $envhashref, $rxvtname, [arg&#8230;]</p>
<dd>Creates a new terminal, very similar as if you had started it with system <tt>&quot;$rxvtname, arg...&quot;</tt>. <tt>$envhashref</tt> must be a reference to a <tt>%ENV</tt>-like hash which defines the environment of the new terminal. </p>
<p> Croaks (and probably outputs an error message) if the new instance couldn&#8217;t be created. Returns <tt>&quot;undef&quot;</tt> if the new instance didn&#8217;t initialise perl, and the terminal object otherwise. The <tt>&quot;init&quot;</tt> and <tt>&quot;start&quot;</tt> hooks will be called before this call returns, and are free to refer to global data (which is race free).</p>
<dt>$term-&gt;destroy</p>
<dd>Destroy the terminal object (close the window, free resources etc.). Please note that urxvt will not exit as long as any event watchers (timers, io watchers) are still active.</p>
<dt>$term-&gt;exec_async ($cmd[, @args])</p>
<dd>Works like the combination of the <tt>&quot;fork&quot;</tt>/<tt>&quot;exec&quot;</tt> builtins, which executes (&#8220;starts&#8221;) programs in the background. This function takes care of setting the user environment before exec&#8217;ing the command (e.g. <tt>&quot;PATH&quot;</tt>) and should be preferred over explicit calls to <tt>&quot;exec&quot;</tt> or <tt>&quot;system&quot;</tt>. </p>
<p> Returns the pid of the subprocess or <tt>&quot;undef&quot;</tt> on error.</p>
<dt>$isset = $term-&gt;option ($optval[, $set])</p>
<dd>Returns true if the option specified by <tt>$optval</tt> is enabled, and optionally change it. All option values are stored by name in the hash <tt>%urxvt::OPTION</tt>. Options not enabled in this binary are not in the hash. </p>
<p> Here is a likely non-exhaustive list of option names, please see the source file <i>/src/optinc.h</i> to see the actual list: </p>
<pre> borderLess buffered console cursorBlink cursorUnderline hold iconic
 insecure intensityStyles iso14755 iso14755_52 jumpScroll loginShell
 mapAlert meta8 mouseWheelScrollPage override_redirect pastableTabs
 pointerBlank reverseVideo scrollBar scrollBar_floating scrollBar_right
 scrollTtyKeypress scrollTtyOutput scrollWithBuffer secondaryScreen
 secondaryScroll skipBuiltinGlyphs skipScroll transparent tripleclickwords
 urgentOnBell utmpInhibit visualBell</pre>
<dt>$value = $term-&gt;resource ($name[, $newval])</p>
<dd>Returns the current resource value associated with a given name and optionally sets a new value. Setting values is most useful in the <tt>&quot;init&quot;</tt> hook. Unset resources are returned and accepted as <tt>&quot;undef&quot;</tt>. </p>
<p> The new value must be properly encoded to a suitable character encoding before passing it to this method. Similarly, the returned value may need to be converted from the used encoding to text. </p>
<p> Resource names are as defined in <i>src/rsinc.h</i>. Colours can be specified as resource names of the form <tt>&quot;color+&lt;index&gt;&quot;</tt>, e.g. <tt>&quot;color+5&quot;</tt>. (will likely change). </p>
<p> Please note that resource strings will currently only be freed when the terminal is destroyed, so changing options frequently will eat memory. </p>
<p> Here is a likely non-exhaustive list of resource names, not all of which are supported in every build, please see the source file <i>/src/rsinc.h</i> to see the actual list: </p>
<pre> answerbackstring backgroundPixmap backspace_key blurradius
 boldFont boldItalicFont borderLess buffered chdir color cursorBlink
 cursorUnderline cutchars delete_key depth display_name embed ext_bwidth
 fade font geometry hold iconName iconfile imFont imLocale inputMethod
 insecure int_bwidth intensityStyles iso14755 iso14755_52 italicFont
 jumpScroll letterSpace lineSpace loginShell mapAlert meta8 modifier
 mouseWheelScrollPage name override_redirect pastableTabs path perl_eval
 perl_ext_1 perl_ext_2 perl_lib pointerBlank pointerBlankDelay
 preeditType print_pipe pty_fd reverseVideo saveLines scrollBar
 scrollBar_align scrollBar_floating scrollBar_right scrollBar_thickness
 scrollTtyKeypress scrollTtyOutput scrollWithBuffer scrollstyle
 secondaryScreen secondaryScroll shade skipBuiltinGlyphs skipScroll
 term_name title transient_for transparent tripleclickwords urgentOnBell
 utmpInhibit visualBell</pre>
<dt>$value = $term-&gt;x_resource ($pattern)</p>
<dd>Returns the X-Resource for the given pattern, excluding the program or class name, i.e. <tt>&quot;$term-&gt;x_resource (&quot;boldFont&quot;)&quot;</tt> should return the same value as used by this instance of rxvt-unicode. Returns <tt>&quot;undef&quot;</tt> if no resource with that pattern exists. </p>
<p> Extensions that define extra resources also need to call this method to access their values. </p>
<p> If the method is called on an extension object (basically, from an extension), then the special prefix <tt>&quot;%.&quot;</tt> will be replaced by the name of the extension and a dot, and the lone string <tt>&quot;%&quot;</tt> will be replaced by the extension name itself. This makes it possible to code extensions so you can rename them and get a new set of resources without having to change the actual code. </p>
<p> This method should only be called during the <tt>&quot;on_start&quot;</tt> hook, as there is only one resource database per display, and later invocations might return the wrong resources.</p>
<dt>$value = $term-&gt;x_resource_boolean ($pattern)</p>
<dd>Like <tt>&quot;x_resource&quot;</tt>, above, but interprets the string value as a boolean and returns <tt>1</tt> for true values, <tt>0</tt> for false values and <tt>&quot;undef&quot;</tt> if the resource or option isn&#8217;t specified. </p>
<p> You should always use this method to parse boolean resources.</p>
<dt>$success = $term-&gt;bind_action ($key, $action)</p>
<dd>Adds a key binding exactly as specified via a <tt>&quot;keysym&quot;</tt> resource. See the <tt>&quot;keysym&quot;</tt> resource in the <i><a href="/docs/linux/man/1-urxvt/">urxvt</a></i>(1) manpage. </p>
<p> To add default bindings for actions, an extension should call <tt>&quot;-&gt;bind_action&quot;</tt> in its <tt>&quot;init&quot;</tt> hook for every such binding. Doing it in the <tt>&quot;init&quot;</tt> hook allows users to override or remove the binding again. </p>
<p> Example: the <tt>&quot;searchable-scrollback&quot;</tt> by default binds itself on <tt>&quot;Meta-s&quot;</tt>, using <tt>&quot;$self-&gt;bind_action&quot;</tt>, which calls <tt>&quot;$term-&gt;bind_action&quot;</tt>. </p>
<pre> sub init {
 my ($self) = @_;
 $self-&gt;bind_action (&quot;M-s&quot; =&gt; &quot;%:start&quot;);
 }</pre>
<dt>$rend = $term-&gt;rstyle ([$new_rstyle])</p>
<dd>Return and optionally change the current rendition. Text that is output by the terminal application will use this style.</p>
<dt>($row, $col) = $term-&gt;screen_cur ([$row, $col])</p>
<dd>Return the current coordinates of the text cursor position and optionally set it (which is usually bad as applications don&#8217;t expect that).</p>
<dt>($row, $col) = $term-&gt;selection_mark ([$row, $col])</p>
<dd>
<dt>($row, $col) = $term-&gt;selection_beg ([$row, $col])</p>
<dd>
<dt>($row, $col) = $term-&gt;selection_end ([$row, $col])</p>
<dd>Return the current values of the selection mark, begin or end positions. </p>
<p> When arguments are given, then the selection coordinates are set to <tt>$row</tt> and <tt>$col</tt>, and the selection screen is set to the current screen.</p>
<dt>$screen = $term-&gt;selection_screen ([$screen])</p>
<dd>Returns the current selection screen, and then optionally sets it.</p>
<dt>$term-&gt;selection_make ($eventtime[, $rectangular])</p>
<dd>Tries to make a selection as set by <tt>&quot;selection_beg&quot;</tt> and <tt>&quot;selection_end&quot;</tt>. If <tt>$rectangular</tt> is true (default: false), a rectangular selection will be made. This is the preferred function to make a selection.</p>
<dt>$success = $term-&gt;selection_grab ($eventtime[, $clipboard])</p>
<dd>Try to acquire ownership of the primary (clipboard if <tt>$clipboard</tt> is true) selection from the server. The corresponding text can be set with the next method. No visual feedback will be given. This function is mostly useful from within <tt>&quot;on_sel_grab&quot;</tt> hooks.</p>
<dt>$oldtext = $term-&gt;selection ([$newtext, $clipboard])</p>
<dd>Return the current selection (clipboard if <tt>$clipboard</tt> is true) text and optionally replace it by <tt>$newtext</tt>.</p>
<dt>$term-&gt;selection_clear ([$clipboard])</p>
<dd>Revoke ownership of the primary (clipboard if <tt>$clipboard</tt> is true) selection.</p>
<dt>$term-&gt;overlay_simple ($x, $y, $text)</p>
<dd>Create a simple multi-line overlay box. See the next method for details.</p>
<dt>$term-&gt;overlay ($x, $y, $width, $height[, $rstyle[, $border]])</p>
<dd>Create a new (empty) overlay at the given position with the given width/height. <tt>$rstyle</tt> defines the initial rendition style (default: <tt>&quot;OVERLAY_RSTYLE&quot;</tt>). </p>
<p> If <tt>$border</tt> is <tt>2</tt> (default), then a decorative border will be put around the box. </p>
<p> If either <tt>$x</tt> or <tt>$y</tt> is negative, then this is counted from the right/bottom side, respectively. </p>
<p> This method returns an urxvt::overlay object. The overlay will be visible as long as the perl object is referenced. </p>
<p> The methods currently supported on <tt>&quot;urxvt::overlay&quot;</tt> objects are:</p>
<dl>
<dd>
<dl>
<dt>$overlay-&gt;set ($x, $y, $text[, $rend])</p>
<dd>Similar to <tt>&quot;$term-&gt;ROW_t&quot;</tt> and <tt>&quot;$term-&gt;ROW_r&quot;</tt> in that it puts text in rxvt-unicode&#8217;s special encoding and an array of rendition values at a specific position inside the overlay. </p>
<p> If <tt>$rend</tt> is missing, then the rendition will not be changed.</p>
<dt>$overlay-&gt;hide</p>
<dd>If visible, hide the overlay, but do not destroy it.</p>
<dt>$overlay-&gt;show</p>
<dd>If hidden, display the overlay again.</dl>
</dl>
<dl>
<dd></dl>
<dt>$popup = $term-&gt;popup ($event)</p>
<dd>Creates a new <tt>&quot;urxvt::popup&quot;</tt> object that implements a popup menu. The <tt>$event</tt> <i>must</i> be the event causing the menu to pop up (a button event, currently).</p>
<dt>$cellwidth = $term-&gt;strwidth ($string)</p>
<dd>Returns the number of screen-cells this string would need. Correctly accounts for wide and combining characters.</p>
<dt>$octets = $term-&gt;locale_encode ($string)</p>
<dd>Convert the given text string into the corresponding locale encoding.</p>
<dt>$string = $term-&gt;locale_decode ($octets)</p>
<dd>Convert the given locale-encoded octets into a perl string.</p>
<dt>$term-&gt;scr_xor_span ($beg_row, $beg_col, $end_row, $end_col[, $rstyle])</p>
<dd>XORs the rendition values in the given span with the provided value (default: <tt>&quot;RS_RVid&quot;</tt>), which <i></i><font SIZE="-1"><i>MUST NOT</i></font><i></i> contain font styles. Useful in refresh hooks to provide effects similar to the selection.</p>
<dt>$term-&gt;scr_xor_rect ($beg_row, $beg_col, $end_row, $end_col[, $rstyle1[, $rstyle2]])</p>
<dd>Similar to <tt>&quot;scr_xor_span&quot;</tt>, but xors a rectangle instead. Trailing whitespace will additionally be xored with the <tt>$rstyle2</tt>, which defaults to <tt>&quot;RS_RVid | RS_Uline&quot;</tt>, which removes reverse video again and underlines it instead. Both styles <i></i><font SIZE="-1"><i>MUST NOT</i></font><i></i> contain font styles.</p>
<dt>$term-&gt;scr_bell</p>
<dd>Ring the bell!</p>
<dt>$term-&gt;scr_add_lines ($string)</p>
<dd>Write the given text string to the screen, as if output by the application running inside the terminal. It may not contain command sequences (escape codes &#8211; see <tt>&quot;cmd_parse&quot;</tt> for that), but is free to use line feeds, carriage returns and tabs. The string is a normal text string, not in locale-dependent encoding. </p>
<p> Normally its not a good idea to use this function, as programs might be confused by changes in cursor position or scrolling. Its useful inside a <tt>&quot;on_add_lines&quot;</tt> hook, though.</p>
<dt>$term-&gt;scr_change_screen ($screen)</p>
<dd>Switch to given screen &#8211; 0 primary, 1 secondary.</p>
<dt>$term-&gt;cmd_parse ($octets)</p>
<dd>Similar to <tt>&quot;scr_add_lines&quot;</tt>, but the argument must be in the locale-specific encoding of the terminal and can contain command sequences (escape codes) that will be interpreted.</p>
<dt>$term-&gt;tt_write ($octets)</p>
<dd>Write the octets given in <tt>$octets</tt> to the tty (i.e. as user input to the program, see <tt>&quot;cmd_parse&quot;</tt> for the opposite direction). To pass characters instead of octets, you should convert your strings first to the locale-specific encoding using <tt>&quot;$term-&gt;locale_encode&quot;</tt>.</p>
<dt>$term-&gt;tt_write_user_input ($octets)</p>
<dd>Like <tt>&quot;tt_write&quot;</tt>, but should be used when writing strings in response to the user pressing a key, to invoke the additional actions requested by the user for that case (<tt>&quot;tt_write&quot;</tt> doesn&#8217;t do that). </p>
<p> The typical use case would be inside <tt>&quot;on_action&quot;</tt> hooks.</p>
<dt>$term-&gt;tt_paste ($octets)</p>
<dd>Write the octets given in <tt>$octets</tt> to the tty as a paste, converting <font SIZE="-1">NL</font> to <font SIZE="-1">CR</font> and bracketing the data with control sequences if bracketed paste mode is set.</p>
<dt>$old_events = $term-&gt;pty_ev_events ([$new_events])</p>
<dd>Replaces the event mask of the pty watcher by the given event mask. Can be used to suppress input and output handling to the pty/tty. See the description of <tt>&quot;urxvt::timer-&gt;events&quot;</tt>. Make sure to always restore the previous value.</p>
<dt>$fd = $term-&gt;pty_fd</p>
<dd>Returns the master file descriptor for the pty in use, or <tt>&quot;-1&quot;</tt> if no pty is used.</p>
<dt>$windowid = $term-&gt;parent</p>
<dd>Return the window id of the toplevel window.</p>
<dt>$windowid = $term-&gt;vt</p>
<dd>Return the window id of the terminal window.</p>
<dt>$term-&gt;vt_emask_add ($x_event_mask)</p>
<dd>Adds the specified events to the vt event mask. Useful e.g. when you want to receive pointer events all the times: </p>
<pre> $term-&gt;vt_emask_add (urxvt::PointerMotionMask);</pre>
<dt>$term-&gt;set_urgency ($set)</p>
<dd>Enable/disable the urgency hint on the toplevel window.</p>
<dt>$term-&gt;focus_in</p>
<dd>
<dt>$term-&gt;focus_out</p>
<dd>
<dt>$term-&gt;key_press ($state, $keycode[, $time])</p>
<dd>
<dt>$term-&gt;key_release ($state, $keycode[, $time])</p>
<dd>Deliver various fake events to to terminal.</p>
<dt>$window_width = $term-&gt;width</p>
<dd>
<dt>$window_height = $term-&gt;height</p>
<dd>
<dt>$font_width = $term-&gt;fwidth</p>
<dd>
<dt>$font_height = $term-&gt;fheight</p>
<dd>
<dt>$font_ascent = $term-&gt;fbase</p>
<dd>
<dt>$terminal_rows = $term-&gt;nrow</p>
<dd>
<dt>$terminal_columns = $term-&gt;ncol</p>
<dd>
<dt>$has_focus = $term-&gt;focus</p>
<dd>
<dt>$is_mapped = $term-&gt;mapped</p>
<dd>
<dt>$max_scrollback = $term-&gt;saveLines</p>
<dd>
<dt>$nrow_plus_saveLines = $term-&gt;total_rows</p>
<dd>
<dt>$topmost_scrollback_row = $term-&gt;top_row</p>
<dd>Return various integers describing terminal characteristics.</p>
<dt>$x_display = $term-&gt;display_id</p>
<dd>Return the <font SIZE="-1">DISPLAY</font> used by rxvt-unicode.</p>
<dt>$lc_ctype = $term-&gt;locale</p>
<dd>Returns the <font SIZE="-1">LC_CTYPE</font> category string used by this rxvt-unicode.</p>
<dt>$env = $term-&gt;env</p>
<dd>Returns a copy of the environment in effect for the terminal as a hashref similar to <tt>&quot;\%ENV&quot;</tt>.</p>
<dt>@envv = $term-&gt;envv</p>
<dd>Returns the environment as array of strings of the form <tt>&quot;VAR=VALUE&quot;</tt>.</p>
<dt>@argv = $term-&gt;argv</p>
<dd>Return the argument vector as this terminal, similar to <tt>@ARGV</tt>, but includes the program name as first element.</p>
<dt>$modifiermask = $term-&gt;ModLevel3Mask</p>
<dd>
<dt>$modifiermask = $term-&gt;ModMetaMask</p>
<dd>
<dt>$modifiermask = $term-&gt;ModNumLockMask</p>
<dd>Return the modifier masks corresponding to the &#8220;<font SIZE="-1">ISO</font> Level 3 Shift&#8221; (often AltGr), the meta key (often Alt) and the num lock key, if applicable.</p>
<dt>$screen = $term-&gt;current_screen</p>
<dd>Returns the currently displayed screen (0 primary, 1 secondary).</p>
<dt>$cursor_is_hidden = $term-&gt;hidden_cursor</p>
<dd>Returns whether the cursor is currently hidden or not.</p>
<dt>$view_start = $term-&gt;view_start ([$newvalue])</p>
<dd>Returns the row number of the topmost displayed line. Maximum value is <tt>0</tt>, which displays the normal terminal contents. Lower values scroll this many lines into the scrollback buffer.</p>
<dt>$term-&gt;want_refresh</p>
<dd>Requests a screen refresh. At the next opportunity, rxvt-unicode will compare the on-screen display with its stored representation. If they differ, it redraws the differences. </p>
<p> Used after changing terminal contents to display them.</p>
<dt>$text = $term-&gt;ROW_t ($row_number[, $new_text[, $start_col]])</p>
<dd>Returns the text of the entire row with number <tt>$row_number</tt>. Row <tt>&quot;$term-&gt;top_row&quot;</tt> is the topmost terminal line, row <tt>&quot;$term-&gt;nrow-1&quot;</tt> is the bottommost terminal line. Nothing will be returned if a nonexistent line is requested. </p>
<p> If <tt>$new_text</tt> is specified, it will replace characters in the current line, starting at column <tt>$start_col</tt> (default <tt>0</tt>), which is useful to replace only parts of a line. The font index in the rendition will automatically be updated. </p>
<p> <tt>$text</tt> is in a special encoding: tabs and wide characters that use more than one cell when displayed are padded with <tt>$urxvt::NOCHAR</tt> (chr 65535) characters. Characters with combining characters and other characters that do not fit into the normal text encoding will be replaced with characters in the private use area. </p>
<p> You have to obey this encoding when changing text. The advantage is that <tt>&quot;substr&quot;</tt> and similar functions work on screen cells and not on characters. </p>
<p> The methods <tt>&quot;$term-&gt;special_encode&quot;</tt> and <tt>&quot;$term-&gt;special_decode&quot;</tt> can be used to convert normal strings into this encoding and vice versa.</p>
<dt>$rend = $term-&gt;ROW_r ($row_number[, $new_rend[, $start_col]])</p>
<dd>Like <tt>&quot;$term-&gt;ROW_t&quot;</tt>, but returns an arrayref with rendition bitsets. Rendition bitsets contain information about colour, font, font styles and similar information. See also <tt>&quot;$term-&gt;ROW_t&quot;</tt>. </p>
<p> When setting rendition, the font mask will be ignored. </p>
<p> See the section on <font SIZE="-1">RENDITION,</font> above.</p>
<dt>$length = $term-&gt;ROW_l ($row_number[, $new_length])</p>
<dd>Returns the number of screen cells that are in use (&#8220;the line length&#8221;). Unlike the urxvt core, this returns <tt>&quot;$term-&gt;ncol&quot;</tt> if the line is joined with the following one.</p>
<dt>$bool = $term-&gt;is_longer ($row_number)</p>
<dd>Returns true if the row is part of a multiple-row logical &#8220;line&#8221; (i.e. joined with the following row), which means all characters are in use and it is continued on the next row (and possibly a continuation of the previous row(s)).</p>
<dt>$line = $term-&gt;line ($row_number)</p>
<dd>Create and return a new <tt>&quot;urxvt::line&quot;</tt> object that stores information about the logical line that row <tt>$row_number</tt> is part of. It supports the following methods:</p>
<dl>
<dd>
<dl>
<dt>$text = $line-&gt;t ([$new_text])</p>
<dd>Returns or replaces the full text of the line, similar to <tt>&quot;ROW_t&quot;</tt></p>
<dt>$rend = $line-&gt;r ([$new_rend])</p>
<dd>Returns or replaces the full rendition array of the line, similar to <tt>&quot;ROW_r&quot;</tt></p>
<dt>$length = $line-&gt;l</p>
<dd>Returns the length of the line in cells, similar to <tt>&quot;ROW_l&quot;</tt>.</p>
<dt>$rownum = $line-&gt;beg</p>
<dd>
<dt>$rownum = $line-&gt;end</p>
<dd>Return the row number of the first/last row of the line, respectively.</p>
<dt>$offset = $line-&gt;offset_of ($row, $col)</p>
<dd>Returns the character offset of the given row|col pair within the logical line. Works for rows outside the line, too, and returns corresponding offsets outside the string.</p>
<dt>($row, $col) = $line-&gt;coord_of ($offset)</p>
<dd>Translates a string offset into terminal coordinates again.</dl>
</dl>
<dl>
<dd></dl>
<dt>$text = $term-&gt;special_encode $string</p>
<dd>Converts a perl string into the special encoding used by rxvt-unicode, where one character corresponds to one screen cell. See <tt>&quot;$term-&gt;ROW_t&quot;</tt> for details.</p>
<dt>$string = $term-&gt;special_decode $text</p>
<dd>Converts rxvt-unicodes text representation into a perl string. See <tt>&quot;$term-&gt;ROW_t&quot;</tt> for details.</p>
<dt>$success = $term-&gt;grab_button ($button, $modifiermask[, $window = $term-&gt;vt])</p>
<dd>
<dt>$term-&gt;ungrab_button ($button, $modifiermask[, $window = $term-&gt;vt])</p>
<dd>Register/unregister a synchronous button grab. See the XGrabButton manpage.</p>
<dt>$success = $term-&gt;grab ($eventtime[, $sync])</p>
<dd>Calls XGrabPointer and XGrabKeyboard in asynchronous (default) or synchronous (<tt>$sync</tt> is true). Also remembers the grab timestamp.</p>
<dt>$term-&gt;allow_events_async</p>
<dd>Calls XAllowEvents with AsyncBoth for the most recent grab.</p>
<dt>$term-&gt;allow_events_sync</p>
<dd>Calls XAllowEvents with SyncBoth for the most recent grab.</p>
<dt>$term-&gt;allow_events_replay</p>
<dd>Calls XAllowEvents with both ReplayPointer and ReplayKeyboard for the most recent grab.</p>
<dt>$term-&gt;ungrab</p>
<dd>Calls XUngrabPointer and XUngrabKeyboard for the most recent grab. Is called automatically on evaluation errors, as it is better to lose the grab in the error case as the session.</p>
<dt>$atom = $term-&gt;XInternAtom ($atom_name[, $only_if_exists])</p>
<dd>
<dt>$atom_name = $term-&gt;XGetAtomName ($atom)</p>
<dd>
<dt>@atoms = $term-&gt;XListProperties ($window)</p>
<dd>
<dt>($type,$format,$octets) = $term-&gt;XGetWindowProperty ($window, $property)</p>
<dd>
<dt>$term-&gt;XChangeProperty ($window, $property, $type, $format, $octets)</p>
<dd>
<dt>$term-&gt;XDeleteProperty ($window, $property)</p>
<dd>
<dt>$window = $term-&gt;DefaultRootWindow</p>
<dd>
<dt>$term-&gt;XReparentWindow ($window, $parent, [$x, $y])</p>
<dd>
<dt>$term-&gt;XMapWindow ($window)</p>
<dd>
<dt>$term-&gt;XUnmapWindow ($window)</p>
<dd>
<dt>$term-&gt;XMoveResizeWindow ($window, $x, $y, $width, $height)</p>
<dd>
<dt>($x, $y, $child_window) = $term-&gt;XTranslateCoordinates ($src, $dst, $x, $y)</p>
<dd>
<dt>$term-&gt;XChangeInput ($window, $add_events[, $del_events])</p>
<dd>
<dt>$keysym = $term-&gt;XStringToKeysym ($string)</p>
<dd>
<dt>$string = $term-&gt;XKeysymToString ($keysym)</p>
<dd>Various X or X-related functions. The <tt>$term</tt> object only serves as the source of the display, otherwise those functions map more-or-less directly onto the X functions of the same name.</dl>
<h3>The urxvt::popup Class</h3>
<dl>
<dt>$popup-&gt;add_title ($title)</p>
<dd>Adds a non-clickable title to the popup.</p>
<dt>$popup-&gt;add_separator ([$sepchr])</p>
<dd>Creates a separator, optionally using the character given as <tt>$sepchr</tt>.</p>
<dt>$popup-&gt;add_button ($text, $cb)</p>
<dd>Adds a clickable button to the popup. <tt>$cb</tt> is called whenever it is selected.</p>
<dt>$popup-&gt;add_toggle ($text, $initial_value, $cb)</p>
<dd>Adds a toggle/checkbox item to the popup. The callback gets called whenever it gets toggled, with a boolean indicating its new value as its first argument.</p>
<dt>$popup-&gt;show</p>
<dd>Displays the popup (which is initially hidden).</dl>
<h3>The urxvt::timer Class</h3>
<p>This class implements timer watchers/events. Time is represented as a fractional number of seconds since the epoch. Example: </p>
<pre> $term-&gt;{overlay} = $term-&gt;overlay (-1, 0, 8, 1, urxvt::OVERLAY_RSTYLE, 0);
 $term-&gt;{timer} = urxvt::timer
 -&gt;new
 -&gt;interval (1)
 -&gt;cb (sub {
 $term-&gt;{overlay}-&gt;set (0, 0,
 sprintf &quot;%2d:%02d:%02d&quot;, (localtime urxvt::NOW)[2,1,0]);
 });</pre>
<dl>
<dt>$timer = new urxvt::timer</p>
<dd>Create a new timer object in started state. It is scheduled to fire immediately.</p>
<dt>$timer = $timer-&gt;cb (sub { my ($timer) = @_; &#8230; })</p>
<dd>Set the callback to be called when the timer triggers.</p>
<dt>$timer = $timer-&gt;set ($tstamp[, $interval])</p>
<dd>Set the time the event is generated to <tt>$tstamp</tt> (and optionally specifies a new <tt>$interval</tt>).</p>
<dt>$timer = $timer-&gt;interval ($interval)</p>
<dd>By default (and when <tt>$interval</tt> is <tt>0</tt>), the timer will automatically stop after it has fired once. If <tt>$interval</tt> is non-zero, then the timer is automatically rescheduled at the given intervals.</p>
<dt>$timer = $timer-&gt;start</p>
<dd>Start the timer.</p>
<dt>$timer = $timer-&gt;start ($tstamp[, $interval])</p>
<dd>Set the event trigger time to <tt>$tstamp</tt> and start the timer. Optionally also replaces the interval.</p>
<dt>$timer = $timer-&gt;after ($delay[, $interval])</p>
<dd>Like <tt>&quot;start&quot;</tt>, but sets the expiry timer to c&lt;urxvt::NOW + <tt>$delay</tt>&gt;.</p>
<dt>$timer = $timer-&gt;stop</p>
<dd>Stop the timer.</dl>
<h3>The urxvt::iow Class</h3>
<p>This class implements io watchers/events. Example: </p>
<pre> $term-&gt;{socket} = ...
 $term-&gt;{iow} = urxvt::iow
 -&gt;new
 -&gt;fd (fileno $term-&gt;{socket})
 -&gt;events (urxvt::EV_READ)
 -&gt;start
 -&gt;cb (sub {
 my ($iow, $revents) = @_;
 # $revents must be 1 here, no need to check
 sysread $term-&gt;{socket}, my $buf, 8192
 or end-of-file;
 });</pre>
<dl>
<dt>$iow = new urxvt::iow</p>
<dd>Create a new io watcher object in stopped state.</p>
<dt>$iow = $iow-&gt;cb (sub { my ($iow, $reventmask) = @_; &#8230; })</p>
<dd>Set the callback to be called when io events are triggered. <tt>$reventmask</tt> is a bitset as described in the <tt>&quot;events&quot;</tt> method.</p>
<dt>$iow = $iow-&gt;fd ($fd)</p>
<dd>Set the file descriptor (not handle) to watch.</p>
<dt>$iow = $iow-&gt;events ($eventmask)</p>
<dd>Set the event mask to watch. The only allowed values are <tt>&quot;urxvt::EV_READ&quot;</tt> and <tt>&quot;urxvt::EV_WRITE&quot;</tt>, which might be ORed together, or <tt>&quot;urxvt::EV_NONE&quot;</tt>.</p>
<dt>$iow = $iow-&gt;start</p>
<dd>Start watching for requested events on the given handle.</p>
<dt>$iow = $iow-&gt;stop</p>
<dd>Stop watching for events on the given file handle.</dl>
<h3>The urxvt::iw Class</h3>
<p>This class implements idle watchers, that get called automatically when the process is idle. They should return as fast as possible, after doing some useful work.</p>
<dl>
<dt>$iw = new urxvt::iw</p>
<dd>Create a new idle watcher object in stopped state.</p>
<dt>$iw = $iw-&gt;cb (sub { my ($iw) = @_; &#8230; })</p>
<dd>Set the callback to be called when the watcher triggers.</p>
<dt>$timer = $timer-&gt;start</p>
<dd>Start the watcher.</p>
<dt>$timer = $timer-&gt;stop</p>
<dd>Stop the watcher.</dl>
<h3>The urxvt::pw Class</h3>
<p>This class implements process watchers. They create an event whenever a process exits, after which they stop automatically. </p>
<pre> my $pid = fork;
 ...
 $term-&gt;{pw} = urxvt::pw
 -&gt;new
 -&gt;start ($pid)
 -&gt;cb (sub {
 my ($pw, $exit_status) = @_;
 ...
 });</pre>
<dl>
<dt>$pw = new urxvt::pw</p>
<dd>Create a new process watcher in stopped state.</p>
<dt>$pw = $pw-&gt;cb (sub { my ($pw, $exit_status) = @_; &#8230; })</p>
<dd>Set the callback to be called when the timer triggers.</p>
<dt>$pw = $timer-&gt;start ($pid)</p>
<dd>Tells the watcher to start watching for process <tt>$pid</tt>.</p>
<dt>$pw = $pw-&gt;stop</p>
<dd>Stop the watcher.</dl>
<h2>Environment</h2>
<h3><font SIZE="-1">URXVT_PERL_VERBOSITY</font></h3>
<p>This variable controls the verbosity level of the perl extension. Higher numbers indicate more verbose output.</p>
<dl>
<dt>== 0 &#8211; fatal messages</p>
<dd>
<dt>&gt;= 3 &#8211; script loading and management</p>
<dd>
<dt>&gt;=10 &#8211; all called hooks</p>
<dd>
<dt>&gt;=11 &#8211; hook return values</p>
<dd></dl>
<h2>Author</h2>
<pre> Marc Lehmann &lt;schmorp [at] schmorp.de&gt;
 <a rel="nofollow" href="http://software.schmorp.de/pkg/rxvt-unicode">http://software.schmorp.de/pkg/rxvt-unicode</a></pre>
