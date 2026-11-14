---
title: "urxvt256c-ml-matcher(1)"
name: "urxvt256c-ml-matcher"
section: "1"
letter: "u"
url: "/docs/linux/man/1-urxvt256c-ml-matcher/"
---

<h2 class="name">NAME</h2>
 

 matcher - match strings in terminal output and change their rendition 

<h2>DESCRIPTION</h2>

 Uses per-line display filtering (<tt>&quot;on_line_update&quot;</tt>) to underline text matching a certain pattern and make it clickable. When clicked with the mouse button specified in the <tt>&quot;matcher.button&quot;</tt> resource (default 2, or middle), the program specified in the <tt>&quot;matcher.launcher&quot;</tt> resource (default, the <tt>&quot;url-launcher&quot;</tt> resource, <tt>&quot;sensible-browser&quot;</tt>) will be started with the matched text as first argument. The default configuration is suitable for matching URLs and launching a web browser, like the former ``mark-urls'' extension. 

 The default pattern to match URLs can be overridden with the <tt>&quot;matcher.pattern.0&quot;</tt> resource, and additional patterns can be specified with numbered patterns, in a manner similar to the ``selection'' extension. The launcher can also be overridden on a per-pattern basis. 

 It is possible to activate the most recently seen match or a list of matches from the keyboard. Simply bind a keysym to ``matcher:last'' or ``matcher:list'' as seen in the example below. 

 The 'matcher:select' action enables a mode in which it is possible to iterate over the matches using the keyboard and either activate them or copy them to the clipboard. While the mode is active, normal terminal input/output is suspended and the following bindings are recognized:
<dl>
<dt>&quot;Up&quot;
<dd> Search for a match upwards.
<dt>&quot;Down&quot;
<dd> Search for a match downwards.
<dt>&quot;Home&quot;
<dd> Jump to the topmost match.
<dt>&quot;End&quot;
<dd> Jump to the bottommost match.
<dt>&quot;Escape&quot;
<dd> Leave the mode and return to the point where search was started.
<dt>&quot;Enter&quot;
<dd> Activate the current match.
<dt>&quot;y&quot;
<dd> Copy the current match to the clipboard.</dl>
 

 Example: load and use the matcher extension with defaults. 

 <pre>
    URxvt.perl-ext:           default,matcher
</pre> 

 Example: use a custom configuration. 

 <pre><code>
    URxvt.url-launcher:       sensible-browser
    URxvt.keysym.C-Delete:    matcher:last
    URxvt.keysym.M-Delete:    matcher:list
    URxvt.matcher.button:     1
    URxvt.matcher.pattern.1:  \\bwww\\.[\\w-]+\\.[\\w./?&amp;@#-]*[\\w/-]
    URxvt.matcher.pattern.2:  \\B(/\\S+?):(\\d+)(?=:|$)
    URxvt.matcher.launcher.2: gvim +$2 $1
</code></pre> 

<h2>Index</h2>


