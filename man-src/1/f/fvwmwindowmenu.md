---
title: "fvwmwindowmenu(1)"
name: "fvwmwindowmenu"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fvwmwindowmenu/"
description: "FvwmWindowMenu – open configurable fvwm menu listing current windows"
---

<p>FvwmWindowMenu &#8211; open configurable fvwm menu listing current windows </p>
<h2>Synopsis</h2>
<p>FvwmWindowMenu should be spawned by <i><a href="/docs/linux/man/1-fvwm/">fvwm</a></i>(1) for normal functionality. </p>
<p> Run this module from your StartFunction: </p>
<pre> AddToFunc StartFunction
 + I Module FvwmWindowMenu</pre>
<h2>Description</h2>
<p>A substitute for <i>fvwm</i> builtin <code>WindowList</code>, but written in Perl and easy to customize. Unlike <code>FvwmIconMan</code> or <code>FvwmWinList</code> the module does not draw its own window, but instead creates an <i>fvwm</i> menu and asks <i>fvwm</i> to pop it up. </p>
<p> By defining a set of regular expressions, windows may be sorted into sections based on a regexp matching the window name, class or resource and included in the menu. </p>
<p> Similarly, another set of regular expressions can be used to exclude items from the menu. </p>
<p> Any windows not matching an instance of the include or exclude list will be placed in the last section of the menu.</p>
<h2>Usage</h2>
<p>Run the module, supposedly from StartFunction in <i>.fvwm2rc</i>: </p>
<pre> Module FvwmWindowMenu</pre>
<p>To actually invoke the menu add something like: </p>
<pre> Key Menu A N SendToModule FvwmWindowMenu \
 Post Root c c SelectOnRelease Menu</pre>
<p>or: </p>
<pre> Mouse 2 A N SendToModule FvwmWindowMenu Popup</pre>
<p>The additional parameters are any valid <code>Menu</code> command parameters without a menu name, see fvwm. </p>
<p> Recognized actions are <code>Post</code> (or its alias <code>Menu</code>) and <code>Popup</code>, they create <i>fvwm</i> menus and invoke them using the corresponding commands <code>Menu</code> and <code>Popup</code>. If the module was started with &#8220;-g&#8221; switch, it additionally supports <code>PostBar</code> (not implemented yet). </p>
<p> Set module options for windows to include (Show) or exclude (DontShow). The syntax is: </p>
<pre> *FvwmWindowMenu: ShowName pattern
 *FvwmWindowMenu: ShowClass pattern
 *FvwmWindowMenu: ShowResource pattern
 *FvwmWindowMenu: DontShowName pattern
 *FvwmWindowMenu: DontShowClass pattern
 *FvwmWindowMenu: DontShowResource pattern</pre>
<p>Pattern is a perl regular expression that will be evaluated in m// context. See <i><a href="/docs/linux/man/1-perlre/">perlre</a></i>(1). </p>
<p> For example: </p>
<pre> *FvwmWindowMenu: ShowResource ^gvim
 *FvwmWindowMenu: ShowName Galeon|Navigator|mozilla-bin|Firefox</pre>
<p>will define two sections containing respectively browsers, and GVim. A third section will contain all other windows. </p>
<p> To only include matching windows, add: </p>
<pre> *FvwmWindowMenu: DontShowName .*</pre>
<p>Similarly: </p>
<pre> *FvwmWindowMenu: DontShowName ^Fvwm
 *FvwmWindowMenu: DontShowClass Gkrellm</pre>
<p>will cause the menu to ignore windows with name beginning with Fvwm or class gkrellm. </p>
<p> Other options:</p>
<dl>
<dt>*FvwmWindowMenu: <i>OnlyIconified</i> {on|off}</p>
<dd>show only iconified windows</p>
<dt>*FvwmWindowMenu: <i>AllDesks</i> {on|off}</p>
<dd>show windows from all desks</p>
<dt>*FvwmWindowMenu: <i>AllPages</i> {on|off}</p>
<dd>show windows from all pages</p>
<dt>*FvwmWindowMenu: <i>MaxLen</i> 32</p>
<dd>max length in chars of entry</p>
<dt>*FvwmWindowMenu: <i>MenuName</i> MyMenu</p>
<dd>name of menu to popup</p>
<dt>*FvwmWindowMenu: <i>MenuStyle</i> MyMenuStyle</p>
<dd>name of MenuStyle to apply</p>
<dt>*FvwmWindowMenu: <i>Debug</i> {0,1,2,3}</p>
<dd>level of debug info output, 0 means no debug</p>
<dt>*FvwmWindowMenu: <i>Function</i> MyWindowListFunc</p>
<dd>function to invoke on menu entries; defaults to WindowListFunc</p>
<dt>*FvwmWindowMenu: <i>ItemFormat</i> formatstring</p>
<dd>how to format menu entries; substitutions are made as follows:</p>
<dl>
<dd>
<dl>
<dt>%n, <tt>%i</tt>, <tt>%c</tt>, <tt>%r</p>
<dd>the window name, icon name, class or resource</p>
<dt>%x</tt>, <tt>%y</p>
<dd>the window x or y coordinates w.r.t. the page the window is on.</p>
<dt>%X</tt>, <tt>%Y</p>
<dd>the window x or y coordinates w.r.t. the desk the window is on.</p>
<dt>%d</p>
<dd>the window desk number</p>
<dt>%m</p>
<dd>the window's mini-icon</p>
<dt>%M</p>
<dd>the window's mini-icon only for iconified windows, otherwise empty</p>
<dt>%t</p>
<dd>a tab</p>
<dt>%%</p>
<dd>a literal %</dl>
</dl>
<dl>
<dd>The format string must be quoted. The default string is ``%m%n%t%t(+%x+%y) - Desk %d</tt>&#8221;.</dl>
</dl>
<h2>More Examples</h2>
<p>Fancy binding of the window menu to the right windows key on some keyboards. Hold this button while navigating using cursor keys, then release it. </p>
<pre> CopyMenuStyle * WindowMenu
 MenuStyle WindowMenu SelectOnRelease Super_R
 *FvwmWindowMenu: MenuStyle WindowMenu
 AddToFunc StartFunction I Module FvwmWindowMenu
 Key Super_R A A SendToModule FvwmWindowMenu Post Root c c WarpTitle</pre>
<h2>Authors</h2>
<p>Richard Lister &lt;ric+lister [at] cns.georgetown.edu&gt;. </p>
<p> Scott Smedley &lt;ss [at] aao.gov.au&gt;. </p>
<p> Mikhael Goikhman &lt;migo [at] homemail.com&gt;.</p>
