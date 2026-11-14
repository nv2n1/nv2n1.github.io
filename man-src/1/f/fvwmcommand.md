---
title: "fvwmcommand(1)"
name: "fvwmcommand"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fvwmcommand/"
---

FvwmCommand - fvwm command external interface
<h2>Synopsis</h2>FvwmCommand [-cmrvw] [-S name] [-i level] [-f name] [-F level] [command...] 

<h2>Description</h2>FvwmCommand lets you monitor fvwm transaction and issue fvwm command from a shell command line or scripts. FvwmCommand takes each argument as a fvwm command. Quotes can be used to send commands including spaces. 

 <pre>FvwmCommand 'FvwmPager 0 1'</pre><h2>Invocation</h2>FvwmCommandS should be spawned once by fvwm, either in .fvwm2rc file, from menu, or from FvwmConsole. From then on, FvwmCommand can be called from a shell or script to execute fvwm commands. 

 From within .fvwm2rc file: 

 <pre>Module FvwmCommandS
 or
AddToFunc StartFunction &quot;I&quot; Module FvwmCommandS</pre>Then, in script file or from shell: 

 

 <pre>FvwmCommand 'popup Utilities'</pre><h2>Options</h2><dl><dt><i>-c</i>
<dd>Informs FvwmCommand to read multiple commands from the standard input instead of the one command specified in the command line arguments. This disables <i>-m</i> or <i>-i</i>. 

 

 <pre>(echo &quot;Exec xload&quot;; echo &quot;Beep&quot;) | FvwmCommand -c</pre><dt><i>-F &lt;level&gt;</i>
<dd>Specifies the level of fvwm window flags FvwmCommand outputs. 

<dl><dd><dl><dt>0
<dd>No window flags will be printed.</dl></dl><dl><dd><dl><dt>2
<dd>Full window flags will be printed if information level, -i option, is 2 or 3. 

</dl></dl><dt><i>-f &lt;name&gt;</i>
<dd>Specifies an alternative FIFO set to communicate with a server. The default FIFO set is /var/tmp/FvwmCommand-${DISPLAY}C, in which FvwmCommand..C is used to send commands and FvwmCommand..M is to receive messages. If that path is unusable ${FVWM_USERDIR}/FvwmCommand-${DISPLAY} will be used instead. FvwmCommandS must have been invoked with the same &lt;name&gt; as its first argument prior to FvwmCommand invocation. Alternatively, option -S can be used. Refer option -S. This option -f is useful when a dedicated connection is necessary to run a background job while another connection is kept for interactive use. 

<dt><i>-i &lt;level&gt;</i>
<dd>Specifies the level of information that FvwmCommand outputs. 

<dl><dd><dl><dt>0
<dd>Error messages only. 

 <pre>FvwmCommand -i0 FvwmBanner</pre>will show a banner without any output. On the other hand, 

 <pre>FvwmCommand -i 0 foobar</pre>will return, 

 <pre>[fvwm][executeModule]: &lt;&lt;ERROR&gt;&gt; No such module
'foobar' in ModulePath '/usr/lib/X11/fvwm'</pre>Note that Fvwm doesn't return any error messages in cases like below since 'windowid' itself is a valid command. 

 

 <pre>FvwmCommand -i 0 'windowid foo bar'</pre><dt>1
<dd>Errors, replies and window configuration information. This is the default. 

 <pre>FvwmCommand send_windowlist</pre>Information like below will show up. 

 <pre>0x02000014 window FvwmConsole
0x02000014 icon FvwmConsole
0x02000014 class XTerm
0x02000014 resource FvwmConsole
0x01c00014 window console
0x01c00014 icon console
0x01c00014 class XTerm
0x01c00014 resource console
0x01000003 window Fvwm Pager
0x01000003 icon
0x01000003 class FvwmModule
0x01000003 resource FvwmPager
0x00c0002c window emacs: FvwmCommand.man
0x00c0002c icon FvwmCommand.man
0x00c0002c icon file xemacs.xpm
0x00c0002c class Emacs
0x00c0002c resource emacs
end windowlist</pre>The first column shows the window ID number, which can be used in 'windowid' command. The second column shows the information types. The last column shows the information contents. If no information is returned, add -w &lt;time&gt; or -r option. This might be needed in heavily loaded systems.
<dt>2
<dd>Above and static window information. 

 <pre>FvwmCommand -i2 'FvwmPager 0 1'</pre>The below is its output. 

 <pre>0x03c00003 frame x 962, y 743, width 187, height 114
