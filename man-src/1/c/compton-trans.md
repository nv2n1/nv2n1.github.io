---

title: "compton-trans(1)"
name: "compton-trans"
section: "1"
letter: "c"
url: "/docs/linux/man/1-compton-trans/"
description: "compton-trans – an opacity setter tool"
---

<p> <code>compton-trans</code> [-w <i>WINDOW_ID</i>] [-n <i>WINDOW_NAME</i>] [-c] [-s] <i>OPACITY</i></p>
<p> <code>compton-trans</code> is a bash script that sets <i>_NET_WM_WINDOW_OPACITY</i> attribute of a window using standard X11 command-line utilities, including <code><a href="/docs/linux/man/1-xprop/">xprop</a></code>(1) and <code><a href="/docs/linux/man/1-xwininfo/">xwininfo</a></code>(1). It is similar to <code><a href="/docs/linux/man/1-transset/">transset</a></code>(1) or <code>transset-df</code>(1).</p>
<h2>OPTIONS</h2>
<p> <code>-w</code> <i>WINDOW_ID</i></p>
<dl>
<dt>
</dt><dd> Specify the window id of the target window.</dd></dl>
<p> <code>-n</code> <i>WINDOW_NAME</i></p>
<dl>
<dt>
</dt><dd> Specify and try to match a window name.</dd></dl>
<p> <code>-c</code></p>
<dl>
<dt>
</dt><dd> Specify the currently active window as target. Only works if EWMH <i>_NET_ACTIVE_WINDOW</i> property exists on root window.</dd></dl>
<p> <code>-s</code></p>
<dl>
<dt>
</dt><dd> Select target window with mouse cursor. This is the default if no window has been specified.</dd></dl>
<p> <code>-o</code> <i>OPACITY</i></p>
<dl>
<dt>
</dt><dd> Specify the new opacity value for the window. This value can be anywhere from 1-100. If it is prefixed with a plus or minus (+/-), this will increment or decrement from the target window&#8217;s current opacity instead.</dd></dl>
<h2>EXAMPLES</h2>
<dl>
<dt>
</dt><dd> &bull; Set the opacity of the window with specific window ID to 75%: </dd>
<dl>
<dt>
</dt><dd>
<pre>
compton-trans -w &quot;$WINDOWID&quot; 75
</pre>
</dd></dl>
</dl>
<dl>
<dt>
</dt><dd> &bull; Set the opacity of the window with the name &quot;urxvt&quot; to 75%: </dd>
<dl>
<dt>
</dt><dd>
<pre>
compton-trans -n &quot;urxvt&quot; 75
</pre>
</dd></dl>
</dl>
<dl>
<dt>
</dt><dd> &bull; Set current window to opacity of 75%: </dd>
<dl>
<dt>
</dt><dd>
<pre>
compton-trans -c 75
</pre>
</dd></dl>
</dl>
<dl>
<dt>
</dt><dd> &bull; Select target window and set opacity to 75%: </dd>
<dl>
<dt>
</dt><dd>
<pre>
compton-trans -s 75
</pre>
</dd></dl>
</dl>
<dl>
<dt>
</dt><dd> &bull; Increment opacity of current active window by 5%: </dd>
<dl>
<dt>
</dt><dd>
<pre>
compton-trans -c +5
</pre>
</dd></dl>
</dl>
<dl>
<dt>
</dt><dd> &bull; Decrement opacity of current active window by 5%: </dd>
<dl>
<dt>
</dt><dd>
<pre>
compton-trans -c -- -5
</pre>
</dd></dl>
</dl>
<h2>BUGS</h2>
<p> Please report any bugs you find to <a rel="nofollow" href="https://github.com/chjj/compton">https://github.com/chjj/compton</a> .</p>
<h2>AUTHORS</h2>
<p> Christopher Jeffrey (<a rel="nofollow" href="https://github.com/chjj">https://github.com/chjj</a>).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-compton/">compton</a></code>(1), <code><a href="/docs/linux/man/1-xprop/">xprop</a></code>(1), <code><a href="/docs/linux/man/1-xwininfo/">xwininfo</a></code>(1) </p>
