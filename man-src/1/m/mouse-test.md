---
title: "mouse-test(1)"
name: "mouse-test"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mouse-test/"
description: "mouse-test – a tool for determining mouse type and device it’s attached to."
---

<h2>NAME</h2>
<p> mouse-test &#8211; a tool for determining mouse type and device it&#8217;s attached to.</p>
<h2>SYNTAX</h2>
<p> <code>mouse-test</code> [ <i>device</i> &#8230; ]</p>
<h2>DESCRIPTION</h2>
<p> This experimental and incomplete application tries to help in detecting which protocol does your mouse speak. It is able to detect MouseMan devices, and to choose between -t ms (three-buttons aware) and -t bare old two-buttons-only serial mice. </p>
<h2>BUGS</h2>
<p> I know the application is buggy, but I only own one mouse device. If you are interested in this application, just call me and awake me from my laziness. </p>
<h3>OPTIONS</h3>
<dl>
<dt><i>device</i></p>
<dd> [ <i>device</i> &#8230; ]</dl>
<p> Check this <i>device</i> for a mouse. If no devices are listed, mouse-test will try all possible devices. </p>
<h2>AUTHOR</h2>
<p> Alessandro Rubini &lt;rubini [at] linux.it&gt; </p>
<h2>FILES</h2>
<pre>
/dev/*              The devices used to search for a mouse
</pre>
<h2>SEE ALSO</h2>
<pre>
<a href="//www.systutorials.com/docs/linux/man/8-gpm/">gpm</a>(8)
</pre>
<h2>Index</h2>