0x03c00003 desktop 0
0x03c00003 StartIconic no
0x03c00003 OnTop yes
0x03c00003 Sticky yes
0x03c00003 WindowListSkip yes
0x03c00003 SuppressIcon no
0x03c00003 NoiconTitle no
0x03c00003 Lenience no
0x03c00003 StickyIcon no
0x03c00003 CirculateSkipIcon no
0x03c00003 CirculateSkip no
0x03c00003 ClickToFocus no
0x03c00003 SloppyFocus no
0x03c00003 SkipMapping no
0x03c00003 Handles no
0x03c00003 Title no
0x03c00003 Mapped no
0x03c00003 Iconified no
0x03c00003 Transient no
0x03c00003 Raised no
0x03c00003 Visible no
0x03c00003 IconOurs no
0x03c00003 PixmapOurs no
0x03c00003 ShapedIcon no
0x03c00003 Maximized no
0x03c00003 WmTakeFocus no
0x03c00003 WmDeleteWindow yes
0x03c00003 IconMoved no
0x03c00003 IconUnmapped no
0x03c00003 MapPending no
0x03c00003 HintOverride yes
0x03c00003 MWMButtons no
0x03c00003 MWMBorders no
0x03c00003 title height 0
0x03c00003 border width 4
0x03c00003 base size width 8, height 7
0x03c00003 size increment width 9, height 9
0x03c00003 min size width 8, height 7
0x03c00003 max size width 32767, height 32767
0x03c00003 gravity SouthEast
0x03c00003 pixel text 0xffffff, back 0x7f7f7f
0x03c00003 window Fvwm Pager
0x03c00003 icon Fvwm Pager
0x03c00003 class FvwmModule
0x03c00003 resource FvwmPager</pre><dt>3
<dd>All information available. 

 <pre>FvwmCommand -i3 'Killmodule Fvwm*'</pre>This will report which windows are closed. 

 <pre>0x03400003 destroy
0x02400002 destroy</pre></dl></dl><dt><i>-m</i>
<dd>Monitors fvwm window information transaction. FvwmCommand continuously outputs information that it receives without exiting. This option can be used in a background job often combined with -i3 option in order to control windows dynamically. 

 <pre>FvwmCommand -mi3 | grep 'iconify'</pre>It will report when windows are iconified or de-iconified. 

 Note: FvwmCommand does not block buffer its output but many utilities such as grep or sed use block buffer. The output of the next example will not show up until either FvwmCommand is terminated or stdout buffer from grep is filled. 

 <pre>FvwmCommand -mi3 | grep ' map' |
sed 's/\(0x[0-9a-f]*\).*/windowid \1 move 0 0/'</pre>Instead, use tools with buffer control such as pty or perl. The below will iconify new windows when opened. 

 <pre>Fvwm -mi3 | perl -ne '
$|=1;
print &quot;windowid $1 iconify\n&quot; if /^(0x\S+) add/;
' &gt; ~/.FvwmCommandC</pre><dt><i>-r</i>
<dd>Waits for a reply before it exits. FvwmCommand exits if no information or error is returned in a fixed amount of time period. (Refer option -w.) The option -r overrides this time limit and wait for at least one message back. After the initial message, it will wait for another message for the time limit. This option is useful when the system is too loaded to make any prediction when the system is responding AND the command causes some message to be sent back. 

<dt><i>-S &lt;name&gt;</i>
<dd>Invokes another server, FvwmCommandS, with FIFO set &lt;name&gt;. 
 If -f option is not used with this option, the invoking FvwmCommand uses the default FIFO to communicate the default server to invoke a new server. 
 If -f option is used with this option, the invoking FvwmCommand uses the default FIFO to communicate the default server to invoke a new server. Then, switch the FIFO set and start communicating the new server. 
 This option -S is useful when a dedicated connection is necessary to run a background job while another connection is kept for interactive use. 

 If the &lt;name&gt; is a relative path name, that is relative from where fvwm is running, not from where FvwmCommand is invoked. 

<dt><i>-v</i>
<dd>Returns FvwmCommand version number and exits. 

<dt><i>-w &lt;time&gt;</i>
<dd>Waits for &lt;time&gt; micro seconds for a message. FvwmCommand exits if no information or error is returned in a fixed amount of time period unless option -m is used. The default is 500 ms. This option overrides this default value. 

</dl><h2>Wrapper</h2>FvwmCommand.sh has bourne shell function definitions to keep the syntax similar to fvwm configuration file. This file is to be sourced: 

 <pre>. FvwmCommand.sh
<br>
DesktopSize 5x5</pre>FvwmCommand.pm is for perl in order to keep the syntax similar to fvwm configuration file. Commas can be used to separate fvwm commands' arguments. 

 <pre>use FvwmCommand;
