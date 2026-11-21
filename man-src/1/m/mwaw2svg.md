---

title: "mwaw2svg(1)"
name: "mwaw2svg"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mwaw2svg/"
description: "mwaw2svg – convert Mac drawing into SVG"
---

<h2>NAME</h2>
<p> mwaw2svg &#8211; convert Mac drawing into SVG</p>
<p> <code>mwaw2svg</code> [<i>-h</i>] [<i>-v</i>] [<i>-t</i>] [<i>-b body | -o file.svg</i>] <i>&lt;Mac Graphic/Presentation Document&gt;</i></p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code></dt>
<dd> Shows this help message.</dd>
<dt><code>-b</code> body</dt>
<dd> Defines the file&#8217;s body name, the different drawings/slides will be stored in body0.svg, body1.svg, &#8230;</dd>
<dt><code>-o</code> file.svg</dt>
<dd> Stores the first drawing/slide in file.svg. Further drawing/slide are not saved.</dd>
<dt><code>-t</code></dt>
<dd> If set, all drawings/slides are send to file.svg or stdout. This option is only intended for debug/regression test.</dd>
<dt><code>-v</code>:</dt>
<dd> Outputs mwaw2svg version.</dd></dl>
<h3>Note:</h3>
<dl>
<dt>
</dt><dd> the content of the first drawing/slide is sent to stdout if neither <code>-b</code> nor <code>-o</code> options are given. </dd>
</dl>