if( $ARGV[0] eq 'home' ) {
 Desk 0,0; GotoPage '1 1';
}elsif( $ARGV[0] eq 'jump' ) {
 Desk &quot;0 2&quot;; GotoPage 0, 1;
}</pre>Although arguments in FvwmCommand are not case sensitive as fvwm, the functions defined in FvwmCommand.sh and FvwmCommand.pl are case sensitive. 

 

<h2>Errors</h2>If the following error message show up, it is most likely that FvwmCommandS is not running. 

 <pre>FvwmCommand error in opening message fifo
--No such file or directory--</pre>Fvwm modules don't return error messages to fvwm but output on stderr. These error messages will not be shown as FvwmCommand messages. 

 FvwmCommand is an interface to send commands to and receive information from Fvwm2 from processes which are not Fvwm modules. 

 

<h2>Examples</h2>&nbsp;<wbr>&nbsp;<wbr>test1.pl&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>- takes 1 argument&nbsp;<wbr>&nbsp;<wbr>'t'&nbsp;<wbr>to invoke FvwmTalk 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>'td'&nbsp;<wbr>&nbsp;<wbr>to kill FvwmTalk 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>''&nbsp;<wbr>&nbsp;<wbr>to move windows 
&nbsp;<wbr>&nbsp;<wbr>test2.sh&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>- takes 1 argument&nbsp;<wbr>&nbsp;<wbr>'b'&nbsp;<wbr>&nbsp;<wbr>to invoke FvwmButtons 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>'kb'&nbsp;<wbr>to kill FvwmButtons 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>'r'&nbsp;<wbr>&nbsp;<wbr>to change&nbsp;<wbr>#&nbsp;<wbr>of button rows 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>'c'&nbsp;<wbr>&nbsp;<wbr>to change&nbsp;<wbr>#&nbsp;<wbr>of button columns 
&nbsp;<wbr>&nbsp;<wbr>ex-auto.pl&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>- auto raise small windows. It will keep them visible. 
&nbsp;<wbr>&nbsp;<wbr>ex-cascade.pl - cascade windows, then move them back. 
&nbsp;<wbr>&nbsp;<wbr>ex-grpmv.pl&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>- choose a group of windows to move together. 

 
&nbsp;<wbr>&nbsp;<wbr>Above examples are not meant to be practical but to show how it can 
&nbsp;<wbr>&nbsp;<wbr>be done. 

 

 

 
&nbsp;<wbr>&nbsp;<wbr>focus-link.pl 
&nbsp;<wbr>&nbsp;<wbr>This is a user programmable window focus script. 
&nbsp;<wbr>&nbsp;<wbr>Default behavior is: 
1. When a window is opened up, focus the window and move the pointer 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>to it. The parent window regains focus when a window is closed. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Parenthood is determined when a window is opened. It is the last 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>focused window with the same X class. 
2.&nbsp;<wbr>#1 would not occur to AcroRead opening window. 
3.&nbsp;<wbr>#1 would not occur when SkipMapping is set and the window is the 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>only window of its class. 
4. For Netscape find dialog window, addition to&nbsp;<wbr>#1, resize the window 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>to 300x150 pixels and move it to East edge of the screen. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Download/upload windows will not be focused nor be in focus link 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>list. 
5. Move appletviewer to NorthWest corner. 
6. Xterm won't focus back to its parent after closed. 
7. When a window is de-iconified, focus it and move the pointer. 

 
&nbsp;<wbr>&nbsp;<wbr>focus-Netscape.pl 
Focuses pop-up windows, such as&nbsp;<wbr>'open URL'&nbsp;<wbr>or&nbsp;<wbr>'find'&nbsp;<wbr>whenever 
opened up. This let the user to type in immediately without 
moving mouse. This script also moves&nbsp;<wbr>'download'&nbsp;<wbr>window to the 
right edge to keep it visible. If this is invoked from 
.fvwm2rc, use as: 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>AddToFunc&nbsp;<wbr>&quot;StartFunction&quot;&nbsp;<wbr>&quot;I&quot;&nbsp;<wbr>Module&nbsp;<wbr>&nbsp;<wbr>FvwmCommandS 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>+&nbsp;<wbr>&quot;I&quot;&nbsp;<wbr>Exec&nbsp;<wbr>$HOME/scripts/focus-Netscape.pl 

 
&nbsp;<wbr>&nbsp;<wbr>push-away.pl&nbsp;<wbr>&lt;direction&gt;&nbsp;<wbr>&lt;window name&gt; 
Pushes windows away to avoid overlapping. use as: 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>push-away.pl up&nbsp;<wbr>'Fvwm Pager' 

 

 

 

 

 

<h2>See Also</h2>fvwm 

<h2>Author</h2>FvwmCommand is the original work of Toshi Isogai.
